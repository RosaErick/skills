# Organize by the established boundaries

Follow the application's feature and route layout. Keep related UI, queries and types discoverable without requiring every component to become a directory or every feature to expose a public barrel.

Export a deliberate public interface when callers need one. A barrel can make that interface clear, but can also complicate tree-shaking, cycles or server/client boundaries depending on the toolchain. Inspect actual imports and bundle behavior before adding or removing one globally.

Move code when responsibility or reuse supports it; avoid repository-wide reorganization during a scoped feature. Existing aliases and routes are the source of truth for example imports.
