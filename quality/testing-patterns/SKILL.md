---
name: testing-patterns
description: "Choose useful automated tests, fixtures, and isolation boundaries for a concrete behavior or regression risk."

---

# Test the behavior that could fail

Identify the observable contract and the important risk. Prefer an existing test seam and runner. Choose unit, integration, contract or browser coverage according to what the failure crosses, rather than a fixed pyramid or percentage target.

Use independent expected outcomes, representative boundaries and descriptive failure messages. Multiple assertions may describe one behavior. Avoid testing private structure, snapshotting large unstable output, or recomputing the implementation as the expected value.

Use fakes or mocks to control external services, time or otherwise impractical dependencies. When the integration contract is the risk, cover it with a realistic fixture or contract/integration test rather than a mock that assumes correctness. Keep fixtures isolated and clean up resources deterministically.

For a bug, capture a failing case before the fix when practical. For an existing behavior, verify current expectations without inventing additional features. Trivial reversible copy/style edits can use inspection or a focused UI check; they do not automatically need new tests.

[The test runner helper](scripts/test_runner.py) is optional; inspect its detection and prefer the repository's actual commands when they differ. Report checks performed and distinguish skipped checks from passes.
