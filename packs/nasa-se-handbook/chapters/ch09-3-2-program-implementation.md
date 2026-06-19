# Chapter 9: 3.2 Program Implementation

## Core Idea
Program Implementation is the active governance phase in which NASA projects execute the program lifecycle across formation, approval, development, integration, operation, and disposal—monitored continuously and adjusted as resources and requirements change. It operationalizes the SE disciplines defined in earlier phases through mandatory technical activities and review gates.

## Frameworks Introduced
- **Program Implementation Technical Activities (per NPR 7120.5)**: The complete execution roadmap spanning formulation, approval, implementation, integration, operation, and decommissioning of NASA programs, with explicit entrance and success criteria tied to program reviews.
  - When to use: Every NASA project must invoke and satisfy these activities; they form the mandatory SE execution thread across the lifecycle.

- **Program/Project Reviews (PSR, PIR, and Phase Gates)**: Structured review points with defined success criteria from NPR 7123.1.
  - PSR/PIR: Used for uncoupled and loosely coupled programs only.
  - Phase reviews (synonymous with project reviews in figure 3.0-4): Used through Phase D for single-project and tightly coupled programs; these are NOT duplicative of PSR/PIR.

## Key Concepts
- **Program Formulation**: Establishing the mission's technical, cost, and schedule feasibility early in Pre-Phase A and gathering Needs, Goals, and Objectives (NGOs) from key stakeholders.
- **Stakeholder Expectations**: The documented needs and success measures collected from customers and end-users; foundational to refining mission goals and operations concepts.
- **Descope Options**: Pre-defined mission degradation paths (e.g., fewer instruments, lower-capability technology, loss of spacecraft components) that bound success criteria if resources become constrained. Developed during NGO documentation but not baselined until needed.
- **Technical Requirements**: Top-level system and science requirements derived from mission goals, serving as the contractual baseline throughout implementation.
- **Measures of Effectiveness (MOEs)**: Quantitative and qualitative success criteria tied to stakeholder expectations and mission objectives.
- **Feasibility Assessment**: Evaluation of mission concepts across performance, cost, schedule, and technology readiness to ensure viability before committing to implementation.
- **Concept of Operations (ConOps)**: The operational profile and use-case narrative that translates stakeholder expectations into implementable system behaviors.
- **Advanced Studies**: Multi-year focused investigations addressing high-risk or high-technology development areas that may span Pre-Phase A into early Phase A.

## Mental Models
- **Think of Program Implementation as a lifecycle monitoring loop**: Continuously observe project formulation, approval, implementation, integration, operation, and disposal; at each stage, adjust resources and requirements based on risk and stakeholder feedback.
- **Use descope options as "plan B" contracts**: Rather than a failure scenario, descope options are contingency bounds that protect stakeholder expectations even if full scope is unachievable—define them upfront so no mid-program surprises occur.
- **View Pre-Phase A as the feasibility-and-stakeholder-buy-in phase**: This is where system engineers do the heavy lifting to assess multiple mission concepts, engage customers, and establish a shared vision before committing capital to implementation.

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
