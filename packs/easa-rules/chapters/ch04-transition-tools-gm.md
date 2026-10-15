# Chapter 4: Tool Qualification Pointer and GM Clarifications

Sources: S1 AMC 20-115D (ED Decision 2017/020/R; AMC-20 Amendment 14, consolidated in Amendment 23), section 10 TOOL QUALIFICATION, lines 581-700 of `sources/text/S1.txt` (printed pp. 424-426), plus GM1 to GM3, lines 838-953 of `sources/text/S1.txt` (printed pp. 428-430). Exclusions: EAR footers; sections 11-12 related-material and availability name lists (not body). Name-only standards cited here by designation: ED-12C/DO-178C, ED-12B/DO-178B, ED-12A/DO-178A, ED-12/DO-178, ED-215/DO-330, ED-216/DO-333, ED-94C/DO-248C. No objective-table reproduction (see ED-12C/DO-178C, not reproduced).

## Core Idea

Paragraph 10 of AMC 20-115D points tool qualification at ED-12C/DO-178C section 12.2 and at ED-215/DO-330, which carries its own complete set of objectives, activities, and life cycle data for tools. The paragraph then specialises that pointer for legacy software paths: when new or modified tools appear on pre-C baselines, how ED-12B/DO-178B-qualified tools map onto C-era tool qualification levels (TQLs), and what may be declared equivalent. GM1 through GM3 add complementary practices the AMC layers on top of the recognised standards: what a software change impact analysis (CIA) should contain, how data coupling and control coupling both feed a verification objective, and why foreseeable error sources should be handled at design level rather than only in source-code review.

## Frameworks Introduced

- **Primary tool-qualification pointer.** Sections 12.2 of ED-12C/DO-178C and ED-215/DO-330 are an acceptable method. ED-215/DO-330 is the dedicated tool document (name-only here).
- **Legacy tool paths by original approval edition.** Separate rules for tools on ED-12/DO-178 or ED-12A/DO-178A baselines, for ED-12B/DO-178B baselines without a C-era equivalence claim, and for ED-12B/DO-178B baselines that will claim C-era software equivalence while still carrying B-era tools.
- **TQL correlation table (AMC Table 2).** Maps B-era development-tool and verification-tool qualification types, by software level, onto C-era tool criteria and TQL-1 through TQL-5. Original summary below; certification decisions use the official table.
- **GM1 CIA content model.** Baseline identification, change summary, problem-report and change-request lists, new-function activation list, then impact and activity lists across eight change item classes.
- **GM2 coupling split.** Data coupling analysis and control coupling analysis are different types with different purposes; both are required for the cited verification objective. Design-phase interface and dependency specification makes the later analyses possible.
- **GM3 design-level error handling.** Identify foreseeable error sources, identify mitigations, specify protection and error-handling in requirements, prefer runtime protection for Levels A and B; formal methods (ED-216/DO-333) may improve runtime-error detection.

## Key Concepts

- **Need-to-qualify test on very old baselines (10.a).** For legacy software approved under ED-12/DO-178 or ED-12A/DO-178A, new or modified tools are checked against ED-12C/DO-178C section 12.2 criteria. If qualification is needed, TQL follows the software level from the system safety assessment, and ED-215/DO-330 supplies objectives, activities, and data. The qualified tool may be declared as satisfying ED-215/DO-330; the legacy software itself is not thereby declared equivalent to ED-12C/DO-178C.
- **B-era baseline without C-era claim (10.b).** Either keep using ED-12B/DO-178B tool qualification processes for new or modified tools that support B-era legacy software, or update tool processes and qualify under ED-215/DO-330 using AMC Table 2 for TQL, then declare the tool as satisfying ED-215/DO-330.
- **B-era tools while claiming C-era software equivalence (10.c).** C-era defines five TQLs from tool use and impact (see the standard's tool section and its table; not reproduced). B-era had development-tool and verification-tool types instead. AMC Table 2 correlates them. Original summary (`see ED-12C/DO-178C, not reproduced` for underlying criteria text):

| B-era type | Software level | C-era tool criteria | TQL |
|------------|----------------|---------------------|-----|
| Development | A | 1 | TQL-1 |
| Development | B | 1 | TQL-2 |
| Development | C | 1 | TQL-3 |
| Development | D | 1 | TQL-4 |
| Verification | A, B | 2 | TQL-4 |
| Verification | C, D | 2 | TQL-5 |
| Verification | All | 3 | TQL-5 |

- **Development tools previously B-qualified (10.c.2).** If the B-era software level assigned to the tool meets or exceeds the required TQL, keep B-era tool processes; changes to the tool or its operational environment take a tool CIA under ED-215/DO-330's change sections and are still performed with B-era tool processes. If the B-era level does not meet the required TQL, update processes and requalify under ED-215/DO-330. Equivalence of the tool to ED-215/DO-330 is allowed only when all tool and process changes satisfy that document.
- **Verification tools previously B-qualified (10.c.3).** TQL-5 required: may keep B-era verification-tool processes; on tool or environment change, run a tool CIA and either reverify with B-era processes or requalify under ED-215/DO-330. TQL-4 required: requalify under ED-215/DO-330. Same equivalence rule as for development tools when claiming ED-215/DO-330 satisfaction.
- **GM1 CIA outputs.** Identify the released baseline the change builds on. Provide a summary of changes and their impact; list problem reports to correct and related change requests; list new functions to activate or implement.
- **GM1 change item classes.** Where applicable, address changes to: software level; development or verification environment; software processes; tools (new version or modified use); processor or other hardware components and interfaces; configuration data (especially function activation/deactivation); software interface characteristics and I/O requirements; software requirements, design, architecture, and code (including items affected by the change, not only the modified life cycle data). For each applicable class, describe impact and name the activities that keep the project satisfying ED-12C/DO-178C or ED-12B/DO-178B and safe operation.
- **GM2 coupling.** Data coupling analysis and control coupling analysis both support the cited verification objective; neither replaces the other. Although the objective is verification-side, the analyses depend on design-phase practice: specified interfaces (I/O) and specified dependencies between components.
- **GM3 error sources (examples the GM lists).** Runtime exceptions and errors (fixed/floating-point overflow, stack/heap overflow, division by zero, counter/timer overrun or wrap-around); data/memory corruption or timing issues (partitioning gaps, improper interrupt or cache management); unpredictable execution features (dynamic allocation, out-of-order execution, resource contention).
- **GM3 mitigation chain.** For each foreseeable source, identify the mitigation; specify protection mechanisms in high-level or low-level requirements, including error-handling mechanisms; for Levels A and B, prefer incorporating runtime protection rather than relying on probabilistic approaches or static analysis alone (good practice at other levels too). Formal methods per ED-216/DO-333 may enhance runtime-error detection.

## Mental Models

- Tool qualification is a separate claim from software baseline equivalence. Paragraph 10 keeps saying you can declare a tool under ED-215/DO-330 without pulling legacy software into a C-era software declaration, and the reverse also holds: software equivalence does not bless unmodified tools.
- Table 2 is a bridge, not a waiver. B-era development tools at lower software levels land on higher (stricter) TQL numbers when read through C-era criteria; verification tools often land on TQL-4 or TQL-5 and may still need requalification when TQL-4 is required.
- CIA is a structured impact story, not a one-line "code changed" note. GM1's eight item classes force environment, tools, hardware interfaces, configuration data, and dependent life cycle data into scope beside the edited units.
- Coupling evidence is earned in design. If interfaces and dependencies were never specified, verification-time coupling analysis has nothing solid to stand on.
- Error handling belongs in requirements and design, not only in a late source-code review checklist. GM3 pushes runtime protection especially at Levels A and B.

## Anti-patterns

- **Declaring legacy software C-era-equivalent because a new tool was qualified under ED-215/DO-330.** Section 10.a separates those claims.
- **Keeping a B-era development tool on a C-era claim when Table 2 says its old level misses the required TQL.** Requalify under ED-215/DO-330.
- **Assuming TQL-4 verification tools can stay on pure B-era process forever.** Section 10.c.3.b requires ED-215/DO-330 requalification when TQL-4 is required.
- **Writing a CIA that lists only edited source files.** GM1 expects level, environment, process, tool, hardware, configuration data, interface, and dependent life cycle impacts when they apply.
- **Treating data coupling analysis as enough for the coupling objective.** GM2 requires control coupling analysis as well, and vice versa.
- **Relying on static analysis alone for Level A/B overflow and partitioning hazards.** GM3 recommends runtime protection mechanisms at those levels.

## Key Takeaways

1. Tool qualification under this AMC points at ED-12C/DO-178C section 12.2 and ED-215/DO-330 (name-only); ED-215/DO-330 owns tool objectives, activities, and life cycle data.
2. Legacy tool rules split by original software approval edition and by whether the applicant will declare C-era software equivalence; AMC Table 2 maps B-era tool types to C-era TQLs.
3. Tool equivalence to ED-215/DO-330 requires that tool and process changes satisfy that document; it does not automatically make legacy software C-era-equivalent.
4. GM1 defines CIA content: baseline, change summary, problem/change-request lists, new functions, then per-item impact and activities across eight change classes.
5. GM2 requires both data coupling and control coupling analyses, grounded in design-time interface and dependency specification.
6. GM3 moves foreseeable error handling into design and requirements, with runtime protection recommended for Levels A and B, and notes formal methods as a detection aid.

## Connects To

- **ch03** - section 9 modify/reuse flow that sends new or changed tools here, and the CIA summary that lands in the PSAC or SAS.
- **ch02** - recognition of ED-215/DO-330 and the supplement set that paragraph 10 relies on.
- **ch07** - planning-interface passages that carry CIA results and tool qualification plans into the joint software/hardware workflow.
