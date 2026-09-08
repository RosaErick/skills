---
name: oauth
description: "Implement or debug OAuth flows, token validation, or protected Fastify routes with provider-specific checks."
metadata:
  tags: oauth, oauth2, security, authentication, authorization, jwt, fastify
---

# Implement the required OAuth boundary

Identify the client type, provider, grant, Fastify/plugin versions and authorization requirement. OAuth access delegation and OpenID Connect login are different contracts: do not treat an arbitrary access token as a verified user identity.

| Need | Read |
|---|---|
| Browser redirect and code exchange | [authorization code + PKCE](AUTHORIZATION_CODE.md), [runnable Fastify example](examples/authorization-code/README.md) |
| JWT or opaque access tokens | [token validation](TOKEN_VALIDATION.md) |
| Machine-to-machine credentials | [client credentials](CLIENT_CREDENTIALS.md) |
| Input-constrained device | [device flow](DEVICE_FLOW.md) |
| Native/mobile client | [mobile OAuth](MOBILE_OAUTH.md) |

Use the provider's registered redirect URI, approved scopes and supported secure flow. Bind the callback to the initiating browser, validate state, use PKCE S256 where supported, and prevent open redirects. Register actual cookie/session/token plugins before using their decorators. Keep tokens out of logs and browser-readable storage when a server session is the intended architecture.

At a resource server, verify token provenance and the API's required claims, then separately authorize the requested resource/action. Handle expiry, key rotation and provider errors without exposing token contents. Apply refresh rotation according to the provider contract and store replacements atomically.

Test the happy path and relevant rejection paths using a local provider fixture before claiming an integrated example works. Real-provider credentials and production deployment remain environment-specific. Consult the provider and applicable standards when their behavior differs from an example.
