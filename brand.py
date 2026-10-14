"""Thaka Hua Desi brand renderer: 1080x1350 meme/carousel slides in house style.

Red #E8262E, yellow #FFD21F, white, black outlines, heavy bold type, sunburst,
@thaka_hua_desi watermark, chai glass mascot (chai level = energy/salary level).
"""
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
RED, YELLOW, WHITE, BLACK = "#E8262E", "#FFD21F", "#FFFFFF", "#111111"
CHAI, CHAI_TOP, GLASS = "#B9733A", "#D79A5E", "#E4F1F5"
# Open-licence (OFL) fonts bundled in the repo so renders match locally and in the cloud.
FONTS = Path(__file__).parent / "fonts"
FONT_HEAD = str(FONTS / "Anton-Regular.ttf")
FONT_BODY = str(FONTS / "ArchivoBlack-Regular.ttf")
HANDLE = "@thaka_hua_desi"


def font(path, size):
    return ImageFont.truetype(path, size)


def sunburst(bg=RED, ray=YELLOW, rays=24, center=None, size=(W, H), angle=0.0):
    img = Image.new("RGB", size, bg)
    d = ImageDraw.Draw(img)
    cx, cy = center or (size[0] // 2, size[1] // 2)
    r = 2600
    step = 2 * math.pi / rays
    off = math.radians(angle)
    for i in range(0, rays, 2):
        a1, a2 = i * step + off, (i + 1) * step + off
        d.polygon([(cx, cy), (cx + r * math.cos(a1), cy + r * math.sin(a1)),
                   (cx + r * math.cos(a2), cy + r * math.sin(a2))], fill=ray)
    return img


def wrap(text, fnt, max_w, d):
    lines = []
    for para in text.split("\n"):
        words, line = para.split(), ""
        for w in words:
            test = f"{line} {w}".strip()
            if d.textlength(test, font=fnt) <= max_w or not line:
                line = test
            else:
                lines.append(line)
                line = w
        lines.append(line)
    return lines


def text_block(img, text, box, path=FONT_HEAD, size=120, fill=WHITE, stroke=BLACK,
               stroke_w=None, min_size=36, align="center", valign="center", spacing=0.12):
    """Fit text inside box (x, y, w, h), shrinking until it fits. Returns bottom y."""
    d = ImageDraw.Draw(img)
    x, y, w, h = box
    while True:
        f = font(path, size)
        sw = stroke_w if stroke_w is not None else max(3, size // 14)
        lines = wrap(text, f, w - 2 * sw, d)
        lh = int(size * (1 + spacing))
        total = lh * len(lines)
        widest = max(d.textlength(l, font=f) for l in lines)
        if (total <= h and widest <= w - 2 * sw) or size <= min_size:
            break
        size -= 4
    ty = y + (h - total) // 2 if valign == "center" else y
    for l in lines:
        lw = d.textlength(l, font=f)
        tx = x + (w - lw) // 2 if align == "center" else x + sw
        if stroke:
            d.text((tx, ty), l, font=f, fill=fill, stroke_width=sw, stroke_fill=stroke)
        else:
            d.text((tx, ty), l, font=f, fill=fill)
        ty += lh
    return ty


def panel(img, box, fill=WHITE, outline=BLACK, width=8, radius=36, shadow=True):
    d = ImageDraw.Draw(img)
    x, y, w, h = box
    if shadow:
        d.rounded_rectangle((x + 12, y + 12, x + w + 12, y + h + 12), radius, fill=BLACK)
    d.rounded_rectangle((x, y, x + w, y + h), radius, fill=fill, outline=outline, width=width)


def label(img, text, xy, fill=YELLOW, size=54, anchor_center=True):
    """Small tilted-feel tag: black box with coloured heavy text."""
    d = ImageDraw.Draw(img)
    f = font(FONT_HEAD, size)
    tw = d.textlength(text, font=f)
    pad = 22
    x, y = xy
    if anchor_center:
        x -= (tw + 2 * pad) / 2
    d.rectangle((x, y, x + tw + 2 * pad, y + size + 2 * pad - 6), fill=BLACK)
    d.text((x + pad, y + pad - 8), text, font=f, fill=fill)


def watermark(img, page=None, y=None):
    d = ImageDraw.Draw(img)
    f = font(FONT_BODY, 30)
    iw, ih = img.size
    y = ih - 72 if y is None else y
    tw = d.textlength(HANDLE, font=f)
    d.text((iw - tw - 48, y), HANDLE, font=f, fill=WHITE, stroke_width=4, stroke_fill=BLACK)
    if page:
        d.text((48, y), page, font=f, fill=WHITE, stroke_width=4, stroke_fill=BLACK)


def mascot(img, cx, top, scale=1.0, level=0.6, mood="tired"):
    """Cutting chai glass with a forced grin. level 0..1 = chai left.
    mood: tired (one wide eye, one twitching), dead (X-ish flat eyes), happy (both wide, big grin)."""
    d = ImageDraw.Draw(img)
    s = scale
    tw, bw, gh = 270 * s, 196 * s, 330 * s
    ol = max(4, int(9 * s))
    tl, tr = (cx - tw / 2, top), (cx + tw / 2, top)
    bl, br = (cx - bw / 2, top + gh), (cx + bw / 2, top + gh)

    def edge_x(yy, side):
        t = (yy - top) / gh
        half = (tw + (bw - tw) * t) / 2
        return cx - half if side < 0 else cx + half

    # glass
    d.polygon([tl, tr, br, bl], fill=GLASS)
    # chai
    level = max(0.0, min(1.0, level))
    cy_top = top + gh * (1 - level * 0.88)
    if level > 0:
        d.polygon([(edge_x(cy_top, -1), cy_top), (edge_x(cy_top, 1), cy_top), br, bl], fill=CHAI)
        d.ellipse((edge_x(cy_top, -1), cy_top - 14 * s, edge_x(cy_top, 1), cy_top + 14 * s), fill=CHAI_TOP)
    # fluting
    for k in range(1, 6):
        t = k / 6
        xt = tl[0] + (tr[0] - tl[0]) * t
        xb = bl[0] + (br[0] - bl[0]) * t
        d.line((xt, top + 70 * s, xb, top + gh - 12 * s), fill="#9FB8C0", width=max(2, int(3 * s)))
    d.polygon([tl, tr, br, bl], outline=BLACK, width=ol)
    d.line((tl[0], top, tr[0], top), fill=BLACK, width=ol + 2)

    # face
    fy = top + 120 * s
    ex1, ex2 = cx - 58 * s, cx + 58 * s
    er = 38 * s
    # dark circles
    for ex in (ex1, ex2):
        d.arc((ex - er - 6 * s, fy - er + 14 * s, ex + er + 6 * s, fy + er + 22 * s), 20, 160,
              fill="#6B3FA0", width=max(3, int(8 * s)))
    if mood == "dead":
        for ex in (ex1, ex2):
            d.line((ex - er * 0.8, fy, ex + er * 0.8, fy), fill=BLACK, width=ol)
            d.line((ex - er * 0.6, fy - er * 0.5, ex + er * 0.6, fy + er * 0.5), fill=BLACK, width=ol - 2)
            d.line((ex - er * 0.6, fy + er * 0.5, ex + er * 0.6, fy - er * 0.5), fill=BLACK, width=ol - 2)
    else:
        # left: wide eye
        r1 = er * 1.15
        d.ellipse((ex1 - r1, fy - r1, ex1 + r1, fy + r1), fill=WHITE, outline=BLACK, width=ol)
        pr = 9 * s
        d.ellipse((ex1 - pr, fy - pr, ex1 + pr, fy + pr), fill=BLACK)
        if mood == "happy":
            d.ellipse((ex2 - r1, fy - r1, ex2 + r1, fy + r1), fill=WHITE, outline=BLACK, width=ol)
            d.ellipse((ex2 - pr, fy - pr, ex2 + pr, fy + pr), fill=BLACK)
        else:
            # right: half-shut twitching eye
            d.chord((ex2 - er, fy - er * 0.7, ex2 + er, fy + er * 0.9), 0, 180, fill=WHITE, outline=BLACK, width=ol)
            d.line((ex2 - er, fy + er * 0.1, ex2 + er, fy + er * 0.1), fill=BLACK, width=ol)
            d.ellipse((ex2 - pr, fy + er * 0.15, ex2 + pr, fy + er * 0.15 + 2 * pr), fill=BLACK)
            for k, ang in enumerate((-40, -10, 20)):
                a = math.radians(ang)
                x0, y0 = ex2 + (er + 14 * s) * math.cos(a), fy - 40 * s + k * 18 * s
                d.line((x0, y0, x0 + 22 * s, y0 - 6 * s), fill=BLACK, width=max(2, int(5 * s)))
    # forced grin
    gy = fy + 78 * s
    gw = 150 * s if mood != "dead" else 90 * s
    if mood == "dead":
        pts = [(cx - gw / 2 + i * gw / 8, gy + (8 * s if i % 2 else -8 * s)) for i in range(9)]
        d.line(pts, fill=BLACK, width=ol)
    else:
        d.chord((cx - gw / 2, gy - 36 * s, cx + gw / 2, gy + 44 * s), 0, 180, fill=WHITE, outline=BLACK, width=ol)
        for k in range(1, 5):
            tx = cx - gw / 2 + k * gw / 5
            d.line((tx, gy + 4 * s, tx, gy + 36 * s), fill=BLACK, width=max(2, int(4 * s)))
        d.line((cx - gw / 2 + 8 * s, gy + 4 * s, cx + gw / 2 - 8 * s, gy + 4 * s), fill=BLACK, width=max(2, int(4 * s)))
    # sweat drops
    if mood != "happy":
        for dx, dy, r in ((-tw / 2 - 30 * s, 40 * s, 16 * s), (tw / 2 + 22 * s, 10 * s, 20 * s)):
            x0, y0 = cx + dx, top + dy
            d.polygon([(x0, y0 - r * 1.8), (x0 - r, y0), (x0 + r, y0)], fill="#5BC0EB", outline=BLACK)
            d.ellipse((x0 - r, y0 - r, x0 + r, y0 + r), fill="#5BC0EB", outline=BLACK, width=max(2, int(4 * s)))
    return top + gh


def soan_papdi(img, cx, top, scale=1.0):
    """The legendary box."""
    d = ImageDraw.Draw(img)
    w, h = 380 * scale, 250 * scale
    x0, y0 = cx - w / 2, top
    d.rectangle((x0 + 14, y0 + 14, x0 + w + 14, y0 + h + 14), fill=BLACK)
    d.rectangle((x0, y0, x0 + w, y0 + h), fill="#F7A21B", outline=BLACK, width=8)
    d.rectangle((x0, y0, x0 + w, y0 + 50 * scale), fill=RED, outline=BLACK, width=8)
    text_block(img, "SOAN PAPDI", (x0 + 10, y0 + 60 * scale, w - 20, 110 * scale), size=80, fill=YELLOW)
    text_block(img, "premium gift pack", (x0 + 10, y0 + 170 * scale, w - 20, 60 * scale),
               path=FONT_BODY, size=34, fill=BLACK, stroke=None)
    return y0 + h


def save(img, path):
    img.save(path, "PNG", optimize=True)
