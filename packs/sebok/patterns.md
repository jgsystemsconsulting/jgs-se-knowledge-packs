# SEBoK Patterns & Techniques

Reusable techniques distilled from the SEBoK v2.14. Each has When / How / Trade-offs. Synthesized for reference use under CC BY-NC-SA 3.0; attribution to the BKCASE Project required.

## Pattern 1: Frame the Problem Before the Solution (Concept Definition)

**When to use**: at the very start of any effort, before architecture, requirements, or technology choices.

**How**: run Business or Mission Analysis to fix the problem space and candidate solution classes, then Stakeholder Needs Definition to produce an integrated set of needs that is correct, consistent, complete, and feasible. Express intent as mission/goals/objectives with Measures of Effectiveness. Only then hand off to System Definition. Distinguish green-field from brown-field and the present-state ("as-is") from the future-state ("to-be").

**Trade-offs**: stakeholders want a solution immediately; investing in the problem feels slow. But solving an unstated or wrong problem is the most expensive mistake in the life cycle, and "how much SE is enough" is a risk-balance, not a fixed amount. (Ch 16, Ch 1)

---

## Pattern 2: Scope the Engineered-System Context, Not the Bare System

**When to use**: whenever you set a system boundary or begin architecting.

**How**: place the system-of-interest inside its engineered-system context — the related engineered, social, and natural systems and environments it touches. Use Hitchins' "Seven Samurai" (context, intervention, realization, deployed, collaborating, sustainment, competing systems) as a checklist so no enabling or competing system is forgotten. Treat narrower vs. wider system-of-interest explicitly.

**Trade-offs**: a wide context is harder to bound and analyse; too narrow a context produces a solution that fails in the field because an enabling, collaborating, or competing system was ignored. (Ch 7, Ch 2)

---

## Pattern 3: Select and Adapt the Life Cycle Model — Don't Inherit One

**When to use**: at project start and whenever context (risk, requirements stability, increment purpose) shifts.

**How**: choose a development approach by three questions — how completely requirements are known up front, whether work is split into increments, and what those increments are for. Map onto sequential / incremental / evolutionary (with agile overlapping), align to ISO/IEC/IEEE 24748-1, and adapt per project using a situation framework (e.g. PMI's context factors / scaling). Re-evaluate continuously.

**Trade-offs**: every real effort is concurrent and iterative to some degree, so the families are reference points, not boxes. Over-fitting a "pure" model to a messy project wastes effort; under-planning the model invites rework. (Ch 10, Ch 12, Ch 9)

---

## Pattern 4: Select and Tailor Processes With Traceable Rigor

**When to use**: when deciding which 15288 processes apply and at what depth.

**How**: select processes from a recognized framework (15288), then tailor with the 24748-2 application strategy; describe every process uniformly per 24774. Balance enough rigor to manage risk against enough agility to avoid waste, and document each tailoring decision so later stakeholders see why the process looks as it does. Expect concurrency, iteration, and recursion, not a serial march.

**Trade-offs**: documenting tailoring rationale costs effort up front but prevents undocumented, unjustifiable process drift; under-tailoring imposes ceremony, over-tailoring strips needed control. (Ch 14, Ch 13)

---

## Pattern 5: Run V&V Down-and-Up the Vee, Not as a Big Bang

**When to use**: across architecture, detailed design, realization, and deployment.

**How**: descend the left of the Vee (architecture definition → detailed design across functional, logical, physical views), then climb the right (implementation → integration → verification → validation → transition → operation). Perform verification and validation concurrently and recursively at each decomposition level. Govern data through an Authoritative Source of Truth where model-based.

**Trade-offs**: level-by-level V&V costs more early instrumentation and discipline, but deferring all V&V to the end concentrates risk where defects are most expensive to fix. (Ch 17, Ch 32, Ch 10)

---

## Pattern 6: Plan Sustainment From Acquisition, Not After Fielding

**When to use**: from stakeholder needs definition onward, for any system with a long operational life.

**How**: define a maintenance concept early and capture initial maintenance requirements during stakeholder needs definition (15288 Cl. 6.4.1). Run maintenance concurrently with operations (Cl. 6.4.9): monitor, record problems, take corrective/adaptive/perfective/preventive action, confirm capability restored. Wrap the maintenance process in a broader sustainment view (product/service life management) covering the twelve integrated product-support elements, LORA, RCM, and life-cycle cost.

**Trade-offs**: designing for sustainment constrains the design and adds early cost; ignoring it produces a system that is unaffordable or unsupportable across the (much longer) operational life. (Ch 18)

---

## Pattern 7: Engineer the Quality Attributes as a Loss-Driven Whole

**When to use**: whenever multiple "-ilities" (safety, security, reliability, resilience, availability) are in play.

**How**: treat the quality attributes as specialty engineering and apply the integration filters to fold specialty constraints into the design. Where attributes share a concern with loss, use a Loss-Driven SE lens — reason about assets, types of loss, types of adversity, and coping strategies once, rather than engineering each "-ility" in a silo. Specify which attributes matter, how each is measured, and how conflicts are traded.

**Trade-offs**: a unified loss view needs cross-specialty coordination and a common vocabulary up front, but isolated specialty work creates conflicting requirements and duplicated effort. (Ch 34)

---

## Pattern 8: Compose, Don't Command, a System of Systems

**When to use**: when constituents are operationally and managerially independent (a true SoS).

**How**: confirm Maier's characteristics first. Architect by managing interfaces and leveraging existing functionality rather than designing a monolith; apply Maier's architecting principles (stable intermediate forms, policy triage, leverage at the interfaces, ensure cooperation). Use the Wave Model for the continually evolving SoSE life cycle and expect socio-technical/socio-economic, not purely technical, work.

**Trade-offs**: you trade central control for partial influence; behaviour can surprise you at the SoS level, so over-specifying constituents is both infeasible and counter-productive. (Ch 24, Ch 23)

---

## Pattern 9: Enable SE at Three Levels Before Expecting It to Perform

**When to use**: when an organization wants SE to deliver value, not just when a project starts.

**How**: enable SE top-down at business/enterprise, team, and individual levels. At enterprise level run a plan-do-check-act loop (strategy → capabilities → organization → assessment → development → barriers → culture). At team level build capability and dynamics (Tuckman stages, IPTs, communication-path arithmetic). At individual level define roles and KSAA competencies, assess gaps, develop them, and hold an ethical frame. Remember competency ≠ performance.

**Trade-offs**: enablement is overhead invisible on any single project, but without it Part 3 techniques cannot deliver; culture, if hostile, can block SE outright and may need transformational change. (Ch 26, Ch 27, Ch 28)

---

## Pattern 10: Make the SE / PM Boundary Explicit Per Project

**When to use**: on every project, because there is no standard SE/PM relationship.

**How**: assign the project manager the programmatic attributes (plans, estimates, schedule, budget, staffing, risk) and the systems engineer the product/technical attributes (requirements flow-down, architecture, integration, V&V, specialty engineering). Decide the split — disjoint, overlapping, or nested — for this project's context, document it in the PMP and SEMP, and communicate frequently across the boundary.

**Trade-offs**: negotiating the boundary takes time and can surface authority tension, but leaving it implicit guarantees gaps and duplicated ownership of the same activity. (Ch 31, Ch 15)
