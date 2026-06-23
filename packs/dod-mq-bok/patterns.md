# DoD M&Q BoK Patterns & Techniques

Reusable manufacturing-and-quality practices distilled from the DoD M&Q BoK (Version 3.0, July 2025). Each pattern lists When to use / How / Trade-offs. Wording is synthesized, not copied from the source.

## Pattern 1: Inject M&Q at the Front End, Before a Design Exists

**When to use**: at Pre-MDD and MSA, while the solution space is still open and before the Analysis of Alternatives narrows it.

**How**: get an M&Q voice onto the technical IPT early; analyze manufacturing feasibility and quality risk for *each* candidate solution; write producibility and industrial-base considerations into the draft ICD, the AoA Study Guidance, and the inputs to the Materiel Development Decision. Keep the candidate field broad — eliminate concepts only when feasibility analysis genuinely rules them out.

**Trade-offs**: front-loading analysis feels slow when stakeholders want a solution now, but the leverage to influence life-cycle cost is highest here and collapses once the design freezes. Over-narrowing the AoA set early courts the cost-and-schedule penalty the BoK attributes to programs that looked at too few alternatives.

---

## Pattern 2: Walk the Twelve Threads as a Phase Checklist

**When to use**: in every phase, to make sure no M&Q topic area is silently dropped.

**How**: treat the twelve threads (A DoD Acquisition System, B Contracting, C Surveillance, D Technology/Industrial Base, E Design, F Cost/Funding, G Materials, H Process Capability/Control, I Quality Management, J Workforce, K Facilities, L Manufacturing Management/Control) as a recurring scan. For the current phase, walk each thread's Activities, decide which Tasks M&Q leads versus supports, and pull the named Tools and Resources. Tailor — not every thread is heavily active in every phase.

**Trade-offs**: the threads are comprehensive, so applying all twelve to a small or fast-pathway program is overkill; the discipline is in tailoring, not in box-checking. But skipping a thread (commonly Facilities or Workforce) is how late industrial-base surprises arise.

---

## Pattern 3: Set MRL Targets per Phase Event and Manage the Gap

**When to use**: whenever a milestone, design review, or production decision is approaching.

**How**: set the phase-appropriate Manufacturing Readiness Level target (broadly: MRL 4 by Milestone A, MRL 6 by Milestone B / PDR, MRL 7–8 across EMD/CDR, MRL 8 by Milestone C / PRR, MRL 9–10 across production), run a Manufacturing Readiness Assessment against the MRL criteria, and where the target is missed, build a Manufacturing Maturation Plan with resources and a schedule to close the gap. Read every maturity claim against the phase target, never as an absolute.

**Trade-offs**: maturing processes ahead of need costs money and may mature things the program later changes; but entering a phase below its MRL target is the classic source of production cost and schedule breach. Note the source is internally inconsistent on the exact FRP target (MRL 9 vs 10) — treat the higher band as gating the production decision.

---

## Pattern 4: Translate Requirements into Key Characteristics, Then Control Their Variation

**When to use**: from MSA design work onward, and intensively through EMD.

**How**: convert validated KPPs/KSAs into Key Characteristics (and Critical Characteristics where safety or catastrophic failure is at stake) using the Pareto principle — a few features dominate performance. For each KC, identify the Key Manufacturing Process that drives its variation, set a capability goal (AS9103 names Cpk ≥ 1.33 unless the customer specifies otherwise), generate data, run Statistical Process Control to confirm the process is both capable and in control, and stand up a Variability Reduction Program (Process Control Plans, FMEA, Six Sigma, DMAIC). Flow KCs down to subcontractors and into the Verification Cross-Reference Matrix.

**Trade-offs**: identifying and controlling every characteristic is uneconomical — the value is in focusing scarce SPC and tooling effort on the vital few KCs/CCs. Under-selecting KCs leaves real variation uncontrolled; over-selecting dilutes attention and inflates inspection cost.

---

## Pattern 5: Demonstrate Manufacturing Maturity on a Pilot Line Before Committing to Rate

**When to use**: in late EMD, before the Production Readiness Review and the move to LRIP.

**How**: progress from a production-representative environment (pre-CDR, as realistic as design maturity allows) to a pilot line that incorporates *all* production-realism elements — production equipment, trained personnel, real materials and components, work instructions, tooling, and environment — using Full-Rate-Production processes to the maximum practical extent. Use First Article Inspection/Test to prove processes are stable, in control, and repeatable before scaling the rate.

**Trade-offs**: a faithful pilot line is expensive and slows the schedule, but skipping it pushes process discovery into rate production, where defects multiply across the whole lot and rework is far costlier.

---

## Pattern 6: Run M&Q Risk Through the RIO Process and Let an ITRA Check It

**When to use**: continuously, with formal independent checks at the milestone gates.

**How**: use the DoD Risk, Issue, and Opportunity five-step process (Planning, Identification, Analysis by likelihood × consequence, Mitigation by accept/avoid/transfer/control, Monitoring) as the engine for manufacturing, materials, supply-chain, and industrial-base risk; feed the outputs into the SEP, TEMP, and Acquisition Strategy. Expect an Independent Technical Risk Assessment (following DTRAM) at Milestones A/B/C and the FRP decision — and remember it renders an *independent* judgment that may not track the raw MRL/TRL numbers.

**Trade-offs**: parallel program and independent risk views add coordination and can disagree; but a self-assessed risk picture with no independent challenge is exactly what the ITRA mandate exists to backstop.

---

## Pattern 7: Tie Surveillance and the Supply Chain to Process Evidence, Not End-Item Inspection

**When to use**: throughout contract execution, especially as production scales and visibility drops below the first tier.

**How**: delegate Contract Administration Services to DCMA where authority and expertise exist (via MOA/LOD/QALI), and adopt DCMA's Detection-to-Prevention posture — verify process capability and management-system health with data rather than re-inspecting end items. Push KC control, AS9100/AS6500 conformance, and counterfeit-avoidance requirements (AS5553, AS6174) down the supply chain, and assess single points of failure (sole/single/fragile/foreign sources) against the NTIB.

**Trade-offs**: process-based surveillance demands more up-front data infrastructure and supplier engagement than spot inspection, and a conforming management system still does not guarantee a conforming product — so audits must reach actual process and product evidence, not just certificates.

---

## Pattern 8: Govern Sustainment with the LCSP and Watch O&S Cost

**When to use**: after IOC, throughout Operations and Support.

**How**: maintain the Life Cycle Sustainment Plan (refresh it when the support strategy changes or at least every five years), structure the support package around the twelve Integrated Product Support Elements, and use the In-Service Review and periodic Independent Logistics Assessments to track readiness, technical health, and — explicitly — O&S cost growth. Manage diminishing-manufacturing-sources (DMSMS) and obsolescence proactively through materials management and parts management (SD-19, SD-22).

**Trade-offs**: sustainment governance is long-running overhead on a fielded system, but O&S typically dominates total life-cycle cost, so under-investing here is where the largest avoidable costs accumulate.
