#!/usr/bin/env python3
"""test_voice_guard.py: Unit tests for voice_guard.py rules and audit logging."""

import tempfile
import unittest
from pathlib import Path

from voice_guard import evaluate_text, log_result


class TestVoiceGuard(unittest.TestCase):
    def test_compliant_draft(self):
        text = (
            "Hi! I would like to investigate issue #22 to implement the local CI "
            "check runner in `scripts/check_all.py` and document fork-sync guidelines "
            "in `CONTRIBUTING.md`. I will prototype the runner against local environments."
        )
        violations = evaluate_text(text)
        self.assertEqual(violations, [])

    def test_assignment_demand_blocked(self):
        text = "Hi, please assign this to me, investigating issue #22 in scripts/check_all.py."
        violations = evaluate_text(text)
        violation_ids = [v["id"] for v in violations]
        self.assertIn("NO_ASSIGNMENT_DEMAND", violation_ids)

    def test_speculative_timelines_blocked(self):
        text = "Investigating issue #22 in scripts/check_all.py, will finish by tomorrow."
        violations = evaluate_text(text)
        violation_ids = [v["id"] for v in violations]
        self.assertIn("NO_SPECULATIVE_TIMELINES", violation_ids)

    def test_overconfident_guarantees_blocked(self):
        text = "Investigating issue #22 in scripts/check_all.py, this is an easy fix and 100% fixed."
        violations = evaluate_text(text)
        violation_ids = [v["id"] for v in violations]
        self.assertIn("NO_OVERCONFIDENT_GUARANTEES", violation_ids)

    def test_generic_boilerplate_blocked(self):
        text = "Great project! I would love to contribute to this amazing repo."
        violations = evaluate_text(text)
        violation_ids = [v["id"] for v in violations]
        self.assertIn("AVOID_GENERIC_BOILERPLATE", violation_ids)
        self.assertIn("MISSING_TECHNICAL_ANCHOR", violation_ids)

    def test_audit_logging(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            log_file = Path(tmpdir) / "test.log"
            log_result(log_file, "Valid draft for issue #22 in check_all.py", [])
            content = log_file.read_text(encoding="utf-8")
            self.assertIn("PASS", content)
            self.assertIn("Passed all voice-guard rules", content)


if __name__ == "__main__":
    unittest.main()
