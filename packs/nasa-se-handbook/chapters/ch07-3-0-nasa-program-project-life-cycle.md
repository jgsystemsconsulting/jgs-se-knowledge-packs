# Chapter 7: 3.0 NASA Program/Project Life Cycle

## Core Idea
NASA organizes all space-flight and research programs and projects through a structured lifecycle consisting of formulation, implementation, and closeout phases, with formally-gated Key Decision Points (KDPs) and maturity-specific reviews ensuring that technical requirements, architectures, and designs are appropriately baselined before progression.

## Frameworks Introduced
- **NASA Program/Project Life Cycle Model (3-Program and 6-Project Phases)**: A gate-based sequencing framework that separates formulation (concept through approval to implement) from implementation (design through operations) and closeout (decommissioning/disposal).
  - When to use: All NASA space-flight programs (NPR 7120.5), research & technology programs (NPR 7120.8), and IT projects (OCIO handbook); timing and content flexibility allowed within KDP-equivalent information requirements.

- **Key Decision Points (KDPs)**: Formal gates (KDP 0, A, B, C, D, E, F for programs; KDP A, B, C, D, E, F for projects) at which decision authority reviews and approves progression to the next phase.
  - When to use: Between major phase boundaries; entrance/exit criteria documented in NPR 7123.1.

- **Phase-Structured Reviews (Technical & Management)**: Sequence of formal reviews (MCR, SRR, SDR, MDR, PDR, CDR, SIR, ORR, FRR, SAR, DR, DRR) aligned to phase gates, with Standing Review Board (SRB) participation for high-risk decisions.
  - When to use: Each review is scheduled at a defined KDP or inter-phase milestone; reviews assess maturity of SE products and readiness to proceed.

- **SE Product Maturity Baseline Strategy**: Defined in Table 3.0-1; each major SE deliverable (Stakeholder Identification, Requirements, Architecture, Design, V&V Plans, Operations Plans, etc.) progresses through Preliminary → Baseline → Update states, with formal approval required at each baseline KDP.
  - When to use: To ensure incremental product rigor; prerequisites for downstream decision gates.

## Key Concepts

- **Formulation Phase**: Establishes cost-effective program plan, allocates user expectations to requirements, derives cost estimates, develops ConOps, and prepares for implementation approval at KDP I. Executed for both tightly/loosely coupled and single-project programs.

- **Implementation Phase**: Spans design (Phases B–C), build/assembly/integration (Phase D), operations (Phase E), and closeout (Phase F). Works to mature baseline requirements, design solutions, verification/validation results, and operational procedures.

- **Key Decision Point (KDP)**: Formal gate at which decision authority (Administrator, MDAA, or Center Director) reviews maturity evidence and approves or gates progression; includes standing review board assessments for critical decisions.

- **Program Life Cycle Variants**: NASA distinguishes uncoupled programs (independent projects), loosely coupled (limited integration), and tightly coupled programs (extensive cross-project dependencies), each with tailored KDP and review timing.

- **Single-Project Program**: Streamlined variant where a single large project is treated as a program; same phase sequence but simplified governance.

- **Mission Concept Review (MCR)**: Pre-formulation review assessing mission feasibility and alignment with NASA strategic goals.

- **System Requirements Review (SRR)**: Formulation-phase review approving preliminary system requirements and constraints.

- **Baseline**: Formal approval state at a KDP; once baselined, changes require formal change control and re-approval at subsequent KDPs.

- **Verification and Validation (V&V) Maturity**: Progresses from Approach (Phase A/B), to Preliminary Plans (Phase C), to Initial/Preliminary Results (Phase D), to Baseline (Phase E), tracked as a leading indicator.

- **Transportation Criteria and Instructions**: SE product emerging in Phase C (Initial) and finalized in Phase D; required for flight certification.

## Mental Models

- **Think of KDPs as "not forward until proven maturity"**: Each gate withholds approval until defined SE products meet their maturity milestone (Preliminary, Baseline, or Updated state); flexibility in review timing is allowed only if equivalent maturity evidence is provided.

- **Treat Formulation as upstream analysis, Implementation as downstream execution**: Formulation (Phases 0–I) asks "What should we build and why?"; Implementation (Phases A–F) asks "How do we build it, prove it works, and operate it?" The split mirrors the problem-definition vs. solution-execution divide.

- **Use SRB participation as a risk/complexity signal**: Red-triangle reviews on the life-cycle figures denote decisions requiring Standing Review Board oversight; these mark high-consequence gates where independent technical authority must concur.

## Anti-patterns

- **Skipping baseline gates to "save time"**: Proceeding to Phase C design without baselined Phase B requirements and architecture is a setup for costly rework; the handbook requires formal approval at each KDP and change-control discipline thereafter.

- **Treating reviews as post-hoc rubber stamps**: KDP reviews must assess maturity BEFORE approval; entrance/exit criteria must be defined and satisfied; post-hoc reviews that discover scope creep or immaturity force re-work or mission risk.

- **Conflating program and project lifecycles without documenting rationale**: The three program variants (uncoupled, loosely coupled, tightly coupled) have different coordination complexity; misalignment between actual program structure and selected lifecycle model leads to review chaos or inadequate cross-project governance.

## Key Takeaways

1. **KDPs are mandatory gates, not suggestions.** Every program/project must pass defined KDPs before progression; decision authority approval is required; no flexibility on maturity requirement, only on review timing and content expression.

2. **Formulation and Implementation are distinct phases with different gates and purposes.** Formulation (through KDP I / KDP A) is "have we planned this correctly?" Implementation (KDP B–F) is "are we building it correctly?" Conflating them causes scope/schedule creep.

3. **SE Product Maturity is tracked incrementally.** Requirements, architectures, V&V plans, and operations procedures are explicitly baselined at specific KDPs and updated at subsequent gates; skipping a baseline or using stale documents at a later gate is a root cause of mission risk.

4. **Standing Review Board participation marks critical decisions.** Red-triangle KDPs require SRB review; these are where independent technical authority has the final word; program/project managers and lead systems engineers must prepare independent evidence for SRB scrutiny.

5. **Program structure drives lifecycle variant selection.** Tightly coupled programs (many cross-project dependencies) require more frequent synchronization reviews; loosely coupled and uncoupled programs allow more independent project scheduling; selecting the wrong variant leads to either bottlenecks or insufficient integration oversight.

6. **Flexibility in timing and review content is allowed only if KDP maturity is met.** NPR 7123.1 and the project plan govern exact review sequencing; the handbook permits adaptation (e.g., MCR timing, PRR necessity only for multi-copy systems) provided that entrance/exit criteria are satisfied and documented.

## Connects To

- **NPR 7120.5 (NASA Space Flight Program and Project Management Requirements)**: Mandates space-flight program use of this lifecycle model and specifies formulation authorization documents, project plan content, and KDP maturity requirements.

- **NPR 7120.8 (NASA Research and Technology Program and Project Management Requirements)**: Applies the same lifecycle logic to research and technology programs; entry criteria differ but gate philosophy is identical.

- **NPR 7123.1 (NASA Systems Engineering Requirements and Processes)**: Defines detailed entrance/exit criteria for each KDP and review, and specifies the SE Product Maturity baseline requirements (Table 2-5 and Appendix D).

- **NASA Office of the Chief Information Officer (OCIO) IT Systems Engineering Handbook**: Adapts the same phased lifecycle to IT projects, with distinctions for highly specialized vs. non-specialized IT.

- **Section 3.10 (NASA Budget Cycle)**: Contextualizes the program/project lifecycle within the Agency's fiscal-year planning and appropriation cycles; systems engineers must align technical phase gates with budget authority and release timing.

- **Appendix B (Glossary)**: Defines "highly specialized IT," "decision authority," "ConOps," "Change Control Board," and other lifecycle governance terms.
