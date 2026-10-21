#!/usr/bin/env python3
"""Daily Python Deep Dive lab tracker: date blocks with direct GitHub lab links."""
from __future__ import annotations

import json
from collections import defaultdict
from datetime import date
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent
PROGRESS_DIR = ROOT / "progress"
LOG_FILE = PROGRESS_DIR / "work_log.json"
REPORT_FILE = PROGRESS_DIR / "PROOF_OF_COMPLETION.md"
REPO_URL = "https://github.com/kadiwalarman1-rgb/python-deep-dive"


def load_entries():
    if not LOG_FILE.exists():
        return []
    try:
        data = json.loads(LOG_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError) as exc:
        raise SystemExit(f"Could not read {LOG_FILE}: {exc}")


def save_entries(entries):
    PROGRESS_DIR.mkdir(parents=True, exist_ok=True)
    LOG_FILE.write_text(
        json.dumps(entries, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def lab_link(lab):
    clean = str(lab).strip()
    if clean.lower().startswith("lab "):
        folder = "Lab " + clean[4:].strip()
        return f"{REPO_URL}/tree/main/{quote(folder, safe='')}"
    return REPO_URL


def grouped_entries(entries):
    groups = defaultdict(list)
    for entry in entries:
        groups[entry.get("date", "Unknown date")].append(entry)
    return dict(sorted(groups.items(), reverse=True))


def add_entry():
    print("\n=== Add Daily Lab Progress ===")
    work_date = input(f"Date [{date.today().isoformat()}]: ").strip() or date.today().isoformat()
    try:
        date.fromisoformat(work_date)
    except ValueError:
        print("Invalid date. Use YYYY-MM-DD.")
        return

    lab = input("Lab name/number (e.g. Lab 40): ").strip()
    if not lab:
        print("Lab name is required.")
        return

    entries = load_entries()
    if any(
        e.get("date") == work_date
        and e.get("lab", "").casefold() == lab.casefold()
        for e in entries
    ):
        print(f"{lab} is already recorded for {work_date}.")
        return

    entries.append({"date": work_date, "lab": lab})
    entries.sort(key=lambda e: (e.get("date", ""), e.get("lab", "").casefold()))
    save_entries(entries)
    write_report(entries)
    print(f"Added {lab} under {work_date}.")
    print(f"GitHub link: {lab_link(lab)}")


def list_entries():
    groups = grouped_entries(load_entries())
    if not groups:
        print("No labs recorded. Run: python progress_tracker.py add")
        return

    print("\n========== LAB PROGRESS ==========")
    for day, items in groups.items():
        print(f"\n{day}")
        for item in items:
            lab = item.get("lab", "Lab")
            print(f"- {lab}: {lab_link(lab)}")


def write_report(entries):
    groups = grouped_entries(entries)
    lines = ["# Python Deep Dive Progress", ""]
    if not groups:
        lines.extend(["No labs recorded yet.", ""])
    for day, items in groups.items():
        lines.extend([f"## {day}", ""])
        seen = set()
        for item in items:
            lab = item.get("lab", "Lab")
            key = lab.casefold()
            if key in seen:
                continue
            seen.add(key)
            lines.append(f"- [{lab}]({lab_link(lab)})")
        lines.append("")

    PROGRESS_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_FILE.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Show Python Deep Dive labs grouped by date with direct GitHub links."
    )
    parser.add_argument("command", choices=("add", "list", "report"))
    args = parser.parse_args()

    entries = load_entries()
    if args.command == "add":
        add_entry()
    elif args.command == "list":
        list_entries()
    else:
        write_report(entries)
        print(f"Report generated: {REPORT_FILE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
