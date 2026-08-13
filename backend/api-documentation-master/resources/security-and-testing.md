# API Security & Testing

> Princípios de segurança e testes para documentação de APIs.

---

## OWASP API Security Top 10

| Vulnerabilidade | Foco do Teste | Impacto |
|----------------|---------------|---------|
| **API1: BOLA** | Acessar recursos de outros usuários | Crítico |
| **API2: Broken Auth** | JWT, session, credenciais | Crítico |
| **API3: Property Auth** | Mass assignment, exposição de dados | Alto |
| **API4: Resource Consumption** | Rate limiting, DoS | Alto |
| **API5: Function Auth** | Endpoints admin, bypass de role | Crítico |
| **API6: Business Flow** | Abuso de lógica, automação | Médio |
| **API7: SSRF** | Acesso à rede interna | Alto |
| **API8: Misconfiguration** | Debug endpoints, CORS | Médio |
| **API9: Inventory** | Shadow APIs, versões antigas | Médio |
| **API10: Unsafe Consumption** | Confiança em API de terceiros | Médio |

---

## Authentication Testing

### JWT Testing

| Verificação | O que Testar |
|------------|-------------|
| Algoritmo | None, confusão de algoritmo |
| Secret | Secrets fracos, brute force |
| Claims | Expiração, issuer, audience |
| Assinatura | Manipulação, key injection |

### Session Testing

| Verificação | O que Testar |
|------------|-------------|
| Geração | Previsibilidade |
| Storage | Segurança client-side |
| Expiração | Enforcement do timeout |
| Invalidação | Efetividade do logout |

---

## Authorization Testing

| Tipo de Teste | Abordagem |
|--------------|-----------|
| **Horizontal** | Acessar dados de outro user do mesmo nível |
| **Vertical** | Acessar funções de nível superior |
| **Contexto** | Acessar fora do scope permitido |

### BOLA/IDOR Testing

1. Identifique resource IDs nas requests
2. Capture request com sessão do user A
3. Replay com sessão do user B
4. Verifique acesso não autorizado

---

## Authentication Documentation Guide

Ao documentar autenticação, inclua sempre:

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

### Obtendo sua API Key

1. Acesse o [Developer Portal](https://portal.example.com)
2. Navegue até Settings → API Keys
3. Clique em "Create New Key"
4. Copie e armazene a key com segurança

### Usando a API Key

Inclua no header de cada request:

```
X-API-Key: your_api_key_here
```

### Boas Práticas

- ⚠️ Nunca exponha keys em código público ou repositórios
- 🔄 Rotacione keys regularmente (a cada 90 dias)
- 🔒 Use keys diferentes para cada ambiente (dev, staging, prod)
- 📊 Monitore o uso de cada key no dashboard
```

### JWT Token Documentation

```markdown
## JWT Tokens

### Estrutura do Token

```
Header.Payload.Signature
```

### Claims Padrão

| Claim | Descrição | Exemplo |
|-------|-----------|---------|
| `sub` | Subject (user ID) | "usr_123" |
| `exp` | Expiração (timestamp) | 1706198400 |
| `iat` | Issued at | 1706194800 |
| `iss` | Issuer | "api.example.com" |
| `aud` | Audience | "example-app" |

### Refresh Flow

```
1. Access token expira (status 401)
2. Client envia refresh token para /auth/refresh
3. Server retorna novo access token + novo refresh token
4. Client usa novo access token
```
```

---

## Input Validation Testing

| Tipo de Injection | Foco do Teste |
|------------------|---------------|
| SQL | Manipulação de query |
| NoSQL | Document queries |
| Command | Comandos do sistema |
| LDAP | Directory queries |

**Abordagem:** Teste todos os parâmetros, tente type coercion, teste boundaries, verifique mensagens de erro.

---

## Rate Limiting Testing

| Aspecto | Verificação |
|---------|------------|
| Existência | Existe algum limite? |
| Bypass | Headers, rotação de IP |
| Scope | Per-user, per-IP, global |

**Técnicas de bypass:** X-Forwarded-For, diferentes HTTP methods, variações de case, versioning de API.

---

## Rate Limiting Documentation Template

```markdown
## Rate Limiting

### Limites

| Tier | Requests/minuto | Descrição |
|------|----------------|-----------|
| Free | 60 | Conta gratuita |
| Pro | 1000 | Conta profissional |
| Enterprise | 10000 | Contato para customização |

### Headers de Resposta

Toda resposta inclui headers de rate limiting:

| Header | Descrição |
|--------|-----------|
| `X-RateLimit-Limit` | Limite máximo de requests na janela |
| `X-RateLimit-Remaining` | Requests restantes na janela atual |
| `X-RateLimit-Reset` | Unix timestamp de quando o limite reseta |
| `Retry-After` | Segundos para aguardar (apenas em 429) |

### Resposta 429

```json
{
  "error": "RATE_LIMITED",
  "message": "Too many requests. Retry after 30 seconds.",
  "retryAfter": 30
}
```

### Retry Strategy

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

| Teste | Foco |
|-------|------|
| Introspection | Exposição do schema |
| Batching | Query DoS |
| Nesting | Depth-based DoS |
| Authorization | Acesso field-level |

---

## CORS Documentation Template

```markdown
## CORS (Cross-Origin Resource Sharing)

### Origens Permitidas

| Ambiente | Origem |
|----------|--------|
| Production | `https://app.example.com` |
| Staging | `https://staging.example.com` |
| Development | `http://localhost:3000` |

### Headers CORS

```
Access-Control-Allow-Origin: https://app.example.com
Access-Control-Allow-Methods: GET, POST, PUT, PATCH, DELETE, OPTIONS
Access-Control-Allow-Headers: Authorization, Content-Type
Access-Control-Max-Age: 86400
```

### Troubleshooting

| Erro | Causa | Solução |
|------|-------|---------|
| CORS blocked | Origem não permitida | Verifique a URL do seu app |
| Preflight failed | OPTIONS não respondido | Verifique configuração do servidor |
| Credentials error | withCredentials mismatch | Alinhe client e server settings |
```

---

## Security Documentation Checklist

**Autenticação:**
- [ ] Método de auth documentado com exemplos
- [ ] Token lifecycle (obtenção, uso, refresh, revogação)
- [ ] Tratamento de erros de auth

**Autorização:**
- [ ] Roles e permissões documentados
- [ ] Escopo de cada endpoint definido
- [ ] Exemplos de respostas de acesso negado

**Segurança de Dados:**
- [ ] Nenhum secret no código ou docs
- [ ] HTTPS obrigatório documentado
- [ ] Política de data retention

**Rate Limiting:**
- [ ] Limites documentados por tier
- [ ] Headers de resposta documentados
- [ ] Retry strategy com exemplos

**CORS:**
- [ ] Origens permitidas documentadas
- [ ] Troubleshooting guide incluído
