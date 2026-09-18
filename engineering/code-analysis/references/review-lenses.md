# Review lenses

Select the sections relevant to the actual change, symptom, or trust boundary.
Use these as investigation prompts, not a checklist that requires one finding per
category. A plausible pattern still needs a reachable failure path and evidence.

## Correctness and contracts

- Follow boundary values through callers and consumers: absent versus empty,
  zero versus false, inclusive versus exclusive ranges, overflow, precision,
  time zones, and ordering. Use the language and domain's actual semantics.
- Compare the implementation with the public contract, including errors and
  status codes. Check whether a changed return shape or default breaks an
  existing consumer, serializer, schema, or persisted record.
- Trace every relevant state transition and forbidden outcome. Confirm that
  validation happens before the consequential side effect and that partial
  failure cannot produce a success response.
- For UI code, inspect state ownership, stale asynchronous responses, loading and
  error states, and relevant accessibility behavior. Treat visual behavior as
  unverified until a browser check or equivalent evidence exists.

## Data integrity and concurrency

- Look for read-check-write sequences. Work through a concrete interleaving and
  inspect isolation level, locking, conditional writes, uniqueness constraints,
  and conflict handling before claiming a race. A transaction alone does not
  necessarily serialize a predicate check.
- Follow retries, duplicate delivery, timeouts, cancellation, and restarts across
  external side effects. Check idempotency key scope, persistence, atomicity,
  retention, and behavior when an outcome is unknown.
- Check ordering and coordination across database writes, queue publication, and
  acknowledgments. Distinguish atomic local transactions from cross-service
  delivery guarantees; do not prescribe an outbox without a demonstrated need.
- Inspect migrations and compatibility across old/new readers and writers,
  especially destructive changes, backfills, defaults, and recovery paths.

## Security and privacy

- Trace untrusted input to a sensitive operation. Identify the real trust
  boundary, authorization context, tenant/resource ownership, and exposure.
  Authentication by itself does not prove authorization; a missing local guard
  does not prove a bypass when enforcement exists upstream or in storage.
- For injection, traversal, SSRF, unsafe deserialization, or similar candidates,
  verify the actual API semantics, input control, validation, and reachable sink.
  Do not label a dangerous-looking function name as a vulnerability by itself.
- Check how secrets and personal data enter logs, errors, URLs, caches, and
  responses. Redact values in findings; cite the location without copying the
  sensitive payload.
- Evaluate cache keys and shared mutable state against user, tenant, and privilege
  boundaries. Consider invalidation and authorization changes, not only key shape.
- For dependency advisories, establish the resolved version and affected usage
  and verify the claim against a primary advisory when permitted. Distinguish an
  advisory match from demonstrated exploitability; do not invent CVE identifiers.

## Reliability and resource lifecycle

- Trace cleanup on success, error, timeout, and cancellation: locks, file handles,
  sockets, subscriptions, transactions, timers, and temporary resources.
- Check asynchronous ownership: awaited work, intentionally detached tasks,
  propagated errors, shutdown, cancellation, and races between completion and
  disposal. Inspect who owns a task before flagging it as unhandled.
- Examine retry bounds, backoff, timeout budgets, queue growth, and overload
  behavior. Identify a concrete exhaustion path rather than recommending generic
  retries that could amplify load or duplicate writes.
- Verify that errors retain useful context without leaking sensitive data and
  that reported success corresponds to the actual committed or delivered result.

## Performance and scalability

- Relate work to input size and plausible load: repeated queries, nested scans,
  unbounded reads, eager materialization, blocking I/O, and cache growth.
- Separate what source establishes (for example, one query per item) from what
  needs measurement (latency, throughput, memory use, or user-visible impact).
  State workload assumptions; do not fabricate benchmark numbers.
- Inspect batching, pagination, indexes, caching, and downstream limits before
  recommending an optimization. An allocation or loop is not a performance defect
  merely because a different implementation exists.
- Propose the smallest representative measurement when impact remains unknown.
  Avoid changing algorithms or adding infrastructure during an analysis-only task.

## Tests and validation quality

- Read assertions and setup, not just test names or coverage percentages. Ask
  whether the test would fail for the concrete defect under investigation.
- Prefer externally observable behavior and independent expected values. Identify
  mocks that bypass the risky boundary or reproduce the same mistake as the code.
- Inspect failure, boundary, retry, and concurrency coverage when those behaviors
  matter. Missing coverage is a validation gap, not proof of a production defect.
- Separate environment/setup errors and pre-existing failures from regressions.
  Record a skipped, unavailable, or unexecuted check honestly.

## Maintainability and change impact

- Tie complexity, coupling, duplication, or misleading names to a concrete cost:
  divergent behavior, an invariant that is easy to violate, a hidden side effect,
  or a public interface that callers cannot use safely.
- Follow the project's documented conventions and established abstractions.
  Prefer a local, sufficient correction over a speculative rewrite.
- Check docs and configuration affected by contract, build, deployment, or
  operational changes. Keep subjective style suggestions optional and separate
  from defects; let formatters handle purely mechanical style when authorized.
