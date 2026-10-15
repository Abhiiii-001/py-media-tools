"""Always-on publisher for GitHub Actions (public repo = free minutes).

Stays awake for up to ~5h40m: publishes due queue items on time, pulls new items pushed by the
content routine every 10 min, commits published state, then re-dispatches itself so the chain never
depends on GitHub's unreliable cron. Cron/push triggers only restart the chain if it ever breaks.
"""
import subprocess
import sys
import time
from datetime import datetime

from publish_due import IST, QUEUE, due_folders

RUN_SECONDS = 5 * 3600 + 40 * 60
CHECK_EVERY = 600


def sh(*cmd, check=False):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if r.returncode and check:
        print(r.stdout, r.stderr)
        raise SystemExit(r.returncode)
    return r


def sync():
    sh("git", "pull", "--rebase", "-q")


def save():
    sh("git", "add", "-A", "content")
    if sh("git", "diff", "--cached", "--quiet").returncode:
        sh("git", "commit", "-q", "-m", "Published due posts")
        for _ in range(3):
            if sh("git", "push", "-q").returncode == 0:
                return
            sync()
        print("push failed after retries")


def next_due():
    times = []
    for f in QUEUE.iterdir() if QUEUE.exists() else []:
        try:
            times.append(datetime.strptime(f.name[:15], "%Y-%m-%d_%H%M").replace(tzinfo=IST))
        except ValueError:
            pass
    return min(times) if times else None


FAILS = {}


def publish_now():
    changed = False
    for f in due_folders(datetime.now(IST)):
        print(f"{datetime.now(IST):%H:%M} publishing {f.name}", flush=True)
        r = sh(sys.executable, "ig_api.py", "post", str(f))
        print(r.stdout or r.stderr, flush=True)
        if r.returncode == 0:
            changed = True
            continue
        FAILS[f.name] = FAILS.get(f.name, 0) + 1
        if FAILS[f.name] >= 3:
            # don't retry a broken item forever: park it so the rest of the day stays on schedule
            dest = QUEUE.parent / "failed" / f.name
            dest.parent.mkdir(exist_ok=True)
            f.rename(dest)
            changed = True
    return changed


def main():
    start = time.time()
    while time.time() - start < RUN_SECONDS:
        sync()
        if publish_now():
            save()
        nd = next_due()
        if nd is None:
            print("queue empty, waiting for the content routine")
        wait = CHECK_EVERY if nd is None else max(60, min(CHECK_EVERY, (nd - datetime.now(IST)).total_seconds()))
        time.sleep(wait)
    print("run window over, handing off to the next run")


if __name__ == "__main__":
    main()
