# Version-aware React migration

Read the upgrade guide for the exact transition. Check framework support and peer dependencies before changing React alone. Keep `react` and `react-dom` versions compatible and update types/test tooling as needed.

For older roots, inspect legacy `ReactDOM.render` and hydration APIs. A root migration can change batching and timing assumptions, so test affected integrations. For React 19, review removed APIs, the modern JSX transform requirement, ref callback cleanup behavior, error reporting and TypeScript changes in the official guide. React 18.3 can expose additional warnings before a React 19 migration; it is an optional preparatory step when appropriate.

Search for usage of an affected API, run the relevant official codemod in a cleanly scoped diff, then inspect semantics. Codemods cannot decide product behavior or guarantee third-party compatibility. Avoid refactoring unrelated state management while resolving version-specific failures.

Test effects with cleanup, external subscriptions, forms, focus, hydration and error boundaries where affected. Reuse regression tests that capture current behavior; add a focused test when the migration reveals a real regression risk. Validate a production build, not only the development server.

Source: [React 19 upgrade guide](https://react.dev/blog/2024/04/25/react-19-upgrade-guide). For another target, use its own release/upgrade documentation and record the version checked.
