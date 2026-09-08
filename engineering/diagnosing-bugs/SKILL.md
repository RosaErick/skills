---
name: diagnosing-bugs
description: "Diagnose a reported failure, isolate its cause with evidence, and verify a targeted fix."
---

# Diagnose from evidence

Capture expected versus actual behavior, the failing input, environment and available error evidence. Inspect the relevant implementation and callers as needed to build a reproduction; a reproduction is useful evidence, not a gate that forbids reading code.

Try the cheapest discriminating check: run the failing test, replay a safe request, inspect a trace or construct a small fixture. If production-only conditions cannot be recreated, record what is known and use static reasoning or instrumentation without claiming a reproduced failure.

Form only the hypotheses needed to explain current evidence. Test the most informative one next and update the explanation. Minimize a case when it will distinguish causes; exhaustive minimization and a fixed number of hypotheses are unnecessary. Avoid unrelated changes while the cause is uncertain.

Fix the cause at the responsible boundary. Where practical, preserve the failing case as a regression test that fails before and passes after the fix. Check neighboring behavior and required project checks. Report the causal chain, what changed and how it was verified; separate remaining uncertainty from established facts.

For bugs needing human interaction or unavailable hardware, adapt the [human-assisted loop template](scripts/hitl-loop.template.sh). Do not invent observations from a run the user has not performed.
