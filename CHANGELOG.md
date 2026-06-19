<!--
Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
SPDX-License-Identifier: MIT
-->

# Changelog

All notable changes to this project are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows
[Semantic Versioning](https://semver.org/).

## [1.0.0] — 2026-06-19

### Added

- Initial release of the jgs-se-knowledge-packs catalogue.
- **`sebok`** pack — Guide to the Systems Engineering Body of Knowledge (SEBoK) v2.13,
  CC BY-NC-SA 3.0, 41 chapters plus glossary, patterns, and cheatsheet.
- Source-vetting rubric (`docs/SOURCE-VETTING.md`) — 3-tier eligibility + Excluded list.
- Licensing & reconstitution justification (`docs/LICENSING.md`).
- Pack contract (`docs/PACK-SPEC.md`) and usage guide (`docs/skill-usage.md`).
- Tooling: `tooling/validate_pack.py`, `tooling/build_pack.py`, `tooling/check_release.py`.
- Cross-platform installers (`install.py`, `install.sh`, `install.ps1`).
- Marketplace metadata (`.claude-plugin/`), `SKILLS.md` index, `NOTICE`, `COPYRIGHT`,
  `SECURITY.md`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, CI quality gate.

### Notes

- Repository tooling is MIT (JG Systems Consulting Ltd.). Pack content is licensed under
  each source's own licence — see `NOTICE` and each `packs/<slug>/LICENSE`.
- No source-material download links are published anywhere; attribution is textual. See
  `docs/LICENSING.md`.
