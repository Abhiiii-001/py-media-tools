"""Batch: 23 Oct 2026 (Friday, evergreen): 1300 reel, 1730 image, 2100 reel + 3 stories.
Run from repo root: python content/scripts/batch_2026-10-21.py [reels|images|stories]"""
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
    "doctor": ("2026-10-23_1300_doctor-stress-reel", [
        dict(dur=2.4, tag="CHECKUP KE BAAD", head="DOCTOR: 'STRESS KAM LO'", level=0.4, mood="tired", sfx="ding"),
        dict(dur=2.6, tag="MAIN MANN MEIN", box="Kaise doctor?\nEMI kam hogi? Rent?\nBoss badal doge?", level=0.3,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="RECEPTION: 'FEES RS 800'", draw=reel_template("hide-the-pain"), sfx="tick"),
        dict(dur=3.8, head="AB STRESS DOUBLE", box="Ek stress salary ka,\nek doctor ki fees ka.\nDawai: 'aaram karo'",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Doctor ne stress kam karne bola, fees dekh ke aur badh gaya 🙂
adulting memes aur salary memes for every thaka hua desi jiska BP bhi EMI se chalta hai

Send karo us dost ko jo 'bas thoda stress hai' bolke 3 saal se chal raha hai 👇

#thakahuadesi #adultingmemes #salarymemes #desimemes #officememes
"""),
    "papa": ("2026-10-23_2100_papa-kitne-ka-reel", [
        dict(dur=2.4, tag="NAYA JOOTA LAAYA", head="PAPA: 'KITNE KA LIYA?'", level=0.6, mood="tired", sfx="ding"),
        dict(dur=2.6, tag="MAIN (ASLI PRICE RS 4,999)", box="'Sale mein tha papa,\nbas Rs 1,200 ka'", level=0.5,
             mood="happy", sfx="pop"),
        dict(dur=2.6, tag="PAPA: 'ITNA MEHNGA?!'", draw=reel_template("3idiots-old-man"), sfx="tick"),
        dict(dur=3.8, head="'HAMARE ZAMAANE MEIN 40 KA AATA THA'", box="Asli price batata\ntoh joota nahi,\nmain ghar ke bahar hota",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Ghar mein har cheez ka price 75% off pe hi batana padta hai 🙂
indian parents memes aur desi memes for everyone jo papa ko asli bill kabhi nahi dikhata

Send karo us dost ko jo price aadha karke batata hai 👇

#thakahuadesi #indianparents #desimemes #middleclassmemes #papamemes
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
                        "25 ki umar mein:",
                        labels=["Ghar, scooter,\n2 bachche", "3 roommates,\n0 savings"],
                        footer="Ek salary mein Papa ka poora ghar chalta tha, meri sirf Maggi")
    out("2026-10-23_1730_papa-at-25", "image", [img], """
Papa 25 mein ghar chala rahe the, main 25 mein khud ko bhi nahi chala pa raha 🙂
middle class memes aur adulting memes for every 25 saal ka thaka hua desi

Send karo us dost ko jo abhi bhi 'settle hone wala hai' 👇

#thakahuadesi #adultingmemes #middleclassmemes #desimemes #salarymemes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-10-23_1000_mood-story", mood_story("Friday hai", "body: office mein\ndil: weekend pe\nkaam: Monday pe", 0.5, "tired"))
    story("2026-10-23_1330_teaser-story", teaser_story("Doctor: 'stress kam lo'", "naya reel feed pe. bhejo us dost ko jiska stress bhi EMI pe chalta hai",
          Q / "2026-10-23_1300_doctor-stress-reel" / "cover.png"))
    story("2026-10-23_2130_question-story", question_story("Sach batao", "Papa ko kisi cheez ka ASLI price kabhi bataya hai?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
