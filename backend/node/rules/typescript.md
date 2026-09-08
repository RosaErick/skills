# Running TypeScript in Node

Read the pinned Node version and existing execution command. Native stripping removes erasable type syntax; it does not type-check, transform JSX, apply path aliases from tsconfig, or replace a library's distribution build. Features and default flags differ across Node releases.

Use native execution when the deployed version supports the required syntax and module format. Keep `tsx`, transpilation or another established tool when the application needs it. For native stripping, use explicit type-only imports and Node-compatible file extensions; avoid syntax needing code generation unless the selected runtime explicitly supports it.

Run the project's separate typecheck command where configured. A successfully executed `.ts` file is not evidence of type safety. Validate the same command and Node version used in deployment.

Source: [Node TypeScript documentation](https://nodejs.org/api/typescript.html), checked 2026-09-07; choose the documentation version matching the project.
