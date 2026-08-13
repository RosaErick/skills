# API Security & Testing

> Security and testing principles for API documentation.

---

## OWASP API Security Top 10

| Vulnerability | Test focus | Impact |
|----------------|---------------|---------|
| **API1: BOLA** | Accessing other users' resources | Critical |
| **API2: Broken Auth** | JWT, session, credentials | Critical |
| **API3: Property Auth** | Mass assignment, data exposure | High |
| **API4: Resource Consumption** | Rate limiting, DoS | High |
| **API5: Function Auth** | Admin endpoints, role bypass | Critical |
| **API6: Business Flow** | Logic abuse, automation | Medium |
| **API7: SSRF** | Internal network access | High |
| **API8: Misconfiguration** | Debug endpoints, CORS | Medium |
| **API9: Inventory** | Shadow APIs, old versions | Medium |
| **API10: Unsafe Consumption** | Trusting third-party APIs | Medium |

---

## Authentication Testing

### JWT Testing

| Check | What to test |
|------------|-------------|
| Algorithm | None, algorithm confusion |
| Secret | Weak secrets, brute force |
| Claims | Expiration, issuer, audience |
| Signature | Tampering, key injection |

### Session Testing

| Check | What to test |
|------------|-------------|
| Generation | Predictability |
| Storage | Client-side security |
| Expiration | Timeout enforcement |
| Invalidation | Logout effectiveness |

---

## Authorization Testing

| Test type | Approach |
|--------------|-----------|
| **Horizontal** | Access another user's data at the same level |
| **Vertical** | Access higher-privilege functions |
| **Context** | Access outside the permitted scope |

### BOLA/IDOR Testing

1. Identify resource IDs in the requests
2. Capture a request with user A's session
3. Replay it with user B's session
4. Check for unauthorized access

---

## Authentication Documentation Guide

When documenting authentication, always include:

### OAuth 2.0 Flow

```
1. Client → Authorization Server: Authorization Request
2. User: Consent & Login
3. Authorization Server → Client: Authorization Code
4. Client → Authorization Server: Code + Client Secret
5. Authorization Server → Client: Access Token + Refresh Token
6. Client → API: Request + Bearer Token
```

### API Key Management

```markdown
## API Keys

### Getting your API key

1. Go to the [Developer Portal](https://portal.example.com)
2. Navigate to Settings → API Keys
3. Click "Create New Key"
4. Copy the key and store it securely

### Using the API key

Include it in the header of every request:

```
X-API-Key: your_api_key_here
```

### Best practices

- ⚠️ Never expose keys in public code or repositories
- 🔄 Rotate keys regularly (every 90 days)
- 🔒 Use a different key per environment (dev, staging, prod)
- 📊 Monitor each key's usage in the dashboard
```

### JWT Token Documentation

```markdown
## JWT Tokens

### Token structure

```
Header.Payload.Signature
```

### Standard claims

| Claim | Description | Example |
|-------|-----------|---------|
| `sub` | Subject (user ID) | "usr_123" |
| `exp` | Expiration (timestamp) | 1706198400 |
| `iat` | Issued at | 1706194800 |
| `iss` | Issuer | "api.example.com" |
| `aud` | Audience | "example-app" |

### Refresh flow

```
1. Access token expires (status 401)
2. Client sends the refresh token to /auth/refresh
3. Server returns a new access token + new refresh token
4. Client uses the new access token
```
```

---

## Input Validation Testing

| Injection type | Test focus |
|------------------|---------------|
| SQL | Query manipulation |
| NoSQL | Document queries |
| Command | System commands |
| LDAP | Directory queries |

**Approach:** test every parameter, try type coercion, test boundaries, inspect error messages.

---

## Rate Limiting Testing

| Aspect | Check |
|---------|------------|
| Existence | Is there any limit at all? |
| Bypass | Headers, IP rotation |
| Scope | Per-user, per-IP, global |

**Bypass techniques:** X-Forwarded-For, different HTTP methods, case variations, API versioning.

---

## Rate Limiting Documentation Template

```markdown
## Rate Limiting

### Limits

| Tier | Requests/minute | Description |
|------|----------------|-----------|
| Free | 60 | Free account |
| Pro | 1000 | Professional account |
| Enterprise | 10000 | Contact us for custom limits |

### Response headers

Every response includes rate limiting headers:

| Header | Description |
|--------|-----------|
| `X-RateLimit-Limit` | Maximum requests allowed in the window |
| `X-RateLimit-Remaining` | Requests left in the current window |
| `X-RateLimit-Reset` | Unix timestamp of when the limit resets |
| `Retry-After` | Seconds to wait (429 responses only) |

### 429 response

```json
{
  "error": "RATE_LIMITED",
  "message": "Too many requests. Retry after 30 seconds.",
  "retryAfter": 30
}
```

### Retry strategy

```javascript
async function fetchWithRetry(url, options, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    const response = await fetch(url, options);

    if (response.status === 429) {
      const retryAfter = response.headers.get('Retry-After') || 30;
      await new Promise(r => setTimeout(r, retryAfter * 1000));
      continue;
    }

    return response;
  }
  throw new Error('Max retries exceeded');
}
```
```

---

## GraphQL Security

| Test | Focus |
|-------|------|
| Introspection | Schema exposure |
| Batching | Query DoS |
| Nesting | Depth-based DoS |
| Authorization | Field-level access |

---

## CORS Documentation Template

```markdown
## CORS (Cross-Origin Resource Sharing)

### Allowed origins

| Environment | Origin |
|----------|--------|
| Production | `https://app.example.com` |
| Staging | `https://staging.example.com` |
| Development | `http://localhost:3000` |

### CORS headers

```
Access-Control-Allow-Origin: https://app.example.com
Access-Control-Allow-Methods: GET, POST, PUT, PATCH, DELETE, OPTIONS
Access-Control-Allow-Headers: Authorization, Content-Type
Access-Control-Max-Age: 86400
```

### Troubleshooting

| Error | Cause | Fix |
|------|-------|---------|
| CORS blocked | Origin not allowed | Check your app's URL |
| Preflight failed | OPTIONS not answered | Check the server configuration |
| Credentials error | withCredentials mismatch | Align client and server settings |
```

---

## Security Documentation Checklist

**Authentication:**
- [ ] Auth method documented with examples
- [ ] Token lifecycle (obtain, use, refresh, revoke)
- [ ] Auth error handling

**Authorization:**
- [ ] Roles and permissions documented
- [ ] Scope defined for each endpoint
- [ ] Examples of access-denied responses

**Data security:**
- [ ] No secrets in code or docs
- [ ] HTTPS requirement documented
- [ ] Data retention policy

**Rate limiting:**
- [ ] Limits documented per tier
- [ ] Response headers documented
- [ ] Retry strategy with examples

**CORS:**
- [ ] Allowed origins documented
- [ ] Troubleshooting guide included
