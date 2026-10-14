"""Batch: 15-17 Oct 2026 (6 posts). Run from repo root: python content/scripts/batch_2026-10-15.py"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from brand import *  # noqa: E402

QUEUE = ROOT / "content" / "queue"


def out(folder, kind, slides, caption):
    f = QUEUE / folder
    f.mkdir(parents=True, exist_ok=True)
    names = []
    for i, img in enumerate(slides, 1):
        n = f"{i}.png"
        save(img, f / n)
        names.append(n)
    (f / "caption.txt").write_text(caption.strip() + "\n", encoding="utf-8")
    (f / "meta.json").write_text(json.dumps({"type": kind, "media": names}, indent=2), encoding="utf-8")
    print("built", folder, len(slides), "slides")


def stage_slide(tag, headline, body, level, mood="tired", page=None, bg=RED, ray=YELLOW):
    img = sunburst(bg, ray)
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


def two_panel(top_tag, top_text, bottom_tag, bottom_text, top_level, bottom_level,
              bottom_mood="dead", title=None):
    img = sunburst()
    y = 60
    if title:
        text_block(img, title, (60, 40, 960, 130), size=96)
        y = 190
    ph = (H - y - 130) // 2 - 20
    for i, (tag, txt, lvl, mood) in enumerate(((top_tag, top_text, top_level, "happy"),
                                                (bottom_tag, bottom_text, bottom_level, bottom_mood))):
        py = y + i * (ph + 40)
        panel(img, (60, py, 960, ph))
        label(img, tag, (90, py - 26), anchor_center=False, size=46)
        text_block(img, txt, (110, py + 60, 560, ph - 90), path=FONT_BODY, size=58, fill=BLACK, stroke=None)
        mascot(img, 840, py + 70, scale=0.62, level=lvl, mood=mood)
    watermark(img)
    return img


# ---------- 15 Oct 1 PM: carousel, 15 taareekh report ----------
c = []
img = sunburst()
label(img, "MID-MONTH REPORT", (W // 2, 110))
text_block(img, "AAJ 15 TAAREEKH HAI", (90, 220, 900, 330), size=170)
mascot(img, W // 2, 600, scale=1.45, level=0.3)
text_block(img, "account check mat karna bhai", (120, 1130, 840, 110), path=FONT_BODY, size=56, fill=WHITE)
watermark(img, "1/6")
c.append(img)
c.append(stage_slide("1 TAAREEKH", "SALARY AAYI", "main Ambani ka chhota bhai. Zomato pe 'add more' bina soche", 1.0, "happy", "2/6"))
c.append(stage_slide("5 TAAREEKH", "EMI NE HI BOLA", "rent, EMI, credit card bill sab ek saath aaye. salary ne bye bola", 0.65, "tired", "3/6"))
c.append(stage_slide("10 TAAREEKH", "ZOMATO UNINSTALL", "ab ghar ka khana khata hu. isko healthy lifestyle bolte hai", 0.35, "tired", "4/6"))
c.append(stage_slide("15 TAAREEKH (AAJ)", "BALANCE: RS 847", "mahina baaki: 15 din\nconfidence: 0\nchai: last wali", 0.08, "dead", "5/6"))
c.append(cta_slide("SEND KARO US DOST KO JISKA BALANCE BHI AAJ 3 DIGIT MEIN HAI",
                   "wo samajh jayega", "6/6"))
out("2026-10-15_1300_15-taareekh", "carousel", c, """
15 taareekh aa gayi aur salary chali gayi
mid month ka sach, desi salary memes for thake hue log

Us dost ko bhejo jiska balance bhi aaj 3 digit ka hai 👇

#thakahuadesi #salarymemes #desimemes #officememes #middleclassmemes
""")

# ---------- 15 Oct 8:30 PM: meme, Diwali gift ----------
img = two_panel("HR KA MAIL", "'Is Diwali company ki taraf se aapke liye special gift'",
                "GIFT", "", 0.9, 0.2, "dead", title="DIWALI GIFT 2026")
soan_papdi(img, 360, 900, 1.0)
watermark(img)
out("2026-10-15_2030_diwali-gift", "image", [img], """
Mail padh ke iPhone soch liya tha
Diwali gift reality check, corporate memes jo dil pe lagte hai

Tag karo us colleague ko jo abhi bhi bonus ka wait kar raha hai 👇

#thakahuadesi #diwalimemes #officememes #corporatememes #desimemes
""")

# ---------- 16 Oct 1 PM: meme, Friday quick call ----------
img = sunburst()
label(img, "FRIDAY 5:58 PM", (W // 2, 70))
panel(img, (70, 190, 940, 300))
text_block(img, "Boss: free ho? ek quick 5 min call le lete hai", (110, 210, 860, 260),
           path=FONT_BODY, size=66, fill=BLACK, stroke=None)
mascot(img, W // 2, 540, scale=1.0, level=0.15, mood="dead")
text_block(img, "QUICK CALL: 1 GHANTA 40 MIN", (70, 920, 940, 200), size=104)
text_block(img, "weekend ki duration: khatam", (70, 1130, 940, 90), path=FONT_BODY, size=56, fill=WHITE)
watermark(img)
out("2026-10-16_1300_friday-quick-call", "image", [img], """
5 min bola tha. 5 min.
office memes for everyone jiska Friday bhi ek 'quick call' ne kha liya

Send karo us dost ko jo abhi isi call pe hai 👇

#thakahuadesi #officememes #corporatememes #fridaymemes #desimemes
""")

# ---------- 16 Oct 8:30 PM: carousel, Diwali safai ----------
c = []
img = sunburst()
label(img, "23 DIN PEHLE. HAAN, 23.", (W // 2, 110))
text_block(img, "DIWALI SAFAI SHURU HO GAYI", (80, 220, 920, 380), size=170)
mascot(img, W // 2, 650, scale=1.35, level=0.4)
text_block(img, "har desi ghar ke 5 stages", (120, 1150, 840, 90), path=FONT_BODY, size=56, fill=WHITE)
watermark(img, "1/7")
c.append(img)
c.append(stage_slide("STAGE 1", "'BAS PANKHA SAAF KAR DE'", "mummy ne bola 5 min ka kaam hai. main stool pe chadha. trap tha", 0.8, "happy", "2/7"))
c.append(stage_slide("STAGE 2", "PANKHA SE POORA GHAR", "pankhe ke baad almari, almari ke baad parde, parde ke baad chhat", 0.6, "tired", "3/7"))
c.append(stage_slide("STAGE 3", "ALMARI KA KHAZANA", "2014 ka bill, 3 toote charger, aur ek dabba jisme sirf aur dabbe hai", 0.45, "tired", "4/7"))
c.append(stage_slide("STAGE 4", "'YE MAT PHENK'", "mummy: sab phenk do\nbhi mummy: ye nahi, kaam aayega", 0.25, "tired", "5/7"))
c.append(stage_slide("STAGE 5", "DIWALI KE DIN", "'tum log ghar ka koi kaam hi nahi karte'", 0.05, "dead", "6/7"))
c.append(cta_slide("SEND KARO US DOST KO JO ABHI PANKHE PE CHADHA HUA HAI",
                   "use bhi pata hona chahiye wo akela nahi", "7/7"))
out("2026-10-16_2030_diwali-safai", "carousel", c, """
Diwali 23 din door hai aur pankha 4 baar saaf ho chuka hai
diwali safai memes, har desi ghar ki same kahani

Send karo us dost ko jo abhi stool pe khada hai 👇

#thakahuadesi #diwalisafai #diwalimemes #desimemes #indianmom
""")

# ---------- 17 Oct 1 PM: meme, Saturday plans ----------
img = two_panel("FRIDAY RAAT", "kal 7 baje uthunga. gym, laundry, groceries. life sort karunga",
                "SATURDAY 1 PM", "utha. phone dekha. thak gaya. wapas so gaya", 1.0, 0.1, "dead",
                title="SATURDAY KA PLAN")
out("2026-10-17_1300_saturday-plan", "image", [img], """
Plan solid tha, bas main nahi tha
weekend memes for every thaka hua desi

Tag karo us dost ko jo abhi bhi bistar mein hai 👇

#thakahuadesi #weekendmemes #relatablememes #desimemes #adultingmemes
""")

# ---------- 17 Oct 8:30 PM: meme, match vs safai ----------
img = sunburst()
label(img, "SATURDAY 7 PM", (W // 2, 70))
text_block(img, "INDIA VS WI MATCH. CHIPS READY. REMOTE HAATH MEIN", (70, 170, 940, 260), size=96)
panel(img, (70, 470, 940, 220))
text_block(img, "Mummy: 'match baad mein, aaj kitchen ki upar wali almari'",
           (110, 490, 860, 180), path=FONT_BODY, size=60, fill=BLACK, stroke=None)
mascot(img, 300, 760, scale=0.95, level=0.2, mood="dead")
panel(img, (560, 760, 450, 360), fill=YELLOW)
label(img, "MERA SCORE", (785, 735), size=44)
text_block(img, "4 almari\n2 parde\n0 overs dekhe", (590, 810, 390, 290), size=84, fill=BLACK, stroke=None)
text_block(img, "Diwali safai > cricket", (70, 1180, 940, 80), path=FONT_BODY, size=52, fill=WHITE)
watermark(img)
out("2026-10-17_2030_match-vs-safai", "image", [img], """
Match ka score pata nahi, almari ka pata hai
cricket memes x diwali safai, desi ghar mein dono saath nahi chalte

Score batao comment mein, main kitchen mein hu 👇

#thakahuadesi #cricketmemes #indvswi #diwalisafai #desimemes
""")
