# Chapter 5: Systems Engineering Life-Cycle and Technical Reviews

## Core Idea
Chapter 5 requires NASA programs and projects to conduct event-based life-cycle reviews — triggered by technical baseline maturity rather than calendar milestones — with prescribed minimum SE work products at defined maturity levels at each review gate, and mandates periodic technical reviews throughout each phase to monitor progress and readiness for the next phase.

## Frameworks Introduced
- **Event-Based Life-Cycle Review System**: Reviews are triggered when entrance criteria are satisfied (technical maturity), not by calendar; each review produces a decision memo signed by the Program/Project Decision Authority.
  - When to use: When scheduling reviews; push back against calendar-driven reviews that force reviews before technical products are ready.
- **Review Work Product Maturity Progression**: Work products progress through Initial → Preliminary → Baselined → Updated maturity states (defined in Appendix F); each review has minimum required maturity levels for mandatory products.
  - When to use: When determining what "done" means for a work product at a given review; the maturity label, not the content volume, is the compliance indicator.
- **Technology Readiness Level (TRL) Tracking**: TRLs (1–9) must be used throughout the life cycle to assess technology maturity; assessed initially in Formulation phase and updated at status reviews; other maturity measures must map back to TRLs.
  - When to use: Whenever incorporating new or evolving technologies; TRL gating prevents incorporation of immature technology into operational products.

## Key Concepts
- **Key Decision Point (KDP)**: The event at which the Decision Authority determines the readiness of a program/project to progress to the next life-cycle phase; not synonymous with a technical review but informed by one.
- **Entrance Criteria**: Minimum accomplishments a program/project must fulfil before a life-cycle review is convened; guidance is in Appendix G; to be tailored per program/project.
- **Success Criteria**: The conditions that must be satisfied for a review to be considered successfully completed; developed by the technical team in collaboration with reviewers.
- **Review Item Discrepancy (RID)**: A formally documented finding from a life-cycle review requiring disposition; review is not complete until all RIDs are dispositioned with ETA concurrence.
- **Request for Action (RFA)**: A formally documented action item from a life-cycle review requiring a response plan; like RIDs, must be tracked through closure.
- **Minimum Required Products by Review**:
  - MCR: Baselined stakeholder expectations, concept definition, approved MOE definitions.
  - SRR: Baselined SEMP, baselined requirements, baselined HSI approach.
  - MDR/SDR: Approved TPM definitions, baselined architecture, baselined requirements allocation, initial TPM trends, baselined SEMP (for programs).
  - PDR: Preliminary design solution, baselined integration plans, baselined V&V Plan.
  - CDR: Baselined detailed design.
  - SIR: Updated integration plan, initial V&V results.
  - ORR: Preliminary V&V results, baselined decommissioning and disposal plans.
  - FRR: Baseline V&V results, final certification for flight/use.
  - DR/DRR: Updated decommissioning and disposal plans.
- **Human Systems Integration (HSI) Approach**: Must be documented and baselined at SRR; HSI is co-owned by ETA, SMA TA, and HMTA; must address crew, operators, users, maintainers, assemblers, and ground support personnel throughout the life cycle.
- **Technical Leading Indicator**: A subset of TPMs that provides forward-looking insight into potential future states; mass margins (for hardware projects) and power margins (for powered projects) are mandated leading indicators.

## Mental Models
- "Baselined going into, formally baselined coming out of" — work products labeled "baseline" in Table 5-1 must be at least final drafts entering the review; they are formally baselined after incorporating approved review comments.
- Reviews are complete only when: all RIDs/RFAs are dispositioned with TA concurrence, the board report is distributed, a plan exists for all issues, and the Decision Authority signs the decision memo.
- Combining or resequencing life-cycle reviews is customization (no waiver needed, document in SEMP); eliminating a review requires a formal waiver or deviation.
- If a required review product is not yet available, the technical team needs a waiver or deviation before the review, not after.

## Anti-patterns
- **Calendar-driven review scheduling**: Scheduling reviews to meet budget/schedule milestones before entrance criteria are met produces incomplete products and downstream rework; reviews must be event-driven.
- **Treating TRL assessment as a one-time gate**: Technology maturity must be tracked continuously; initial assessment in Formulation and updates at every status review are both required.
- **Ignoring software in life-cycle reviews**: All software aspects of the system must be included in every life-cycle and technical review; software review requirements (NPR 7150.2) are integrated, not separate.

## Key Takeaways
1. Life-cycle reviews are event-based (maturity-triggered), not calendar-based; the entrance criteria in Appendix G define readiness, not a date.
2. Specific SE work products are mandated at specific reviews with specific minimum maturity levels — these are "shall" requirements (SE-35 through SE-69), not guidelines.
3. A review is not complete until all RIDs and RFAs are dispositioned with TA concurrence and the Decision Authority signs a decision memo.
4. TRLs must be assessed at programme initiation and tracked at every status review; technologies below TRL 6 at CDR represent significant risk flags.
5. Mass and power margins are the two mandated technical leading indicators; monitoring them continuously provides early warning of budget erosion.
6. Baselined integration plans and a baselined V&V Plan are both required by PDR — a new addition in NPR 7123.1D versus previous versions.

## Connects To
- **Appendix G (Entrance and Success Criteria)**: Provides the detailed guidance tables for every life-cycle review type; referenced directly from this chapter's requirements.
- **Appendix E (TRL Definitions)**: Defines TRL 1–9 for hardware and software; referenced for technology maturity assessment requirements.
- **Appendix F (Work Product Maturity Terminology)**: Defines Initial, Preliminary, Baseline, Update, Approve, and Final as used in Table 5-1 and Section 5.2.2.2.
- **NPR 7120.5 (Space Flight Program and Project Management Requirements)**: The governing NPR for program/project life cycles; life-cycle reviews in this NPR align to the KDP structure defined there.
- **NPR 7150.2 (Software Engineering Requirements)**: Software review requirements are mandated to be included in every life-cycle review per this chapter.
