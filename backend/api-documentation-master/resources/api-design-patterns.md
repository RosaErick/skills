# API Design Patterns

> Design and decision-making principles for modern APIs.
> **Learn to THINK, not to copy fixed patterns.**

---

## 🌳 Decision Tree: Which API Style?

```
Who are the API's consumers?
│
├── Public API / Multiple platforms
│   └── REST + OpenAPI (widest compatibility)
│
├── Complex data / Multiple frontends
│   └── GraphQL (flexible queries)
│
├── TypeScript frontend + backend (monorepo)
│   └── tRPC (end-to-end type safety)
│
├── Real-time / Event-driven
│   └── WebSocket + AsyncAPI
│
└── Internal microservices
    └── gRPC (performance) or REST (simplicity)
```

### Quick Comparison

| Factor | REST | GraphQL | tRPC |
|-------|------|---------|------|
| **Best for** | Public APIs | Complex apps | TS monorepos |
| **Learning curve** | Low | Medium | Low (if TS) |
| **Over/under fetching** | Common | Solved | Solved |
| **Type safety** | Manual (OpenAPI) | Schema-based | Automatic |
| **Caching** | Native HTTP | Complex | Client-based |

---

## REST Design Principles

### Resource Naming

```
Principles:
├── Use NOUNS, not verbs (resources, not actions)
├── Use PLURAL (/users, not /user)
├── Use lowercase with hyphens (/user-profiles)
├── Nest for relationships (/users/123/posts)
└── Keep it shallow (3 levels max)
```

### HTTP Methods

| Method | Purpose | Idempotent? | Body? |
|--------|-----------|-------------|-------|
| **GET** | Read resource(s) | Yes | No |
| **POST** | Create a new resource | No | Yes |
| **PUT** | Replace the whole resource | Yes | Yes |
| **PATCH** | Partial update | No | Yes |
| **DELETE** | Remove resource | Yes | No |

### Status Codes

| Situation | Code | When to use |
|----------|--------|-------------|
| Success (read) | 200 | Default response |
| Created | 201 | New resource created |
| No content | 204 | Success, nothing to return |
| Bad request | 400 | Malformed request |
| Unauthorized | 401 | Auth missing/invalid |
| Forbidden | 403 | Valid auth, no permission |
| Not found | 404 | Resource doesn't exist |
| Conflict | 409 | State conflict (duplicate) |
| Validation error | 422 | Valid syntax, invalid data |
| Rate limited | 429 | Too many requests |
| Server error | 500 | Internal failure |

### Resource Collection Pattern

```python
# ✅ Good: resource-oriented endpoints
GET    /api/users              # List users (paginated)
POST   /api/users              # Create user
GET    /api/users/{id}         # Fetch a specific user
PUT    /api/users/{id}         # Replace user
PATCH  /api/users/{id}         # Update user fields
DELETE /api/users/{id}         # Delete user

# Nested resources
GET    /api/users/{id}/orders  # The user's orders
POST   /api/users/{id}/orders  # Create an order for the user

# ❌ Bad: action-oriented endpoints (avoid)
POST   /api/createUser
POST   /api/getUserById
POST   /api/deleteUser
```

---

## Response Format

### Envelope Pattern

```json
{
  "success": true,
  "data": { ... },
  "error": null,
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 150,
    "totalPages": 8,
    "hasNext": true,
    "hasPrev": false
  }
}
```

### Error Response (standard)

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid email format",
    "details": [
      { "field": "email", "message": "Must be a valid email address" }
    ],
    "requestId": "req_abc123"
  }
}
```

> ⚠️ **Never expose** stack traces, internal paths or implementation details in error responses.

### Pagination Types

| Type | Best for | Trade-offs |
|------|------------|------------|
| **Offset** | Simple, jumpable | Poor performance on large datasets |
| **Cursor** | Large datasets | Can't jump to a specific page |
| **Keyset** | Performance-critical | Requires a sortable key |

---

## Versioning

| Strategy | Implementation | Trade-offs |
|-----------|--------------|------------|
| **URI** | /v1/users | Clear, easy caching |
| **Header** | Accept-Version: 1 | Clean URLs, hard to discover |
| **Query** | ?version=1 | Easy to add, confusing |
| **None** | Evolve carefully | Fine internally, risky in public |

```
Rule of thumb:
├── Public API? → Version in the URI
├── Internal only? → You may not need versions
├── GraphQL? → No versions (evolve the schema)
├── tRPC? → Types guarantee compatibility
```

---

## Authentication

| Pattern | Best for |
|---------|------------|
| **JWT** | Stateless, microservices |
| **Session** | Traditional web, simple |
| **OAuth 2.0** | Third-party integration |
| **API Keys** | Server-to-server, public APIs |
| **Passkey** | Modern passwordless (2025+) |

### JWT Best Practices

```
Rules:
├── Always verify the signature
├── Check expiration
├── Include minimal claims
├── Use short expiry + refresh tokens
└── Never store sensitive data in the JWT
```

---

## Rate Limiting

### Strategies

| Type | How | When |
|------|------|--------|
| **Token bucket** | Bursts allowed, refills over time | Most APIs |
| **Sliding window** | Even distribution | Strict limits |
| **Fixed window** | Simple per-window counters | Basic needs |

### Response Headers (mandatory)

```
Headers:
├── X-RateLimit-Limit (max requests)
├── X-RateLimit-Remaining (requests left)
├── X-RateLimit-Reset (when the limit resets)
└── Return 429 when exceeded + Retry-After header
```

---

## HATEOAS (Hypermedia)

```json
{
  "id": "usr_123",
  "name": "John Doe",
  "email": "john@example.com",
  "_links": {
    "self": { "href": "/api/users/usr_123" },
    "orders": { "href": "/api/users/usr_123/orders" },
    "update": { "href": "/api/users/usr_123", "method": "PATCH" },
    "delete": { "href": "/api/users/usr_123", "method": "DELETE" }
  }
}
```

---

## GraphQL Principles

### When to Use

```
✅ Good fit:
├── Complex, interconnected data
├── Multiple frontend platforms
├── Clients need flexible queries
├── Evolving data requirements
└── Cutting over-fetching matters

❌ Poor fit:
├── Simple CRUD operations
├── Heavy file uploads
├── HTTP caching matters
└── Team has no GraphQL experience
```

### Schema Design

```
Principles:
├── Think in graphs, not endpoints
├── Design for evolvability (no versions)
├── Use connections for pagination (Relay spec)
├── Be specific with types (no generic "data")
└── Handle nullability carefully
```

### Security

```
Protect against:
├── Query depth attacks → set a max depth
├── Query complexity → compute a cost per query
├── Batching abuse → limit batch size
├── Introspection → disable it in production
```

---

## tRPC Principles

### When to Use

```
✅ Perfect fit:
├── TypeScript on both sides
├── Monorepo
├── Internal tooling
├── Fast development
└── Type safety is critical

❌ Poor fit:
├── Non-TypeScript clients
├── Public API
├── You need REST conventions
└── Backends in multiple languages
```

---

## ❌ Anti-Patterns

**DON'T:**
- Default to REST for everything without evaluating
- Put verbs in REST endpoints (/getUsers, /deleteUser)
- Use inconsistent response formats
- Expose internal errors to clients
- Skip rate limiting
- Couple the API structure to the database schema

**DO:**
- Choose the API style based on context
- Ask about the clients' requirements
- Document thoroughly
- Use correct HTTP status codes
- Standardize error responses
