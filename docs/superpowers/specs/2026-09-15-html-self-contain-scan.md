# Spec: HTML self-containment scan (P12)

- Date: 2026-09-15
- Package: P12, visual website cut
- Status: ready for implementation
- Owner: jgs-se-knowledge-packs maintainers

## Problem

The public GitHub Pages site claims to be self-contained. `docs/index.html` lines 5 to 6
carry the header comment "Self-contained (inline CSS, no third-party asset/CDN/tracking)"
and `docs/packs.html` line 6 claims "Self-contained (inline CSS/JS, no third-party asset)".
Nothing enforces either claim. `tooling/check_release.py` collects text files by suffix at
lines 125 to 127 with the set `{.md, .py, .json, .yaml, .yml, .txt, .sh, .ps1}`, which omits
`.html`, so the leak and link-policy scans never read the pages. The CI workflow
`.github/workflows/validate.yml` repeats the same omission at its link-policy step (around
lines 116 to 120), where the suffix set is `{.md, .json, .yaml, .yml, .txt}`.

The result is a hole in the gate: the first image PR can hotlink a remote `og:image`, a CDN
font, or a tracking script in any `docs/*.html` page and every check stays green.

## Evidence

- `docs/index.html:5-6`: self-contained claim in the header comment. Lines 14, 19 carry
  `jgsystemsconsulting.github.io` canonical and `og:url` values. Line 15 is a
  `data:image/svg+xml` favicon whose payload contains the literal `http://www.w3.org/2000/svg`.
  Lines 24 to 29 reference fonts with relative paths under `fonts/`.
- `docs/packs.html:5-6`: generated page (RR-B-00, by `tooling/gen_packs_page.py`), same
  self-contained claim, same data-URI favicon, same relative font paths. The page body
  carries 68 intentional `github.com/.../blob/main/...` anchor links, one per pack row.
- `tooling/check_release.py:125-127`: `text_files` suffix set omits `.html`.
- `.github/workflows/validate.yml` link-policy step (~116-120): same omission, inline.
- `tooling/check_release.py:212-227` (RR-B-30, check 5c): the code comment claims the check
  covers "no third-party asset", but the code only implements three checks: packs.html
  exists, no em dash, and byte-equality with a fresh `gen_packs_page` render. No third-party
  asset scan exists anywhere. The comment overclaims; this spec makes it true.
- `docs/fonts/` holds four git-tracked woff2 files (Inter-Regular, Inter-SemiBold,
  JetBrainsMono-Regular, JetBrainsMono-Bold), so the existing relative font references
  resolve inside the repo.
- `tooling/test_link_policy.py` and `tooling/test_ci_gate.py` establish the repo's probe
  style: assert-based, no framework, imports the local gate module, and pins CI parity by
  extracting heredocs from `validate.yml` by pinned step name and asserting byte-identical
  regex literals.

## Goal

Fail closed when any `docs/*.html` page references an external http(s) asset, in both the
local gate (`tooling/check_release.py`) and the CI twin (inline stdlib step in
`validate.yml`), with an explicit allowlist for first-party hosts and data URIs, and an
assert-based probe covering the scan logic and the CI parity.

## Non-goals

- Creating artwork, OG cards, or hero stills (P12's visual work is separate).
- A full visual regression suite.
- Adopting a CDN.
- The P8 ledger.
- Non-HTML tooling backlog items.
- Local-asset existence checking (broken-link detection is a different gate; the fonts exist
  and are tracked today). The scan classifies URLs; it does not stat `docs/fonts/`.
- Adding `.html` to the `text_files` suffix set of checks 2 and 3 (leak sentinels, link
  policy). That would change the blast radius of two existing gates beyond this package.
  The new scan owns `.html` scanning, standalone.
- CSP or subresource-integrity work.

## Requirements

1. Every `docs/*.html` file is scanned for external asset references on every
   `check_release.py` run and every CI run.
2. An external asset is an http(s) URL whose host is not allowlisted, found in an asset
   position (see Design). Relative URLs and `data:` URIs never fail. Protocol-relative
   URLs (`//host/x`) fail.
3. Allowlisted hosts, exact match: `github.com` and `jgsystemsconsulting.github.io`.
4. A failure exits non-zero with a `[html-assets]` tagged message naming the file and URL.
5. The CI twin inlines the same regexes and allowlist as byte-identical literals, executes
   no checkout Python, and is pinned by `test_ci_gate.py` parity extraction.
6. An assert-based probe `tooling/test_html_assets.py` covers the scan with fixtures and
   asserts the real pages scan clean.
7. The self-host path convention (`docs/assets/` for images, `docs/fonts/` for fonts,
   relative references only) is documented in the scanner docstring and in
   `tooling/test_html_assets.py`, not in every failure message.

## Design

### Where the scan lives

A new section in `tooling/check_release.py`, placed adjacent to the RR-B-30 block, plus a
module-level function so the probe can unit test it without touching the tree:

```python
FIRST_PARTY_HOSTS = {"github.com", "jgsystemsconsulting.github.io"}

def scan_html_external_assets(text: str) -> list[str]:
    """Return the distinct external asset URLs in one HTML document."""
```

`main()` globs `sorted((ROOT / "docs").glob("*.html"))` only (the GH Pages root; not
rglob, so `docs/superpowers/` planning files stay out). Zero `.html` files found is itself
a `[html-assets]` failure, keeping the check fail closed. The module docstring's numbered
check list gains entry 12, and the "CI-covered" line in the docstring gains `html-assets`.

Regex, not `html.parser`: the repo's CI parity mechanism (`test_ci_gate.py`) pins
byte-identical regex literals between the local gate and the workflow heredoc. A parser
class cannot be pinned that way and would have to be duplicated wholesale. The pages are
generated or hand-maintained by us, and every ambiguity below resolves toward failing.

### What counts as an external asset

Two passes, case-insensitive, over the raw text.

Pass one, tag-scoped attributes. Slice candidate open tags with a **quote-aware** open-tag
regex that does not stop on `>` inside single- or double-quoted attribute values. Canonical
literal (byte-identical in local gate, CI twin, and `test_ci_gate.py` parity pins):

```
TAG_SLICE = re.compile(
    r"<(link|img|script|iframe|source|video|audio|embed|track|object|base|meta)\b"
    r"(?:\"[^\"]*\"|'[^']*'|[^>])*>",
    re.I,
)
```

Within each slice, read asset attributes. Attribute values may be double-quoted, single-quoted,
or unquoted (token until whitespace or `>`). Canonical attribute extractor is the **three-branch**
form only (do not use a conditional named-group quote; an empty optional quote group can take
the wrong branch and yield an empty value for unquoted attrs):

```
ATTR = re.compile(
    r"""(?P<name>href|src|data|srcset|content|http-equiv|property|name)\s*=\s*"""
    r"""(?:"(?P<d>[^"]*)"|'(?P<s>[^']*)'|(?P<u>[^\s>]+))""",
    re.I,
)
```

Value = first non-None of groups `d`, `s`, `u`.

| Element slice | Attribute read |
|---|---|
| `link`, `base` | `href` |
| `img`, `script`, `iframe`, `source`, `video`, `audio`, `embed`, `track` | `src` |
| `object` | `data` |
| any sliced tag | `srcset` (split on commas; first whitespace token per group is the URL, descriptors dropped) |
| `meta` with `property` of `og:image`, `og:image:secure_url`, or `name` of `twitter:image`, `twitter:image:src` | `content` |
| `meta` with `http-equiv` matching `refresh` (case-insensitive) | URL after `url=` inside `content` (`url=` match is case-insensitive; optional whitespace around `=`; take the remainder of the content value after the first `url=`; strip optional surrounding single or double quotes from that remainder) |

Element/attribute taxonomy is **closed** at the rows above for this package. Omitting
`video poster`, `input src`, SVG `image`/`use` href, and `link imagesrcset` is intentional;
expand only in a later package if those elements appear on the public pages.

Anchor tags (`<a href>`) are excluded by construction: the 68 github.com blob links in
`packs.html` rows are navigation, never fetched as page assets, so they never enter the
scan. `base` is included because an absolute `base href` silently re-hosts every relative
asset on the page.

Pass two, inline CSS. Over the whole document, match all of:

1. `url(...)` with optional quotes inside the parentheses
2. `@import "..."` (double-quoted)
3. `@import '...'` (single-quoted)
4. `@import url(...)` (url-form)

Canonical pass-two literals (byte-identical in local gate, CI twin, and parity pins):

```
CSS_URL = re.compile(r"""url\(\s*(['"]?)([^)'"\s]+)\1\s*\)""", re.I)
CSS_IMPORT = re.compile(
    r"""@import\s+(?:url\(\s*(['"]?)([^)'"\s]+)\1\s*\)|(['"])([^'"]+)\3)\s*;?""",
    re.I,
)
```

(Capture the URL group from whichever branch matched.) This is intentionally over-broad
(a `url(` inside an inline script string would be flagged); that direction is fail closed
and acceptable for our own pages.

Attribute order inside a slice does not matter because the attribute regex runs on the
slice, not on a fixed element template.

### Classification

For each candidate URL, stripped, in order:

1. Empty, or starts with `#`: skip.
2. Starts with `data:` (case-insensitive): allowed. This rule is load bearing: the favicon
   on both pages embeds `http://www.w3.org/2000/svg` inside a data URI, and that must never
   fail.
3. Starts with `http://` or `https://` (case-insensitive): external candidate. Parse with
   `urllib.parse.urlsplit`. Allow iff `hostname` lowercased is in `FIRST_PARTY_HOSTS` by
   exact match **and** `username` and `password` are both empty/None (reject userinfo tricks
   such as `https://user@github.com/...`). Subdomains and `www.` variants are not allowed.
4. Starts with `//`: external, fail (protocol-relative fetches inherit the page scheme and
   are a classic tracking vector).
5. Anything else: allowed (relative paths such as `fonts/JetBrainsMono-Regular.woff2`,
   `assets/og.png`, `./x`, and root-relative `/x`). Root-relative paths are technically
   wrong on a project Pages site (they resolve against the user site root, not the repo
   path) but they are not a self-containment violation; not enforced here.

### Allowlist rules

`FIRST_PARTY_HOSTS` holds exactly `github.com` and `jgsystemsconsulting.github.io`.
`github.com` is policy-first-party per the package decision: blob links in the page body
are not scanned as anchors, but an asset URL pointed at github.com is treated as
first-party rather than failed. `jgsystemsconsulting.github.io` covers the canonical links
and absolute OG/page URLs both pages already carry. The set is a module constant in
`check_release.py`, mirrored as an inline literal in the workflow step; no new data file.
Two hosts do not justify a third `tooling/*.txt` reader.

### Interaction with RR-B-30

No logic change to check 5c. The scan runs for all `docs/*.html`, which includes
`packs.html`, so the RR-B-30 comment at `check_release.py:212-213` becomes true once this
lands; update that comment to point at the `[html-assets]` check instead of claiming the
asset scan itself. Consequence for the generated page: if `gen_packs_page.py` output ever
embeds an external URL, the gate fails the tree and the fix belongs in the generator
template, never a hand edit to `packs.html` (RR-B-00 freshness would fail anyway).

One allowed comment touch on the pages themselves: `docs/index.html` lines 5 to 6 may gain
"(enforced by [html-assets] in tooling/check_release.py)". Do not hand-edit
`docs/packs.html` for the same note; it is generated.

### Failure messages

Match the `[tag]` idiom of the other checks, one line per distinct (file, URL):

```
[html-assets] external asset in docs/index.html: https://cdn.example/track.png
[html-assets] no docs/*.html found
```

Messages are URL-only after the file path (no element/attr context required). The
self-host convention note lives in the scanner docstring and the probe, not in every
message. CI prints the same content through the `::error file=...::` annotation format
the other steps use.

### CI twin

A new step in `.github/workflows/validate.yml`, named exactly `HTML self-containment`
(the string `test_ci_gate.py` pins), placed after the link-policy step:

- Inline `python3 - <<'PY'` heredoc, stdlib only, same two-pass regexes and the same
  `FIRST_PARTY_HOSTS` literal as `check_release.py`, byte-identical.
- Scans `docs/*.html` with the same glob shape, same classification order, exits 1 on any
  finding or on zero files, prints `::error` annotations per finding.
- Never executes checkout repository code (same trust boundary as every other step).
- The workflow header's coverage map gains a line: the step twins check_release
  `[html-assets]` as a complete port.

`tooling/test_ci_gate.py` extension: add `HTML self-containment` to `PINNED_STEPS` (this
makes the probe extract and execute the shipped heredoc against a clean-tree copy, which
the existing machinery already does for the other four steps). Update the probe docstring
count from "four" inline CI gates to five. Mandatory parity literals (all must appear
verbatim in both `check_release.py` and `validate.yml`):

1. both host strings (`github.com`, `jgsystemsconsulting.github.io`)
2. `TAG_SLICE` pattern string
3. `ATTR` pattern string
4. `CSS_URL` pattern string
5. `CSS_IMPORT` pattern string
6. the meta property/name tokens used for image meta (`og:image`, `twitter:image`, and the
   variants listed in the asset table)

### Honest residual

The allowlist is a two-element literal duplicated in the local gate and the workflow. A PR
can relax both in one edit; review is the control. That is the same posture as the overlap
whitelist documented in the workflow header. Accidental drift between the two copies is
loud: the probe pins the literals and executes the shipped heredoc.

Accepted scan limitations (document in the scanner docstring):

- HTML entity-encoded URLs (e.g. `https&#58;//cdn.example/x`) are not decoded before matching;
  raw-text regex will miss them. Our pages do not entity-encode asset URLs.
- The element/attribute taxonomy is closed; see Pass one table.
- No check that a relative path resolves to an on-disk file under `docs/`.

## Acceptance criteria

1. On the current tree, `python tooling/check_release.py` prints a PASS receipt with no
   `[html-assets]` lines.
2. `scan_html_external_assets` flags, in fixtures: `img src`, `link href` stylesheet and
   icon, `script src`, `iframe src`, `srcset` with multiple candidates, `og:image` and
   `twitter:image` content in both attribute orders, `meta http-equiv=refresh` with a
   non-allowlisted `url=`, CSS `url()`, and `@import` in double-quote, single-quote, and
   `url(...)` forms, whenever the URL is an http(s) URL on a non-allowlisted host. Also
   flags a fixture where a quoted attribute value contains `>` before a later external
   `src` (quote-aware slice), and an unquoted `src=https://cdn.example/x` on an img tag.
3. The scan allows: `data:` URIs including a fixture replicating the real favicon payload
   with its embedded `www.w3.org` URL; relative `fonts/...` and `assets/...` paths;
   `https://github.com/...` and `https://jgsystemsconsulting.github.io/...` URLs with empty
   userinfo. Rejects `https://user@github.com/...`.
4. Protocol-relative `//cdn.example/x` fails.
5. `python tooling/test_html_assets.py` passes all asserts and additionally runs the scan
   against the real `docs/*.html` and asserts zero findings.
6. `python tooling/test_ci_gate.py` passes with the new pinned step: heredoc extraction
   succeeds, the clean-tree run exits 0, and the parity literals are byte-identical.
7. A negative demo: appending
   `<img src="https://cdn.example/track.png">` to `docs/index.html` makes both
   `python tooling/check_release.py` and a local run of the extracted CI heredoc exit 1
   with `[html-assets]` output naming the file; reverting the line restores PASS.
8. CI on a PR that adds any external asset to `docs/*.html` fails at the
   `HTML self-containment` step.

## Verification

```bash
python tooling/test_html_assets.py
python tooling/test_ci_gate.py
python tooling/check_release.py
# negative demo (revert afterwards)
printf '<img src="https://cdn.example/track.png">\n' >> docs/index.html
python tooling/check_release.py; echo "expect exit 1"
git checkout -- docs/index.html
python tooling/check_release.py; echo "expect exit 0"
```

## Files touched

- `tooling/check_release.py`: `FIRST_PARTY_HOSTS`, `scan_html_external_assets()`, main()
  section, docstring entry 12, RR-B-30 comment correction. Roughly 60 lines.
- `tooling/test_html_assets.py`: new assert-based probe, no framework, imports
  `check_release`. Roughly 90 lines.
- `tooling/test_ci_gate.py`: one pinned step name, parity literals (hosts, TAG_SLICE, ATTR,
  CSS_URL, CSS_IMPORT, meta image tokens), every hardcoded "four" inline-gate count (docstring,
  header comment, assert message) updated to five.
- `.github/workflows/validate.yml`: new step plus one header coverage-map line.
- `docs/index.html`: optional one-line header comment note.

## Codebase context

The repo already runs an eleven-plus-check local gate (`tooling/check_release.py`,
`[tag]`-styled failures, PASS receipt with version and short sha) and an inline-stdlib CI
twin (`.github/workflows/validate.yml`) that never executes checkout code, with parity
enforced by `tooling/test_ci_gate.py` step extraction and literal pins. Probes are
assert-based stdlib scripts (`tooling/test_link_policy.py`, `tooling/test_validate_pack.py`)
that print an OK line and exit nonzero on any failed assert. `docs/packs.html` is generated
by `tooling/gen_packs_page.py` and must never be hand-edited. This spec follows all four
conventions rather than introducing new ones.

## Research

research: skipped (stdlib HTML self-containment scan; no external API, library, or version-sensitive platform choice)
