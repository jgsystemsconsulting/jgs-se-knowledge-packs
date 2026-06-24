# NASA NPR 7150.2D Cheatsheet

Decision rules, selection tables, and tells & smells for applying NPR 7150.2D.
All values are from the directive (Rev D, effective March 8, 2022).

## Quick Decision Rules

**"Which requirements actually apply to my software?"**
Classify the system/subsystem (Appendix D, SWE-020) → read the "X" cells for that class in the Requirements Mapping Matrix (Appendix C). "X" = mandatory; blank = optional/not invoked.

**"Two classes both seem to fit — which do I pick?"**
The higher (more rigorous) one. Ambiguity always rounds up.

**"Is this software safety-critical, and can it be Class E?"**
If it could lead to severe injury, major damage, or mission failure when done wrong, it is safety-critical → it must be Class D or higher. Class E can never be safety-critical.

**"Can I skip a requirement?"**
Only via tailoring: rationale + risk evaluation + impacted-discipline concurrence + named-authority signature in the RMM + responsible manager's formal risk acceptance. No signature, no relief.

**"Who approves the tailoring?"**
The authority named for that requirement in Appendix C. Cybersecurity (Section 3.11) relief also needs the SAISO signature; IV&V (SWE-141) relief is the Chief of SMA's call; human-safety risk needs the actual risk takers to agree.

**"Is it verification or validation?"**
Against specified requirements → verification ("built it right"). Against intended use in the target environment → validation ("built the right thing").

**"Bought, reused, or auto-generated — lighter V&V?"**
No. Verify and validate to the same level as an equivalent developed component (SWE-027, SWE-146).

**"My coverage isn't 100% — now what?"**
Classify the gap: missing requirement / missing test / extraneous (dead) code / deactivated code. Each demands a different fix (SWE-189/190).

---

## The Six Software Classes at a Glance

| Class | Name | Worst-case consequence driver |
|---|---|---|
| **A** | Human-Rated Space Software Systems | Loss of life / primary human-spaceflight mission |
| **B** | Non-Human Space-Rated Systems or Large-Scale Aeronautics Vehicles | Loss of non-human mission / large vehicle ($250M+ life-cycle, per NPR 7120.8) |
| **C** | Mission-Support, Smaller Aeronautics, or Major Facility Software | Harm to secondary objectives / operational problems |
| **D** | Basic Science/Engineering Design and Research-and-Technology Software | Development and basic-research impact only |
| **E** | Design Concept, Research, Technology, General-Purpose Software | At worst one user or a small group (never safety-critical) |
| **F** | General-Purpose Computing, Business, and IT Software | Productivity of many users; cost/schedule/technical impact |

Five classification factors: usage with/within a NASA system, system criticality, human dependence, developmental/operational complexity, Agency investment.
Tiebreaker on definition disputes: the NASA Chief Engineer.

---

## Requirement-Vocabulary Key (Preface, item g)

| Verb | Meaning |
|---|---|
| **shall** | Mandatory; carries a numbered SWE identifier |
| **should** | Recommended good practice |
| **will** | Expected outcome (not a requirement on the actor) |
| **may / can** | Discretionary permission |
| **is / are** | Descriptive material |

---

## Chapter Map (where the requirements live)

| Ch | Scope |
|---|---|
| 2 | Roles, responsibilities, tailoring (largely outside the Appendix C matrix) |
| 3 | Software management: classify, plan, cost, schedule, train, secure, assure, trace |
| 4 | Life-cycle engineering: requirements → architecture → design → implementation → test → ops/maintenance/retirement |
| 5 | Supporting disciplines: SCM, risk, peer reviews/inspections, measurement, non-conformance |
| 6 | Recommended software records (menu, content in NASA-HDBK-2203) |

---

## Key Quantitative Gates and Thresholds

| Gate / threshold | Value | Where |
|---|---|---|
| MC/DC coverage, safety-critical | 100% | SWE-219 |
| Cyclomatic complexity, safety-critical | ≤ 15 (exceedance waived w/ rationale) | SWE-220 |
| CMMI-DEV maturity, Class A | Level 3 or higher | SWE-032 |
| CMMI-DEV maturity, Class B | Level 2 or higher | SWE-032 |
| Cost models, Class A/B at ≥ $2M | At least two | SWE-015 |
| MOTS "modified" upper bound | ~30% code changed (beyond → new development) | Appendix A |
| MOTS lower bound | ~5% changed may not count as "modified" | Appendix A |
| Major facility, Current Replacement Value | ≥ $50M | Appendix A |
| Major facility, Mission Dependency Index | ≥ 70 | Appendix A |
| Large-scale aeronautics (Class B) life-cycle cost | > $250M (per NPR 7120.8) | Appendix D |

---

## Selected SWE Requirement Numbers (high-traffic)

| SWE | What it requires |
|---|---|
| SWE-013 | Develop and execute software plans (incl. security) with approved tailoring |
| SWE-020 | Classify each system/subsystem at the highest applicable class |
| SWE-021 | Update plans/contracts when a system migrates class |
| SWE-027 | Off-the-shelf/reused-component discipline (V&V to same level) |
| SWE-032 | CMMI-DEV rating by class |
| SWE-052 | Bidirectional traceability across the element chain |
| SWE-125 / SWE-139 | Maintain the RMM; "X" requirements are mandatory |
| SWE-134 | Safety-critical behavioral (safe-state) requirements |
| SWE-135 | Static analysis during development and test |
| SWE-141 | IV&V applicability (gated by category/payload/MDAA selection) |
| SWE-146 | Auto-generated code held to developed-code standard |
| SWE-205 | Safety-critical determination per NASA-STD-8739.8 |
| SWE-219 / SWE-220 | 100% MC/DC; complexity ≤ 15 |

---

## Companion Documents (don't confuse with the NPR)

| Document | Role |
|---|---|
| **NASA-HDBK-2203** | Software Engineering Handbook — content, timing, tailoring guidance (not binding) |
| **NASA-STD-8739.8** | Software Assurance & Software Safety Standard — binding; safety-critical and IV&V criteria |
| **NASA-STD-8739.9** | Software Formal Inspection Standard — inspection best practice |
| **IEEE 828-2012** | Configuration management reference for 5.1 |
| **CMMI-DEV** | External maturity benchmark for development organizations |
| **NPR 7123.1** | Systems Engineering Processes — supplies milestone reviews |
| **NPR 7120.5/7/8** | Program/project management — supplies life-cycle phases |

---

## Tells & Smells

- **"It just flies in space, so it's Class A."** Venue ≠ class. Consequence and dependence decide; a personal music player aboard a crewed vehicle is not Class A.
- **"We bought it / reused it, so the V&V is lighter."** Wrong bar. Same level as a developed component.
- **"The requirement is marked Not-Applicable" with no rationale.** A TA must confirm a Not-Applicable is genuinely inapplicable; an unjustified N/A is a finding.
- **A relief request with no signature.** Tailoring without the named authority's signature in the RMM is not approved tailoring — it is an unbacked compliance gap.
- **A high-severity non-conformance closed when the bug is fixed.** Not closed: a process assessment must ask why the process allowed it (closed-loop).
- **Build tools and compiler versions left out of configuration control.** They shape the software and must be in the CM ledger; otherwise the build is not reproducible.
- **An uncontrolled printed copy treated as authoritative.** Verify the current version in the NODIS Library; printed copies are uncontrolled.
- **Treating coding bugs as "just quality."** Buffer overflows and inconsistent error handling are also cybersecurity weaknesses under this directive.
