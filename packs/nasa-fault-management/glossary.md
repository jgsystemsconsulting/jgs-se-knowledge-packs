# NASA Fault Management Handbook Glossary

Key terms from NASA-HDBK-1002 *Fault Management Handbook* **Draft 2 (April 2, 2012)**, alphabetical, with chapter references. **Draft source** — terminology may differ from any later released edition.

**Ambiguity group** — the set of candidate components that the available detections cannot tell apart; diagnosis quality is measured by how small these groups are. (Ch 7)

**Anomaly** — the *unexpected* (but not necessarily unacceptable) performance of an intended function; distinct from a failure, and useful because anomalies can foreshadow or trigger faults. (Ch 1, Ch 7)

**Abort** — a contingency FM class used when a fault is non-recoverable and its TTC is too short even for safe mode; applies to powered ascent, collision-risk rendezvous, and powered descent. (Ch 4)

**Assessment and analysis (FM activity)** — the FM process activity that answers the four fundamental questions using FMEA/FMECA, PRA, FTA, ESD/ETA, hazard, FCR, FEPP, detection/isolation, and prognostics analyses; in the source, partly a draft placeholder. (Ch 2, Ch 5)

**Automation** — *who* implements an FM function: machines vs. humans (fully, partly, or not automated). Distinct from autonomy. (Ch 4, Ch 7)

**Autonomy** — the *locus of control*: how decision authority is distributed between two locations (classically flight vs. ground) relative to a reference point. (Ch 4, Ch 7)

**Backup Flight Control System (BFCS)** — an independently developed control system for crewed vehicles, justified only when its protection against common-mode failure exceeds what the same resources would buy by hardening the primary. (Ch 4)

**Behavior** — the time evolution of a system's states. (Ch 1, Ch 7)

**Contingency procedures** — line-by-line operator procedures for off-nominal events; owned by operations with heavy FM input. (Ch 2, Ch 6)

**Critical event** — a planned mission-critical activity (launch, orbit insertion, flyby, docking, landing) or a failure condition needing a timely response; usually demands a fail-operational rather than fail-safe FM posture. (Ch 2, Ch 4)

**Critical Failure Effect (CFE)** — a failure effect that, once it occurs, irrevocably compromises one or more system or mission objectives. (Ch 1, Ch 4, Ch 7)

**Detection (failure)** — determining that something unexpected (a failure or anomaly) has occurred, typically via a threshold, a persistence/filtering check, and notification. (Ch 1, Ch 7)

**Diagnosis** — composed of **fault isolation** (locating the causal mechanism) and **fault identification/characterization** (determining possible causes). (Ch 1, Ch 7)

**Driving requirements** — the small subset of FM requirements (fault tolerance, fail-safe/fail-operational, time-to-criticality) that shape the whole architecture. (Ch 3, Ch 4)

**Error** — the difference between the ideal (desired) state/behavior and the *estimated* state/behavior. (Ch 1)

**Failure** — the unacceptable performance of an intended function; by definition an *effect*. (Ch 1, Ch 7)

**Failure containment** — preventing a failure from causing further failures (cf. fault containment, which stops a fault from causing further faults). (Ch 1, Ch 7)

**Failure Containment Region (FCR)** — a zone bounded by failure-containment boundaries; defining FCRs is a key part of FM architecture. (Ch 3, Ch 7)

**Failure Effect Propagation Path (FEPP)** — the path along which a failure's effects spread from the fault, often transforming physically along the way. (Ch 5, Ch 7)

**Failure recovery** — restoring functions to meet existing or redefined goals after a failure. (Ch 1, Ch 7)

**Failure response** — acting to retain or regain control of system state after a failure. (Ch 1, Ch 7)

**Failure tolerance (= fault tolerance)** — the ability to keep performing a function despite a specified number of coincident, independent failure causes of specified types; always tolerance *of a named fault class*. (Ch 1, Ch 7)

**Fail-operational** — no loss of functionality after the specified failures. (Ch 4, Ch 7)

**Fail-safe** — a critical subset of functions is preserved after the specified failures. (Ch 4, Ch 7)

**Fault** — a physical or logical cause that explains a failure; an internally-rooted cause. FM is named for faults but governs failures generally. (Ch 1, Ch 7)

**FM Architecture Document** — defines how all allocated FM responsibilities combine into a complete system; produced in Architecture & Design. (Ch 2, Ch 6)

**FM Concept Document** — sets the FM boundary/scope, design principles, and ConOps; carries the safing strategy and gets project buy-in. (Ch 2, Ch 6)

**FM Design Specification / Design Document** — the detailed FM design (phase C), authoritative over subsystem specs. (Ch 2, Ch 6)

**FM milestone reviews** — the recommended minimum set of seven dedicated FM reviews: FMCR, FMARR, FMPDR, FMCDR, FMTRR, FMLRR, FMCERR. (Ch 6)

**FM Requirements Document** — the centrally-owned, authoritative FM requirements, allocated down to systems and subsystems. (Ch 2, Ch 3)

**FM Requirements Checklist** — eleven quality dimensions (Clarity, Completeness, Compliance, Consistency, Traceability, Correctness, Functionality, Performance, Interfaces, Maintainability, Verifiability) adapted from the NASA SE Handbook. (Ch 3)

**FM V&V Plan** — sets the FM verification/validation approach, risk posture, test planning, and required test-bed fidelity. (Ch 2, Ch 5)

**Five FM strategies** — Design-Time Fault Avoidance and Operational Failure Avoidance (failure *prevention*); Failure Masking, Failure Recovery, and Goal Change (failure *tolerance*). (Ch 7)

**Four fundamental FM questions** — What can go wrong? How often? What happens if it does? What can be done to avoid or tolerate it? (Ch 2)

**Goal change** — shifting to new, usually degraded goals that remain achievable after a failure; safing is the typical case. (Ch 7)

**Incompressible Test List** — the agreed minimum set of FM tests that must pass before launch, exercised at the highest level of integration. (Ch 2, Ch 5)

**Knowledge error** — how far the estimated state sits from the ideal expected state. (Ch 1)

**Mission class (A–D)** — the risk-classification banding (per NPR 8705.4) that sets fault-tolerance ambition: Class A flagship/single-fault-tolerant with full redundancy; Class D minimal-tolerance/single-string. (Ch 3, Ch 4)

**Model adjustment** — updating the models on which expectations rest as the system's real behavior is learned; the FM function most prone to normalization of deviance. (Ch 1, Ch 7)

**Nominal / off-nominal** — *nominal* = an intended, acceptable state or behavior; *off-nominal* = beyond expected boundaries, split into anomalous, degraded, and failed. (Ch 1)

**Normalization of deviance** — repeatedly tolerating anomalies until they are treated as expected, masking danger signals; cited in Challenger and Columbia. (Ch 7, Ch 8)

**Observer** — a human or human-generated algorithm carrying engineering judgment that monitors the system; humans are *inside* the FM boundary. (Ch 1, Ch 7)

**Operational FM functions** — Detection, Diagnosis, Decision, Response, and Model Adjustment, active during the operational phase. (Ch 7)

**Possibility over probability** — the source's stance: protect all electrical and protectable mechanical faults and core health-and-safety functions regardless of computed probability, because low-probability items disproportionately fail in flight. (Ch 3)

**Prognosis / prognostics** — predicting a future failure or future states; deliberately omitted from the draft's operational-function diagram. (Ch 1, Ch 5, Ch 7)

**Redundancy (four approaches)** — hardware-identical, functional (dissimilar/analytic), informational, and temporal; each counters a different fault class. (Ch 7)

**Response latency** — the elapsed time from a fault occurring to the failure condition being corrected; decomposed into observation, detection, decision, execution, and recovery intervals. (Ch 4)

**Risk posture** — the project's accepted level of risk (set by mission class); the master sizing dial for FM complexity, formality, cost, and which work products apply. (Ch 2, Ch 4)

**Root cause** — the earliest fault or environmental trigger in the explanatory event chain behind a failure. (Ch 1, Ch 7)

**Safe mode / safing** — a deliberate goal change to a degraded, asset-preserving state; the universal default for any failure not covered by a predetermined response. Must still accept ground commands and transmit data. (Ch 2, Ch 4)

**Safety net** — a system-wide requirement structure that catches situations the failure-modes analyses miss, sourced from scenario analysis, operational modes, judgment, and lessons learned. (Ch 2, Ch 3, Ch 6)

**State** — the value(s) of a system's state variables at an instant; the **system state** is the set of all such states. (Ch 1, Ch 7)

**System boundary** — the bound of FM responsibility; must enclose all hardware, software, procedures, and personnel performing FM functions, plus documented boundary conditions. (Ch 7)

**Test as you fly / fly what you test** — the V&V best practice of testing the flight-representative configuration. (Ch 2, Ch 5, Ch 6)

**Time to Criticality (TTC)** — how long failure effects take to propagate from the failure mode to the CFE; FM is effective only if its loop finishes within the TTC. (Ch 1, Ch 4, Ch 7)

**TRL 6 by PDR** — the technology-maturity gate the source levies on any new FM technology, with a fallback if not met. (Ch 2, Ch 6)

**Verification (FM)** — bottom-up, design-specific proof that the system reacts to failures as its requirements specify ("built it right"). (Ch 5)

**Validation (FM)** — top-down, intent-specific, system-wide proof that the reactions preserve assets and mission function ("built the right thing"). (Ch 5)
