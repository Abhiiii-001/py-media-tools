"""Batch made 17 Nov 2026 (9 AM run).
Swap for Wed 18 Nov: 2100 reel 'test-3-30' (IND vs NZ 1st Test starts 19 Nov 3:30 AM IST) + 2130 question story.
Fill Thu 19 Nov (2 days out, evergreen): 1300 reel (mummy 'wahin rakha hai'), 1730 image (Expanding Brain,
month-end dinner), 2100 reel (office lunch kahan?) + 3 stories.
Run from repo root: python content/scripts/batch_2026-11-19.py [reels|images|stories]"""



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
    "test-3-30": ("2026-11-18_2100_test-3-30-reel", [
        dict(dur=2.4, tag="KAL SUBAH 3:30 BAJE TEST MATCH", head="MAIN: 'POORA DEKHUNGA'", level=0.7, mood="happy", sfx="ding"),
        dict(dur=2.8, tag="PLAN BILKUL READY", box="3:15 ka alarm laga diya\nChai ka saamaan ready\nOffice 10 baje, no tension\nBas reels dekh ke sota hu", level=0.5,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="RAAT 1 BAJE: 'SOYUNGA HI NAHI, SIMPLE'", draw=reel_template("roll-safe"), sfx="tick"),
        dict(dur=3.8, head="3:40 AM", box="Toss dekha\nPehli ball pe 'bas 2 min'\nUtha 10:20, office late\nScore WhatsApp se pata chala",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Match 3:30 baje tha, meri neend 3:31 pe aa gayi 🙂
cricket memes aur desi memes for every thaka hua desi jo har Test ke liye alarm lagata hai

Send karo us dost ko jo bolta hai 'main toh poora dekhunga' 👇

#thakahuadesi #cricketmemes #desimemes #indvsnz #relatablememes
"""),
    "wahin-rakha-hai": ("2026-11-19_1300_wahin-rakha-hai-reel", [
        dict(dur=2.4, tag="MUMMY, KITCHEN SE:", head="'FRIDGE MEIN DEKH, WAHIN RAKHA HAI'", level=0.5, mood="tired", sfx="ding"),
        dict(dur=2.8, tag="MAINE 5 MINUTE TAK", box="Fridge 3 baar khola\nPeeche, upar, neeche dekha\nSabzi hata ke bhi dekha\nNahi hai, pakka nahi hai", level=0.3,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="MAIN: 'MUMMY NAHI HAI'. MUMMY, AATE HUE:", draw=reel_template("3idiots-old-man"), sfx="tick"),
        dict(dur=3.8, head="1 SECOND MEIN NIKAL DIYA", box="Saamne hi rakha tha\n'Aankhein hai ya button?'\n'Maine dhoondh liya na toh...'\nWo line aaj bhi poori nahi hui",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
5 minute maine dhoondha, 1 second mein Mummy ne, aur taana 1 hafta chalega 🙂
indian mom memes aur desi memes for every thaka hua desi jise fridge mein kabhi kuch nahi milta

Send karo us bhai/behen ko jo 'nahi hai' bolke daant khaata hai 👇

#thakahuadesi #desimemes #indianmoms #momsmemes #relatablememes
"""),
    "lunch-kahan": ("2026-11-19_2100_lunch-kahan-reel", [
        dict(dur=2.4, tag="1 BAJE, OFFICE GROUP:", head="'AAJ LUNCH KAHAN?'", level=0.5, mood="tired", sfx="ding"),
        dict(dur=2.8, tag="40 MINUTE KI CHARCHA", box="Ek: 'Chinese chalega'\nDusra: 'main diet pe hu'\nTeesra: 'kuch bhi chalega'\nPar 'kuch bhi' pe sab ka veto", level=0.3,
             mood="tired", sfx="pop"),
        dict(dur=2.6, tag="1:40 PM, LUNCH COMMITTEE KI MEETING", draw=reel_template("panchayat-office"), sfx="tick"),
        dict(dur=3.8, head="2:15 PM, FINAL DECISION", box="Wahi canteen\nWahi rajma chawal\nLunch break khatam\nKal phir wahi sawaal",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
40 minute discussion, result wahi rajma chawal 🙂
office memes aur corporate memes for every thaka hua desi jiska lunch group parliament se lamba chalta hai

Send karo apne lunch group ko, aaj bhi decide nahi hoga 👇

#thakahuadesi #officememes #corporatememes #desimemes #officelife
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
    img = template_meme("expanding-brain",
                        "Mahine ke last week ka dinner plan:",
                        labels=["Swiggy pe\norder", "Ghar pe\ndal chawal", "Maggi,\naadha\npacket",
                                "'Aaj\nbhook\nnahi\nhai'"],
                        footer="Salary 1 ko aayegi, bhook bhi tab")
    out("2026-11-19_1730_dinner-plan", "image", [img], """
Mahine ke end mein bhook bhi budget dekh ke lagti hai 🙂
salary memes aur desi memes for every thaka hua desi jiska wallet 20 taareekh ko hi so jaata hai

Send karo us roommate ko jo aaj bhi 'bhook nahi hai' bolega 👇

#thakahuadesi #salarymemes #desimemes #adultingmemes #relatablememes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-11-18_2130_question-story", question_story("Sach batao", "Kal 3:30 baje Test ke liye alarm kisne lagaya hai? Aur uthega kaun?"))
    story("2026-11-19_1000_mood-story", mood_story("Guruvaar ki subah", "Friday abhi bhi 1 din door\nchai: chauthi\nenergy: 15%", 0.15, "tired"))
    story("2026-11-19_1330_teaser-story", teaser_story("'Wahin rakha hai'", "naya reel feed pe. bhejo us bhai/behen ko jise fridge mein kuch nahi milta",
          Q / "2026-11-19_1300_wahin-rakha-hai-reel" / "cover.png"))
    story("2026-11-19_2130_question-story", question_story("Sach batao", "Tumhare office mein 'lunch kahan?' decide hone mein kitna time lagta hai?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
