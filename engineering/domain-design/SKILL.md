---
source: original
name: domain-design
description: "Translate domain rules into implementation boundaries, state transitions, and consistency decisions."
---

# Design around domain invariants

Read the relevant domain language, current model and affected use cases. Reuse an existing domain model; use `domain-modeling` when the business concepts themselves remain unclear. Choose representations from the invariants and codebase conventions, whether functions, types, modules or classes.

Identify valid states, commands, transitions and forbidden outcomes. Make invalid states hard to create and enforce authorization at the appropriate boundary. Distinguish business policy from storage and transport details.

Choose aggregate and transaction boundaries from actual consistency requirements. One aggregate per transaction is a useful DDD default, not a correctness law. A single database transaction across related records may be the simplest correct option. For asynchronous boundaries, specify retries, idempotency, ordering, failure recovery and which temporary inconsistency users can tolerate; do not impose eventual consistency where the business requires atomicity.

Keep interfaces narrow and expose behavior rather than mutable internals. Add factories, repositories or domain events when they express a real lifecycle or integration boundary, not to satisfy a class template.

Record the resulting model using [MODEL.md conventions](MODEL-FORMAT.md) when a durable model document is useful. Include decisions and concrete invariant examples that implementation and tests can use. Continue implementation when it is part of the request.
