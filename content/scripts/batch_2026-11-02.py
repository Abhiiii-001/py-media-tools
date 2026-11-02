"""Batch: 4 Nov 2026 (Wednesday, evergreen): 1300 + 2100 reels, 1730 image + 3 stories.
Run from repo root: python content/scripts/batch_2026-11-02.py [reels|images|stories]"""

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
    "diwali-leave": ("2026-11-04_1300_diwali-leave-reel", [
        dict(dur=2.4, tag="DIWALI WEEK", head="'SIR, 6 SE 9 CHUTTI CHAHIYE'", level=0.6, mood="happy", sfx="ding"),
        dict(dur=2.6, tag="MANAGER", box="'Hmm... saari team\nek saath chutti pe?\nDeadline ka kya?'", level=0.4,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="MANAGER KA DIMAAG", draw=reel_template("bhushan"), sfx="tick"),
        dict(dur=3.8, head="CHUTTI APPROVE HO GAYI", box="'Bas laptop ghar le jaana,\nemergency ke liye.'\nEmergency roz 11 baje\naa rahi hai",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Chutti approve hui hai, kaam nahi gaya 🙂
office memes aur corporate memes for every thaka hua desi jiska laptop bhi Diwali pe ghar aa raha hai

Send karo us colleague ko jiski chutti abhi bhi 'pending' hai 👇

#thakahuadesi #officememes #corporatememes #desimemes #diwalileave
"""),
    "papa-forward": ("2026-11-04_2100_papa-forward-reel", [
        dict(dur=2.4, tag="7:02 AM, FAMILY GROUP", head="PAPA KA NAYA FORWARD AAYA", level=0.5, mood="tired", sfx="ding"),
        dict(dur=2.6, tag="'FORWARDED MANY TIMES'", box="'Raat ko 3 glass garam\npaani piyo, 100 saal\njiyoge. Doctor bhi\nshocked hai'", level=0.4,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="MAINE BOLA 'PAPA YE FAKE HAI'", draw=reel_template("abba-nahi-manenge"), sfx="tick"),
        dict(dur=3.8, head="'TUMSE ZYADA PADHA HUA HU'", box="Usi din wo forward\n4 aur groups mein gaya.\nAb mujhe bhi 3 glass\npaani pilaya jaata hai",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Fact check karo toh papa ka forward aur strong ho jaata hai 🙂
family memes aur desi memes for every thaka hua desi jiske family group mein roz ek naya 'doctor bhi shocked hai' aata hai

Send karo apne bhai behen ko, tumhare family group ka bhi yahi haal hai 👇

#thakahuadesi #familymemes #indianparents #desimemes #relatablememes
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
    img = template_meme("expanding-brain",
                        "Office mein busy dikhne ke tareeke",
                        labels=["Kaam karo", "Excel khula rakho,\nbas scroll karte raho", "Mouse\nhilate raho,\ngreen dot\non rahe",
                                "Meeting mein\n'offline\nlete hai'\nbolo"],
                        footer="Promotion bhi offline hi hai")
    out("2026-11-04_1730_busy-dikhna", "image", [img], """
Kaam karna optional hai, busy dikhna full time job hai 🙂
office memes aur corporate memes for every thaka hua desi jiska green dot uski asli mehnat hai

Send karo us colleague ko jo har meeting 'offline' le jaata hai 👇

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
    story("2026-11-04_1000_mood-story", mood_story("Wednesday hai", "Diwali chutti: pending\nkaam: double\nenergy: 25%", 0.25, "tired"))
    story("2026-11-04_1330_teaser-story", teaser_story("'Sir, Diwali pe chutti chahiye'", "naya reel feed pe. bhejo us colleague ko jiski chutti abhi bhi pending hai",
          Q / "2026-11-04_1300_diwali-leave-reel" / "cover.png"))
    story("2026-11-04_2130_question-story", question_story("Family group", "Family group ka sabse best forward kaunsa tha?"))

if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
