# Description rework — worklist

`description` is the only thing that decides whether the model reaches a skill on its own. These
ones state what the skill *is* but never when to reach for it, so they only fire when named
explicitly.

## What a working description does

Topic, then trigger — the words that show up in a real request, verbatim — then the boundary against
the neighbours that would otherwise match the same request.

- `react-patterns` — "Modern React (18/19) component, hook, state and TypeScript patterns… Use when writing or reviewing React components and hooks, deciding where state should live… Trigger terms: React component, custom hook, useState, useEffect…"
- `api-patterns` — "HTTP API design and contracts… Use when designing a new endpoint or API, reviewing an API contract before implementation… Trigger terms: API design, REST endpoint, status code, error response, pagination…"
- `tdd` — "Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions 'red-green-refactor', or wants integration tests."

The reworked five (`react-patterns`, `tailwind-patterns`, `api-patterns`, `python-patterns`,
`mcp-builder`) and the imported ones (`fastify`, `node`, `oauth`, `documentation`,
`linting-neostandard-eslint9`, `skill-optimizer`) are the in-repo reference for the shape.

Two rules settled while reworking those: overlapping skills need *disjoint* triggers and an explicit
"this belongs to X instead" line in the body; and a skill only ever invoked by name belongs in
user-invoked (`disable-model-invocation: true`) rather than carrying a weak description.

## Excluded

The 18 user-invoked skills in `engineering/`, `productivity/` and `workflow/` — they're
reached by typing their name, so trigger phrasing buys them nothing.

## Queue

### backend

- [ ] **database-design** (118 chars)
      `Database design principles and decision-making. Schema design, indexing strategy, ORM selection, serverless databases.`
- [ ] **nodejs-best-practices** (147 chars)
      `Node.js development principles and decision-making. Framework selection, async patterns, security, and architecture. Teaches thinking, not copying.`

### frontend

- [ ] **frontend-dev-guidelines** (257 chars)
      `Opinionated frontend development standards for modern React + TypeScript applications. Covers Suspense-first data fetching, lazy loading, feature-based architecture, MUI v7 styling, TanStack Router, performance optimization, and strict TypeScript practices.`
- [ ] **i18n-localization** (126 chars)
      `Internationalization and localization patterns. Detecting hardcoded strings, managing translations, locale files, RTL support.`
- [ ] **nextjs-best-practices** (82 chars)
      `Next.js App Router principles. Server Components, data fetching, routing patterns.`
- [ ] **ui-ux-pro-max** (89 chars)
      `UI/UX design intelligence. 50 styles, 21 palettes, 50 font pairings, 20 charts, 9 stacks.`
- [ ] **web-performance-optimization** (147 chars)
      `Optimize website and web application performance including loading speed, Core Web Vitals, bundle size, caching strategies, and runtime performance`

### infra

- [ ] **deployment-procedures** (150 chars)
      `Production deployment principles and decision-making. Safe deployment workflows, rollback strategies, and verification. Teaches thinking, not scripts.`
- [ ] **server-management** (145 chars)
      `Server management principles and decision-making. Process management, monitoring strategy, and scaling decisions. Teaches thinking, not commands.`

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

- [ ] **vulnerability-scanner** (123 chars)
      `Advanced vulnerability analysis principles. OWASP 2025, Supply Chain Security, attack surface mapping, risk prioritization.`

### workflow

- [ ] **brainstorming** (170 chars)
      `Socratic questioning protocol + user communication. MANDATORY for complex requests, new features, or unclear requirements. Includes progress reporting and error handling.`

### writing

- [ ] **geo-fundamentals** (83 chars)
      `Generative Engine Optimization for AI search engines (ChatGPT, Claude, Perplexity).`
- [ ] **seo-fundamentals** (76 chars)
      `SEO fundamentals, E-E-A-T, Core Web Vitals, and Google algorithm principles.`
- [ ] **ux-writing** (116 chars)
      `User Experience, guided interaction and UX Writing guidelines, grounded in the fundamentals of modern web usability.`

---

20 skills queued.
