"""Batch: 24 Oct 2026 trend swap (IND vs NZ 2nd T20I) 1300 reel + teaser, and
25 Oct 2026 (Sunday, evergreen): 1300 reel, 1730 image, 2100 reel + 3 stories.
Run from repo root: python content/scripts/batch_2026-10-23.py [reels|images|stories]"""

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
    "chase": ("2026-10-24_1300_salary-chase-reel", [
        dict(dur=2.4, tag="PICHLE MATCH MEIN", head="INDIA NE 226 CHASE KAR LIYA", level=0.8, mood="happy", sfx="ding"),
        dict(dur=2.6, tag="4 WICKET JALDI GIRE, PHIR BHI", box="Pressure mein bhi\n2 ball pehle\nmatch khatam", level=0.7,
             mood="happy", sfx="pop"),
        dict(dur=2.6, tag="AUR MERA CHASE?", draw=reel_template("hide-the-pain"), sfx="tick"),
        dict(dur=3.8, head="SALARY TAK 7 DIN", box="Account mein Rs 1,100\nRequired rate: Rs 157/din\nWicket: sab gir chuke",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
India ne 226 chase kar liya, main mahine ke last 7 din chase nahi kar paata 🙂
cricket memes aur salary memes for every thaka hua desi jiska account 24 tareekh ko hi all out ho jaata hai

Send karo us dost ko jo abhi 'bas salary aane do' bol raha hai 👇

#thakahuadesi #cricketmemes #indvsnz #salarymemes #desimemes
"""),
    "khana": ("2026-10-25_1300_kya-banau-reel", [
        dict(dur=2.4, tag="SUNDAY, 11 BAJE", head="MUMMY: 'AAJ KYA BANAU?'", level=0.6, mood="happy", sfx="ding"),
        dict(dur=2.6, tag="MAIN: 'KUCH BHI'", box="Rajma? nahi\nPaneer? nahi\nBhindi? bilkul nahi", level=0.4,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="MUMMY: 'TOH KHUD BANA LE'", draw=reel_template("3idiots-old-man"), sfx="tick"),
        dict(dur=3.8, head="1 GHANTE BAAD", box="Wahi dal chawal\njo pehle se\nbanna tha",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
'Kuch bhi' bola tha, kuch bhi mein bhi options nahi hote 🙂
indian mom memes aur desi memes, har Sunday ki same kahani

Send karo us dost ko jo 'kuch bhi' bolke har cheez pe nahi bolta 👇

#thakahuadesi #indianmom #desimemes #sundaymemes #relatablememes
"""),
    "dhaniya": ("2026-10-25_2100_dhaniya-pudina-reel", [
        dict(dur=2.4, tag="MUMMY", head="'BETA BAS 3 CHEEZ LE AA'", level=0.6, mood="happy", sfx="ding"),
        dict(dur=2.6, tag="DUKAAN PE PHONE AAYA", box="'Aur haan, doodh,\nanda, bread, Maggi,\naur dhaniya bhi'", level=0.4,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="GHAR PAHUNCH KE", draw=reel_template("gajab-bezzati"), sfx="tick"),
        dict(dur=3.8, head="'YE PUDINA HAI'", box="25 saal ka ho gaya,\nsalary leta hu,\ndhaniya nahi pehchanta",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Office mein senior hu, sabzi mandi mein abhi bhi intern 🙂
desi memes aur indian mom memes for every beta jo 3 cheez lene gaya aur galat 1 laaya

Send karo us dost ko jo dhaniya aur pudina mein confuse hota hai 👇

#thakahuadesi #desimemes #indianmom #relatablememes #desikids
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
                        "Sunday 12 baje utha toh Mummy vs Main:",
                        labels=["Sharma ji ka beta 6 baje uthta hai!", "Uski salary bhi 6 guna hai"],
                        footer="Comparison karna hai toh poora karo")
    out("2026-10-25_1730_sharma-ji-jogging", "image", [img], """
Sharma ji ka beta 6 baje uthta hai, uski salary bhi 6 guna hai 🙂
indian parents memes aur desi memes for every Sunday ka 12 baje wala riser

Send karo us dost ko jiske ghar bhi ek Sharma ji ka beta hai 👇

#thakahuadesi #indianparents #desimemes #sharmajikabeta #relatablememes
""")

def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-10-24_1330_teaser-story", teaser_story("India ka chase vs mera chase", "naya reel feed pe. bhejo us dost ko jiska account 24 ko hi all out hai",
          Q / "2026-10-24_1300_salary-chase-reel" / "cover.png"))
    story("2026-10-25_1000_mood-story", mood_story("Sunday hai", "mera plan: kuch nahi\nmummy ka plan: sab kuch\nchai: teesri", 0.5, "tired"))
    story("2026-10-25_1330_teaser-story", teaser_story("Sunday ka 'kya banau?'", "naya reel feed pe. bhejo us dost ko jo 'kuch bhi' bolke sab pe nahi bolta",
          Q / "2026-10-25_1300_kya-banau-reel" / "cover.png"))
    story("2026-10-25_2130_question-story", question_story("Sach batao", "Sabzi lene gaye aur galat cheez laaye ho? Kya laaye the?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
