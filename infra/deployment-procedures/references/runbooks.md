# Select a deployment runbook

| Platform | Before execution | After execution | Recovery |
|---|---|---|---|
| Managed application platform | Inspect project/environment mapping, build command and release configuration | Confirm release ID, route health and affected flow | Use platform rollback/redeploy procedure; verify configuration compatibility |
| Container/orchestrated service | Identify image digest, namespace/service, probes and rollout strategy | Inspect rollout status, failing replicas, logs and request health | Restore compatible image/config through the deployment controller |
| Directly managed host | Identify service manager, artifact path, owner, config and writable data | Confirm running process/version, service status and local/external health | Restore prior artifact/config and restart through the service manager |

Use the existing CI pipeline when it owns deployment; avoid a parallel manual release path without a reason. Keep credentials in the established secret store. Check migrations separately: backups need a usable restoration path, and irreversible data changes require a compatible forward repair or explicitly planned recovery.

For partial rollouts, compare representative health signals with the baseline. Low traffic may require synthetic verification; high traffic may expose regressions quickly. Choose observation duration from that evidence, not a fixed schedule.
