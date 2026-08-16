# Chapter 1: Scope and the IRD/ICD Document Family

## Core Idea
FAA-STD-025f standardizes how the FAA and its contractors prepare **Interface Requirements Documents (IRD)** and **Interface Control Documents (ICD)** for key interfaces among FAA Enterprise Subsystems (FESS), National Airspace System (NAS) subsystems, facilities, and external entities. It sets format and minimum content so interface agreements are complete, verifiable, and configuration-managed.

## Frameworks Introduced
- **IRD vs ICD pairing**: IRD states *what* the interface must satisfy (shall-requirements); ICD records *how* those requirements are implemented (as-built design characteristics).
- **FESS applicability**: Applies to programs acquiring, upgrading, or developing FAA Enterprise Subsystems, including NAS operational, support, and administrative subsystems and external interfaces.
- **Order of precedence**: Conflicts among documents are resolved by the controlling acquisition/order hierarchy; this standard governs preparation of IRD/ICD content and format.
- **Interface-type decision tree**: Content outlines differ for facility, analog, discrete, general service, and web-service interfaces.

## Key Concepts
- **IRD purpose**: Capture interface requirements between two subsystems, a subsystem and a multi-fill "user," or a facility and a subsystem/service. Requirements often trace to or derive from system-level specifications.
- **ICD purpose**: Formal agreement documenting how IRD requirements are implemented; becomes the as-built configuration baseline for the interface.
- **Baselining**: Approved IRDs/ICDs become baseline documents under configuration management (see FAA Order 1800.66 and Appendix I process).
- **TBS (To Be Supplied)**: Allowed in IRDs when data are not yet known at baseline; not used in ICDs except for clearly future capability. TBS items must be closed by timely revision.
- **Facility exception**: Facility interfaces require IRDs but do not require ICDs.
- **Orphan ICD**: An ICD without a parent IRD must carry both requirements (shall) and design characteristics (is/are); discouraged practice.
- **Verb discipline**: IRDs use "shall" for requirements; ICDs use "is/are" for design characteristics.

## Mental Models
- Think **contract boundary document pair**: IRD is the bilateral requirements contract; ICD is the implemented form/fit/function receipt.
- **Requirements first, design second**: Start the IRD early (before SOW finalization); approve IRD before ICD when both are needed.
- **Missing content is explicit**: Prefer "This IRD/ICD imposes no explicit [topic] requirements/characteristics" or TBS over silent omissions.

## Anti-patterns
- Writing an ICD before the IRD is approved when both are required.
- Leaving TBS items open indefinitely after design is known.
- Mixing shall-requirements into ICD prose without a parent IRD update.
- Treating facility interfaces as needing a full ICD when the standard says they do not.

## Key Takeaways
1. FAA-STD-025f is the preparation standard for IRD and ICD interface documentation in FESS/NAS contexts.
2. IRD = requirements (shall); ICD = implemented design (is/are) traced to the IRD.
3. Approved documents are CM baselines; incomplete data uses controlled TBS language.
4. Interface type (facility/analog/discrete/service/web) drives required outline sections.
5. Facility IRDs are special-cased (no ICD).

## Connects To
- **ch02**: Shared front matter, format, and common content sections.
- **ch03–ch04**: IRD- and ICD-specific detailed content.
- **ch05**: Verification/VRTM hooks shared across both document types.
- **ch06**: Revisions, CM, and development/approval roles.
