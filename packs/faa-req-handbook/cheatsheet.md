# FAA Requirements Handbook — Cheatsheet

Fast reference for the eleven recommended practices, the four-variable model, and
the quality checks. For real-time, embedded, avionics/medical control systems.

---

## The eleven recommended practices (rough execution order)

| # | Practice (section) | What it produces |
|---|---|---|
| 1 | System overview (2.1) | Synopsis, contexts, external-entity descriptions, goals |
| 2 | System boundary (2.2) | Monitored & controlled variables; physical interfaces |
| 3 | Operational concepts (2.3) | Use cases (sunny-day first), preliminary function list |
| 4 | Environmental assumptions (2.4) | Outward obligations on the world (type/range/units → plant models) |
| 5 | Functional architecture (2.5) | Dependency diagrams; functions grouped by what changes together |
| 6 | Revise for constraints (2.6) | Final architecture after safety/legacy/platform constraints |
| 7 | System modes (2.7) | The externally visible behavioral discontinuities + transitions |
| 8 | Detailed behavior & performance (2.8) | Ideal value + tolerance + latency per variable |
| 9 | Software requirements (2.9) | Four-variable extension: INPUT/OUTPUT, IN'/REQ'/OUT' |
| 10 | Allocate to subsystems (2.10) | Standalone subsystem specs; duplicated high-level requirements |
| 11 | Provide rationale (2.11) | The *why* for non-obvious requirements, assumptions, values |

Iteration is expected; tailoring is assumed. Order is not rigid.

---

## The four-variable model at a glance

| Symbol | Meaning |
|---|---|
| **MON** | Environmental quantities the system monitors (senses) |
| **CON** | Environmental quantities the system controls (affects) |
| **NAT** | The environment's natural relationship — i.e. the assumptions |
| **REQ** | The relationship the system must maintain between MON and CON |
| **INPUT / OUTPUT** | What the software can actually read / write |
| **IN / OUT** | How inputs relate to MON / how CON relates to outputs |
| **IN' / OUT'** | Driver layer: recreate MON' images / drive outputs from CON' images |
| **REQ'** | Application layer: same ideal value function as system REQ |

Mantra: *software requirements = system requirements + the four-variable wrapper.*
The prime mark (MON', CON', airspeed') = "a delayed, slightly-wrong copy of reality."

---

## Requirement structure

```
condition  →  assignment
   |              |
mode + variable   ideal value (+ tolerance, + latency for controlled vars)
constraints
```

- **Ideal value function** — what a perfect system would assign, for every state.
- **Tolerance** — allowed deviation, *numerical* controlled variables only (N/A for Boolean/enum).
- **Latency** — max lag, *every* controlled variable, with a physics-tethered rationale.
- **Internal variables** — never get latency or tolerance (no promise made about them).

---

## The three quality checks for a detailed requirement set

| Check | Rule | Tell it's violated |
|---|---|---|
| **Completeness** | Every controlled/internal variable has one value in every state | A mode or condition range with no assignment (use UNSPECIFIED if truly none) |
| **Consistency** | No state gets two different values | Overlapping conditions — often a `<` vs `<=` slip at a boundary |
| **Non-duplication** | No outcome stated twice | Literal repetition or overlapping mode/condition ranges |

A condition/event/mode table makes completeness and consistency checkable by eye.

---

## Decision rules

- **Boundary variable or internal artifact?** Apply the *elimination test* — would it still exist if the system vanished? If no, it's an input/output or wire format, not a boundary variable.
- **Monitored variable abstraction level?** Match what the system actually senses. A system that *estimates* altitude from sources should make each source's estimate a monitored variable — not "true altitude."
- **Controlled variable or presentation?** Color/blinking is HMI design, not the boundary. Split into the underlying value + a status.
- **Should this be a mode?** Only if it marks a discontinuity inferable from *observable* behavior. If you can't observe it, it's not a mode.
- **Requirement or rationale?** "What the system does" is the requirement; "why" is rationale — keep them separate. If the *why* is essential to behavior, promote it to a requirement.
- **Eliminate the assumption or keep it?** If strengthening the system removes the assumption, do it (robustness). But keep at least type/range/units.
- **Derived requirement?** A design choice with no higher trace that affects visible behavior or safety (e.g. a saturation clamp range) → flag it as derived and route to the safety assessment.

---

## Tells & smells (warning signs)

- **Wire format as a variable** (e.g. specifying an ARINC 429 word where an abstract quantity belongs) → spec dragged to implementation level, brittle, non-reusable.
- **HMI baked into operational concepts** (keypad vs. dial, buzzer vs. light) → requirements narrowed to one interface; poor operator-interface design is tied to avionics accidents.
- **Trusting unknown/stale monitored values** → add a status attribute; initialize so the variable isn't trusted until first sensed.
- **Over-complex transition diagram** → design decisions leaking into the requirements.
- **Mode confusion** (silent transitions, inconsistent behavior, missing feedback, differing authority limits) → a safety hazard implicated in real aviation accidents.
- **Pulling lower-level detail up into a high-level requirement** → forces undefined vocabulary and defeats the architecture.
- **Rationale as a back-door requirement** → it's non-binding and never verified; the behavior will never be implemented or checked.
- **Copying a trade study into the rationale** → summarize and cite instead.
- **A bare number with no rationale** (the "93°F test") → invites a cost-driven substitution that could be fatal.
- **Subsystem latencies summing past the parent's end-to-end budget** → composed timing must stay within the parent budget.

---

## Two running examples

- **Isolette Thermostat** (Appendix A) — small, single-system, driven all the way to detailed requirements: monitored/controlled variables, safety requirements from hazard H1, INIT/NORMAL/FAILED modes, per-variable rules with latency/tolerance and rationale. Two independent functions: *Regulate Temperature* and *Monitor Temperature*.
- **FCS → FGS / Autopilot** (Appendices B/C/D) — large, about *allocation*: one system spec carved into subsystem specs for different subcontractors; deliberately stops at high-level requirements.
