"""Batch made 23 Nov 2026 (9 AM run).
Fill Wed 25 Nov (2 days out, evergreen): 1300 meme reel (lift mein boss ke saath 12 floor ki small talk, Welcome sofa),
1730 image (Is This A Pigeon: pre-approved loan SMS = amiri?), 2100 mascot reel (raat 11 baje, chaabi andar reh gayi),
1000 mood + 1330 teaser + 2130 question stories. No trend swap (nothing fresh verified).
Run from repo root: python content/scripts/batch_2026-11-25.py [reels|images|stories]"""

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
    "lift-boss": ("2026-11-25_1300_lift-boss-reel", [
        dict(dur=2.4, tag="SUBAH 9:58, LIFT MEIN GHUSA", head="ANDAR BOSS KHADA THA", level=0.5, mood="tired", sfx="ding"),
        dict(dur=2.9, tag="FLOOR 1 SE 3:", box="Boss: 'aur, sab badiya?'\nMain: 'haan sir, aap?'\nBoss: 'haan'\n...", level=0.4,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="BAAKI 9 FLOOR, HUM DONO:", draw=reel_template("welcome-sofa"), sfx="tick"),
        dict(dur=3.8, head="AGLE DIN SE SEEDHI", box="12 floor paidal chadha\nUpar boss khada tha\n'Fitness pe kaam\nho raha hai kya?'",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Lift 40 second ki thi, awkwardness 40 saal ki 🙂
office memes aur corporate memes for every thaka hua desi jo boss ko lift mein dekhke 'main agli le lunga' bolta hai

Send karo us colleague ko jo boss ke saath lift mein phone pe busy hone ki acting karta hai 👇

#thakahuadesi #officememes #corporatememes #desimemes #relatablememes
"""),
    "chaabi": ("2026-11-25_2100_chaabi-reel", [
        dict(dur=2.3, tag="RAAT 11 BAJE OFFICE SE LAUTA", head="CHAABI GHAR KE ANDAR", level=0.4, mood="tired", sfx="ding"),
        dict(dur=2.9, tag="OPTIONS:", box="Roommate: phone switch off\nMakaan malik: 'subah aana'\nChaabi wale bhaiya:\n'Rs 800 lagega'",
             level=0.2, mood="tired", sfx="pop"),
        dict(dur=2.3, tag="MAINE BOLA:", box="Theek hai bhaiya,\ntod do", level=0.1, mood="dead", sfx="tick"),
        dict(dur=3.8, head="LOCK TUTA, 800 GAYE", box="Andar jaake jacket utaari\nChaabi jacket ki\ndoosri jeb mein thi\nPoore time se",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Chaabi poore time jeb mein thi, bas dimaag ghar pe reh gaya tha 🙂
desi memes aur bachelor life memes for every thaka hua desi jo har roz darwaze pe 'chaabi kahan rakhi' wala dance karta hai

Send karo us roommate ko jiska phone hamesha tab band hota hai jab chaabi uske paas ho 👇

#thakahuadesi #desimemes #bachelorlife #relatablememes #hinglishmemes
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
                        "Mahine ki 25 taareekh, account mein Rs 640, aur phir ek SMS aaya",
                        labels=["Main", "'Rs 2 lakh ka pre-approved loan'", "Kya main ameer ho gaya?"])
    out("2026-11-25_1730_loan-sms", "image", [img], """
Account mein 640, SMS mein 2 lakh, dil mein Ambani 🙂
salary memes aur desi memes for every thaka hua desi jise bank sirf mahine ke end mein yaad karta hai

Send karo us dost ko jo har 'pre-approved' SMS pe 1 second ke liye khush ho jaata hai 👇

#thakahuadesi #salarymemes #desimemes #relatablememes #indianmemes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-11-25_1000_mood-story", mood_story("Budhvaar ki subah", "hafta aadha gaya\nmain poora gaya\nchai: 2\nenergy: 25%", 0.25, "tired"))
    story("2026-11-25_1330_teaser-story", teaser_story("Lift mein boss mil gaya", "naya reel feed pe. bhejo us colleague ko jo boss ko dekhke agli lift leta hai",
          Q / "2026-11-25_1300_lift-boss-reel" / "cover.png"))
    story("2026-11-25_2130_question-story", question_story("Sach batao", "Chaabi bhool ke kabhi ghar ke bahar atke ho? Kitni der?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
