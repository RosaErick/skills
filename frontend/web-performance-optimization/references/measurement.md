# Measure before selecting an optimization

Choose the user-visible symptom and a reproducible journey. Record URL/build, device, browser, network/CPU settings, cache state and run count. Use field measurements at the relevant percentile for user experience where available; use browser traces and repeatable lab runs to isolate causes.

| Symptom | Evidence to inspect |
|---|---|
| Main content arrives late | LCP element, server response, critical request chain, image priority |
| Interaction responds slowly | INP, long tasks, event handlers, rendering and input delay |
| Layout moves unexpectedly | CLS sources, missing dimensions, fonts and inserted content |
| Excess memory or CPU | Heap/CPU profiles, retained objects, repeated work |
| Large transfers | Resource waterfall, compression, unused code, images and third-party assets |

Use DevTools Performance/Network, framework profiling, bundle analysis or Lighthouse according to the question. FID appears in historical reports; do not present it as the current responsiveness Core Web Vital. Synthetic scripts that never perform the interaction cannot establish its real-user latency.

Test one meaningful optimization, compare the same scenario, and repeat enough to distinguish the effect from noise. Record regressions and tradeoffs such as stale data, cache invalidation or delayed functionality. Stop when the agreed objective is met rather than chasing every possible micro-optimization.
