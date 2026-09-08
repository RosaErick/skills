---
name: skill-optimizer
description: "Diagnose a skill’s false activations, missed triggers, harmful instructions, or excessive context cost."
metadata:
  tags: skills, optimization, benchmarking, activation, regressions, prompt-engineering
---

# Improve an observed skill failure

Start with the task, expected behavior and actual failure. Decide whether the problem is discovery, instruction ambiguity, missing domain knowledge, stale resources or an unnecessary workflow. More activation is not always better: unintended activation and scope expansion are regressions too.

Make the smallest useful revision. Keep a discriminating description and the core decisions near the entrypoint; move branch-specific detail into references. Remove redundant instructions before adding stronger wording or more checklists.

Scale evaluation to the change. For a wording/link correction, inspect the resulting text and validate the link. For a workflow rewrite or runnable helper, exercise representative behavior, including a nearby task that should not activate the skill. For uncertain model-dependent gains, use a controlled with/without comparison and record the environment and limits.

Choose a reference when needed: [activation](rules/activation-design.md), [context budget](rules/context-budget.md), [comparative benchmarks](rules/benchmark-loop.md), [regression triage](rules/regression-triage.md), or [release checks](rules/release-gates.md). A benchmark matrix and external follow-up issues are not mandatory for every edit.

Report what improved and the evidence actually collected. Structural validation or shorter text alone does not prove better task performance.
