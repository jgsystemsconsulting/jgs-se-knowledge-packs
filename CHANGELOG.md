<!--
Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
SPDX-License-Identifier: MIT
-->

# Changelog

All notable changes to this project are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows
[Semantic Versioning](https://semver.org/).

## [1.10.0] — 2026-06-24

### Added

- **`gao-cost`** (8 ch) — GAO Cost Estimating and Assessment Guide (GAO-20-195G, March 2020):
  GAO's cross-government best-practice authority on program cost estimating — the four
  characteristics of a reliable estimate (comprehensive, well documented, accurate, credible) and
  the 18 best practices, the 12-step cost estimating process (purpose, plan, technical baseline,
  WBS, ground rules and assumptions, data, point estimate, sensitivity, risk/uncertainty,
  document, present, update), the estimating methods (analogy, parametric/CER, engineering
  build-up, learning curves), Monte Carlo risk/uncertainty analysis with confidence levels and
  contingency, auditing and validating an estimate against the four characteristics, earned value
  management (EIA-748, BCWS/BCWP/ACWP, CPI/SPI/TCPI, EAC, PMB, IBR), and specialized techniques
  (software cost estimating, learning curves, Analysis of Alternatives, WBS templates, the Green
  Book internal-control framework). The cost-estimating companion to `gao-schedule` and `gao-tra`;
  names referenced standards (EIA-748, MIL-STD-881D, the Green Book) without reproducing them.
  Tier 1 (US-gov public domain, GAO reproduction notice).
- **`gao-schedule`** (8 ch) — GAO Schedule Assessment Guide (GAO-16-89G, 2015): GAO's
  cross-government best-practice authority on schedule reliability — the ten best practices of a
  reliable integrated master schedule (capture, sequence, resource, duration, traceability, valid
  critical path, reasonable total float, schedule risk analysis, updating, baseline), the four
  characteristics (comprehensive, well-constructed, credible, controlled), critical path method
  arithmetic (forward/backward pass, total float), schedule risk analysis (Monte Carlo,
  contingency), statusing and baseline control, and the Appendix II audit triad. The time-domain
  companion to `gao-cost` and to the agency SE handbooks; NOT a cost-estimating guide, full SE
  process model, agile guide, or risk-management framework. Names third-party material (the
  Hornbacher-adapted reliability process, the GAO/NDIA recovery techniques table) without
  reproducing it. Tier 1 (US-gov public domain, GAO reproduction notice).
- **`nasa-ceh`** (7 ch) — NASA Cost Estimating Handbook (CEH) v4.0 (February 2015): NASA's
  12-step, three-part cost estimating process (Project Definition, Cost Methodology, Cost
  Estimate), the WBS/CADRe/ONCE data backbone, estimating methodologies (analogy, parametric/CER,
  engineering build-up, EVM, Delphi), ground rules and assumptions, data normalization and
  inflation (BY/CY/RY), the point-estimate-to-S-curve cost-risk chain and Unallocated Future
  Expense (UFE) reserves, Joint Cost and Schedule Confidence Level (JCL) analysis via probabilistic
  cost-loaded schedules, decision-support analyses (sensitivity, trade studies,
  make/lease-vs-buy, affordability, CAIV), and economic analysis (discounting, NPV, OMB Circular
  A-94). The cost-and-cost-risk complement to NASA's SE and risk packs (`nasa-risk`,
  `nasa-se-handbook`, `nasa-npr-7123`) and to the GAO cost canon (`gao-cost`, `gao-schedule`);
  names third-party tools/standards (ACEIT, SEER, PRICE TruePlanning, OMB A-94, GAO-09-3SP)
  without reproducing them. Tier 1 (US-gov public domain).

Catalogue now 35 packs (+2 signposts).

## [1.9.0] — 2026-06-23

### Added

- **`faa-hf-std`** (9 ch) — FAA Human Factors Design Standard (HF-STD-001B, Dec 30, 2016): the
  FAA's consolidated human-factors / human-systems-integration design criteria for systems it
  manages, operates, or maintains — general HF design principles, automation and function
  allocation, designing equipment for maintenance, displays/controls/visual indicators,
  alarms/audio/voice communications, the computer-human interface (information presentation,
  coding, interaction styles, windows, dialogue), keyboards/input devices and workstation/
  workplace ergonomics, and system security/personnel safety/environment/anthropometry/user
  documentation, plus intended-use and tailoring guidance. A quantified, source-attributed
  synthesis (millimetres, newtons, decibels, contrast ratios, percentile rules) that heavily
  cites MIL-STD-1472G, MIL-HDBK-759C, DOD-HFDG-ATCCS, NUREG-0700, NASA-STD-3000, ANSI, OSHA, and
  ISO 9241 — none of which it reproduces. Design criteria, NOT an HSI lifecycle/process model;
  complements `nasa-hsi` as the civil-aviation HSI tradition. Tier 1 (US-gov public domain).
- **`dod-mq-bok`** (6 ch) — DoD Manufacturing and Quality Engineering Body of Knowledge (M&Q BoK,
  v3.0, July 2025, OUSD(R&E)): the manufacturing-and-quality view of the defense acquisition life
  cycle — what M&Q engineers do across the Adaptive Acquisition Framework phases (Pre-MDD, MSA,
  TMRR, EMD, P&D, O&S), the twelve M&Q threads (A–L) built on the "5 Ms", manufacturing
  feasibility and producibility, Manufacturing Readiness Levels and assessments, Key/Critical
  Characteristics and process capability (Cp/Cpk, SPC), the standards stack (AS6500, AS9100/
  ISO 9001, AS9103, AS9145), technical reviews (ASR/PDR/CDR/PRR) and milestone gates, DCMA
  surveillance, industrial base and supply chain, and sustainment (LCSP, IPS, ILA, ISR). Answers
  the recurring M&Q question "*Can it be built?*". A best-practice compilation, NOT policy — it
  does not supersede DoDI 5000.02, JCIDS, or law; names third-party standards (SAE AS-series,
  ISO 9001, IEEE 15288.1/.2, MIL-STD-881) without reproducing them. Tier 1 (US-gov public domain,
  Distribution A).

Catalogue now 32 packs (+2 signposts).

## [1.8.0] — 2026-06-23

### Added

- **`nasa-de-acquisition`** (8 ch) — NASA Digital Engineering Acquisition Framework Handbook
  (NASA-HDBK-1004, Baseline 2020, superseding NASA-HDBK-0008): the acquisition-and-contracting
  side of digital engineering — the Data Requirements Description (DRD) instrument and the
  Appendix A DRD suite (TDP, MBx, CDMP, CSA, CR, FCA/PCA, SDT, EMDAL, REF, MRI), the Data Type
  1–5 control scale, SOW/RFP/Cost-Volume contract language and data rights (FAR/DFARS, Table 3
  license categories), the Requirements Exchange Format (REF/ReqIF, UUID schema) and Master
  Records Index, model-based data definition (MBSE, CAD/PMI, M&S credibility, BOM, release-state
  mapping, PLM), digital data collaboration, the four owned architectures, interoperability
  standards (MIL-STD-31000, STEP/ISO 10303, ASME Y14), the four MBE interoperability use cases,
  and MBE Plan development. Names third-party standards (ISO/STEP/ASME/MIL-STD/SAE, FAR/DFARS)
  without reproducing them; pairs with NASA-HDBK-1009A for the deeper practitioner detail.
  Tier 1 (US-gov public domain).
- **`nasa-fault-management`** (8 ch) — NASA Fault Management Handbook (NASA-HDBK-1002, Draft 2,
  April 2012): the SE discipline of designing what a system does when it fails — the
  fault/failure/anomaly vocabulary, the five FM strategies (fault avoidance, failure avoidance,
  failure masking, failure recovery, goal change), the six FM process activities across NASA
  mission phases Pre-A to E, response-latency-versus-time-to-criticality (TTC) design trades,
  fault/failure containment regions and FEPPs, the four redundancy approaches, top-down FM
  requirements development, FM verification vs. validation, the seven dedicated FM milestone
  reviews (FMCR/FMARR/FMPDR/FMCDR/FMTRR/FMLRR/FMCERR), FM organizational structure, and mined
  NASA Lessons Learned. **Built from an UNAPPROVED DRAFT** — treat as informational guidance,
  NOT a controlling standard; several source sections are placeholders and are correspondingly
  thin. Tier 1 (US-gov public domain).
- **`faa-system-safety`** (7 ch) — FAA System Safety Handbook (Dec 30, 2000): system safety as
  a specialty within systems engineering — the five-step safety risk management process (mandated
  by FAA Order 8040.4 and the AMS), the severity-by-likelihood risk matrix and acceptance bands,
  the Safety Order of Precedence, system-description models (5M, SHEL(L)), the hazard-analysis
  activities (PHL/PHA/RHA/SSHA/SHA/O&SHA/HHA), integrated system hazard analysis, the analysis
  techniques (FTA, FMEA/FMECA, Fault Hazard, Common Cause, Sneak Circuit, Energy Trace),
  closed-loop hazard tracking (Safety Action Record), and the specialty domains (acquisition-
  lifecycle safety and contracting, software safety/DO-178B, test & facilities safety, commercial
  launch safety, training, Operational Risk Management). A year-2000 FAA how-to that predates the
  modern FAA/ICAO Safety Management System (SMS); names MIL-STD-882/DO-178B and other third-party
  standards without reproducing them. Tier 1 (US-gov public domain).

Catalogue now 30 packs (+2 signposts).

## [1.7.0] — 2026-06-23

### Added

- **`nasa-rm-standard`** (6 ch) — NASA Reliability and Maintainability Standard
  (NASA-STD-8729.1A, Rev A, 2017): NASA's objectives-driven R&M framework — the R&M objectives
  hierarchy (one Top Objective decomposed into four sub-objectives, paired with tailorable
  strategies), how R&M requirements are established inside the SMA Plan required by NPR 7120.5,
  the SMA Technical Authority concurrence/independent-evaluation governance, milestone vs.
  readiness review gates, the reliability/maintainability/availability vocabulary (Ai vs. Ao,
  the failure causal chain, risk as a triplet), and the R&M Evidentiary Methods catalogue
  (FMEA/FMECA, FTA, RBDA, RCM, LORA, plus the space-environment and parts-pedigree analyses).
  An objectives-and-strategies standard — defers step-by-step procedures to the referenced
  NASA Preferred Reliability Practices. Tier 1 (US-gov public domain).
- **`dod-rio`** (8 ch) — DoD Risk, Issue, and Opportunity (RIO) Management Guide for Defense
  Acquisition Programs (OUSD R&E, Sep 2023 incl. Change 2.2): the defense-acquisition mechanics
  of program risk management — the RIO definitions, the five-step risk process
  (plan-identify-analyze-mitigate-monitor), 1–5 likelihood/consequence scoring and the 5×5 risk
  matrix, the four mitigation options (accept/avoid/transfer/control), burn-down plans, issue
  management (probability=1), opportunity management toward should-cost, cross-program/interface
  risk, tailoring RIO to the six AAF pathways (UCA/MTA/MCA/Software/DBS/Services), specialized
  methods (RMF, MBCRA/Cyber Table Top, Agile metrics, FMECA, ITRA/DTRAM), and institutionalizing
  RIO via the PRMP, boards (RMB/JRMB/ROMB/RWG), tiered roles, and WBS/IMP/IMS/EVM/TPM integration.
  The DoD-acquisition complement to `nasa-risk` and `dau-se-guidebook`; names third-party policy
  material (EIA-748, MIL-STD-881F, DCMA metrics) without reproducing it. Tier 1 (US-gov public
  domain, Distribution A).
- **`dod-digital-engineering`** (7 ch) — DoD Digital Engineering Strategy (2018, OUSD/ODASD(SE)):
  the Department of Defense's five digital engineering goals — (1) formalize the development,
  integration, and use of models; (2) provide an enduring authoritative source of truth;
  (3) incorporate technological innovation; (4) establish supporting infrastructure and
  environments; (5) transform the culture and workforce — plus their focus areas, the
  document-to-model and design-build-test→model-analyze-build shifts, model formalisms/provenance,
  governance and access control of the authoritative source of truth, and the
  coordinate→plan→pilot→sustain rollout. A vision-and-policy strategy, deliberately
  non-prescriptive (no how-to method or MBSE/SysML mechanics); excludes the CAC-gated Digital
  Engineering Body of Knowledge (DEBoK). Tier 1 (US-gov public domain, Distribution A).

Catalogue now 27 packs (+2 signposts).

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
