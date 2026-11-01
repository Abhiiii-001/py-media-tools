"""Batch: 3 Nov 2026 (Tuesday, evergreen): 1300 + 2100 reels, 1730 image + 3 stories.
Run from repo root: python content/scripts/batch_2026-11-01.py [reels|images|stories]"""

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
    "six-baje": ("2026-11-03_1300_6-baje-nikalna-reel", [
        dict(dur=2.4, tag="5:55 PM, OFFICE", head="'AAJ 6 BAJE PAKKA NIKAL RAHA HU'", level=0.6, mood="happy", sfx="ding"),
        dict(dur=2.6, tag="PLAN", box="5:57 laptop band\n5:58 bag pack\n5:59 chupke se lift", level=0.7,
             mood="happy", sfx="pop"),
        dict(dur=2.6, tag="6:00 PM, MAIN", draw=reel_template("phir-hera-pheri-run"), sfx="tick"),
        dict(dur=3.8, head="LIFT MEIN MANAGER MILA", box="'Arre perfect timing!\nChalo ek quick call\nle lete hai, walk karte hue'\nGhar 9:40 pe pahuncha",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
6 baje nikalne ka plan har roz banta hai, har roz lift mein marta hai 🙂
office memes aur corporate memes for every thaka hua desi jo bas time pe ghar jaana chahta hai

Send karo us colleague ko jo roz '6 baje pakka' bolta hai 👇

#thakahuadesi #officememes #corporatememes #desimemes #relatablememes
"""),
    "shaadi-sofa": ("2026-11-03_2100_shaadi-mein-fasa-reel", [
        dict(dur=2.4, tag="RELATIVE KI SHAADI", head="'BAS 10 MIN JAAKE AA JAATE HAI'", level=0.5, mood="tired", sfx="ding"),
        dict(dur=2.6, tag="AUNTY NE PAKAD LIYA", box="'Beta package kitna hai?'\n'Itna hi?'\n'Sharma ji ka beta toh...'", level=0.3,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="SOFA PE FASA HUA MAIN", draw=reel_template("welcome-sofa"), sfx="tick"),
        dict(dur=3.8, head="'AUR SHAADI KAB KAR RAHE HO?'", box="Khana abhi laga nahi,\nnikalne ka raasta\naunty ke peeche hai.\n10 min ho gaye 2 ghante",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Shaadi mein khana baad mein milta hai, sawaal pehle 🙂
relatives memes aur desi memes for every thaka hua desi jo shaadi season mein sofa pe fasa hai

Send karo us dost ko jise is shaadi season bhi 'shaadi kab' wala sawaal milega 👇

#thakahuadesi #relativesmemes #shaadiseason #desimemes #indianmemes
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
    img = template_meme("distracted-boyfriend",
                        "Mera har mahine ka self improvement",
                        labels=["Naya course\n'AI seekho\n30 din mein'", "Main", "Pichhle 7\ncourses\n(12% done)"],
                        footer="Cart full, completion 0%")
    out("2026-11-03_1730_naya-course", "image", [img], """
Course kharidna hi sabse bada achievement hai, khatam karna optional 🙂
adulting memes aur office memes for every thaka hua desi jiska 'upskilling' sirf wishlist mein hai

Send karo us dost ko jiske paas 10 adhure courses hai 👇

#thakahuadesi #adultingmemes #officememes #desimemes #relatablememes
""")

def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-11-03_1000_mood-story", mood_story("Tuesday hai", "Monday ka excuse: khatam\nFriday: abhi bahut door\nenergy: 20%", 0.2, "tired"))
    story("2026-11-03_1330_teaser-story", teaser_story("'6 baje pakka nikal raha hu'", "naya reel feed pe. bhejo us colleague ko jo roz late nikalta hai",
          Q / "2026-11-03_1300_6-baje-nikalna-reel" / "cover.png"))
    story("2026-11-03_2130_question-story", question_story("Shaadi season", "Shaadi mein relatives ka sabse irritating sawaal kaunsa hai?"))

if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
