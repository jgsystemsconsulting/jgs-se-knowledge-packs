# Chapter 8: Applying Cyber Resiliency & Risk (Vol 2)

## Core Idea
Cyber resiliency is applied by **tailoring** the framework (goals → objectives → techniques → approaches → principles) to a specific system, its **mission risk**, and a specific **adversary** — above all the **advanced persistent threat (APT)**. From a risk-management perspective, cyber resiliency reduces the mission/business/organizational risk of *depending on cyber resources*, and it integrates with the NIST risk ecosystem (RMF / SP 800-37 and controls / SP 800-53) rather than replacing it.

## Frameworks Introduced
- **Adversary-driven tailoring** — select and place resiliency against the APT's likely goals, attack vectors, and adaptation, not against a generic checklist.
  - When to use: when deciding which objectives/techniques/approaches a given system actually needs.
- **Risk integration** — cyber resiliency as a contributor to enterprise risk management, expressed through the RMF and the SP 800-53 control set.
  - When to use: when justifying, prioritizing, and governing resiliency investment alongside other security controls.

## Key Concepts
- **The APT model**: the advanced persistent threat is capable, well-resourced, stealthy, and *adaptive* — it pursues objectives over time via multiple vectors (cyber, physical, deception), adapts to defenders' efforts, and seeks to maintain presence. Cyber resiliency assumes such an adversary is present or will succeed in getting in.
- **Reduce mission risk of cyber dependence**: the purpose statement — resiliency exists to keep the mission viable despite the unavoidable risk of relying on compromiseable cyber resources.
- **Tailoring inputs**: mission/business functions and their criticality; the threat (APT behaviors and vectors); the architecture and its trust relationships; cost, performance, and other constraints. These drive which goals/objectives/techniques to emphasize.
- **Trade-offs and analysis**: resiliency techniques cost money, performance, and complexity, and may interact (positively or negatively) with each other and with conventional security; selection is an explicit cost/benefit and interaction analysis against the adversary.
- **Integration with RMF and SP 800-53**: cyber-resiliency techniques map to security/privacy controls and control enhancements; resiliency is selected, implemented, assessed, and authorized through the same risk-management processes as other controls, and informed by the organizational risk strategy.
- **Deny the adversary, don't just absorb**: effective application both keeps essential function alive (withstand/recover) and actively degrades the adversary's freedom of action (constrain, deceive, increase cost) — turning resiliency into a contest, not just endurance.

## Mental Models
- Tailor to mission and adversary, then to architecture: start from *which functions must survive* and *who is attacking*, and let that drive technique selection and placement — never the reverse.
- Resiliency is a risk investment: every technique buys down some mission risk at some cost; prioritize by risk reduced per unit cost, governed through the RMF.
- Assume the adversary adapts: a static resiliency posture decays; the **Adapt** goal and Unpredictability/Realignment techniques exist because the APT changes.
- Resiliency and prevention are complementary: conventional security (prevention) plus cyber resiliency (operate-through-compromise) together cover both "keep them out" and "survive when they're in."

## Anti-patterns
- **Generic-threat resiliency**: applying techniques without modeling the actual adversary, producing cost without targeted benefit.
- **Resiliency outside risk governance**: deploying techniques disconnected from the RMF, the control set, and the organizational risk strategy.
- **Absorb-only posture**: building to survive hits but never to detect, constrain, or impose cost on the adversary.
- **Set-and-forget**: a fixed posture against an adversary that adapts — no realignment or unpredictability over time.

## Key Takeaways
1. Cyber resiliency is **tailored** to the system, its **mission risk**, and a specific **adversary** — above all the **APT**.
2. Its purpose is to **reduce the mission risk of depending on cyber resources** — assume breach.
3. Tailoring is driven by **critical functions, threat, architecture, and constraints**, with explicit cost/benefit/interaction analysis.
4. It **integrates with RMF (SP 800-37) and SP 800-53**, not replacing them — governed by the organizational risk strategy.
5. Effective application **denies the adversary freedom of action**, not just absorbs hits — and **adapts**, because the APT does.

## Connects To
- **ch05–ch07**: the framework, techniques, and design principles this chapter tailors and applies.
- **ch01 (Foundations)**: SSE's "adequately secure" and risk-informed stance.
- **`nist-csf`**: organizational cybersecurity risk management and the Recover function.
- **RMF (SP 800-37) / SP 800-53**: the risk and control processes resiliency integrates with.
- **`nist-ai-rmf`**: an analogous adversary/risk-tailored approach for AI systems.
