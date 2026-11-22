"""Batch made 22 Nov 2026 (9 AM run).
Fill Tue 24 Nov (2 days out, evergreen): 1300 meme reel (guests coming, room 'saaf' = sab almirah mein, Hide the Pain),
1730 image (Squidward window: who are these people in a cafe on Tuesday 3 PM), 2100 mascot reel (phone 9% bahar nikalte hi),
1000 mood + 1330 teaser + 2130 question stories. No trend swap (nothing fresh verified).
Run from repo root: python content/scripts/batch_2026-11-24.py [reels|images|stories]"""

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
    "guest-almirah": ("2026-11-24_1300_guest-almirah-reel", [
        dict(dur=2.4, tag="MUMMY:", head="'GUEST AA RAHE HAI, ROOM SAAF KARO'", level=0.5, mood="tired", sfx="ding"),
        dict(dur=2.9, tag="MERI 10 MINUTE KI SAFAI:", box="Kapde: almirah mein\nCharger, chips: almirah mein\nGeela towel: almirah mein\nDarwaza dhakka maarke band", level=0.4,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="AUNTY: 'KITNA SAAF ROOM!' MAIN:", draw=reel_template("hide-the-pain"), sfx="tick"),
        dict(dur=3.8, head="GUEST GAYE, ALMIRAH KHOLI", box="Sab neeche gir gaya\n3 hafte purane kapde\nEk khoya hua remote\nAur peeche mummy ki chappal",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Room 10 minute mein saaf ho gaya, almirah 10 saal ke liye kharab 🙂
desi memes aur indian mom memes for every thaka hua desi jiski safai ka matlab hai sab almirah mein thoosna

Send karo us bhai/behen ko jiski almirah kholna mana hai 👇

#thakahuadesi #desimemes #indianmommemes #relatablememes #desifamily
"""),
    "battery-9": ("2026-11-24_2100_battery-9-reel", [
        dict(dur=2.3, tag="GHAR SE NIKLA", head="PHONE: 9% BATTERY", level=0.5, mood="tired", sfx="ding"),
        dict(dur=2.9, tag="AAJ KE KAAM:", box="Cab book karni hai\nUPI se payment karna hai\nMaps chalana hai\nMummy ko 'pahunch gaya' bolna",
             level=0.3, mood="tired", sfx="pop"),
        dict(dur=2.3, tag="MERA PLAN:", box="Brightness 0\nBattery saver on\nKoi reel nahi dekhunga", level=0.6, mood="happy", sfx="tick"),
        dict(dur=3.8, head="2 REEL BAAD: 1%", box="Phone band, cab wala: 'cash do'\n3 km paidal\nMummy ke 14 missed call\nCharger dost le gaya tha",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
9% mein poora din chalana tha, 2 reel mein khatam 🙂
desi memes aur relatable memes for every thaka hua desi jiska phone hamesha 10% pe hi ghar se nikalta hai

Send karo us dost ko jo hamesha 'charger hai kya?' poochta hai 👇

#thakahuadesi #desimemes #relatablememes #indianmemes #hinglishmemes
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
                        "Main office se, Tuesday dopahar 3 baje cafe mein baithe logo ko dekhte hue",
                        footer="Inki naukri kya hai?? Mujhe bhi chahiye")
    out("2026-11-24_1730_tuesday-cafe", "image", [img], """
Tuesday 3 baje cafe mein kaun baitha hota hai?? Mujhe bhi wahi naukri chahiye 🙂
office memes aur corporate memes for every thaka hua desi jo weekday pe sirf office ki khidki se duniya dekhta hai

Send karo us dost ko jo har weekday cafe se story daalta hai 👇

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
    story("2026-11-24_1000_mood-story", mood_story("Mangalvaar ki subah", "Monday gaya\npar Monday wali feeling nahi gayi\nchai: 1 (aur chahiye)\nenergy: 30%", 0.3, "tired"))
    story("2026-11-24_1330_teaser-story", teaser_story("'Beta kitna saaf room hai'", "naya reel feed pe. bhejo us bhai/behen ko jiski almirah kholna mana hai",
          Q / "2026-11-24_1300_guest-almirah-reel" / "cover.png"))
    story("2026-11-24_2130_question-story", question_story("Sach batao", "Phone kitne % pe aate hi panic shuru hota hai?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
