---
name: to-spec
description: "Turn an agreed change into an implementation-ready specification with observable acceptance criteria."
disable-model-invocation: true
---

# Write the useful specification

Use the request, existing decisions and relevant code to describe the problem, desired behavior and scope. Ask only about material ambiguities that change implementation or acceptance; carry forward agreed interfaces and test seams.

Scale the document to the change. A small behavior may need a few paragraphs and examples. A larger feature benefits from explicit non-goals, affected contracts, data/state transitions, failure behavior, compatibility and rollout. Include user stories only where they clarify distinct outcomes; do not manufacture a long inventory.

Make acceptance criteria observable and independently testable. Separate required behavior from suggestions about implementation. Identify unresolved decisions honestly rather than filling them with invented business rules.

Draft in the established documentation or issue format without requiring setup. Writing a local draft is part of this work. Create or update an external issue when the user authorized it; otherwise complete the draft so any needed approval concerns a concrete artifact. If implementation was requested too, continue from the agreed spec.
