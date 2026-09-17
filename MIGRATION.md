# Migration and rollback

## Pi-first collection

The former collection is preserved on `old_version` at commit `5dbac4d4eb8a7f0dc086e52ced61e8dcfb4d61e2`. The new collection contains 17 selected skills and the `/discuss` prompt, exposed through the Pi package manifest.

The legacy Claude/Codex plugin manifests and installer are no longer included. Remove installations of `erickrosa-skills@rosaerick` and links to the old collection before enabling this package. Keep unrelated skills and plugins installed.

Use one installation route, as described in [README.md](README.md). A package installation loads both the skill categories and `/discuss`; registering the repository only in Pi's `skills` setting does not load its prompt template.

The imported frontend design skill is invoked with `/skill:frontend-design-mitsuhiko` to avoid colliding with other `frontend-design` installations.

## Recover older content

Inspect a previous file without changing the working tree:

```bash
git show old_version:writing/documentation/SKILL.md
```

Create a separate checkout of the previous collection:

```bash
git worktree add --detach ../skills-old-version old_version
```

This leaves the active collection unchanged. Review and copy only the content needed; do not install the old and new collections together.

## Roll back the collection

1. Save or commit current changes and back up Pi settings.
2. Remove this collection's package entry from Pi settings, preserving other entries.
3. Create the separate `old_version` checkout shown above.
4. Register that checkout in Pi's `skills` setting, using its absolute path.
5. Restart Pi and verify discovery. The remake's `/discuss` is not part of the old collection.

A branch rollback restores repository content, not user settings or other agents' installations. Restore those from the local migration backup if needed. Do not rewrite the remote branch history to roll back.

## Follow-up review

- Review imported host-specific conventions, including Claude-named tmux socket examples.
- Review cross-skill recommendations that point outside the selected collection.
- Review inherited licensing and tool requirements before broader redistribution; see [SOURCES.md](SOURCES.md).
