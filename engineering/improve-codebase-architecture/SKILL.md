---
name: improve-codebase-architecture
description: "Find concrete architectural friction in an existing codebase and propose focused module-boundary improvements."
disable-model-invocation: true
---

# Find improvements where work is difficult

Inspect recently changed or difficult areas, callers and tests. Look for responsibilities spread across files, shallow wrappers, repeated caller knowledge and unstable boundaries. Tie each candidate to a concrete change cost or failure risk; do not score the whole repository against an abstract ideal.

For each useful candidate, describe the current friction, proposed boundary, expected benefit and migration risk. Use `codebase-design` for deeper interface tradeoffs. Independent investigations are optional when available and authorized.

Present a concise recommendation in the requested format. Use [HTML-REPORT.md](HTML-REPORT.md) only when an HTML artifact would help; Markdown and local diagrams are valid, and external CDNs are optional dependencies.

If the user requested an assessment or alternative selection, finish with the reviewable candidates. If a specific improvement is already authorized, implement and verify it rather than requiring a second selection ceremony.
