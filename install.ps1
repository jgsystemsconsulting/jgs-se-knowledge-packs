# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
#
# Thin wrapper around install.py so `./install.ps1 [--dry-run] [--flat] [--target DIR]`
# works on Windows PowerShell. All arguments pass through to install.py.
$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$python = (Get-Command python -ErrorAction SilentlyContinue)
if (-not $python) { $python = (Get-Command python3 -ErrorAction SilentlyContinue) }
if (-not $python) { Write-Error "Python not found on PATH."; exit 1 }
& $python.Source (Join-Path $here "install.py") @args
exit $LASTEXITCODE
