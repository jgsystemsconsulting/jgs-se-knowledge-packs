# Chapter — Automation

> Source: FAA *Human Factors Design Standard* (HF-STD-001B), Section 5.1 "Automation" (paragraphs 5.1.1 through 5.1.15). Every requirement, definition, and discussion in this chapter is drawn from that section. Where the standard cites an underlying author (Billings, Parasuraman, Wiener, Woods, NRC, NUREG, and others), those citations are the standard's own attributions.

## Core Idea

HF-STD-001B defines automation as a device or system independently carrying out a function that a person used to perform. The standard's whole posture toward that shift is human-centered: automation exists to support the operator, not to displace the operator from command. Section 5.1 turns that posture into roughly 150 discrete, individually-cited design requirements organized into fifteen topic clusters — general principles, design and evaluation, feedback, interface, trust, modes, monitoring, fault management, false alarms, training, function allocation, and the three "type" sections (information, control, and adaptive automation) plus decision aids.

The recurring tension the section keeps returning to: automation is usually introduced to cut workload and boost performance, but poorly designed automation does the opposite — it distracts, raises workload exactly when it is already high, breeds complacency, erodes situation awareness, and lets manual skills decay. So the standard's requirements are mostly guardrails against those failure modes rather than enthusiasm for automating more. Two hard `shall` rules anchor everything: keep the user in the command role, and never make the system so automation-dependent that a person can no longer recover from an emergency or run it by hand if the automation quits.

This chapter is grounded entirely in the FAA standard. It is human factors guidance written for air-traffic and aviation-domain systems — distinct from, and complementary to, the NASA HSI body of knowledge. Where NASA's material frames human-systems integration as a lifecycle discipline woven into the SE engine, HF-STD-001B supplies the concrete, requirement-level design rules an engineer applies to an automated subsystem. The two are meant to be read together; this is the design-rule layer, not the program-process layer.

## Frameworks Introduced (exact source names, when/how)

- **Minimum automation human factors requirements (5.1.1.1).** A five-part baseline every automated system should meet: keep the user informed of operating mode, intent, function, and output; signal failure or degradation; warn when an unsafe mode is manually selected; stay out of the way of manual tasks; and permit manual override. This is the section's opening checklist — apply it to any automated function before going further.

- **Human-centered vs. technology-centered automation (5.1.1.4).** The standard's framing distinction: automate to support the user where it genuinely helps (human-centered), not merely because the capability exists (technology-centered). Used to justify *whether* a function should be automated at all.

- **Error resistance vs. error tolerance (5.1.1.18).** Two complementary error strategies. Resistance makes mistakes hard to commit (simplicity and clear information are the named tools); tolerance limits the damage of mistakes that do occur (adding monitoring is the named lever). Both are required, not either/or.

- **Levels of automation, high to low (Exhibit 5.1.11).** A ten-step ladder ranging from a system acting autonomously with no human involvement, down through variants that inform after acting, allow a timed veto, act only on approval, suggest one or a few alternatives, offer the full alternative set, and finally offer no assistance. Used to pick *how much* authority to grant a given function, and to constrain it — for higher-uncertainty, higher-risk tasks the section says automation should go no further than suggesting a preferred option (5.1.11.7).

- **Function allocation alternatives (5.1.11.1).** A defined set of allocation schemes to evaluate for feasibility and effectiveness: fully manual, partially automated, fully automated, and adaptive. Machines get only functions they do well; tasks demanding flexibility in unpredictable conditions go to the person (5.1.11.3–5.1.11.4).

- **Fault management, four tasks (5.1.8).** The standard adopts a definition of fault management spanning detection, diagnosis, prognosis, and compensation — covering how a user notices and recovers from failures the automation may or may not have caught itself.

- **Information automation (5.1.12).** A named automation type covering acquisition and integration of data: filtering, distributing, transforming, confidence estimates, integrity checks, and serving user requests. Its primary stated objective is maintaining and enhancing situation awareness.

- **Control automation (5.1.15).** A named type where the system executes actions or control tasks with some autonomy. Its central constraints are bounded authority — it must not jeopardize safety or worsen a bad situation — and guaranteed override/backup for safety-critical or life-critical controls.

- **Adaptive automation (5.1.13).** A named type defined as real-time, flexible reallocation of tasks between user and system as situational demands change. Its rationale is keeping the user an active controller rather than a passive observer, which guards against the monitoring, situation-awareness, and manual-skill decrements that plague static high automation.

- **Decision aids / decision support systems (5.1.14).** Automated systems that support human decision-making, solicited or not, by narrowing alternatives or suggesting a preferred option. The section's governing rule (5.1.14.6): aids should assist rather than replace the decision maker, supplying data for judgment instead of commands to execute.

- **The trust model (5.1.5).** A characterization of how operator trust in automation behaves: it builds slowly through reliable, predictable, robust, familiar, and useful performance, but drops suddenly after a critical error, and is harder to rebuild than to earn the first time. The asymmetry — and the warning that very high reliability can itself breed complacency — is the framework's key insight.

## Key Concepts

- **User stays in command (5.1.1.2, 5.1.1.21).** A `shall`: automated systems must not remove the user from the command role. Automation should not veto user actions or leave the user unable to override the rules governing it — the one carve-out being when there is genuinely not enough time for a human decision.

- **Automate only with justification (5.1.1.3, 5.1.1.9).** Functions should be automated only if doing so improves system performance *without* reducing human involvement, situation awareness, or task performance. How to implement automation should follow the system's explicit goals, not a head-to-head comparison of automated against manual versions.

- **Active involvement sustains awareness (5.1.1.7, 5.1.7.3).** Awareness of system state cannot be held passively. The standard requires giving users a genuinely active role through meaningful tasks regardless of automation level, because reduced involvement lengthens emergency response times and erodes knowledge and skills over time.

- **Workload is two-sided (5.1.1.10, 5.1.1.11).** Automation should not increase demand for cognitive resources, and both extremes of workload — too high and too low — should be avoided. Poorly designed automation tends to add load precisely when load is already high.

- **Predictability and transparency (5.1.1.19, 5.1.3.4).** Systems must behave predictably so users know the purpose of the automation and how it affects operations; predictability also makes malfunction easier to spot. When feedback is poor the section calls the automation "silent," and warns silent automation surprises users and causes coordination and system failures.

- **Mode awareness (5.1.6).** Mode and function status should be clear whenever behavior changes across modes, because lack of feedback about which mode is active causes mode errors. The number of modes should be minimized — more modes mean more flexibility but more error opportunity and harder learning.

- **Monitoring is real work (5.1.7).** Vigilance tasks that look "simple" carry significant cognitive cost. The section caps purely-monitoring stretches at 20 minutes (5.1.7.5), recommends keeping users in active control rather than passive monitoring, prescribes intermittent manual control during long automated periods (5.1.7.12), and tells designers to account for vigilance decrements and even circadian effects on monitoring performance.

- **The complacency / over-reliance trap (5.1.5.5, 5.1.10.7, 5.1.12.16).** Constant high reliability is double-edged: it earns trust but encourages users to monitor with less vigilance and overlook errors. Countermeasures named include training against over-reliance, intermittent manual control, and making automated and non-automated cues equally prominent so users still gather confirming/disconfirming evidence.

- **False alarms erode trust (5.1.9).** False-alarm rates should not be frequent enough to make users mistrust the system. Where event base rates are low, even a sensitive warning system yields many false alarms, and users should be told this is inevitable.

- **Setup error and input validation (5.1.1.25, 5.1.12.1).** Automation failures are often setup errors, so systems should let users check setup and inputs — possibly with independent error-checking — and distinguish an algorithm malfunction from bad input data. The system should flag when data are incomplete, missing, unreliable, invalid, or sourced from backup.

- **Graceful degradation and override (5.1.8.1, 5.1.15.6).** A `shall`: when automation a function depends on fails, the system must still allow manual control and preserve safe operation. For safety- or life-critical controls, override and backup alternatives must be available and the backup information readily accessible.

- **Decision-aid explainability (5.1.14.16–5.1.14.21).** Aids should estimate and indicate the certainty of their analysis with rationale, expose the data behind derived results for verification, give access to the rules/algorithms used, and offer layered explanations (a short one first, more detail on request) in terms familiar to the user.

## Mental Models

- **Mental model (defined, 5.1.14.7).** An individual's understanding of the processes underlying system operation. The standard treats the operator's mental model as a design target: users need an accurate one to monitor effectively, diagnose failures, and predict future states (5.1.7.11), and decision-aid support should be consistent with it.

- **Trust calibration (5.1.5.2).** The goal is not maximum trust but *calibrated* trust — training should give the user a sound sense of when the automation can be relied on and when it cannot in a given set of conditions, and teach them when to question it (5.1.10.6). Both over-trust and under-trust are failure states.

- **Knowledge of intent (5.1.14.30).** In an intelligent human-machine system, each element should know the others' intent. Monitoring of the system by the user, and of the user by the system, only works if each knows what the other is trying to accomplish — a two-way transparency model.

- **The vigilance decrement.** A continuously declining ability to maintain attention while monitoring. The section's notable point: it is not caused by understimulation but by the heavy, often frustrating cognitive load of vigilance, and it strikes experts and novices alike. This reframes "just keep watching the screen" as an expensive, fatiguing task that must be designed around.

- **Authority graded to risk.** Reading the levels-of-automation ladder together with 5.1.11.7 and 5.1.15.2 gives a working model: the more uncertain or risky the task, the lower on the autonomy ladder the system should sit — capping at "suggest a preferred alternative" for high-risk decisions, and never granting control automation enough authority to make a bad situation worse.

## Anti-patterns

The standard names several failure modes directly:

- **Technology-centered automation (5.1.1.4)** — automating because the capability exists rather than because it helps the user.
- **Silent automation (5.1.3.4)** — automation with poor feedback, which surprises users and triggers coordination and system failures.
- **Mode errors (5.1.6.1)** — acting on the wrong assumption about which mode is active, caused by inadequate feedback on automation state.
- **Automation bias (5.1.10.5, 5.1.12.16)** — using automation heuristically instead of actively seeking and processing information; named as a thing to train against and to counter by making non-automated cues equally salient.
- **Complacency / over-reliance (5.1.5.5, 5.1.7.12, 5.1.10.7)** — reduced vigilance and overlooked errors that follow from constantly reliable automation; combated with intermittent manual control and explicit training.
- **Manual-skill degradation and lost situation awareness (5.1.7.12, 5.1.13)** — atrophy of instrument scan, positional awareness, and hand-flying skill from extended automated operation, making automation-to-manual transitions difficult.

## Key Takeaways

- Treat the five-part minimum requirement (5.1.1.1) and the two `shall` anchors — keep the user in command (5.1.1.2) and never become un-recoverably automation-dependent (5.1.1.20) — as non-negotiable gates before designing any automated function.
- Automation is justified only when it improves performance without costing human involvement, situation awareness, or skill. "We can automate this" is not a reason; the standard explicitly rejects technology-centered automation.
- Match automation authority to task risk and uncertainty using the levels-of-automation ladder; hold high-risk decisions at "suggest, do not execute."
- Design for the human as an active participant: cap pure-monitoring stints, schedule intermittent manual control, and keep cues balanced — because passive monitoring degrades vigilance, skills, and awareness.
- Build for transparency and trust calibration: predictable behavior, effective (non-silent) feedback, clear mode status, uncertainty estimates on decision aids, and training that teaches when to trust and when to question.
- Engineer the failure path first: unambiguous failure indication, graceful degradation to manual control, accessible overrides and backups, and validation under both normal and failure modes (5.1.2.8) with representative users before fielding (5.1.2.9).
- Decision aids assist; they do not decide. Provide data for judgment, expose rationale and underlying data, and let the user control whether and how the aid is used.

## Connects To

- **nasa-hsi (companion pack).** This chapter is the design-rule complement to the NASA HSI material. NASA HSI frames human-systems integration as a lifecycle discipline embedded in the systems engineering engine and program phases; HF-STD-001B Section 5.1 supplies the concrete, citable automation design requirements an engineer applies once a function is being automated. Use NASA HSI to decide *where in the lifecycle* human-automation concerns get addressed and *how to plan* them; use this chapter for *what the automated subsystem must actually do*. Note the caveat: human-systems integration extends well beyond the NASA treatment — HF-STD-001B is one of those broader, domain-specific sources.
- **Function allocation and the SE process.** The function-allocation alternatives (5.1.11) and the human-centered-goals-first design sequence (5.1.2.2) connect directly to functional analysis and allocation in any systems-engineering process; the standard insists allocation be evaluated (including via high-fidelity simulation, 5.1.11.2) rather than assumed.
- **Verification and validation.** Design-and-evaluation requirements (5.1.2) — test as a whole, test normal and failure modes, validate with human-in-the-loop simulation, test with representative users before implementation — map onto V&V and human-in-the-loop test planning.
- **Situation awareness and workload.** The monitoring, information-automation, and adaptive-automation clusters lean on situation awareness and cognitive-workload constructs that recur throughout human factors and HSI literature; this chapter is the FAA's requirement-level expression of them.
- **Other HF-STD-001B sections.** Section 5.1 sits inside Section 5, "Specific Design Requirements"; its interface, display, alarm, and control rules connect to the standard's broader display, controls, and alerting guidance.
