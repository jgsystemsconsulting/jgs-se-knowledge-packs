# FAA AMS Lifecycle V&V Guidelines — Cheatsheet

Decision rules, selection tables, and tells from the FAA AMS Lifecycle V&V Guidelines,
Version 3.0 (April 2017). Synthesized reference — paraphrased, not source text.

## Quick Decision Rules

**"Verify or validate?"**
- *Verification* = built right — does it conform to its template / specification / standard / policy?
- *Validation* = right thing — does it satisfy the operational need, the user, and the mission once in its environment?
Run both, separately, on every artifact. A pass on one is not a pass on the other.

**"Which tier am I in?"**
- *Work product* — anything that represents, defines, or directs the product (plans, designs, specs, requirements, models, prototypes, contracts).
- *Product component* — a lower-level element integrated upward.
- *Product* — the delivered system/service/facility/operational change.
V&V flows up: work products first, components before integration, product before operational acceptance.

**"Which method do I use?"** — pick the catalog by tier × question:

| | Verification (built right) | Validation (right thing) |
|---|---|---|
| **Work product** | Inspection, Peer Review, Audit, Checklist | + Discussions w/ users, User Survey, Functional Presentation, Walk-through/dry run, Analysis, Testing, Demonstration, Modeling, Storyboarding |
| **Product / component** | Inspection, Peer Review, Audit, Analysis, Checklist, Testing, Demonstration, Simulation, **Accreditation** | Discussions w/ users, User Evaluation Questionnaire, Functional Presentation, Inspection, Peer Review, Audit, Analysis, Checklist, Testing, Demonstration, Simulation |

(Validation catalogs are user-facing and broader; product-tier verification adds analysis, testing, simulation, and accreditation. Definitions: Appendix C.)

**"Is this V&V complete?"**
Every checklist row needs *method used* + *artifact* (an objective, authenticated record). Passing rows with empty evidence columns = incomplete by definition.

**"Can I trust this criterion?"**
Only if it was itself V&V'd. Criteria are work products, not axioms. Foundational documents (NAS ConOps, NAS Requirements Document, EA, NSIP, NARP, NextGen Implementation Plan) get V&V'd against FAA Strategic Initiatives *before* downstream use.

**"Is the program ready for the gate?"**
Only when the minimum work products for that decision point have cleared V&V per the phase table — and (in early lifecycle) both the Appendix B track and the Business Case / IER track have reported.

**"A change is fielded — what V&V?"**
Both halves: verify the change against new/revised requirements + policy; validate that the requirement/concept driving it still serves the mission (Post-Implementation Review, Operational Analysis).

---

## AMS Lifecycle Phases & Their V&V Emphasis

| Phase | Decides | Primary V&V emphasis | Chapter |
|---|---|---|---|
| **Service Analysis & Strategic Planning (SASP)** | What capability the agency needs (EA as-is/to-be + roadmaps) | Validate Preliminary Shortfall Analysis, CRD Plan, ISS Risk Factors Assessment | Ch 3 |
| **Concept & Requirements Definition (CRD)** | Need → preliminary requirements + solution ConOps | Validate preliminary requirements, concept of use, EA products, shortfall analysis, initial IA plan, Preliminary ISS | Ch 3 |
| **Investment Analysis — Initial** | Which alternative? | Validate alternatives → recommend to IDA | Ch 4 |
| **Investment Analysis — Final** | Is the baseline ready to commit? | Validate program baseline (final PRD/BC/ISPD, APB, PMP, initial TEMP, SIR, ISR checklist) | Ch 4 |
| **Solution Implementation (SI)** | Build/buy/test/field the solution | DT (verify) + OT/IOA (validate); PDR/CDR; safety & security gates | Ch 5 |
| **In-Service Management (ISM)** | Sustain & change the fielded system | Verify change vs. requirements; validate purpose still served; ISM DT/OT/IOA | Ch 6 |

*Research for Systems Analysis (RSA)* is a non-phase activity feeding SASP/CRD/IA/early SI, sharing their reviewers. Figure 3 shows *emphasis* only — Tables 1–6 define the required minimum set.

---

## Decision Points → Gates (with acronyms)

| Gate | Acronym | Sits at end of / within |
|---|---|---|
| Concept & Requirements Definition Readiness Decision | CRDRD | end of SASP |
| Investment Analysis Readiness Decision | IARD | end of CRD |
| Initial Investment Decision | IID | Initial IA |
| Final Investment Decision | FID | Final IA |
| Contract Award / Product Demonstration / Production / In-Service Decision | — / — / — / ISD | Solution Implementation |
| Decision to Implement a Change / Decision to Deploy a Change | — | In-Service Management |

---

## The Nine V&V Planning Elements (§2.1)

Fold these (as they apply) into ISPD, TEMP, PMP, SEMP, QA Plan, and phase plans:
1. Verification methods · 2. Validation methods · 3. Items to be V&V'd · 4. Processes/standards/criteria · 5. Tracking measures & reports · 6. Roles & responsibilities · 7. Identification of independent reviewers · 8. Tools/models/prototypes/labs/simulators needed · 9. Required training.

## V&V Report — Minimum Content (§2.3)

Introduction · Purpose · Criteria · V&V Approach · Participants · Results · Recommendations. Reports must be controlled, archived, and feed performance measurement.

---

## The Four Appendix B Checklist Documents

| Document | Acronym | V&V via | Through-line |
|---|---|---|---|
| Program Requirements Document | PRD (→ fPRD) | Appendix B checklist | Requirement-quality bar; CPRs identified |
| Acquisition Program Baseline | APB | Appendix B checklist | CPRs consistent with PRD, each with its value |
| Implementation Strategy & Planning Document | ISPD | Appendix B checklist | Program controls track CPRs |
| Program Management Plan | PMP | Appendix B checklist | WBS validated by all engineering domains |

(Business Case is V&V'd separately — Investment Planning & Analysis → IER, *not* an Appendix B checklist.)
Common skeleton: **template conformance → content → stakeholder validation**.

---

## Requirement-Quality Bar (PRD checklist)

Each requirement: clearly stated · unambiguous · complete · necessary & traceable · verifiable/measurable/testable · solution-independent. For the **fPRD**: also achievable against current/emerging technology. Complete against: EA, Solution ConOps, Functional Analysis Report, EA Shortfall Analysis, Investment Analysis Assessments (fPRD), and applicable specs (e.g., NAS-RD-2010, NAS-RD-2025).

---

## Method Codes (Appendix B legend)

`I`=Inspection · `P`=Peer Review · `A`=Audit · `C`=Checklist · `D`=Discussion · `U`=User Survey · `F`=Functional Presentation · `W`=Walk-through/dry run · `An`=Analysis · `T`=Testing · `Dem`=Demonstration · `M`=Modeling

**Method tells (Appendix C):**
- *Analysis* — compare design vs. known principles/data/practice.
- *Inspection* — visual observation / mechanical measurement / doc examination.
- *Demonstration* — qualitative, during a dynamic test; **software functional requirements usually validated this way** (behavior observed through a secondary medium).
- *Testing* — operate under specified conditions, record, evaluate.
- *Audit* — independent compliance examination (incl. data security/integrity).
- *Peer review* — unbiased SMEs independent of the work product's development/approval.
- *Accreditation* — formal certification a test capability is acceptable for a specific application.

---

## T&E Triad (product/component V&V)

| Activity | Serves | Run by |
|---|---|---|
| **Development Test (DT)** | Verification | Developer (FAA witnessing) |
| **Operational Test (OT)** | Validation | ANG-E OT Test Director + team (Air Traffic, Tech Ops, 2nd-level maintenance) |
| **Independent Operational Assessment (IOA)** | Independent operational-readiness read | PM from Independent Safety Assessment Team (designated products) |

Concentrated in Solution Implementation and In-Service Management. PDR → allocated baseline; CDR → product baseline.

---

## Tells & Smells (anti-patterns)

- **Treating "process was followed" as proof.** That's QA, not V&V. QA checks process adherence; V&V checks requirements/mission/risk. Don't conflate them.
- **Reading Figure 3 as the required V&V set.** It shows emphasis only — the minimum set lives in Tables 1–6.
- **Trusting the published tables as current authority.** Tables 1–6 are policy *as of publication (April 2017)*; current detailed phase guidance and templates supersede them.
- **Skipping front-end paperwork V&V "to save time."** Early planning/requirements documents seed every downstream verification — under-validating them propagates the wrong product forward undetected.
- **Empty evidence columns.** A passing checklist with no named artifacts is incomplete by the source's own definition.
- **Verifying a change but not re-validating its purpose (ISM).** Conformance to spec ≠ still serving the mission. Both passes mandatory.
- **Quoting CMMI verbatim.** The verification/validation definitions trace to CMMI v1.2 (SEI) — a copyrighted model. Paraphrase and cite; never copy.
