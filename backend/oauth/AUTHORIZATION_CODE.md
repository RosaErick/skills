# Authorization code with PKCE in Fastify

Use an exact registered redirect URI and the provider's documented authorization/token endpoints. For a web server, keep client credentials and tokens server-side. A public client cannot safely hold a client secret. Use PKCE S256 and a random state bound to the initiating session; consume that state when processing a callback.

Register `@fastify/cookie` before `@fastify/session` and `@fastify/oauth2`. The callback should call `getAccessTokenFromAuthorizationCodeFlow(request, reply)` so PKCE cookie cleanup can occur. Rotate the application session after establishing the connection. Use secure, HttpOnly, appropriately SameSite-scoped cookies and host-prefixed cookie names for HTTPS deployments. An OAuth connection grants access to a resource; use the provider's OIDC flow and ID-token validation when a verified login identity is required.

The [example](examples/authorization-code/README.md) pins Fastify 5.12.3, OAuth2 8.3.0, cookie/session 11.1.2. It tests a local provider and keeps token responses off the browser. It is a connection example, not a complete OIDC identity implementation.

For refresh, use the installed plugin's `getNewAccessTokenUsingRefreshToken` API with the current token object. Replace a rotated refresh token atomically, serialize concurrent refreshes and handle revoked/expired credentials by requiring reconnection. The example deliberately exercises code exchange; add provider-specific refresh and revocation only when integrating those capabilities.

Sources: [Fastify OAuth2 plugin](https://github.com/fastify/fastify-oauth2), [OAuth security best current practice](https://www.rfc-editor.org/rfc/rfc9700.html).
