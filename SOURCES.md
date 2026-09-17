# Sources and attribution

Selected tracked files were imported with their supporting resources. File-level SHA-256 checksums, original paths, destination paths, and exact revisions are recorded in [sources.json](sources.json). Checksums describe the initial import, not subsequent adaptations listed below.

## RosaErick/skills

Source: <https://github.com/RosaErick/skills>

Revision: `5dbac4d4eb8a7f0dc086e52ced61e8dcfb4d61e2`

Imported 11 skills from the local checkout: `api-documentation-master`, `api-patterns`, `domain-design`, `tdd`, `i18n-localization`, `web-performance-optimization`, `architecture`, `parallel-agents`, `plan-writing`, `documentation`, and `ux-writing`.

The selected revision has no repository-wide license file. Existing attribution and metadata are preserved. Review inherited third-party licensing before publication; no blanket license is asserted for this collection.

## mitsuhiko/agent-stuff

Source: <https://github.com/mitsuhiko/agent-stuff>

Revision: `122e2994adddb113c04764c5697217dae120fcc6`

Imported `tmux`, `update-changelog`, `web-browser`, `native-web-search`, `github`, and `commands/discuss.md` (stored here as `prompts/discuss.md`). Supporting scripts and dependency manifests are included; generated files and installed dependencies are not.

The upstream Apache 2.0 license is preserved in [licenses/agent-stuff-Apache-2.0.txt](licenses/agent-stuff-Apache-2.0.txt). Skill-level attribution and metadata are retained, including informal upstream license labels that need review before publication.

### Historical frontend-design

Imported from revision `ebbb8ac40a1344fb1ac6a77457d8c691a4018d8e`, where the skill was introduced. It was later removed by upstream in `a571b86f70fed288fb9419fe5f6171f48b66a402`.

This is the historical `agent-stuff` skill, not a replacement copied from another local installation.

## Local adaptations

- `frontend/frontend-design/SKILL.md`: renamed the invocation name to `frontend-design-mitsuhiko` and added a modification notice. The instructions are unchanged. This avoids colliding with independently installed `frontend-design` skills; the directory and original-import checksum retain their source identity.
