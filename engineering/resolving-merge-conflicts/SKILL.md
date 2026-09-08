---
name: resolving-merge-conflicts
description: "Resolve an in-progress git merge or rebase while preserving both intended changes and unrelated local work."
---

# Resolve the current operation

Inspect `git status`, unmerged paths and the merge/rebase state. Read the conflicting versions, relevant commit messages and callers to understand each side's intent. Account for the different meaning of ours/theirs during a rebase instead of choosing a side by label alone.

Resolve hunks to preserve compatible intentions. When behavior is incompatible, use the stated migration or merge objective and document the choice. If a consequential decision cannot be inferred, ask that focused question while resolving independent conflicts. Do not invent a new feature to make the conflict disappear.

Run the checks relevant to the combined result and fix integration failures. Stage only resolved paths or explicitly selected hunks; never use blanket staging to collect unrelated user edits. Check the staged diff and remaining unmerged paths before continuing.

If the user requested completing the merge/rebase, continue the existing operation through remaining commits, resolving and checking each conflict as needed. A request only to inspect conflicts does not authorize completing it. Do not abort, reset, stash or overwrite unrelated work merely to simplify the task; an explicitly requested or necessary recovery can be considered with its actual consequences.

Report the resolution, verification, operation status and any unresolved decision.
