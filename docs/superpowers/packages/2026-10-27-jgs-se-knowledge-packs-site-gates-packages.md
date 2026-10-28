---
date: 2026-10-27
project: jgs-se-knowledge-packs-site-gates
mode: full
rounds: 1
input_digest: 1f2c19f170cd294bdff490d13a4aa27c0ed79d485faeef2fa347b97e17c76207
open_objections: ["X5"]
---

Picked 2026-10-27 (user: run all four cuts to completion). X5 default: ATTR grain stays OUT of P46 (value+risk reading; b-39 carries the grain).

# Work packages - jgs-se-knowledge-packs-site-gates (2026-10-27, full scoped re-run)

Scope of this cut: the per-pack landing-page gate family and the ship runbooks.
I5 html-assets pack-page glob (with prior P46 ATTR grain per fork X5), I6+I7
gen_pack_pages sitemap/REV/probe, I11+I12 contributor/release runbooks. Converged in
one round (value 4, risk 4, cohesion 3 candidates; merge produced 4 packages; triage
zero_critical). Open fork X5 travels in `open_objections`.

## P46 - html-assets-pack-pages

- **id**: P46; **name**: html-assets-pack-pages; **size**: M; **status**: done; **corroboration**: 3 (value, risk, cohesion); **deps**: none; **promoted_ids**: [html-self-contain-scan-1]
- **problem**: The HTML self-containment gate triple (validate.yml CI heredoc, check_release check 12, test_html_assets real-page pass) enumerates only non-recursive docs/*.html, so the 71 tracked docs/packs/\<slug\>/index.html landing pages never enter the scanned set: an external CDN script or image on any pack page stays green in CI and locally (finding I5, HIGH). The shared twin files also carry the prior P46 ATTR suffix over-match grain; whether it is absorbed here is open fork X5.
- **evidence**: tooling/check_release.py:L1099-1107 (docs-level glob only, not rglob); validate.yml html-assets step (`pages = sorted(pathlib.Path("docs").glob("*.html"))`); tooling/test_html_assets.py:L132-137 (same glob); tooling/check_release.py:L157-160 and test_ci_gate.py ATTR pins (X5 grain).
- **in_scope**: widen html-assets page discovery so docs/packs/\<slug\>/index.html pages are scanned in all three places, still excluding docs/superpowers and other gitignored planning trees; keep page-set parity across the triple; update test_ci_gate pins if the discovery literal is pinned. X5 positions recorded: cohesion absorbs the ATTR name-boundary fix here (promoting html-self-contain-scan-1); value and risk scope ATTR out (fail-closed over-match judged safer than a silent external miss). Spec phase applies the human's X5 pick.
- **out_scope**: sitemap/REV checks (P51); generator probe (P52); runbooks (P53); CI licence/signpost/checkout gates; pack HTML content edits; version bump.
- **why_now**: HIGH production lie on the bulk of the new docs surface; every new pack page multiplies unscanned surface. Must land before P52 freezes the correct page set.
- **triage notes**: PASS, size M. X5 is separable: the glob fix completes under either resolution, and the ATTR side is one bounded regex edit plus two byte-identical pin updates in files this package already touches.
- **first_prompt**: `/superpowers-process full widen html-assets gate to per-pack landing pages`

## P51 - gen-pack-pages-sitemap-rev

- **id**: P51; **name**: gen-pack-pages-sitemap-rev; **size**: M; **status**: done; **corroboration**: 3 (value, risk, cohesion); **deps**: none; **promoted_ids**: []
- **problem**: tooling/gen_pack_pages.py always calls write_sitemap(slugs) with the current run's slug list, so --only rebuilds docs/sitemap.xml down to the named packs, and generated page comments teach exactly that path; nothing compares sitemap locs to the live catalog set. Pack pages embed REV from version() at generate time while the [site-version] CI check asserts docs/index.html only (finding I6, HIGH). One partial regen truncates the sitemap or leaves stale REV with CI green.
- **evidence**: tooling/gen_pack_pages.py:L262-293 (write_sitemap from run slugs; --only argument); docs/packs/jsp-376/index.html:L7 ("Regenerate with: python tooling/gen_pack_pages.py --only jsp-376"); validate.yml [site-version] step.
- **in_scope**: stop --only (any partial slug list) from rewriting the sitemap below the live catalog set (full-catalog write or refuse on partial); gate sitemap locs against the live catalog; assert pack-page REV against RELEASE-INFO so drift fails closed; fix generated regen comments.
- **out_scope**: html-assets glob (P46); dedicated probe harness (P52); packs.html rewrite; CI running generators; version bump.
- **why_now**: HIGH silent wipe of tracked release artifacts on a normal maintainer path, documented on live pages.
- **triage notes**: PASS, size M.
- **first_prompt**: `/superpowers-process full make gen_pack_pages sitemap and pack-page REV drift-proof`

## P52 - gen-pack-pages-probe

- **id**: P52; **name**: gen-pack-pages-probe; **size**: M; **status**: done; **corroboration**: 2 (value, risk); **deps**: [P46, P51]; **promoted_ids**: []
- **problem**: The per-pack page generator is new release surface (f99a0ea, e84ad2f, title-suffix fix 20ba23a) but tooling/ has no test_gen_pack_pages.py while sibling generators and gates have assert probes, and CI never runs generators (finding I7, MEDIUM). Without a probe, the P46 and P51 fixes rot on the next generator edit.
- **evidence**: tooling test inventory (11 test_*.py, none for gen_pack_pages); commit 20ba23a (title-suffix collision already bit once).
- **in_scope**: add tooling/test_gen_pack_pages.py covering title-suffix non-collision, --only must not truncate the sitemap, pack-page REV vs version source, and pack HTML staying inside the html-assets scan set; wire into the local pre-tag verification story.
- **out_scope**: implementing P46/P51 fixes themselves; generators in CI; Playwright suite (b-18 row).
- **why_now**: locks the I5/I6 payoff; the prior title-suffix bite proves the class ships bugs without a probe.
- **triage notes**: PASS, size M; deps satisfied by order.
- **first_prompt**: `/superpowers-process full add test_gen_pack_pages regression probe`

## P53 - site-release-runbooks

- **id**: P53; **name**: site-release-runbooks; **size**: M; **status**: done; **corroboration**: 3 (value, risk, cohesion); **deps**: none; **promoted_ids**: []
- **problem**: Contributor and release guidance are one doc data-flow with two holes: CONTRIBUTING's registration step points at a nonexistent tooling/ catalog writer and omits the live surfaces a pack must touch (SKILLS.md, /se map, watchlist, capability-map inputs, packs.html, per-pack pages, plugin skill lists) while PR guidance names only validate_pack (finding I11); and the ship path never mentions check_release while the CI-green-is-not-release-ready warning lives only in a validate.yml comment and a deep SOURCE-FRESHNESS paragraph (finding I12). Tagging from green CI alone can publish while local-only gates never ran.
- **evidence**: CONTRIBUTING.md:L45-54 (dead "see tooling/" pointer), L70 ("CI does not run `validate_pack.py`."); validate.yml header coverage-map warning; docs/SOURCE-FRESHNESS.md:L51-55 (source-watch check 18 local only).
- **in_scope**: complete the live-pack registration checklist for real surfaces; make the pre-tag `python tooling/check_release.py` requirement discoverable in CONTRIBUTING and/or a short docs release runbook; kill the dead catalog-writer pointer; align PR guidance with surfaces CI already enforces.
- **out_scope**: implementing the missing catalog writer tool; moving local-only gates into CI; PACK-SPEC install section (P54 in the doc-truth cut); version bump; frozen P8.
- **why_now**: the release bite is live (branch ahead of main, tag risk); registration friction multiplies wrong-surface PRs into the same blind ship path.
- **triage notes**: PASS, size M. Doc-only, independent of gate code fixes.
- **first_prompt**: `/superpowers-process full rewrite contributor registration and release runbooks`
