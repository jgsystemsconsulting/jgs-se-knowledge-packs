# Chapter — Foundations: System Safety Policy, Process, and Principles

## Core Idea

In the FAA's framing, system safety is not a separate discipline bolted onto engineering — it is a specialty *within* systems engineering that exists to support program risk management. The whole point is to optimize safety: find the risks that matter, then eliminate or control them through design and procedure, in a defined order of preference, across every phase of a system's life. The FAA's *System Safety Handbook* (SSH, dated December 30, 2000) was written to teach FAA personnel and their contractors *how* to do this — it is deliberately a "how-to" document, leaving the "when, who, and why" to the safety planning documents it points to.

The policy spine that makes all of this mandatory is **FAA Order 8040.4**, issued by the Administrator on June 28, 1998. It requires every Line of Business (LOB) in the FAA to run a formal, disciplined, documented decision-making process for safety risk on high-consequence decisions affecting the full life cycle. The Handbook exists to give those LOBs a consistent, standardized set of procedures and analytical tools so they can actually comply with that order rather than each inventing their own approach.

The throughline of the foundation chapters: describe the system, identify its hazards, characterize each hazard by severity and likelihood, compare alternatives on a risk basis, decide with management owning the residual risk, and track everything in a closed loop until controls are verified. Do it early, do it continuously, and keep it in balance with cost, schedule, and performance.

## Frameworks Introduced (exact source names, when/how)

The slice introduces a stack of named instruments, policies, and analytical constructs. Listed with how the source uses each:

- **FAA Order 8040.4** — the originating safety risk management policy. Sets requirements for FAA-wide implementation of safety risk management and establishes the SRMC. Defines the five-step approach (Planning, Hazard Identification, Analysis, Assessment, Decision) and supplies the working definition of "hazard."
- **Acquisition Management System (AMS)** — agency-wide acquisition policy covering the whole acquisition life cycle. Its System Safety Management section (2.9.13) is the principal policy directive that requires each LOB to operate a system safety program per Order 8040.4 and to report safety status at every Joint Resources Council (JRC) meeting.
- **System Safety Handbook (SSH)** — the document itself; a tool inside the FAA Acquisition System Toolset (FAST), organized general-to-specific across 17 chapters.
- **FAA Acquisition System Toolset (FAST)** — the toolset that contains the SSH and the second-tier process documents.
- **Safety Risk Management Committee (SRMC)** — body established by Order 8040.4, staffed with safety/risk experts representing the Associate/Assistant Administrators and the offices of Chief Counsel, Civil Rights, Government and Industry Affairs, and Public Affairs; advises program offices on request.
- **System Engineering Council (SEC)** and **System Engineering Manual (SEM)** — the SEC oversees the safety risk process within the AMS and approved the FAA's Severity and Likelihood definitions; the SEM is referenced for functional-analysis detail.
- **The three plan types** — **System Safety Management Plan (SSMP)** for general organizational processes, **System Safety Program Plan (SSPP)** for individual programs/projects, and **Integrated System Safety Program Plan (ISSPP)** for large complex systems with multiple subcontractors.
- **FAST process documents** flowing down from AMS Section 2 — the Mission Analysis Process (MAP); the Investment Analysis Process (IAP) with its lettered appendices; the Integrated Program Plan (IPP); and the Acquisition Strategy Paper (ASP).
- **The hazard-analysis family** introduced via the IPDS life cycle — Operational Safety Assessment (OSA), Operational Safety Requirements (OSR), Comparative Safety Assessment (CSA), Preliminary Hazard Analysis (PHA), Preliminary Hazard List (PHL), Subsystem Hazard Analysis (SSHA), System Hazard Analysis (SHA), Operating and Support Hazard Analysis (O&SHA), and Hazard Tracking and Risk Resolution (HTR).
- **Integrated Product Development System (IPDS)** — the AMS life-cycle process (Mission Analysis → Investment Analysis → Solution Implementation → In Service Management → Service Life Extension) onto which the safety activities are mapped.
- **Safety Action Record (SAR)** — the record structure used to track each hazard through the closed-loop process.
- **FAA Report No. WP-59-FA7N1-97-2** (the July 1999 update of the *Comparative Safety Assessment Guidelines* for investment analysis) — the corporate CSA guidance for the IAP.
- **Severity / Likelihood definitions** — the SEC-approved FAA AMS tables (Catastrophic through No Safety Effect; Probable through Extremely Improbable), presented alongside the **MIL-STD-882** / **MIL-STD-882C** categories (I–IV severity, A–E likelihood) and a **FAR/JAR** comparison drawn from the Aircraft Performance Comparative Safety Assessment Model (APRAM) study. **AMJ 25.1309** is cited for worst-credible-case severity determination.
- **Risk Acceptability Matrix / Risk Acceptance Criteria** — the severity-by-likelihood matrix producing High/Medium/Low bands; the example MIL-STD-882C version is called a Hazard Risk Index (HRI) or Risk Rating Factor (RRF), with regions R1–R4.
- **Safety Order of Precedence** — the four-priority hierarchy for treating hazards (Table 3-7).
- **Behavioral-Based Safety** — the culture-and-people approach using a "train-the-trainer" model and real-time hazard identification by operational personnel.
- **The 5M model and the SHEL(L) model** — the two system-description models the AMS program uses to capture the interrelationships among hardware, software, human, environment, and procedures. The system definition itself is anchored to **MIL-STD-882 (System Safety Program Requirements)**.

## Key Concepts

**The five-step risk management process.** Order 8040.4 frames safety risk management as five steps: Planning, Hazard Identification, Analysis, Assessment, and Decision. The plan must be set in advance and must state the acceptability criteria for risk; hazard identification surfaces the risks; analysis characterizes them by severity and likelihood; the Comparative Safety Assessment measures them against the plan's criteria; and the decision — owned by management — incorporates that assessment. The order permits qualitative or quantitative assessment but states a preference for quantitative, and asks that assessments be scientifically objective, unbiased, and inclusive of relevant data, with any unavoidable assumptions made conservative and documented.

**Hazard vs. risk.** The Handbook stresses that these are distinct, and the glossary exists partly to keep them straight. A *hazard* is defined (per Order 8040.4) as any condition, event, or set of circumstances with the potential to cause — or to contribute toward — an unplanned or undesired outcome. *Risk* combines two elements that must both be characterized — severity of consequence and likelihood of occurrence — and the inability to quantify or the absence of historical data does not excuse a hazard from being assessed.

**The accident-scenario / hazard model.** Accidents rarely stem from a single hazard. The source models an accident as a sequence: an initiating hazard plus contributory hazards, where contributory hazards bring in the system state (e.g., operating environment) along with failures or malfunctions, leading to harm. This is the conceptual seed for the deeper "initiating" and "contributing" hazard treatment that begins in Chapter 7.

**Severity and likelihood scales.** The SEC-approved AMS severity scale runs Catastrophic (multiple fatalities and/or loss of system) → Hazardous → Major → Minor → No Safety Effect, with each tier tied to descriptions of safety-margin reduction, workload, injury, and environmental/property damage. The likelihood scale runs Probable → Remote → Extremely Remote → Extremely Improbable, each with both a qualitative description and a quantitative probability-per-operational-hour band (e.g., Extremely Improbable corresponds to below 1×10⁻⁹). The source pointedly shows these next to the MIL-STD-882C categories and a FAR/JAR cross-walk so the reader sees that these are conventions, not the only possible scheme.

**The risk matrix and acceptance bands.** Severity and likelihood are combined in a matrix yielding High, Medium, and Low risk. The acceptance rule: High is unacceptable and must be tracked in the FAA Hazard Tracking System until reduced and accepted; Medium is acceptable only with review by the appropriate management authority (and tracked until accepted); Low is acceptable without review and needs no further tracking. The MIL-STD-882C example renames the bands R1–R4 (unacceptable / must control or mitigate / acceptable with MA review / acceptable without review), but the function is identical — it is management's criterion for risk acceptability.

**The Comparative Safety Assessment (CSA) as decision and planning tool.** The CSA lists every hazard tied to a design change and gives a comparative assessment for each alternative considered — including the "no action / baseline" option — so options can be *ranked* for decision-making. It is both a decision tool (it makes the change in risk between alternatives explicit) and a planning tool (it drives development of safe operating procedures and test programs to resolve uncertainty where design alone cannot control the risk). A central caveat: the lower-risk alternative is not automatically the right choice once mission assurance is weighed — recognizing that tension is described as the keystone of safety risk management.

**Closed-loop hazard tracking and the Safety Action Record (SAR).** Hazard Tracking and Risk Resolution exists to make risk control a closed loop, with management risk acceptance as the key gate: the activity responsible for fielding the system must knowingly decide on the controls. The SAR is the tracking record — carrying reference number, status (open/monitor/closed), description of the hazardous event and its worst-case outcome, causes/contributors, initial and residual risk, suggested and implemented controls, verification and validation (by inspection, analysis, demonstration, and test), narrative history, references, originators, and the concurrences required to close it. IPT/Program Management concurrence is required to accept residual risk.

**Cost-versus-safety balance.** A balanced program optimizes safety, performance, and cost together; safety is one element interacting with cost, schedule, and performance. The principle is that the more severe the potential consequence, the lower its probability must be driven for the risk to be acceptable — so spending to reduce probability is justified for severe hazards, while less-severe ones may be tolerated at higher probabilities. Defining what is acceptable and unacceptable *early* is presented as just as important as defining cost and performance parameters.

**Managing Authority (MA).** Throughout the Handbook, the MA is the responsible FAA organization for a program, project, or activity. The MA approves managerial and technical procedures and adjudicates conflicts — both between safety and other design requirements, and among associate contractors.

**Safety Order of Precedence.** A fundamental principle: treat hazards in priority order — (1) design for minimum risk (eliminate by design, or reduce to acceptable through design selection); (2) incorporate safety devices (fixed/automatic features, with periodic functional checks); (3) provide warning devices (when design/devices can't adequately reduce risk, detect the condition and warn, designed to minimize bad human reactions, plus placards); (4) develop procedures and training (last resort, and typically requiring concurrence of authority when used against catastrophic, hazardous, major, or critical severity).

**Behavioral-based safety.** The source frames a shift from "safety by compliance" to "prevention by planning," arguing that compliance reliance tends toward after-the-fact detection that misses the organizational errors which often contribute to accidents. Modern system safety management blends system theory, statistics, behavioral science, and continuous improvement; its two critical elements are a sound safety culture and genuine people involvement. Real-time analysis — operational personnel identifying hazards themselves, via a train-the-trainer format — is the key to this approach.

**System-description models: 5M and SHEL(L).** Before any risk work, the system must be described (functions, general physical characteristics, operations). A system is defined (per MIL-STD-882) as a composite of personnel, procedures, material, tools, equipment, facilities, and software used together to achieve a mission. The **5M model** decomposes a system into Mission (central purpose), Man (human element), Machine (hardware/software/firmware), Management (procedures, policy, regulations), and Media (operational and ambient environment). The **SHEL(L) model** uses Software, Hardware, Environment, and Liveware (human), and emphasizes that the match or mismatch at the *interfaces* between blocks matters as much as the blocks themselves.

## Mental Models

**Safety is a balance point, not a maximum.** The cost-vs-safety-effort idea (Figure 3-1's "seek balance") says total cost is the sum of the cost of accidents and the cost of the safety program; you are looking for the minimum of that sum, not the elimination of all risk. Unnecessary safety requirements can break a system just as accidents can. Some level of risk must be accepted, and deciding that level is management's job.

**The system is a composite of interacting elements — describe it before you assess it.** Both 5M and SHEL(L) exist to force the analyst to look at every element — and crucially every *interface* — on an individual, interface, and system level. A description has breadth (where the system boundaries sit) and depth (level of detail), and the two trade off inversely: broad systems like the NAS get general descriptions; a narrow system like a landing-gear valve can be described in fine detail.

**Severity sets the bar for acceptable probability.** Rather than treating severity and likelihood as independent knobs, the model couples them: catastrophic outcomes demand far lower allowable probabilities than minor ones. This is why the same matrix that combines them is the management decision criterion.

**Earlier is cheaper.** A safety risk discovered (or an incident occurring) late in a program can overpower schedule, cost, and performance. Because safety can act as a design constraint, it is easy to under-weight it early — so the discipline deliberately front-loads risk-acceptability parameters, design tradeoffs, avoidance of high-risk approaches, and test planning into the investment-analysis and early solution-implementation phases.

**Hazards and risks are many-to-many.** A single risk may be reached through many hazards; conversely, predictive analysis hypothesizes accidents that are potential in nature, so severity is assessed against a hazard's *potential* to do harm, on a worst-credible-case basis.

**Map the activity to the life-cycle phase.** The IPDS model ties specific analyses to specific milestones: the OSA before the mission-need decision at JRC-1; CSA and PHA refined during investment analysis; formal SSPP-driven system and subsystem hazard analysis during solution implementation; O&SHA before the in-service decision; and continuous hazard tracking and incident investigation across the whole life cycle.

## Anti-patterns

The source names several behaviors to avoid, mostly inside its "general principles of safety risk management":

- **Over-reacting to every identified risk.** The guidance is explicit: don't overreact to each risk — make a conscious, deliberate decision about how to handle it, keeping hazards in proper perspective.
- **Treating "safety by compliance" as sufficient.** Relying on compliance is criticized as after-the-fact hazard detection that fails to catch the organizational errors that frequently contribute to accidents — the reason for moving to "prevention by planning."
- **Telling designers their approach won't work.** The principle is to point out the safety goals and how they can be achieved, rather than simply rejecting a designer's approach.
- **Reaching for generic procedures over program-specific objectives.** It is described as more important to set clear objectives and parameters for the Comparative Safety Assessment specific to the program than to fall back on generic approaches.
- **Labeling things "safety problems."** The source reframes these: in planning or design there are no "safety problems," only engineering or management problems that may lead to accidents if left unresolved — and there is rarely a single solution; a combination of directions often works best.
- **Imposing unreasonable safety requirements.** Just as a program cannot afford accidents that defeat its mission, it cannot afford systems crippled by unnecessary or unreasonable safety requirements — safety must be kept in proper perspective.

## Key Takeaways

- System safety in the FAA is a specialty within systems engineering aimed at optimizing safety, made mandatory by **FAA Order 8040.4** (1998) and carried into acquisition by the **AMS** (Section 2.9.13). The **SSH** is the "how-to"; the **SSMP/SSPP/ISSPP** plans cover the when/who/why.
- The process is five steps — Planning, Hazard Identification, Analysis, Assessment, Decision — with the plan stating risk-acceptability criteria up front and management owning the residual-risk decision.
- Risk is always two coupled dimensions, severity and likelihood, combined in a matrix that yields High/Medium/Low acceptance bands and serves as the management acceptance criterion; the FAA AMS scales sit alongside MIL-STD-882C and FAR/JAR equivalents.
- The **Comparative Safety Assessment** ranks alternatives (including no-action baseline) on a risk basis and is both a decision tool and a planning tool; the lower-risk option isn't automatically best once mission assurance is considered.
- Hazard control is a closed loop tracked via the **Safety Action Record**, gated by explicit management risk acceptance and closed only after verification and validation.
- The **Safety Order of Precedence** prioritizes design-out first, then safety devices, then warnings, then procedures/training — with procedures/training the least-preferred option for serious hazards.
- Safety is balanced against cost, schedule, and performance, defined early; severity drives the allowable probability; and risk found late is disproportionately expensive.
- Culture matters: **behavioral-based safety** moves from compliance to prevention-by-planning, leaning on safety culture, people involvement, and real-time hazard identification.
- Every assessment starts by describing the system using the **5M** and **SHEL(L)** models, where interfaces are as important as the elements themselves.

## Connects To

- **Order 8040.4 → AMS → FAST → SSH chain.** The mandatory policy (8040.4) is operationalized through acquisition policy (AMS 2.9.13) and the FAST toolset, of which this Handbook is one tool — the institutional backbone the later chapters assume.
- **Later SSH chapters.** Chapter 4 (establishing a program and writing the SSPP), Chapter 5 (plan preparation and ISSPPs), Chapter 6 (integration and CSA), Chapter 7 (integrated system hazard analysis; the initiating/contributory hazard methodology), Chapters 8–9 (hazard-analysis tasks and analytical techniques), and Chapter 14 (training, where the behavioral-based train-the-trainer detail lives). Chapter 3's glossary (Appendix A) underpins the hazard-vs-risk vocabulary used throughout.
- **Standards landscape.** Direct ties to **MIL-STD-882 / 882C** (system definition, severity/likelihood categories, HRI matrix) and to airworthiness criteria via **AMJ 25.1309** and the **FAR/JAR** classification cross-walk — useful anchors when relating this pack to broader SE and safety standards.
- **Systems engineering canon.** The framing of system safety as a specialty within systems engineering, the use of system-description models, life-cycle phasing (IPDS), and the cost/schedule/performance/safety balance connect this pack to mainstream SE lifecycle and risk-management material.

---

*Source: FAA System Safety Handbook (December 30, 2000), Chapters 1–3, as reproduced in the pack's built full text. Use the FAA original; reprint commentary is not in the public domain. All claims above are paraphrased from that source slice.*
