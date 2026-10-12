# Cheatsheet: fda-med-device

Decision rules for device software questions. Each checklist names the chapter that owns the detail.

## Is my software a device at all? → ch01, ch08, ch11

- Does the function meet the section 201(h) device definition, and does no section 520(o) exclusion apply? Regulated documentation starts only there. (ch01)
- Solely transfer, store, convert formats, or display medical device data, with no analysis, interpretation, or device control? Non-Device-MDDS: not a device. (ch08)
- Alarms, prioritization, or active patient monitoring aimed at immediate clinical intervention? Device function; the MDDS exit closes. (ch08)
- Analyzes a medical image, IVD signal, or pattern from an acquisition system? Fails CDS Criterion 1: device. (ch11)
- HCP-facing recommendations built on medical information, options not directives, with a real independent-review path and no time-critical decision? All four 520(o)(1)(E) criteria must hold for Non-Device CDS. (ch11)
- Multi-function product? Excluded functions stay excluded under 520(o)(2), but their impact on device functions is still assessed. (ch01, ch08)

## Which premarket path and format? → ch01, ch12

- Path follows product status: 510(k) with a predicate, De Novo without one, PMA for Class III; IDE, HDE, and BLA carry software documentation when a device software function is in scope. (ch01)
- eSTAR is the format: mandatory for 510(k) since 2023-10-01 and De Novo since 2025-10-01; clear "eSTAR Complete" and technical screening before review. (ch12)
- Software evidence goes in the Software/Firmware section; cybersecurity evidence in Cybersecurity/Interoperability. (ch12)
- Planning algorithm or performance evolution? Consider a PCCP as a premarket design choice, usually socialized through a Q-Submission. (ch01, ch02)

## What Documentation Level? → ch02

- Could a failure or flaw of any device software function present a hazardous situation with probable risk of death or serious injury, assessed before risk controls and including cybersecurity compromise? Yes means Enhanced; no means Basic.
- One level for the device as a whole; module-by-module ratings and schedule pressure are not inputs.
- Class III devices, combination-product constituents, and named blood-device categories default to Enhanced; arguing down to Basic needs a documented rationale.
- Both levels: level statement, software description, risk management file, SRS, architecture diagram, version history, unresolved anomalies. Enhanced adds SDS, fuller configuration-management and maintenance evidence, and unit/integration test protocols and reports.

## What validation or assurance approach? → ch03, ch04

- Software that is or supports a device function? GPSV lifecycle validation: requirements baseline, risk-scaled coverage, independent review, regression after change. (ch03)
- Production or QMS software (including cloud used in that role)? CSA: state intended use, classify high vs not-high process risk, pick proportionate activities. (ch04)
- High process risk: rigor follows medical device risk. Not high: process risk sets the dial. (ch04)
- Unscripted testing (scenario, error guessing, exploratory) is a legitimate assurance tool where risk allows; record what was done and found. (ch04)
- Any software change reopens impact analysis and regression before the software counts as validated again. (ch03)

## What cybersecurity artifacts? → ch07, ch09 (process: ch06)

- Content spine: threat model, cybersecurity risk assessment, machine-readable SBOM with per-component support level and end-of-support, vulnerability and supportability analysis, unresolved security anomalies, traceability. (ch07)
- Architecture views: global system, multi-patient harm, updateability/patchability, security use cases for safety-relevant functions. (ch07, ch09)
- Security testing beyond ordinary V&V: security requirements, threat mitigation, and vulnerability testing (abuse cases, fuzzing, attack surface, composition analysis). (ch07)
- Labeling with actionable security information, plus a cybersecurity management plan for postmarket vulnerability handling. (ch07, ch09)
- Cyber device? The section 524B plan, reasonable-assurance processes, and SBOM are statutory floors on top of the recommendations. (ch06, ch07, ch09)
- Scale breadth with connectivity and harm potential; keep every element type in play, and treat the IDE package as a thinner cut of the same set. (ch09)

## Does my change need a new 510(k)? → ch10

- Presumption of assessment, not presumption of filing: run the S9 sequence. "Document" (no new 510(k)) is a recorded outcome, not an ignore.
- Intent to significantly affect safety or effectiveness? New 510(k) likely, regardless of later questions.
- Q1: change solely to strengthen cybersecurity with no other impact? Often no. Q2: solely restoring the cleared specification? Often no.
- Q3a: new or modified risk of significant harm not effectively mitigated on the cleared device, or Q3b: new or modified risk control for such harm? Likely yes. Q4: significant effect on clinical functionality or performance specifications? Likely yes.
- Verification and validation confirm a no-file decision; clean tests never override a "could significantly affect" finding.
- Baseline is the last cleared configuration, and simultaneous plus cumulative changes are judged against it.
- Every change gets quality-system change control and records whether or not a filing results. (ch05, ch10)

## QMSR obligations? → ch05

- On and after 2026-02-02, part 820 is the QMSR: document a QMS that meets applicable ISO 13485:2016 requirements plus the FDA overlays.
- An ISO certificate or MDSAP participation is not a shield against FDA inspection; the FD&C Act and specific regulations win conflicts.
- Devices automated with computer software (Class II, Class III, and listed Class I) meet Design and Development Clause 7.3, including software validation.
- Named clause bridges must also be satisfied: UDI (part 830), device tracking (part 821), MDR reporting (part 803), advisory notices (part 806).
- Section 820.35 complaint and servicing record fields and section 820.45 labeling and packaging controls still bind on top of the incorporated clauses.
- Software changes stay inside QMS change control even when no new 510(k) is filed. (ch10)

## Quick anchors

| Need | Answer | Chapter |
|------|--------|---------|
| Documentation Level test | Pre-control probable death or serious injury, device as a whole | ch02 |
| Enhanced adds | SDS, CM/maintenance documents, unit/integration reports | ch02 |
| Device software validation | GPSV principles (S2, minus superseded Section 6) | ch03 |
| Production/QMS software method | CSA | ch04 |
| Quality system rule | QMSR (part 820), effective 2026-02-02 | ch05 |
| SBOM floor for cyber devices | 524B(b)(3): machine-readable, plus support data | ch07 |
| Change baseline | Last cleared configuration | ch10 |
| Cyber-only patch | Often documents out; analysis and V&V still run | ch10 |
| eSTAR mandatory dates | 510(k) 2023-10-01; De Novo 2025-10-01 | ch12 |

## Tells & smells

| Smell | Likely gap | Chapter |
|-------|------------|---------|
| Version number used as the regulatory classification | The S9 flowchart was never run | ch10 |
| Module-by-module documentation depth | Device-as-a-whole rule missed | ch02 |
| Static SBOM spreadsheet without support data | SBOM content floor unmet | ch07 |
| "We hold an ISO certificate" as QMSR compliance | Certificate is not compliance | ch05 |
| Regression report as the whole change record | Risk reasoning missing | ch10 |
| Screenshot binders for every admin screen | Assurance not risk-proportionate | ch04 |
| One network diagram as every architecture view | Missing views | ch07, ch09 |
| Time-critical tool claiming Non-Device CDS | Criterion 4 fails | ch11 |

## What this pack is not

- Not legal advice: guidances carry recommendations; cited statutes and regulations bind. (ch01)
- Not a substitute for the guidance documents or the ISO standards named in them. (ch02, ch05)
- Not EU MDR, UKCA, or drug, biologic, and combination-product rules.
