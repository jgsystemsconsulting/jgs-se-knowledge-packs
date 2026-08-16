# Chapter 6: Revisions, Configuration Management, and Approval

## Core Idea
Once baselined, IRDs/ICDs change through full document revisions under FAA configuration management (Order 1800.66)—not a separate "interface revision" artifact. Appendix I defines development/approval flow, roles, and the IRD-before-ICD timing rule.

## Frameworks Introduced
- **Revision-not-delta model**: Historical special Interface Revision documents are obsolete; issue a new revision number that supersedes the prior IRD/ICD.
- **CM anchor**: Submit revised IRD/ICD for approval per FAA Order 1800.66 (NAS Configuration Management Procedures).
- **Appendix I process guide**: Overview of interface management, IRD development/approval, roles, and ICD approval as a subset of the IRD path.
- **Facility IRD iteration model**: Initial, Primary, Intermediate, and Final maturity stages.

## Key Concepts
- **Reasons to revise**: Improve/expand requirements; complete incomplete documents; align with actual design/operation; resolve incompatibility; document interface changes; correct errors.
- **IRD timing**: Start early in acquisition; must be in place before SOW finalization when used in procurement packages (except facility IRDs' different use).
- **ICD timing**: If both required, IRDs must be approved prior to ICD; ICD implements IRD requirements in design. Revisions can occur anytime after baselining.
- **Facility IRD iterations**:
  - **Initial**: Minimal data; reserves transition planning scope (space/prep).
  - **Primary**: After system specification; mixes assumptions and firm data.
  - **Intermediate**: After prototype or first-article testing.
  - **Final**: Refined from acceptance or key-site testing.
- **Roles (Appendix I)**:
  - **Project Management (PM)**: Owns program coordination and need for the interface documents.
  - **IRD Author**: Develops/maintains content (FAA or appropriate contractor).
  - **Interface Working Group**: Cross-party technical coordination forum.
  - **NAS SE Requirements and Interface Management Group**: Enterprise interface governance participant.
  - **System Engineer**: Technical integrity of requirements/design alignment.
  - **Configuration Management (CM)**: Baselining, revision control, release under 1800.66.
- **ICD approval**: Subset of the IRD/revision approval process; developer prepares the formal agreement of form/fit/function.

## Mental Models
- **Superseding baselines**: Each approved revision replaces the prior baseline entirely for CM purposes.
- **Procurement coupling**: Non-facility IRDs travel with the contractor package so design aims at a shared boundary.
- **Working group before signature**: Technical concurrence in the IWG reduces approval thrash.

## Anti-patterns
- Trying to patch interfaces with informal emails instead of a numbered revision.
- Finalizing SOW without a needed IRD.
- Approving ICD content that conflicts with an unrevised IRD.
- Stopping facility IRDs at "initial" while construction decisions proceed.

## Key Takeaways
1. Revisions are full reissues under Order 1800.66 CM, not side delta forms.
2. IRD precedes ICD when both are required; start IRDs early.
3. Facility IRDs mature through four planned iterations.
4. PM, author, IWG, SE, enterprise interface group, and CM share distinct duties.

## Connects To
- **ch01**: Baselining and TBS closure via revision.
- **ch03–ch04**: Content that must stay consistent across revisions.
- **ch05**: Verification updates when shalls change.
