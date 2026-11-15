"""Batch: 17 Nov 2026 (Tuesday, 2 days out, evergreen):
1300 reel (Mummy ka sweater), 1730 image (Buff Doge vs Cheems, Monday vs Tuesday motivation),
2100 reel (refund 5-7 working days) + 3 stories.
Run from repo root: python content/scripts/batch_2026-11-17.py [reels|images|stories]"""


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
    "mummy-sweater": ("2026-11-17_1300_mummy-sweater-reel", [
        dict(dur=2.4, tag="GHAR SE NIKALTE WAQT", head="MUMMY: 'SWEATER KAHAN HAI?'", level=0.6, mood="tired", sfx="ding"),
        dict(dur=2.8, tag="BAHAR 24 DEGREE, PHIR BHI", box="Main: 'thand nahi hai'\nMummy: 'mujhe lag rahi hai'\nPapa: 'maa ki sun le'\nDadi: 'topi bhi pehen'", level=0.35,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="GALI KA CORNER AATE HI", draw=reel_template("phir-hera-pheri-run"), sfx="tick"),
        dict(dur=3.8, head="SHAAM 7 BAJE", box="Sweater: bag mein\nNaak: band\nAawaz: gayab\nMummy: 'maine bola tha na'",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Sweater bag mein tha, zukaam naak mein, aur 'maine bola tha na' kaan mein 🙂
desi memes aur indian mom memes for every thaka hua desi jiski mummy ko 24 degree pe bhi thand lagti hai

Send karo us bhai/behen ko jo gali ke corner pe sweater utaar deta hai 👇

#thakahuadesi #desimemes #indianmoms #wintermemes #relatablememes
"""),
    "refund-wait": ("2026-11-17_2100_refund-wait-reel", [
        dict(dur=2.4, tag="ORDER RETURN KIYA, PICKUP 2 MIN MEIN", head="REFUND: '5-7 WORKING DAYS'", level=0.5, mood="tired", sfx="ding"),
        dict(dur=2.8, tag="REFUND KA SAFAR", box="Din 3: 'processing'\nDin 7: 'initiated'\nDin 10: customer care bot\nBot: 'aur kya madad karu?'", level=0.3,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="MAIN, DIN 12 PE", draw=reel_template("waiting-skeleton"), sfx="tick"),
        dict(dur=3.8, head="DIN 14", box="Rs 1,499 wapas aaye\nUsi din: 'SALE LIVE HAI'\nCart: phir bhar gaya\nRefund: phir gaya",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Pickup 2 minute mein, refund 2 hafte mein, aur sale 2 second mein 🙂
online shopping memes aur desi memes for every thaka hua desi jo refund ka status roz check karta hai

Send karo us dost ko jiska refund abhi bhi 'processing' mein hai 👇

#thakahuadesi #desimemes #shoppingmemes #salarymemes #relatablememes
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
    img = template_meme("buff-doge-cheems",
                        "Weekly motivation ki expiry date:",
                        ["Monday wala main:\n'is hafte sab kaam\ntime pe karunga'", "Tuesday wala main:\n'kal se pakka'"],
                        footer="Planner mein sirf Monday bhara hai")
    out("2026-11-17_1730_monday-vs-tuesday", "image", [img], """
Monday ko CEO wali energy, Tuesday ko 'kal dekhte hai' 🙂
office memes aur desi memes for every thaka hua desi jiska motivation 24 ghante mein expire ho jaata hai

Send karo us dost ko jo har Monday naya plan banata hai 👇

#thakahuadesi #officememes #desimemes #mondaymemes #relatablememes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-11-17_1000_mood-story", mood_story("Mangalvaar ki subah", "Monday khatam, kaam nahi\nchai: doosri\nenergy: 25%", 0.25, "tired"))
    story("2026-11-17_1330_teaser-story", teaser_story("'Sweater kahan hai?'", "naya reel feed pe. bhejo us bhai/behen ko jo corner pe sweater utaar deta hai",
          Q / "2026-11-17_1300_mummy-sweater-reel" / "cover.png"))
    story("2026-11-17_2130_question-story", question_story("Sach batao", "Refund ke liye sabse lamba kitne din wait kiya hai?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
