# Description rework — worklist

`description` is the only thing that decides whether the model reaches a skill on its own. These
ones state what the skill *is* but never when to reach for it, so they only fire when named
explicitly. Rewriting them is the pending item; this file is the queue, not the plan.

## What a working description does

Names the topic, then the trigger — the words that show up in a real request, verbatim.

- `tdd` — "Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions 'red-green-refactor', or wants integration tests."
- `web-design-guidelines` — "Review UI code for Web Interface Guidelines compliance. Use when asked to 'review my UI', 'check accessibility', 'audit design'..."
- `fastify` — "...Use when building, configuring, or debugging a Fastify application — including defining routes... Trigger terms: Fastify, Node.js server, REST API, API routes, backend framework, fastify.config, server.ts, app.ts."

The recent additions (`fastify`, `node`, `nodejs-core`, `oauth`, `documentation`,
`linting-neostandard-eslint9`, `skill-optimizer`) already follow that shape — use them as the
in-repo reference while rewriting the rest.

Two rules worth settling before rewriting: overlapping skills need *disjoint* triggers, or the
model picks between them at random; and a skill you only ever invoke by name is better off
user-invoked (`disable-model-invocation: true`) than carrying a weak description.

## Excluded

The 14 user-invoked skills in `engineering/` and `productivity/` — they're reached by
typing their name, so trigger phrasing buys them nothing.

## Queue

### backend

- [ ] **api-patterns** (119 chars)
      `API design principles and decision-making. REST vs GraphQL vs tRPC selection, response formats, versioning, pagination.`
- [ ] **database-design** (118 chars)
      `Database design principles and decision-making. Schema design, indexing strategy, ORM selection, serverless databases.`
- [ ] **mcp-builder** (104 chars)
      `MCP (Model Context Protocol) server building principles. Tool design, resource patterns, best practices.`
- [ ] **nodejs-best-practices** (147 chars)
      `Node.js development principles and decision-making. Framework selection, async patterns, security, and architecture. Teaches thinking, not copying.`
- [ ] **python-patterns** (149 chars)
      `Python development principles and decision-making. Framework selection, async patterns, type hints, project structure. Teaches thinking, not copying.`

### frontend

- [ ] **frontend-dev-guidelines** (257 chars)
      `Opinionated frontend development standards for modern React + TypeScript applications. Covers Suspense-first data fetching, lazy loading, feature-based architecture, MUI v7 styling, TanStack Router, performance optimization, and strict TypeScript practices.`
- [ ] **frontend-mobile-development-component-scaffold** (200 chars)
      `You are a React component architecture expert specializing in scaffolding production-ready, accessible, and performant components. Generate complete component implementations with TypeScript, tests, s`
- [ ] **i18n-localization** (126 chars)
      `Internationalization and localization patterns. Detecting hardcoded strings, managing translations, locale files, RTL support.`
- [ ] **nextjs-best-practices** (82 chars)
      `Next.js App Router principles. Server Components, data fetching, routing patterns.`
- [ ] **react-patterns** (97 chars)
      `Modern React patterns and principles. Hooks, composition, performance, TypeScript best practices.`
- [ ] **tailwind-patterns** (115 chars)
      `Tailwind CSS v4 principles. CSS-first configuration, container queries, modern patterns, design token architecture.`
- [ ] **ui-ux-pro-max** (89 chars)
      `UI/UX design intelligence. 50 styles, 21 palettes, 50 font pairings, 20 charts, 9 stacks.`
- [ ] **web-performance-optimization** (147 chars)
      `Optimize website and web application performance including loading speed, Core Web Vitals, bundle size, caching strategies, and runtime performance`

### infra

- [ ] **deployment-procedures** (150 chars)
      `Production deployment principles and decision-making. Safe deployment workflows, rollback strategies, and verification. Teaches thinking, not scripts.`
- [ ] **powershell-windows** (80 chars)
      `PowerShell Windows patterns. Critical pitfalls, operator syntax, error handling.`
- [ ] **server-management** (145 chars)
      `Server management principles and decision-making. Process management, monitoring strategy, and scaling decisions. Teaches thinking, not commands.`

### productivity

- [ ] **career-ops** (95 chars)
      `AI job search command center -- evaluate offers, generate CVs, scan portals, track applications`

### quality

- [ ] **clean-code** (90 chars)
      `Pragmatic coding standards - concise, direct, no over-engineering, no unnecessary comments`
- [ ] **code-review-checklist** (75 chars)
      `Code review guidelines covering code quality, security, and best practices.`
- [ ] **performance-profiling** (85 chars)
      `Performance profiling principles. Measurement, analysis, and optimization techniques.`
- [ ] **tdd-workflow** (70 chars)
      `Test-Driven Development workflow principles. RED-GREEN-REFACTOR cycle.`
- [ ] **testing-patterns** (71 chars)
      `Testing patterns and principles. Unit, integration, mocking strategies.`
- [ ] **webapp-testing** (75 chars)
      `Web application testing principles. E2E, Playwright, deep audit strategies.`

### security

- [ ] **red-team-tactics** (95 chars)
      `Red team tactics principles based on MITRE ATT&CK. Attack phases, detection evasion, reporting.`
- [ ] **vulnerability-scanner** (123 chars)
      `Advanced vulnerability analysis principles. OWASP 2025, Supply Chain Security, attack surface mapping, risk prioritization.`

### workflow

- [ ] **app-builder** (168 chars)
      `Main application building orchestrator. Creates full-stack applications from natural language requests. Determines project type, selects tech stack, coordinates agents.`
- [ ] **behavioral-modes** (128 chars)
      `AI operational modes (brainstorm, implement, debug, review, teach, ship, orchestrate). Use to adapt behavior based on task type.`
- [ ] **brainstorming** (170 chars)
      `Socratic questioning protocol + user communication. MANDATORY for complex requests, new features, or unclear requirements. Includes progress reporting and error handling.`
- [ ] **intelligent-routing** (175 chars)
      `Automatic agent selection and intelligent task routing. Analyzes user requests and automatically selects the best specialist agent(s) without requiring explicit user mentions.`

### writing

- [ ] **documentation-master** (253 chars)
      `Master documentation skill: generates complete technical documentation (API, architecture, code, user), explains complex code with visual diagrams, creates READMEs, OpenAPI specs and contribution guides, and automates documentation pipelines with CI/CD.`
- [ ] **documentation-templates** (113 chars)
      `Documentation templates and structure guidelines. README, API docs, code comments, and AI-friendly documentation.`
- [ ] **geo-fundamentals** (83 chars)
      `Generative Engine Optimization for AI search engines (ChatGPT, Claude, Perplexity).`
- [ ] **seo-fundamentals** (76 chars)
      `SEO fundamentals, E-E-A-T, Core Web Vitals, and Google algorithm principles.`
- [ ] **ux-writing** (116 chars)
      `User Experience, guided interaction and UX Writing guidelines, grounded in the fundamentals of modern web usability.`

---

34 skills queued.
