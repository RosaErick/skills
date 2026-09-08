---
name: ask-matt
description: "Choose an engineering workflow for an idea, specification, implementation, review, or handoff."
disable-model-invocation: true
--- 

# Choose the next useful workflow

Route by the user's intended outcome and the evidence already present. Start at the relevant step; this is an index, not a mandatory lifecycle.

| Need | Workflow |
|---|---|
| Clarify a consequential product decision | `grilling` |
| Describe domain language or invariants | `domain-modeling`, then `domain-design` if an implementation model is needed |
| Record an agreed change | `to-spec` |
| Split substantial work for delivery | `to-tickets` or `wayfinder` |
| Deliver an agreed change | `implement` |
| Investigate a failure | `diagnosing-bugs` |
| Assess an existing diff | `two-axis-review` |
| Transfer context | `handoff` |

Use existing repository conventions. `setup-matt-pocock-skills` is available when the user wants to configure this collection; it is not required before doing work. Small requests often need none of these intermediate artifacts.

Continue the authorized work after a workflow produces its result. Do not clear context, demand a new session or stop at a planning artifact when implementation is requested. For an actual context transition, consult [continuity guidance](PHASE-BOUNDARIES.md).
