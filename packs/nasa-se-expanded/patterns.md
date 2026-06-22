# Expanded Guidance for NASA Systems Engineering — Patterns & Techniques

Reusable practitioner patterns drawn from the *Expanded Guidance for NASA Systems Engineering* (NASA/SP-2016-6105-SUPPL). Each has When / How / Trade-offs. These are the *expanded* mechanics — the operating procedures the base handbook only names.

## Pattern 1: Stamp the SE Engine onto Every Product, Re-run Per Phase

**When to use**: whenever you decompose a system into a product hierarchy and march it through the life cycle.

**How**: treat the 17-process engine as a template you re-instantiate at each tier — every product "resets to process 1" and runs its own full pass with stakeholders inherited from the tier above. Re-run the engine with a phase-specific cadence: development processes (1–9) fire across five engine cycles (Pre-Phase A → D); technical-management processes (10–17) fire across seven (Pre-Phase A → F). Split Phases C and D so the left side (design) runs in C and the right side (realization) in D.

**Trade-offs**: stamping the engine everywhere feels repetitive, but skipping a tier's stakeholder/requirements pass because "we already did it" confuses recursion with iteration and orphans that tier's expectations. Running realization before design has produced something buildable jumps sides too early.

---

## Pattern 2: Iterate to Fix, Recurse to Move

**When to use**: any time you re-run a process and need to know which kind of re-run it is.

**How**: classify the re-run. Same product, correcting a found discrepancy → **iterate**. Moving to the next lower design layer, the next upper realization layer, or a later life-cycle phase → **recurse**. The label tells you whether you are repairing or advancing.

**Trade-offs**: the distinction costs a moment of classification, but conflating them hides whether you are making progress (recursion) or fixing rework (iteration) — and that confusion corrupts schedule and maturity reporting.

---

## Pattern 3: Tailor a "Shall", Customize a "Should"

**When to use**: right-sizing NPR 7123.1 to a program/project of any class.

**How**: decide whether you are changing *whether* a binding requirement applies or only *how* you meet it. Changing applicability → **tailor**: produce a deviation/waiver and log it in the Compliance Matrix (H.1/OCE for Center-wide, H.2/Center Director for program/project). Changing the practice depth → **customize**: no waiver needed; document significant cases in the SEMP. Anchor "how much relief is defensible" in a risk classification (NPR 8705.4) and the eight tailoring characteristics, not opinion. Check the *governing PM directive* (7120.5/.7/.8, 7150.2) separately — it may demand a standalone document even when the SE NPR does not.

**Trade-offs**: mislabeling a real waiver as mere customization leaves an unapproved compliance gap; mislabeling customization as a waiver buries a small project in needless paperwork. Stopping at the SE-NPR check misses PM-NPR relief obligations.

---

## Pattern 4: Run the System-Design Loop as a Consistency Clamp

**When to use**: in every "create concepts" turn from Pre-Phase A through Phase C.

**How**: force three artifacts into mutual agreement — a strawman architecture/design, its matching ConOps, and the derived requirements — and don't stop when each is individually written. Stop when moving any one no longer forces a change in the other two *and* the clamped assembly passes three blunt validation questions: will it work as expected, is it achievable in budget/schedule, and does it deliver the functionality that justified the funding. Calibrate decomposition depth to one bar: deep enough that an independent review team would judge the design feasible and credible, and deep enough to support cost and operations modeling.

**Trade-offs**: inconsistency is the normal state and the iteration is the work — accepting that costs effort up front, but baselining a still-inconsistent triad ships contradictions downstream. Decomposing past the feasibility bar burns schedule for no return.

---

## Pattern 5: Route Every Requirement by Flow, Type, and Ownership

**When to use**: writing, changing, or waiving any requirement.

**How**: classify by origin (directorate-imposed / program-imposed / self-derived), by type (programmatic vs. technical), and by owner. Programmatic requirements — and their waivers — belong to the program/project; technical requirements belong to the Technical Authority. Populate the per-requirement metadata (ID, rationale, traced-from, owner, verification method/lead/level). Distinguish a legitimate self-derived requirement (seek concurrence from the next level up) from gold-plating (eliminate it). Apply standards in their order of authority: law, then voluntary consensus, then other government, then NASA standards.

**Trade-offs**: the routing discipline slows the first edit of any requirement, but sending a change or waiver to the wrong authority breaks change control, and retaining orphaned "shall" statements gold-plates the system.

---

## Pattern 6: Hold V&V Apart, Then Exploit the Overlap

**When to use**: planning and running the realization (right-side) processes.

**How**: keep verification ("built right", traces to requirements, instrumented/controlled) and validation ("right thing built", traces to the ConOps, realistic environment, typical users) as separate gates with separate baselines. Then deliberately share configurations and events so one rig answers both where possible. Sort each activity by its cardinality clock — verify, qualify, and certify once per design; accept once per unit (and remember certification is an *audit* of evidence, not a test). Convert tests you already label "functional"/"engineering" into credited validation by preplanning them in the V&V Plan, running them in a relevant environment, and recording them formally.

**Trade-offs**: maintaining two gates is more planning than one combined "test phase," but a product can pass verification and still fail validation when the requirements faithfully captured the *wrong* need. Leaving real validation uncredited forfeits its cost-saving and stakeholder-assurance value.

---

## Pattern 7: Engineer Interactions, Not Assemblies

**When to use**: from concept development through integration, operations, and de-integration.

**How**: model the system as the set of flows across interfaces (mechanical, fluid, thermal, electrical, data, logical, human), not the set of boxes. Begin integration engineering at concept, not at hardware arrival. Continuously balance subsystem-to-subsystem and subsystem-to-environment interactions to optimize the *system* (the "elegant" system), resisting over-optimization of any one subsystem. Engineer de-integration and disposal in from the start — disposal capability is a design requirement.

**Trade-offs**: front-loading interface engineering competes for early cost/schedule, but the surprises — intended and unintended — live in the interactions, and verifying the parts is explicitly *not* sufficient to conclude the integrated whole works.

---

## Pattern 8: Make "Test the Way We Fly" a Coverage Discipline

**When to use**: building and running the end-to-end V&V program.

**How**: turn the slogan into mechanics — inject prioritized faults to cover the fault space without combinatorial blowup; stand up a skeleton early with stubbed/simulated items; put a fresh-eyes operator (uninvolved in the testing) at the controls to surface requirement misses; rerun regression after every fix; authenticate the test-environment fidelity and document any test-vs-operational differences; and fall back to piecemeal-plus-analysis only where true end-to-end is impossible (e.g., on-orbit-assembled systems). Keep scope at the external-interface level down to the verification-plan's designated level.

**Trade-offs**: this discipline is more expensive than an ad-hoc "run it once" test, but an unauthenticated environment quietly undermines every result, and insiders go blind to off-nominal responses a fresh operator catches.

---

## Pattern 9: Build Schedules in Six Steps and Expect to Replan

**When to use**: establishing the network schedule for each lowest-available WBS element.

**How**: (1) identify activities and dependencies as workflow diagrams; (2) **negotiate** external dependencies — agree content, format, and labeling of cross-WBS receivables/deliverables; (3) estimate durations and write the basis of estimate; (4) load a scheduling tool for the element critical path, iterating and adding reserve to critical-path activities; (5) integrate lower schedules into the project network (folding in holidays/weekends) to expose the project critical path; (6) review workforce and funding profiles and adjust logic/durations until within constraints. Treat replanning as almost always needed.

**Trade-offs**: the negotiation in step 2 and the reserve in step 4 slow the first schedule, but a schedule without negotiated interfaces or float is brittle and produces large baseline-vs-actual variances.

---

## Pattern 10: Match Cost-Estimating Method to Design Maturity

**When to use**: producing or defending a life-cycle cost estimate at any phase.

**How**: run estimation as progressive refinement — **parametric** when only history and a concept exist, **analogous** once a design is baselined but actuals are thin, **engineering/grassroots** once detailed scope and actuals accumulate. Wrap hardware estimates with management/SE/test factors, apply full-cost factors carefully to avoid double-counting in-house vs. contracted scope, normalize constant-year dollars, apply learning curves for repetitive manufacturing, and phase costs with a beta curve (or resource-load the schedule for a JCL). Buy better LCCE information early, because 50–70% of life-cycle cost is committed by architecture selection and up to 90% by preliminary design.

**Trade-offs**: pairing a precise grassroots number to an immature design is false confidence; the source prizes honest uncertainty over spurious precision. But under-resourcing planning forces a project into perpetual change-chasing.

---

## Pattern 11: Assess Every Requirement Change Before Approval

**When to use**: inside the CM process, before a CCB approves any requirement or interface change.

**How**: run the three-tool impact check — a **Performance Margins** list (what slack the change consumes), a **CM Topic Evaluators List** (who must review so all impacts surface), and a **Risk/Threats List** (how the change shifts existing-risk likelihood/consequence or adds new risk). Route the decision and its documentation through the CCB after SRR baseline; bilateral interface changes need unanimous, all-sides approval via PIRN/IRN. Treat late (Phase B/C) changes with harder scrutiny — their cost/schedule impact is far larger.

**Trade-offs**: the three-tool check costs reviewer time per change, but a change accepted in one process view without posting it to interfaces, schedule, cost, and risk is an unbalanced ledger entry discovered later — expensively.

---

## Pattern 12: Manage Risk as RIDM-plus-CRM, Built from Initiating Events

**When to use**: across the life cycle, switching modes by activity.

**How**: use **RIDM** where you are *choosing* — architecture, trades, baseline performance requirements — so risk and uncertainty shape the selection; switch to **CRM** once you are *executing* to drive identified risks to acceptable residual levels against trigger thresholds. Build each risk statement from the **initiating event** outward: chain mitigating/exacerbating events into a scenario, then attach likelihood and consequence with their uncertainties — the triplet is the *output* of that construction, not a template. Don't dismiss programmatic risk (ITAR, partner agreements, congressional/OMB direction, contractor restructuring) just because it originates outside the project.

**Trade-offs**: running CRM where RIDM belongs means managing risks inside a design you never risk-informed; building the triplet from scenarios takes longer than filling a template but is why two engineers' "same risk" finally reconciles.

---

## Pattern 13: Read Margins as Leading Indicators of Maturity *and* Stability

**When to use**: continuously from SRR through SAR, at the rolled-up program/project level.

**How**: report the three NPR 7123.1-mandated leading indicators — **mass margin, power margin, and RFA/RID/action-item burndown** — plotted against allocation and not-to-exceed bands with life-cycle reviews marked on the time axis. Read both signals: a design can be CDR-*mature* yet *unstable* if its requirements are still churning. Track TPMs (planned-profile or margin-management method) against KPPs and selected MOEs/MOPs, and remember performance is judged through earned value (BCWP), never planned-vs-actual spend.

**Trade-offs**: each metric costs effort to collect, so balance metric value against collection cost — but margins read only at the end (lagging) give no time to act, which is the whole point of a *leading* indicator.

---

## Pattern 14: Scope Decision Boards by Information; Scale Rigour to Consequence

**When to use**: designing any decision/control board and choosing how formal the analysis should be.

**How**: treat the board as a communication channel — every information source the decision depends on must be represented (engineering disciplines, SMA, procurement, business office), or the missing information becomes noise and bias. Define each board's scope, cover every affected discipline (including its uncertainties), and **minimize the number of boards** to avoid overlapping scopes. Raise formality when **Complexity, Uncertainty (that could flip the ranking), Multiple Attributes, or Diversity of Stakeholders** are high; otherwise keep it informal. Reduce uncertainty only when doing so is **net beneficial** (could change the ranking *and* the project can afford the schedule slip). Record criteria, alternatives, uncertainties, recommendation, and **dissent** in an archived decision report.

**Trade-offs**: full formal analysis is expensive and slow, so over-applying it wastes resources; under-applying it on a complex, uncertain, multi-stakeholder choice yields a partially informed decision with unintended consequences. Overlapping board scopes drain skilled staff into duplicate representation.
