from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "skills/labflow-self-review/scripts/check_self_review.py"
HEADINGS = "\n".join(
    [
        "## Scope",
        "## Requirement Coverage",
        "## Checks Executed",
        "## Code Review",
        "## Mathematics and Artifacts",
        "## Visual Report Review",
        "## Visual Evidence",
        "## Changes Requested",
        "## Blockers",
        "## Final Status",
    ]
)


class SelfReviewContractTests(unittest.TestCase):
    def test_accepts_passed_review(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "SELF_REVIEW.md"
            path.write_text(HEADINGS + "\nFinal Status: passed\n", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(CHECKER), str(path), "--require-passed"],
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_rejects_missing_heading(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "SELF_REVIEW.md"
            path.write_text("## Scope\n## Final Status\nFinal Status: passed\n", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(CHECKER), str(path)],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("missing headings", result.stderr)

    def test_require_passed_rejects_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "SELF_REVIEW.md"
            path.write_text(HEADINGS + "\nFinal Status: blocked\n", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(CHECKER), str(path), "--require-passed"],
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 2)


if __name__ == "__main__":
    unittest.main()
