# MODEL.md Format

`MODEL.md` sits next to the `CONTEXT.md` of the same context — repo root for a single-context repo,
`src/<context>/` when a `CONTEXT-MAP.md` exists.

It records **decisions about the model**: what the aggregates are, what each one guarantees, and what
is deliberately allowed to lag. It is not a class list, not a schema, and not a spec.

## Structure

```md
# {Context Name} — Model

## Aggregates

### Order

**Protects:**
- An order's total always equals the sum of its line amounts
- An order may not contain two lines with the same SKU
- A confirmed order cannot change its lines

**Boundary:** the order, its lines and its discounts. Payments and shipments are separate aggregates.

**Identity:** `OrderId` (UUIDv7, assigned by us at placement)

**References:** `CustomerId`, `SkuCode` — by id, never loaded inside the transaction

**Emits:** `OrderPlaced`, `LineAdded`, `OrderConfirmed`, `OrderCancelled`

### Payment

**Protects:**
- A payment's refunds never sum to more than the amount captured
- A payment can be captured at most once

**Boundary:** the payment and its refunds

**Identity:** `PaymentId`

**References:** `OrderId`

**Emits:** `PaymentCaptured`, `RefundIssued`

## Value objects

- **Money** — amount in minor units plus a currency; arithmetic refuses to mix currencies
- **SkuCode** — validated at construction, uppercase, `AAA-000` shape
- **DateRange** — cannot be constructed with `end` before `start`

## Events

| Event | Emitted when | Carries | Consumed by |
|---|---|---|---|
| `OrderPlaced` | An order is submitted | `orderId`, `customerId`, line SKUs and quantities | Fulfillment (starts picking) |
| `PaymentCaptured` | The gateway confirms capture | `paymentId`, `orderId`, `Money` | Billing (issues the invoice) |

`OrderPlaced` and `PaymentCaptured` are **integration events**: their shape is a contract with the
other contexts and is versioned. Everything else in this file is internal and free to change.

## Eventual consistency, deliberately

- **Stock reservation** lags order placement by up to a few seconds. Agreed with product: an order
  may be placed and then rejected for stock. The customer sees "confirming…" in the meantime.
- **Invoice generation** lags capture by up to a minute. Nobody is waiting on it.

## Open questions

- Can a cancelled order be reinstated, or is a new order the only path? Blocks the `OrderCancelled`
  consumer in Fulfillment.
```

## Rules

- **Invariants are statements, in glossary vocabulary.** *"A confirmed order cannot change its
  lines"*, not *"validate `status !== 'confirmed'` before mutating `lines`"*. If a term isn't in
  `CONTEXT.md`, add it there first.
- **Every aggregate names what it protects.** An aggregate with no invariant to defend is a table
  with ambitions — merge it into whatever does have the rule, or make it a value object.
- **Say what is *not* in the boundary**, and why. That sentence is the one that stops the aggregate
  from growing next quarter.
- **List eventual consistency explicitly.** Anything not listed is expected to be atomic; if the code
  disagrees, the code is wrong or the file is stale.
- **Mark which events are integration events.** Everything else stays internal and refactorable.
- **Open questions belong here** while they're open. An unanswered question in the model is worth
  more than a confident guess.
- **Write lazily.** Add an aggregate when it's decided, not when it's imagined. Delete sections that
  stopped being true rather than letting them rot.
- **No code, no schemas, no file paths.** They go stale in a week; the decisions here should outlive
  three refactors. The only exception is a type shape that encodes a decision more precisely than
  prose can — a state union, for instance.
