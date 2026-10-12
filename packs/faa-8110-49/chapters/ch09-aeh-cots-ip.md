# Chapter 9 - AEH COTS Intellectual Property

Sources: AC 20-152A, Development Assurance for Airborne Electronic Hardware (2022-10-07), section 5.11 (printed pages 12-19; custom-device base path in ch07; sections 5.6-5.10 in ch08; glossary Soft/Firm/Hard IP definitions used as terms only).

## Core Idea

Section 5.11 covers commercial-off-the-shelf intellectual property instantiated inside FPGAs, PLDs, or ASICs during custom device development. Most COTS IP was not built to aviation assurance standards, so availability alone does not make it airworthy. The AC adds objectives IP-1 through IP-7 for selection, provider/data assessment, complementary assurance and verification strategy, planning, requirements capture for used and unused functions, and Appendix B handling when code coverage cannot see into the IP at DAL A/B.

## Frameworks Introduced

- **COTS IP definition and forms.** IP means design functions (modules, blocks, IP libraries) used to implement part or all of a custom device. It is COTS IP when it is a commercially available function used by many different users across varied applications. Custom IP built for a few specific aircraft equipments is not COTS IP. Source forms: Soft IP (RTL HDL, readable or encrypted; user synthesizes, places, routes), Firm IP (technology-dependent netlist; user places and routes), Hard IP (physical layout / GDSII-class data; user instantiates at physical design, or the FPGA/PLD vendor embeds it in silicon). A function can mix forms; each part is addressed.

- **Risk-driven assurance.** Approach follows IP category (soft/firm/hard) and identified failure risk from design error in the IP or in how the custom device uses it. Entry point is allocated requirements for the function the IP will perform inside the custom device process that already follows ED-80/DO-254 and the CD objectives.

- **Five work aspects.** Selection; assessment of provider and IP data; planning (including verification strategy); requirements/derived requirements; design integration, implementation, and verification inside the custom device.

- **IP-2 gaps drive IP-3 mitigation.** When provider data cannot fully meet IP-2 items 1, 2, 4, or 5, define complementary development assurance activities based on ED-80/DO-254 objectives. IP-2 item 3 (provider verification trustworthiness for the applicant use case) feeds the verification strategy rather than IP-3.

- **Three-aspect verification strategy (IP-4).** Cover (1) the COTS IP itself, (2) the IP after applicant design steps such as synthesis/place-and-route, and (3) integration of the IP inside the custom device. One verification step may serve more than one aspect.

## Key Concepts

### Applicability (section 5.11.2)

- Applies to COTS IP (per glossary) used in a custom device: digital, analog, and mixed-signal. Analog COTS IP is in scope because it can sit inside a custom mixed-signal device.

- Applies when the IP contributes to hardware DAL A, B, or C functions.

- Applies to Soft, Firm, and Hard IP inserted by the applicant. Does **not** apply to Hard IP embedded in FPGA/PLD silicon by the device manufacturer; that silicon-embedded IP is part of the COTS device and is handled under section 6 (ch10).

### Why the extra objectives exist

Availability does not equal suitability. Some COTS IP carries full ED-80/DO-254 life cycle data; most does not. Stated risk themes include incomplete behavioral or integration documentation, weak provider verification, deficient quality, unknown process rigor, misaligned intended usage, incomplete detailed operation data, incorrect integration, integrator inexperience with the IP function, and applicant-introduced physical-implementation errors from incomplete internal knowledge.

### Selection (IP-1)

Select COTS IP that is an acceptable solution based on at least:

1. Technical suitability for the intended function;
2. Architecture/design-concept description that supports understanding of functionality, modes, configuration, and source format (or format combination);
3. Data/documentation quality and availability sufficient to understand functions, modes, and behavior and to integrate and verify (datasheets, application notes, user guide, errata knowledge, and similar);
4. Information enabling physical implementation (synthesis constraints, usage and performance limits, physical implementation and routing instructions);
5. Demonstrability that the COTS IP fulfills its intended function.

### Provider and data assessment (IP-2)

Assess the COTS IP provider and associated data against at least:

1. Provider supplies information needed to integrate and implement the IP in the custom device (constraints, usage domain, performance limits, physical implementation and routing instructions);
2. Configurations, selectable options, and scalable modules are documented so implementation can be managed;
3. IP was verified by a trustworthy, reliable process, and that verification covers the applicant's specific use case (including used scale for scalable IP and selected functions for selectable functions);
4. Known errors and limitations are available to the IP user, with a process to provide updates;
5. Service experience data shows reliable operation for the applicant's specific use case.

Document the assessment; submit results for certification.

### Complementary assurance (IP-3)

When IP-2 items 1, 2, 4, or 5 cannot be completely met from provider data, define appropriate development assurance activities that mitigate the unmet criteria and the associated development-error risk, based on ED-80/DO-254 objectives. (Item 3 results are consumed by the verification strategy section, not by IP-3.)

### Verification strategy (IP-4)

Provider verification usually is not an ED-80/DO-254 verification process, though it may yield partial credit. Assurance level varies by vendor. Strategy may combine means beyond classical requirements-based testing. Describe in the hardware verification plan, PHAC, or related plan a strategy that covers all three aspects:

1. Verification of the COTS IP itself, addressing risk from IP-2 item 3;
2. Verification of the COTS IP after applicant design steps (for example synthesis/place-and-route);
3. Verification of integrated COTS IP functions within the custom device.

Notes from the AC:

- Reliable provider test data, cases, or procedures may be used as part of the strategy.
- If the IP implements an industry standard, proven standardized test vectors for that standard may be used.
- Strategy covers at least used functions and ensures unused functions are correctly disabled or deactivated and do not interfere with used functions.

### Planning the assurance approach (IP-5)

Describe in the PHAC or related plan a hardware development assurance approach for using the COTS IP that at least includes:

1. Identification of selected COTS IP (version) and source format(s) with the design-flow point(s) where it integrates into the custom device;
2. Summary of COTS IP functions;
3. Development assurance process defined to satisfy section 5.11.3 objectives;
4. Process for design integration and usage of the COTS IP inside custom device development;
5. Tool assessment and qualification aspects when tools perform design and/or verification steps for the COTS IP.

### Requirements and validation (IP-6)

Capture requirements related to allocated COTS IP functions to an extent commensurate with the verification strategy. Also capture derived requirements covering:

1. Used functions (parameters, configuration, selectable aspects);
2. Deactivation or disabling of unused functions;
3. Correct control and use of the COTS IP per provider data.

If the verification strategy relies solely on requirements-based testing, "commensurate" means complete requirement capture of the COTS IP following ED-80/DO-254. Validate COTS IP requirements as part of the overall custom device validation process.

Granularity of custom device requirements that touch IP-supported functions varies with IP function and with how visible those functions are at device level. When requirements-based testing is a large part of the IP verification strategy, refine detail to address IP functions and implementation. Capture requirements for all design details used to connect, configure, constrain, and integrate the IP.

### Verification execution and Appendix B (IP-7)

Verify the COTS IP as part of overall custom device verification per ED-80/DO-254, following the PHAC (or related) verification strategy. For the requirements-based verification portion, satisfy ED-80/DO-254 section 6.2 for requirements related to the COTS IP; that work can sit inside the overall custom device process (no separate objective).

**IP-7 (DAL A or B).** Satisfy ED-80/DO-254 Appendix B. Code coverage recognized under section 5.7 elemental analysis might not be possible on the COTS IP portion. Appendix B allows other methods, including safety-specific analysis. If using safety-specific analysis on the COTS IP function and its integration:

- Identify safety-sensitive portions of the IP and potential design errors that could affect DAL A/B functions in the custom device or system;
- For unmitigated aspects of those safety-sensitive portions, determine additional requirements, design features, and verification activities needed for safe operation;
- Feed those outputs back into the appropriate process.

## Mental Models

- COTS IP is a third-party design fragment you finish. You own integration, physical implementation closure, used/unused function control, and the certification argument even when the vendor shipped attractive datasheets.

- Soft/Firm/Hard is about where you enter the design flow, not about how safe the IP is. Hard IP glued in by the FPGA vendor is a section 6 COTS-device problem, not a section 5.11 IP problem.

- IP-1 asks "can we even use this product?" IP-2 asks "can we trust this vendor's data for our use case?" IP-3 patches data holes; IP-4 patches verification holes; IP-5 makes the plan readable; IP-6 sizes requirements to the chosen verification strategy; IP-7 handles DAL A/B elemental/Appendix B reality when coverage cannot see inside the IP.

- Unused functions are active risk until proven disabled and non-interfering. Selection and verification both say so.

- Provider tests are inputs to your strategy, not a substitute for it, unless and until you accept them under IP-4 notes with eyes open.

## Anti-patterns

- **Dropping commercial IP into an FPGA because it is popular.** IP-1 and IP-2 are explicit gates; popularity is not a criterion.

- **Treating manufacturer-embedded FPGA Hard IP under section 5.11.** Section 5.11.2 sends that case to section 6.

- **Stopping at IP-2 gaps without IP-3 mitigation activities.** Unmet items 1, 2, 4, or 5 require defined complementary assurance.

- **Verification strategy that only re-runs vendor unit tests.** IP-4 still needs post-applicant-implementation and integration aspects.

- **Ignoring unused functions.** IP-4 note 3 and IP-6 item 2 require deactivation/disable and non-interference.

- **Solely requirements-based strategy with thin IP requirements.** IP-6 forces full DO-254-style capture of the IP in that case.

- **DAL A/B custom device with uncovered COTS IP and no Appendix B story.** IP-7 requires Appendix B; safety-specific analysis is an explicit alternative path when code coverage cannot finish the job.

- **Leaving tool use on IP design/verification out of the PHAC.** IP-5 item 5 calls it out.

## Key Takeaways

1. Section 5.11 applies to applicant-instantiated Soft/Firm/Hard COTS IP in custom devices at hardware DAL A/B/C; manufacturer-embedded FPGA/PLD Hard IP is section 6 instead.

2. IP-1 selection and IP-2 provider/data assessment (submitted) are the entry gates; most COTS IP lacks aviation life cycle data, so risk is assumed until argued down.

3. IP-3 mitigates unmet IP-2 data criteria (items 1, 2, 4, 5) with DO-254-based complementary activities; IP-4 requires a three-aspect verification strategy (IP, post-applicant implementation, integration).

4. IP-5 plans identification, functions, assurance process, integration/usage process, and tools; IP-6 sizes function and integration requirements (including unused-function disable) to the verification strategy and validates them with the custom device.

5. IP-7 requires ED-80/DO-254 Appendix B at DAL A/B, with safety-specific analysis available when elemental code coverage cannot cover the IP portion; feed extra requirements, design features, and verification back into the process.

## Connects To

- **ch07** - custom device process and CD objectives that COTS IP plugs into.

- **ch08** - HDL code coverage recognition, tool assessment (CD-10/CD-11), and elemental-analysis limits that IP-7 and IP-5 item 5 lean on.

- **ch10** - COTS devices (including vendor-embedded Hard IP) and CBA flow-down of functions that embed this IP.

- **ch01** - hardware recognition chain and where paywalled DO-254/ED-80 content lives (avionics-signpost).

- **ch05** - software recognition pattern; DO-330 appears again when tools touch IP design or verification.
