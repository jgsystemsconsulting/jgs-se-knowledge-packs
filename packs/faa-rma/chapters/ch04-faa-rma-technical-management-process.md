# Chapter — RMA Technical Management Process

> Source: FAA-HDBK-006D (2020), Section 6, "Reliability, Maintainability, and Availability (RMA) Technical Management Process." This chapter uses the 006D (2020) revision, not the earlier 006B.

## Core Idea

Where the RMA development stages concentrate on building the system, this process turns its attention to the **acquisition side** of RMA: how a program office translates enterprise-level requirements into a contract, evaluates competing offerors, oversees a developer's design work, and verifies the delivered system. The handbook frames this as a systems engineering process, adapted from the FAA Systems Engineering Manual (SEM), in which RMA practitioners feed inputs into the Acquisition Management System (AMS) and produce its output products.

The governing metaphor for the whole process is a **bridge**: the first task exists to span the gap between abstract, enterprise-level requirements and the concrete procurement specifications for the physical systems that will satisfy them. Everything downstream — the procurement package, the proposal evaluation, the monitoring, the testing — is about keeping that bridge structurally sound as the program moves from concept toward in-service operation.

A second, equally important idea is that **one allocation method does not fit all systems**. The handbook explicitly carves FAA systems into categories and argues that top-down mathematical availability allocation is appropriate for some and actively misleading for others.

## Frameworks Introduced (exact source names, when/how)

- **Acquisition Management System (AMS)** — the FAA acquisition framework whose phases (Service Analysis and Strategic Planning, Concept and Requirements Definition, Investment Analysis, Solution Implementation, In-Service Management) are mapped against the RMA stages and the RMA-related tasks in **Table 6-1**. RMA practitioners synthesize process inputs into AMS output products.
- **The six RMA technical management process tasks** — introduced via **Figure 6-1**, which lays out the task relationships with flow running left to right, mirroring the acquisition process flow. The tasks are: (1) Preliminary Requirements Analysis, (2) Procurement Package Preparation, (3) Proposal Evaluation, (4) Design Monitoring, (5) Testing and Verification, and (6) Requirements Analysis and Maintenance.
- **FAA System Categories for RMA** — a three-way classification (Information Systems, Remote and Distributed Systems, Infrastructure Systems) introduced in Section 6.4, each warranting distinct treatment when specifying RMA requirements.
- **Figure 6-2 (Effect of Service Interruptions on NAS Capacity)** — used to illustrate the transition from full-capacity to reduced-capacity operation and the safety-hazard interval (the shaded triangle) that can open up during that transition.
- **NAPRS / FAA Order 6040.15H** — the National Airspace Performance Reporting System defines the services on which NAS-RD RMA requirements are allocated to Service Threads.
- **ASQ Certified Reliability Engineer Body of Knowledge** — the certification framework the handbook points to for qualifying RMA subject-matter experts.

## Key Concepts

**The six tasks, in sequence.**

1. **Preliminary Requirements Analysis** builds the bridge from enterprise requirements to procurement specifications and captures operational requirements early enough to support planning. The handbook gives two worked examples: *scheduled downtime*, defined in advance so operators can plan and so the chance of unscheduled outages is reduced; and *redundancy and fault tolerance* requirements, which become necessary when system elements alone cannot meet availability targets and which require specifying fault-tolerance performance characteristics such as switchover and restart times.

2. **Procurement Package Preparation** produces the specifications that define RMA and fault-tolerance requirements and form the basis of a binding contract; it defines the developer effort needed for documentation, engineering, and testing; and it guides offerors on what the RMA sections of their technical proposal must contain. The RMA-relevant package contents are the **System Specification Document (SSD)** (derived from the Program Requirements Document, carrying the quantitative RMA characteristics of fault detection/recovery, monitor-and-control, manual recovery, and diagnostics), the **Statement of Work (SOW)** (the developer's RMA-related tasks, including risk monitoring, fault-avoidance programs, and the reliability growth testing program), and the **Information for Proposal Preparation (IFPP)** (the RMA activities the Government expects the developer to perform).

3. **Proposal Evaluation** judges the offeror against three key factors: *reliability modeling and assessment* (can the offeror substantiate the RMA goals?), *fault-tolerant design evaluation* (is the proposed fault-detection/recovery/redundancy architecture complete and consistent, and crucially, does it substantiate compliance with recovery-time requirements?), and *performance modeling and assessment* (predicted loads, capacity, and response times).

4. **Design Monitoring** keeps Government insight into the developer's work through *formal design reviews*, *Technical Interchange Meetings (TIMs)* that scrutinize fault-tolerance timing parameters and the model predictions or measurements backing them, and *fault tolerance design risk management* aimed at catching RMA flaws early. The handbook directs that separate risk-management activities be stood up for fault-tolerant infrastructure, error handling in software applications, and performance monitoring; for software application fault tolerance, risk management means setting developer standards and enforcing them.

5. **Testing and Verification** covers *fault tolerance diagnostic testing* (observing the protocols in operation and diagnosing abnormalities), *functional testing* (verifying each RMA-related functional requirement — redundancy, failure, recovery, fallback), and *reliability growth testing* (validating the reliability growth program, with the underlying concept carried in Section 5).

6. **Requirements Analysis and Maintenance** sustains the requirements baseline over time through *NAS-RD maintenance* — keeping Service Thread mapping flexible so new NAS capabilities and threads can be accommodated — and *RMA requirements assessment*, recognizing that NAS-RD RMA requirements allocate to Service Threads grounded in NAPRS services.

**Process inputs and outputs.** The process consumes FAA policy and standards, the NAS Enterprise Architecture, NAS Requirements, the Systems Engineering Management Plan, program requirements, functional analysis, physical architecture, developer TIM minutes and briefings, and developer data item deliverables. It emits a corresponding set of products grouped by task — the RMA sections of the NAS-RD, the RMA/fault-tolerance sections of the SSD and SOW, Data Item Descriptions, IFPP content, the three evaluation assessments, the monitoring artifacts, the three test types, and the maintenance products.

**Three FAA system categories.** *Information Systems* are software-intensive air traffic automation and communications capabilities with stringent availability requirements; their heavy custom-software content drives cost and schedule risk, and because they deliver the most critical and most visible services, they receive the most attention and are characterized and allocated by NAS-level RMA requirements. *Remote and Distributed Systems* are built from elements — for instance sensors converging upward into an information subsystem, or a service distributed outward across many display workstations; they reach the needed availability through diversity and overlapping coverage rather than through per-element allocation. *Infrastructure Systems* are supporting utilities such as power and HVAC that keep the Service Thread equipment running.

**The safety hazard interval.** When a critical service is interrupted and the NAS transitions from normal to reduced capacity, controllers fall back on manual procedures, increase separation, and clear airspace until a steady state returns. During that transition, a safety-hazard risk can momentarily rise (the shaded triangle in Figure 6-2). The handbook is careful to note that in most cases this interval is negligible or absent, leaving efficiency — not safety — as the practical concern.

**SMEs across the lifecycle.** RMA practitioners are meant to be present from concept studies (when performance, cost, and technology trade-offs are being debated), through requirements development driven by the Concept of Operations (CONOPS), as core members of multi-disciplinary development teams during design, into test and evaluation, and finally through integration, deployment, and operations.

## Mental Models

- **RMA acquisition as a bridge.** The recurring image is a span connecting enterprise requirements on one bank to physical procurement specifications on the other. The six tasks build, inspect, and maintain that span; if the bridge is unsound, the delivered system will not actually satisfy the requirements it was supposed to.
- **The reliability block diagram as the "end-user service" view.** Infrastructure systems are best understood as a reliability block diagram capturing all the "sensor to glass" equipment needed to deliver a service to the air traffic specialist — a way of reasoning about availability that follows the end-to-end service rather than isolated boxes.
- **Availability as a binary up/down measure with limited reach.** Availability is fundamentally an up-or-down quantity. That makes it a poor descriptor for subsystems composed of many independent, partially redundant elements, where the real question is graceful degradation rather than a single up/down verdict.
- **Match the allocation method to the system's failure structure.** Top-down mathematical allocation suits centralized, software-intensive information systems but breaks down where elements degrade gracefully (remote/distributed) or where failures are correlated rather than independent (infrastructure). The right tool depends on how the system actually fails.

## Anti-patterns

The source explicitly names two practices to avoid:

- **Forcing top-down "r of n" availability allocations onto remote and distributed subsystems.** The handbook argues this is inappropriate because it requires arbitrary failure definitions — its example is a surveillance subsystem declared "down" the instant 48 of 50 radars are up when the threshold was set at 49 — which does not reflect operational reality and produces unrealistic allocations. Such subsystems are robust precisely because losing individual elements only degrades, rather than fails, the whole; their element-level availability is better set from lifecycle-cost considerations and acquisition managers' knowledge of achievable reliability, and their overall suitability is best determined by subject-matter-expert judgment on element number and placement rather than by an arbitrary mathematical allocation.
- **Applying top-down availability allocation to infrastructure systems.** Because power, HVAC, and similar systems violate the independent-failure assumption underlying RMA calculations — they can directly cause failures in the systems they support — top-down allocation is inappropriate. The handbook's preferred alternative is a well-defined set of standard configurations matched to the availability needs of the Service Threads being supported.

A related caution, framed positively in the SME section, is treating RMA as a stand-alone specialty summoned only during a crisis; the handbook insists instead that it is a continuous element of acquisition across the lifecycle.

## Key Takeaways

- The RMA technical management process is the **acquisition-facing** complement to the development stages, organized as six sequential tasks running in parallel with the AMS phases (Table 6-1, Figure 6-1).
- Task 1 exists to **bridge enterprise requirements to procurement specifications**, capturing operational requirements such as scheduled downtime and fault-tolerance timing (switchover, restart) early.
- The procurement package's RMA backbone is the **SSD, SOW, and IFPP**, with the SSD carrying the quantitative RMA characteristics and the SOW defining the developer's RMA tasks and reliability growth program.
- Proposal evaluation hinges on three factors, with **substantiated compliance to recovery-time requirements** singled out as the critical element of the fault-tolerant design review.
- Design monitoring runs **separate fault-tolerance risk-management threads** for infrastructure, software error handling, and performance monitoring, and software fault tolerance is governed by setting and enforcing developer standards.
- **One allocation method does not fit all**: top-down allocation fits Information Systems but is named as an anti-pattern for Remote/Distributed Systems (graceful degradation, arbitrary "r of n" thresholds) and Infrastructure Systems (correlated, dependency-driven failures).
- Service interruptions can briefly raise safety-hazard risk during the **capacity-transition interval**, though usually the practical impact is on efficiency, not safety.
- RMA expertise belongs **across the entire lifecycle**, and the handbook points to ASQ Certified Reliability Engineer credentials (eight years of experience, three in a decision-making role) and training from ASQ, DAU, and others.

## Connects To

- **The RMA development stages (Section 5)** — this process is the acquisition counterpart; reliability growth testing introduced here as a Task 5 verification activity has its underlying concept defined there.
- **FAA Systems Engineering Manual (SEM)** — the source from which Section 6 was adapted, anchoring this process in the broader FAA systems engineering discipline.
- **NAS-RD, Service Threads, and NAPRS (FAA Order 6040.15H)** — the requirements and service framework against which RMA requirements are allocated and maintained in Task 6.
- **Availability and reliability block-diagram modeling** — the "sensor to glass" reliability block diagram view of infrastructure systems and the binary-availability critique link directly to the quantitative RMA modeling methods used elsewhere in the handbook.
- **Acquisition / contracting practice** — the SSD/SOW/IFPP package, proposal evaluation factors, and design-monitoring TIMs tie this chapter to general systems-engineering acquisition and source-selection practice.
- **Reliability engineering as a profession** — the certification and training guidance connects to the ASQ CRE body of knowledge and DAU's acquisition workforce training.
