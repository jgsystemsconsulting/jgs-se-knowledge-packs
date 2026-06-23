# Chapter 1 — Introduction and the AMS Lifecycle

> **Caveat — read this first.** The FAA Systems Engineering Manual (SEM) is a *civil-agency* SE process companion to NASA's and DAU's defense/aerospace guidance. It speaks the same lifecycle language (concept → development → production → utilization, mapped to ISO/IEC 15288), but it is wrapped around one agency-specific decision framework: the FAA Acquisition Management System (AMS). Where NASA gives you KDPs and the DAU guidebook gives you milestone reviews, the SEM gives you AMS *decision points*. Treat this pack as the FAA dialect of a shared SE grammar, not a rival doctrine.

## Core Idea

The SEM exists to make systems engineering *the connective tissue* of FAA acquisition. It is a guidance document that bundles industry and government best practices and re-expresses them in the operating context of the FAA — an agency whose mission, stated bluntly at the front of the manual, is to run the safest and most efficient aerospace system in the world. The central premise is that SE pays off only when it starts the moment a need is recognized and runs unbroken through the entire program lifecycle; done that way, it catches deficiencies early in acquisition and keeps cost and schedule overruns from compounding.

The organizing spine of the whole pack is the **AMS lifecycle**. Every significant FAA project — whether it touches the National Airspace System (NAS) or not — is tracked against a sequence of lifecycle phases punctuated by formal decision points. A solution begins as an identified *service need*, passes through analysis and solution development, and ends as a fielded capability that stays in service until it is replaced or retired. The SEM's job is to overlay a systems-engineering view on that journey: what SE products are required, what role the systems engineer plays, and which decision-point documentation package the work has to feed.

Two altitudes of SE are distinguished from the outset. At the **enterprise level**, SE management integrates across investment programs so the FAA stays efficient and interoperable. At the **program level**, SE optimizes the performance, benefits, operations, and lifecycle cost of one solution. Individual programs are expected to *tailor* the processes, tools, and techniques to the complexity of what they are building — the manual is explicitly a menu of proven practices, not a fixed checklist.

## Frameworks Introduced (exact source names, when/how)

- **FAA Systems Engineering Manual (SEM), Version 1.0** — the document itself. Introduced in the Preface and Section 1 as the agency-wide replacement for the older *National Airspace System SEM, Version 3.1* (published 2006). The revision was driven by usability complaints, 2012 workshops, and the need to support the transition to NextGen. Updates are scheduled every one to two years.

- **Acquisition Management System (AMS)** — introduced in Section 2 as the FAA acquisition policy established in 1996. It is the lifecycle framework the SEM wraps around, covering strategic planning, budgeting, enterprise architecture, portfolio management, and investment decision-making. Policy detail lives in the FAA Acquisition System Toolset (FAST).

- **Next Generation Air Transportation System (NextGen)** — named in the Preface and Section 1.5 as the comprehensive modernization of the NAS that the SEM is meant to support. NextGen is the reason the NAS is described as evolving into a more complex System of Systems.

- **Plan, Do, Check, Act (PDCA) cycle** — introduced in Section 1.4 as an optional organizing/continuous-improvement device that the systems engineer may lay over iterating SE and Technical Management processes. The manual credits Walter Shewhart (Bell Laboratories, 1930s) as originator and W. Edwards Deming as popularizer, and notes Deming's later "Plan, Do, Study, Act" variant (he objected that "check" stressed inspection over analysis). It cites the Anderson 2011 attribution and flags the modern "Adjust" reading of the fourth step.

- **System of Systems (SoS)** — introduced in Section 1.5. The SEM leans on the INCOSE handbook definition of a system — interacting elements combined and organized to meet one or more stated purposes — alongside the prior SEM's definition, and cites Maier (1998) for distinguishing SoS characteristics and Carlock (2001) for the emergent-union argument. ADS-B is given as the worked FAA example.

- **ISO standard No. 15288 (2008)** — invoked in Section 2.1 (Figure 4) as the generic product life cycle the FAA phases are mapped against (Concept / Development / Production / Utilization stages). This is the explicit bridge to the broader SE canon.

- **Enterprise Architecture (EA), NAS ConOps, and Destination 2025** — named as the top-level strategy artifacts that Service Analysis & Strategic Planning keeps current. EA roadmaps specify *when* a service need enters the AMS lifecycle; Destination 2025 sets long-term strategic and performance goals.

- **Integrated Systems Engineering Framework (ISEF)** — referenced in the CRD and Investment Analysis work-product tables as the guidance source for *which* EA products a given initiative needs.

- **Acquisition Category (ACAT)** — introduced in Investment Analysis as the designation, based on dollar thresholds plus qualitative factors (program risk, complexity, political sensitivity, likely NAS safety impact), that scales the rigor of the analysis.

- **Safety Management System (SMS) Manual** — cited repeatedly as the governing reference for the safety assessments that recur at each decision point (OSA, CSA, PHA, SSHA, SHA, O&SHA, SSAR).

## Key Concepts

**The five AMS lifecycle phases.** The manual lays out the phases and their concluding decision points in order:

1. **Service Analysis & Strategic Planning** — identify and define service needs; align them with strategic objectives. Decision point (1): Concept and Requirements Definition Readiness Decision.
2. **Concept and Requirements Definition (CRD)** — research concepts that could satisfy the need; define functional and performance requirements; identify preliminary alternatives. Decision point (2): Investment Analysis Readiness Decision.
3. **Investment Analysis (IA)** — refine requirements, analyze alternatives, gather industry feedback, select an option to fund. Split into Initial IA and Final IA, with decision points (3) Initial Investment Decision and (4) Final Investment Decision.
4. **Solution Implementation (SI)** — develop and produce the solution; deploy and commission it. Decision point (5): In-Service Decision.
5. **In-Service Management** — operate, maintain, and sustain the solution until disposal, update, or replacement.

**Decision points as gates.** Because the AMS lifecycle is formalized in FAA policy, each decision point demands a defined set of completed activities and an approved documentation package whose contents reflect the maturity of the program's requirements, planning, and development. SE is what carries a program cleanly through those gates.

**Research for Service Analysis (RSA).** A *non-phase* activity that recurs across several phases as needed, feeding Service Analysis. It draws on two portfolios — Research, Engineering & Development (RE&D) and Concept Maturity and Technology Development (CMTD) — to mature operational concepts, reduce risk, and validate requirements before a program formally enters CRD.

**Requirements maturation as the program's heartbeat.** Requirements thread through every phase and ratchet up in specificity, captured in a named document series: preliminary (pPR/pPRD) in CRD → initial (iPR/iPRD) in Initial IA → final (fPR/fPRD) in Final IA, after which system specifications add low-level detail. The manual frames requirements development as the recognized proxy for a solution's maturity. A parallel ratchet runs on the contracts side — Screening Information Requests (SIRs) and Statements of Work — and the two must stay in sync: the SEM stresses that industry feedback is critical to informing requirements and ensuring all available technologies are considered.

**Solution-agnostic to solution-specific.** Preliminary requirements must be solution-agnostic so alternatives can be evaluated without bias; only as analysis narrows do requirements become solution-specific, and finally synchronized with a vendor proposal (without becoming vendor-specific until contract award, which is withheld until *after* the Final Investment Decision).

**Acquisition Program Baseline (APB).** The cost/schedule/performance contract binding three parties — the investment decision authority, the service organization that implements the solution, and the community of users — finalized just before the Final Investment Decision and the yardstick the program is measured against thereafter.

**Two halves of Solution Implementation.** SI splits into *Product Realization* (turning the approved baseline into hardware, software, and processes) and *Deployment and Transition* (fielding, installing, and switching over from the legacy asset). The FAA almost always contracts production out — the manual contrasts the agency with an industrial "widget-maker" — so the systems engineer's job in SI is oversight, advisory, and verification, not fabrication.

**Operational readiness = effectiveness + suitability.** Before a solution goes operational it needs a declared readiness date. *Effectiveness* measures how well it satisfies the service need; *suitability* measures how well it fits its environment (compatibility, reliability, human factors, maintenance, safety, training). Candidate test sites named include the FAA Academy, the FAA Logistics Center, and the William J. Hughes Technical Center.

**Verification testing and the build/test loop.** In Product Realization, each solution element must pass its Verification Plan criteria before further assembly; a failed test forces rebuild or redesign unless a mitigation exists. COTS components are flagged as a way to simplify verification and reduce risk. Design reviews (SRR, SDR, PDR, CDR, TRR, FCA, PCA) and audits punctuate the build.

**In-Service Management feeds back into the front of the lifecycle.** Operational analysis of fielded assets detects performance shortfalls, cost-of-ownership trends, and adverse support trends — and when a capability can no longer meet demand (or a better option exists), the service organization re-enters service analysis toward a new investment. The manual stresses looking far enough ahead to field a replacement before the incumbent fails or goes obsolete. The NAS Change Proposal (NCP) is the formal mechanism for requesting a NAS change.

## Mental Models

- **The lifecycle as a maturity ratchet.** Each phase exists to raise the resolution of the same few things — the need, the requirements, the alternatives, the cost estimate, the safety picture. Nothing is created once and frozen; the shortfall analysis, the ConOps, and the requirements documents are *revised* and *quantified* with each pass. Think of it as successive zoom levels on one solution, not a relay of independent stages.

- **SE as a skill set, not a job title.** The manual is emphatic that systems engineering is a competency distributed across a project team. Many lifecycle activities support the program manager and may land on any team member; the reader is warned not to assume everything in Section 2 is "for systems engineers only." The "Systems Engineering Role" boxes describe a *function being performed*, regardless of who holds the badge.

- **Two altitudes, always.** Hold both the enterprise view (integration across investment programs, EA roadmaps, portfolio alignment) and the program view (optimizing one solution) in mind simultaneously. The systems engineer is described as uniquely qualified to apply a system-of-systems perspective — spotting capabilities shared across systems that must be coordinated, not duplicated.

- **PDCA as an inner loop.** Where a process iterates within or across phases, wrap it in Plan-Do-Check-Act: set measurable output expectations, execute and collect data, compare actual against planned, then act on the root causes of the gap. Start small to surface adverse effects cheaply. The fourth step is better read as "adjust the gap between current and planned state" than "do something."

- **Evidence over advocacy at the decision points.** Investment Analysis is framed as developing *convincing evidence* of two propositions: that the proposal is the most attractive economic opportunity available, and that the implementation plan is well-conceived, low-risk, and well-understood. The decision authorities (the Joint Resources Council) are choosing among competing proposals for a limited capital pool, so the SE deliverable is a defensible cross-check, not a pitch.

- **System of Systems changes the unit of analysis.** In a true SoS, each component system keeps its own independent purpose and independence, yet the union does something none of the parts can. The model to carry: capability is emergent and lives in the *connections*, so assurance properties already verified on individual systems (security, safety, reliability, availability) must be *re-assessed* once those systems are networked — networking can introduce new vulnerabilities.

## Anti-patterns

The SEM is written as positive guidance and does not present a labeled catalogue of named anti-patterns, so this section is intentionally sparse. The closest the slice comes to naming things-to-avoid are stated as cautions rather than named failure modes:

- **Writing requirements that presuppose a solution.** Preliminary requirements that are not solution-agnostic bias the comparison of alternatives and defeat unbiased, measurable evaluation.
- **Assuming SoS assurance carries over for free.** Treating a networked System of Systems as if the constituent systems' verified safety, security, and reliability still hold — without reassessing the combination — is flagged as a way new vulnerabilities slip in.
- **Treating "Act" as merely "do."** The manual notes the misreading of PDCA's fourth step as action/implementation (which actually belongs in "Do"), obscuring its real purpose of correcting the gap to plan.

## Key Takeaways

- The SEM is the FAA's agency-wide SE guidance, replacing the 2006 NAS SEM and explicitly oriented toward enabling NextGen; it is a tailorable compilation of proven practices, not a rigid procedure.
- The **AMS lifecycle** — five phases (Service Analysis & Strategic Planning → CRD → Investment Analysis → Solution Implementation → In-Service Management) gated by five numbered decision points — is the backbone every chapter hangs from.
- **Requirements maturity is the program's pulse**: pPR → iPR → fPR → system specifications, kept in lockstep with the SIR/contracts track and with the enterprise architecture.
- SE is a *distributed skill set* that supports the program manager and recurs through standard "Systems Engineering Role" responsibilities at each step; it is not the exclusive province of people titled "systems engineer."
- Safety, via the SMS Manual, is assessed and re-assessed at every decision point with progressively sharper analyses (OSA/CSA → PHA → SSHA/SHA/O&SHA/SSAR), each potentially adding or modifying safety requirements.
- The FAA contracts out production; the systems engineer's leverage in Solution Implementation is oversight, verification, and integration (technology, business, user) rather than building.
- The lifecycle is a *closed loop*: In-Service Management's operational analysis feeds shortfalls and obsolescence signals back into service analysis, restarting the cycle before the incumbent capability fails.

## Connects To

- **NASA Systems Engineering Handbook / NPR 7123.1 (sibling packs).** The AMS phases map onto the same generic lifecycle NASA uses; FAA decision points are the civil-agency analogue of NASA Key Decision Points (KDPs). Read the SEM's phase gates against NASA's gate criteria to see the same maturity-ratchet logic in a different institutional skin.
- **DAU Systems Engineering Guidebook (sibling pack).** Both are government SE companions wrapped around an acquisition system; the SEM's Investment Analysis and ACAT designation parallel DoD milestone decisions and acquisition categories. The "evidence for an investment decision" framing is shared DNA.
- **ISO/IEC/IEEE 15288 and the SEBoK (sibling packs).** Section 2.1's explicit mapping to ISO 15288 (2008) is the door from FAA-specific language into the broader SE canon — lifecycle stages, processes, and tailoring.
- **INCOSE-grounded definitions and the System-of-Systems literature.** The SoS treatment (Maier 1998, Carlock 2001, INCOSE handbook) connects to any pack covering SoS engineering, emergent behavior, and the reassessment of assurance properties across networked systems.
- **Quality / continuous-improvement traditions (Shewhart, Deming).** PDCA links the SEM to statistical process control and modern quality management, and to any pack treating process improvement as an inner loop on engineering processes.
- **Downstream SEM chapters.** This chapter sets up Section 3 (Systems Engineering Processes — Operational Concept Development, Functional Analysis, Requirements Analysis, Architectural Design Synthesis), Section 4 (Technical Management), and Section 5 (Specialty Engineering: RMA, Lifecycle Engineering, E3/Spectrum, Human Factors, Information Security, System Safety, HazMat/Environmental) — all of which iterate across the AMS phases introduced here.
