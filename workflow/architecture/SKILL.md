---
name: architecture
description: "Evaluate system-level architecture choices against deployment, consistency, scaling, ownership, and migration constraints."

---

# Make the system decision explicit

Use the existing architecture and concrete requirement. Distinguish system boundaries/deployment from domain vocabulary (`domain-modeling`), domain invariants (`domain-design`) and module interfaces (`codebase-design`). These scopes can cooperate without duplicating every design review.

Read only the relevant branch: [context discovery](context-discovery.md), [tradeoff analysis](trade-off-analysis.md), [pattern selection](pattern-selection.md), [examples](examples.md) or [pattern reference](patterns-reference.md).

Compare credible alternatives against the actual load, consistency, availability, operating cost and team constraints. Include the cost of migration and recovery, not only the target diagram. Prefer the least complicated design that meets the requirements, while acknowledging constraints that make later change costly.

Document significant durable decisions in the project's ADR format with context, choice, consequences and rejected alternatives. Routine implementation choices need not create an ADR. When execution is requested and the choice is supported, continue with the authorized change and validate the relevant system behavior.
