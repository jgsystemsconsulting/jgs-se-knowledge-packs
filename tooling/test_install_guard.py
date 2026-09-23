"""Guard probe: install.py replaces only catalogue-owned destinations."""
import sys, tempfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import install

FOREIGN_SKILL = "---\nname: se\ndescription: user's own se skill\n---\n# mine\n"
FOREIGN_PACK_YAML = "slug: other-thing\ntitle: not ours\n"

def main() -> int:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        packs = root / "packs"; packs.mkdir()
        member = packs / "se"; member.mkdir()
        (member / "SKILL.md").write_text(
            "---\nname: se\nkind: orchestrator\ndescription: catalogue orchestrator\n---\n# se\n",
            encoding="utf-8")
        (member / "PACK.yaml").write_text(
            'slug: se\nkind: orchestrator\ntitle: "SE orchestrator"\n', encoding="utf-8")

        # (1) foreign native destination survives, run reports and exits 1
        base = root / "skills"; (base / "se").mkdir(parents=True)
        (base / "se" / "SKILL.md").write_text(FOREIGN_SKILL, encoding="utf-8")
        rc = install.install_native_guarded("claude", [member], base, dry=False)
        assert (base / "se" / "SKILL.md").read_text(encoding="utf-8") == FOREIGN_SKILL
        assert rc == 1, rc

        # (2) prior catalogue install is replaced
        (base / "se" / "PACK.yaml").write_text(
            'slug: se\nkind: orchestrator\ntitle: "SE orchestrator"\n', encoding="utf-8")
        rc = install.install_native_guarded("claude", [member], base, dry=False)
        assert rc == 0 and "catalogue orchestrator" in (base / "se" / "SKILL.md").read_text(encoding="utf-8")

        # (3) foreign transform destination survives (provenance comment absent)
        tdir = root / "prompts"; tdir.mkdir()
        (tdir / "se.md").write_text("user prompt\n", encoding="utf-8")
        rc = install.install_transform_guarded("codex", [member], tdir, dry=False)
        assert (tdir / "se.md").read_text(encoding="utf-8") == "user prompt\n" and rc == 1

        # (4) dry-run with a foreign destination reports "would skip" and touches nothing
        dry_base = root / "dry"; (dry_base / "se").mkdir(parents=True)
        (dry_base / "se" / "SKILL.md").write_text(FOREIGN_SKILL, encoding="utf-8")
        rc = install.install_native_guarded("claude", [member], dry_base, dry=True)
        assert rc == 0
        assert (dry_base / "se" / "SKILL.md").read_text(encoding="utf-8") == FOREIGN_SKILL
    print("install guard: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
