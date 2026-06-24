# NASA NPR 7150.2D Glossary

Key terms from NPR 7150.2D, drawn mainly from Appendix A (Definitions). Where the
directive scopes a term to itself ("only for this document") or imports it from an
external standard, that is noted. Chapter references point to where the term is used
or defined in this pack.

**Accredit** — Official acceptance of a tool, model, or simulation, together with its data, as fit for a specific stated purpose. Distinct from *verify* and *validate*. (Ch 7)

**Acquirer** — The party that obtains or procures a software product or service from a supplier; in this directive, typically NASA exercising insight and electronic access over a developer. (Ch 3, Ch 7)

**Assure** — To make certain that other parties have actually carried out the specified software engineering, management, and assurance activities. An act of confirmation, not of doing the work itself. (Ch 7)

**Auto-Generated Code** — Source code produced by a tool from models, schemas, or other inputs rather than written by hand; held to the same engineering and V&V standard as hand-written code, with the generating tool itself validated. (Ch 3, Ch 4)

**Bidirectional Traceability** — The ability to follow a relationship in both directions — parent requirement to child and back, requirement to design, design to code, requirement to test, requirement to hazard. Imported from ISO/IEC/IEEE 24765. (Ch 3, Ch 7)

**Class (Software Class A–F)** — The category assigned to a system or subsystem containing software that decides which NPR requirements apply and at what rigor. A–E are engineering-related; F is Business/IT infrastructure. (Ch 1, Ch 3, Ch 8)

**Code Coverage** — The percentage of the software that a given test suite actually executes; a structural test-completeness measure. (Ch 3, Ch 4, Ch 7)

**COTS (Commercial Off-the-Shelf)** — Software available for purchase and usable as delivered, without further development, from the commercial market. (Ch 3, Ch 7)

**Cyclomatic Complexity** — A count of the linearly independent paths through a unit of code; a ceiling of 15 applies to safety-critical components, with exceedances reviewed and justified. (Ch 3, Ch 7)

**Defect** — Anything incomplete or incorrect when measured against requirements or expectations; the first link in the defect → fault → failure chain. From NASA-STD-8739.9. (Ch 5, Ch 7)

**Embedded Software** — Software that runs on a processor built into a larger device, including processors inside programmable logic devices; explicitly within the directive's scope. From ISO/IEC/IEEE 24765. (Ch 1, Ch 7)

**Ensure** — To secure or guarantee an outcome — to make something sure or certain. Distinguished from *assure* and *accredit*. (Ch 7)

**Failure** — The actual incorrect or undesired behavior, of a defined severity, that occurs when a fault is encountered. Last link in the defect/fault/failure chain. (Ch 5, Ch 7)

**Fault** — The manifestation of an error that may lead to a failure; the middle link in the chain. From the NASA-STD-8719.24 annex. (Ch 5, Ch 7)

**Glueware** — Software written to connect off-the-shelf or reused components to the rest of a system: interface adapters, isolating "firewalls," and input/output checkers. (Ch 7)

**GOTS (Government Off-the-Shelf)** — Government-created software, usually from a prior project, normally supplied with source code and documentation. (Ch 3, Ch 7)

**Insight** — A monitoring relationship in which the acquirer observes a developer's processes and products without directing them day to day; contrasted with oversight. From NPR 7123.1. (Ch 3, Ch 7)

**IV&V (Independent Verification and Validation)** — V&V performed by an organization technically, managerially, and financially independent of the developer; its applicability and criteria come from NASA-STD-8739.8. (Ch 2, Ch 3, Ch 7)

**Major Engineering/Research Facility** — A facility qualifying as a significant investment (Current Replacement Value at or above $50M) with a Mission Dependency Index at or above 70, hosting software that supports NPR 7120.x-managed programs. A two-gate threshold definition. (Ch 7, Ch 8)

**MC/DC (Modified Condition/Decision Coverage)** — A coverage criterion requiring each condition within a decision to be shown to independently affect the outcome, by varying one condition while holding the others fixed; 100% is mandated for safety-critical components. (Ch 3, Ch 4, Ch 7)

**Mission Critical Software** — Software able to cause, help cause, or help prevent the loss of capabilities on which the primary mission objectives depend. From NPR 8715.3. (Ch 7, Ch 8)

**Model** — Scoped in this directive to the software-implemented form; a representation used for analysis, design, or V&V. Narrowed from the broader NASA-STD-7009 sense. (Ch 4, Ch 7)

**MOTS (Modified Off-the-Shelf)** — COTS or heritage software that has been changed; graduated thresholds decide whether a change leaves it "modified" or pushes it into new development (see *MOTS thresholds*). (Ch 3, Ch 7)

**MOTS thresholds** — A rule of thumb in Appendix A: under roughly 5% of code changed may not count as "modified"; up to about 30% changed can still be treated as modified; beyond 30% changed, or any new code added, the product is handled as a new development. (Ch 7)

**NODIS (NASA Online Directives Information System)** — NASA's controlled repository of directives; the NODIS Library holds the authoritative current version of the NPR, since printed copies are uncontrolled. (Ch 1, Ch 6)

**Non-Conformance** — A condition where a product, process, or activity does not meet a requirement; tracked with defined severity levels, including for tools and ground software. (Ch 5, Ch 7)

**Off-the-Shelf Software** — The umbrella term over software the project did not build for itself: COTS, GOTS, MOTS, OSS, freeware, shareware, trial/demo, and legacy/heritage/reuse software. (Ch 3, Ch 7)

**Open-Source Software (OSS)** — Software whose source is made broadly available at no cost under an OSS license granting use, modification, and redistribution rights, often developed openly. (Ch 3, Ch 7)

**Process Asset Library** — A managed store of process assets — procedures, templates, lessons — that an organization reuses; the Agency maintains one. From CMMI. (Ch 2, Ch 7)

**Project Manager** — The role to whom nearly every NPR 7150.2D "shall" requirement is directed; accountable for classifying, planning, costing, securing, and assuring the project's software. Roles drawn from NPR 7120.5. (Ch 3, Ch 4, Ch 5)

**Requirements Mapping Matrix (RMM)** — The Appendix C artifact mapping each NPR requirement against a project by class, recording commitments, "Not-Applicable" calls, and approved tailoring with authority signatures; the verification instrument for compliance. (Ch 1, Ch 2, Ch 3)

**Reuse / Heritage / Legacy Software** — Products written for one project that, without prior planning, turn out useful elsewhere; treated under the off-the-shelf governance rules. (Ch 3, Ch 7)

**Safety-Critical Software** — Software that, if done wrong or left uncorrected, could lead to severe injury, major damage, or mission failure; carries the behavioral safe-state requirements plus the 100% MC/DC and complexity-≤15 gates. From NPR 8715.3. (Ch 3, Ch 8)

**Simulation** — Scoped, like *model*, to the software-implemented form for this directive; the execution of a model over time. Narrowed from NASA-STD-7009. (Ch 4, Ch 7)

**Software** — Defined expansively to leave little out: NASA-developed, contracted, and maintained code; COTS/GOTS/MOTS/OSS; reused, auto-generated, embedded, legacy, and heritage code; applications, freeware, shareware, trial/demo, and open-source components. The breadth is the point. (Ch 1, Ch 7)

**Software Assurance** — The planned, systematic set of activities that give confidence the life-cycle processes and their products meet the applicable requirements, standards, and procedures; for NASA it bundles a named discipline set — Software Quality, Software Safety, Software Reliability, Mission Software Cybersecurity Assurance, Software V&V, and IV&V. (Ch 2, Ch 7)

**Software Configuration Management (SCM)** — Technical and administrative direction and surveillance applied across the life cycle to identify items, control changes, account for status, and verify conformance, preserving product integrity. See IEEE 828-2012. (Ch 5)

**Software Validation** — Confirmation that the delivered product satisfies its intended use in the target environment — "the right thing was built." From IEEE 1012. (Ch 4, Ch 7)

**Software Verification** — Confirmation that products correctly reflect their specified requirements — "the thing was built right." From IEEE 1012. (Ch 4, Ch 7)

**Static Analysis** — Examination of code without executing it, to detect defects, security issues, coverage, and complexity; required during development and test. From ISO/IEC/IEEE 24765. (Ch 4, Ch 7)

**SWE-### (Software Engineering requirement identifier)** — The unique tag attached to each mandatory "shall" statement in the directive (for example SWE-013, SWE-141, SWE-219), used for traceability, applicability mapping in the RMM, and tailoring. (Ch 3, Ch 4, Ch 5)

**Tailoring** — The governed process of seeking relief from a requirement in a way consistent with objectives, acceptable risk, and constraints; justified, risk-evaluated, formally accepted, concurred by impacted disciplines, and recorded in the RMM. (Ch 2)

**Technical Authority (TA)** — The governance structure (Engineering and SMA chains) that controls how requirements are applied and approves deviations; each requirement's responsible authority is named in Appendix C. (Ch 2, Ch 8)

**Unit Test** — Testing of an individual software unit in isolation to confirm it behaves as designed, producing repeatable results. One branch from ISO/IEC/IEEE 24765. (Ch 4, Ch 7)
