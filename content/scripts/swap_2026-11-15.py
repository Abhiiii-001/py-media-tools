"""Trend swap (run 14 Nov 4 PM IST): Sun 15 Nov 1300 reel -> IND vs NZ 5th ODI (Mount Maunganui, 7:30 AM IST start).
Old 1300 `screen-time` reel + its 1330 teaser moved to content/backlog/ (Sunday evergreen, reuse a later Sunday).
Joke is about waking up early for a match on a Sunday, result-agnostic, no players named.
Run from repo root: python content/scripts/swap_2026-11-15.py"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from memes import reel_template  # noqa: E402
from reel import render_reel  # noqa: E402
from stories import teaser_story  # noqa: E402

Q = ROOT / "content" / "queue"
FOLDER = "2026-11-15_1300_sunday-match-alarm-reel"

BEATS = [
    dict(dur=2.4, tag="OFFICE WALE DIN", head="ALARM: 5 BAAR SNOOZE", level=0.25, mood="tired", sfx="ding"),
    dict(dur=2.8, tag="SUNDAY, INDIA KA MATCH 7:30 AM", box="Uth gaya: 7:05, bina alarm\nChai: ready\nTV: on\nNeend: 'zaroorat hi nahi'",
         level=0.85, mood="happy", sfx="pop"),
    dict(dur=2.6, tag="MAIN, 7:29 PE SOFA PE", draw=reel_template("abhi-maza-ayega"), sfx="tick"),
    dict(dur=3.8, head="SHAAM 4 BAJE", box="Match: khatam\nMain: 'bas 10 min let raha hu'\nUtha: raat 9 baje\nSunday: gaya. Kal Monday.",
         level=0.05, mood="dead", sfx="trombone", shake=True),
]

CAPTION = """
Office ke liye 5 snooze, match ke liye 7 baje bina alarm 🙂
cricket memes aur sunday memes for every thaka hua desi jiska Sunday match aur neend mein khatam ho gaya

Send karo us dost ko jo aaj subah 7 baje se TV ke saamne hai 👇

#thakahuadesi #cricketmemes #indvsnz #sundaymemes #desimemes
"""


def main():
    render_reel(BEATS, Q / FOLDER, CAPTION)
    f = Q / "2026-11-15_1330_teaser-story"
    f.mkdir(parents=True, exist_ok=True)
    teaser_story("Match wala Sunday", "naya reel feed pe. bhejo us dost ko jo 7 baje se TV ke saamne hai",
                 Q / FOLDER / "cover.png").save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built teaser")


if __name__ == "__main__":
    main()
