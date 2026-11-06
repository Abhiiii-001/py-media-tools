"""Batch: 8 Nov 2026 (Sunday, Diwali day: soan papdi/relatives/chutti angles only, no religious side): 1300 + 2100 reels, 1730 image + 3 stories.
Run from repo root: python content/scripts/batch_2026-11-07.py [reels|images|stories]"""

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
    "soan-papdi": ("2026-11-08_1300_soan-papdi-reel", [
        dict(dur=2.4, tag="DIWALI KA ASLI TRAVELLER", head="SOAN PAPDI KA EK DABBA", level=0.6, mood="happy", sfx="ding"),
        dict(dur=2.8, tag="ROUTE MAP", box="Padosi aunty -> hum\nHum -> mama ji\nMama ji -> chachi\nChachi -> ???", level=0.5,
             mood="tired", sfx="pop"),
        dict(dur=2.4, tag="5 DIN BAAD, DOORBELL", draw=reel_template("monkey-puppet"), sfx="tick"),
        dict(dur=3.8, head="WAHI DABBA WAPAS AAYA", box="Sticker pe abhi bhi\nhumari handwriting:\n'Happy Diwali'\nKisi ne khola tak nahi",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Soan papdi ne pura mohalla ghoom liya, khaya kisi ne nahi 🙂
desi memes aur diwali memes for every thaka hua desi jiske ghar har saal wahi dabba ghoom ke aata hai

Send karo us dost ko jiske ghar abhi 4 dabbe soan papdi pade hai 👇

#thakahuadesi #diwalimemes #soanpapdi #desimemes #relatablememes
"""),
    "diwali-sunday": ("2026-11-08_2100_diwali-sunday-reel", [
        dict(dur=2.4, tag="CALENDAR KHOLA", head="IS SAAL DIWALI KIS DIN? SUNDAY.", level=0.4, mood="tired", sfx="ding"),
        dict(dur=2.6, tag="HISAAB", box="Extra chutti: 0\nBonus: 'next quarter'\nKal: 9:30 standup", level=0.25,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="OFFICE KA GROUP CHAT", draw=reel_template("gajab-bezzati"), sfx="tick"),
        dict(dur=3.8, head="MONDAY 10 BAJE, MANAGER:", box="'Hope everyone had\na restful long\nweekend!'\nKaunsa long, sir?",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Diwali bhi Sunday ko aayi, chutti ne bhi weekend mein adjust kar liya 🙂
office memes aur diwali memes for every thaka hua desi jiska Monday kal subah 9:30 pe hai

Tag karo us colleague ko jo kal standup mein aankh khol ke so raha hoga 👇

#thakahuadesi #officememes #diwalimemes #corporatememes #desimemes
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
    img = template_meme("salary-kitne",
                        "Diwali pe chacha ji,\nmithai se bhi pehle:",
                        footer="'Toh beta, package kitna hai ab?'")
    out("2026-11-08_1730_package-kitna", "image", [img], """
Mithai baad mein milti hai, salary ka sawaal pehle 🙂
relatives memes aur salary memes for every thaka hua desi jo aaj ghar pe interview dene wala hai

Send karo us dost ko jiska package aaj poore khandaan ko pata chalega 👇

#thakahuadesi #relativesmemes #salarymemes #diwalimemes #desimemes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-11-08_1000_mood-story", mood_story("Diwali Sunday ko", "extra chutti: 0\nrelatives: aane wale\nenergy: 50%", 0.5, "tired"))
    story("2026-11-08_1330_teaser-story", teaser_story("Soan papdi ka safar", "naya reel feed pe. bhejo us dost ko jiske ghar 4 dabbe pade hai",
          Q / "2026-11-08_1300_soan-papdi-reel" / "cover.png"))
    story("2026-11-08_2130_question-story", question_story("Sach batao", "Aaj relatives ne sabse darawna sawaal kya pucha?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
