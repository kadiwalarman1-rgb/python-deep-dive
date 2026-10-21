#!/usr/bin/env python3
"""Track daily work and attach verifiable GitHub commit links.

Usage:
    python3 progress_tracker.py add
    python3 progress_tracker.py list
    python3 progress_tracker.py report
"""
from __future__ import annotations

import json
import subprocess
from datetime import date, datetime
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
PROGRESS_DIR = ROOT / "progress"
LOG_FILE = PROGRESS_DIR / "work_log.json"
REPORT_FILE = PROGRESS_DIR / "PROOF_OF_COMPLETION.md"


def load_entries() -> list[dict]:
    if not LOG_FILE.exists():
        return []
    try:
        data = json.loads(LOG_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError) as exc:
        raise SystemExit(f"Could not read {LOG_FILE}: {exc}")


def save_entries(entries: list[dict]) -> None:
    PROGRESS_DIR.mkdir(parents=True, exist_ok=True)
    LOG_FILE.write_text(
        json.dumps(entries, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def latest_commit() -> dict:
    """Read the current local Git commit; never invent a commit URL."""
    def git(*args: str) -> str:
        result = subprocess.run(
            ["git", "-C", str(ROOT), *args],
            capture_output=True, text=True, check=True,
        )
        return result.stdout.strip()

    try:
        sha = git("rev-parse", "HEAD")
        subject = git("log", "-1", "--pretty=%s")
        committed_at = git("log", "-1", "--pretty=%cI")
        remote = git("remote", "get-url", "origin")
    except (subprocess.CalledProcessError, FileNotFoundError):
        return {"sha": "", "message": "", "url": "", "committed_at": ""}

    remote = remote.removesuffix(".git")
    if remote.startswith("git@github.com:"):
        repo_path = remote.removeprefix("git@github.com:")
        url = f"https://github.com/{repo_path}/commit/{sha}"
    else:
        parsed = urlparse(remote)
        if parsed.hostname == "github.com":
            url = f"https://github.com{parsed.path}/commit/{sha}"
        else:
            url = ""

    return {
        "sha": sha,
        "message": subject,
        "url": url,
        "committed_at": committed_at,
    }


def prompt(label: str, required: bool = True) -> str:
    while True:
        value = input(f"{label}: ").strip()
        if value or not required:
            return value
        print("This field is required.")


def add_entry() -> None:
    print("\n=== Add Daily Work Log ===")
    work_date = input(f"Date [{date.today().isoformat()}]: ").strip()
    if not work_date:
        work_date = date.today().isoformat()
    try:
        date.fromisoformat(work_date)
    except ValueError:
        print("Invalid date. Use YYYY-MM-DD.")
        return

    lab = prompt("Lab / topic (e.g. Lab 40)")
    work = prompt("What did you work on?")
    learned = prompt("What did you learn?", required=False)
    status = input("Status [completed/in-progress] (default completed): ").strip().lower()
    if not status:
        status = "completed"
    if status not in {"completed", "in-progress"}:
        print("Status must be 'completed' or 'in-progress'.")
        return

    commit = latest_commit()
    if commit["sha"]:
        print(f"Latest local commit: {commit['sha'][:7]} — {commit['message']}")
        if not commit["url"]:
            print("GitHub origin URL was not detected; commit link will be omitted.")
    else:
        print("Git commit not found. Entry will be saved without commit proof.")

    attach = input("Attach this latest commit? [Y/n]: ").strip().lower()
    if attach in {"n", "no"}:
        commit = {"sha": "", "message": "", "url": "", "committed_at": ""}

    entries = load_entries()
    entry = {
        "date": work_date,
        "recorded_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "lab": lab,
        "work": work,
        "learned": learned,
        "status": status,
        "commit_sha": commit["sha"],
        "commit_message": commit["message"],
        "commit_url": commit["url"],
        "commit_date": commit["committed_at"],
    }
    entries.append(entry)
    entries.sort(key=lambda item: (item.get("date", ""), item.get("recorded_at", "")))
    save_entries(entries)
    write_report(entries)
    print(f"Saved. Daily log: {LOG_FILE.relative_to(ROOT)}")
    print(f"Report updated: {REPORT_FILE.relative_to(ROOT)}")


def list_entries() -> None:
    entries = load_entries()
    if not entries:
        print("No work logs yet. Run: python3 progress_tracker.py add")
        return
    print("\n=== Daily Work Log ===")
    for item in entries:
        print(f"\n{item.get('date', 'Unknown date')} | {item.get('lab', 'No lab')} | {item.get('status', 'unknown')}")
        print(f"  Work: {item.get('work', '')}")
        if item.get("learned"):
            print(f"  Learned: {item['learned']}")
        if item.get("commit_url"):
            print(f"  Commit: {item['commit_url']}")
        elif item.get("commit_sha"):
            print(f"  Commit SHA: {item['commit_sha']} (no GitHub URL detected)")


def write_report(entries: list[dict]) -> None:
    completed = sum(item.get("status") == "completed" for item in entries)
    lines = [
        "# Proof of Completion",
        "",
        "> Generated from progress/work_log.json. Each entry is a self-reported work log; commit links point to Git history when available.",
        "",
        f"- **Total work-log entries:** {len(entries)}",
        f"- **Completed entries:** {completed}",
        f"- **In-progress entries:** {len(entries) - completed}",
        "",
    ]
    if not entries:
        lines.extend(["No entries recorded yet.", ""])
    else:
        lines.extend(["## Daily Records", ""])
        for item in reversed(entries):
            lines.extend([
                f"### {item.get('date', 'Unknown date')} — {item.get('lab', 'No lab')}",
                "",
                f"- **Status:** {item.get('status', 'unknown')}",
                f"- **Work completed:** {item.get('work', '')}",
            ])
            if item.get("learned"):
                lines.append(f"- **What I learned:** {item['learned']}")
            if item.get("commit_url"):
                lines.append(f"- **GitHub commit:** [{item.get('commit_sha', '')[:7]} — {item.get('commit_message', 'View commit')}]({item['commit_url']})")
            elif item.get("commit_sha"):
                lines.append(f"- **Commit SHA:** {item['commit_sha']} (GitHub link unavailable)")
            else:
                lines.append("- **GitHub commit:** Not attached")
            lines.append("")

    PROGRESS_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_FILE.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def create_report() -> None:
    entries = load_entries()
    write_report(entries)
    print(f"Report generated: {REPORT_FILE.relative_to(ROOT)}")
    print(f"Entries: {len(entries)}")


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Daily work log and GitHub commit proof tracker.")
    parser.add_argument("command", choices=("add", "list", "report"), help="add a log, list logs, or generate the report")
    args = parser.parse_args()

    if args.command == "add":
        add_entry()
    elif args.command == "list":
        list_entries()
    else:
        create_report()


if __name__ == "__main__":
    main()
