# Chapter 4: Computer Software Assurance

Sources: S3 Computer Software Assurance for Production and Quality Management System Software (2026-02-03), §§ I–V and Appendix A (CSA definition; intended use; high vs not-high process risk; assurance activities including scripted and unscripted testing; record contents; examples). Supersedes S2 GPSV Section 6 only; supplements the rest of GPSV (ch03).

## Core Idea

Computer software assurance (CSA) is FDA's risk-based approach for establishing and maintaining confidence that software used as part of medical device **production** or the **quality management system** is fit for its intended use and stays in a validated state. CSA is the replacement operating model for the old computer-system-validation habit of maximal scripted testing and binder-heavy evidence on every admin screen. The method is: decide whether the software (or each feature, function, or operation) is in scope for production/QMS use; analyze reasonably foreseeable failures; classify **high process risk** versus **not high process risk**; select assurance activities and evidence rigor matched to medical-device risk or process risk; record intended use, risk result, activities, issues, and conclusion without drowning the file in screenshots. CSA supplements GPSV and **explicitly supersedes GPSV Section 6**. Device software functions that are themselves medical devices still follow GPSV principles and S1 premarket documentation; they are not re-homed into CSA.

## Frameworks Introduced

- **CSA definition**: risk-based approach to establish and maintain confidence that software is fit for intended use, with assurance effort driven by risk of compromised safety and/or quality if the software fails, keeping a validated state through the lifecycle.
- **Intended-use gate (V.A.1)**: validation applies when software is or will be used as part of production or the QMS, directly or in support roles (including specified cloud IaaS/PaaS/SaaS patterns for production/QMS). Examine features, functions, and operations when they carry different intended uses.
- **Process risk vs medical device risk**: process risk is potential to compromise production or the QMS. Medical device risk is potential to harm patient or user. CSA's first cut asks whether software failure causes a quality problem that **foreseeably compromises safety** (high process risk). That analysis is distinct from ISO 14971 device risk management, though device risk still scales assurance rigor when process risk is high.
- **High process risk vs not high process risk (binary presentation)**: FDA presents a binary for guidance readability; manufacturers may still grade intermediate or low process risk inside the "not high" band when choosing activities.
- **Assurance activity selection (V.A.4–V.A.5)**: scripted testing (detailed or limited), unscripted testing (scenario/ad-hoc, error guessing, exploratory and other experience-based techniques), hybrid approaches, continuous performance monitoring, data monitoring, and use of vendor/cloud/developer activities and other production/QMS controls.
- **Record of assurance (V.A.6)**: intended use; risk-based analysis result; description of testing/assurance performed; issues found and disposition; conclusion of acceptability; who/when; review/approval when appropriate. Prefer digital system evidence over paper duplication.
- **Least-burdensome posture**: burden of assurance no greater than needed for the risk; efficiency is a stated goal when quality is preserved.

## Key Concepts

- **Scope boundary with device software.** CSA targets computers and automated data-processing systems used as part of production or the quality management system. Cloud computing in that role is in scope. Cloud computing used as part of **device software functions** is out of CSA scope (those functions follow device-software guidances). Development tools that test or monitor production/QMS software, and automation of general record-keeping that is not itself the quality record, are "support" intended uses still inside the production/QMS umbrella.
- **Why CSA exists.** Manufacturers rely on automation for monitoring, operation, alerts, and data movement. A documentation-maximal CSV culture burns effort without proportional quality gain. CSA keeps the validated-state obligation while allowing unscripted methods, monitoring, and supplier evidence when risk allows.
- **Identifying intended use (V.A.1).** Direct production/QMS uses include automating production processes, inspection, testing, collection/processing of production data; and automating QMS processes, QMS data handling, or maintaining a quality record under QMS obligations. Support uses include tools that develop/run tests for production/QMS software and automation of general record-keeping outside the quality record. Document the decision that a feature is or is not in that scope.
- **Feature-level thinking.** A single COTS package can host mixed risk. Example pattern in S3: spreadsheet used only to record curing time/temperature may need little beyond vendor assessment plus installation/configuration; custom formulas that calculate process suitability statistics may need more manufacturer assurance. When every feature shares one intended use, a whole-application analysis can suffice.
- **Risk-based analysis (V.A.2).** Systematically identify reasonably foreseeable failures (not only "likely" ones). Ask whether failure poses high process risk. Select and time assurance activities commensurate with medical-device risk or process risk. Consider configuration, security, data integrity, storage, transfer, and operation error as failure factors.
- **High process risk examples.** Features that maintain essential process parameters (temperature, pressure, humidity) affecting safety-critical physical properties; measure/inspect/analyze/determine acceptability with limited or no human review; perform process corrections or parameter adjustments from monitoring/feedback without human review; produce IFU or other labeling necessary for safe operation; automate surveillance/trending/tracking of data the manufacturer treats as essential to safety (including cybersecurity) and quality.
- **Not high process risk examples.** Collect/record monitoring data without direct impact on process performance; CAPA routing, complaint logging/tracking, automated change-control or procedure management; data management, automating an existing calculation, extra monitoring, or exception alerts on established processes; other support roles under V.A.1. ERP restocking with qualified-person check before use can be intermediate (not high) process risk; the same automation that also auto-accepts material without human check can become high process risk.
- **Choosing rigor (V.A.4).** If high process risk (quality problem may foreseeably compromise safety), assurance level follows **medical device risk** of the resulting harm path. If not high process risk, assurance follows **process risk**. Higher risk means more objective evidence; lower risk means less. A feature that could cause severe patient harm is generally high medical-device risk work when process risk is high.
- **Scripted testing.** Test cases recorded and executed manually or by automation. Detail and evidence scale with risk: detailed scripted testing when repeatability, traceability, or auditability must be tight; limited scripted testing when risk is lower.
- **Unscripted testing.** Tester actions not prescribed by written cases. Includes scenario/ad-hoc testing, error guessing, exploratory testing, and related experience-based techniques. Legitimate assurance tools, not informal shortcuts, when applied under a risk-based strategy.
- **Risk-based testing principle.** Manage, select, prioritize, and use testing from analyzed risk. S3's tendency lines: high process risk often leans scripted or hybrid; not-high often leans unscripted or lighter mixes. Tendencies are not bans: unscripted can still fit some high-risk features; scripted automation can still be efficient on low-risk features.
- **Credit other controls (V.A.5).** Downstream inspection, data-integrity procedures, separate process verification, supplier or cloud-provider assurance, continuous monitoring, and similar mechanisms can reduce additional assurance effort when they truly bound the failure impact. That credit is reasoned, not assumed.
- **Changes (V.A.3).** Production or QMS software changes get assurance scaled to impact. CSA remains the method after go-live, not only at first validation. (PMA supplement reporting categories for manufacturing changes are a separate regulatory channel illustrated in S3; do not confuse reporting category with assurance depth.)
- **Establishing the record (V.A.6).** Capture intended use; risk-analysis result; assurance activity description; issues (deviations, defects, failures) and resolutions or risk justification; acceptability conclusion; performer and date; review/approval when appropriate. Do not collect more evidence than needed to show performance as intended for the identified risk. Prefer digital retention (logs, audit trails, electronic capture, automated traceability) over paper screenshots that duplicate system memory. Record retention still follows QMS obligations (ISO 13485 record controls as applied under part 820).
- **Electronic records.** Part 11 and related electronic-record considerations appear in S3 Section V.B when records are electronic; assurance planning should include integrity, availability, and authenticity needs driven by intended use.
- **Relationship to GPSV.** S3 supplements GPSV and supersedes **only** Section 6 (automated process equipment and quality system software). Device software validation principles in GPSV §§1–5 remain the reference (ch03). S1 premarket device-software documentation remains the premarket device-software reference (ch02).
- **Appendix A pattern.** Worked examples (nonconformance management, LMS, business intelligence, SaaS PLM, and similar) show feature-level intended use, risk calls, activity choices, and lean records. Use them as pattern libraries, not as mandatory templates for your system names.

## Mental Models

- **Intended use first, scripts second.** If you cannot state the production or QMS job of the feature, you are not ready to pick tests.
- **Safety-compromise gate.** High process risk means failure can cause a quality problem that foreseeably hurts safety. That gate decides whether medical-device risk or process risk sets the dial.
- **Assurance case, not binder mass.** The record must show reasoning and enough objective evidence for the risk. Page count is not a quality metric.
- **Activities over artifacts.** Unscripted exploration, monitoring, and supplier evidence can be real assurance. A thick script with no risk link can be fake assurance.
- **Validated state is continuous.** CSA is lifecycle control, including after changes, not a one-time CSV project.

## Anti-patterns

- **Full IQ/OQ/PQ theatre on every QMS configuration screen.** CSA replaced that Section 6 habit for production/QMS software with risk-proportionate assurance.
- **Treating unscripted testing as "uncontrolled tinkering."** Under S3, scenario, error-guessing, and exploratory methods are named assurance options when risk supports them; still record what was done and what was found.
- **One risk score for an entire enterprise platform.** Feature, function, and operation intended uses often differ; so must assurance.
- **Claiming credit from a human check that does not actually exist.** ERP examples hinge on whether a qualified person really gates use.
- **Applying CSA to the device's clinical software functions to dodge S1/GPSV.** Wrong scope. Device software functions stay on device-software guidances.
- **Screenshot binders as the default evidence form.** S3 prefers digital system evidence when it is accurate and reliable for the intended use.
- **Equating "not high process risk" with "no assurance."** Lower rigor still means some fit-for-use confidence and a record.
- **Stopping at go-live.** Changes need impact-scaled assurance or the validated state rots.

## Key Takeaways

1. CSA is risk-based assurance that production/QMS software is fit for intended use and remains in a validated state; it supersedes GPSV Section 6 and supplements the rest of GPSV.
2. Start with intended use of the software or of each feature/function/operation; confirm production or QMS scope (direct or support), including relevant cloud models.
3. Classify high process risk when failure may cause a quality problem that foreseeably compromises safety; otherwise treat as not high process risk (with optional finer grades inside that band).
4. Match assurance rigor to medical-device risk when process risk is high, and to process risk when it is not; collect objective evidence in proportion.
5. Scripted testing, unscripted testing, hybrids, monitoring, and supplier/cloud evidence are all in the toolkit under risk-based selection.
6. The assurance record needs intended use, risk result, activities, issues/disposition, conclusion, identity/date, and approval when appropriate; prefer lean digital evidence.
7. CSA does not replace S1 premarket documentation or GPSV principles for device software functions; keep scopes separate.
8. Worked examples in S3 Appendix A are the practical pattern book for applying the framework.

## Connects To

- **ch03**: GPSV principles that still govern device software validation; Section 6 handoff point into this chapter.
- **ch02**: premarket device-software documentation (different scope from production/QMS CSA).
- **ch05**: QMSR/ISO 13485 validation clauses CSA helps satisfy for production and QMS software.
- **ch06**: cybersecurity process software and monitoring tools may themselves be production/QMS software under CSA when used that way.
- **ch01**: orientation map placing CSA beside device-software validation.
