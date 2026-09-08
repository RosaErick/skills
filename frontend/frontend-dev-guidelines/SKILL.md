---
name: frontend-dev-guidelines
description: "Apply an existing React, MUI and TanStack frontend’s component, data, routing, and styling conventions."
---

# Work within this frontend stack

Use this guide for projects already using these conventions or explicitly adopting them. Inspect package versions, neighboring components, routing and styling first; it is not a reason to migrate another stack to MUI or TanStack.

Choose the relevant resource: [components](resources/component-patterns.md), [data fetching](resources/data-fetching.md), [loading/errors](resources/loading-and-error-states.md), [routing](resources/routing-guide.md), [styling](resources/styling-guide.md), [TypeScript](resources/typescript-standards.md), [organization](resources/file-organization.md), [performance](resources/performance.md), [common patterns](resources/common-patterns.md) or [examples](resources/complete-examples.md).

Keep components and data ownership clear. Use the project's established query mode: Suspense boundaries for suspense queries, explicit pending/error/data states for ordinary queries. A background refresh should not unnecessarily replace usable data.

Follow existing exports and component typing. `React.FC`, public barrel files and `useCallback` are choices, not universal requirements. Memoization should solve an observed identity or performance problem and account for any enabled React Compiler.

Implement the requested change, verify relevant interactions and accessibility, and run configured checks. A numeric complexity score or a separate approval checkpoint is not required before coding.
