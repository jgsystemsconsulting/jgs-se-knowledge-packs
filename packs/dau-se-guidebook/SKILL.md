---
name: dau-se-guidebook
description: "Knowledge base from the DoD Systems Engineering Guidebook (OUSD R&E, February 2022). Use for the DoD SE process model — the 16 SE processes (8 technical management + 8 technical) mapped to ISO/IEC/IEEE 15288, the event-driven technical reviews and audits across the Major Capability Acquisition life cycle (ASR, SRR, SFR, PDR, CDR, SVR/FCA, PRR, PCA), the Systems Engineering Plan (SEP), risk/issue/opportunity management, TPMs and leading indicators, system-of-systems and digital engineering, and the 24 design considerations (RAM, system safety, HSI, system security engineering, MOSA, supportability, etc.). Acquisition-program oriented: thin on detailed cost estimating, contracting law, and non-DoD or commercial life cycles."
---

<!-- argument-hint: [SE process name, review/audit (ASR/SRR/SFR/PDR/CDR/SVR/FCA/PRR/PCA), SEP, TPM, risk/issue/opportunity, design consideration, digital engineering, SoS, chapter number] -->

# DoD Systems Engineering Guidebook (OUSD R&E, February 2022)
**Source**: US Department of Defense (OUSD R&E) — US Government work, public domain; Distribution A | **Chapters**: 6

## When to use
Use this skill when you need to apply, explain, or assess the DoD's systems engineering approach for defense acquisition programs: the 16 SE processes and how they map to ISO/IEC/IEEE 15288, the event-driven technical review and audit sequence, the Systems Engineering Plan (SEP), risk/issue/opportunity management, technical performance measurement, system-of-systems and digital-engineering practice, or any of the 24 design considerations (RAM, system safety, HSI, system security engineering, MOSA, etc.). This is the OUSD(R&E) companion to DoDI 5000.88 (*Engineering of Defense Systems*); it is guidance, not policy — programs scale and tailor it.

**Prerequisites:** none — plain Markdown; no MCP server, API key, or licence tier needed at runtime.

## How to Use This Skill
- **Without arguments** — load the core frameworks below for an overview of the SE process model, the review/audit sequence, and the SEP.
- **With a topic** — ask about a specific process (e.g., "architecture design process", "configuration management"), a review/audit (e.g., "PDR entrance criteria", "SVR/FCA"), the SEP, TPMs/leading indicators, or a design consideration (e.g., "human systems integration", "system security engineering").
- **With a chapter** — ask for `ch04` (8 technical management processes), `ch05` (8 technical processes), `ch03` (reviews & audits), `ch06` (design considerations).

Supporting files: `glossary.md`, `patterns.md`, `cheatsheet.md`.

## Core Frameworks & Mental Models

### The DoD SE Process Model — 16 Processes (8 + 8)

The practice of SE is composed of **16 processes**: eight **technical management** processes and eight **technical** processes. They map to the ISO/IEC/IEEE 15288 SE processes and are applied in an integrated, overlapping, iterative manner along the V-diagram. Programs **scale** the processes to the system's maturity, complexity, size/scope, acquisition pathway, and life-cycle phase.

**Eight Technical Processes** (top-down design, then bottom-up realization — the V):
1. **Stakeholder Requirements Definition** — translate operational requirements from stakeholders into top-level technical requirements.
2. **Requirements Analysis** — decompose into a complete set of system functional and performance requirements.
3. **Architecture Design** — capture functional requirements and interdependencies in the system architecture (often via system modeling, trade-offs, decision analyses).
4. **Implementation** — mature and realize the design of the system and system elements; generate the product baseline.
5. **Integration** — assemble system elements into the system for test.
6. **Verification** — developmental test: did we build the system right (conformance to requirements)?
7. **Validation** — operational test: did we build the right system (meets the operational need)?
8. **Transition** — formally deliver the capability and enabling system elements to the end users for operation and sustainment.

**Eight Technical Management Processes** (run across the whole life cycle, providing insight and control):
1. **Technical Planning** — plan, organize, and resource the technical effort; outputs feed the SEP, IMP, IMS, WBS.
2. **Decision Analysis** — apply formal criteria, alternatives, and analysis to significant technical decisions.
3. **Technical Assessment** — measure technical progress against plans; conduct technical reviews; track TPMs and leading indicators.
4. **Requirements Management** — maintain bidirectional traceability and control requirement changes.
5. **Risk Management** — manage risks, issues, and opportunities (RIO) with reporting matrices.
6. **Configuration Management** — establish and control configuration baselines and changes.
7. **Technical Data Management** — capture and manage technical data, trade studies, and analyses.
8. **Interface Management** — define and control internal and external interfaces.

> **Not the NASA 17-process model.** This is the DoD's **8 + 8** model (16 processes) tied to the *Major Capability Acquisition* life cycle and ISO/IEC/IEEE 15288 — distinct from NASA NPR 7123's SE Engine (17 processes). The review names differ too (DoD has ASR, SVR/FCA, PRR, PCA).

### Technical Reviews & Audits (event-driven)

Reviews are **event-driven** (triggered by meeting entrance criteria documented in the SEP, not by calendar). Each provides a knowledge-based control point that reduces risk over time. The Major Capability Acquisition sequence:

| Review/Audit | Purpose (what maturity it gates) |
|---|---|
| **ASR** — Alternative Systems Review | Preferred materiel solution(s) feasible; requirements understood |
| **SRR** — System Requirements Review | System requirements baselined and traceable to capability needs |
| **SFR** — System Functional Review | Functional baseline established; design traceable to requirements |
| **PDR** — Preliminary Design Review | Allocated baseline established; preliminary design meets requirements at acceptable risk |
| **CDR** — Critical Design Review | Initial product baseline; design mature enough to start fabrication/coding |
| **SVR/FCA** — System Verification Review / Functional Configuration Audit | System verified against functional baseline ("did we build it right") |
| **PRR** — Production Readiness Review | System ready to enter production at acceptable risk |
| **PCA** — Physical Configuration Audit | Product baseline matches the as-built configuration |

A review is well-run when entrance criteria are met first, the right products are at the right maturity, action items (RFAs) are dispositioned, and the result informs the next milestone decision.

### The Systems Engineering Plan (SEP)

The SEP is the master technical plan: it documents the program's SE approach, technical risks, processes, resources, metrics, SE products, organization, design considerations, and the timing/entrance criteria of technical reviews. Key rules:
- **Required** for MDAPs and ACAT II/III programs (per DoDI 5000.88) unless waived; recommended best practice for all other development.
- A **living document** — updated as the approach evolves and (best practice) reapproved before each technical review.
- Prepared by the Lead Systems Engineer under the PM; approval authority depends on ACAT level (USD(R&E) for ACAT ID).
- Must be **consistent with** the APB, TEMP, PPP, LCSP, IMP/IMS, WBS, and Risk Management Plan — no redundancy, plain language.

### Risk, Issue, and Opportunity (RIO) Management

The Risk Management process manages three related things, each with its own reporting matrix:
- **Risk** — a *future* event with negative consequence; scored on a **likelihood × consequence** 5×5 matrix; managed by mitigation (accept / avoid / transfer / control).
- **Issue** — a risk that **has been realized** (or a present problem); scored on a consequence-based issue matrix; managed by corrective action (a "burn-down").
- **Opportunity** — a potential *future benefit* (cost/schedule/performance); managed by pursue / reject decisions.

### Technical Performance Measurement

- **TPMs** — quantitative measures tracked against a planned profile to assess whether the design will meet requirements; organized in a TPM hierarchy.
- **Leading indicators** — forward-looking measures (trends) that signal whether risk-mitigation is on track *before* a threshold is breached; drive early corrective action.
- TPMs roll up to MOPs/MOEs and feed the Technical Assessment process and reviews.

### System-Level Considerations

- **System of Systems (SoS)** — four types (virtual, collaborative, acknowledged, directed); SE differs from single-system SE in authority, funding, and interface control.
- **Digital Engineering (DE)** — an authoritative source of truth and models used across the life cycle; changes *how* reviews/analyses are done, not *what* must be done.
- **MOSA** — Modular Open Systems Approach; required "to the maximum extent practicable" for evolvability and competition.
- **Mission engineering, software engineering, value engineering, sustainability analysis** — enterprise techniques feeding SE.

### Design Considerations (24)

Section 5 carries 24 cross-cutting design considerations the SE process must balance — among them **Reliability & Maintainability (R&M) engineering**, **System Safety** (incl. software system safety, ESOH, hazard tracking), **Human Systems Integration (HSI)**, **System Security Engineering**, **Manufacturing & Quality** (incl. manufacturing readiness), **Supportability**, **Survivability**, **Interoperability**, **Modular Design**, **Standardization**, **Spectrum Management**, **Corrosion Prevention**, **DMSMS**, **Operational Energy**, **Affordability trade-offs**, **Section 508 accessibility**, **Anti-counterfeiting**, **Critical Safety Items**, and **Demilitarization & Disposal**.

---

## Chapter Index

| # | Section | Key content |
|---|---------|-------------|
| [ch01](chapters/ch01-introduction.md) | Introduction | Purpose & definition of SE, the 16-process model, V-diagram, SE policy/guidance (DoDD 5000.01, DoDI 5000.02/5000.88), the SEP, development planning, process scaling |
| [ch02](chapters/ch02-system-level-considerations.md) | System-Level Considerations | SoS (four types), digital engineering, mission/software/value engineering, MOSA, sustainability, engineering resources & roles, IPTs, certifications, SE role in contracting (RFP technical content) |
| [ch03](chapters/ch03-technical-reviews-and-audits.md) | Technical Reviews & Audits | Event-driven review philosophy, ASR/SRR/SFR/PDR/CDR/SVR-FCA/PRR/PCA — purpose, products, and entrance/success criteria; the technical review process; baselines (functional/allocated/product) |
| [ch04](chapters/ch04-technical-management-processes.md) | Technical Management Processes (8) | Technical Planning, Decision Analysis, Technical Assessment (TPMs, leading indicators), Requirements Management, Risk (RIO) Management, Configuration Management, Technical Data Management, Interface Management |
| [ch05](chapters/ch05-technical-processes.md) | Technical Processes (8) | Stakeholder Requirements Definition, Requirements Analysis, Architecture Design, Implementation, Integration, Verification, Validation, Transition — the V-diagram top-down/bottom-up flow |
| [ch06](chapters/ch06-design-considerations.md) | Design Considerations (24) | R&M, system safety/ESOH, HSI, system security engineering, manufacturing & quality / manufacturing readiness, supportability, survivability, MOSA/modular design, interoperability, affordability trade-offs, and the rest of the 24 |

## Topic Index

- **16-process SE model / ISO 15288 mapping / V-diagram / process scaling** → ch01, ch04, ch05
- **Systems Engineering Plan (SEP)** → ch01, ch04, cheatsheet
- **Roles (PM, Systems Engineer, Lead Software Engineer) / IPTs** → ch01, ch02
- **System of Systems (SoS) / Digital Engineering / mission engineering** → ch02
- **MOSA / modular design** → ch02, ch06
- **Contracting / RFP technical content** → ch02
- **Technical reviews & audits (ASR, SRR, SFR, PDR, CDR, SVR/FCA, PRR, PCA)** → ch03, cheatsheet
- **Baselines (functional / allocated / product)** → ch03, ch05
- **Technical management processes** (Technical Planning, Decision Analysis, Technical Assessment, Requirements/Configuration/Technical Data/Interface Management) → ch04
- **Risk / Issue / Opportunity (RIO) management** → ch04, cheatsheet
- **TPMs / leading indicators** → ch04, cheatsheet
- **Technical processes** (Stakeholder Requirements, Requirements Analysis, Architecture Design, Implementation, Integration) → ch05
- **Verification vs. Validation / Transition** → ch05, cheatsheet
- **Design considerations — the 24** (R&M, System Safety/ESOH, HSI, System Security Engineering, Manufacturing & Quality/MRLs, supportability, survivability, DMSMS, …) → ch06, cheatsheet

## Supporting Files

- [glossary.md](glossary.md) — key DoD SE terms (processes, reviews, baselines, RIO, TPM, SoS, design considerations), alphabetical, with chapter references
- [patterns.md](patterns.md) — reusable SE patterns (process scaling, event-driven review gating, SEP maintenance, risk vs. issue triage, MOSA adoption, design-consideration balancing) with When/How/Trade-offs structure
- [cheatsheet.md](cheatsheet.md) — decision rules, the 16-process table, review/audit sequence, RIO matrices, TPM vs. leading indicator, design-considerations list, tells & smells

---

## Scope & Limits

**Covers**: the DoD SE approach for defense acquisition programs per the OUSD(R&E) Systems Engineering Guidebook (February 2022) — the 16 SE processes (8 technical management + 8 technical) and their ISO/IEC/IEEE 15288 mapping; the event-driven technical review and audit sequence (ASR, SRR, SFR, PDR, CDR, SVR/FCA, PRR, PCA) with products and entrance/success criteria; the Systems Engineering Plan (SEP); risk/issue/opportunity management; technical performance measurement (TPMs, leading indicators); system-of-systems and digital-engineering practice; engineering resources, roles, IPTs, and the SE role in contracting; and the 24 design considerations.

**Does not cover in depth**: detailed cost estimating and JCL analysis (see a cost-estimating source); contracting law and the FAR/DFARS; the Adaptive Acquisition Framework pathways themselves (see the *Engineering of Defense Systems Guidebook* and DoDI 5000.02); test & evaluation planning detail (see the DoD T&E guidance / TEMP); program protection and cybersecurity RMF detail (see the Program Protection Plan and NIST/RMF sources); software development methodology detail; and non-DoD, commercial, or civil-agency life cycles. This is **guidance, not policy** — the binding requirements live in DoDI 5000.88 and related issuances.

**Jurisdiction**: US Government public domain work (Distribution Statement A). Applies to DoD acquisition programs; non-DoD organisations may adopt the framework voluntarily.
