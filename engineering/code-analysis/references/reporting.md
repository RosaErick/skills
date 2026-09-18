# Evidence and reporting

Use the user's requested output format when supplied; otherwise use the compact
shape below. Expand only where it improves a decision. These priority labels are
local reporting conventions, not a security scoring standard.

## Calibrate priority separately from confidence

| Priority | Meaning |
| --- | --- |
| P0 — critical | Immediate, severe impact requiring a stop or containment; supported without speculative deployment assumptions. Rare. |
| P1 — high | A reachable failure can cause significant data loss, unauthorized access, broken core behavior, or serious operational disruption. |
| P2 — medium | A concrete defect with limited reach, recoverable impact, or a less common but credible triggering condition. |
| P3 — low | A small actionable defect with minor impact; not a label for personal style preferences. |

Explain the affected users/data and triggering conditions; do not select priority
from scary terminology alone. Use the project's severity system instead if one
exists, and make any mapping explicit.

Describe evidence as **reproduced**, **statically supported**, or **unresolved**.
Use high/medium confidence only with a short reason, not an invented numerical
probability. A reproducible low-impact issue and a high-impact unresolved concern
are different decisions. Keep the latter in open questions rather than presenting
it as a confirmed defect.

A static finding needs a complete causal path under stated, supported conditions.
If correctness depends on unknown middleware, database configuration, or external
semantics, inspect that dependency or state the missing evidence.

## Compact report shape

```text
Scope: <paths or component; revision/working tree; base/head when relevant>
<For understanding/audit requests: short entry-point and behavior map.>

Findings, highest impact first:
- [P1] <consequence-oriented title> — <path:lines and revision side if needed>
  Trigger and impact: <condition → incorrect outcome → affected user/data>.
  Evidence: <contract + relevant path/callers/guards; reproduced or static>.
  Confidence: <high/medium and why; any bounded assumption>.
  Direction: <smallest corrective approach, not an unsolicited patch>.
  Regression check: <input/state and observable expected behavior>.

Open questions: <unresolved claim, missing fact, and next discriminating check>.
Validation: <checks actually run, scope, outcomes; proposed checks labeled as such>.
Coverage limits: <unread paths, unavailable dependencies, untested behaviors>.
```

Keep one finding per root cause; cite multiple affected locations together when
appropriate. Use short line ranges that identify the problem, not an entire file.
Do not invent line numbers from an outline or quote lines from a different
revision. If only a snippet is available, label the supplied path and snippet
lines explicitly, or identify the symbol.

In a diff review, anchor findings to the changed lines responsible for the
regression and cite baseline context where needed. Mention serious pre-existing
issues separately if relevant; do not relabel them as introduced by the patch.

## Illustrative finding

The following paths and behavior are fictional examples, not findings about the
repository being reviewed:

> **[P1] Prevent cross-tenant report cache reuse — `src/reports/cache.ts:24–31`**
>
> The cache stores a tenant-specific report under `request.path` alone. Two
> authenticated tenants requesting the same path within the cache lifetime can
> receive the first tenant's report, because a cache hit returns before the
> tenant-scoped database query. The route contract requires tenant isolation.
> This is statically supported by the cache-hit branch and its caller; confidence
> is high, but no runtime reproduction was executed. Include the tenant identity
> in the cache boundary and test that a warm cache for tenant A cannot satisfy
> tenant B's request with A's data.

Without the caller and cache-hit evidence, the same suspicion belongs in open
questions: identify which middleware or cache partitioning needs inspection.

## No-finding and blocked outcomes

- **No supported defect:** "No actionable defect found in the inspected diff and
  its callers. Validation covered X; Y was not exercised." Do not manufacture nits
  to fill the findings section.
- **Insufficient evidence:** "The snippet does not establish whether retries are
  idempotent; the provider implementation is unavailable. Inspect its deduplication
  contract or run a controlled replay test before concluding duplicate effects."
- **Unsafe/unavailable check:** State why the check was not run, what static
  inspection establishes, and what remains unknown. A blocked test runner is not
  a passed check and does not by itself prove that the code is broken.
