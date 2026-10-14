"""Reels for 15-17 Oct 2026. Run from repo root: python content/scripts/reels_2026-10-15.py [slug]"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from brand import soan_papdi, panel, text_block, label, BLACK, YELLOW  # noqa: E402
from reel import render_reel  # noqa: E402

Q = ROOT / "content" / "queue"


def papdi(img, y):
    return soan_papdi(img, 540, y, 1.25)


def score_card(img, y):
    panel(img, (190, y, 700, 380), fill=YELLOW)
    label(img, "MERA SCORE", (540, y - 30), size=52)
    text_block(img, "4 almari\n2 parde\n0 overs dekhe", (220, y + 50, 640, 300), size=96, fill=BLACK, stroke=None)
    return y + 380


REELS = {
    "diwali-gift": ("2026-10-15_2030_diwali-gift-reel", [
        dict(dur=2.6, tag="HR KA MAIL AAYA", head="'IS DIWALI AAPKE LIYE SPECIAL GIFT'", level=1.0, mood="happy", sfx="ding"),
        dict(dur=2.4, tag="MERA DIMAAG", head="BONUS? iPHONE? 2 DIN EXTRA CHHUTTI?", level=1.0, mood="happy", sfx="pop"),
        dict(dur=1.8, tag="DABBA KHOLA...", head="...", level=0.6, mood="tired", sfx="tick"),
        dict(dur=4.2, head="SOAN PAPDI", box="aur ek 'we are a family' wala card", draw=papdi,
             sfx="trombone", shake=True),
    ], """
Mail padh ke iPhone soch liya tha 🙂
Diwali gift reality check, corporate memes jo dil pe lagte hai

Tag karo us colleague ko jo abhi bhi bonus ka wait kar raha hai 👇

#thakahuadesi #diwalimemes #officememes #corporatememes #desimemes
"""),
    "quick-call": ("2026-10-16_1300_quick-call-reel", [
        dict(dur=2.6, tag="FRIDAY 5:58 PM", head="LAPTOP BAND KARNE HI WALA THA", level=0.9, mood="happy", sfx="pop"),
        dict(dur=2.4, box="Boss: free ho? ek quick 5 min call le lete hai?", level=0.6, mood="tired", sfx="ding"),
        dict(dur=2.2, tag="CALL CHALU", head="5 MIN... 25 MIN... 55 MIN...", level=0.3, mood="tired", sfx="tick"),
        dict(dur=4.0, head="7:38 PM", box="quick call khatam. weekend bhi.", level=0.03, mood="dead",
             sfx="trombone", shake=True),
    ], """
5 min bola tha. 5 min.
office memes for everyone jiska Friday bhi ek 'quick call' ne kha liya

Send karo us dost ko jo abhi isi call pe hai 👇

#thakahuadesi #officememes #corporatememes #fridaymemes #desimemes
"""),
    "match-vs-safai": ("2026-10-17_2030_match-vs-safai-reel", [
        dict(dur=2.6, tag="SATURDAY 7 PM", head="INDIA VS WI. CHIPS READY. REMOTE HAATH MEIN", level=1.0, mood="happy", sfx="pop"),
        dict(dur=2.6, box="Mummy: 'match baad mein, pehle kitchen ki upar wali almari'", level=0.5, mood="tired", sfx="ding"),
        dict(dur=4.0, draw=score_card, level=0.05, mood="dead", sfx="trombone", shake=True),
        dict(dur=1.6, head="DIWALI SAFAI > CRICKET", sfx="pop"),
    ], """
Match ka score pata nahi, almari ka pata hai
cricket memes x diwali safai, desi ghar mein dono saath nahi chalte

Score batao comment mein, main kitchen mein hu 👇

#thakahuadesi #cricketmemes #indvswi #diwalisafai #desimemes
"""),
}

if __name__ == "__main__":
    for slug in sys.argv[1:] or REELS:
        folder, beats, cap = REELS[slug]
        render_reel(beats, Q / folder, cap)
