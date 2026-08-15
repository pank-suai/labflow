#!/usr/bin/env python3
"""Create a neutral Typst report skeleton for labflow projects."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


FIELDS = (
    "title",
    "subject",
    "author",
    "group",
    "university",
    "faculty",
    "department",
    "city",
)


def typst_string(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--kind", choices=("lab", "coursework", "practical"), default="lab")
    parser.add_argument("--title", default="")
    parser.add_argument("--subject", default="")
    parser.add_argument("--author", default="")
    parser.add_argument("--group", default="")
    parser.add_argument("--university", default="")
    parser.add_argument("--faculty", default="")
    parser.add_argument("--department", default="")
    parser.add_argument("--city", default="")
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output = args.output_dir.resolve()
    docs = output / "docs"
    lib = docs / "lib"
    template_root = Path(__file__).resolve().parents[1] / "templates" / "gost"
    generated = [docs / "index.typ", lib / "gost.typ", lib / "titlepage.typ", lib / "template.typ"]

    if not args.force:
        existing = [str(path.relative_to(output)) for path in generated if path.exists()]
        if existing:
            raise SystemExit("refusing to overwrite existing files: " + ", ".join(existing) + "; use --force")

    lib.mkdir(parents=True, exist_ok=True)
    for source_name in ("gost.typ", "titlepage.typ", "template.typ"):
        shutil.copy2(template_root / "lib" / source_name, lib / source_name)

    values = {field: typst_string(getattr(args, field)) for field in FIELDS}
    values["kind"] = {
        "lab": "Лабораторная работа",
        "coursework": "Курсовой проект",
        "practical": "Практическая работа",
    }[args.kind]
    index = (template_root / "index.typ").read_text(encoding="utf-8")
    for key, value in values.items():
        index = index.replace(f"__{key.upper()}__", value)
    docs.joinpath("index.typ").write_text(index, encoding="utf-8")

    metadata = {
        "kind": args.kind,
        "title": args.title,
        "subject": args.subject,
        "author": args.author,
        "group": args.group,
        "university": args.university,
        "faculty": args.faculty,
        "department": args.department,
        "city": args.city,
    }
    output.joinpath("context").mkdir(exist_ok=True)
    output.joinpath("context", "typst-metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({"created": [str(path.relative_to(output)) for path in generated] + ["context/typst-metadata.json"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
