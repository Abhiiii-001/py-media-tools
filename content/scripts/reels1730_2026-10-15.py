"""Extra 1730 reels for 15-17 Oct 2026 (2 reels/day mix). Run from repo root:
python content/scripts/reels1730_2026-10-15.py [slug]"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from memes import reel_template  # noqa: E402
from reel import render_reel  # noqa: E402

Q = ROOT / "content" / "queue"

REELS = {
    "sale-cart": ("2026-10-15_1730_sale-cart-reel", [
        dict(dur=2.6, tag="FESTIVE SALE CHALU", head="70% OFF. NO COST EMI.", level=1.0, mood="happy", sfx="ding"),
        dict(dur=2.2, tag="MERA CART", head="14 ITEMS. ₹38,499", level=0.8, mood="happy", sfx="pop"),
        dict(dur=2.6, tag="BANK BALANCE: ₹1,240", draw=reel_template("hera-pheri-trio-shock"), sfx="tick"),
        dict(dur=3.8, head="REMOVE. REMOVE. REMOVE.", box="cart mein bacha: 1 phone cover. wo bhi 'save for later'",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Sale 70% off thi, main 100% broke tha 🙂
sale memes, salary memes aur desi memes for every cart-only shopper

Send karo us dost ko jiska cart uski salary se mehenga hai 👇

#thakahuadesi #salememes #salarymemes #desimemes #middleclassmemes
"""),
    "papa-phone": ("2026-10-16_1730_papa-phone-reel", [
        dict(dur=2.6, tag="PAPA KA CALL", head="'BETA EK MINUTE, PHONE MEIN KUCH HO GAYA'", level=0.8, mood="happy", sfx="ding"),
        dict(dur=2.4, box="Phone khola: storage full, 47 updates pending, 3,000 good morning photos", level=0.5,
             mood="tired", sfx="pop"),
        dict(dur=2.4, tag="GHAR KA IT DEPARTMENT", draw=reel_template("this-is-fine"), sfx="tick"),
        dict(dur=4.0, head="SAB THEEK KAR DIYA", box="Papa: 'kuch delete toh nahi kiya na?'",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
1 minute bola tha, 1 ghanta laga, thank you bhi nahi mila 🙂
indian parents memes, desi ghar ka free tech support

Send karo us dost ko jo apne ghar ka IT department hai 👇

#thakahuadesi #indianparents #desimemes #relatablememes #desifamily
"""),
    "raat-2-baje": ("2026-10-17_1730_raat-2-baje-reel", [
        dict(dur=2.4, tag="RAAT 2:47 AM", head="BAS NEEND AANE HI WALI THI", level=0.4, mood="happy", sfx="pop"),
        dict(dur=2.6, box="Dimaag: 'yaad hai 2014 mein teacher ko \"you too\" bola tha?'", level=0.3,
             mood="tired", sfx="ding"),
        dict(dur=3.0, tag="DIMAAG KA PLAN", draw=reel_template("jethalal-thinking",
             ["sab ne suna tha", "teacher ko yaad hoga", "group mein meme bana", "life khatam"]), sfx="tick"),
        dict(dur=3.8, head="5:10 AM", box="alarm 7 ka hai. dimaag: 'ab so ja, kal important din hai'",
             level=0.03, mood="dead", sfx="trombone", shake=True),
    ], """
Dimaag ko bhi raat ko hi sab yaad aata hai 🙂
overthinking memes, desi memes for 2 AM wale log

Send karo us dost ko jo abhi bhi jaag raha hai 👇

#thakahuadesi #overthinking #desimemes #relatablememes #2ammemes
"""),
}

if __name__ == "__main__":
    for slug in sys.argv[1:] or REELS:
        folder, beats, cap = REELS[slug]
        render_reel(beats, Q / folder, cap)
