# UKCA-era obligations for device software, per the MHRA guidance

Once software qualifies as a medical device on the GB market, S6 attaches a set of obligations: classification route, essential requirements, registration, vigilance, field safety, labelling, and end-of-life duties.
This chapter collects those obligations; how software crosses the qualification line in the first place is ch03's subject.

## Market and marking

Qualified stand-alone software and apps must be UKCA marked under UK MDR 2002 for Great Britain; the government has extended acceptance of CE marked devices, and Northern Ireland applies different rules.
A prospective buyer should be able to see conformity before purchase, so the guidance wants the UKCA mark on the app's primary landing page and as an app store screenshot.

## Route to compliance

General devices fall into four classes (I, IIa, IIb, III), and the guidance lists the classification rules most likely to bite for software: software driving or influencing a device takes that device's class; active therapeutic devices that exchange energy sit at IIa or IIb; active diagnostic devices sit at IIa, rising to IIb where they allow direct diagnosis or monitoring of vital parameters whose variation could immediately endanger the patient; all other active devices sit at class I; contraception and sexually transmitted disease prevention devices sit at IIb.
Class I relies on the manufacturer's self-declaration; the other classes require a UK Approved Body, or an EU notified body for CE marked devices.
Every device placed on the GB market must also be registered with the MHRA.
IVD software follows the parallel IVD route with four product categories (general IVDs, self-testing IVDs, List A, List B) and its own essential requirements, and accessory software for an active implantable device is treated as an active implantable.

## Essential requirements

The general requirements demand that benefits outweigh risks, that design follows the acknowledged state of the art, and that risk reduction follows the hierarchy: design out the risk, protect against what remains, inform users of residual risk.
A clinical evaluation is required, and the guidance points to the standard European clinical evaluation guide for how to run it.
Evidence is the operative word: the manufacturer needs to show the app does what it claims, gathered through clinical evaluation.

The design and construction requirements the guidance flags for software are worth listing as the assessment will meet them:

- Safety of the whole combination when the software works with other devices or equipment, including the connection system.
- For stand-alone software this means demonstrating compatibility with the recommended hardware platforms.
- Repeatable, reliable performance of electronic programmable systems, with single-fault conditions addressed.
- Software validated to the state of the art, taking in development lifecycle, risk management, verification, and validation.
- Alarm systems where the device monitors clinical parameters whose deterioration could be fatal.
- Information accompanying the device: label particulars and instructions adequate for the intended user's training and knowledge.
- Installation and connection details in the instructions where the software must work with identified devices or equipment.
- For measuring functions: stated accuracy limits, ergonomic display design, and legal units of measurement.

Instructions may be supplied electronically where that carries less risk than paper, and Class I and IIa devices can omit them where they can be used safely without.
The guidance cross-recommends two state-of-the-art provisions as an interim: medical device software should address the software-validation provision of the medical device legislation's essential requirements, and diagnostic software using IVD data should address the corresponding performance provision of the IVD legislation's essential requirements.

Manufacturers must also consider data protection law (the GDPR and the privacy and electronic communications regulations).
In-house manufacture carries partial exemptions where the device is used only for patients within the institution that made it.
Software that is not a medical device at all is not outside every rule: other UK legislation, such as the general product safety regime, may still apply.

## Post-market duties

The manufacturer runs an effective post-market surveillance system and reports serious adverse incidents to the MHRA through its reporting portal.
Because app stores break traceability, the guidance recommends a registration or activation scheme so users of distributed copies can be found when a field safety corrective action is needed.
Field safety notices go to the MHRA and to users; for online apps the notice summary should appear at app start-up with a link to the full notice, and the guidance extends the same expectation to cybersecurity notices.
End-of-life gets its own appendix: in-app alerts announcing decommissioning, reasonable timelines for end of support and market withdrawal, planned handling of cybersecurity and compatibility after support ends, continued surveillance while devices remain in use, and awareness that app stores may require some useful function for the app to stay listed.

The guidance closes with a standards shelf for developers (usability engineering, software lifecycle processes, quality management systems, risk management, and risk management applied to software) and appendices on symptom checkers, clinical calculators, the drives-or-influences question, and field safety and end-of-life notices.

Sources: S6
