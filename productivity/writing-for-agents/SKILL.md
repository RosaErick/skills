---
name: writing-for-agents
description: "Write or revise instructions for agents with precise scope, useful references, and low context cost."
---

# Write instructions that change behavior usefully

Start from a concrete task and observed failure. Keep the decision rule, domain constraint or resource that a capable agent would otherwise miss. Remove generic competence advice, duplicated host rules and extra process that does not improve the result.

Use a short, discriminating description: the task and the condition that should activate the skill. Exclude adjacent tasks that need a different workflow. Put core decisions in the entrypoint and specialized examples or implementation details in linked references, naming when each is useful. Do not require reading every reference.

Prefer clear outcomes and reasons over rigid sequences or escalating MUST/NEVER language. Reserve hard constraints for actual invariants and authorization boundaries. Reuse available context and previous user decisions. Match validation to the failure risk rather than imposing interviews, approvals, tests or agents on every task.

Check references, scripts and paths in an installed copy as well as in the repository. Evaluate a representative positive task and a plausible false-positive trigger; for a substantial rewrite, compare outputs against the observed failure. Brevity alone is not evidence of better behavior.

For skill frontmatter and host-specific invocation controls, read [skill mechanics](SKILL-MECHANICS.md). Keep claimed host behavior tied to documentation and avoid treating a natural-language instruction as an enforcement mechanism.
