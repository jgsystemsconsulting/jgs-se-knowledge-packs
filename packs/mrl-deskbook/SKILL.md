---
name: mrl-deskbook
description: "Knowledge base from the DoD Manufacturing Readiness Level (MRL) Deskbook (Version 2022, OSD ManTech / Joint Service–Industry MRL Working Group). Use for assessing and managing manufacturing maturity and producibility risk in defense acquisition: the 10-level MRL scale and its non-linear, target-not-grade nature; the five demonstration environments (laboratory → production-relevant → production-representative → pilot line → production line); the nine manufacturing-risk threads and sub-threads; how MRL targets map onto Adaptive Acquisition Framework milestones (MRL 4/6/7/8/9); conducting an MRL Assessment; building a Manufacturing Maturation Plan; putting MRL maturity into contract language (Section L/M, SOW, AS6500A, DIDs); tailoring criteria for S&T, single-system, ship, sustainment, and industry contexts; and screening operational-technology cybersecurity. Manufacturing-readiness focused — it measures producibility risk and frames mitigation; it is NOT a technology-readiness (TRL) guide, a full systems-engineering process model, a cost-estimating or schedule guide, or a deep cybersecurity audit method (see sibling packs for those)."
---

<!-- argument-hint: [MRL level, demonstration environment, manufacturing-risk thread, milestone target (MRL 4/6/7/8/9), MRL Assessment process, Manufacturing Maturation Plan (MMP), contract language (Section L/M, AS6500A, DID), tailoring (S&T/ship/single-system), OT cybersecurity, chapter number] -->

# DoD Manufacturing Readiness Level (MRL) Deskbook (Version 2022)
**Source**: OSD Manufacturing Technology Program with the Joint Service/Industry MRL Working Group — US Government work, public domain; "not a DoD requirement... offered as a best practice." | **Chapters**: 8

## When to use
Use this skill when you need to assess, explain, or critique the **maturity and risk of a manufacturing capability** in a defense (or defense-style) acquisition: assigning a Manufacturing Readiness Level, judging whether an element has reached the maturity its milestone expects, planning and conducting an MRL Assessment, building a Manufacturing Maturation Plan for a shortfall, writing MRL maturity into an RFP or contract, tailoring the criteria for a science-and-technology effort / single-system build / ship / sustainment activity / industry product line, or screening operational-technology cybersecurity on the shop floor.

**Prerequisites:** none — plain Markdown; no MCP server, API key, or licence tier needed at runtime.

## How to Use This Skill
- **Without arguments** — load the core frameworks below for an overview of the MRL 1–10 scale, the five environments, the nine threads, the milestone targets, and the assessment-to-MMP loop.
- **With a topic** — ask about an MRL level, a demonstration environment, a risk thread, a milestone target, the assessment process, the MMP, contract language, tailoring, or OT cybersecurity.
- **With a chapter** — ask for `ch02` (the scale, threads, MRL/TRL), `ch03` (milestone mapping), `ch04` (conducting an assessment), `ch05` (MMPs), `ch06` (contract language), `ch07` (tailoring), or `ch08` (OT cybersecurity).

Supporting files: `glossary.md`, `patterns.md`, `cheatsheet.md`.

## Core Frameworks & Mental Models

### What an MRL is (and isn't)

A **Manufacturing Readiness Level (MRL)** is a 10-level ordinal scale that states how mature a manufacturing capability should be at a given point in the acquisition life cycle, and where the open manufacturing risks lie. MRLs were created because manufacturing reviews (PRRs, production-capability reviews) were structurally rigorous but used inconsistent metrics, leaving risk uncomparable across programs — a shared scale is a shared language. The scale is **non-linear**: the effort to climb from one level to the next is not equal. Crucially, the number is a **risk-focusing target, not a grade**, and an MRL Assessment is a **risk-identification tool, not a go/no-go gate**. Maturity is determined by working the **MRL Criteria Matrix** for the element — never by simply stamping a level on it.

### The MRL 1–10 scale

1 basic implications identified · 2 concepts identified · 3 proof of concept · 4 produce in a **laboratory** environment · 5 produce prototype components in a **production-relevant** environment · 6 produce a prototype system in a production-relevant environment · 7 produce in a **production-representative** environment · 8 **pilot-line** capability (LRIP-ready) · 9 LRIP demonstrated (FRP-ready) · 10 FRP demonstrated, lean / continuous improvement.

### The five demonstration environments

Maturity is shown in progressively more realistic settings: **laboratory → production-relevant → production-representative → pilot line → production line.** Each is a more demanding stage to prove the same claim — "we can build this to requirements." The responsible organization and its contractors must agree the production-realism content for each, tied to the actual risk; "production-relevant" is a stakeholder agreement for the application, not a fixed place.

### The nine manufacturing-risk threads

Manufacturing risk is decomposed into nine **threads** (and sub-threads) so each dimension traces independently from MRL 1 to MRL 10: **Technology & Industrial Base · Design · Cost & Funding · Materials · Process Capability & Control · Quality · Manufacturing Workforce · Facilities · Manufacturing Management.** Hold the scale as a **grid** — levels across the top, threads down the side — not a thermometer. A program is at some maturity *per thread*; the number people quote is shorthand for the worst-supported corner.

### MRL vs TRL — pace one by the other

**MRLs** measure manufacturing/production risk; **TRLs** (9 levels) measure technology/performance maturity. They are related but **not one-to-one**. The governing best practice is to **pace manufacturing maturity by technology maturity** and pull producibility concerns into technology development early — the literal meaning of **"moving manufacturing left."** A high TRL with ignored manufacturability, or a high MRL on an unstable design, both raise programmatic risk.

### MRL targets map onto acquisition milestones

For Major Capability Acquisition: **MRL 4** at MSA (on each competing solution), **MRL 6** by Milestone B, **MRL 7** by CDR, **MRL 8** for LRIP at Milestone C, **MRL 9** for FRP. Faster pathways compress this (UCA: 7→8→9 under two years; MTA Rapid Prototyping enters at MRL 4, Rapid Fielding at MRL 8). Best practice is to **look forward**: assess against the current target while reviewing the *next* level's criteria for gaps. MRL Assessments are best practice for MCA/MTA/UCA, not required for Business Systems or Services.

### Assessment → Maturation Plan loop

An **MRL Assessment** follows an eight-activity flow (scope → taxonomy/schedule → form team → orient contractors → self-assessment → agenda → conduct → report), assesses **top-down** but reports **bottom-up**, and uses nine filtering questions to decide *what* to assess. Wherever an element falls below target, the assessment feeds a **Manufacturing Maturation Plan (MMP)** — a costed, scheduled, owned mitigation per shortfall. *The assessment is the flashlight; the MMP is the work order.* A low MRL early is acceptable; it tells you where to invest before the next phase. At a milestone shortfall the PM has three courses of action: delay, switch to lower-risk approach, or carry the risk forward with a funded MMP.

### Making maturity binding, and tailoring it

The Criteria Matrix is **descriptive, not directive** — it grades maturity but does not task work. Tasking comes from **AS6500A** plus **RFP Section L** (what to submit) / **Section M** (how it's scored) / the **SOW** "shall" statements. **Tailoring** the criteria to context (S&T, single/limited system, ship, sustainment, industry) is legitimate and expected, but bounded by three rules: keep traceability to the criteria, document and justify any criterion you cannot assess, and rely on trained SMEs — because tailoring out a criterion silently buries a known-unknown risk.

---

## Chapter Index

| # | Section | Key content |
|---|---------|-------------|
| [ch01](chapters/ch01-mrl-deskbook-foundations-and-dod-policy.md) | Foundations & DoD Policy | Why MRLs exist (GAO findings, uncomparable metrics), what an MRA does, the PQM lead under DoDI 5000.88, phase-gated maturity, statutory/DFARS/NTIB basis, "responsible organization" |
| [ch02](chapters/ch02-mrl-deskbook-scale-threads-and-trl-relationship.md) | The Scale, Threads & MRL–TRL Relationship | MRL 1–10 per-level definitions, the non-linear ordinal nature, the five environments, manufacturability vs producibility, the nine threads/sub-threads, MRL vs TRL, critical technologies |
| [ch03](chapters/ch03-mrl-deskbook-adaptive-acquisition-framework.md) | MRLs in the Adaptive Acquisition Framework | AAF pathways (MCA/MTA/UCA/Business/Services), MRL-to-milestone mapping (4/6/7/8/9), the three courses of action on a shortfall, ITRA/SETR feed, MMP as a feeder |
| [ch04](chapters/ch04-mrl-deskbook-conducting-assessments.md) | Conducting MRL Assessments | The eight-activity flow (Figure 4-1), nine filtering questions, on-site selection, team independence, contractor self-assessment, the deep dive, top-down assess / bottom-up report, the ten-element report |
| [ch05](chapters/ch05-mrl-deskbook-maturation-plans-and-risk.md) | Manufacturing Maturation Plans & Risk | The MMP as the product of an assessment, the 12-item MMP outline, fallbacks with expiry dates, supplier/sub-tier risk, five risk-management best practices, not trusting the contractor alone (DCMA) |
| [ch06](chapters/ch06-mrl-deskbook-contract-language.md) | Applying MRLs in Contract Language | Criteria Matrix as non-directive, AS6500A tasking, RFP Section L/M, SOW "shall" statements, AS9100D/ISO 9001/IATF 16949 quality, DIDs (DI-MGMT-81889B etc.) on DD Form 1423, flow-down, FAR/DFARS floor |
| [ch07](chapters/ch07-mrl-deskbook-tailoring-and-users-guide.md) | Tailoring Criteria & the MRL Users Guide | The Excel Users Guide (six worksheets, six-field pop-ups), tailoring rules, S&T anchors, Sustainment Maturity Levels / Depot Activation, single/limited-system and space front-loading, the Navy ship 2-pass 6-gate map, industry adoption |
| [ch08](chapters/ch08-mrl-deskbook-ot-cybersecurity.md) | Operational Technology Cybersecurity | OT defined (NIST SP 800-37), OT vs IT/PIT/MIS, Federal vs Non-Federal System routing, NIST SP 800-53/171/82, FAR/DFARS clauses, SPRS, CMMC as wrapper not source, PTAC/MEP/CSET for small manufacturers |

## Topic Index

- **MRL — definition, non-linear ordinal scale, target-not-grade** → ch02, ch01
- **Why MRLs exist / GAO rationale / policy basis** → ch01
- **PQM lead / DoDI 5000.88 responsibilities** → ch01, ch03
- **Responsible organization** → ch01
- **MRL 1–10 per-level definitions** → ch02, cheatsheet
- **Demonstration environment (laboratory / production-relevant / production-representative / pilot line / production line)** → ch02, cheatsheet
- **Manufacturability vs producibility** → ch02
- **Nine manufacturing-risk threads and sub-threads** → ch02, cheatsheet
- **MRL vs TRL relationship / moving manufacturing left** → ch02, cheatsheet
- **Critical technology (CT)** → ch02
- **Adaptive Acquisition Framework / pathways (MCA, MTA, UCA)** → ch03, cheatsheet
- **MRL-to-milestone target mapping (MRL 4/6/7/8/9)** → ch03, cheatsheet
- **Three courses of action on a milestone shortfall** → ch03, ch05
- **Materiel Solution Analysis / TMRR / EMD phases** → ch03
- **Rapid Prototyping / Rapid Fielding (MTA)** → ch03
- **Urgent Capability Acquisition (UCA) targets** → ch03
- **ITRA / SETR / MRL Assessment as a feeder** → ch03
- **MRL Assessment process / eight-activity flow** → ch04, patterns
- **Taxonomy / what to assess / nine filtering questions** → ch04
- **On-site selection / site-visit agenda** → ch04
- **Contractor self-assessment** → ch04
- **Deep dive (sub-component examination)** → ch04
- **Top-down assess, bottom-up report / weakest-link rollup** → ch04
- **MRL Assessment report (ten elements)** → ch04
- **Manufacturing Maturation Plan (MMP) / 12-item outline** → ch05, cheatsheet
- **Fallbacks and the latest decision date** → ch05
- **Supplier and sub-tier risk** → ch05, ch06
- **Risk-management best practices / DCMA independence** → ch05, ch04
- **MRL Criteria Matrix (descriptive, not directive)** → ch06, ch02
- **AS6500A manufacturing-management tasking** → ch06
- **RFP Section L and Section M** → ch06
- **Statement of Work (SOW) "shall" statements** → ch06
- **AS9100D / ISO 9001 / IATF 16949 quality standards** → ch06
- **Data Item Descriptions (DIDs) / DD Form 1423 CDRL** → ch06
- **Requirements flow-down to suppliers** → ch06
- **Tailoring the MRL criteria** → ch07, patterns
- **MRL Users Guide (Excel worksheets, pop-ups, questionnaire)** → ch07
- **Science & Technology (S&T) MRL anchors** → ch07
- **Sustainment Maturity Levels (SML) / Depot Activation** → ch07
- **Single or limited system acquisition / space systems** → ch07
- **Ship acquisition / Navy 2-pass 6-gate** → ch07
- **Gated Product Development / industry adoption** → ch07
- **Operational Technology (OT) cybersecurity** → ch08, patterns
- **OT defined (NIST SP 800-37) / OT vs IT** → ch08
- **Federal vs Non-Federal System routing** → ch08
- **NIST SP 800-53 / 800-171 / 800-82** → ch08
- **DMZ / layered networks / ICS security concepts** → ch08
- **SPRS / DFARS 252.204-7019 7020** → ch08
- **CMMC as certification wrapper, not source** → ch08
- **PTAC / MEP / CSET small-manufacturer support** → ch08

## Supporting Files

- [glossary.md](glossary.md) — key MRL terms (MRL, MRA/Assessment, Criteria Matrix, the five environments, the nine threads, MMP, AS6500A, OT, SML, tailoring), alphabetical, with chapter references
- [patterns.md](patterns.md) — reusable patterns (map MRL targets to milestones, run the eight-activity flow, resist single-number/weakest-link rollups, build an MMP per shortfall, decide at a shortfall, put maturity into the contract, tailor without burying risk, screen OT cybersecurity) with When / How / Trade-offs
- [cheatsheet.md](cheatsheet.md) — MRL 1–10 table, the five environments, the nine threads, MRL vs TRL, pathway targets, milestone-target decision rules, and tells & smells

---

## Scope & Limits

**Covers**: DoD best practices for assessing and managing manufacturing maturity and producibility risk per the MRL Deskbook (Version 2022) — the MRL 1–10 scale and its non-linear, target-not-grade nature; the five demonstration environments; the nine manufacturing-risk threads and sub-threads; the manufacturability/producibility distinction; how MRL targets map onto Adaptive Acquisition Framework milestones across MCA/MTA/UCA; conducting an MRL Assessment and reporting it; building a Manufacturing Maturation Plan; embedding MRL maturity in contract language (Section L/M, the SOW, AS6500A, the quality standards, DIDs/CDRLs); tailoring the criteria for S&T, single/limited-system, ship, sustainment, and industry contexts; and screening operational-technology cybersecurity in the assessment.

**Thin or silent on** (where the source itself is light): the **MRL Criteria Matrix and MRL Users Guide content themselves** are not reproduced — the Deskbook points to the separately distributed Appendix A matrix and the Excel Users Guide for the per-thread, per-level criteria text, so this pack carries the framework and how to use it, not the cell-by-cell criteria. It is **not** a technology-readiness (TRL) guide (see `gao-tra`, which this pack deepens on the manufacturing side); **not** a full systems-engineering process model (see `dau-se-guidebook`, `nasa-se-handbook`, `nasa-npr-7123`); **not** a cost-estimating or schedule guide (see the GAO cost/schedule packs); and **not** a deep cybersecurity-audit method — Chapter 8 is an explicit top-level screen for major OT gaps, deferring to NIST SP 800-37/53/171/82 and CMMC for the actual controls and certification.

**Jurisdiction**: US DoD acquisition context. The Deskbook is explicitly "not a DoD requirement... offered as a best practice," and is tailorable to industry — the methods are adoptable by any organisation managing manufacturing risk, but the milestone, statute, FAR/DFARS, and clause references are DoD-specific.

**Source version**: Manufacturing Readiness Level (MRL) Deskbook, Version 2022 (1 October 2022 update), OSD Manufacturing Technology Program with the Joint Service/Industry MRL Working Group.
