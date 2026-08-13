---
source: original
name: api-patterns
description: "HTTP API contracts: REST/GraphQL/tRPC choice, URLs, status codes, RFC 9457 errors, pagination, idempotency, versioning, rate limits, webhooks. Use when designing or reviewing an endpoint, an error format or a paging strategy."
allowed-tools: Read, Write, Edit, Glob, Grep
metadata:
  tags: api, rest, http, graphql, trpc, versioning, pagination, idempotency, webhooks
---

# API Patterns

The contract, not the framework. Implementation in Fastify is `backend/fastify`; publishing an
OpenAPI spec and a developer portal is `backend/api-documentation-master`; exposing tools to agents
over MCP is `backend/mcp-builder`.

An API is a promise about behavior that other people build on. The cost of every decision here is
paid on the day you want to change it — so decide deliberately, then stay consistent. **A boring,
predictable API beats a clever one.**

## 1. Choosing the style

| Consumers | Style |
|---|---|
| Public, third parties, many languages, long life | **REST + OpenAPI** |
| One TypeScript frontend and backend in a monorepo | **tRPC** (delete it the day a non-TS client appears) |
| Many clients with genuinely different data needs, deep graphs | **GraphQL** |
| Internal service-to-service, latency and payload critical | **gRPC** |
| Agents and LLM tools | **MCP** — see `backend/mcp-builder` |
| Server-pushed events, incremental output | **SSE** for one-way, **WebSocket** for duplex |

Two failure modes to avoid: GraphQL adopted for CRUD (you inherit N+1, caching and complexity limits
for nothing), and REST adopted for a monorepo TS app (you hand-maintain types that tRPC infers).

## 2. Resources and URLs

```
GET    /v1/orders               list, paginated and filterable
POST   /v1/orders               create
GET    /v1/orders/{id}          fetch one
PATCH  /v1/orders/{id}          partial update
DELETE /v1/orders/{id}          delete
GET    /v1/orders/{id}/items    a sub-resource, at most one level deep
POST   /v1/orders/{id}/cancel   an action that isn't CRUD — a verb, deliberately
```

- Plural nouns, lowercase, hyphens: `/purchase-orders`, never `/getPurchaseOrders`
- Nesting at most one level. Past that, filter instead: `/items?orderId=…`
- Actions that aren't a state field get an explicit verb sub-resource (`/cancel`, `/refund`,
  `/retry`). Pretending everything is CRUD produces worse APIs than admitting the exception.
- Opaque, non-sequential ids (UUIDv7, ULID). Sequential integers leak volume and invite enumeration.
- `PATCH` replaces nothing it wasn't given; `PUT` replaces the whole resource. Pick one per endpoint
  and document it — most APIs want `PATCH`.

## 3. Status codes

| Code | Meaning | Use when |
|---|---|---|
| 200 | OK | Read, or an update returning the new state |
| 201 | Created | Creation, with a `Location` header pointing at the new resource |
| 202 | Accepted | Work was queued; return something the client can poll |
| 204 | No Content | Delete, and updates that deliberately return nothing |
| 400 | Bad Request | Malformed syntax — unparseable JSON, wrong content type |
| 401 | Unauthorized | Missing, expired or invalid credentials |
| 403 | Forbidden | Valid credentials, insufficient permission |
| 404 | Not Found | No such resource — also the right answer for "exists but you may not know" |
| 409 | Conflict | State conflict: duplicate, version mismatch, already cancelled |
| 410 | Gone | The resource is deliberately, permanently removed |
| 422 | Unprocessable Content | Syntactically valid, semantically wrong (failed validation) |
| 429 | Too Many Requests | Rate limited, always with `Retry-After` |
| 500 | Internal Server Error | Your bug — never the client's fault |
| 503 | Service Unavailable | Dependency down or shedding load, with `Retry-After` |

Never return 200 with `{"success": false}`. HTTP already has the field; a client that has to parse
the body to learn it failed will eventually forget to.

## 4. Errors: RFC 9457 Problem Details

One shape for every error, `Content-Type: application/problem+json`:

```json
{
  "type": "https://api.example.com/problems/insufficient-stock",
  "title": "Insufficient stock",
  "status": 409,
  "detail": "SKU ABC-123 has 2 units available, 5 requested.",
  "instance": "/v1/orders/ord_01H8X",
  "sku": "ABC-123",
  "available": 2,
  "requestId": "req_01H8XQ"
}
```

- `type` is a stable URI the client can branch on — the machine-readable identity of the error.
  `title` and `detail` are for humans and may be reworded without a breaking change.
- Extension members (`sku`, `available`) carry what the client needs to fix the problem.
- Validation failures list every offending field at once, not the first one:
  `"errors": [{ "pointer": "/items/0/quantity", "detail": "must be between 1 and 100" }]`.
- Always include a request id, and log it server-side under the same value.
- Never leak stack traces, SQL, internal hostnames or upstream error text.

## 5. Collections

**Pagination.** Cursor by default; offset only where "jump to page N" is a real requirement.

```json
{
  "data": [ … ],
  "nextCursor": "eyJjcmVhdGVkQXQiOiIyMDI2LTA1LTAxIn0",
  "hasMore": true
}
```

Offset pagination degrades with depth (the database scans and discards) and skips or repeats rows
when the underlying data shifts between pages. Cursors are opaque, encode the sort key, and stay
constant-time. Cap `limit` server-side and document the cap.

**Filtering and sorting.** Explicit query parameters (`?status=pending&createdAfter=…&sort=-createdAt`)
beat a query DSL in a string. Whitelist sortable fields — every sortable field is an index you owe
the database.

**Field selection.** `?fields=id,status,total` for expensive payloads, if and only if a real consumer
asks for it. Sparse fieldsets are a caching problem you don't want early.

## 6. Idempotency and concurrency

Non-idempotent writes will be retried — by flaky networks, by clients, by queues. Design for it:

- `POST` that creates something accepts an `Idempotency-Key` header. Store the key with the response
  for 24h; a repeat with the same key returns the original response instead of creating a second
  resource. A repeat with the same key and a *different* body is a 422.
- `PUT`, `PATCH` and `DELETE` should be naturally idempotent. Deleting something already gone is 204
  (or 404, consistently) — never 500.
- Lost-update protection with `ETag` + `If-Match`, or a `version` field returning 409 on mismatch.

## 7. Versioning and deprecation

- Version in the URL (`/v1/…`) for public APIs: visible in logs, trivial to route, obvious to the
  reader. Header versioning is cleaner in theory and worse in practice.
- Version the whole API, not each endpoint. Per-endpoint versions become a matrix nobody can hold.
- Additive changes don't need a version: new optional fields, new endpoints, new enum values the
  client can ignore. **Removing or renaming a field, tightening validation, or changing a status code
  is breaking** — even when it "fixes" the behavior.
- Deprecate with signal, not surprise: `Deprecation` and `Sunset` headers, a `Link` to the migration
  guide, a changelog entry, and metrics on who is still calling before you remove anything.

## 8. Auth

| Pattern | Fits |
|---|---|
| Session cookie (`HttpOnly`, `Secure`, `SameSite`) | Browser client and API on the same site |
| OAuth 2.1 with PKCE | Third-party access, delegated authorization — see `backend/oauth` |
| Short-lived JWT + refresh rotation | Stateless services, multiple consumers |
| API key | Server-to-server, machine clients, simple public APIs |

Non-negotiable: TLS everywhere, tokens with short expiry, refresh tokens rotated on use and revocable,
scopes per capability rather than one god token, and authorization checked on the **object** for every
request — the top vulnerability in APIs is still a valid token reading another tenant's row.

## 9. Rate limiting

Return the state, don't just deny: `RateLimit-Limit`, `RateLimit-Remaining`, `RateLimit-Reset` on
every response, plus `Retry-After` on the 429. Limit per identity (token, user, tenant), not only per
IP. Token bucket for typical traffic; document the limits per tier in the API reference. Give clients
a reason to back off politely instead of hammering.

## 10. Webhooks and streaming

- Sign every webhook payload (HMAC over the raw body + a timestamp) and document how to verify it,
  including the replay window.
- Delivery is at-least-once: include an event id and require consumers to be idempotent.
- Retry with exponential backoff and expose the delivery history; let consumers replay.
- For long-running work: `202 Accepted` + a status resource to poll, or SSE for incremental output.
  Never hold an HTTP request open for minutes and hope.

---

## Review checklist

- [ ] Consistent URL, casing and pluralization across every endpoint
- [ ] Correct status codes; no 200-with-an-error-body anywhere
- [ ] One error shape (problem+json), stable `type` URIs, request id included
- [ ] Cursor pagination with a server-side `limit` cap
- [ ] Creation endpoints accept `Idempotency-Key`; updates guarded by `ETag`/version
- [ ] Object-level authorization on every read and write, not just route-level
- [ ] Rate limit headers on responses, `Retry-After` on 429
- [ ] Breaking changes gated behind a version, with `Deprecation`/`Sunset` before removal
- [ ] Timestamps in UTC ISO-8601, money in minor units with an explicit currency, enums documented
- [ ] The spec is generated from the code, or validated against it in CI

## Anti-patterns

| ❌ | ✅ |
|---|---|
| `/api/getUserOrders?action=delete` | `DELETE /v1/users/{id}/orders/{orderId}` |
| Error text differing per endpoint | One problem+json shape, everywhere |
| `?page=200` on a large table | Cursor pagination |
| Returning the database row verbatim | An explicit response model you control |
| Floats for money | Integer minor units + currency code |
| Local timestamps, no timezone | UTC, ISO-8601, `Z` suffix |
| Breaking change shipped "because it's a bug fix" | New version, deprecation window, migration guide |
| Auth checked once at the route | Authorization checked against the object being touched |

---

**Deeper references** in this folder: [rest.md](rest.md), [graphql.md](graphql.md),
[trpc.md](trpc.md), [auth.md](auth.md), [rate-limiting.md](rate-limiting.md),
[versioning.md](versioning.md), [response.md](response.md), [api-style.md](api-style.md),
[security-testing.md](security-testing.md). Read only the one the task needs.
