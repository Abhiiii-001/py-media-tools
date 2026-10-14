"""Publish every queued post whose scheduled time (IST) has arrived.

Queue folders are named <YYYY-MM-DD>_<HHMM>_<slug>, time in IST.
Runs in GitHub Actions (creds from env vars) or locally (creds from .env).
"""
import json
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).parent
QUEUE = ROOT / "content" / "queue"
IST = timezone(timedelta(hours=5, minutes=30))


def due_folders(now):
    due = []
    for f in sorted(QUEUE.iterdir()) if QUEUE.exists() else []:
        if not f.is_dir() or not (f / "meta.json").exists():
            continue
        try:
            when = datetime.strptime(f.name[:15], "%Y-%m-%d_%H%M").replace(tzinfo=IST)
        except ValueError:
            print(f"skip (bad name): {f.name}")
            continue
        if when <= now:
            due.append(f)
    return due


def main():
    now = datetime.now(IST)
    due = due_folders(now)
    print(f"{now:%Y-%m-%d %H:%M} IST - {len(due)} due")
    failed = False
    for f in due:
        print(f"publishing {f.name}")
        r = subprocess.run([sys.executable, str(ROOT / "ig_api.py"), "post", str(f)],
                           capture_output=True, text=True, encoding="utf-8")
        print(r.stdout or r.stderr)
        failed |= r.returncode != 0
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
