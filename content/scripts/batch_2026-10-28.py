"""Batch: 30 Oct 2026 (Friday, evergreen): 1300 reel, 1730 image + 3 stories.
2100 = backlog saturday-alarm reel (moved in, not rebuilt).
Run from repo root: python content/scripts/batch_2026-10-28.py [reels|images|stories]"""

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
    "call": ("2026-10-30_1300_pahunch-ke-call-reel", [
        dict(dur=2.4, tag="GHAR SE NIKALTE WAQT MUMMY", head="'PAHUNCH KE CALL KARNA'", level=0.55, mood="happy", sfx="ding"),
        dict(dur=2.6, tag="PAHUNCH GAYA", box="Phone silent pe.\nCall karna bhool gaya.\n3 ghante nikal gaye", level=0.35,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="PHONE KHOLA: 23 MISSED CALLS, MUMMY", draw=reel_template("dhak-dhak"), sfx="tick"),
        dict(dur=3.8, head="CALL BACK KIYA", box="'Pahunch gaya?' 'Haan'.\nPhir 40 minute lecture\n'call karna' pe",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Pahunch toh gaya tha, bas call karna nahi pahuncha 🙂
indian mom memes aur desi memes for every beta jiska phone silent pe aur mummy ka BP high pe hota hai

Send karo us dost ko jo kabhi 'pahunch ke call' nahi karta 👇

#thakahuadesi #indianmommemes #desimemes #indianparents #relatablememes
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
    img = template_meme("trade-offer",
                        "Month end pe bank ka trade offer:",
                        labels=["Rs 590 'minimum\nbalance' charge", "Ek SMS:\n'Dear Customer'"],
                        footer="Balance minimum, charge maximum")
    out("2026-10-30_1730_bank-trade-offer", "image", [img], """
Balance minimum tha, charge pura maximum kaat liya 🙂
salary memes aur middle class memes for every thaka hua desi jiska account month end pe 3 digit pe aa jaata hai

Send karo us dost ko jiska balance bhi abhi 'Dear Customer' wala hai 👇

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
    story("2026-10-30_1000_mood-story", mood_story("Friday hai", "weekend: 6 baje\nkaam: Monday\nenergy: 9%", 0.09, "tired"))
    story("2026-10-30_1330_teaser-story", teaser_story("'Pahunch ke call karna'", "naya reel feed pe. bhejo us dost ko jo kabhi call nahi karta",
          Q / "2026-10-30_1300_pahunch-ke-call-reel" / "cover.png"))
    story("2026-10-30_2130_question-story", question_story("Sach batao", "Saturday ko bina alarm ke kitne baje uth jaate ho?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
