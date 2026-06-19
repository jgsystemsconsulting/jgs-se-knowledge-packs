# Chapter 33: 6.7 Technical Assessment

## Core Idea
Technical Assessment is the formal process by which NASA programs and projects systematically review their products and progress against requirements, designs, and performance baselines at defined life-cycle gates, ensuring engineering integrity and readiness to proceed through project phases.

## Frameworks Introduced
- **Technical Review Process**: A structured forum where projects present requirements, designs, plans, and progress to management and independent assessors; serves as both technical control and decision authority input across three NASA review tracks (spaceflight per NPR 7120.5, IT per NPR 7120.7, research/technology per NPR 7120.8).
  - When to use: At established life-cycle gates and KDPs; mandatory for all programs and projects; tailored by mission type complexity (mission types 1–5) and program/project structure (single-project, uncoupled, loosely coupled, tightly coupled).

- **Earned Value Management (EVM)**: A disciplined integration of technical scope, schedule, and cost that tracks Budget Cost of Work Performed (BCWP/earned value), Budget Cost of Work Scheduled (BCWS), and Actual Cost of Work Performed (ACWP) to compute variance and performance indices at control account level.
  - When to use: Required for spaceflight and IT programs/projects (NPR 7120.5, 7120.7); applied starting Phase B; standard ANSI-EIA-748; particularly valuable for identifying cost overrun and schedule slip risk early.

- **Technical Performance Measures (TPMs)**: Tracked critical or key mission success parameters monitored throughout implementation by comparing actual achievement against anticipated values; selected for KPPs and key MOEs/MOPs.
  - When to use: TPMs should be established for each KPP and selected technical parameters that provide early warning of design maturity and stability; tracked from Phase B through SAR; assessment methods include planned-profile and margin-management approaches.

- **Measures of Effectiveness (MOEs), Measures of Performance (MOPs), Key Performance Parameters (KPPs)**: Hierarchical performance characterization from customer outcome (MOE, stakeholder viewpoint) through design delivery (MOP, supplier viewpoint) to critical thresholds that jeopardize mission success (KPP); relationship illustrated by INCOSE model.
  - When to use: MOEs established from stakeholder expectations during NGO and concept development; MOPs derived from MOEs during requirements definition; KPPs identified during Phase A and tracked throughout as minimum essential capabilities; used to validate MOE achievement and inform trade studies.

- **Configuration Audits (Functional Configuration Audit, Physical Configuration Audit)**: Systematic examination of configured products to verify functional compliance (FCA, post-requirements baseline) and physical correspondence to build-to baseline (PCA, post-CDR).
  - When to use: FCA conducted on both hardware and software after functional baseline approved; PCA precedes final assembly and shipment; both are forms of earned configuration evidence, not optional reviews.

- **Standing Review Board (SRB)**: Independent external reviewers appointed to assess program/project technical and programmatic approach, risk posture, and progress; advisory (no content authority) but provides key input to KDP decision authority.
  - When to use: Convened for spaceflight life-cycle reviews (MCR, SRR, PDR, CDR, PRR, SIR, SAR, ORR, FRR, PLAR, CERR, PFAR, DR, DRR) and other major milestones as defined by decision authority.

- **Internal Peer Reviews**: Focused, in-depth technical reviews of design approaches, trade studies, and analyses conducted by project personnel and external experts before formal life-cycle reviews; often called "tabletop" or "interim design reviews."
  - When to use: Throughout the project life cycle, particularly before major milestones; essential for establishing baseline maturity and identifying deficiencies early; should have well-defined entrance and success criteria, external peer reviewers with relevant technical background, and a roundtable format.

## Key Concepts
- **Review Entrance and Success Criteria**: Objective, measurable conditions that must be satisfied before a review can commence and after it concludes; defined in NPR 7123.1 tables (G-3 through G-18) and project/program plan; examples include requirements frozen, interface documentation complete, trade study results documented, corrective actions closed.

- **Key Decision Point (KDP)**: A scheduled gate (KDP A→B, B→C, C→D, D→E, E→F) at which the decision authority determines program/project readiness to proceed to the next life-cycle phase, informed by SRB findings, PMC review, and program/project status; outcomes include approval, conditional approval with actions, or disapproval with direction to continue current phase or redirect.

- **Schedule Variance and Cost Variance**: EVM-derived metrics comparing work accomplished (BCWP) to work scheduled (BCWS) and budgeted (BCWP) to actual cost (ACWP); when either exceeds control account thresholds, variances trigger root-cause analysis and corrective action planning.

- **Control Account Manager (CAM)**: The person responsible for a control account (typically subsystem level in WBS); develops work/product plans, schedules, time-phased budgets, and analyzes variances at that level, often a subsystem technical manager.

- **Technical Leading Indicators**: Predictive measures (mass margin, power margin, RFA/RID/action item burndown) that signal design maturity and stability by trending against time and alert zones; required by NPR 7123.1 starting after SRR through SAR.

- **Review Item Disposition (RID) / Request For Action (RFA)**: Formal mechanisms for capturing, tracking, and resolving review findings and recommendations; projects choose RID/RFA or Action Item framework early in Phase A and track burndown toward closure milestones.

- **Requirement Volatility**: Rate of newly identified or changed requirements after baseline freeze; a systems engineering process quality metric indicating whether requirements are stabilizing or destabilizing the project; tracked separately by requirement type.

## Mental Models
- **Think of MOE→MOP→TPM flow as customer outcome → supplier capability → project health signal.** An MOE ("mission can observe targets") becomes an MOP ("sensor provides 5-meter resolution") becomes a TPM ("optical surface roughness stays within ±50 nm"). Traceability breaks down when TPM selection is disconnected from the underlying stakeholder need.

- **Use SRB and internal peer review in parallel lanes:** Internal peer reviews (high detail, frequent, in-house) prepare the project; SRB reviews (external, selective, formal) validate readiness for KDP. The SRB is advisory but carries weight because it represents independent expertise and institutional confidence.

- **Visualize EVM indices as efficiency ratios.** Schedule Performance Index (BCWP÷BCWS < 1 = behind schedule) and Cost Performance Index (BCWP÷ACWP < 1 = cost overrun) are independent of spending; they measure work accomplishment per dollar and per time unit. Traditional "planned vs. actual cost" comparison is not EVM and masks true project health.

- **Margin management is forward-looking; burndown is backward-looking.** Mass and power margins are predictive (design maturity signal); RID/RFA burndown is historical (problem resolution rate). Together they show whether the design is stabilizing and problems are being closed.

## Anti-patterns
- **Conflating spending with progress.** A project can spend money without earning schedule or technical value. EVM corrects this by measuring BCWP (value earned), not just ACWP (dollars spent). Comparing planned cost to actual cost is not earned value analysis.

- **Freeze requirements too early, then let them creep.** Requirements volatility is high if baseline is set before technical feasibility is understood; it remains high if baseline is not protected post-freeze. Leading to high RID/RFA counts near major milestones signals a requirement definition problem, not a review problem.

- **Selecting too many TPMs.** Tracking requires resource allocation; oversaturation dilutes focus and increases noise. NASA recommends a small, succinct set of TPMs for each KPP and key MOEs/MOPs, tracked at program/project level, with subsystem-level visibility as needed for allocation and trending.

- **Reviewing without entrance criteria.** Reviews that begin before entrance criteria are met discover foundational gaps mid-review, extending timelines and reducing decision confidence. Entrance criteria are filters that allow early termination without board convening cost.

- **Ignoring uncertainty in decision alternatives.** A decision is robust when it reflects sufficient technical evidence and uncertainty characterization to withstand reasonable variations in key assumptions. Decisions made without documenting assumptions, uncertainties, and their effects risk being overturned when state of knowledge changes.

## Key Takeaways
1. **Technical reviews are mandatory gating mechanisms, not optional reviews.** Every NASA program and project must conduct them at defined life-cycle gates; the content and formality are tailored by mission type and program structure, but skipping or deferring reviews is policy violation.

2. **Entrance and success criteria are the operational definition of readiness.** They must be objective, measurable, and agreed by technical team, project manager, and decision authority before the review. They serve as both a filter (can we proceed?) and a scorecard (did we achieve maturity?).

3. **Independent review (SRB) and internal review (peer) are complementary, not redundant.** Internal peer reviews establish baseline maturity and resolve deficiencies early at high technical depth; SRB reviews provide independent assessment and institutional confidence for KDP decision authority. Both are essential.

4. **EVM is a unified technical-cost-schedule control system, not a financial accounting tool.** Its value lies in early detection of schedule slip and cost overrun via variance analysis and performance indices; it requires fully integrated baselines (scope, schedule, budget) to be effective.

5. **TPMs are predictive tools for design health, not just dashboard gauges.** Properly selected TPMs (tied to KPPs, tracked at multiple levels, assessed against margin/profile limits) enable corrective action before problems become costly. Poor TPM selection (too many, disconnected from requirements, not measurable) creates data without insight.

6. **Configuration audits verify contract compliance and traceability.** FCA and PCA are formal audits (not design reviews) that confirm the built product meets functional and physical baselines. They bridge the gap between approved design (CDR baseline) and ready-for-delivery product (SAR baseline).

7. **Decision authority must be clearly structured with non-overlapping scopes.** Overlapping decision-making bodies create uncertainty, conflict, and delays; clear scopes, full discipline representation, and well-documented assumptions support robust decisions. Decision analysis rigor should scale with decision complexity and uncertainty.

## Connects To
- **ISO/IEC/IEEE 15288 (Systems and software engineering—System and software engineering life cycle processes)**: NASA's review structure maps to 15288 life-cycle stages (concept, development, production, utilization, support, disposal); TPM selection and EVM planning align with 15288 requirements specification and verification/validation planning.

- **NPR 7120.5 (NASA Space Flight Program and Project Management Requirements)**: Prescribes the three technical review tracks (spaceflight, IT, R&T), life-cycle phases, KDP structure, and SRB role; section 6.7 provides guidance on executing NPR 7120.5 review requirements.

- **NPR 7123.1 (NASA Systems Engineering Requirements)**: Defines the 17 common technical processes, including Technical Assessment; specifies entrance/success criteria tables (G-3–G-18) for all required reviews; establishes leading indicator requirements (mass, power, RFA/RID/action item burndown).

- **NASA/SP-2012-599 (Earned Value Management Implementation Handbook)**: Provides detailed EVM guidance complementary to section 6.7.2.6.1; includes WBS structure, control account definition, CAM responsibilities, and variance analysis methods.

- **NPR 8705.4 (Risk Classification for NASA Payloads)**: Classifies missions by payload risk (A, B, C, D); drives tailoring of review formality and oversight; referenced in mission type definition for appropriate review roadmap selection.

- **INCOSE Systems Engineering Handbook**: The MOE/MOP/KPP/TPM relationship diagram (Figure 6.7-4) and decision analysis trade methodologies reflect INCOSE best practice; NPR 7123.1 and NASA SE Handbook Sections 6.7–6.8 operationalize INCOSE concepts for NASA context.
