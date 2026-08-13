---
source: original
name: python-patterns
description: "Modern Python (3.11–3.13) code and project patterns — uv and pyproject layout, ruff, typing with PEP 695 generics, dataclasses vs Pydantic, async with TaskGroup and timeouts, error handling, logging, configuration, testing with pytest, and packaging. Use when starting or restructuring a Python project, choosing between sync and async, adding or fixing type hints, designing modules and dependency boundaries, handling errors and retries, configuring ruff/mypy/pytest, or reviewing Python for correctness and clarity. Trigger terms: Python project, pyproject.toml, uv, ruff, type hints, mypy, dataclass, Pydantic, asyncio, async def, pytest, virtualenv, requirements.txt."
allowed-tools: Read, Write, Edit, Glob, Grep
metadata:
  tags: python, typing, async, pytest, uv, ruff, pydantic, packaging
---

# Python Patterns

Language and project-level Python. HTTP contract design is `backend/api-patterns`; API docs are
`backend/api-documentation-master`.

Target 3.11+ — that's where `TaskGroup`, `ExceptionGroup`, `Self` and `tomllib` live. Prefer 3.12+
for PEP 695 generics. Everything below assumes type hints are on by default.

## 1. Project layout

```
project/
├── pyproject.toml          the only config file that matters
├── src/mypackage/          src layout: tests import the installed package, not the working copy
│   ├── __init__.py
│   ├── config.py           settings, loaded once
│   ├── domain/             pure logic, no I/O, no framework imports
│   ├── adapters/           database, HTTP clients, storage — everything that touches the world
│   └── api/                the delivery layer (Flask/FastAPI routes, CLI entry points)
└── tests/
```

```toml
[project]
name = "mypackage"
requires-python = ">=3.11"
dependencies = ["httpx>=0.27", "pydantic>=2.7"]

[dependency-groups]
dev = ["pytest>=8", "pytest-asyncio", "ruff", "mypy"]

[tool.ruff]
line-length = 100
[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B", "SIM", "RUF"]

[tool.mypy]
strict = true

[tool.pytest.ini_options]
addopts = "-q --strict-markers"
```

- **uv** for environments, installs, locking and running (`uv sync`, `uv run pytest`,
  `uv add httpx`). It replaces pip + virtualenv + pip-tools, and it's fast enough that nobody skips
  the lockfile anymore. `requirements.txt` only survives where a platform demands it.
- **ruff** for lint and format — one tool instead of flake8 + isort + black.
- Commit the lockfile for applications; don't for libraries.
- Keep the dependency arrow pointing inward: `api → domain ← adapters`. The domain importing a
  framework is how a codebase becomes untestable.

## 2. Typing

```python
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from typing import Self

type OrderId = str                      # PEP 695 alias (3.12+)

def total[T: (int, float)](values: Iterable[T]) -> T:   # PEP 695 generics (3.12+)
    return sum(values)

@dataclass(frozen=True, slots=True)
class Order:
    id: OrderId
    items: Sequence[Item]
    note: str | None = None

    def with_note(self, note: str) -> Self:
        return replace(self, note=note)
```

- `X | None`, not `Optional[X]`. Built-in `list[str]`, `dict[str, int]` — never `typing.List`.
- Accept the widest sensible type, return the narrowest: take `Iterable[Item]`, return `list[Item]`.
- Import ABCs from `collections.abc`, not `typing`.
- `Protocol` for structural interfaces — it keeps the domain free of adapter imports and needs no
  inheritance from the implementer.
- `mypy --strict` (or pyright) in CI on the package, relaxed for tests. Types that aren't checked are
  comments.
- `Any` is a decision, not a default. When it's unavoidable, isolate it at the boundary and cast once.

### Dataclass or Pydantic

| Need | Use |
|---|---|
| Internal value object, already-valid data | `@dataclass(frozen=True, slots=True)` |
| Parsing untrusted input (HTTP body, config file, env, JSON) | Pydantic v2 model |
| Settings from environment | `pydantic-settings` |
| Hot path, millions of instances | `dataclass(slots=True)` or `NamedTuple` |

Validate at the edge, once, into a typed object. Passing raw `dict`s inward is how `KeyError` gets
into production.

## 3. Async

Async buys concurrency for **I/O waiting**, nothing else. CPU-bound work belongs in a process pool;
a mostly-CPU service is simpler and often faster as sync code with more workers.

```python
async def fetch_all(urls: list[str]) -> list[Response]:
    async with httpx.AsyncClient(timeout=10) as client:
        async with asyncio.TaskGroup() as tg:          # 3.11+
            tasks = [tg.create_task(client.get(url)) for url in urls]
    return [t.result() for t in tasks]
```

- `TaskGroup` over bare `gather`: it cancels siblings on failure and raises an `ExceptionGroup`, so
  no task is silently orphaned. Catch with `except*`.
- Every network call gets a timeout. `asyncio.timeout()` wraps a block; clients take their own.
- Never `await` inside a lock held across I/O you don't control, and never block the loop —
  `time.sleep`, `requests`, heavy parsing all freeze every other task. Push them to
  `asyncio.to_thread` or a process pool.
- Don't mix drivers: one sync `psycopg` call in an async handler stalls the whole loop.
- Fire-and-forget tasks need a reference (`background.add(task)`) or the GC will collect them
  mid-flight.

## 4. Errors

```python
class OrderError(Exception): ...
class OutOfStock(OrderError):
    def __init__(self, sku: str, available: int) -> None:
        super().__init__(f"{sku}: only {available} available")
        self.sku, self.available = sku, available
```

- Define an exception hierarchy per package, rooted in one base — callers catch the base or a leaf,
  never `Exception`.
- Carry the data the caller needs to react (`sku`, `available`), not just a message string.
- `raise ... from err` when re-raising, so the original traceback survives.
- Catch narrowly and near the boundary; the domain raises, the delivery layer maps to a status code.
- `finally` and context managers over manual cleanup; `contextlib.suppress` instead of an empty
  `except: pass`.
- Retry only what's idempotent, with exponential backoff and a cap (`tenacity` if it earns the
  dependency).

## 5. Configuration and logging

```python
class Settings(BaseSettings):
    database_url: str
    log_level: str = "INFO"
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()      # constructed once, imported everywhere
```

- Config comes from the environment, is validated once at startup, and fails loudly if a required
  value is missing. Reading `os.environ` scattered through the code is a runtime surprise waiting to
  happen.
- Never commit secrets; `.env` in `.gitignore`, `.env.example` in the repo.
- `logging` with a structured formatter (JSON in production), never `print`. One logger per module:
  `logger = logging.getLogger(__name__)`.
- Log the request/correlation id on every line; log at the boundary, not in every helper.
- Never log credentials, tokens or full request bodies.

## 6. Testing

```python
@pytest.mark.parametrize(
    ("quantity", "expected"),
    [(1, 10), (3, 30), (0, 0)],
)
def test_line_total(quantity: int, expected: int) -> None:
    assert line_total(price=10, quantity=quantity) == expected
```

- pytest, plain `assert`, fixtures for setup — no `unittest` boilerplate.
- Test behavior through the public function. Tests that import a private helper break on every
  refactor and prove nothing about the contract.
- Parametrize instead of copy-pasting cases; the failure output tells you which case broke.
- Mock the boundary (HTTP, clock, storage), never the domain. `respx`/`responses` for HTTP,
  `freezegun` or an injected clock for time, a real (temporary) database over a mocked one when it's
  affordable — mocked SQL asserts nothing about SQL.
- `pytest-asyncio` for async tests; mark the mode in config to avoid decorating every test.
- Property-based tests (Hypothesis) pay off for parsers, encoders and anything with invariants.

## 7. Data and performance

- Comprehensions and generators over manual loops with `append`. Generators for anything that might
  be large — they don't materialize the list.
- `pathlib.Path` over `os.path`. `tomllib` for TOML (stdlib, 3.11+).
- Dicts and sets for lookups; a linear scan inside a loop is the most common accidental O(n²).
- Batch database access — the N+1 query is the default failure mode of ORMs.
- `functools.lru_cache`/`cache` for pure functions with small argument spaces.
- Profile before optimizing: `cProfile`, `py-spy` for a live process, `timeit` for microbenchmarks.
  Reach for C extensions, `polars` or Cython only after the profile names them.

---

## Anti-patterns

| ❌ | ✅ |
|---|---|
| Mutable default argument (`def f(x=[])`) | `x: list[int] | None = None`, build inside |
| `except Exception: pass` | Catch the specific error, handle or re-raise |
| `from module import *` | Explicit imports |
| Business logic in the route handler | Domain function, called by the handler |
| `dict` passed through five layers | A typed dataclass or model |
| `time.sleep` in async code | `await asyncio.sleep` |
| `os.environ["X"]` scattered around | One validated settings object |
| `print` for diagnostics | `logging` |
| Comparing with `== None` / `== True` | `is None`, truthiness |
| Requirements pinned by hand across three files | `pyproject.toml` + lockfile via uv |

---

> Modern Python is boring on purpose: one config file, one tool for lint and format, types checked in
> CI, I/O at the edges, pure logic in the middle. Everything else is a preference.
