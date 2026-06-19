<!--
Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
SPDX-License-Identifier: MIT
-->

# Changelog

All notable changes to this project are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows
[Semantic Versioning](https://semver.org/).

## [1.1.0] — 2026-06-19

### Added

- **Nine new packs**, all Tier-1 public-domain or Tier-2 open:
  - `nasa-npr-7123` (NASA SE process requirements), `nasa-risk` (Risk Management Handbook),
    `nasa-system-safety` (System Safety Handbook v2), `nasa-hsi` (Human Systems Integration).
  - `nist-ai-rmf` (AI Risk Management Framework 1.0), `nist-ssdf` (SP 800-218), `nist-csf` (CSF 2.0).
  - `mil-std-882` (DoD System Safety).
  - `requirements-writing` (original guidance: EARS patterns + requirement quality, CC BY 4.0 —
    cites methods rather than reproducing ISO 29148 / the EARS paper).
- `docs/PACK-BACKLOG.md` source ledger; `docs/SOURCE-VETTING.md` Excluded list extended
  (OMG `formal/` corpus, NAF, DAU). `eu-ai-act` and `dodaf` deferred (source download blocked).

### Removed

- **`omg-sysml`** pack — pulled from the catalogue. The OMG Specification License public grant
  permits only informational, unmodified, non-network-posted use ("will not be copied or posted
  on any network computer" and "no modifications are made to this specification"), so a hosted,
  transformed knowledge pack is not redistributable. OMG `formal/` specifications (UML, SysML,
  BPMN, UAF, …) are now on the Excluded list (`docs/SOURCE-VETTING.md`), confirmed by two
  independent licence reads. (Shipped in error in v1.0.0; that tag was private and never published.)

## [1.0.0] — 2026-06-19

### Added

- Initial release of the jgs-se-knowledge-packs catalogue.
- **`sebok`** pack — Guide to the Systems Engineering Body of Knowledge (SEBoK) v2.13,
  CC BY-NC-SA 3.0, 41 chapters plus glossary, patterns, and cheatsheet.
- **`nasa-se-handbook`** pack — NASA Systems Engineering Handbook (NASA/SP-2016-6105 Rev 2),
  public domain (US gov), 34 chapters (the SE Engine and 17 processes, project life cycle,
  V&V, crosscutting technical management) plus glossary, patterns, and cheatsheet.
- **`omg-sysml`** pack — OMG Systems Modeling Language (SysML) v1.6, OMG Specification License,
  11 clause chapters (blocks, ports & flows, constraint blocks, behaviour, allocations,
  requirements, profiles) plus glossary, patterns, and cheatsheet.
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
