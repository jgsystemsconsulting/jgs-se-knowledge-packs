import json
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import eval as ev  # noqa: E402


class TestBankLoading(unittest.TestCase):
    def _bank(self, **over):
        b = {"slug": "demo", "status": "complete", "questions": [
            {"id": "d-01", "type": "topic", "prompt": "p",
             "routing": {"any_of": ["ch01"], "all_of": []},
             "must_include": ["x"], "provenance": "src ch01"}]}
        b.update(over)
        return b

    def test_valid_bank_returns_no_errors(self):
        self.assertEqual(ev.validate_bank(self._bank()), [])

    def test_missing_slug_is_error(self):
        b = self._bank(); del b["slug"]
        self.assertIn("missing 'slug'", " ".join(ev.validate_bank(b)))

    def test_bad_status_is_error(self):
        self.assertTrue(any("status" in e for e in ev.validate_bank(self._bank(status="done"))))

    def test_duplicate_ids_is_error(self):
        b = self._bank()
        b["questions"].append(dict(b["questions"][0]))
        self.assertTrue(any("duplicate" in e for e in ev.validate_bank(b)))

    def test_trigger_question_requires_expect_fire(self):
        b = self._bank(questions=[{"id": "d-tn", "type": "trigger-negative", "prompt": "p"}])
        self.assertTrue(any("expect_fire" in e for e in ev.validate_bank(b)))

    def test_topic_question_requires_routing(self):
        b = self._bank(questions=[{"id": "d-01", "type": "topic", "prompt": "p",
                                   "must_include": ["x"], "provenance": "s"}])
        self.assertTrue(any("routing" in e for e in ev.validate_bank(b)))


if __name__ == "__main__":
    unittest.main()
