# NIST CPS Framework Patterns & Techniques

Reusable patterns drawn from the NIST CPS Framework (SP 1500-201/202/203). Each has When / How / Trade-offs. All wording is synthesized from the source.

## Pattern 1: Analyze a CPS on the Aspect × Facet Grid

**When to use**: at the start of any CPS study, design, or evolution effort — to make sure nothing important is omitted.

**How**: enumerate the nine **aspects** (groupings of concerns) and examine each through all three **facets** — conceptualization (the CPS model as properties), realization (build/operate), and assurance (the assurance case). Treat the grid as a coverage map: every aspect gets looked at in every facet, or is explicitly marked not-applicable. Tailor the grid down to the slice your problem needs before analyzing.

**Trade-offs**: the full grid is heavy for a small device, so tailoring is mandatory — but tailoring is an explicit, recorded decision, not an implicit default. Skipping aspects silently loses the coverage guarantee that justifies the method.

---

## Pattern 2: Run the Facets as Modes, Not a Waterfall

**When to use**: whenever CPS analysis is iterative, reverse-engineering, agile, service-based, or gap-driven — i.e. almost always.

**How**: treat conceptualization, realization, and assurance as interchangeable **modes of analysis** you transition between at any point in the lifecycle. Specialize the generic facet activities to the domain, then feed domain lessons back to improve the generic conceptions. Follow one property (e.g. "ambulance arrives within target time") through all three facets to keep the flow honest.

**Trade-offs**: mode-switching needs discipline to avoid thrash; the payoff is iteration and feedback the waterfall forfeits. Locking into linear conceptualization → realization → assurance is the named anti-pattern.

---

## Pattern 3: Manage Trustworthiness as Cross-Property Risk, Not Five Silos

**When to use**: for any CPS where safety, security, privacy, reliability, and resilience interact — i.e. any CPS that touches the physical world.

**How**: replace siloed, discipline-specific risk management with one process spanning all five top-level properties. Set an overall system-of-systems objective, treat the **risk budget** as a common resource each property draws on (allocated by consequence, not split equally), and push each protection onto the element type — physical, analog, or cyber — best able to enforce it. Remember cyber components likely consume the largest share of the budget.

**Trade-offs**: cross-property design needs every property's lead at the table, which is more coordination than five separate optimizations — but optimizing property-by-property is exactly what Stuxnet defeated. A simple physical over-speed interlock would have stopped that attack regardless of any digital command.

---

## Pattern 4: Climb the Interoperability Ladder and Insert a Canonical Hub

**When to use**: when independent CPS must exchange data across ownership, scale, and domain boundaries.

**How**: secure physical connectivity, then climb the three rungs — **syntactical** (move the bytes intact), **semantic** (agree on meaning), **contextual** (agree on the rules of use). Replace quadratic pairwise translators with a shared **canonical model** plus well-placed **adaptors**, cutting transformations from roughly n(n−1) toward n. Give each datum a persistent, resolvable identifier; keep changeable attributes (location, owner) out of the identifier string. Where data is too big, fast, or legally immovable, move the computation to it (Fog).

**Trade-offs**: a canonical model is upfront design cost and a governance commitment; bilateral mappings feel cheaper for two systems but explode as systems are added. Clean-slate designs that ignore legacy are called unacceptable — legacy CPS must be accommodated.

---

## Pattern 5: Specify Timing as Time Intervals and Pick the Weakest Class That Works

**When to use**: whenever a CPS has timing requirements — i.e. by definition.

**How**: express each requirement as a bound on a **time interval** between two significant events, then classify it: **Bounded** (a deadline only), **Deterministic** (a precise relationship on the system's own clock), or **Accurate** (internationally traceable, UTC/TAI). Use a Bounded TI for deadlines (landing gear: late is failure, early is fine), a Deterministic TI for repeatable precision (fuel injection vs. shaft position), and an Accurate TI only where spatial scale or regulation forces it (continental synchrophasors). Push time-awareness down to the network and hardware layers, reason in logical time, and enforce physical time only at the boundary to sensors and actuators.

**Trade-offs**: over-specifying the class wastes hardware (demanding SI-traceable accuracy where a 0.1% quartz oscillator would do); under-specifying it silently violates correctness. Modern general-purpose CPUs/OSes are not time-aware, so accurate timing may force FPGAs/ASICs or time-aware PHYs.

---

## Pattern 6: Engineer Secure, Resilient Time as a Supply Chain

**When to use**: for any CPS whose correctness or safety depends on accurate time, especially in critical infrastructure.

**How**: treat an accurate instant like a critical supply — it has a *source* (GNSS or a national lab), a *transfer path* (network and OS layers), a *quality spec* (AVAR/MTIE), *failure modes* (jamming, spoofing, slips, PDV), and a *continuity plan*. Assume Byzantine faults and active attacks. Build on source-channel and source-data assurance, authenticate the whole packet (not just the time payload), use strong symmetric keys (avoid NTP Autokey and outdated HMACs), and design for **predictable failure**: detect compromise early, alarm the operator, and fail over to an equally precise trusted backup. Provide source diversity (other GNSS, dedicated WANs, SyncE+PTP/White Rabbit, WWVB/WWV, eLORAN) and holdover.

**Trade-offs**: redundant assured sources and crypto cost money and can degrade accuracy (IPsec end-to-end vs. MACsec hop-by-hop). Naively "restoring" time after a compromise risks introducing new discontinuities — recovery must itself be bounded. Distinguish *denial* (degrade to a safe fallback) from *spoofing* (confident wrong time) and design for the harder spoofing case.

---

## Pattern 7: Drive Requirements from Use Cases (Survey Wide, Drill Narrow)

**When to use**: when eliciting and validating the functional requirements a CPS reference architecture must support.

**How**: collect broad **CPS Examples** (many systems/actors) for breadth, then decompose each into single-actor/single-system **specific use cases** whose steps map to **primitive requirements**. Score every example consistently against the requirement-category form (a living artifact: extend it and re-apply retroactively when a new characteristic appears). Cluster on architectural characteristics to find coverage gaps, and deliberately recruit a use case to fill an empty cell.

**Trade-offs**: use cases gather *functional* requirements only, so combine with other elicitation for non-functional needs. The set is never "done"; declaring it finished defeats its validation purpose. Inconsistent, ad hoc scoring breaks the clustering the whole method depends on.
