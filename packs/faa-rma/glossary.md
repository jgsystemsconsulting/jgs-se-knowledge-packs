# FAA-HDBK-006D (RMA) Glossary

Key terms from FAA-HDBK-006D (2020), Appendix A and the body, alphabetical, with chapter references. Definitions are synthesized in original wording, not reproduced. Cite the **006D** revision, not 006B.

**Accelerated Life Testing (ALT)** — a test that applies loads beyond normal service to provoke faults quickly and predict service life and maintenance intervals; not applicable to software. (Ch 5)

**Availability** — the probability a system is operational when called upon; uptime / (uptime + downtime). A *family* of figures, not one number — always state which downtime is counted. (Ch 2, Ch 6)

**Availability, Equipment & Services (A_es)** — (max service hours − total unscheduled hours) / max service hours; excludes scheduled downtime. (Ch 2, Ch 8)

**Availability, Inherent (A_i)** — design-intrinsic availability = MTBF / (MTBF + MTTR); counts corrective-maintenance downtime only, excluding logistics, administrative, and scheduled-maintenance time. (Ch 2, Ch 6)

**Availability, Operational (A_op / A_o)** — field-use availability counting all downtime, scheduled and unscheduled, in the real operating and support environment. (Ch 2, Ch 6)

**Bathtub Curve** — failure rate vs. time across three life phases: decreasing (infant mortality), constant (random/useful life), increasing (wear-out). Conceptual; not applicable to software. (Ch 2, Ch 5)

**Bayesian Network Analysis** — a probabilistic graphical model of conditional dependence supporting forward (prediction) and backward (diagnosis) cause-and-effect reasoning. (Ch 5)

**Confidence Interval** — a plausible range for an unknown parameter at a stated confidence level; preferred over a bare point estimate. (Ch 2)

**Criticality (Service Thread Loss Severity Category, STLSC)** — severity class assigned by the impact of losing a service thread: Safety-Critical, Efficiency-Critical, Essential, or Routine. (Ch 3, Ch 8)

**DCACAS (Data Collection, Analysis, and Corrective Action System)** — the FAA's closed-loop post-implementation instantiation of FRACAS, fed by repositories such as NASPAS/NAPRS. (Ch 3, Ch 5)

**Dependability** — the umbrella term combining a system's reliability, maintainability, and availability. (Ch 1, Ch 6)

**Error** — a wrong internal state (of hardware, software, or data) that a fault gives rise to. (Ch 1, Ch 6)

**Failure** — the external manifestation of an error; the inability to perform a required function within specified limits. (Ch 1, Ch 6)

**Failure Mode and Effects Analysis (FMEA)** — inductive, bottom-up cataloguing of each failure mode and its effect; a core RMA task; pair with a top-down method. (Ch 5, Ch 6)

**Failure Mode, Effects, and Criticality Analysis (FMECA)** — FMEA plus a criticality value ranking modes by importance; build the FMEA first, then add criticality. (Ch 5, Ch 6)

**Fault** — a deviation of system behavior from its requirements; for hardware, a latent fault that is never activated causes no failure. (Ch 1, Ch 6)

**Fault Tree Analysis (FTA)** — top-down, deductive tracing from a defined top-level failure event to contributing causes, with path probabilities; pair with a bottom-up method. (Ch 5, Ch 6)

**Figure of Merit** — the handbook's umbrella name for an RMA quantitative metric defined against an explicitly scoped "system of interest." (Ch 2)

**FRACAS (Failure Reporting, Analysis, and Corrective Action System)** — a closed loop: report → analyze for root cause → implement and verify corrective action. (Ch 5)

**IFPP (Information for Proposal Preparation)** — the RMA activities the Government expects the developer to perform, conveyed in the procurement package. (Ch 4, Ch 6)

**Interruption** — any break in continuity or unavailability, of any duration or cause (vs. an outage's one-minute threshold). (Ch 6)

**Ishikawa (Fishbone) Diagram** — a cause-and-effect diagram organizing potential and root causes of a failure; clutters on complex systems. (Ch 5, Ch 6)

**Maintainability** — the ability to retain a system in, or restore it to, a specified condition; splits into corrective (unscheduled) and preventive (scheduled). (Ch 2, Ch 8)

**MDT (Mean Down Time)** — average non-operational time for repair or preventive maintenance, including logistics and administrative delays. (Ch 6)

**MLDT (Mean Logistics Delay Time)** — the wait component of downtime: parts, tools, test-equipment setup, dispatch, supply and transport delays. (Ch 6)

**Monte Carlo Simulation** — an analytical tool modeling outcome distributions via repeated random sampling; best where interrelationships are too numerous to evaluate by hand. (Ch 5, Ch 6)

**MTBF (Mean Time Between Failure)** — average lifetime across items; applied to systems and subsystems. (Ch 2, Ch 6)

**MTBO (Mean Time Between Outages)** — total operating hours / number of outages; the services/facilities analog the FAA uses in place of MTBF. (Ch 2, Ch 6)

**MTTR (Mean Time To Restore)** — total outage time / number of outages; the maintainability measure, spanning detection, isolation, access, repair/replacement, and return to service. (Ch 2, Ch 8)

**NAS-RD (NAS Requirements Document, NAS-RD-2013)** — the requirements baseline fixing per-severity availability/reliability and restore-time targets. (Ch 3, Ch 8)

**NAPRS / NASPAS** — FAA reporting repositories feeding post-implementation RMA monitoring and corrective action. (Ch 3, Ch 4)

**Orthogonal Defect Classification (ODC)** — a defect-sorting scheme pointing at which part of development (design, code, or test) needs investigation. (Ch 6, Ch 7)

**Outage** — loss of a facility/service for one minute or more; the threshold that makes it countable in RMA computations. (Ch 6)

**Parts Screening** — running components through the bathtub curve's infant-mortality phase and assembling only the survivors. (Ch 5, Ch 6)

**Quality Function Deployment (QFD)** — the House of Quality; a matrix translating the voice of the customer into weighted, quantifiable requirements. (Ch 5, Ch 6)

**Recovery Time** — total time to detect, isolate, and recover; successful automatic recoveries within the prescribed time do not count as downtime, but their frequency is capped. (Ch 6)

**Redundancy** — backup functional capability that engages automatically on failure detection. (Ch 6, Ch 8)

**Reliability** — probability of zero failures (satisfactory operation) over a stated interval/mission under stated conditions; decomposes into material, mission, and logistics reliability. (Ch 1, Ch 2)

**Reliability Block Diagram (RBD)** — a deductive, top-down symbolic-logic model of series/parallel reliability relationships; the central allocation/verification artifact. (Ch 3, Ch 5)

**Reliability-Centered Maintenance (RCM)** — a structured framework (functional analysis → failure analysis → decision) for choosing the optimum maintenance mix, grounded in SAE JA1011 §1.1. (Ch 3)

**Reliability Growth** — driving reliability upward over time via design/development changes; tracked with the Duane and Crow models. (Ch 3, Ch 5)

**Resiliency** — the layer above RMA: anticipate, withstand, and recover from high-impact events via redundancy, diversity, response time, and recovery. (Ch 1)

**Safety Risk** — the life-preservation worldview that shares methods with RMA but optimizes against catastrophic failure modes, not cost of failure. (Ch 1, Ch 4)

**Series / Parallel** — series fails when any one element fails (reliabilities multiply); parallel fails only when all elements fail (redundancy raises availability). (Ch 3, Ch 6)

**Service Thread** — a string of systems and functions delivering a specific NAS Enterprise Architecture data path (e.g., radar surveillance) to controllers or pilots. (Ch 3, Ch 6)

**SLOC (Software Lines of Code)** — the size estimate that software defect-density prediction requires. (Ch 7)

**Software Reliability** — the probability that software does not cause system failure under specified conditions for a stated time; no wear-out phase. (Ch 7)

**SOW (Statement of Work)** — the developer's RMA-related tasks, including risk monitoring, fault-avoidance, and the reliability growth program. (Ch 4, Ch 6)

**SSD (System Specification Document)** — carries the quantitative RMA characteristics (fault detection/recovery, monitor-and-control, manual recovery, diagnostics), derived from the PRD. (Ch 4)

**System Specification / SEMP (Systems Engineering Management Plan)** — contractual artifacts carrying RMA tasks and oversight provisions. (Ch 6)

**Vee Model (Systems Engineering Vee)** — the iterative lifecycle model: left side determines/allocates requirements, right side verifies and validates them. (Ch 3, Ch 5)
