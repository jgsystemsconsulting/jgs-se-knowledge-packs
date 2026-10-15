# Chapter 4 - Software Conformity Inspection

Sources: FAA Order 8110.49A, Software Approval Guidelines (effective 2018-03-29), Chapter 4 paragraphs 1-5 (printed pages 4-1 to 4-4).

## Core Idea

Software conformity inspection is how the FAA confirms that the software article and its installation match approved type design before tests run for certification credit and before aircraft-level ground or flight tests. Order 8110.49A Chapter 4 applies on TC, STC, ATC, ASTC, and TSO authorization projects. It rests on 14 CFR 21.33(b), FAA Order 8110.4B, and the type-design data set in DO-178B Section 9.4. Day-to-day compliance is largely assessed through ASE or authorized DER reviews across the life cycle (Chapter 2). Conformity inspection adds two documented checkpoints: software part conformity and software installation conformity.

## Frameworks Introduced

- **Type design minimum for software.** At minimum: Software Requirements Data, Design Description, Source Code, Executable Object Code, Software Configuration Index (SCI), and Software Accomplishment Summary (SAS), per DO-178B Section 9.4.

- **Two conformity means.** (1) Software part conformity inspection for each test conducted for certification credit. (2) Software installation conformity inspection whenever an FAA aircraft-level ground or certification flight test is performed (for example under a TIA).

- **ASE then ASI split.** The Aviation Safety Engineer (ASE) establishes baseline and test-configuration facts, then initiates FAA Form 8120-10, Request for Conformity, so Manufacturing Inspection District/Satellite Office (MIDO/MISO) staff (the ASI) can witness or verify the build, load, and setup steps.

- **Certification-credit test definition.** A system certification test run under an FAA-approved test plan to show regulatory compliance. That approved test plan is not the DO-178B Software Verification Plan. Examples include DO-160D environmental qualification, system functional and integration tests, aircraft ground functional tests, and TIA flight tests.

- **Other means of compliance still inherit the concept.** The chapter is written around DO-178B as the typical means (recognized by AC 20-115B in the order wording), but if another means is used the conformity concepts still apply.

## Key Concepts

### Software part conformity - ASE tasks (paragraph 4-3.a)

1. **Baseline approval path.** Establish that the software baseline complies with type design and released software plans by FAA desk and/or on-site reviews (Chapter 2), or establish that a delegated software DER has approved the baseline on FAA Form 8110-3, Statement of Compliance with the Federal Aviation Regulations. The DER statement on Form 8110-3 should say the purpose is to approve the software baseline for conducting FAA testing for certification credit.

2. **Test configuration match.** Establish that the software test configuration to be installed in the Line Replaceable Unit (LRU) complies with the software test baseline.

3. **Artifact control.** Establish that all software artifacts for the test baseline are properly identified, under configuration control, and reflect the current state of the software under test.

4. **Tool qualification status.** Establish that development or verification tools that require qualification have been qualified; if qualification is incomplete at conformity time, document the tools and supporting data configuration.

5. **Form 8120-10 to MIDO/MISO.** Initiate the request and instruct the ASI to verify: correct build and load files taken from the SCM library; approved build and load instructions followed; data integrity checks and software part/version numbers verified in the LRU; test setup conforms to the setup in the approved engineering test plan.

6. **Retention and archive.** Establish that retention, archive, and retrieval of software life cycle data comply with the approved Software Configuration Management (SCM) plan.

### Software part conformity - ASI and sequencing

- The ASI performs the tasks listed on the Form 8120-10 (the items under ASE task 5 above).

- Part conformity must succeed before installation conformity is requested.

### Special-purpose test software

When special-purpose software is used for environmental qualification testing, the manufacturer must verify, validate, and configuration-control that test software. It is included in the test-setup conformity done before qualification testing.

### Software installation conformity - objectives and ASE role

Required for FAA aircraft-level ground or certification flight tests (for example TIA). Main objectives: an approved, controlled software version is loaded successfully under approved system installation and/or software loading procedures; the correct version for that system was loaded and initializes successfully.

ASE ensures:

1. Prior software part conformity completed successfully.

2. Load procedures are approved.

3. Form 8120-10 or FAA Form 8110-1 (TIA) is initiated and carries the software part and/or version number under request. That identity must be identifiable, under configuration control, reproducible, and documented in the SCI or similar configuration record. The request lists ASI verification actions, including: correct software version loaded and correct system hardware (part and serial numbers) installed on the aircraft; loading procedures ensure correct software part/version into correct hardware, with error indication on mismatch or failed load; manufacturer loading procedures followed; successful initialization; mismatches identified and documented.

### Installation conformity - ASI methods

The ASI performs the inspection from Form 8120-10 or TIA Form 8110-1 by either:

1. **Physical witness.** Watch successful loading of the correct software part/version into the actual system (actual part and serial number) installed or to be installed on the aircraft. Success may be shown by witnessing an integrity check (for example CRC comparison) and successful initialization, all per ASE-approved load procedures.

2. **Manufacturing inspection records.** Obtain records of the actual load: aircraft identification, hardware part/serial numbers, software part/version, when and how loaded, and that load and initialization succeeded. Records must let the ASI (or delegated designee) trace hardware identity to the unit on the aircraft and show which software part was loaded.

### Summary purposes (paragraph 4-5)

Part and installation conformity together ensure: the unit under test reflects the hardware/software configuration approved for that certification-credit test; the configuration is well documented if hardware or software changes after the test; aircraft-installed systems and loaded software for aircraft-level testing conform to FAA-approved type design; the final software and hardware product baseline presented for certification conforms to type design.

## Mental Models

- Life-cycle ASE/DER reviews build confidence continuously; conformity freezes a configuration at two hard gates (test article and aircraft install) so credit-bearing tests are not run on an uncontrolled build.

- Form 8120-10 is the handoff from engineering judgment (ASE) to manufacturing inspection execution (ASI). The ASE writes what must be verified; the ASI verifies it.

- Part conformity before installation conformity is a sequence rule, not a preference. Installation assumes a known-good part baseline.

- Form 8110-3 baseline approval by a DER is an alternate path to ASE review for the baseline question, not a substitute for the ASI conformity steps on Form 8120-10.

- FAA-approved test plan in this chapter means the plan approved for the official ground or flight test, not the DO-178B Software Verification Plan.

## Anti-patterns

- **Running certification-credit tests without part conformity.** Paragraph 4-3 requires part conformity for each such test; skipping it leaves test results without a documented configuration basis.

- **Requesting installation conformity before part conformity.** The order requires successful part conformity first.

- **Vague Form 8120-10 instructions.** If the ASE omits build/load/integrity/setup checks, the ASI has nothing concrete to witness or record.

- **Uncontrolled special-purpose environmental test software.** Qualification credit on a setup that includes unversioned test software fails the note under 4-3.a(1).

- **Assuming tool qualification can be silent at conformity.** If qualification is incomplete, configuration of tools and supporting data must still be documented.

- **Treating manufacturing records as optional without traceability.** Record-based ASI method only works when hardware identity traces to the aircraft unit and the loaded software part is explicit.

## Key Takeaways

1. Conformity shows the product matches approved type design under 14 CFR 21.33(b); for software, type design starts from the DO-178B Section 9.4 data set.

2. Two inspections matter: software part conformity (each certification-credit test) and software installation conformity (aircraft-level ground/flight tests).

3. ASE establishes baseline, test configuration, artifact control, tool status, SCM retention, and opens Form 8120-10; ASI executes the listed witness/verify steps.

4. DER Form 8110-3 may approve the software baseline for FAA testing when delegated; it should state that purpose explicitly.

5. Installation conformity confirms correct, controlled software is loaded into the correct hardware and initializes, by witness or by traceable manufacturing records.

6. Part conformity precedes installation conformity; both support a documented final baseline at certification.

## Connects To

- **ch01** - map of Order 8110.49A conformity duties versus AC-level development assurance guidance.

- **ch02** - desk and on-site reviews the ASE uses to establish the software baseline before opening Form 8120-10.

- **ch03** - LOI that influences how heavily ASE and designees are engaged across the same life cycle.

- **ch05** - AC 20-115D rules on life cycle data submittal and type-design data by software level (including Level D exclusions for Design Description and Source Code under DO-178C Section 9.4 as stated in the AC).

