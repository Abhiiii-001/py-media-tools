"""Batch: 18 Oct 2026 (Sunday, evergreen): 1300 reel, 1730 template meme, 2100 reel + 3 stories.
Run from repo root: python content/scripts/batch_2026-10-16.py [reels|images|stories]"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from brand import save  # noqa: E402
from memes import reel_template, template_meme  # noqa: E402
from reel import render_reel  # noqa: E402
from stories import mood_story, question_story, teaser_story  # noqa: E402

Q = ROOT / "content" / "queue"

REELS = {
    "sunday-dar": ("2026-10-18_1300_sunday-dar-reel", [
        dict(dur=2.4, tag="SUNDAY 11 AM", head="AAJ KUCH NAHI KARUNGA. FULL AARAM", level=0.9, mood="happy", sfx="ding"),
        dict(dur=2.4, tag="SUNDAY 6 PM", box="Dimaag: 'kal Monday hai. wo pending mail yaad hai?'", level=0.4,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="SHAAM 6 BAJE KA DIL", draw=reel_template("dhak-dhak"), sfx="tick"),
        dict(dur=3.8, head="MONDAY 9:30 AM", box="Boss: 'weekend kaisa tha?'\nMain: 'accha tha sir' (aadha Monday ke dar mein gaya)",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Sunday ki chhutti 6 baje tak hi valid hai 🙂
sunday memes aur office memes for everyone jo abhi se Monday soch raha hai

Send karo us dost ko jiska Sunday bhi Monday ne kha liya 👇

#thakahuadesi #officememes #mondaymemes #desimemes #corporatememes
"""),
    "salary-plan": ("2026-10-18_2100_salary-plan-reel", [
        dict(dur=2.4, tag="IS MAHINE PAKKA", head="AB SE SAVING SHURU", level=1.0, mood="happy", sfx="ding"),
        dict(dur=3.2, tag="MERA FINANCIAL PLAN", draw=reel_template("gru-plan",
             ["salary aayi", "SIP shuru", "4 din baad", "balance ₹212"]), sfx="tick"),
        dict(dur=2.2, box="SIP ki jagah: Swiggy, Zepto, 'sale mein sasta tha', dost ki party", level=0.3,
             mood="tired", sfx="pop"),
        dict(dur=3.6, head="NAYA PLAN", box="'next month se pakka'\n(pichle 14 mahine se yahi plan hai)",
             level=0.03, mood="dead", sfx="trombone", shake=True),
    ], """
Plan solid hai, bas har mahine postpone hota hai 🙂
salary memes aur desi memes for every 'next month se pakka' wala

Send karo us dost ko jo 2 saal se SIP shuru kar raha hai 👇

#thakahuadesi #salarymemes #desimemes #middleclassmemes #adultingmemes
"""),
}


def out_image(folder, img, caption):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    save(img, f / "1.png")
    (f / "caption.txt").write_text(caption.strip() + "\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "image", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def images():
    out_image("2026-10-18_1730_sunday-relatives", template_meme(
        "welcome-sofa",
        "Sunday ko relatives aaye aur 10 min mein pooch liya: salary kitni hai, shaadi kab, aur 'thoda mota ho gaya na?'\nMera face:",
        footer="jaate jaate: 'Diwali pe phir aayenge beta'"), """
Aaye the chai peene, gaye meri poori life audit karke 🙂
relatives memes, desi family ka Sunday special

Tag karo us dost ko jiske ghar is Sunday bhi relatives aa rahe hai 👇

#thakahuadesi #relativesmemes #desifamily #desimemes #indianmemes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-10-18_1000_mood-story", mood_story("Sunday hai", "subah: full aaram\nshaam: Monday ka dar\nraat: 5 alarm set", 0.7, "happy"))
    story("2026-10-18_1330_teaser-story", teaser_story("Sunday 6 PM wala dar", "naya reel feed pe. bhejo us dost ko jo abhi se Monday soch raha hai",
          Q / "2026-10-18_1300_sunday-dar-reel" / "cover.png"))
    story("2026-10-18_2130_question-story", question_story("Kal Monday hai", "Monday ke liye kitne alarm lagaye? Sach batao"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
