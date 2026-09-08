---
name: two-axis-review
description: "Review a code change for correctness and design, including committed, staged, and uncommitted work."
---

# Review the change that exists

Identify the requested scope from the task and `git status --short`. Infer a comparison base from branch tracking, the PR or repository history when possible. Record the chosen scope. Missing spec or base does not prevent reviewing files and behavior that are available.

| Scope | Evidence |
|---|---|
| Branch commits only | `git diff <base>...HEAD` |
| Staged change | `git diff --cached` |
| Unstaged change | `git diff` |
| Branch plus local work | Find `git merge-base <base> HEAD`, then `git diff <merge-base>`; also inspect relevant untracked files |
| Specific files or supplied patch | Read that patch plus the surrounding callers and tests needed to judge it |

`git ls-files --others --exclude-standard` identifies untracked files. Read task-relevant files without dumping secrets or generated output. For a branch with both committed and local changes, the merge-base-to-working-tree diff shows the net result; inspect intermediate diffs only when provenance matters. Review does not stage, reset or stash the user's work.

Evaluate two independent questions:

- **Correctness:** Does the result fulfill the request and preserve affected contracts? Check errors, authorization, concurrency, compatibility and meaningful test coverage where relevant.
- **Design:** Are responsibilities and interfaces understandable? Look for unnecessary coupling, duplicate sources of truth and complexity with a concrete cost. Existing conventions matter more than a preferred style.

For a small diff, use a quick pass over behavior, edge cases, security boundaries and tests. For a complex diff, separate passes help; independent reviewers are optional when delegation is available and authorized. Neither mode requires project setup or a formal spec first.

Report actionable findings in severity order, with file/line, trigger, consequence and a feasible correction. Distinguish verified defects from questions and preferences. State review coverage and checks performed; if none are found, say so with any relevant limits. When invoked as part of implementation, fix in-scope findings and validate them before finishing.
