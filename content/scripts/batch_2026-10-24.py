"""Batch: 26 Oct 2026 (Monday, evergreen): 1300 reel, 1730 image, 2100 reel + 3 stories.
Run from repo root: python content/scripts/batch_2026-10-24.py [reels|images|stories]"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from brand import *  # noqa: E402,F403
from memes import reel_template, template_meme  # noqa: E402
from reel import render_reel  # noqa: E402
from stories import mood_story, question_story, teaser_story  # noqa: E402

Q = ROOT / "content" / "queue"

REELS = {
    "weekend": ("2026-10-26_1300_weekend-kaisa-reel", [
        dict(dur=2.4, tag="MONDAY, 10:05 AM", head="MANAGER: 'WEEKEND KAISA RAHA?'", level=0.5, mood="tired", sfx="ding"),
        dict(dur=2.6, tag="ASLI WEEKEND", box="Saturday: 6 baje neend khul gayi\nSunday: mummy ka 'bas ek kaam'\nAaram: 0 ghante", level=0.3,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="MAIN, MUSKURATE HUE", draw=reel_template("hide-the-pain"), sfx="tick"),
        dict(dur=3.8, head="'BAHUT BADHIYA SIR, FRESH HU'", box="Fresh sirf chehre pe hai,\nandar se\nFriday ka wait shuru",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
'Weekend kaisa raha?' ka sach bata diya toh appraisal bhi jaayega 🙂
office memes aur monday memes for every thaka hua desi jo 10 baje se Friday gin raha hai

Send karo us colleague ko jo har Monday 'fresh hu' bolta hai 👇

#thakahuadesi #officememes #mondaymemes #desimemes #corporatelife
"""),
    "maps": ("2026-10-26_2100_maps-jhooth-reel", [
        dict(dur=2.4, tag="MONDAY, 9:15 AM", head="MAPS: 'OFFICE 22 MIN'", level=0.6, mood="happy", sfx="ding"),
        dict(dur=2.6, tag="9:40 AM", box="Wahi signal\nwahi auto\nmaps: 'aap sabse fast route pe ho'", level=0.4,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="10:30 AM, ABHI BHI RAASTE MEIN", draw=reel_template("waiting-skeleton"), sfx="tick"),
        dict(dur=3.8, head="MANAGER: 'JALDI NIKLA KARO'", box="Sir jaldi hi nikla tha,\nbas Google Maps\njhooth bolta hai",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
22 minute bola tha, 75 lage, aur late main hu 🙂
office memes aur traffic memes for every thaka hua desi jiska Monday raaste mein hi khatam ho jaata hai

Send karo us dost ko jo roz 'bas 5 min mein pahunch raha hu' bolta hai 👇

#thakahuadesi #officememes #mondaymemes #trafficmemes #desimemes
"""),
}

def out(folder, kind, slides, caption):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    names = []
    for i, img in enumerate(slides, 1):
        n = f"{i}.png"
        save(img, f / n)
        names.append(n)
    (f / "caption.txt").write_text(caption.strip() + "\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": kind, "media": names}, indent=2), encoding="utf-8")
    print("built", folder, len(slides), "slides")


def images():
    img = template_meme("two-buttons",
                        "Monday, 7:45 AM:",
                        labels=["Leave le lu", "Office jaake rou", "Main"],
                        footer="Dono mein salary same, dard alag")
    out("2026-10-26_1730_monday-buttons", "image", [img], """
Monday subah ka sabse bada decision, aur dono option galat 🙂
monday memes aur office memes for every thaka hua desi jo 7:45 pe bistar mein meeting kar raha hai

Send karo us dost ko jo har Monday sick leave ka draft likh ke delete karta hai 👇

#thakahuadesi #mondaymemes #officememes #desimemes #relatablememes
""")

def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-10-26_1000_mood-story", mood_story("Monday hai", "alarm: 4 baar snooze\nchai: 2 glass\nenergy: 9%", 0.1, "tired"))
    story("2026-10-26_1330_teaser-story", teaser_story("'Weekend kaisa raha?'", "naya reel feed pe. bhejo us colleague ko jo har Monday 'fresh hu' bolta hai",
          Q / "2026-10-26_1300_weekend-kaisa-reel" / "cover.png"))
    story("2026-10-26_2130_question-story", question_story("Sach batao", "Monday ko 'weekend kaisa raha' pe kabhi sach bola hai?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
