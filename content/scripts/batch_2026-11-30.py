"""Batch made 28 Nov 2026 (9 AM run).
Fill Mon 30 Nov (2 days out, evergreen, month end / salary eve): 1300 meme reel (raat 12 baje bank app refresh,
Raju 'paisa laya?'), 1730 image (Two Buttons: Rs 87 aur dost ki party), 2100 mascot reel (chai chhod di, 2 din ke liye),
1000 mood + 1330 teaser + 2130 question stories. No trend swap.
Run from repo root: python content/scripts/batch_2026-11-30.py [reels|images|stories]"""

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
    "bank-refresh": ("2026-11-30_1300_bank-refresh-reel", [
        dict(dur=2.4, tag="30 TAAREEKH, RAAT 11:58", head="'BAS 2 MINUTE, PHIR SALARY'", level=0.1, mood="tired", sfx="ding"),
        dict(dur=2.8, tag="11:58 SE 12:20 TAK:", box="Bank app refresh: 31 baar\nBalance: Rs 87\nPhir bhi refresh: 32", level=0.08,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="MAIN, APNE BANK APP SE:", draw=reel_template("paisa-laya"), sfx="tick"),
        dict(dur=3.8, head="12:21 AM", box="'Server under maintenance.\nPlease try after 6 AM'\nNeend bhi gayi,\nsalary bhi nahi aayi",
             level=0.0, mood="dead", sfx="trombone", shake=True),
    ], """
Salary 1 taareekh ko aati hai, refresh 30 ki raat se shuru 🙂
salary memes aur month end memes for every thaka hua desi jo raat 12 baje bank app ko ghoor raha hai

Send karo us dost ko jo aaj raat bhi 'bas ek baar aur' refresh karega 👇

#thakahuadesi #salarymemes #desimemes #monthend #officememes
"""),
    "chai-chhod-di": ("2026-11-30_2100_chai-chhod-di-reel", [
        dict(dur=2.3, tag="MONDAY + 30 TAAREEKH", head="COLLEAGUE: 'CHAL, CHAI PE CHALTE HAI'", level=0.3, mood="tired", sfx="ding"),
        dict(dur=2.6, tag="MERA ACCOUNT:", head="RS 87", level=0.08, mood="tired", sfx="pop"),
        dict(dur=2.6, tag="MAIN, FULL CONFIDENCE MEIN:", head="'NAHI YAAR, MAINE CHAI CHHOD DI'", level=0.05,
             mood="happy", sfx="tick"),
        dict(dur=3.8, head="CHHOD DI.", box="Kab tak?\n1 taareekh, subah 9:02\n(salary credit hone tak)",
             level=0.0, mood="dead", sfx="trombone", shake=True),
    ], """
Chai nahi chhodi, bas salary ka wait kar raha hu 🙂
salary memes aur office memes for every thaka hua desi jiska health ka decision bank balance leta hai

Send karo us colleague ko jo month end pe 'diet pe hu' bolta hai 👇

#thakahuadesi #salarymemes #officememes #desimemes #chailover
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
    img = template_meme("two-buttons", "30 taareekh, account mein Rs 87, dost: 'aaj party hai, aaja':",
                        labels=["'Sirf paani\npiyunga'", "'Tabiyat\nkharab hai'", "Main, Rs 87 ke saath"],
                        footer="Party 30 ko hi kyu hoti hai bhai")
    out("2026-11-30_1730_party-87", "image", [img], """
Party 30 taareekh ko, salary 1 taareekh ko, timing hi galat hai 🙂
salary memes aur desi memes for every thaka hua desi jiski month end pe achanak tabiyat kharab ho jaati hai

Send karo us dost ko jo hamesha 30 taareekh ko hi party rakhta hai 👇

#thakahuadesi #salarymemes #desimemes #monthend #relatablememes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-11-30_1000_mood-story", mood_story("Somvaar + 30 taareekh", "chai: 3 (udhaar pe)\nenergy: 5%\nbalance: mat poocho\nsalary: kal (shayad)\nhimmat: 0 (Monday)", 0.05, "dead"))
    story("2026-11-30_1330_teaser-story", teaser_story("Raat 12 baje: bank app refresh", "naya reel feed pe. bhejo us dost ko jo aaj raat refresh karega",
          Q / "2026-11-30_1300_bank-refresh-reel" / "cover.png"))
    story("2026-11-30_2130_question-story", question_story("Sach bolo",
          "Salary aate hi\nsabse pehle\nkya karte ho?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
