# Chapter — R&M Required Approach: Objectives & Strategies

## Core Idea

The R&M Required Approach defines *what* reliability and maintainability work must achieve before it ever prescribes *how* to achieve it. The top-level aim is to give confidence that a system will keep performing as required across its whole lifecycle, so that mission objectives — including the program's safety, reliability, maintainability, and quality-assurance requirements — are met. Crucially, the Standard does not hand programs a fixed catalogue of R&M deliverables and processes. Instead it states the key objectives and leaves programs free to choose how to satisfy them in a way that fits their acquisition, management, and engineering context and their tolerance for risk. This is the heart of the **Objectives-driven R&M framework**: the objectives are mandatory and stable, while the path to them is deliberately flexible.

## Frameworks Introduced (exact source names, when/how)

- **R&M Technical Objectives** (Section 4.1). The Standard opens its required approach by naming a single top-level objective — sustaining required performance over the lifecycle to satisfy mission goals — and then decomposing it. Programs are expected to meet it by running analysis and testing, and by making design and operational choices that hold down the chance of faults and failures while supplying enough mitigation and restoration capability to keep functionality at an acceptable level.

- **The four subobjectives** (Section 4.1.3). The top-level objective is broken into four parts: (a) the system matches its design intent across interfaces and functions, behaving as planned whether operating nominally or in a failed state; (b) the system and its elements remain functional across the intended life span — its expected environment, operating regime, and patterns of use; (c) the system tolerates faults, failures, and other anomalous events arising internally or externally; and (d) the system reaches an acceptable level of reliability and maintainability so the availability requirement is properly met.

- **Strategies and the objectives-to-strategies decomposition** (Section 4.1.4, with the mapping carried in Appendix A). For each subobjective the Standard supplies strategies — suggested guidance that spaceflight programs can tailor to their risk classification and accepted risk posture. These strategies are framed as the minimum expectations for R&M work on NASA spaceflight programs and projects, with the full objective-to-strategy breakdown placed in Appendix A.

- **Objectives-Driven Approach** (Section 4.2). This section makes the philosophy explicit: the Standard's intent is to provide key R&M objectives rather than a locked set of products and processes, preserving flexibility to meet those objectives consistent with the governing approaches and commensurate with risk tolerance. As a planning activity, programs and projects are required to identify how they will address the objectives, implement the associated strategies, and gather evidence that implementation succeeded.

- **SMA Plan linkage** (Section 5.1, Planning and Implementation). The implementation requirements tie the objectives back to formal planning: the project or program must establish and implement R&M requirements within the SMA Plan called for by NPR 7120.5, and that plan should cover the objectives and strategies of Appendix A and the related Appendix B tables.

## Key Concepts

- **Lifecycle performance assurance.** The organizing concern is not a single design milestone but sustained performance across the system's entire life, judged against mission objectives that include safety, reliability, maintainability, and quality assurance.

- **Two complementary levers.** Programs are expected to act on two fronts at once: reduce the likelihood that faults and failures occur, and build in the mitigation and restoration capability needed to preserve acceptable functionality when they do.

- **Decomposition as the working structure.** The single top-level objective is split into four subobjectives that separate distinct concerns — conformance to design intent, endurance over the intended life, fault tolerance, and adequate reliability/maintainability to satisfy availability. Each then carries its own strategies.

- **Strategies as minimum, tailorable expectations.** Strategies are guidance, not rigid mandates; they can be tailored to a program's risk classification and risk posture, yet they collectively set the floor for what R&M activity is expected to cover.

- **Availability as the integrating requirement.** Subobjective (d) frames reliability and maintainability as the means to a higher end — meeting the availability requirement — which connects component-level R&M work to a system-level performance commitment.

- **Plan-level accountability.** Addressing the objectives is not informal. Programs must state in their planning how they intend to meet the objectives, implement the strategies, and evaluate evidence of success, and they must capture R&M requirements in the SMA Plan required by NPR 7120.5.

- **Shared ownership beyond the R&M discipline.** Some activities needed to address the objectives may be carried out by parts of the program outside the R&M practitioner's scope or discipline; nonetheless every objective and strategy remains relevant to program reliability and mission success, so the appropriate interfaces have to be coordinated.

## Mental Models

- **Objectives are the contract; methods are the implementation.** Picture a stable interface — the four subobjectives — behind which any conforming implementation is allowed. Programs pick the implementation that fits their constraints, but they cannot renegotiate the interface.

- **A decomposition tree from goal to action.** One top-level objective branches into four subobjectives, each of which branches further into strategies. Reading the tree top-down tells you *why*; reading it bottom-up lets you trace any chosen activity back to the mission goal it serves.

- **Prevention paired with recovery.** Think of two parallel pipelines: one drives the probability of faults and failures down, the other stands ready to mitigate and restore. Acceptable functionality is the output of both running together, not either alone.

- **Risk posture as a dial, not a switch.** Tailoring works because strategies flex with risk classification and risk tolerance — a higher-criticality program turns the dial toward more rigor, a lower-risk one toward less, without changing which objectives must be met.

## Key Takeaways

- The required approach fixes the *ends* (one top-level R&M objective, decomposed into four subobjectives) and leaves the *means* open, by design.
- The four subobjectives cover design-intent conformance under nominal and failed conditions, endurance over the intended life and environment, tolerance to internal and external anomalous events, and reliability/maintainability sufficient to satisfy availability.
- Strategies, mapped to objectives in Appendix A, are tailorable guidance that nonetheless represent the minimum expectation for R&M work on NASA spaceflight programs.
- The objectives-driven philosophy exists to preserve flexibility consistent with a program's governing acquisition, management, and engineering approaches and its risk tolerance.
- Programs must plan explicitly how they will meet the objectives, implement the strategies, and evaluate evidence of success — and must record R&M requirements in the SMA Plan required by NPR 7120.5.
- Responsibility for meeting the objectives can extend beyond the R&M discipline, so cross-organizational interfaces must be coordinated.

## Connects To

- **The objectives-to-strategies mapping in Appendix A**, which carries the full decomposition referenced throughout Section 4 and underpins the SMA Plan content.
- **The SMA Plan and NPR 7120.5**, the planning vehicle in which R&M requirements are established and the objectives and strategies are addressed.
- **Implementation Requirements (Section 5)**, which converts the objectives-driven philosophy into the planning and coordination obligations placed on programs and projects.
- **Availability and mission-success requirements**, to which subobjective (d) explicitly ties the reliability and maintainability targets.
