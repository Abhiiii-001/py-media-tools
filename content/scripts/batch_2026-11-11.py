"""Batch: 11 Nov 2026 (Wednesday, 2 days out so evergreen: binge watching, friend group, shaadi shagun): 1300 + 2100 reels, 1730 mascot carousel + 3 stories.
Run from repo root: python content/scripts/batch_2026-11-11.py [reels|images|stories]"""

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
    "bas-ek-episode": ("2026-11-11_1300_bas-ek-episode-reel", [
        dict(dur=2.4, tag="RAAT 11:30 BAJE MAIN", head="'BAS EK EPISODE, PHIR SO JAUNGA'", level=0.7, mood="happy", sfx="ding"),
        dict(dur=2.8, tag="TIMELINE", box="12:15 'ye cliffhanger pe kaun sota hai'\n1:40 'ab 2 hi toh bache hai'\n3:10 'season khatam karke hi'\n4:05 next season ka trailer", level=0.35,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="MAIN, KHUD KO SAMJHATE HUE", draw=reel_template("clown-makeup", ["Bas ek episode", "Kal late uthunga", "Meeting 10 baje hai, chalega", "Camera off rakh dunga"]), sfx="tick"),
        dict(dur=3.8, head="SUBAH 9:58 STANDUP", box="Manager: 'Sab theek?'\nMain: 'Sir kal raat\nnetwork issue tha'\nNetflix: 'Are you still watching?'",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
'Bas ek episode' bola tha, season khatam ho gaya aur neend bhi 🙂
binge watching memes aur office memes for every thaka hua desi jo 4 baje 'kal se jaldi sounga' bolta hai

Send karo us dost ko jo abhi bhi 'bas ek aur' pe atka hai 👇

#thakahuadesi #officememes #netflixmemes #desimemes #relatablememes
"""),
    "shagun-season": ("2026-11-11_2100_shagun-season-reel", [
        dict(dur=2.4, tag="SHAADI SEASON SHURU", head="IS MAHINE 6 SHAADI KE CARD AAYE", level=0.7, mood="happy", sfx="ding"),
        dict(dur=2.8, tag="HISAAB", box="Shagun: 6 x Rs 1,100\nNaya kurta: 'ek hi lunga'\nCab: Rs 900 har baar\nSalary: wahi purani", level=0.35,
             mood="tired", sfx="pop"),
        dict(dur=2.4, tag="MAIN, POORA HISAAB DEKH KE", draw=reel_template("hera-pheri-trio-shock"), sfx="tick"),
        dict(dur=3.8, head="NAYA PLAN", box="Lifafe mein 1,100\nKhana khaunga 1,800 ka\nMeri life ka ekmatra\nprofitable investment",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Shaadi unki, EMI meri 🙂
shaadi season memes aur salary memes for every thaka hua desi jiska shagun budget salary se pehle khatam ho gaya

Send karo us dost ko jo har shaadi mein bas khaane ke liye jaata hai 👇

#thakahuadesi #shaadiseason #salarymemes #desimemes #relatablememes
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


def stage_slide(tag, headline, body, level, mood="tired", page=None):
    img = sunburst()
    label(img, tag, (W // 2, 90))
    text_block(img, headline, (80, 200, 920, 230), size=120)
    panel(img, (90, 450, 900, 300))
    text_block(img, body, (130, 470, 820, 260), path=FONT_BODY, size=58, fill=BLACK, stroke=None)
    mascot(img, W // 2, 820, scale=1.05, level=level, mood=mood)
    watermark(img, page)
    return img


def images():
    c = []
    img = sunburst()
    text_block(img, "HAR FRIEND GROUP MEIN YE 5 LOG HOTE HI HAI", (80, 160, 920, 420), size=120)
    mascot(img, W // 2, 640, scale=1.3, level=0.5, mood="tired")
    text_block(img, "tum kaunse ho? swipe karo", (120, 1160, 840, 90), path=FONT_BODY, size=54)
    watermark(img, "1/7")
    c.append(img)
    c.append(stage_slide("NO. 1", "PLAN MASTER", "Har hafte 'is baar pakka trip'\nbooking ke din:\n'yaar mera nahi ho payega'", 0.7, "happy", "2/7"))
    c.append(stage_slide("NO. 2", "BILL AATE HI GAAYAB", "Khana khatam, bill aaya\naur bhai ko achanak\n'ek zaroori call' aa gaya", 0.5, "tired", "3/7"))
    c.append(stage_slide("NO. 3", "PHOTO INSPECTOR", "40 photo li\n39 mein uski aankh band\n'ek aur le na bhai'", 0.45, "tired", "4/7"))
    c.append(stage_slide("NO. 4", "2 AM PHILOSOPHER", "Raat 2 baje: 'jaag rahe ho?'\nphir 3 page ka\nlife ka gyaan", 0.3, "tired", "5/7"))
    c.append(stage_slide("NO. 5", "SEEN ZONE KING", "Group mein 200 message\nreply sirf 'haha'\nwo bhi 3 din baad", 0.15, "dead", "6/7"))
    img = sunburst(BLACK, "#222222")
    text_block(img, "GROUP MEIN BHEJO AUR DEKHO KAUN SABSE PEHLE CHIDHTA HAI", (90, 160, 900, 620), size=104, fill=YELLOW)
    mascot(img, W // 2, 820, scale=0.95, level=0.5, mood="tired")
    text_block(img, "wahi no. 2 hai", (90, 1180, 900, 80), path=FONT_BODY, size=48)
    watermark(img, "7/7")
    c.append(img)
    out("2026-11-11_1730_friend-group-5-log", "carousel", c, """
Har group mein ek no. 2 hota hai, aur wo ye post kabhi share nahi karega 🙂
dosti memes aur desi memes for every thaka hua desi ka friend group

Friend group mein bhejo aur number assign karo 👇

#thakahuadesi #dostimemes #friendsmemes #desimemes #relatablememes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-11-11_1000_mood-story", mood_story("Budhwar ki subah", "hafta: aadha gaya\nbaaki: abhi bhi 2.5 din\nenergy: 25%", 0.25, "tired"))
    story("2026-11-11_1330_teaser-story", teaser_story("'Bas ek episode'", "naya reel feed pe. bhejo us dost ko jo 4 baje tak Netflix dekhta hai",
          Q / "2026-11-11_1300_bas-ek-episode-reel" / "cover.png"))
    story("2026-11-11_2130_question-story", question_story("Sach batao", "Is shaadi season kitne card aaye, aur shagun ka budget kitna hai?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
