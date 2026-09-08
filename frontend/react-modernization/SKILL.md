---
source: original
name: react-modernization
description: "Migrate an existing React application between identified versions or replace legacy APIs incrementally."
---

# Migrate from an identified baseline

Record current and target React/React DOM versions, framework, TypeScript types, test utilities and third-party compatibility. Choose a supported target from the project's constraints; an old 16→17→18 sequence is not a definition of the latest release.

Use the matching official upgrade guide and [migration playbook](resources/implementation-playbook.md). Inventory removed/deprecated APIs, root rendering, effects, refs and test assumptions in affected code. Apply a relevant codemod to a reviewable scope and inspect the resulting diff; do not run an unpinned migration blindly across unrelated files.

Migrate in slices that keep the app runnable. Preserve observable behavior and test the flows most exposed to rendering, effect cleanup and state changes. Treat Strict Mode diagnostics as evidence of lifecycle assumptions rather than disabling it to hide failures.

A version upgrade does not automatically require converting every class, replacing the state library or enabling a compiler. Adopt new APIs only where they solve the requested problem. Report the actual target, changes, compatibility decisions and validation performed.
