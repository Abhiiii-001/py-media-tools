"""Batch: 22 Oct 2026 (Thursday): 1300 reel (IND vs NZ 1st T20I, 12:30 PM IST, office hours),
1730 image, 2100 reel (evergreen) + 3 stories.
Run from repo root: python content/scripts/batch_2026-10-20.py [reels|images|stories]"""
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
    "match": ("2026-10-22_1300_match-office-reel", [
        dict(dur=2.4, tag="IND vs NZ, 12:30 PM", head="MATCH SHURU. AUR MAIN? OFFICE MEIN", level=0.6, mood="tired", sfx="ding"),
        dict(dur=2.6, tag="MERA PLAN", box="Laptop pe excel,\nphone pe score,\nface pe 'very productive'",
             level=0.7, mood="happy", sfx="pop"),
        dict(dur=2.6, tag="MANAGER PEECHE KHADA THA", draw=reel_template("monkey-puppet"), sfx="tick"),
        dict(dur=3.8, head="MANAGER:", box="'Score kya hua?'\nWoh 1 PM ki meeting\nmute karke match dekh raha tha",
             level=0.4, mood="dead", sfx="trombone", shake=True),
    ], """
Excel bhi khula tha, score bhi, bas kaam nahi hua 🙂
cricket memes aur office memes for everyone jo aaj meeting mein bhi score dekh raha hai

Send karo us colleague ko jo abhi isi tab pe hai 👇

#thakahuadesi #cricketmemes #officememes #indvsnz #desimemes
"""),
    "salary": ("2026-10-22_2100_salary-mehmaan-reel", [
        dict(dur=2.4, tag="10:02 AM", head="SALARY CREDITED", level=1.0, mood="happy", sfx="ding"),
        dict(dur=2.4, tag="MAIN", box="Aaj toh party.\nBiryani, naya joota,\nshayad Goa bhi", level=0.9,
             mood="happy", sfx="pop"),
        dict(dur=2.6, tag="10:03 AM, 4 SMS AAYE", draw=reel_template("hera-pheri-trio-shock"), sfx="tick"),
        dict(dur=3.8, head="EMI. RENT. CARD BILL. SIP.", box="Salary 1 minute ki mehmaan thi,\njaate jaate 'bye' bhi nahi bola",
             level=0.03, mood="dead", sfx="trombone", shake=True),
    ], """
Salary aayi, salary gayi, beech mein sirf ek SMS 🙂
salary memes aur middle class memes for every EMI wala desi

Send karo us dost ko jiski salary bhi 1 minute ki mehmaan hai 👇

#thakahuadesi #salarymemes #middleclassmemes #desimemes #officememes
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
    img = template_meme("jethalal-reactions",
                        "Boss: 'ek minute aana zara'",
                        labels=["Kal wala\nmail?", "2019 wali\ngalti?", "PIP?", "Resume update\nkar leta hu"],
                        footer="Boss: 'charger hai kya?'")
    out("2026-10-22_1730_ek-minute", "image", [img], """
Charger maanga tha, maine poori career replay kar li 🙂
office memes aur overthinking memes for everyone jiska dil 'ek minute aana' se ruk jaata hai

Send karo us colleague ko jo boss ke message pe hi pasina pasina ho jaata hai 👇

#thakahuadesi #officememes #overthinking #corporatememes #desimemes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-10-22_1000_mood-story", mood_story("Thursday hai", "match: 12:30\nmeeting: 12:30\nkismat: same", 0.35, "tired"))
    story("2026-10-22_1330_teaser-story", teaser_story("Excel khula, score bhi", "naya reel feed pe. bhejo us colleague ko jo abhi score dekh raha hai",
          Q / "2026-10-22_1300_match-office-reel" / "cover.png"))
    story("2026-10-22_2130_question-story", question_story("Salary check", "Salary account mein kitni der tikti hai? Ghante, din ya 1 minute?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
