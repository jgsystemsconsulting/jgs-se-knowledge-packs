<!--
Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
SPDX-License-Identifier: MIT
-->

# Changelog

All notable changes to this project are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows
[Semantic Versioning](https://semver.org/).

## [1.6.0] — 2026-06-23

### Added

- **`faa-sem`** (7 ch) — FAA Systems Engineering Manual (SEM) v1.0.1: civil-agency SE as the FAA
  practices it inside the Acquisition Management System (AMS) and the National Airspace System —
  the five-phase AMS lifecycle and its five decision points, operational concept development and
  implementation-free functional analysis (ConOps, FFBD/N², CMLs), requirements and architecture
  synthesis (PRS→MRS, the pPRD→iPRD→fPRD ratchet, RAM, CPRs), the seven technical management
  disciplines (Integrated Technical Management/SEMP, Interface Management/IRD-ICD, Risk-Issue-
  Opportunity, Configuration Management, SE Information Management, Decision Analysis, V&V), and the
  specialty disciplines (RMA via Service Threads, Life Cycle Engineering, E3/Spectrum, Human
  Factors, Information Security via the NIST RMF, System Safety via the SMS, environmental/EOSH).
  Tier 1 (US-gov public domain).
- **`nasa-schedule`** (8 ch) — NASA Schedule Management Handbook (2024 ed., Rev 2): program/project
  schedule management of aerospace and large engineering efforts — the five sub-functions (Planning,
  Development, Assessment & Analysis, Maintenance & Control, Documentation & Communication), the
  Integrated Master Schedule (IMS) and WBS/OBS/CBS, the Schedule Management Plan (SMP) and Basis of
  Estimate, Critical Path Method, float and margin, tiered schedule assessment (the Shock Test, the
  Dimensions of Schedule Reliability), Schedule Risk Analysis (SRA), Integrated Cost-Schedule Risk
  Analysis (ICSRA), Monte Carlo and the Joint Confidence Level (JCL), baselining vs. replan vs.
  rebaseline, and EVM schedule metrics (SPI, BEI, CEI, Earned Schedule, CPLI). Grounded in NPR
  7120.5 and the GAO Schedule Assessment Guide. Tier 1 (US-gov public domain).
- **`dod-mosa`** (7 ch) — *Implementing a Modular Open Systems Approach in DoD Programs* (OUSD R&E,
  Feb 2025): MOSA as a DoD acquisition + design discipline — the statutory/regulatory basis
  (10 U.S.C. 4401–4403, FY2017/FY2021 NDAA, DFARS), the five OUSD(R&E) pillars, the
  plan→modularize→identify→define→standardize interface lifecycle, technical levers (WBS/
  MIL-STD-881F taxonomy, standards profiling, API-first software, COTS/cybersecurity), MOSA
  assessment metrics and tools (PART/OAAT/KOSS/SEAM/MAUT), technology-change and DMSMS management,
  roadmaps, MOSA across the six AAF pathways, and contracting/IP/data-rights mechanics. Names
  third-party standards (FACE, OMS, DISR) without reproducing them. Tier 1 (US-gov public domain,
  Distribution A).

Catalogue now 24 packs (+2 signposts).

## [1.5.0] — 2026-06-23

### Added

- **`nasa-pra`** (8 ch) — NASA Probabilistic Risk Assessment Procedures Guide (NASA/SP-2011-3421,
  2nd ed., 2011): the quantitative PRA engine — the risk triplet and scenario logic stack (MLD,
  ESD, event trees, fault trees, minimal cut sets), Bayesian data collection and parameter
  estimation, aleatory/epistemic uncertainty and common-cause failure (Alpha Factor, beta-factor,
  CCBE), human reliability analysis (THERP, CREAM, NARA, SPAR-H), context-based software risk
  (CSRM), physics-based/structural models (stress-strength, FORM/SORM, NASGRO), uncertainty
  propagation and importance measures (F-V, RAW, Birnbaum, DIM), and launch-abort modeling with
  worked examples. The quantitative engine beneath NASA's risk doctrine; pairs with the
  qualitative RIDM/CRM framework in `nasa-risk`. Tier 1 (US-gov public domain).
- **`nasa-se-expanded`** (6 ch) — Expanded Guidance for NASA Systems Engineering
  (NASA/SP-2016-6105-SUPPL, Vol 1, March 2016): the practitioner-depth supplement to the NASA SE
  Handbook — the SE Engine's per-phase cadence and iterative-vs-recursive distinction, life-cycle
  tailoring vs. customization and the Compliance Matrix, the recursive system-design consistency
  loop (ConOps, requirement flow/type/ownership), product realization (verify/qualify/accept/
  certify cardinality, protoflight, 'test the way we fly'), and crosscutting technical management
  (six-step scheduling, cost estimating, JCL, interface document family, RIDM/CRM, CM baselines,
  EVM, MOE/MOP/KPP/TPM, leading indicators, decision-analysis methods). The depth layer over the
  base `nasa-se-handbook` pack. Tier 1 (US-gov public domain).

Catalogue now 21 packs (+2 signposts).

## [1.4.0] — 2026-06-23

### Added

- **`nist-800-37`** (7 ch) — NIST SP 800-37 Rev 2, the Risk Management Framework: the seven steps
  (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor), tasks and roles, control
  selection/tailoring, and the assess–authorize–monitor loop. Tier 1 (US-gov public domain).
- **`nist-cps`** (8 ch) — NIST Framework for Cyber-Physical Systems (SP 1500-201/202/203): the
  three facets (conceptualization, realization, assurance), the nine aspects, the CPS reference
  architecture, and trustworthiness/timing/data concerns. Tier 1 (US-gov public domain).
- **`digital-systems-engineering`** (7 ch) — *Towards Digital Engineering* (arXiv:2002.11672):
  the digital-engineering/DSE conceptual framework, the DoD Digital Engineering Strategy goals,
  the Authoritative Source of Truth, digitalization vs digitization, and the four-level
  (vision/strategy/action/foundation) research framework. Tier 2 (CC BY 4.0, attribution).

Catalogue now 19 packs (+2 signposts).

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
