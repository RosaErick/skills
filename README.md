# skills

My agent skills — 81 of them, all in one place, organized by category.

Each skill is a folder with a `SKILL.md` (frontmatter `name` + `description`) and supporting files
alongside it when needed. It's the standard format Claude Code, Codex, opencode and the like read:
to use them in a project, point or link the category you want into that project's `.claude/skills`.

A new skill goes into whichever category fits. If none fits, create the folder, write its README,
and add the row to the table below.

## Categories

| Folder | What's in it | Skills |
|---|---|---|
| [engineering](./engineering/README.md) | Code workflow: spec → tickets → implement → review, TDD, bug diagnosis, domain modeling | 18 |
| [frontend](./frontend/README.md) | React, Next.js, Tailwind, interface design, mobile, web performance, i18n | 21 |
| [backend](./backend/README.md) | APIs, Node, Python, Rust, databases, MCP | 7 |
| [infra](./infra/README.md) | Shell, server management, deployment | 4 |
| [quality](./quality/README.md) | Testing, review, debugging, linting, profiling | 8 |
| [security](./security/README.md) | Vulnerabilities and red teaming | 2 |
| [workflow](./workflow/README.md) | How the agent works: brainstorming, planning, architecture, multi-agent orchestration | 7 |
| [writing](./writing/README.md) | Copy, UX writing, documentation, SEO/GEO | 6 |
| [productivity](./productivity/README.md) | Non-code work: grilling, handoff, teaching, job search | 8 |
| **Total** | | **81** |

The READMEs under `engineering/` and `productivity/` split their skills into **user-invoked** (only
run when you type them) and **model-invoked** (the model reaches for them from the description). The
other categories don't make that distinction yet — everything in them is model-reachable.

## Original skills

They carry `source: original` in their frontmatter; everything else here comes from
the community — public skill packs, vendor guides and open-source repos — kept because I use them,
and curated: picked one by one, filed by category, trimmed of what I don't run.

| Skill | What it does |
|---|---|
| [frontend/nextjs-best-practices](./frontend/nextjs-best-practices/SKILL.md) | App Router defaults: Server Components, data fetching, routing |
| [frontend/react-patterns](./frontend/react-patterns/SKILL.md) | Modern React: hooks, composition, performance, TypeScript |
| [frontend/react-ui-patterns](./frontend/react-ui-patterns/SKILL.md) | Loading states, error handling and async data in components |
| [frontend/react-modernization](./frontend/react-modernization/SKILL.md) | Version upgrades, class-to-hooks migration, concurrent features, codemods |
| [frontend/web-performance-optimization](./frontend/web-performance-optimization/SKILL.md) | Core Web Vitals, bundle size, caching, runtime performance |
| [backend/api-documentation-master](./backend/api-documentation-master/SKILL.md) | API docs end to end: OpenAPI 3.1, interactive docs, multi-language samples, CI/CD automation |
| [writing/documentation-master](./writing/documentation-master/SKILL.md) | Technical documentation: API, architecture, code and user docs, with Mermaid diagrams |
| [writing/ux-writing](./writing/ux-writing/SKILL.md) | UX writing, guided interaction and interface usability |

## Known overlaps

Kept on purpose, since they're different depths of the same subject:

- `engineering/tdd` (guided loop, with references) × `quality/tdd-workflow` (short checklist)
- `engineering/code-review` (two-axis review, sub-agents) × `quality/code-review-checklist`
- `engineering/diagnosing-bugs` (diagnosis loop) × `quality/systematic-debugging` (4 phases)
- `frontend/nextjs-react-expert` × `frontend/react-best-practices` — same Vercel rules, one as a guide, one as a rule base
