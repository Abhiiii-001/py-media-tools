"""Batch: 31 Oct 2026 (Saturday, evergreen): 1300 + 2100 reels, 1730 image + 3 stories.
Run from repo root: python content/scripts/batch_2026-10-29.py [reels|images|stories]"""

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
    "udhaar": ("2026-10-31_1300_udhaar-dost-reel", [
        dict(dur=2.4, tag="6 MAHINE SE GAYAB DOST", head="'BHAI KAISA HAI? BAHUT YAAD AAYI'", level=0.6, mood="happy", sfx="ding"),
        dict(dur=2.6, tag="MAIN", box="Itna pyaar?\nShayad mera Rs 2000\nlautane wala hai", level=0.5,
             mood="happy", sfx="pop"),
        dict(dur=2.6, tag="USKA AGLA MESSAGE", draw=reel_template("paisa-laya"), sfx="tick"),
        dict(dur=3.8, head="'BHAI 3000 DE DE'", box="Purane 2000 ka\nzikr bhi nahi.\nAb total 5000 ka dost hai",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Yaad bhi tab aati hai jab wallet khaali hota hai 🙂
dosti memes aur desi memes for everyone jiske Rs 2000 kisi dost ke paas 'bas next week tak' pade hai

Send karo us dost ko jisne abhi tak tumhara udhaar nahi lautaya 👇

#thakahuadesi #dostimemes #desimemes #friendsmemes #relatablememes
"""),
    "saturday": ("2026-10-31_2100_saturday-raat-reel", [
        dict(dur=2.4, tag="SATURDAY RAAT, 8 BAJE", head="DOST: 'AAJ BAHAR CHALTE HAI'", level=0.6, mood="happy", sfx="ding"),
        dict(dur=2.8, tag="18 SAAL vs 26 SAAL", draw=reel_template("buff-doge-cheems",
             ["18 mein:\n'raat 3 baje\ntak bahar'", "26 mein:\n'thak gaya\nhu bhai'"]), sfx="tick"),
        dict(dur=2.6, tag="9:30 PM", box="Khichdi kha li.\nLights band.\nPhone: 'bas 5 min'", level=0.3,
             mood="tired", sfx="pop"),
        dict(dur=3.8, head="2:47 AM", box="Jaag toh raat 3 baje\ntak hi raha hu.\nBas bina mazze ke",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Party ke liye thaka hua, reels ke liye full energy 🙂
weekend memes aur adulting memes for every 25+ thaka hua desi jiska Saturday night khichdi pe khatam hota hai

Send karo us dost ko jo har baar 'thak gaya hu bhai' bolke mana karta hai 👇

#thakahuadesi #weekendmemes #adultingmemes #desimemes #relatablememes
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
    img = template_meme("two-guys-bus",
                        "Saturday subah 9 baje:",
                        labels=["Main: alternate\nSaturday working", "Dost: 'bhai\nbrunch chalein?'"],
                        footer="Ek hi bus, alag alag Saturday")
    out("2026-10-31_1730_alternate-saturday", "image", [img], """
Ek hi bus, bas meri window pe pahaad hai 🙂
office memes aur corporate memes for every thaka hua desi jiska alternate Saturday bhi office ka hai

Send karo us colleague ko jo aaj bhi office mein hai 👇

#thakahuadesi #officememes #corporatememes #desimemes #relatablememes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-10-31_1000_mood-story", mood_story("Saturday hai", "alarm: band\nplan: kuch nahi\nenergy: 40%", 0.4, "happy"))
    story("2026-10-31_1330_teaser-story", teaser_story("'Bhai kaisa hai?'", "naya reel feed pe. bhejo us dost ko jiske paas tumhara udhaar hai",
          Q / "2026-10-31_1300_udhaar-dost-reel" / "cover.png"))
    story("2026-10-31_2130_question-story", question_story("Sach batao", "Saturday raat: bahar party ya ghar pe khichdi + reels?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
