---
name: node
description: "Build or debug Node.js application runtime behavior: async work, streams, modules, errors, shutdown, and profiling."
metadata:
  tags: node, nodejs, javascript, typescript, type-stripping, backend, server
---

# Node.js application decisions

Check the actual Node version, package manager, module format and build/test scripts. Preserve the established runtime and TypeScript toolchain unless a change is part of the task. This skill concerns applications; `nodejs-core` covers contributing to the Node runtime itself.

Read only the reference needed:

| Problem | Reference |
|---|---|
| TypeScript execution or module resolution | [TypeScript](rules/typescript.md), [modules](rules/modules.md) |
| Concurrency, cancellation or backpressure | [async work](rules/async-patterns.md), [streams](rules/streams.md) |
| Repeated expensive work | [caching](rules/caching.md) |
| Failure boundaries or diagnostics | [errors](rules/error-handling.md), [logging](rules/logging.md) |
| Process lifecycle | [shutdown](rules/graceful-shutdown.md), [stuck processes](rules/stuck-processes-and-tests.md) |
| Tests | [testing](rules/testing.md), [flaky tests](rules/flaky-tests.md) |
| CPU/memory/latency | [profiling](rules/profiling.md), [performance](rules/performance.md) |
| Configuration | [environment](rules/environment.md) |
| Service boundaries and deployment | [service architecture](rules/service-architecture.md) |
| Library implementation investigation | [node_modules exploration](rules/node-modules-exploration.md) |

Native type stripping is an option for compatible Node versions and erasable TypeScript syntax; it does not type-check or honor all tsconfig transformations. Do not replace a working build just because files end in `.ts`.

For large data flows, bound memory and concurrency and propagate failures. `pipeline` is often useful, but a Transform stream, async iterator or established parser may already fit the problem. CSV does not require an async generator or a cache by itself. Verify runtime behavior at the relevant boundary and use the existing project's checks.
