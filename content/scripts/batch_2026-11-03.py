"""Batch: 5 Nov 2026 (Thursday, evergreen): 1300 + 2100 reels, 1730 image + 3 stories.
Run from repo root: python content/scripts/batch_2026-11-03.py [reels|images|stories]"""

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
    "raat-ka-message": ("2026-11-05_1300_raat-ka-message-reel", [
        dict(dur=2.4, tag="10:47 PM", head="BOSS: 'ARE YOU THERE?'", level=0.4, mood="tired", sfx="ding"),
        dict(dur=2.6, tag="DIMAAG", box="Reply kiya = raat ka kaam\nNahi kiya = subah tension\nSeen kiya = dono", level=0.3,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="MAIN, NOTIFICATION DEKH KE", draw=reel_template("bilkul-risk-nahi"), sfx="tick"),
        dict(dur=3.8, head="SUBAH 7 BAJE", box="'Sorry sir, so gaya tha'\nSach: raat bhar phone\nko ghoorta raha,\nneend bhi nahi aayi",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Message open nahi kiya, par neend bhi nahi aayi 🙂
office memes aur corporate memes for every thaka hua desi jiska boss raat 10 baje 'are you there?' bhejta hai

Send karo us colleague ko jo subah 'so gaya tha sir' bolta hai 👇

#thakahuadesi #officememes #corporatememes #desimemes #relatablememes
"""),
    "5-saal-baad": ("2026-11-05_2100_5-saal-baad-reel", [
        dict(dur=2.4, tag="INTERVIEW", head="'5 SAAL BAAD KHUD KO KAHA DEKHTE HO?'", level=0.6, mood="happy", sfx="ding"),
        dict(dur=2.6, tag="MAIN, FULL CONFIDENCE", box="'Sir, leadership role mein,\nteam lead karunga,\ngrowth hi growth'", level=0.5,
             mood="happy", sfx="pop"),
        dict(dur=2.6, tag="5 SAAL BAAD", draw=reel_template("hide-the-pain"), sfx="tick"),
        dict(dur=3.8, head="SAME COMPANY, SAME CHAIR", box="Title mein 'Senior'\nlag gaya. Salary ne\nwo interview suna\nhi nahi tha",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
5 saal ka plan bana tha, bas designation update hua 🙂
office memes aur salary memes for every thaka hua desi jo interview mein 'growth' bolke aaya tha

Send karo us colleague ko jo 5 saal se 'next year promotion pakka' bol raha hai 👇

#thakahuadesi #officememes #salarymemes #desimemes #corporatememes
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
    img = template_meme("is-this-a-pigeon",
                        "Har mahine 5 tareekh ko",
                        labels=["Main", "Salary ka\nSMS", "Kya ye savings hai?"],
                        footer="Nahi beta, ye EMI ka hai")
    out("2026-11-05_1730_salary-pigeon", "image", [img], """
Salary aati hai, bas mere liye nahi aati 🙂
salary memes aur middle class memes for every thaka hua desi jiska account sirf EMI ka transit point hai

Send karo us dost ko jo har mahine 'is baar bachaunga' bolta hai 👇

#thakahuadesi #salarymemes #middleclassmemes #desimemes #emimemes
""")

def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-11-05_1000_mood-story", mood_story("Thursday hai", "Friday: kal\nkaam: aaj hi chahiye\nenergy: 30%", 0.3, "tired"))
    story("2026-11-05_1330_teaser-story", teaser_story("'Are you there?' 10:47 PM", "naya reel feed pe. bhejo us colleague ko jiska boss raat ko message karta hai",
          Q / "2026-11-05_1300_raat-ka-message-reel" / "cover.png"))
    story("2026-11-05_2130_question-story", question_story("Interview", "Interview mein sabse bada jhooth kya bola tha?"))

if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
