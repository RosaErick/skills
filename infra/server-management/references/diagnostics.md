# Service diagnostic procedures

| Signal | Evidence | Likely next decision |
|---|---|---|
| Start fails | Supervisor exit status, application startup log, config validation, occupied port | Fix the observed configuration/dependency/permission issue before restarting |
| Health fails but process exists | Readiness/liveness distinction, active requests, event-loop/thread state, upstream timeouts | Identify blocked work or dependency failure; choose a bounded drain/restart if needed |
| Memory or disk pressure | Process/resource metrics, growth over time, logs/temp/data ownership | Recover capacity without deleting application data or evidence blindly |
| Restart loop | Exit reason, signal, resource limit, readiness/startup timing | Fix the trigger rather than increasing restart frequency |
| Requests fail after deploy | Running revision, route/proxy configuration, migrations, dependency compatibility | Restore a compatible release or apply the targeted correction |

For systemd, inspect the exact unit with `systemctl status <unit>` and scoped `journalctl -u <unit>`. For containers, use the owning runtime/controller's status, events and logs. Commands require actual host tools and permissions; do not present an invented unit name as discovered evidence.

Validate recovery with a real operation and supervision state. Separate temporary mitigation from the permanent fix, and preserve relevant timestamps for later investigation.
