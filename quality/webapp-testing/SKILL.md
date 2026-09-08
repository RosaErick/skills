---
name: webapp-testing
description: "Create, debug, or run Playwright tests for specified web flows, or audit a defined browser surface."

---

# Match browser testing to the requested scope

Choose the mode from the request: configure Playwright, fix a failing test, verify named flows, or audit an agreed set of routes. A focused interaction check does not require crawling every route. For a full audit, enumerate the agreed surface and track what was covered and what remains.

Inspect existing tests, base URL, authentication fixtures and server lifecycle. Reuse project commands and browser tooling. If a helper is useful, inspect [playwright_runner.py](scripts/playwright_runner.py) and its options; do not assume it represents the whole application's test suite.

Prefer role/name, label and other user-facing locators. Use explicit test IDs when a stable semantic locator is unavailable. Scope ambiguous matches; avoid fragile DOM chains and arbitrary sleep delays. Use Playwright's actionability checks and web-first assertions rather than racing the application.

Test observable outcomes, including the significant error/empty/authorization states of the requested flow. Isolate data and sessions; use a local/test environment for side effects and respect authorization for external operations. Capture traces/screenshots when they explain failures.

Fix relevant test or app failures within scope, rerun the affected checks and report the flows exercised, environment and unresolved limitations. Passing one route does not establish complete coverage.

Source: [Playwright best practices](https://playwright.dev/docs/best-practices).
