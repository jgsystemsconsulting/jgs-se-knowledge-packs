# Context: ci-local-gate-coverage-gap (2026-09-14)

## Context brief

**Primary question**: Close the highest-value CI-blind release-gate gaps without executing checked-out repo Python, and document what must stay local-only with a pre-tag fail-closed answer.

**Sub-questions**:
1. Enumerate the eleven local `check_release` checks (id, what each reads, fail idiom) plus the extra sub-checks the file actually runs.
2. Enumerate the four CI steps and the P4 link-policy parity assert already landed.
3. Build the gap matrix: which checks are CI-blind, which are closable as inline stdlib / pure data reads, which must stay local.
4. Version-trio (+ website YAML) single-source mechanics.
5. SKILLS.md count mechanics.
6. Map / overlap / classification invariant shapes expressible as pure data reads.
7. What exists today that would catch a skipped local gate pre-tag (fail-closed question).
8. Design constraints: trust boundary, drift risk, P4 data-file precedent, local-only remainder.

**Success criteria**: SC1 local eleven (+extras); SC2 CI four + P4; SC3 gap matrix with closable/not; SC4 version/SKILLS/map-overlap mechanics; SC5 pre-tag surface + design considerations.

**Out of scope**: host-list parity itself (P4 done; do not undo); running `tooling/check_release.py` in CI; third-party Actions or PyYAML; content-quality evals; Phase 21 CONTRACT prose; restoring deleted `tooling/eval` pytest suite.

**Budget**: single-pass context gate.

**Workspace baseline**: P4 landed (commits 1e47bb0/f3fff72/e025f79/89464a1/a42e3d9); P6/P7 also landed on main. This package is P5 only.

**Parent-verified package facts** (packages.md P5):
- CI = four shallow steps; local = eleven checks including website YAMLs on version gate.
- Phases 19-20 map/overlap/classification/replay invisible to CI.
- In scope: version trio incl. website YAMLs, SKILLS.md vs packs count, map/overlap invariants as inline stdlib or pure data reads; document remaining local-only; fail closed if required local gate skipped pre-tag; preserve `permissions: read-all` and no-checkout-code-execution.
- Out: P4 host parity; execute `check_release.py` in CI.

## Findings

Grades: CORROBORATED 9, SINGLE-SOURCE 14, CONFLICTED 0, STALE 2 (TESTING.md line refs / eleven-check doc lag behind extra sub-checks).

| # | Claim | Grade |
|---|-------|-------|
| 1 | Local docstring names eleven numbered checks | CORROBORATED |
| 2 | Code also runs 5b RR-S-13, 5c packs.html, 6b cursor skills (not in docstring count) | SINGLE-SOURCE |
| 3 | CI has exactly four content steps + P4 parity inside the link step | CORROBORATED |
| 4 | CI trust boundary: inline stdlib only; never exec repo Python; permissions read-all | CORROBORATED |
| 5 | Version SoT: plugin.json + CHANGELOG top + RELEASE-INFO + two website YAMLs vs RELEASE-INFO | CORROBORATED |
| 6 | SKILLS.md count = non-signpost slug packs/ entries vs non-signpost pack dirs | SINGLE-SOURCE |
| 7 | Overlap = basename multiset of packs/*/chapters/*.md minus WHITELIST | CORROBORATED |
| 8 | Map freshness / classification / replay import tooling/*.py (local-only today) | CORROBORATED |
| 9 | Partial map/rules envelope + disk set diffs are pure JSON+fs readable | SINGLE-SOURCE |
| 10 | Full validate_pack, packs.html regen, generator --check need repo code | CORROBORATED |
| 11 | No automated pre-tag hook/workflow requires check_release today | CORROBORATED |
| 12 | TESTING.md ~L80 still says packs.html/SKILLS only caught locally (stale line refs, true gap) | STALE/SS |
| 13 | CONCERNS trust-boundary row still sound; host-list row resolved by P4 | CORROBORATED |
| 14 | P4 precedent: trusted inline pin + parity vs data file; do not undo | CORROBORATED |
| 15 | Package in_scope/out_scope as quoted above | SINGLE-SOURCE |
| 16 | Live signposts: omg-signpost, se-standards-signpost | SINGLE-SOURCE |
| 17 | Content packs 63; SKILLS entries 63 (matched at gate time) | SINGLE-SOURCE |
| 18 | Docstring claims eleven; problem statement matches docstring; extras are additional blind surface | SINGLE-SOURCE |

## Exact current state

### Local gate: tooling/check_release.py

Docstring order (the "eleven"):

| # | Id / tag prefix | What it reads | Needs repo code exec? | Fail idiom |
|---|-----------------|---------------|----------------------|------------|
| 1 | `[files]` | fixed REQUIRED_FILES list via Path.is_file | no (pure fs) | fail(errs, "[files] missing…") |
| 2 | `[leak]` | all text files under ROOT minus SKIP_DIRS; sentinel fragments | no (pure scan) | "[leak] sentinel '…' found in …" |
| 3 | `[links]` / `[links-parity]` | tooling/link-policy-hosts.txt as data + text scan; signpost dirs skipped | no (data+scan; loader in this file) | "[links] …" or "[links-parity] …" |
| 4 | `[version]` | .claude-plugin/plugin.json version; CHANGELOG ## [N.N.N]; RELEASE-INFO Version:; two website YAMLs version: "N.N.N" | no (json+regex) | "[version] … disagreement / missing" or website path mismatch |
| 5 | `[pack:<slug>]` / `[pack]` | imports validate_pack.check_pack per non-signpost pack dir | **yes** | per-pack errors or "[pack] validate_pack failed to run" |
| 6 | `[index]` | SKILLS.md slug links vs non-signpost pack count | no (text+fs) | "[index] SKILLS.md lists N packs but M are shipped" |
| 7 | `[header]` | fixed authored file list head 600 chars for JGSC + SPDX sentinels | no (text) | "[header] missing …" |
| 8 | `[overlap]` | import check_overlap; check_overlap.main() | **yes** (logic is pure; entry is import) | "[overlap] check_overlap.py failed…" |
| 9 | `[map]` | import check_capability_map; .main() | **yes** | "[map] check_capability_map.py failed…" |
| 10 | `[classification-rules]` | import check_classification_rules; .main() | **yes** | "[classification-rules] … failed…" |
| 11 | `[map-replay]` | read map JSON generated_on; import generate_capability_map; .main([--generated-on, disk_on, --check]) | **yes** | "[map-replay] …" |

Extra sub-checks present in main() but outside the docstring eleven:

| Code block | Tag | What | Repo exec? |
|------------|-----|------|------------|
| 5b RR-S-13 | `[rr-s-13:<slug>]` | each content pack SKILL.md has ## When to use + prerequisites marker | no (regex) |
| 5c RR-B-30 | `[rr-b-30]` | docs/packs.html exists, no em dash, equals gen_packs_page.render(...) | **yes** (import gen_packs_page) |
| 6b MA-01 | `[cursor]` | .cursor-plugin/plugin.json skills paths cover every non-commercial_use: false pack | no (json+fs+regex) |

Report: if errs: print RELEASE CHECK: FAIL (N issue(s)) + each err; return 1. Else RELEASE CHECK: PASS; return 0.

SKIP_DIRS (local only): .git, sources, .build, .playwright-mcp, __pycache__, .worktrees, .ruff_cache, .pytest_cache, .venv, venv, .idea, .vscode, .planning, .superpowers, superpowers.

Signpost detection (shared shape with CI): packs/*/SKILL.md with ^kind:\s*signpost\s*$. Live: omg-signpost, se-standards-signpost.

### CI gate: .github/workflows/validate.yml

- **name**: validate
- **triggers**: push branches [main]; all pull_request
- **permissions**: read-all
- **job**: content-integrity on ubuntu-latest
- **header contract**: self-contained inline bash + python3 stdlib only; never executes checked-out repository code; leak + link skip .planning; link policy enforces from trusted inline host set and asserts set-parity vs tooling/link-policy-hosts.txt (P4)

Four steps:

| # | Step name | Mechanism | Fail idiom |
|---|-----------|-----------|------------|
| 1 | Content integrity check (leak sentinels) | bash grep -RIn fragment sentinels; exclude .git .planning | ::error::leak sentinel found; hits=1; test hits -eq 0 |
| 2 | Link policy check (no source-material URLs) | inline python3 heredoc: TRUSTED_HOSTS frozenset (18 tokens) + parity vs data file + scan with signpost skip; also skips .git/.planning/superpowers | ::error::link-policy parity: … or ::error file=…::source-material URL; sys.exit(1) |
| 3 | Pack frontmatter lint | inline python3: every packs/*/SKILL.md has YAML frontmatter, kebab-case name, non-empty description | ::error file=…::…; sys.exit(1 if fails) |
| 4 | Catalog JSON valid | python3 -c json.load(open('catalog.json')) | non-zero on parse error |

P4 parity is **inside** step 2 (not a fifth step). Do not remove or weaken it.

CI does **not** cover checks 1 (required files), 4 (version), 5 (full pack), 5b/5c/6b, 6 (SKILLS count), 7 (headers), 8-11 (overlap/map/rules/replay). Partial overlap with 2/3 via leak+frontmatter only; CI frontmatter is shallower than validate_pack.

### Trust-boundary rationale

Why CI must never execute checked-out tooling/*.py:

1. Workflow header + check_release module docstring state it explicitly.
2. CONCERNS.md Security: a "simplify to call check_release.py" change would let a malicious PR run arbitrary checkout code under Actions.
3. Safe: read plain data (txt/json/yaml-as-text), run inline stdlib heredocs baked into the workflow file (reviewable under workflow CODEOWNERS/branch protection).
4. Unsafe: python tooling/check_release.py, import validate_pack, any run: that treats checkout as code.
5. P4 chose hybrid: trusted inline pin + parity against editable data file. Same posture for P5 expansions.

## Gap matrix

| Local surface | CI today | Closable as inline stdlib / pure data? | Notes |
|---------------|----------|----------------------------------------|-------|
| 1 required files | blind | **yes** | low value vs release; easy Path.is_file loop |
| 2 leak | covered | already in CI | residual scan-scope diffs remain (suffixes/SKIP_DIRS); out of P5 min |
| 3 links + parity | covered (P4) | already in CI | **do not undo** |
| 4 version trio + website YAMLs | blind | **yes (in_scope minimum)** | json + three regexes; no PyYAML |
| 5 full validate_pack | blind (frontmatter only) | **no** (keep local) | YAML-subset parser, license_tier, chapter link resolve; re-implement = drift factory |
| 5b RR-S-13 When to use | blind | **yes** (optional) | two regexes on SKILL.md; not in package minimum list but cheap |
| 5c packs.html freshness | blind | **no** (keep local) | needs gen_packs_page.render; em-dash-only check is pure but weak |
| 6 SKILLS.md count | blind | **yes (in_scope minimum)** | signpost filter + link regex + pack dirs |
| 6b cursor skills | blind | **yes** (optional) | json + PACK.yaml commercial_use line scan |
| 7 authored headers | blind | **yes** (optional) | fixed path list + two sentinels |
| 8 overlap basenames | blind | **yes (in_scope minimum)** | pure glob multiset; whitelist must be pinned (inline set or data+parity) |
| 9 map freshness (full) | blind | **partial** | envelope + pack/chapter set diffs = pure JSON+fs; cluster thresholds + note rules need checker logic; keep full checker local |
| 10 classification-rules (full) | blind | **partial** | envelope + assignment (pack,chapter) coverage vs disk chapters = pure; support/signpost/uniqueness edge rules richer; keep full checker local |
| 11 map-replay --check | blind | **no** (keep local) | deterministic generator re-exec; defining replay without the generator is a second generator |

**Package minimum closable set (explicit)**:
1. Version agreement including website YAMLs.
2. SKILLS.md vs packs count (signpost-aware).
3. Map/overlap invariants expressible as pure data reads (at least overlap basename gate; map/rules envelope + disk membership if chosen).

**Must stay local-only (document + pre-tag)**:
- Full validate_pack / RR-B-30 packs.html regen equality / generator --check replay.
- Full map threshold/note logic and full classification assignment semantics beyond set coverage (unless intentionally subsetted and parity-pinned).

## Version-trio single-source mechanics

Sources compared today (check 4 + 4a):

| Source | Path | Extract |
|--------|------|---------|
| plugin | .claude-plugin/plugin.json | json.load(...).get("version") |
| changelog | CHANGELOG.md | first ^##\s*\[(\d+\.\d+\.\d+)\] (Unreleased section sits above; first version heading wins) |
| release-info | RELEASE-INFO.txt | Version:\s*([0-9]+\.[0-9]+\.[0-9]+) |
| website product | docs/products/website/01-jgs-se-knowledge-packs.yaml | first version:\s*"([0-9]+\.[0-9]+\.[0-9]+)" must equal RELEASE-INFO |
| website catalog | docs/products/website/catalog.yaml | same regex; must equal RELEASE-INFO |

Agreement rule: build versions dict for the three core files; website paths compared to expected = versions["RELEASE-INFO.txt"]; then distinct = {v for v in versions.values() if v}; fail if len(distinct) > 1 or any empty string in versions.values().

Current live value (gate time): 1.20.0 across plugin, RELEASE-INFO, both YAMLs; CHANGELOG top version heading ## [1.20.0] (with ## [Unreleased] above it; regex still finds 1.20.0 as first ## [N.N.N]).

Not in version gate: packs/*/PACK.yaml source_version (different class; 4a scoped to the two website paths only). docs/capability-pack-map.json / classification-rules.json map_version is a map version field checked by map/rules tools, not by check 4.

CI port: inline python3 reading the five paths with the same regexes/json; no import of check_release.

## SKILLS.md count mechanics

```text
signpost_dirs = {parent of packs/*/SKILL.md | body matches ^kind:\s*signpost\s*$}
packs = sorted dirs under packs/ not in signpost_dirs
entry_slugs = re.findall(r"\[`([^`]+)`\]\(packs/", SKILLS.md text)
entry_count = len([s for s in entry_slugs if s not in signpost_names])
fail if packs and entry_count != len(packs)
```

Live: 2 signposts; 63 content packs; 63 SKILLS entries. Header prose says 63 packs (+2 signposts) but the gate counts table links, not the prose numeral.

CI port: same signpost detection + findall + dir listing. No need to parse the HTML comment or the prose count line.

## Map / overlap invariant shapes (pure-data subset)

### Overlap (TOOL-20) - fully expressible as pure data

- Scan: packs/*/chapters/*.md basenames only (support files outside chapters/ excluded by path).
- Collision: basename maps to list of pack slugs; any len>1 not in WHITELIST fails.
- WHITELIST today (code constant in check_overlap.py): {ch01-introduction.md}.
- Fail: print OVERLAP: FAIL; list basename: pack1, pack2; exit 1.
- CI port options: (A) inline identical whitelist frozenset + glob logic; (B) move whitelist to a data file + P4-style parity against trusted inline pin. Prefer not to import check_overlap.

### Map freshness - partial pure subset

docs/capability-pack-map.json envelope (live): schema_version: 2, map_version: "1.20.0", generated_on: "2026-08-27", clusters: [ {name, chapters:[{pack, chapter, ...}]} ] (32 clusters).

Pure-data checks possible without generator:
- file exists + top-level object
- schema_version == 2; map_version non-empty semver-ish; generated_on YYYY-MM-DD
- every on-disk non-signpost pack with chapters/ appears in some cluster entry; every map pack has on-disk chapters/
- every on-disk packs/<p>/chapters/<c> appears as a (pack, chapter) in the map and vice versa (set equality)

Not pure without reimplementing checker policy:
- per-cluster minimum thresholds by cluster name
- note/override consistency
- full staleness messaging parity with check_capability_map.py

### Classification-rules - partial pure subset

docs/classification-rules.json envelope (live): schema_version: 1, map_version: "1.20.0", generated_on: "2026-08-27", assignments n=644, cluster_names n=32, signpost_packs n=2, plus support_policy / rules_of_construction / support_filenames.

Pure-data checks possible:
- envelope fields present/typed
- every live chapter basename under non-signpost packs has an assignment row (pack, chapter)
- no assignment row points at missing files (optional inverse)
- no assignment for packs listed in signpost_packs

Not pure without reimplementing:
- support-file policy edges, uniqueness subtleties already encoded in check_classification_rules.check_rules, rules-vs-map generated_on fidelity (P7 WR-02), cluster_name pipe/CR/LF rejects (P7 WR-01)

### Generator replay - not pure

generate_capability_map.main([--generated-on, disk_on, --check]) rebuilds map from rules+overrides and diffs JSON (+ md freshness per P7 WR-03). CI cannot call it. Document as local-only required pre-tag check.

## Pre-tag fail-closed question

**What exists today that catches a skipped local gate before tag?**

| Mechanism | Present? | Effect |
|-----------|----------|--------|
| git pre-tag / pre-push hook requiring check_release | **no** | none |
| CI workflow on tag / release event running full gate | **no** | validate.yml is push main + pull_request only; still shallow |
| GitHub Release / gh release path that blocks on artifact | process only (P8 /gsd-ship) | human-driven |
| Docs saying run before tagging | **yes** | check_release.py docstring; PACK-SPEC / capability-map-CONTRACT references; build_all_packs.workflow.js Register step |
| Branch protection requiring green validate | ops-level | only covers the four shallow checks |

**Conclusion**: today a human (or agent) can tag without ever running check_release.py. CI green is not release-ready. P5 must specify a fail-closed control for required local-only checks, for example one of:

1. **Receipt artifact**: pre-tag checklist file or CI-readable stamp produced only by a trusted local run (still requires process discipline unless a release workflow verifies the stamp).
2. **Release workflow gate**: on tag push, a workflow that does not exec repo Python but does re-run the inline closable set, and fails the release job unless a signed/local attestation exists for local-only checks (design heavy).
3. **Explicit blocker doc + ship skill step**: /gsd-ship / release runbook refuses to proceed without a pasted RELEASE CHECK: PASS transcript (soft fail-closed; matches current P8 ownership).
4. **CODEOWNERS + required status** only helps the closable CI subset; does not cover local-only.

Spec must pick a concrete fail-closed mechanism; documenting remaining local-only alone is not fail-closed.

## Design considerations the spec must settle

1. **Which closable checks land in validate.yml this package**
   Minimum from package: version (+website YAMLs), SKILLS count, overlap (and/or map/rules pure subset). Optional cheap adds: RR-S-13, headers, cursor skills, required-files. Do not attempt full validate_pack or packs.html regen or replay in CI.

2. **Inline-python-only additions**
   New steps = python3 heredocs (or bash for trivial existence checks). Stdlib only. No pip install. No uses: beyond existing actions/checkout@v4. No PyYAML (version YAML uses one-line regex, same as local 4a).

3. **Drift risk between CI copies and check_release**
   Structural risk #1 for P5. Every inlined algorithm can diverge silently (the exact failure mode P4 fixed for hosts). Mitigations patterned on P4:
   - Data-file + trusted pin + parity for any list/constant (overlap WHITELIST, required-files list, authored header list).
   - Shared expected-regex comments + a kept local probe that asserts CI workflow text contains the same version regex / SKILLS regex (optional meta-check; local-trusted only).
   - Do not dual-maintain complex parsers; if logic is non-trivial, keep it local-only rather than fork it into the workflow.

4. **P4 data-file precedent (preserve)**
   Link hosts: CI enforces from inline TRUSTED_HOSTS; parity vs tooling/link-policy-hosts.txt; local loads the file fail-closed. P5 must not replace that step or switch CI to just-read-the-file without a pin. New P5 data files (if any) should follow the same hybrid if the constant is policy-bearing.

5. **What stays local-only and why**
   - validate_pack full structural/licence gate: non-trivial parser; signpost rules just aligned in P6; forking into CI invites permanent drift.
   - gen_packs_page freshness: generated artifact equality needs the generator.
   - generate_capability_map --check replay (+ md freshness): definitionally generator execution.
   - Full map thresholds / full classification semantics: large policy surface; pure set-coverage subset is enough for CI smoke if desired.

6. **Failure UX**
   Keep local fail() tags stable ([version], [index], [overlap], ...). CI should use ::error:: / ::error file=:: and name the check id in the message for grep parity. New parity tags if data files introduced (cf. [links-parity]).

7. **Scan-scope residual**
   Leak/link SKIP_DIRS and suffix sets still differ slightly between CI and local. Out of P5 minimum unless cheap; do not expand scope into a rewrite of leak policy.

8. **Permissions posture**
   Keep permissions: read-all. No write tokens. No pull_request_target.

9. **Doc surfaces to update when implementing** (not this context write): TESTING.md CI-gap note; CONCERNS if new residual; CHANGELOG; capability-map-CONTRACT line that says CI does not exec repo Python (still true).

10. **Ordering relative to other packages**
    P4 done (dependency satisfied). P6 signpost validator parity done (SKILLS/pack counting signpost filter already consistent). P7 map residuals done on local tools; CI pure subset should not assume broken generator.

## Synthesis

SC1-SC5 covered. Spec should:

- Add inline CI steps for the package minimum closable set (version+website, SKILLS count, overlap; optional map/rules envelope+membership).
- Leave full pack validate, packs.html regen, and map-replay local-only.
- Name a real pre-tag fail-closed control (today: none automated).
- Apply P4-style pin/parity anywhere a constant is copied into the workflow.
- Never run: python tooling/check_release.py.

## Evidence index

| Loc | Kind |
|-----|------|
| tooling/check_release.py:1-373 | code (whole local gate) |
| tooling/check_release.py:10-28 | doc (eleven-check list + CI boundary) |
| tooling/check_release.py:121-145 | code (version + website 4a) |
| tooling/check_release.py:147-191 | code (validate_pack, RR-S-13, packs.html) |
| tooling/check_release.py:193-240 | code (SKILLS count, cursor) |
| tooling/check_release.py:242-320 | code (overlap, map, classification, replay) |
| tooling/check_release.py:322-370 | code (headers + report) |
| .github/workflows/validate.yml:1-134 | config (whole CI) |
| tooling/check_overlap.py:1-67 | code (basename + WHITELIST) |
| tooling/check_capability_map.py | code (envelope + staleness; local) |
| tooling/check_classification_rules.py | code (rules; local) |
| tooling/generate_capability_map.py | code (replay --check; local) |
| docs/capability-pack-map.json | data (envelope live) |
| docs/classification-rules.json | data (envelope live) |
| docs/products/website/*.yaml | data (version fields) |
| RELEASE-INFO.txt / .claude-plugin/plugin.json / CHANGELOG.md | data (version trio) |
| SKILLS.md | data (index links) |
| .planning/codebase/TESTING.md ~L80 | doc (CI-gap note; stale line nums) |
| .planning/codebase/CONCERNS.md | doc (trust boundary; P4 resolution residual) |
| docs/superpowers/packages/...-packages.md P5 | doc (in/out scope) |
| docs/superpowers/context/2026-09-14-ci-link-policy-parity-context.md | format ref (P4) |
