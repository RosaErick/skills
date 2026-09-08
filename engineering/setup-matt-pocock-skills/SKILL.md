---
name: setup-matt-pocock-skills
description: "Configure project conventions for the Matt Pocock workflow skills when setup is requested."
disable-model-invocation: true
---

# Configure only the missing conventions

Inspect existing instructions, documentation layout, issue tracking and labels. Reuse them. Setup is an optional configuration task; implementation, review and specifications can proceed without it.

Choose the relevant integration: [local tracking](issue-tracker-local.md), [GitHub](issue-tracker-github.md), [GitLab](issue-tracker-gitlab.md), [domain documents](domain.md) or [triage labels](triage-labels.md). Read only the branches needed. Treat their layouts as templates, adapting names and locations to the project.

Prepare concrete configuration and document changes before requesting any external permission that is actually missing. Existing user authorization persists. Do not create duplicate labels, overwrite custom instructions, or require a new tracking system when one already works.

Apply authorized changes idempotently: compare existing values first and make a second run produce no duplicate content. Report the paths and integrations configured, with any external action still pending. No setup completion marker is a gate for the other skills.
