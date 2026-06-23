# Chapter — Production and Deployment (P&D) Phase

*Source: the DoD M&Q BoK (Manufacturing and Quality Engineering Body of Knowledge), Chapter 5 — v3.0, dated July 2025 — from OUSD(R&E)'s office for Systems Engineering and Architecture (within Research and Engineering). Approved for public release; DOPSR Case # 25-T-2448. This chapter synthesizes the P&D slice (roughly pp. 5-1 to 5-270); the BoK as a whole is large (~1,658 pp) and is intended to be consulted by phase rather than read straight through.*

## Core Idea

The Production and Deployment (P&D) phase is where a system that satisfies an operational capability is actually produced and fielded to the end user. It begins after a successful Milestone C review and the close of Engineering and Manufacturing Development (EMD), and it contains two distinct production efforts: Low-Rate Initial Production (LRIP) and Full-Rate Production and Deployment (FRP&D). The source treats the commitment to enter production as expensive and hard to unwind, so it frames the central engineering job as proving — before scaling up — that the design is stable, technologies are matured, and manufacturing processes are capable, stable, and under control.

The BoK organizes all of P&D around the manufacturing-and-quality (M&Q) practitioner's vantage point inside a Major Capability Acquisition (MCA) program. Three M&Q roles recur throughout the phase: influencing the design for producibility, preparing for production through planning, and executing the manufacturing and quality-assurance plans. M&Q personnel are positioned as supporters and analysts on the technical Integrated Product Team (IPT) — they do not sign contracts or own milestone authority, but they feed evidence, risk findings, and metrics into the documents and reviews that the Program Management Office (PMO) and Milestone Decision Authority depend on. A stated Program Manager priority is to reduce manufacturing risk and demonstrate producibility before committing to Full-Rate Production.

## Frameworks Introduced

The chapter is itself structured as twelve "threads" (lettered A through L), each a topic area drawn from the "5 Ms" (Manpower, Machines, Materials, Methods, Measurement), from Manufacturing Readiness Level criteria, and from DoD-unique functions not found in commercial industry. The threads, by letter: **A** the DoD Acquisition System, **B** Defense Contracting, and **C** Surveillance (the DoD-unique trio); then **D** Technology and the Industrial Base, **E** Design, **F** Cost and Funding, and **G** Materials Management; and finally **H** Process Capability/Control, **I** Quality Management, **J** the Manufacturing Workforce, **K** Facilities, and **L** Manufacturing Management/Control. Within each one the BoK lists its Activities, the Tasks that M&Q staff lead or support, and the available Tools and Resources.

Named frameworks, standards, and methods the slice introduces and tells you when and how to apply:

- **Adaptive Acquisition Framework (AAF) / DoDI 5000.02.** The governing acquisition policy. The BoK documents the Major Capability Acquisition path in detail but states the practices are tailorable to the other AAF pathways (Urgent Capability Acquisition, Middle Tier of Acquisition, etc.). Used as the backbone that places every P&D activity in its milestone context.

- **Manufacturing Readiness Levels (MRLs) and Manufacturing Readiness Assessments (MRAs).** The primary maturity gauge for production risk. The source ties specific MRL targets to phase events: an MRA at MRL 9 is conducted during LRIP to confirm low-rate maturity, and MRL 10 criteria are used to assess Full-Rate Production maturity. (Note: the slice is internally inconsistent — one passage names MRL 9 as the FRP-decision target while another names MRL 10 for FRP — but the consistent intent is that the higher MRL bands gate the production decisions.) The Interactive MRL Users Guide and MRL Deskbook are the working tools, sourced from dodmrl.org.

- **AS6500, Manufacturing Management Program.** Identified as the industry best practice for manufacturing management; the BoK recommends reviewing its requirements even when it is not contractually invoked, and points to MIL-HDBK-896, Manufacturing Management Program Guide, for how to implement AS6500 on DoD programs. AS6500 also supplies the working definitions of critical characteristic and critical manufacturing process.

- **AS9100 and ISO 9001, Quality Management Systems.** The quality-system standards used to assess and structure the contractor's Quality Management System (QMS). The slice walks through the ISO 9001 / AS9100 clause structure (leadership, planning, support, operation, control of externally provided processes, production and service provision, control of nonconforming outputs, performance evaluation, and continual improvement).

- **AS9103, Variation Management of Key Characteristics**, and the broader AS91xx family (AS9102 First Article Inspection, AS9133, AS9134 supply-chain guidelines, AS9136 root-cause analysis, AS9138 statistical process acceptance, AS9145 APQP/PPAP). AS9103 is named as the best practice for identifying and controlling Key Characteristics and requires the producer to document KCs and control the manufacturing processes that drive their variation.

- **Advanced Product Quality Planning (APQP) / AS9145.** A structured five-step approach to designing the product and its process: first plan and define; then develop the product design; then develop the process design; then validate product and process together; and finally capture production feedback.

- **DoD Risk, Issue, and Opportunity (RIO) Management Guide.** Supplies the five-step risk process the BoK reuses for manufacturing risk: Risk Planning, Risk Identification, Risk Analysis (likelihood × consequence), Risk Mitigation (accept, avoid, transfer, or control), and Risk Monitoring.

- **Independent Technical Risk Assessment (ITRA).** Mandated by 10 U.S.C. §2448b for Major Defense Acquisition Programs prior to Milestones A, B, and C and before the FRP decision. The slice stresses that an ITRA leverages ongoing work (TRAs, MRAs, technical reviews) but renders an *independent* judgment — so its conclusions may not track the raw readiness-level numbers.

- **DCMA Manufacturing Systems Risk Assessment** and its checklists, drawn from DCMA Instruction 204. These define mandatory surveillance areas at resident contractor offices: Production Planning and Control (with its sub-elements Demand Management, Resource Requirements Planning, Aggregate Planning, Rough Cut Capacity Planning, Material Requirements Planning, Capacity Requirements Planning, and Shop Floor Controls); Work Measurement; Producibility; and the Defense Priorities and Allocation System.

- **DoD Digital Engineering Strategy / digital thread / Product Lifecycle Management (PLM).** Introduced as the means of using integrated digital models and curated data across the life cycle, and used to run process-capability studies, optimize designs and cost models, and feed cost assessments.

- **DoD Systems Engineering process model (Table 5-1).** Sixteen processes — eight technical management processes (Technical Planning, Decision Analysis, Technical Assessment, Requirements Management, Risk Management, Configuration Management, Technical Data Management, Interface Management) and eight technical processes (Stakeholder Requirements Definition, Requirements Analysis, Architecture Design, Implementation, Integration, Verification, Validation, Transition) — that M&Q personnel support.

## Key Concepts

**LRIP vs. FRP as a two-gate proving sequence.** LRIP is described as up to roughly 10 percent of the estimated production volume and is the step that moves articles beyond the EMD pilot-line environment into a genuine low-rate production environment. The exit conditions the source lists for LRIP include: minimal remaining system changes, stable and test-proven major design features, materials available to meet rate schedules, process capability adequate to hold design Key Characteristics, ongoing production-risk monitoring, met LRIP cost targets, and learning curves analyzed against actual data with a cost model built for the FRP environment. FRP&D then scales to authorized rate, and the FRP decision verifies there are no significant manufacturing risks, that industrial capacity exists, that critical processes are affordable and executable, that suppliers are qualified, and that the relevant processes are under statistical process control.

**Manufacturing readiness considerations at Milestone C and the FRP decision.** The recurring checklist of production-risk dimensions: industrial base viability, design stability, process (and change) control and maturity, supply-chain stability and management, quality management through the supply chain, facilities and tooling availability and capability, and manufacturing-skills availability. The PMO is expected to update the Acquisition Strategy and surface remaining risks before the FRP decision, drawing on PRRs, MRAs, ICAs, ITRAs, and Program Status Reviews, plus pre-award surveys and trade studies, the tooling and make-or-buy plans, the manufacturing plans, and the bills of material.

**Key, Critical, and Significant Characteristics and Critical Manufacturing Processes (CMPs).** A characteristic is a measurable feature defined by design data. Per AS9100, a Key Characteristic is a selected feature whose variation must be controlled to meet customer requirements; AS6500 defines a critical characteristic as one whose defect would create or increase a hazard to human safety or cause functional failure; significant characteristics are those whose variation could affect fit, function, durability, satisfaction, or manufacturability. A critical manufacturing process is one that creates or affects a key or critical characteristic. The BoK links KC identification to the Pareto principle — a small number of features drive most of the performance impact — and sets a process-capability target of Cpk ≥ 1.33 (or as the customer specifies). KCs flow down to subcontractors, and both contractor and program office must hold a top-level understanding of them.

**The Statement of Work and the production-phase requirement set.** The source enumerates the M&Q items that belong in the production SOW: manufacturing management systems, work measurement, manufacturing data and plan updates, initial production facilities, production/material control systems, manufacturing reporting (notably line of balance), control of subcontractors and vendors, make-or-buy programs, government-furnished property, system audit, technical data, and competition. It notes that incentives and multiyear contracting can be used to motivate cost and performance.

**The contractual data deliverables (CDRLs/DIDs).** Update Program Documentation (Activity A.2) lists the specific Data Item Descriptions M&Q personnel request, including the Integrated Program Management Report (DI-MGMT-81861); the Manufacturing Plan, whose DID is DI-MGMT-81889A; the Manufacturing Risk Assessment Report, DID DI-SESS-81974; a Critical Manufacturing Process Description; the Production Line of Balance Status; a Progress Curve Report (DD Form 1921-2); and the suite of Quality Program/QMS/QAP descriptions. This is the BoK's mechanism for turning oversight intent into enforceable contract artifacts.

**The Surveillance System and DCMA's role.** Thread C details how the Defense Contract Management Agency performs Contract Administration Service functions at industry sites — monitoring FMECA/Critical Items List requirements, system safety (Safety Assessment Reports, MIL-STD-882), test and evaluation, Physical and Functional Configuration Audits, FRACAS, and parts-management compliance — and feeds Manufacturing and Quality System, Program/Product, Continuous-Improvement, and Supply-Chain analyses back to the program office.

**Modeling, Simulation, and process capability.** Thread H positions M&S as a way to virtually test production, assembly, inventory, and transportation methods before committing to tooling or capacity, reducing physical-test cost and scrap/rework. AS6500 requires analyzing manufacturing processes with M&S to find bottlenecks, validate cycle times, and plan resources. The thread feeds into yield enhancement, variability reduction, and demonstration of critical processes in LRIP and FRP.

**Workforce planning as a quantitative discipline.** Thread J frames workforce planning as a supply/demand/gap analysis — Strategic Direction, Demand Analysis, Supply Analysis, Gap Analysis, and Solution Identification — using tools such as Manufacturing Resource Planning (MRP II), bottleneck (Theory of Constraints) analysis, learning-curve estimation, and line-of-balance templates, with explicit attention to retirement, hard-to-fill skills, and digital-engineering and cybersecurity competency gaps.

**Industrial base, ManTech, and supply-chain resilience.** Thread D and the materials/management threads stress assessing and managing industrial-base risk, maturing high-risk processes through Manufacturing Technology (ManTech) and Title III projects, maintaining a Critical Capabilities List / watch-list of critical items and sources, and managing Diminishing Manufacturing Sources and Material Shortages (DMSMS), counterfeit-part avoidance, obsolescence, and sole/single/foreign/fragile sourcing risk.

**Industrial cybersecurity.** Treated as a first-class production risk: conformance to DFARS 252.204-7012 (which covers the safeguarding of covered defense information, plus reporting of cyber incidents), to NIST 800-171 (Controlled Unclassified Information), and to NIST 800-82 (security for Industrial Control Systems), extended down through the supply chain and into manufacturing information systems and industrial operations.

## Mental Models

- **Production commitment is a one-way door.** The BoK's framing — entering production is expensive and difficult to reverse — means the engineering posture is to gather enough test, maturity, and risk evidence *before* the gate that the decision is defensible rather than hopeful.

- **The 5 Ms as a checklist for a "complete" manufacturing environment.** Manpower, Machines, Methods, Materials, and Measurement (plus components, work instructions, and tooling) define what it means to have demonstrated a process in a representative environment. A demonstration that omits any of these is not a real demonstration.

- **Readiness as a number, judgment as a separate thing.** MRLs and TRLs give defensible scales, but the ITRA exists precisely because an independent team may reach different conclusions than the readiness numbers suggest. Treat the level as evidence, not as the verdict.

- **No plan means no program.** The source states bluntly that without a detailed manufacturing plan there can be no effective monitoring, assessing, scheduling, review, or testing — in effect, no production program at all. Planning is the precondition for oversight, not paperwork after the fact.

- **Variation is the enemy of performance.** Products perform better with less variation on key and critical characteristics; the whole KC/Cpk/SPC apparatus exists to find the vital few features and hold them.

- **M&Q influences, it does not command.** Because M&Q staff supply inputs to documents and reviews owned by others, their leverage comes from being embedded early on the IPT and from translating manufacturing reality into the contractual and review artifacts decision-makers act on.

## Anti-patterns

The source names several recurring P&D failure modes:

- **Deferring the manufacturing plan past EMD.** When no formal manufacturing plan is built during EMD, the BoK warns that production opens with — and keeps suffering — needless cost growth and schedule churn.

- **The "identical facility" and "same-site" fallacies.** The M&S discussion explicitly cautions against two false assumptions: that identical production facilities will experience identical problems, and that a line that ran smoothly in one location will run smoothly after a move — variability from disassembly, relocation, and reassembly will occur even with the same workforce.

- **The production-risk list itself.** The phase introduction lists conditions to guard against: requirements that keep moving under a flood of engineering changes; production rates and quantities that will not settle; too little process proofing; too little material characterization; late swaps of proven materials, processes, subcontractors, vendors, or components; producibility never considered; configuration management and subcontractor management left weak; and gaps in special tooling and test equipment — and stresses these can originate early, not just at production.

## Key Takeaways

- P&D produces and fields the system through two gated efforts — LRIP (≈10% of volume, proving the move beyond the pilot line) and FRP&D (scaling to authorized rate) — with Milestone C and the FRP decision as the controlling gates.
- The chapter is organized as twelve M&Q threads (A–L) spanning acquisition, contracting, surveillance, industrial base, design, cost, materials, process control, quality, workforce, facilities, and manufacturing management.
- Manufacturing maturity is judged with MRL/MRA criteria (MRL 9 in LRIP; the higher MRL bands at the FRP decision), and overall technical risk is independently judged by the statutorily required ITRA.
- The core standards are AS6500 (manufacturing management, implemented via MIL-HDBK-896), AS9100/ISO 9001 (quality systems), and AS9103/AS9145 (Key Characteristic variation control and APQP/PPAP).
- Key Characteristics, critical characteristics, and critical manufacturing processes are the spine of quality control; the goal is to hold the vital few features (Pareto) under statistical process control at Cpk ≥ 1.33.
- M&Q leverage is exercised through documents and reviews — Acquisition Strategy, SEP (with Manufacturing and Quality Plans), TEMP, IMP/IMS, LCSP, RFP/SSP — and through the CDRL/DID data deliverables that make oversight enforceable.
- DCMA surveillance, ManTech/Title III investment, DMSMS and counterfeit-part management, and industrial cybersecurity (DFARS 252.204-7012, NIST 800-171/800-82) round out the production-risk picture.

## Connects To

- **DAU Systems Engineering Guidebook / Engineering of Defense Systems Guidebook (DoDI 5000.88).** The sixteen-process SE model in Table 5-1 and the technical-review/audit structure (PDR, CDR, PRR, FCA, PCA) are shared with these references; this chapter is the manufacturing-and-quality view of those same processes during production.
- **GAO Technology Readiness Assessment Guide (GAO-20-48G) and the DoD TRA Guide.** The MRL apparatus here is the manufacturing analog of technology-readiness assessment, and the BoK explicitly pairs MRAs with TRAs as inputs to the ITRA and the FRP decision.
- **DoD Digital Engineering Strategy / Digital Engineering Body of Knowledge.** Thread E and Thread H lean on the digital thread, model-based definition (ASME Y14.41, MIL-STD-31000B technical data packages, MIL-HDBK-539), and PLM — connecting P&D to the broader digital-engineering packs.
- **DoD RIO Management Guide.** The five-step risk process reused for manufacturing risk in Thread L is the same management framework used program-wide.
- **NIST 800-171 and 800-82.** The industrial-cybersecurity requirements tie P&D into the controlled-unclassified-information and industrial-control-systems security guidance carried in the NIST-aligned packs.
- **Adjacent M&Q BoK chapters.** As one of six life-cycle chapters (Pre-MDD, MSA, TMRR, EMD, P&D, O&S), this chapter inherits planning and risk artifacts matured in EMD and hands the fielded system, with its Life Cycle Sustainment Plan, into Operations and Support.
