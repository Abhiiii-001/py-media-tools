"""Batch: 10 Nov 2026 (Tuesday, 2 days out so evergreen: post-Diwali office mithai, card bill, rent): 1300 + 2100 reels, 1730 image + 3 stories.
Run from repo root: python content/scripts/batch_2026-11-10.py [reels|images|stories]"""

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
    "office-mithai": ("2026-11-10_1300_office-mithai-reel", [
        dict(dur=2.4, tag="DIWALI KE BAAD OFFICE", head="PANTRY MEIN KAJU KATLI KA DABBA AAYA", level=0.6, mood="happy", sfx="ding"),
        dict(dur=2.8, tag="PLAN", box="10:00 dabba dekha\n10:05 'meeting ke baad lunga'\n10:30 meeting shuru\n11:30 meeting khatam", level=0.4,
             mood="tired", sfx="pop"),
        dict(dur=2.4, tag="POORI TEAM, PANTRY PAHUNCH KE", draw=reel_template("hum-dukhi-the"), sfx="tick"),
        dict(dur=3.8, head="DABBE MEIN BACHA:", box="Sirf chandi wala kaagaz\nMeeting skip karne wala intern:\n'Sir bahut acchi thi'",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Meeting ne kaam bhi liya aur kaju katli bhi 🙂
office memes aur desi memes for every thaka hua desi jo 'baad mein lunga' bolke reh gaya

Tag karo us colleague ko jo pantry ke paas hi baitha rehta hai 👇

#thakahuadesi #officememes #corporatememes #desimemes #relatablememes
"""),
    "card-bill": ("2026-11-10_2100_card-bill-reel", [
        dict(dur=2.4, tag="DIWALI SALE MEIN MAIN", head="'SIRF 499 KA HI TOH HAI'", level=0.7, mood="happy", sfx="ding"),
        dict(dur=2.8, tag="CART MEIN", box="Lights: 499\nKurta: 899\nAirfryer: 'no cost EMI'\nAur 9 cheezein 'sirf 499'", level=0.4,
             mood="tired", sfx="pop"),
        dict(dur=2.4, tag="AB MERA DIMAAG, PURANE MUJHE:", draw=reel_template("mocking-spongebob"), sfx="tick"),
        dict(dur=3.8, head="CARD STATEMENT AAYA", box="Total due: Rs 18,640\nMinimum due: mera sukoon\nSalary aane mein:\nabhi 20 din",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
499 ke 12 order, ab 20 din Maggi 🙂
salary memes aur sale memes for every thaka hua desi jiska credit card Diwali pe mujhse zyada khush tha

Send karo us dost ko jiska 'sirf 499' wala cart abhi bhi bhara hai 👇

#thakahuadesi #salarymemes #desimemes #middleclassmemes #relatablememes
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
    img = template_meme("babu-rao-game",
                        "Landlord uncle jab 10 tareekh ho gayi\naur rent nahi aaya:",
                        footer="Main: 'Uncle salary Diwali pe udd gayi'")
    out("2026-11-10_1730_rent-uncle", "image", [img], """
Diwali pe patake nahi phode, salary phod di 🙂
salary memes aur flat life memes for every thaka hua desi jo mahine ki 10 tareekh ko landlord se chhup raha hai

Send karo us roommate ko jiska rent share abhi bhi 'kal pakka' hai 👇

#thakahuadesi #salarymemes #desimemes #middleclassmemes #roommatememes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-11-10_1000_mood-story", mood_story("Diwali ke baad Tuesday", "mithai: khatam\npaisa: khatam\nenergy: 15%", 0.15, "dead"))
    story("2026-11-10_1330_teaser-story", teaser_story("Office ka kaju katli dabba", "naya reel feed pe. bhejo us colleague ko jo pantry ke paas baitha hai",
          Q / "2026-11-10_1300_office-mithai-reel" / "cover.png"))
    story("2026-11-10_2130_question-story", question_story("Sach batao", "Diwali sale mein sabse bekaar cheez kya kharidi?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
