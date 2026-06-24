# FAA-HDBK-006D (RMA) Cheatsheet

Guidance only — the handbook is explicit it must **not** be cited as a requirement. Use the **006D (2020)** revision, not 006B.

## Quick Decision Rules

**"Where do I start an RMA requirement?"**
With **criticality**, never a number. Locate the **service thread**, run the Service Risk Assessment, get a severity category, then read the NAS-RD target.

**"Which availability number do I mean?"**
Name the variant. **Operational (A_op)** counts all downtime (what the user feels); **Equipment & Services (A_es)** drops scheduled downtime; **Inherent (A_i) = MTBF/(MTBF+MTTR)** counts corrective-only. A number with no named variant is not comparable.

**"MTBF or MTBO?"**
**MTBF** for systems/subsystems; **MTBO** (and uMTBO) for services/facilities — the FAA substitution. MTTR is the restore-time measure.

**"No data to compute a figure of merit?"**
Use a **distribution** matched to the phenomenon — but it is a model, not truth. Never use the Normal for time variables.

**"One failure analysis or two?"**
Two. **FMEA** bottom-up + **FTA** top-down; neither is trusted alone. Add criticality to get **FMECA**.

**"Top-down availability allocation — always?"**
No. Only for **Information Systems**. Wrong for Remote/Distributed (graceful degradation) and Infrastructure (correlated failures).

**"Can I prove software reliability before fielding?"**
Usually not. **Field-then-grow**: predict before contract, then run a reliability-growth program on problem-report metrics.

---

## The Three Pillars (+ umbrella)

| Pillar | Plain definition | Headline metric |
|---|---|---|
| **Reliability** | probability of zero failures over an interval/mission | MTBF / uMTBO; R = e^(−t/m) |
| **Maintainability** | how easily/quickly restored after failure | MTTR (sMTTR / uMTTR) |
| **Availability** | % of time ready when called upon | A_op / A_es / A_i |
| **Dependability** | the combined R-M-A picture | (umbrella term) |

`Availability = uptime / (uptime + downtime)` · narrow engineering form `= MTBF / (MTBF + MTTR)`.

## The Four Severity Categories (NAS-RD-2013)

| Category | Availability floor | Restore time (illustrative) |
|---|---|---|
| **Safety-Critical** | ≥ 0.99999 (≥ 2 service threads) | seconds |
| **Efficiency-Critical** | ≥ 0.9999 | ~6 s |
| **Essential** | ≥ 0.999 | ~10 min |
| **Routine** | ≥ 0.99 | up to 72 h |

Targets are **overall system/service** values; subsystem values are **derived by analysis**. Safety-Critical is satisfied by ≥ 2 independent Efficiency-Critical threads, not a single number.

## The "Nines" of Availability

Each added nine cuts allowed downtime by an order of magnitude: one nine (90%) ≈ 36.5 days/yr down; out to seven nines (99.99999%). Higher targets need disproportionately more data to demonstrate.

## The Four RMA Stages → AMS Phases (11 steps)

| Stage | AMS phase | Steps |
|---|---|---|
| **Concept/Operational Assessment** | SA&SP, CRD | 1 identify service thread · 2 determine criticality · 3 allocate parameters |
| **Requirements Development** | CRD, IA | 4 examine architecture · 5 analysis · 6 develop RBD · 7 allocate RMA reqs |
| **Testing & Implementation** | Solution Implementation | 8 test artifacts · 9 reliability growth |
| **Monitoring & Post-Implementation** | In-Service Management | 10 collect/report data · 11 corrective action |

Left side of the **Vee** = determine requirements; right side = verify & validate. Iterative, not waterfall.

## The Six Technical-Management Tasks (acquisition side)

1 Preliminary Requirements Analysis (the bridge) · 2 Procurement Package Prep (**SSD/SOW/IFPP**) · 3 Proposal Evaluation (reliability + fault-tolerant design + performance; **recovery-time substantiation** is critical) · 4 Design Monitoring (reviews, TIMs, separate fault-tolerance risk threads) · 5 Testing & Verification (fault-tolerance / functional / reliability-growth) · 6 Requirements Analysis & Maintenance.

## The RMA Toolbox (Section 7)

| Design-time (7.1) | Test-time (7.2) |
|---|---|
| Bathtub Curve · QFD · RBD · FMEA · FMECA · FTA · Ishikawa · Monte Carlo · Bayesian Network | FRACAS/DCACAS · Accelerated Life Testing · Parts Screening · Stability Tests · Reliability Growth Tests · Failure Recovery Tests |

Tool choice is **deterministic** — read it off your AMS phase + RMA stage (Table 7-1, Figure 7-6). **FMECA ↔ FRACAS** is a reinforcing loop.

## The Seven Distributions

Normal (symmetric repair variation — not for time) · Exponential (memoryless, constant rate; MTBF = 1/λ) · Poisson (rare-event counts) · Lognormal (positive-only, skewed repair) · Binomial (yes/no trials) · Weibull (tunable trend; = Exponential at shape 1) · Empirical (nothing parametric fits). **Lognormal and Weibull** are the reliability workhorses.

## The fault → error → failure chain

**Fault** (deviation from required behavior; may stay latent) → **Error** (incorrect resulting state) → **Failure** (external manifestation). Avoidance/tolerance act on faults; FRACAS/DCACAS act after failures.

---

## Tells & Smells

- **A number with no named availability variant** → not comparable; state A_op vs A_es vs A_i.
- **Availability target chosen before criticality** → arbitrary; classify the service thread first.
- **RMA figure quoted out of context** → seriously biased; name design, environment, support, training, materiel, diagnostics.
- **Estimate built on too-small or bad data** → the whole estimation process is questionable.
- **Normal distribution for a time variable** → can yield negative times; use Exponential.
- **FMEA used as if it ranked criticality** → it doesn't; you need FMECA.
- **Single-direction failure analysis** → pair bottom-up FMEA with top-down FTA.
- **Top-down "r of n" allocation on remote/distributed systems** → unrealistic; use SME judgment + lifecycle cost.
- **Top-down allocation on infrastructure (power/HVAC)** → violates independent-failure assumption; use standard configurations.
- **Treating software like hardware (swap in a better part)** → software has no wear-out; new code temporarily raises failures.
- **Asserting an MTTR without designing the diagnostics** → the restore time is unreachable without fault detection/isolation.
- **"Reliable" treated as "safe"** → safety is a separate, life-driven assessment.
- **Pasting every Appendix-D example requirement verbatim** → they need tailoring; many won't apply.
- **Filing RMA as a one-shot report** → it's a closed loop (NAPRS → DCACAS → corrective action) across the whole lifecycle.
