# Node service architecture

Start from deployment needs and ownership. A modular service is often enough; separate deployables only when independent scaling, isolation or release cadence justifies the operational cost.

Keep transport parsing, application policy and persistence responsibilities understandable. Use the framework's existing structure instead of imposing controllers/services/repositories everywhere. Validate external input once at a trusted boundary and enforce authorization close to the protected operation.

Choose Fastify, Express, a framework or plain Node from the existing stack and requirements. Model async work explicitly: cancellation, timeouts, bounded concurrency, retries only for safe operations, and idempotency for repeated side effects. Use durable queues when work must survive process loss.

Measure before adding workers, caches or distributed services. Design shutdown to stop intake, finish or safely return in-flight work, and close dependencies. Record health/readiness semantics and operational signals that distinguish a healthy process from a usable service.

This reference incorporates the service-design material formerly in `nodejs-best-practices`; detailed runtime examples remain in the surrounding Node rules.
