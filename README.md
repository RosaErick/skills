# Skills

A curated collection of **17 skills and one prompt command**, with **Pi Agent** as the default host.

A focused, Pi-first collection rebuilt from selected skills. The previous collection is preserved on the [`old_version`](https://github.com/RosaErick/skills/tree/old_version) branch.

## Use with Pi Agent

The package manifest exposes the skill categories and `/discuss` directly to Pi. Each skill contains a `SKILL.md` and any supporting scripts or references.

Install directly from GitHub:

```bash
pi install git:github.com/RosaErick/skills
```

Or use a local clone when editing the collection:

```bash
pi install /path/to/skills
```

Choose one route; do not also register the same skills through symlinks or the `skills` setting. Restart Pi or use `/reload` after changing resources. See [MIGRATION.md](MIGRATION.md) for upgrading and rollback.

Invoke a skill with `/skill:name`, such as `/skill:tdd`. Use `/discuss` to clarify a plan before implementation.

## Categories

| Folder | Focus | Skills |
| --- | --- | --- |
| [backend](backend/) | API contracts and documentation | 2 |
| [engineering](engineering/) | Domain design and test-driven development | 2 |
| [frontend](frontend/) | Interface design, localization, performance, browser automation | 4 |
| [productivity](productivity/) | Terminal sessions, web search, GitHub | 3 |
| [workflow](workflow/) | Planning, architecture, agent coordination | 3 |
| [writing](writing/) | Technical docs, interface copy, changelogs | 3 |

## Skills

| Skill | Purpose |
| --- | --- |
| [api-documentation-master](backend/api-documentation-master/SKILL.md) | API references, OpenAPI contracts, guides, and examples |
| [api-patterns](backend/api-patterns/SKILL.md) | HTTP contracts, errors, pagination, versioning, and rate limits |
| [domain-design](engineering/domain-design/SKILL.md) | Domain rules, boundaries, state transitions, and consistency |
| [tdd](engineering/tdd/SKILL.md) | Failing tests, minimal implementation, and safe refactoring |
| [frontend-design-mitsuhiko](frontend/frontend-design/SKILL.md) | Distinctive, working frontend interfaces |
| [i18n-localization](frontend/i18n-localization/SKILL.md) | Locale messages, formatting, and language behavior |
| [web-performance-optimization](frontend/web-performance-optimization/SKILL.md) | Measure and improve loading, responsiveness, and stability |
| [web-browser](frontend/web-browser/SKILL.md) | Chrome/Chromium automation through CDP |
| [github](productivity/github/SKILL.md) | Issues, pull requests, and CI through the GitHub CLI |
| [native-web-search](productivity/native-web-search/SKILL.md) | Provider-native web search with source URLs |
| [tmux](productivity/tmux/SKILL.md) | Interactive terminal sessions and output capture |
| [architecture](workflow/architecture/SKILL.md) | System-level choices, constraints, and trade-offs |
| [parallel-agents](workflow/parallel-agents/SKILL.md) | Explicitly requested delegation and result integration |
| [plan-writing](workflow/plan-writing/SKILL.md) | Implementation plans with dependencies and verification |
| [documentation](writing/documentation/SKILL.md) | Tutorials, how-to guides, references, and explanations |
| [ux-writing](writing/ux-writing/SKILL.md) | Clear interface labels, instructions, and messages |
| [update-changelog](writing/update-changelog/SKILL.md) | Concise, user-facing release notes |

## Prompt command

- [`/discuss`](prompts/discuss.md): inspect the project, ask focused questions, and refine a plan without implementing it.

## Requirements

Pi handles skill discovery; individual helpers have their own requirements. Terminal automation uses `tmux`, GitHub workflows use `gh`, browser automation requires Chrome/Chromium and its script dependencies, and native web search requires Node.js and provider authentication. Follow each skill's setup instructions.

## Sources

Selected from [RosaErick/skills](https://github.com/RosaErick/skills) and [mitsuhiko/agent-stuff](https://github.com/mitsuhiko/agent-stuff). Imports retain their supporting files and original content for incremental review.

`frontend-design-mitsuhiko` was recovered from the `agent-stuff` history and given a distinct invocation name to coexist with other `frontend-design` skills. See [SOURCES.md](SOURCES.md) for provenance and licensing notes.
