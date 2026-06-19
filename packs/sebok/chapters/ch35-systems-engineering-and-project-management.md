# Chapter 35: Systems Engineering and Project Management

## Core Idea
Systems engineering operates horizontally across project and program management, ensuring technical integration and traceability; while portfolio management operates at the enterprise level to select "right" projects aligned with strategy. Together, these three disciplines form a nested governance structure: portfolio management chooses *what* projects to fund, project management executes them "right," and systems engineering ensures technical solutions are architecturally sound and cost-effective.

## Frameworks Introduced

- **Acquisition Process Model**: A phased lifecycle for procuring complex systems (technology maturation → engineering development → production → field support), allowing systems to enter at any phase depending on technology readiness.
  - When to use: Major systems acquisition in government or defense; tailors phases based on technology novelty and risk.

- **Portfolio Management Process Implementation**: A six-domain lifecycle (qualification/prioritization → identification → resource allocation → responsibility definition → sustainment → redirection/closure) producing seven major outcomes: opportunity qualification, project identification, budget allocation, accountability structures, requirement sustainment, unsatisfactory project termination, and successful closure.
  - When to use: Enterprise-level decision making to balance competing projects against organizational strategy and capacity.

- **Six Performance Management Domains for Portfolio**: Portfolio Strategic Management, Portfolio Governance, Portfolio Capacity and Capability Management, Portfolio Stakeholder Engagement, Portfolio Value Management, and Portfolio Risk Management.
  - When to use: Structuring portfolio management processes; each domain addresses a different critical success factor.

- **Vertical vs. Horizontal Role Distinction (SE/SwE)**: In complex systems, SE has a horizontal integrating role; traditional engineering disciplines (electrical, mechanical, software) have vertical domain-specific roles. Both types contribute to cross-cutting concerns.
  - When to use: Organizing team responsibilities in multi-discipline projects; clarifies SE's integrating mandate versus specialist expertise.

- **Three Cost Estimating Methodologies**: Analogical (uses historical analogy), Parametric (uses statistical relationships between cost drivers), and Build-Up (detailed bottom-up enumeration of cost elements).
  - When to use: Select based on program lifecycle phase, data availability, and required accuracy; analogical early-phase, build-up for detailed proposals.

## Key Concepts

- **Systems Engineering Plan (SEP)**: A governance document that records the SE strategy for a project, acts as the blueprint for conduct and control of technical aspects, defines SE structure and boundaries (government/contractor), links to program risks, and describes contractor/supplier technical management.

- **Acquisition Strategy**: A high-level business and technical management approach designed to achieve program objectives within resource constraints; provides the integrated framework for planning, organizing, staffing, controlling, and leading a program throughout its lifecycle.

- **Procurement**: The act of buying goods and services; a direct subset of acquisition, which spans the entire lifecycle of acquired systems from conception through disposal.

- **Cost Estimating**: A multidisciplinary practice that develops future costs for products and services by analyzing historical data and using quantitative methods; falls in the intersecting domain of systems engineering and project management.

- **Historical Data**: The foundation for all cost estimation; without sufficient data, estimates are guesses; collection is akin to forensic analysis of development history and typically requires dedicated resources, tools, and access to both technical and financial records plus stakeholder interviews.

- **Portfolio Management**: An organizational project-enabling process that uses an organization's strategic plan and portfolio direction as inputs to define, authorize, and evaluate a portfolio of projects/programs, then terminate or continue them based on contribution to strategy.

- **Work Breakdown Structure (WBS)**: A hierarchical decomposition of system scope used to support cost estimation, schedule planning, responsibility assignment, and technical baseline definition.

- **Contract Types**: Mechanisms for allocating risk and responsibility—Fixed Price (supplier bears cost risk), Cost-Reimbursement (offeror bears risk), Subcontracts (specialized task delegation), COTS variants (commercial-off-the-shelf with none/minor/major modifications), and IT Services.

- **Request for Proposal (RFP)**: A formal communication path for offeror/supplier to align on technical attributes, requirements, and capability expectations; directly linked to the acquisition process model and acquisition strategy.

- **Statement of Work (SOW) / Statement of Objectives (SOO)**: Documents that define technical scope, deliverables, acceptance criteria, and schedule; developed collaboratively by the Lead Systems Engineer, Contract Officer, and Program Manager.

## Mental Models

- **Use the three-layer governance model when structuring enterprise delivery**: Portfolio managers select projects aligned with strategy; program/project managers execute them on schedule and budget; systems engineers ensure technical integration, traceability, and architectural coherence. Each layer has distinct accountability—do not conflate them.

- **Think of SE as the "horizontal integrator" and domain engineering (electrical, mechanical, software) as "vertical specialists"**: SE ensures the interfaces between specialists are well-defined and the emergent behavior of the integrated system is correct; domain engineers focus on optimizing their vertical slice.

- **View cost estimation as a three-point decision**: Analogical for concept phase (high uncertainty, historical comparison), parametric for preliminary design (statistical correlations), and build-up for detailed proposals (full component enumeration). Data quality drives method choice.

- **Treat the acquisition strategy as the "master plan"**: It reconciles technical goals, budget constraints, schedule, risk, and organizational capability. All subsequent contracting, RFP, SOW, and execution decisions flow from it. Misalignment with acquisition strategy is a red flag.

## Anti-patterns

- **Omitting historical data collection from cost estimation**: Any estimate made without sufficient historical data is a guess lacking credibility and defensibility. Forensic analysis of prior programs, stakeholder interviews, and ongoing knowledge management are not optional—they are the foundation.

- **Starting acquisition at the wrong phase**: Entering a system with unproven technology at engineering development instead of technology maturation will incur huge rework costs. Conversely, force-fitting mature technology into an unproven problem creates integration risk. Match entry point to technology readiness.

- **Conflating portfolio management with project management**: Portfolio management chooses *what* to fund (strategy-driven, enterprise-level); project management executes *how* to deliver (timeline and budget discipline). Merging these creates strategy-execution misalignment and budget overruns.

- **Developing an RFP without a Systems Engineering Plan**: The RFP is the formal offeror-supplier communication channel for technical alignment. Without a SEP, the RFP will be vague, contradictory, or missing critical technical requirements. The SEP is the precursor.

- **Assigning cost estimation to non-multidisciplinary teams**: Cost estimating requires expertise in engineering, mathematics, domain knowledge, and historical precedent. A single estimator or finance-only team will miss technical dependencies, integration costs, and risk margins. Collaboration between systems engineers and cost analysts is not optional.

- **Using fixed-price contracts when requirements are uncertain**: Fixed-price contracts shift all cost risk to the supplier and lead to either high bids (to absorb risk) or supplier insolvency. High-risk, uncertain-scope efforts demand cost-reimbursement with active program management and change control.

## Key Takeaways

1. **Cost estimation is a multidisciplinary practice requiring historical data, quantitative methods, and collaboration between systems engineers and cost analysts.** Without sufficient historical data, any estimate is a guess lacking credibility. The effort to collect and analyze this data is not overhead—it is the foundation of defensible planning.

2. **The acquisition strategy is the master plan that reconciles technical objectives, budget, schedule, risk, and capability.** All downstream contracting, RFP, SOW, and execution decisions must flow from and align with it. A misaligned acquisition strategy leads to scope creep, cost overruns, and schedule slip.

3. **Systems engineering has a horizontal integrating role; domain engineering (electrical, mechanical, software) has vertical specialist roles.** SE ensures all vertical disciplines work together coherently, interfaces are well-defined, and emergent system behavior is correct. Both role types are essential; neither can substitute for the other.

4. **Portfolio management, program management, and project management are nested but distinct governance layers.** Portfolio chooses *what* to fund (strategy alignment); program/project management executes *how* to deliver (schedule and budget discipline); systems engineering ensures *technical correctness* (architecture, traceability, integration). Mixing these layers leads to strategy-execution misalignment.

5. **Match cost estimation methods to program lifecycle phase and data availability.** Analogical estimation works early when historical analogy is valid. Parametric estimation works in preliminary design when cost drivers are known. Build-up estimation is required for detailed proposals when specifications are mature. No single method is universally best.

6. **The Systems Engineering Plan (SEP) is the governance document that bridges acquisition strategy and contract execution.** It documents the SE strategy, structure, boundaries, risk linkages, and contractor/supplier technical management. The RFP and SOW are derived from the SEP; do not develop them in parallel.

7. **In software-intensive systems, software often shapes the entire system architecture and drives much of the complexity, cost, and schedule.** Traditional physical-system acquisition approaches may underestimate software's horizontal role. SE must ensure software architecture and system architecture co-evolve, not that software is bolted on as a vertical component.

## Connects To

- **ISO/IEC/IEEE 15288 (Systems and Software Engineering — System Life Cycle Processes)**: SEBoK life cycle processes and portfolio management activities are grounded in 15288's organizational and project-enabling processes; 15288 also provides the lifecycle framework that acquisition and portfolio management operate within.

- **ISO/IEC/IEEE 12207 (Software Life Cycle Processes)**: When systems are software-intensive, SE processes from 15288 must be integrated with software processes from 12207. Software and systems engineering are distinct disciplines with overlapping accountability in complex systems.

- **Project Management Institute (PMI) Portfolio Management Standard (3rd Edition)**: SEBoK portfolio management is directly aligned with PMI's six performance management domains and fundamental principles for portfolio management; both frameworks emphasize strategy alignment, governance transparency, and value optimization.

- **Defense Acquisition University (DAU) and DoD Acquisition Framework**: The acquisition process model, SEP outline, and systems engineering role in procurement are drawn from U.S. defense acquisition guidance and are widely adapted in aerospace, automotive, and other safety-critical domains.

- **Systems Engineering and Quality Attributes**: Cost is a quality attribute and an outcome of systems engineering trade studies. Budget and schedule constraints are inputs to SE problem formulation; cost estimation outputs feed system architecture and design decisions.
