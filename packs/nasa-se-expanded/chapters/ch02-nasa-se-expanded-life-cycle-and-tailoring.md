# Chapter — NASA Program/Project Life Cycle and Tailoring of NPR 7123.1

> **Depth note.** The companion `nasa-se-handbook` pack already walks the phase-by-phase narrative (Pre-Phase A through F), the KDP/review sequence, the program coupling taxonomy, and the SE Product Maturity table at a survey level. This chapter does **not** re-tell those phases. It goes deeper on the machinery the handbook treats only in passing: how the life cycle becomes a *tailoring substrate*, how the Compliance Matrix mechanizes relief from "shall" statements, the precise line between tailoring and customization, the eight tailoring criteria, the project-type (A–F) scaling scheme, the approval governance chain, and how the annual budget cycle injects uncertainty into an otherwise orderly gate structure. Where a phase is named below, it is to expose a *mechanism* (descope options, SEMP baseline timing, baseline-then-only-refine discipline), not to summarize the phase.

## Core Idea

The Expanded Guidance frames the life cycle not as a fixed pipeline every project marches through identically, but as a **scaffold that is deliberately right-sized to each program/project**. The phases and Key Decision Points (KDPs) supply the skeleton; tailoring and customization decide how much flesh each project hangs on it. The governing insight is that NPR 7123.1 was written to span everything from a human-rated launch system to a tabletop technology demonstrator, so its "shall" statements intentionally carry slack — and a systems engineer who fails to exploit that slack either drowns a small project in process or under-disciplines a critical one. Getting the scaling right, documenting it through the Compliance Matrix, and routing it through the correct approval authority is itself a core SE activity, not paperwork bolted on after the fact.

## Frameworks Introduced

- **NASA life-cycle phase decomposition (Formulation / Implementation)** — From NPR 7120.5. Two top-level periods. Formulation answers whether a sound, affordable plan exists; Implementation executes it. For space-flight projects these expand into seven incremental pieces (Pre-Phase A Concept Studies; Phase A Concept & Technology Development; Phase B Preliminary Design & Technology Completion; Phase C Final Design & Fabrication; Phase D Assembly/Integration/Test/Launch; Phase E Operations & Sustainment; Phase F Closeout). Used to chop a project into management-sized, separately-fundable, separately-gated pieces.

- **Key Decision Points (KDPs)** — The events where the decision authority judges readiness to enter the next phase. Phase boundaries are set so each is a natural go/no-go. A pass may be conditional, carrying *liens* that must clear inside an agreed window; a fail can mean retry-after-fix or termination. Used as the irreversible commitment points that separate phases.

- **Governing-document routing** — The life cycle a project actually follows depends on which directive governs it: NPR 7120.5 (space flight), NPR 7120.7 (IT and institutional infrastructure), NPR 7120.8 (research & technology), NPR 7150.2 (software). The Expanded Guidance stresses that "highly specialized IT" (defined in the glossary) is pulled back under 7120.5 or 7120.8 rather than 7120.7. Used to pick the correct phase model and gate-product set before any tailoring begins.

- **SE Product Maturity table (Table 3.0-1, drawn from NPR 7123.1)** — A grid mapping each major SE product (stakeholder/concept definition, MOEs, cost & schedule, SEMP, requirements, TPMs, architecture, requirement allocation, design solution, interfaces, implementation/integration/V&V plans, V&V results, operations plans/procedures, certification, decommissioning/disposal plans) against phases, marking where each is *Preliminary → Baseline → Update*. Cells flagged `**` are *required* products for that review. Used as the objective checklist of what maturity each gate demands.

- **Tailoring (NPR 7123.1 defined term)** — NPR 7123.1 defines it as the process for seeking relief from the SE NPR's requirements in a way that stays consistent with the program/project's objectives, its allowable risk, and its constraints. Tailoring produces **deviations or waivers** (per NPR 7120.5 §3.5) and is recorded in the next SEMP revision. Used to legally remove or scale a binding "shall."

- **Customization (Expanded-Guidance defined term)** — Defined as modifying the *recommended* SE practices through which an SE requirement is met. Because the NPR's wording leaves latitude, you can change *how* you satisfy a requirement without changing *whether* you satisfy it. Customization needs **no** waiver or deviation, though significant customization should still be written into the SEMP. Used to adapt practice depth without invoking the formal relief machinery.

- **Compliance Matrix (NPR 7123.1 Appendix H.2)** — The instrument that lists every NPR requirement and records compliance, intent to comply, or the justification for relief. It carries a rationale for each requirement, captures customization decisions, and is attached to the SEMP (or folded into the project plan if no standalone SEMP exists). Appendix H.1 is the *Center-level* variant (a Center tailoring the NPR for standard use, approved by the OCE); Appendix H.2 is the *program/project* variant (approved by the Center Director or designee). Used as the single auditable record of every tailoring/customization decision and its approver.

- **Risk-classification entry point (NPR 8705.4)** — Assigns a risk classification to payloads on human- or non-human-rated systems and is named as the *starting point* for defining tailoring criteria. Used to anchor "how much relief is defensible" in a formal risk class rather than in opinion.

- **Project-type scaling scheme (Table 3.11-1, Types A–F)** — An example taxonomy running from very complex/high-priority/low-risk Type A (e.g., human space flight, very large science) down to simple, high-risk-tolerant Type F (aircraft or ground-based tech demos), with Types B–E in between. Each type carries example priority, acceptable risk, cost band, lifetime, and assurance posture. Explicitly labeled *guidance, not rigid characterization* — a project can be Type A in one aspect and Type D in another, so tailoring can be granular per aspect. Used as a first-cut dial for how aggressively to tailor.

- **Product-tailoring example (Table 3.11-2)** — Pairs the Type A–F scheme against required NPR 7120.5 products (concept docs, architectures, requirements, design docs, ConOps, TRA docs, HSI plan, control plans, etc.), marking each cell *Fully Compliant / Tailor / Not Applicable*. Used to show concretely that simpler types collapse many products into "Tailor" or "Not Applicable."

- **PPBE budget cycle (FMR Volume 4)** — Planning, Programming, Budgeting, and Execution: NASA's rolling annual resource-alignment process feeding the President's budget and congressional appropriation. Used to situate the technical gate schedule inside a fiscal rhythm the SE does not control.

## Key Concepts

- **The life cycle exists to create visibility, not ceremony.** Decomposing a project into phases is justified in the Expanded Guidance primarily as a way to give managers *incremental visibility* at points that line up with the management and budgetary environment. Each phase boundary is engineered to be a clean go/no-go, which is why baselining discipline lives at the boundaries.

- **Liens are conditional passes with a clock.** A KDP decision to proceed can be qualified by liens that must be retired within an agreed period. This is the formal mechanism for "you may advance, but these specific gaps must close by date X" — a middle path between pass and hold.

- **Descope options are pre-positioned fallbacks, not failures.** During Pre-Phase A the team develops a preliminary set of descope options — what the mission still accomplishes if resources shrink or hardware is lost (fewer instruments, a thinner mission profile, what an orbiter can do after losing its lander). These are a gate product for the MCR but are deliberately *not* baselined or maintained; they are archived for later retrieval. Success criteria are reduced to match a descoped mission. This is a depth point the survey-level phase narrative skips.

- **The Agency Baseline Commitment (ABC) is the irreversible external promise.** At the end of Phase B (toward KDP C), the project and the Agency lock in what they will achieve, bounded by an agreed cost and schedule. For projects whose life-cycle cost exceeds $250M, that promise is extended outward to Congress and OMB and is named the ABC. After this point, the doctrine of successive refinement applies: almost all baseline changes are expected to be refinements, not fundamental redesigns, because changes at and beyond Phase B grow increasingly expensive.

- **SEMP baseline timing depends on program type — a subtle gate nuance.** Per the Table 3.0-1 footnote, the SEMP baselines at **SRR** when the effort is a project, a tightly coupled program, or a single-project program — but it slips to **MDR/SDR** for the uncoupled and loosely coupled cases. The SEMP itself is the vehicle that documents how NPR 7123.1's practices will be addressed across the life cycle — so *when* it baselines is when the tailoring story becomes binding.

- **Three concrete ways to tailor a requirement.** (1) Eliminate a requirement that simply does not apply (in-house-only project → the NPR's contract chapter is moot; no software → software requirements are moot). (2) Eliminate a requirement whose cost of compliance adds *more* risk (by diverting resources) than non-compliance does. (3) Scale the requirement to better balance implementation cost against project risk.

- **Two ways to customize a practice.** (1) Vary the way any of the seventeen SE processes gets carried out. (2) Vary how formal a review is and when it lands. Neither needs a waiver.

- **Scope relief vs. waiver — the stand-alone-document test.** The SE NPR itself does not demand any stand-alone documents, so on a small project many "plans" can collapse into a few paragraphs inside the SEMP or project plan. But if the *governing project-management* directive (7120.5, 7150.2, 7120.7, 7120.8) requires a document to stand alone, removing that requires a waiver/deviation against *that* directive. If no such standalone requirement exists, where you record the information is pure customization — record the location in the Compliance Matrix and move on.

- **Review formality and spacing are customizable; review existence is not (without a waiver).** The governing PM directive fixes the *number and timing* of reviews, but formality is open: a large project might run a multi-week formal review with a RID/RFA process, boards, and pre-boards; a small project might run the same review around a tabletop in a few hours with issues logged in a slide deck. Combining reviews (e.g., SRR + SDR/MDR) needs no SE-NPR waiver *provided the intent of both is met* — though the governing PM NPR may still require one. Dropping a required review entirely does need a waiver/deviation.

- **The Compliance Matrix is the system of record for relief.** Tailoring can happen at any point in the life cycle; depending on timing it yields deviations (relief sought before the requirement bites) or waivers (relief after). Either can go to the Designated Governing Authority one at a time, or be batched through the matrix, which then rides attached to the SEMP. Center-wide tailoring uses H.1 → OCE; delegated program/project tailoring uses H.2 → Center Director or designee. The result is folded into the next SEMP revision with rationale and documented approvals, so the whole team — and any independent assessor — sees the modified expectations.

- **The budget cycle is a non-SE gate that behaves like a risk source.** Annual funding creates an implicit funding control gate at every fiscal-year start. These gates are explicitly *not* part of an orderly SE process; they are a source of uncertainty that drives project risk and must be planned around. NASA builds its budget starting roughly each February off the latest President's budget, completes the PPBE planning/programming/budgeting phases by late August, submits to OMB in September, the President transmits to Congress around January, and congressional action often runs through summer — frequently past the October 1 fiscal-year start, forcing operation under a continuing resolution.

## Mental Models

- **The life cycle is a chassis; tailoring is the suspension tuning.** Every project rides the same Formulation/Implementation chassis with the same KDP wheels. Tailoring is how you tune stiffness for the road: a human-rated mission gets the firm, fully-compliant setup; a Type F tech demo gets the soft, heavily-tailored setup. The chassis never changes — what changes is how much each component is allowed to flex.

- **Tailoring removes a "shall"; customization reshapes a "should."** If you are changing *whether* a binding requirement applies, you are tailoring and you need a deviation/waiver in the Compliance Matrix. If you are only changing *how* you meet it, you are customizing and you just document it. Mislabeling the two is the most common governance error: treating a real waiver as mere customization leaves an unapproved gap; treating customization as a waiver buries the team in needless paperwork.

- **Read Table 3.0-1 left-to-right as a maturity ratchet.** Each SE product climbs Preliminary → Baseline → Update across phases and never slides back. A gate's job is to confirm the ratchet has advanced to the marked state — the `**` cells tell you exactly which products *must* be present at that review. If a product is still "Preliminary" where the table says "Baseline," the gate is not ready, regardless of how the meeting goes.

- **Type A–F is a dial, not a label — and you can turn it per aspect.** Resist stamping a whole project "Type C." The guidance explicitly invites tailoring *more* on the simple, risk-tolerant aspects and *less* on the complex, risk-averse aspects of the *same* project. The taxonomy is a starting conversation about where rigor buys safety and where it only buys overhead.

- **The acceptable-risk handshake gates all tailoring.** No relief is legitimate until an acceptable risk posture is understood and agreed by the project, the customer/stakeholder, Center management, and the independent reviewers. Tailoring is downstream of that agreement; without it, tailoring is just cutting corners.

- **Budget gates are weather, not schedule.** You cannot move them and they do not respect your technical readiness. The disciplined SE plans the technical phase gates with the fiscal calendar as a known disturbance — tracking life-cycle cost vigilantly so a development-phase budget squeeze does not silently push cost (and design compromise) downstream into operations.

## Anti-patterns

> These are the failure modes the source itself names or directly warns against; not every section yields one.

- **Letting development-budget pressure push costs into operations.** The source explicitly warns that without vigilance and life-cycle-cost tracking, budget constraints during development lead to compromises in design and to pushing costs down the road — a product cheap to develop can become expensive to operate, maintain, and supply because development was insensitive to operational-phase demands.

- **Tailoring a requirement away when compliance is genuinely cheaper than the risk.** The mirror of legitimate relief: type-2 tailoring (eliminating an "overly burdensome" requirement) is only valid when the *cost of compliance adds more risk than non-compliance*. Invoking it where that math does not hold is removing a control that was earning its keep.

- **Confusing SE-NPR relief with PM-NPR relief.** The source repeatedly cautions that even when the SE NPR needs no waiver (e.g., combining reviews, or folding a plan into the SEMP), the governing project-management directive may still require one. Stopping at the SE-NPR check leaves an unapproved gap against 7120.5/7120.8.

## Key Takeaways

1. **Tailoring and customization are expected SE activities, not exceptions.** The Expanded Guidance treats them as accepted, expected tools for setting the right NPR requirements for any size of program or project — the goal is to keep the benefits while shedding unnecessary overhead.

2. **Know the precise line: relief vs. reshaping.** Tailoring seeks relief from a "shall" and *requires* a deviation or waiver logged in the Compliance Matrix; customization reshapes how a practice satisfies the requirement and needs no waiver (but document the significant cases).

3. **The Compliance Matrix is the auditable spine of every decision.** Every compliance, intent-to-comply, and relief justification lives there, attached to the SEMP, with the right approver — H.1/OCE for Center-wide use, H.2/Center Director for delegated program/project relief.

4. **Eight characteristics calibrate how far you can tailor.** Mission type, criticality to the Strategic Plan, acceptable risk, national significance, complexity, mission lifetime, cost, and launch constraints together set the defensible tailoring envelope; high values on these generally pull the project toward fuller compliance.

5. **Maturity gates are objective, the meeting is not.** Table 3.0-1's `**` cells define which SE products *must* exist and at what maturity for each review; readiness is judged against that ratchet, not against optimism in the room.

6. **The budget cycle is a planned disturbance, not an SE process.** Annual funding imposes an implicit fiscal gate at each year's start, frequently slipping past October 1 into a continuing resolution; the SE plans around it and tracks life-cycle cost so fiscal pressure does not silently degrade the design.

7. **Granular, per-aspect tailoring beats project-wide labels.** Many projects mix complexity levels; tailor harder on the simple/risk-tolerant aspects and lighter on the complex/risk-averse ones rather than assigning one blanket type.

## Connects To

- **NPR 7123.1 (NASA Systems Engineering Processes and Requirements)** — The "shall" statements being tailored, the source of the tailoring/customization definitions, the SE Product Maturity table, and Appendices G (review entrance/success criteria) and H (Compliance Matrices H.1/H.2). This chapter is essentially the operating manual for relief from that NPR.

- **NPR 7120.5 / 7120.7 / 7120.8 / 7150.2 (program/project management directives)** — Define the phase model, gate products, and standalone-document requirements that determine whether a given relief needs a PM-NPR waiver in addition to (or instead of) an SE-NPR one. §3.5 of 7120.5 is the home of the deviation/waiver definitions.

- **NPR 8705.4 (Risk Classification for NASA Payloads)** — The formal anchor for tailoring criteria; converts "how much relief is defensible" into a risk class rather than judgment alone.

- **The SEMP (and its Compliance Matrix attachment)** — The living document where tailoring/customization, rationale, and approvals are recorded each revision; its baseline timing (SRR vs. MDR/SDR by program type) determines when the tailoring story becomes binding. See the handbook's technical-planning treatment for SEMP content.

- **`nasa-se-handbook` ch07–ch16 (life-cycle phase narratives) and ch27 (technical planning)** — The survey-level companion this chapter deliberately does not duplicate; read those for the per-phase activities, products, and reviews, then return here for the tailoring machinery and budget-cycle context.

- **FMR Volume 4 / PPBE process** — The fiscal cadence (planning, programming, budgeting, execution) that frames every technical gate; the SP-2014-3705 Space Flight Program and Project Management Handbook is named as the deeper reference on the life cycle itself.
