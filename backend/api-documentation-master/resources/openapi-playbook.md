# OpenAPI 3.1 Playbook

> Complete templates and patterns for creating professional OpenAPI specifications.

---

## Design Approaches

| Approach | Description | Best for |
|-----------|-----------|-------------|
| **Design-First** | Write the spec before the code | New APIs, contracts |
| **Code-First** | Generate the spec from the code | Existing APIs |
| **Hybrid** | Annotate the code, generate the spec | Evolving APIs |

---

## Template 1: Spec Completa (Design-First)

```yaml
openapi: 3.1.0
info:
  title: User Management API
  description: |
    API for managing users and profiles.

    ## Authentication
    All endpoints require a Bearer token.

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
    description: User management operations
  - name: Profiles
    description: User profile operations
  - name: Admin
    description: Administrative operations

paths:
  /users:
    get:
      operationId: listUsers
      summary: List all users
      description: Returns a paginated list of users with optional filters.
      tags: [Users]
      parameters:
        - $ref: '#/components/parameters/PageParam'
        - $ref: '#/components/parameters/LimitParam'
        - name: status
          in: query
          description: Filter by user status
          schema:
            $ref: '#/components/schemas/UserStatus'
        - name: search
          in: query
          description: Search by name or email
          schema:
            type: string
            minLength: 2
            maxLength: 100
      responses:
        '200':
          description: Successful response
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
      summary: Create a new user
      description: Creates a new user account and sends a welcome email.
      tags: [Users]
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateUserRequest'
            examples:
              standard:
                summary: Standard user
                value:
                  email: user@example.com
                  name: John Doe
                  role: user
              admin:
                summary: Admin user
                value:
                  email: admin@example.com
                  name: Admin User
                  role: admin
      responses:
        '201':
          description: User created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
          headers:
            Location:
              description: URL of the created user
              schema:
                type: string
                format: uri
        '400':
          $ref: '#/components/responses/BadRequest'
        '409':
          description: Email already exists
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
      summary: Fetch user by ID
      tags: [Users]
      responses:
        '200':
          description: Successful response
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
      summary: Update user
      tags: [Users]
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateUserRequest'
      responses:
        '200':
          description: User updated
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
      summary: Delete user
      tags: [Users, Admin]
      responses:
        '204':
          description: User deleted
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
          description: Unique user identifier
        email:
          type: string
          format: email
          description: User's email address
        name:
          type: string
          minLength: 1
          maxLength: 100
          description: User's display name
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
          description: Custom metadata
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
      description: User account status

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
          description: Error code for programmatic handling
        message:
          type: string
          description: Human-readable message
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
          description: Request ID for support

  parameters:
    UserIdParam:
      name: userId
      in: path
      required: true
      description: User ID
      schema:
        type: string
        format: uuid

    PageParam:
      name: page
      in: query
      description: Page number (1-based)
      schema:
        type: integer
        minimum: 1
        default: 1

    LimitParam:
      name: limit
      in: query
      description: Items per page
      schema:
        type: integer
        minimum: 1
        maximum: 100
        default: 20

  responses:
    BadRequest:
      description: Invalid request
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            code: VALIDATION_ERROR
            message: Invalid request parameters
            details:
              - field: email
                message: Must be a valid email address

    Unauthorized:
      description: Authentication required
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            code: UNAUTHORIZED
            message: Authentication required

    NotFound:
      description: Resource not found
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            code: NOT_FOUND
            message: User not found

    RateLimited:
      description: Muitas requests
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
      headers:
        Retry-After:
          description: Seconds until the rate limit resets
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
      description: API key for service-to-service calls

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
    description="API for managing users and profiles",
    version="2.0.0",
    openapi_tags=[
        {"name": "Users", "description": "User operations"},
        {"name": "Profiles", "description": "Profile operations"},
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
    email: EmailStr = Field(..., description="User's email")
    name: str = Field(..., min_length=1, max_length=100, description="Display name")

class UserCreate(UserBase):
    role: UserRole = Field(default=UserRole.user)
    metadata: Optional[dict] = Field(default=None, description="Custom metadata")

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
    id: UUID = Field(..., description="Unique identifier")
    status: UserStatus
    role: UserRole
    avatar: Optional[str] = Field(None, description="Avatar URL")
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
    code: str = Field(..., description="Error code")
    message: str = Field(..., description="Mensagem de erro")
    details: Optional[List[ErrorDetail]] = None
    request_id: Optional[str] = Field(None, alias="requestId")

# Endpoints
@app.get(
    "/users",
    response_model=UserListResponse,
    tags=["Users"],
    summary="List all users",
    description="Returns a paginated list with optional filters.",
    responses={
        400: {"model": ErrorResponse, "description": "Invalid request"},
        401: {"model": ErrorResponse, "description": "Unauthorized"},
    },
)
async def list_users(
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(20, ge=1, le=100, description="Items per page"),
    status: Optional[UserStatus] = Query(None, description="Filter by status"),
    search: Optional[str] = Query(None, min_length=2, max_length=100),
):
    """
    Lists users with pagination and filters.

    - **page**: Page number (1-based)
    - **limit**: Items per page (max 100)
    - **status**: Filter by user status
    - **search**: Search by name or email
    """
    pass

@app.post(
    "/users",
    response_model=User,
    status_code=201,
    tags=["Users"],
    summary="Create a new user",
    responses={
        400: {"model": ErrorResponse},
        409: {"model": ErrorResponse, "description": "Email already exists"},
    },
)
async def create_user(user: UserCreate):
    """Creates a new user and sends a welcome email."""
    pass

@app.get(
    "/users/{user_id}",
    response_model=User,
    tags=["Users"],
    summary="Fetch user by ID",
    responses={404: {"model": ErrorResponse}},
)
async def get_user(user_id: UUID = Path(..., description="User ID")):
    """Returns a specific user by ID."""
    pass

@app.patch(
    "/users/{user_id}",
    response_model=User,
    tags=["Users"],
    summary="Update user",
    responses={
        400: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
    },
)
async def update_user(
    user_id: UUID = Path(..., description="User ID"),
    user: UserUpdate = ...,
):
    """Updates user attributes."""
    pass

@app.delete(
    "/users/{user_id}",
    status_code=204,
    tags=["Users", "Admin"],
    summary="Delete user",
    responses={404: {"model": ErrorResponse}},
)
async def delete_user(user_id: UUID = Path(..., description="User ID")):
    """Permanently deletes a user."""
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
  /** Unique identifier */
  id: string;
  /** User's email */
  email: string;
  /** Display name */
  name: string;
  status: UserStatus;
  role: UserRole;
  /** Avatar URL */
  avatar?: string;
  /** Custom metadata */
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
   * Lists users with pagination and filters
   * @param page Page number (1-based)
   * @param limit Items per page (max 100)
   * @param status Filter by status
   * @param search Search by name or email
   */
  @Get()
  @Security("bearerAuth")
  @Response<ErrorResponse>(401, "Unauthorized")
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
  @Response<ErrorResponse>(400, "Invalid request")
  @Response<ErrorResponse>(409, "Email already exists")
  public async createUser(
    @Body() body: CreateUserRequest
  ): Promise<User> { /* impl */ }

  @Get("{userId}")
  @Security("bearerAuth")
  @Response<ErrorResponse>(404, "Not found")
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

# Relay-style pagination
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
