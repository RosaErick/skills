# OpenAPI 3.1 Playbook

> Templates completos e patterns para criar especificações OpenAPI profissionais.

---

## Design Approaches

| Abordagem | Descrição | Melhor Para |
|-----------|-----------|-------------|
| **Design-First** | Escreva spec antes do código | APIs novas, contratos |
| **Code-First** | Gere spec a partir do código | APIs existentes |
| **Hybrid** | Anote código, gere spec | APIs em evolução |

---

## Template 1: Spec Completa (Design-First)

```yaml
openapi: 3.1.0
info:
  title: User Management API
  description: |
    API para gerenciamento de usuários e perfis.

    ## Autenticação
    Todos os endpoints requerem Bearer token.

    ## Rate Limiting
    - 1000 requests/minuto (tier standard)
    - 10000 requests/minuto (tier enterprise)
  version: 2.0.0
  contact:
    name: API Support
    email: api-support@example.com
    url: https://docs.example.com
  license:
    name: MIT
    url: https://opensource.org/licenses/MIT

servers:
  - url: https://api.example.com/v2
    description: Production
  - url: https://staging-api.example.com/v2
    description: Staging
  - url: http://localhost:3000/v2
    description: Local development

tags:
  - name: Users
    description: Operações de gerenciamento de usuários
  - name: Profiles
    description: Operações de perfil de usuário
  - name: Admin
    description: Operações administrativas

paths:
  /users:
    get:
      operationId: listUsers
      summary: Listar todos os usuários
      description: Retorna lista paginada de usuários com filtros opcionais.
      tags: [Users]
      parameters:
        - $ref: '#/components/parameters/PageParam'
        - $ref: '#/components/parameters/LimitParam'
        - name: status
          in: query
          description: Filtrar por status do usuário
          schema:
            $ref: '#/components/schemas/UserStatus'
        - name: search
          in: query
          description: Buscar por nome ou email
          schema:
            type: string
            minLength: 2
            maxLength: 100
      responses:
        '200':
          description: Resposta com sucesso
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserListResponse'
              examples:
                default:
                  $ref: '#/components/examples/UserListExample'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '429':
          $ref: '#/components/responses/RateLimited'
      security:
        - bearerAuth: []

    post:
      operationId: createUser
      summary: Criar novo usuário
      description: Cria uma nova conta de usuário e envia email de boas-vindas.
      tags: [Users]
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateUserRequest'
            examples:
              standard:
                summary: Usuário padrão
                value:
                  email: user@example.com
                  name: John Doe
                  role: user
              admin:
                summary: Usuário admin
                value:
                  email: admin@example.com
                  name: Admin User
                  role: admin
      responses:
        '201':
          description: Usuário criado com sucesso
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
          headers:
            Location:
              description: URL do usuário criado
              schema:
                type: string
                format: uri
        '400':
          $ref: '#/components/responses/BadRequest'
        '409':
          description: Email já existe
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      security:
        - bearerAuth: []

  /users/{userId}:
    parameters:
      - $ref: '#/components/parameters/UserIdParam'

    get:
      operationId: getUser
      summary: Buscar usuário por ID
      tags: [Users]
      responses:
        '200':
          description: Resposta com sucesso
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '404':
          $ref: '#/components/responses/NotFound'
      security:
        - bearerAuth: []

    patch:
      operationId: updateUser
      summary: Atualizar usuário
      tags: [Users]
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateUserRequest'
      responses:
        '200':
          description: Usuário atualizado
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '400':
          $ref: '#/components/responses/BadRequest'
        '404':
          $ref: '#/components/responses/NotFound'
      security:
        - bearerAuth: []

    delete:
      operationId: deleteUser
      summary: Deletar usuário
      tags: [Users, Admin]
      responses:
        '204':
          description: Usuário deletado
        '404':
          $ref: '#/components/responses/NotFound'
      security:
        - bearerAuth: []

components:
  schemas:
    User:
      type: object
      required: [id, email, name, status, createdAt]
      properties:
        id:
          type: string
          format: uuid
          readOnly: true
          description: Identificador único do usuário
        email:
          type: string
          format: email
          description: Endereço de email do usuário
        name:
          type: string
          minLength: 1
          maxLength: 100
          description: Nome de exibição do usuário
        status:
          $ref: '#/components/schemas/UserStatus'
        role:
          type: string
          enum: [user, moderator, admin]
          default: user
        avatar:
          type: string
          format: uri
          nullable: true
        metadata:
          type: object
          additionalProperties: true
          description: Metadados customizados
        createdAt:
          type: string
          format: date-time
          readOnly: true
        updatedAt:
          type: string
          format: date-time
          readOnly: true

    UserStatus:
      type: string
      enum: [active, inactive, suspended, pending]
      description: Status da conta do usuário

    CreateUserRequest:
      type: object
      required: [email, name]
      properties:
        email:
          type: string
          format: email
        name:
          type: string
          minLength: 1
          maxLength: 100
        role:
          type: string
          enum: [user, moderator, admin]
          default: user
        metadata:
          type: object
          additionalProperties: true

    UpdateUserRequest:
      type: object
      minProperties: 1
      properties:
        name:
          type: string
          minLength: 1
          maxLength: 100
        status:
          $ref: '#/components/schemas/UserStatus'
        role:
          type: string
          enum: [user, moderator, admin]
        metadata:
          type: object
          additionalProperties: true

    UserListResponse:
      type: object
      required: [data, pagination]
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/User'
        pagination:
          $ref: '#/components/schemas/Pagination'

    Pagination:
      type: object
      required: [page, limit, total, totalPages]
      properties:
        page:
          type: integer
          minimum: 1
        limit:
          type: integer
          minimum: 1
          maximum: 100
        total:
          type: integer
          minimum: 0
        totalPages:
          type: integer
          minimum: 0
        hasNext:
          type: boolean
        hasPrev:
          type: boolean

    Error:
      type: object
      required: [code, message]
      properties:
        code:
          type: string
          description: Código de erro para tratamento programático
        message:
          type: string
          description: Mensagem legível para humanos
        details:
          type: array
          items:
            type: object
            properties:
              field:
                type: string
              message:
                type: string
        requestId:
          type: string
          description: ID da request para suporte

  parameters:
    UserIdParam:
      name: userId
      in: path
      required: true
      description: ID do usuário
      schema:
        type: string
        format: uuid

    PageParam:
      name: page
      in: query
      description: Número da página (1-based)
      schema:
        type: integer
        minimum: 1
        default: 1

    LimitParam:
      name: limit
      in: query
      description: Itens por página
      schema:
        type: integer
        minimum: 1
        maximum: 100
        default: 20

  responses:
    BadRequest:
      description: Request inválida
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            code: VALIDATION_ERROR
            message: Parâmetros de request inválidos
            details:
              - field: email
                message: Deve ser um email válido

    Unauthorized:
      description: Autenticação necessária
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            code: UNAUTHORIZED
            message: Autenticação necessária

    NotFound:
      description: Recurso não encontrado
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            code: NOT_FOUND
            message: Usuário não encontrado

    RateLimited:
      description: Muitas requests
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
      headers:
        Retry-After:
          description: Segundos até o rate limit resetar
          schema:
            type: integer
        X-RateLimit-Limit:
          description: Limite de requests por janela
          schema:
            type: integer
        X-RateLimit-Remaining:
          description: Requests restantes na janela
          schema:
            type: integer

  examples:
    UserListExample:
      value:
        data:
          - id: "550e8400-e29b-41d4-a716-446655440000"
            email: "john@example.com"
            name: "John Doe"
            status: "active"
            role: "user"
            createdAt: "2024-01-15T10:30:00Z"
        pagination:
          page: 1
          limit: 20
          total: 1
          totalPages: 1
          hasNext: false
          hasPrev: false

  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: JWT token de /auth/login

    apiKey:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key para chamadas service-to-service

security:
  - bearerAuth: []
```

---

## Template 2: Code-First (Python FastAPI)

```python
from fastapi import FastAPI, HTTPException, Query, Path, Depends
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime
from uuid import UUID
from enum import Enum

app = FastAPI(
    title="User Management API",
    description="API para gerenciamento de usuários e perfis",
    version="2.0.0",
    openapi_tags=[
        {"name": "Users", "description": "Operações de usuário"},
        {"name": "Profiles", "description": "Operações de perfil"},
    ],
    servers=[
        {"url": "https://api.example.com/v2", "description": "Production"},
        {"url": "http://localhost:8000", "description": "Development"},
    ],
)

# Enums
class UserStatus(str, Enum):
    active = "active"
    inactive = "inactive"
    suspended = "suspended"
    pending = "pending"

class UserRole(str, Enum):
    user = "user"
    moderator = "moderator"
    admin = "admin"

# Models
class UserBase(BaseModel):
    email: EmailStr = Field(..., description="Email do usuário")
    name: str = Field(..., min_length=1, max_length=100, description="Nome de exibição")

class UserCreate(UserBase):
    role: UserRole = Field(default=UserRole.user)
    metadata: Optional[dict] = Field(default=None, description="Metadados customizados")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "user@example.com",
                    "name": "John Doe",
                    "role": "user"
                }
            ]
        }
    }

class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    status: Optional[UserStatus] = None
    role: Optional[UserRole] = None
    metadata: Optional[dict] = None

class User(UserBase):
    id: UUID = Field(..., description="Identificador único")
    status: UserStatus
    role: UserRole
    avatar: Optional[str] = Field(None, description="URL do avatar")
    metadata: Optional[dict] = None
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: Optional[datetime] = Field(None, alias="updatedAt")

    model_config = {"populate_by_name": True}

class Pagination(BaseModel):
    page: int = Field(..., ge=1)
    limit: int = Field(..., ge=1, le=100)
    total: int = Field(..., ge=0)
    total_pages: int = Field(..., ge=0, alias="totalPages")
    has_next: bool = Field(..., alias="hasNext")
    has_prev: bool = Field(..., alias="hasPrev")

class UserListResponse(BaseModel):
    data: List[User]
    pagination: Pagination

class ErrorDetail(BaseModel):
    field: str
    message: str

class ErrorResponse(BaseModel):
    code: str = Field(..., description="Código do erro")
    message: str = Field(..., description="Mensagem de erro")
    details: Optional[List[ErrorDetail]] = None
    request_id: Optional[str] = Field(None, alias="requestId")

# Endpoints
@app.get(
    "/users",
    response_model=UserListResponse,
    tags=["Users"],
    summary="Listar todos os usuários",
    description="Retorna lista paginada com filtros opcionais.",
    responses={
        400: {"model": ErrorResponse, "description": "Request inválida"},
        401: {"model": ErrorResponse, "description": "Não autorizado"},
    },
)
async def list_users(
    page: int = Query(1, ge=1, description="Número da página"),
    limit: int = Query(20, ge=1, le=100, description="Itens por página"),
    status: Optional[UserStatus] = Query(None, description="Filtrar por status"),
    search: Optional[str] = Query(None, min_length=2, max_length=100),
):
    """
    Lista usuários com paginação e filtros.

    - **page**: Número da página (1-based)
    - **limit**: Itens por página (máx 100)
    - **status**: Filtrar por status do usuário
    - **search**: Buscar por nome ou email
    """
    pass

@app.post(
    "/users",
    response_model=User,
    status_code=201,
    tags=["Users"],
    summary="Criar novo usuário",
    responses={
        400: {"model": ErrorResponse},
        409: {"model": ErrorResponse, "description": "Email já existe"},
    },
)
async def create_user(user: UserCreate):
    """Cria novo usuário e envia email de boas-vindas."""
    pass

@app.get(
    "/users/{user_id}",
    response_model=User,
    tags=["Users"],
    summary="Buscar usuário por ID",
    responses={404: {"model": ErrorResponse}},
)
async def get_user(user_id: UUID = Path(..., description="ID do usuário")):
    """Retorna um usuário específico pelo ID."""
    pass

@app.patch(
    "/users/{user_id}",
    response_model=User,
    tags=["Users"],
    summary="Atualizar usuário",
    responses={
        400: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
    },
)
async def update_user(
    user_id: UUID = Path(..., description="ID do usuário"),
    user: UserUpdate = ...,
):
    """Atualiza atributos do usuário."""
    pass

@app.delete(
    "/users/{user_id}",
    status_code=204,
    tags=["Users", "Admin"],
    summary="Deletar usuário",
    responses={404: {"model": ErrorResponse}},
)
async def delete_user(user_id: UUID = Path(..., description="ID do usuário")):
    """Deleta permanentemente um usuário."""
    pass

# Exportar spec OpenAPI
if __name__ == "__main__":
    import json
    print(json.dumps(app.openapi(), indent=2))
```

---

## Template 3: Code-First (TypeScript tsoa)

```typescript
import {
  Controller, Get, Post, Patch, Delete,
  Route, Path, Query, Body, Response,
  SuccessResponse, Tags, Security, Example,
} from "tsoa";

interface User {
  /** Identificador único */
  id: string;
  /** Email do usuário */
  email: string;
  /** Nome de exibição */
  name: string;
  status: UserStatus;
  role: UserRole;
  /** URL do avatar */
  avatar?: string;
  /** Metadados customizados */
  metadata?: Record<string, unknown>;
  createdAt: Date;
  updatedAt?: Date;
}

enum UserStatus {
  Active = "active",
  Inactive = "inactive",
  Suspended = "suspended",
  Pending = "pending",
}

enum UserRole {
  User = "user",
  Moderator = "moderator",
  Admin = "admin",
}

interface CreateUserRequest {
  email: string;
  name: string;
  role?: UserRole;
  metadata?: Record<string, unknown>;
}

interface UserListResponse {
  data: User[];
  pagination: Pagination;
}

interface ErrorResponse {
  code: string;
  message: string;
  details?: { field: string; message: string }[];
  requestId?: string;
}

@Route("users")
@Tags("Users")
export class UsersController extends Controller {
  /**
   * Lista usuários com paginação e filtros
   * @param page Número da página (1-based)
   * @param limit Itens por página (máx 100)
   * @param status Filtrar por status
   * @param search Buscar por nome ou email
   */
  @Get()
  @Security("bearerAuth")
  @Response<ErrorResponse>(401, "Não autorizado")
  @Response<ErrorResponse>(429, "Rate limited")
  public async listUsers(
    @Query() page: number = 1,
    @Query() limit: number = 20,
    @Query() status?: UserStatus,
    @Query() search?: string
  ): Promise<UserListResponse> { /* impl */ }

  @Post()
  @SuccessResponse(201, "Criado")
  @Security("bearerAuth")
  @Response<ErrorResponse>(400, "Request inválida")
  @Response<ErrorResponse>(409, "Email já existe")
  public async createUser(
    @Body() body: CreateUserRequest
  ): Promise<User> { /* impl */ }

  @Get("{userId}")
  @Security("bearerAuth")
  @Response<ErrorResponse>(404, "Não encontrado")
  public async getUser(
    @Path() userId: string
  ): Promise<User> { /* impl */ }
}
```

---

## GraphQL Schema Template

```graphql
type User {
  id: ID!
  email: String!
  name: String!
  status: UserStatus!
  role: UserRole!
  createdAt: DateTime!
  orders(first: Int = 20, after: String): OrderConnection!
  profile: UserProfile
}

# Paginação Relay-style
type OrderConnection {
  edges: [OrderEdge!]!
  pageInfo: PageInfo!
  totalCount: Int!
}

type OrderEdge {
  node: Order!
  cursor: String!
}

type PageInfo {
  hasNextPage: Boolean!
  hasPreviousPage: Boolean!
  startCursor: String
  endCursor: String
}

enum UserStatus { ACTIVE INACTIVE SUSPENDED PENDING }
enum UserRole { USER MODERATOR ADMIN }
scalar DateTime

type Query {
  user(id: ID!): User
  users(first: Int = 20, after: String, search: String): UserConnection!
}

type Mutation {
  createUser(input: CreateUserInput!): CreateUserPayload!
  updateUser(input: UpdateUserInput!): UpdateUserPayload!
  deleteUser(id: ID!): DeleteUserPayload!
}

input CreateUserInput {
  email: String!
  name: String!
  password: String!
}

type CreateUserPayload {
  user: User
  errors: [Error!]
}

type Error {
  field: String
  message: String!
}
```
