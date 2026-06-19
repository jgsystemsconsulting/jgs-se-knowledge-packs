# Chapter 6: Developing the Risk-Informed Safety Case (RISC) — The Provider's Role

## Core Idea
The Provider builds the RISC as a hierarchical claims tree — top claim that the system is adequately safe, decomposed into intermediate and base claims, each base claim supported by direct and supporting evidence, with assurance deficits scored 1–5 — documented in a RISC Report submitted at each KDP.

## Frameworks Introduced
- **Claims Tree Structure**: A top-down hierarchy from a top claim (system is adequately safe) through intermediate claims to base claims supported by evidence; mirrors the operational safety objectives tree; uses Goal Structuring Notation (GSN) optionally.
  - When to use: To organise the entire safety argument into a form that is evaluable, traceable to objectives, and free from confirmation bias.
- **Assurance Deficit Scoring (1–5 Scale)**: Base claims are assessed by rating the degree to which evidence knowledge gaps erode confidence: Rank 1 (~95–100% confidence) through Rank 5 (~0–35% confidence); exact percentile ranges set by the Acquirer based on mission criticality.
  - When to use: At each base claim to quantify evidentiary strength and flag weak links requiring additional evidence or risk treatment.
- **RISC Graded Approach**: Allocating RISC development depth proportional to mission criticality (same Priority 1/2/3 framework as ISA); lower-priority elements may have simplified claims and less formal evidence.
  - When to use: When managing RISC development resources across a complex system with subsystems of varying criticality.

## Key Concepts
- **Top Claim**: The apex claim in the RISC that the system is (or will be) adequately safe for a given application in a given environment; all sub-claims must be demonstrated to make this claim valid.
- **Intermediate Claim**: A claim further decomposed into lower-level sub-claims; demonstrated true when all feeding sub-claims are demonstrated true with high confidence.
- **Base Claim**: A claim not further decomposed; demonstrated true by direct and supporting evidence, with assurance deficits scored to quantify remaining uncertainty.
- **Direct Evidence**: Mostly quantitative information showing that the risk of not meeting a base claim is acceptably low (e.g., failure rates, PRA results, precursor analysis, adherence to best practices).
- **Supporting Evidence**: Mostly qualitative information that provides confidence in direct evidence or demonstrates responsiveness to safety concerns (e.g., personnel qualifications, V&V of tools, documentation quality, external review quality, safety culture).
- **Assurance Deficit**: Any knowledge gap prohibiting perfect confidence; caused by variability or lack of knowledge in data, models, inputs, or interpretations.
- **Goal Structuring Notation (GSN)**: An optional graphical notation for representing the claims tree visually; supported by NASA RISC Evaluation Management Tool.
- **RISC Report**: The documentation vehicle communicating the RISC to the Acquirer; contains executive summary, system description, safety objectives and requirements, safety argument with evidence, roadmap for ongoing activities, configuration management procedures, audit process description, and plans to resolve unresolved issues.
- **Confirmation Bias**: The tendency to use the safety case as a paper exercise repeating what engineers already believe; the RISC structure counters this by demanding both deductive (what could go wrong) and inductive (why it is nonetheless safe) argument.
- **Subsystem RISC Integration**: Where sub-providers develop sub-RISCs, the lead Provider takes full ownership of all subcontractor evidence integrated into the system RISC.

## Mental Models
- Build the claims tree top-down from objectives, not bottom-up from available analyses: start with the operational objectives tree, derive claims to match each objective, then ask what evidence would demonstrate each claim.
- Score assurance deficits at the base claim level, not the top claim: deficit scores propagate up through the tree to inform overall confidence, but the evaluation and remediation focus is at the leaf nodes where evidence is directly evaluated.
- Use the RISC Report structure as a quality gate: a well-formed RISC Report should contain an executive summary, system description, objectives/requirements documentation, argument + evidence, life-cycle roadmap, CM procedures, audit process, and unresolved issues plan; missing any of these is a completeness deficit.
- Treat the RISC as a living contract: commitments made in the RISC become part of the safety performance baseline managed under CRM; changes in programme circumstances (budget cuts, new findings) that invalidate the RISC must trigger a RISC update.

## Anti-patterns
- **Confirmation bias in evidence selection**: Selecting only evidence that confirms safety without systematically seeking disconfirming scenarios; the RISC must include deductive analysis of potential failure paths, not only inductive argument from existing results.
- **Claiming base-level confidence without evidence**: Assigning Rank 1 (very high confidence) without documented direct and supporting evidence; the deficit ranking must be traceable to specific evidence gaps, not asserted.
- **Static RISC**: Preparing the RISC once and not updating it for evolving programmatic conditions, new analysis results, or anomalies; a RISC that does not reflect the current state of the system cannot provide valid support for risk acceptance.
- **Subsystem RISC without integration**: Collecting sub-system RISCs from subcontractors without integrating them into a coherent system-level argument; the lead Provider must take ownership of the entire integrated RISC.

## Key Takeaways
1. The RISC is built top-down from objectives: each operational safety objective generates claims, each claim generates evidence requirements, each evidence gap generates an assurance deficit to be managed.
2. Assurance deficits are the currency of RISC quality: tracking, scoring, and reducing deficits is the core safety management activity once claims are established.
3. Direct evidence is quantitative risk demonstration; supporting evidence is qualitative confidence in the direct evidence. Both are required; neither alone is sufficient.
4. The claims tree is also a self-assessment tool: building it forces identification of gaps, cross-system interactions, and assumptions that the Provider might otherwise overlook.
5. Configuration management of the RISC is itself evidence of safety culture and management commitment; poor CM of the RISC is a supporting-evidence deficit.
6. The graded approach applies to RISC development as well as ISA: focus the deepest RISC development effort on the highest-criticality claims and accept less formal treatment of lower-criticality subsystems.

## Connects To
- **Chapter 5 (ISA)**: The ISA generates the quantitative direct evidence that populates base claims; ISA outputs and RISC base claims must be kept in sync throughout the life cycle.
- **Chapter 7 (RISC Evaluation)**: The RISC is evaluated against the same criteria used to build it; the Acquirer rates assurance deficits and claim importance using the same 1–5 scale.
- **NASA RISC Evaluation Management Tool**: NASA software tool incorporating a generic evaluation tree based on the framework in this chapter.
- **NPR 7123.1B**: RISC documentation requirements are consistent with KDP entrance criteria specified in NPR 7123.1B.
