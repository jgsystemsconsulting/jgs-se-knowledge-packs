#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. - MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""Assert-based probe for the orchestrator routing-map check (P17; no framework).

Run:  python tooling/test_routing_map.py
Exits 0 when the demo matrix (pass, coverage, resolution, self-reference,
licence parity, subheading and marker grammar, cardinality) and the real-tree
fail-closed state all hold. Any failed assert raises and exits nonzero.
"""
from __future__ import annotations

import re
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_release  # noqa: E402

TAG = "[routing-map]"
BEGIN = "<!-- ROUTING-MAP:BEGIN -->"
END = "<!-- ROUTING-MAP:END -->"

DEFAULT_PACK_YAML = 'license: "Public Domain"\n'


def _skill(slug: str, kind: str | None = None) -> str:
    """Frontmatter-only SKILL.md body; kind line omitted when None."""
    kind_line = f"kind: {kind}\n" if kind else ""
    return f"---\nname: {slug}\n{kind_line}description: x\n---\n# {slug}\n"


def build_member(root: Path, skill_text: str, pack_yaml: bool | str = True) -> None:
    """Write packs/<name>/ (slug from frontmatter name:) with SKILL.md.

    pack_yaml True writes the default Public Domain PACK.yaml; a str is
    written verbatim as PACK.yaml; False writes no PACK.yaml.
    """
    m = re.search(r"^name:\s*(\S+)\s*$", skill_text, re.M)
    assert m, skill_text
    d = root / m.group(1)
    d.mkdir(parents=True)
    (d / "SKILL.md").write_text(skill_text, encoding="utf-8")
    if pack_yaml is True:
        (d / "PACK.yaml").write_text(DEFAULT_PACK_YAML, encoding="utf-8")
    elif isinstance(pack_yaml, str):
        (d / "PACK.yaml").write_text(pack_yaml, encoding="utf-8")


_HDRS = {
    "topics": "| Topic | When | Packs (best first) |\n| --- | --- | --- |\n",
    "agency": "| Context | When | Packs |\n| --- | --- | --- |\n",
    "deliverables": (
        "| Deliverable | When | Draft | Review | Verify |\n"
        "| --- | --- | --- | --- | --- |\n"
    ),
    "licences": "| Pack | Licence | Notes |\n| --- | --- | --- |\n",
}


def _orch(
    topics: list[str] | None = None,
    agency: list[str] | None = None,
    deliverables: list[str] | None = None,
    licences: list[str] | None = None,
    *,
    slug: str = "se",
    double_topics: bool = False,
) -> str:
    """Orchestrator SKILL.md whose routing map is built from table rows."""
    t = topics if topics is not None else ["| setup | first | `alpha`, `beta` |"]
    a = agency if agency is not None else ["| refit | later | `alpha` |"]
    d = deliverables if deliverables is not None else [
        "| plan | now | `alpha` | `beta` |  |"
    ]
    l = licences if licences is not None else ["| `beta` | MIT | upstream MIT |"]
    topics_block = _HDRS["topics"] + "\n".join(t) + "\n"
    if double_topics:
        topics_block += "\n### Topics\n" + _HDRS["topics"]
    return (
        _skill(slug, "orchestrator")
        + BEGIN + "\n"
        + "### Topics\n" + topics_block + "\n"
        + "### Agency contexts\n" + _HDRS["agency"] + "\n".join(a) + "\n\n"
        + "### Deliverables\n" + _HDRS["deliverables"] + "\n".join(d) + "\n\n"
        + "### Licences\n" + _HDRS["licences"] + "\n".join(l) + "\n"
        + END + "\n"
    )


def main() -> int:
    with tempfile.TemporaryDirectory() as td:
        packs = Path(td) / "packs"
        packs.mkdir()
        build_member(packs, _skill("alpha"))
        build_member(packs, _skill("beta"), pack_yaml='license: "MIT"\n')

        def swap(text: str) -> None:
            (packs / "se" / "SKILL.md").write_text(text, encoding="utf-8")

        def expect(text: str, *fragments: str) -> list[str]:
            swap(text)
            errs = check_release.check_routing_map(packs)
            assert errs, errs
            for f in fragments:
                assert any(f in e for e in errs), (f, errs)
            return errs

        # 1. pass: one orchestrator covering both packs, licence parity holds
        build_member(packs, _orch())
        assert check_release.check_routing_map(packs) == []

        # 2. content pack missing from Topics (coverage failure naming the slug)
        expect(
            _orch(topics=["| setup | first | `alpha` |"]),
            "content slug `beta` missing from ### Topics Packs column",
        )

        # 3. phantom slug in a Packs cell (resolution failure)
        expect(
            _orch(topics=["| setup | first | `alpha`, `ghost` |"]),
            "unknown pack slug `ghost`",
        )

        # 4. signpost target in a Packs cell (allowed; passes)
        build_member(packs, _skill("omega-sign", "signpost"), pack_yaml=False)
        swap(_orch(agency=["| refit | later | `alpha`, `omega-sign` |"]))
        assert check_release.check_routing_map(packs) == []

        # 5. self-reference to the orchestrator slug (failure)
        expect(
            _orch(topics=["| setup | first | `alpha`, `se` |"]),
            "orchestrator slug `se` must not appear as a routing target",
        )

        # 6. wrong licence cell text (parity failure)
        expect(
            _orch(licences=["| `beta` | Apache-2.0 | upstream MIT |"]),
            "### Licences licence cell for `beta`",
            "expected 'MIT'",
        )

        # 7. missing licence row for a non-Public-Domain pack (parity failure)
        expect(_orch(licences=[]), "missing row for non-Public-Domain pack `beta`")

        # 8. extra Licences row for a public-domain pack (parity failure)
        expect(
            _orch(
                licences=[
                    "| `beta` | MIT | upstream MIT |",
                    "| `alpha` | Public Domain |  |",
                ]
            ),
            "extra row for `alpha`",
        )

        # 9. doubled subheading (### Topics twice)
        expect(_orch(double_topics=True), "'### Topics'", "found 2")

        # 10. slug listed only in an Agency row (coverage failure)
        expect(
            _orch(topics=["| setup | first |  |"]),
            "missing from ### Topics Packs column",
        )
        swap(_orch(topics=["| setup | first |  |"]))
        errs = check_release.check_routing_map(packs)
        assert any("alpha" in e for e in errs), errs
        assert any("`beta`" in e for e in errs), errs

        # 11. plain-text token in a pack cell (rule 4 parse failure)
        expect(
            _orch(deliverables=["| plan | now | see alpha first | `beta` |  |"]),
            "pack cell has non-slug text",
            "'see alpha first'",
        )

        # 12. missing marker and doubled marker (marker failures)
        expect(
            _orch().replace(BEGIN + "\n", ""),
            f"expected exactly one {BEGIN}",
            "found 0 BEGIN / 1 END",
        )
        expect(
            _orch().replace(BEGIN, BEGIN + "\n" + BEGIN, 1),
            "found 2 BEGIN / 1 END",
        )

        # 13. zero orchestrators
        shutil.rmtree(packs / "se")
        assert check_release.check_routing_map(packs) == [
            f"{TAG} exactly one orchestrator member required: 0 found"
        ]

        # 14. two orchestrators
        build_member(packs, _orch())
        build_member(packs, _orch(slug="se2"))
        errs = check_release.check_routing_map(packs)
        assert errs == [
            f"{TAG} exactly one orchestrator member required: 2 found"
        ], errs

    # Real tree: Task 7 (packs/se) has not landed yet, so the fail-closed
    # "0 found" error is the expected mid-pipeline state. When Task 7 lands,
    # flip this assert to `real == []`.
    real = check_release.check_routing_map(ROOT / "packs")
    assert real == [
        f"{TAG} exactly one orchestrator member required: 0 found"
    ], real

    print("routing-map probe: OK (demo matrix, real-tree fail-closed state)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
