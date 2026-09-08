---
name: nextjs-supabase-auth
description: "Integrate Supabase authentication with Next.js server rendering, cookie refresh, protected data, and RLS."
source: vibeship-spawner-skills (Apache 2.0)
---

# Connect SSR authentication end to end

Inspect the installed Next.js, `@supabase/ssr` and `@supabase/supabase-js` versions and existing clients. Use the current [Supabase SSR guide](https://supabase.com/docs/guides/auth/server-side/creating-a-client?framework=nextjs) for the matching framework and [local integration checklist](references/ssr-auth.md) for implementation decisions.

Create a browser client for Client Components and a per-request server client for server code. Configure cookies through the supported `getAll`/`setAll` adapter. Server Components cannot persist refreshed cookies themselves; use the version-appropriate middleware or Proxy layer and preserve its cookie changes on the response actually returned.

Verify identity server-side with `getClaims()` when supported, or `getUser()` when a fresh server user record is needed. Do not authorize from the user object in an unverified `getSession()` result. Handle sign-in callbacks, expiry and sign-out as part of the same cookie lifecycle.

Authorize each server action/data operation and enforce Row Level Security for user-scoped database access. Never expose secret/service-role keys to the browser. Public/publishable keys rely on properly configured policies, not secrecy. Page redirects and hidden UI are not data authorization.

Verify anonymous, authenticated and wrong-user access, token refresh, redirects and logout. Use local Supabase or an authorized test project; report what was actually exercised. Keep private responses out of shared caches.
