# Chapter 9: 3.2 Program Implementation

## Core Idea
Program Implementation is the active governance phase in which NASA projects execute the program lifecycle across formation, approval, development, integration, operation, and disposal—monitored continuously and adjusted as resources and requirements change. It operationalizes the SE disciplines defined in earlier phases through mandatory technical activities and review gates.

## Frameworks Introduced
- **Program Implementation Technical Activities (per NPR 7120.5)**: The complete execution roadmap spanning formulation, approval, implementation, integration, operation, and decommissioning of NASA programs, with explicit entrance and success criteria tied to program reviews.
  - When to use: Every NASA project must invoke and satisfy these activities; they form the mandatory SE execution thread across the lifecycle.
  - Key INPUTS: The approved program plan from formulation (baseline technical, cost, and schedule commitments, review and governance structure, descope options), the NGO baseline, and the KDP schedule.
  - Key ACTIVITIES: Monitor project execution across all phases, convene program or phase reviews per the coupling class, assess maturity evidence at each KDP, adjust resources and requirements as risks resolve or grow, and activate descope options when trigger thresholds are hit.
  - Key OUTPUTS: Recorded gate decisions (approve, conditionally approve, disapprove), an updated program plan, descope activation decisions with stakeholder impact assessments, and lessons learned carried to follow-on programs.

- **Program/Project Reviews (PSR, PIR, and Phase Gates)**: Structured review points with defined success criteria from NPR 7123.1.
  - PSR/PIR: Used for uncoupled and loosely coupled programs only.
  - Phase reviews (synonymous with project reviews in figure 3.0-4): Used through Phase D for single-project and tightly coupled programs; these are NOT duplicative of PSR/PIR.
  - Key INPUTS: Maturity evidence for each SE product at its required state, entrance-criteria status, earned value data, and the current risk posture.
  - Key ACTIVITIES: Verify entrance criteria before convening (reviews that begin before criteria are met discover foundational gaps mid-review); present to the Standing Review Board (advisory, no content authority) and to internal peer reviews; disposition findings through RID/RFA or action items tracked to closure; record the KDP decision.
  - Key OUTPUTS: The gate decision with rationale, a RID/RFA register with burndown toward closure, conditional-approval actions assigned and tracked, and an updated risk posture.
  - Review type by program class: PSR/PIR carry the program role for uncoupled and loosely coupled programs; MCR, SRR, SDR/MDR, PDR, CDR, SIR, ORR, FRR, and DR carry it for single-project and tightly coupled programs through Phase D.
  - Entrance versus success criteria: entrance criteria gate whether the review convenes at all; success criteria score whether the maturity evidence was accepted. Both are objective, measurable, and defined in NPR 7123.1 criteria tables before the review.

## Key Concepts
- **Program Formulation**: Establishing the mission's technical, cost, and schedule feasibility early in Pre-Phase A and gathering Needs, Goals, and Objectives (NGOs) from key stakeholders.
- **Stakeholder Expectations**: The documented needs and success measures collected from customers and end-users; foundational to refining mission goals and operations concepts.
- **Descope Options**: Pre-defined mission degradation paths (e.g., fewer instruments, lower-capability technology, loss of spacecraft components) that bound success criteria if resources become constrained. Developed during NGO documentation but not baselined until needed.
- **Technical Requirements**: Top-level system and science requirements derived from mission goals, serving as the contractual baseline throughout implementation.
- **Measures of Effectiveness (MOEs)**: Quantitative and qualitative success criteria tied to stakeholder expectations and mission objectives.
- **Feasibility Assessment**: Evaluation of mission concepts across performance, cost, schedule, and technology readiness to ensure viability before committing to implementation.
- **Concept of Operations (ConOps)**: The operational profile and use-case narrative that translates stakeholder expectations into implementable system behaviors.
- **Advanced Studies**: Multi-year focused investigations addressing high-risk or high-technology development areas that may span Pre-Phase A into early Phase A.
- **Program-Level vs Project-Level Review Separation**: Program reviews (PSR/PIR) evaluate the program's performance against Agency goals, funding constraints, and cross-project integration; project phase reviews evaluate one project's SE product maturity. In single-project and tightly coupled programs the phase reviews carry the program role; running both review families on the same effort duplicates gates without adding oversight.
- **Descope Governance**: Descope options developed during formulation stay unbaselined until triggered; activation is a program-level governance decision that re-baselines success criteria and carries a stakeholder-expectation impact assessment, not a project-level scope edit.
- **EVM as the Implementation Health Signal**: Implementation monitoring compares earned value (BCWP) to scheduled (BCWS) and actual (ACWP) cost at the control account level, and variances trigger root-cause analysis. Tracking spending instead of earned value is a review-readiness failure, not evidence of progress.
- **Review Not-Ready Tells**: Entrance criteria unmet, RID/RFA count spiking near a milestone, requirement volatility still high after baseline, and spending tracked instead of earned value are the standard signals that a review should not convene.
- **Technical Leading Indicators**: Mass margin, power margin, and RID/RFA/action-item burndown are trended against alert zones from SRR through SAR; during implementation they show whether design maturity and problem closure are on track ahead of each gate.
- **Requirement Volatility**: The rate of newly identified or changed requirements after baseline freeze, tracked separately by requirement type; persistently high volatility during implementation signals unstable requirements, not a review problem.
- **Conditional Approval Mechanics**: A KDP decision authority may conditionally approve progression with assigned actions; implementation governance tracks those actions to closure before the next gate convenes.
- **Gate Preparation Discipline**: Internal peer reviews (tabletop or interim design reviews) at high technical depth prepare the maturity evidence that Standing Review Board reviews validate; projects that skip peer reviews push deficiency discovery into the formal gate, where it costs schedule.

## Mental Models
- **Think of Program Implementation as a lifecycle monitoring loop**: Continuously observe project formulation, approval, implementation, integration, operation, and disposal; at each stage, adjust resources and requirements based on risk and stakeholder feedback.
- **Use descope options as "plan B" contracts**: Rather than a failure scenario, descope options are contingency bounds that protect stakeholder expectations even if full scope is unachievable—define them upfront so no mid-program surprises occur.
- **View Pre-Phase A as the feasibility-and-stakeholder-buy-in phase**: This is where system engineers do the heavy lifting to assess multiple mission concepts, engage customers, and establish a shared vision before committing capital to implementation.
- **Treat review cadence as the program's heartbeat and entrance criteria as cheap filters**: Objective entrance criteria let a gate terminate early without convening the board, so a missed criterion is a cheap signal while the program can still react; if RID/RFA burndown and requirement volatility look unhealthy approaching a gate, the cadence itself is warning before the Standing Review Board does.

## Key Takeaways
1. **Perform all mandatory Program Implementation technical activities** (formulation, approval, implementation, integration, operation, decommissioning) as required by NPR 7120.5; omitting any creates a gap in traceability.

2. **Engage stakeholders early and document their expectations as NGOs**: The earlier you identify and align key stakeholders (including customers, users, and operators), the lower the risk of mid-program requirement churn.

3. **Develop descope options concurrently with NGO documentation**: Don't treat descope as a contingency afterthought; embed it in program planning so the team has a ready fallback if budget or schedule constraints force scope reduction.

4. **Satisfy entrance and success criteria for all program reviews**: Each review (PSR, PIR, or Phase gate) has explicit criteria from NPR 7123.1; meeting these criteria is not optional—it gates progression to the next lifecycle stage.

5. **Assess feasibility across the full lifecycle**: In Pre-Phase A, evaluate each mission concept not just for its near-term technical merit but for its implications through Operations and Disposal, including technology maturity and cost-effectiveness.

6. **Establish a clear, shared vision of the problem and solution**: Before moving from Pre-Phase A to Phase A, the team and stakeholders must agree on what problem the program solves, how the solution addresses it, and why it is feasible and cost-effective.

## Connects To
- **NPR 7120.5 (NASA Program and Project Management Requirements)**: The authoritative source for Program Implementation activities and success criteria; this handbook section operationalizes its mandate.
- **NPR 7123.1 (NASA Systems Engineering Processes and Requirements)**: Defines entrance and exit criteria for program reviews (PSR, PIR, Phase gates); linked directly to Program Implementation governance.
- **Figure 3.0-4 (Project Life Cycle Phases)**: Illustrates the relationship between Phase-A through Phase-E reviews and program review ceremonies (PSR/PIR); essential for understanding when each review type applies.
- **ISO/IEC/IEEE 15288 (Systems and Software Engineering—System and Software Engineering Services and Life Cycle Processes)**: Provides generic lifecycle process definitions that NASA's program implementation framework specializes for the government context.
- **Program Formulation (Section 3.1)**: The formulation side of the same reviews; formulation classifies the coupling that selects PSR/PIR versus phase reviews, schedules the gates, and develops the descope options that implementation governance holds ready.
- **Technical Assessment (Section 6.7)**: Supplies the EVM variance data, TPM and leading-indicator trends, RID/RFA framework, and SRB and peer-review structure that implementation monitoring consumes at each gate.
- **Technical Risk Management (Section 6.4)**: Continuous risk management between gates keeps residual risk acceptable; trigger thresholds and risk posture feed every gate decision with current evidence.
- **Decision Analysis (Section 6.8)**: Descope activation and resource rebalancing under constraint are direction-setting decisions; the six-step decision process with documented rationale structures them.
