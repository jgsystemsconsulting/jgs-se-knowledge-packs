# Chapter 2: Lifecycle Model and Quality Reviews

## Core Idea
SEM partitions the information systems engineering lifecycle into eight major stages, each with activities, tasks, intermediate work products, and a measurable Stage Exit. Quality is enforced continuously via Structured Walkthroughs, In-Stage Assessments, and Stage Exit decisions — not only at final test.

## Frameworks Introduced
- **Eight-stage lifecycle**: Planning → Requirements Definition → Functional Design → System Design → Construction → Integration and Testing → Installation and Acceptance → Maintenance.
- **Three quality gates per stage pattern**: Structured Walkthrough (peer technical review), In-Stage Assessment (independent QA review), Stage Exit (go/no-go with owner/stakeholder approval).
- **Size-based tailoring**: Project size classes adapt activity depth and deliverables (exhibits map work products by size).

## Key Concepts
- **Stage structure**: Activities and tasks produce inspected intermediate work products used to assess integrity, quality, and status early.
- **Success premises**: Feasible concept; comprehensive participatory planning; resource/schedule commitments; complete accurate requirements; sound design; consistent maintainable construction; comprehensive testing.
- **Structured Walkthrough**: Organized peer review of technical work products/documentation; may include reviewers beyond the immediate team; detailed in the Structured Walkthrough Process Guide.
- **In-Stage Assessment**: Independent review of stage work products/deliverables, typically by QA, results to the project manager; recommended after major milestones and deliverable completion; detailed in the In-Stage Assessment Process Guide.
- **Stage Exit**: End-of-stage review to proceed, continue in stage, or abandon; system owner and stakeholder approval keep control and prevent unauthorized advancement; detailed in the Stage Exit Process Guide.
- **End products**: System, data, technical documentation, user training and support — sustained under configuration management.
- **Adaptation**: Lifecycle can be tailored (including COTS-oriented adaptations illustrated in SEM exhibits) while preserving review and exit discipline.
- **Maintenance as lifecycle continuation**: After acceptance, maintenance applies a nested process model (problem identification through delivery of changes).

## Mental Models
- Every stage is a mini-project with exit criteria, not a waterfall label on a Gantt bar.
- Peer walkthroughs catch technical defects; independent assessments catch process/completeness gaps; exits catch authorization gaps.
- Tailor depth to size, not the existence of planning, CM, QA, or exits.
- Early work-product inspection is how SEM front-loads quality instead of relying on late testing alone.

## Anti-patterns
- **Paper Stage Exits without owner decision rights**: Defeats control intent.
- **Walkthroughs as slide reviews with no work-product inspection**: Misses defect discovery.
- **One size of process for tiny and enterprise projects**: Ignores size tailoring tables.
- **Skipping assessments until final acceptance**: Loses intermediate integrity knowledge SEM is built to create.

## Key Takeaways
1. Eight stages structure DOE IT systems engineering from planning through maintenance.
2. Each stage ends in a controlled Stage Exit with owner/stakeholder authority.
3. Structured Walkthroughs and In-Stage Assessments provide complementary quality views.
4. Intermediate work products are first-class status and quality evidence.
5. Tailor activities by project size while keeping the control skeleton.
6. Companion process guides supply procedural detail for the three review types.

## Connects To
- **ch01**: Why SEM exists and CMM alignment.
- **ch03**: Planning stage — first application of the model.
- **ch04–ch06**: Development stages using the same review machinery.
- **ch07**: Maintenance nested lifecycle after acceptance.
