<!--
Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
SPDX-License-Identifier: MIT
-->

# Changelog

All notable changes to this project are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows
[Semantic Versioning](https://semver.org/).

## [1.3.0] — 2026-06-22

### Added

- **`dau-se-guidebook`** (6 ch) — DoD Systems Engineering Guidebook (OUSD R&E, Feb 2022):
  the DoD SE process model (16 processes — 8 technical management + 8 technical, mapped to
  ISO/IEC/IEEE 15288), event-driven technical reviews and audits (ASR/SRR/SFR/PDR/CDR/
  SVR-FCA/PRR/PCA), the Systems Engineering Plan (SEP), risk/issue/opportunity management,
  TPMs and leading indicators, system-of-systems and digital engineering, and the 24 design
  considerations. US-gov public domain (Distribution A).
- **`gao-tra`** (7 ch) — GAO Technology Readiness Assessment Guide (GAO-20-48G): Technology
  Readiness Levels (TRL 1–9) and related scales (MRL, IRL), Critical Technology Elements
  (CTEs), the five-step TRA process, the four characteristics of a reliable TRA, Technology
  Maturation Plans (TMPs), and knowledge-based milestone decisions. US-gov public domain
  (GAO reproduction notice).
- **`nist-sse`** (8 ch) — NIST SP 800-160 Vol 1 (Engineering Trustworthy Secure Systems) +
  Vol 2 (Developing Cyber-Resilient Systems): the three SSE framework contexts, 30+ design
  principles for trustworthy secure design, trustworthiness & assurance cases, security
  across the life-cycle process groups, and the cyber-resiliency engineering framework
  (4 goals, objectives, 14 techniques, design principles) for the APT threat model. US-gov
  public domain; references third-party ISO/IEC/IEEE 15288 material which is **not** reproduced.
- **`se-standards-signpost`** — a *signpost*, not a knowledge pack: maps the whole SE
  standards landscape (ISO/IEC/IEEE 15288/24748/29148/42010/15026/24765, INCOSE SE Handbook
  & Vision 2035, OMG SysML, SAE/EIA, ECSS, NATO AAP-48, CMMI, NIST SP 800-160, …) with each
  standard's owner, redistributability status, and where to get it. Zero reproduced content;
  Excluded standards point to the owner, open ones point to the real pack.

Catalogue now **16 live packs (+2 signposts)**.

## [1.2.1] — 2026-06-19

### Added

- **`omg-signpost`** — a *signpost*, not a knowledge pack: zero OMG content, just spec names,
  purposes, and the OMG download URL. OMG specs are Excluded (licence forbids packaging), so
  this points users to OMG instead. New `kind: signpost` marker; `check_release.py` exempts
  signposts from the link ban and pack-structure checks.

## [1.2.0] — 2026-06-19

### Added

- **`dodaf`** (11 ch) — DoD Architecture Framework 2.02 Change 1, Volume II: the eight DoDAF
  viewpoints (All / Capability / Data & Information / Operational / Project / Services /
  Standards / Systems), the DM2 meta-model, and fit-for-purpose model selection. US-gov
  public domain (Distribution A).
- **`eu-ai-act`** (12 ch) — EU Artificial Intelligence Act (Regulation (EU) 2024/1689):
  prohibited practices, high-risk classification & requirements, operator obligations,
  conformity assessment, GPAI models, transparency, governance, and Annex III. EU Official
  Journal (reproduction authorised with source acknowledgement).
- Both were deferred in v1.1.0 (automated source download blocked); built from user-supplied,
  title-verified PDFs. Catalogue now 13 live packs.

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
