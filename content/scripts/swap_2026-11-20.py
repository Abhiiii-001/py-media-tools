"""Trend swap made 20 Nov 2026 (4 PM run).
GTA 6 launched in India 19 Nov 2026 (PS5/Xbox, Rs 5,999 standard, ~200GB+, PS5 bundle ~Rs 70k+; verified via 91mobiles/analyticsinsight).
Swaps out tonight's evergreen 2100 `movie-dhoondh` reel + its 2130 question story (moved to content/backlog/).
Run from repo root: python content/scripts/swap_2026-11-20.py"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from memes import reel_template  # noqa: E402
from reel import render_reel  # noqa: E402
from stories import question_story  # noqa: E402

Q = ROOT / "content" / "queue"

BEATS = [
    dict(dur=2.4, tag="GTA 6 AA GAYA", head="BACHPAN SE IS DIN KA WAIT THA", level=0.6, mood="happy", sfx="ding"),
    dict(dur=3.0, tag="HISAAB LAGAYA", box="Game: Rs 5,999\nPS5 bhi lena padega\nTotal: 70 hazaar+\nAccount mein: Rs 4,312", level=0.2,
         mood="tired", sfx="pop"),
    dict(dur=2.6, tag="EMI CALCULATOR KHOLA:", draw=reel_template("hera-pheri-trio-shock"), sfx="tick"),
    dict(dur=3.8, head="FINAL PLAN", box="200 GB ka game\nPhone mein 3 GB bacha hai\nYouTube pe gameplay dekh liya\n'Graphics mast hai yaar'",
         level=0.05, mood="dead", sfx="trombone", shake=True),
]

CAPTION = """
Game 6 hazaar ka, console 65 hazaar ka, meri salary bas trailer dekhne layak 🙂
gaming memes aur salary memes for every thaka hua desi jo GTA 6 YouTube pe hi khelega

Send karo us dost ko jiske paas PS5 hai, 'bhai bas ek mission' 👇

#thakahuadesi #gta6 #salarymemes #gamingmemes #desimemes
"""


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


if __name__ == "__main__":
    render_reel(BEATS, Q / "2026-11-20_2100_gta-salary-reel", CAPTION)
    story("2026-11-20_2130_question-story",
          question_story("Sach batao", "GTA 6 ka plan? PS5 kharidoge ya dost ke ghar 'bas ek mission'?"))
