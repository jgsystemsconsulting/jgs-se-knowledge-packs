# Chapter — The R&M Objectives Hierarchy & Scope Identification

## Core Idea
This standard expresses Reliability & Maintainability (R&M) not as a list of imposed requirements but as an **objectives-driven framework**: a hierarchy that names the R&M *objectives* a system must satisfy and pairs each one with the *strategies* used to accomplish it. The standard presents this hierarchy in two complementary views — first a **flowchart (graphical) view** of objectives and strategies, then a **tabular view** that augments the same hierarchy with the evidence methods and the scope appropriate to each mission class. Together they answer three questions in order: *what* characteristics the design must have (objectives), *how* to achieve them (strategies), and *how much* effort and what kind of evidence is warranted given the mission's risk (scope).

## Frameworks Introduced
- **R&M Objectives Hierarchy** — introduced as a flowchart view. It defines objectives and sub-objectives and maps each to the strategies that accomplish them. A single top-level **Top Objective** sits at the apex as the highest-level goal, and lower objectives elaborate it. When/how: use it to structure R&M intent for a system, reading it as an alternating chain of objective-then-strategy pairs that decomposes the high-level goal into achievable work.
- **The two essential block types (Objective and Strategy)** — the hierarchy is built from these two block types used in an **alternating fashion**: every objective is coupled with at least one strategy, and every sub-objective produced under that pairing is in turn coupled with at least one strategy. When/how: apply this alternation as the construction rule whenever you extend or read the hierarchy — an objective never stands alone, and a strategy always exists to serve a parent objective or sub-objective.
- **Supporting block types (Requirement and Context)** — beyond the two primary blocks, the notation adds **Requirement** blocks (which identify requirements relevant to an objective) and **Context** blocks. Context blocks are descriptive tags attached to an Objective or Strategy block, used purely to define context elements rather than to drive the hierarchy. When/how: use Requirement blocks to tie objectives back to governing requirements, and Context blocks to record constraints or related activities without confusing them for objectives or strategies.
- **R&M Objectives Hierarchy with Scope Identification** — introduced as the tabular view of the same hierarchy. It adds, for each **bottom-level strategy**, an *evidence* column suggesting the methodologies that may satisfy the corresponding objective, plus *scope* definitions describing how much of that method to perform for a given mission class. When/how: use it when formulating an R&M Plan for a program or project, to choose evidentiary methods and right-size their scope to the mission.

## Key Concepts
- **Objective block**: describes a necessary characteristic or attribute of the system or design. The **Top Objective** is the single highest-level goal of the hierarchy.
- **Strategy block**: describes the ways or methods used to accomplish a parent objective or sub-objective.
- **SubObjective block**: describes an intermediate goal that further elaborates a parent objective under a given strategy.
- **Requirement block**: identifies the requirements that are relevant to an objective, connecting the hierarchy to the requirement set.
- **Context block**: a descriptive tag on an Objective or Strategy that records constraints or other related activities; it adds context only and does not advance the objective-strategy chain.
- **Alternation rule**: objective and strategy blocks alternate down the hierarchy, so each objective is paired with at least one strategy and each resulting sub-objective is again paired with at least one strategy.
- **Evidence**: in the tabular view, the suggested type of methodology that may be used to satisfy a bottom-level strategy's objective.
- **Scope**: the extent to which an evidence method should be performed. The **top-level mission class** — that is, human spaceflight, or Class A robotic missions — is where the standard pins its suggested scope, allowing that scope to be pared back as applicable for higher-risk mission classes.

## Mental Models
- **Objectives-driven, not requirements-imposed.** Read the hierarchy as a chain of "what we need (objective) → how we'll get it (strategy)," not as a checklist of mandated shall-statements. Requirements appear as supporting blocks that feed objectives, but the spine of the model is the objective-strategy pairing.
- **Two views of one structure.** The flowchart view and the tabular view describe the *same* hierarchy. The flowchart shows the logical shape (objectives, sub-objectives, strategies, context); the table layers on the practical decisions — what evidence satisfies each bottom-level strategy and how far to take it for a given mission.
- **Evidence and scope hang off the leaves.** Evidence and scope are attached at the **bottom-level strategies**, not at the top objective. The high-level goal is constant; the tailoring decisions live at the bottom of the tree where concrete methods are chosen.
- **Scope is dialed by mission class.** Treat the top-level mission class (human spaceflight / Class A robotic) as the default-full scope baseline, then reduce scope as appropriate as mission risk increases — scope is a tailoring knob, not a fixed value.
- **Context is a tag, not a node.** When a piece of information is a constraint or a related activity rather than a goal or a method, attach it as a Context tag instead of forcing it into the objective-strategy alternation.

## Key Takeaways
1. The standard frames R&M as an **objectives-driven framework**: a hierarchy pairing objectives (necessary system/design characteristics) with the strategies that accomplish them.
2. The hierarchy is built from two essential block types — **Objective** and **Strategy** — used in an alternating fashion, with **Requirement** and **Context** blocks playing supporting roles.
3. Every objective is coupled with **at least one strategy**, and each sub-objective under that pairing is again coupled with at least one strategy.
4. A single **Top Objective** anchors the apex as the highest-level goal; sub-objectives elaborate it downward.
5. The **tabular view (with Scope Identification)** adds, per bottom-level strategy, an **evidence** column (suggested methods) and **scope** definitions for use when building an R&M Plan.
6. **Scope** is suggested at the top-level mission class (human spaceflight / Class A robotic) and may be **reduced for higher-risk mission classes** — making the framework explicitly tailorable.

## Connects To
- **R&M Plan formulation**: the evidence and scope columns of the tabular view directly feed the program/project R&M Plan referenced by the standard (its Section 5), translating the hierarchy into planned, mission-appropriate work.
- **Mission classification**: the scope tailoring depends on mission class (human spaceflight, Class A robotic, and higher-risk classes), linking R&M effort to the broader risk-classification scheme.
- **Requirements traceability**: Requirement blocks tie each objective to its governing requirements, connecting this hierarchy to upstream requirements management.
- **Verification and evidence planning**: the evidence column connects each bottom-level strategy to the methodologies that demonstrate satisfaction of an objective, linking the hierarchy to V&V and assurance activities.
