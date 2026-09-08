# SSR auth implementation checklist

1. Reuse environment naming from the app. Browser code receives the project URL and publishable key only. Keep privileged keys in server-only modules and avoid bypassing RLS for ordinary user requests.
2. Use `createBrowserClient` from `@supabase/ssr` for the browser utility. In the server utility, obtain the request cookie store (asynchronously on newer Next.js), then pass `getAll` and the framework-supported `setAll` implementation to `createServerClient`. Do not share a server client across requests.
3. Implement token refresh in `middleware.ts` for the applicable older Next.js version or `proxy.ts` for Next.js 16. Update request cookies so downstream server code sees refreshed credentials; propagate all cookie changes to the response. If creating a redirect or replacing a response, carry those changes forward. Use the official version-matched example rather than swallowing cookie-write errors in a layer expected to write them.
4. For a PKCE login/email callback, exchange the code using the server client and return the resulting cookies. Validate any return destination as an allowed local path; reject protocol-relative or foreign URLs. Never log codes or tokens.
5. At protected operations, check the verified identity and the operation's ownership/role requirements. Use `getUser` if current user state is required beyond token claims. JWT validation does not itself prove every current permission or revocation state.
6. Add RLS policies for relevant SELECT/INSERT/UPDATE/DELETE operations and verify another user's identifier cannot access the row. A successful login is not an RLS test.
7. Test fresh login, an expired access token with a valid refresh token, invalid refresh, anonymous access, two users, logout and callback redirect validation. Avoid shared caching of responses that set auth cookies or contain user-specific data.

Source: [Supabase SSR client creation](https://supabase.com/docs/guides/auth/server-side/creating-a-client?framework=nextjs), checked 2026-09-07. Follow its current code for the versions installed in the target app.
