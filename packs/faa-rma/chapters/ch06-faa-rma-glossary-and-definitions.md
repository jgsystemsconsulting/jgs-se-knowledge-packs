# Chapter — Acronyms, Glossary, and Key RMA Definitions

> Source: FAA-HDBK-006D (2020), Appendix A "Acronyms & Glossary." Use 006D (2020), not 006B.

## Core Idea

Reliability, Maintainability, and Availability (RMA) work falls apart when the same word means different things to different parties — when one engineer's "availability" silently excludes the logistics delay that another engineer's number includes, the resulting trade studies and contractual thresholds are no longer comparable. Appendix A of the handbook exists to close that gap: it fixes a shared controlled vocabulary so that requirements, analyses, test results, and oversight decisions across the National Airspace System (NAS) all rest on the same definitions. The appendix is split in two — an acronym list (A.1) that decodes the dense alphabet-soup of FAA and defense-acquisition shorthand, and a glossary (A.2) that gives each RMA term a precise, citation-backed meaning. Many definitions carry bracketed reference numbers, signaling that the handbook is not inventing terms but harmonizing them across standards bodies (IEEE, SAE, ISO-aligned SE guides) and FAA orders.

The recurring lesson in this slice is that RMA quantities are only meaningful once you state *what time is counted*. Availability, the various mean-time metrics, and the bathtub-curve life phases are all defined by which intervals — logistics delay, administrative downtime, preventive maintenance, scheduled outages — are swept in or excluded. Getting the definition right is therefore a prerequisite to getting the math right.

## Frameworks Introduced (exact source names, when/how)

The glossary names a set of analytical methods and reference constructs and gives each a working definition. These are introduced as defined terms, not stepwise procedures:

- **Bathtub Curve** — a graphical depiction of how a system's failure rate changes across its life, showing three regimes: early "infant mortality" failures, a constant-rate random-failure middle, and end-of-life "wear out" failures. It is the organizing picture behind several other glossary entries (decreasing, constant, and increasing failure rate; infant mortality, random, and wear-out phases).
- **Failure Mode and Effects Analysis (FMEA)** — a method that walks each potential failure mode to determine its effect on the system and classify it by severity.
- **Failure Mode, Effects, and Criticality Analysis (FMECA)** — described as an extension of FMEA that additionally assesses the risk of each mode, ranks issues by importance, and drives corrective action toward the most serious concerns.
- **Fault Tree Analysis (FTA)** — a top-down, graphical enumeration of the different ways a particular failure can come about.
- **Reliability Block Diagram (RBD)** — a deductive, top-down symbolic-logic model that depicts the reliability (and/or availability) relationships among the system and its elements or events.
- **Ishikawa Diagram** — also called the fishbone diagram; a chart that identifies, classifies, and differentiates the potential and root causes of a failure affecting system operation.
- **Bayesian Network Analysis** — a probabilistic graphical model the handbook flags as well-suited to capturing causal relationships within a target system.
- **Monte Carlo Simulation** — an analytical tool for deriving RMA parameters by repeated random sampling to model the probability distribution of outcomes as random variables are introduced.
- **Quality Function Deployment (QFD)** — a matrix-based tool that captures the voice of the customer, translating stakeholder-requested features into weighted requirements, benchmarks, and scores.
- **Orthogonal Defect Classification (ODC)** — a scheme for sorting defects into classes that point to which part of the development process (design, code, or test) needs investigation.
- **FRACAS** (Failure Reporting, Analysis, and Corrective Action System) and the FAA's **DCACAS** (Data Collection, Analysis and Corrective Action System) — closed-loop processes for reporting, classifying, and analyzing failures and planning corrective action; DCACAS is the FAA's post-implementation data-capture instantiation tied to its data subsystems and repositories.
- **Systems Engineering Vee Model** — named as a graphical representation of the development lifecycle summarizing the main development steps, situating RMA within the broader SE process.

Several governing documents and artifacts are also defined as terms, showing where RMA content is contractually carried: the **Information for Proposal Preparation (IFPP)**, **Statement of Work (SOW)**, **System Specification Document**, and **Systems Engineering Management Plan (SEMP)** each are expected to carry specific RMA tasks, oversight provisions, or quantitative characteristics.

## Key Concepts

**Availability and its variants.** Availability is the probability that a system is operational at a randomly chosen instant — equivalently, the fraction of total available operating time it is up. The general expression is uptime divided by the sum of uptime plus downtime, where downtime is defined broadly to include logistics, ready, administrative, and both preventive and corrective maintenance time. The glossary then carefully distinguishes narrower forms:

- **Inherent Availability (Ai)** isolates the equipment's intrinsic design quality. It is computed in an idealized support environment, counting only corrective maintenance downtime while excluding logistics, administrative, and preventive-maintenance downtime; it is derived from engineering analysis of quantities the designer controls.
- **Operational Availability (Ao)** is the field-use figure — the percentage of time a system or group is operationally capable, again uptime over uptime-plus-downtime, but now reflecting the real operating and support environment.
- **Equipment & Services Availability** is given an FAA-specific operational definition: maximum facility/service hours minus total unscheduled hours, divided by maximum facility/service hours, expressed as a percentage.
- **Target Operational Availability** is simply the desired Ao associated with a given NAS service — the requirement to be met.

The takeaway encoded across these entries is that "availability" is never a single number; you must state which downtime contributors are in scope.

**The mean-time family.** The handbook fixes a cluster of mean-time metrics that are easy to conflate:

- **MTBF** (Mean Time Between Failure) — the average lifetime across all items considered; applied to systems and subsystems.
- **MTBO** (Mean Time Between Outages) — the services/facilities analog, total operating hours divided by number of outages, used in place of MTBF for services and facilities.
- **MTTR** (Mean Time to Restore) — a maintainability measure: total outage time divided by the number of outages over an interval, i.e., mean duration per outage.
- **MTBM** (Mean Time Between Maintenance) — average time between all maintenance actions, corrective and preventive.
- **MDT** (Mean Down Time) — average non-operational time due to repair or preventive maintenance, including logistics and administrative delays.
- **MLDT** (Mean Logistics Delay Time) — the wait component: locating parts and tools, setting up test equipment, dispatching personnel, supply and transportation delays; heavily dependent on the logistics support structure.
- **MMT** (Mean Maintenance Time) — total preventive plus corrective maintenance time divided by the total scheduled and unscheduled events.

The handbook further splits scheduled versus unscheduled variants (e.g., scheduled and unscheduled MTTR, unscheduled MTBO), reinforcing that whether planned maintenance counts changes the number.

**Faults, errors, and failures as a causal chain.** The glossary insists on three distinct terms. A **fault** is a deviation of system behavior from its requirements — for hardware, a physical change that may stay latent and never produce a failure if never activated. An **error** is an incorrect state of hardware, software, or data that results from a fault. A **failure** is the external manifestation of that error — the inoperable state in which an item does not perform as specified. This fault → error → failure ordering is what FMEA, FTA, and root-cause analysis exploit.

**Reliability as a structured probability.** Reliability is the probability that a system performs its required function without failure for a specified time in a specified environment. The handbook notes it can be decomposed into material (hardware/software/firmware), mission (intentions/goals), and logistics (implementation/support) reliability — a reminder that "reliable" is multi-dimensional. **Software Reliability** gets its own definition (probability that software does not cause system failure under specified conditions), alongside **Software Reliability Engineering** and **Software Reliability Prediction**.

**Maintenance taxonomy.** **Preventive (scheduled / periodic) maintenance** is regular servicing to keep systems running; **unscheduled (corrective) maintenance** is performed to identify or correct a problem — repair, adjustment, calibration, troubleshooting. **Scheduled downtime** is the time consumed by preventive tasks, software upgrades, and adaptation-data changes that render a system non-operational.

**Outage and interruption.** An **outage** is the loss of a facility/service for one minute or more; an **interruption** is any break in continuity or unavailability regardless of duration or cause. The one-minute threshold is what makes an outage countable in RMA computations.

**Redundancy and recovery accounting.** **Redundancy** provides backup functional capability that automatically engages on failure detection. **Recovery Time** is the total time to detect, isolate, and recover; the handbook makes a crucial accounting rule explicit — successful automatic recoveries within the prescribed recovery time are *not* counted as downtime, but requirements still cap the allowable frequency of those automatic recovery actions.

**Series and parallel structure.** **Systems in Series** fail when any one connected element fails; **Systems in Parallel** fail only when all connected elements fail. These two definitions underpin RBD math and redundancy design.

**Service threads and severity.** A **Service Thread** is a string of systems and functions supporting a NAS Enterprise Architecture function — a specific data path (e.g., radar surveillance) to controllers or pilots. **Service Thread Loss Severity Category (STLSC)** assigns a severity class based on the impact that losing that thread would have on safe and efficient aircraft operation, linking RMA directly to safety consequence.

**Dependability as the umbrella.** **Dependability** is named as the combined term for a system's reliability, maintainability, and availability characteristics together — the single word that contains all three RMA pillars.

## Mental Models

**The bathtub as a clock.** Read the bathtub curve left to right as the life of the system. The descending left wall is **infant mortality** (decreasing failure rate, caused by defects built into the system); **parts screening** deliberately runs components through this phase so only survivors are assembled. The flat floor is the **constant / random failure rate** of normal operation. The rising right wall is **wear out** (increasing failure rate from age degradation). Almost a dozen glossary entries are just named positions on this one curve — internalizing the curve gives you most of the failure-rate vocabulary for free.

**State what time you count.** For every availability or mean-time figure, ask which intervals are in or out: logistics delay, administrative downtime, preventive maintenance, scheduled outages. Inherent availability excludes most of them (ideal support, corrective-only); operational availability includes the real-world ones. The number is meaningless until the scope is named.

**Fault is potential, failure is realized.** A fault can lie dormant forever. The chain fault → error → failure is the lens for analysis: avoidance and tolerance act on faults before they activate; reporting and corrective-action systems (FRACAS/DCACAS) act after failures manifest.

**Top-down meets bottom-up.** The glossary explicitly pairs a **Top-Down Approach** (treat the system holistically, then decompose to understand its sub-systems, reverse-engineering style) with a **Bottom-up Approach** (start from elements and subsystems and assemble understanding of the whole). FTA and RBD are top-down; FMEA reasons from the part upward.

## Key Takeaways

- The appendix is a controlled vocabulary, not background reading: requirements, analyses, and oversight decisions across the NAS must use these exact definitions to stay comparable.
- "Availability" is a family, not a number. Inherent (Ai), operational (Ao), equipment & services, and target availability differ precisely in which downtime they count — always name the variant.
- The mean-time metrics (MTBF, MTBO, MTTR, MTBM, MDT, MLDT, MMT) each scope a different slice of operating and maintenance time; MTBO/MTTR are the service/facility-side analogs the FAA uses where MTBF would apply to systems.
- Keep fault, error, and failure distinct — they form the causal chain that every RMA analysis method works along.
- Recovery accounting is a defined rule: automatic recoveries within the prescribed recovery time do not count as downtime, but their frequency is still bounded by requirement.
- Most failure-rate terms are just labeled regions of the bathtub curve; learn the curve and the rest follow.
- Bracketed citations on glossary entries signal harmonization with external standards — the handbook is aligning terminology, not coining it.

## Connects To

- **Availability and reliability modeling chapters** of this pack: the series/parallel definitions, RBD, and the availability variants here are the vocabulary those quantitative methods compute against.
- **Failure analysis methods** (FMEA, FMECA, FTA, Ishikawa, root-cause analysis): defined here, applied where the handbook details RMA analysis techniques.
- **Acquisition and contractual artifacts** — IFPP, SOW, System Specification Document, SEMP: these carry the RMA requirements and oversight tasks that the rest of the lifecycle executes against, tying RMA into FAA's Acquisition Management System (AMS) and Investment Analysis (IA).
- **Safety**: STLSC and the safety/safety-risk definitions connect RMA quantities to operational safety consequence, linking to FAA Safety Risk Management guidance and the broader SE Vee lifecycle.
- **Broader SE canon** (SEBoK, IEEE/SAE standards referenced in brackets): the appendix's harmonized definitions are the bridge between FAA-specific RMA practice and the wider systems-engineering body of knowledge.
