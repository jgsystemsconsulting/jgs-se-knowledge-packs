# Chapter 4: Software System Safety & the Software Safety Criticality Matrix

## Core Idea
Software safety in MIL-STD-882E is addressed separately from hardware because probability of software failure cannot be reliably estimated from historical data — software is application-specific and does not exhibit wear-out failure modes. Instead, the standard uses a two-dimensional criticality framework: the degree of software control over safety-significant hardware (Software Control Category, SCC) crossed with the severity of the potential mishap, producing a Software Criticality Index (SwCI). The SwCI drives required Level of Rigor (LOR) analysis and testing tasks, not a direct risk level.

## Frameworks Introduced

- **Software Control Categories (SCC) Table IV**: five levels (1–5) describing the degree of software autonomy and control authority over safety-significant hardware functions.
  - When to use: assigned to every software function that has any interaction with safety-significant hardware; re-evaluated if legacy software is incorporated into a SoS environment.

- **Software Safety Criticality Matrix (SSCM) Table V**: 5x4 grid of SCC (rows 1–5) crossed with severity category (columns I–IV) producing SwCI 1 through 5.
  - When to use: mandatory per 4.4.1 unless a tailored alternative is formally approved; applied at the functional level, not the code level.

- **SwCI-to-LOR Task Mapping Table VI**: maps each SwCI to a required set of Level of Rigor tasks and specifies the default risk level if those tasks are incomplete.
  - When to use: drives the software development plan (SDP) and software test plan (STP); if LOR tasks are unspecified or incomplete, the risk is escalated to the PM for formal acceptance.

## Key Concepts

- **Software Control Category 1 — Autonomous (AT)**: software exercises autonomous control authority over safety-significant hardware without possibility of predetermined safe detection and intervention to preclude a mishap. Includes complex multi-subsystem, parallel-processor, time-critical SCF implementations.
- **Software Control Category 2 — Semi-Autonomous (SAT)**: software exercises control authority but allows time for independent safety mechanisms to mitigate; fault detection and annunciation notifies the control entity. Also includes time-critical safety-significant displays where operator response time is sufficient.
- **Software Control Category 3 — Redundant Fault Tolerant (RFT)**: software issues commands over safety-significant hardware with redundant, independent fault-tolerant mechanisms for each hazardous condition; adequate fault detection, annunciation, tolerance, and recovery prevent hazard occurrence even if software fails.
- **Software Control Category 4 — Influential**: software generates safety-critical or safety-related information used for decisions by an operator, but does not require operator action to avoid a mishap. No autonomous control authority.
- **Software Control Category 5 — No Safety Impact (NSI)**: software has no command or control authority over safety-significant hardware, does not provide safety-significant information, and does not transport or resolve safety-significant or time-sensitive communication.
- **SwCI 1**: highest criticality; requires analysis of requirements, architecture, design, and code, plus in-depth safety-specific testing. If LOR tasks incomplete: default risk = HIGH.
- **SwCI 2**: requires analysis of requirements, architecture, and design plus in-depth safety-specific testing. If incomplete: default risk = SERIOUS.
- **SwCI 3**: requires analysis of requirements and architecture plus in-depth safety-specific testing. If incomplete: default risk = MEDIUM.
- **SwCI 4**: requires safety-specific testing only. If incomplete: default risk = LOW.
- **SwCI 5**: once assessed as Not Safety by safety engineering, no safety-specific analysis or verification is required.
- **Level of Rigor (LOR)**: specification of the depth and breadth of software analysis and verification activities needed to provide sufficient confidence that a safety-critical or safety-related software function will perform as required.
- **Safety-Significant Software Function (SSSF)**: a software function that can cause, contribute to, or influence a safety-significant hazard.
- **Safety-Critical Function (SCF)**: a function whose failure to operate or incorrect operation will directly result in a mishap of Catastrophic or Critical severity.

## The Software Safety Criticality Matrix

```
               Severity
SCC            Cat I         Cat II        Cat III       Cat IV
               (Catastrophic)(Critical)    (Marginal)    (Negligible)
1 (AT)         SwCI 1        SwCI 1        SwCI 3        SwCI 4
2 (SAT)        SwCI 1        SwCI 2        SwCI 3        SwCI 4
3 (RFT)        SwCI 2        SwCI 3        SwCI 4        SwCI 4
4 (Influential)SwCI 3        SwCI 4        SwCI 4        SwCI 4
5 (NSI)        SwCI 5        SwCI 5        SwCI 5        SwCI 5
```

Note: The SSCM is NOT an assessment of risk. It determines required rigor; actual risk assessment of software contributions uses Table B-I criteria in Appendix B.

## Mental Models

- **"SSCM is a rigor driver, not a risk assessor"** — SwCI 1 does not mean the software is High risk; it means high rigor is required to assess and reduce the software's contribution to system risk. Risk is the output of the LOR task completion process, not of the SSCM itself.
- **"Incompleteness defaults upward"** — if any SwCI-specified LOR task is unspecified or incomplete, the risk from that software automatically escalates to the corresponding default level (SwCI 1 → HIGH), and the PM must formally accept or fund the tasks. There is no "it's probably fine" option.
- **"SoS demands SCC re-evaluation"** — legacy software SCCs must be re-evaluated at functional and physical interfaces when that software is incorporated into a SoS; an SCC 4 component in an isolated system may behave as SCC 1 or 2 when integrated with other autonomous systems.

## Anti-patterns

- **Confusing SwCI with RAC**: SwCI is a criticality index (rigor driver); RAC is a risk assessment code (severity × probability). Appendix B Table B-I provides the separate criteria for mapping software causal factors to risk levels.
- **Assigning NSI (SwCI 5) to avoid work**: once assessed as NSI, no safety analysis is required — but the assessment itself must be documented as a safety engineering judgment, not assumed by default.
- **Applying SSCM at the code-file level instead of function level**: the SCC and SwCI apply to software functions and associated requirements, not to files or modules. Functions map to implementing modules for traceability; the analysis is function-first.

## Key Takeaways

1. Software safety uses a criticality framework (SCC × severity → SwCI) rather than the hardware risk framework (severity × probability → RAC), because software failure probability is not reliably estimable.
2. The SSCM is mandatory; tailored alternatives require formal DoD Component approval and must meet or exceed standard LOR task requirements.
3. If LOR tasks are incomplete, the PM receives a formal document stating the contribution to system risk at the default level; this is a mandatory escalation path, not a discretionary one.
4. SCC 1 (Autonomous) software with Catastrophic severity (Cat I) generates SwCI 1, the highest rigor level, requiring requirements, architecture, design, and code analysis plus in-depth testing.
5. Appendix B provides the full software system safety integrity process: FHA → SCC assignment → SwCI → LOR tasks → risk assessment.
6. The Functional Hazard Analysis (Task 208) is the primary mechanism for identifying SSSFs and assigning SCCs; it feeds directly into the software development plan.

## Connects To

- **Chapter 3 (Risk Assessment)**: Table VI links SwCI levels to the same High/Serious/Medium/Low risk levels used in the hardware risk matrix.
- **Chapter 6 (Task 208 — Functional Hazard Analysis)**: the FHA is the upstream task that identifies SSSFs and maps them to SCC assignments.
- **Chapter 5 (Task 102 — SSPP)**: the SSPP must document the systematic software system safety approach, SwCI assignments, and LOR task plans.
- **AOP 52 / Joint Software Systems Safety Engineering Handbook**: referenced normative documents for detailed LOR task guidance, complementary to MIL-STD-882E Appendix B.
- **DO-178C (Software Considerations in Airborne Systems)**: comparable avionics standard using Design Assurance Levels (DALs); DAL A/B roughly correspond to SwCI 1/2 in intent.
