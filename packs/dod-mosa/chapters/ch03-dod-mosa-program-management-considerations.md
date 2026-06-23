# Chapter 3: Program Management Considerations — Plan, Modularize, and the Interface Lifecycle

> Authority note: This chapter reflects the current DoD guide *Implementing a MOSA in DoD Programs*, which supersedes the 2013 Open Systems Architecture (OSA) guidebook. Where older OSA-era guidance conflicts, treat this guide as the governing reference.

## Core Idea
Adopting a Modular Open Systems Approach is not a bolt-on technical choice — it is a program-management discipline that the PMO must plan, fund, and sustain across the whole acquisition life cycle. Before committing, a program should run a cost-benefit analysis that weighs MOSA's long-term advantages against its risks and its impact on cost and schedule, and that compares alternative courses of action. Once committed, the PMO works a repeatable framework — plan, identify, define, manage, and verify the compliance of system interfaces — and then threads MOSA into every governing acquisition document so the strategy becomes a contractual obligation rather than an aspiration. The unifying thread is the interface: modules are only as open as the interfaces between them are clear, standardized, and maintained.

## Frameworks Introduced

- **Cost-benefit / cost analysis for MOSA adoption** — the decision-support analysis a program runs *before* committing to MOSA. It pairs the expected benefits against a frank discussion of risks and of effects on program cost and schedule, and it evaluates alternative courses of action.
  - When to use: at the front of the decision, so long-term advantages are not lost in near-term cost pressure; the guide frames this as a way to reach more affordable programs and less costly fielded systems.

- **MOSA Planning Framework (Figure 3-1)** — the guide's recommended sequence of steps for handling interfaces: *plan → modularize → identify interfaces → define interfaces → standardize interfaces*, set inside the broader obligation to plan, identify, define, manage, and ensure interface compliance. Each program is expected to author its own way of documenting or modeling the framework rather than inheriting a fixed template.
  - When to use: from the start of, and continuously throughout, the acquisition life cycle; it should capture every internal and external interface requirement consistent with the program's Acquisition Strategy, and it must be maintained, not produced once and shelved.

- **JCIDS integration for MOSA** — the practice of carrying MOSA into the Joint Capabilities Integration and Development System so the approach is applied consistently from inception and across all mission elements. MOSA is expected to surface in the JCIDS outputs — among them the CBA (Capabilities-Based Assessment), the ICD (Initial Capabilities Document), and the CDD (Capability Development Document) — per CJCSI 5123.01.
  - When to use: even before a formal program and program office exist — MOSA should already be a consideration for candidate materiel solutions.

- **Statutory and policy documentation set** — the mandated acquisition activities and documents that, under 10 U.S.C. 4401–4403, DoDI 5000.85, and DoDI 5000.88, must address MOSA. The required set spans the Analysis of Alternatives (or Economic Analysis), the Request for Proposal, the Systems Engineering Plan, the Acquisition Strategy, and the Program Capability Document (CDD).
  - When to use: as the program steps through the Adaptive Acquisition Framework; the guide ties each document to its statute or instruction so the MOSA content is auditable.

- **Supporting documentation set ("address as appropriate")** — the second tier of artifacts that should reinforce MOSA without being the primary mandate: Product Support Strategy, Life Cycle Sustainment Plan, performance specifications (System Performance Specification / SRD and System/Subsystem Specification), system architecture products, contract documents (CWBS, CDRLs, IDD/SRS CDRLs, V&V checklists), and the interface documents — Interface Control Document and Interface Requirements Specification.
  - When to use: as each artifact is produced, so sustainment, specifications, architecture, and contract data all pull in the same direction as the MOSA.

## Key Concepts

### The five interface-lifecycle steps
- **Plan**: define MOSA objectives that align with both technical and business goals, expressed as specific, measurable, achievable targets tied to the system's near- and long-term needs (for example, greater flexibility, lower life-cycle cost, faster insertion of new technology). Planning then identifies the needed resources — technology and talent — and establishes or adopts governance frameworks and procedures that keep modular development consistent and interoperable.
- **Modularize**: decompose system capabilities into smaller, self-contained functional modules, each owning one function or capability. Isolating functions lets modules stay independent yet interoperable, so upgrades, replacements, and technology insertions can happen without disrupting the whole system. Every module needs clearly defined interfaces; the payoff is simpler design plus better maintainability and adaptability.
- **Identify Interfaces**: locate the boundaries through which modules exchange data, signals, or commands. Specifications should be clear, standardized, and compatible with open standards so modules interoperate regardless of origin or designer, and they should be robust enough for the required data flow yet flexible enough for future change.
- **Define Interfaces**: turn identified interfaces into explicit protocols and data formats that adhere to open standards, enabling cross-vendor interoperability. Well-defined interfaces let modules be developed, tested, and upgraded independently without breaking the larger system, and they should be both robust and flexible enough to absorb later enhancements.
- **Standardize Interfaces**: lock the interface specifications to consistent, open standards so modules can be upgraded, replaced, or enhanced without reworking the whole system. Standardization eases insertion of new technology, reduces lock-in to any single vendor, and — by fostering competition among suppliers — both accelerates innovation and extends the system's usable life.

### Where MOSA lives in acquisition
- **Pre-program**: MOSA is a consideration for candidate materiel solutions before a formal program office stands up; it should be woven into JCIDS and its outputs (CBA, ICD, CDD).
- **Post-establishment**: once the program exists and the PM completes the planning framework, the PM must carry MOSA and its strategy into acquisition and contracting so requirements become formal contract obligations and the interests/goals of Government and industry are balanced (Appendix B lists industry recommendations).
- **AoA / Economic Analysis**: a comparison of operational effectiveness, suitability, and life-cycle cost across alternatives that meet the capability need, initiated after the Materiel Development Decision to guide the Materiel Solution Analysis phase. Each alternative's assessment should include how MOSA would be implemented for that option.
- **RFP**: both the technical and the non-technical tenets of the MOSA implementation must be made clear to bidders so offers align to MOSA needs; the level of detail in every key bid material should be consistent with the MOSA intent (Appendix C gives contracting considerations and sample language).
- **SEP**: defines the technical approach, applying MOSA to the maximum extent practicable, describes architectures including all hardware and software modular system interfaces, and provides rationale where MOSA is not feasible or cost-effective (SEP Outline v4.1).
- **Acquisition Strategy**: describes how MOSA will be used (business and technical), differentiates the major system platform from major system components (including components developed outside the program for integration), lays out the capability evolution planned across increments, identifies major system components that may be added later, addresses intellectual property and technical-data deliverables, and covers system integration and configuration management for the relevant cyber-threat environment.
- **Program Capability Document (CDD)**: expresses capability requirements as KPPs, KSAs, and APAs, and should present MOSA as an enabler for achieving them.

### The interface as the unit of openness
- An interface is the boundary across which modules trade data, signals, or commands; getting it standardized and open is what makes interoperability and integration real.
- Among supporting artifacts, the **Interface Control Document (ICD)** and **Interface Requirements Specification (IRS)** are singled out as especially important for capturing MOSA detail and defining how components interact through standardized interfaces.

## Mental Models
- **Decide before you build, then never stop maintaining.** The cost-benefit analysis is a gate at the front; the planning framework is a living artifact maintained across the life cycle, not a one-time deliverable.
- **The five steps are a pipeline, not a menu.** You plan, then modularize, then identify, define, and standardize the interfaces — each step assumes the previous one is done. Skipping "define" or "standardize" leaves you with modules that are nominally separate but not actually swappable.
- **A module is only as open as its interface.** Independence comes from the interface contract, not from drawing a box around a function. Clear, open, standardized interfaces are what let a module be upgraded or replaced without touching the rest of the system.
- **Standardization is a vendor strategy, not just a technical one.** Open, standard interfaces reduce dependence on any single supplier and open the door to competition — that is where lower cost and faster innovation actually come from.
- **MOSA is real only when it is contractual.** Until MOSA requirements are translated into formal contract obligations through the RFP and Acquisition Strategy, the strategy is intent, not commitment.
- **Trace MOSA through the document chain.** From JCIDS outputs (CBA/ICD/CDD) to AoA, RFP, SEP, Acquisition Strategy, CDD, and on into sustainment, specification, architecture, contract, and interface documents — MOSA should be visible and consistent at each step.

## Key Takeaways
1. Run a **cost-benefit analysis** before committing to MOSA — weigh long-term advantages against risks, cost, schedule, and alternative courses of action.
2. Work the **MOSA Planning Framework**: *plan → modularize → identify → define → standardize* interfaces, and keep it maintained across the entire life cycle.
3. **Modularize** by function into self-contained, independent-yet-interoperable modules, each with clearly defined interfaces.
4. The **interface lifecycle** — identify, define, standardize — is where openness is won or lost; open, standardized specifications enable upgrades, reduce vendor lock-in, and extend system life.
5. Carry MOSA into **JCIDS early** (CBA, ICD, CDD) — even before a program office exists.
6. MOSA is **mandatory content** (10 U.S.C. 4401–4403; DoDI 5000.85; DoDI 5000.88) in the AoA/Economic Analysis, RFP, SEP, Acquisition Strategy, and CDD, and should be reinforced in the supporting documentation set.
7. The **ICD and IRS** are the high-value interface artifacts for documenting how standardized interfaces actually work.
8. MOSA becomes binding only when it is **translated into formal contract obligations** that balance Government and industry interests.

## Connects To
- **ch01 / ch02 (this pack)**: the MOSA tenets and definitions that the planning framework operationalizes.
- **`dau-se-guidebook` pack — SEP and technical baselines**: the SEP that must define the MOSA technical approach is the same plan that documents review timing and baselines; modular interfaces map onto the functional/allocated/product baselines established at SFR/PDR/CDR.
- **`dau-se-guidebook` pack — Acquisition Strategy / AAF tailoring**: incorporating MOSA into the Major Capability Acquisition Acquisition Strategy and tailoring planning documents across the Adaptive Acquisition Framework (DAU AAF guidance).
- **JCIDS / CJCSI 5123.01**: the requirements process whose outputs (CBA, ICD, CDD) must carry MOSA from inception.
- **Statute and policy**: 10 U.S.C. 4401–4403 / 4402 / 4324, DoDI 5000.85, and DoDI 5000.88 — the legal and policy basis that makes MOSA documentation mandatory.
- **Interface management / configuration management**: the ICD and IRS, plus configuration-management approach in the Acquisition Strategy, govern how standardized interfaces are controlled over time.
