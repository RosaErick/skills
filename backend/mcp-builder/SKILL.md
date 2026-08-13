---
name: mcp-builder
description: "Building MCP servers: tools vs resources vs prompts, schemas an agent can use, structured output, stdio vs streamable HTTP, OAuth, token-efficient responses. Use when writing or reviewing an MCP server or its tools."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
metadata:
  tags: mcp, tools, agents, typescript, python, oauth, transport
---

# MCP Builder

An MCP server exposes capability to an agent. The hard part is not the protocol — the SDKs handle
that — it's deciding **what to expose and how to describe it** so a model uses it correctly under
context pressure. Design the surface for a reader with no memory of your codebase and a limited
budget of tokens.

## 1. Pick the right primitive

| Primitive | Controlled by | Use for |
|---|---|---|
| **Tool** | The model | Actions and queries the model decides to run: search, create, update |
| **Resource** | The application | Context the client attaches deliberately: a file, a record, a schema |
| **Prompt** | The user | Reusable flows the user invokes explicitly: "/review-pr", "/summarize-incident" |

The common mistake is making everything a tool. A file the user picks is a resource; a workflow the
user starts is a prompt. Tools are for what the model chooses.

Client-side features worth knowing, because they change your design: **sampling** (the server asks
the client's model for a completion), **roots** (the client tells the server which directories are in
scope), **elicitation** (the server asks the user a structured question mid-call instead of failing).

## 2. Tool design

This is where servers succeed or fail.

**Few, high-value tools beat many thin ones.** Wrapping every endpoint one-to-one produces 40 tools
that flood the context and confuse selection. Consolidate around the task: one
`search_orders(status?, customer?, since?)` beats `list_orders` + `filter_by_status` +
`filter_by_customer`. If two tools are almost always called in sequence, make them one.

**Name for discovery.** `orders_search`, `orders_create` — a consistent prefix per domain groups the
surface and avoids collisions with other servers in the same session.

**The description is a prompt.** Say what it does, when to use it, when *not* to, and what it returns.
Spell out the non-obvious constraints — units, formats, limits, side effects.

```ts
server.registerTool(
  "orders_search",
  {
    title: "Search orders",
    description:
      "Searches orders by status, customer or date range. Returns at most 50 orders, newest first, " +
      "with a nextCursor when more exist. Use for finding orders; use orders_get for the full detail " +
      "of one known order id. Dates are ISO-8601 UTC.",
    inputSchema: {
      status: z.enum(["pending", "paid", "shipped", "cancelled"]).optional()
        .describe("Filter by lifecycle status"),
      customerId: z.string().optional().describe("Exact customer id, e.g. cus_01H8X"),
      since: z.string().datetime().optional().describe("Only orders created at or after this instant"),
      cursor: z.string().optional().describe("nextCursor from a previous call"),
    },
    outputSchema: {
      orders: z.array(orderSummary),
      nextCursor: z.string().optional(),
    },
    annotations: { readOnlyHint: true, openWorldHint: true },
  },
  async ({ status, customerId, since, cursor }) => {
    const page = await findOrders({ status, customerId, since, cursor });
    return {
      content: [{ type: "text", text: summarize(page) }],
      structuredContent: page,
    };
  },
);
```

Rules that follow from that example:

- **Constrain the input schema.** Enums over free strings, `.describe()` on every field, required vs
  optional deliberate. A well-typed schema prevents a whole class of bad calls before they happen.
- **Return structured output** (`outputSchema` + `structuredContent`) when the caller will compute on
  the result, and a readable text block alongside it for the model to reason over.
- **Annotations are hints, not enforcement.** `readOnlyHint`, `destructiveHint`, `idempotentHint`
  help a client decide what to auto-approve; the server still enforces its own rules.
- **Resource links** let a tool point at a resource instead of inlining a large payload.

## 3. Responses: spend tokens like they're yours

Every character a tool returns competes with the rest of the agent's context.

- Paginate, cap and say so: return a page plus a cursor, never 5,000 rows.
- Return the fields that drive decisions; drop internal ids, audit columns and nulls.
- Offer a verbosity switch (`detail: "summary" | "full"`) when both are genuinely needed.
- Prefer stable, readable identifiers over opaque ids where the agent has to correlate results.
- Truncate long text explicitly, with a marker and a way to fetch the rest — silent truncation makes
  the model confidently wrong.

## 4. Errors that teach

A failed call should leave the agent knowing what to do next.

```ts
return {
  isError: true,
  content: [{
    type: "text",
    text: "No order matches id 'ord_999'. Order ids look like 'ord_01H8X...'. " +
          "Use orders_search with a customerId or date range to find the right id.",
  }],
};
```

- Return `isError: true` with an explanatory message for tool-level failures. Reserve protocol errors
  for genuine protocol problems.
- Say what was wrong, what a valid input looks like, and which tool to try instead.
- Never leak stack traces, connection strings or credentials into tool output — the model may repeat
  them back to the user.
- Validate everything at the boundary even though the client validated the schema; a client is not a
  trust boundary.

## 5. Transport and deployment

| Transport | When |
|---|---|
| **stdio** | Local server launched by the client — the default for anything running on the user's machine |
| **Streamable HTTP** | Remote or shared server; supports streaming responses and resumable sessions |

The old HTTP+SSE transport is superseded by Streamable HTTP; new servers should not implement it.

For local stdio servers: never write anything but protocol messages to stdout — logs go to stderr,
or the client's parser breaks.

For remote HTTP servers:

- Validate the `Origin` header, and bind to `127.0.0.1` when the server is meant to be local, to block
  DNS-rebinding from a browser tab.
- Authenticate with OAuth 2.1: the server is a resource server, tokens must be audience-bound to it,
  and it must reject tokens minted for anyone else. Never accept a client-passed upstream token and
  forward it — that's the confused deputy, and it's the most common MCP security failure.
- Session ids identify a session; they are not credentials and never grant authorization.
- Rate limit per identity, and treat every tool call as an authorization decision on the object it
  touches, not just on the route.

## 6. Prompt injection is a design constraint

Anything a tool returns — a fetched page, a database row someone else wrote, a file — can contain
instructions aimed at the model. Assume it will.

- Keep destructive operations behind explicit, separate tools with `destructiveHint`, so a client can
  require human approval.
- Never let tool output decide authorization. The server's checks run server-side, on the caller's
  identity.
- Label untrusted content in the response ("fetched page content follows") rather than presenting it
  as your own instruction.

## 7. Testing

- **MCP Inspector** (`npx @modelcontextprotocol/inspector`) — connect, list, call each tool by hand,
  read the raw JSON-RPC. First stop for "the client can't see my server".
- Unit-test the handlers as plain functions; the SDK layer needs no mocking.
- Then test what actually matters: give a real agent real tasks and watch which tool it picks and
  where it gets stuck. Tool descriptions are prompt engineering — iterate on them with evidence, and
  keep a small suite of task prompts to re-run after every change.
- Log every call (name, duration, error) to see which tools are used, misused or dead.

---

## Checklist

- [ ] Tools consolidated around tasks, not mapped one-to-one from endpoints
- [ ] Consistent `domain_action` naming, no collisions with common servers
- [ ] Every description says what, when, when-not and what it returns
- [ ] Enums and `.describe()` on every input field; output schema where the result is structured
- [ ] Paginated, capped, field-trimmed responses
- [ ] Errors explain the fix and name the next tool
- [ ] stdio: nothing but protocol on stdout — Streamable HTTP: Origin checked, OAuth audience-bound
- [ ] Destructive tools separated and annotated
- [ ] Verified in Inspector, then with an agent on real tasks

## Anti-patterns

| ❌ | ✅ |
|---|---|
| One tool per REST endpoint | One tool per task the agent performs |
| `description: "Gets data"` | What, when, when not, and the return shape |
| Returning the full row set | A capped page plus a cursor |
| Free-text `status: string` | `z.enum([...])` |
| Errors as empty results | `isError` with a message that teaches |
| Forwarding the caller's token upstream | Tokens issued for, and validated by, this server |
| `console.log` in a stdio server | Log to stderr |
| Shipping after "it connects" | Ran real agent tasks and fixed the descriptions |
