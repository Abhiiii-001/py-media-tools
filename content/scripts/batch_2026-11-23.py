"""Batch made 21 Nov 2026 (9 AM run).
Fill Mon 23 Nov (2 days out, evergreen): 1300 meme reel (Mummy ka video call, Maggi, monkey puppet),
1730 image (Waiting Skeleton: Monday 10:05 AM waiting for Friday), 2100 mascot reel (Monday 147 unread mails),
1000 mood + 1330 teaser + 2130 question stories. No trend swap (nothing fresh verified).
Run from repo root: python content/scripts/batch_2026-11-23.py [reels|images|stories]"""

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
    "mummy-video-call": ("2026-11-23_1300_mummy-video-call-reel", [
        dict(dur=2.4, tag="RAAT 9 BAJE", head="MUMMY KA VIDEO CALL", level=0.5, mood="tired", sfx="ding"),
        dict(dur=2.9, tag="MUMMY:", box="'Khaana khaya?'\nMaggi dikhayi\n'YE KHAANA HAI??'\n'Ghar kab aa raha hai?'", level=0.3,
             mood="tired", sfx="pop"),
        dict(dur=2.5, tag="MAIN, CAMERA SE NAZAR CHURATE HUE:", draw=reel_template("monkey-puppet"), sfx="tick"),
        dict(dur=3.8, head="CALL KATNE KE 2 MIN BAAD", box="Papa ka msg: 'Mummy bol rahi\nhai tu patla ho gaya'\nMasi ko bhi pata chal gaya\nMaggi thandi ho gayi",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
Ek Maggi dikhayi thi, ab poore khaandan ko pata hai main patla ho gaya 🙂
indian mom memes aur desi memes for every thaka hua desi jo ghar se door PG/hostel mein Maggi pe zinda hai

Send karo us roommate ko jo mummy ke call pe hi sabzi banane ki acting karta hai 👇

#thakahuadesi #indianmommemes #desimemes #hostellife #relatablememes
"""),
    "147-unread": ("2026-11-23_2100_147-unread-reel", [
        dict(dur=2.3, tag="MONDAY, 10:02 AM", head="LAPTOP KHOLA...", level=0.5, mood="tired", sfx="ding"),
        dict(dur=2.9, tag="INBOX:", box="147 unread\n23 'gentle reminder'\n1 'URGENT', Friday 6:58 PM ka\n'Hope you had a great weekend'",
             level=0.3, mood="tired", sfx="pop"),
        dict(dur=2.3, tag="MERA PLAN:", box="Ek ek karke padhunga\nSab reply karunga\nAaj inbox zero", level=0.6, mood="happy", sfx="tick"),
        dict(dur=3.8, head="10:04 AM", box="Select all\nMark as read\nChai pe chala gaya\n'Mail nahi aaya, spam mein hoga'",
             level=0.05, mood="dead", sfx="trombone", shake=True),
    ], """
147 unread the, 2 second mein zero ho gaye. Productivity 🙂
office memes aur monday memes for every thaka hua desi jiska inbox zero sirf 'mark as read' se hota hai

Send karo us colleague ko jo har mail pe 'spam mein chala gaya hoga' bolta hai 👇

#thakahuadesi #officememes #mondaymemes #desimemes #corporatememes
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
    img = template_meme("waiting-skeleton",
                        "Main, Monday 10:05 AM se Friday 6 baje ka wait karte hue",
                        footer="Abhi sirf 4 din 7 ghante 55 minute baaki")
    out("2026-11-23_1730_friday-ka-wait", "image", [img], """
Monday shuru hue 5 minute hue the, Friday ka countdown chalu ho gaya 🙂
monday memes aur office memes for every thaka hua desi jo har Monday subah Friday gin raha hai

Send karo us colleague ko jo Monday 10 baje hi 'Friday kab aayega' bolta hai 👇

#thakahuadesi #mondaymemes #officememes #desimemes #relatablememes
""")


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


def stories():
    story("2026-11-23_1000_mood-story", mood_story("Somvaar ki subah", "alarm: 5 baar\nchai: abhi tak 0\nweekend: kab khatam hua??\nenergy: 15%", 0.15, "dead"))
    story("2026-11-23_1330_teaser-story", teaser_story("'Ye khaana hai??'", "naya reel feed pe. bhejo us dost ko jo PG mein Maggi pe zinda hai",
          Q / "2026-11-23_1300_mummy-video-call-reel" / "cover.png"))
    story("2026-11-23_2130_question-story", question_story("Sach batao", "Monday subah kitne unread mail the? Aur padhe kitne?"))


if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "images", "stories"]
    if "reels" in what:
        for folder, beats, cap in REELS.values():
            render_reel(beats, Q / folder, cap)
    if "images" in what:
        images()
    if "stories" in what:
        stories()
