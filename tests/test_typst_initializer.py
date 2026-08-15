from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "optional-skills/labflow-typst/scripts/init_typst.py"


CONTEXT = """
kind: lab
title: Test lab
subject: Test subject
metadata:
  author: Student
  group: M412
  university: Test university
  city: Test city
deliverables:
  report_sections:
    - Цель работы
    - Выполнение работы
    - Выводы
"""


class TypstInitializerTests(unittest.TestCase):
    def test_creates_full_lab_structure_from_context(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            context = root / "context.yaml"
            context.write_text(CONTEXT, encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--context", str(context), "--output-dir", tmp],
                check=True,
                capture_output=True,
                text=True,
            )
            output = json.loads(result.stdout)
            self.assertEqual(output["kind"], "lab")
            for relative in (
                "docs/index.typ",
                "docs/content.typ",
                "docs/lib/context.typ",
                "docs/lib/gost.typ",
                "docs/lib/titlepage.typ",
                "artifacts/.gitkeep",
                "data/.gitkeep",
                "images/.gitkeep",
                "math/.gitkeep",
                "src/.gitkeep",
                "tests/.gitkeep",
            ):
                self.assertTrue((root / relative).exists(), relative)
            context_typ = (root / "docs/lib/context.typ").read_text(encoding="utf-8")
            self.assertIn("Test lab", context_typ)
            self.assertIn("Лабораторная работа", context_typ)
            content = (root / "docs/content.typ").read_text(encoding="utf-8")
            self.assertIn("= Цель работы", content)

    def test_does_not_overwrite_without_force(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            context = root / "context.yaml"
            context.write_text(CONTEXT, encoding="utf-8")
            subprocess.run([sys.executable, str(SCRIPT), "--context", str(context), "--output-dir", tmp], check=True)
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--context", str(context), "--output-dir", tmp],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("refusing to overwrite", result.stderr + result.stdout)


if __name__ == "__main__":
    unittest.main()
