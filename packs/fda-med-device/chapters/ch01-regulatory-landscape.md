# Chapter 1: Regulatory Landscape and Pathways

Sources: S1 Content of Premarket Submissions for Device Software Functions (2023-06-14), §§ I–V (device software functions, premarket submission types, documentation level); S4 Medical Devices; Quality System Regulation Amendments, 89 FR 7496 (published 2024-02-02, effective 2026-02-02), purpose and QMSR framing; S9 Deciding When to Submit a 510(k) for a Software Change to an Existing Device (2017-10-25), § I (devices subject to 510(k)); S10 Medical Device Data Systems, Medical Image Storage Devices, and Medical Image Communications Devices (2022-09-28), §§ III–IV.A (Non-Device-MDDS framing); S11 Electronic Submission Template for Medical Device 510(k) Submissions (2023-10-02), § VI.B (510(k) eSTAR mandatory date); S12 Electronic Submission Template for Medical Device De Novo Requests (2024-08-23), § VI.B (De Novo eSTAR mandatory date).

## Core Idea

FDA regulates software the same way it regulates other device functions: first ask whether the software meets the device definition, then pick the premarket path that fits the product, then put the right software evidence in the submission and keep a quality system that can defend design and change decisions. For software people, the landscape is a stack of questions, not a single form. Is this a device software function under section 201(h), or a software function excluded under section 520(o)? If it is a device function, which premarket submission type carries it (510(k), De Novo, PMA, or another listed type)? What documentation depth does the risk of the function demand? After clearance or approval, which software changes reopen premarket review, and which stay inside the quality system? The pack answers those questions from the pinned FDA sources; this chapter is the map.

## Frameworks Introduced

- **Device software function**: a software function that meets the device definition in FD&C Act section 201(h). A "function" is a distinct purpose of the product, which may be the whole intended use or a subset of it. One product can carry several functions (for example storage, transfer, and analysis).
- **Premarket submission set for device software**: for the S1 guidance, "premarket submission" includes 510(k), De Novo classification request, PMA, IDE, HDE, and BLA when a device software function is in scope. The path is chosen by the product's regulatory status; the software documentation recommendations travel with whichever path applies.
- **Documentation Level (Basic or Enhanced)**: risk-based depth for software content in the premarket file. Enhanced applies when a failure or flaw of any device software function could present a hazardous situation with a probable risk of death or serious injury (assessed before risk controls). Basic is everything else. The level is set for the device as a whole, not module by module.
- **QMSR framing**: the 2024 final rule retitled 21 CFR part 820 as the Quality Management System Regulation, incorporates ISO 13485:2016 by reference, and takes effect 2026-02-02. Premarket software work still sits on design-control and validation obligations that the quality system must produce and keep.
- **Non-Device-MDDS framing (one line)**: software solely intended to transfer, store, convert formats, or display medical device data and results, without analyzing or interpreting that data or controlling connected devices, is not a device under section 201(h). Boundary detail lives in ch08.
- **510(k) change trigger (pointer)**: software and firmware changes to an existing 510(k)-subject device run a documented decision sequence under S9; ch10 owns the flowchart.
- **eSTAR authoring (pointer)**: 510(k) electronic submissions via eSTAR became mandatory 2023-10-01; De Novo electronic submissions via eSTAR become mandatory 2025-10-01. ch12 owns template structure.

## Key Concepts

- **Device definition and the software carve-out.** Section 201(h) defines "device" to include instruments, machines, implants, in vitro reagents, and similar articles intended for diagnosis, cure, mitigation, treatment, or prevention of disease, or to affect the structure or function of the body. The same definition excludes software functions removed under section 520(o). Software people start here: regulated documentation follows only after the function is a device function.
- **Where software functions fit.** Device software functions include firmware and other software-based control of medical devices, software accessories, and software-only functions that meet the device definition (including functions intended to run on commercial off-the-shelf computing platforms). Manufacturing and quality-system software, and software that is not a device, sit outside the S1 premarket documentation guidance.
- **Multiple functions on one product.** A product can mix device functions and non-device software functions. FDA reviews the device software functions; non-device functions still matter when they can affect the safety or effectiveness of the device functions (see also MDDS and CDS boundary chapters).
- **510(k) path.** Premarket notification under section 510(k) is the path for devices that rely on substantial equivalence to a legally marketed predicate. S9 applies the "when to submit a new 510(k)" analysis to 510(k)-cleared devices, preamendments devices subject to 510(k), and devices granted marketing authorization via De Novo when later changes are evaluated under 510(k) rules.
- **De Novo path.** De Novo classification under section 513(f)(2) is the path when there is no predicate and the sponsor seeks Class I or Class II classification with general controls, or general and special controls, rather than remaining in automatic Class III. After a De Novo grant, later software changes are evaluated against the original authorized device under the S9 framework when 510(k) requirements apply.
- **PMA path.** Premarket Approval under section 515 is the path for Class III devices that require a reasonable assurance of safety and effectiveness through the PMA process. S1 treats PMA as a premarket submission type that still carries device software documentation when the device includes software functions. S1 also notes that Class III devices generally call for Enhanced Documentation unless the sponsor justifies Basic.
- **Other submission types named in S1.** IDE, HDE, and BLA appear in the same premarket-submission list when a device software function is under review, including device constituent parts of combination products assigned across centers.
- **Classification basics for software authors.** Classification is not a documentation level, but the two travel together. Enhanced Documentation is the default recommendation when software failure could cause death or serious injury before mitigations; blood establishment computer software and several blood-related device categories are called out for Enhanced; combination-product device constituents and Class III devices generally get Enhanced unless a reasoned Basic case is made. Special controls for a classified device type can demand extra software content beyond the baseline S1 tables.
- **Quality system always on.** Whether or not a given change needs a new 510(k), manufacturers of finished devices must review and approve design and production changes, document them, and validate process software where 21 CFR 820 requires it. S1 reminds sponsors that design validation includes software validation and risk analysis where appropriate. The QMSR rule does not erase that expectation; it reframes part 820 around ISO 13485 with FDA additions, effective 2026-02-02.
- **Predetermined change control plans (PCCP).** Section 515C lets FDA clear or approve a plan describing planned device changes that would otherwise need a new 510(k) or PMA supplement. Changes consistent with an authorized PCCP do not need a separate supplemental submission. Software teams that want planned algorithm or performance evolution should treat PCCP as a premarket design choice, usually socialized through a Q-Submission first.
- **MDDS in one line.** Non-Device-MDDS software (solely transfer, store, convert formats, or display of medical device data and results, without analysis, interpretation, or device control) is outside the device definition; see ch08 for hardware Device-MDDS policy, active patient monitoring, and multi-function products.
- **Guidances are recommendations; rules bind.** S1 states the usual FDA guidance posture: guidances are current thinking and recommendations unless they cite specific statutory or regulatory requirements. Follow the binding regulation text when a requirement is cited, and treat the rest as the Agency's recommended way to show safety and effectiveness.

## Mental Models

- **Function first, form second.** Name every distinct purpose of the product. Sort each purpose into device function, non-device software function, or out of scope. Only then pick 510(k), De Novo, PMA, or another submission type.
- **Risk sets paperwork depth.** Documentation Level answers "how bad is failure," not "how much process theatre can we afford." Enhanced is triggered by probable death or serious injury before controls, including cybersecurity compromise of functionality.
- **Premarket file vs quality system file.** The submission is a slice of evidence for FDA review. The design history and change records are the standing obligation. A no-new-510(k) decision still leaves a QS paper trail.
- **Original device is the baseline for later changes.** After a 510(k) clearance or De Novo grant, software change analysis compares the modified device to that original authorized configuration (or the most recently cleared 510(k) for the device), not to an arbitrary predicate story.
- **Orientation chapter, not the deep dive.** Use this chapter to route: documentation depth to ch02; validation to ch03-ch04; QMSR detail to ch05; cyber to ch06-ch07 and ch09; MDDS/OTS to ch08; change triggers to ch10; CDS to ch11; eSTAR mechanics to ch12.

## Anti-patterns

- **Treating "it's software" as automatically a device.** Section 520(o) exclusions and Non-Device-MDDS functions exist. Skipping the device-definition step wastes a submission or misses a regulated function.
- **Equating Documentation Level with device class.** Class III often lines up with Enhanced, but the driver is hazardous situations and probable serious harm, assessed for the device as a whole.
- **Writing the premarket software story after the code ships.** S1 flags retrospective design-history construction as a control problem. Synchronize DHF evidence with development.
- **Assuming QS work substitutes for a required new 510(k).** S9 and the QS regulation work together: many changes stay inside QS, but a change that could significantly affect safety or effectiveness still needs a new 510(k).
- **Ignoring non-device functions that touch device functions.** Multi-function products can carry Non-Device-MDDS or other excluded software beside regulated functions; impact on the device functions still gets assessed.

## Key Takeaways

1. Start with section 201(h) and section 520(o): only device software functions enter the premarket software documentation regime in S1.
2. A function is a distinct purpose; products can host several functions with different regulatory fates.
3. Premarket paths named for device software include 510(k), De Novo, PMA, IDE, HDE, and BLA; pick the path from the product's classification and marketing history, then attach software evidence to that path.
4. Documentation Level is Basic or Enhanced, driven by pre-control risk of death or serious injury from software failure, for the device as a whole.
5. Non-Device-MDDS software (transfer/store/convert/display only) is not a device; details and edge cases are in ch08.
6. The QMSR (part 820 as amended, effective 2026-02-02) is the quality-system frame that must still generate design control, validation, and change records.
7. Software changes to existing 510(k)-subject devices use the S9 decision sequence (ch10); eSTAR shapes how 510(k) and De Novo files are authored (ch12).
8. Guidance recommendations are not freestanding law; cited statutes and regulations are.

## Connects To

- **ch02**: Basic vs Enhanced documentation elements once the path and Documentation Level are known.
- **ch03-ch04**: lifecycle validation principles and CSA for production/QMS software (S1 points to GPSV; CSA owns automated production and quality-system software).
- **ch05**: QMSR obligations after the 2026-02-02 transition (S4/S4a/S5 detail).
- **ch08**: MDDS and OTS boundary detail (this chapter only frames Non-Device-MDDS).
- **ch10**: when a software change needs a new 510(k).
- **ch11**: clinical decision support and the section 520(o)(1)(E) criteria.
- **ch12**: eSTAR structure and mandatory electronic submission dates for 510(k) and De Novo.
