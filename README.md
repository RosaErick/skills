# skills

My agent skills — 77 of them, all in one place, organized by category.

Each skill is a folder with a `SKILL.md` (frontmatter `name` + `description`) and supporting files
alongside it when needed. It's the standard format Claude Code, Codex, opencode and the like read.

## Installing

Two ways in. **Pick one per machine or project** — installing both leaves every skill twice, and
the model then sees two candidates for every trigger.

### Managed — read-only, updates when I ship

```
/plugin marketplace add RosaErick/skills
/plugin install skills@erick-skills
/plugin update skills          # pick up whatever I pushed since
```

Claude Code keeps its own checkout and reads the skills from there. Nothing lands in your project
and nothing is yours to edit — an update overwrites it. This is the option to want unless you
specifically need to change a skill.

### Vendored — editable, frozen

```bash
npx github:RosaErick/skills -c -t .              # every skill, copied into ./.claude/skills
npx github:RosaErick/skills -c -t . frontend     # or just one category
```

Real files, copied in, yours to hack on. They never see an update from here again; re-running with
`-f` overwrites your edits. Use it when a skill needs to become project-specific.

### From a clone

```bash
scripts/install.sh                     # symlink every category into ~/.claude/skills
scripts/install.sh frontend backend    # or just these
scripts/install.sh -t ../my-project    # into that project's .claude/skills
scripts/install.sh -c -t ../my-project # copy instead of link (same as the npx route)
scripts/install.sh -u                  # remove the links again
```

Symlinks, so there's one copy on disk and editing a linked skill edits this repo — that's the mode
for the machine where you maintain them. Links go in one skill at a time, because agents look for
`<target>/<skill>/SKILL.md` and linking a whole category would hide everything inside it. It never
overwrites a real folder already in the target, and `-u` only removes links pointing back here.

## Maintaining

```bash
python3 scripts/check.py           # validate, refresh the README counts and the plugin bundle
python3 scripts/check.py --check   # verify only, non-zero exit if something is off
```

It checks frontmatter, listing in the category README, dead links and repeated skills, then
rewrites the counts below and regenerates `skills/` — the flat folder the plugin ships, one symlink
per skill, since plugins expect `skills/<name>/SKILL.md` with no categories in between.

A new skill goes into whichever category fits. If none fits, create the folder, write its README,
add the row to the table below, and run `check.py`.

## Categories

| Folder | What's in it | Skills |
|---|---|---|
| [engineering](./engineering/README.md) | Code workflow: spec → tickets → implement → review, TDD, bug diagnosis, domain modeling | 18 |
| [frontend](./frontend/README.md) | React, Next.js, Tailwind, interface design, mobile, web performance, i18n | 17 |
| [backend](./backend/README.md) | APIs, Node, Python, Rust, databases, MCP | 7 |
| [infra](./infra/README.md) | Shell, server management, deployment | 4 |
| [quality](./quality/README.md) | Testing, review, debugging, linting, profiling | 8 |
| [security](./security/README.md) | Vulnerabilities and red teaming | 2 |
| [workflow](./workflow/README.md) | How the agent works: brainstorming, planning, architecture, multi-agent orchestration | 7 |
| [writing](./writing/README.md) | Copy, UX writing, documentation, SEO/GEO | 6 |
| [productivity](./productivity/README.md) | Non-code work: grilling, handoff, teaching, job search | 8 |
| **Total** | | **77** |

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
- `frontend/nextjs-best-practices` (principles) × `frontend/nextjs-app-router-patterns` (implementation playbook)
- `frontend/react-patterns` (general patterns) × `frontend/react-ui-patterns` (loading, error and empty states)

## Pending

[description-rework.md](./description-rework.md) — the skills whose `description` says what they
are but never when to use them, so the model can't reach them on its own. Queued, not started.
