# Criteria file format

One file per spec, in `docs/specs/`, named `NNNN-slug.md` with a zero-padded sequence that never gets
reused.

## Template

```md
# 0007 — Checkout rejection rules

**Status:** agreed | in progress | shipped | superseded by 0011
**Spec:** #142 (tracker) · **Context:** src/ordering
**Updated:** 2026-05-14

## Scope

One paragraph: the behavior this file governs, and what it deliberately leaves out.

## Criteria

### AC-1 — Reject a cart with no lines

**Given** a cart with no lines
**When** checkout is submitted
**Then** the order is rejected with `EmptyCart` and the cart is left unchanged

Seam: `checkout()` application handler

### AC-2 — Reject a cart whose stock has gone

**Given** a cart holding a SKU that is now out of stock
**When** checkout is submitted
**Then** the order is rejected with `OutOfStock` naming the SKU, and the remaining lines are kept

Seam: `checkout()` application handler

### AC-3 — Checkout stays responsive under load

**Given** 100 concurrent checkouts of 10-line carts
**When** each is submitted
**Then** p95 end-to-end latency is under 300 ms

Seam: load test against the HTTP boundary

### ~~AC-4~~ — superseded by AC-8

Partial checkout was replaced by whole-cart rejection. See 0011.

### AC-5 — Rejection is visible in the audit log

**Given** any rejected checkout
**When** the rejection is recorded
**Then** an `OrderRejected` entry exists carrying the cart id, the reason and the instant

Seam: `auditLog` port · **not-tested:** verified manually against the vendor's log viewer; no
sandbox available.

## Out of scope

- Payment failures after acceptance — governed by 0009
- Cart merging on login — governed by 0004
```

## Rules

- **Ids are permanent.** `AC-3` refers to the same behavior forever. Remove a criterion by striking it
  through and naming its successor; never renumber the survivors.
- **Given / When / Then, one behavior each.** "And also" means two criteria.
- **Every criterion names its seam** — the observation point where its test will live. Prefer a seam
  that already exists.
- **Numbers for anything non-functional.** No number, no criterion.
- **Glossary vocabulary only.** New term ⇒ add it to `CONTEXT.md` first.
- **`not-tested:` requires a reason**, on the same line. It's a visible, deliberate gap — not a
  missing test.
- **Status is one word**, and `superseded by NNNN` names the file that replaced it.

## Test binding

The criterion id, verbatim, at the start of the test name:

```ts
test("AC-1: rejects a cart with no lines", …)
describe("checkout", () => { test("AC-2: rejects a SKU that went out of stock", …) })
```

```python
def test_ac_1_rejects_a_cart_with_no_lines(): ...
```

```go
func TestAC1_RejectsACartWithNoLines(t *testing.T) { … }
```

The verifier matches `AC-<n>` case-insensitively and tolerates `_`, `-` or a space between `AC` and
the number, so all three styles above bind correctly. Anything else — an annotation, a comment, a
separate mapping file — is a second source of truth that will rot.

## Repos with several contexts

One `docs/specs/` at the repo root, with `**Context:**` naming which context each spec governs. A
spec that governs two contexts is a sign the boundary is wrong — check with `domain-design` before
writing it.
