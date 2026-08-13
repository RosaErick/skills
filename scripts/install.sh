#!/usr/bin/env bash
# Put these skills where an agent will read them: <target>/.claude/skills/<skill>/SKILL.md
#
#   install.sh                       link every category into ~/.claude/skills
#   install.sh frontend backend      link only those categories
#   install.sh -t ../my-project      link into that project's .claude/skills
#   install.sh -c -t ../my-project   COPY instead of link — editable, yours to change
#   install.sh -u                    remove the links this script created
#
# link (default): one copy on disk, in this repo. Editing a linked skill edits the repo.
# copy (-c):      independent files. Hackable, and they never see an update from here.
# Pick one per target. Doing both leaves every skill in twice.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="$HOME/.claude/skills"
MODE=link
FORCE=false

while getopts ":t:cuf" opt; do
  case $opt in
    t) TARGET="$(cd "$OPTARG" && pwd)/.claude/skills" ;;
    c) MODE=copy ;;
    u) MODE=uninstall ;;
    f) FORCE=true ;;
    *) echo "usage: $0 [-t project-dir] [-c] [-f] [-u] [category...]" >&2; exit 2 ;;
  esac
done
shift $((OPTIND - 1))

if [ $# -gt 0 ]; then
  CATEGORIES=("$@")
else
  CATEGORIES=()
  for dir in "$REPO"/*/; do
    # A category is a top-level folder holding at least one skill.
    compgen -G "${dir}*/SKILL.md" > /dev/null && CATEGORIES+=("$(basename "$dir")")
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
        if [ -e "$dest" ] && [ ! -L "$dest" ]; then
          echo "skip: $name already exists in $TARGET and is not a link" >&2
          skipped=$((skipped + 1))
          continue
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
