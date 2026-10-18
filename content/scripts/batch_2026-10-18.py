"""Batch: 20 Oct 2026 (Tuesday, evergreen): 1300 reel, 1730 image, 2100 reel + 3 stories.
Run from repo root: python content/scripts/batch_2026-10-18.py [reels|images|stories]"""
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
    "camera-on": ("2026-10-20_1300_camera-on-reel", [
        dict(dur=2.4, tag="10:30 AM, TEAM CALL", head="BOSS: 'SAB CAMERA ON KARO'", level=0.8, mood="happy", sfx="ding"),
        dict(dur=2.6, tag="MERI HALAT", box="Upar formal shirt. Neeche shorts.\nPeeche bistar khula, mummy pocha laga rahi",
             level=0.5, mood="tired", sfx="pop"),
        dict(dur=2.6, tag="MOUSE CAMERA BUTTON PE", draw=reel_template("dhak-dhak"), sfx="tick"),
        dict(dur=3.8, head="MAIN:", box="'Sir mera camera kharab hai'\n(2 saal se kharab hai. Zoom pe bhi, Teams pe bhi)",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Camera 2 saal se kharab hai, aur kharab hi rahega 🙂
wfh memes aur office memes for everyone jo 'net slow hai sir' bolke bach jaata hai

Send karo us colleague ko jiska camera kabhi on nahi hota 👇

#thakahuadesi #wfhmemes #officememes #corporatememes #desimemes
"""),
    "gym": ("2026-10-20_2100_gym-membership-reel", [
        dict(dur=2.4, tag="1 JANUARY", head="IS SAAL BODY BANAKE RAHUNGA", level=0.95, mood="happy", sfx="ding"),
        dict(dur=2.6, tag="12 MAHINE KI MEMBERSHIP", box="Rs 18,000 ek saath.\n'Monthly loge toh mehenga padega sir'",
             level=0.6, mood="happy", sfx="pop"),
        dict(dur=2.6, tag="OCTOBER: GYM GAYA 4 BAAR", draw=reel_template("hera-pheri-trio-shock"), sfx="tick"),
        dict(dur=3.8, head="PER VISIT: Rs 4,500", box="Itne mein 5 star hotel mein nahaa leta.\nBody nahi bani.\nGym wale ki Diwali ban gayi",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
'Kal se gym' 10 mahine se chal raha hai 🙂
gym memes aur adulting memes for every 'kal se pakka' wala

Send karo us dost ko jo January se 'kal se gym' bol raha hai 👇

#thakahuadesi #gymmemes #adultingmemes #desimemes #relatablememes
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
    img = template_meme("waiting-skeleton",
                        "Group chat: 'Is baar Goa pakka chalenge, dates fix karo'\n\nGoa plan, 2016 se:",
                        footer="dates abhi bhi fix ho rahi hai")
    out("2026-10-20_1730_goa-plan", "image", [img], """
Goa plan 2016 mein bana tha, ab tak sirf group ka naam badla hai 🙂
friends memes aur desi memes for every group chat ka 'pakka plan'

Apne group mein bhejo, dekhte hai kaun pehle 'is baar pakka' bolta hai 👇

#thakahuadesi #goaplan #friendsmemes #desimemes #relatablememes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-10-20_1000_mood-story", mood_story("Tuesday hai", "Monday ka hangover: 100%\nFriday: abhi bhi 3 din door\nchai: 3rd cup", 0.25, "tired"))
    story("2026-10-20_1330_teaser-story", teaser_story("'Sir camera kharab hai'", "naya reel feed pe. bhejo us colleague ko jiska camera kabhi on nahi hota",
          Q / "2026-10-20_1300_camera-on-reel" / "cover.png"))
    story("2026-10-20_2130_question-story", question_story("Pakka plan", "Tumhare group ka 'is baar pakka' plan kitne saal se pending hai?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
