# Chapter 21: 5.1 Product Implementation

## Core Idea
Product implementation transforms design specifications into tangible products through make/buy/reuse strategies, with rigorous control over fabrication, procurement, and quality to ensure the delivered product is ready for verification.

## Frameworks Introduced
- **Make/Buy/Reuse Strategy**: A decision-making framework for acquiring products (in-house fabrication, commercial purchase, or reuse of existing items).
  - When to use: Established early in the program lifecycle; informs acquisition planning, scheduling, cost, and verification approach.

- **Material Review Board (MRB)**: A formal review mechanism for nonconforming products during production.
  - When to use: Large projects where component defects or specification deviations require disposition (accept, rework, scrap/remake).

- **Heritage Review**: A structured assessment of an existing product's suitability for reuse in a new application.
  - When to use: Whenever reuse of an existing product (prior program heritage or COTS) is considered; especially critical for space environments and catastrophic/critical applications.

## Key Concepts
- **As-Built Documentation**: Design drawings, design models, code listings, and procedural records created during implementation; essential for handoff to verification and operations teams.

- **Off-The-Shelf (OTS) Product**: Hardware or software with existing operational heritage, usually from commercial, military, or prior NASA programs; requires careful assessment for environmental and performance compatibility.

- **Heritage** (of a product): The original manufacturer's proven quality and reliability, measured by time in service, unit quantity, mean time between failure (MTBF), and use cycles; unaffected modifications or environmental changes degrade heritage.

- **Nonconformance**: A product deviation from specification; dispositioning determines whether it is acceptable, reworked, or scrapped.

- **Requalification**: Required verification and validation testing when a reused product is placed in a new or more extreme environment than its original qualification.

- **Nondisclosure Agreements**: Special arrangements sometimes required to obtain reuse products or supplier documentation.

- **Configuration Documentation**: Specifications, Interface Control Documents (ICDs), drawings, integration plans, and procedures needed to guide implementation.

- **Vendor/Supplier Involvement**: The degree of technical oversight and control exerted over manufacturing or software coding contracts, dependent on system criticality.

- **Design Factors of Safety and Margins**: Performance and construction standards that must be reassessed for reuse; incompatibility may render a component unsuitable without formal waiver.

## Mental Models
- **Think of make/buy/reuse as a strategy choice with long-term consequences**: The decision affects cost, schedule, verification scope, and ongoing supportability; revisit periodically as production schedules evolve.

- **Use heritage as a risk proxy**: High-heritage products (original design, extensive service history, unchanged environment) carry lower requalification risk; low-heritage products (redesigned, new environment, limited history) require extra scrutiny and possible full reverification.

- **Treat reused products as "new designs" if modified**: Even minor modifications by NASA shift the product to a new baseline and trigger the full design review and verification pipeline.

## Anti-patterns
- **Assuming prior verification and validation transfers blindly**: Reused products must have prior V&V documentation that demonstrates equivalence in requirements, environments, and expectations; cost savings come from elimination of requalification (if conditions are identical) or elimination of low-level specification tasks, not from skipping acceptance-level testing.

- **Applying OTS products in environments for which they were never qualified**: Many OTS products developed for benign Earth environments (standard temperature, atmospheric pressure, normal gravity) fail catastrophically in space (vacuum, radiation, extreme temperature, atomic oxygen, zero gravity, launch vibrations). Space-qualified heritage is not transferable from terrestrial applications.

- **Inadequate vendor documentation and supplier engagement**: Insufficient drawings, code listings, design procedures, or operational manuals create blind spots in the verification and validation process; NASA modification of a product without original manufacturer input risks undetected interactions.

- **Weak nonconformance review discipline**: Allowing defects or deviations to proceed without formal MRB review and documented disposition invites late-stage failures and untraced quality issues.

## Key Takeaways
1. **Implementation strategy choice (make/buy/reuse) must be made explicitly and documented early**, with clear rationale for cost, schedule, and risk trade-offs; revisit during production as constraints change.

2. **Off-the-shelf products require rigorous requirements-driven evaluation and heritage review**, especially for space environments where terrestrial COTS products often fail; document environmental applicability and identify any modifications needed for compliance.

3. **Reuse decisions must be grounded in proof that the prior product meets equivalent requirements and was verified/validated in equivalent environments**; simply reusing prior test data without verifying environmental and requirement equivalence is a common failure mode.

4. **All implementation activities (fabrication, coding, purchasing) must produce complete as-built documentation**—design drawings, closeout photos, manuals, baseline records, certificates of compliance—handed off to verification and operations in a form ready for their processes.

5. **Material Review Boards and formal nonconformance disposition** are critical for large projects; even small defects require documented review and decision (accept, rework, scrap) to maintain traceability.

6. **The implementation process is complete when end products are ready for verification**, meaning they are fabricated/purchased/acquired, reviewed and checked for integrity, and accompanied by all required documentation.

## Connects To
- **ISO/IEC/IEEE 15288 (Systems and Software Engineering — System and Software Life Cycle Processes)**: Product implementation is one of the six primary process groups; aligns with "Implementation" and "Integration and Integration Testing" processes.

- **Configuration Management (NASA SE processes)**: As-built documentation and configuration baselines are controlled through CM; nonconformance and waiver records feed the change control process.

- **Product Verification Process (NASA 5.3)**: The handoff from Product Implementation to Product Verification occurs when the end product is ready for acceptance-level testing; verification plan and procedures must account for the chosen implementation strategy.

- **NPR 7123.1 (NASA Systems Engineering Processes and Requirements)**: Mandates implementation planning and traceability of requirements through fabrication and procurement.
