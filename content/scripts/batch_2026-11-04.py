"""Batch: 6 Nov 2026 (Friday, evergreen): 1300 + 2100 reels, 1730 image + 3 stories.
Run from repo root: python content/scripts/batch_2026-11-04.py [reels|images|stories]"""

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
    "tatkal-ticket": ("2026-11-06_1300_tatkal-ticket-reel", [
        dict(dur=2.4, tag="10:00:00 AM", head="TATKAL KHUL GAYA, GHAR JAANA HAI", level=0.6, mood="happy", sfx="ding"),
        dict(dur=2.6, tag="10:00:01 SE 10:02", box="Captcha galat\nOTP late aaya\nPayment page loading...\nloading...", level=0.3,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="WO DOST JISNE 2 MAHINE PEHLE BOOK KIYA", draw=reel_template("raju-laughing"), sfx="tick"),
        dict(dur=3.8, head="STATUS: WL 247", box="Bus wala 3 guna\nfare maang raha.\nIs baar ghar sirf\nvideo call pe jaunga",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Ghar jaane ka plan tha, IRCTC ka plan kuch aur tha 🙂
desi memes aur relatable memes for every thaka hua desi jo 9:59 se refresh daba raha tha

Send karo us dost ko jisne 2 mahine pehle ticket karwa li thi 👇

#thakahuadesi #desimemes #relatablememes #indianmemes #officememes
"""),
    "monday-quick-call": ("2026-11-06_2100_monday-quick-call-reel", [
        dict(dur=2.4, tag="FRIDAY 5:58 PM", head="MANAGER: 'MONDAY QUICK CALL, KUCH DISCUSS KARNA HAI'", level=0.5, mood="tired", sfx="ding"),
        dict(dur=2.6, tag="DIMAAG, POORA WEEKEND", box="Kya discuss?\nKoi galti hui?\nAppraisal? Layoff?\nMain hi kyun?", level=0.3,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="MAIN, SUNDAY RAAT 2 BAJE", draw=reel_template("this-is-fine"), sfx="tick"),
        dict(dur=3.8, head="MONDAY 10 BAJE", box="'Haan, bas ye poochna\ntha, team lunch\nWednesday ko\nrakh le?'",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
2 minute ki call ke liye 2 din ka overthinking 🙂
office memes aur corporate memes for every thaka hua desi jiska weekend ek 'quick call' kha gaya

Send karo us colleague ko jo 'kuch discuss karna hai' sunke hi pasina pasina ho jaata hai 👇

#thakahuadesi #officememes #corporatememes #overthinking #desimemes
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
    img = template_meme("squidward-window",
                        "Diwali wala Friday:\naadhi team gayab",
                        footer="Mera leave request: abhi bhi 'pending'")
    out("2026-11-06_1730_aadhi-team-chutti", "image", [img], """
Office khaali hai, bas main bhara hua hu 🙂
office memes aur desi memes for every thaka hua desi jo Diwali se pehle wale Friday ko bhi login hai

Send karo us colleague ko jo already ghar pahunch gaya 👇

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
    story("2026-11-06_1000_mood-story", mood_story("Friday hai", "weekend: aa raha\nkaam: abhi bhi pending\nenergy: 40%", 0.4, "tired"))
    story("2026-11-06_1330_teaser-story", teaser_story("Tatkal 10:00:00 AM", "naya reel feed pe. bhejo us dost ko jiski ticket waiting mein hai",
          Q / "2026-11-06_1300_tatkal-ticket-reel" / "cover.png"))
    story("2026-11-06_2130_question-story", question_story("Friday 6 PM", "Manager ka sabse darawna message kya hai?"))

if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
