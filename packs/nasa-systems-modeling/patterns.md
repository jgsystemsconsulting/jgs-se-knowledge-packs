# NASA Systems Modeling Handbook — Patterns & Techniques

Reusable modeling patterns drawn from NASA-HDBK-1009A, each with *When to use*, *How*,
and *Trade-offs / cautions*. These paraphrase the handbook's guidance; they are not a
substitute for NPR 7123.1 or the NASA SE Handbook, which govern.

---

## 1. Separate the three aspects before you start

**When** — at the outset of any MBSE effort, to avoid the classic confusion of language, method, and organization.

**How** — set three independent dials explicitly: the **language** (what symbols mean — SysML here), the **methodology** (what order to do things in — NASA SE Engine + the two OOSEM steps), and the **framework** (where things go — the MBSE Grid). Record the choices, including the language binding, in the Modeling Plan.

**Trade-offs** — a language gives structure and rigor but no procedure; a procedure does not tell you how to organize results. Because the metamodel sits underneath all three, the language dial can be swapped without disturbing the others — but only if you have kept them distinct in the first place.

---

## 2. Write a Modeling Plan as a SEMP subset, then keep it living

**When** — early in the life cycle, during Technical Process 10 (Technical Planning), before substantive modeling.

**How** — produce a Modeling Plan inventorying the project products the models support, modeling resources, roles and responsibilities, tools, conventions, model accessibility, and model management. Trace every modeling decision up to a SEMP / NPR 7123.1 obligation. Seed it from a Modeling Plan Template (NASA MBSE Community of Practice). Revisit and update it at each life-cycle transition.

**Trade-offs** — a plan written once at concept and never revisited goes stale and stops describing the truth. If a modeling decision can't be traced up to a SEMP/NPR obligation, it probably doesn't belong in the plan.

---

## 3. Set up the model — name it, govern it, file it

**When** — at "Step 0," the start of the System Design Processes, before drawing elements.

**How** — make three setup decisions: **conventions** (naming rules for elements and packages), **standards** (standard profiles and other modeling standards per project need), and **organization** (a package structure/hierarchy that reflects the system hierarchy). Document all three back into the Modeling Plan. Figure 6-1's sample organization is a starting point, not a mandate.

**Trade-offs** — setup without a plan yields a tidy model that supports no SE product; a plan without setup leaves modelers with intentions but no scaffold. Filing should mirror the system's own hierarchy, which only the project knows.

---

## 4. Build a trace-back metamodel, language in brackets

**When** — when you need a model that is auditable against NASA SE process rather than a tool's idiosyncrasies, or when you already have a modeling approach and must show it connects to NASA SE elements.

**How** — base the metamodel on the SE elements and relationships in NPR 7123.1 (Figures 7-1 general, 7-2 V&V). Keep the language-specific type in square brackets — `[requirement]`, `[block]`, `[derives]` — so the SE concept stays fixed while the bracketed type is pluggable. Use the metamodel as a Rosetta Stone (trace-back), not a cage you must build inside. Record the adopted metamodel and its assumptions in the Modeling Plan.

**Trade-offs** — figures are simplified ("shown at one level for simplicity"); treat each drawn relationship as a representative instance that can exist at many levels. The binding to SysML 1.7 is current-state — plan for the migration to SysML v2.0.

---

## 5. Pair every diagram with its metamodel fragment

**When** — whenever building or reviewing a sample SysML diagram or table (the engine of handbook Section 8).

**How** — show the relevant slice of the section 7 metamodel beside the concrete SysML view. When you see a diagram, ask which metamodel elements and relationships it is permitted to use — that fragment is the grammar; the diagram is one sentence. Build the diagrams in any order, since SE work can enter the SE Engine at multiple points.

**Trade-offs** — skipping the fragment lets a diagram drift to elements/relationships the metamodel does not sanction, breaking traceability. The "any order" freedom is real: do not impose a stakeholders→context→behavior→structure→requirements waterfall.

---

## 6. One element, many views — choose the diagram for the question

**When** — when deciding how to present model content for a given audience or section.

**How** — render the same underlying elements through the view that fits the question: context as a **bdd** (cataloging) *and* an **ibd** (interconnection); activities as an **activity diagram** (flow) *and* a **functional-decomposition bdd** (hierarchy); requirements as a **req diagram** (graph) *and* a **table** (spreadsheet). For behavior: modes/triggers → state machines; ordered interactions → sequence diagrams; flow + allocation → activity diagrams; capability-from-the-user's-view → use cases.

**Trade-offs** — the diagram type is a choice of emphasis, not a different truth; the model holds one set of facts. Ports can be shown or hidden and detail offloaded to tables — visual fidelity is adjustable to audience, while the model stays precise underneath.

---

## 7. Model V&V once, swap the relationship for validation

**When** — when building verification and validation content.

**How** — learn the verification thread first: a requirement with a success-criteria **constraint** (curly braces), traced to higher requirements, owning a V&V **case** that owns an **activity**, referencing a shared V&V **configuration** (equipment, personnel, facilities). Carry `verifies` (one system requirement can have many verification requirements). For validation, reuse the identical shape and swap `verifies` for `satisfies`. Put the `verifyMethod` on the requirement early and migrate it to the verification requirement as the life cycle matures. Treat a requirements diagram and its matrix/VCS as two windows on one model.

**Trade-offs** — much validation can be discharged through verification activities, so a validation activity may reuse verification work. Matrix columns are a modeling choice — the handbook documents exactly which it adds/drops versus NASA/SP-2016-6105 Tables D-1/E-1 (e.g. the facility column is omitted because that data lives in the V&V configuration parts).

---

## 8. Harvest the model into work products (cut list, not authored prose)

**When** — when standing up the NPR 7123.1 SE work products (ConOps, MOE, MOP, TPM, V&V) for a technical review.

**How** — treat each work product as a *named set of views* — a figure (the view family) plus a table (the bill of materials with Section 8 references) — extracted from the populated model. Extract by hand or third-party tools; place into report templates, export to webpages/viewers, or browse in-tool. Hold the measure chain as a descending ladder: **MOE** (qualitative satisfaction) → **MOP** (quantitative target) → **TPM** (time-tracked subset of MOPs).

**Trade-offs** — tailoring is a feature: produce the subset of views that fits the program's maturity and the review at hand, not the full menu. For shared V&V views, you may split them per process when that serves the project.

---

## 9. Tailor the MBSE Grid to NASA's processes

**When** — when organizing where diagrams and tables live across the modeling effort.

**How** — map the Grid's problem (black box / white box) and solution rows onto NASA's four System Design Processes: Stakeholder Expectation Definition → black box; Technical Requirements Definition + Logical Decomposition → white box; Design Solution Definition → solution. Put processes 1–9 on rows, the four pillars on columns; file diagrams and tables in the cross-sections (Appendix C shows a populated grid). Append extra rows to reach product-realization steps if needed.

**Trade-offs** — the Grid deliberately excludes technical-management processes 10–17. The same diagram can legitimately appear in more than one row (e.g. behavior in both Logical Decomposition and Design Solution), reused with content tuned per process.

---

## 10. Reach for an alternative approach as a pillar-targeted extension

**When** — when the base metamodel needs sharpening in one pillar (numerical requirements, ConOps scenarios, structure-to-requirements tracing, or V&V simulation).

**How** — select from Appendix D as a menu, each a pluggable extension to a single pillar: **PBR** (Requirements — numerical attributes/constraints), **Scenario Modeling** (Behavior — a context block bridging activities and state machines), **System Specification** (Structure→Requirements bridge), **Verification Modeling** (V&V/parametric layer). Ensure your constructs still trace back to the section 7 metamodel, and record the choice in the Modeling Plan.

**Trade-offs** — these are targeted extensions, not competing whole methodologies; mixing several is fine as long as traceability to NASA SE elements holds. Three of them (Scenario, System Specification, Verification) come from The OpenSE Cookbook, an external source.

---

## 11. Overlay model content onto the ConOps outline (draw once, reference many)

**When** — when producing a ConOps that should be consistent with the system model rather than authored separately.

**How** — keep the NASA SE Handbook (Appendix S) ConOps outline text intact and insert MBSE views only where they add value: context bdd/ibd for overview and interfaces, requirements table/diagram for NGOs, state machines for modes, use cases and activity decomposition for capabilities, scenario/DRM behavior diagrams for operational threads. When a view fits more than one section, reference the earlier figure rather than re-pasting it. Label threads (e.g. `[DRM-0100]`) for traceability. Keep system/key-element descriptions implementation-free.

**Trade-offs** — model only what drives the design (e.g. environment content that will shape it), not an encyclopedia. Sections without a strong model story (Documents, impact/risk narratives) stay primarily textual; the handbook's risk-as-block example is minimal and other risk-modeling methods are out of scope in this version.
