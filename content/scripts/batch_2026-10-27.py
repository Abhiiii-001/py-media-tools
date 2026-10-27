"""Batch: 29 Oct 2026 (Thursday, evergreen): 1300 reel, 1730 image, 2100 reel + 3 stories.
Run from repo root: python content/scripts/batch_2026-10-27.py [reels|images|stories]"""

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
    "cab": ("2026-10-29_1300_cab-cancel-reel", [
        dict(dur=2.4, tag="OFFICE KE LIYE CAB BOOK KIYA", head="'DRIVER 2 MIN AWAY'", level=0.5, mood="happy", sfx="ding"),
        dict(dur=2.6, tag="15 MINUTE BAAD", box="Ab bhi '2 min away'.\nGaadi wahi ki wahi,\nmain wahi ka wahi", level=0.35,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="PHIR RIDE CANCEL HUI", draw=reel_template("dekh-raha-hai-binod"), sfx="tick"),
        dict(dur=3.8, head="CANCEL USNE KIYA", box="Cancellation fee\nmujhse kati.\nLate mark bhi mujhe laga",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
'2 min away' wala 2 minute aaj tak kisi ne nahi dekha 🙂
office memes aur traffic memes for every thaka hua desi jo roz cab ke chakkar mein late hota hai

Send karo us colleague ko jiska bahana roz 'cab cancel ho gayi' hota hai 👇

#thakahuadesi #officememes #trafficmemes #desimemes #relatablememes
"""),
    "episode": ("2026-10-29_2100_bas-ek-episode-reel", [
        dict(dur=2.4, tag="RAAT 11 BAJE", head="'BAS EK EPISODE, PHIR SO JAUNGA'", level=0.55, mood="happy", sfx="ding"),
        dict(dur=2.6, tag="1:30 AM", box="Screen: 'Next episode\nin 5... 4...'\nMain: 'ye last wala'", level=0.35,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="3 AM: SOYA HI NAHI TOH LATE KAISE UTHUNGA", draw=reel_template("roll-safe"), sfx="tick"),
        dict(dur=3.8, head="9:30 AM STANDUP", box="Sir: 'kal kya kiya?'\nMain: 'research'.\nAankh abhi bhi band",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
'Bas ek episode' bola tha, poora season aur neend dono gaye 🙂
ott memes aur office memes for every thaka hua desi jo 3 baje so ke 9 baje standup mein 'research' bolta hai

Send karo us dost ko jo 'bas ek episode' bolke subah ki chai dekhta hai 👇

#thakahuadesi #ottmemes #officememes #desimemes #relatablememes
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
    img = template_meme("clown-makeup",
                        "Har mahine ka budget plan:",
                        labels=["Is mahine paise bachaunga", "Excel sheet bhi bana di",
                                "Bas ek chhota sa order", "29 tareekh: Rs 312 bache"],
                        footer="Excel mein savings, account mein clown")
    out("2026-10-29_1730_budget-clown", "image", [img], """
Budget Excel mein perfect tha, account ne padha hi nahi 🙂
salary memes aur middle class memes for every thaka hua desi jo 29 tareekh ko hi broke ho jaata hai

Send karo us dost ko jo har 1 tareekh ko 'is mahine pakka bachaunga' bolta hai 👇

#thakahuadesi #salarymemes #middleclassmemes #desimemes #relatablememes
""")

def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-10-29_1000_mood-story", mood_story("Thursday hai", "Friday: bas kal\nsalary: 3 din door\nenergy: 31%", 0.31, "tired"))
    story("2026-10-29_1330_teaser-story", teaser_story("'Driver 2 min away'", "naya reel feed pe. bhejo us colleague ko jiski cab roz cancel hoti hai",
          Q / "2026-10-29_1300_cab-cancel-reel" / "cover.png"))
    story("2026-10-29_2130_question-story", question_story("Sach batao", "'Bas ek episode' bolke sabse late kitne baje soye ho?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
