# Documentation templates

Starting points, not laws. Delete every section that has nothing to say — an empty heading is worse
than a missing one.

## README

The README is the front door, not the manual. Everything past "how do I run this" belongs in `docs/`.

```markdown
# project-name

One sentence: what it does and who it's for.

## Quick start

​```bash
git clone https://github.com/owner/project-name.git
cd project-name
npm install
cp .env.example .env      # fill in the values marked required
npm run dev
​```

Open http://localhost:3000 — you should see X.

## Configuration

| Variable | Required | Default | Description |
|---|---|---|---|
| `DATABASE_URL` | yes | — | Postgres connection string |
| `PORT` | no | `3000` | HTTP port |

## Documentation

- [Getting started](./docs/getting-started.md) — build your first X
- [API reference](./docs/api.md)
- [Architecture](./docs/architecture.md) — why it's shaped this way

## Development

​```bash
npm test          # unit + integration
npm run lint
​```

## License

MIT
```

Order matters: name → what it is → running it → configuring it → everything else. A reader who has
to scroll past a badge wall and a feature essay to find `npm install` has already lost patience.

## API endpoint reference

One shape, repeated for every endpoint, no exceptions.

```markdown
## POST /v1/orders

Creates an order and reserves stock for 15 minutes.

**Auth:** Bearer token, scope `orders:write`
**Rate limit:** 100 req/min per token
**Idempotency:** send `Idempotency-Key`; repeats within 24h return the original response

### Request

| Field | Type | Required | Description |
|---|---|---|---|
| `items[].sku` | string | yes | Product SKU |
| `items[].quantity` | integer | yes | 1–100 |
| `note` | string | no | Free text, max 500 chars |

​```json
{ "items": [{ "sku": "ABC-123", "quantity": 2 }], "note": "leave at door" }
​```

### Responses

**201 Created**

​```json
{ "id": "ord_01H...", "status": "pending", "expiresAt": "2026-05-01T12:15:00Z" }
​```

| Status | Condition | Body |
|---|---|---|
| 400 | Malformed JSON | Problem Details, `type: .../bad-request` |
| 401 | Missing or expired token | Problem Details |
| 409 | SKU out of stock | Problem Details with `sku` |
| 422 | Quantity out of range | Problem Details with `errors[]` |
| 429 | Rate limit exceeded | `Retry-After` header |

### Example

​```bash
curl -X POST https://api.example.com/v1/orders \
  -H "Authorization: Bearer $TOKEN" \
  -H "Idempotency-Key: $(uuidgen)" \
  -H "Content-Type: application/json" \
  -d '{"items":[{"sku":"ABC-123","quantity":2}]}'
​```
```

## Architecture Decision Record

```markdown
# ADR-007: Cursor pagination for the orders API

**Status:** accepted — 2026-04-18
**Supersedes:** ADR-003

## Context

Offset pagination on `/orders` scans the whole table before discarding rows; p95 on page 200 is
2.4s. Clients page through the full history nightly.

## Decision

Cursor pagination keyed on `(created_at, id)`, opaque base64 cursor, `limit` capped at 100.

## Consequences

- Constant-time pages regardless of depth
- No "jump to page 200" — the dashboard's page picker becomes next/previous
- Cursors are tied to the sort key; changing the sort invalidates outstanding cursors
- Offset stays supported on `/orders` until v2 is retired (2026-09)
```

An ADR is written once and never edited into a lie. A decision that changes gets a new ADR that
supersedes it.

## Changelog

[Keep a Changelog](https://keepachangelog.com/) headings, newest first, breaking changes impossible
to miss.

```markdown
# Changelog

## [Unreleased]
### Added
- `GET /v1/orders/{id}/events`

## [2.0.0] - 2026-04-18
### ⚠️ Breaking
- `GET /v1/orders` returns cursor pages; `?page=` now returns 400. See the [migration guide](./docs/migrate-v2.md).

### Added
- `Idempotency-Key` support on all POST endpoints

### Fixed
- `created_at` returned in the server's local timezone instead of UTC
```

## JSDoc / TSDoc

Types come from TypeScript; the comment carries what types cannot.

```typescript
/**
 * Reserves stock for an order and returns the reservation window.
 *
 * Reservations expire after 15 minutes; expiry is enforced by the sweeper job,
 * so a reservation can survive a few seconds past `expiresAt`.
 *
 * @param items - SKUs and quantities to reserve
 * @returns The reservation, including its expiry instant
 * @throws OutOfStockError - when any SKU has insufficient free stock
 *
 * @example
 * const reservation = await reserveStock([{ sku: 'ABC-123', quantity: 2 }]);
 */
```

Comment the *why*, the surprising behavior and the contract. Never restate the signature.

## llms.txt

A map for agents and crawlers at `/llms.txt`. One line per entry, no marketing.

```markdown
# project-name

> Order management API for the retail platform.

## Docs
- [Getting started](https://example.com/docs/getting-started.md): first request in 5 minutes
- [API reference](https://example.com/docs/api.md): every endpoint, request and response
- [Architecture](https://example.com/docs/architecture.md): services, data flow, boundaries

## Key concepts
- Reservation: 15-minute hold on stock created with an order
- Idempotency key: client-supplied UUID that makes POST retries safe

## Optional
- [ADRs](https://example.com/docs/adr/): decision history
```
