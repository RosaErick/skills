---
disable-model-invocation: true
name: app-builder
description: "Scaffold a new application or deliver a substantial feature using the project’s stack and selected templates."

---

# Build the requested application

Inspect the workspace before scaffolding. For an existing project, follow its stack, architecture and scripts; for a new project, infer requirements from the request and ask only about consequential missing choices.

Read [project detection](project-detection.md) or [stack selection](tech-stack.md) if that decision is unresolved. For a new application, choose the matching entry in the [13-template index](templates/SKILL.md), adapting versions, packages and structure to the actual requirements. Templates are starting points, not instructions to add every listed feature.

Implement an end-to-end useful slice, then continue through the agreed scope. Use [scaffolding](scaffolding.md) for initial structure and [feature delivery](feature-building.md) for integration. Keep any plan in the repository's established location; a root plan file and a minimum interview are unnecessary.

Use only tools and agents actually available. [Coordination guidance](agent-coordination.md) applies when independent delegation is available and authorized; the work does not depend on a fixed roster of specialists.

Verify the app's relevant behavior, startup/build and configured checks. Resolve in-scope findings and deliver runnable files with any necessary environment instructions. Existing authorization governs installation, commits and deployment; do not stop at scaffolding when a working feature was requested.
