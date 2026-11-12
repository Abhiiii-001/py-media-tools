"""Batch: 14 Nov 2026 (Saturday + Children's Day, a fixed date so it won't go stale; 2 days out):
1300 reel (bachpan ki wish), 1730 template image (bachpan vs aaj handshake), 2100 reel (Saturday kapde) + 3 stories.
Run from repo root: python content/scripts/batch_2026-11-14.py [reels|images|stories]"""


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
    "bachpan-wish": ("2026-11-14_1300_bachpan-wish-reel", [
        dict(dur=2.4, tag="BACHPAN MEIN HAR BIRTHDAY PE", head="'BAS JALDI SE BADA HONA HAI'", level=0.8, mood="happy", sfx="ding"),
        dict(dur=2.8, tag="WISH POORI HO GAYI", box="Rent: 18,000\nEMI: 3 chal rahi\nKhana: khud banao\nNeend: 5 ghante", level=0.35,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="MAIN, BADA HOKE", draw=reel_template("this-is-fine"), sfx="tick"),
        dict(dur=3.8, head="CHILDREN'S DAY PE BAS EK SAWAAL", box="'Bade hoke kya banoge?'\nAaj ka jawab:\nthaka hua",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Bachpan mein bada hona tha, ab bada hoke bas sona hai 🙂
desi memes aur adulting memes for every thaka hua desi jiski wish galti se poori ho gayi

Children's Day pe bhejo us dost ko jo school mein sabse zyada 'jaldi bada hona hai' bolta tha 👇

#thakahuadesi #childrensday #desimemes #adultingmemes #relatablememes
"""),
    "saturday-kapde": ("2026-11-14_2100_saturday-kapde-reel", [
        dict(dur=2.4, tag="SATURDAY, 11 AM", head="'AAJ SIRF AARAM KARUNGA'", level=0.7, mood="happy", sfx="ding"),
        dict(dur=2.8, tag="KAMRE KI KURSI PE", box="2 hafte ke kapde\n'Kal pehnunga' wali jeans\nMoze: 3, teeno akele\nKursi: dikh hi nahi rahi", level=0.35,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="MAIN: 'BAS 10 MINUTE KA KAAM HAI'", draw=reel_template("raju-waiting-pose"), sfx="tick"),
        dict(dur=3.8, head="RAAT 9 BAJE", box="Machine chalayi: haan\nSukhaye: bhool gaya\nKapde: phir se geele\nKursi: phir se full",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Kapde dhul gaye, bas sukhana bhool gaya, Saturday phir se waste 🙂
weekend memes aur bachelor life memes for every thaka hua desi jiski kursi asli wardrobe hai

Send karo us roommate ko jiski kursi pe 2 hafte ke kapde pade hai 👇

#thakahuadesi #weekendmemes #bachelorlife #desimemes #relatablememes
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
                        "Children's Day special:",
                        ["Bachpan\nwala main", "Aaj wala\nmain", "Karela aur\ntinde se nafrat"],
                        footer="Salary badh gayi, taste wahi ka wahi")
    out("2026-11-14_1730_bachpan-handshake", "image", [img], """
Height badh gayi, salary thodi si badhi, par karela aaj bhi nahi 🙂
desi memes aur childhood memes for every thaka hua desi jo mummy se aaj bhi 'aaj kya bana hai' poochta hai

Send karo us dost ko jo tiffin mein karela dekh ke canteen bhaag jaata tha 👇

#thakahuadesi #childrensday #desimemes #childhoodmemes #indianmemes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-11-14_1000_mood-story", mood_story("Shanivaar ki subah", "alarm: band\nplan: kuch nahi\nenergy: 65% (weekend mode)", 0.65, "happy"))
    story("2026-11-14_1330_teaser-story", teaser_story("'Jaldi bada hona hai'", "naya reel feed pe. bhejo us dost ko jiski bachpan wali wish poori ho gayi",
          Q / "2026-11-14_1300_bachpan-wish-reel" / "cover.png"))
    story("2026-11-14_2130_question-story", question_story("Sach batao", "Tumhari kursi pe abhi kitne din ke kapde pade hai?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
