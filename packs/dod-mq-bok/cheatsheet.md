# DoD M&Q BoK Cheatsheet

Decision rules, selection tables, and tells & smells for applying the DoD Manufacturing and Quality Engineering Body of Knowledge (Version 3.0, July 2025). Synthesized, not reproduced.

## Quick Decision Rules

**"When do M&Q considerations start?"**
At Pre-MDD — before a design exists, before the AoA. The leverage to influence producibility and life-cycle cost is highest at the front end and falls as the design freezes.

**"What is the one question M&Q keeps asking?"**
*"Can it be built?"* — i.e. can this solution be produced with available capability while meeting quality, rate, cost, and schedule. That is manufacturing feasibility, and it recurs in every phase.

**"How mature does manufacturing need to be at this gate?"**
Read the maturity claim against the phase-appropriate MRL target, never as an absolute. Broad targets: MRL 4 → Milestone A · MRL 6 → Milestone B/PDR · MRL 7–8 → EMD/CDR · MRL 8 → Milestone C/PRR · MRL 9–10 → production. (Source is inconsistent on the exact FRP target; treat the higher band as gating.)

**"Which features do I control?"**
The vital few. Translate KPPs/KSAs into Key Characteristics (Pareto principle), promote to Critical Characteristics where safety/catastrophic failure is at stake, and target Cpk ≥ 1.33 (or as the customer specifies).

**"Capable or in control?"**
Both, and they are different. *Capable* = meets specification (Cp/Cpk). *In control* = statistically predictable (SPC/control charts). A process must be both before you trust its output.

**"Does M&Q have authority?"**
No — M&Q influences, it does not sign. The deliverable is credible M&Q input embedded in someone else's document (ICD, AoA guidance, SEP, RFP Sections L/M, the milestone determination).

---

## The Acquisition Lifecycle (AAF / MCA path) → M&Q focus

| Phase | Gate after | M&Q centre of gravity | Key review |
|---|---|---|---|
| **Pre-MDD** (Ch 1) | MDD | Feasibility of each concept; producibility into ICD/AoA guidance | — |
| **MSA** (Ch 2) | Milestone A | Pick a producible concept; KPP→KC translation; industrial-base assessment | ASR |
| **TMRR** (Ch 3) | Milestone B | Drive risk down; prototype; mature processes toward EMD | SRR · SFR · **PDR** |
| **EMD** (Ch 4) | Milestone C | Influence design, prepare for production, execute the plans; pilot line | **CDR** · TRR · SVR/FCA · PCA · **PRR** |
| **P&D** (Ch 5) | FRP decision | LRIP → Full-Rate Production; demonstrate rate maturity | MRA at MRL 9/10 |
| **O&S** (Ch 6) | (disposal) | Sustainment, supply chain, obsolescence, O&S cost control | **ISR** · ILA |

---

## The Twelve M&Q Threads (A–L) — the constant scaffold

| | Thread | | Thread |
|---|---|---|---|
| **A** | DoD Acquisition System | **G** | Materials Management |
| **B** | Defense Contracting System | **H** | Process Capability and Control |
| **C** | Surveillance System | **I** | Quality Management |
| **D** | Technology and Industrial Base | **J** | Manufacturing Workforce |
| **E** | Design | **K** | Facilities |
| **F** | Cost and Funding | **L** | Manufacturing Management and Control |

Built on the **"5 Ms"** — Manpower, Machines, Materials, Methods, Measurement — plus MRL criteria and three DoD-unique functions (acquisition, contracting, surveillance). Each thread decomposes into Activities → Tasks → Tools → Resources.

---

## Standards Stack (know these by number)

| Standard | Covers |
|---|---|
| **AS6500** | Manufacturing Management Program (the MMS benchmark) |
| **MIL-HDBK-896** | How to implement AS6500 on DoD programs |
| **AS9100 / ISO 9001** | the QMS (quality-system) standard |
| **AS9103** | controlling variation in Key Characteristics |
| **AS9145** | APQP — advance product/process quality planning, plus PPAP |
| **AS9102** | First Article Inspection |
| **AS5553 / AS6174** | Counterfeit electronic parts / counterfeit materiel avoidance |
| **IEEE 15288.1 / .2** | SE on defense programs / technical reviews and audits |
| **MIL-STD-881** | Work Breakdown Structure |

---

## The RIO Risk Engine (reused in every phase)

**Plan → Identify → Analyze (likelihood × consequence) → Mitigate (accept / avoid / transfer / control) → Monitor.**
Miss an MRL or capability target → write a **Manufacturing Maturation Plan**. Expect an **ITRA** (per DTRAM) at Milestones A/B/C and the FRP decision — an *independent* judgment that may not track the MRL/TRL numbers.

---

## Process Capability Vocabulary

- **Cp / Cpk** — capability of an established, in-control process (predicts conformance).
- **Pp / Ppk** — performance: how a process actually ran over time (whole-population sigma).
- **KC / CC** — Key Characteristic (control variation to meet requirements) / Critical Characteristic (variation risks loss of life or catastrophic failure).
- **KMP** — Key Manufacturing Process: creates or affects a KC/CC.
- **Yield** — First Pass · Rolling Throughput · Final.
- Toolkit: SPC, DOE, MSA, FMEA (D/P/Criticality), QFD, DFMA, Value Stream Mapping, Root Cause Analysis, Lean (TIMWOOD wastes), Six Sigma/DMAIC.

---

## Tells & Smells

- **M&Q shows up only after a design exists** → leverage already lost; cost is locked in.
- **AoA looked at one or two alternatives** → narrow trade space; the BoK ties this to worse cost/schedule outcomes.
- **Maturity claimed as an absolute ("it's mature")** → mature *for which phase*? Score it against the phase MRL target.
- **Every characteristic treated as critical** → no Pareto focus; inspection cost balloons, vital few get diluted.
- **Process is "capable" but never charted** → capable ≠ in control; demand SPC evidence.
- **Rate production entered without a pilot line / FAI** → process discovery pushed into the lot, where defects multiply.
- **Supplier certificate accepted as proof of quality** → a conforming QMS does not guarantee a conforming product; reach the actual process/product evidence.
- **No view below the first-tier supplier** → most supply-chain risk (sole/single/fragile/foreign sources, counterfeits) hides there.
- **Self-assessed risk with no independent challenge** → that is exactly the gap the ITRA mandate fills.
- **O&S treated as an afterthought** → O&S usually dominates life-cycle cost; govern it with the LCSP, ISR, and ILA.
- **Same plant assumed to behave identically after a line move** → variability from disassembly/move/reassembly is real even with the same workforce.
