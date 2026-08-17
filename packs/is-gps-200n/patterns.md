# Patterns — ICD Exemplar from IS-GPS-200N

## Pattern: Definition, then identification, then criteria
- **When**: Starting any new ICD/IS.
- **How**: One-paragraph interface object (who talks to whom, over what); named parts list with applicability tags; then measurable shalls. Keep bit maps in annexes.
- **Trade-offs**: Readers flip to appendices for details; the body stays reviewable in one sitting.

## Pattern: Reserved empty sections
- **When**: A template has unused clause numbers.
- **How**: Print “NOT APPLICABLE” and keep the numbers so later IRNs do not renumber every reference.
- **Trade-offs**: Slightly odd outline; stable cross-references.

## Pattern: PIRN / ICWG / CCB paper trail
- **When**: Changing a public interface.
- **How**: Anyone in the working group proposes; contractor writes PIRN; 45-day review; board approves; fold into the next revision letter. Cite IRN/RFC IDs in the record.
- **Trade-offs**: Slow versus hallway agreement; auditable for every receiver vendor.

## Pattern: Payload families with annex homes
- **When**: The interface carries messages too large for the body.
- **How**: Name the family, rate, host signal, and appendix. Split annexes when identifier neighborhoods diverge (here, PRN 1–32 vs 33–63).
- **Trade-offs**: Two places to maintain LNAV; decoders do not break when the upper neighborhood changes.

## Pattern: Hygiene definitions next to the shalls
- **When**: Fields like URA, reserved, invalid, or issue-of-data will be misread.
- **How**: Put normative definitions in notes (or a glossary annex) and force CEI-as-a-set / health-protocol behavior.
- **Trade-offs**: Extra reading; far fewer silent interoperability bugs.

## Pattern: Complementary preparation pack
- **When**: The user asks “how do I write our ICD?”
- **How**: Route to `faa-std-025` for outlines, VRTM, and CM. Stay here for “what a finished IS looks like.”
- **Trade-offs**: Two slugs to remember; avoids turning either pack into the other.
