"""Batch made 18 Nov 2026 (9 AM run).
Fill Fri 20 Nov (2 days out, evergreen): 1300 reel (bank KYC '10 min ka kaam'), 1730 image (They Don't Know,
shaadi season shagun), 2100 reel (Friday night movie selection) + 3 stories. No trend swap (nothing fresh verified).
Run from repo root: python content/scripts/batch_2026-11-20.py [reels|images|stories]"""

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
    "bank-kyc": ("2026-11-20_1300_bank-kyc-reel", [
        dict(dur=2.4, tag="BANK KA SMS: 'KYC UPDATE KARO'", head="'BAS 10 MINUTE KA KAAM HAI'", level=0.6, mood="happy", sfx="ding"),
        dict(dur=2.8, tag="BRANCH PAHUNCHA, HALF DAY LEKE", box="Token 47, chal raha 12\nCounter 3: 'counter 5 jaiye'\nCounter 5: 'lunch ke baad'\nForm mein 4 jagah sign", level=0.3,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="DEKH RAHA HAI BINOD, 10 MIN KA KAAM", draw=reel_template("dekh-raha-hai-binod"), sfx="tick"),
        dict(dur=3.8, head="3:55 PM, MERA NUMBER AAYA", box="'Server down hai'\n'Kal aana, photocopy leke'\nPhotocopy thi, galat wali\nKal phir half day",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
10 minute ka kaam tha, 2 half day kha gaya, aur KYC abhi bhi pending 🙂
desi memes aur adulting memes for every thaka hua desi jo 'bas 10 min' sunke bank gaya tha

Send karo us dost ko jiska KYC 3 baar 'update' ho chuka hai 👇

#thakahuadesi #desimemes #adultingmemes #relatablememes #middleclassmemes
"""),
    "movie-dhoondh": ("2026-11-20_2100_movie-dhoondh-reel", [
        dict(dur=2.4, tag="FRIDAY RAAT 10 BAJE", head="'AAJ KOI ACCHI MOVIE DEKHTE HAI'", level=0.7, mood="happy", sfx="ding"),
        dict(dur=2.8, tag="45 MINUTE KA SELECTION", box="3 app khole\n12 trailer dekhe\n'Ye dekhi hai', 'ye boring'\nRating 7.9? nahi, 8 chahiye", level=0.4,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="11:15 PM: 'BAS YE FINAL, PAKKA'", draw=reel_template("raju-waiting-pose"), sfx="tick"),
        dict(dur=3.8, head="11:22 PM", box="Khana thanda ho gaya\nAankh lag gayi\nUtha toh credits chal rahe\nPhir wahi purana show lagaya",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Movie dhoondhne mein 45 minute, dekhne mein 7 🙂
ott memes aur weekend memes for every thaka hua desi jiska Friday night trailer dekh ke hi khatam hota hai

Send karo us dost ko jo har baar 'tu hi kuch suggest kar' bolta hai 👇

#thakahuadesi #ottmemes #weekendmemes #desimemes #relatablememes
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
    img = template_meme("they-dont-know",
                        "Shaadi mein sab naach rahe hai. Inhe nahi pata shagun ka lifafa maine udhaar leke bhara hai",
                        labels=None,
                        footer="Sab naach rahe hai, balance nahi")
    out("2026-11-20_1730_shagun-udhaar", "image", [img], """
Lifafe mein 2100, account mein 210 🙂
shaadi memes aur salary memes for every thaka hua desi jiska shaadi season EMI pe chal raha hai

Send karo us dost ko jiske is mahine 4 shaadi hai 👇

#thakahuadesi #shaadimemes #salarymemes #desimemes #relatablememes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-11-20_1000_mood-story", mood_story("Shukravaar ki subah", "Friday aa gaya\nbody abhi Wednesday pe hai\nenergy: 40%\nsirf ummeed pe", 0.4, "happy"))
    story("2026-11-20_1330_teaser-story", teaser_story("'Bas 10 min ka kaam'", "naya reel feed pe. bhejo us dost ko jiska KYC abhi bhi pending hai",
          Q / "2026-11-20_1300_bank-kyc-reel" / "cover.png"))
    story("2026-11-20_2130_question-story", question_story("Sach batao", "Movie choose karne mein zyada time lagta hai ya dekhne mein?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
