# Chapter 6: Integration & Testing and Installation & Acceptance Stages

## Core Idea
Integration and Testing verifies that constructed components work together against requirements. Installation and Acceptance put the system into the operational environment and obtain formal owner acceptance — the lifecycle hinge before Maintenance.

## Frameworks Introduced
- **Integration and Testing stage**: Assemble components; execute integration and system tests; manage defects; demonstrate requirement satisfaction.
- **Installation and Acceptance stage**: Deploy to target environment; train users; perform acceptance; transition to operational support.
- **Test traceability**: Tests map back through the RTM to requirements and design.

## Key Concepts
### Integration and Testing
- **Purpose**: Comprehensive testing program — a SEM success premise — validates integrated behavior, interfaces, and non-functional needs.
- **Activities**: Integration builds; test planning/execution; defect logging and regression; security/performance tests as required by the requirements baseline; readiness evidence for acceptance.
- **Quality reviews**: Walkthroughs of test plans/results as work products; In-Stage Assessments; Stage Exit to authorize installation.
- **Size tailoring**: Smaller projects still test against baselined requirements but with scaled documentation.

### Installation and Acceptance
- **Purpose**: Install the system in the operational setting, validate it works there, train users, and obtain acceptance from the system owner.
- **Activities**: Deployment/installation procedures; data conversion as needed; user and operations training; acceptance test/review; delivery of documentation and support materials; CM handoff to operational baselines.
- **Acceptance authority**: Owner acceptance is the business decision that the investment is fit for use — distinct from technical test pass alone.
- **Transition**: Successful exit starts Maintenance under documented CM procedures.

## Mental Models
- Integration testing answers “does the system work as a whole?”; acceptance answers “will the owner run the mission on it?”
- Environment parity matters: lab-green and production-red is an installation failure mode SEM tries to catch.
- Training and support artifacts are end products, not optional PDFs.
- Defects found here should still trace to requirements/design gaps for learning, not only hotfixes.

## Anti-patterns
- **Acceptance as a signature ceremony without acceptance criteria**: Hollow Stage Exit.
- **Testing only happy paths**: Misses mission-essential failure modes.
- **Deploying without CM baseline of what was installed**: Maintenance cannot reproduce the system.
- **Skipping user training**: Operational rejection after technical success.

## Key Takeaways
1. Integration and Testing prove end-to-end behavior against the requirements baseline.
2. Traceability makes test coverage auditable and directed.
3. Installation validates the system in its real environment.
4. Owner acceptance is a controlled Stage Exit decision.
5. Training, documentation, and support deliverables complete the end product set.
6. Clean handoff into Maintenance depends on CM baselines and acceptance records.

## Connects To
- **ch04–ch05**: Requirements/design/construction inputs to test.
- **ch02**: Exit controls at the end of development stages.
- **ch07**: Maintenance process begins after acceptance.
- **ch03**: Performance measures from planning should be evaluable here.
