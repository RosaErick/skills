---
name: database-design
description: "Design or review database schemas, indexes, query plans, ORM choices, and safe migrations."

---

# Choose from the actual data problem

Read the existing database/ORM, migrations, schema and affected queries first. Infer established choices from configuration. Ask about a database preference only when a new selection is in scope and cannot be resolved from requirements.

| Decision | Reference |
|---|---|
| Database selection | [database-selection.md](database-selection.md) |
| ORM/query builder | [orm-selection.md](orm-selection.md) |
| Entities, keys and relationships | [schema-design.md](schema-design.md) |
| Index design | [indexing.md](indexing.md) |
| Query performance/N+1 | [optimization.md](optimization.md) |
| Schema evolution | [migrations.md](migrations.md) |

Define integrity and consistency requirements before picking representation. Add indexes from access patterns and inspect query plans where performance is the question. Consider write cost, data volume and deployment constraints; neither adding every possible index nor changing the database by default is appropriate.

Plan compatible migration ordering and data recovery where needed. Validate the affected invariant/query/migration using the actual database version and project checks. [schema_validator.py](scripts/schema_validator.py) is a heuristic helper and does not prove a migration safe.
