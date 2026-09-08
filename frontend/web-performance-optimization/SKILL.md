---
source: original
name: web-performance-optimization
description: "Measure and improve a web page’s user-visible loading, responsiveness, stability, or resource cost."
---

# Optimize a measured bottleneck

Identify the affected page/flow, device/network conditions and performance symptom. Capture a reproducible baseline before changing code when feasible. Distinguish field experience from laboratory diagnostics; one Lighthouse score does not represent all users.

Use [measurement guidance](references/measurement.md) to choose metrics and tools. Current Core Web Vitals are LCP, INP and CLS; FID is a historical metric. Compare like-for-like runs and note variability.

Trace the limiting work: request waterfalls, image/font delivery, render-blocking assets, JavaScript execution, third-party code, expensive rendering or layout shifts. Fix the largest supported cause with a reviewable change, then measure the same scenario again and check visual/functional behavior.

Use code splitting, asset sizing, caching, memoization, CDN delivery or a service worker only when the evidence and architecture justify them. A universal 200 KB bundle budget or mandatory offline layer is not appropriate for every application. Set budgets from user needs and baseline evidence.

Report before/after observations, measurement conditions and remaining uncertainty. [The Lighthouse helper](scripts/lighthouse_audit.py) can collect a lab report when its runtime dependencies are available; inspect its options and use a safe target. Do not label missing tooling or an unmeasured result as a performance pass.

Source: [INP became a Core Web Vital](https://web.dev/blog/inp-cwv-launch).
