"""Batch: 16 Nov 2026 (Monday, 2 days out, evergreen):
1300 reel (Monday password expired), 1730 image (Gru's Plan, winter morning walk),
2100 reel (office AC in November) + 3 stories.
Run from repo root: python content/scripts/batch_2026-11-16.py [reels|images|stories]"""


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
    "password-expired": ("2026-11-16_1300_password-expired-reel", [
        dict(dur=2.4, tag="MONDAY 9:30, LAPTOP KHOLA", head="'YOUR PASSWORD HAS EXPIRED'", level=0.6, mood="tired", sfx="ding"),
        dict(dur=2.8, tag="NAYA PASSWORD KE RULES", box="1 capital, 1 number, 1 symbol\nPichhle 5 se alag\n12 character minimum\nYaad bhi rakhna hai", level=0.35,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="MAIN, 7VI KOSHISH PE", draw=reel_template("hide-the-pain"), sfx="tick"),
        dict(dur=3.8, head="10:15 AM", box="Account: locked\nIT ticket: 'within 3 days'\nManager: 'kaam kahan tak?'\nMain: login tak",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Monday ka pehla kaam: password yaad karna, aur wahi nahi hua 🙂
office memes aur monday memes for every thaka hua desi jiska password har 90 din mein mazaak ban jaata hai

Send karo us colleague ko jo har baar 'Password@123' rakhta hai 👇

#thakahuadesi #officememes #mondaymemes #corporatememes #desimemes
"""),
    "office-ac": ("2026-11-16_2100_office-ac-reel", [
        dict(dur=2.4, tag="NOVEMBER, BAHAR 14 DEGREE", head="OFFICE KA AC: 18 PE", level=0.5, mood="tired", sfx="ding"),
        dict(dur=2.8, tag="MERI DESK PE", box="Sweater + jacket\nGaram chai, teesri baar\nHaath: jebon mein\nTyping: ek ungli se", level=0.3,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="COLLEAGUE: 'THODI GARMI HAI NA?'", draw=reel_template("bhushan"), sfx="tick"),
        dict(dur=3.8, head="REMOTE KAHAN HAI?", box="Admin ke paas\nAdmin: 'policy hai'\nMain: 9 ghante kulfi\nGhar pe: geyser kharab",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Bahar sardi, andar Shimla, aur remote admin ki jeb mein 🙂
office memes aur winter memes for every thaka hua desi jo office mein shawl odh ke kaam karta hai

Send karo us colleague ko jo November mein bhi AC 18 pe chalata hai 👇

#thakahuadesi #officememes #wintermemes #corporatememes #desimemes
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
    img = template_meme("gru-plan",
                        "Sardi ka fitness plan:",
                        ["Kal se subah\n6 baje walk", "Alarm laga\ndiya", "Subah 6 baje\nbahar 12 degree", "Subah 6 baje\nbahar 12 degree"],
                        footer="Razai ne plan approve nahi kiya")
    out("2026-11-16_1730_sardi-walk-plan", "image", [img], """
Plan 6 baje ka tha, razai ne 9 baje tak meeting rakh li 🙂
desi memes aur winter memes for every thaka hua desi jiska fitness plan November mein freeze ho jaata hai

Send karo us dost ko jo har sardi 'kal se walk' bolta hai 👇

#thakahuadesi #desimemes #wintermemes #fitnessmemes #relatablememes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-11-16_1000_mood-story", mood_story("Somvaar ki subah", "alarm: 4 baar snooze\ndimaag: abhi bhi Sunday pe\nenergy: 15%", 0.15, "tired"))
    story("2026-11-16_1330_teaser-story", teaser_story("'Password expired'", "naya reel feed pe. bhejo us colleague ko jo har baar Password@123 rakhta hai",
          Q / "2026-11-16_1300_password-expired-reel" / "cover.png"))
    story("2026-11-16_2130_question-story", question_story("Sach batao", "Tumhare office ka AC November mein kitne pe chalta hai?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
