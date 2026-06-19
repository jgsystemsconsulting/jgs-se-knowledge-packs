# NASA HSI Practitioner Guide Patterns & Techniques

## Pattern: Early HSI Entry (Pre-Phase A Engagement)
**When to use**: At program inception, before any design decisions are committed to baseline.
**How**: Assign an HSI practitioner to the concept team from the start. Initiate ConOps development, function allocation, and HSI planning under SEE 1/2/3 before the MCR. Document human factors, user populations, interface types, and logistics infrastructure in pre-MCR materials.
**Trade-offs**: Requires HSI budget and staffing from day one, before the program is formally funded at full rate. The cost is low relative to later re-design savings; withholding HSI until Phase A means LCC is already partly locked in by the time HSI begins.

---

## Pattern: ConOps-Anchored Design
**When to use**: Whenever system design trades are evaluated or requirements are being written.
**How**: Develop ConOps covering nominal, off-nominal, and emergency scenarios. Use it as the primary source for function allocation. Validate all design alternatives against ConOps scenarios, not just performance specifications. Update ConOps at every major review.
**Trade-offs**: A ConOps that is too constrained can unnecessarily bound the design solution space. Keep the design solution content minimal in the ConOps to preserve engineering flexibility.

---

## Pattern: Function Allocation Trade Study
**When to use**: At architecture definition (Pre-Phase A through Phase B) whenever a decision must be made about whether a function should be automated, semi-automated, or manually executed by a human.
**How**: Apply the NASA function allocation process: define what the system must do at successively lower levels → include human performance requirements and constraints → define adaptive UI and feedback requirements → evaluate trade-offs across autonomy levels → examine HSI domain implications of each option.
**Trade-offs**: Allocating too much to automation reduces human situational awareness and degrades performance in unexpected failure modes. Allocating too much to humans increases training burden and operational manning costs.

---

## Pattern: Iterative HITL Evaluation Ladder
**When to use**: Throughout concept development and design (Pre-Phase A through Phase D).
**How**: Build increasingly faithful human-in-the-loop evaluations at each phase: (1) low-fidelity foam/wood mockups in Pre-Phase A to assess access, reach, and visual perception; (2) medium-fidelity mockups and software simulators in Phases A-B for task analysis and workload measurement; (3) high-fidelity integrated system HITL in Phase C/D for V&V closure. Pre-declare Phase B/C HITL for Phase D verification credit.
**Trade-offs**: Higher-fidelity evaluations are more costly. Investment in early low-fidelity HITL pays off when it catches fundamental human-system incompatibilities before fabrication commitments.

---

## Pattern: Crew Time as Cost Proxy
**When to use**: In trade studies where design alternatives differ primarily in human effort or operational burden rather than hardware cost.
**How**: Express design options in person-hours required (task time, training time, maintenance time, logistics preparation). Use crew time as the primary cost-equivalent metric. Set threshold and objective values early (e.g., ≤40% / ≤35% of crew work-day for maintenance burden). Compare alternatives on this basis before conducting a full monetary LCC analysis.
**Trade-offs**: Crew time is a necessary but not sufficient LCC proxy; also account for skill requirements (number of qualified personnel) and resupply logistics costs.

---

## Pattern: HSI-Informed Requirements Development
**When to use**: During technical requirements definition (SEE 2) in Phase A and Phase B.
**How**: Start with applicable standards (NASA-STD-3001, MIL-STD-1472D, NASA-STD-5005D). Translate standard statements into verifiable program "shall" requirements using ConOps scenarios and function allocation outputs as the context. Write each requirement with enough specificity to drive design decisions but enough flexibility to allow engineering trade space. Develop the V&V approach for each requirement at the same time it is written.
**Trade-offs**: Over-specified requirements constrain design solutions; under-specified requirements cannot be verified. Balance by grounding specificity in human performance constraints (measurable physiological and cognitive limits) rather than preference.

---

## Pattern: SME Integration Brokering
**When to use**: Whenever domain SMEs provide conflicting inputs, or when SME knowledge is highly specialised and difficult to translate into design decisions.
**How**: The HSI practitioner acts as integrator: collect inputs from all relevant domain SMEs, identify conflicts, resolve or mitigate them before escalating to P/P management, then translate the consensus into design requirements or risk items. Document the integration rationale in the HSI Plan.
**Trade-offs**: The integrator role risks diluting highly specialised knowledge into generic requirements. Preserve fidelity by ensuring SMEs review the translated requirements and verify that their intent is captured.

---

## Pattern: Three-Scale HSI Effort Calibration
**When to use**: At program inception and at every phase transition.
**How**: Classify the P/P using two axes — Human Safety (Category I/II/III per NPR 7120.5E) and Human Involvement (complexity of coupling between human action and critical system performance). Use Appendix B checklist to document the assessment. Map the classification to Large/Medium/Small HSI effort tier and select the corresponding product and activity set from Table 4.2-2.
**Trade-offs**: Do not use budget as the primary scoping criterion (explicitly warned against in the guide). A low-budget program with high human safety risk must receive appropriate HSI effort regardless of cost constraints.

---

## Pattern: Product Maturity Gating
**When to use**: When preparing for any lifecycle review (MCR, SRR, PDR, CDR, etc.).
**How**: Use the Product Maturity Matrix (Table 3.1-3 for programs; Table 3.1-4 for human-rated programs) to identify which HSI products must be at D/I/U/X maturity by the upcoming review. Assess current maturity of each product. For gaps, either close them before the review or document a closure plan with schedule. Include maturity evidence in the review package.
**Trade-offs**: Gating on maturity level without verifying quality can create compliance artifacts rather than genuine products. Ensure that "I" (Initial baseline) products are actually usable by the SE team, not merely existential documents.

---

## Pattern: COTS HSI Screening
**When to use**: When a COTS hardware or software product is a candidate for selection.
**How**: Beyond standard functional assessment, evaluate: vendor reputation and product history; complexity of operation; interface suitability for the intended crew; crew task time impact; safety to crew, vehicle, and mission; lifecycle obsolescence risk; training requirements. Develop a program-specific HSI criteria checklist for each trade study. Identify the product in design reviews for TA visibility.
**Trade-offs**: COTS saves schedule and non-recurring cost but shifts integration risk to the HSI team. The more specialised the mission environment (e.g., space EVA, extreme thermal), the more likely a nominally functional COTS product will fail HSI screening.

---

## Pattern: V&V Pre-Declaration
**When to use**: When planning Phase A-C HITL evaluations that could contribute to Phase D verification closure.
**How**: At the time of planning a HITL evaluation in Phases A, B, or C, formally document its intended verification credit: identify the specific HSI requirement(s) it will verify, the fidelity standard it must meet, and the "test as you fly" conditions required. Gain SE and TA concurrence on the pre-declaration. In Phase D, assess the pre-declared HITL for closure against the documented conditions.
**Trade-offs**: Pre-declaration saves Phase D schedule but creates a formal commitment that the HITL must meet. If conditions change (system design evolves significantly), the pre-declared credit may be invalidated and must be re-earned.

---

## Pattern: Lessons-Learned Linkage
**When to use**: During Phase E operations and at Phase F closeout.
**How**: Systematically collect in-mission data (crew time, error incidents, physiological indicators, crew debriefs, mission anomalies). Generate lessons learned that explicitly link Phase E operational successes and failures to specific HSI decisions made in Phases A-C. Archive in the P/P documentation system. Communicate to successor programs via institutional channels.
**Trade-offs**: Lessons learned that are not linked to specific design decisions are anecdotes, not actionable knowledge. The investment in traceability (connecting Phase E data to Phase A-C decisions) is what produces transferable institutional memory.

---

## Pattern: Agile-NASA Hybrid HSI
**When to use**: When a P/P uses Agile or incremental development.
**How**: Map HSI feedback loops to sprint boundaries: conduct usability evaluations at the end of each sprint, feed results into the next sprint's design backlog. Maintain formal ConOps and HSI Plan as program-level documents updated quarterly or at sprint milestones. Ensure safety-critical HSI requirements are treated as non-negotiable constraints in the backlog, not as technical debt.
**Trade-offs**: Agile's speed can outpace HSI analysis if sprint cycles are very short. Maintain at least two HSI review points per sprint: early (to identify human-interaction risks before implementation) and late (usability verification of implemented features).
