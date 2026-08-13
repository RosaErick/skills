# skills

My curated agent skills — 79 of them, all in one place, organized by category.

Each skill is a folder with a `SKILL.md` (frontmatter `name` + `description`) and supporting files
alongside it when needed. It's the standard format agent hosts read — Codex, OpenCode, Claude Code, Copilot CLI and others.

## Install

Three routes. **Pick one per machine or project** — two of them leaves every skill twice, and the
model then sees two candidates for every trigger.

<details>
<summary><b>As a plugin</b> — read-only, namespaced, updates when I ship</summary>

The host keeps its own checkout and reads the skills from there. Nothing lands in your project and
nothing is yours to edit — an update overwrites it. Skills arrive namespaced as
`erickrosa-skills:<name>`, so it's obvious where they came from.

Both manifests (`.claude-plugin/`, `.codex-plugin/`) point at the same flat `skills/` folder, so
every host installs the identical set.

**Codex** — add the marketplace from the shell, then install from inside the TUI:

```bash
codex plugin marketplace add RosaErick/skills
codex
```

Then `/plugins`, select the `rosaerick` marketplace, install. Skills are invoked with `@name`. The
desktop app picks the same install up after a restart. Remove with
`codex plugin remove erickrosa-skills`.

**GitHub Copilot CLI** — same mechanism, from the shell or as slash commands:

```bash
copilot plugin marketplace add RosaErick/skills
copilot plugin install erickrosa-skills@rosaerick
```

**Claude Code** — two separate prompts; the install doesn't take in one:

```
/plugin marketplace add RosaErick/skills
/plugin install erickrosa-skills@rosaerick
```

Updating, on any of them, is the marketplace refresh followed by the plugin update — in Claude Code:

```
/plugin marketplace update rosaerick
/plugin update erickrosa-skills
```

</details>

<details>
<summary><b>From a clone</b> — symlinks, edits go straight back to the repo</summary>

For the machine where you maintain them: one copy on disk, and editing a linked skill edits this
repo. The script links skill by skill, because hosts look for `<target>/<skill>/SKILL.md` and linking
a whole category would hide everything inside it.

`-a` names the host, and there is no default — pass it, or name a directory with `-T`.

```bash
scripts/install.sh -a codex                     # ~/.codex/skills
scripts/install.sh -a opencode                  # ~/.config/opencode/skills
scripts/install.sh -a claude frontend backend   # only these categories
scripts/install.sh -a codex -t ../my-project    # that project's .codex/skills
scripts/install.sh -a agents -t ../my-project   # that project's .agents/skills
scripts/install.sh -T ~/.qwen/skills            # any directory you name
scripts/install.sh -a codex -u                  # remove the links again
```

| `-a` | Personal | Project (`-t`) |
|---|---|---|
| `codex` | `~/.codex/skills` | `<project>/.codex/skills` |
| `opencode` | `~/.config/opencode/skills` | `<project>/.opencode/skills` |
| `claude` | `~/.claude/skills` | `<project>/.claude/skills` |
| `agents` | — | `<project>/.agents/skills` — the shared folder several hosts read |

Anything not in that table — Qwen Code, Antigravity, a host I haven't tried — takes `-T` with its
skills directory. It never overwrites a real folder or someone else's link already in the target, and
`-u` only removes links pointing back here.

Skills installed this way arrive **without** the `erickrosa-skills:` prefix — indistinguishable from
any other personal skill.

</details>

<details>
<summary><b>Vendored</b> — copies you own, frozen at copy time</summary>

```bash
npx github:RosaErick/skills -c -a codex -t .            # copy into ./.codex/skills
npx github:RosaErick/skills -c -a claude -t .           # copy into ./.claude/skills
npx github:RosaErick/skills -c -a codex -t . frontend   # or just one category
```

Real files, copied in, yours to hack on. They never see an update from here again; re-running with
`-f` overwrites your edits. Use it when a skill needs to become project-specific.

</details>

## Categories

| Folder | What's in it | Skills |
|---|---|---|
| [engineering](./engineering/README.md) | Code workflow: spec → tickets → implement → review, TDD, bug diagnosis, domain modeling | 20 |
| [frontend](./frontend/README.md) | React, Next.js, Tailwind, interface design, mobile, web performance, i18n | 15 |
| [backend](./backend/README.md) | APIs, Node, Python, Rust, databases, MCP | 11 |
| [infra](./infra/README.md) | Shell, server management, deployment | 3 |
| [quality](./quality/README.md) | Testing, review, debugging, linting, profiling | 10 |
| [security](./security/README.md) | Vulnerability analysis and OWASP | 1 |
| [workflow](./workflow/README.md) | How the agent works: brainstorming, planning, architecture, multi-agent orchestration | 7 |
| [writing](./writing/README.md) | Copy, UX writing, documentation, SEO/GEO | 5 |
| [productivity](./productivity/README.md) | Non-code work: grilling, handoff, teaching, questionnaires | 7 |
| **Total** | | **79** |

The READMEs under `engineering/`, `productivity/` and `workflow/` split their skills into
**user-invoked** (only run when you type them, `disable-model-invocation: true`) and **model-invoked**
(the model reaches for them from the description). Everything in the other categories is
model-reachable.

<details>
<summary><b>Original skills</b> — the twelve that are mine to maintain</summary>

They carry `source: original` in their frontmatter, or `source: adapted` where the base came from
someone else's skill and I reworked it. Everything else here comes from the community — public skill
packs, vendor guides and open-source repos — kept because I use them, and curated: picked one by one,
filed by category, trimmed of what I don't run.

| Skill | What it does |
|---|---|
| [engineering/domain-design](./engineering/domain-design/SKILL.md) | Invariants, aggregates, value objects, domain events, bounded contexts and context mapping |
| [engineering/spec-driven](./engineering/spec-driven/SKILL.md) | Falsifiable acceptance criteria in the repo, bound to tests by id, verified against a test run |
| [frontend/nextjs-best-practices](./frontend/nextjs-best-practices/SKILL.md) | App Router defaults: Server Components, data fetching, routing |
| [frontend/react-patterns](./frontend/react-patterns/SKILL.md) | React 18/19: state placement, effects, composition, React Compiler, TypeScript props |
| [frontend/react-ui-patterns](./frontend/react-ui-patterns/SKILL.md) | Loading states, error handling and async data in components |
| [frontend/react-modernization](./frontend/react-modernization/SKILL.md) | Version upgrades, class-to-hooks migration, concurrent features, codemods |
| [frontend/web-performance-optimization](./frontend/web-performance-optimization/SKILL.md) | Core Web Vitals, bundle size, caching, runtime performance |
| [backend/api-patterns](./backend/api-patterns/SKILL.md) | API contracts: style, URLs, status codes, problem details, pagination, idempotency, versioning |
| [backend/python-patterns](./backend/python-patterns/SKILL.md) | Python 3.11+: uv and pyproject, typing, async, errors, pytest |
| [backend/api-documentation-master](./backend/api-documentation-master/SKILL.md) | API docs end to end: OpenAPI 3.1, interactive docs, multi-language samples, CI/CD automation |
| [writing/documentation](./writing/documentation/SKILL.md) | Diátaxis documentation plus README, API reference, ADR, changelog, diagrams, llms.txt |
| [writing/ux-writing](./writing/ux-writing/SKILL.md) | UX writing, guided interaction and interface usability |

</details>

<details>
<summary><b>Known overlaps</b> — kept on purpose, different depths of the same subject</summary>

- `engineering/domain-modeling` (the glossary) × `engineering/domain-design` (the model) × `engineering/codebase-design` (the module shape)
- `engineering/to-spec` (writes the spec) × `engineering/spec-driven` (makes it falsifiable and keeps it honest)
- `engineering/tdd` (guided loop, with references) × `quality/tdd-workflow` (short checklist)
- `engineering/two-axis-review` (Standards + Spec, sub-agents) × `quality/code-review-checklist` (fast pass)
- `engineering/diagnosing-bugs` (diagnosis loop) × `quality/systematic-debugging` (4 phases)
- `frontend/nextjs-best-practices` (principles) × `frontend/nextjs-app-router-patterns` (implementation playbook)
- `frontend/react-patterns` (general patterns) × `frontend/react-ui-patterns` (loading, error and empty states)
- `backend/node` (Node 22+ and native TypeScript) × `backend/nodejs-best-practices` (framework and architecture choices) × `backend/nodejs-core` (contributing to Node itself)
- `backend/api-patterns` (the contract) × `backend/fastify` (implementing it) × `backend/api-documentation-master` (publishing it) × `backend/mcp-builder` (exposing it to agents)
- `quality/lint-and-validate` (lint as a habit, any stack) × `quality/linting-neostandard-eslint9` (ESLint v9 setup and migration)

</details>

<details>
<summary><b>Maintaining</b> — the one script, and where a new skill goes</summary>

```bash
scripts/check.sh           # validate, and rebuild the plugin bundle if it drifted
scripts/check.sh --check   # verify only, non-zero exit if something is off
```

The skills are the source of truth; the script reads them and complains about everything that fell
out of step. It checks frontmatter (name present and matching the folder, description present),
whether each skill is listed in its category README, dead relative links in every README and skill
file, and repeated skills. It also regenerates `skills/` — the flat folder the plugin ships, one
symlink per skill, since plugins expect `skills/<name>/SKILL.md` with no categories in between.

A new skill goes into whichever category fits. If none fits, create the folder, write its README, add
the row to the categories table, and run `scripts/check.sh`.

Descriptions carry the whole activation surface, and the roster the model receives has a budget — go
long on every skill and the ones at the end of the alphabet arrive name-only. Keep each one to what
the skill is, when to reach for it, and the boundary against its neighbour.

</details>
