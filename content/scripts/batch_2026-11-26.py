"""Batch made 24 Nov 2026 (9 AM run).
Fill Thu 26 Nov (2 days out, evergreen): 1300 meme reel (office birthday contribution, Raju pose),
1730 image (Gru's Plan: month end Rs 400, 'bas 1 chai'), 2100 mascot reel (month end ATM receipt + uncle peeche),
1000 mood + 1330 teaser + 2130 question stories. No trend swap (nothing fresh verified).
Run from repo root: python content/scripts/batch_2026-11-26.py [reels|images|stories]"""

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
    "birthday-contribution": ("2026-11-26_1300_birthday-contribution-reel", [
        dict(dur=2.4, tag="OFFICE GROUP PE MSG AAYA", head="'BIRTHDAY HAI, SAB 200 BHEJO'", level=0.5, mood="tired", sfx="ding"),
        dict(dur=2.9, tag="IS SAAL KA HISAAB:", box="11 birthday, 3 farewell\n2 shaadi, 1 promotion\nTotal: Rs 3,400", level=0.3,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="PHIR MERA BIRTHDAY AAYA:", draw=reel_template("raju-waiting-pose"), sfx="tick"),
        dict(dur=3.8, head="MERA BIRTHDAY", box="Group pe 4 'HBD'\n1 thumbs up\nCake? 'Bro next week\nsaath mein kar lenge'",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
3,400 diye, badle mein 4 'HBD' mile, wo bhi spelling galat 🙂
office memes aur corporate memes for every thaka hua desi jo har mahine 'contribution' bhejta hai

Send karo us colleague ko jo har birthday pe paise collect karta hai par apna birthday bhool jaata hai 👇

#thakahuadesi #officememes #corporatememes #desimemes #relatablememes
"""),
    "atm-receipt": ("2026-11-26_2100_atm-receipt-reel", [
        dict(dur=2.3, tag="MAHINE KI 26 TAAREEKH", head="ATM GAYA, BALANCE CHECK", level=0.3, mood="tired", sfx="ding"),
        dict(dur=2.6, tag="SCREEN PE:", head="Rs 312", level=0.1, mood="dead", sfx="pop"),
        dict(dur=2.5, tag="PEECHE LINE MEIN:", box="Uncle jhaank rahe the\nMaine bola: 'card ka\nchip kharab hai shayad'", level=0.1,
             mood="tired", sfx="tick"),
        dict(dur=3.8, head="BAAHAR NIKLA", box="Receipt wahin chhod di\nUncle ne utha ke padhi\n'Beta, 100 chahiye?'",
             level=0.0, mood="dead", sfx="trombone", shake=True),
    ], """
Balance 3 digit ka tha, izzat usse bhi kam bachi 🙂
salary memes aur middle class memes for every thaka hua desi jo month end pe ATM sirf balance dekhne jaata hai

Send karo us dost ko jiska account bhi abhi 1 taareekh ka wait kar raha hai 👇

#thakahuadesi #salarymemes #middleclassmemes #desimemes #relatablememes
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
    img = template_meme("gru-plan",
                        "Mahine ka end, account mein Rs 400, salary 1 taareekh ko. Mera plan:",
                        labels=["Rs 400 bache", "Ghar pe Maggi, zero kharcha", "Dost: 'neeche aa, bas 1 chai'", "Bill Rs 1,150"])
    out("2026-11-26_1730_bas-ek-chai", "image", [img], """
Plan Maggi ka tha, dost 'bas ek chai' bolke pura budget pee gaya 🙂
salary memes aur desi memes for every thaka hua desi jiska month end bhi dosto ki wajah se jaldi aata hai

Send karo us dost ko jiski 'bas ek chai' kabhi ek nahi hoti 👇

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
    story("2026-11-26_1000_mood-story", mood_story("Guruvaar ki subah", "kal Friday hai\npar aaj khatam\nnahi ho raha\nchai: 2\nenergy: 20%", 0.2, "tired"))
    story("2026-11-26_1330_teaser-story", teaser_story("Office birthday ka sach", "naya reel feed pe. bhejo us colleague ko jo har mahine 200 maangta hai",
          Q / "2026-11-26_1300_birthday-contribution-reel" / "cover.png"))
    story("2026-11-26_2130_question-story", question_story("Sach batao", "Month end pe account mein kitna bacha hai? 3 digit wale haath upar"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
