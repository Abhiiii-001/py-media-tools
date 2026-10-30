"""Batch: 1 Nov 2026 (Sunday, 1st of month, evergreen): 1300 + 2100 reels, 1730 image + 3 stories.
Run from repo root: python content/scripts/batch_2026-10-30.py [reels|images|stories]"""

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
    "naya-main": ("2026-11-01_1300_naya-mahina-reel", [
        dict(dur=2.4, tag="1 NOVEMBER", head="NAYA MAHINA, NAYA MAIN", level=0.7, mood="happy", sfx="ding"),
        dict(dur=2.6, tag="IS MAHINE KA PLAN", box="6 baje uthna\nGym jaana\nBudget mein rehna\nGhar ka khana", level=0.6,
             mood="happy", sfx="pop"),
        dict(dur=2.6, tag="1 TAREEKH WALA MAIN", draw=reel_template("raju-waiting-pose"), sfx="tick"),
        dict(dur=3.8, head="PHIR YAAD AAYA", box="Aaj toh Sunday hai.\nNaya main kal se.\nWaise 10 mahine se\n'kal se' hi hai",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Naya mahina har baar aata hai, naya main abhi tak nahi aaya 🙂
desi memes aur adulting memes for every thaka hua desi jiska 'kal se pakka' January se pending hai

Send karo us dost ko jo har 1 tareekh ko 'is baar serious hu' bolta hai 👇

#thakahuadesi #desimemes #adultingmemes #relatablememes #hinglishmemes
"""),
    "pakka-plan": ("2026-11-01_2100_pakka-plan-reel", [
        dict(dur=2.4, tag="GROUP CHAT, MONDAY", head="'IS SUNDAY PAKKA MILTE HAI'", level=0.6, mood="happy", sfx="ding"),
        dict(dur=2.6, tag="SUNDAY, 11 BAJE", box="Ek: 'bhai thoda late'\nDoosra: 'shayad nahi'\nTeesra: seen", level=0.4,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="MAIN, TAIYAAR HOKE", draw=reel_template("ab-tak-aa-jana-chahiye"), sfx="tick"),
        dict(dur=3.8, head="'NEXT SUNDAY PAKKA'", box="Ye 'pakka' 2019 se\nchal raha hai.\nGroup ka naam bhi\n'Goa Plan 2019' hai",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Har Sunday ka plan pakka hota hai, bas hum log nahi 🙂
dosti memes aur desi memes for every group chat jiska 'pakka plan' kabhi plan se aage nahi gaya

Send karo apne group mein, dekhte hai is baar kaun 'seen' karke chhodta hai 👇

#thakahuadesi #dostimemes #desimemes #friendsmemes #relatablememes
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
    img = template_meme("they-dont-know",
                        "Sunday shaam family ke saath hasta hua main. Inhe nahi pata kal 10 baje wali presentation ki ek slide bhi nahi bani",
                        labels=None,
                        footer="Chehra Sunday, dimaag Monday")
    out("2026-11-01_1730_sunday-presentation", "image", [img], """
Bahar se Sunday, andar se Monday 9:59 AM 🙂
office memes aur sunday memes for every thaka hua desi jiski presentation abhi bhi 'Untitled' hai

Send karo us colleague ko jiski kal wali slide abhi tak khaali hai 👇

#thakahuadesi #officememes #sundaymemes #corporatememes #desimemes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-11-01_1000_mood-story", mood_story("1 tareekh + Sunday", "naya mahina: shuru\nnaya main: kal se\nenergy: 30%", 0.3, "happy"))
    story("2026-11-01_1330_teaser-story", teaser_story("Naya mahina, naya main", "naya reel feed pe. bhejo us dost ko jo har mahine 'kal se' bolta hai",
          Q / "2026-11-01_1300_naya-mahina-reel" / "cover.png"))
    story("2026-11-01_2130_question-story", question_story("Sach batao", "Tumhare group ka 'pakka plan' last kab sach mein hua tha?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
