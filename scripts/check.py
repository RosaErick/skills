#!/usr/bin/env python3
"""Validate the skills in this repo and refresh the counts in README.md.

Usage:
    python3 scripts/check.py           validate, refresh the README counts and the
                                      flat skills/ bundle the plugin ships
    python3 scripts/check.py --check   validate only; exit 1 if anything is off (for CI)

A skill is a directory directly under a category directory containing a SKILL.md.
Nested SKILL.md files (templates, sub-documents) are not skills.
"""
import os
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = {".git", "__pycache__", "scripts", "skills"}


def categories():
    """A category is a top-level directory holding at least one skill."""
    return sorted(
        d for d in ROOT.iterdir()
        if d.is_dir() and d.name not in SKIP and not d.name.startswith(".")
        and any(sub.joinpath("SKILL.md").is_file() for sub in d.iterdir() if sub.is_dir())
    )


def skills(category):
    return sorted(d for d in category.iterdir() if (d / "SKILL.md").is_file())


def frontmatter(skill_md):
    """Return the frontmatter block as a dict of top-level keys, or None if absent."""
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fields = {}
    for line in text[4:end].split("\n"):
        m = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if m:
            fields[m.group(1)] = m.group(2).strip().strip('"\'')
    return fields


def validate():
    problems = []
    for category in categories():
        readme = category / "README.md"
        if not readme.is_file():
            problems.append(f"{category.name}/: missing README.md")
        for skill in skills(category):
            rel = f"{category.name}/{skill.name}"
            fm = frontmatter(skill / "SKILL.md")
            if fm is None:
                problems.append(f"{rel}: SKILL.md has no frontmatter block")
                continue
            name = fm.get("name")
            if not name:
                problems.append(f"{rel}: frontmatter has no name")
            elif name != skill.name:
                problems.append(f"{rel}: frontmatter name is '{name}', folder is '{skill.name}'")
            description = fm.get("description")
            if not description:
                problems.append(f"{rel}: frontmatter has no description")
            if readme.is_file() and skill.name not in readme.read_text(encoding="utf-8"):
                problems.append(f"{rel}: not listed in {category.name}/README.md")
    return problems


def dead_links():
    """Relative markdown links in READMEs that point at nothing."""
    problems = []
    for readme in [ROOT / "README.md"] + [c / "README.md" for c in categories()]:
        if not readme.is_file():
            continue
        for target in re.findall(r"\]\((\./[^)#]+)\)", readme.read_text(encoding="utf-8")):
            if not (readme.parent / target).exists():
                problems.append(f"{readme.relative_to(ROOT)}: dead link {target}")
    return problems


def duplicates():
    """Two skills with the same folder name, or with byte-identical SKILL.md."""
    problems = []
    by_name, by_body = {}, {}
    for category in categories():
        for skill in skills(category):
            rel = f"{category.name}/{skill.name}"
            if skill.name in by_name:
                problems.append(f"{rel}: same skill name as {by_name[skill.name]}")
            by_name[skill.name] = rel
            body = (skill / "SKILL.md").read_bytes()
            if body in by_body:
                problems.append(f"{rel}: SKILL.md is identical to {by_body[body]}")
            by_body[body] = rel
    return problems


def refresh_plugin(check_only):
    """Mirror every skill as a flat symlink under skills/, the layout a plugin expects."""
    flat = ROOT / "skills"
    wanted = {s.name: f"../{c.name}/{s.name}" for c in categories() for s in skills(c)}
    if not flat.exists():
        if check_only:
            return ["skills/: plugin bundle missing (run python3 scripts/check.py)"]
        flat.mkdir()
    current = {p.name: os.readlink(p) for p in flat.iterdir() if p.is_symlink()}
    stale = [p for p in flat.iterdir() if p.name not in wanted]
    if current == wanted and not stale:
        return []
    if check_only:
        return ["skills/: plugin bundle is out of sync (run python3 scripts/check.py)"]
    for p in stale:
        p.unlink() if p.is_symlink() else shutil.rmtree(p)
    for name, target in wanted.items():
        link = flat / name
        if link.is_symlink():
            link.unlink()
        link.symlink_to(target)
    print(f"skills/: plugin bundle refreshed ({len(wanted)} skills)")
    return []


def counts():
    return {c.name: len(skills(c)) for c in categories()}


def refresh_readme(check_only):
    """Rewrite the per-category and total counts in the root README table."""
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    current = counts()
    total = sum(current.values())

    def row(match):
        name, middle, number = match.group(1), match.group(2), match.group(3)
        return f"| [{name}](./{name}/README.md) |{middle}| {current.get(name, number)} |"

    updated = re.sub(r"\| \[(\w+)\]\(\./\w+/README\.md\) \|(.*?)\| (\d+) \|", row, text)
    updated = re.sub(r"\| \*\*Total\*\* \| \| \*\*\d+\*\* \|",
                     f"| **Total** | | **{total}** |", updated)
    updated = re.sub(r"^My agent skills — \d+ of them",
                     f"My agent skills — {total} of them", updated, flags=re.M)

    if updated == text:
        return []
    if check_only:
        return ["README.md: counts are stale (run python3 scripts/check.py)"]
    readme.write_text(updated, encoding="utf-8")
    print(f"README.md: counts refreshed ({total} skills)")
    return []


def main():
    check_only = "--check" in sys.argv
    problems = (validate() + duplicates() + dead_links()
                + refresh_readme(check_only) + refresh_plugin(check_only))
    for p in problems:
        print(p)
    if problems:
        print(f"\n{len(problems)} problem(s)")
        return 1
    print(f"{sum(counts().values())} skills, all valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
