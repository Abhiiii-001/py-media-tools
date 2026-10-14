"""Template memes in Thaka Hua Desi style: caption band on top (the format Indian meme pages use),
the template below, red frame, @thaka_hua_desi watermark. Templates live in content/templates/
with templates.json describing each one (use_for, optional text zones).

  template_meme("paisa-laya", "Me on 1st of every month to HR")
  template_meme("drake", "Salary day pe", labels=["Savings karna", "Zomato pe 4 order"])
"""
import json
from pathlib import Path

from PIL import Image, ImageDraw

from brand import (BLACK, FONT_BODY, FONT_HEAD, RED, WHITE, YELLOW, H, W, font, text_block,
                   watermark, wrap)

TPL = Path(__file__).parent / "content" / "templates"
LIB = json.loads((TPL / "templates.json").read_text(encoding="utf-8"))
MARGIN = 36


def _caption_height(text, size, width):
    d = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    lines = wrap(text, font(FONT_BODY, size), width, d)
    return int(len(lines) * size * 1.18)


def template_meme(slug, caption, labels=None, footer=None):
    """Return a 1080x1350 image. labels fill the template's zones in order (see templates.json)."""
    meta = LIB[slug]
    tpl = Image.open(TPL / f"{slug}.jpg").convert("RGB")
    inner_w = W - 2 * MARGIN
    canvas = Image.new("RGB", (W, H), RED)
    d = ImageDraw.Draw(canvas)

    # caption band: biggest font that keeps the band within what the template leaves free
    # (wide templates leave room, so the caption grows instead of leaving empty red space)
    tpl_h_at_full_w = tpl.height * inner_w / tpl.width
    room = max(H * 0.22, min(H * 0.42, H - 2 * MARGIN - 80 - tpl_h_at_full_w))
    size = 84
    while size > 34 and _caption_height(caption, size, inner_w - 60) + 60 > room:
        size -= 3
    cap_h = _caption_height(caption, size, inner_w - 60) + 60
    foot_h = 80 if not footer else 150
    avail_h = H - 2 * MARGIN - cap_h - foot_h

    scale = min(inner_w / tpl.width, avail_h / tpl.height)
    tw, th = int(tpl.width * scale), int(tpl.height * scale)
    tpl = tpl.resize((tw, th), Image.LANCZOS)

    block_h = cap_h + th
    top = MARGIN + (H - 2 * MARGIN - foot_h - block_h) // 2
    # white card behind caption + image, yellow accent line
    d.rectangle((MARGIN - 6, top - 6, W - MARGIN + 6, top + block_h + 6), fill=BLACK)
    d.rectangle((MARGIN, top, W - MARGIN, top + cap_h), fill=WHITE)
    text_block(canvas, caption, (MARGIN + 30, top + 18, inner_w - 60, cap_h - 36), path=FONT_BODY,
               size=size, fill=BLACK, stroke=None, min_size=30)
    d.rectangle((MARGIN, top + cap_h - 8, W - MARGIN, top + cap_h), fill=YELLOW)
    ix = (W - tw) // 2
    iy = top + cap_h
    if tw < inner_w:  # narrow template: fill the card sides
        d.rectangle((MARGIN, iy, W - MARGIN, iy + th), fill=WHITE)
    canvas.paste(tpl, (ix, iy))

    dark = meta.get("dark_labels")
    for zone, text in zip(meta.get("zones") or [], labels or []):
        zx, zy, zw, zh = zone
        text_block(canvas, text, (ix + int(zx * tw) + 6, iy + int(zy * th) + 4, int(zw * tw) - 12,
                                  int(zh * th) - 8), path=FONT_BODY if dark else FONT_HEAD,
                   size=72, min_size=24, fill=BLACK if dark else WHITE, stroke=None if dark else BLACK)

    if footer:
        text_block(canvas, footer, (MARGIN, H - MARGIN - foot_h, inner_w, foot_h - 50),
                   path=FONT_BODY, size=46, fill=YELLOW, stroke=BLACK)
    watermark(canvas)
    return canvas


def catalog():
    """One line per template, for picking: slug | name | use_for | zones."""
    return "\n".join(f"{k} | {v['name']} | {v['use_for']} | zones={len(v['zones'] or [])}"
                     for k, v in LIB.items())


if __name__ == "__main__":
    print(catalog())


def reel_template(slug, labels=None, width=940):
    """For reel.py beats: draw=reel_template("paisa-laya") pastes the template (with zone labels)
    into the reel frame below the headline. Static movie stills only, never movie clips."""
    meta = LIB[slug]

    def draw(img, y):
        tpl = Image.open(TPL / f"{slug}.jpg").convert("RGB")
        max_h = 1480 - y - 40
        s = min(width / tpl.width, max_h / tpl.height)
        tw, th = int(tpl.width * s), int(tpl.height * s)
        tpl = tpl.resize((tw, th), Image.LANCZOS)
        x = (img.width - tw) // 2
        ImageDraw.Draw(img).rectangle((x - 8, y - 8, x + tw + 8, y + th + 8), fill=BLACK)
        img.paste(tpl, (x, y))
        dark = meta.get("dark_labels")
        for zone, text in zip(meta.get("zones") or [], labels or []):
            zx, zy, zw, zh = zone
            text_block(img, text, (x + int(zx * tw) + 6, y + int(zy * th) + 4, int(zw * tw) - 12,
                                   int(zh * th) - 8), path=FONT_BODY if dark else FONT_HEAD, size=64,
                       min_size=22, fill=BLACK if dark else WHITE, stroke=None if dark else BLACK)
        return y + th
    return draw
