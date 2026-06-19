# Chapter 18: 4.2 Technical Requirements Definition

## Core Idea
Technical Requirements Definition is the NASA SE process that transforms validated stakeholder expectations and mission objectives into a complete, verifiable, traceable set of functional, performance, and interface requirements that form the basis for design, cost estimation, and verification planning.

## Frameworks Introduced
- **Technical Requirements Definition Process**: Systematic identification, specification, validation, and baselining of technical requirements derived from stakeholder expectations, mission objectives, and constraints.
  - When to use: Early in Phase A and B; whenever stakeholder needs must be translated into design inputs. Results feed Logical Decomposition and Design Solution Definition.
  - Key INPUTS: Stakeholder Expectations, Mission Objectives and Constraints, Concept of Operations (ConOps), Mission Success Criteria, validated problem statement.
  - Key ACTIVITIES: Develop candidate requirements, perform functional analysis, allocate requirements across PBS, validate against stakeholder needs and technical feasibility, establish MOPs and TPMs, baseline requirements at System Requirements Review (SRR).
  - Key OUTPUTS: Validated Technical Requirements document (SRD/PRD/IRD/SRS), Measures of Performance, Technical Performance Measures, Requirements Metadata and traceability database.

- **Requirements Validation Framework** (five-step gatekeeping): (1) Format correctness ("shall" statements, editorial), (2) Technical correctness (bidirectional traceability to stakeholder expectations, valid assumptions, consistency with lifecycle phase), (3) Stakeholder satisfaction (relevant groups confirm adequacy), (4) Feasibility (technical sense, achievable), (5) Verifiability (stated with sufficient information to verify post-implementation).
  - When to use: Before baselining any requirement set. Validation results determine go/no-go for Logical Decomposition entry.

## Key Concepts
- **Functional Requirements**: What functions the system must perform to accomplish objectives. Derived from Concept of Operations by asking: what functions, where, how often, by whom, under what conditions?

- **Performance Requirements**: How well the system must perform its functions, quantitatively specified. Drawn from ConOps and scenarios by asking: frequency, accuracy, quality, quantity, stress conditions, duration, range, tolerance, throughput, bandwidth.

- **Interface Requirements**: All boundaries between the product and external world, including operational/command-and-control, computer-to-computer, human-system, mechanical, electrical, thermal, and data interfaces. Applicable across all lifecycle phases (test equipment, transportation, ILS, manufacturing, operations, maintenance).

- **Crosscutting Requirements** (Non-Functional): Requirements that apply across the system architecture rather than down the PBS, including environmental (radiation, thermal, acoustic, mechanical loads, contamination, RF), safety (deterministic and risk-informed), human factors engineering, reliability, and "-ilities" (producibility, maintainability, availability, upgradeability).

- **Key Design Requirement (KDR)**: A requirement with large impact on cost or schedule when implemented; identified early to enable better management and design tradeoffs.

- **Measures of Performance (MOPs)**: Quantitative, measurable performance characteristics the system should exhibit in its intended environment; derived from MOEs but stated from the supplier/technical perspective; typically multiple MOPs support a single MOE.

- **Technical Performance Measure (TPM)**: A physical or functional characteristic of the system derived from MOPs that is critical or key to mission success; monitored during implementation by comparing actual achievement against anticipated values to confirm progress and identify cost/schedule risk.

- **Requirement Traceability**: Bidirectional linkage of parent (stakeholder-level) requirements to derived (lower-level) requirements, ensuring each requirement is necessary and no unallocated functionality exists.

- **Threshold vs. Baseline Performance**: Threshold is the minimum acceptable value needed for mission success; baseline is the desired performance level. Specifying both provides design trade space while preventing overspecification that eliminates solutions.

## Mental Models
- **Think of Technical Requirements Definition as a translation layer.** High-level expectations and mission objectives flow in (often vague or qualitative); rigorous requirements activities flow them through functional analysis, constraint derivation, and stakeholder review; validated, traceable technical requirements flow out (specific, measurable, verifiable). Each requirement is a contract between stakeholders and developers.

- **Use the PBS-to-requirements decomposition as a risk-mitigation tool.** As you allocate parent requirements down the Product Breakdown Structure, lack of traceability at any level signals either missing requirements (underdesign) or unjustified requirements (overdesign). Iteratively validate until every line item has a parent and every requirement has allocations.

- **Think of MOPs and TPMs as early-warning sensors.** MOPs are "how well the design delivers the performance promise." TPMs are the subset of MOPs that are so critical to mission success that you monitor them continuously during implementation. If a TPM trend shows degradation, you catch cost or schedule risk long before verification.

- **Distinguish deterministic from risk-informed safety requirements.** Deterministic safety (e.g., hardware stops, command limits, fault-tolerant processors) prevents hazards by design; risk-informed safety (e.g., "P(LOC) < p at confidence level q") acknowledges residual risk and specifies acceptable upper bounds on consequence probabilities.

## Anti-patterns
- **Overly restrictive performance requirements**: Specifying performance tighter than necessary (e.g., recharge time < 3 hours when 12 hours is adequate; weight ±0.5 kg when ±2.5 kg is acceptable) eliminates viable design solutions and increases cost without adding value. Always justify performance thresholds through tradeoff analysis and capture rationale.

- **Vague, unverifiable requirements**: Statements like "minimize noise" or "maximize reliability" are not verifiable. Rewrite as quantitative specifications with clear success criteria (e.g., "noise level of component X shall remain under Y decibels") so verification is unambiguous.

- **Untraced or orphaned requirements**: Requirements not allocated to lower-level elements result in unimplemented functionality or lost stakeholder intent. Conversely, lower-level requirements with no parent traceability signal scope creep or overdesign.

- **Requirement changes without impact analysis or formal control**: In Phases A and B, requirements and constraints evolve constantly. Uncontrolled changes break traceability and introduce hidden cost/schedule impacts. All changes must undergo formal review, approval, and impact assessment at all hierarchical levels before re-baselining.

- **Missing or incomplete metadata**: Omitting rationale, verification method, traceability linkages, and ownership creates ambiguity and rework downstream. Capture metadata (ID, rationale with parent reference, verification method and lead, owner, verification level) at requirements-write time, not retroactively.

- **Neglecting crosscutting requirements**: Focusing only on functional and performance requirements in the PBS while missing environmental, safety, human factors, and reliability requirements leads to inadequate design and late-stage redesigns.

## Key Takeaways
1. **Requirements are contracts.** Well-written technical requirements establish mutual agreement between stakeholders and developers on what the product must do, enabling early identification of misunderstandings and omissions before costly redesign.

2. **Functional analysis is the engine.** Decompose top-level requirements into functions by asking what must happen, where, when, by whom, and under what conditions. Allocate functions and derived requirements down the PBS systematically; validate traceability at each level.

3. **Validation before baselining is mandatory.** A five-step validation gatekeeping process (format, technical correctness, stakeholder satisfaction, feasibility, verifiability) prevents defective requirements from propagating into design and verification. Validation results determine entry into Logical Decomposition.

4. **Threshold and baseline provide design trade space.** Specifying performance in terms of minimum acceptable (threshold) and desired (baseline) values allows designers to explore alternatives without scope creep or overspecification.

5. **Metadata and traceability are operational requirements, not nice-to-haves.** Rationale captures intent (reason, assumptions, design constraints); bidirectional traceability ensures nothing is forgotten or unjustified; ownership ensures accountability. Maintain a requirements database for visibility across the project team.

6. **MOPs and TPMs are early-warning systems.** Measures of Performance translate mission effectiveness expectations into technical metrics; Technical Performance Measures flag the critical few that you monitor continuously during implementation to detect cost and schedule risk before it becomes a crisis.

7. **Crosscutting requirements demand discipline.** Environmental, safety, human factors, reliability, and "-ilities" requirements do not flow down the PBS but cut across all elements. Structure requirements explicitly to capture them; discipline engineering to ensure they are allocated and not lost in functional decomposition.

## Connects To
- **ISO/IEC/IEEE 15288 (Systems Engineering — System Life Cycle Processes)**: Requirements definition and analysis are central lifecycle processes; this NASA process operationalizes the ISO framework for aerospace and mission-critical projects.

- **System Requirements Review (SRR)** (Section 6.7): The SRR gates requirements baselining; it is the formal review point where stakeholder and technical teams confirm that all requirements are complete, correct, and approved before Logical Decomposition proceeds.

- **Logical Decomposition Process** (Section 4.3): Consumes validated Technical Requirements; applies functional analysis and architecture framework to decompose parent requirements into derived requirements allocated to lower-level system elements.

- **Design Solution Definition Process** (Section 4.4): Uses baselined Technical Requirements as input to design-to specifications; verifies compliance during detailed design and integration.

- **MOEs and MOPs relationship** (Section 6.7.2.6.2): MOEs express stakeholder/mission effectiveness expectations; MOPs are quantitative measures the design must achieve to realize those MOEs; TPMs are the critical subset monitored during implementation.

- **Verification and Validation** (Appendix E and Section 6.7): Verification methods (test, inspection, analysis, demonstration) are determined and captured as part of metadata during requirements development; validation confirms requirements satisfy stakeholder needs and mission success criteria.
