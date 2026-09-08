#!/usr/bin/env python3
"""Collect local content signals. Does not predict indexing, citations or ranking."""
import argparse
import json
import os
import re
from pathlib import Path

SKIP = {'.git', 'node_modules', '.venv', 'dist', 'build', '.next', '__pycache__'}


def find_web_pages(target):
    target = Path(target)
    if target.is_file():
        return [target]
    files = []
    for root, dirs, names in os.walk(target):
        dirs[:] = [name for name in dirs if name not in SKIP]
        files.extend(Path(root) / name for name in names if Path(name).suffix.lower() in {'.html', '.htm', '.jsx', '.tsx', '.md', '.mdx'})
    return sorted(files)


def check_page(file_path):
    path = Path(file_path)
    try:
        content = path.read_text(encoding='utf-8')
    except (OSError, UnicodeError) as error:
        return {'file': str(path), 'status': 'unverified', 'error': str(error)}
    return {'file': str(path), 'status': 'observed', 'signals': {
        'json_ld_marker': 'application/ld+json' in content,
        'h1_tags': len(re.findall(r'<h1\b', content, re.I)),
        'heading_tags': len(re.findall(r'<h[2-6]\b', content, re.I)),
        'attribution_marker': bool(re.search(r'author|byline|rel=["\x27]author', content, re.I)),
        'date_marker': bool(re.search(r'datePublished|dateModified|datetime=', content, re.I)),
        'link_markers': len(re.findall(r'<a\b|\]\(https?://', content, re.I)),
    }, 'interpretation': 'Source-text markers only; inspect rendered content, truthfulness and the target provider policy.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('target', nargs='?', default='.')
    args = parser.parse_args()
    files = find_web_pages(args.target)
    results = [check_page(path) for path in files]
    unverified = not results or any(result['status'] == 'unverified' for result in results)
    print(json.dumps({'status': 'unverified' if unverified else 'observed', 'files_checked': len(results),
        'limitation': 'No ranking/citation score or visibility guarantee. Source files may not be public pages.', 'results': results}, indent=2))
    return 2 if unverified else 0


if __name__ == '__main__':
    raise SystemExit(main())
