---
source: original
name: nextjs-best-practices
description: "Implement or debug Next.js App Router boundaries, routing, data fetching, caching, and server mutations."

---

# Match the installed Next.js version

Read `package.json`, the lockfile and `next.config.*` before applying version-sensitive advice. Preserve the Pages Router when that is the affected application; App Router migration is separate work.

Keep server-only dependencies and secrets in server code. Use Client Components for browser APIs, local state and event handlers, placing the boundary as low as useful. Client components may still participate in server rendering; avoid browser globals during render.

Choose caching deliberately. Next.js 15 changed server `fetch` and GET Route Handler defaults to uncached; route prerendering and other caches are distinct. On Next.js 16, inspect whether Cache Components are enabled before using its cache directives and invalidation APIs. Do not apply a Next.js 14 caching table to newer projects.

Read [routing and data patterns](references/app-router.md) for loading/error boundaries, parallel routes, server actions and version-specific examples. Validate inputs and authorize server mutations where data is accessed. Prefer direct server-side data access over calling the application's own HTTP route solely to reach the same database.

Choose runtime from dependency and platform support. Node is an appropriate default for ordinary server dependencies; Edge is a specific deployment choice. Next.js 16 uses the `proxy` convention, whose runtime support differs from older middleware examples.

Check the changed route in the relevant production mode, including authentication and revalidation when involved. Run the configured build/types/tests, without expanding a small route fix into a framework migration.

Sources: [Next.js 15 upgrade guide](https://nextjs.org/docs/app/guides/upgrading/version-15), [Next.js 16 upgrade guide](https://nextjs.org/docs/app/guides/upgrading/version-16), checked 2026-09-07.
