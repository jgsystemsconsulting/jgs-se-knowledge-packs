# Chapter 5: Verification and Requirements Traceability

## Core Idea
FAA-STD-025f binds interface documentation to verification: IRDs (and ICDs) must define who verifies, any special verification needs, and a Verification Requirements Traceability Matrix (VRTM) with explicit levels and methods so every shall is testable.

## Frameworks Introduced
- **SEM-aligned verification**: Use Test and Evaluation process guidelines from the FAA System Engineering Manual (SEM) verification and validation material, tailored to the VRTM.
- **VRTM one-to-one rule**: Each "shall" maps to exactly one VRTM entry.
- **Three verification levels**: Subsystem/Service (Development), Integration, and Site.
- **Verification methods catalog**: Only methods actually used appear at the top of the VRTM (as defined with the SEM-compatible set in the standard).

## Key Concepts
- **IRD verification section**: Specifies the verification process for interface requirements presented; references SEM T&E guidance.
- **ICD verification section**: Specifies verification process for interface design characteristics.
- **Responsibility for verification (IRD)**: Government is responsible for developing and implementing verification of requirements; may delegate to other organizations, independent contractors, and/or the major prime.
- **ICD verification responsibility**: Documents the contractor's testing responsibilities.
- **Special verification requirements**: List and describe special needs; conformance and interoperability verification for ATN and IPS subsystems; government approves contractor-conducted conformance/interoperability activities; program offices obtain results.
- **VRTM statement**: IRD states verification shall be in accordance with the VRTM table; format complies with (tailored) SEM.
- **Levels**:
  - **Subsystem/Service (Development)**: Usually at contractor facility; culminates in formal acceptance of a contractual end-item.
  - **Integration**: Cross-subsystem/service integration verification.
  - **Site**: On-site/key-site verification of the installed interface.
- **Coverage rule**: All requirements imposed by the IRD technical sections shall be verified at one or more of the three levels.

## Mental Models
- **No orphan shalls**: If you cannot place a shall on the VRTM with level and method, the requirement is not ready to baseline.
- **Delegation is not abdication**: Government may delegate execution but remains responsible for the verification approach on IRDs.
- **Special tests are first-class**: Conformance/interoperability for networking stacks is not an afterthought appendix.

## Anti-patterns
- VRTM rows that do not match shall count.
- Listing methods never used, or using methods not declared.
- Verifying only at subsystem level when site integration risks remain.
- ICDs with no stated contractor test responsibility.

## Key Takeaways
1. Verification scaffolding is mandatory content in IRD/ICD documents.
2. VRTM enforces 1:1 shall-to-verification mapping with SEM-compatible methods.
3. Development, integration, and site levels cover the interface life cycle.
4. ATN/IPS interfaces carry explicit conformance/interoperability expectations.

## Connects To
- **ch03**: IRD shalls that populate the VRTM.
- **ch04**: ICD characteristics under contractor test responsibility.
- **ch02**: Common QA section that introduces verification.
- **ch06**: CM/approval gates that expect verification planning to be present.
