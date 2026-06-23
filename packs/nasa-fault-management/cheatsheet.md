# NASA Fault Management Handbook Cheatsheet

From NASA-HDBK-1002 *Fault Management Handbook* **Draft 2 (April 2, 2012)**. **Draft source** — verify against the current released handbook before formal use.

## Quick Decision Rules

**"Is this a fault or a failure?"**
- Unacceptable performance of an intended function → **failure** (an *effect*).
- The internal cause that explains it → **fault**. Name and isolate upward from the failure to the fault. Reserve "fault" for internal causes; say "failure causes" when you mean all causes.

**"Failure, anomaly, or neither?"**
- Unacceptable function → **failure**. · Unexpected (not necessarily unacceptable) function → **anomaly**. · An anomaly can be a non-failure; a planned expendable depletion is a non-anomalous failure.

**"Can the ground handle this fault, or must it be onboard/automatic?"**
- Sum the response latency (observation + detection + decision + execution + recovery) for each candidate implementer; compare to the failure's **TTC**.
- Latency **< TTC** → viable. Ground loop too slow / TTC too short (powered ascent, EDL, docking) → **automatic onboard FDIR**. Far from Earth, sparse contact → **autonomy**.

**"What's the default response if nothing predetermined fits?"**
- **Safe mode** — preserve assets, still accept ground commands and transmit data, buy humans time. If non-recoverable *and* TTC too short even for safe-mode evaluation → **abort**.

**"Verification or validation?"**
- Bottom-up, does each element meet its requirement? → **verification** ("built it right").
- Top-down, do the system's reactions preserve assets and mission? → **validation** ("built the right thing"). You need both.

**"Which strategy for this failure mode?"** (the five FM strategies)
- Prevent it by quality/margin → **Design-Time Fault Avoidance** · Predict & forestall it → **Operational Failure Avoidance** · Block its effect → **Failure Masking** · Restore the function → **Failure Recovery** · Accept it and degrade goals → **Goal Change**.

**"Probability or possibility?"**
- Don't pick faults to protect by computed probability — low-probability items disproportionately fail in flight and estimates are routinely underestimated. Protect **all electrical and protectable mechanical faults** and **core health-and-safety functions** regardless of probability.

---

## The Six FM Process Activities (run inside the SE lifecycle)

| Activity | Phase(s) | Key work product(s) |
|---|---|---|
| Conceptual Design Development | Pre-A / early A | FM Concept Document, Technology Plan/Assessment |
| Requirements Development | A → before CDR | FM Requirements Document |
| Architecture & Design | B (prelim) → C (detail), final before CDR | FM Architecture Document, FM Design Specification |
| Assessment & Analysis | A–C, continually | Analysis products (FMEA/FMECA, PRA, FTA, ESD/ETA, hazard, FCR, FEPP, detection/isolation, prognostics) |
| Verification & Validation | early B → D | FM V&V Plan, Incompressible Test List, Verification & Validation Matrices |
| Operations & Maintenance | B–E | FM Operations Plan, contingency procedures |

**Four fundamental FM questions** drive Assessment & Analysis: *What can go wrong? How often? What happens? What can be done?*

---

## Response Latency Decomposed (vs. TTC)

1. **Observation** — fault occurs → effects observable.
2. **Detection** — observable effect → mechanism detects it.
3. **Decision** — diagnose, decide, begin executing.
4. **Response execution** — duration of the recovery activity.
5. **Recovery** — completion → effects gone, status restored.

Sum 1–5 per implementer (ground operators, ground software, crew, flight software, firmware, hardware). **Viable iff sum < TTC.** Count human latency. The ground path is usually the longest.

---

## The Four Redundancy Approaches → Fault Class

| Redundancy | Counters | Powerless against |
|---|---|---|
| **Hardware-identical** | Random part failure, lifetime limits | Common-cause / common-mode flaws |
| **Functional** (dissimilar / analytic) | Common-mode; also detection cross-checks, workarounds | — |
| **Informational** (EDAC) | Bit corruption (single-event upsets) | Gross loss of data path |
| **Temporal** (repeat-in-time, checkpoint-rollback) | Transient faults | Permanent faults |

**Rule:** always state tolerance *of a named fault class*. "Single fault tolerant" with no named fault class is incomplete and dangerous.

---

## Mission Class → Fault-Tolerance Posture (Table 12)

| Class | Posture |
|---|---|
| **A** (flagship) | Single-fault tolerant; full redundancy; extensive FDIR |
| **B / C** | Intermediate; selective/partial redundancy |
| **D** | Medium-to-high risk; minimal tolerance; single-string |

Set by NPR 8705.4 mission classification. Risk posture is the master sizing dial for FM complexity, cost, schedule, and which work products apply.

---

## The Seven Dedicated FM Reviews (precede the project gate)

| FM Review | Precedes | Gates / demonstrates |
|---|---|---|
| **FMCR** (Concept) | MCR/MDR | FM scope/boundary matches resources & risk posture; safing strategy; TRL-6-by-PDR plan |
| **FMARR** (Architecture/Requirements) | SRR/MDR, PDR | Architecture & requirements mutually consistent; coverage sufficient |
| **FMPDR** (Preliminary Design) | PDR | Preliminary design meets requirements at acceptable risk; agreed fault set; new tech at TRL 6 |
| **FMCDR** (Critical Design) | CDR | Design maturity consistent across subsystems; ready to implement |
| **FMTRR** (Test Readiness) | SIR/TRR | System-level test plan & procedures ready |
| **FMLRR** (Launch Readiness) | Launch | FM maturity sufficient to launch; testing/analysis/contingency complete |
| **FMCERR** (Critical Event Readiness) | a critical event | FM readiness for that event (timeline, predicted responses, reconfig plans) |

Each review = entrance criteria (what must be complete) + success criteria (pass/fail) + Table 28 questions. Three-tier structure: FM in major program reviews, FM in system/subsystem reviews, **and** these dedicated FM reviews.

---

## FM Organization — Three Success Principles

1. **Authority sized to area of concern** — own every element FM functions could be allocated to.
2. **Vertical interfaces** — FM teams at each level, seating delegates from above and below, so issues have somewhere to be resolved.
3. **Horizontal integration** — documented interfaces *and* a coordinating board/panel with cognizance over **all** of FM, across engineering, S&MA, V&V, I&T, operations.

Plus: a single chartered **FM lead** (programmatic + technical duties); FM as a tracked engineering element (own WBS, budget, history); **plan for the staffing bump** (0.5 FTE planned vs. 14+ FTE actual at I&T).

---

## Tells & Smells

- **"Do FM" / "protect against faults"** as a top-level requirement → too-general; implementer can declare a substandard design done.
- **Top-level requirement naming a specific monitor and response** → too-specific; breaks when design shifts.
- **FM picked by probability** → low-probability faults fail in flight; protect by possibility.
- **"Single fault tolerant" with no named fault class** → incomplete; invites false confidence.
- **A response exists but finishes after the function is lost** → latency not budgeted against TTC.
- **FM reviewed only as a sidebar in nominal reviews** → gaps guaranteed; hold dedicated FM reviews.
- **Heritage FM reused without an inheritance review** ("analysis by similarity") → imports mismatched complexity and undiscovered bugs.
- **Operators/crew treated as outside the system** → they perform FM functions; their latency and judgment belong inside the boundary and the analysis.
- **Tolerated anomalies drifting into "expected"** → normalization of deviance (Challenger, Columbia).
- **No watchdog timer / keep-out zones not in software / FM enabled on unused components** → named recurring Lessons Learned failure modes.
- **Flat FM staffing plan** → the bump is a pattern, not a surprise; budget the curve.
- **No top-down SE owner asking "what could go wrong"** → the single most-cited historical root cause.

---

## Key Artifacts the Reviews Gate

FM Concept Document · FM Development & Analysis Plan · FM Technology Plan/Assessment · FM Requirements Document · FM Architecture Document · FM Design Specification · Analysis products (FMEA/FMECA, PRA, FTA, FEPP) · FM V&V Plan · FM Verification Matrix · FM Validation Matrix · Incompressible Test List · FM Test Procedures · FM Operations Plan · contingency procedures · program-accepted fault-tolerance / single-point-failure-exemption list.
