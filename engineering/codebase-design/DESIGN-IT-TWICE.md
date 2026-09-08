# Compare alternative interfaces

For a consequential boundary, write the constraints and a representative caller. Sketch a few meaningfully different interfaces: minimize caller decisions, favor the common operation, or isolate a volatile dependency. Do not force a fixed number of alternatives or agents.

For each useful alternative, show a usage example, hidden implementation responsibilities, error/ordering guarantees and dependency strategy. Compare complexity transferred to callers, locality of change and test seams. Recommend a design with concrete tradeoffs; a hybrid is useful only if it stays understandable.

Independent design passes may help when delegation is available and authorized. Give each worker the relevant context, constraints and expected output; shared history is not guaranteed. Otherwise compare designs directly. Read [deepening guidance](DEEPENING.md) when dependency placement is the uncertainty.
