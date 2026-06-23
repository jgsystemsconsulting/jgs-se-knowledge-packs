# Chapter — Schedule Management Planning

## Core Idea

Schedule Management Planning is the up-front discipline of deciding *how* a program or project (P/p) will run its scheduling work across the entire life cycle — before any logically-linked network of activities is ever built. It defines and documents the design, development, and deployment of every Schedule Management process, tool, reporting form, and format. The single product that captures all of this is the **Schedule Management Plan (SMP)**: an implementation plan that gives the P/p the guidance and procedures it needs to execute the Schedule Management function in line with Agency requirements. The SMP is explicitly *not* a step-by-step "how to schedule" procedure; it is a guideline for applying principles, processes, and best practices, and it should be placed under document control whether it stands alone or sits inside the broader P/p Plan.

The planning effort is front-loaded but continuous: it runs throughout the life cycle yet carries its heaviest emphasis in Phase A, because that is when mission and system definition finally becomes discrete enough to break work into real tasks and milestones. The payoff of careful SMP development is a P/p that can generate a coupled cost-and-schedule estimate, time-phase its schedule build to match how the project matures, size the resources the function will consume, and assign clear roles and responsibilities for managing the schedule.

> Edition note: This chapter is grounded in the 2024 edition of the NASA Schedule Management Handbook. Do not rely on the superseded 2010 edition (SP-2010-3403).

## Frameworks Introduced (exact source names, when/how)

- **Schedule Management Plan (SMP)** — the master planning document. Introduced as the container for all Schedule Management requirements and processes (§4, §4.3). It is decomposed into **four sub-plans**: (1) the Schedule Development Plan (with the Milestone Registry and Activity Attributes as subsections), (2) the Schedule Analysis and Assessment Plan, (3) the Schedule Maintenance and Control Plan, and (4) the Schedule Documentation and Communication Plan.
- **Schedule Management Planning Best Practices SM.P.1–SM.P.5** — the five named planning best practices in Figure 4-1: SM.P.1 *Schedule Management Plan Exists*, SM.P.2 *Scheduling Methods/Approaches are Selected*, SM.P.3 *Schedule Management Tools are Selected*, SM.P.4 *Milestone Registry is Defined*, and SM.P.5 *Activity Attributes are Defined* (§4.1).
- **Critical Path Method (CPM)** — named as the scheduling method demonstrated effective for NASA P/ps; a network-diagram technique that finds the shortest possible project duration by computing the longest path of tasks to the end date. Recommended for use "when practical" (§4.3.1.2.1).
- **Rolling Wave Planning** — a progressive-elaboration technique used alongside CPM, scheduling work in waves and adding detail as the project evolves (§4.3.1.2.1).
- **Milestone Registry** — a controlled table of all key dates and milestones with their trigger points, attached as an SMP appendix; populated at minimum with notification and control milestones, with Management Agreement (MA) and Agency Baseline Commitment (ABC) dates added at KDP B (§4.3.1.2.3, Figure 4-7).
- **Activity Attributes** — the set of data fields configured in the scheduling tool to code activities in the IMS; grouped into cost-interface, risk-management-interface, P/p-defined, and intrinsic attributes (§4.3.1.2.4).
- **Schedule Risk Analysis (SRA) / Integrated Cost and Schedule Risk Analysis (ICSRA) Model** — the analytical machinery the Analysis Plan must provision. The ICSRA Model is the cost-loaded vehicle for a Joint Confidence Level (JCL) estimate (§4.3.2.2).
- **Technical, Schedule, and Cost (TSC) Control Plan** — the NPR 7120.5-required control plan that the Maintenance and Control section of the SMP must support and stay consistent with (§4.3, §4.3.3).
- **Governing Agency documents** introduced as requirement sources: **NPR 7120.5** and **NPR 7123.1**, plus the FAD, PCA, PFA, P/p Plan, P/p Budget, and TSC Control Plan (§4.3.1.1.2). For research-and-technology (R&T) projects, **NPR 7120.8** is referenced, with the note that R&T work tied to space-flight mission success is normally managed under NPR 7120.5.

## Key Concepts

**The SMP's four sub-plans and the build-up to the IMS.** The SMP orchestrates the development, deployment, and execution of all four sub-functions. The Schedule Development Plan collects every requirement that drives construction of the Integrated Master Schedule (IMS) — tool selection, make/buy plans, the Schedule Database, the data-collection procedures that populate it, and the Schedule Outputs — the result being a working end-to-end capability that can plan the work, record how it performs, and emit the reports.

**Where IMS requirements come from.** Top-level requirements derive from four source classes (§4.3.1.1):
- *P/p requirements* — the largest source; flowing from products such as the WBS and WBS Dictionary (work packages and Performance Measurement Techniques for EVMS), the OBS, the CBS / control accounts, the Acquisition Plan, and interfaces to other PP&C functions (Resource Management, EVM, Risk Management, CM/DM).
- *Agency requirements* — driven by NPR 7120.5 and NPR 7123.1 via the FAD, PCA, PFA, P/p Plan, P/p Budget, and TSC Control Plan; these typically yield control milestones for the Registry and prescribed reporting forms. After PDR, the MA and ABC dates become mandatory Schedule Database content with required performance reporting; the annual PPBE guideline document levies scheduling requirements tied to the funding profile.
- *External requirements* — impacts that are real but not intrinsic to the P/p, arising from partnerships (e.g., an inter-agency service-module partnership), ride-along experiments, launch-vehicle or data-handling services, university-funded payloads, and national/international policy on hazardous or nuclear materials.
- *Organizational requirements* — usually resource- and process-related: personnel and facility availability, host-Center process standards (e.g., a Center's "Gold Rules" or design principles), margin guidelines, mandated reporting forums, and sometimes a standardized scheduling toolset. Multi-Center P/ps must reconcile mixed Center requirements.

**Ancillary and derivative requirements.** Beyond imposed requirements, the Schedule Management function generates its own internal requirements (§4.3.1.2): selecting scheduling methods (CPM, optionally with Rolling Wave Planning), selecting tools, building the Milestone Registry, and identifying Activity Attributes.

**Tool categories.** The source names four tool classes (§4.3.1.2.2): the *Scheduling Tool* (the integrating core of the Schedule Database — examples cited are Oracle Primavera P6 and MS Project); *Schedule Assessment Tools* (health-check add-ons such as a NASA STAT MS Project add-on, standalone tools such as Acumen Fuse, or checklists drawn from the GAO Schedule Assessment Guide); *Schedule Risk Analysis Tools* (integral packages or add-on macros — JACS, Polaris, Primavera Risk Analysis, @Risk, Full Monte — which must be selected in parallel with the scheduling tool for compatibility); and *Specialty Tools* for custom reports and performance plots (BEI, SPI, CEI, JCL/confidence-level curves, scatterplots, sensitivity and trend reports), often produced in Excel.

**Activity Attribute families.** Cost-interface attributes tie activities to cost estimates (resource name/type, uncertainty distributions); risk-management-interface attributes tie to the risk process (likelihood and impact distributions); P/p-defined attributes are special flags and references (contract names, sub-project references, sort flags); intrinsic attributes are activity-native (WBS, OBS, CBS/CAM, uncertainty distribution), many of which scheduling software supplies by default. Establishing these early also feeds the Schedule Basis of Estimate (BoE).

**Assessment vs. Analysis.** *Schedule Assessment* tests the quality and integrity of the IMS against requirements and best-practice sets, using procedures such as a Requirements Check, Health Check, Risk ID & Mapping Check, Critical/Driving Path and Structural Check, Basis Check, and Resource Integration Check (some of which depend on others passing first). *Schedule Analysis* evaluates the magnitude and significance of uncertainty and risk on projected future performance. NPR 7120.5 demands risk-informed completion-range estimates as early as MCR (met via an SRA) and a JCL estimate at KDP C (met via a cost-loaded ICSRA Model); NPR 7123.1 sets the success criterion that cost and schedule commitments be achievable at acceptable risk.

**Maintenance vs. Control.** *Maintenance* loads current performance into the IMS (typically a monthly cycle) and processes change orders through CM/DM — change orders being on-demand events such as rolling-wave detailing, PPBE-driven changes, corrective actions, and approved risk-mitigation activities. *Control* defines the performance metrics and their action thresholds. Backward-looking measures include BEI/CEI, SPI, float/margin erosion, and milestones-due-versus-completed; forward-looking measures (via SRA) include probability of on-time delivery/completion and margin sufficiency. The control content must align with the NPR 7120.5 TSC Control Plan, which carries an extensive set of leading indicators (requirement, interface, verification, review, software, problem-report, cost, schedule, staffing, and technical-performance trends) and the 30-percent ABC breach-threshold logic.

**Documentation and Communication.** This sub-plan defines when and how schedule information is recorded and disseminated, leaning on CM/DM. Items under control include the SMP, the Schedule Database (with inputs and Schedule BoE), Schedule Outputs (IMS, Summary Schedule, Analysis Schedule), assessment and SRA outputs, performance reports and baseline change requests, and lessons learned. Report forms and formats are typically specified through Data Requirements Documents (DRDs) attached as SMP appendices, with communication tailored to each audience.

## Mental Models

- **Plan-before-build.** The SMP is the blueprint that must exist before the IMS is poured. Every downstream capability — scheduling, performance capture, analysis, reporting — is only as good as the requirements collected during planning. As the source warns, retrofitting data-field assignments after the schedule tool is populated is difficult and inefficient; decisions like the scheduling method must be made *early* because they cascade into tool choice, reporting formats, and process design.

- **Requirements funnel.** Picture four inflows — P/p, Agency, External, Organizational — converging into the Schedule Development Plan, joined by the function's own ancillary/derivative requirements. Planning is fundamentally an act of collecting, reconciling, and compiling these streams before construction begins.

- **Maturity that tracks the life cycle.** SMP maturity is phase-keyed (Figure 4-3): the Schedule Development Plan portion and Milestone Registry appear in Pre-Phase A; a *preliminary* SMP completes around Phase A–SRR; full execution and an updated SMP follow at SDR/MDR; the SMP is *baselined* at PDR (Phase B); and from CDR/SIR/ORR through launch and closeout it is implemented and updated as needed. The plan should mature in lock-step with project knowledge, not ahead of it.

- **The IMS as the PP&C backbone.** Because the IMS forms the spine of EVM, the schedule must be configured and maintained so that its fields align with the EVM tool's fields for clean data transfer — Schedule Management never plans in isolation from Resource Management, EVM, Risk Management, and CM/DM.

- **Stand-alone or embedded, but always controlled.** Each sub-plan (and the SMP itself) may be a standalone document or folded into the P/p Plan; structure is flexible, but document control is not optional.

## Key Takeaways

- The deliverable of Schedule Management Planning is the **SMP**, a guidance-and-procedure plan — not a scheduling cookbook — comprising four sub-plans: Development, Assessment & Analysis, Maintenance & Control, and Documentation & Communication.
- Five named best practices anchor the function: an SMP exists (SM.P.1), scheduling methods are selected (SM.P.2), tools are selected (SM.P.3), the Milestone Registry is defined (SM.P.4), and Activity Attributes are defined (SM.P.5).
- Planning is **front-loaded into Phase A** and matures by phase, reaching a baseline at PDR; it can only begin once prerequisites (PCA/FAD concurrence, defined P/p scope, descope plan, initial risk list, WBS/Dictionary, work packages and control accounts, external milestones, interfaces, the current PPBE guideline, and assigned roles) are in place.
- **CPM is the default method when practical**, optionally combined with **Rolling Wave Planning** for progressive elaboration.
- The **Milestone Registry** captures control milestones (owned by sponsors/stakeholders, immovable by the P/p) and notification milestones (P/p-owned but requiring sponsor notification of changes), with MA and ABC dates added at KDP B.
- **Activity Attributes must be defined up front** across cost, risk, P/p-defined, and intrinsic families — both to enable EVM/SRA data transfer and to feed the Schedule BoE — because doing so after the schedule is populated is costly.
- Tool selection should follow a **requirements-first, common-toolset, make-or-buy** discipline across scheduling, assessment, SRA, and specialty/reporting tools.
- The Maintenance & Control sub-plan must **support and stay consistent with the NPR 7120.5 TSC Control Plan**, including its leading-indicator suite and ABC breach-threshold logic.
- Every sub-plan section should close by **estimating the resources and skills** needed to build and run that capability across the life cycle.

## Anti-patterns

The source names one timing-and-efficiency failure explicitly: deferring **Activity Attribute / data-field assignment** until after the scheduling tool is already populated and in service. The handbook calls this "very difficult and inefficient," using the example of scrambling to find empty fields for SRA inputs (such as MS Project software add-ons) on a schedule that is already loaded — the fix is to establish all attributes during planning. The source does not enumerate further named anti-patterns in this slice.

## Connects To

- **Schedule Development (Chapter 5).** The Schedule Development Plan is the first sub-plan; best practices for building the IMS, integrating schedule data across acquisition strategies, and aligning to EVM live there and feed back into this plan.
- **Schedule Assessment and Analysis (Chapter 6).** The Assessment & Analysis Plan provisions the checks (Health Check, Critical/Driving Path Check, etc.) and the SRA/ICSRA capability detailed in that chapter.
- **Schedule Maintenance and Control (Chapter 7).** Supplies the maintenance update cycle, control metrics, and thresholds that this plan must capture and align to the TSC Control Plan.
- **Schedule Documentation and Communication (Chapters 7–8).** Defines the DRD-driven forms, formats, and audience-tailored reporting that the Documentation & Communication Plan compiles.
- **NPR 7120.5 / NPR 7123.1 / NPR 7120.8.** The governing Agency policy that levies SMP maturity, JCL-at-KDP-C, completion-range estimates, and the TSC Control Plan, and that frames how R&T projects are managed.
- **PP&C functions.** Resource Management (budget-schedule time-phasing correlation), EVM (IMS-as-backbone and field alignment), Risk Management (risk-interface attributes, SRA inputs), and CM/DM (change orders, document control) all interface with the planning effort.
- **External guidance.** The GAO Schedule Assessment Guide is cited as a source of best-practice assessment checklists; the SCoPe website is referenced for the SMP Annotated Template, the Agency Schedule Management Tool Matrix, EVM-alignment guidance, and required skills/competencies.
