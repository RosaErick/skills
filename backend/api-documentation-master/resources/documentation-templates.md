# Documentation Templates

> Templates profissionais para gerar documentação de API incrível.

---

## 1. Endpoint Documentation Template

Para **cada endpoint**, use este formato:

```markdown
## [METHOD] /path/to/resource

Descrição clara e concisa do que o endpoint faz.

**Endpoint:** `[METHOD] /api/v1/resource`

**Autenticação:** Required (Bearer token) | Optional | None

**Rate Limit:** 100 requests/minuto

### Parâmetros

#### Path Parameters
| Nome | Tipo | Obrigatório | Descrição |
|------|------|-------------|-----------|
| id | string (UUID) | Sim | ID do recurso |

#### Query Parameters
| Nome | Tipo | Obrigatório | Default | Descrição |
|------|------|-------------|---------|-----------|
| page | integer | Não | 1 | Número da página |
| limit | integer | Não | 20 | Itens por página (máx 100) |

#### Request Body
```json
{
  "email": "user@example.com",      // Obrigatório: Email válido
  "password": "SecurePass123!",     // Obrigatório: Mín 8 chars, 1 maiúscula, 1 número
  "name": "John Doe",               // Obrigatório: 2-50 caracteres
  "role": "user"                    // Opcional: "user" ou "admin" (default: "user")
}
```

### Respostas

#### Sucesso (201 Created)
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

#### Erros

- `400 Bad Request` — Dados de entrada inválidos
  ```json
  {
    "error": "VALIDATION_ERROR",
    "message": "Formato de email inválido",
    "field": "email"
  }
  ```

- `409 Conflict` — Email já existe
  ```json
  {
    "error": "EMAIL_EXISTS",
    "message": "Uma conta com este email já existe"
  }
  ```

- `401 Unauthorized` — Token de autenticação ausente ou inválido

### Exemplos

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
## Autenticação

Todas as requests da API requerem autenticação via Bearer tokens.

### Obtendo um Token

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

### Usando o Token

Inclua o token no header Authorization:

```
Authorization: Bearer YOUR_TOKEN
```

### Token Expirado

Tokens expiram após 1 hora. Use o refresh token para obter novo access token:

**Endpoint:** `POST /api/v1/auth/refresh`

**Request:**
```json
{
  "refreshToken": "refresh_token_here"
}
```

### Erros de Autenticação

| Código | Significado | Ação |
|--------|------------|------|
| 401 | Token ausente ou inválido | Faça login novamente |
| 403 | Sem permissão | Verifique sua role |
| 429 | Muitas tentativas | Aguarde e tente novamente |
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

### Pré-requisitos

- Python 3.8+ / Node.js 18+
- PostgreSQL 12+
- Redis 6+

### Instalação

```bash
git clone https://github.com/${ORG}/${REPO}.git
cd ${REPO}
pip install -e .  # ou npm install
```

### Primeiro Request

```python
import requests

response = requests.get(
    'https://api.example.com/api/v1/users',
    headers={'Authorization': f'Bearer {token}'}
)
print(response.json())
```

## Configuração

### Variáveis de Ambiente

| Variável | Descrição | Default | Obrigatório |
|----------|-----------|---------|-------------|
| DATABASE_URL | Connection string PostgreSQL | - | Sim |
| REDIS_URL | Connection string Redis | - | Sim |
| SECRET_KEY | Chave secreta da aplicação | - | Sim |
| PORT | Porta do servidor | 3000 | Não |

## Documentação

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

Todos os changes notáveis deste projeto serão documentados aqui.
Formato baseado em [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]
### Added
- Nova feature em desenvolvimento

## [2.0.0] - 2026-01-15
### ⚠️ Breaking Changes
- Removido endpoint `GET /api/v1/legacy-users`
- Campo `username` renomeado para `name`

### Added
- Paginação cursor-based para listagem de usuários
- Suporte a Passkey authentication

### Changed
- Rate limit aumentado para 1000 req/min

### Fixed
- Corrigido bug de timezone em `createdAt`

## [1.0.0] - 2025-06-01
### Added
- Release inicial da API
- CRUD de usuários
- Autenticação JWT
```

---

## 5. Architecture Decision Record (ADR)

```markdown
# ADR-001: [Título da Decisão]

## Status
Accepted | Deprecated | Superseded by ADR-XXX

## Context
Por que estamos tomando esta decisão? Qual problema estamos resolvendo?

## Decision
O que decidimos fazer? Descreva a abordagem escolhida.

## Consequences
Quais são os trade-offs? O que ganhamos e o que perdemos?

### Positivos
- Benefício 1
- Benefício 2

### Negativos
- Trade-off 1
- Trade-off 2
```

---

## 6. Code Examples Generator Pattern

Ao documentar endpoints, gere exemplos em múltiplas linguagens:

```python
def generate_code_examples(endpoint):
    """Gera code examples para API endpoints em múltiplas linguagens"""

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
> Descrição em uma linha.

## Core Files
- [src/index.ts]: Entry point principal
- [src/api/]: API routes
- [docs/]: Documentação

## Key Concepts
- Conceito 1: Explicação breve
- Conceito 2: Explicação breve
```

---

## Princípios de Estrutura

| Princípio | Por quê |
|-----------|---------|
| **Scannable** | Headers, listas, tabelas |
| **Exemplos primeiro** | Mostre, não apenas explique |
| **Detalhe progressivo** | Simple → Complexo |
| **Atualizado** | Desatualizado = enganoso |
| **Consistente** | Mesmo formato em toda a doc |

---

## ✅ Do This / ❌ Don't Do This

### ✅ Faça

- Use formato consistente para todos os endpoints
- Inclua exemplos funcionais em múltiplas linguagens
- Documente todos os códigos de erro possíveis
- Use dados de exemplo realistas (não "foo" e "bar")
- Explique cada parâmetro com tipos e constraints
- Versione sua API com números na URL (/api/v1/)
- Inclua timestamps de última atualização
- Link endpoints relacionados entre si
- Documente políticas de rate limiting
- Forneça Postman Collection ou OpenAPI spec

### ❌ Não Faça

- Não pule cenários de erro
- Não use descrições vagas ("Gets data")
- Não esqueça da autenticação
- Não ignore edge cases (paginação, filtros, ordenação)
- Não deixe exemplos quebrados
- Não use informação desatualizada
- Não overcomplicate — mantenha simples e scannable
- Não esqueça de response headers importantes
