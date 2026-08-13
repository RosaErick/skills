#!/usr/bin/env python3
"""Check that every acceptance criterion is bound to a test, and vice versa.

    python3 verify-criteria.py                          # docs/specs + whole repo
    python3 verify-criteria.py --specs docs/specs --tests test src
    python3 verify-criteria.py --quiet                  # only the failures

Criteria are read from `### AC-<n> — title` headings in the spec files. A binding is the same id
appearing in a test name, in any of the AC-1 / AC_1 / AC 1 spellings. Superseded criteria (struck
through with ~~AC-3~~) and criteria marked `not-tested:` are reported separately, not as failures.

Exit code 1 if anything is uncovered, orphaned or skipped-only.
"""
import argparse
import re
import sys
from pathlib import Path

HEADING = re.compile(r"^###\s+(~~)?(AC[-_ ]?(\d+))(~~)?\s*(?:—|-|–)?\s*(.*)$", re.I)
NOT_TESTED = re.compile(r"\bnot-tested:", re.I)
CITATION = re.compile(r"(?<![A-Za-z0-9])AC[-_ ]?(\d+)(?![A-Za-z0-9])", re.I)
SKIPPED = re.compile(r"\b(skip|xit|xtest|todo|pending)\b", re.I)
TEST_FILE = re.compile(r"(test|spec)", re.I)
CODE_SUFFIX = {".ts", ".tsx", ".js", ".jsx", ".mjs", ".py", ".go", ".rb", ".rs", ".java", ".kt",
               ".php", ".cs", ".swift", ".ex", ".exs"}
IGNORE_DIR = {".git", "node_modules", "dist", "build", "vendor", "__pycache__", ".venv", "venv",
              "target", "coverage", ".next"}


def read_criteria(spec_dir: Path):
    """{id: {title, file, superseded, not_tested}} for every criterion in every spec file."""
    criteria = {}
    for spec in sorted(spec_dir.rglob("*.md")):
        lines = spec.read_text(encoding="utf-8").splitlines()
        for i, line in enumerate(lines):
            m = HEADING.match(line)
            if not m:
                continue
            cid = f"AC-{int(m.group(3))}"
            # The criterion's body ends at the next heading of any level.
            body_lines = []
            for following in lines[i + 1:]:
                if following.startswith("#"):
                    break
                body_lines.append(following)
            body = "\n".join(body_lines)
            criteria[cid] = {
                "title": m.group(5).strip(),
                "file": f"{spec}:{i + 1}",
                "superseded": bool(m.group(1)),
                "not_tested": bool(NOT_TESTED.search(body)),
            }
    return criteria


def read_citations(roots):
    """{id: [(location, is_skipped)]} for every AC id cited in a test file."""
    citations = {}
    for root in roots:
        for path in Path(root).rglob("*"):
            if (not path.is_file() or path.suffix not in CODE_SUFFIX
                    or set(path.parts) & IGNORE_DIR
                    or not TEST_FILE.search(str(path))):
                continue
            try:
                lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
            except OSError:
                continue
            for i, line in enumerate(lines):
                for number in CITATION.findall(line):
                    cid = f"AC-{int(number)}"
                    citations.setdefault(cid, []).append(
                        (f"{path}:{i + 1}", bool(SKIPPED.search(line)))
                    )
    return citations


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--specs", default="docs/specs")
    parser.add_argument("--tests", nargs="*", default=["."])
    parser.add_argument("--quiet", action="store_true", help="print only failures")
    args = parser.parse_args()

    spec_dir = Path(args.specs)
    if not spec_dir.is_dir():
        print(f"no spec directory at {spec_dir}", file=sys.stderr)
        return 2

    criteria = read_criteria(spec_dir)
    if not criteria:
        print(f"no criteria found in {spec_dir} (expected '### AC-1 — title' headings)")
        return 2
    citations = read_citations(args.tests)

    uncovered, skipped_only, orphaned, covered, excused = [], [], [], [], []

    for cid, meta in sorted(criteria.items(), key=lambda kv: int(kv[0].split("-")[1])):
        hits = citations.get(cid, [])
        live = [loc for loc, is_skipped in hits if not is_skipped]
        if meta["superseded"]:
            continue
        if meta["not_tested"]:
            excused.append((cid, meta))
        elif live:
            covered.append((cid, meta, live))
        elif hits:
            skipped_only.append((cid, meta, [loc for loc, _ in hits]))
        else:
            uncovered.append((cid, meta))

    known = {cid for cid, meta in criteria.items() if not meta["superseded"]}
    for cid, hits in sorted(citations.items(), key=lambda kv: int(kv[0].split("-")[1])):
        if cid not in known:
            orphaned.append((cid, [loc for loc, _ in hits]))

    if not args.quiet:
        for cid, _meta, live in covered:
            print(f"{cid:<7} covered    {', '.join(live)}")
        for cid, meta in excused:
            print(f"{cid:<7} not-tested (declared)  {meta['file']}")
    for cid, meta, locs in skipped_only:
        print(f"{cid:<7} SKIPPED    only skipped tests cite it: {', '.join(locs)}")
    for cid, meta in uncovered:
        print(f"{cid:<7} UNCOVERED  {meta['title']}  ({meta['file']})")
    for cid, locs in orphaned:
        print(f"{cid:<7} ORPHANED   cited by {', '.join(locs)} but in no spec")

    failures = len(uncovered) + len(skipped_only) + len(orphaned)
    total = len(covered) + len(excused) + failures
    print(f"\n{len(covered)}/{total} proven, {len(excused)} declared not-tested, {failures} problem(s)")
    print("Contradiction between a criterion and the code is not mechanical — read for it.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
