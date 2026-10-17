"""Batch: 19 Oct 2026 (Monday, evergreen): 1300 reel, 1730 carousel, 2100 reel + 3 stories.
Run from repo root: python content/scripts/batch_2026-10-17.py [reels|images|stories]"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from brand import *  # noqa: E402,F403
from memes import reel_template  # noqa: E402
from reel import render_reel  # noqa: E402
from stories import mood_story, question_story, teaser_story  # noqa: E402

Q = ROOT / "content" / "queue"

REELS = {
    "delivery": ("2026-10-19_1300_delivery-wait-reel", [
        dict(dur=2.4, tag="8:00 AM KA SMS", head="AAPKA ORDER AAJ AAYEGA", level=0.9, mood="happy", sfx="ding"),
        dict(dur=2.6, tag="PURA DIN", box="Ghar se nikla nahi. Nahaya nahi. Bathroom bhi 30 second mein.\nBell baji? Nahi, padosi ka tha",
             level=0.5, mood="tired", sfx="pop"),
        dict(dur=2.6, tag="SHAAM 6 BAJE", draw=reel_template("ab-tak-aa-jana-chahiye"), sfx="tick"),
        dict(dur=3.8, head="9:02 PM", box="'Delivery attempted. Customer not available.'\nMain: 13 ghante se gate pe baitha tha",
             level=0.03, mood="dead", sfx="trombone", shake=True),
    ], """
13 ghante gate pe baitha, phir bhi 'customer not available' 🙂
online shopping memes aur desi memes for everyone jo aaj bhi delivery ka wait kar raha hai

Send karo us dost ko jiska order bhi 'out for delivery' hi reh gaya 👇

#thakahuadesi #onlineshopping #desimemes #relatablememes #indianmemes
"""),
    "mummy-phone": ("2026-10-19_2100_mummy-phone-reel", [
        dict(dur=2.4, tag="MUMMY, 9 PM", head="PHONE RAKH DE. AANKHEIN KHARAB HO JAYENGI", level=0.7, mood="tired", sfx="ding"),
        dict(dur=2.4, tag="11:40 PM", box="Main paani peene utha.\nMummy ke room se phone ki light aa rahi thi", level=0.5,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="DARWAZE SE DEKHA", draw=reel_template("jethalal-peeking"), sfx="tick"),
        dict(dur=3.8, head="MUMMY:", box="'bas ek recipe dekh rahi thi'\n(reel no. 147, aur family group pe 23 forward)",
             level=0.1, mood="dead", sfx="trombone", shake=True),
    ], """
Rule sirf bachchon ke liye tha 🙂
indian mom memes, desi ghar ka raat 11 baje ka sach

Send karo apne bhai/behen ko, unki mummy bhi same hai 👇

#thakahuadesi #indianmom #desifamily #desimemes #relatablememes
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
    text_block(img, headline, (80, 200, 920, 230), size=130)
    panel(img, (90, 450, 900, 300))
    text_block(img, body, (130, 470, 820, 260), path=FONT_BODY, size=60, fill=BLACK, stroke=None)
    mascot(img, W // 2, 820, scale=1.05, level=level, mood=mood)
    watermark(img, page)
    return img


def cta_slide(line, sub, page):
    img = sunburst(BLACK, "#222222")
    text_block(img, line, (90, 180, 900, 620), size=120, fill=YELLOW)
    mascot(img, W // 2, 820, scale=0.95, level=0.5, mood="tired")
    text_block(img, sub, (90, 1180, 900, 80), path=FONT_BODY, size=44)
    watermark(img, page)
    return img


def images():
    c = []
    img = sunburst()
    label(img, "HAR HAFTE. SAME KAHANI.", (W // 2, 110))
    text_block(img, "MONDAY KE 5 STAGES", (80, 220, 920, 380), size=170)
    mascot(img, W // 2, 650, scale=1.35, level=0.5)
    text_block(img, "chai level dekhte jao", (120, 1150, 840, 90), path=FONT_BODY, size=56, fill=WHITE)
    watermark(img, "1/7")
    c.append(img)
    c.append(stage_slide("7:00 AM", "'BAS 5 MIN AUR'", "6 alarm, 6 baar '5 min aur'. aankh khuli toh 8:52 tha", 0.9, "happy", "2/7"))
    c.append(stage_slide("9:45 AM", "47 UNREAD MAIL", "laptop khola, mail dekhe, laptop band kiya. pehle chai", 0.7, "tired", "3/7"))
    c.append(stage_slide("11:00 AM", "1 GHANTE KI MEETING", "summary: 'iske liye ek aur meeting rakhte hai'", 0.45, "tired", "4/7"))
    c.append(stage_slide("3:30 PM", "GHADI DEKHI", "3:34. 20 min baad phir dekhi. 3:36. ghadi bhi Monday mana rahi hai", 0.2, "tired", "5/7"))
    c.append(stage_slide("10 PM", "EK DIN GAYA", "ab sirf 4 din aur. haan, ye khushi ki baat hai", 0.03, "dead", "6/7"))
    c.append(cta_slide("SEND KARO US DOST KO JISKA MONDAY ABHI BHI 3:34 PE ATKA HAI",
                       "Friday tak saath nibhayenge", "7/7"))
    out("2026-10-19_1730_monday-stages", "carousel", c, """
Monday ne phir se haath pakad ke bitha diya 🙂
monday memes aur office memes, har hafte ki same kahani

Send karo us colleague ko jo abhi bhi ghadi dekh raha hai 👇

#thakahuadesi #mondaymemes #officememes #corporatememes #desimemes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-10-19_1000_mood-story", mood_story("Monday hai", "alarm: 6\nchai: 2\nmotivation: loading...", 0.3, "tired"))
    story("2026-10-19_1330_teaser-story", teaser_story("'Customer not available'", "naya reel feed pe. bhejo us dost ko jo aaj bhi delivery ka wait kar raha hai",
          Q / "2026-10-19_1300_delivery-wait-reel" / "cover.png"))
    story("2026-10-19_2130_question-story", question_story("Monday khatam", "Aaj ka Monday 1 se 10 mein kitna bekaar tha?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
