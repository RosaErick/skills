#!/usr/bin/env bash
# Validate the skills and regenerate the flat skills/ folder the plugin manifests point at.
#
#   scripts/check.sh           validate, and rebuild skills/ if it drifted
#   scripts/check.sh --check   validate only, touch nothing (for CI and hooks)
#
# A skill is a directory directly under a category directory containing a SKILL.md.
# Nested SKILL.md files (templates, sub-documents) are not skills.
set -euo pipefail
shopt -s nullglob

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO"

CHECK_ONLY=false
[ "${1:-}" = "--check" ] && CHECK_ONLY=true

problems=0
note() { printf '%s\n' "$1"; problems=$((problems + 1)); }

# The value of a top-level frontmatter key, quotes stripped.
field() {
  awk -v key="$2" '
    NR == 1 && $0 != "---" { exit }
    /^---$/ { fence++; if (fence == 2) exit; next }
    fence == 1 && index($0, key ":") == 1 {
      sub("^" key ":[ \t]*", ""); gsub(/^["'"'"']|["'"'"']$/, ""); print; exit
    }' "$1"
}

# A category is a top-level folder holding at least one skill. skills/ is the generated
# mirror and scripts/ holds these files, so neither is one.
categories=()
for dir in */; do
  dir="${dir%/}"
  case "$dir" in skills | scripts) continue ;; esac
  compgen -G "$dir/*/SKILL.md" > /dev/null && categories+=("$dir")
done

# --- frontmatter, and every skill listed in its category README -----------------------
total=0
declare -A count_of
for category in "${categories[@]}"; do
  readme="$category/README.md"
  [ -f "$readme" ] || note "$category/: missing README.md"
  count_of["$category"]=0
  for skill in "$category"/*/; do
    skill="${skill%/}"
    name="$(basename "$skill")"
    [ -f "$skill/SKILL.md" ] || continue
    count_of["$category"]=$(( count_of["$category"] + 1 ))
    total=$((total + 1))

    declared="$(field "$skill/SKILL.md" name)"
    if [ -z "$declared" ]; then
      note "$category/$name: frontmatter has no name"
    elif [ "$declared" != "$name" ]; then
      note "$category/$name: frontmatter name is '$declared', folder is '$name'"
    fi
    [ -n "$(field "$skill/SKILL.md" description)" ] ||
      note "$category/$name: frontmatter has no description"
    if [ -f "$readme" ] && ! grep -qF "$name" "$readme"; then
      note "$category/$name: not listed in $readme"
    fi
  done
done

# --- duplicates ------------------------------------------------------------------------
while read -r name; do
  [ -n "$name" ] && note "$name: two skills share this name"
done < <(find . -mindepth 3 -maxdepth 3 -name SKILL.md -not -path './skills/*' |
  awk -F/ '{ print $3 }' | sort | uniq -d)

while read -r _ path; do
  [ -n "${path:-}" ] && note "$path: SKILL.md is byte-identical to another skill's"
done < <(for category in "${categories[@]}"; do md5sum "$category"/*/SKILL.md 2>/dev/null; done |
  sort | uniq -Dw32)

# --- dead relative links, in the READMEs and inside the skills --------------------------
# Fenced code blocks are skipped: a type hint or a path in an example is not a link.
links_in() {
  awk '
    /^[ \t]*```/ { fenced = !fenced; next }
    fenced { next }
    { line = $0
      while (match(line, /\]\([^)#]+\)/)) {
        target = substr(line, RSTART + 2, RLENGTH - 3)
        if (target !~ /^(http|mailto|#)/ && target !~ /[ \t]/) print target
        line = substr(line, RSTART + RLENGTH)
      } }' "$1"
}

for doc in README.md */README.md */*/*.md */*/*/*.md; do
  case "$doc" in skills/* | scripts/*) continue ;; esac
  [ -f "$doc" ] || continue
  while read -r target; do
    [ -e "$(dirname "$doc")/$target" ] || note "$doc: dead link $target"
  done < <(links_in "$doc")
done

# --- the counts in the root README ------------------------------------------------------
# The table cells are pipe-delimited, so awk splits them and the count is the last real column.
count_cell() { awk -F'|' -v want="$1" 'index($2, want) { gsub(/[^0-9]/, "", $(NF - 1)); print $(NF - 1); exit }' README.md; }

for category in "${categories[@]}"; do
  stated="$(count_cell "[$category]")"
  [ -n "$stated" ] || continue
  [ "$stated" = "${count_of[$category]}" ] ||
    note "README.md: $category says $stated, actual ${count_of[$category]}"
done
stated_total="$(count_cell '**Total**')"
[ -z "$stated_total" ] || [ "$stated_total" = "$total" ] ||
  note "README.md: total says $stated_total, actual $total"
stated_headline="$(sed -n 's/.*skills — \([0-9][0-9]*\) of them.*/\1/p' README.md | head -1)"
[ -z "$stated_headline" ] || [ "$stated_headline" = "$total" ] ||
  note "README.md: headline says $stated_headline, actual $total"

# --- the flat skills/ folder the plugin manifests point at -------------------------------
declare -A want
for category in "${categories[@]}"; do
  for skill in "$category"/*/; do
    skill="${skill%/}"
    [ -f "$skill/SKILL.md" ] || continue
    want["$(basename "$skill")"]="../$category/$(basename "$skill")"
  done
done

drifted=false
for name in "${!want[@]}"; do
  [ "$(readlink "skills/$name" 2>/dev/null || true)" = "${want[$name]}" ] || drifted=true
done
for entry in skills/*; do
  [ -n "${want[$(basename "$entry")]:-}" ] || drifted=true
done

if $drifted; then
  if $CHECK_ONLY; then
    note "skills/: plugin bundle is out of sync (run scripts/check.sh)"
  else
    rm -rf skills
    mkdir skills
    for name in "${!want[@]}"; do ln -s "${want[$name]}" "skills/$name"; done
    printf 'skills/: plugin bundle rebuilt (%d skills)\n' "${#want[@]}"
  fi
fi

if [ "$problems" -gt 0 ]; then
  printf '\n%d problem(s)\n' "$problems"
  exit 1
fi
printf '%d skills, all valid\n' "$total"
