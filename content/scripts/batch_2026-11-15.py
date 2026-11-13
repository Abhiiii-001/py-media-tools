"""Batch: 15 Nov 2026 (Sunday, 2 days out, evergreen):
1300 reel (Sunday screen time report), 1730 = backlog carousel '15 taareekh' (moved from content/backlog/),
2100 reel (Sunday meal prep) + 3 stories.
Run from repo root: python content/scripts/batch_2026-11-15.py [reels|stories]"""


import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from brand import *  # noqa: E402,F403
from memes import reel_template  # noqa: E402
from reel import render_reel  # noqa: E402
from stories import mood_story, question_story, teaser_story  # noqa: E402

Q = ROOT / "content" / "queue"

REELS = {
    "screen-time": ("2026-11-15_1300_screen-time-reel", [
        dict(dur=2.4, tag="SUNDAY SUBAH, PHONE KA NOTIFICATION", head="'WEEKLY SCREEN TIME REPORT'", level=0.7, mood="happy", sfx="ding"),
        dict(dur=2.8, tag="ROZ KA AVERAGE", box="Instagram: 4 ghante\nYouTube: 2 ghante\nKaam ki app: 11 minute\nTotal: 7 ghante 48 min", level=0.35,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="MAIN, REPORT PADH KE", draw=reel_template("monkey-puppet"), sfx="tick"),
        dict(dur=3.8, head="5 SECOND BAAD", box="Report: swipe karke hata di\nReels: phir se chalu\nSunday: 9 ghante wala\nBahana: 'chhutti hai yaar'",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Phone ne sach bataya, maine phone se hi sach chhupa liya 🙂
desi memes aur relatable memes for every thaka hua desi jiska screen time uski neend se zyada hai

Send karo us dost ko jo 'main toh phone kam chalata hu' bolta hai 👇

#thakahuadesi #desimemes #relatablememes #sundaymemes #indianmemes
"""),
    "meal-prep": ("2026-11-15_2100_meal-prep-reel", [
        dict(dur=2.4, tag="SUNDAY SHAAM KA JOSH", head="'IS HAFTE SIRF GHAR KA KHANA'", level=0.7, mood="happy", sfx="ding"),
        dict(dur=2.8, tag="PLAN", box="7 din ka khana aaj banega\n7 dabbe fridge mein\nSwiggy: uninstall\nPaisa: bach jaayega", level=0.45,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="MAIN: 'KITNA SMART HU MAIN'", draw=reel_template("roll-safe"), sfx="tick"),
        dict(dur=3.8, head="AGLA SUNDAY", box="Dabbe: 6 abhi bhi fridge mein\nSwiggy: wapas install\nKhana: khol ke dekhne ki\nhimmat nahi",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
7 din ka khana banaya tha, 6 din Swiggy ne khilaya 🙂
bachelor life memes aur desi memes for every thaka hua desi jiska fridge dabbon ka museum hai

Send karo us roommate ko jiske dabbe abhi bhi fridge mein pade hai 👇

#thakahuadesi #bachelorlife #desimemes #sundaymemes #relatablememes
"""),
}


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-11-15_1000_mood-story", mood_story("Ravivaar ki subah", "uthe: 11:40 AM\nnashta: lunch ke saath\nenergy: 70% (Monday tak 0)", 0.7, "happy"))
    story("2026-11-15_1330_teaser-story", teaser_story("Screen time report", "naya reel feed pe. bhejo us dost ko jo 'phone kam chalata hu' bolta hai",
          Q / "2026-11-15_1300_screen-time-reel" / "cover.png"))
    story("2026-11-15_2130_question-story", question_story("Sach batao", "Sunday ko banaya khana kis din tak chalta hai?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "stories" in what:
        stories()
