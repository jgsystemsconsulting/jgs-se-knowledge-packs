# DoD RIO Management Guide — Patterns & Techniques

Reusable techniques drawn from the RIO guide, each with *when to use*, *how*, and
*trade-offs*. These are the concrete moves a program office makes; the underlying
likelihood/consequence theory lives in `nasa-risk`.

---

## 1. Write a structured risk statement (event + consequence + cause)

- **When**: every time a candidate risk is raised, before it reaches the RMB.
- **How**: state the potential *event*, its *consequence(s)* to cost/schedule/performance,
  and the contributing *circumstance/cause* if known — often in "if–then" form. Use one
  consistent format program-wide. Exclude any mitigation or solution from the statement.
- **Trade-offs**: rigid format prevents vague, drifting statements but takes discipline to
  enforce; embedding a mitigation (a common error) corrupts later scoring. (ch02)

## 2. Score with 1–5 ordinal scales, max-of-three on consequence

- **When**: during analysis, after identification.
- **How**: rate likelihood 1–5 (Table 2-2 bands) and consequence 1–5 (tailored from Table 2-1),
  taking the *single worst* of cost/schedule/performance as the consequence score, assessed as
  if the risk were *fully realized with no further mitigation*. Use fully burdened costs. A
  KPP/APB threshold breach forces a Level-5 performance rating.
- **Trade-offs**: ordinal scoring keeps risks comparable but tempts fractional precision
  (2.4) — which the guide bans. Scoring unmitigated is counter-intuitive but protects the
  baseline rating from optimism. (ch02)

## 3. Classify by category to assign ownership

- **When**: at identification, to decide who works the risk.
- **How**: tag each risk Technical (→ Technology / Engineering / Integration), Programmatic
  (within PM/PEO control), or Business/External (outside program control). PM works
  controllable risks directly and escalates External ones up the chain with contingency plans.
- **Trade-offs**: a single risk often spans categories (technical cause → cost/schedule
  effect); pick the dominant one rather than forcing exclusivity. (ch02)

## 4. Choose one of four mitigation options

- **When**: once a risk is analyzed and prioritized.
- **How**: pick **Accept** (Watch Item — track, pre-identify the resources needed if realized),
  **Avoid** (alternate path/defer — only if the system would ship without it anyway), **Transfer**
  (MOA/MOU to another party — never fully removes Government exposure), or **Control** (drive
  likelihood/consequence down via prototyping, parallel efforts, DOE, M&S, demos, process
  proofing), or a hybrid.
- **Trade-offs**: Transfer is hardest (depends on an outside party); Avoid by deferral risks
  pushing hard problems downstream; Control is default but must produce *real* reduction, not
  relabeled baseline work. (ch03)

## 5. Build a six-step burn-down plan

- **When**: for all high/moderate risks and selected low risks being controlled.
- **How**: (1) sequence activities with realistic precedence; (2) make each *objective and
  measurable*; (3) assign each a planned likelihood/consequence; (4) estimate start/finish;
  (5) load into the IMS; (6) chart risk level vs. time (Fig. 2-8).
- **Trade-offs**: forces measurable milestones (a "perform a test" activity fails; "brassboard
  meets threshold, user-approved" passes) — **meetings do not burn down risk, results do**.
  Front-load high-*consequence* risks so they retire (or force change) while there is still
  schedule to react. (ch03, ch08)

## 6. Manage issues on the consequence axis only

- **When**: an event has occurred or is certain (probability = 1).
- **How**: skip likelihood scoring; score consequence against the same criteria; assign an RMB
  owner; correction options are mainly **Ignore** (after a business-case analysis) or **Control**;
  plan a corrective action (POA&M) with an EAC in the IMS; re-assess for new spawned risks.
- **Trade-offs**: the cleanest risk-vs-issue test is "is it still uncertain?" — but pre-position
  corrective plans for high-likelihood antecedent risks so the plan exists before the issue lands. (ch03)

## 7. Run opportunity management as the upside mirror

- **When**: continuously, to reach should-cost rather than merely stay within will-cost.
- **How**: run the six-activity loop (plan → identify → analyze [business case] → decide → monitor →
  feedback); decide Pursue / Defer / Reevaluate / Reject on benefit-vs-risk; log in the opportunity
  register; push pursued ones into the IMS and their residual risk into the risk register.
- **Trade-offs**: spending effort *raises* the likelihood of a good event (the inverted lever vs.
  risk). Aggregate many small low-disruption wins; reject short-term-gain/long-term-loss candidates;
  deeper analysis can flip a first-pass business case. (ch04)

## 8. Contain cross-program / interface risk

- **When**: a system depends on hardware/software/schedules controlled by other programs.
- **How**: appoint a designated technical authority over interfaces; bind parties with MOAs carrying
  cost/schedule/performance *tripwires*; stand up an ICWG; use ICDs/IRSs, synchronized schedules,
  an integration plan, and giver–receiver deliverables tracked in the IMS. Escalate early up
  PM → PEO → SAE → DAE; refer requirements disputes to the CSB. Reconcile SWAP-C across interfaces.
- **Trade-offs**: interfaces are owned by no one by default, so explicit authority and tripwires are
  what keep the risk from falling through the seam between portfolios. (ch04)

## 9. Tailor RIO to the AAF pathway

- **When**: at pathway selection — the pathway pre-sets the risk posture.
- **How**: UCA accepts deficiencies for speed (ends in disposition analysis); MTA fails early and
  descopes (hold the operational demo a year before completion for margin); MCA front-loads risk
  decisions, picks the entry milestone by where risk lives, burns down Technology/Engineering/
  Integration risk in TMRR while money is cheap, and gates with SETRs (ASR/SRR/SFR/PDR →
  CDR/TRR/SVR/FCA/PRR → OTRR/IOT&E/PCA) plus TRA/MRA/SRA. Software builds the automated pipeline up
  front (MVP→MVCR, User Agreement, technical-debt tracking); DBS uses fit-gap and ATP gates; Services
  put the risk in the requirement (ARRT → PWS/QASP, CPARS). Contract type follows the risk profile.
- **Trade-offs**: pathway choice itself is a risk decision; tailoring is fine adjustment within a
  pre-set dial, not a fresh calibration each time. (ch05, ch06)

## 10. Layer in specialized methods and funnel them back

- **When**: at the points where general RIO won't surface a risk class — cyber authorization,
  mission cyber effects, Agile delivery, digital-engineering model risk, independent technical risk.
- **How**: run RMF (DoDI 8510.01; seven steps; Assess Only below system level; tier per NIST SP
  800-39), MBCRA/CTT (DoDI 5000.89) for mission-framed cyber, Agile metrics (Size/Time/Effort/
  Defects), FMECA on the digital model (DoDI 5000.88), and ITRA/DTRAM (eight areas × seven factors).
  Each is a sensor in its own silo — map its output back into the enterprise register with a common
  consequence language; roll micro-risks up and decompose macro-risks down.
- **Trade-offs**: specialized methods carry their own (lower-fidelity) scales; the integration work
  is deliberate mapping, not automatic. The *implementation/testing* of the controls is itself a
  program risk to weigh. (ch07)

## 11. Institutionalize via PRMP, boards, tools, roles, and traceability

- **When**: at program formulation; refresh at re-baselining, phase changes, T&E, sustainment.
- **How**: write the PRMP to the recommended outline; stand up the RMB (PM-chaired; JRMB for mutual
  risk; chartered RWGs from the SE/PM IPT); select a common/interoperable tool early and document it
  in the SEP (Project Recon / Active Risk Manager / Risk Exchange); assign roles across Executive/
  Management/Working tiers with the non-negotiable rule that **every risk has an owner**; trace each
  mitigation to a funded WBS work package, IMS task, IMP event, and TPM. Gate SRA on DCMA-14-point
  schedule health; read SRA/CRA/PRA outputs as indicators, not verdicts.
- **Trade-offs**: traceability is what makes mitigation real — a mitigation not tied to a funded work
  package and a schedule activity is aspiration, not management. Contract type bends who holds
  decision authority (fixed-price Government direction can trigger a mod/claim). (ch08)
