# Patterns — FAA-STD-025f

## 1. IRD-First Boundary Contract
- **When:** New or upgraded FESS/NAS interface needing bilateral agreement before design freeze or SOW finalization.
- **How:** Author IRD with shalls, scope template, responsibility list, and VRTM; baseline under CM; only then author ICD characteristics.
- **Trade-offs:** Upfront coordination cost vs costly redesign from ambiguous boundaries.

## 2. Explicit N/A / TBS Slots
- **When:** Outline requires a section that is not applicable or not yet knowable.
- **How:** Use standard N/A sentence for non-applicable titled items; mark TBS in IRDs and schedule a revision; avoid silent blanks.
- **Trade-offs:** Slightly verbose documents vs hidden gaps that fail review.

## 3. Interface-Type Outline Selection
- **When:** Starting a new IRD/ICD.
- **How:** Use the standard decision tree to pick facility/analog/discrete vs general-service/web-service outline; do not mix trees ad hoc.
- **Trade-offs:** Constrained structure vs reviewer familiarity and completeness.

## 4. Bilateral Security Risk Pass
- **When:** Writing IRD security requirements.
- **How:** Jointly assess sensitivity/criticality and exposure at both ends; document every security-relevant layer; cite applicable FAA orders.
- **Trade-offs:** Workshop time vs one-sided security assumptions.

## 5. Single Power Baseline
- **When:** One subsystem supplies power across the interface.
- **How:** Choose either FAA-G-2100g or 2100h once; specify voltage/frequency/current/transients/protection/grounding/connectors consistently in IRD and ICD.
- **Trade-offs:** Early equipment constraint vs incompatible power assumptions.

## 6. VRTM as Exit Criteria
- **When:** Approaching IRD baseline or test planning.
- **How:** Enforce 1:1 shall-to-row mapping; declare only used methods; assign Development/Integration/Site levels; include special ATN/IPS conformance needs.
- **Trade-offs:** Matrix maintenance vs unverifiable shalls.

## 7. Facility IRD Maturity Waves
- **When:** Site preparation depends on evolving subsystem data.
- **How:** Plan Initial→Primary→Intermediate→Final IRD iterations tied to spec, prototype, and key-site evidence.
- **Trade-offs:** Multiple CM cycles vs frozen wrong space/power data.

## 8. Full-Document Revision under 1800.66
- **When:** Any baselined IRD/ICD must change.
- **How:** Issue superseding revision (not a side delta form); route approval per Order 1800.66; keep ICD aligned after IRD changes.
- **Trade-offs:** Formal overhead vs configuration chaos.
