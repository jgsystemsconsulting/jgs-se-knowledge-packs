# NASA System Safety Handbook v2 Patterns & Techniques

## Pattern 1: Objectives-Driven Requirements Development
**When to use:** At program/project inception when translating stakeholder safety policy into verifiable requirements.
**How:** Decompose the two fundamental principles (minimum tolerable level + ASARP) into operational safety objectives specific to the mission; derive safety requirements from each objective; trace all requirements to objectives so no objective is uncovered and no requirement is unjustified.
**Trade-offs:** More upfront analytical investment than prescriptive checklists; pays back by eliminating requirements that are irrelevant and ensuring all relevant concerns are captured.

## Pattern 2: Safety Performance Margin Derivation
**When to use:** When setting probabilistic safety requirements for a new system without sufficient operational flight experience.
**How:** (1) Identify analogous historical programs with documented loss data. (2) Compute the ratio of actual total loss probability to modelled known-risk loss probability. (3) Apply this ratio as the safety performance factor. (4) Derive initial analytic requirement = Safety Threshold ÷ SPF. (5) Derive goal requirement = Safety Goal ÷ SPF_mature.
**Trade-offs:** Ratio estimates carry uncertainty; they are best estimates, not high-confidence bounds. Margins based on dissimilar programmes may misrepresent the new system's UU risk profile.

## Pattern 3: Graded ISA Scoping
**When to use:** When deciding how much analytic depth to apply to a system or subsystem within resource constraints.
**How:** Classify mission by project priority ranking (Priority 1: human spaceflight/>$1B/strategic → full PRA + qualitative; Priority 2: $250M–$1B → qualitative + targeted PRA; Priority 3: <$250M → qualitative only). Within a mission, apply finer-grained grading to scenario criticality: high-criticality scenarios get full quantitative treatment; lower-criticality scenarios get qualitative analysis.
**Trade-offs:** Risk of under-analysing an important scenario if criticality is mis-classified; requires periodic re-evaluation of criticality assignments as system design matures.

## Pattern 4: Claims Tree Construction
**When to use:** When building a RISC to argue for adequate safety at a KDP.
**How:** (1) Start from the operational objectives tree. (2) Map each objective to one or more claims. (3) Decompose intermediate claims until base claims are reachable by direct evidence. (4) For each base claim, identify direct evidence (quantitative) and supporting evidence (qualitative). (5) Score assurance deficits 1–5 for each base claim. (6) Review tree completeness to ensure all credible failure paths are addressed.
**Trade-offs:** The tree can become very large for complex systems; a graded approach selectively deepens the tree where evidence is weakest or criticality is highest.

## Pattern 5: Assurance Deficit Management as CRM Integration
**When to use:** Continuously from RISC development through programme execution to the next KDP.
**How:** (1) At RISC development, score each base claim assurance deficit 1–5. (2) Deficits rated 3+ become CRM risk statements with assigned owners. (3) Owners track and mitigate per NPR 8000.4A CRM process. (4) At next KDP, updated evidence is reflected in revised deficit scores. (5) Repeat.
**Trade-offs:** Requires disciplined integration of safety and risk management functions; if safety and risk management operate in silos, deficits will be scored but not managed.

## Pattern 6: Acquirer-Provider SSRA Handshake
**When to use:** Early in system development (pre-formulation through preliminary design) before requirements are baselined.
**How:** (1) Acquirer provides candidate requirement set. (2) Provider conducts SSRA: reviews NASA/military/industry standards, historical precedent, and mission-specific constraints to identify all applicable requirements. (3) Provider evaluates whether the requirement set can be met within design, cost, and schedule constraints. (4) Joint negotiation resolves infeasibilities; outcomes documented in MoU. (5) Resulting baselined requirements drive the SSMP.
**Trade-offs:** Early negotiation costs time; avoiding it leads to late requirement infeasibility findings that are far more costly to resolve.

## Pattern 7: SCI Designation from the ISA
**When to use:** When establishing safety-critical item management provisions and design protection measures.
**How:** (1) Conduct top-down ISA to identify hardware, software, interfaces, procedures, and management practices required for safety requirements to be met. (2) Designate as SCIs all items explicit in the ISA (redundancies, backup systems) and implicit (structural integrity assumptions). (3) For human-harm scenarios, apply SCI management provisions to all SCIs regardless of failure probability. (4) For equipment-loss-only scenarios, further filter to risk drivers (high probability + critical consequence). (5) As RISC develops, add SCIs identified through claims analysis that are not in the ISA.
**Trade-offs:** A broad SCI list imposes management overhead on many items; the risk-driver subset reduces overhead for non-human-harm scenarios but requires ongoing monitoring to verify the basis for exclusion remains valid.

## Pattern 8: Time-Varying Safety Requirement Profile
**When to use:** For systems expected to fly many times and mature through operational experience.
**How:** (1) Set initial requirement at Safety Threshold ÷ SPF (accounts for UU risk at first flight). (2) Set mature requirement at Safety Goal ÷ SPF_mature (assumes UU risks reduced by ~50% after ~125 flights). (3) Interpolate using exponential burndown curve calibrated to historical programmes. (4) Track the system's known-risk PRA result against this time-varying profile at each review.
**Trade-offs:** The burndown rate assumes an operational improvement programme; if the programme does not fund safety upgrades, the system will fall behind the profile.

## Pattern 9: RISC Staged Evaluation
**When to use:** At each KDP when the Evaluator receives a RISC from the Provider.
**How:** (1) Acceptance Review: verify completeness against SSMP commitments and analysis protocol requirements; issue RAIs if needed before proceeding. (2) Qualitative Scope/Methods Review: compare to standard methods and analogues; assess Provider qualifications; form independent perspective on results. (3) Quantitative Auditing: spot-check key calculations; perform simplified independent models for critical claims; run sensitivity studies on key assumptions. (4) Rate Acceptable/Unacceptable based on all phases.
**Trade-offs:** Three phases consume evaluation resources; the staged structure is efficient because it gates deeper work behind completeness — a comprehensive review of an incomplete RISC wastes effort.

## Pattern 10: Value-of-Information Decision Structuring
**When to use:** When an Evaluator identifies a significant assurance deficit and the decision maker must decide how to respond.
**How:** (1) Frame the three choices: accept risk (increase tolerance), mitigate risk (add controls), or reduce uncertainty (more testing/analysis). (2) Estimate expected cost of mitigation; estimate probability mitigation succeeds. (3) Estimate expected cost of additional information; estimate probability it closes the deficit sufficiently. (4) Compare expected values; present structured recommendation to decision maker. (5) Document the analysis in the RISC Evaluation Report.
**Trade-offs:** VOI analysis requires probability estimates for its own inputs, which may be uncertain; it is a decision aid, not an optimiser — the decision maker retains authority.

## Pattern 11: Expert Judgement Elicitation for RISC Scoring
**When to use:** When aggregating multiple evaluators' overall confidence assessments into a single RISC rating.
**How:** (1) Each expert provides a numerical confidence estimate (% confident the top claim is demonstrated true) backed by explicit deficit and importance rankings. (2) Compile all estimates. (3) If divergence is moderate, average after removing outliers (Delphi method). (4) If divergence is large and consensus is not reachable, identify the specific remedies that would bring divergent experts to consensus; communicate these to the Provider via RAI or conditional approval.
**Trade-offs:** Expert elicitation is inherently subjective; divergence reveals genuine uncertainty rather than error; forcing premature consensus obscures real disagreement that should inform the decision maker.

## Pattern 12: ISA-Informed Design Trade Analysis
**When to use:** When evaluating competing design alternatives for safety impact during system design.
**How:** (1) Use existing ISA to model the safety performance (probability of loss) for each alternative. (2) Plot P(loss) vs. programme cost (or schedule/mass) for each alternative. (3) Identify the ASARP frontier (where further safety improvement requires disproportionate sacrifice). (4) Select the alternative on the ASARP frontier that meets the safety performance requirement. (5) Document the rationale in the RISC.
**Trade-offs:** ISA fidelity limits the precision of trade results; early-phase ISAs are coarse and trades should acknowledge analytic uncertainty; re-run trades as ISA matures.

## Pattern 13: Safety Performance Monitoring and Precursor Analysis
**When to use:** During system operations to maintain ISA currency and detect emerging risks.
**How:** (1) Use ISA to identify system attributes with highest uncertainty and safety impact; establish monitoring protocols for those attributes. (2) Establish a precursor analysis programme: every anomaly and near-miss is evaluated for potential risk significance using the ISA. (3) When an anomaly shifts the risk picture significantly, update the ISA and propagate to the RISC before the next KDP. (4) Document trends and corrective actions as supporting evidence in the RISC.
**Trade-offs:** Precursor analysis requires sustained resource commitment during operations; programmes under budget pressure tend to reduce this activity, increasing UU risk exposure.
