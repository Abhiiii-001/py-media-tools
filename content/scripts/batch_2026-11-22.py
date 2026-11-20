"""Batch made 20 Nov 2026 (9 AM run).
Fill Sun 22 Nov (2 days out, evergreen): 1300 reel + 1330 teaser are the backlog `sunday-screen-time` pair (gap filler).
New: 1730 image (Jethalal reactions: Sunday 'bas 20 min ki jhapki'), 2100 reel (Sunday 11:40 PM Monday shirt + iron,
This Is Fine), 1000 mood + 2130 question stories. No trend swap (nothing fresh verified).
Run from repo root: python content/scripts/batch_2026-11-22.py [reels|images|stories]"""

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
    "monday-shirt": ("2026-11-22_2100_monday-shirt-reel", [
        dict(dur=2.4, tag="SUNDAY, RAAT 11:40", head="'KAL OFFICE MEIN KYA PEHNU?'", level=0.5, mood="tired", sfx="ding"),
        dict(dur=2.9, tag="ALMIRAH KHOLI", box="Saari shirts dhulne mein\nEk mili, poori silwatein\nIron on kiya\nLight chali gayi", level=0.25,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="MAIN, 11:58 PM:", draw=reel_template("this-is-fine"), sfx="tick"),
        dict(dur=3.8, head="MONDAY 9:30 AM", box="Upar se jacket pehen li\nAndar wahi silwat wali shirt\nAC band, phir bhi jacket on\n'Thand lag rahi hai yaar'",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Shirt pe silwatein thi, toh jacket ne izzat bacha li 🙂
office memes aur monday memes for every thaka hua desi jiska Monday ka outfit Sunday raat 11:58 pe decide hota hai

Send karo us colleague ko jo AC band hone pe bhi jacket nahi utaarta 👇

#thakahuadesi #officememes #mondaymemes #desimemes #relatablememes
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
                        "Sunday dopahar: 'bas 20 minute ki jhapki'",
                        labels=["3:00 PM: bas 20 min", "7:40 PM: aankh khuli, andhera", "Subah hai ya shaam??", "Yaad aaya: kal Monday hai"],
                        footer="Jhapki 20 min ki thi, Sunday poora le gayi")
    out("2026-11-22_1730_sunday-jhapki", "image", [img], """
20 minute ki jhapki li thi, Sunday hi kha gayi 🙂
sunday memes aur desi memes for every thaka hua desi jo shaam 7 baje uthke 'main kaun hu' soch raha hai

Send karo us dost ko jo har Sunday 'bas 20 min' bolke 4 ghante sota hai 👇

#thakahuadesi #sundaymemes #desimemes #relatablememes #indianmemes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-11-22_1000_mood-story", mood_story("Ravivaar ki subah", "chutti ka last din\n'aaj kuch productive\nkarunga' (nahi karunga)\nenergy: 60% (6 baje tak)", 0.6, "happy"))
    story("2026-11-22_2130_question-story", question_story("Sach batao", "Monday ke kapde Sunday raat press karte ho ya Monday subah jugaad?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
