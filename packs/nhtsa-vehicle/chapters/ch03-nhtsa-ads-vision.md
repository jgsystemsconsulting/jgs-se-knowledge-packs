# Chapter 3: Automated Driving Systems 2.0: A Vision for Safety

> Source: NHTSA Automated Driving Systems 2.0: A Vision for Safety (2017); extract pages 1–36 (no pages dropped by third-party screen).

## Currency caveat

ADS 2.0 is NHTSA's current ADS guidance as of the 2026-09-25 vetting check, per the `docs/SOURCE-VETTING.md` post-v1.21.0 row (evidence: FR action of 2026-07-31); a successor exists in draft; do not call it the final federal ADS policy.

## Core Idea

ADS 2.0 is DOT/NHTSA **voluntary guidance**. It updates the September 2016 Federal Automated Vehicles Policy and states NHTSA's operating guidance posture for Automated Driving Systems at the time of publication. It is a vision-and-practice document for entities that design, test, and deploy ADSs on US public roads, and a technical-assistance document for States. It is not a binding design standard, not a substitute for FMVSS compliance where FMVSS apply, and not a restatement of SAE driving-automation level definitions.

NHTSA's safety goal framing is crash-free roadways through lifesaving technology. ADS technologies, including designs with no human driver, are described as having large potential to cut fatalities and injuries dominated today by human behavior. The guidance deliberately stays nonregulatory so federal policy does not freeze innovation while the technology is still moving quickly.

This chapter is the **US vision document**. Taxonomy anchors such as SAE J3016 are acknowledged by ADS 2.0 for consistent language; level definitions are not restated here. For J3016 orientation use `automotive-signpost` only.

## Document Structure

ADS 2.0 has two major parts:

1. **Section 1: Voluntary Guidance** for ADS designers and related entities, built around twelve priority safety design elements and a Voluntary Safety Self-Assessment path.
2. **Section 2: Technical Assistance to States**, covering federal/state role split, practices for legislatures, and practices for state highway safety officials.

Entities in scope include traditional vehicle manufacturers and other parties that manufacture, design, supply, test, sell, operate, or deploy ADSs. The voluntary guidance focuses on design aspects of motor vehicles and systems that incorporate higher automation (the document anchors its focus using SAE automation taxonomy without this pack reprinting those level tables). Commercial motor vehicle operations remain under their own federal regime; ADS 2.0 points readers there rather than absorbing FMCSA rules.

## Federal Enforcement Context (as the document frames it)

States asked how NHTSA's enforcement authority applies to ADSs. ADS 2.0 answers in plain terms: NHTSA retains broad enforcement authority to address unreasonable safety risks in motor vehicles and motor vehicle equipment, including new technologies. Voluntary guidance does not shrink that authority. Federal and State roles stay divided along familiar lines (vehicle and equipment safety performance at the federal level; licensing, registration, traffic law enforcement, and insurance at the State level), and NHTSA asks States not to blur that split by turning this voluntary guidance into State statutory mandates for development, testing, or deployment phases.

## Twelve Priority Safety Design Elements

Entities are encouraged to consider each element in design and to keep a self-documented process for assessment, testing, and validation. No single measuring stick is declared; entities may innovate on methods. Privacy and ethical deliberation are acknowledged as important companion topics outside the twelve-element list proper.

### 1. System Safety

Follow a robust design and validation process on a systems-engineering footing, aimed at designing ADSs free of unreasonable safety risks. Monitor evolving industry methods. Link design decisions to assessed risks. Test, validate, and verify design decisions. Document the process end to end, including hazards considered and the standard or method applied.

### 2. Operational Design Domain (ODD)

Define and document the ODD for each ADS feature on the vehicle: the conditions where the feature is intended to operate safely (road types, geography, speed range, weather, time of day, and other constraints the entity sets). The ADS should operate safely inside that ODD and should transition safely when conditions leave the ODD or the ODD boundary moves dynamically.

### 3. Object and Event Detection and Response (OEDR)

OEDR is detection of circumstances relevant to the immediate driving task and the appropriate response. Entities need a documented process for how the ADS perceives and responds inside its ODD, covering normal driving behaviors and crash-avoidance / hazard scenarios the ODD implies. Behavioral competencies expected of a given ADS depend on that ODD; the document points at research taxonomies for minimum competencies without freezing one mandatory list for every system.

### 4. Fallback (Minimal Risk Condition)

Document how the ADS transitions to a minimal risk condition when it cannot continue the trip normally (system fault, ODD exit, or other problem). Fallback design should assume human drivers may not always respond as hoped, and should administer fallback in a way that itself manages safety risk. At higher automation, where a human may be unavailable, the fallback path cannot depend on that human.

### 5. Validation Methods

Because automation functions differ widely in scope and capability, entities should develop validation methods that fit the risks of their design. Demonstrate expected performance for deployment and for the testing that leads there. Prefer substantial work before on-road testing. Testing may be in-house or independent. Keep working with NHTSA and standards bodies as methods mature.

### 6. Human Machine Interface (HMI)

Driver-vehicle interaction grows harder as automation takes on more of the dynamic driving task. Document HMI considerations for drivers, operators, occupants, and other road users (including motorcyclists, bicyclists, and pedestrians). Convey ADS state clearly. Vehicles intended to operate without conventional driver controls need deliberate HMI design for that mode. The field is research-heavy; entities are pointed at ongoing work across multiple standards bodies by name only.

### 7. Vehicle Cybersecurity

Use a robust product development process grounded in systems engineering to reduce safety risk from cybersecurity threats and vulnerabilities. Design ADSs with established best practices from named communities (including NIST, NHTSA, SAE International, trade associations, and Auto-ISAC). Document how cybersecurity was incorporated. Share cybersecurity information so the industry learns faster than attackers. Detailed federal cyber practice material for modern vehicles sits in this pack's Chapter 2; ADS 2.0 states the expectation at vision level rather than repeating that catalog.

### 8. Crashworthiness

**Occupant protection.** Mixed fleets of ADS-equipped and conventional vehicles will share roads; crashworthiness still matters. Use applicable research and existing occupant-protection thinking when ADS geometries or seating concepts change.

**Compatibility.** Unoccupied or unconventional ADS vehicles should still present geometric and energy-management compatibility that limits harm to other road users and vehicles in crashes.

### 9. Post-Crash ADS Behavior

After a crash during testing or deployment, return the ADS to a safe state. Consider how propulsion, fuel/energy, electrical systems, and automated controls behave immediately after impact. If the vehicle talks to an operations center, that channel may matter for safe-state actions. Document the post-crash process.

### 10. Data Recording

Crash and near-crash data are central to learning. Record data that supports reconstruction and that shows ADS status and whether the ADS was controlling the vehicle. Coordinate toward more uniform data approaches with industry and standards organizations. Use data policies that support continual learning without pretending one recorder format already settles every question.

### 11. Consumer Education and Training

Education is treated as a safety control for deployment. Build and maintain programs for employees, dealers, distributors, and consumers. Cover HMI, fallback scenarios, ODD limits, and on-road ADS behavior. Be explicit about the driver's or operator's responsibilities when any remain. Dealers and distributors need training paths that match the systems they hand to customers.

### 12. Federal, State, and Local Laws

Document how the ADS is intended to comply with applicable law. Testing may use a trained test driver or other mechanism to manage compliance. Edge cases (for example maneuvers that would normally violate a traffic rule only to avoid a worse harm) should be thought through in the documented approach rather than improvised in the field.

## Voluntary Safety Self-Assessment

Entities testing or deploying ADSs may publish a Voluntary Safety Self-Assessment showing how they address the twelve elements through industry practice, their own practice, standards, or other methods. Aims stated in the document include aiding NHTSA's understanding, encouraging industry safety norms, and building public trust. Submission is not required as a legal precondition in the guidance itself. Assessments should avoid dumping purely confidential detail in public form; entities can indicate, element by element, how the topic was addressed, including an explanation when an element is not applicable. NHTSA may provide illustrative templates; content can vary by system.

## Technical Assistance to States (Section 2)

### Role clarity

NHTSA encourages States to read each other's draft ADS policies and aim for consistency rather than a patchwork that blocks interstate operation. Federal responsibilities emphasized in the document include setting and enforcing FMVSS, overseeing recalls and safety defects, and issuing national guidance. State responsibilities emphasized include licensing human drivers (where humans remain), vehicle registration and titling, traffic law enforcement, safety inspections where used, and insurance/liability frameworks.

NHTSA strongly discourages States from codifying ADS 2.0 itself into State statutes as a legal requirement for development, testing, or deployment.

### Practices for legislatures

When legislatures act, the document urges them to avoid unnecessary barriers to competition and innovation, to keep the federal/state lane lines clear, to monitor safe operation without inventing conflicting vehicle performance regimes, and to review vehicle codes and traffic laws for definitions and rules that silently assume a human driver at every wheel.

### Practices for state highway safety officials

A practical framework offered to States follows the document's own seven headings:

1. **Administrative.** Lead agency and related oversight choices; coordination with stakeholders the State finds useful. NHTSA does not require States to invent new entities.
2. **Application for entities to test ADSs on public roadways.** What a State may ask an entity to file (identity, vehicle identifiers, test operators, safety/compliance plan, financial-responsibility evidence, test-operator training summary) for recordkeeping and assurance.
3. **Permission for entities to test ADSs on public roadways.** How a State that grants test permission may involve law enforcement, request application changes, and notify approval; preference that permission stay at State level with local coordination.
4. **Specific considerations for ADS test drivers and operations.** Test-driver training summaries, traffic-rule and crash-reporting expectations, and the licensed-driver role for lower automation versus fully automated operation under stated conditions.
5. **Considerations for registration and titling.** Identifying ADS capability on title/registration records and handling significant ADS upgrades.
6. **Working with public safety officials.** How police, fire, and EMS learn to interact with ADS behaviors and safe states.
7. **Liability and insurance.** State choices about financial responsibility as automation changes who was "driving."

The tone is assistance, not a single mandatory State program template.

## Key Takeaways

1. ADS 2.0 is **voluntary guidance** and a **vision** document; per the SOURCE-VETTING post-v1.21.0 row it remains NHTSA's current ADS guidance as of the 2026-09-25 check (FR evidence 2026-07-31), with a successor in draft; **not** final federal ADS policy.
2. Twelve priority safety design elements (system safety, ODD, OEDR, fallback, validation, HMI, cybersecurity, crashworthiness, post-crash behavior, data recording, education, and law compliance) structure industry self-documentation.
3. The **Voluntary Safety Self-Assessment** is encouraged for trust and transparency; the guidance does not cast it as a legal admission ticket.
4. States are asked to keep **federal/state roles** clear and **not** to codify this voluntary guidance into State law as a development or deployment mandate.
5. This chapter does **not** restate SAE J3016 level definitions; continue at `automotive-signpost` for that taxonomy.

## Connects To

- **ch01 (introduction):** pack refusals, including "not final ADS policy" and "not SAE J3016."
- **ch02 (cyber practices):** detailed NHTSA vehicle cybersecurity guidance that ADS element 7 points toward at vision level.
- **ch04–ch06 (FMVSS):** federal vehicle performance standards that still apply to vehicles regardless of automation narratives in ADS 2.0.
- **`automotive-signpost`:** SAE J3016 and related ADS taxonomy/regulatory pointers this chapter deliberately does not reproduce.
