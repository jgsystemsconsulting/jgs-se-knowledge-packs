# FAA AMS Lifecycle V&V Guidelines: Cheatsheet

Decision rules, gate maps, and checklist mechanics from the FAA AMS Lifecycle Verification
and Validation Guidelines, Version 4.0 (January 2023). Synthesized reference: paraphrased,
not source text.

## Quick Decision Rules

**"Verify or validate?"**
- *Verification* = built right: does it conform to a template, specification, standard, or policy?
- *Validation* = right thing: does it satisfy the operational need, user, and mission in the intended environment?
Run both, separately, on the item. A pass on one is not a pass on the other. (`ch01`)

**"Which tier am I in?"**
- *Work product*: anything that represents, defines, or directs the product (plans, designs, specs, models, prototypes, contracts).
- *Product component*: a lower-level element integrated upward, possibly in multiple levels.
- *Product*: the delivered system, service, enterprise capability, facility, or operational change.
V&V flows up the hierarchy: work products first, components before integration, product before operational acceptance. (`ch01`)

**"Which method do I use?"** Pick the catalog by tier x question:

| | Verification (built right) | Validation (right thing) |
|---|---|---|
| **Work product** | Inspections, peer reviews, audits, checklists | Discussions with users, user surveys, functional presentations, walk-throughs/dry runs, analyses, testing, demonstrations, modeling, storyboarding |
| **Product / component** | Inspections, peer reviews, audits, analyses, checklists, testing, demonstrations, simulations, accreditation | Discussions with users, user evaluation questionnaires, functional presentations, inspections, peer reviews, audits, analyses, checklists, testing, demonstrations, simulations |

Validation catalogs are broader and user-facing; product-tier verification adds analyses, testing, simulations, and accreditation. Method definitions live in `glossary.md`. (`ch02`)

**"Can I trust this criterion?"**
Only after the critical technical documents (NAS ConOps, NAS Requirements Document, NAS Segment Implementation Plan, National Air Research Plan, NextGen Implementation Plan, Enterprise Architecture) have themselves been V&V'd against FAA Strategic Initiatives plus each document's applicable standards. (`ch02`)

**"Are prerequisites clean?"**
While performing V&V, reviewers must stay cognizant of the validity of V&V performed (or missed) on prerequisite work products, components, and products. If earlier V&V is inconsistent, conflicts, or was skipped: document and resolve before proceeding. (`ch02`)

**"Is the program ready for the gate?"**
Only when the minimum work products for the decision point have cleared V&V per the phase table, and V&V events were planned as entrance criteria, scheduled well in advance, applied consistently, and the results actually support the decision point's objectives. (`ch02`, `ch03`, `ch04`)

**"A change is fielded. What V&V?"**
Both halves: verify the change against new or modified requirements and governing policy, and validate that the requirement or operational concept driving it is itself valid and still serves the mission. Table 6 names ISM DT and OT (IOA if applicable) as the major V&V activities. (`ch04`)

---

## Plan / Perform / Report / Decide Pipeline

- **Plan** (`ch02` §2.1): V&V planning is required for all acquisition programs and is embedded in phase and program planning documents (CRD plan, IA plans, ISPD, TEMP, PMP, SEMP, QA Plan), each carrying the nine planning elements that apply.
- **Perform** (`ch02` §2.2): independent stakeholders and reviewers, named in Tables 1-6, run matched methods, checking prerequisite V&V first. Work products get document-grade methods; products and components get T&E.
- **Report** (`ch02` §2.3): documentation is controlled and archived; minimum content: Introduction, Purpose, Criteria, V&V Approach, Participants, Results, Recommendations. Reporting feeds performance measurement against technical performance criteria.
- **Decide** (`ch02` §2.4): results are entrance criteria at decision points, aiding the Joint Resources Council, the Acquisition Executive Board, and in-service decision authorities. Surface technical and non-technical risk before the gate, not after.

## AMS Lifecycle Phase Map

| Phase | V&V focus (paraphrased) | Minimum set (table) | Chapter |
|---|---|---|---|
| **Service Analysis & Strategic Planning (SASP)** | Capabilities needed now and later (EA as-is/to-be + roadmaps) | Preliminary Shortfall Analysis, CRD Plan, ISS Risk Factors Assessment (Table 1) | `ch03` |
| **Concept & Requirements Definition (CRD)** | Needs into preliminary requirements + solution ConOps; shortlist alternatives (EA's own alternative included) | Preliminary PRD, concept of use, EA products/amendments, shortfall analysis, initial IA plan, Preliminary ISS Assessment (Table 2) | `ch04` |
| **Investment Analysis (Initial / Final)** | Which alternative, then baseline ready to commit | Initial: initial PRD/ISPD/BC, preliminary TEMP, EA updates. Final: final PRD/BC/ISPD, APB, PMP, initial TEMP, tailored ISR checklist, SIR (Tables 3-4) | `ch04` |
| **Solution Implementation (SI)** | Build/buy/test/field; Contract Award through ISD | Products and components via DT/OT/IOA; test artifacts themselves V&V'd; PDR/CDR baselines; safety and security gates (Table 5) | `ch04` |
| **In-Service Management (ISM)** | Sustain and change the fielded system | Verify change vs. requirements and policy; validate purpose; EA updates, NCPs, implemented changes, System Support Directives, ISPD updates (Table 6) | `ch04` |

*Research for Service Analysis (RSA)* is a non-phase activity feeding SASP, CRD, IA, and early SI, sharing reviewers (`ch03`).

## Decision Points and Gates

| Gate | Acronym | Sits at end / within |
|---|---|---|
| Concept & Requirements Definition Readiness Decision | CRDRD | SASP (`ch03`) |
| Investment Analysis Readiness Decision | IARD | CRD (`ch04`) |
| Initial Investment Decision | IID | Initial IA (`ch04`) |
| Final Investment Decision | FID | Final IA (`ch04`) |
| Contract Award / Product Demonstration / Product Acceptance-CAI / Production Decision / In-Service Decision | CA / PD / CAI / Prod / ISD | SI (`ch04`) |
| Decision to Implement / Deploy an Improvement or Change | — | ISM (`ch04`) |

## Nine Planning Elements (paraphrased)

1. Verification methods · 2. Validation methods · 3. Items to V&V · 4. Processes, standards, and criteria (SEM, Concept Development and Validation Guidelines, T&E Handbook) · 5. Tracking measures and reports · 6. Roles and responsibilities · 7. Independent stakeholders/reviewers identified · 8. Tools, models, prototypes, labs, simulators · 9. Required training. (`ch02`)

## Four Appendix B Checklist Documents

| Document | Acronym | Checklist mechanics |
|---|---|---|
| Program Requirements Document | PRD (final: FPRD) | Each checklist names key elements that must be verified or validated; per key element, record methods used and artifacts produced (`ch03`, `ch04`) |
| Acquisition Program Baseline | APB | Same mechanics; performance, cost, schedule baselines for a program segment (`ch03`, `ch04`) |
| Implementation Strategy & Planning Document | ISPD | Same mechanics; overall implementation strategy and planning (`ch03`, `ch04`) |
| Program Management Plan | PMP | Same mechanics; how the service team executes the ISPD strategy (`ch03`, `ch04`) |

Common rule: a checklist row is complete only when the acceptance assessment, the method used, and the artifact produced are all recorded. The Business Case is deliberately outside the set: Investment Planning & Analysis verifies and validates it under the AFI Business Case Evaluation and Assessment Guideline, and the Independent Evaluation Review (IER) satisfies documentation and reporting requirements (`ch03`).

## T&E Triad (product/component V&V)

| Activity | Serves | Run by |
|---|---|---|
| **Development Test (DT)** | Verification | Developer, witnessed by FAA (`ch02`, `ch04`) |
| **Operational Test (OT)** | Validation | OT Test Director + OT test team (Air Traffic, Technical Operations, second-level maintenance; external entities as required) (`ch02`, `ch04`) |
| **Independent Operational Assessment (IOA)** | Independent operational-readiness determination | PM and Independent Safety Assessment Team, for designated products (`ch02`, `ch04`) |

Concentrated in Solution Implementation and In-Service Management. PDR gates the allocated baseline; CDR gates the product baseline; ISD is the operational-readiness gate. (`ch04`)

## Snapshot Discipline

- Tables 1 through 6 are January 2023 policy snapshots. Each table's own footnote says detailed phase guidelines and templates exist and should be reviewed for current guidance. Treat criteria, offices, and form numbers as illustrative, not live authority. (`ch03`, `ch04`)
- Figure 4 shows primary emphasis only; the tables carry the required minimum (`ch03`). The ARM is a relationship diagram, not a process flow (`ch03`).
- The verification/validation definitions trace to CMMI for Development, Version 1.2 (SEI, August 2006). Paraphrase and cite; never copy. (`ch01`)
