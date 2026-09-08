# Token validation and authorization

Determine whether the resource server receives a JWT access token or an opaque token. Decoding either token or an ID token is not authorization to this API.

For JWT access tokens, configure a maintained verifier with the expected issuer, intended API audience and an allowed algorithm set. Obtain keys from the trusted issuer's documented JWKS location; do not follow a token-supplied URL blindly. Verify signature and the claim/time requirements of the issuer's access-token profile, including expiry, and allow only an explicit clock-skew tolerance. Audience can be a string or an array. Missing required claims fail validation.

Use bounded JWKS caching with rotation support. An unknown key can justify a controlled refresh; do not turn arbitrary key IDs into unbounded remote requests. Consider whether the application also needs current revocation or account-state evidence beyond local JWT validity.

For opaque tokens, use the provider's authenticated introspection endpoint and require `active: true`, the expected resource/scope and applicable expiry. Bound any cached result by token expiry and the revocation tolerance. An introspection failure must not be treated as an active token.

After validation, authorize the requested tenant/object/action. Return a generic authentication failure for invalid tokens and a suitable forbidden response for a known identity lacking permission. Never return raw tokens or verifier internals in errors. Test wrong issuer/audience, expiry, missing required claims, key rotation, inactive introspection and wrong-object access.

Sources: [JWT access-token profile](https://www.rfc-editor.org/rfc/rfc9068.html), [token introspection](https://www.rfc-editor.org/rfc/rfc7662.html).
