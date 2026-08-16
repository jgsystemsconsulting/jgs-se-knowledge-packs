# Patterns — DoD M&S VV&A RPG

## 1. Intended-Use Lock-In
- **When:** Starting any new M&S or reuse for a new decision.
- **How:** Write who/what/when/stakes; derive acceptability criteria before deep design or V&V spend.
- **Trade-offs:** Up-front debate vs endless rework of validation scope.

## 2. Single V&V Thread with Specialists
- **When:** Staffing V&V for new development.
- **How:** Prefer one V&V Agent organization from the start; add SMEs/labs for specialized tests.
- **Trade-offs:** Coordination overhead vs split learning curves and late validation starts.

## 3. Build-for-Observability
- **When:** Architecture and sprint planning.
- **How:** Require logs, probes, scenario control, and CM identity so verification/validation can run.
- **Trade-offs:** Instrumentation cost vs unverifiable “black box” claims.

## 4. Referent-First Validation Design
- **When:** Planning validation cases.
- **How:** Choose referent type and comparison method per critical behavior; document domain of applicability.
- **Trade-offs:** Hard referent work vs easy but weak face-only comfort.

## 5. Fidelity by Attribute
- **When:** Requirements and design reviews.
- **How:** Specify fidelity per decision-driving attribute; explicitly list non-goals.
- **Trade-offs:** Nuanced specs vs false single-score fidelity marketing.

## 6. Data as Configuration
- **When:** Any accredited or baseline run.
- **How:** Pin dataset versions, transforms, and pedigree alongside software baselines.
- **Trade-offs:** CM discipline vs silent data drift invalidating prior V&V.

## 7. Residual-Risk Accreditation
- **When:** Preparing Authority decisions.
- **How:** Map each claim to evidence or an explicit residual risk/constraint.
- **Trade-offs:** Political discomfort vs hidden operational Type II risk.

## 8. Delta-VV&A on Reuse
- **When:** Reusing legacy M&S for a new intended use.
- **How:** Gap-analyze prior evidence; plan only the delta V&V and re-accreditation triggers.
- **Trade-offs:** Analysis effort vs blind reuse of old accreditation letters.

## 9. Contract for Access
- **When:** Procuring M&S development.
- **How:** Encode independent V&V access, data rights, deliverable evidence, and participation in the SOW.
- **Trade-offs:** Negotiation time vs unverifiable contractor black boxes.

## 10. T&E Bridge
- **When:** M&S supports DT/OT or live test planning.
- **How:** Align VV&A products with T&E strategy evidence needs; route to dote/dod-te packs for enterprise T&E.
- **Trade-offs:** Dual frameworks vs disconnected digital and live evidence stories.
