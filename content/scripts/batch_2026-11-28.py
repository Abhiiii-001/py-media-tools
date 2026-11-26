"""Batch made 26 Nov 2026 (9 AM run).
Fill Sat 28 Nov (2 days out, evergreen): 1300 meme reel (storage full, Hide the Pain Harold),
1730 image (Monkey Puppet: Mummy 'aaj din bhar kya kiya?'), 2100 mascot reel (free delivery ke liye Rs 50 aur),
1000 mood + 1330 teaser + 2130 question stories. No trend swap.
Run from repo root: python content/scripts/batch_2026-11-28.py [reels|images|stories]"""

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
    "storage-full": ("2026-11-28_1300_storage-full-reel", [
        dict(dur=2.4, tag="PHONE KA NOTIFICATION", head="'STORAGE ALMOST FULL'", level=0.5, mood="tired", sfx="ding"),
        dict(dur=2.9, tag="SATURDAY, DELETE KARNE BAITHA:", box="6,212 photos\n3,400 screenshots\n2 GB 'Good Morning'\n(family group se)", level=0.4,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="HAR PHOTO PE: 'YE TOH ZAROORI HAI'", draw=reel_template("hide-the-pain"), sfx="tick"),
        dict(dur=3.8, head="1 GHANTE BAAD", box="Delete kiya: 1 blurry photo\nKharid liya: 100 GB,\nRs 130/month\nEMI list mein ek aur",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Delete karne baitha tha, subscription le ke utha 🙂
desi memes aur relatable memes for every thaka hua desi jiska phone 3,400 screenshots ka godown hai

Send karo us dost ko jiska phone bhi roz 'storage full' bolta hai 👇

#thakahuadesi #desimemes #relatablememes #indianmemes #adultingmemes
"""),
    "free-delivery": ("2026-11-28_2100_free-delivery-reel", [
        dict(dur=2.3, tag="SATURDAY RAAT, BHOOKH LAGI", head="CART: Rs 149", level=0.4, mood="tired", sfx="ding"),
        dict(dur=2.6, tag="APP NE BOLA:", head="'Rs 50 AUR, FREE DELIVERY!'", level=0.4, mood="tired", sfx="pop"),
        dict(dur=2.6, tag="TOH SMARTLY ADD KIYA:", box="1 coke Rs 60\n1 brownie Rs 99\n'bachat ho gayi'", level=0.2,
             mood="tired", sfx="tick"),
        dict(dur=3.8, head="HISAAB", box="Delivery bachayi: Rs 35\nExtra uda diye: Rs 159\nAur proud bhi hu",
             level=0.0, mood="dead", sfx="trombone", shake=True),
    ], """
Rs 35 bachane ke liye Rs 159 uda diye, finance minister banna chahiye mujhe 🙂
middle class memes aur desi memes for every thaka hua desi jo free delivery ke liye kuch bhi add kar deta hai

Send karo us dost ko jo 'bas 50 aur' pe brownie add karta hai 👇

#thakahuadesi #middleclassmemes #desimemes #relatablememes #indianmemes
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
    img = template_meme("monkey-puppet", "Saturday shaam, Mummy: 'Aaj din bhar kya kiya?'",
                        footer="Main, jo 2 baje utha aur 4 baje phir so gaya")
    out("2026-11-28_1730_din-bhar-kya-kiya", "image", [img], """
Kiya toh bahut kuch, bas sab bistar pe hi hua 🙂
weekend memes aur indian mom memes for every thaka hua desi jiska Saturday 2 jhapkiyon mein khatam ho gaya

Send karo us dost ko jo Saturday ko bhi 'busy' hota hai, so ke 👇

#thakahuadesi #weekendmemes #indianmommemes #desimemes #relatablememes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-11-28_1000_mood-story", mood_story("Shanivaar ki subah", "aaj ka plan: kuch nahi\nprogress: 100%\nchai: 2\nenergy: 50%\n(Monday tak bachake)", 0.5, "tired"))
    story("2026-11-28_1330_teaser-story", teaser_story("'Storage almost full'", "naya reel feed pe. bhejo us dost ko jiska phone screenshots ka godown hai",
          Q / "2026-11-28_1300_storage-full-reel" / "cover.png"))
    story("2026-11-28_2130_question-story", question_story("Sach bolo",
          "Free delivery ke chakkar mein\nkabhi kitna extra uda diya?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
