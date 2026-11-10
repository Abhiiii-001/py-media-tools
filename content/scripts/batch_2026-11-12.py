"""Batch: 12 Nov 2026 (Thursday, 2 days out so evergreen: thand mein nahana, UPI pending, Thursday energy): 1300 + 2100 reels, 1730 template image + 3 stories.
Run from repo root: python content/scripts/batch_2026-11-12.py [reels|images|stories]"""

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
    "thand-mein-nahana": ("2026-11-12_1300_thand-mein-nahana-reel", [
        dict(dur=2.4, tag="NOVEMBER, SUBAH 8:40", head="OFFICE 9:30 KA HAI AUR PAANI BARF HAI", level=0.6, mood="tired", sfx="ding"),
        dict(dur=2.8, tag="TIMELINE", box="8:41 geyser on\n8:45 'garam hone do'\n8:55 bas 2 reel aur\n9:12 paani garam, time khatam", level=0.35,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="MAIN, BATHROOM KE BAHAR", draw=reel_template("two-buttons", ["Nahana", "Office time pe", "Main, towel leke"]), sfx="tick"),
        dict(dur=3.8, head="9:28 OFFICE PAHUNCH GAYA", box="Nahaya nahi, deo maara\nManager: 'aaj fresh\nlag rahe ho'\nGeyser abhi bhi on hai",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Geyser 30 min mein garam hua, mera time 30 min pehle khatam 🙂
winter memes aur office memes for every thaka hua desi jo thand mein 'kal pakka nahaunga' bolta hai

Send karo us dost ko jo aaj bhi sirf deo pe chal raha hai 👇

#thakahuadesi #wintermemes #officememes #desimemes #relatablememes
"""),
    "upi-pending": ("2026-11-12_2100_upi-pending-reel", [
        dict(dur=2.4, tag="CHAI WALE BHAIYA KE PAAS", head="SCAN KIYA, Rs 20 BHEJE", level=0.6, mood="happy", sfx="ding"),
        dict(dur=2.8, tag="UPI KA DRAMA", box="Mera phone: 'Debited'\nBhaiya ka phone: kuch nahi\nUPI: 'Payment pending'\nPeeche line: 7 log", level=0.35,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="MAIN AUR BHAIYA, DONO PHONE DEKHTE HUE", draw=reel_template("ab-tak-aa-jana-chahiye"), sfx="tick"),
        dict(dur=3.8, head="BHAIYA: 'EK BAAR AUR KARO'", box="Dobara kiya, dobara kata\nRefund: 3-5 working days\nChai: Rs 20\nMera nuksaan: Rs 40",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Chai 20 ki thi, UPI ne 40 ki bana di 🙂
upi memes aur salary memes for every thaka hua desi jiske 'payment pending' wale paise abhi tak hawa mein hai

Send karo us dost ko jo har baar 'ek baar aur scan karo' bolta hai 👇

#thakahuadesi #upimemes #salarymemes #desimemes #relatablememes
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
                        "Same hafta, same main:",
                        ["Monday: 'is hafte sab\nkhatam karunga'", "Thursday: 'kal Friday\nhai, kal dekhenge'"])
    out("2026-11-12_1730_thursday-energy", "image", [img], """
Monday ka josh Thursday tak 'kal dekhenge' ban jaata hai 🙂
office memes aur monday memes for every thaka hua desi jiska to-do list har hafte next week shift hota hai

Tag karo us colleague ko jo aaj se hi Friday mode mein hai 👇

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
    story("2026-11-12_1000_mood-story", mood_story("Guruvaar ki subah", "thand: full\nrazai: chhodne ko tayyar nahi\nenergy: 20%", 0.2, "tired"))
    story("2026-11-12_1330_teaser-story", teaser_story("'Thand mein nahana'", "naya reel feed pe. bhejo us dost ko jo aaj bhi sirf deo pe chal raha hai",
          Q / "2026-11-12_1300_thand-mein-nahana-reel" / "cover.png"))
    story("2026-11-12_2130_question-story", question_story("Sach batao", "Thand mein na nahane ka tumhara sabse best bahana kya hai?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
