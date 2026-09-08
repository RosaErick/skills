---
name: prototype
description: "Build a focused UI or logic experiment to resolve an identified design uncertainty."
---

# Prototype the question

State the uncertainty and the observation that would resolve it. Choose [UI exploration](UI.md) for visual/interaction alternatives or [logic exploration](LOGIC.md) for state transitions and rules. Reuse existing context and constraints.

Build the smallest usable experiment that exposes the decision. Keep disposable scaffolding separate from production responsibilities and use local fixtures unless the question specifically requires an authorized integration.

Run the prototype and inspect the behavior relevant to its question. Testing effort follows the experiment's risk; a prototype does not need a production suite, but a targeted check can validate a critical assumption.

Capture the decision and useful artifact in the project's existing scratch/documentation location. Promotion into production, committing a prototype branch or updating an external issue is separate work unless already requested. When promotion is authorized, integrate deliberately and apply production validation; do not assume experimental code is ready to ship.
