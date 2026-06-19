# NASA HSI Practitioner Guide Cheatsheet

## Core Decision Rules

| Situation | Action |
|---|---|
| Joining a new P/P as HSI lead | Read current SEMP and HSI Plan (if they exist). Run the Appendix B checklist. Identify life-cycle phase and current open products. Do a gap analysis against the Product Maturity Matrix. |
| Program management asks "do we need a full HSI Plan?" | Use the two-axis scale: (1) Human Safety Category per NPR 7120.5E (I/II/III) and (2) Human Involvement (tight/moderate/loose coupling). Category I + tight coupling = standalone HSI Plan mandatory. |
| Design trade study includes human vs. automation option | Apply function allocation process. Use crew time as cost-equivalent metric. Check workload, training burden, maintenance man-hours, and skill requirements. Document in trade study report. |
| Team says "we'll address HSI after CDR" | Escalate. Post-CDR HSI changes are very expensive. LCC is locked in early. The right time is Pre-Phase A. Even if late, start immediately — a gap analysis must identify which Pre-Phase A/Phase A products were skipped. |
| HITL activity is planned in Phase B or C | Formally pre-declare it for Phase D V&V credit now. Document the specific requirement(s) it will close, the "test as you fly" conditions, and get SE/TA concurrence. |
| COTS product is under consideration | Run the HSI screening checklist: usability, crew task time, crew safety, interface suitability, lifecycle obsolescence, training requirement. Do not accept standard functional assessment as sufficient. |
| Phase E anomaly or operational problem appears | Investigate for HSI root cause. Collect data (crew time, error incidents, physiological data). Document lessons learned with explicit link to Phase A-C design decisions. Feed corrections to sustaining engineering. |

---

## Quick-Reference: HSI Milestone Map

| Milestone | Phase | Key HSI Deliverables |
|---|---|---|
| MCR | Pre-Phase A | Initial ConOps draft; preliminary MOEs; function allocation initiated; HSI planning started |
| SRR | Phase A | ConOps baseline; HSI team formed; HSI requirements baselined; MOPs/TPMs established |
| SDR/MDR | Phase A | HSI requirements updated for new allocations; TPMs tracked |
| PDR | Phase B | Human requirements agreed; V&V framework established; HITL mockups/models produced |
| CDR | Phase C | Detailed requirements baselined; all trade studies complete; production/training/logistics plans |
| TRR | Phase D | HSI inputs to system-level test objectives, plans, procedures |
| SAR | Phase D | All HSI V&V closure records; validated analytical models; ops/training support products |
| ORR/FRR | Phase D | Human Rating Certification Package inputs; risk management plan updated |
| PLAR/CERR/PFAR | Phase E | Human-system readiness inputs; lessons learned; TPM final values emerging |
| DR | Phase E/F | Final TPM values; final lessons learned |
| DRR | Phase F | HSI inputs to decommissioning and disposal plan; knowledge archived |

---

## Tells and Smells (Warning Signs)

**Smell: "HSI" means only HFE displays/controls work**
Tell: The program has a human factors engineer reviewing cockpit layouts but no ConOps, no function allocation, and no HSI domain coverage beyond HFE.
Fix: Expand to all six HSI domains. Initiate ConOps if not already started.

**Smell: HSI Plan written once at program start, never updated**
Tell: The HSI Plan version number matches the SRR date. No updates since.
Fix: Update the HSI Plan at every major review. It must reflect current design maturity, current risks, and current product commitments.

**Smell: Budget is the primary argument for reducing HSI effort**
Tell: "We don't have budget for a full HSI team." Program is Category I safety risk.
Fix: The guide explicitly warns against budget-driven HSI scoping. Escalate to TA channels. Use LCC models and case studies to justify HSI investment.

**Smell: V&V left to Phase D**
Tell: No HITL plan, no V&V framework, no pre-declarations exist at CDR.
Fix: Establish the V&V approach for every HSI requirement at the time it is written. Plan Phase B/C HITL activities and pre-declare them immediately.

**Smell: Training plan starts at CDR**
Tell: "We'll figure out training after the design is final."
Fix: Training domain participation must begin in Pre-Phase A. Early training consideration identifies design features that reduce training burden and cost.

**Smell: ConOps is a paragraph, not a document**
Tell: There is a brief "system overview" but no operational scenarios, no off-nominal cases, no function allocation rationale.
Fix: ConOps must cover nominal, emergency, and contingency scenarios for all human actors (flight crew, ground crew, maintainers). It is the left side of the SE V and the validation anchor.

**Smell: No crew time data collected in operations**
Tell: Phase E monitoring captures hardware anomalies and sensor data but no crew time, error incidents, or task time.
Fix: Establish crew time and human performance data collection plans in Phase D as part of Phase E monitoring setup. This data is the primary source for HSI lessons learned and LCC validation.

---

## The Four HSI Key Concepts (Always True)
1. **System = hardware + software + human** — all three on equal footing.
2. **All personnel across the full lifecycle** — users, operators, maintainers, trainers, logistics, ground control.
3. **Integration and collaboration** — HSI resolves cross-domain conflicts before P/P management must engage.
4. **Early is mandatory** — HSI in Pre-Phase A maximises LCC savings. Late HSI is expensive and often ineffective.
