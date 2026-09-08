---
name: implement
description: "Implement an agreed spec, ticket, or clearly scoped change through validation and review."
disable-model-invocation: true
---

# Implement the agreed outcome

Read the request, applicable repository instructions, relevant code and current git status. Reuse decisions and acceptance criteria already agreed in the conversation; a separate spec file or setup skill is not a prerequisite.

Implement a coherent slice, using existing interfaces and test seams. Use `tdd` for behavior that benefits from a regression test; a reversible copy or style edit need not acquire artificial tests. Run focused checks during changes and the project's required checks before finishing.

Review the actual work with `two-axis-review`: include applicable commits, staged changes, working-tree changes and relevant untracked files. A comparison ending at HEAD alone misses work performed before a commit. Resolve actionable findings within scope, rerun affected checks, and repeat review when the fixes warrant it.

Continue until the authorized outcome is complete. Report behavior changed, verification and any real limitation. Preserve unrelated user edits. Commit, push, publish or deploy when the request or project workflow authorizes that action; implementation itself does not require creating a commit.
