"""Batch: 18 Nov 2026 (Wednesday, 2 days out, evergreen):
1300 reel (you're on mute), 1730 image (Woman Yelling At Cat, Mummy vs raat ka phone),
2100 reel (WiFi gaya 10 min) + 3 stories.
Run from repo root: python content/scripts/batch_2026-11-18.py [reels|images|stories]"""


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
    "on-mute": ("2026-11-18_1300_on-mute-reel", [
        dict(dur=2.4, tag="20 MINUTE KA PITCH KE BAAD", head="MANAGER: 'YOU'RE ON MUTE'", level=0.6, mood="tired", sfx="ding"),
        dict(dur=2.8, tag="US 20 MINUTE MEIN MAINE", box="Slides share kiye\nJoke bhi maara\nNumbers samjhaye\nSab chup, socha impress hai", level=0.35,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="POORI TEAM KE SAAMNE", draw=reel_template("gajab-bezzati"), sfx="tick"),
        dict(dur=3.8, head="UNMUTE KIYA", box="Dobara shuru kiya\nAadha bhool gaya\nManager: 'mail kar do'\nMail: 2 line ka",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
20 minute bola, suna sirf mere mic ne 🙂
office memes aur wfh memes for every thaka hua desi jiska best idea hamesha mute pe nikalta hai

Send karo us colleague ko jo har call mein 'you're on mute' sunta hai 👇

#thakahuadesi #officememes #desimemes #wfhmemes #corporatememes
"""),
    "wifi-gaya": ("2026-11-18_2100_wifi-gaya-reel", [
        dict(dur=2.4, tag="RAAT 9 BAJE", head="GHAR KA WIFI GAYA: 'BAS 10 MIN'", level=0.5, mood="tired", sfx="ding"),
        dict(dur=2.8, tag="MAJBOORI MEIN", box="Router 4 baar restart\nHall mein aake baitha\nFamily se baat ki\nPata chala sofa naya hai", level=0.3,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="GHARWALE, MUJHE HALL MEIN DEKH KE", draw=reel_template("hera-pheri-trio-shock"), sfx="tick"),
        dict(dur=3.8, head="10:40, WIFI WAPAS", box="Sab apne kamre mein\nBaat wahi ruk gayi\nMummy ka WhatsApp:\n'so ja ab'",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
WiFi 1 ghanta gaya, family se 1 saal ki baatein ho gayi 🙂
desi memes aur family memes for every thaka hua desi jo ghar mein rehke bhi WhatsApp pe milta hai

Send karo us bhai/behen ko jo saamne wale kamre se message karta hai 👇

#thakahuadesi #desimemes #familymemes #relatablememes #indianmemes
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
                        "Raat 11:45, Mummy vs Main:",
                        ["'Phone rakh de,\naankhein kharab\nho jaayengi!'", "'Aapka Good Night\nforward abhi\naaya hai'"],
                        footer="Family group ki night shift: Mummy")
    out("2026-11-18_1730_raat-ka-phone", "image", [img], """
Mujhe 11 baje phone band karne bola, khud 11:45 pe 'Good night' bhej rahi hai 🙂
indian mom memes aur desi memes for every thaka hua desi jiski mummy family group ki night shift pe hai

Send karo us bhai/behen ko jiski mummy sabse late online hoti hai 👇

#thakahuadesi #desimemes #indianmoms #momsmemes #relatablememes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-11-18_1000_mood-story", mood_story("Budhvaar ki subah", "aadha hafta gaya, kaam wahi\nchai: teesri\nenergy: 20%", 0.2, "tired"))
    story("2026-11-18_1330_teaser-story", teaser_story("'You're on mute'", "naya reel feed pe. bhejo us colleague ko jo mute pe pitch deta hai",
          Q / "2026-11-18_1300_on-mute-reel" / "cover.png"))
    story("2026-11-18_2130_question-story", question_story("Sach batao", "WiFi jaaye toh ghar mein sabse pehle kaun hall mein aata hai?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
