#!/usr/bin/env python3
"""Copy one skill with dereferenced resources, excluding local runtime caches."""
import shutil
import sys
from pathlib import Path


def copy_skill(source, destination):
    source, destination = Path(source), Path(destination)
    if source.resolve() == destination.resolve() or source.resolve() in destination.resolve().parents:
        raise ValueError('Cannot copy a skill onto itself or inside itself')
    shutil.copytree(source, destination, symlinks=False,
                    ignore=shutil.ignore_patterns('node_modules', '__pycache__', '*.pyc', '.venv', '.git'))


if __name__ == '__main__':
    copy_skill(sys.argv[1], sys.argv[2])
