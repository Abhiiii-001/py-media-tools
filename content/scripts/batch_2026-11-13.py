"""Batch: 13 Nov 2026 (Friday, 2 days out so evergreen: Friday 5:58 'Hey', exam se pehle ki raat, barber 'thoda sa'): 1300 + 2100 reels, 1730 template image + 3 stories.
Run from repo root: python content/scripts/batch_2026-11-13.py [reels|images|stories]"""


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
    "friday-hey": ("2026-11-13_1300_friday-hey-reel", [
        dict(dur=2.4, tag="FRIDAY, SHAAM 5:58", head="LAPTOP BAND KARNE HI WALA THA", level=0.6, mood="happy", sfx="ding"),
        dict(dur=2.8, tag="TEAMS PE MANAGER", box="5:59 'Hey'\n6:00 typing...\n6:07 typing...\n6:14 abhi bhi typing...", level=0.35,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="MAIN, 'HEY' KE AAGE KA MESSAGE DHOONDTE HUE", draw=reel_template("waiting-skeleton"), sfx="tick"),
        dict(dur=3.8, head="6:19 PM", box="'Nvm, Monday baat karte hai'\nWeekend shuru\nDimaag: 'kya baat\nkarni hogi?'",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Friday 5:59 ka 'Hey' poora weekend kha gaya 🙂
office memes aur friday memes for every thaka hua desi jiska manager 'Hey' bhej ke gaayab ho jaata hai

Send karo us colleague ko jo aaj 5:58 pe laptop band karke bhaagega 👇

#thakahuadesi #officememes #corporatememes #desimemes #relatablememes
"""),
    "haircut-thoda-sa": ("2026-11-13_2100_haircut-thoda-sa-reel", [
        dict(dur=2.4, tag="SALON MEIN", head="'BHAIYA, BAS THODA SA TRIM'", level=0.6, mood="happy", sfx="ding"),
        dict(dur=2.8, tag="AGLE 10 MINUTE", box="Bhaiya: 'haan haan'\nPhone pe call shuru\nMachine on\nPeeche se: silence", level=0.35,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="MAIN, SHEESHE MEIN DEKHTE HUE", draw=reel_template("gajab-bezzati"), sfx="tick"),
        dict(dur=3.8, head="BHAIYA: 'EKDUM MAST, 150 DO'", box="Office: 'naya look?'\nMummy: 'garmi kam lagegi'\nMahina: November\nTopi: ab permanent",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
'Thoda sa' bola tha, bhaiya ne poora sach kaat diya 🙂
desi memes aur relatable memes for every thaka hua desi jo har baar 'bas thoda sa' bolke pachhtata hai

Send karo us dost ko jiska last haircut dekh ke tum hase the 👇

#thakahuadesi #desimemes #relatablememes #indianmemes #funnymemes
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
    img = template_meme("distracted-boyfriend",
                        "Exam se ek raat pehle:",
                        ["YouTube pe\n'how pencils\nare made'", "Main", "14 chapter\nka syllabus"],
                        footer="Padha kuch nahi, pencil expert ban gaya")
    out("2026-11-13_1730_exam-se-pehle", "image", [img], """
Syllabus 14 chapter ka tha, research pencil pe ho gayi 🙂
exam memes aur student memes for every thaka hua desi jiska dimaag sirf exam se ek raat pehle curious hota hai

Send karo us dost ko jo exam se pehle sabse zyada 'gyaan' share karta tha 👇

#thakahuadesi #exammemes #studentmemes #desimemes #relatablememes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-11-13_1000_mood-story", mood_story("Shukravaar ki subah", "body: office mein\ndimaag: weekend pe\nenergy: 40% (Friday bonus)", 0.4, "tired"))
    story("2026-11-13_1330_teaser-story", teaser_story("'Friday 5:59 ka Hey'", "naya reel feed pe. bhejo us colleague ko jiska manager Friday shaam ko hi yaad karta hai",
          Q / "2026-11-13_1300_friday-hey-reel" / "cover.png"))
    story("2026-11-13_2130_question-story", question_story("Sach batao", "Barber ko 'bas thoda sa' bolke sabse bura haircut kab mila?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
