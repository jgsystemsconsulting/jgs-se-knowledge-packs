# Chapter 7: HSI Products, Scaling, and Tailoring

## Core Idea
Every P/P produces a tailored HSI product set anchored by three guiding documents — ConOps, SEMP, and HSI Plan — scaled to three effort levels (Large, Medium, Small) determined by human safety risk and operational involvement, not budget.

## Frameworks Introduced
- **Three-Tier HSI Scaling Framework**: P/Ps are classified as Large-Scale, Medium-Scale, or Small-Scale HSI effort based on two axes — Human Safety (Category I/II/III per NPR 7120.5E) and Human Involvement (complexity of coupling between human action and critical system performance).
  - When to use: At program inception, when the HSI practitioner first assesses what level of HSI effort the P/P requires; use Appendix B checklist to document the assessment.
- **HSI Implementation Planning Checklist (Appendix B)**: A domain-by-domain checklist used to identify what HSI activities and products are needed for a specific P/P; should be initiated immediately upon assuming HSI lead responsibility.
  - When to use: At P/P outset; revisit at each major phase transition to identify new requirements.
- **Incremental Development Integration**: A hybrid approach combining agile/incremental development cycles with NASA's plan-based SE culture, ensuring HSI usability and human-centered design processes are embedded in iterative sprints.
  - When to use: When the P/P uses Agile or spiral development; requires cohesive, communicative teams that maintain customer expectations across rapid iterations.

## Key Concepts
- **Large-Scale HSI Effort**: Category I safety risk, human-rated program, life-sustaining equipment, flight crew lives-in-the-product, extensive training required. Products: standalone ConOps, standalone HSI Plan, required HSI team, significant HITL (iterative), full verification/validation.
- **Medium-Scale HSI Effort**: Category II safety risk, modest hazard controls, crew essential to mission success, moderate human-system coupling. Products: possible standalone ConOps, HSI Plan as part of SEMP, recommended HSI team, strong HITL effort.
- **Small-Scale HSI Effort**: Category III safety risk, low risk, crew involved with some aspects, automation reduces human interactions. Products: ConOps and HSI Plan as part of project documents, modest HSI team effort, desired HITL.
- **ConOps (Concept of Operations)**: The system description from the user's perspective; establishes operational scenarios, function allocation rationale, and the standard for system validation. Developed in Pre-Phase A, baselined in Phase A, updated at all major reviews.
- **SEMP (Systems Engineering Management Plan)**: The primary top-level technical management document. For smaller P/Ps, the HSI Plan may be a section within the SEMP rather than a standalone document.
- **HSI Plan**: The central HSI management document; documents HSI objectives, strategy, domain approach, requirements, organisation, roles/responsibilities, implementation approach, and products. Content outline: Sections 1-6 (Introduction, Applicable Docs, HSI Objectives, HSI Strategy, Requirements/Organisation/Risk, Implementation).
- **HSI Requirements**: Verifiable "shall" statements that embed human-centered goals into the system design baseline. Developed, integrated, interpreted, and verified with support from SE personnel and HSI domain experts.
- **Commercial-Off-The-Shelf (COTS) HSI Assessment**: Structured evaluation of COTS products against HSI criteria beyond functional form/fit/function: vendor reputation, product life cycle, complexity of operation, interface suitability, crew task time impact, safety to crew/vehicle/mission. All COTS items must be identified in design reviews for regulating-authority visibility.
- **Crew Time as Cost-Equivalent Metric**: Crew time (person-hours) used as a cost proxy in trade studies and requirements; enables economic comparison between design alternatives without computing exact monetary cost.

## Mental Models
- Use the safety and human-involvement axes — not budget — to determine HSI scale. The guide explicitly cautions: "The HSI practitioner is cautioned against using the P/P budget as a primary consideration when determining HSI effort."
- Use crew time as a trade study currency: converting design options to crew-time impact creates a common, measurable metric that translates to operational cost without requiring a full LCC model.
- For incremental development (Agile), maintain HSI's "feedback loop" philosophy: each sprint's early user feedback replaces the traditional HITL mockup cadence, but the core principle — iterative human input to design decisions — remains identical.

## Anti-patterns
- **Using budget as the primary HSI scoping criterion**: The guide explicitly warns against this; a low-budget P/P with high human safety risk requires appropriate HSI effort regardless of cost constraints.
- **Accepting COTS products without HSI screening**: "A increasing trend within P/P is the use of COTS hardware or software... COTS products also increase the need for HSI assessment." Standard functional assessment is insufficient; domain-specific usability, safety, and crew-time criteria must be applied.
- **Treating the COTS selection criteria list as complete**: The guide provides an example criteria list but notes that an "evaluation checklist should be developed that includes HSI criteria for each trade study being conducted" — the generic list is a starting point, not a standard.

## Key Takeaways
1. The three-tier HSI scaling framework drives product selection: Large requires standalone plans and significant HITL; Small uses project-embedded plans and desired HITL; Medium sits between.
2. The HSI Implementation Planning Checklist (Appendix B) is the primary scoping tool; it should be initiated at program inception and revisited at each phase transition.
3. ConOps, SEMP, and HSI Plan are the three anchor documents; all other HSI products are subordinate and documented within or derived from them.
4. HSI requirements are the ultimate mechanism for embedding human considerations in design; they must be verifiable, connected to MOEs/MOPs/TPMs, and baselined by SRR.
5. Crew time as a cost-equivalent metric enables HSI trade studies to participate in economic decision-making without requiring full monetary cost models.
6. COTS selections require explicit HSI assessment against human-system criteria (usability, crew task time, crew safety, interface suitability) beyond standard engineering qualification.

## Connects To
- **NPR 7120.5E, section 2.1.4**: Program category definitions (Category I/II/III) used in the scaling framework.
- **HSIPG Appendix A**: Annotated HSI Plan content outline for practitioner reference.
- **HSIPG Appendix B**: Sample HSI Implementation Planning Checklist.
- **HSIPG Appendix C.6**: Incremental/Agile development implementation example.
- **NASA/SP-2010-576**: Risk-Informed Decision Making Handbook — referenced for architecture-level trade-off decision support.
