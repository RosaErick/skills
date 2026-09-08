# App Router patterns

Use file conventions to express the route: `page.tsx` for a page, `layout.tsx` for shared UI, `loading.tsx` for a route loading boundary, `error.tsx` for a client error boundary and `not-found.tsx` for missing resources. Route groups organize without adding URL segments. Parallel slots and intercepting routes help with persistent panels or modal navigation; implement a conventional route when those behaviors are unnecessary.

Fetch independent data concurrently when doing so preserves authorization and avoids unnecessary work. Put a Suspense boundary around a slow section when streaming improves the page. A boundary cannot stream work already awaited above it. Handle empty results and upstream failures explicitly.

For Next.js 15+ examples, request cache behavior explicitly when freshness matters:

```ts
const response = await fetch(endpoint, { cache: 'no-store' });
if (!response.ok) throw new Error('Upstream request failed');
const data = await response.json();
```

Use `force-cache` or a supported revalidation configuration for deliberately shared data. Never place per-user results in a shared cache without an appropriate isolation strategy. Distinguish Data Cache, route output and client navigation state while investigating stale UI.

Dynamic request APIs and route parameters changed across versions. For Next.js 15/16, use the documented asynchronous forms of `cookies`, `headers` and `params`; check the installed version before applying an older synchronous example. In Next.js 16 with Cache Components, use the matching cache and invalidation API rather than mixing configurations from older guides.

Treat a Server Action or Route Handler as an externally reachable boundary: validate input, authenticate, authorize the operation and constrain returned fields. After mutation, invalidate only the affected data using the version's supported mechanism. Do not rely on hiding a button or redirecting a layout for authorization.

For modal or parallel routing, verify both client navigation and a direct/reloaded URL, plus browser back. For caching changes, test a production build with two distinct users if results are personalized.

Sources: [Next.js routing](https://nextjs.org/docs/app/getting-started/layouts-and-pages), [fetch API](https://nextjs.org/docs/app/api-reference/functions/fetch), [version 16 changes](https://nextjs.org/docs/app/guides/upgrading/version-16). This replaces the older Next.js 14 implementation playbook.
