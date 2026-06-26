---
name: faa-ams-vv
description: "Knowledge base from the FAA AMS Lifecycle V&V Guidelines (verification and validation), Version 3.0, dated April 2017. Use for applying verification and validation across the FAA Acquisition Management System (AMS) lifecycle: the verify-vs-validate distinction (built right vs. right thing), the work-product/component/product tiers, the nine V&V planning elements, the four method catalogs (Appendix C), decision-point-gated V&V (SASP, CRD, Investment Analysis, Solution Implementation, In-Service Management), the Appendix B document checklists (PRD/APB/ISPD/PMP), and the DT/OT/IOA test triad. Scope limits: this is an FAA acquisition-V&V doctrine, NOT a general SE process model, requirements-engineering manual, or test-design textbook. It borrows its core V&V definitions from CMMI v1.2 (SEI, paraphrased) and presumes the surrounding AMS lifecycle (see the FAA SEM pack); its phase tables are policy snapshots as of April 2017 and it is thin on detailed test methods, tool specifics, and anything outside FAA acquisition governance."
---

<!-- argument-hint: [verify vs validate, work product / component / product, V&V method, AMS phase (SASP/CRD/IA/SI/ISM), decision point/gate, planning element, Appendix B checklist (PRD/APB/ISPD/PMP), DT/OT/IOA, chapter number] -->

# FAA AMS Lifecycle V&V Guidelines (Verification and Validation) — Version 3.0, April 2017
**Source**: Federal Aviation Administration (FAA) — US Government work, public domain | **Chapters**: 7

## When to use
Use this skill when you need to apply verification and validation across the FAA Acquisition Management System (AMS) lifecycle, as defined in the FAA AMS Lifecycle V&V Guidelines Version 3.0 (April 2017). This pack covers the verify-vs-validate distinction (built right vs. right thing), the work-product/component/product tiers, the nine V&V planning elements, the four method catalogs (Appendix C), decision-point-gated V&V across AMS phases (SASP, CRD, Investment Analysis, Solution Implementation, In-Service Management), the Appendix B document checklists (PRD/APB/ISPD/PMP), and the DT/OT/IOA test triad. Pair it with the FAA SEM pack for the surrounding AMS lifecycle context.

**Prerequisites:** none, plain Markdown; no MCP server, API key, or licence tier needed at runtime.

## How to Use This Skill

- **Without arguments** — load the Core Frameworks below for the verify-vs-validate split, the three V&V tiers, the four method catalogs, and how V&V gates each AMS decision point.
- **With a topic** — ask about verifying vs. validating, choosing a V&V method, the nine planning elements, the Appendix B checklists, the DT/OT/IOA triad, or what gets V&V'd in a given phase.
- **With a phase** — ask for SASP/CRD (`ch03`), Investment Analysis (`ch04`), Solution Implementation (`ch05`), or In-Service Management (`ch06`).
- **With a chapter** — request `ch01`–`ch07` directly (index below).

Supporting files: `glossary.md` (terms + acronyms), `patterns.md` (11 how-to techniques), `cheatsheet.md` (decision rules, phase/gate/method tables, tells & smells).

**Prerequisites:** none — plain Markdown; no MCP server, API key, or licence tier needed at runtime. Pairs with the FAA SEM pack, which defines the surrounding AMS lifecycle this V&V doctrine overlays.

## Core Frameworks & Mental Models

### Verification vs. Validation — the two questions

The spine of the entire guideline. **Verification** confirms the thing was *built right* — that selected work products meet the requirements specified for them (templates, standards, specifications, policy). It is inherently incremental, running from initial requirements through every change to the finished end product. **Validation** confirms the *right thing was built* — that the finished product, a component, or a selected work product will deliver its intended purpose and satisfy user needs once in its operating environment. Both definitions are drawn from, and here paraphrased from, **CMMI for Development v1.2 (SEI, 2006)**; the guideline cites CMMI and notes GAO relies on it for quality audits. The relative *emphasis* of the two shifts with program maturity: validation-heavy while needs and concepts are still forming, verification-heavy as design and product harden. It is a sliding balance, not a fixed split.

A worked example crystallizes it: a system specification is *verified* against the standards/templates that govern its content and format, and *validated* against the needs captured in the higher-level requirements document. Verification looks **down** at the spec; validation looks **up** at the need.

### The three V&V tiers (and the upward flow)

V&V applies to a deliberate hierarchy: **work product → product component → product**.
- **Work product** — anything that represents, defines, or directs the product (designs, specs, plans, requirements, models, prototypes, contracts).
- **Product component** — a lower-level element integrated upward (possibly nested).
- **Product** — the delivered system, service, facility, or operational change.

V&V flows up the hierarchy: work products first, components before integration, the product before operational acceptance. Any item may undergo V&V more than once if modified. Both **government and contractor** organizations are required to perform V&V, on both parties' work. **V&V ≠ QA**: V&V targets requirements/mission/risk; QA targets whether the established *processes* were followed.

### The four method catalogs (Appendix C)

Cross "verification vs. validation" with "work product vs. product/component" to get four method lists:
- **Work-product verification** — checklists, audits, peer reviews, inspections.
- **Work-product validation** — broader and user-facing: surveys and discussions with users, functional presentations, dry-run walk-throughs, storyboarding and modeling, demonstrations and testing, plus the verification set (analyses, audits, peer reviews, inspections, checklists).
- **Product/component verification** — analyses, audits, peer reviews, inspections, checklists, simulations, testing, demonstrations, and **accreditation**.
- **Product/component validation** — user-evaluation questionnaires and discussions with users, functional presentations, simulations and testing, demonstrations, analyses, audits, peer reviews, inspections, and checklists.

Validation catalogs are user-facing and broader; product-tier catalogs add analysis, simulation, and (for verification) accreditation. Definitions live in Appendix C (Ch 7).

### Plan → Perform → Report → Decide

V&V is a four-stage pipeline, not an end-of-line test. **Plan**: V&V planning is mandatory for every AMS program and embedded in the program's documents (ISPD, TEMP, PMP, SEMP, QA Plan, phase plans), each carrying the relevant subset of the **nine planning elements** (methods × 2, items to V&V, processes/standards/criteria, tracking/reports, roles, independent reviewers, tools/labs, training). **Perform**: independent reviewers (not the item's developers) run the matched methods, confirming prerequisite V&V was done and still holds. **Report**: a controlled, archived report covering Introduction, Purpose, Criteria, Approach, Participants, Results, Recommendations. **Decide**: results become *entrance criteria* for AMS decision points. A gap in any earlier stage starves the decision.

### Decision-point-gated, table-driven V&V across the AMS lifecycle

The guideline organizes V&V by the **AMS lifecycle** (SASP → CRD → Investment Analysis → Solution Implementation → In-Service Management), not a generic V-model — with the non-phase activity **RSA** feeding the front end. For each phase, a table (Tables 1–6) anchors on decision points and fixes four columns: the **decision point**, the **minimum work products** to V&V there, the **criteria** (validation criteria = substantive upstream content; verification criteria = templates/policy), and the **responsible stakeholder**. To plan V&V for any artifact, find its row — criteria and owner are pre-bound. Critically, the *criteria are themselves V&V'd* (yardsticks are earned, not assumed), and the tables are **policy snapshots as of April 2017** — current phase guidance supersedes them. Figure 3 shows emphasis only; the tables define the required minimum.

### Foundations, chaining, and front-loaded safety/security

Foundational documents (NAS ConOps, NAS Requirements Document, NSIP, NARP, NextGen Implementation Plan, **Enterprise Architecture**) are V&V'd against FAA Strategic Initiatives *before* downstream use. V&V is a **chain**: each verified-and-validated artifact becomes the baseline for the next, and a maturing product's earlier V&V results feed in as validation criteria for its later version — so under-validating early work products propagates the wrong product forward. **Information security** enters at the very first phase (ISS assessments validated against **FIPS-199**, verified against **ISGSA**) and **safety** (FAA SMS, Safety Risk Management documentation) joins as a gated obligation toward the In-Service Decision. The **EA** is both a source criterion and a recipient of V&V feedback — a closed loop.

### The product-V&V engine: DT / OT / IOA

Product and component V&V lives mainly in **Test and Evaluation**, concentrated in Solution Implementation and In-Service Management: **Development Test (DT)** serves verification (developer-run, FAA witnessing); **Operational Test (OT)** serves validation (ANG-E OT Test Director and team); **Independent Operational Assessment (IOA)** gives an independent operational-readiness read for designated products. **PDR** verifies against the allocated baseline, **CDR** against the product baseline. The surrounding test plans/procedures/reports are themselves V&V'd first — bad test artifacts mean a decision built on bad data.

---

## Chapter Index

| # | Section | Key content |
|---|---------|-------------|
| [ch01](chapters/ch01-faa-ams-vv-introduction-and-vv-philosophy.md) | Introduction: Terms, Definitions, Philosophy | Verify vs. validate (paraphrased from CMMI v1.2), the work-product/component/product hierarchy, who performs V&V, V&V vs. QA, the EA as source criterion + feedback loop, V&V as a decision-and-risk instrument |
| [ch02](chapters/ch02-faa-ams-vv-implementation-guidance.md) | Implementation Guidance: Plan/Perform/Report/Decide | The nine planning elements, document-embedded planning, independence, the validity chain, the four method catalogs, T&E (DT/OT/IOA), report minimum content, decision support |
| [ch03](chapters/ch03-faa-ams-vv-approach-and-early-lifecycle.md) | Approach + Early Lifecycle (SASP, CRD, RSA) | The five AMS phases, RSA as a non-phase activity, the five early management documents (APB/PRD/BC/ISPD/PMP), Appendix B checklists, the IER track, Tables 1–2, front-loaded security (FIPS-199/ISGSA) |
| [ch04](chapters/ch04-faa-ams-vv-investment-analysis.md) | Investment Analysis (Initial & Final) | Two-stage gating (which alternative? / is the baseline ready?), per-product validation vs. verification criteria, prior V&V results as forward criteria, per-product stakeholder accountability, Tables 3–4 |
| [ch05](chapters/ch05-faa-ams-vv-solution-implementation.md) | Solution Implementation | The IBR baseline revalidation, the SI gate spine (Contract Award → ISD), DT/OT/IOA, PDR/CDR baseline staircase, safety (SMS) and security (System Security Authorization/POA&M) gates, Table 5 |
| [ch06](chapters/ch06-faa-ams-vv-in-service-management.md) | In-Service Management | "Prove the change, re-prove the purpose," the implement/deploy gates, configuration management (FAA Form 1800-2, Orders 1800.66 & 1320.58A), ISM DT/OT/IOA, EA-change control authority, Table 6 |
| [ch07](chapters/ch07-faa-ams-vv-acronyms-checklists-definitions.md) | Reference: Acronyms, Checklists, Definitions | Appendix A acronyms, Appendix B four document checklists (PRD/APB/ISPD/PMP), method codes + artifact definition, Appendix C method definitions, CPRs as cross-document through-line, requirement-quality bar |

## Topic Index

- **Accreditation (method)** → ch02, ch07
- **Acquisition Management System (AMS) lifecycle** → ch01, ch03
- **Acquisition Program Baseline (APB)** → ch03, ch04, ch07
- **Analysis (verification method)** → ch07
- **Appendix B checklists (PRD/APB/ISPD/PMP)** → ch03, ch07
- **Artifact (evidence record)** → ch07
- **Audit (method)** → ch02, ch07
- **Business Case + IER track** → ch03, ch04
- **Concept & Requirements Definition (CRD)** → ch03
- **Concept of Operations / Concept of Use** → ch03, ch05
- **Configuration management (Form 1800-2, Order 1800.66)** → ch06
- **Critical Design Review (CDR)** → ch05
- **Critical Operational Issue (COI)** → ch05
- **Critical Performance Requirement (CPR)** → ch07
- **Critical technical documents** → ch02
- **CMMI v1.2 (paraphrased source of definitions)** → ch01, ch03, ch07
- **Decision points / gates (CRDRD, IARD, IID, FID, ISD)** → ch02, ch03, ch04, ch05, ch07
- **Demonstration (method)** → ch02, ch07
- **Development Test (DT)** → ch02, ch05, ch06
- **Enterprise Architecture (EA)** → ch01, ch03, ch04, ch06
- **EA Control Board** → ch03, ch04, ch06
- **FIPS-199 (security categorization)** → ch03
- **Independence of reviewers** → ch02
- **Independent Evaluation Review (IER)** → ch03
- **Independent Operational Assessment (IOA)** → ch02, ch05, ch06
- **Information Security Guidance for System Acquisition (ISGSA)** → ch03, ch04
- **Information System Security (ISS) assessment** → ch03, ch04
- **In-Service Decision (ISD)** → ch05, ch07
- **In-Service Management (ISM)** → ch06
- **Integrated Baseline Review (IBR)** → ch05
- **Inspection (method)** → ch02, ch07
- **Investment Analysis (Initial & Final)** → ch04
- **Method catalogs (four)** → ch02, ch07
- **Modeling / Simulation / Storyboarding (methods)** → ch07
- **NAS Change Proposal (NCP)** → ch06
- **Nine V&V planning elements** → ch02
- **Operational Test (OT)** → ch02, ch05, ch06
- **Peer review (method)** → ch02, ch07
- **Plan / Perform / Report / Decide pipeline** → ch02
- **Plan of Actions and Milestones (POA&M)** → ch05
- **Preliminary Design Review (PDR)** → ch05
- **Product / component / work product (the three tiers)** → ch01, ch02
- **Program Management Plan (PMP)** → ch03, ch04, ch07
- **Program Requirements Document (PRD / fPRD)** → ch03, ch04, ch07
- **Quality Assurance (QA) vs. V&V** → ch01
- **Requirement-quality bar** → ch07
- **Research for Systems Analysis (RSA)** → ch03
- **Safety Management System (SMS) / safety V&V** → ch05
- **Screening Information Request (SIR)** → ch04
- **Service Analysis & Strategic Planning (SASP)** → ch03
- **Solution Implementation (SI)** → ch05
- **System Security Authorization** → ch05
- **Tables 1–6 (phase V&V specifications)** → ch03, ch04, ch05, ch06
- **Test and Evaluation Master Plan (TEMP)** → ch02, ch04, ch05
- **Testing (method)** → ch02, ch07
- **Validation (right thing built)** → ch01, ch02
- **Validity chain / prerequisite V&V** → ch02, ch04
- **Verification (built right)** → ch01, ch02
- **V&V report minimum content** → ch02
- **Walk-through / dry run (method)** → ch07

## Supporting Files

- **`glossary.md`** — alphabetical terms and acronyms (ACAT through V&V) with chapter refs.
- **`patterns.md`** — 11 reusable patterns (When / How / Trade-offs): split verify/validate, embed planning, gate on decision points, find-your-row, V&V the foundations & criteria, chain forward, match method to tier, demand method+artifact, two governance tracks, front-load safety/security, prove-the-change-and-re-prove-the-purpose.
- **`cheatsheet.md`** — decision rules, the four-catalog method matrix, phase/gate tables, the nine planning elements, the four checklist documents, requirement-quality bar, method codes & tells, the DT/OT/IOA triad, and anti-pattern tells & smells.

## Scope & Limits

- **Source version**: the FAA AMS Lifecycle V&V Guidelines (verification and validation), **Version 3.0, dated April 2017**. A living document; the FAA states it is updated as better practices emerge, so check FAST for a current version.
- **This is FAA acquisition-V&V doctrine, not general SE.** It assumes the surrounding **AMS lifecycle** and the FAA Acquisition Management Policy as scaffolding — it does not define them (see the FAA SEM pack). It is *not* a general systems-engineering process model, a requirements-engineering manual, or a test-design textbook.
- **Definitions are paraphrased, not canonical.** The core verification/validation definitions trace to **CMMI for Development v1.2 (SEI)** — a copyrighted model the guideline cites; this pack paraphrases and never quotes it. For the authoritative process-area treatment, go to CMMI directly.
- **Tables 1–6 are policy snapshots as of April 2017.** The source repeatedly cautions that detailed, *current* phase guidelines and templates exist and take precedence over the published tables. Treat the table contents (criteria, stakeholders, owning offices, form/order numbers) as illustrative of the model, not as live authority.
- **Thin on**: detailed test-method design and statistics; specific tools, labs, and simulators (named only as planning elements); cost and schedule estimating; and anything outside FAA acquisition governance. Office names and org structures (e.g., ANG-E, ATO) reflect the 2017 FAA organization and may have changed.
- **No source link published** (per the repo's no-source-link policy); the source is identified textually by title, publisher (FAA), and version.
