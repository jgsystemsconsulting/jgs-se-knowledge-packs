# Patterns — MIL-HDBK-61B Configuration Management

Reusable CM techniques drawn from the handbook, each with **When to use**,
**How**, and **Trade-offs**. These are the practitioner moves the handbook
endorses, expressed as repeatable patterns — not a restatement of the chapters.

---

## 1. Adopt-and-tailor (don't reinvent CM)

**When to use** — Whenever you need the *requirements* behind a CM activity, or
must put CM on a DoD contract.

**How** — Treat MIL-HDBK-61B as the interpretive layer, not the rulebook. Go to
the adopted EIA-649 suite for what CM requires: EIA-649 for principles, EIA-649-1
(tailored) for contract requirements, GEIA-HB-649 for implementation. Use 61B's
Appendix B to decide *which* requirements belong on this contract in this phase.

**Trade-offs** — 61B cannot be cited as a contractual requirement; contractual
teeth come only from tailored EIA-649-1 and the citing acquisition documents.
Anchor on each concept's definition and map local industry aliases rather than
fighting them — the handbook deliberately declines to enforce one vocabulary.

---

## 2. Progressive baselining (FBL → ABL → PBL)

**When to use** — Deciding what documentation the Government will control and at
which review gate.

**How** — Lock configuration documentation in three stages: the Functional
Baseline (system-level performance) when its FCD is approved; the Allocated
Baselines (CI-level performance/interface) per CI; the Product Baseline (complete
production/re-procurement definition) per CI at its CDR, then finalized and
validated at the PCA. The final PBL drives full-rate production. Once locked,
change happens only through the CCB.

**Trade-offs** — Control authority is now an *independent* variable from the
baseline itself: who approves changes (Government or contractor) is chosen per
acquisition approach, phase, support, and interface needs. Apply Government
control only to the level necessary and let contractor control operate below it.

---

## 3. "Know your starting point" before any change

**When to use** — Before planning, approving, or implementing any configuration
change.

**How** — Establish the current approved configuration (the "current baseline")
as a formal point of reference first. Read every change through "which baseline
am I touching — FBL, ABL, or PBL?" to keep impact analysis honest, since the
FCD→ACD→PCD order of precedence governs conflicts.

**Trade-offs** — Maintaining the audit trail from original requirements through
each incremental baseline (kept in CSA) is ongoing work, but without it change
impact analysis is guesswork.

---

## 4. Route the change by baseline ownership

**When to use** — Dispositioning an ECP or variance — deciding who approves it.

**How** — Apply the routing rule: the Government decides when the change touches
a Government-controlled baselined document, or when a contractor-document change
affects contractually specified performance/supportability for a Government CI.
The contractor decides for its own documents that do not touch Government
baselines. The CDCA is the single content authority per document; if the
contractual approval authority is not the CDCA, it must solicit ECP approval from
the applicable CDCA or pick an alternate design.

**Trade-offs** — Class I ECPs require the CCB plus a contract modification (slow,
formal); Class II changes usually need only local Government representative
concurrence. Whoever holds approval authority is both technically and fiscally
responsible for the change.

---

## 5. Use the right change instrument (ECP / NOR / RFV)

**When to use** — Selecting the documentary vehicle for a change or exception.

**How** — Match the instrument to the intent: the **ECP** carries the change
itself; the **NOR** pins down the precise edits to a specific affected document;
the **RFV** buys a bounded permission to deliver/install something off-baseline.
Talk before you file — clear pre-ECP communication among Government, CDCA, and
contractor (ideally in an IPT) is one of the largest contributors to control
efficiency.

**Trade-offs** — RFV approval (minor/major/critical) is an inherently
Governmental, non-delegable function requiring negotiated consideration. Recurring
RFVs against the same characteristic are a warning sign — escalate to a Class I
ECP to fix the requirement, not a standing exception.

---

## 6. Treat CSA as exhaust, then query it

**When to use** — Building program visibility and CM metrics.

**How** — Let status accounting accumulate as a by-product of normal CM
transactions rather than instrumenting a separate process. Query the CSA database
for as-designed / as-built / as-delivered / as-modified views — currently and as
of any prior date. Build metrics from CSA data: each metric needs an operational
definition, a data query, and a presentation format (run/control chart, Pareto,
histogram, cause-and-effect).

**Trade-offs** — Government and contractor each account only for the data they
control or support; shared seams (warranty being canonical) must be coordinated
deliberately. Use a few critical, forward-focused metrics — score-keeping metrics
are explicitly the wrong design.

---

## 7. Build verification in; make audit a settlement

**When to use** — Planning V&V and audits for a CI across its life.

**How** — Embed configuration verification (functional + physical) inside the
contractor's own build/modify process so the Government can *validate the process*
in place of independent physical inspection where appropriate. Scale change
verification to the change (inspection → test series → full audit). Run audits in
three phases (pre-audit, audit, post-audit) and do not declare success until every
action item is closed. FCA answers "does it perform?"; PCA answers "does the
documentation match what we deliver and support?".

**Trade-offs** — Expect audits in EMD and early production, not MSA/TMRR; PCA
commonly slips toward production when EMD articles are unrepresentative prototypes.
A weak verification process forces a heavyweight, adversarial audit.

---

## 8. Pass all three data gates (order ≠ own ≠ hold)

**When to use** — Acquiring the technical data CM will control.

**How** — Clear three separate gates: **order** the data via a CDRL/DID tied to a
SOW task; secure the **rights** to use it (FFF and OMIT data are unlimited
automatically; otherwise funding source sets unlimited / Government purpose /
limited-restricted, negotiable upward); and **hold** the official master copy in a
Government PDM-type system. Make bidders disclose use restrictions
(DFARS 252.227-7017) before award. Never substitute access for delivery.

**Trade-offs** — Determine needs broadly across every functional area, then
de-duplicate in a requirements review — over-ordering and under-acquiring are both
named cost drivers. Contractor-only storage is rejected: markings can be altered
and large datasets are hard to recover when the contract ends.

---

## 9. Designate one master; keep derived/transformed data in sync

**When to use** — When copies of configuration data proliferate across IT systems.

**How** — Designate the authoritative master instance, place it under
configuration control, and notify copy-owners of any master change so they can
assess impact. Regenerate derived data (e.g., provisioning lists) and transformed
data (e.g., a 2D drawing from a 3D model) whenever the master changes. Treat
technical data as a shared DoD corporate asset, not a hoarded program asset.

**Trade-offs** — Requires a consolidated, trusted IT environment; redundant,
non-interoperable PDM systems drive cost and violate portfolio-management guidance.

---

## 10. Extend CM into the digital environment

**When to use** — Operating model-based engineering, digital twins, or reuse
libraries.

**How** — Bring three new object classes under CM: models/viewpoints/datasets;
digital artifacts; and processes/algorithms/computations (IEEE 828). Apply
approved changes to the *baseline digital environment* so regenerated static
artifacts reflect the approved configuration, preserving traceability between
baseline model and artifact. For digital twins, capture each unit's as-built and
as-maintained configuration, not just the as-designed baseline.

**Trade-offs** — Data volumes multiply and new authoring tools are needed; the CM
*principle* is constant but its scope widens. Reuse libraries need version control,
parallel-development, and build management so reuse improves quality without
introducing errors.

---

## 11. Make modularity hold at the interface (MOSA)

**When to use** — Implementing a Modular Open Systems Approach.

**How** — Separate the system into standards-based, verifiable modules and put the
modular technical baselines and interface specifications/standards/control drawings
under strict configuration control, confirmed early. Control MOSA CI form, fit,
function, and interface characteristics. Make MOSA a proposal evaluation criterion
and secure the COTS data and rights the strategy needs. Document and control all
external interfaces and dependencies.

**Trade-offs** — COTS/NDI brings IP-rights, single-source, and obsolescence risk
(you may have to maintain multiple configurations of one product). An uncontrolled
or undocumented interface quietly recreates the vendor lock-in MOSA was meant to
break.

---

## 12. Tailor CM per phase (subtract from a vetted maximum)

**When to use** — Putting CM requirements on a contract for a specific life-cycle
phase.

**How** — Start from EIA-649-1's full "shall"-statement catalog and *remove* what
the phase does not need. Use the Figure B-1 R/T/NR matrix to decide whether each
requirement applies in this phase, then EIA-649-1 Annex A (the Tailoring
Worksheet — usable directly in contracts) to select the specific statements, put
them in the tasking document, and execute via GEIA-HB-649. Use the Appendix C
phase templates (TMRR/EMD/P&D/O&S) to see *what* each function looks like once
selected — read the risk column as the business case for funding it.

**Trade-offs** — Requirements drive cost, so importing the standard wholesale is
the named failure mode. There is no MSA template (CM not applicable pre-Milestone
A); audits are central in EMD/Production but absent in TMRR and O&S. Keep tailored
practice matched to product complexity — over-tailoring a complex item is as
hazardous as over-specifying a simple one.
