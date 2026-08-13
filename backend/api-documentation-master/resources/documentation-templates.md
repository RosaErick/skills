# Documentation Templates

> Professional templates for generating outstanding API documentation.

---

## 1. Endpoint Documentation Template

For **each endpoint**, use this format:

```markdown
## [METHOD] /path/to/resource

Clear, concise description of what the endpoint does.

**Endpoint:** `[METHOD] /api/v1/resource`

**Authentication:** Required (Bearer token) | Optional | None

**Rate limit:** 100 requests/minute

### Parameters

#### Path Parameters
| Name | Type | Required | Description |
|------|------|-------------|-----------|
| id | string (UUID) | Yes | Resource ID |

#### Query Parameters
| Name | Type | Required | Default | Description |
|------|------|-------------|---------|-----------|
| page | integer | No | 1 | Page number |
| limit | integer | No | 20 | Items per page (max 100) |

#### Request Body
```json
{
  "email": "user@example.com",      // Required: valid email
  "password": "SecurePass123!",     // Required: min 8 chars, 1 uppercase, 1 number
  "name": "John Doe",               // Required: 2-50 characters
  "role": "user"                    // Optional: "user" or "admin" (default: "user")
}
```

### Responses

#### Success (201 Created)
```json
{
  "id": "usr_1234567890",
  "email": "user@example.com",
  "name": "John Doe",
  "role": "user",
  "createdAt": "2026-01-20T10:30:00Z",
  "emailVerified": false
}
```

#### Errors

- `400 Bad Request` — Invalid input data
  ```json
  {
    "error": "VALIDATION_ERROR",
    "message": "Invalid email format",
    "field": "email"
  }
  ```

- `409 Conflict` — Email already exists
  ```json
  {
    "error": "EMAIL_EXISTS",
    "message": "An account with this email already exists"
  }
  ```

- `401 Unauthorized` — Authentication token missing or invalid

### Examples

**cURL:**
```bash
curl -X POST https://api.example.com/api/v1/users \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "SecurePass123!",
    "name": "John Doe"
  }'
```

**JavaScript (fetch):**
```javascript
const response = await fetch('https://api.example.com/api/v1/users', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    email: 'user@example.com',
    password: 'SecurePass123!',
    name: 'John Doe'
  })
});

const user = await response.json();
```

**Python (requests):**
```python
import requests

response = requests.post(
    'https://api.example.com/api/v1/users',
    headers={
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    },
    json={
        'email': 'user@example.com',
        'password': 'SecurePass123!',
        'name': 'John Doe'
    }
)

user = response.json()
```
```

---

## 2. Authentication Documentation Template

```markdown
## Authentication

Every API request requires authentication via Bearer tokens.

### Getting a token

**Endpoint:** `POST /api/v1/auth/login`

**Request:**
```json
{
  "email": "user@example.com",
  "password": "your-password"
}
```

**Response:**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expiresIn": 3600,
  "refreshToken": "refresh_token_here"
}
```

### Using the token

Include the token in the Authorization header:

```
Authorization: Bearer YOUR_TOKEN
```

### Expired token

Tokens expire after 1 hour. Use the refresh token to get a new access token:

**Endpoint:** `POST /api/v1/auth/refresh`

**Request:**
```json
{
  "refreshToken": "refresh_token_here"
}
```

### Authentication errors

| Code | Meaning | Action |
|--------|------------|------|
| 401 | Token missing or invalid | Log in again |
| 403 | No permission | Check your role |
| 429 | Too many attempts | Wait and retry |
```

---

## 3. README Template

```markdown
# ${PROJECT_NAME}

${BADGES}

${SHORT_DESCRIPTION}

## Features

${FEATURES_LIST}

## Quick Start

### Prerequisites

- Python 3.8+ / Node.js 18+
- PostgreSQL 12+
- Redis 6+

### Installation

```bash
git clone https://github.com/${ORG}/${REPO}.git
cd ${REPO}
pip install -e .  # or npm install
```

### First request

```python
import requests

response = requests.get(
    'https://api.example.com/api/v1/users',
    headers={'Authorization': f'Bearer {token}'}
)
print(response.json())
```

## Configuration

### Environment variables

| Variable | Description | Default | Required |
|----------|-----------|---------|-------------|
| DATABASE_URL | PostgreSQL connection string | - | Yes |
| REDIS_URL | Redis connection string | - | Yes |
| SECRET_KEY | Application secret key | - | Yes |
| PORT | Server port | 3000 | No |

## Documentation

- [API Reference](./docs/api.md)
- [Architecture](./docs/architecture.md)
- [Contributing](./CONTRIBUTING.md)

## License

MIT
```

---

## 4. Changelog Template (Keep a Changelog)

```markdown
# Changelog

All notable changes to this project will be documented here.
Format based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]
### Added
- New feature in development

## [2.0.0] - 2026-01-15
### ⚠️ Breaking Changes
- Removed the `GET /api/v1/legacy-users` endpoint
- Field `username` renamed to `name`

### Added
- Cursor-based pagination for user listing
- Passkey authentication support

### Changed
- Rate limit raised to 1000 req/min

### Fixed
- Fixed a timezone bug in `createdAt`

## [1.0.0] - 2025-06-01
### Added
- Initial API release
- User CRUD
- JWT authentication
```

---

## 5. Architecture Decision Record (ADR)

```markdown
# ADR-001: [Decision title]

## Status
Accepted | Deprecated | Superseded by ADR-XXX

## Context
Why are we making this decision? What problem are we solving?

## Decision
What did we decide to do? Describe the chosen approach.

## Consequences
What are the trade-offs? What do we gain and what do we lose?

### Positive
- Benefit 1
- Benefit 2

### Negative
- Trade-off 1
- Trade-off 2
```

---

## 6. Code Examples Generator Pattern

When documenting endpoints, generate examples in multiple languages:

```python
def generate_code_examples(endpoint):
    """Generates code examples for API endpoints in multiple languages"""

    # Python
    python = f'''
import requests

url = "https://api.example.com{endpoint['path']}"
headers = {{"Authorization": "Bearer YOUR_API_KEY"}}

response = requests.{endpoint['method'].lower()}(url, headers=headers)
print(response.json())
'''

    # JavaScript
    javascript = f'''
const response = await fetch('https://api.example.com{endpoint['path']}', {{
    method: '{endpoint['method']}',
    headers: {{'Authorization': 'Bearer YOUR_API_KEY'}}
}});

const data = await response.json();
console.log(data);
'''

    # cURL
    curl = f'''
curl -X {endpoint['method']} https://api.example.com{endpoint['path']} \\
    -H "Authorization: Bearer YOUR_API_KEY"
'''

    return {"python": python, "javascript": javascript, "curl": curl}
```

---

## 7. CI/CD Documentation Pipeline

```yaml
name: Generate Documentation

on:
  push:
    branches: [main]
    paths:
      - 'src/**'
      - 'api/**'

jobs:
  generate-docs:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: |
        pip install -r requirements-docs.txt
        npm install -g @redocly/cli

    - name: Generate API documentation
      run: |
        python scripts/generate_openapi.py > docs/api/openapi.json
        redocly build-docs docs/api/openapi.json -o docs/api/index.html

    - name: Generate code documentation
      run: sphinx-build -b html docs/source docs/build

    - name: Deploy to GitHub Pages
      uses: peaceiris/actions-gh-pages@v4
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./docs/build
```

---

## 8. Swagger UI Setup

```html
<!DOCTYPE html>
<html>
<head>
    <title>API Documentation</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@latest/swagger-ui.css">
</head>
<body>
    <div id="swagger-ui"></div>

    <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@latest/swagger-ui-bundle.js"></script>
    <script>
        window.onload = function() {
            SwaggerUIBundle({
                url: "/api/openapi.json",
                dom_id: '#swagger-ui',
                deepLinking: true,
                presets: [SwaggerUIBundle.presets.apis],
                layout: "StandaloneLayout"
            });
        }
    </script>
</body>
</html>
```

---

## 9. AI-Friendly Documentation (llms.txt)

```markdown
# Project Name
> One-line description.

## Core Files
- [src/index.ts]: Main entry point
- [src/api/]: API routes
- [docs/]: Documentation

## Key Concepts
- Concept 1: brief explanation
- Concept 2: brief explanation
```

---

## Structural Principles

| Principle | Why |
|-----------|---------|
| **Scannable** | Headers, lists, tables |
| **Examples first** | Show, don't just explain |
| **Progressive detail** | Simple → complex |
| **Up to date** | Stale = misleading |
| **Consistent** | Same format throughout the docs |

---

## ✅ Do This / ❌ Don't Do This

### ✅ Do

- Use a consistent format for every endpoint
- Include working examples in multiple languages
- Document every possible error code
- Use realistic sample data (not "foo" and "bar")
- Explain each parameter with types and constraints
- Version your API with numbers in the URL (/api/v1/)
- Include last-updated timestamps
- Link related endpoints to each other
- Document rate limiting policies
- Provide a Postman collection or OpenAPI spec

### ❌ Don't

- Don't skip error scenarios
- Don't use vague descriptions ("Gets data")
- Don't forget authentication
- Don't ignore edge cases (pagination, filters, sorting)
- Don't leave broken examples
- Don't publish outdated information
- Don't overcomplicate — keep it simple and scannable
- Don't forget important response headers
