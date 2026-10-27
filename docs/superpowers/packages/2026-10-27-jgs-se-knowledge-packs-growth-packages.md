---
date: 2026-10-27
project: jgs-se-knowledge-packs-growth
mode: full
rounds: 1
input_digest: 0e8c605d87ad359150bcf40eb2cda2b32780fc2ec00b6bee17711a9bed94d78a
open_objections: []
---

# Work packages - jgs-se-knowledge-packs-growth (2026-10-27, full scoped re-run)

Scope of this cut: the two remaining ranked pack builds. P28 jsp-936 (reused id),
P42 fhwa-its-se (reused id). Converged in one round (value 2, risk 2, cohesion 0
honest zero; merge reused both prior ids; triage zero_critical). No conflicts.

## P28 - uk-defence-jsp-936-pack

- **id**: P28; **name**: uk-defence-jsp-936-pack; **size**: L; **status**: done (2026-10-27; EXECUTED + IVL logs in docs/superpowers/plans/); **corroboration**: 2 (value, risk); **deps**: none; **promoted_ids**: []
- **problem**: Build-order row 4 uk-defence family is still partial: jsp-815 and jsp-376 live, but packs/jsp-936 is absent and /se Defence routing plus the Licences rows carry only those two. The 2026-10-14 research gate ranked JSP 936 Part 1 (Dependable AI in Defence, OGL v3) as first alternate after 376. Risk bite: shipping without per-document OGL v3 vet or missing any live registration surface leaves a CI-green pack that breaks redistribution trust or drifts the orchestrator/index (the known I11 registration class, which CI only catches after the miss).
- **evidence**: docs/candidate-packs.md:L19 (row 4, partially built 2026-10-14), L25 ("The remaining full-pack work on this list is the unfinished part of the uk-defence family."), L69; packs/se/SKILL.md:L117 (Defence row routes jsp-815, jsp-376 only), L157-158 (OGL licence rows); NOTICE OGL attribution block; packs/jsp-936 absent (glob verified empty).
- **in_scope**: per-document OGL v3 vet of JSP 936 Part 1 on gov.uk before build; build packs/jsp-936 per docs/PACK-SPEC.md (SKILL.md, PACK.yaml, LICENSE with OGL text, chapters, glossary/cheatsheet as source allows); register every live gate surface: SKILLS.md, catalog.json, source-watchlist, packs/se Topics+agency+Licences rows, capability map/classification regenerate, NOTICE attribution, packs.html + per-pack landing page, plugin skill paths if required; update candidate-packs row 4 for the jsp-936 slug only; gates green on touched surfaces.
- **out_scope**: other JSPs and DEF-STANs; jsp-815/jsp-376 rework; paywalled clause reproduction; version bump; GitHub Release; frozen P8; CI/gate findings I1-I12 and P43-P47.
- **why_now**: only remaining ranked full-pack gap on the intake build order; research already named 936; prior JSP packs proved the registration path; full registration here keeps the UK licence/routing pattern proven before later UK packs compound a half-registered miss.
- **triage notes**: PASS, size L (prior jsp-815/jsp-376 runs proved the one-run pattern).
- **first_prompt**: `/superpowers-process full build jsp-936 Dependable AI in Defence pack under OGL and register it`

## P42 - fhwa-its-se-pack

- **id**: P42; **name**: fhwa-its-se-pack; **size**: L; **status**: ready; **corroboration**: 2 (value, risk); **deps**: none; **promoted_ids**: [b-32]
- **problem**: fhwa-its-se is the sole remaining named Proposed full pack that is tier 1 public domain, sector Civil infrastructure scored FULL, and still has no packs/ folder and no numbered build-order rank (backlog b-32, promoted into this package). Risk bite: building without a pinned primary FHWA/USDOT ITS SE source set invites construction-code or non-SE dumps; leaving b-32 unresolved keeps intake contradictory (FULL sector vs unranked candidate).
- **evidence**: docs/candidate-packs.md:L74 (fhwa-its-se tier 1 candidate), L51 (Civil infrastructure FULL row), L31 (unreached sectors list); docs/superpowers/backlog.md b-32 row (promoted into P42); packs/fhwa* absent (glob verified empty).
- **in_scope**: select and pin one FHWA/USDOT ITS systems-engineering primary source set; record the tier-1 public-domain licence statement in PACK.yaml/LICENSE; resolve the b-32 ranking inside the build (numbered build-order row and/or candidate-packs built mark); build packs/fhwa-its-se per PACK-SPEC; full registration (catalog.json, source-watchlist, SKILLS.md, /se routing, capability map/classification, NOTICE, landing pages/plugin paths as required); gates green on touched surfaces.
- **out_scope**: construction codes and non-SE FHWA dumps; FEMA-only packs; telecom-3gpp; UK defence JSPs; standalone ranking memo with no pack; CI/gate findings; version bump.
- **why_now**: last named tier-1 FULL sector with zero folder; source-pin and rank must land with the pack or wrong content and the intake contradiction compound; independent of the UK OGL line.
- **triage notes**: PASS, size L.
- **first_prompt**: `/superpowers-process full build fhwa-its-se pack and resolve its build-order rank`
