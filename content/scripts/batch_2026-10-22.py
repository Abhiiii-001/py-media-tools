"""Batch: 24 Oct 2026 (Saturday, evergreen): 1300 reel, 1730 image, 2100 reel + 3 stories.
Run from repo root: python content/scripts/batch_2026-10-22.py [reels|images|stories]"""
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
    "alarm": ("2026-10-24_1300_saturday-alarm-reel", [
        dict(dur=2.4, tag="MONDAY TO FRIDAY", head="ALARM 7:00, SNOOZE x5", level=0.2, mood="dead", sfx="ding"),
        dict(dur=2.6, tag="SATURDAY, KOI ALARM NAHI", box="Body: 6:00 AM\nfull fresh, aankh khuli\n'chalo uthte hai'", level=0.8,
             mood="happy", sfx="pop"),
        dict(dur=2.6, tag="MAIN, 6 BAJE, CHHAT GHOORTE HUE", draw=reel_template("hide-the-pain"), sfx="tick"),
        dict(dur=3.8, head="AUR MONDAY KO?", box="Phir se 5 snooze.\nBody ko bhi\noffice se nafrat hai",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Weekday pe 5 alarm kam padte hai, Saturday ko 6 baje khud uth jaata hu 🙂
weekend memes aur office memes for every thaka hua desi jiski body bhi Monday se darti hai

Send karo us dost ko jo 5 snooze ke bina nahi uthta 👇

#thakahuadesi #weekendmemes #officememes #desimemes #relatablememes
"""),
    "split": ("2026-10-24_2100_upi-hisaab-reel", [
        dict(dur=2.4, tag="SATURDAY RAAT", head="DOST: 'BAS EK CHAI PE MILTE HAI'", level=0.6, mood="happy", sfx="ding"),
        dict(dur=2.6, tag="3 GHANTE BAAD", box="Cafe, cold coffee,\nfries, momos\nBill: Rs 2,437", level=0.3,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="GHAR PAHUNCHTE HI", draw=reel_template("jethalal-evil-smile"), sfx="tick"),
        dict(dur=3.8, head="UPI REQUEST: RS 812.50", box="Dosti 10 saal ki,\nhisaab 50 paise ka.\nNote: 'chai'",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Dosti free hai, bas chai ka hisaab 50 paise tak hota hai 🙂
dosti memes aur desi memes for every group ka 'request bhej diya hai' wala

Send karo us dost ko jo 50 paise ka bhi UPI request bhejta hai 👇

#thakahuadesi #dostimemes #desimemes #friendsmemes #relatablememes
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
    img = template_meme("gru-plan",
                        "Weekend ka plan:",
                        labels=["Sat: gym, laundry", "Sun: kitaab, meal prep", "Pehle bas 5 min reels", "Pehle bas 5 min reels"],
                        footer="Sunday raat 11 baje: 'agle weekend pakka'")
    out("2026-10-24_1730_weekend-plan", "image", [img], """
Weekend ka plan har hafte solid hota hai, bas '5 min reels' kabhi khatam nahi hote 🙂
weekend memes aur adulting memes for every thaka hua desi jiska poora weekend 5 min mein nikal jaata hai

Send karo us dost ko jo abhi bhi '5 min' wali reel dekh raha hai 👇

#thakahuadesi #weekendmemes #adultingmemes #desimemes #relatablememes
""")

def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-10-24_1000_mood-story", mood_story("Saturday hai", "alarm: band\nbody: phir bhi 6 baje uth gaya\nplans: bistar", 0.6, "happy"))
    story("2026-10-24_1330_teaser-story", teaser_story("Weekday vs Saturday ki neend", "naya reel feed pe. bhejo us dost ko jo 5 snooze ke bina nahi uthta",
          Q / "2026-10-24_1300_saturday-alarm-reel" / "cover.png"))
    story("2026-10-24_2130_question-story", question_story("Sach batao", "Group mein 50 paise ka bhi hisaab rakhne wala dost kaun hai?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
