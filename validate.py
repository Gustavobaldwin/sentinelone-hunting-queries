#!/usr/bin/env python3
"""Validate hunting queries and (re)build the README index.

Usage:
  python scripts/validate.py          # validate + check README is up to date (CI)
  python scripts/validate.py --write  # validate + rewrite README index
"""
import datetime as dt
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = json.loads((ROOT / "schema" / "query.schema.json").read_text(encoding="utf-8"))
README = ROOT / "README.md"
START, END = "<!-- INDEX:START -->", "<!-- INDEX:END -->"
STATUS_BADGE = {"experimental": "🧪", "tested": "✅", "production": "🛡️", "deprecated": "⚠️"}


def load_queries():
    validator = Draft202012Validator(SCHEMA)
    errors, queries, seen = [], [], {}
    for path in sorted((ROOT / "queries").rglob("*.y*ml")):
        rel = path.relative_to(ROOT).as_posix()
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            errors.append(f"{rel}: invalid YAML: {exc}")
            continue
        # PyYAML parses dates into date objects; schema expects strings
        for k in ("created", "updated"):
            if isinstance(data.get(k), dt.date):
                data[k] = data[k].isoformat()
        for err in validator.iter_errors(data):
            loc = "/".join(map(str, err.path)) or "(root)"
            errors.append(f"{rel}: {loc}: {err.message}")
        qid = data.get("id")
        if qid in seen:
            errors.append(f"{rel}: duplicate id {qid} (also in {seen[qid]})")
        seen[qid] = rel
        if path.parent.name != data.get("mitre", {}).get("tactic"):
            errors.append(f"{rel}: folder '{path.parent.name}' does not match mitre.tactic")
        queries.append((rel, data))
    return queries, errors


def build_index(queries):
    lines = [
        "| ID | Query | Tactic | Techniques | Status |",
        "|----|-------|--------|------------|--------|",
    ]
    for rel, q in sorted(queries, key=lambda x: x[1]["id"]):
        techs = ", ".join(
            f"[{t}](https://attack.mitre.org/techniques/{t.replace('.', '/')}/)"
            for t in q["mitre"]["techniques"]
        )
        badge = STATUS_BADGE.get(q["status"], "")
        lines.append(
            f"| {q['id']} | [{q['title']}]({rel})<br><sub>{q['title_pt']}</sub> "
            f"| {q['mitre']['tactic']} | {techs} | {badge} {q['status']} |"
        )
    tactics = sorted({q["mitre"]["tactic"] for _, q in queries})
    techniques = sorted({t for _, q in queries for t in q["mitre"]["techniques"]})
    lines.append("")
    lines.append(
        f"**{len(queries)} queries** · **{len(tactics)} tactics** · **{len(techniques)} ATT&CK techniques**"
    )
    return "\n".join(lines)


def main():
    write = "--write" in sys.argv
    queries, errors = load_queries()
    if errors:
        print("❌ Validation failed:")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print(f"✅ {len(queries)} queries valid")

    readme = README.read_text(encoding="utf-8")
    head, _, rest = readme.partition(START)
    _, _, tail = rest.partition(END)
    new = f"{head}{START}\n{build_index(queries)}\n{END}{tail}"
    if new != readme:
        if write:
            README.write_text(new, encoding="utf-8")
            print("📝 README index updated")
        else:
            print("❌ README index is out of date. Run: python scripts/validate.py --write")
            sys.exit(1)
    else:
        print("✅ README index up to date")


if __name__ == "__main__":
    main()
