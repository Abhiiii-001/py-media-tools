"""Batch made 25 Nov 2026 (9 AM run).
Fill Fri 27 Nov (2 days out, evergreen): 1300 meme reel (dost ka 'bas thoda saaman', Hera Pheri trio shock),
1730 image (Woman Yelling At Cat: Papa vs light on reh gayi), 2100 = backlog movie-dhoondh reel (Friday night),
1000 mood + 1330 teaser stories, 2130 = backlog movie-dhoondh question story. No trend swap.
Run from repo root: python content/scripts/batch_2026-11-27.py [reels|images|stories]"""

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
    "shifting-help": ("2026-11-27_1300_shifting-help-reel", [
        dict(dur=2.4, tag="FRIDAY RAAT, DOST KA CALL", head="'BHAI KAL FREE HAI?'", level=0.5, mood="tired", sfx="ding"),
        dict(dur=2.8, tag="MAIN KHUSH, PARTY HOGI", box="'Haan bhai bol na'\nDost: 'shift kar raha hu,\nbas thoda sa saaman hai'", level=0.4,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="SATURDAY SUBAH, 'THODA SA':", draw=reel_template("hera-pheri-trio-shock"), sfx="tick"),
        dict(dur=3.8, head="SHAAM 7 BAJE", box="4th floor, lift nahi\n1 almirah, 1 fridge, 28 carton\nPayment: 1 Pepsi aur\n'tu hi asli dost hai'",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
'Bas thoda sa saaman' bola tha, poora ghar utha ke 4th floor pe le gaye 🙂
dosti memes aur desi memes for every thaka hua desi jiska Saturday dost ki shifting kha gayi

Send karo us dost ko jo saal mein ek hi baar call karta hai, shifting ke din 👇

#thakahuadesi #dostimemes #desimemes #relatablememes #indianmemes
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
    img = template_meme("woman-yelling-cat",
                        "Kamre se sirf 5 second ke liye paani peene nikla aur light on reh gayi:",
                        labels=["Papa: 'Bijli muft ki hai kya??'", "Main, glass haath mein, 5 second baad"])
    out("2026-11-27_1730_light-on", "image", [img], """
5 second ki light, 45 minute ka lecture, aur saath mein 2015 ka AC wala kissa bhi 🙂
indian parents memes aur desi memes for every thaka hua desi jiske ghar mein Papa hi bijli vibhag hai

Send karo us bhai/behen ko jisne bhi ye lecture suna hai 👇

#thakahuadesi #indianparentsmemes #desimemes #relatablememes #indianmemes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-11-27_1000_mood-story", mood_story("Shukravaar ki subah", "body office mein\ndimaag weekend pe\nchai: 3\nenergy: 15%\n(6 baje 100%)", 0.15, "tired"))
    story("2026-11-27_1330_teaser-story", teaser_story("'Bas thoda sa saaman hai'", "naya reel feed pe. bhejo us dost ko jo sirf shifting pe yaad karta hai",
          Q / "2026-11-27_1300_shifting-help-reel" / "cover.png"))
    # 2130 question story = backlog movie-dhoondh-question-story (ties to the 2100 backlog reel)


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
