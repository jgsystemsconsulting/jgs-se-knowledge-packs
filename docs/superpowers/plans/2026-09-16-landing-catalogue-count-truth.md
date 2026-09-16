# Landing Catalogue Count Truth (P15) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Date:** 2026-09-16

**Goal:** Make landing section 06 and the catalogue still state live inventory as **63 packs · 2 signposts**, recount family chips (including OMB and a separate Signposts chip), and add fail-closed check 13 `[catalogue-count]` with a CI twin so those strings cannot drift from `packs/`.

**Architecture:** Live N/M come from filesystem inventory of `packs/*/SKILL.md` (signpost via frontmatter `kind: signpost`). Landing parse is scoped to the `<!-- §06 The catalogue -->` slice. Chip COUNTs sum to N with exactly one Signposts chip equal to M. SVG subtitle/footer carry the same N/M. Check 13 lives in `tooling/check_release.py`; CI inlines a stdlib twin; `test_ci_gate.py` pins shared regex literals and runs a negative demo; `test_catalogue_count.py` covers parsers with inline fixtures.

**Tech Stack:** Python 3 stdlib for gates/tests. Pillow (local only) to regenerate `still-catalogue.png` from the SVG text layout when no resvg/Inkscape is available. No new runtime dependency.

**Spec:** docs/superpowers/specs/2026-09-16-landing-catalogue-count-truth.md

**Research:** research: skipped (in-repo count honesty; no external API)

## Global Constraints

- Landing convention: pack = content; skill = anything installable. Headline is `63 packs · 2 signposts` (HTML: `&middot;`). Do not change `docs/packs.html` or `tooling/gen_packs_page.py`.
- Live counts always from filesystem; never hardcode N/M inside check 13.
- Signpost detection (local and CI twin): after opening `---`, a line matching `^kind:\s*signpost\s*$` (case-insensitive) marks a signpost.
- Chip COUNT is only the integer after the separator in `<b>LABEL · COUNT</b>`; digits in `<span>` are ignored.
- Exactly one chip whose `<b>` contains `signpost` (case-insensitive); its COUNT equals M; excluded from content sum.
- SVG family **row** counts are review-only (not pinned by check 13); at edit time they match the recount top five (NASA 16, DoD 19, NIST 09, FAA 07, GAO 04, zero-padded as today).
- PNG is review-only freshness; regenerate at 1200x675 and commit with the SVG.
- No version bump, CHANGELOG, plugin.json, RELEASE-INFO, or catalog.json edits (P16 owns catalog).
- Em-dash-free durable prose.
- Gates: `python tooling/test_catalogue_count.py`, `python tooling/test_ci_gate.py`, `python tooling/check_release.py`.

## Codebase context

- `docs/index.html:226` h2 still says 54; chips 228-235 sum to 54; figcaption 241 says Fifty-four; no OMB chip; EU chip still folds signposts into its description.
- `docs/assets/still-catalogue.svg` subtitle line 12 and footer line 24 still say 54; rows still 15/13/09/06/04.
- `tooling/check_release.py` checks numbered through 12 (`[html-assets]` / `[brand-tokens]`); module docstring CI-covered line needs check 13.
- `.github/workflows/validate.yml` coverage map ends at HTML self-containment; new twin step after that step.
- `tooling/test_ci_gate.py` uses `PINNED_STEPS`, `RELEASE_PAIR` / `HTML_ASSET_PAIR`, extract-and-run heredocs, negative demos, positive real-tree runs.
- Live recount verified 2026-09-16: NASA 16, DoD/DAU/OSD 19, NIST 9, FAA 7, GAO 4, DOE 2, CISA/DHS 1, OMB/cross-federal 1, EU/academic/JGS 4, Signposts 2. Sum content 63.

---

### Task 1: Recount landing §06 in docs/index.html

**Files:**
- Modify: `docs/index.html` (section 06 only: h2, packs chips, FIG.06 figcaption)

**Model:** flash

- [ ] **Step 1: Rewrite h2**

Replace line 226 with:

```html
    <h2>63 packs &middot; 2 signposts</h2></div>
```

- [ ] **Step 2: Rewrite family chips from live slug lists**

Replace the eight chips with nine content families plus Signposts. Markup shape stays `<div class="pk"><b>LABEL &middot; COUNT</b><span>description</span></div>`. Verified counts and description seeds (implementer may tighten wording; COUNTs must match):

| Label | COUNT | Description seed (content only) |
|---|---|---|
| NASA | 16 | SE Handbook & Expanded Guidance, NPR 7123 / 7150, risk, system safety, fault management, HSI, PRA, R&M, schedule, cost, digital engineering, systems modeling, M&S 7009, STD 8719 |
| DoD / DAU / OSD | 19 | SE Guidebook, MIL-STD-882E, DoDAF, MOSA, RIO, digital engineering, M&Q BoK, T&E, V&V RPG, MIL-HDBK-61 CM, MRL Deskbook, SD-22 DMSMS, MIL-HDBK-338B, MIL-HDBK-516C, MIL-STD-40051, MIL-STD-881F, DAFMAN 63-119, DOT&E T&E, IS-GPS-200N |
| NIST | 9 | AI RMF, SSDF, CSF 2.0, SP 800-160 SSE, SP 800-37 RMF, Cyber-Physical Systems, NIST/SEMATECH statistics, SP 800-171 CUI, SP 800-61 incident response |
| FAA | 7 | RMA Handbook, Systems Engineering Manual, System Safety, Human Factors Design Std, AMS V&V, Requirements Engineering Management, STD-025 |
| GAO | 4 | Technology Readiness, Cost Estimating, Schedule Assessment, Agile Assessment guides |
| DOE | 2 | Systems Engineering Methodology (SEM3), capital-asset project management (O 413.3) |
| CISA / DHS | 1 | Cross-Sector Cybersecurity Performance Goals 2.0 |
| OMB / cross-federal | 1 | Federal benefit-cost analysis (OMB) |
| EU / academic / JGS | 4 | EU AI Act 2024/1689, Digital Systems Engineering (arXiv), EARS requirements-writing, SEBoK |
| Signposts | 2 | OMG and SE-standards download pointers (not content packs) |

Remove the old EU chip text that said "plus OMG & SE-standards signposts".

- [ ] **Step 3: Rewrite figcaption**

```html
    <figcaption>FIG.06 · Sixty-three packs plus two signposts across open sources; filter the full list on packs.html.</figcaption>
```

- [ ] **Step 4: Spot-check slice**

```bash
python - <<'PY'
from pathlib import Path
import re
t = Path('docs/index.html').read_text(encoding='utf-8')
assert '<!-- §06 The catalogue -->' in t
assert '63 packs &middot; 2 signposts' in t
assert 'Sixty-three packs plus two signposts' in t
assert 'OMB / cross-federal' in t
assert re.search(r'Signposts\s*&middot;\s*2|Signposts\s*·\s*2', t)
assert 'plus OMG' not in t
print('index §06 OK')
PY
```

---

### Task 2: Update still-catalogue.svg and regenerate PNG

**Files:**
- Modify: `docs/assets/still-catalogue.svg`
- Modify: `docs/assets/still-catalogue.png`

**Model:** standard

- [ ] **Step 1: Edit SVG text**

- Subtitle (line 12): `63 packs  ·  2 signposts  ·  open sources only` (keep double-space style).
- Family rows (top five only, existing design): NASA 16, DoD / DAU / OSD 19, NIST 09, FAA 07, GAO 04.
- Footer (line 24): `63 PACKS · 2 SIGNPOSTS · FILTER ON packs.html`.

- [ ] **Step 2: Regenerate PNG at 1200x675**

Prefer resvg/Inkscape/headless Chromium if present. Otherwise Pillow draw matching layout (ink ground `#0a0a0b`, paper spine `#f4f2ec`, mono labels) and write `docs/assets/still-catalogue.png`.

```bash
python -c "from PIL import Image; im=Image.open('docs/assets/still-catalogue.png'); print(im.size, im.mode); assert im.size==(1200,675)"
```

- [ ] **Step 3: Confirm SVG strings**

```bash
rg -n "63 packs|63 PACKS|16|19|09|07|04" docs/assets/still-catalogue.svg
```

---

### Task 3: check_release check 13 [catalogue-count]

**Files:**
- Modify: `tooling/check_release.py` (module docstring numbering + CI-covered line; helpers + main body after brand-tokens)

**Model:** deep

- [ ] **Step 1: Docstring**

Add check 13 description after check 12. Extend CI-covered line to include catalogue-count / check 13.

- [ ] **Step 2: Shared inventory + parse helpers (module level)**

Implement stdlib helpers used by main and by `test_catalogue_count.py`:

- `SIGNPOST_KIND_RE = re.compile(r"^kind:\s*signpost\s*$", re.I | re.M)` (same literal already in RELEASE_PAIR).
- Inventory: every immediate child dir of `packs/` must have `SKILL.md` with YAML frontmatter between `---` fences; missing or unparseable fails. Classify content vs signpost via SIGNPOST_KIND_RE on the frontmatter body. Return `(N, M)` or collect fail messages.
- Section slice: from `<!-- §06 The catalogue -->` to next `<!-- §` comment (or EOF).
- H2: match `<N> packs <sep> <M> signposts` with sep `&middot;` or middle dot `·`.
- Chips: for each `<div class="pk">...</div>` in slice, parse `<b>...sep COUNT</b>`; if label contains `signpost` (case-insensitive) it is the signpost chip (exactly one required, COUNT == M); else add COUNT to content sum (must equal N).
- Figcaption: require digits N and M, or the prescribed caption after whitespace normalize: `FIG.06 · Sixty-three packs plus two signposts across open sources; filter the full list on packs.html.`
- SVG: subtitle and footer of `docs/assets/still-catalogue.svg` must carry N and M (case-insensitive on words packs/signposts; digits exact). Do not pin family row counts.

Pin-worthy regex/string literals that must also appear in the CI twin (for `test_ci_gate.py`):

- Section marker: `"<!-- §06 The catalogue -->"`
- H2 pattern text (entity-aware)
- Chip `class="pk"` / `<b>` COUNT pattern
- SVG path `"docs/assets/still-catalogue.svg"` or equivalent open path string
- Failure tag substring `"[catalogue-count]"`

- [ ] **Step 3: Wire into main()**

After brand-tokens block, run check 13. On any mismatch include live versus stated numbers in the message. Tag every failure `[catalogue-count]`.

- [ ] **Step 4: Smoke**

```bash
python tooling/check_release.py
# expect PASS and no [catalogue-count] failures once Tasks 1-2 done
```

---

### Task 4: CI twin in validate.yml

**Files:**
- Modify: `.github/workflows/validate.yml` (header coverage map + new step)

**Model:** standard

- [ ] **Step 1: Coverage map line**

After the HTML self-containment map line, add:

```text
#   Landing catalogue counts                    twins check_release 13 [catalogue-count]
```

- [ ] **Step 2: New step after HTML self-containment**

Step name exactly `Landing catalogue counts`. Inline `python3 - <<'PY'` stdlib only; never import or exec repo code. Recompute live N/M from `packs/*/SKILL.md`, slice index.html §06, parse h2/chips/figcaption, parse SVG subtitle/footer, same equality rules as check 13. Print `::error::[catalogue-count] ...` on failure; exit 1 if any fail.

Shared literals with check_release must match byte-for-byte for pins in Task 5.

---

### Task 5: test_ci_gate pins + test_catalogue_count.py

**Files:**
- Modify: `tooling/test_ci_gate.py`
- Create: `tooling/test_catalogue_count.py`

**Model:** standard

- [ ] **Step 1: Extend test_ci_gate.py**

- Add `"Landing catalogue counts"` to `PINNED_STEPS`.
- Add catalogue-count parity pairs (section marker, h2 regex text, chip pattern, SVG-related literal, `[catalogue-count]` tag as needed) to a `CATALOGUE_COUNT_PAIR` list checked against both `check_release.py` and `validate.yml`.
- Update docstring counts ("five" -> "six" pinned steps where stated).
- Negative demo: fixture tree with live 1 content + 0 signpost packs but index h2 saying `62 packs` (or any wrong N) fails with `[catalogue-count]` and live-versus-stated wording.
- Positive run against real tree for the new step.

- [ ] **Step 2: Create test_catalogue_count.py**

Assert-based (no pytest fixtures). Cover:

- h2 extraction entity-aware (`&middot;` and `·`)
- chip summing and signpost-chip exclusion
- exactly-one signpost chip rule
- SVG subtitle and footer extraction
- frontmatter signpost detection

Import helpers from `check_release` after `sys.path` insert. Print OK line; `raise SystemExit(main())`.

- [ ] **Step 3: Run probes**

```bash
python tooling/test_catalogue_count.py
python tooling/test_ci_gate.py
```

---

### Task 6: Gates, negative demo, package status

**Files:**
- Modify: `docs/superpowers/packages/2026-09-16-jgs-se-knowledge-packs-packages.md` (P15 status -> done when EXECUTED exists)
- Create: `docs/superpowers/plans/2026-09-16-landing-catalogue-count-truth-EXECUTED.md`
- Create: `docs/superpowers/plans/2026-09-16-landing-catalogue-count-truth-ivl-triage-log.md`

**Model:** flash

- [ ] **Step 1: Full green**

```bash
python tooling/test_catalogue_count.py
python tooling/test_ci_gate.py
python tooling/check_release.py
```

- [ ] **Step 2: Negative demo then restore**

Temporarily change §06 h2 to `62 packs &middot; 2 signposts`, run check_release, confirm FAIL with `[catalogue-count]` naming live vs stated, restore h2, confirm PASS.

- [ ] **Step 3: Confirm packs.html untouched**

```bash
git diff --stat -- docs/packs.html catalog.json
# expect empty
```

- [ ] **Step 4: Mark package done + EXECUTED + IVL log**

- packages doc P15 `status: done`
- EXECUTED.md one line: `done`
- IVL triage log Track 1 or Track 3 clean after verifying gates

- [ ] **Step 5: Commit**

Clear messages covering HTML/still, gate+CI+tests, and docs/status as needed.

## Out of scope (do not touch)

- `docs/packs.html`, `tooling/gen_packs_page.py` (beyond still asset if shared; it is not)
- `catalog.json` / P16
- Version bump, CHANGELOG, plugin.json, RELEASE-INFO
- P8 ledger, P9-P14 reopen

## Success criteria (from spec)

- §06 headline, chips (OMB + Signposts), figcaption, SVG subtitle/footer all state 63 packs and 2 signposts; SVG top-five rows match recount; PNG matches SVG layout; packs.html byte-identical.
- `python tooling/check_release.py` PASS with `[catalogue-count]` in the gate surface (no failure lines).
- `validate.yml` twin step present; coverage map names check 13.
- Negative demo h2 62 packs fails then restore PASS.
- `test_catalogue_count.py` and `test_ci_gate.py` pass.
