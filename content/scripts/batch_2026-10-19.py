"""Batch: 21 Oct 2026 (Wednesday, evergreen): 1730 image, 2100 reel + 3 stories.
1300 slot is the backlog `sale-cart-reel` (gap filler, moved from content/backlog/).
Run from repo root: python content/scripts/batch_2026-10-19.py [reels|images|stories]"""
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
    "appraisal": ("2026-10-21_2100_appraisal-hike-reel", [
        dict(dur=2.4, tag="APPRAISAL MEETING", head="MANAGER: 'IS SAAL COMPANY KA BAHUT ACCHA GAYA'", level=0.8, mood="happy", sfx="ding"),
        dict(dur=2.6, tag="MAIN, MANN MEIN", box="Bas 30% bhi mil jaaye\ntoh EMI aur Goa dono set",
             level=0.7, mood="happy", sfx="pop"),
        dict(dur=2.6, tag="HIKE LETTER KHULA", draw=reel_template("150-rupiya-dega"), sfx="tick"),
        dict(dur=3.8, head="HIKE: 3%", box="Mehngai: 6%.\nMatlab is saal maine\ncompany ko pay kiya",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Company ka saal accha gaya, mera nahi 🙂
appraisal memes aur salary memes for everyone jiska hike chai se bhi kam hai

Send karo us colleague ko jo abhi bhi 'is baar accha hike milega' bol raha hai 👇

#thakahuadesi #appraisalmemes #salarymemes #officememes #desimemes
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
    img = template_meme("trade-offer",
                        "Friday 6:58 PM, boss ka message:",
                        labels=["Saturday\n'bas 1 ghanta'\nka kaam", "'Thanks for\nbeing a team\nplayer'"],
                        footer="1 ghanta = poora Saturday")
    out("2026-10-21_1730_team-player", "image", [img], """
'Bas 1 ghanta' bola tha, Saturday hi chala gaya 🙂
office memes aur corporate memes for every 'team player' jo bas mana nahi kar paaya

Send karo us colleague ko jo har Saturday 'team player' banta hai 👇

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
    story("2026-10-21_1000_mood-story", mood_story("Wednesday hai", "hafta: aadha gaya\nenergy: poori gayi\nchai: 2nd cup, 10 baje hi", 0.2, "tired"))
    story("2026-10-21_1330_teaser-story", teaser_story("Cart full, account khaali", "naya reel feed pe. bhejo us dost ko jiska cart uski salary se mehenga hai",
          Q / "2026-10-21_1300_sale-cart-reel" / "cover.png"))
    story("2026-10-21_2130_question-story", question_story("Hike check", "Is saal ka hike kitna aaya? Ya abhi bhi 'process mein hai'?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
