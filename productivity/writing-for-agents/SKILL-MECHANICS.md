# Skill mechanics by host

A skill normally has a `SKILL.md` with a stable name and a short description. The description is discovery metadata, not the entire instruction body. Hosts differ in how they expose metadata and explicit invocation; do not infer universal context costs or invocation rules from one implementation.

For Codex, `agents/openai.yaml` can set `policy.allow_implicit_invocation: false`. This prevents automatic selection while retaining explicit invocation. Preserve useful interface metadata when changing policy. The Claude Code frontmatter field `disable-model-invocation: true` is a separate host setting; do not assume it alone configures Codex. Consult the installed host documentation before adding or changing controls.

A workflow may point to another skill or an ordinary reference, but such a pointer does not override host invocation policy, user intent or tool availability. Do not claim that manual-only skills are universally invisible, have zero metadata cost, or can never be explicitly requested through a workflow.

Use a router only when choosing among several distinct outcomes is useful to the user. Avoid keyword routers that activate for all work or manufacture unavailable agents. Shared references must remain accessible in the distribution mode: a link across sibling skills may fail if the user installs only one.

Source: [Codex skills documentation](https://developers.openai.com/codex/skills/), checked 2026-09-07. Recheck when host semantics matter to a change.
