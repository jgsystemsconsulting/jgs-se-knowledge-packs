# Chapter — Assessment, Analysis, Verification and Validation

> **DRAFT SOURCE.** This chapter synthesizes NASA-HDBK-1002 *Draft 2 (April 2, 2012)*. The "Assessment and Analysis" section of the source is itself a placeholder topic outline marked for expansion in later releases; only the "Verification and Validation" section is fully written. Treat the assessment material here as a roadmap of intended topics, not settled guidance, and treat the whole pack as draft-quality reference until a released handbook version supersedes it.

## Core Idea

Fault Management (FM) verification and validation is the slice of the system's overall V&V effort that targets behavior in off-nominal situations. The source draws a sharp split: FM **verification** is a bottom-up, design-specific proof that the system reacts to failures exactly as its requirements specify; FM **validation** is a top-down, intent-specific, system-wide proof that the system's reactions actually preserve the assets and the functions the mission cares about. The reason FM V&V deserves its own treatment is asymmetry of scale — a system has far more ways to fail (contingency paths) than ways to succeed (nominal paths), yet FM V&V is usually funded and planned as a small fraction of total system V&V. That mismatch, traced to an under-appreciation of system complexity, is why FM V&V is historically short on people, time, and budget and chronically surprised during integration.

## Frameworks Introduced (exact source names, when/how)

- **FM V&V Process (the five V&V activities)** — the source organizes its FM V&V guidance around the same five activities defined in the NASA SE Handbook, applied to FM: **V&V Planning**, **V&V Preparation**, **Perform V&V**, **Analyze V&V Results**, and the surrounding V&V Guidance. Use it as the spine for scoping and sequencing any FM V&V effort; it is meant to extend, not replace, the system V&V process in the NASA SE Handbook, capturing the FM-specific differences.

- **FM validation matrix** — introduced during V&V Preparation as an explicit *extension* of the validation matrix described in the NASA SE Handbook, the difference being that the FM version folds failure scenarios into the system validation matrix. Build it when you need to identify which system tests confirm the system is doing the right thing under failure, capture the test platform and resources per test, and (per the planning section) drive a credible resource estimate for off-nominal V&V.

- **Top-down failure-scenario selection (three-step method)** — introduced under V&V Guidance to make scenario selection less subjective: (a) identify the set of mission activities; (b) identify the objectives within each activity, covering both mission goals and the health of assets, crew, and operators; (c) select one or more failure cases that threaten each objective. Use it to anchor coverage in mission goals rather than in engineering taste alone; it leans on top-down analyses already common on projects (FTA, PRA, success-tree analysis).

- **Four-tier failure-scenario priority scheme** — introduced under Prioritization of Failure Scenarios as **Required / High / Medium / Low**, each tier defined by the risk incurred by *not* performing the action (from unacceptable down to acceptable). Use it to map a selected scenario set onto the project's stated risk posture and to define the minimum certifying set when schedule pressure forces cuts.

- **Intent categorization (three classes)** — the specification of intent that FM validation needs is captured as objectives per system activity, each sorted into **safety-critical / mission-critical / noncritical**. The standard SE or safety-and-mission-assurance (S&MA) workflow should ideally produce this, though in practice an FM practitioner may end up gathering and recording it.

- **Assessment and Analysis topic outline (DRAFT placeholder)** — the source's "Assessment and Analysis" section is an outline of topics planned for later releases, not yet written. Named intended topics include: Quantitative versus Qualitative Analysis (with safety net, quantitative buy-down, qualitative "patch-up", and analysis for design versus V&V); LOC/LOM and Availability (control-loop effectiveness, single vs. multiple-fault criteria, failure-effect propagation, latent faults and effect interaction); Failure Scenarios (criteria and usage); Detection (coverage, false positive, false negative); Isolation and Identification / Diagnosis (observability, isolation FP/FN, isolation for repair and recovery, identification for root-cause analysis); Failure Response Decision and Failure Response (race conditions, response interactions); Prognostics (remaining useful life); and Models (goal tree/success tree, fault tree, discrete events and state machines, directed graphs, physics-based models). Treat this as a forward map of where FM assessment guidance is heading, not as instructions.

## Key Concepts

- **Verification vs. validation, FM-flavored.** Verification proves conformance to the requirement set (formal spec, plus requirements levied via ICDs and IRDs). Validation proves conformance to stakeholder expectations as captured in the ConOps, showing the system can deliver its intended behavior at the system level across realistic conditions — both nominal and off-nominal — judged by exercising scenarios and assessing the resulting behavior, not by tracing to individual requirements.

- **"System" is boundary-relative.** The FM V&V approach is written against a "system" defined by a chosen boundary, and the same process applies whether that system is a part, board, subsystem, vehicle, facility, or a combination of vehicles and facilities (a system of systems). The method scales with the boundary you draw.

- **Plan FM V&V alongside system V&V, early.** FM V&V planning nests inside the broader system V&V planning effort, runs concurrently with it, and must stay consistent with the project/program V&V plan. It documents guidelines, goals, and process steps, and spans test planning, simulator build-up, certification of test beds, and the identification of which test assets are needed at what fidelity. Crucially, the fidelity and fault-injection needs surfaced here often *drive* the scope of system V&V test assets — in some cases consuming half the total test-asset planning time.

- **Coverage is a cost/risk trade decided early.** A core planning output is the scope of off-nominal scenarios — how well the V&V action set covers the identified failure space, the as-built FM design, and the intended off-nominal behavior. This is a cost/risk decision with major schedule and risk-posture implications and must be made and documented early in the lifecycle so plans and costs can be set; deferring it is a common driver of test-phase overruns.

- **Pass/fail criteria must include critical objectives.** Criteria should account for the anticipated state of every objective that is health- or mission-critical; where those conditions aren't physically present in the hardware or simulation, analysis must assess them, so it is clear whether a result demands a retest.

- **Incompressible test list and regression suites.** By the start of the test program the plan should carry an *incompressible test list* — the bare-minimum set needed to qualify the design — plus a standard FM regression suite for design changes and, optionally, a minimal regression suite for parameter-only changes. Naming these up front heads off last-minute disputes when schedule pressure mounts.

- **Validation drives requirement specificity.** As you integrate upward through a multi-tier system of systems, requirements get less specific and test resources get larger; validation is where you confirm that requirement allocation was actually correct, because the bottom-up checkbox cannot.

- **Test beds: more visibility, more reliance on models.** Test beds offer greater visibility, more available time, and stronger fault-injection ability than the flight unit — but substitute heavier reliance on modeling and analysis, and hardware models often don't behave flight-like during failures. The source asks for all subsystems in the test bed (power and thermal are routinely short-changed, causing on-orbit surprises), test-bed sparing, at least one dedicated HITL test bed (valuable especially for acquiring timing data, and matching flight redundancy such as dual-string), and software simulations fully characterized against hardware and the flight vehicle with differences documented.

- **Formal modeling matters more for FM.** Because the number of possible failure scenarios is so large and failure-effect propagation can only be exercised incompletely by test, formal models and model checkers let you explore far more states than testing can, leaving a small residue of validation cases for flight hardware.

- **Failure space is huge and partly unknowable.** Failure scenarios = unique failure effects (failure modes collapsed to the smaller set of distinct effects) × system configurations over time. For moderately complex systems the count can run to the thousands; a rule of thumb puts the number of scenarios about an order of magnitude below the number of failure modes. You can never be sure all failure modes are even known — the unknown unknowns are nearly certain to exist.

- **Independence in validation and analysis.** The team running validation tests should be independent of the team that built the design, and every analysis should get a second set of eyes, preferably from a group independent of the design team. Test results should be used to validate the assumptions baked into analyses.

## Mental Models

- **Verification looks down, validation looks up.** Verification is bottom-up and design-specific — does each element do what its requirement says? Validation is top-down and intent-specific — across the whole system, do the reactions preserve assets and mission function? You need both because each is blind to what the other sees.

- **"Prove it's met" vs. "find where it breaks."** Default verification asks "prove requirement X holds under conditions we expect it to hold." The more honest question for FM is "find a condition where X is *not* satisfied." Checking the box under one favorable initial condition leaves the requirement potentially unmet elsewhere.

- **Allocate requirements, never allocate verification.** Requirements flow down to subsystems; verification of a higher-level requirement does not. Two fully verified subsystems B and C do not make integrated system A verified — you verify A by testing the combined system, where the cross-subsystem interactions actually live.

- **Coverage is mission-first, not catalog-first.** Validation answers "do you have what you need," which outranks "what do you have." So objective/activity coverage — especially mission-critical activities — takes priority over design coverage like covering every FM monitor or response.

- **Validation as an early paper test.** Building system-level validation tests during the design phase surfaces inconsistencies in FM design and assumptions before they reach the formal test program; the act of writing the tests is itself an early check, while FM engineers can still influence subsystem designs and confirm enough monitoring (test points, telemetry) will exist.

- **Automation turns the intractable tractable.** The failure space is too large to cover by hand. Scripted, automated testing with automatic pass/fail assessment slashes per-test overhead so far more cases run — the source's Cassini Saturn Orbit Insertion example ran over 3,000 automated tests to confirm the core attitude-control FM logic, saving many work-years and solving a problem that was otherwise intractable.

- **Architecture as a coverage multiplier.** Architectural features that allow well-behaved extrapolation let a tested scenario's results extend by analysis to other scenarios sharing that feature — widening failure-space coverage while keeping the analysis grounded in real test results.

## Anti-patterns

The source explicitly labels these as **Pitfalls**:

- **The Bump.** Many projects hit a large, unplanned spike in resources needed to finish system-level FM V&V — the planned-effort line versus the much higher actual-effort line. Prepare for it by planning FM testing adequately and budgeting for integration issues, unplanned interactions, and unexpected behaviors; its size depends on the integration flow, architecture, and FM mechanisms chosen.

- **Incremental verification.** Low-level subsystem verification done early, in standalone environments with external interfaces and stimuli simulated or absent, can leave problems undiscoverable — dependent subsystem and system interactions aren't visible to the subsystem developer even with a perfect subsystem plan.

- **Limitations of testing.** A verification test typically proves a response is taken under one engineer-chosen set of conditions; initial conditions and other subsystems' effects can produce scenarios where the requirement fails, yet once the box is checked under a single condition, verification moves on. Counter it by considering all scenarios under which the requirement must hold, adding tests and analyses as needed.

- **Verification by allocation.** Reducing system verification to bookkeeping — checking higher-level boxes as lower-level subsystem requirements verify — is a greatly flawed approach. Verify high-level requirements on the integrated system instead; validation can also play a key role here by confirming the allocation itself was correct.

- **Integration issues.** FM integration is usually more troublesome than nominal functions because of its far-reaching effects on system behavior; provide extra schedule margin for FM tests and flight-system demonstrations.

## Key Takeaways

1. **FM verification is bottom-up to requirements; FM validation is top-down to intent.** You need both; one proves the design responds as specified, the other proves the responses preserve assets and mission.
2. **Plan FM V&V early and inside system V&V planning** — its fidelity and fault-injection needs can drive system test-asset scope and even half the test-asset planning time.
3. **Decide coverage as an explicit cost/risk trade up front**, document the resulting risk posture, and capture an incompressible test list plus regression suites before the test program starts.
4. **Select scenarios top-down from mission activities and objectives**, then prioritize them Required/High/Medium/Low to map onto the project's risk posture.
5. **Lean on formal modeling, automation, and architectural extrapolation** to cover a failure space too large for testing alone — and keep validation and analysis independent of the design team.
6. **Avoid the named pitfalls** — the Bump, incremental verification, testing's limits, verification by allocation, and integration surprises — by integrating, hunting for failure conditions, and budgeting schedule margin.

## Connects To

- **System V&V (NASA SE Handbook).** The source presumes familiarity with the NASA SE Handbook V&V process and explicitly extends it — Product Verification (Sec 5.3), Product Validation (Sec 5.4), and the Verification/Validation Process Activities (Secs 4.3.1.2 and 4.4.1.2) for execution detail and outputs.
- **Failure scenarios and the FM models (earlier chapters / the Assessment outline).** Scenario selection depends on the failure-space concepts and on top-down models — FTA, PRA, success-tree/goal-tree, fault tree, state machines, directed graphs, physics-based models — that the Assessment-and-Analysis outline plans to develop.
- **FM planning and risk posture.** The four-tier priority scheme and coverage decisions tie FM V&V directly to the project's documented risk posture and to the FM V&V plan (standalone or folded into the project V&V plan).
- **S&MA and intent definition.** The safety-critical / mission-critical / noncritical objective categorization ideally originates in the standard SE or safety-and-mission-assurance workflow that fixes mission intent.
- **`nasa-se-handbook`** (sibling pack): the parent V&V process this FM treatment specializes; **`nasa-pra`** and **`nasa-risk`**: the top-down failure analyses and risk posture that feed scenario selection and prioritization.
