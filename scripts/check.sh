#!/usr/bin/env bash
# Validate the catalogue and refresh generated copies/links. --check is read-only.
set -euo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
exec python3 "$REPO/scripts/check_catalog.py" "$@"
