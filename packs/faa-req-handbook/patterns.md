# FAA Requirements Handbook — Patterns & Techniques

Reusable techniques distilled from the Handbook's eleven recommended practices.
Each gives *when* to reach for it, *how* the Handbook applies it, and the
*trade-offs* it carries. The slant is real-time, embedded, avionics/medical control
systems; reinterpret for information systems with care.

---

## 1. Define the boundary as monitored & controlled variables

**When** — at the very start, before any "shall" statement, and on every subsystem you carve off later.

**How** — view the system as a black box and list the environmental quantities it senses directly (monitored) and affects directly (controlled). Apply the *elimination test*: a true boundary variable would still exist in the world if the system vanished. Keep variables abstract (a number with a range and precision), never a wire format. Split a formatted display into its underlying value plus a status. Define physical interfaces separately and lower down.

**Trade-offs** — abstraction buys robustness and reuse but defers concrete interface work; the boundary will shift as functionality migrates between systems, so accept early imperfection over no boundary at all.

---

## 2. Drive operational concepts with textual use cases

**When** — once an overview exists and before detailed requirements, to validate intended behavior and surface missing functions/variables.

**How** — write each use case as a dialogue: actors, primary actor, preconditions, postconditions, a main success ("sunny day") scenario first, then exception cases and alternate courses as extensions. Title each by its goal, trace it to system goals, and link its steps to the System Functions they invoke. Walking the scenarios is also a discovery tool — it reuses boundary vocabulary and exposes overlooked entities and variables.

**Trade-offs** — informal and readable by all stakeholders, but not a formal design notation; keep the operator-interface (HMI) decisions out, or you narrow the requirements to one physical interface.

---

## 3. State environmental assumptions as outward-facing requirements

**When** — alongside the required behavior, for every monitored and controlled variable and every dependency on the world.

**How** — capture assumptions ranging from simple type/range/precision/units up to full plant models and rate-of-change limits. Group each with the external entity responsible for ensuring it holds. Give each a rationale. Treat assumptions + requirements as a precondition/postcondition contract that lets components be built independently and reused safely.

**Trade-offs** — every documented assumption is reuse insurance, but a long list signals fragility; where you can eliminate an assumption by making the system more robust, do so — though no real system reaches zero assumptions.

---

## 4. Organize requirements by a change-tolerant functional architecture

**When** — for any specification too large to be a flat list (i.e. nearly all real systems).

**How** — recursively group functions that are closely related and likely to change together (the Isolette's operator-facing functions collapse into one *Manage Operator Interface*). Draw dependency diagrams with monitored/controlled/internal variables as arrows. Label arrows with stable, high-level problem-domain concepts and seal volatile dependencies inside functions, pushed as deep as possible — building *firewalls* against change. Keep high-level requirements honestly high-level; never borrow lower-level vocabulary or fold in rationale.

**Trade-offs** — grouping by volatility maximizes change tolerance and doubles as traceability, but requires judgment about what will co-vary; the structure must be revised when implementation constraints intrude (see pattern 5).

---

## 5. Revise the ideal architecture for safety and platform constraints

**When** — after the ideal (problem-domain) architecture exists, once safety, legacy-integration, or platform realities bite.

**How** — run FHA → PSSA → fault tree to apportion failure-probability budgets to functions. Where a per-component budget is infeasible or too costly, change the *architecture* rather than the component (the Isolette adds an independent Monitor instead of buying ultra-reliable parts). Deform the ideal architecture as little as possible, then follow the change through the full cascade: overview/goals, operational concepts, exception cases, boundary, assumptions, diagrams, high-level requirements.

**Trade-offs** — absorbing constraints into one architecture beats maintaining two mappings, but each structural change ripples; minimizing the deformation keeps the final architecture stable because the problem domain outlasts any implementation.

---

## 6. Identify modes, then specify behavior as condition → assignment

**When** — once the architecture is in place, to turn it into testable requirements.

**How** — name the small set of externally visible behavioral discontinuities (e.g. INIT / NORMAL / FAILED) and define every transition, including any latching (FAILED persists until power cycle). Write each requirement as *condition (mode + variable constraints) → assignment of an ideal value*. Build the ideal value function variable by variable so every controlled/internal variable has exactly one value in every state; mark UNSPECIFIED — and document it — where no meaningful value exists.

**Trade-offs** — modes make the input-to-output mapping tractable and per-piece checkable, but only introduce a mode for an *observable* discontinuity; an over-complex transition diagram signals design leaking into the requirements.

---

## 7. Make completeness and consistency checkable with tables

**When** — when verifying a detailed requirement set, especially for safety-relevant variables.

**How** — render the requirements as condition/event/mode tables (or and/or tables) — modes down one axis, condition ranges across the other, the variable's value in the cells. The set is complete only when every cell holds one ideal value, consistent only when no cell holds two. Watch range boundaries: a `<` versus `<=` slip is the classic inconsistency.

**Trade-offs** — tables make completeness/consistency confirmable by inspection, but the obligation is identical whatever the notation; a graphical model can be compact yet blur where one requirement ends and the next begins.

---

## 8. Attach latency and tolerance, tethered to physics

**When** — for every controlled variable that the system owes its environment within a time bound or accuracy band.

**How** — specify *latency* (max lag from monitored change to controlled response) for every controlled variable and *tolerance* (allowed deviation) for every numerical one. Tether each number to a rationale that chains back to the environmental assumptions — the Isolette's 6-second heat latency derives from the assumed 1°F/min drift and the sensor's required 0.1°F resolution. Never specify latency or tolerance for internal variables.

**Trade-offs** — physically-grounded numbers survive review and protect against silent breakage when an assumption is later relaxed; a free-floating timing number is a guess.

---

## 9. Bridge to software with the four-variable model

**When** — when transitioning a system spec to a software spec for any sensor- or actuator-driven function.

**How** — treat software requirements as an *extension*, not a new document: define the INPUT/OUTPUT variables the software can actually read and write, then the IN'/OUT' relations (the driver layer that recreates MON'/CON' images and drives outputs) and REQ' (the application layer, which reuses the system's ideal value function unchanged). Give every input/output a definition, an accuracy bound, a latency bound, and a status attribute initialized to invalid. Confirm the end-to-end latency budget survives sensing lag + actuation lag + computation time. Map artifacts onto DO-178B high-level/low-level requirements and flag derived requirements to the safety assessment.

**Trade-offs** — the IN'/OUT' vs. REQ' split insulates behavioral software from hardware churn, but introduces prime-marked images (MON'/CON') that lag and deviate from reality — treat them as approximations in all timing/tolerance analysis.

---

## 10. Allocate to subsystems by duplicating high-level requirements

**When** — on large systems where functions are spun off to subcontractors.

**How** — carve along function boundaries (FCS → Flight Guidance + Autopilot). Keep a copy of each allocated function and its high-level requirements in the parent so each subsystem's topmost requirement traces to an identical parent requirement. Expose the parent's internal variables as genuine monitored/controlled variables at the subsystem interface, define them, and give them assumptions. Make each subsystem spec complete on its own (overview, variables, operational concepts, assumptions). Ensure summed subsystem latencies and tolerances stay within the parent's end-to-end budgets.

**Trade-offs** — deliberate duplication costs maintenance but buys clean contractor/subcontractor boundaries and traceability; drop parent variables the subsystem never uses.

---

## 11. Record rationale at the moment of authoring

**When** — continuously, for every non-obvious requirement, every non-obvious assumption, and every specific value or range.

**How** — write short, relevant *why* notes separate from the requirement; cite long trade studies rather than copying them. Capture rationale while the author is still reasoning — reconstructing it later is reverse-engineered guesswork. Use the act of articulating *why* as a quality filter: a requirement with no defensible reason is often unnecessary or an implementation detail to delete.

**Trade-offs** — cited as the single most cost-effective practice, but rationale is non-binding and never verified — so anything essential to behavior must be promoted to a real requirement, never left in the rationale.
