"""Batch: 7 Nov 2026 (Saturday, evergreen): 1300 + 2100 reels, 1730 image + 3 stories.
Run from repo root: python content/scripts/batch_2026-11-05.py [reels|images|stories]"""

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
    "patla-mota": ("2026-11-07_1300_patla-mota-reel", [
        dict(dur=2.4, tag="GHAR PAHUNCHTE HI", head="MUMMY: 'KITNA PATLA HO GAYA, KHAATA NAHI KYA?'", level=0.6, mood="happy", sfx="ding"),
        dict(dur=2.6, tag="AGLE 2 DIN", box="4 paratha\n2 katori kheer\n'aur le na'\n'bas ek aur'", level=0.8,
             mood="happy", sfx="pop"),
        dict(dur=2.6, tag="PAPA, TEESRE DIN", draw=reel_template("uday-shetty-majnu"), sfx="tick"),
        dict(dur=3.8, head="'ITNA MOTA KAISE HO GAYA?'", box="Same beta.\nSame hafta.\nBeech mein bas mummy\nke parathe aaye the",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Ghar pe 2 din mein patla se mota, koi gym itna fast nahi 🙂
desi memes aur indian parents memes for every thaka hua desi jo chutti pe ghar gaya hai

Send karo us dost ko jo ghar se 3 kilo extra leke lautta hai 👇

#thakahuadesi #desimemes #indianparents #relatablememes #desimom
"""),
    "mummy-free-ho": ("2026-11-07_2100_mummy-free-ho-reel", [
        dict(dur=2.4, tag="MUMMY KA MESSAGE, 4:12 PM", head="'FREE HO TOH CALL KARNA, EK BAAT BATANI HAI'", level=0.5, mood="tired", sfx="ding"),
        dict(dur=2.2, tag="DIMAAG, AGLE 10 SECOND", box="Sab theek hai na?\nKisi ne kuch bola?\nMaine kya kiya ab?", level=0.3,
             mood="tired", sfx="pop"),
        dict(dur=3.0, tag="DIMAAG KA FULL PLAN", draw=reel_template("jethalal-thinking",
             ["koi bimaar?", "paise chahiye?", "rishta aaya?", "result aaya?"]), sfx="tick"),
        dict(dur=3.8, head="CALL PE MUMMY:", box="'Wo Netflix ka password\nkya tha? TV maang\nraha hai'",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
'Ek baat batani hai' sunke dil 4 baar ruka, baat sirf password ki thi 🙂
desi memes aur indian mom memes for every thaka hua desi jo mummy ka ek message padhke hi overthinking mein chala jaata hai

Send karo us dost ko jo ghar ka permanent IT support hai 👇

#thakahuadesi #desimemes #indianmom #overthinking #relatablememes
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
    img = template_meme("chatur-speech",
                        "LinkedIn pe main:\n'Thrilled to share,\nnew role started!'",
                        footer="Asli mein: same kaam, naya Excel")
    out("2026-11-07_1730_linkedin-thrilled", "image", [img], """
LinkedIn pe thrilled, office mein thaka hua 🙂
office memes aur corporate memes for every thaka hua desi jiski 'new role' sirf designation mein hai

Send karo us colleague ko jo har chhoti cheez LinkedIn pe daalta hai 👇

#thakahuadesi #officememes #corporatememes #linkedinmemes #desimemes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-11-07_1000_mood-story", mood_story("Saturday hai", "neend: abhi bhi kam\nmummy ka khaana: full\nenergy: 60%", 0.6, "happy"))
    story("2026-11-07_1330_teaser-story", teaser_story("Patla ya mota?", "naya reel feed pe. bhejo us dost ko jo ghar se 3 kilo extra laata hai",
          Q / "2026-11-07_1300_patla-mota-reel" / "cover.png"))
    story("2026-11-07_2130_question-story", question_story("Sach batao", "Mummy ka sabse darawna message kya hota hai?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
