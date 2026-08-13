#!/usr/bin/env bash
# Put these skills where an agent will read them: <target>/<skill>/SKILL.md
#
#   install.sh -a codex                     every category into ~/.codex/skills
#   install.sh -a opencode frontend         only these categories
#   install.sh -a claude -t ../my-project   into that project's .claude/skills
#   install.sh -T /any/path                 into a directory you name yourself
#   install.sh -a codex -c -t ../project    COPY instead of link — editable, yours to change
#   install.sh -a codex -u                  remove the links this script created
#
# -a names the host whose skills directory to use; there is no default host.
#   claude    ~/.claude/skills                    <project>/.claude/skills
#   codex     ~/.codex/skills                     <project>/.codex/skills
#   opencode  ~/.config/opencode/skills           <project>/.opencode/skills
#   agents    (project only)                      <project>/.agents/skills
#
# link (default): one copy on disk, in this repo. Editing a linked skill edits the repo.
# copy (-c):      independent files. Hackable, and they never see an update from here.
# Pick one per target. Doing both leaves every skill in twice.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
AGENT=""
PROJECT=""
TARGET=""
MODE=link
FORCE=false

while getopts ":a:t:T:cuf" opt; do
  case $opt in
    a) AGENT="$OPTARG" ;;
    t) PROJECT="$(cd "$OPTARG" && pwd)" ;;
    T) TARGET="$OPTARG" ;;
    c) MODE=copy ;;
    u) MODE=uninstall ;;
    f) FORCE=true ;;
    *) echo "usage: $0 -a claude|codex|opencode|agents [-t project-dir] [-T path] [-c] [-f] [-u] [category...]" >&2; exit 2 ;;
  esac
done
shift $((OPTIND - 1))

if [ -z "$TARGET" ]; then
  case "$AGENT" in
    "") echo "which host? pass -a claude|codex|opencode|agents, or -T <path>" >&2; exit 2 ;;
    claude)   TARGET="${PROJECT:+$PROJECT/.claude}";   TARGET="${TARGET:-$HOME/.claude}/skills" ;;
    codex)    TARGET="${PROJECT:+$PROJECT/.codex}";    TARGET="${TARGET:-$HOME/.codex}/skills" ;;
    opencode) TARGET="${PROJECT:+$PROJECT/.opencode}"; TARGET="${TARGET:-${XDG_CONFIG_HOME:-$HOME/.config}/opencode}/skills" ;;
    agents)
      [ -n "$PROJECT" ] || { echo "-a agents is project-scoped: pass -t <project-dir>" >&2; exit 2; }
      TARGET="$PROJECT/.agents/skills" ;;
    *) echo "unknown agent: $AGENT (claude, codex, opencode, agents — or name a path with -T)" >&2; exit 2 ;;
  esac
fi

if [ $# -gt 0 ]; then
  CATEGORIES=("$@")
else
  CATEGORIES=()
  for dir in "$REPO"/*/; do
    name="$(basename "$dir")"
    # A category is a top-level folder holding at least one skill. skills/ is the flat
    # bundle generated for the plugin manifests — installing from it would link every
    # skill a second time, through a folder that gets rebuilt.
    case "$name" in skills | scripts) continue ;; esac
    compgen -G "${dir}*/SKILL.md" > /dev/null && CATEGORIES+=("$name")
  done
fi

mkdir -p "$TARGET"
done_count=0 skipped=0

for category in "${CATEGORIES[@]}"; do
  if [ ! -d "$REPO/$category" ]; then
    echo "skip: no such category: $category" >&2
    continue
  fi
  for skill in "$REPO/$category"/*/; do
    [ -f "${skill}SKILL.md" ] || continue
    name="$(basename "$skill")"
    dest="$TARGET/$name"

    case $MODE in
      uninstall)
        # Only remove links pointing back into this repo — never touch real folders.
        if [ -L "$dest" ] && [[ "$(readlink "$dest")" == "$REPO"/* ]]; then
          rm "$dest"
          done_count=$((done_count + 1))
        fi
        ;;
      link)
        # Never clobber something already there unless it is our own link: a folder is
        # somebody's real skill, and a link elsewhere belongs to another collection.
        if [ -e "$dest" ] || [ -L "$dest" ]; then
          current="$(readlink "$dest" 2>/dev/null || true)"
          if [ -z "$current" ] || [[ "$current" != "$REPO"/* ]]; then
            echo "skip: $name already in $TARGET, pointing elsewhere" >&2
            skipped=$((skipped + 1))
            continue
          fi
        fi
        ln -sfn "${skill%/}" "$dest"
        done_count=$((done_count + 1))
        ;;
      copy)
        if [ -e "$dest" ] && ! $FORCE; then
          echo "skip: $name already exists in $TARGET (use -f to overwrite)" >&2
          skipped=$((skipped + 1))
          continue
        fi
        rm -rf "$dest"
        cp -RL "${skill%/}" "$dest"
        done_count=$((done_count + 1))
        ;;
    esac
  done
done

case $MODE in
  uninstall) echo "removed $done_count link(s) from $TARGET" ;;
  link)      echo "linked $done_count skill(s) into $TARGET${skipped:+, skipped $skipped}" ;;
  copy)      echo "copied $done_count skill(s) into $TARGET${skipped:+, skipped $skipped} — they no longer track this repo" ;;
esac
