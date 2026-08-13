# API Design Patterns

> Princípios de design e tomada de decisão para APIs modernas.
> **Aprenda a PENSAR, não copiar padrões fixos.**

---

## 🌳 Árvore de Decisão: Qual API Style?

```
Quem são os consumidores da API?
│
├── API Pública / Múltiplas plataformas
│   └── REST + OpenAPI (maior compatibilidade)
│
├── Dados complexos / Múltiplos frontends
│   └── GraphQL (queries flexíveis)
│
├── TypeScript frontend + backend (monorepo)
│   └── tRPC (type safety end-to-end)
│
├── Real-time / Event-driven
│   └── WebSocket + AsyncAPI
│
└── Microserviços internos
    └── gRPC (performance) ou REST (simplicidade)
```

### Comparação Rápida

| Fator | REST | GraphQL | tRPC |
|-------|------|---------|------|
| **Melhor para** | APIs públicas | Apps complexos | TS monorepos |
| **Curva de aprendizado** | Baixa | Média | Baixa (se TS) |
| **Over/under fetching** | Comum | Resolvido | Resolvido |
| **Type safety** | Manual (OpenAPI) | Schema-based | Automático |
| **Caching** | HTTP nativo | Complexo | Client-based |

---

## REST Design Principles

### Resource Naming

```
Princípios:
├── Use SUBSTANTIVOS, não verbos (resources, não actions)
├── Use PLURAL (/users não /user)
├── Use lowercase com hyphens (/user-profiles)
├── Aninhe para relacionamentos (/users/123/posts)
└── Mantenha shallow (máx 3 níveis)
```

### HTTP Methods

| Método | Propósito | Idempotente? | Body? |
|--------|-----------|-------------|-------|
| **GET** | Ler recurso(s) | Sim | Não |
| **POST** | Criar novo recurso | Não | Sim |
| **PUT** | Substituir recurso inteiro | Sim | Sim |
| **PATCH** | Atualização parcial | Não | Sim |
| **DELETE** | Remover recurso | Sim | Não |

### Status Codes

| Situação | Código | Quando Usar |
|----------|--------|-------------|
| Sucesso (leitura) | 200 | Resposta padrão |
| Criado | 201 | Novo recurso criado |
| Sem conteúdo | 204 | Sucesso, nada a retornar |
| Bad request | 400 | Request malformado |
| Não autorizado | 401 | Auth ausente/inválida |
| Proibido | 403 | Auth válida, sem permissão |
| Não encontrado | 404 | Recurso não existe |
| Conflito | 409 | Conflito de estado (duplicata) |
| Erro de validação | 422 | Sintaxe válida, dados inválidos |
| Rate limited | 429 | Muitas requests |
| Erro do servidor | 500 | Falha interna |

### Resource Collection Pattern

```python
# ✅ Bom: Endpoints orientados a recursos
GET    /api/users              # Listar users (com paginação)
POST   /api/users              # Criar user
GET    /api/users/{id}         # Buscar user específico
PUT    /api/users/{id}         # Substituir user
PATCH  /api/users/{id}         # Atualizar campos do user
DELETE /api/users/{id}         # Deletar user

# Nested resources
GET    /api/users/{id}/orders  # Orders do user
POST   /api/users/{id}/orders  # Criar order para user

# ❌ Ruim: Endpoints orientados a ações (evitar)
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

### Error Response (padrão)

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

> ⚠️ **Nunca exponha** stack traces, internal paths, ou detalhes de implementação em respostas de erro.

### Pagination Types

| Tipo | Melhor Para | Trade-offs |
|------|------------|------------|
| **Offset** | Simples, "jumpable" | Performance ruim em datasets grandes |
| **Cursor** | Datasets grandes | Não pode pular para página específica |
| **Keyset** | Performance crítica | Requer chave ordenável |

---

## Versionamento

| Estratégia | Implementação | Trade-offs |
|-----------|--------------|------------|
| **URI** | /v1/users | Claro, easy caching |
| **Header** | Accept-Version: 1 | URLs limpas, difícil descobrir |
| **Query** | ?version=1 | Fácil de adicionar, confuso |
| **Nenhum** | Evolua com cuidado | Melhor para interno, arriscado para público |

```
Regra prática:
├── API pública? → Version na URI
├── Somente interna? → Talvez não precise
├── GraphQL? → Sem versões (evolua o schema)
├── tRPC? → Types garantem compatibilidade
```

---

## Autenticação

| Pattern | Melhor Para |
|---------|------------|
| **JWT** | Stateless, microserviços |
| **Session** | Web tradicional, simples |
| **OAuth 2.0** | Integração com terceiros |
| **API Keys** | Server-to-server, APIs públicas |
| **Passkey** | Passwordless moderno (2025+) |

### JWT Best Practices

```
Regras:
├── Sempre verifique a assinatura
├── Cheque expiração
├── Inclua claims mínimas
├── Use expiry curto + refresh tokens
└── Nunca armazene dados sensíveis no JWT
```

---

## Rate Limiting

### Estratégias

| Tipo | Como | Quando |
|------|------|--------|
| **Token bucket** | Burst permitido, recarrega ao longo do tempo | Maioria das APIs |
| **Sliding window** | Distribuição uniforme | Limites estritos |
| **Fixed window** | Contadores simples por janela | Necessidades básicas |

### Response Headers (obrigatórios)

```
Headers:
├── X-RateLimit-Limit (requests máximas)
├── X-RateLimit-Remaining (requests restantes)
├── X-RateLimit-Reset (quando o limite reseta)
└── Return 429 quando excedido + Retry-After header
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

### Quando Usar

```
✅ Bom fit:
├── Dados complexos e interconectados
├── Múltiplas plataformas frontend
├── Clientes precisam de queries flexíveis
├── Requisitos de dados em evolução
└── Reduzir over-fetching importa

❌ Ruim fit:
├── Operações CRUD simples
├── Upload de arquivos pesado
├── HTTP caching importante
└── Time sem experiência em GraphQL
```

### Schema Design

```
Princípios:
├── Pense em graphs, não endpoints
├── Design para evoluibilidade (sem versões)
├── Use connections para paginação (Relay spec)
├── Seja específico com tipos (não use "data" genérico)
└── Trate nullability com cuidado
```

### Security

```
Proteja contra:
├── Query depth attacks → Set max depth
├── Query complexity → Calcule custo por query
├── Batching abuse → Limite batch size
├── Introspection → Desabilite em produção
```

---

## tRPC Principles

### Quando Usar

```
✅ Fit perfeito:
├── TypeScript em ambos os lados
├── Monorepo
├── Ferramentas internas
├── Desenvolvimento rápido
└── Type safety é crítico

❌ Ruim fit:
├── Clientes não-TypeScript
├── API pública
├── Precisa de convenções REST
└── Backends em múltiplas linguagens
```

---

## ❌ Anti-Patterns

**NÃO FAÇA:**
- Default REST para tudo sem avaliar
- Verbos em REST endpoints (/getUsers, /deleteUser)
- Formatos de resposta inconsistentes
- Expor erros internos para clientes
- Pular rate limiting
- Acoplar estrutura da API ao schema do banco

**FAÇA:**
- Escolha API style baseado no contexto
- Pergunte sobre requisitos dos clientes
- Documente minuciosamente
- Use status codes HTTP corretos
- Padronize respostas de erro
