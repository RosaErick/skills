#!/usr/bin/env python3
"""Remove only retired symlinks owned by this checkout, within selected categories."""
import argparse
import json
from pathlib import Path


def migrate(target, categories, repo):
    retired = json.loads((repo / 'scripts/retired-skills.json').read_text())
    removed = []
    for old in retired:
        category, name = old.split('/')
        if category not in categories:
            continue
        link = target / name
        if not link.is_symlink():
            continue
        raw = link.readlink()
        destination = (raw if raw.is_absolute() else link.parent / raw).resolve()
        owned = {(repo / old).resolve(), (repo / 'skills' / name).resolve()}
        if destination in owned:
            link.unlink()
            removed.append(name)
    return removed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('target', type=Path)
    parser.add_argument('categories', nargs='+')
    args = parser.parse_args()
    removed = migrate(args.target, args.categories, Path(__file__).resolve().parent.parent)
    if removed:
        print('Removed retired checkout links: ' + ', '.join(removed))


if __name__ == '__main__':
    main()
