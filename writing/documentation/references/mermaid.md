# Mermaid diagrams

A diagram earns its place when the relationship is the point — order of calls, branching, ownership
of data. If a sentence says it, write the sentence.

## Picking the type

| You need to show | Use |
|---|---|
| A decision or a process with branches | `flowchart` |
| Who calls whom, in what order, over time | `sequenceDiagram` |
| Tables and their relationships | `erDiagram` |
| The states a thing moves through | `stateDiagram-v2` |
| Services and boundaries | `flowchart` with `subgraph` |
| Types and their relations | `classDiagram` |

Keep it under ~15 nodes. Past that, split into two diagrams or drop to prose — a wall of boxes
communicates less than a list.

## Flowchart

```mermaid
flowchart TD
    Request[Incoming request] --> Auth{Valid token?}
    Auth -->|no| Reject[401 Unauthorized]
    Auth -->|yes| Limit{Under rate limit?}
    Limit -->|no| Throttle[429 Too Many Requests]
    Limit -->|yes| Handler[Route handler]
    Handler --> DB[(Postgres)]
```

`TD` top-down, `LR` left-right. `[]` process, `{}` decision, `[()]` database, `(())` start/end.

## Sequence

```mermaid
sequenceDiagram
    participant C as Client
    participant A as API
    participant S as Auth server

    C->>A: POST /orders (Bearer token)
    A->>S: introspect token
    S-->>A: active, scope=orders:write
    A-->>C: 201 Created + Location
    Note over A,S: introspection is cached for 60s
```

`->>` call, `-->>` response, `-)` async with no reply. Use `activate`/`deactivate` only when the
lifetime of a call is the thing you're explaining.

## Entity relationship

```mermaid
erDiagram
    USER ||--o{ ORDER : places
    ORDER ||--|{ ORDER_ITEM : contains
    PRODUCT ||--o{ ORDER_ITEM : "appears in"

    USER {
        uuid id PK
        string email UK
        timestamptz created_at
    }
    ORDER {
        uuid id PK
        uuid user_id FK
        string status
    }
```

Cardinality reads left-to-right: `||` exactly one, `o{` zero or many, `|{` one or many.

## State

```mermaid
stateDiagram-v2
    [*] --> pending
    pending --> paid: payment confirmed
    pending --> cancelled: timeout after 30m
    paid --> shipped: warehouse dispatch
    shipped --> delivered
    delivered --> [*]
    paid --> refunded: refund requested
```

## Architecture with boundaries

```mermaid
flowchart LR
    subgraph client[Client]
        Web[Next.js app]
    end
    subgraph platform[Platform]
        API[Fastify API]
        Worker[Job worker]
    end
    Web -->|HTTPS| API
    API -->|enqueue| Queue[(Redis)]
    Queue --> Worker
    Worker --> DB[(Postgres)]
    API --> DB
```

## Rules that keep diagrams readable

- Label every edge that isn't obvious — an unlabeled arrow is a guess
- One direction per diagram; mixed flow directions read as noise
- Name nodes as they're named in the code, so the diagram is greppable
- Skip custom colors unless a color carries meaning; the default theme adapts to light and dark
- Put the diagram next to the prose it supports, never as the only explanation — screen readers and
  diffs both need the text
