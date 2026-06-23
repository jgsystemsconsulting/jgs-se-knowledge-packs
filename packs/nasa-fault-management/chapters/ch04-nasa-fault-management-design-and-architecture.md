# Chapter 4 — Fault Management Design and Architecture

> **DRAFT SOURCE.** This chapter synthesizes Section 6 of NASA-HDBK-1002 **Draft 2 (April 2, 2012)**, an unapproved working draft. One subsection of the source (architectures, design features, and approaches) is explicitly marked as a placeholder reserved for a future revision, and the terminology, tables, and recommended practices below reflect that draft rather than any later released edition. Treat as guidance, not a controlling standard.

## Core Idea

A fault management (FM) design is not invented from a blank page — it is *derived downward* from the mission. The handbook's central claim in this section is that a handful of mission attributes drive everything the operational FM system must do, and that the FM engineer's first job is to trace those attributes into priorities, then into constraints, then into the hardware, software, and operational architecture that realizes protective functions. Get that derivation right early and you scope the FM effort correctly; get it wrong or start it late and FM complexity, cost, and risk all balloon.

Two questions organize the whole chapter. First, *what must FM protect?* — the goals, critical events, finite resources, and continuously-available functions whose loss would compromise the mission. Second, *where and how fast can FM act?* — a question answered almost entirely by **response latency**, the elapsed time from a fault occurring to the failure condition being corrected, measured against the **time-to-criticality (TTC)** of the failure. The relationship between those two numbers decides whether a function can be left to ground operators or must be handled by onboard automation, and it varies dramatically by mission type, by mission phase, and by how far the vehicle is from Earth. The remainder of the chapter is essentially a catalog of how mission type, phase, and operational mode shift that latency-versus-TTC balance, with recommended practices attached to each case.

## Frameworks Introduced

- **Mission Requirements and FM Design flow-down (Figure 4)** — the organizing model for the section: mission attributes are turned into FM requirements, which then flow down into the architecture and design of the operational FM system. The handbook uses it to argue that an early understanding of how mission and system choices drive FM, from the top level down to hardware and software, lets engineers pick the right protective strategies and lets project managers scope and resource the effort.
  - When/how used: at the front of the design process, before architecture is fixed, so that the mission design itself can still be adjusted to support preferred FM strategies.

- **Mission risk posture, anchored in NPR 8705.4** — the choice of mission classification under NASA NPR 8705.4 (Risk Classification for NASA Payloads) sets the project's tolerance for risk, which in turn sets how exhaustively FM must address possible failures. The handbook ties this to Table 12 of Section 5.3, which summarizes mission classes and applicable fault-tolerant approaches.
  - When/how used: at mission definition, as the first of two steps that fix the risk posture (the second being the fault-tolerance requirements themselves).

- **Fault-tolerance requirements as the risk-distribution mechanism** — single-fault-tolerance requirements applied across a whole system drive the most expensive, highest-quality FM (high-grade parts, full redundancy, thorough containment, extensive operational FM). Higher-risk-tolerance missions instead distribute risk: mixed or targeted tolerance (single-fault for health-and-safety functions like pointing and power, none for ancillary instruments), partial or selective redundancy, smaller mitigated fault sets, and acceptance of certain operational risks.
  - When/how used: written in response to the mission-class definition; for higher-risk missions the FM engineer trades risk against resources to find where limited resources buy the most protection, working with S&MA and project management.

- **Response latency, decomposed (Figures 5 and 6)** — the time from fault occurrence to correction of the failure condition, which the source breaks into five sequential intervals so each can be analyzed and traded independently:
  1. **Observation latency** — fault occurrence to the failure effects becoming observable.
  2. **Detection latency** — observable effect to a mechanism detecting (and possibly identifying) it.
  3. **Decision latency** — time to diagnose, decide a response, and begin executing it.
  4. **Response execution time** — duration of the recovery activity itself.
  5. **Recovery time** — response completion to the point where effects are gone and status is restored to nominal.
  - When/how used: applied per system element (ground operators, ground software, crew, flight software, firmware, hardware) to build up the total latency for any candidate FM implementation, then compared against the failure's TTC to decide feasibility.

- **Primary-consideration tables by mission type, category, and phase (Tables 15–19)** — a set of lookup tables giving the single dominant FM design consideration for each mission type (robotic → prevent LOM; with crew → prevent LOC; interacting vehicles → avoid harming the other vehicle), each mission category (fixed-phase, multiphase, multifunction), and each mission phase across space, air, and surface vehicles.
  - When/how used: as an entry point to size FM scope; the source treats the full FM requirement set for a vehicle as the *union* of the requirements from every phase it will fly.

- **Operational capability taxonomy** — a classification of how control authority is distributed: automated operations (pre-programmed sequences triggered by phase changes, events, or commands), human-in-the-loop, autonomous operations (the vehicle determines its own course independent of ground intervention), ground operations, hybrid operations (a blend), overrides, and onboard displays and controls (D&C).
  - When/how used: to decide, per fault class, who or what acts — driven by whether TTC permits crew or ground response, and bounded by the rule that onboard FM generally must still provide a path for human oversight, intervention, or override.

- **Backup Flight Control System (BFCS)** — a distinct FM design option for crewed vehicles: an independently developed control system that protects against unanticipated faults in the primary avionics/software and against common-mode faults that could take out the primary system and its redundancy together.
  - When/how used: considered when potential common-mode failures (systematic design flaws, major software bugs, accidents damaging many components at once) threaten the primary system; justified only when its added safety exceeds what the same resources would buy by making the primary system more reliable.

## Key Concepts

- **Two response latencies, two different deadlines.** A staged response — say, software autonomously powering off an assembly to contain a failure, then waiting for ground operators to restore the function — has two latencies with different stakes. The first must complete before a critical failure effect (CFE) permanently harms health and safety; the second must complete before the lost function compromises mission goals (a missed observation, resources burned in the wrong mode). Both are evaluated against the failure's TTC.

- **Where to split flight versus ground is the core trade.** For any system, ground operators, ground software, crew, flight software, firmware, and hardware are all candidate places to implement detection, diagnosis, containment, and recovery. Choosing among them is a trade against the mission characteristics that govern latency. The ground path — fault, to operator's eyes, and back — is often the longest latency in the system; the source enumerates its many contributors (data generation cadence, storage, communications schedules, round-trip light time, bent-pipe relays, processing, human analysis and decision time, uplink scheduling, and onboard command execution).

- **Distance from Earth forces autonomy.** Systems far from Earth, with long round-trip light time and infrequent contact, cannot count on operators intervening before a failure's TTC; an event can begin and end before data even reaches the ground. Such missions lean heavily on sophisticated autonomous or automated functions. Earth-orbiting systems with frequent contacts can lean on ground interaction and limit onboard automation.

- **A mission's goals imply implicit fault-tolerance requirements.** Beyond explicit requirements, design features quietly levy their own. An availability or up-time requirement bounds how much science time a failure response may consume. A one-time, irreversible critical event (orbit insertion, a comet-flyby encounter, a docking, a landing) that cannot be retried demands the FM be able to recover functionality fast enough to still meet the goal — often fully autonomously when paired with long ground response times and a single-fault-tolerance requirement.

- **Protecting a resource usually means imposing a constraint.** Finite consumables (cryogen), critical payloads (sample return), and crew safe-haven needs become FM priorities, and protecting them typically shows up as a system constraint — a cryogenic telescope protects cryogen by keeping heat sources out of the bore-sight, which becomes a pointing keep-out-zone constraint. The same constraint can also exist on its own (a sun-pointing constraint protecting optics) and produces a similar FM priority.

- **Some functions must always be available — and that is where redundancy belongs.** A system may require certain functions to be continuously or near-continuously available, including the minimal "safing" set that keeps the vehicle safe while it waits for operators to recover it. When redundancy is limited, this always-on set is the natural place to apply physical or functional redundancy.

- **Phases with different needs demand reconfigurable FM.** A single-mode mission (e.g., a UAV that essentially just flies) can use static FM. A multi-phase mission (e.g., a Mars rover spanning launch, cruise, landing, and surface operations) needs multiple FM sets or FM functions that reconfigure by activity. The handbook's category model captures this: fixed-phase FM stays operative throughout; multiphase FM changes modes with each phase; multifunction systems need multiple phases when different functions require different FM (a rover grinding a rock has different restrictions than the same rover imaging its surroundings).

- **TTC is what makes phase matter.** The reason responses differ by phase is that TTC differs by phase. On orbit, the time for a fault's consequences to become critical is generally long; during powered ascent or entry, descent, and landing (EDL) it can be seconds or milliseconds — too short for ground or even onboard crew interaction — which is exactly why those phases mandate automatic, onboard FDIR for all flight-critical components.

- **Safe mode is the default response across phases.** Repeatedly across free flight, drifting balloons, and stationary and mobile surface vehicles, the recommended default for any failure not covered by a predetermined fault-isolation/reconfiguration capability is to fall into a protective safe mode that buys the ground (or onboard crew) time to formulate a recovery. A working safe mode must still accept ground commands and transmit data as directed so ground-directed recovery is possible, and may carry rudimentary onboard capability (e.g., sun-pointing to keep generating power) to head off short-TTC effects.

- **Interacting vehicles introduce cross-vehicle FM.** When one vehicle depends on another (a velocity-change burn, rendezvous targeting, latched docking, propellant transfer, beamed power), FM must respond not only to its own faults but to those on the partner, with insight into how the interaction is affected. During rendezvous and docking with a crewed target, preventing collision-induced loss of crew (LOC) takes priority over restoring lost capability — and FM must be able to facilitate safe separation if remaining fault tolerance is too low, unless the rendezvous itself is what prevents LOC.

- **The latency-versus-TTC split is reusable across every phase.** RPOD shows the pattern compressing as range closes: long TTC at far range lets the ground diagnose and formulate recovery; proximity operations cut TTC to minutes with collision risk; docking cuts it to seconds, demanding rapid onboard restoration of lost state or control. Berthing shifts FM responsibility to the target vehicle once the arriving vehicle goes to free drift.

- **Ground response latency and telemetry bandwidth set the autonomy floor.** The planned ground role must always account for communication gaps, delays, and bandwidth limits. Where the ground can respond quickly and confidently, little onboard autonomy is needed; as ground-in-the-loop latency grows past the TTC of certain faults, more onboard autonomy becomes mandatory. Bandwidth additionally bounds the fidelity and completeness of the data the ground can use to understand a fault and its response.

- **Aborts are a special contingency class of FM.** When a fault is non-recoverable and its TTC is too short even to use safe mode for evaluation, a crewed vehicle aborts. Aborts apply to powered ascent, collision-risk rendezvous, and powered descent for landings; they may use dedicated contingency hardware (a launch abort system / escape tower) or alternative software on systems already in use (typical of a rendezvous abort). Reentry is generally not abortable once initiated.

## Mental Models

- **Latency budget vs. TTC clock.** Picture every fault as starting a countdown (its TTC) and every candidate response as consuming a budget (its summed latency, intervals 1–5). A response is only viable if its budget fits inside the clock. This single comparison decides flight-vs-ground, onboard-vs-operator, and automatic-vs-crew for every fault in the system.

- **Two dials: risk and resources.** Low-risk missions turn the risk dial to minimum and pay whatever it costs (full redundancy, premium parts, exhaustive FM). Higher-risk missions instead balance the two dials, spending limited resources where they reduce the most consequential risk. The handbook frames higher-risk FM as managing risk and resources, not driving risk to zero at all costs.

- **The union-of-phases rule.** A vehicle's FM requirement set is the union of every phase's requirements. Add a phase, inherit its FM burden. A fixed-phase vehicle carries one constant set; a multiphase vehicle carries the superset, with mode-switching logic between them.

- **Concentric TTC shells around a target.** In rendezvous, imagine shrinking shells: far range (long TTC, ground can think), proximity (minutes, must be able to retreat safely), docking (seconds, must restore state/control onboard immediately). The FM response strategy hardens and accelerates as the vehicle crosses inward.

- **Safe mode as the universal fallback.** Treat safe mode as the catch-all branch of the FM decision tree: whatever predetermined responses exist, the final "else" is a protective, command-accepting, data-transmitting holding state that hands the problem to humans with enough time to solve it.

- **Independence is the price of a true backup.** A BFCS is only worth its cost if it shares almost nothing with the primary — independently developed and verified software, distinct processing and sensing where possible, separate command paths to effectors, and ideally a separate development team — because its entire purpose is surviving the common-mode failure that would defeat the primary and its redundancy together.

## Anti-patterns

The source flags these explicitly as **Pitfalls**:

- **Letting risk/cost priorities drift uncorrected over the lifecycle.** FM cost and complexity can often be traced to shifting assumptions about acceptable risk. Early on, cost dominates, so FM is under-staffed and started late; near launch, priority swings to risk, straining the FM system and its designers. An in-flight failure (e.g., a loss of redundancy) can shift the posture again. The named counter — a **recommended practice** — is to maintain an explicit fault-tolerance and risk-policy statement; a terse requirement alone cannot capture a risk policy's nuances, and a fuller philosophy statement heads off later disputes over interpretation.

- **Neglecting "core operations" FM support.** It is tempting to pour FM effort only into detecting and responding to failures, while underfunding the core functionality that FM itself needs: setting FM parameters, deployment sequencing, monitoring FM processing, reporting FM actions, and supporting troubleshooting of both system and FM behavior. The design must also ensure the information needed to trace and resolve faults survives a cascade of failures in telemetry, so the ground can reconstruct events and find root cause. These functions are critical during V&V and operations yet easily overlooked.

- **Partitioning ascent abort authority carelessly.** When a crew is aboard during powered ascent, abort responsibility between launch vehicle and spacecraft must be partitioned with care: the crewed spacecraft must be able to initiate an abort on a serious booster failure even without notification from the booster, yet its trigger conditions must avoid firing an abort that conditions do not actually merit.

- **Automatic orbit-insertion responses that cause irreversible loss.** An automatic FM response to an orbit-insertion or phasing propulsion failure must avoid actions that cause irreversible loss or degrade the mission when the detected failure was in fact recoverable in time.

- **Crew terminating a rendezvous over a benign, poorly understood fault.** An uncrewed vehicle rendezvousing with a crewed one must give the crew override capability, but unless sufficient FM situational awareness is provided, the crew may terminate the rendezvous in response to a benign but poorly understood fault or trajectory perturbation.

- **Analytic propulsion-fault detection during atmospheric entry.** Detecting propulsion failures analytically can be very difficult during atmospheric entry, where atmospheric properties and vehicle aerodynamics carry sizable uncertainty.

- **Ambiguous abort displays.** Crew displays for determining abort status can be complex enough that the correct response is ambiguous in some scenarios; care is required so the crew commands an abort only when truly necessary.

## Key Takeaways

1. **Derive FM top-down from the mission.** Mission attributes → FM requirements → architecture and design. Start the assessment early enough that the mission design can still flex to support the FM strategies you need.
2. **Risk posture is set in two steps.** Mission classification under NPR 8705.4 fixes risk tolerance; the fault-tolerance requirements then distribute that risk. Single-fault-tolerance across the system is the most capable and most expensive posture; higher-risk missions target redundancy and accept selected risks.
3. **First identify what FM must protect.** Mission goals (including one-time, irreversible critical events), implicit availability requirements, finite resources and constraints (consumables, keep-out zones, payload integrity, crew safe haven), and the always-available function set — the natural home for limited redundancy.
4. **Response latency versus TTC is the master trade.** Decompose latency into observation, detection, decision, execution, and recovery, sum it for each candidate implementer, and compare to the failure's TTC. The ground loop is usually the longest path.
5. **Distance and contact cadence dictate autonomy.** Long light-time and sparse contact force onboard autonomy; frequent Earth contact permits ground-centric FM with less automation.
6. **Phase drives FM mode, and TTC drives phase behavior.** A vehicle's FM is the union of all its phases' requirements; short-TTC phases (powered ascent, EDL, docking) mandate automatic onboard FDIR, while long-TTC phases (free flight, orbit) can default to safe mode and ground recovery.
7. **Safe mode is the universal default.** For anything not covered by a predetermined response, fall into a protective state that still accepts ground commands and transmits data, buying humans time to recover.
8. **Match the operational mode to TTC, and keep human override.** Use automated/autonomous FM when TTC is too short for crew or ground; provide human-in-the-loop and override paths wherever feasible, with adequate telemetry and D&C to support informed intervention.
9. **Special cases carry their own rules.** Interacting vehicles need cross-vehicle FM and safe-separation capability; aborts are the contingency response when neither recovery nor safe mode fits the TTC; constrained launch/reentry windows favor early FM activation, redundancy on window-critical components, and limited FM innovation to protect schedule; a BFCS is justified only when its independent protection against common-mode failure beats spending the same resources hardening the primary.

## Connects To

- **Chapter 1 (Introduction and FM Definitions):** This chapter operationalizes the system-level FM discipline defined there, turning the prevent/detect/isolate/diagnose/respond goals into concrete architecture-level trades.
- **Section 4 of the source (FM functions and concepts):** Response latency is built directly on the FM-function set (Figure 5) and the TTC and critical-failure-effect concepts introduced in Section 4; this chapter assembles those functions along a timeline.
- **Section 5.3 of the source (mission classes):** Table 12's mission-class risk tolerances feed the risk-posture discussion (6.1.1) and the by-type/by-category/by-phase tables here.
- **Section 6.3 of the source (architectures, design features, approaches):** Left as a placeholder for future revision in this draft — the detailed architectural building blocks that would follow this chapter's requirements-derivation are not yet populated.
- **`nasa-risk` and `nasa-pra` packs:** Risk posture, mission classification, and the cost-versus-risk trades here are the qualitative front-end whose likelihoods and dependence the probabilistic risk-assessment machinery quantifies; FM redundancy and common-mode (BFCS) reasoning connect directly to CCF treatment.
- **`nasa-system-safety` and `mil-std-882` packs:** LOM/LOV/LOC prevention, range-safety disposal (NPR 8715.5), abort logic, and harm-to-ground constraints are the safety objectives this FM architecture is built to satisfy.
- **NASA Systems Engineering Handbook (NASA/SP-2007-6105) and NPR 7123.1A:** The FM flow-down (Figure 4) is meant to operate inside the established SE technical processes, with FM requirements derived as part of normal requirements flow-down.
