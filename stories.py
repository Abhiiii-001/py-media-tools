"""1080x1920 Story cards in brand style. The API can't add stickers (polls, links, music),
so stories here are images that make people REPLY (replies land in DMs = strong signal)
or go to the feed.

  mood_story("Aaj ka mood", "chai: 20%\\nmotivation: 0%\\nEMI: 100%", level=0.2)
  teaser_story("Naya reel aaya hai", "dekha kya? feed pe jao", preview="content/queue/.../cover.png")
  question_story("Sach batao", "Salary aate hi pehla kharcha kya hota hai?", "reply karo, best wala story pe")
"""
from PIL import Image, ImageDraw, ImageFilter

from brand import (BLACK, FONT_BODY, FONT_HEAD, RED, WHITE, YELLOW, label, mascot, panel, sunburst,
                   text_block, watermark)

SW, SH = 1080, 1920
TOP, BOTTOM = 260, 1560  # keep clear of the story header and reply bar


def _base(bg=RED, ray=YELLOW):
    return sunburst(bg, ray, size=(SW, SH), center=(SW // 2, 1000))


def mood_story(title, body, level=0.3, mood="tired"):
    img = _base()
    label(img, title.upper(), (SW // 2, TOP), size=64)
    panel(img, (100, TOP + 150, 880, 520))
    text_block(img, body, (140, TOP + 180, 800, 460), path=FONT_BODY, size=78, fill=BLACK, stroke=None)
    mascot(img, SW // 2, TOP + 760, scale=1.25, level=level, mood=mood)
    watermark(img, y=BOTTOM + 30)
    return img


def teaser_story(title, sub, preview=None):
    img = _base(BLACK, "#222222")
    text_block(img, title.upper(), (80, TOP, 920, 260), size=130, fill=YELLOW)
    if preview:
        p = Image.open(preview).convert("RGB")
        p.thumbnail((760, 900))
        # tease, don't give it away: blur the lower half
        lower = p.crop((0, p.height // 2, p.width, p.height)).filter(ImageFilter.GaussianBlur(22))
        p.paste(lower, (0, p.height // 2))
        x, y = (SW - p.width) // 2, TOP + 300
        d = ImageDraw.Draw(img)
        d.rectangle((x - 10, y - 10, x + p.width + 10, y + p.height + 10), fill=YELLOW)
        img.paste(p, (x, y))
        ty = y + p.height + 50
    else:
        mascot(img, SW // 2, TOP + 400, scale=1.3, level=0.5, mood="tired")
        ty = TOP + 900
    text_block(img, sub, (80, ty, 920, BOTTOM - ty), path=FONT_BODY, size=60, fill=WHITE)
    watermark(img, y=BOTTOM + 30)
    return img


def question_story(title, question, sub="reply karo, best wale story pe dalenge"):
    img = _base()
    label(img, title.upper(), (SW // 2, TOP), size=64)
    panel(img, (90, TOP + 150, 900, 600))
    text_block(img, question, (130, TOP + 180, 820, 540), path=FONT_BODY, size=84, fill=BLACK, stroke=None)
    mascot(img, 300, TOP + 830, scale=0.95, level=0.5, mood="tired")
    text_block(img, sub, (520, TOP + 860, 500, 300), path=FONT_HEAD, size=72, fill=WHITE)
    watermark(img, y=BOTTOM + 30)
    return img
