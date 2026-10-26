"""Batch: 28 Oct 2026 (Wednesday, evergreen): 1300 reel, 1730 image, 2100 reel + 3 stories.
Run from repo root: python content/scripts/batch_2026-10-26.py [reels|images|stories]"""

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
    "doubt": ("2026-10-28_1300_koi-doubt-reel", [
        dict(dur=2.4, tag="MEETING KE END MEIN", head="SIR: 'KOI DOUBT?'", level=0.5, mood="tired", sfx="ding"),
        dict(dur=2.6, tag="MAIN, POORE CONFIDENCE SE", box="'Nahi sir,\nsab clear hai'", level=0.45,
             mood="happy", sfx="pop"),
        dict(dur=2.6, tag="ASLI MEIN", draw=reel_template("dhak-dhak"), sfx="tick"),
        dict(dur=3.8, head="MEETING KE BAAD", box="Colleague ko DM:\n'bhai kaam kya bola?'\nUsko bhi nahi pata",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
'Sab clear hai sir' bolna aata hai, kaam kya hai wo nahi 🙂
office memes aur corporate memes for every thaka hua desi jo meeting ke baad DM mein meeting karta hai

Send karo us colleague ko jisse tum roz 'kya bola sir ne?' poochte ho 👇

#thakahuadesi #officememes #corporatememes #desimemes #relatablememes
"""),
    "paanch": ("2026-10-28_2100_bas-5-min-reel", [
        dict(dur=2.4, tag="GROUP CHAT, 7 BAJE", head="DOST: 'BAS 5 MIN MEIN PAHUNCH RAHA'", level=0.55, mood="happy", sfx="ding"),
        dict(dur=2.6, tag="7:45 PM", box="Live location:\nabhi bhi ghar pe.\nOnline bhi hai", level=0.35,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="8:30 PM, MAIN", draw=reel_template("ab-tak-aa-jana-chahiye"), sfx="tick"),
        dict(dur=3.8, head="9 BAJE: 'BHAI TRAFFIC THA'", box="Traffic ghar ke\nbathroom mein tha.\nNahane hi 8 baje gaya",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Uska 5 minute aur mera 2 ghanta, ek hi ghadi mein chalte hai 🙂
dosti memes aur desi memes for every group ka 'nikal gaya hu' wala

Send karo us dost ko jo 'bas pahunch raha' bolke abhi naha raha hai 👇

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
    img = sunburst()
    label(img, "DESI DICTIONARY", (W // 2, 100))
    text_block(img, "'THEEK HU' KA ASLI MATLAB", (70, 180, 940, 230), size=120)
    panel(img, (70, 440, 940, 470))
    text_block(img, "'Theek hu' = 3 din se\nneend poori nahi hui\n\n'Bas chal raha hai' =\nkuch nahi chal raha\n\n'Busy hu' = reels dekh raha hu",
               (110, 460, 860, 430), path=FONT_BODY, size=50, fill=BLACK, stroke=None)
    mascot(img, W // 2, 940, scale=0.8, level=0.15, mood="tired")
    watermark(img)
    out("2026-10-28_1730_theek-hu", "image", [img], """
'Kaise ho?' ka ek hi jawab hai, aur wo jhooth hai 🙂
adulting memes aur desi memes for every thaka hua desi jo smile karke 'theek hu' bolta hai

Send karo us dost ko jo 'theek hu' bolke 2 baje tak jaagta hai 👇

#thakahuadesi #adultingmemes #desimemes #overthinkingmemes #relatablememes
""")

def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-10-28_1000_mood-story", mood_story("Wednesday hai", "hafta: aadha gaya\nweekend: abhi bhi door\nenergy: 22%", 0.22, "tired"))
    story("2026-10-28_1330_teaser-story", teaser_story("'Koi doubt?' 'Nahi sir'", "naya reel feed pe. bhejo us colleague ko jisse tum kaam poochte ho",
          Q / "2026-10-28_1300_koi-doubt-reel" / "cover.png"))
    story("2026-10-28_2130_question-story", question_story("Sach batao", "Group mein 'bas 5 min' bolke 1 ghanta lagane wala kaun hai?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
