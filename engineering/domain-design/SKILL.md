---
source: original
name: domain-design
description: "Decide the domain model itself — which invariants exist, which aggregate protects each one, what is a value object, which events the domain emits, and where one bounded context ends and the next begins. Use when designing a feature whose rules matter, when a transaction spans too much, when a term means two different things in two places, when deciding what may be eventually consistent, when splitting a service or module along domain lines, or when the code has an anemic model of a rich domain. Trigger terms: aggregate, invariant, value object, entity, domain event, bounded context, context map, anti-corruption layer, consistency boundary, DDD, transaction boundary, split this service."
---

# Domain Design

Three sibling skills, three different questions:

| Skill | Question |
|---|---|
| `domain-modeling` | What do the words mean? (`CONTEXT.md`, the glossary) |
| **`domain-design`** | **What are the things, what must always be true about them, and where are the walls?** |
| `codebase-design` | What shape does the code take? (modules, interfaces, seams) |

This one sits in the middle and is the one nobody writes down. Terminology gets a glossary, code gets
a review — but the decision that a `Cart` may never hold two lines of the same SKU, and that this
rule is checked inside one transaction while stock reservation is not, gets made silently inside an
implementation and is unrecoverable six months later.

Do this work **before** `to-spec` when the rules are the hard part. The spec then describes behavior
that the model already makes possible.

---

## 1. Start from invariants, never from nouns

The standard failure is listing nouns (Order, Customer, Product, Invoice), turning each into a class,
and discovering later that "Order" is a 40-field god object nobody can change.

Work the other way:

1. **List the rules that must never be violated.** Write them as statements, in glossary vocabulary:
   *"An order's total always equals the sum of its lines."* *"A cart may not contain two lines with
   the same SKU."* *"A refund never exceeds the amount captured."*
2. **For each rule, list what you must read to check it.** The total rule needs the order and all its
   lines. The refund rule needs the payment and its prior refunds.
3. **Group rules that need the same data.** Each group is a candidate aggregate; the data it needs is
   the aggregate's boundary.
4. **Name the group** with the term the glossary already uses — and if there isn't one, you found a
   missing glossary entry: hand it to `domain-modeling` before continuing.

What's left over — rules that need data from two groups — is the interesting part. Those are the ones
that must become eventually consistent, or must move, or reveal that the boundary is wrong. Decide
which, explicitly, and record it.

## 2. The aggregate is a consistency boundary

Not a folder, not a table, not "the entity with children". It's the answer to: *what has to be
correct all at once, in one transaction?*

The rules that follow from that:

- **One aggregate per transaction.** If saving a change touches two aggregates atomically, either
  they're one aggregate or the rule spanning them isn't really an invariant.
- **Reference other aggregates by id**, never by object. `order.customerId`, not `order.customer`.
  Object references invite lazy loading, cascade deletes and a boundary that quietly dissolves.
- **The root is the only door.** Callers get the root; everything inside is reached through it and
  changed through its methods. A line item that can be mutated from outside is not inside anything.
- **Invariants inside the boundary are enforced synchronously. Everything across boundaries is
  eventual** — and that's a business decision, not a technical one. "The customer may see stock
  reserved a second later" is a sentence a product owner must agree with.
- **Small beats big.** A large aggregate serializes writes on itself and turns unrelated updates into
  contention. When in doubt, split and accept eventual consistency between the halves.

### Symptoms

| Symptom | What it means | Fix |
|---|---|---|
| Two users editing unrelated things collide | The aggregate spans unrelated rules | Split it |
| Loading one aggregate pulls thousands of rows | A collection inside should be its own aggregate | Reference by id, query separately |
| Every use case needs three aggregates in one transaction | The boundary cuts through an invariant | Merge, or make the rule eventual |
| The root has getters for everything and no methods | Anemic model — the rules live in services | Move behavior in, keep state private |
| A "manager" or "service" class enforces the invariant | Same | Same |

## 3. Entities, value objects, and making illegal states unrepresentable

- **Value object** — no identity, equal by value, immutable, self-validating: `Money`, `EmailAddress`,
  `DateRange`, `Quantity`. Default to this. Most "entities" in a typical codebase are value objects
  wearing a database row.
- **Entity** — has identity that survives change: this `Order` is this order even after every field
  changed. Identity is the *only* reason to make something an entity.
- **Typed identifiers.** `OrderId` and `CustomerId` are different types, even when both wrap a string.
  A function that takes three bare `string` ids will eventually receive them in the wrong order.
- **Validate at construction, not at use.** A `DateRange` that cannot be built with `end < start`
  removes an entire class of check from every call site. The parse-don't-validate move: the type's
  existence is the proof.
- **Primitive obsession is the tell.** `number` for money, `string` for state, `boolean` flags for
  status. Replace with `Money`, a state union, and a state machine.

Illegal states unrepresentable beats illegal states validated. Every branch you delete is a branch
that cannot be wrong.

## 4. Domain events

An event is a **fact that already happened**, named in past tense, in glossary vocabulary:
`OrderPlaced`, `PaymentCaptured`, `ShipmentDispatched`. Not `OrderUpdated` — that's a database
notification wearing a domain costume, and every consumer will have to diff two states to work out
what actually happened.

- Events carry the facts a consumer needs to act, plus the id and the instant. They do not carry the
  whole aggregate, and they never carry a pointer the consumer must dereference to understand it.
- They are immutable and never revised. A mistake is corrected by a new event.
- **Domain event** (inside the context, in-process, free to change with the model) is not the same as
  **integration event** (published to other contexts, a contract you now owe). Publishing your domain
  events straight onto a broker exports your internal model and freezes it.
- Events are how the work that crosses aggregate boundaries gets done: one transaction changes one
  aggregate and records an event; a handler picks it up and changes the next one.

Commands, events, queries: a command may be rejected, an event cannot (it already happened), a query
changes nothing. Keep the three vocabularies apart in naming and in code.

## 5. Where the model lands in code

```
domain/        aggregates, value objects, domain events, pure rules — no I/O, no framework imports
application/   one handler per command: load aggregate → call method → save → dispatch events
adapters/      repositories, HTTP clients, the anti-corruption layer against other contexts
```

- **One repository per aggregate**, not per table. Its interface speaks the domain
  (`orders.findPending(customerId)`), never SQL.
- The application layer owns the transaction — one per command, one aggregate inside it.
- The domain layer imports nothing that knows about the outside world. If the rule needs data from
  another context, the handler fetches it and passes it in.
- Seam and interface design for all of this is `codebase-design`'s job; hand off rather than
  re-deciding it here.

## 6. Bounded contexts

A context is a region where every term has exactly one meaning. Split when:

- **The same word means two things.** "Customer" in Sales is a prospect with a pipeline stage; in
  Billing it's a legal entity with a tax id. One class serving both grows fields that are null half
  the time.
- **The lifecycles differ.** One side changes weekly, the other yearly.
- **The consistency needs differ.** One side needs atomic guarantees the other would be slowed by.
- **A single change always touches both halves** — that's the *opposite* signal: they're one context
  that's been split too early. Merge them back.

Do not split by technical layer, and do not split because a service is "getting big". Contexts follow
language and rules.

### Relating contexts

| Pattern | Use when |
|---|---|
| **Anti-corruption layer** | The other side's model is wrong for you (legacy, vendor, another team). Translate at the edge so their vocabulary never reaches your domain. The default for anything you don't own. |
| **Published language** | You expose a stable contract for many consumers: an event schema or an API type set, versioned independently of your internals. |
| **Customer/supplier** | Both sides are yours, downstream needs can shape upstream's roadmap. |
| **Conformist** | You accept the other model wholesale because translating isn't worth it. A deliberate, recorded surrender — not a default. |
| **Shared kernel** | A small set of types both sides own jointly (`Money`, `CustomerId`). Keep it tiny; every addition is a coordination cost. |
| **Separate ways** | The integration isn't worth it. Duplicate the small thing and move on. |

Record the choice in `CONTEXT-MAP.md` (format in
[`domain-modeling/CONTEXT-FORMAT.md`](../domain-modeling/CONTEXT-FORMAT.md)), and create that file
when the second context appears. If the choice was hard to reverse and the result of a real
trade-off, it's also an ADR — see `domain-modeling`.

---

## Artifact

Write the model to `MODEL.md`, next to the `CONTEXT.md` of the same context — format and a worked
example in [MODEL-FORMAT.md](MODEL-FORMAT.md).

Division of labour, so nothing is written twice:

- `CONTEXT.md` — what terms mean. Glossary only, no structure.
- `MODEL.md` — aggregates, their invariants, value objects, events, and what's eventually consistent.
- `CONTEXT-MAP.md` — the contexts and how they relate.
- ADR — a specific hard-to-reverse decision and why the alternatives lost.

Write it lazily, as decisions crystallize, the same way `domain-modeling` writes the glossary. A
`MODEL.md` produced in one sitting for a domain nobody has built yet is fiction.

## In the flow

- **Before `to-spec`** when the rules are the hard part — the spec then describes behavior the model
  supports, in vocabulary that already exists.
- **With `grill-with-docs`** when the model is genuinely unclear: that skill runs the interview, this
  one supplies the questions worth asking (which invariant, which boundary, which consistency).
- **Feeding `tdd`** — an invariant is the best test there is. Each one in `MODEL.md` should have a
  test that proves it holds and a test that proves the aggregate rejects the violation.
- **Feeding `spec-driven`** — invariants become acceptance criteria almost verbatim.
- **During `code-review`** — a diff that adds a rule to a service instead of an aggregate, or makes
  two aggregates atomic, is a model regression, not a style issue.

## Anti-patterns

| ❌ | ✅ |
|---|---|
| One class per noun, discovered from the database | Aggregates discovered from invariants |
| Anemic entities plus a `*Service` holding the rules | Behavior on the aggregate, state private |
| Aggregate references another aggregate object | Reference by typed id |
| Two aggregates saved in one transaction | One per transaction, event for the rest |
| `OrderUpdated` events | Facts in past tense: `OrderCancelled`, `LineAdded` |
| Domain events published straight to the broker | An explicit integration event you version |
| `string` ids, `number` money, `boolean` status | `OrderId`, `Money`, a state union |
| Validation scattered across call sites | Constructors that cannot build an invalid value |
| Contexts split by layer or by size | Contexts split by language and rules |
| Folders named `domain/` with none of the above | The rules actually living in the domain |

---

> An aggregate is a promise about what is true at the end of every transaction. Everything else in
> this file is bookkeeping for keeping that promise honest.
