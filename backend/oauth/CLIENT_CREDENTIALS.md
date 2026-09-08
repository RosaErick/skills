# Client credentials

Use this grant for a confidential service acting on its own behalf, without a human user's delegated identity. Follow the provider's token endpoint authentication method; keep credentials in the established server secret store and request the narrow scopes/resource required.

Send `grant_type=client_credentials` to the token endpoint over TLS. Cache the access token only until shortly before expiry, deduplicate concurrent acquisition and reacquire when needed. Do not assume the grant returns a refresh token. Bound retries and redact request credentials and token responses.

The resource server must validate the token for its own audience and authorize the service's operation. A successful token request does not grant every tenant or resource permission. Test invalid client credentials, incorrect scope, expiry and provider failures with a safe fixture.

Source: [RFC 6749 client credentials](https://www.rfc-editor.org/rfc/rfc6749.html#section-4.4).
