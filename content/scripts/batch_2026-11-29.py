"""Batch made 27 Nov 2026 (9 AM run).
Fill Sun 29 Nov (2 days out, evergreen): 1300 meme reel (Papa 'bas 10 minute ka kaam', Waiting Skeleton),
1730 image (Two Guys on a Bus: shaam 6 baje Saturday vs Sunday), 2100 mascot reel (Sunday raat neend ka hisaab),
1000 mood + 1330 teaser + 2130 question stories. No trend swap.
Run from repo root: python content/scripts/batch_2026-11-29.py [reels|images|stories]"""

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
    "papa-10-minute": ("2026-11-29_1300_papa-10-minute-reel", [
        dict(dur=2.4, tag="SUNDAY 11 BAJE", head="PAPA: 'CHAL, BAS 10 MINUTE KA KAAM HAI'", level=0.5, mood="tired", sfx="ding"),
        dict(dur=2.9, tag="10 MINUTE KA KAAM:", box="Hardware ki dukaan\nphir bank ka passbook\nphir 'yahan tak aaye hai\ntoh Gupta ji se mil lete'", level=0.4,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="PAPA: 'BAS 2 MINUTE, ANDAR SE AAYA'", draw=reel_template("waiting-skeleton"), sfx="tick"),
        dict(dur=3.8, head="4 GHANTE BAAD", box="Sunday khatam.\nKaam hua: 1 nut-bolt,\nRs 12 ka.\nPapa: 'dekha, jaldi ho gaya'",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
10 minute bola tha, Sunday ka 10% bhi nahi bacha 🙂
desi memes aur indian parents memes for every thaka hua desi jo Papa ke 'bas 10 minute' pe phir se fas gaya

Send karo us bhai/behen ko jo har Sunday Papa ke saath 'bas 10 minute' ke liye jaata hai 👇

#thakahuadesi #desimemes #indianparents #relatablememes #sundaymemes
"""),
    "neend-hisaab": ("2026-11-29_2100_neend-hisaab-reel", [
        dict(dur=2.3, tag="SUNDAY RAAT 10 BAJE", head="'KAL 7 BAJE UTHNA, 9 GHANTE NEEND. PERFECT'", level=0.5, mood="tired", sfx="ding"),
        dict(dur=2.6, tag="12:30 AM, REELS KE BEECH:", head="'6.5 GHANTE BHI KAAFI HAI'", level=0.35, mood="tired", sfx="pop"),
        dict(dur=2.6, tag="2:10 AM:", head="'LOG 4 GHANTE MEIN BHI JEETE HAI'", level=0.15,
             mood="tired", sfx="tick"),
        dict(dur=3.8, head="3:40 AM", box="'Ab sone ka kya fayda,\nseedha nahake\noffice chala jaata hu'\n6:55 AM: so gaya",
             level=0.0, mood="dead", sfx="trombone", shake=True),
    ], """
9 ghante ka plan tha, 9 minute ki neend mili 🙂
monday memes aur office memes for every thaka hua desi jo Sunday raat ko neend ka hisaab lagata rehta hai

Send karo us dost ko jo abhi bhi 'bas 1 reel aur' bol raha hai 👇

#thakahuadesi #mondaymemes #officememes #desimemes #relatablememes
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
    img = template_meme("two-guys-bus", "Shaam 6 baje, same chai, same balcony:",
                        labels=["Sunday wala main:\n'kal Monday hai'", "Saturday wala main:\n'kal Sunday hai'"],
                        footer="24 ghante mein personality badal gayi")
    out("2026-11-29_1730_shaam-6-baje", "image", [img], """
Chai wahi, balcony wahi, bas kal ka din alag 🙂
sunday memes aur office memes for every thaka hua desi jiska Sunday shaam 6 baje hi khatam ho jaata hai

Send karo us colleague ko jiska mood bhi Sunday shaam ko off ho jaata hai 👇

#thakahuadesi #sundaymemes #officememes #mondaymemes #desimemes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-11-29_1000_mood-story", mood_story("Ravivaar ki subah", "uthne ka time: jab mann kare\nchai: 1 (abhi)\nenergy: 40%\nMonday ka dar: 60%\n(shaam tak 100%)", 0.4, "tired"))
    story("2026-11-29_1330_teaser-story", teaser_story("Papa: 'Bas 10 minute ka kaam hai'", "naya reel feed pe. bhejo us bhai/behen ko jo har baar fas jaata hai",
          Q / "2026-11-29_1300_papa-10-minute-reel" / "cover.png"))
    story("2026-11-29_2130_question-story", question_story("Sach bolo",
          "Sunday raat kitne baje\nsote ho actually?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
