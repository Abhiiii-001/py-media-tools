"""Batch: 27 Oct 2026 (Tuesday, evergreen): 1300 reel, 1730 image, 2100 reel + 3 stories.
Run from repo root: python content/scripts/batch_2026-10-25.py [reels|images|stories]"""

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
    "fees": ("2026-10-27_1300_food-fees-reel", [
        dict(dur=2.4, tag="APP PE KHANA", head="BIRYANI: RS 249", level=0.6, mood="happy", sfx="ding"),
        dict(dur=2.8, tag="CHECKOUT PE", box="Delivery fee: 40\nPlatform fee: 12\nPackaging: 25\nSmall cart fee: 30\n+ GST", level=0.35,
             mood="tired", sfx="pop"),
        dict(dur=2.4, tag="TOTAL DEKH KE", draw=reel_template("hera-pheri-trio-shock"), sfx="tick"),
        dict(dur=3.8, head="RS 412. KAL SE GHAR KA KHANA", box="Kal bhi order kiya.\nKhana 249 ka tha,\nbaaki sab meri izzat ka",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Biryani 249 ki thi, fees ne 412 bana di 🙂
food memes aur salary memes for every thaka hua desi jo roz 'kal se ghar ka khana' bolta hai

Send karo us dost ko jo checkout pe aake hi ruk jaata hai 👇

#thakahuadesi #foodmemes #salarymemes #desimemes #relatablememes
"""),
    "mummy": ("2026-10-27_2100_khana-khaya-reel", [
        dict(dur=2.4, tag="PG, RAAT 10 BAJE", head="MUMMY: 'KHANA KHAYA?'", level=0.5, mood="tired", sfx="ding"),
        dict(dur=2.6, tag="MAIN", box="'Haan mummy, dal sabzi roti,\nekdum ghar jaisa'", level=0.4,
             mood="happy", sfx="pop"),
        dict(dur=2.6, tag="ASLI PLATE: TEESRE DIN KI MAGGI", draw=reel_template("monkey-puppet"), sfx="tick"),
        dict(dur=3.8, head="MUMMY: 'AAWAZ KAMZOR KYU HAI?'", box="1000 km door se\nMaggi pakad li.\nMaa ko sab pata hai",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Jhooth bolne ka koi fayda nahi, mummy aawaz se plate dekh leti hai 🙂
indian mom memes aur pg life memes for every ghar se door thaka hua desi

Send karo us dost ko jo roz 'haan mummy kha liya' bolta hai 👇

#thakahuadesi #indianmommemes #desimemes #pglife #hostelmemes
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
    img = template_meme("drake",
                        "Halka sa sir dard:",
                        labels=["Doctor ko dikhana", "Google pe symptoms padh ke\n4 bimaari confirm karna"],
                        footer="Raat 2 baje tak will bhi likh di")
    out("2026-10-27_1730_google-doctor", "image", [img], """
Sir dard tha, Google ne poori medical file bana di 🙂
overthinking memes aur adulting memes for every thaka hua desi jo doctor ki jagah Google ko fees deta hai

Send karo us dost ko jo har chheenk pe symptoms search karta hai 👇

#thakahuadesi #overthinkingmemes #adultingmemes #desimemes #relatablememes
""")

def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-10-27_1000_mood-story", mood_story("Tuesday hai", "Monday ka hangover: baaki\nFriday: 3 din door\nenergy: 14%", 0.15, "tired"))
    story("2026-10-27_1330_teaser-story", teaser_story("Biryani 249 ki, bill 412 ka", "naya reel feed pe. bhejo us dost ko jo checkout pe ruk jaata hai",
          Q / "2026-10-27_1300_food-fees-reel" / "cover.png"))
    story("2026-10-27_2130_question-story", question_story("Sach batao", "Mummy ko 'khana kha liya' bolke kabhi Maggi khayi hai?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
