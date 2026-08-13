---
source: original
name: spec-driven
description: "Turn a spec into numbered acceptance criteria that live in the repo, bind each criterion to the test that proves it, and verify the binding against a test run — finding criteria no passing test claims, tests citing criteria that no longer exist, tests that carry an id without asserting the behavior, and criteria the code now contradicts. Use when a spec needs criteria before implementation starts, when asked whether the code still does what the spec says, when writing or reviewing acceptance criteria, when a feature's behavior is disputed, or when checking that a change kept its promises. Trigger terms: acceptance criteria, spec-driven development, SDD, given when then, does the code match the spec, spec drift, traceability, definition of done, is this covered by a test."
---

# Spec-Driven

A spec is worth keeping only if it can be proven false. Prose can't be: *"the checkout should handle
invalid carts gracefully"* is true of every implementation and of none. A criterion can:
*"Given a cart with zero lines, when checkout is submitted, the order is rejected and the cart is
unchanged."* One of those is falsifiable, and therefore testable, and therefore still worth reading
next year.

This skill owns the link between three things that normally drift apart:

```
spec (why + what)  →  criteria (falsifiable)  →  tests (executable)  →  code
```

`to-spec` writes the first. `tdd` writes the third. Nothing in the flow keeps the middle honest, and
without it the spec closes with the ticket and stops describing reality.

## When it runs

- **Before implementation** — turn an agreed spec into criteria, and get them confirmed. Cheapest
  possible moment to discover that two people read the spec differently.
- **During implementation** — each criterion is a red test waiting to be written. `tdd` does the loop.
- **After a change** — verify: is every criterion still proven, and does any of them now disagree
  with the code?
- **On an old feature** — reconstruct criteria from the tests that exist, to find out what is
  actually guaranteed versus what everyone assumes.

---

## 1. Writing a criterion

```md
### AC-3 — Reject an empty cart

**Given** a cart with no lines
**When** checkout is submitted
**Then** the order is rejected with `EmptyCart` and the cart is left unchanged

Seam: `checkout()` application handler
```

Five rules, all of which fail loudly when broken:

1. **Falsifiable.** You can describe the run that makes it fail. "Graceful", "user-friendly",
   "performant" cannot fail — rewrite or drop them.
2. **One behavior.** A criterion containing "and also" is two criteria. Splitting them is what makes
   a failure point at something.
3. **Observable at a seam.** State the seam it will be tested at, and prefer one that already exists
   (`codebase-design`'s vocabulary, `tdd`'s seam discipline). A criterion nobody can observe without
   reaching into internals is describing implementation, not behavior.
4. **Glossary vocabulary.** Terms from `CONTEXT.md`. A criterion that invents a word has found a
   missing glossary entry — send it to `domain-modeling` first.
5. **No implementation.** No file paths, no function names beyond the seam, no "sets `status` to
   `'cancelled'`". What the system does, not how.

**Non-functional criteria need a number or they aren't criteria:** *"p95 under 300 ms at 100 rps with
a 10k-row cart"*, not *"fast"*. If nobody will commit to the number, the requirement isn't real yet —
say so instead of writing an unprovable line.

**Invariants make the best criteria.** If `MODEL.md` exists (`domain-design`), every invariant should
appear here twice: once proving it holds, once proving the system rejects the violation.

## 2. Where criteria live

```
docs/specs/0007-checkout-rejection.md
```

In the repo, versioned with the code, changed in the same commit as the behavior they describe. The
tracker keeps the discussion and the decision trail; the repo keeps the contract. An issue gets
closed and forgotten — a file in `docs/specs/` shows up in every grep and every review.

Format and the full file template: [CRITERIA-FORMAT.md](CRITERIA-FORMAT.md).

If the project runs the tracker flow, link the spec issue at the top of the file and the file from
the issue. If it doesn't, this works standalone — the file is the spec.

## 3. Binding criteria to tests

The binding is the criterion id in the test name:

```ts
test("AC-3: rejects an empty cart and leaves it unchanged", …)
```

```python
def test_ac_3_rejects_an_empty_cart(): ...
```

Plain text, greppable from either direction, no tooling, no annotations to maintain, works in every
language and runner. One criterion may need several tests; every criterion needs at least one.

Rules:

- **The id never changes.** `AC-3` means the same thing forever. Superseded criteria are marked
  `~~AC-3~~ superseded by AC-9`, never renumbered — renumbering silently breaks every binding.
- **A skipped test does not count as proof.** Verification reports it as unproven.
- **A criterion may be marked `not-tested` with a reason** — a manual check, a third-party behavior.
  Deliberate and visible beats silently missing.

## 4. The verify pass

**Run the test suite first.** Everything below is read against what actually ran — not against what
the source files appear to contain. This is not pedantry: a grep-based verifier was tried here and
dropped, because it reported a commented-out test and a test inside `describe.skip` as proven. A
string in a file is not evidence.

With the suite's output in hand, four questions, in order:

**Uncovered** — which criteria does no passing test claim? Collect the ids from the runner's report
(the names of tests that ran and passed), and compare against the ids in `docs/specs/`. An id that
appears only in the source but not in the report means the test is skipped, commented out, filtered
out by a pattern, or failing. All four are "unproven".

**Orphaned** — which tests cite an id that no longer exists in any spec? That test is guarding a
promise nobody made. Either the criterion was deleted without its test, or the id was mistyped.

**Hollow** — open each test that claims a criterion and check that it *asserts* the behavior the
criterion describes. A test named `AC-3` that asserts nothing, or asserts something adjacent, is a
label, not a proof. This is the one only a reader catches, and it's the most common failure in a
suite that was retrofitted with ids.

**Contradiction** — read the code behind each criterion and decide whether it still does what the
criterion says. When they disagree, one of them is wrong, and the resolution is a decision, never a
silent edit:

- The code is wrong → it's a bug; the criterion stays, and a test should already be failing.
- The criterion is outdated → mark it superseded, write the new one, note why in the spec.

Never "update the doc to match the code" without saying which of the two you decided was right. That
move is how a spec becomes a changelog of whatever happened.

If the suite emits JUnit XML (`vitest --reporter=junit`, `jest --reporters=jest-junit`,
`pytest --junit-xml`, Maven surefire, `phpunit --log-junit`), the first two questions can be answered
mechanically from that report, since it lists each test's name and whether it passed, was skipped or
failed. Write that check for the project at hand if it's worth it there — it is not worth shipping as
a generic script, because the useful half of this pass is the reading.

## 5. Reporting

Report as a table, most alarming first:

```
AC-1  proven         checkout.test.ts:14 (passed)
AC-2  proven         checkout.test.ts:31, cart.test.ts:8 (passed)
AC-3  UNCOVERED      no passing test claims it
AC-4  UNPROVEN       checkout.test.ts:52 — inside describe.skip, never ran
AC-5  HOLLOW         cart.test.ts:20 claims it but only asserts the call didn't throw
AC-7  CONTRADICTED   code rejects with `InvalidCart`, criterion says `EmptyCart`
```

Then one line of judgement: is this feature actually guaranteed, or does it just have tests? Those
are different claims, and only reading the criteria against the suite tells them apart.

## In the flow

| Skill | Relationship |
|---|---|
| `to-spec` | Writes the spec. This skill turns it into criteria — run it right after. |
| `to-tickets` | Splits work; a ticket should carry the criterion ids it closes. |
| `tdd` | Writes the tests. Each red test starts as a criterion id. |
| `implement` | Builds it; the criteria are the definition of done. |
| `code-review` | Its Spec axis asks "does this match the spec?" — criteria give it something exact to check instead of re-reading prose. |
| `domain-design` | Invariants in `MODEL.md` become criteria nearly verbatim. |
| `triage` | An incoming bug is a criterion that was missing or wrong. Add it, then fix. |

## Anti-patterns

| ❌ | ✅ |
|---|---|
| Criteria written after the tests, to match them | Criteria first — they're the reason the test exists |
| "Handles errors gracefully" | The specific input, the specific outcome |
| 40 criteria for a two-day feature | The behaviors someone would notice breaking |
| Criteria naming functions and fields | Behavior at a seam |
| Renumbering when one is removed | Ids are permanent; supersede instead |
| Criteria in a tracker comment | A file in `docs/specs/`, versioned with the code |
| Verifying once, at merge | Verifying whenever the behavior is questioned |
| Trusting a grep over the test suite's own report | Reading the report, then the tests it names |
| Editing a criterion to match new code, silently | Deciding which was wrong, and recording it |
| A test name counted as proof | Proof is a test that ran, passed and asserts the behavior |

---

> Tests prove the code does what the tests say. Criteria are what make that the same question as
> "does the code do what we agreed?".
