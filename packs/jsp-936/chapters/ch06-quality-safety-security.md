Sources: JSP 936 Part 1 V1.1, printed body pp. 28-29 (source Chapter 7, paragraphs 187 to 197).

# Quality, Safety and Security

## Core Idea

Chapter 7 of the source is short and directive: the established quality, safety and security regimes continue to apply to AI, each with an AI-specific overlay. Nothing here replaces the existing frameworks; the chapter states which ones bind AI work and what extra attention AI demands of each.

## Frameworks Introduced

- Quality: MOD quality policy in JSP 940 must be applied to AI product development and use, with quality planning and activities commensurate with the risk and maturity of the AI.
- Safety: the Defence Safety Management System framework in JSP 815 continues to govern, with evidence-based safety management as its fundamental principle, and unique AI safety risks folded into wider safety cases and risk assessments under JSP 375 and JSP 376.
- Security: the Secure by Design approach required for information-based capabilities across definition, acquisition, development, maintenance and disposal extends to AI, upgraded from one-time security assurance to continuous assurance.

## Key Concepts

On quality, planning must account for the pivotal role of data, how users interact with the system, and the dynamic nature of AI, including its ability to adapt to its environment and its rate of change. Quality assurance activities must cover the broader AI aspects: compliance with configuration management, safety, security and ethical requirements.

On safety, because of the size and complexity of many AI applications and datasets, the evidence that supports a meaningful SMS may need collecting and managing from the earliest development stages. AI may present unique safety risks from its development or behaviour; these must be analysed and included in the relevant wider safety cases and software and system risk assessments. Safety-related risk assessments are carried out early in the AI lifecycle and risks are managed coherently and proportionately throughout, including, where appropriate, demonstration of compliance with Def Stan 00-056 for system safety and Def Stan 00-055 for software safety. Risk analyses should include the reasonably predictable behaviours of the entities the AI interacts with, in both benign and adversarial environments, and operating excursions beyond the ODD. JSP 892 must be applied to AI risk, with consequences of failure reflecting direct impacts and wider societal concerns, and with risk-management activities capable of keeping pace with AI's typical rate of change.

On security, the directive is explicit that traditional security risk-management approaches may not satisfy because of the rapidly evolving nature of AI. The focus should be continuous assurance of system security: the system continually monitored, hardened and improved, potentially to the point of being self-defending and self-monitoring with minimal manual interference. AI may present unique security risks from development or behaviour, with data poisoning given as the worked example; these must be analysed at the earliest practicable opportunity and included in the security aspects of wider safety cases and risk assessments. Security analyses must cover both conventional risks and adversaries interfering with AI performance, such as privacy loss through data breaches or induced adversarial behaviour that makes the AI produce an incorrect output from misleading input, and they must include the data used to develop the AI, because poisoned development data leads to unsafe behaviour in operation.

## Mental Models

- Three regimes, one overlay: quality, safety and security each keep their JSP anchor and each gain an AI-specific duty list from this chapter.
- Evidence timing is the safety message: for AI, start collecting safety evidence earlier than for conventional systems, because scale and complexity make late reconstruction infeasible.
- Security shifts from built-secure to staying-secure: a static compliance snapshot does not match a system that keeps changing under it.

## Anti-patterns

Treating the traditional security risk assessment as sufficient for AI is refused outright. Leaving data poisoning out of the security analysis is refused, since the development data chain is named as an attack surface. Deferring safety evidence gathering until later lifecycle stages is refused where the size and complexity of the AI make early evidence the only viable route.

## Key Takeaways

- The named anchors are JSP 940 for quality, JSP 815 for the SMS framework, JSP 375 and JSP 376 for safety cases and risk assessments, JSP 892 for risk management, Def Stan 00-056 and Def Stan 00-055 for safety compliance demonstration, and the internal Secure by Design policy for security.
- This pack names those sources and does not restate them; the jsp-815 pack carries the safety management system, and the jsp-376 pack carries acquisition safety policy.
- The chapter's brevity is the point: AI does not get a new quality, safety or security regime, it gets new obligations inside the existing ones.

## Connects To

The hazard analysis and data duties in ch05 produce the inputs this chapter places into safety cases; the adversarial-interference material connects to the ODD-excursion assurance in ch08; the ethics compliance that quality assurance must cover is defined in ch03.
