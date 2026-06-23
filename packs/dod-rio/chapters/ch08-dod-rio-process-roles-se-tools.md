# Chapter — Process and Roles, Integration with SE/PM Tools, and an Implementation Example

> Scope note: This chapter is the DoD-side complement to the `nasa-risk` and `dau-se-guidebook` packs. It captures how a defense acquisition program *institutionalizes* risk, issue, and opportunity (RIO) management — the planning document, the boards and working groups, the tool selection, the tiered roles, the wiring into program-management and systems-engineering artifacts, and a worked end-to-end example. Where NASA's continuous-risk-management canon describes the discipline in agency-neutral terms, this material is grounded in the defense acquisition context (contract types, RFP/proposal flow, milestone authorities, MIL-STD/EIA references). Use it alongside — not instead of — those packs. Every claim below is drawn from Appendices B, C, and D of the DoD RIO Management Guide.

## Core Idea

Risk management only works when a program turns the abstract five-step process into durable institutional machinery: a written plan, named decision bodies, an agreed tool, explicit role assignments at every tier, and tight coupling to the artifacts a program already maintains for cost, schedule, and technical performance. The guide's central argument across these appendices is that RIO management is not a parallel bureaucracy bolted onto the program — it is woven into the work breakdown structure, the schedule, the earned-value baseline, and the technical performance measures, so that mitigating a risk is the same act as funding a work package and tracking it to completion. The implementation example then demonstrates that the whole apparatus exists to serve a single concrete decision: choosing and burning down a mitigation that protects a key performance parameter.

## Frameworks Introduced (exact source names, when/how)

- **Program Risk Management Process (B.1) and the Program Risk Management Plan (PRMP).** The PRMP is the foundational planning document. Programs may keep a combined RIO process document or separate plans, and should deliberately decide whether to combine all three areas. The plan is created at initial program formulation and refreshed at life-cycle intervals — re-baselining, phase changes, developmental/operational testing, sustainment. The guide supplies a recommended PRMP outline: Introduction, Program Summary, Definitions, Risk Management Board(s)/Risk Working Group(s), Roles/Responsibilities/Authorities, Risk Process (the tailorable five-step DoD process), Risk Process in Relation to Other Program Management Tools, Risk Evaluation Techniques, and a Communication and Feedback Process.

- **The tailorable five-step DoD process**, referenced as the methodology the PRMP documents: risk planning, risk identification, risk analysis, risk mitigation, and risk monitoring.

- **Risk Management Board (RMB) and Risk Working Group (RWG) (B.2).** As a senior advisory body, the Government RMB is stood up and usually chaired by the PM. The guide introduces the **Joint Risk Management Board (JRMB)** for common Government–contractor risks (Figure B-1), often co-chaired by the two PMs. It names tiered lower-level boards on large programs, and notes that boards also handling opportunities are sometimes called **risk and opportunity management boards (ROMBs)**. Each RWG operates under a charter and is led by someone drawn from either the Program Management IPT or the Systems Engineering IPT.

- **Service-endorsed risk management tools (B.3).** Three are named explicitly: **Project Recon** (Army-developed, available DoD-wide), **Active Risk Manager** (a commercial tool the Air Force directed for use), and **Risk Exchange** (Navy-developed, hosted on the Naval Systems Engineering Resource Center site). The PM selects the tool early and documents it in the SEP.

- **Tiered Roles and Responsibilities (B.4.3, Figure B-2),** organized as Executive Level (Milestone Decision Authority, PEO), Management Level (PM, Program RMB, IPT RMB/RWG, Risk Manager), and Working Level (IPTs/Sub-IPTs/Working Groups, Risk Owner, Team Members).

- **Integration with PM and SE tools (Appendix C):** the **Work Breakdown Structure (WBS)** with reference to **MIL-STD-881F**; the **Integrated Master Plan (IMP)** and **Integrated Master Schedule (IMS)**; the **Schedule Health Assessment (SHA)** using the **DCMA 14-point schedule metrics** (Table C-1); **Earned Value Management (EVM)** governed by the **EIA-748** industry standard; **Technical Performance Measures (TPMs) and metrics** (required by **DoDI 5000.02**, and to be **SMART** — Specific/Objective, Measurable, Achievable/Observable, Relevant, Timely); and the three analytical analyses — **Schedule Risk Analysis (SRA)**, **Cost Risk Analysis (CRA)**, and **Performance Risk Analysis (PRA)**, the first two commonly driven by **Monte Carlo** simulation.

- **Risk Management Process Implementation Example (Appendix D):** a hypothetical UAV Jammer on the **MCA (Major Capability Acquisition)** pathway, walked through identification, analysis, mitigation, monitoring, and closure, with a risk matrix (Figure D-1), a risk burn-down diagram (Figure D-2), and a multi-risk reporting chart (Figure D-3).

## Key Concepts

**The PRMP defines and tailors, not just records.** The plan must define and tailor the program's identify/analyze/mitigate/monitor process, establish the working structure and responsibilities, document how resources (personnel, schedule, budget) are requested and allocated, define how the process's own effectiveness is monitored, and address integration across contractors, subcontractors, and teammates. Documentation and reporting procedures are set before contract award and amended afterward; updates are triggered by milestones, contract award, system-level technical reviews, Acquisition Strategy changes, re-baselining, or realization of a major risk.

**Contract type bends decision authority.** A cost-type environment generally affords the Government RMB broader latitude to participate with the contractor across investment decisions; in a fixed-price environment the Government RMB largely tracks prime-contractor progress and supports PM duties around GFE and Government testing, and the contractor usually holds decision authority. The guide is explicit that Government direction in a fixed-price setting can trigger a contract modification or claim. This is the defense-specific texture that the agency-neutral NASA material does not carry.

**Tool commonality is a first-class requirement.** The expectation is a common or electronically compatible tool shared by Government and contractor, accessible through an Integrated Data Environment, ideally extended to key subcontractors and external programs — with firewalls and protection of sensitive Government and proprietary data. All three named tools share traceability and embedded reporting, qualitative and quantitative assessment support, and an audit trail.

**Roles are assigned at every tier, with ownership as the linchpin.** The RMB ensures the process runs per the PRMP, validates program-level risks, approves mitigation plans and resourcing, monitors burn-down, decides which risks are program-level/special-interest versus IPT-level, and — critically — ensures **every risk has an assigned owner** to lead plan development and execution. The Risk Manager runs the process and tools, maintains the PRMP and risk register, trains the team, and prepares briefings. The Risk Owner estimates initial likelihood/consequence, builds the mitigation plan (with cost, resource estimates, and fallback plans for high risks), briefs it for approval, and reports progress. Team members identify and submit candidate risks.

**Traceability is the integration mechanism.** The WBS is the checklist that guarantees every task is examined for risk; approved risks are entered in the register and linked to the work packages funding their mitigation. In-scope mitigation goes into the IMS for consistent progress measurement; out-of-scope or new mitigation may require new resource-loaded work packages. Major program-level risks belong in the IMP, and mitigation resources are reflected across IMP, IMS, and EVM baselines. The expectation statement makes traceability between mitigation activities and the WBS/IMP/IMS/TPMs an explicit deliverable.

**Schedule quality gates the analysis.** Before running an SRA, the program assesses IMS health (a single hard constraint can corrupt SRA outputs). The DCMA 14-point metrics (logic, leads, lags, relationship type, hard constraints, high duration, high float, negative float, invalid dates, resources, missed tasks, critical path test, CPLI, BEI) provide the structural-integrity check, each with a stated goal (e.g., negative float = 0 tasks, CPLI and BEI ≥ 95%).

**The analyses produce indicators, not verdicts.** An SRA result is best read as an indicator of likely schedule progression absent further mitigation — useful for "what-if" evaluations and prioritizing mitigations — rather than a definitive forecast. Outputs include histograms (a probability density approximation), S-curves (cumulative distribution), probabilistic critical path, and sensitivity analysis. CRA mirrors this with histograms and S-curves; EVM estimates at completion should be cross-checked against risk analysis results. PRA is engineering-discipline-specific and spans examples from AoA and ballistic testing to probability of kill.

## Mental Models

- **The risk register is a join table, not a side ledger.** Its rows link to WBS work packages, IMS tasks, IMP events, and TPMs. If a mitigation cannot be traced to a funded work package and a schedule activity, it is aspiration, not management.

- **Boards as a nested authority lattice.** Authority and visibility flow up the tiers (Working Level → Management Level → Executive Level) while delegated decision-making pushes down. Lower-level boards must hold both the authority *and* the resources to execute within their scope, and the program must retain recurring visibility into what they decide.

- **Mitigation = a planned descent on the matrix.** A controlled risk is expected to move in discrete steps across the likelihood/consequence matrix as quantitative metrics are met. The burn-down diagram is the projection of that descent over time, with each step tied to a measurable demonstration event.

- **The KPP as the gravitational center.** In the example, the entire mitigation apparatus orbits a single threatened key performance parameter. The "why" of every board meeting, tool entry, and TPM is ultimately to protect (or knowingly trade) that parameter.

- **Tool commonality as a shared coordinate system.** When Government and contractor work in the same (or interoperable) tool through a shared data environment, risk data moves without translation loss — the precondition for a JRMB to function on mutual risks.

## Anti-patterns

The source frames its cautions as positive expectations and pitfalls rather than named anti-patterns; the following are the failure modes it explicitly flags:

- **Letting incompatible tools fragment the data.** If Government and contractor use different tools, the guide insists they must be capable of seamlessly exchanging data and that the transfer mechanism be described — otherwise commonality is lost.

- **Treating out-of-contract risks as out of mind.** The guide warns that a development contractor may not identify a production risk; the program must recognize such risks are still valid and capture them regardless of contract scope.

- **Running an SRA on an unhealthy schedule.** The guide explicitly cautions that a single hard constraint can produce erroneous SRA results, so the IMS must be assessed against the DCMA criteria first.

## Key Takeaways

- The **PRMP** is the program's institutional contract with itself for RIO management — created at formulation, refreshed at life-cycle events, and structured to the guide's recommended outline; the same principles extend to issues and opportunities.
- **Boards and working groups** give the process decision authority: the PM-chaired RMB, optional JRMBs for mutual risk, tiered lower-level boards (sometimes ROMBs), and chartered RWGs led from the SE or PM IPT.
- **Tool selection is an early, documented decision** (in the SEP), favoring a common or interoperable tool — Project Recon, Active Risk Manager, or Risk Exchange — accessible through an Integrated Data Environment.
- **Roles are assigned across three tiers**, with the non-negotiable rule that every risk has an owner; the Risk Manager runs the machinery and the register.
- **Integration with WBS, IMP, IMS, EVM, and TPMs** is what makes mitigation real — traceable, resourced, and measurable — governed by MIL-STD-881F, EIA-748, and DoDI 5000.02, with TPMs kept SMART.
- **SRA, CRA, and PRA** (Monte Carlo for the first two) are analytical aids whose outputs are decision indicators, gated by schedule health (DCMA 14-point / SHA) and cross-checked against EVM.
- The **UAV Jammer example** shows the loop closing end to end: a KPP-threatening (4,5) risk on ram-air-turbine power, a controlled parallel-magnet mitigation chosen over three alternatives, a three-event burn-down (H1 field strength → KWb bench power → KWf in-flight power) projected to (1,5), tracked in the IMS, register, and EVM, and closed on successful flight test.

## Connects To

- **`nasa-risk`** — the agency-neutral continuous-risk-management discipline this chapter operationalizes for defense acquisition; read NASA's identify/analyze/plan/track/control loop alongside this guide's five-step process and PRMP machinery.
- **`dau-se-guidebook`** — the systems-engineering process backbone; the RWG's home in the SE IPT, the SEP-documented tool and TPM selections, technical reviews, and trade-off analyses all live in that pack's territory. This chapter is the DoD-side complement, not a replacement.
- **Within this pack:** the five-step process chapters (the methodology the PRMP documents), the risk-matrix and likelihood/consequence material (the analysis basis for the (4,5)→(1,5) descent), and the issue/opportunity treatment (which the PRMP and ROMBs extend the same principles to).
- **External standards named in the slice:** MIL-STD-881F (WBS), EIA-748 (EVM), DoDI 5000.02 (TPMs), the DCMA 14-point schedule metrics, and the MCA acquisition pathway.
