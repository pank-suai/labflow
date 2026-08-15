from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "optional-skills/typst-report/scripts/init_typst.py"


class TypstInitializerTests(unittest.TestCase):
    def test_creates_lab_skeleton_and_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--output-dir",
                    tmp,
                    "--kind",
                    "lab",
                    "--title",
                    "Test lab",
                    "--author",
                    "Student",
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            created = json.loads(result.stdout)["created"]
            self.assertIn("docs/index.typ", created)
            index = Path(tmp, "docs/index.typ").read_text(encoding="utf-8")
            self.assertIn("Test lab", index)
            self.assertIn("Лабораторная работа", index)
            metadata = json.loads(Path(tmp, "context/typst-metadata.json").read_text())
            self.assertEqual(metadata["kind"], "lab")

    def test_does_not_overwrite_without_force(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run([sys.executable, str(SCRIPT), "--output-dir", tmp], check=True)
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--output-dir", tmp],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("refusing to overwrite", result.stderr + result.stdout)


if __name__ == "__main__":
    unittest.main()
