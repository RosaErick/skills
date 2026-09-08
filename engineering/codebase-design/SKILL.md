---
name: codebase-design
description: "Design module interfaces and test seams that hide complexity and keep related changes local."
---

# Design useful module boundaries

Inspect the affected callers, responsibilities and change pressure. A deep module exposes a small understandable interface while hiding meaningful implementation complexity. A seam is an observable boundary for integration or testing; an adapter connects that boundary to an external dependency.

Name concepts in the project's language. API, service, component and module are valid terms when they describe the actual abstraction; terminology policing does not improve a boundary.

Prefer interfaces that make common operations clear, protect invariants and avoid exposing internal representation. Judge a design by caller complexity, locality of change, dependency direction and testability rather than line counts or a fixed number of entrypoints.

Read [deepening](DEEPENING.md) when combining shallow responsibilities and [alternative designs](DESIGN-IT-TWICE.md) when comparing substantially different interfaces is useful. Comparison can be done locally; delegation and agent counts depend on actual available tools and authorization.

Implement or recommend the smallest boundary change that addresses the demonstrated problem, with verification at its observable contract.
