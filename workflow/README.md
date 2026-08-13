# Workflow

How the agent runs the work: planning, orchestrating, deciding.

## Model-invoked

- **[brainstorming](./brainstorming/SKILL.md)** — Socratic questioning protocol for vague requirements, plus progress and error reporting.
- **[plan-writing](./plan-writing/SKILL.md)** — Structured planning: task breakdown, dependencies, verification criteria.
- **[architecture](./architecture/SKILL.md)** — Architectural decision framework: requirements, trade-offs, ADRs.
- **[parallel-agents](./parallel-agents/SKILL.md)** — Orchestrating multiple agents in parallel by domain.

## User-invoked

Reachable only when you type them (`disable-model-invocation: true`), because they either take over
the session or duplicate what the harness already does.

- **[app-builder](./app-builder/SKILL.md)** — Full-stack application build orchestrator driven by a natural-language request.
- **[behavioral-modes](./behavioral-modes/SKILL.md)** — Operating modes (brainstorm, implement, debug, review, teach, ship, orchestrate).
- **[intelligent-routing](./intelligent-routing/SKILL.md)** — Picks a specialist agent for a request.
