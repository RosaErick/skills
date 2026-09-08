#!/usr/bin/env python3
"""Run configured checks. Exit 0 passed, 1 failed, 2 unverified. No auto-install."""
import json
import shutil
import subprocess
import sys
from pathlib import Path


def detect_project_type(project_path):
    root = Path(project_path)
    result = {'type': 'unknown', 'linters': [], 'warnings': []}
    manifest = root / 'package.json'
    if manifest.exists():
        result['type'] = 'node'
        try:
            package = json.loads(manifest.read_text())
            declared = package.get('packageManager', '').split('@')[0]
            locks = {manager for manager, names in {'npm': ['package-lock.json', 'npm-shrinkwrap.json'], 'pnpm': ['pnpm-lock.yaml'], 'yarn': ['yarn.lock'], 'bun': ['bun.lock', 'bun.lockb']}.items() if any((root / name).exists() for name in names)}
            if declared and declared not in {'npm', 'pnpm', 'yarn', 'bun'}:
                result['warnings'].append(f'Unsupported package manager: {declared}')
                return result
            if (declared and locks - {declared}) or len(locks) > 1:
                result['warnings'].append('Conflicting package manager/lockfile configuration; use the actual project command')
                return result
            manager = declared or next(iter(locks), 'npm')
            for name in ('lint', 'typecheck', 'type-check', 'check:types'):
                if name in package.get('scripts', {}):
                    result['linters'].append({'name': name, 'cmd': [manager, 'run', name]})
        except (ValueError, OSError) as error:
            result['warnings'].append(str(error))
    pyproject = root / 'pyproject.toml'
    if pyproject.exists():
        result['type'] = 'mixed' if result['type'] == 'node' else 'python'
        try:
            import tomllib
            config = tomllib.loads(pyproject.read_text()).get('tool', {})
            prefix = ['uv', 'run', '--no-sync'] if (root / 'uv.lock').exists() else []
            if 'ruff' in config:
                result['linters'].append({'name': 'ruff', 'cmd': prefix + ['ruff', 'check', '.']})
            if 'mypy' in config:
                result['linters'].append({'name': 'mypy', 'cmd': prefix + ['mypy', '.']})
        except (ImportError, ValueError, OSError) as error:
            result['warnings'].append(str(error))
    return result


def run_linter(linter, cwd):
    command = list(linter['cmd'])
    executable = shutil.which(command[0])
    if not executable:
        return {'name': linter['name'], 'cmd': command, 'status': 'unverified', 'passed': None, 'error': f'Command not found: {command[0]}'}
    command[0] = executable
    try:
        result = subprocess.run(command, cwd=cwd, capture_output=True, text=True, timeout=120)
        return {'name': linter['name'], 'cmd': command, 'status': 'passed' if result.returncode == 0 else 'failed', 'passed': result.returncode == 0, 'returncode': result.returncode, 'output': result.stdout, 'error': result.stderr}
    except (OSError, subprocess.TimeoutExpired) as error:
        return {'name': linter['name'], 'cmd': command, 'status': 'unverified', 'passed': None, 'error': str(error)}


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
    if not root.is_dir():
        print(json.dumps({'status': 'unverified', 'passed': None, 'error': 'Project directory does not exist'}))
        return 2
    detected = detect_project_type(root)
    results = [run_linter(check, root) for check in detected['linters']]
    status = 'failed' if any(r['status'] == 'failed' for r in results) else 'unverified' if detected['warnings'] or not results or any(r['status'] == 'unverified' for r in results) else 'passed'
    print(json.dumps({'project': str(root), 'type': detected['type'], 'status': status, 'passed': {'passed': True, 'failed': False, 'unverified': None}[status], 'checks': results, 'warnings': detected['warnings']}, indent=2))
    return {'passed': 0, 'failed': 1, 'unverified': 2}[status]


if __name__ == '__main__':
    raise SystemExit(main())
