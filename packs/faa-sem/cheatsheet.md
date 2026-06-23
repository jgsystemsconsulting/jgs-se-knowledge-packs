# FAA Systems Engineering Manual — Cheatsheet

## Quick Decision Rules

**"Is this a Risk, an Issue, or an Opportunity?"** (ask: *has it happened yet?*)
- Not yet, and bad → **Risk** (`if [cause], then [impact]`; likelihood A–E × impact 1–5; give it a realization date)
- Already / certainly, and bad → **Issue** (`due to [cause], [impact] was experienced`; skip likelihood, score impact only)
- Not yet, and good → **Opportunity** (`[impact] may be achieved if [cause]`)
- Classify by **root cause, not symptom**. Funding cuts are usually *not* a program risk (decided at Agency level).

**"Verification or Validation?"**
- "Built it right" — conformance to requirements/specs, incremental, supported by Development Test (DT) → **Verification**
- "Built the right thing" — fulfills purpose in the intended environment, iterative and early, supported by OT/IOA → **Validation**
- Validation criteria come mainly from the ConOps and the NAS Enterprise Architecture.

**"Allocate a function or a requirement?"**
- **Never allocate a function.** Convert function → PRS → MRS, then allocate the *requirement* to the physical architecture (tracked in the RAM).

**"Which loop when alternatives fail?"**
- **All** alternatives fail the **same** requirements → functional architecture suspect → **design loop**
- Compliance **varies** across alternatives → requirements suspect → **requirements feedback loop**

**"Can I request the Final Investment Decision?"**
- Only with an approved **fPRD** and a requirements set **≥ 80% stable** (recommended: no change for the last quarter). CPRs finalized and copied verbatim into the APB.

**"Should I spec availability?"**
- For software-intensive information systems: **no** — allocate dependability by **Service Thread / STLSC** instead. Availability stays a planning/trade/operational metric only.
- Distributed/remote and infrastructure systems: **no top-down allocation** — use lifecycle-cost reasoning + SME judgment (failure-independence assumptions break).

**"Policy or guidance?"**
- The **SEM is guidance** (a tailorable menu of proven practices). Binding acquisition policy lives in the **AMS** (FAST), and discipline detail lives in the FAA orders/handbooks the SEM points to.

---

## The AMS Lifecycle — 5 Phases, 5 Decision Points

| # | Phase | Concluding decision point |
|---|-------|---------------------------|
| 1 | Service Analysis & Strategic Planning | (1) Concept & Requirements Definition Readiness Decision |
| 2 | Concept and Requirements Definition (CRD) | (2) Investment Analysis Readiness Decision |
| 3 | Investment Analysis (Initial → Final IA) | (3) Initial Investment Decision · (4) Final Investment Decision |
| 4 | Solution Implementation (Product Realization → Deployment & Transition) | (5) In-Service Decision |
| 5 | In-Service Management | (feeds shortfalls back to Service Analysis) |

**Requirements maturity ratchet:** pPR/pPRD (CRD) → iPR/iPRD (Initial IA) → fPR/fPRD (Final IA) → system specifications. Contract track in lockstep: SIRs / Statements of Work.

---

## The 7 Technical Management Disciplines (over a mandatory QMS)

1. Integrated Technical Management (ITM) · 2. Interface Management · 3. Risk Management (RIO) · 4. Configuration Management · 5. SE Information Management (SEIM) · 6. Decision Analysis · 7. Verification and Validation.

---

## The Five FAA Baselines

| Baseline | Established | Note |
|----------|-------------|------|
| **Functional** | after concept exploration | first formal baseline |
| **Allocated** | typically after SRR | design requirements |
| **Product** | after **both** FCA and PCA pass | delivered configuration |
| **Facility** | as-built | facility space + critical power-panel data |
| **Operational** | post-deployment | product baseline localized to NAS conditions + in-service changes |

---

## Reviews & Audits (entry/exit-criteria gates)

`TRA · SRR · SDR · SSR · PDR · CDR · TRR · ISR · FCA · PCA · PRR` — plus the nine-level Technology Readiness / Levels of Maturity scale used in the TRA. SRR establishes the allocated baseline; PDR is often the last viable point for technology insertion; CDR judges readiness to start manufacturing; FCA verifies functions/performance; PCA confirms documentation matches the as-built system.

---

## RIO at a Glance

- **Five steps:** Identify → Analyze & Assess → Develop Plan → Execute Plan → Track & Monitor.
- **Plan strategies:** Avoid · Transfer · **Control** (most common) · Accept · Research and Knowledge.
- **Rating:** Level (High/Med/Low) + Alpha (likelihood A–E) + numeric (impact 1–5). Issues have no likelihood.
- **Governance:** Risk Management Board (RMB) dispositions per the status lifecycle; escalate/transfer across program-portfolio-enterprise; report aggregate on a Probability Impact Diagram (PID); major programs feed OMB Exhibit 300 (Circular A-11).

---

## Interface Management Compliance Chain

`ICD (as-built design) → complies with → IRD (requirements) → complies with → fPRD`
Change path runs the other way: **ICR → IWG → CM**. Governed by FAA-STD-025f; services use WSRD/WSDD under FAA-STD-070/065.

---

## RMA — Service Thread Loss Severity Categories (STLSC)

| Category | Availability target | Note |
|----------|--------------------|------|
| **Essential** | .9999 | capacity reduction, localized efficiency impact |
| **Efficiency-Critical** | .99999 | economic-efficiency impact, possibly system-wide |
| **Safety-Critical** | two independent .99999 threads | no single thread may carry it |

No "routine" category exists — a top-down allocation for routine service yields unacceptably low requirements. Hazard/failure methods: **FTA** (top-down, may miss non-obvious top events) and **FMEA/FMECA** (bottom-up; add criticality for FMECA).

---

## Specialty Engineering Anchors

| Discipline | Governing references |
|------------|---------------------|
| **RMA** | FAA RMA Handbook (FAA-HDBK-006A); NAPRS / FAA Order 6040.15 |
| **LCE / ILS** | six-step LCE; nine ILS/NAILS elements; ISPR/OEA/ISR-ISD; COTS Risk Mitigation Guide |
| **E3 / Spectrum** | FAA-G-2100, ANSI C63.14, FCC Title 47 Part 15; FAA Order 6050.19, ATC Spectrum Engineering Services, NTIA |
| **HFE** | Human Factors Acquisition Job Aid (FAST); Human Performance Interfaces taxonomy; 24 Areas of Interest |
| **ISE** | FISMA, FIPS 199/200, NIST RMF (SP 800-37), FAA Order 1370.82A; CSAM tool |
| **SSE** | SMS Manual, SRMGSA, FAA Order 8040.4; SRM 5-phase loop; OSA→CSA→PHA→SSHA→SHA→O&SHA→SSAR |
| **HMM/EE/EOSH** | CAA, CWA, NEPA, RCRA, OSHA; cradle-to-grave; hazardous-materials inventory |

---

## Tells & Smells (when something is off)

- A requirement with **no verification method** → invalid (not a real requirement); fix the VRTM.
- A requirement using **"should"**, **"and/or"**, or vague "minimum/maximum" → rewrite (`shall`/`will`/`may` + explicit relational operators).
- A **preliminary requirement that names a solution** → biases the alternatives comparison; make it solution-agnostic.
- A **FAD left frozen** while requirements/architecture evolve → it's a living document; re-evaluate it.
- A **risk stated as its mitigation plan** → restate by root cause; keep mitigation separate.
- **Security added late / treated as standalone** → converts to residual risk + POA&Ms; categorize-then-tailor early and embed it.
- **Tailoring the ISPD by addition** → tailoring is by *deletion* with documented rationale; additions only for program-unique needs.
- **Trusting SoS assurance for free** → networking can add vulnerabilities; reassess safety/security/reliability of the combination.
