# Cursor plugin SSOT gates Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Put `.cursor-plugin/plugin.json` version into the release single-source and add a pure-data CI twin of check 6b that fails closed when the Cursor skills array does not match the commercially eligible pack set.

**Architecture:** Three independent edits, one commit surface. The version dict in `tooling/check_release.py` and the matching heredoc in `.github/workflows/validate.yml` both gain a `cursor-plugin.json` key. A new workflow step, `Cursor skills eligible set`, sits between `SKILLS index count` and `Chapter basename overlap` and reimplements check 6b with stdlib only, fail-closed on a missing file. `tooling/test_ci_gate.py` grows one pinned step name, one fixture file, and two negative demos so the probe runs the shipped text.

**Tech Stack:** Python 3 stdlib (`json`, `re`, `os`, `pathlib`, `sys`). No new dependency. No import of `validate_pack`, `check_release`, or any other repository module from a workflow step.

**Spec:** `docs/superpowers/specs/2026-10-28-cursor-plugin-ssot-gates.md`

Spec certificate sha256: `58e571a41e5f68ad74e6a02be43cfa077c557b9e8ff62222a28ccb09b719f6ae`.

## Global Constraints

- D1: `.cursor-plugin/plugin.json` `version` moves from `1.22.0` to `1.23.0`. That is the only version edit. Do not bump `RELEASE-INFO.txt`, `.claude-plugin/plugin.json`, either website YAML, `docs/index.html`, or pack-page REV.
- D2: `tooling/check_release.py` check 4 gains dict key `cursor-plugin.json`, read from `.cursor-plugin/plugin.json` via `.get("version", "")` inside a try/except shaped like the existing `plugin.json` read. On exception, call `fail()` and do not assign the key. The existing `"" in versions.values()` arm then does not fire for a missing file. The existing `len(distinct) > 1` arm is the disagreement path.
- D3: The `Version single-source` heredoc (`.github/workflows/validate.yml`, step at line 1173, body through line 1329) gains the same key, same path, same try/except, byte-compatible with how `test_ci_gate.py` extracts heredocs. On read failure print `::error::[version] cannot read cursor-plugin.json: {e}`, set `versions["cursor-plugin.json"]` to `""`, and let the existing `fails += 1` on disagreement fire. Do not `sys.exit` inside the except. Do not touch the sitemap block or the pack-rev block inside that heredoc.
- D4: `VERSION_BASE` in `tooling/test_ci_gate.py` (lines 232-238) gains `".cursor-plugin/plugin.json": '{"version": "1.2.3"}\n'`, matching the claude fixture, not the 1.2.4 RELEASE-INFO fixture. The existing disagreement demo at line 482 keeps failing on RELEASE-INFO 1.2.4. Add one negative demo: copy `VERSION_BASE`, set the cursor file to `{"version": "9.9.9"}\n`, set `RELEASE-INFO.txt` to `Version:    1.2.3\n` so the other files agree, expect non-zero and `[version]`. Follow the `v2 = dict(VERSION_BASE)` pattern at line 485. Do not add a demo framework.
- D5: Check 6b moves into CI as a new step named `Cursor skills eligible set`, placed immediately after `SKILLS index count` and before `Chapter basename overlap`. Pure data. Stdlib `json`, `re`, `pathlib` only. No import of `validate_pack`, `check_release`, or any other repository module. A pack is excluded when `packs/<slug>/PACK.yaml` contains the substring `commercial_use: false`. Slug parse stays `packs/<slug>/` via `re.search`. Missing file, bad JSON, or `skills` not a list fails closed with `[cursor]`. That is the CI difference from check 6b, which silent-passes a missing file. Do not change check 6b's missing-file skip.
- D6: `PINNED_STEPS` (lines 61-72) gains an eleventh name, `"Cursor skills eligible set"`, inserted after `"SKILLS index count"` and before `"Chapter basename overlap"`, matching workflow order. The assertion string `expected exactly ten pinned heredocs` (line 463) becomes `expected exactly eleven pinned heredocs`. Module docstring counts move: `ten inline CI gates` (line 4) and `ten pinned steps` (line 17) become eleven. No other assertion string changes.
- D7: One skills negative demo, same `demo()` helper. Tiny tree: `packs/alpha/SKILL.md`, `packs/alpha/PACK.yaml` containing `commercial_use: true`, `packs/beta/SKILL.md`, `packs/beta/PACK.yaml` containing `commercial_use: false`, `.cursor-plugin/plugin.json` whose `skills` lists only `./packs/beta/SKILL.md`. Expect non-zero and `[cursor]`. Do not assert the full missing/extra wording.
- D8: One sentence in `CONTRIBUTING.md` under `## Before you tag`, after the sentence `CI green necessary but not sufficient.` State that `.cursor-plugin/plugin.json` version is in the single-source with the claude manifest, `RELEASE-INFO.txt`, and `CHANGELOG.md`, and that CI also checks the Cursor skills array against packs whose `PACK.yaml` does not contain `commercial_use: false`. Do not rewrite the section.
- D9: One `### Changed` bullet under `## [Unreleased]` in `CHANGELOG.md`. Do not add an `## [x.y.z]` heading. Do not edit `## [1.23.0]` or its Noted bullet, including the stale 79.
- D10: Pack count stays 74. Skill count stays 83. `catalog.json` `updated` stays `2026-10-14`. Cursor skills length stays 80. `easa-rules`, `med-device-eu`, and `sebok` stay absent from the Cursor skills array. No release bump. No tag. No push. No commit unless the parent execution mode says commit. No other `validate.yml` step edited.
- Regex literals already required to appear in both `tooling/check_release.py` and `validate.yml` stay byte-identical. Do not rewrap them. The new cursor read is not in `RELEASE_PAIR`. Do not add it there.
- Do not import `validate_pack` or any repository module from a workflow step (b-38).
- Do not add the three `commercial_use: false` packs to the Cursor manifest. Exclusion is the product rule.
- Do not close backlog rows. `b-38` stays.
- Per-task briefs live at `.superpowers/sdd/2026-10-28-cursor-plugin-ssot-gates/task-N-brief.md`. The controller writes them at dispatch. This plan does not create those files.

## Codebase context

Post-P59 baseline, re-checked on main at `44e8df5` on 2026-10-28.

- `.cursor-plugin/plugin.json` today: `version` is `1.22.0` (line 5). `skills` is a list of 80 strings shaped `./packs/<slug>/SKILL.md`. Last entry is `./packs/se-standards-signpost/SKILL.md`. Keys, in order: `name`, `displayName`, `description`, `version`, `author`, `homepage`, `repository`, `license`, `keywords`, `category`, `tags`, `skills`. `.claude-plugin/plugin.json` is already `1.23.0` with 83 skills. The three-skill gap is the three `commercial_use: false` packs (`easa-rules`, `med-device-eu`, `sebok`). They stay out.
- `tooling/check_release.py` check 4 (lines 1164-1216) builds `versions` with three keys: `plugin.json` (try/except, `fail()` on exception, key not assigned), `CHANGELOG.md`, `RELEASE-INFO.txt`. Website YAML versions are compared to `RELEASE-INFO.txt` but are not dict keys. Agreement is `distinct = {v for v in versions.values() if v}` then `if len(distinct) > 1 or "" in versions.values()`. The cursor key joins that dict. It does not join the website-YAML loop.
- Check 6b (lines 1363-1407) is the MA-01 backstop. If `.cursor-plugin/plugin.json` exists, parse JSON, require `skills` to be a list, collect slugs from `packs/<slug>/` path segments, subtract packs whose `PACK.yaml` contains `commercial_use: false`, fail `[cursor]` when the slug sets differ. A missing file is a silent pass. CI has no twin today. Eligible count today is 80. Cursor count today is 80. After the version field moves to `1.23.0` the local gate passes both checks. Before that bump it fails `[version]`. That failure is the point of D1. Do not weaken the comparison.
- `.github/workflows/validate.yml` `Version single-source` (line 1173, heredoc body lines 1176-1329) uses `open()` relative paths, not `ROOT /`. The claude read (lines 1182-1187) prints `::error::[version] cannot read plugin.json: {e}` and sets the key to `""`. The cursor read copies that shape. Disagreement print is line 1326: `::error::[version] disagreement / missing: {versions}`. Sitemap and pack-rev blocks inside this heredoc stay untouched.
- `SKILLS index count` ends at line 1352 (`PY`). `Chapter basename overlap` starts at line 1354. The new step goes between those two lines. Header coverage map (lines 16-26) gains one row for the new step. Nothing else in that header moves.
- `tooling/test_ci_gate.py` extracts each pinned step's heredoc and runs the shipped text. `PINNED_STEPS` (lines 61-72) is ten names, in workflow order. `extract_heredoc` finds `- name: <step>`, then the `python3 - <<'PY'` body, and stops at a line whose strip equals `PY`. A new step with that marker shape is extracted with no extractor edit. Positive runs (lines 1027-1032) loop `PINNED_STEPS` against `ROOT` and require exit 0. The new step must exit 0 on the live tree, which it will: both sets are 80.
- `VERSION_BASE` (lines 232-238) is a five-file dict. Only the version-step negative demos use it. The disagreement demo (line 482) writes it as-is and expects `[version]`. Adding a sixth file at `1.2.3` keeps that demo failing, because `RELEASE-INFO.txt` stays `1.2.4`. No existing demo constructs a cursor file. No existing demo asserts a five-file dict length.
- `demo()` (lines 468-473) writes a tiny tree, runs one extracted heredoc, asserts non-zero exit and a substring in the output. `demo_ok()` asserts exit 0. Both take `files`, `step`, and `label`. The D7 demo uses `demo()`. No new helper.
- `CHANGELOG.md` `## [Unreleased]` already has `### Added` (line 14) and `### Changed` (line 18). The new bullet goes under the existing `### Changed`, after the `faa-ams-vv` bullet (line 21). Do not add a heading.
- `CONTRIBUTING.md` line 119 is `CI green necessary but not sufficient.` The D8 sentence follows it. Do not rewrite lines 117, 121, or 123.
- Counts that must not move: pack count 74, skill count 83, `catalog.json` `updated` `2026-10-14`, Cursor skills length 80.

## Research

research: skipped

No world claim. The spec is a wiring change against files in this repo. Line numbers and fixture shapes above were re-read on main at `44e8df5` on 2026-10-28. The certificate hash was recomputed and matches.

## File map

Modify:

- `.cursor-plugin/plugin.json` (the `version` string only)
- `tooling/check_release.py` (check 4 dict, one key; docstring coverage line)
- `.github/workflows/validate.yml` (version heredoc, one new step, coverage-map row)
- `tooling/test_ci_gate.py` (`PINNED_STEPS`, `VERSION_BASE`, two demos, three count strings)
- `CONTRIBUTING.md` (one sentence)
- `CHANGELOG.md` (one bullet)

Do not modify: `RELEASE-INFO.txt`, `.claude-plugin/plugin.json`, `catalog.json`, `docs/index.html`, `docs/products/website/`, `docs/packs/`, `packs/`, `docs/superpowers/backlog.md`, `## [1.23.0]` in `CHANGELOG.md`.

---

### Task 1: Cursor version into the local single-source

**Gate:** gate-enforced (spec D1, D2).

**Files:**
- Modify: `.cursor-plugin/plugin.json` (line 5, the version string)
- Modify: `tooling/check_release.py:1164-1216` (check 4 dict)
- Modify: `tooling/check_release.py:74-76` (docstring CI-covered list)

**Interfaces:**
- Consumes: nothing from an earlier task.
- Produces: `versions["cursor-plugin.json"]` set from `.cursor-plugin/plugin.json` `.get("version", "")` on the success path. On exception the key is absent and `fail()` has been called. Task 2's heredoc copies this key name and this path. Task 3 does not read this function.

**Model:** flash

Per-task brief: `.superpowers/sdd/2026-10-28-cursor-plugin-ssot-gates/task-1-brief.md`

- [ ] **Step 1: Confirm the field is stale, then bump it**

```bash
python -c "import json; print(json.load(open('.cursor-plugin/plugin.json', encoding='utf-8'))['version'])"
```

Expected: `1.22.0`. If it already prints `1.23.0`, stop and report. Do not edit a file that has already moved.

Edit `.cursor-plugin/plugin.json` line 5. Replace the version string only.

```json
  "version": "1.23.0",
```

Do not touch `skills`, `name`, or any other key. Do not reformat the file.

- [ ] **Step 2: Add the cursor key to check 4**

In `tooling/check_release.py`, immediately after the `plugin.json` try/except (the block that ends `fail(errs, f"[version] cannot read plugin.json: {e}")`, line 1169) and before the `CHANGELOG.md` read (line 1170), insert this block. Same shape. Key name is `cursor-plugin.json`, not `plugin.json`. On exception call `fail()` and do not assign the key.

```python
    try:
        versions["cursor-plugin.json"] = json.loads(
            (ROOT / ".cursor-plugin/plugin.json").read_text(encoding="utf-8")
        ).get("version", "")
    except Exception as e:
        fail(errs, f"[version] cannot read cursor-plugin.json: {e}")
```

Leave the `distinct` comparison (lines 1214-1216) as it is. The new key rides the existing agreement check. Do not add a special case.

In the module docstring, the CI-covered sentence (line 74) lists the checks CI twins. Add `cursor skills` to that list so the docstring does not claim CI has no cursor twin after Task 2 lands. Exact replacement of the sentence that starts `CI-covered:`:

```text
CI-covered: version (including .cursor-plugin/plugin.json), index, cursor skills, overlap, map/rules data invariants, html-assets,
```

Keep the rest of that sentence. Do not rewrite the numbered check list above it. Check 6b's missing-file skip stays.

- [ ] **Step 3: Run the local gate**

```bash
python tooling/check_release.py
```

Expected: exit 0. PASS line contains `v1.23.0`. If it fails `[version]`, the cursor field did not land at `1.23.0` or the new key read the wrong path. Fix that. Do not weaken the comparison.

- [ ] **Step 4: Confirm frozen surfaces did not move**

```bash
python -c "
import json, pathlib
cur = json.load(open('.cursor-plugin/plugin.json', encoding='utf-8'))
assert cur['version'] == '1.23.0', cur['version']
assert len(cur['skills']) == 80, len(cur['skills'])
joined = '\n'.join(cur['skills'])
for slug in ('easa-rules', 'med-device-eu', 'sebok'):
    assert slug not in joined, slug
cat = json.load(open('catalog.json', encoding='utf-8'))
assert cat['updated'] == '2026-10-14', cat['updated']
print('cursor version 1.23.0, skills 80, excluded three still out, catalog updated frozen')
"
```

Expected: the print line, exit 0.

---

### Task 2: CI version key and the Cursor skills step

**Gate:** gate-enforced (spec D3, D5, D10).

**Files:**
- Modify: `.github/workflows/validate.yml:16-26` (coverage map)
- Modify: `.github/workflows/validate.yml:1182-1187` (version heredoc, cursor read inserted after the claude read)
- Modify: `.github/workflows/validate.yml:1352-1354` (new step between `PY` of SKILLS index count and `Chapter basename overlap`)

**Interfaces:**
- Consumes: the key name `cursor-plugin.json` and the path `.cursor-plugin/plugin.json` from Task 1. Does not import Task 1's function.
- Produces: a workflow step whose `- name:` value is exactly `Cursor skills eligible set`, with a `python3 - <<'PY'` heredoc terminated by a line whose strip is `PY`. Task 3's `PINNED_STEPS` entry must match that name byte for byte, and `extract_heredoc` depends on the `PY` terminator.

**Model:** standard

Per-task brief: `.superpowers/sdd/2026-10-28-cursor-plugin-ssot-gates/task-2-brief.md`

- [ ] **Step 1: Add the cursor read inside the version heredoc**

In `.github/workflows/validate.yml`, inside the `Version single-source` step, immediately after the claude except block (the line `versions["plugin.json"] = ""`, line 1187) and before the `CHANGELOG.md` read (line 1188), insert this block. Indentation matches the heredoc body (14 spaces). On failure set the key to `""`. Do not call `sys.exit` here.

```python
          try:
              with open(".cursor-plugin/plugin.json", encoding="utf-8") as fh:
                  versions["cursor-plugin.json"] = json.load(fh).get("version", "")
          except Exception as e:
              print(f"::error::[version] cannot read cursor-plugin.json: {e}")
              versions["cursor-plugin.json"] = ""
```

Do not edit the sitemap block, the pack-rev block, the three version regexes, or the disagreement print at line 1326. The new key rides that print.

- [ ] **Step 2: Add the coverage-map row**

In the workflow header coverage map, after the `SKILLS index count` row (line 17) and before the `Chapter basename overlap` row (line 18), add one row:

```text
#   Cursor skills eligible set                 twins check_release 6b (fail-closed on missing file; local silent-pass stays)
```

Do not edit any other coverage row. Do not edit the "CI does not cover" paragraph except to leave it alone: it does not name check 6b, so it stays true.

- [ ] **Step 3: Insert the Cursor skills step**

Between the `PY` that closes `SKILLS index count` (line 1352) and `- name: Chapter basename overlap` (line 1354), insert this step. The `- name:` value is the extraction key. Do not import a repository module. Do not call `validate_pack`. Eligibility is the substring test, the same one check 6b uses.

```yaml
      - name: Cursor skills eligible set
        run: |
          python3 - <<'PY'
          # Twins tooling/check_release.py check 6b. Stdlib only. Does not import
          # repository code (b-38). Differs from the local gate in one place:
          # a missing .cursor-plugin/plugin.json fails closed here. Local check
          # 6b silent-passes a missing file. Do not copy that skip into CI.
          import json, re, sys, pathlib
          root = pathlib.Path(".")
          cursor_path = root / ".cursor-plugin" / "plugin.json"
          if not cursor_path.is_file():
              print("::error::[cursor] missing .cursor-plugin/plugin.json")
              sys.exit(1)
          try:
              cursor = json.loads(cursor_path.read_text(encoding="utf-8"))
          except Exception as e:
              print(f"::error::[cursor] cannot read .cursor-plugin/plugin.json: {e}")
              sys.exit(1)
          skills_list = cursor.get("skills") if isinstance(cursor, dict) else None
          if not isinstance(skills_list, list):
              print("::error::[cursor] .cursor-plugin/plugin.json missing skills array")
              sys.exit(1)
          all_skill_dirs = sorted(p.parent for p in root.glob("packs/*/SKILL.md"))
          nc_packs = {
              p.name for p in all_skill_dirs
              if (p / "PACK.yaml").is_file()
              and "commercial_use: false" in (p / "PACK.yaml").read_text(
                  encoding="utf-8", errors="ignore"
              )
          }
          pack_slugs = {p.name for p in all_skill_dirs} - nc_packs
          cursor_slugs = set()
          for s in skills_list:
              if not isinstance(s, str):
                  continue
              m = re.search(r"packs[/\\]([^/\\]+)[/\\]", s)
              if m:
                  cursor_slugs.add(m.group(1))
          missing = sorted(pack_slugs - cursor_slugs)
          extra = sorted(cursor_slugs - pack_slugs)
          if len(cursor_slugs) != len(pack_slugs) or missing or extra:
              detail = []
              if missing:
                  detail.append("missing=" + str(missing))
              if extra:
                  detail.append("extra=" + str(extra))
              msg = (
                  f"[cursor] manifest skills count {len(cursor_slugs)} "
                  f"!= eligible packs {len(pack_slugs)}"
              )
              if detail:
                  msg += " (" + "; ".join(detail) + ")"
              print("::error::" + msg)
              sys.exit(1)
          print(f"[cursor] manifest skills match eligible packs ({len(cursor_slugs)})")
          PY
```

The slug regex `packs[/\\]([^/\\]+)[/\\]` is the same pattern check 6b uses at line 1389. Keep it. Do not put it in `RELEASE_PAIR`. It is not a parity literal today, and the local gate reads via `ROOT /` while this heredoc reads via `pathlib.Path(".")`.

- [ ] **Step 4: Confirm the step extracts and the version regexes did not move**

```bash
python -c "
import pathlib
text = pathlib.Path('.github/workflows/validate.yml').read_text(encoding='utf-8')
assert 'Cursor skills eligible set' in text
i = text.find('- name: SKILLS index count')
j = text.find('- name: Cursor skills eligible set')
k = text.find('- name: Chapter basename overlap')
assert 0 < i < j < k, (i, j, k)
# version regexes still byte-identical to the local gate
rel = pathlib.Path('tooling/check_release.py').read_text(encoding='utf-8')
for lit in (r'^##\s*\[(\d+\.\d+\.\d+)\]', r'Version:\s*([0-9]+\.[0-9]+\.[0-9]+)', r'version:\s*\"([0-9]+\.[0-9]+\.[0-9]+)\"'):
    assert lit in text and lit in rel, lit
print('step order ok, version regexes intact')
"
```

Expected: `step order ok, version regexes intact`, exit 0.

Do not run `python tooling/test_ci_gate.py` yet. It still pins ten steps and will fail extraction until Task 3 lands. That failure is expected. Task 3 is the probe update.

---

### Task 3: Probe pin, cursor version demo, skills demo, docs

**Gate:** gate-enforced (spec D4, D6, D7, D8, D9).

**Files:**
- Modify: `tooling/test_ci_gate.py:4` (docstring count)
- Modify: `tooling/test_ci_gate.py:17` (docstring count)
- Modify: `tooling/test_ci_gate.py:61-72` (`PINNED_STEPS`)
- Modify: `tooling/test_ci_gate.py:232-238` (`VERSION_BASE`)
- Modify: `tooling/test_ci_gate.py:463` (eleven-heredoc assertion)
- Modify: `tooling/test_ci_gate.py:481-490` (one new version demo after the existing disagreement demo)
- Modify: `tooling/test_ci_gate.py` after the index demos (one skills demo, before the overlap demos)
- Modify: `CONTRIBUTING.md:119` (one sentence after)
- Modify: `CHANGELOG.md:18-21` (one bullet under `### Changed`)

**Interfaces:**
- Consumes: the step name `Cursor skills eligible set` and the `[cursor]` / `[version]` print strings from Task 2. Consumes the `cursor-plugin.json` key from Task 1 only as a fixture path the version heredoc reads. Does not call either function.
- Produces: nothing later tasks read. This is the last task.

**Model:** standard

Per-task brief: `.superpowers/sdd/2026-10-28-cursor-plugin-ssot-gates/task-3-brief.md`

- [ ] **Step 1: Write the two failing demos before the pin, confirm they cannot run yet**

Do not add the `PINNED_STEPS` entry in this step. The demos below name a step the extractor does not know, so the probe fails. That is the red. Then Step 3 adds the pin and Step 4 goes green.

In `tooling/test_ci_gate.py`, extend `VERSION_BASE` (the dict that ends with the `catalog.yaml` entry, line 237) with one key. Value matches the claude fixture version, not the RELEASE-INFO fixture.

```python
VERSION_BASE = {
    ".claude-plugin/plugin.json": '{"version": "1.2.3"}\n',
    ".cursor-plugin/plugin.json": '{"version": "1.2.3"}\n',
    "CHANGELOG.md": "# Changelog\n\n## [Unreleased]\n\n## [1.2.3]: 2026-01-01\n",
    "RELEASE-INFO.txt": "Version:    1.2.4\n",
    "docs/products/website/01-jgs-se-knowledge-packs.yaml": 'version: "1.2.3"\n',
    "docs/products/website/catalog.yaml": 'version: "1.2.3"\n',
}
```

After the existing disagreement demo (the `demo(VERSION_BASE, "Version single-source", "[version] disagreement / missing", "version-disagreement")` call, lines 482-483) and before the website-YAML demo (line 485), insert the cursor disagreement demo. `RELEASE-INFO.txt` moves to `1.2.3` so the other four files agree and only the cursor file disagrees. The existing demo stays. It still fails on RELEASE-INFO `1.2.4`.

```python
        v_cur = dict(VERSION_BASE)
        v_cur["RELEASE-INFO.txt"] = "Version:    1.2.3\n"
        v_cur[".cursor-plugin/plugin.json"] = '{"version": "9.9.9"}\n'
        demo(v_cur, "Version single-source", "[version]", "version-cursor-disagreement")
```

After the last SKILLS index demo (`index-signpost-unmarked`, the `demo(index_tree(SKILLS_CONTENT_ONLY, SIGNPOST_UNMARKED), ...)` call) and before the overlap demos, insert the skills demo. Beta is excluded, so the eligible set is alpha. The manifest lists only beta: one extra excluded slug, one missing eligible slug. Assert `[cursor]` only.

```python
        demo({
            "packs/alpha/SKILL.md": "---\nname: alpha\n---\nbody\n",
            "packs/alpha/PACK.yaml": "commercial_use: true\n",
            "packs/beta/SKILL.md": "---\nname: beta\n---\nbody\n",
            "packs/beta/PACK.yaml": "commercial_use: false\n",
            ".cursor-plugin/plugin.json": json.dumps(
                {"skills": ["./packs/beta/SKILL.md"]}
            ) + "\n",
        }, "Cursor skills eligible set", "[cursor]", "cursor-skills-mismatch")
```

`json` is already imported at line 46. Do not add an import.

- [ ] **Step 2: Run the probe, confirm the new step name fails extraction**

```bash
python tooling/test_ci_gate.py
```

Expected: non-zero. The failure names `Cursor skills eligible set` and `extraction failed` (the `demo()` lookup `bodies[step]` raises `KeyError` on that name, or the assertion inside `demo` never runs because extraction of the unknown step is not what fails first). Either a `KeyError: 'Cursor skills eligible set'` or an extraction assertion is the red. A green run here means the pin was added too early. Remove it and rerun.

If the failure is instead `expected exactly ten pinned heredocs` or a positive-run failure of `Cursor skills eligible set` against the real tree, the pin was already added. That is Step 3's job. Stop and do Step 3 only if this run failed for the missing-name reason.

- [ ] **Step 3: Pin the eleventh step and the three count strings**

`PINNED_STEPS` must stay in workflow order. Insert the new name after `"SKILLS index count"` and before `"Chapter basename overlap"`.

```python
PINNED_STEPS = [
    "Version single-source",
    "SKILLS index count",
    "Cursor skills eligible set",
    "Chapter basename overlap",
    "Map and classification data invariants",
    "HTML self-containment",
    "Landing catalogue counts",
    "Catalog live-set parity",
    "Routing map coverage",
    "Pack content quality",
    "Pack licence and signpost shape",
]
```

Line 463, replace the assertion string. Do not change the assertion shape.

```python
    assert len(bodies) == len(PINNED_STEPS), "expected exactly eleven pinned heredocs"
```

Docstring line 4, replace `ten inline CI gates` with `eleven inline CI gates`. Docstring line 17, replace `the ten pinned steps` with `the eleven pinned steps`. Do not edit any other assertion string. Do not add a `RELEASE_PAIR` entry.

- [ ] **Step 4: Run the probe and the local gate**

```bash
python tooling/test_ci_gate.py
python tooling/check_release.py
```

Expected: both exit 0. The probe prints `ci-gate probe: OK (parity, extraction, negative demos, positive runs)`. The release gate PASS line contains `v1.23.0`.

A failure in `version-cursor-disagreement` means the version heredoc did not read `.cursor-plugin/plugin.json`. A failure in `cursor-skills-mismatch` means the new step did not print `[cursor]` or exited 0 on the tiny tree. A positive-run failure of `Cursor skills eligible set` means the live skills array does not match the eligible set. Do not add `easa-rules`, `med-device-eu`, or `sebok` to make it pass. Fix the step.

- [ ] **Step 5: CONTRIBUTING sentence and CHANGELOG bullet**

In `CONTRIBUTING.md`, after the line `CI green necessary but not sufficient.` (line 119) and before the `Local-only classes:` paragraph (line 121), add one sentence. Do not rewrite the section.

```markdown
`.cursor-plugin/plugin.json` version is in that single-source with the claude manifest, `RELEASE-INFO.txt`, and `CHANGELOG.md`, and CI also checks the Cursor skills array against packs whose `PACK.yaml` does not contain `commercial_use: false`.
```

In `CHANGELOG.md`, under `## [Unreleased]` `### Changed`, after the `faa-ams-vv` bullet (line 21), add one bullet. Do not add a heading. Do not edit `## [1.23.0]` or the Noted bullet that says 79 skills.

```markdown
- `.cursor-plugin/plugin.json` version joins the release single-source at 1.23.0, and CI checks its skills array against packs whose `PACK.yaml` does not contain `commercial_use: false`.
```

- [ ] **Step 6: Prose check and the full tooling suite**

```bash
python ~/.zcode/scripts/prose_check.py CONTRIBUTING.md CHANGELOG.md
python tooling/test_catalog_live_set.py
python tooling/test_catalogue_count.py
python tooling/test_ci_gate.py
python tooling/test_gen_pack_pages.py
python tooling/test_generate_capability_map.py
python tooling/test_html_assets.py
python tooling/test_install_guard.py
python tooling/test_link_policy.py
python tooling/test_pack_quality.py
python tooling/test_routing_map.py
python tooling/test_source_watch.py
python tooling/test_validate_pack.py
```

Expected: every command exits 0. A finding in the two new sentences gets fixed or justified in the run notes. Zero em dashes in the sentences this task wrote.

- [ ] **Step 7: Frozen-surface check**

```bash
python -c "
import json, pathlib, subprocess, sys
cur = json.load(open('.cursor-plugin/plugin.json', encoding='utf-8'))
assert cur['version'] == '1.23.0'
assert len(cur['skills']) == 80
joined = '\n'.join(cur['skills'])
for slug in ('easa-rules', 'med-device-eu', 'sebok'):
    assert slug not in joined
cat = json.load(open('catalog.json', encoding='utf-8'))
assert cat['updated'] == '2026-10-14'
# no PACK.yaml diff
diff = subprocess.run(['git', 'diff', '--name-only', '--', 'packs'], capture_output=True, text=True)
assert diff.stdout.strip() == '', diff.stdout
print('frozen surfaces hold')
"
```

Expected: `frozen surfaces hold`, exit 0.

Do not commit unless the parent execution mode says commit. Do not push. Do not tag. Do not open a PR.

---

## Self-review

Spec coverage: D1 and D2 are Task 1. D3 and D5 are Task 2. D4, D6, D7, D8, D9 are Task 3. D10's frozen counts are the Step 7 check in Task 3 and the Step 4 check in Task 1. The existing version disagreement demo is kept, not replaced. Check 6b's missing-file skip is not copied into CI and is not removed locally. `RELEASE_PAIR` is not extended. No task edits `## [1.23.0]`, `RELEASE-INFO.txt`, `.claude-plugin/plugin.json`, `catalog.json`, or any file under `packs/`.

Placeholder scan: every code step has the code. Every run step has the command and the expected output. No deferred-work marker, no cross-task shorthand, no validation step without a command.

Type consistency: the dict key is `cursor-plugin.json` in Task 1, Task 2, and the Task 3 fixture. The step name is `Cursor skills eligible set` in Task 2 and in `PINNED_STEPS`. The fail tag is `[cursor]` in the heredoc and in the D7 demo. The version fail tag is `[version]` in the heredoc and in the D4 demo.
