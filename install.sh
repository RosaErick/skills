#!/usr/bin/env bash
# Link skills from this repo into a place an agent actually reads.
#
#   ./install.sh                          all categories -> ~/.claude/skills
#   ./install.sh frontend backend         only those categories -> ~/.claude/skills
#   ./install.sh -t path/to/project       all categories -> <project>/.claude/skills
#   ./install.sh -t path/to/project quality
#   ./install.sh -u [categories...]       remove the links this script created
#
# Skills are linked one folder at a time: agents look for <target>/<skill>/SKILL.md,
# so linking a whole category folder would hide everything inside it.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET="$HOME/.claude/skills"
UNINSTALL=false

while getopts ":t:u" opt; do
  case $opt in
    t) TARGET="$(cd "$OPTARG" && pwd)/.claude/skills" ;;
    u) UNINSTALL=true ;;
    *) echo "usage: $0 [-t project-dir] [-u] [category...]" >&2; exit 2 ;;
  esac
done
shift $((OPTIND - 1))

if [ $# -gt 0 ]; then
  CATEGORIES=("$@")
else
  CATEGORIES=()
  for dir in "$REPO"/*/; do
    [ -f "${dir}README.md" ] && CATEGORIES+=("$(basename "$dir")")
  done
fi

mkdir -p "$TARGET"
linked=0 removed=0 skipped=0

for category in "${CATEGORIES[@]}"; do
  if [ ! -d "$REPO/$category" ]; then
    echo "skip: no such category: $category" >&2
    continue
  fi
  for skill in "$REPO/$category"/*/; do
    [ -f "${skill}SKILL.md" ] || continue
    name="$(basename "$skill")"
    link="$TARGET/$name"

    if $UNINSTALL; then
      # Only remove links that point back into this repo — never touch real folders.
      if [ -L "$link" ] && [[ "$(readlink "$link")" == "$REPO"/* ]]; then
        rm "$link"
        removed=$((removed + 1))
      fi
      continue
    fi

    if [ -e "$link" ] && [ ! -L "$link" ]; then
      echo "skip: $name already exists in $TARGET and is not a link" >&2
      skipped=$((skipped + 1))
      continue
    fi
    ln -sfn "${skill%/}" "$link"
    linked=$((linked + 1))
  done
done

if $UNINSTALL; then
  echo "removed $removed link(s) from $TARGET"
else
  echo "linked $linked skill(s) into $TARGET${skipped:+, skipped $skipped}"
fi
