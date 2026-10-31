"""Batch: 2 Nov 2026 (Monday, evergreen): 1300 + 2100 reels, 1730 image + 3 stories.
Run from repo root: python content/scripts/batch_2026-10-31.py [reels|images|stories]"""

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
    "standup": ("2026-11-02_1300_friday-kya-kiya-reel", [
        dict(dur=2.4, tag="MONDAY STANDUP, 10 BAJE", head="MANAGER: 'FRIDAY KYA KIYA THA?'", level=0.5, mood="tired", sfx="ding"),
        dict(dur=2.6, tag="MERA DIMAAG", box="Friday ka kuch yaad nahi\nBas itna yaad hai ki\n5:59 pe laptop band kiya", level=0.3,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="BAAKI TEAM KO DEKHTE HUE", draw=reel_template("monkey-puppet"), sfx="tick"),
        dict(dur=3.8, head="'SIR, PENDING ITEMS PE THA'", box="Kaunse items?\nWo bhi pending hai.\nAur standup bhi\n45 min se chal raha hai",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Monday standup mein Friday yaad karna sabse bada task hai 🙂
office memes aur monday memes for every thaka hua desi jiska weekend dimaag ka cache clear kar deta hai

Send karo us colleague ko jo har standup mein 'same as yesterday' bolta hai 👇

#thakahuadesi #officememes #mondaymemes #corporatememes #desimemes
"""),
    "it-support": ("2026-11-02_2100_ghar-ka-it-support-reel", [
        dict(dur=2.4, tag="PAPA KA SAWAAL", head="'BETA, OFFICE MEIN KARTE KYA HO?'", level=0.6, mood="happy", sfx="ding"),
        dict(dur=2.6, tag="MAIN, POORE CONFIDENCE SE", box="'Papa, cloud migration,\nstakeholder alignment,\nsprint deliverables'", level=0.5,
             mood="happy", sfx="pop"),
        dict(dur=2.6, tag="GHAR WALE", draw=reel_template("hera-pheri-trio-shock"), sfx="tick"),
        dict(dur=3.8, head="PAPA: 'ACCHA, TOH PRINTER THEEK KAR DO'", box="3 saal se ghar ka\nIT support bhi main hu.\nBina salary, bina leave",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Office mein 'senior engineer', ghar pe printer wala bhaiya 🙂
indian parents memes aur office memes for every thaka hua desi jiski job ghar pe koi nahi samajhta

Send karo us dost ko jo ghar ka permanent WiFi aur printer technician hai 👇

#thakahuadesi #indianparents #officememes #desimemes #relatablememes
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
    img = template_meme("epic-handshake",
                        "Do log jo kabhi ek dusre se mile nahi, phir bhi same training li hai",
                        labels=["Mummy", "Manager", "'Bas ek minute\nka kaam hai'"],
                        footer="Ek minute = 2 ghante")
    out("2026-11-02_1730_ek-minute-kaam", "image", [img], """
Mummy ka 'ek minute' aur manager ka 'quick call', dono ka timer same factory se aata hai 🙂
office memes aur indian mom memes for every thaka hua desi jiska 'ek minute' kabhi ek minute nahi hota

Send karo us dost ko jo abhi bhi 'bas ek minute' wale kaam mein phasa hua hai 👇

#thakahuadesi #officememes #indianmom #desimemes #relatablememes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-11-02_1000_mood-story", mood_story("Monday + 2 tareekh", "salary: aa gayi\nmotivation: nahi aayi\nenergy: 15%", 0.15, "tired"))
    story("2026-11-02_1330_teaser-story", teaser_story("'Friday kya kiya tha?'", "naya reel feed pe. bhejo us colleague ko jo har standup mein ghabra jaata hai",
          Q / "2026-11-02_1300_friday-kya-kiya-reel" / "cover.png"))
    story("2026-11-02_2130_question-story", question_story("Sach batao", "Ghar walo ko tumhari job kya lagti hai? Sabse funny description batao"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
