# Chapter 1 — Introduction, Scope, and FM Definitions

> **DRAFT SOURCE.** This chapter synthesizes NASA-HDBK-1002 **Draft 2 (April 2, 2012)**, an unapproved working draft. Terminology, scope, and review names below reflect that draft and may differ from any later released edition. Treat as guidance, not a controlling standard.

## Core Idea

Fault Management (FM) is the systems-engineering activity responsible for what a system does when things go wrong. The handbook frames it as the discipline that equips an operational system to **prevent, detect, isolate, diagnose, and respond to** off-nominal and failed conditions before they disrupt the intended mission. Its stated end goal is the preservation of system assets — explicitly including crew — and of the system's intended functionality in the presence of predicted or existing failures, achieved either by design or by active control.

Crucially, FM is not a localized, subsystem-level concern. The handbook insists it demands a **system-level perspective**: a design is not considered complete until potential failures have been addressed, and effective FM depends on the cooperative design and operation of separately deployed elements (in the space domain, the flight, ground, and operations deployments working together) to meet reliability, availability, and safety objectives. FM is also resource-constrained like any other system element, so practitioners must balance the risk reduction additional FM buys against the cost of designing, building, validating, deploying, and operating it.

## Frameworks Introduced

- **Fault Management (FM) as an SE discipline** — defined in the Scope (Section 1) as the part of systems engineering focused on detecting faults and accommodating off-nominal behavior. The handbook presents FM both *methodologically* (processes to analyze, specify, design, verify, and validate FM functions) and *technologically* (the hardware and control elements — often realized in software and procedures — plus situational-awareness capabilities such as caution/warning functions that notify operators and crew).
  - When/how used: applied across the whole mission lifecycle and embedded inside the broader SE technical processes, not run as a separate track.

- **FM as part of the SE process (Figure 2 reference; Section 4)** — the handbook positions FM as following an SE process aimed at the *off-nominal* design, complementing the conventional SE focus on nominal behavior. The document explicitly says it should be used as a companion to the NASA Systems Engineering Handbook (NASA/SP-2007-6105 Rev 1), while noting FM guidance is not yet at the same maturity level.
  - When/how used: nominal and off-nominal behaviors are to be considered, addressed, and designed *together* to yield a cohesive, robust system.

- **NPR 7123.1A systems-engineering technical processes (Figure 1)** — the handbook anchors FM activities inside the SE technical processes enumerated in NPR 7123.1A. FM is meant to produce derived requirements consistent with existing SE practice as it flows down the NASA organizational hierarchy.
  - When/how used: during system design and realization, FM work happens within this established process context rather than alongside it.

- **The ISO network-management analogy** — to justify the term "fault management" the handbook borrows from network management, where ISO (in ISO/IEC 23004-6:2008) characterizes FM as the functions for finding, localizing, and repairing malfunctions, with the aim of keeping a system dependable despite faults. The handbook flags that "fault management" is itself a mild misnomer, since the discipline concerns *failures in general*, not only faults (which are specifically failure causes rooted inside the system).
  - When/how used: invoked once, to ground NASA's terminology and goal statement in an existing international standard rather than to import the standard wholesale.

## Key Concepts

- **What FM functions cover.** The formal *Fault Management* definition stretches across the full verb-set — containing, preventing, detecting, isolating, diagnosing, responding to, and recovering from any condition able to disrupt nominal operations. The Scope's shorter list — prevent, detect, isolate, diagnose, respond — is the recurring shorthand.

- **Fault vs. failure (the central distinction).** A **failure** is the *unacceptable performance of an intended function*; a **fault** is a *physical or logical cause that explains a failure*. The discipline is named for faults but is really about failures broadly. Related: an **anomaly** is the *unexpected* performance of an intended function (unexpected, not necessarily unacceptable).

- **The off-nominal state space.** **Nominal** means an intended, acceptable state or behavior; **off-nominal** means a state or behavior beyond the boundaries of expected states. The handbook names exactly three off-nominal states: **anomalous, degraded, and failed**. This three-way split is what FM must detect and act within.

- **Error, expectation, and knowledge error.** **Error** is the difference between the desired (ideal) state/behavior and the *estimated* state/behavior; **expectation** is the most likely predicted state/behavior; **knowledge error** is the deviation between the estimated state and the ideal expected state. These tie FM to state estimation, not just hardware redundancy.

- **The failure-response vocabulary.** The definitions decompose the response side finely: **failure detection** (determining something unexpected occurred), **fault isolation** (locating a hypothesized cause to a defined granularity), **fault diagnosis** (determining possible locations and/or causes), **failure response** (acting to retain/regain control of system state), **failure recovery** (restoring functions to meet existing or redefined goals), **failure response determination** (selecting the mitigating actions), and proactive forms — **failure preclusion** (actively preventing a failure), **fault avoidance** (passive prevention), and **failure prognosis** / **prognosis** (predicting a future failure or future states).

- **Containment and tolerance.** **Failure containment** prevents a failure from causing further failures; **fault containment** prevents a fault from causing further faults. **Failure tolerance** (synonymous with **fault tolerance**) is the ability to keep performing a function despite a specified number of coincident, independent failure causes of specified types.

- **Criticality and causation.** A **critical failure effect** is one that, once it occurs, irrevocably compromises one or more system objectives. **Root cause** is the earliest fault or environmental trigger in the explanatory event chain behind a failure. **Time to criticality** measures how long the effects take to travel from the originating failure mode out to that critical effect — a key timing budget for whether a response can act in time.

- **State-based system view.** **State** is the value(s) of state variables at a point in time; **system state** is the set of all such states; **behavior** is the temporal evolution of a state; a **function** transforms an input state to an output state. **State determination** ascertains current states; **model adjustment** updates the model on which expectations are based; **goal change** alters the current objective. This vocabulary frames FM as control over a system's state under uncertainty.

- **The observer.** An **observer** is a human or human-generated algorithm (carrying human engineering judgment) that monitors operational or non-operational systems — making FM partly an automation problem and partly an operations/human-judgment problem.

## Mental Models

- **A design isn't done until failure is designed for.** The handbook's recurring stance: nominal-only design is incomplete. FM is the half of SE that handles off-nominal behavior, and the two halves must be designed together.

- **Faults are causes; failures are the loss of acceptable function.** Reason upward — observe a failure (unacceptable function), then isolate/diagnose toward the fault (the rooted cause). The naming ("fault" management) is historical convenience; the scope is the whole failure chain.

- **Three off-nominal states, not a binary.** Systems are not simply "working" or "broken." FM must distinguish anomalous, degraded, and failed, because each calls for different responses.

- **Time-to-criticality is a budget.** Because failure effects propagate, FM design is a race: detection, isolation, and response must complete before the propagation reaches a critical failure effect. This reframes FM from "have a response" to "have a response *fast enough*."

- **FM is a balance, not a maximization.** More FM is not automatically better — it costs design, validation, deployment, and operations resources, and adds complexity. Practitioners trade FM coverage against those costs and against the program's risk posture.

- **One discipline, many local names.** The same underlying activity appears across missions and organizations under different banners; the work is similar even when the label differs (see Anti-patterns).

## Anti-patterns

The handbook explicitly names two organizational/cultural traps:

- **FM as an unrecognized, loosely defined side duty.** Because FM is not always identified as a distinct system-level discipline, it is often handed to subsystem engineers as an extra, vaguely scoped responsibility. The handbook calls this a *cultural and organizational threat* to cohesive, comprehensive FM.

- **Fragmentation under inconsistent names.** When FM *is* called out, it has historically gone by clashing labels — among them Fault Protection, Health Management, Redundancy Management, Safing, and Fault Detection and Response. The handbook flags this nomenclature drift as something to overcome to achieve Agency-wide consistency, since the underlying activities are the same across missions.

## Key Takeaways

1. FM is a **system-level SE discipline**, not a subsystem afterthought: a design is incomplete until failures are addressed, and FM relies on flight, ground, and operations elements cooperating.
2. The discipline's defining functions are **prevent, detect, isolate, diagnose, respond, contain, and recover** — covering off-nominal conditions across the entire mission lifecycle.
3. **Fault ≠ failure**: a failure is unacceptable function; a fault is a cause that explains it. FM is named for faults but governs failures generally.
4. Off-nominal is **three states** — anomalous, degraded, failed — and **time-to-criticality** sets the clock FM must beat.
5. FM is **resource-constrained**, so it is a deliberate **risk/cost balance** tuned to the mission's risk posture, not a maximize-everything exercise.
6. The handbook is **guidance, not a prescription** (and a **Draft 2** at that): it is meant to be adapted per mission and per NASA Center, and used as a companion to the NASA SE Handbook.

## Connects To

- **NPR 7123.1A — NASA SE Processes and Requirements**: the SE technical-process framework (Figure 1) inside which FM activities and derived requirements live (`nasa-npr-7123`).
- **NASA SE Handbook (NASA/SP-2007-6105 Rev 1)**: the nominal-focused companion this FM handbook augments with off-nominal guidance (`nasa-se-handbook`).
- **ISO/IEC 23004-6:2008**: the network-management FM definition ("detect, isolate, correct malfunctions") used to ground NASA's terminology and goal statement.
- **Later chapters of this pack**: the FM development process and lifecycle (Section 4), requirements exemplars, architecture building blocks, V&V considerations, and operations — all foreshadowed here as the Purpose (Section 1.2) of the handbook.
- **Reliability / safety frameworks**: FMEA/FMECA, FTA, and PRA referenced in the document's stakeholder and applicable-documents sections, linking FM to the broader dependability toolset (`nasa-pra`, `mil-std-882`).
