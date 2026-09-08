---
name: deployment-procedures
description: "Prepare, execute, or troubleshoot a deployment using the target platform’s runbook and verification signals."

---

# Deploy a reviewable change

Identify the target environment, platform, artifact and requested action. Inspect the repository's deployment configuration and existing runbook. Reuse earlier authorization; prepare the artifact and checks before asking for a missing approval to affect an external environment.

Choose the relevant [deployment runbook](references/runbooks.md): a managed platform, container service or directly managed host. Confirm configuration and secret references without printing values. Build and run required checks in the mode relevant to deployment.

For schema or compatibility changes, define ordering and recovery before execution. A rollback must account for data compatibility; reverting application code alone may be unsafe after a destructive migration.

Execute the authorized deployment with the project's tooling. Verify the deployed revision, health/readiness and the affected user flow. Observe error rate, latency or queue behavior over a period appropriate to traffic and rollout risk rather than a universal time window or weekday rule.

If the release regresses, use the applicable recovery procedure within authorization and report evidence. Finish with deployment state, revision, checks and any real limitation. A deployment task is not satisfied by a checklist alone when execution was requested and is authorized.
