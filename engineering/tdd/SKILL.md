---
name: tdd
description: "Develop or fix behavior through a failing test, a minimal implementation, and safe refactoring."
---

# Red, green, refactor

Use the project's test runner and agreed observable behavior. Reuse established test seams and acceptance criteria. Ask about an unresolved business decision only when it changes what should pass; do not ask again for already approved interfaces.

1. Choose one useful vertical behavior, including a failure case when that is the risk. Write a test through a stable interface, then run it and confirm it fails for the intended missing or incorrect behavior. Setup errors are not the red signal.
2. Implement enough production behavior to pass. Run the focused test and nearby affected tests.
3. Refactor while green when duplication or a misleading boundary has become visible. Preserve behavior and rerun affected checks. Refactoring is part of this loop, not a forbidden phase.
4. Repeat for remaining agreed behavior, then run the required project checks.

Prefer independent expected values and observable outcomes. Several assertions can describe one coherent behavior. Avoid mirroring internals, speculative tests for unrequested features, and mocks that supply the answer being tested. Boundary fakes can isolate time, external services or costly I/O; use integration coverage when the boundary contract itself is the risk.

Read [test examples](tests.md) when selecting an assertion boundary and [mocking guidance](mocking.md) when isolation is necessary. The loop does not mandate commits, a specific test pyramid or agents per cycle. For a trivial reversible edit, use a proportional verification method rather than manufacturing a red test.
