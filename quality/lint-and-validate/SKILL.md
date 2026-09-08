---
name: lint-and-validate
description: "Run the project’s configured lint, type, and relevant validation checks for a coherent code change."

---

# Validate the change using project commands

Inspect package scripts, lockfiles, CI and tool configuration. Use the existing package manager and supported commands. Do not install a new linter or infer that every Python project uses mypy merely from a pyproject file.

Run focused checks after a coherent change, then the required project checks before delivery. Select checks from the affected behavior and dependencies; neither a keystroke-by-keystroke lint loop nor an automatic full security audit is necessary.

Fix failures introduced by the work and rerun affected checks. Separate pre-existing failures using available baseline evidence; do not reset unrelated work to manufacture a clean baseline. A missing tool or unconfigured check is an explicit limitation, not a successful validation.

[lint_runner.py](scripts/lint_runner.py) can run detected configured checks; inspect its detected commands and use direct project commands when a custom workflow is more accurate. [type_coverage.py](scripts/type_coverage.py) is a heuristic aid, not a substitute for the compiler/type checker.

Report commands or a concise verification summary, results and material gaps. Continue authorized fixes without adding a confirmation round solely because a check found a problem.
