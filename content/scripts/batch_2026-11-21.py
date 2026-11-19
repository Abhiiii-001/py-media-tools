"""Batch made 19 Nov 2026 (9 AM run).
Fill Sat 21 Nov (2 days out, evergreen): 1300 reel (Saturday 'aaj ghar pe hai na' chores list), 1730 image
(Drake: weekend plan vs 'kal milte hai'), 1000 mood + 1330 teaser stories. 2100 reel + 2130 question story are the
backlog `wifi-gaya` pair (gap filler). No trend swap (nothing fresh verified).
Run from repo root: python content/scripts/batch_2026-11-21.py [reels|images|stories]"""

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
    "ghar-pe-hai-na": ("2026-11-21_1300_ghar-pe-hai-na-reel", [
        dict(dur=2.4, tag="SATURDAY, CHUTTI KA DIN", head="'AAJ SIRF AARAM KARUNGA'", level=0.8, mood="happy", sfx="ding"),
        dict(dur=2.9, tag="MUMMY: 'AAJ GHAR PE HAI NA?'", box="Cylinder book kar\nBijli ka bill bhar\nDarzi se kapde le aa\nPankha bhi saaf kar dena", level=0.4,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="'DOST BULA RAHA HAI' BOLKE NIKALTE HUE", draw=reel_template("phir-hera-pheri-run"), sfx="tick"),
        dict(dur=3.8, head="SHAAM 7 BAJE", box="Dost ka phone band\nMummy ki list 2 kaam lambi\nPankha abhi bhi ganda\nMonday ka wait kar raha hu",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Chutti meri thi, plan mummy ka tha 🙂
desi memes aur indian mom memes for every thaka hua desi jiska weekend 'aaj ghar pe hai na' se shuru hota hai

Send karo us bhai/behen ko jo har Saturday 'dost bula raha hai' bolke bhaag jaata hai 👇

#thakahuadesi #desimemes #indianmommemes #weekendmemes #relatablememes
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
    img = template_meme("drake",
                        "Group pe Saturday night ka plan",
                        labels=["Bahar milte hai, pakka", "10 baje: 'kal milte hai yaar, thak gaya'"],
                        footer="Plan har hafte, milna saal mein ek baar")
    out("2026-11-21_1730_kal-milte-hai", "image", [img], """
Group mein 14 log, plan mein 14 bahane 🙂
dosti memes aur weekend memes for every thaka hua desi jiska Saturday plan WhatsApp pe hi poora ho jaata hai

Send karo us dost ko jo har baar last moment pe 'kal pakka' bolta hai 👇

#thakahuadesi #dostimemes #weekendmemes #desimemes #relatablememes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-11-21_1000_mood-story", mood_story("Shanivaar ki subah", "chutti hai\npar mummy ki list\npehle se ready hai\nenergy: 70% (abhi tak)", 0.7, "happy"))
    story("2026-11-21_1330_teaser-story", teaser_story("'Aaj ghar pe hai na?'", "naya reel feed pe. bhejo us bhai/behen ko jo har Saturday bhaag jaata hai",
          Q / "2026-11-21_1300_ghar-pe-hai-na-reel" / "cover.png"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
