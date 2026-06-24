# Chapter 1 — Introduction, Key Documents, and Important Definitions

> **Caveat — read this first.** This pack is built on **FAA-HDBK-006D (2020)**, not the older 006B. The handbook itself supersedes FAA-RMA-HDBK-006C version 1.1 (19 November 2015), which it still lists among its own applicable documents. When you cite a clause, a definition, or a section number from this pack, it is the **006D** revision you are pointing at. Use 006D — anything labeled 006B is out of scope here.

## Core Idea

FAA-HDBK-006D is the FAA's guidance for engineering and managing **Reliability, Maintainability, and Availability (RMA)** across the full lifecycle of National Airspace System (NAS) hardware and software. The handbook's claim is that the dependability of a NAS system is something you *estimate, manage, and improve* with deliberate analytical and management methods — not a property you hope falls out of good design. It bundles the processes, tools, and figures of merit needed to assess RMA from concept feasibility through design, development, test, and field implementation.

The three attributes the handbook is organized around are defined plainly at the front:

- **Reliability** — the probability of zero failures over a stated time interval or mission.
- **Maintainability** — a measure of how easily and quickly a system can be returned to operational status after a failure.
- **Availability** — the percentage of time a system is ready to use when it is called upon.

The reason RMA matters to the FAA is mission-specific. Once fielded, NAS systems have to deliver continuous service to extremely complex air-traffic operations, and they collectively carry the agency's safety mission, where operations follow strict requirements to keep accident risk low. Continuity plus safety means NAS systems have to stay highly dependable — and a structured RMA estimation process is how you steer toward that. Notably, the handbook deliberately refuses to mandate any single RMA method; it leaves practitioners free to pick the techniques that fit their application.

A second organizing idea is that RMA is an *estimate*, never an exact truth. Because the numbers come from statistical measurement data, the true RMA of a system is never precisely known — the data is subject to random error, and it can be limited, imprecise, wrong, or missing entirely. The handbook treats this as a feature to manage, not a flaw to hide, and insists that results only mean something *in context*.

## Frameworks Introduced (exact source names, when/how)

- **FAA-HDBK-006D — "Reliability, Maintainability, and Availability (RMA) Handbook"** — the document itself. Introduced in Section 1 (Introduction) as lifecycle guidance for RMA on NAS hardware and software systems. It is updated periodically as adjudicated stakeholder comments arrive, via the comment transmittal form provided in Appendix F.

- **FAA-RMA-HDBK-006C version 1.1 (19 November 2015)** — the prior revision, listed in Section 2.2.1 among the FAA applicable documents. Its appearance signals that 006D is the supersession; the pack is grounded in 006D.

- **FAA Safety Management System (SMS) Manual, July 2017 (SS-Manual-2017)** — cited in Section 2.2.1 and again as the source of the handbook's definition of **SAFETY**. It anchors the relationship between RMA and safety risk discussed in Section 1.9.

- **FAA System Engineering Manual (SEM), Version 1.1 (11 September 2015)** — listed in Section 2.2.1 and used as a defining reference for several core terms (availability, maintainability, reliability, failure rate, MTBF, risk). It is the SE-process companion that this RMA handbook plugs into.

- **National Airspace System Requirements Document, NAS-RD-2013** — listed in Section 2.2.1 as the requirements baseline (Baseline, 11 August 2014) the NAS is engineered against.

- **MIL-STD-721C (1981)** — the DoD's terminology standard, whose title covers the definition of R&M terms; listed under Department of Defense publications (Section 2.2.2) as the canonical DoD vocabulary source for reliability and maintainability terms.

- **MIL-HDBK-217F (Notice 1&2), "Reliability Prediction of Electronic Equipment" (28 February 1995)** — listed in 2.2.2 as the electronics reliability-prediction reference.

- **MIL-STD-1629A (Notice 1&2), "Procedures for Performing a Failure Mode Effects and Criticality Analysis" (28 November 1984)** — the FMECA procedure, listed in 2.2.2.

- **MIL-HDBK-189C, "Reliability Growth Management" (14 June 2011)** and **AMSAA TR-652, "AMSAA Reliability Growth Guide" (September 2000)** — the reliability-growth references in 2.2.2.

- **MIL-STD-882E, "DoD Standard Practice for System Safety" (11 May 2012)** — the DoD system-safety practice, listed in 2.2.2.

- **MIL-STD-3034A / DoD Manual 4151.22-M, Reliability Centered Maintenance (RCM)** — the RCM process and policy references in 2.2.2; paired on the FAA side with FAA Order 6000.207, the Reliability Centered Maintenance Handbook.

- **DoD Guide for Achieving Reliability, Availability, and Maintainability (DoD Guide RAM, 3 August 2005)** — listed in 2.2.2; a defining reference (alongside the SEM) for the MTBF/MTTR form of availability.

- **NASA SP-2016-6105, "NASA Systems Engineering Handbook, rev 2" (2016)** and **NASA-STD-8729.1A, "Reliability and Maintainability (R&M) Standard…" (13 June 2017)** — the NASA references in 2.2.3; NASA SP-2016-6105 is the cited source for the handbook's definitions of FAILURE and RELIABILITY's divisions.

- **NUREG/CR-6101 (1993)** — the NRC report on software dependability for nuclear-reactor protection systems; listed in 2.2.3 and used as the defining source for ERROR, FAILURE, and FAULT.

- **IEEE Std 1633-2016, "IEEE Recommended Practice on Software Reliability"** — the non-government software-reliability reference (Section 2.3).

- **RTCA DO-178C** and **RTCA DO-278A** — the airborne and CNS/ATM software assurance guidance, listed in Section 2.3.

The handbook's own preview (Section 1.11) lays out where the rest of the document goes: Section 2 is the applicable-documents list (FAA, DoD, Government, Non-Government), Section 3 is the short definitions list (the full glossary is Appendix A), Section 4 covers the quantitative concepts (figures of merit, probability distributions, statistics), Section 5 covers the four stages of an RMA program across the acquisition lifecycle, Section 6 covers managing RMA efforts and building them into a procurement package, and Section 7 maps RMA methodologies and tools onto the lifecycle phases. Appendices add acronyms/glossary (A), references (B), a software-reliability overview (C), guidance for the RMA sections of a Program Requirements Document (D), NAS service-thread diagrams (E), and the change transmittal form (F).

## Key Concepts

**Reliability has three flavors.** The handbook splits reliability into (a) *material* reliability — hardware, software, firmware; (b) *mission* reliability — intentions and goals; and (c) *logistics* reliability — implementation, support, and coordination. This decomposition recurs both in Section 1.5 and in the Section 3 definition, so it is meant to be carried as a working distinction, not a one-off remark.

**MTBF is the worked example of a figure of merit.** Mean Time Between Failures is offered as the traditional reliability statistic — a probability-based measure estimated from collected failure data averaged over time. The handbook is explicit that MTBF is used for *systems and subsystems*, whereas **MTBO (Mean Time Between Outages)** is the analogous measure for *services and facilities*.

**The "nines" of availability.** Table 1-1 ties availability-as-a-percentage to concrete downtime budgets across observation windows (per year, per month, per week). "One nine" (90%) leaves roughly 36.5 days of downtime per year; each added nine cuts the allowed downtime by an order of magnitude, on out to "seven nines" (99.99999%). This is the intuition pump for what a small percentage difference actually costs operationally.

**Two forms of the availability equation.** Section 3 gives availability as `uptime / (uptime + downtime)`, including logistics time, ready time, administrative/waiting downtime, and both preventive and corrective maintenance downtime. It also gives the narrower engineering form, `MTBF / (MTBF + MTTR)`, which deliberately *ignores* standby and scheduled-maintenance delays and administrative/logistics downtime. Which form you use changes what the number means — that is the point of presenting both.

**The error → fault → failure chain.** The handbook keeps these three crisply separate, citing NUREG/CR-6101: an **error** is an incorrect state of hardware, software, or data that results from a fault; a **fault** is a deviation of system behavior from what its requirements specify (a hardware fault that is never activated never becomes effective and causes no failure); a **failure** is the external manifestation of an error — the inability to perform the required function within specified limits. Direction of causation matters: fault enables error, error surfaces as failure.

**Dependability is the umbrella.** Dependability is the combined R-M-A picture — the confidence that a system will operate as users expect and won't fail in normal use. RMA exists to produce that confidence as measured information.

**Hardware RMA and software RMA are not the same problem.** Section 1.8 draws the contrast sharply. Hardware degrades through wear and tear; software does not — software degrades through logical errors and faults, including hidden cyber-attack vulnerabilities or dependence on support that no longer exists (an obsolete compiler, say). Hardware reliability shifts at the extremes of life (early use, end of life); software reliability shifts during development and test as logic errors, bad statements, misunderstood requirements, and wrong input descriptions are found and removed. Hardware repair is swap-in-an-identical-part; software repair is not, because a fix can introduce new errors, and without configuration control you may even edit the wrong version. The handbook narrows its own focus to hardware-and-software availability as the two principal components of system availability, explicitly bracketing out human, service, facility, and communications "availabilities" as out of scope.

**RMA history starts at NASA.** Reliability analysis in federal projects traces to the NASA space program, where the foundational principle was set: a system's reliability equals the composite reliability of its components, so the weakest link governs. Availability and maintainability grew out of reliability afterward.

**RMA is broad-scope, lifecycle-wide.** The RMA effort spans the entire lifecycle — concept, requirements, design, integration, test, deployment, and disposal — collecting and integrating data, then aggregating it into figures of merit that express overall mission effectiveness. It can also be exercised in a lab using simulated data.

## Mental Models

- **RMA as an estimate under uncertainty, not a fact.** The true RMA of a system is never exactly known because it rests on statistical data that carries random error and may be sparse or flawed. Carry every RMA number as a best estimate with a confidence story behind it, and remember that bad enough data makes the whole estimation process questionable. Good measurement design and thorough analysis are what keep the estimate worth trusting.

- **Context is part of the measurement.** An RMA result pulled out of context can be seriously biased — measuring during a period without knowing the factors in play at that time distorts the answer. The handbook names the context that must be understood: system design, manufacturing quality, the operating environment, the support system's own design and development, operator/maintainer training and skill, availability of repair materiel, and the diagnostic aids and instrumentation on hand. The model: an RMA figure is meaningless until you can name the conditions under which it was produced.

- **The weakest link governs.** From the NASA-origin principle — composite reliability is dominated by the least reliable component — so improving overall dependability means hunting the weakest element, not polishing the strong ones.

- **RMA and safety risk are cousins, not twins.** They share analytical methods and analysts often lean on both, but their worldviews differ. RMA optimizes against *cost* of failure — downtime, spares, repair gear, personnel, warranty — and chases dependability levels fixed in advance. Safety optimizes to *preserve life*, attends only to dangerous failure modes, and seeks to avoid any catastrophic loss of a service even briefly. The consequence to hold: a system can be "reliable" against its design criteria and still carry safety risk that needs its own separate assessment and mitigation. Safety is also broader in scope (the whole air-transportation system) where RMA is narrower (specific systems, services, facilities).

- **Resiliency sits on top of RMA.** Resiliency adds the ability to prevent, blunt, and recover from high-impact events — preparing for and adapting to changing conditions, and withstanding deliberate attacks, accidents, and natural threats. Its building principles are redundancy, diversity, response time, and recovery, achieved through a standardized lifecycle approach to diversifying service capabilities. Treat resiliency as a layer that supplements RMA rather than a synonym for it.

- **A spectrum of "availabilities."** True operational availability is a composite that includes human, service, facility, and communications availability — even though this handbook scopes its analysis down to hardware-plus-software. The model keeps you honest about what your in-scope number is *not* capturing.

## Anti-patterns

The handbook is written as positive guidance and does not present a labeled catalogue of named anti-patterns. The closest it comes are stated as cautions and limitations, not named failure modes:

- **Reading RMA results out of context.** Treating an RMA figure as portable when it was produced under unknown conditions introduces serious bias; the named context factors must be understood first.
- **Trusting estimates built on bad data.** When statistical data is limited, imprecise, erroneous, or missing to an excessive degree, the value of the RMA estimation process itself becomes questionable.
- **Assuming software repair is a clean swap.** Unlike replacing a hardware part with an identical one, a software correction can inject new errors — and without enforced configuration control, the wrong version may be modified, reintroducing old problems or dropping current features.
- **Equating "reliable" with "safe."** A system that meets its dependability design criteria may still carry unaddressed safety risk; conflating the two skips a required separate safety assessment.

## Key Takeaways

- This pack is grounded in **FAA-HDBK-006D (2020)**, which supersedes 006C v1.1 (2015); cite 006D, not 006B.
- **Reliability, Maintainability, Availability** are the three pillars: probability of zero failures over an interval/mission; ease and speed of restoration after failure; and percentage of time ready when tasked — with dependability as the combined umbrella.
- RMA is a **lifecycle-wide, methodology-agnostic** discipline: it spans concept through disposal, and the handbook deliberately declines to mandate any single approach.
- RMA values are **estimates under statistical uncertainty** and are only meaningful **in context** — system design, manufacturing quality, environment, support system, training, materiel, and diagnostics all have to be known.
- **Figures of merit** are the currency: MTBF for systems/subsystems, MTBO for services/facilities, MTTR for restore time, and availability expressible either as `uptime/(uptime+downtime)` or the narrower `MTBF/(MTBF+MTTR)`.
- The **fault → error → failure** chain is kept distinct: a fault is a deviation from required behavior, an error is the resulting incorrect state, a failure is the external manifestation.
- **Hardware and software RMA differ fundamentally** — wear-out versus logic faults, identical-part swap versus risk-laden code fixes — and the handbook scopes itself to hardware-plus-software availability, bracketing human/service/facility/communications availability out.
- **RMA, safety risk, and resiliency are related but distinct**: RMA minimizes cost-of-failure to a preset dependability target; safety preserves life across dangerous modes; resiliency layers on prevent/limit/recover against high-impact events.
- Section 2 binds the handbook to a wide reference base — FAA orders and the SEM/SMS, DoD MIL-STDs/HDBKs (721C, 217F, 1629A, 882E, RCM), NASA SE/R&M standards, NUREG/CR-6101, IEEE 1633, and RTCA DO-178C/DO-278A.

## Connects To

- **FAA System Engineering Manual (SEM) (sibling pack).** 006D is RMA specialty-engineering content that plugs directly into the SEM's process framework, and the SEM is a defining reference for several RMA terms. Read this pack as the deep dive behind the SEM's RMA/specialty-engineering treatment.
- **FAA System Safety pack and the SMS Manual.** Section 1.9's RMA-versus-safety-risk distinction and the SAFETY definition both point at the FAA SMS Manual; pair this chapter with the safety pack to see where the cost-driven and life-driven worldviews must be reconciled.
- **DoD reliability/maintainability standards (MIL-STD-882, MIL-HDBK family).** The DoD applicable-documents list (882E for system safety, 1629A for FMECA, 217F for reliability prediction, 721C for terms, 189C/AMSAA for reliability growth, RCM standards) ties this pack to the broader defense R&M canon — useful when an FAA effort borrows DoD analytical methods.
- **NASA SE Handbook and R&M Standard (sibling packs).** The handbook's RMA origin story is the NASA space program, and NASA SP-2016-6105 / NASA-STD-8729.1A are cited definitional sources; the weakest-link composite-reliability principle is shared DNA across the NASA packs.
- **Software-assurance and software-reliability references.** NUREG/CR-6101, IEEE 1633-2016, and RTCA DO-178C/DO-278A connect Section 1.8's hardware-versus-software RMA contrast (and Appendix C's software-reliability overview) to any pack covering software dependability, certification, and configuration control.
- **Downstream 006D chapters.** This chapter sets up Section 4 (quantitative concepts — figures of merit, probability distributions, statistics), Section 5 (the four stages of an RMA program across acquisition), Section 6 (managing RMA and embedding it in a procurement package), and Section 7 (RMA methodologies and tools mapped to lifecycle phases) — plus Appendix D's guidance for the RMA sections of a Program Requirements Document.
