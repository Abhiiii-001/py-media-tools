"""Stories for 15-17 Oct 2026 (3/day: 1000 mood, 1330/2130 teaser or question)."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from stories import mood_story, question_story, teaser_story  # noqa: E402

Q = ROOT / "content" / "queue"


def story(folder, img):
    f = Q / folder
    f.mkdir(parents=True, exist_ok=True)
    img.save(f / "1.png", "PNG", optimize=True)
    (f / "caption.txt").write_text("\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": "story", "media": ["1.png"]}, indent=2), encoding="utf-8")
    print("built", folder)


story("2026-10-15_1000_mood-story", mood_story("Aaj 15 taareekh hai", "chai: 20%\nbalance: 3 digit\nmotivation: loading...", 0.2))
story("2026-10-15_1330_teaser-story", teaser_story("Naya post aaya", "15 taareekh wala sach. feed pe dekho, phir us dost ko bhejo",
      Q / "2026-10-15_1300_15-taareekh" / "1.png"))
story("2026-10-15_2130_question-story", question_story("Sach batao", "Diwali gift mein sabse bekaar cheez kya mili hai aaj tak?"))

story("2026-10-16_1000_mood-story", mood_story("Friday hai bhai", "body: office mein\ndimaag: weekend pe\nboss: 'ek quick call?'", 0.5))
story("2026-10-16_1330_teaser-story", teaser_story("Friday 5:58 PM", "naya reel feed pe. tag karo us colleague ko jo abhi call pe hai",
      Q / "2026-10-16_1300_quick-call-reel" / "cover.png"))
story("2026-10-16_2130_question-story", question_story("Diwali safai update", "Tumhare ghar ki safai kitne % ho gayi? Pankha saaf hua ya nahi?"))

story("2026-10-17_1000_mood-story", mood_story("Saturday mood", "plan: gym\nreality: bistar\nguilt: 0%", 0.9, "happy"))
story("2026-10-17_1330_question-story", question_story("Aaj ka scene", "India vs WI match dekhoge ya almari saaf karoge? Sach bolna"))
story("2026-10-17_2130_teaser-story", teaser_story("Match vs Mummy", "reel feed pe hai. score comment mein batao, main kitchen mein hu",
      Q / "2026-10-17_2030_match-vs-safai-reel" / "cover.png"))
