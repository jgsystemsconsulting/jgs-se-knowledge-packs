# Chapter 1: CUI Scope, Fundamentals, and Requirement Structure

## Core Idea
NIST SP 800-171 Rev. 3 defines recommended security requirements that federal agencies place on nonfederal organizations so Controlled Unclassified Information (CUI) keeps a consistent confidentiality posture whether it lives in federal or contractor systems. The publication is a tailored subset of the SP 800-53 moderate baseline, organized into 17 requirement families with discussion text and organization-defined parameters (ODPs).

## Frameworks Introduced
- **CUI protection model for nonfederal systems**: Same safeguarding intent as federal moderate confidentiality, applied only to components that process, store, transmit, or protect CUI.
- **Tailoring from SP 800-53B moderate baseline**: Drop controls that are primarily a federal responsibility, unrelated to CUI confidentiality, redundant, or not applicable.
- **Organization-defined parameters (ODPs)**: Assignment/selection slots that agencies (or, if unset, the nonfederal organization) fill so requirements become assessable.
- **Requirement anatomy**: Normative statement + informative discussion + source-control references (not a second set of mandates).

## Key Concepts
- **Controlled Unclassified Information (CUI)**: Information that law, regulation, or government-wide policy requires to be safeguarded or dissemination-controlled, excluding classified national security information.
- **Nonfederal organization / nonfederal system**: Any entity or system that is not a federal information system; the pack’s requirements target these when they handle CUI under contract or agreement.
- **Scope boundary**: Requirements apply only to CUI-touching components (and their protectors). Isolating CUI into a separate security domain (physical and/or logical) can limit investment without over-hardening the whole enterprise.
- **Confidentiality focus with integrity coupling**: Primary objective is confidentiality of CUI; many mechanisms also support integrity, and unauthorized modification is in scope.
- **Seventeen families**: Access Control; Awareness and Training; Audit and Accountability; Configuration Management; Identification and Authentication; Incident Response; Maintenance; Media Protection; Personnel Security; Physical Protection; Risk Assessment; Security Assessment and Monitoring; System and Communications Protection; System and Information Integrity; Planning; System and Services Acquisition; Supply Chain Risk Management.
- **Families deliberately omitted from 800-53**: PII Processing and Transparency (PII is a CUI category, not a separate family here); Program Management (not baseline-linked); Contingency Planning for availability (with limited backup-confidentiality exceptions).
- **Discussion vs requirement**: Discussion sections explain intent and give notional examples; they do not expand the normative statement or prescribe a single solution.
- **Assessment companion**: SP 800-171A supplies assessment procedures derived from SP 800-53A; this pack does not replace 171A.
- **Exceptions path**: Enduring limitations (e.g., specialized OT/medical devices) are documented in the system security plan (03.15.02); temporary gaps go into plans of action and milestones (03.12.02).

## Mental Models
- Think “moderate confidentiality overlay for contractors,” not “full federal RMF authorization package.”
- Scope first, then implement: identify CUI flows and isolate them before buying controls for the entire estate.
- ODPs are the contract’s dials — if the agency leaves them blank, the nonfederal org must set values to make the requirement complete and testable.
- Tailoring already happened upstream (NIST removed many 800-53 controls); do not re-expand the set unless a specific CUI category’s authorizing instrument demands more.

## Anti-patterns
- **Applying 800-171 to systems that never touch CUI**: Over-scoping burns budget and creates false compliance theater.
- **Treating discussion examples as mandatory configurations**: Examples are illustrative, not exhaustive baselines.
- **Ignoring FISMA boundary**: Organizations operating systems *on behalf of* a federal agency fall under FISMA/full federal control sets, not this publication’s nonfederal CUI set.
- **Assuming availability/contingency is fully covered**: CP family was largely tailored out; backup confidentiality is the notable exception path.

## Key Takeaways
1. SP 800-171r3 is the federal-to-nonfederal bridge for CUI confidentiality, derived from the SP 800-53 moderate baseline via explicit tailoring criteria.
2. Applicability is component-scoped: CUI processors/stores/transmitters and the components that protect them.
3. Seventeen families carry the requirements; each item pairs a normative statement with informative discussion and SP 800-53 provenance.
4. ODPs must be filled — by the agency or, failing that, by the nonfederal organization — before assessment can be meaningful.
5. CUI impact is treated as no less than moderate confidentiality unless a category-specific law/policy sets different controls.
6. Document enduring exceptions in the SSP and track deficiencies via POA&M rather than silently skipping requirements.

## Connects To
- **ch02–ch08**: Detailed family coverage grouped for progressive disclosure.
- **NIST SP 800-53 / 800-53B**: Source control catalog and moderate baseline used for tailoring.
- **NIST SP 800-171A**: Assessment procedures for these requirements.
- **NARA CUI program / 32 CFR 2002**: Categories, marking, and federal CUI handling context that drive when 800-171 is invoked.
- **FIPS 199 / FIPS 200**: Impact categorization and minimum security requirements underlying the moderate confidentiality assumption.
