# Fastify authorization-code + PKCE example

A server-side OAuth resource connection using pinned Fastify 5.12.3, `@fastify/oauth2` 8.3.0 and cookie/session 11.1.2. Requires Node 22+. It stores the access token in a server session and returns selected resource fields, never the token.

```bash
npm ci
npm test
```

Tests use a local token/resource server, with no real accounts or credentials. They cover PKCE exchange, session rotation, protected-resource access, invalid state, callbacks from a different session, missing verifier, replay and disconnect origin checks.

`server.mjs` is a loopback development entrypoint. Set `PROVIDER_URL`, `CLIENT_ID`, `CLIENT_SECRET`, `SESSION_SECRET` (at least 32 random characters) and the exact registered `CALLBACK_URI`, then run `npm start`. Navigate to `/connect`. Use development credentials and an appropriate local/test provider. The automated fixture creates its own provider; it is not a public identity service.

For production integration, call `buildApp` with HTTPS URLs and a persistent `sessionStore` compatible with `@fastify/session`. The default memory store is only for explicit local development. Integrate the host's TLS, logging/redaction, resource policy, refresh and revocation lifecycle. Disconnect clears the local session; it does not claim to revoke the provider grant.

This is OAuth delegation, not an OpenID Connect login implementation or a general JWT resource server. Use the corresponding skill references for those contracts.
