# Chapter 10: Life Cycle Terms and Concepts

## Core Idea

Technical reviews and audits are the primary mechanisms by which independent stakeholders assess system state and progress against pre-established criteria, supporting both programmatic and technical decision-making across lifecycle stages.

## Frameworks Introduced

- **Technical Review (per ISO/IEC/IEEE 24748-8)**: A series of systems engineering activities conducted at logical transition points in a system lifecycle to assess project progress relative to technical requirements using mutually agreed-upon criteria.
  - When to use: At decision gates and milestones to validate readiness to proceed between lifecycle stages.

- **Audit (per ISO/IEC/IEEE 15288)**: An independent examination of a work product or set of work products to assess compliance with specifications, standards, contractual agreements, or other criteria.
  - When to use: When objective verification of compliance is required; can authorize risky activities (e.g., safety-critical testing).

- **Three Review Timing Strategies (Boehm & Lane)**:
  - **Schedule-based**: Fixed, pre-agreed dates (early feedback; risk of insufficient information)
  - **Event-based**: Triggered by delivery of defined artifacts (more complete information; risk of late issues)
  - **Evidence-based**: Triggered when specific technical risk levels are achieved (higher stakeholder commitment; risk of late feedback)

## Key Concepts

- **Transition Points**: Logical moments in the lifecycle where technical reviews/audits should occur—typically aligned to stage boundaries or major milestones.

- **Decision Gates**: Checkpoints where technical review results inform decisions to proceed, pause, restart, or terminate work.

- **Entry and Exit Criteria**: Pre-defined conditions that must be met before a review begins (entry) and before it closes (exit); essential for objective, comprehensive assessment.

- **Subject Matter Expertise (SME)**: Selection of reviewers requires balancing people close enough to the project for insight with reviewers far enough removed for independence; specialty engineering representation is critical.

- **Configuration Baselines**: Technical reviews and audits support establishing, revising, and verifying configuration baselines as part of configuration management.

- **Validation via Reviews**: Technical reviews and audits enable early validation of requirements, design, and work products through involvement of appropriate stakeholders (including end users).

- **Independent Analysis**: Reviews are most effective when conducted by stakeholders sufficiently independent and knowledgeable to objectively assess outcomes without bias.

## Mental Models

- **The Independence-Insight Balance**: Build review teams with a mixture of people close enough to provide critical insights and people far enough removed to maintain objectivity. Avoid both extremes: "too close" (bias from incentives) and "too far" (miss domain nuances).

- **Three Phases of Execution**: Structure reviews as Prepare (define scope, criteria, entry/exit conditions, identify reviewers) → Conduct (participants analyze relevant information from multiple perspectives; discuss results) → Complete (communicate findings, implement identified actions).

- **Recursive Applicability**: Technical reviews and audits can be applied to a system of interest, recursively to constituent system elements, and can occur sequentially, iteratively, incrementally, or concurrently—as long as entry criteria are met first.

## Anti-patterns

- **Insufficient Preparation**: Holding a technical review without meeting entry criteria, with incomplete information, or under schedule/cost pressure results in missed defects and unreliable decision support.

- **Lack of Clear Criteria**: Reviews without pre-established, mutually agreed-upon assessment criteria become subjective and fail to provide objective evidence for decision-making.

- **Wrong Reviewer Mix**: Selecting reviewers who are "too close" (biased by project incentives) or "too far" (unable to surface critical issues) undermines the independence and effectiveness of the review.

## Key Takeaways

1. Technical reviews and audits are essential mechanisms for project visibility, risk management, and support for decision gates—not overhead activities.

2. Review timing strategy (schedule-based, event-based, evidence-based) depends on project maturity and organizational culture; each has distinct tradeoffs in information completeness and feedback timing.

3. Entry and exit criteria must be defined, coordinated, and verified before a review begins; this is non-negotiable for objective outcomes.

4. Reviewer selection requires deliberate balance between deep project knowledge and independence; specialty engineering (safety, security, reliability) perspectives should always be included.

5. The three-phase approach (Prepare, Conduct, Complete) ensures that reviews produce actionable results: findings are communicated, actions are tracked, and project outcomes are improved.

6. Technical reviews and audits support four critical SE processes: project assessment and control, configuration management, validation of requirements and design, and authorization of high-risk activities.

7. These practices can scale from a system to individual system elements and work recursively across the hierarchy—making them adaptable to projects of any size or complexity.

## Connects To

- **ISO/IEC/IEEE 15288 (System Life Cycle Processes)**: Provides the normative framework for lifecycle management and defines audit as an independent compliance examination.

- **ISO/IEC/IEEE 24748-8 (Technical Reviews and Audits on Defense Programs)**: Specialized guidance for applying reviews and audits in defense acquisition; offers domain-specific tailoring examples.

- **Decision Gates and Entry/Exit Criteria** (see Life Cycle Stages chapter): Technical reviews are the mechanism by which decision gates are executed; entry/exit criteria are the prerequisite framework.

- **Configuration Management**: Baselines are established, revised, and verified through technical review processes.

- **Development Approaches** (sequential, incremental, evolutionary): Each development approach requires reviews at different cadences and with different timing strategies; the approach determines when and how often reviews occur.

- **DoD, NATO, and NASA System Engineering Standards**: Each domain provides representative examples of how to tailor technical reviews for their specific lifecycle models and regulatory contexts.
