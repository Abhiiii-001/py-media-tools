"""Batch: 9 Nov 2026 (Monday, 2 days out so evergreen: ghar se wapas, office meetings): 1300 + 2100 reels, 1730 image + 3 stories.
Run from repo root: python content/scripts/batch_2026-11-09.py [reels|images|stories]"""

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
    "mummy-ka-bag": ("2026-11-09_1300_mummy-ka-bag-reel", [
        dict(dur=2.4, tag="GHAR SE WAPAS JAATE WAQT", head="MUMMY: 'BAS THODA SA PACK KIYA HAI'", level=0.6, mood="happy", sfx="ding"),
        dict(dur=2.8, tag="'THODA SA'", box="2 kilo laddoo\n3 dabbe achaar\n1 litre ghee\nAur ek bag 'raaste ke liye'", level=0.4,
             mood="tired", sfx="pop"),
        dict(dur=2.4, tag="AIRPORT COUNTER WALA, BAG TAULTE HUE", draw=reel_template("abhi-maza-ayega"), sfx="tick"),
        dict(dur=3.8, head="BAG: 23 KG", box="4 kg kapde\n19 kg mummy ka pyaar\nExtra baggage: Rs 3,400\nMummy: 'bahar ka mat khana'",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Kapde bhool gaya, par achaar 3 dabbe hai 🙂
desi memes aur mummy memes for every thaka hua desi jo chutti ke baad wapas sheher ja raha hai

Send karo us dost ko jiska bag aaj bhi ghee se bhara hai 👇

#thakahuadesi #desimemes #mummymemes #hostellife #relatablememes
"""),
    "3-baje-meeting": ("2026-11-09_2100_3-baje-meeting-reel", [
        dict(dur=2.4, tag="LUNCH KE BAAD", head="3 BAJE KI MEETING", level=0.3, mood="tired", sfx="ding"),
        dict(dur=2.8, tag="ANDAR KI LADAI", box="Aankhein: band ho rahi\nCamera: on hai\nSir: hila raha hu\nDimaag: kab ka so gaya", level=0.15,
             mood="tired", sfx="pop"),
        dict(dur=2.4, tag="MANAGER: 'ANY THOUGHTS, TEAM?'", draw=reel_template("welcome-scene"), sfx="tick"),
        dict(dur=3.8, head="MAINE BOLA: 'AGREED SIR'", box="Baad mein pata chala\nkis cheez pe agree kiya:\nwo task ab\nmera hai",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Neend mein 'agreed' bola, ab poora hafta wahi kaam karna hai 🙂
office memes aur corporate memes for every thaka hua desi jo lunch ke baad meeting mein zinda hone ki acting karta hai

Tag karo us colleague ko jo camera on karke so jaata hai 👇

#thakahuadesi #officememes #corporatememes #desimemes #workmemes
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
    img = template_meme("panchayat-office",
                        "Monday 10 baje ki meeting\njo ek mail ho sakti thi:",
                        footer="Agenda: agli meeting kab rakhein")
    out("2026-11-09_1730_meeting-ka-agenda", "image", [img], """
Meeting ka ek hi outcome nikla: ek aur meeting 🙂
office memes aur monday memes for every thaka hua desi jiska Monday calendar invites mein hi khatam ho jaata hai

Send karo us colleague ko jo har meeting ke baad 'quick sync' rakhta hai 👇

#thakahuadesi #officememes #mondaymemes #corporatememes #desimemes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-11-09_1000_mood-story", mood_story("Chutti ke baad Monday", "neend: ghar pe chhoot gayi\ninbox: 214 unread\nenergy: 10%", 0.1, "dead"))
    story("2026-11-09_1330_teaser-story", teaser_story("Mummy ka 'thoda sa'", "naya reel feed pe. bhejo us dost ko jiska bag ghee se bhara hai",
          Q / "2026-11-09_1300_mummy-ka-bag-reel" / "cover.png"))
    story("2026-11-09_2130_question-story", question_story("Sach batao", "Mummy ne is baar bag mein sabse ajeeb cheez kya pack ki?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
