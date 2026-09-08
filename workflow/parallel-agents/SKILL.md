---
name: parallel-agents
description: "Split an explicitly delegated task into independent work units and integrate their results using available agent tools."

---

# Delegate useful independent work

Confirm that delegation is available and authorized in the current host. Inspect the actual tools and concurrency limits; do not assume named specialists, a fixed agent count or shared conversation history.

Delegate a bounded task only when useful local work can proceed alongside it. Give each worker the objective, relevant context, permitted paths/actions, expected artifact and verification responsibility. State whether workers share a filesystem and assign ownership to avoid overlapping edits.

Keep dependent decisions sequential. Read-only investigations can overlap; shared mutations need explicit coordination. Do not create a test-engineer task just to satisfy a roster, or divide a small change into agents whose work costs more to integrate than to perform.

While workers run, continue local work, communicate changed assumptions and track unresolved dependencies. Inspect their evidence and diffs, resolve conflicts and validate the integrated result. A worker's success message is not proof that the combined product works.

Report the completed outcome and verification, including any relevant unresolved gap. If tools or authorization do not support delegation, perform the task directly without pretending agents ran.
