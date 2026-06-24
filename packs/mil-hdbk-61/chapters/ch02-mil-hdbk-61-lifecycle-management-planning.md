# Chapter 2: CM Life Cycle Management & Planning

> Source: MIL-HDBK-61B (current revision). This chapter draws on Section 4 of the B revision; do not substitute the superseded 2001 MIL-HDBK-61A(SE) text, whose process model and standards references are out of date.

## Core Idea
Configuration management is, at root, a non-delegable government responsibility. Authority over CM activities can be distributed to configuration managers, contractors, and oversight agencies, but the Government Program Manager remains accountable for ensuring that operating forces receive correctly configured hardware and software plus the information needed to operate and maintain the end item. That accountability holds in every acquisition phase. The rest of the chapter unpacks how a single shared CM process — common to government and contractor — is planned, related to systems engineering and logistics, and managed across the life cycle through a repeating cycle of plan, establish, manage, and improve.

## Frameworks Introduced

- **CM process implementation view (Figure 2)**: a phase-by-phase map of CM as an iterative program. It arranges the work across five strategy stages — Plan, Establish, Manage, and Improve the CM Program — over the life cycle bands of requirements/planning, development/implementation, implementation/maintenance, and maintenance/disposal. Each band lists the concrete tasks: develop the CMP and CM strategy in the planning band; onboard CM staff, stand up the allocated baseline and CCB during implementation; update the CMP, collect performance metrics, and establish the initial product baseline during maintenance; and run continuous process improvement, finalize the product baseline, and conduct the physical control audit toward disposal.
  - When to use: as the program-level reference for sequencing CM tasks; it shows which activities (baselining, training, CCB stand-up, audits) belong to which life-cycle band.

- **Top-level CM activity model (Figure 3)**: an IDEF-style reference model of the whole CM process from the government's viewpoint. Each functional activity is a box with inputs on the left, outputs on the right, constraints on top, and enabling tools/methods on the bottom. It is meant as a planning reference, not an org chart — the need to perform the activities is independent of whether the program uses IPTs or conventional functional organizations.
  - When to use: to plan and reason about the major CM functions and their interfaces before committing to any particular organizational structure.

- **Three progressive baselines — FBL, ABL, PBL**: the government takes control of configuration documentation in three stages. The Functional Baseline captures system-level performance requirements; the Allocated Baseline captures CI-level requirements; the Product Baseline (the bottom of the three technical baselines) is a snapshot of detail specifications and Technical Data Packages. The initial PBL for each hardware and software CI is normally placed under control at that CI's Critical Design Review, the system PBL is set at the system-level CDR, and the PBL is finalized and validated at the Physical Configuration Audit. The final PBL drives full-rate production.
  - When to use: whenever deciding what documentation the government will control and at which review gate; the baseline progression is the spine of configuration identification.

- **SAE EIA-649 and SAE EIA-649-1**: the industry CM standard (SAE EIA-649) states the CM principles and best practices each design activity must establish, document, and execute for its products. SAE EIA-649-1 is the vehicle the government uses to impose appropriately tailored CM requirements on contracts (see the handbook's Appendix B for tailoring guidance).
  - When to use: EIA-649 as the principle base every design activity tailors to its products; EIA-649-1 as the contractual flow-down for government-imposed, tailored requirements.

- **GEIA-HB-649 (referenced as GEIA-HB-649 / "the latest version")**: the companion handbook the standard points to for developing CM performance metrics, identifying process-improvement opportunities, and obtaining activity-guide templates.
  - When to use: when building the metrics program and looking for template support for CM activities.

- **DAG (Defense Acquisition Guidebook)**: cited as the authority describing the PBL as a snapshot of item detail specifications and TDPs at the bottom of the technical baseline stack.
  - When to use: as the supporting reference for baseline definitions in the acquisition context.

## Key Concepts

- **Responsibility cannot be delegated; authority can.** This is the chapter's governing principle. The PM, backed by configuration managers, owns the outcome regardless of how the work is parceled out.
- **One shared CM process.** The CM process described is common to both the government and its contractors; the planning activity decides how the functional activities are allocated between them, not whether each side runs a separate process.
- **Class I vs. Class II change control.** The government controls baselines by approving Class I (major) changes through its CCB and concurring in Class II (minor) changes, which are typically adjudicated by DCMA representatives. By holding the baselines, the government blocks changes that are not beneficial, unsupportable, or too costly.
- **The five core CM functional activities.** Management and planning is the central government activity; the other four it coordinates are configuration identification (the foundation for all the rest), configuration control, configuration status accounting (CSA), and configuration verification and audit (FCA and PCA).
- **Configuration identification is foundational.** It produces approved configuration documentation, establishes the baselines for both government and contractor control, creates the CSA database records, and supplies the product/document identifiers (nomenclature and numbering). Data management — version/revision control, electronic access, and distribution — is implicitly tied to it even though Figure 3 does not draw it as a separate box.
- **CSA is a by-product.** Status accounting data accumulates automatically as the other CM functions run their transactions. The CSA database can hold as-designed, as-built, as-delivered, and as-modified configurations of any serial-numbered unit or replaceable component, plus change status, change history, and audit schedules and action-item status. Metrics are generated from this database and fed back to management and planning.
- **Verification and audit closes the loop.** FCA and PCA confirm that performance requirements were met by the design and that the design was accurately documented; successful completion yields a verified product/documentation set that can confidently be treated as the PBL, plus a validated process. Verification should be embedded in the contractor's own create/modify process, and government process validation may substitute for physical inspection.
- **Maintenance plan drives the level of government configuration control.** Wherever the maintenance concept stops calling for replacement — the deepest indenture level at which the government must stock spares — is the same depth to which the government has to keep configuration under its control. Logistics coordination, especially maintenance planning, is therefore essential to CM planning.
- **Metrics are more than measurements.** A metric comprises an operational definition (what, why, when, where, how — and when to retire it), the actual data collection (often a query against the CSA database), and a reduction into a presentation format (run chart, control chart, cause-and-effect diagram, Pareto chart, histogram) that surfaces the root cause or biggest constraint. Effective metrics are meaningful to customers, tied to organizational goals, timely/simple/repeatable/economical, and trend-revealing.
- **DCMA as a full team member.** Because DCMA provides contract administration and interfaces most directly with the contractor on performance measurement, it should participate as a full team member, ideally on a common set of agreed objectives.
- **"Preparing for the next phase."** During each phase, CM tasking for the following phase is developed — e.g., EMD-phase CM tasking is worked during the TMRR phase. CM planning means setting the CM concept of operation and acquisition strategy for the coming phase and revising the CM Plan to match, while looking ahead to capture information future phases will need.
- **RFP as a CM lever.** The RFP must align with the government's CM plan yet stay flexible enough to accept varied contractor responses. It signals that the government is serious about CM, and Section L proposal evaluation criteria should treat CM as a key management and past-performance discriminator, weighted to reflect how much a documented contractor CM process mitigates risk.

## Mental Models

- **"The PM owns the configuration, no matter who does the work."** Delegating tasks never transfers the accountability — a useful test when deciding how much hands-on control the government configuration manager must retain.
- **"Baselines are progressive locks: FBL → ABL → PBL."** Each review gate (CDR for the initial PBL, PCA for the final PBL) snaps another layer of documentation under government control, and once locked, change only happens through the CCB.
- **"Identification is the foundation; everything else builds on it."** If the configuration documentation, identifiers, and baseline records are wrong, control, status accounting, and audit all inherit the error.
- **"Status accounting is exhaust, not extra work."** Because CSA data is a by-product of normal CM transactions, the database is the natural single source for both visibility and metrics — query it rather than re-instrumenting the process.
- **"Maintenance concept sets the depth of control."** Decide how deep into the system the government will stock spares, and you have decided how deep the government must control configuration.
- **"Metrics point forward, not backward."** Use only a few critical metrics, design them to motivate rather than keep score, and orient them toward where the program is going.
- **"CM is cross-functional by nature."** No important CM function happens without interaction with systems engineering, design, logistics, and contracting — so CM objectives must be measured against overall program objectives, not CM efficiency in isolation.

## Anti-patterns

- **Contract restrictions that constrain CM.** The handbook states that when contract provisions limit either government or contractor CM, it generally signals ineffective planning and coordination of requirements, or a failure to win management approval for the needed contract language. Constrained CM is treated as a planning failure, not an external accident.
- **Measuring CM efficiency for its own sake.** The text warns that it is not the efficiency of CM activities per se that adds value, but their contribution to overall program objectives — so divorcing CM objectives and measurements from the interacting engineering, logistics, and contracting processes is the wrong move.
- **Score-keeping metrics.** Metrics built to keep score or to merely compile past history are called out as the wrong design; metrics should positively motivate and stay forward-focused.

## Key Takeaways

1. CM responsibility rests with the government PM and is non-delegable across every acquisition phase, even though the authority to do the work is distributed.
2. The government assumes control of configuration documentation through three progressive technical baselines — FBL, then ABL, then PBL — with the initial PBL set at CDR and the final PBL validated at PCA.
3. Baseline control runs on Class I (CCB-approved) and Class II (DCMA-adjudicated, government-concurrence) change handling, letting the government block changes that are not beneficial, supportable, or affordable.
4. The CM process is a single process shared by government and contractor; the management-and-planning activity decides how the functional activities are allocated and produces the documented process plus the SOW/RFP language.
5. Configuration identification is the foundation for every other CM activity; CSA accumulates as a by-product and is the source of both visibility and metrics.
6. CM is embedded in systems engineering — SE produces the technical information (requirements, drawings, data sets) for which CM provides technical control, and SE is re-exercised whenever CM generates a change.
7. The maintenance concept and the government's spares-stocking decision determine the lowest indenture level at which the government must exercise configuration control.
8. Plan the next phase during the current one: develop CM tasking, answer the roles-and-responsibilities question set (CIs, baselines, identifiers, status accounting, CDCA), revise the CM Plan, and shape the RFP and Section L criteria accordingly.
9. Build the metrics program around a few critical, forward-focused metrics with operational definitions, CSA-sourced data, and clear presentation formats; reference GEIA-HB-649 for templates and improvement guidance.
10. Tailor CM requirements onto contracts via SAE EIA-649-1 (with EIA-649 as the principle base), using the handbook's Appendix B tailoring guidance.

## Connects To

- **Systems engineering process (Figure 4 in the source)**: CM provides technical control over the information that systems engineering produces. As the SE requirements loop and design loop iterate, performance specifications form the FBL and CI ABLs, and released drawings/data sets become the PBL after verification and audit; every CM-generated change re-invokes SE to define its technical basis.
- **Logistics / maintenance planning (Figure 5 in the source)**: maintenance planning begins before EMD inside the IPTs and iterates across the life cycle; the maintenance plan drives the level of government configuration control and the support mix between government organic support and OEM support, and it shapes the information needed to fully document an engineering change.
- **Configuration identification, control, status accounting, and audit chapters**: this chapter is the management-and-planning hub that coordinates the four other CM functional activities; the detailed mechanics of each live in their own chapters.
- **SAE EIA-649 / EIA-649-1 and GEIA-HB-649**: the industry-standard principle base, the contractual tailoring vehicle, and the metrics/templates companion referenced throughout this section.
- **DCMA and DoD acquisition phasing (TMRR, EMD, full-rate production)**: DCMA participates as a full team member on Class II changes and performance metrics; CM tasking for each phase is prepared in the preceding phase.
