# Skill catalogue migration — September 2026

The catalogue now has **67 active skills**: 39 rewritten, 19 adjusted, six retained and three optional shortcuts retained. Seven overlapping entrypoints were merged and five removed from active distribution. `wait-what` also received its recommended language/context correction.

| Previous entry | Replacement |
|---|---|
| `tdd-workflow` | `tdd` — one red/green/refactor workflow |
| `systematic-debugging` | `diagnosing-bugs` — evidence, reproduction and causal verification |
| `code-review-checklist` | `two-axis-review` — quick mode and complete diff selection |
| `nodejs-best-practices` | `node` — service architecture reference |
| `nextjs-app-router-patterns` | `nextjs-best-practices` — version-aware App Router reference |
| `performance-profiling` | `web-performance-optimization` — measurement reference and Lighthouse helper |
| `brainstorming` | `grilling` — optional exploration mode |
| `clean-code`, `intelligent-routing`, `behavioral-modes`, `bash-linux`, `rust-pro` | Archived; no automatic replacement |

Useful distinctions remain: domain language/model/module design; API contract/framework/docs; Node applications/runtime contributions; general React/state/performance. `grill-me`, `grill-with-docs` and `wait-what` remain optional personal shortcuts.

## Installed links and copies

Rerun the existing install command for the host/target you maintain. The installer removes retired symlinks only when they point back to this checkout and their category was selected. It preserves real copied directories and links owned by another collection. Copy-mode users should compare their modified copies with this mapping before removing retired copies manually; `-f` replaces active copies only when explicitly selected.

The flat `skills/` plugin bundle contains 67 symlinks to the canonical category directories. `scripts/check.sh` refreshes it without deleting real files found there. No external publication or host reinstall is implied by editing this checkout.

## Validation and generated files

Run `scripts/check.sh --check` for catalogue structure, local Markdown links at all reference depths, explicit-invocation metadata, merger targets and generated-file drift. Run `python3 -m unittest discover -s scripts/tests -v` for helper regression tests; optional OpenAPI and PowerPoint tests require their declared Python dependencies.

The OpenAPI validator's canonical source is `backend/api-documentation-master/scripts/`. `scripts/check.sh` generates the copy bundled with `api-patterns`, so either skill remains usable when installed alone or distributed through npm. Do not edit the generated copy directly. Both JSON and YAML use a schema validator; missing dependencies, absent specs and unsupported remote references are explicitly unverified. Local references are confined to the input document's directory.

The OAuth example has its own pinned dependencies and local-provider tests under `backend/oauth/examples/authorization-code/`. Lint checks use configured commands and the detected package manager. Security regex matches are candidates; registry advisories are separate evidence and require `--audit-dependencies`. GEO output contains observations, without ranking/citation scores. UI/UX Pro Max now includes its previously missing 24 CSV files, pinned upstream provenance and MIT license; searches fail explicitly if data is absent. The detailed validation record is in [the application report](APLICACAO-SKILLS-2026-09-08.md).

## Reversible local archive

Before modification, a snapshot was created at `.archive/skills-before-2026-09-07.tar.gz` (539 members; SHA-256 `18733be5d47a253c2c263d6797474ed5a7837279c4888daeb89fdcd01776d1d1`). It includes retired skills and the old UX writing generators/PDFs. Extract selected paths to a separate directory when comparing or recovering content; do not overwrite current work blindly.

The archive is ignored by git and excluded from distribution. Historical tracked content also remains in the pre-migration repository history. The original audit is a historical assessment; its citations refer to the original revision rather than the rewritten files.
