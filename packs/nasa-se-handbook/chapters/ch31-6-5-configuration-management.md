# Chapter 31: 6.5 Configuration Management

## Core Idea
Configuration Management (CM) ensures that all system items remain under controlled, traceable, documented oversight throughout the project lifecycle; losing CM control results in mission failure, safety hazards, and unmanageable project chaos.

## Frameworks Introduced
- **Configuration Management Process**: A discipline for identifying, documenting, controlling, and auditing all baseline configurations and changes to items placed under CM throughout the program lifecycle.
  - When to use: On all space flight programs and projects; particularly critical in aerospace, safety-critical, and complex systems where configuration drift, unincorporated changes, or fraudulent verification data can cause mission loss or loss of life.

## Key Concepts
- **Configuration Item (CI)**: A physical, functional, or documentary entity selected for control; the baseline definition and procedures ensure its adequacy for performance.
- **Baseline**: A formally reviewed and approved configuration of specified items; all current baselines are made available to all technical teams and stakeholders.
- **Change Request (CR)**: A formal document that proposes, justifies, and documents changes to items under configuration control; requires Change Control Board (CCB) approval.
- **Configuration Audit**: A verification process (functional and physical audits) that ensures the delivered system matches the approved baseline configuration.
- **Configuration Control Board (CCB)**: The governance body (composed of hardware managers, quality assurance, engineering, SMA, and program office) that evaluates and approves or rejects change requests.
- **Redline**: Markup of drawings or documents during design, fabrication, production, or testing to mark errors; requires hardware manager and quality assurance approval and must be controlled by procedure.
- **Configuration Management List (CM List)**: The set of items designated as subject to configuration control; their baselines are maintained and reported.
- **CM Reports**: Periodic status reports on CM items and changes, disseminated to all stakeholders at agreed frequencies and key lifecycle reviews.
- **Loss of Configuration Control**: State in which inconsistencies between hardware and documentation lead to confusion, unmanageable data, mission failure, or unintended safety hazards.
- **Unincorporated Documentation Changes**: Engineering changes that were not formally recorded, approved, or implemented into the physical system (cited in Columbia accident investigation).

## Mental Models
- **Think of CM as the single source of truth.** Every change to a baseline item must be recorded, approved, and linked back to a CR in a way that traceability never breaks. If you cannot trace a physical part, tool, procedure, or drawing to a released part number and current specification, you have lost CM control.
- **Use the red-flag checklist as a diagnostic.** When a program shows warning signs (failure to define top-level requirements, CCB time compression, vendors making unauthorized changes, manufacturing tooling losing sync with design changes, verification data untraced to current specs, operational manuals untraceable to released drawings), you are already in control-loss territory or approaching it.
- **Redlines are a temporary measure, not a design method.** When procedures contain heavily redlined steps that operators must "jump around," and those procedures have never been executed in that exact form before, errors occur. Redlines must be limited in scope, controlled by procedure, approved, and incorporated into the baseline at the next opportunity.

## Anti-patterns
- **Failure to define a top-level technical requirement.** Programs that say "we don't need a specification" or declare that requirements-definition is unnecessary lose the foundation of all subsequent baseline control.
- **Reducing change-evaluation time to impossible levels.** When a program office mandates CCB review periods that engineering, SMA, and other board members cannot realistically meet, bad approvals or hidden changes result.
- **Declaring "no dissent in the record" in CCB documentation.** This suppresses alternative perspectives and creates an audit trail that masks disagreement, reducing decision quality and traceability.
- **Redlines used as the production-floor design control mechanism.** Extensive, uncontrolled redlines on production drawings and assembly procedures—especially those never before executed in that exact sequence—create confusion, missed steps, and mishaps.
- **Subcontractors and vendors making unauthorized engineering changes.** If vendors change design or submit waivers to safety requirements without integrating-contractor approval and formal engineering review, configuration authority is lost.
- **Manufacturing tooling losing sync with released design changes.** Tooling must be updated and re-controlled when design changes occur; out-of-date tooling creates production errors and fit/assembly failures.
- **Verification data untraceable to released part numbers and specifications.** Verification evidence must be correlated to the exact specification and part number under which the test was performed; orphaned verification data cannot prove adequacy.
- **Operational manuals and repair procedures untraceable to released drawings.** If maintenance teams cannot correlate repair instructions to the current released part number and configuration of the system being repaired, they will apply procedures intended for an older configuration, introducing defects.
- **Parts lacking proper identification markings.** When manufactured items do not have traceable markings (serial numbers, part numbers, lot numbers), they cannot be correlated back to their verification or configuration records.
- **Digital closeout photography untraceable to released engineering.** As-built photography must be correlated to the released engineering baseline it represents; undated or uncorrelated photos provide no proof of configuration compliance.
- **NASA unable to verify latest released engineering through contractor CM Web site access.** Configuration transparency and stakeholder access to current baselines is critical for lifecycle support and auditing.

## Key Takeaways
1. **CM control failure is a cascading hazard.** Unincorporated documentation changes, uncontrolled redlines, and subcontractor design changes accumulate into mission failure, loss of property and life, or significant cost overruns. Examples: Columbia accident (unincorporated documentation inconsistencies), NOAA N-Prime mishap (extensive unreviewed redlines in assembly procedures), X-37 fast-prototyping program (schedule prioritized over CM recording).

2. **Baselines and change control are non-negotiable.** Every system baseline must be formally approved, documented, and placed under CM. All changes require a Change Request, CCB evaluation, and documented approval; redlines and informal changes are temporary expedients only, and must be incorporated into the formal baseline promptly.

3. **Traceability is the enforcement mechanism.** Hardware must be traceable to a released part number and specification. Verification must be traceable to the specification and part number under test. Operational manuals must be traceable to the released configuration they support. Manufacturing tooling must be kept in sync with design changes. If any element breaks traceability, you cannot prove configuration compliance.

4. **Redlines must be procedurally controlled and limited.** All redlines require approval by hardware manager and quality assurance at minimum. Procedures must specify redline approval authority and incorporation timelines. Redlines must never become a substitute for formal design control on production floors, and procedures heavily redlined and never before executed in that exact sequence pose a safety hazard.

5. **The CCB is the governance checkpoint.** Configuration control authority resides in the Change Control Board, which must include hardware management, quality assurance, engineering, program office, and safety/mission-assurance representatives. The CCB must have sufficient time to evaluate changes; compressed review periods, suppressed dissent, or unauthorized authority undermine control.

6. **Configuration audits verify intent versus actuality.** Functional and physical configuration audits identify discrepancies between the documented baseline and the delivered system. Discrepancies must be resolved through formal change requests or corrective actions. If audits are not conducted, or findings are not closed, configuration drift accumulates silently.

7. **CM data and access must be shared and current.** Current baselines, CM status reports, change request dispositions, and audit results must be available to all technical teams and stakeholders at agreed-upon frequencies and at key lifecycle reviews. Opacity in CM data indicates control loss.

## Connects To
- **ISO/IEC/IEEE 15288 (Systems and software engineering – System and software engineering processes)**: CM is one of 17 common technical processes in the ISO framework; NASA applies CM principles aligned to systems lifecycle standards.
- **NPR 7120.5 (NASA Systems Engineering)**: Mandates that space flight programs define data management planning as part of configuration management oversight.
- **NPR 7123.1 (Program and Project Management)**: Requires CM planning and implementation; delegating specifics to Centers and program offices while mandating baseline control and change tracking.
- **NPR 1441.1 (NASA Records Retention Schedules)**: Governs retention of configuration and technical data records beyond system retirement.
- **Material Review Board (MRB)**: The quality and engineering body that evaluates non-conformances and waivers; must understand the distinction between critical, major, and minor defects and appropriate waiver classification.
- **Technical Data Management (Section 6.6)**: Works side-by-side with CM; changes to items under configuration control require a CR, while changes to data under Technical Data Management do not require a CR but must be tracked and access-controlled.
