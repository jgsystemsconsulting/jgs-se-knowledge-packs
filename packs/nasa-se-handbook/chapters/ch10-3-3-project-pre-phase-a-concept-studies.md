# Chapter 10: 3.3 Project Pre-Phase A: Concept Studies

## Core Idea
Pre-Phase A is the entry gate where a concept is tested for feasibility and technical credibility before advancing to formal Phase A development; it establishes whether the proposed mission aligns with NASA's strategic plans, resources, and risk appetite through concept maturation, trade studies, and proposal documentation.

## Frameworks Introduced
- **Concept of Operations (ConOps)**: A narrative description of how the program's outcomes will cost-effectively satisfy mission objectives.
  - When to use: At concept entry to establish stakeholder alignment and operational context before detailed technical work.
  - Key INPUTS: Stakeholder expectations, Needs/Goals/Objectives, MOEs, design drivers, and constraints captured during concept elicitation.
  - Key ACTIVITIES: Write the narrative of how the system operates in its environment: roles, staffing, timelines, nominal AND off-nominal/contingency scenarios, critical events, and a Design Reference Mission.
  - Key OUTPUTS: A ConOps document consumed at MCR as the feasibility narrative, then carried into Phase A as the source from which functional and performance requirements are derived and against which validation is planned.

- **Analysis of Alternatives (AoA)**: Systematic evaluation of competing mission/system architectures and approaches.
  - When to use: To select the most cost-effective architecture early, before design commitment.
  - Key INPUTS: Candidate mission and system architectures, evaluation criteria split into primary factors (distinguish alternatives) and secondary factors (refine within one), and MOE/MOP/cost data per alternative.
  - Key ACTIVITIES: Frame the decision, build a trade tree, generate and screen alternatives, evaluate against criteria with measures converted to a common scale (e.g., 1-3-9), assess robustness under uncertainty, and recommend with documented rationale.
  - Key OUTPUTS: A selected architecture with archived trade rationale consumed at MCR to justify cost-effectiveness, and a bounded alternative space that Phase A refines rather than reopens.

- **Preliminary SEMP (Systems Engineering Management Plan)**: Outline of how NASA SE requirements and NPR 7123.1 practices will be applied throughout the lifecycle.
  - When to use: To document governance and process commitments before Phase A formality.
  - Key INPUTS: The NPR 7123.1 process set, program constraints, the project risk classification, and tailoring rationale.
  - Key ACTIVITIES: Outline how SE processes, reviews, technical planning, and control disciplines will be applied; record each NPR requirement's disposition with rationale.
  - Key OUTPUTS: A SEMP outline consumed at MCR as governance evidence and baselined in Phase A; the dispositions recorded here seed the Compliance Matrix.

- **Technology Development Plan**: Strategy for assessing, developing, and maturing technologies required by the mission.
  - When to use: When mission success depends on unproven or immature technologies.
  - Key INPUTS: The technologies the concept depends on, their current maturity, and the mission-critical functions they must support.
  - Key ACTIVITIES: Assess each required technology's maturity, define development or maturation efforts, and identify which must be proven before Phase A or B commitment; high-risk areas may run as advanced studies spanning into early Phase A.
  - Key OUTPUTS: A plan consumed at MCR to show every immature technology has a credible maturation path, feeding advanced studies and Phase A technology development.

## Key Concepts
- **Mission Justification**: The business and strategic case for the proposed project, clearly articulated in proposal documentation.
- **Concept Maturity**: The level of engineering detail and credibility achieved before formal phase entry; includes preliminary designs, cost estimates, and risk identification.
- **Work Breakdown Structure (WBS)**: A hierarchical decomposition of project scope used to allocate cost, schedule, and technical responsibility.
- **Risk Classification and Technical Risk**: Systematic identification of mission, programmatic, and technical risks early to inform feasibility judgments.
- **Preliminary Verification and Validation (V&V) Approach**: A plan outlining how the mission concept will be tested and validated before commitment.
- **Rough Order of Magnitude (ROM) Cost and Schedule Estimates**: High-level, preliminary life-cycle cost and schedule projections to support resource planning.
- **Roles and Responsibilities**: Definition of technical team, flight crew, and ground crew assignments, including training implications.
- **MCR (Mission Concept Review) Entrance/Success Criteria**: Gate criteria from NPR 7123.1 that Pre-Phase A activities must satisfy for phase advancement.
- **No Entry Gate, One Review**: Pre-Phase A is entered without a KDP; MCR is the review that assesses mission feasibility and alignment with NASA strategic goals, and its maturity evidence feeds the KDP A decision that authorizes Phase A.
- **NGO Capture During Concept Studies**: Needs, Goals, and Objectives are collected from stakeholders during Pre-Phase A alongside the ConOps; they anchor the later bidirectional traceability from objectives down to requirements.
- **Concept Maturity as Evidence, Not Confidence**: Maturity is demonstrated by artifacts (preliminary design, ROM cost and schedule, risk register, V&V approach) so MCR entrance criteria can check them objectively; a concept that feels ready but lacks the artifacts is not ready.
- **Feasibility-Filter Cost Asymmetry**: Concept-phase decisions lock in most downstream cost, so screening out a weak concept at MCR is the cheapest rejection the lifecycle offers; the same concept rejected after PDR carries sunk design, fabrication, and schedule.
- **ROM Estimates Bound the Business Case**: Rough-order-of-magnitude life-cycle cost and schedule projections support early resource planning ahead of MCR; they are deliberately coarse, and Phase A refines them into the formal cost and schedule baselines.
- **Alignment With NASA Strategic Goals**: Feasibility is necessary but not sufficient; MCR also weighs alignment with NASA strategic goals, resources, and risk appetite, so an affordable, buildable concept can still be rejected as off-strategy.

## Mental Models
- **Think of Pre-Phase A as a feasibility filter**: It answers "Is this mission worth pursuing?" before NASA commits budget and formal oversight.
- **Use AoA early and often**: Trade studies should precede — not follow — system design decisions; at concept entry, this means comparing competing architectures, not refining a single baseline.
- **ConOps is the contract between mission need and engineering solution**: It ensures stakeholders and the engineering team share a common picture of how the system will operate.
- **Sharpen the AoA rule with factor discipline**: Primary factors define what makes alternatives genuinely distinct (whole architectures, not instrument swaps within one favored design); secondary factors only refine within an alternative. Mixing the two bloats the option set and hides the real trade.

## Key Takeaways
1. **Concept maturation is the primary goal**: Pre-Phase A produces a ConOps, preliminary architecture, ROM cost/schedule, and risk characterization credible enough to justify Phase A entry.
2. **Trade studies and AoA drive early architecture selection**: Systematically evaluate alternatives for cost-effectiveness before allocating functions to hardware, software, or human elements.
3. **Risk and technology readiness shape feasibility**: Identify technical risks, classify them, and assess technology maturity to expose showstoppers before formal commitment.
4. **Planning documents set Phase A boundaries**: A preliminary SEMP, V&V strategy, and technology development plan document how SE governance will operate downstream.
5. **MCR entrance criteria are non-negotiable gates**: Pre-Phase A deliverables must satisfy NASA's NPR 7123.1 MCR success criteria; informal proposal review may precede the formal MCR.
6. **Role and responsibility clarity prevents integration failure**: Explicitly define who does what across technical teams, flight operations, and ground support — including training needs — to avoid downstream coordination gaps.

## Connects To
- **NPR 7123.1 (Program and Project Management Requirements)**: Defines MCR entrance/success criteria and the formal review structure for Pre-Phase A gate decisions.
- **ISO/IEC/IEEE 15288 (Systems and Software Engineering — System and Software Engineering Processes)**: Aligns Pre-Phase A concept studies with the concept-phase processes in the system lifecycle model.
- **Phase A (Concept and Technology Development)**: Pre-Phase A outputs (ConOps, preliminary requirements, WBS, risk register) serve as Phase A inputs and are refined with greater formality and depth.
- **Stakeholder Expectations Definition (Section 4.1)**: The elicitation machinery behind Pre-Phase A; NGOs, MOEs, constraints, and the ConOps narrative are that process's products, consumed here as MCR evidence.
- **Cost-Effectiveness Considerations (Section 2.5)**: AoA selection applies cost-effectiveness discipline early, where most downstream cost locks in; alternatives compare against the envelope curve, not build cost alone.
- **Decision Analysis (Section 6.8)**: The AoA and trade work runs on the six-step decision process, with method depth scaled to decision stakes and rationale documented.
