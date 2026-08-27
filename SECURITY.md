<!--
Copyright (c) 2026 JG Systems Consulting Ltd. MIT License (see LICENSE).
SPDX-License-Identifier: MIT
-->

# Security & Licensing Policy

## Reporting a vulnerability

Report privately to **`support@jgsystemsconsulting.com`**. Please do **not** open a
public issue for a security report.

- Include a description, affected files/packs, and reproduction steps.
- Expect an acknowledgement within **5 working days**.
- Please allow private disclosure: give us a reasonable window to remediate before any
  public discussion.

This is open-source software provided under the MIT licence (tooling) with no warranty.
There is **no bug-bounty programme**; reports are handled on a best-effort basis.

## Reporting a licensing concern

This catalogue's integrity depends on every pack being lawfully redistributable. If you
believe a pack misrepresents its source's licence, includes Excluded-source material, or
otherwise should not be redistributed, report it to the same address with the `licensing`
subject line. **Licensing reports are triaged first:** we would rather pull a pack than
ship one that should not be redistributed. See [docs/SOURCE-VETTING.md](docs/SOURCE-VETTING.md)
and [docs/LICENSING.md](docs/LICENSING.md).

## Scope

Packs are plain Markdown and the tooling is stdlib Python; there is no runtime server,
network service, or credential handling in this repository.

## Accepted risks

Logged accepted risks for the capability-map generator work (Phases 19 and 20). These are
record-keeping entries only; they do not change the reporting policy above.

### T-20-SC / T-19-SC (supply chain, high)

**Risk:** third-party package installs could enter the map tooling path.

**Acceptance:** tooling under `tooling/` is stdlib Python only. These phases do not add
pip, npm, or cargo installs. Avoidance is verified by import scan of the generator and
checkers, plus Phase 19/20 commit file lists that contain no `requirements.txt`,
`pyproject.toml`, or `package.json`.

**Why accepted:** this catalogue has no runtime server, and CI does not execute repo
Python for map generation or checkers.

**Review cadence:** re-confirm each phase that no dependency manifest appeared in the
phase commit set or under `tooling/`.

### T-20-08 / T-19-05 (FAIL line disclosure, low)

**Risk:** checker and generator FAIL lines print pack slugs and chapter basenames.

**Acceptance:** those strings are already public tree names in this repository. The
messages name existing pack directories and chapter files; they do not introduce private
paths or secrets.
