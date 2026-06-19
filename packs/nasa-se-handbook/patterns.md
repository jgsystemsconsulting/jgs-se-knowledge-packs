# NASA SE Handbook Patterns & Techniques

## Apply the SE Engine Recursively per Tier and Phase
**When to use**: Developing any system with a multi-level product hierarchy across the lifecycle (Pre-Phase A through F).
**How**: Run the left side (stakeholder expectations -> technical requirements -> logical decomposition -> design solution) top-down per Product Breakdown Structure tier; then run the right side (implement -> integrate -> verify -> validate -> transition) bottom-up. Each tier and phase spawns a fresh engine pass. Implementation happens only at the lowest tier; higher tiers integrate already-realized products.
**Trade-offs**: Stopping decomposition too early orphans requirements and hides interfaces; decomposing deeper than engineering judgment warrants (e.g., circuit-board detail in Phase A) burns resources without proportional risk reduction.

## Stakeholder Expectations -> Requirements -> Decomposition -> Design Flow
**When to use**: Front-end definition; always before locking design.
**How**: Capture and baseline stakeholder expectations as Needs, Goals, Objectives (NGOs). Derive functional + performance + interface + crosscutting requirements. Decompose into logical/behavioral models. Convert into a design solution traceable back to expectations. Baseline at each step.
**Trade-offs**: Skipping the baseline causes scope creep; orphaned requirements (no parent, or unallocated to children) signal overdesign or lost intent.

## ConOps Development
**When to use**: Earliest concept work (Pre-Phase A / Phase A), before requirements are written.
**How**: Write a narrative of how the system operates in its environment: roles, staffing, timelines, nominal AND off-nominal/contingency scenarios, critical events. Include a Design Reference Mission. Drives requirements and is the basis for validation.
**Trade-offs**: A nominal-only or late ConOps reveals critical requirements after design is locked, forcing rework; a purely technical ConOps misses long-term staffing and operational cost.

## Requirements Validation (5-Gate Check)
**When to use**: Before baselining any technical requirement.
**How**: Check each requirement for (1) format ("shall", editorial), (2) technical correctness + bidirectional traceability, (3) stakeholder satisfaction, (4) feasibility, (5) verifiability. Capture metadata (ID, rationale, verification method/level, owner) at write-time.
**Trade-offs**: Over-tight performance values eliminate viable designs and add cost; vague requirements ("minimize noise") are unverifiable. Specify threshold vs. baseline values to preserve trade space.

## Logical Decomposition via Functional Analysis
**When to use**: Translating requirements into an architecture.
**How**: Use Functional Flow Block Diagrams (sequences), N-squared diagrams (interfaces), and Timeline Analyses (time-critical functions). Allocate functions to hardware/software/human elements; capture derived requirements. Iterate until each level is defined and baselined.
**Trade-offs**: Multiple valid decompositions exist; outcome depends on engineer skill. Remain willing to revise earlier architecture as understanding improves.

## Trade Study + Decision Analysis
**When to use**: Selecting among competing architectures or design concepts.
**How**: Six steps: frame the decision, define criteria (primary factors distinguish alternatives; secondary refine within), generate/screen alternatives via a trade tree, evaluate against criteria, assess robustness under uncertainty, recommend with documented rationale. Build a decision matrix; normalize heterogeneous measures (e.g., 1-3-9) with explicit operational definitions.
**Trade-offs**: Match method depth to decision stakes; don't apply formal MAUT/AHP to a binary choice or discussion-only methods to high-stakes architecture. Recommending a lower-ranked option without explanation signals broken evaluation logic.

## Analytic Hierarchy Process (AHP)
**When to use**: Multi-criteria decisions mixing subjective and objective measures, needing defensible weights.
**How**: Decompose objectives into a criteria hierarchy; assign weights via expert pair-wise comparisons; compare alternatives pair-wise against each criterion; combine mathematically; iterate to consensus.
**Trade-offs**: Pair-wise comparisons assume other factors are fixed and independent; when factors interact, use AHP for weighting only and run a separate holistic evaluation.

## Cost-Effectiveness Optimization
**When to use**: Balancing performance against total lifecycle cost early (Phases A-B), where decisions lock in most downstream cost.
**How**: Treat effectiveness as mission outcome (nominal + off-nominal). Compare alternatives against the envelope (Pareto) curve. Use least-cost, cost-effectiveness, or weighted cost-effectiveness analysis. Treat schedule (e.g., launch windows) as a hard resource.
**Trade-offs**: Optimizing build cost while ignoring operations locks in higher lifecycle cost; assuming training compensates for poor design pushes burden to Phase E.

## Continuous Risk Management + RIDM
**When to use**: Throughout development; RIDM at direction-setting, CRM ongoing.
**How**: Characterize each risk as a triplet (scenario, likelihood, consequence) across safety/technical/cost/schedule/programmatic domains. Define trigger thresholds; apply proactive mitigation (reduce likelihood/consequence) and pre-plan contingency actions. Monitor residual risk until acceptable.
**Trade-offs**: Risk management as a compliance checkbox produces noise; waiting for a crisis squanders cheap early mitigation. Don't dismiss programmatic (regulatory/contractual) risk as "not engineering."

## WBS Development from the PBS
**When to use**: Technical planning; foundation for cost, schedule, and EVM.
**How**: Derive a product-oriented WBS from the Product Breakdown Structure, adding enabling functions (management, SE, integration & verification). Align WBS branch points with how subsystems will be physically/functionally assembled.
**Trade-offs**: A function-based WBS ("Design", "Testing") fractures accountability; WBS/PBS misalignment loses traceability and masks integration cost.

## Network Scheduling + EVM + JCL
**When to use**: Planning and tracking cost/schedule performance.
**How**: Build a network schedule (PERT/precedence) to find the critical path. Apply EVM at cost-account level: compare earned value (BCWP) to scheduled (BCWS) and actual (ACWP); variances trigger root-cause analysis. Run a Joint Confidence Level (integrated cost+schedule+risk) at KDP-C for projects above $250M.
**Trade-offs**: Comparing planned to actual cost is NOT earned value; spending money is not earning progress. Separating cost and schedule estimates yields infeasible plans. Contingency is risk mitigation, not padding to spend down.

## Requirements Management with Bidirectional Traceability
**When to use**: After requirements baseline (typically post-SRR, late Phase A).
**How**: Maintain hierarchical requirements with upward (to parent) and downward (to children) traceability in a requirements tool. Route all post-baseline changes through a Configuration Control Board with impact assessment on cost/performance/schedule/safety. Track requirement volatility as a process-health metric.
**Trade-offs**: Late changes have exponential cost; a stale traceability matrix is worse than none. Distinguish legitimate evolution from undisciplined creep, but route both through formal change control.

## Interface Management via ICDs
**When to use**: As soon as system elements are partitioned.
**How**: Define logical/physical/electrical/mechanical/human/environmental interfaces as early as possible in Interface Control Documents; prefer discipline/technology standards over novel interfaces. Verify element interfaces before assembly; track all interface changes in one accessible place and notify affected developers.
**Trade-offs**: Uncontrolled interfaces let individually-correct components fail to work together; emulators are acceptable only where their limitations are well characterized.

## Configuration Management with Baselines + CCB
**When to use**: From first baseline through disposal.
**How**: Designate Configuration Items; place baselines under control; route Change Requests through a Change Control Board; run functional and physical configuration audits to confirm the as-built matches the approved baseline. Keep current baselines visible to all teams.
**Trade-offs**: Loss of configuration control (hardware/doc mismatch, unincorporated changes, uncontrolled redlines) caused real mishaps (cited in Columbia). Verification data and repair procedures must trace to exact released part numbers.

## Verification by Test / Analysis / Inspection / Demonstration
**When to use**: Proving each product meets its "shall" requirements ("built right").
**How**: Pick the method per requirement: test (most rigorous), analysis, inspection, or demonstration. Approve detailed procedures at a Test Readiness Review. Run qualification (worst-case + margin) then acceptance (operational levels, detect workmanship defects). Document a verification report; manage discrepancies (stop, root-cause, decide nonconformance vs. procedure flaw).
**Trade-offs**: Over-testing without margin analysis induces unrealistic failures and burns budget; dismantling the test setup before root-cause closure loses the live system. Pedigree of reused/OTS products does not transfer to new environments.

## Validation Against Stakeholder Expectations
**When to use**: Confirming the system does the right job in its operational context ("built the right thing").
**How**: Test/demonstrate/analyze the product in its operational (or representative) environment against stakeholder expectations and the ConOps, with real operators. For software, classify by criticality and tailor methods; use regression testing after corrections. For models, distinguish verification, validation, and certification.
**Trade-offs**: A system can pass verification yet fail validation if the ConOps misrepresented use. Deriving dozens of requirements to quantify qualitative expectations costs more than planned validation with a representative user population; inadequate prep (untrained operators, uncalibrated gear) invalidates results.

## Product Integration (Bottom-Up) + EDU
**When to use**: Assembling realized components into higher assemblies.
**How**: Follow an integration plan that sequences receipt/assembly/activation to minimize cost and assembly difficulty. Integrate bottom-up, running functional tests at each level before fitting into the next. Re-evaluate the sequence as schedules shift. Smaller projects may use an Engineering Development Unit instead of full assembly.
**Trade-offs**: Skipping post-assembly functional testing hides integration defects until correction is expensive; a static integration sequence breaks when delivery schedules vary.

## Product Transition
**When to use**: Moving a product up a PBS level or delivering to the customer.
**How**: Embed packaging/handling/transportation requirements in the design. Protect against transit environments (thermal, shock, corrosion, contamination); track provenance and hazmat. Run functional/acceptance tests after installation. Deliver the full enablement package (manuals, training, support equipment).
**Trade-offs**: Bolting on handling design after realization causes rework; skipping post-installation verification leaves latent transit damage undetected.

## Technical Assessment via TPMs and Leading Indicators
**When to use**: Monitoring design maturity through implementation.
**How**: Select a small set of Technical Performance Measures for each Key Performance Parameter and key MOE/MOP. Trend technical leading indicators (mass margin, power margin, RID/RFA/action-item burndown) against alert zones from SRR through SAR. Compare actual vs. anticipated values to flag cost/schedule risk early.
**Trade-offs**: Too many TPMs dilute focus and add noise; tracking consumes resources, so keep the set succinct with subsystem visibility only as needed.

## Technical Reviews at Key Decision Points
**When to use**: At each lifecycle gate (MCR, SRR, SDR/MDR, PDR, CDR, SIR, ORR, FRR, DR).
**How**: Define and satisfy objective entrance/success criteria before convening. Present requirements/design/plans/progress to management plus a Standing Review Board (advisory) and internal peer reviews. The KDP decision authority approves, conditionally approves, or disapproves progression based on maturity evidence.
**Trade-offs**: Reviews that begin before entrance criteria are met discover foundational gaps mid-review; treating KDPs as rubber stamps forces late rework. Entrance criteria are cheap filters that allow early termination without convening the board.

## Tailoring with a Compliance Matrix
**When to use**: Scaling SE rigor to project risk class (Type A human-rated down to Type F demos).
**How**: Anchor tailoring to defensible mission characteristics (risk classification, mission lifetime, national significance). Record every NPR requirement's disposition (compliant/tailored/non-applicable) with explicit rationale in a Compliance Matrix attached to the SEMP. Document non-waiver customization too.
**Trade-offs**: Blanket tailoring "because it's small" ignores which risks the project can bear and courts approval failure; an entry that says only "tailored" without rationale fails governance.
