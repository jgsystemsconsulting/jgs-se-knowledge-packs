# Chapter: Recommended DE data acquisition contract language

## Core Idea

Section 8 is the handbook's main method chapter for turning DE data needs into acquisition language. It covers needs assessment, data management language, data acquisition and interoperability language, and configuration and data management (CDM) Statement of Work patterns. The pack describes placement and practice. It does not copy clause text, RCL rows, or DRD field lists.

Language belongs in more than one place. Typical placement spans the SOW/PWS (what work and outcomes are required), the DRD or data procurement document (what each data item must contain and how it is encoded), the solicitation and proposal instructions, and the cost volume (data as a priced element, not a free side effect). Data rights handling rides the same stack so access survives performance and closeout.

## Frameworks Introduced

- **Needs assessment first.** Before clauses, assess digital data standardization, definition and interoperability, MBSE and system-model development, acquisition paths, exchange processes, integrity, rights and accessibility, proprietary handling, RFP language, related procurement circulars, and training.
- **Source-to-destination mapping.** Plan how each data item moves from producer systems to NASA destinations, including bill of materials and product breakdown structure views where they apply.
- **Interoperability use cases.** Exchange and distribution of models, CAD interoperability cases, industry-standard paths (including families such as MIL-STD-31000 and STEP/ISO 10303 where invoked), and integrity checks are treated as design work, not IT afterthoughts.
- **Data management plan.** A Digital Engineering Data Management Plan (or equivalent) records how rights, protection, authoritative sources, system-to-system interfaces, and domain artifacts will be handled.
- **CDM SOW patterns.** Configuration and data management planning, identification, baselines, control, status accounting, and related audits appear as SOW building blocks that reference DRDs as required.

## Key Concepts

- **Standardization and definition.** Agree early on structures, schemas, and neutral formats so deliveries do not strand in proprietary encodings.
- **MBSE and M&S credibility.** When models are deliverables, acquisition language must say what "done" means for structure, metadata, state, and credible use, without pasting external standard text.
- **Rights and accessibility.** Distinguish technical data and computer software categories, flow-down to subcontractors, marking for less-than-unlimited rights, and access paths into NASA systems.
- **Authoritative sources of truth.** Name which contractor or Agency sources own which classes of data; avoid silent dual masters.
- **Domain artifact bundles.** Requirements sets, CAD packages, modeling and simulation products, tabulated data suited to downstream automation, and Earth-science contract considerations appear as domain slices of the same method.
- **Acquisition and interoperability pair.** Buying the bit-stream is incomplete without buying the exchange rules that let NASA use it.
- **Close with CDM.** Configuration identification, baselines, change control, and status accounting keep the digital thread auditable after award.

## Mental Models

- **Three-home rule.** If a data need lives only in the SOW, only in a DRD, or only in the cost volume, it is under-specified.
- **Price the data.** Unpriced data work becomes scope pressure against the hardware or service line.
- **Map before exchange.** Source-to-destination mapping prevents "delivered" files that no NASA system can load.
- **Rights are lifecycle fuel.** Lessons in ch03 show that missing rights language becomes a balloon payment.

## Anti-patterns

- Pasting full RCL blocks without tailoring to the answered guiding questions.
- Accepting contractor format as default with no neutral-exchange requirement.
- Omitting cost-volume treatment so data work is unpaid.
- Writing interoperability hopes in the SOW with no DRD that pins format and timing.

## Key Takeaways

- Section 8 is method and placement, not a clause scrapbook.
- Cover needs assessment, data management, acquisition/interoperability, and CDM SOW patterns.
- Place language across SOW, DRD, solicitation, and cost volume.
- Handle data rights, flow-down, and authoritative sources explicitly.
- Copy no clause text into pack files; name FAR/DFARS families only when the handbook does.

## Connects To

- ch05 questions that justify each language block
- ch07 RCL selection matrix for picking statements
- ch08 DRD template library for data-item shape
- ch03 lessons that this method is meant to prevent
