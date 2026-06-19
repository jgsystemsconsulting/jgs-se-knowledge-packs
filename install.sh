#!/usr/bin/env bash
# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
#
# Thin wrapper around install.py so `./install.sh [--dry-run] [--flat] [--target DIR]`
# works on Unix-like systems. All arguments pass through to install.py.
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="${PYTHON:-python3}"
command -v "$PYTHON" >/dev/null 2>&1 || PYTHON="python"
exec "$PYTHON" "$DIR/install.py" "$@"
