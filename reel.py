"""Thaka Hua Desi reel engine: beats -> animated 1080x1920 MP4 with original synthesized audio.

A beat is a dict:
  dur    seconds on screen
  tag    small black label (optional)
  head   big outlined headline (optional)
  box    white speech panel text (optional)
  level  chai level 0..1, mood: happy | tired | dead
  sfx    ding | pop | tick | trombone | none   (fires at beat start)
  draw   optional fn(img, top_y) for custom art (e.g. soan_papdi)
  shake  True to jitter on entry (punchline)
No licensed music anywhere: every sound is generated here.
"""
import math
import shutil
import subprocess
import wave
from pathlib import Path

import numpy as np
from PIL import Image

from brand import (BLACK, FONT_BODY, RED, WHITE, YELLOW, label, mascot, panel,
                   sunburst, text_block, watermark)

RW, RH, FPS, SR = 1080, 1920, 30, 48000
# Reels UI covers ~top 220px and bottom ~420px; keep content inside this band.
SAFE_TOP, SAFE_BOTTOM = 250, 1480


def find_ffmpeg():
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    hits = list(Path.home().glob("AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin/ffmpeg.exe"))
    if not hits:
        raise SystemExit("ffmpeg not found")
    return str(hits[0])


# ---------------- visuals ----------------
def beat_overlay(b):
    """Everything except the background, as a transparent layer."""
    img = Image.new("RGBA", (RW, RH), (0, 0, 0, 0))
    y = SAFE_TOP
    if b.get("tag"):
        label(img, b["tag"], (RW // 2, y), size=60)
        y += 130
    if b.get("head"):
        y = text_block(img, b["head"], (70, y, 940, 420 if not b.get("box") else 330), size=150) + 30
    if b.get("box"):
        bh = 300
        panel(img, (80, y, 920, bh))
        text_block(img, b["box"], (120, y + 20, 840, bh - 40), path=FONT_BODY, size=66, fill=BLACK, stroke=None)
        y += bh + 50
    if b.get("draw"):
        y = b["draw"](img, y) + 40
    if b.get("level") is not None:
        room = SAFE_BOTTOM - y
        scale = max(0.6, min(1.3, room / 360))
        mascot(img, RW // 2, max(y, SAFE_BOTTOM - int(360 * scale)), scale=scale,
               level=b["level"], mood=b.get("mood", "tired"))
    watermark(img, y=SAFE_BOTTOM + 40)
    return img


def render_frames(beats):
    overlays = [beat_overlay(b) for b in beats]
    t_global = 0
    for b, ov in zip(beats, overlays):
        n = int(round(b["dur"] * FPS))
        bg_colors = b.get("bg", (RED, YELLOW))
        for i in range(n):
            t = i / FPS
            frame = sunburst(*bg_colors, size=(RW, RH), center=(RW // 2, 900),
                             angle=(t_global + t) * 9).convert("RGBA")
            layer = ov
            # pop-in: scale 0.82 -> 1.0 over first 0.18s
            if t < 0.18:
                s = 0.82 + 0.18 * (t / 0.18)
                w, h = int(RW * s), int(RH * s)
                layer = Image.new("RGBA", (RW, RH), (0, 0, 0, 0))
                layer.paste(ov.resize((w, h)), ((RW - w) // 2, (RH - h) // 2))
            dx = dy = 0
            if b.get("shake") and t < 0.45:
                dx = int(14 * math.sin(t * 90))
                dy = int(8 * math.cos(t * 70))
            frame.alpha_composite(layer, (dx, dy)) if dx or dy else frame.alpha_composite(layer)
            yield frame.convert("RGB")
        t_global += b["dur"]


def make_cover(beats, path):
    """Cover = first beat, fully settled. Grid crops 1080x1350 from the middle, so it still reads."""
    bg = sunburst(*beats[0].get("bg", (RED, YELLOW)), size=(RW, RH), center=(RW // 2, 900)).convert("RGBA")
    bg.alpha_composite(beat_overlay(beats[0]))
    bg.convert("RGB").save(path, "PNG", optimize=True)


# ---------------- audio ----------------
def _env(n, attack=0.005, release=None):
    t = np.arange(n) / SR
    a = np.clip(t / attack, 0, 1)
    r = np.exp(-t / release) if release else 1
    return a * r


def sfx_ding():
    n = int(0.9 * SR); t = np.arange(n) / SR
    tone = sum(np.sin(2 * np.pi * f * t) * g for f, g in ((1320, 1), (2640, .35), (3960, .15)))
    return 0.5 * tone * _env(n, release=0.25)


def sfx_pop():
    n = int(0.12 * SR); t = np.arange(n) / SR
    f = 500 + 1400 * t / t[-1]
    return 0.6 * np.sin(2 * np.pi * np.cumsum(f) / SR) * _env(n, release=0.04)


def sfx_tick(dur):
    out = np.zeros(int(dur * SR))
    click_n = int(0.03 * SR)
    rng = np.random.default_rng(1)
    for k, start in enumerate(np.arange(0, dur, 0.25)):
        i = int(start * SR)
        c = rng.normal(0, 1, click_n) * _env(click_n, 0.001, 0.006) * (0.5 if k % 2 else 0.35)
        c = np.convolve(c, np.ones(4) / 4, "same")
        out[i:i + click_n] += c[:len(out) - i]
    return out


def sfx_trombone():
    """Classic 'wah wah wah waaah', synthesized brass-ish tone."""
    notes = [(293.7, .38), (277.2, .38), (261.6, .38), (246.9, 1.4)]
    parts = []
    for k, (f, d) in enumerate(notes):
        n = int(d * SR); t = np.arange(n) / SR
        vib = 1 + (0.025 * np.sin(2 * np.pi * 6 * t) * np.clip(t / 0.3, 0, 1) if k == 3 else 0)
        ph = 2 * np.pi * np.cumsum(f * vib) / SR
        tone = sum(np.sin(h * ph) / h ** 0.9 for h in range(1, 9))
        env = np.clip(t / 0.04, 0, 1) * np.clip((d - t) / 0.08, 0, 1)
        if k == 3:
            env *= np.exp(-t / 1.1)
        parts.append(0.22 * tone * env)
    return np.concatenate(parts)


def bed(dur, bpm=96):
    """Quiet original groove under everything: kick + hat."""
    out = np.zeros(int(dur * SR))
    beat = 60 / bpm
    kn = int(0.25 * SR); kt = np.arange(kn) / SR
    kick = np.sin(2 * np.pi * (45 + 80 * np.exp(-kt * 30)) * kt) * np.exp(-kt * 12)
    hn = int(0.05 * SR)
    hat = np.random.default_rng(2).normal(0, 1, hn) * np.exp(-np.arange(hn) / SR * 90)
    hat = hat - np.convolve(hat, np.ones(6) / 6, "same")
    for k, start in enumerate(np.arange(0, dur, beat / 2)):
        i = int(start * SR)
        snd = kick * 0.5 if k % 2 == 0 else hat * 0.12
        out[i:i + len(snd)] += snd[:len(out) - i]
    return out


def build_audio(beats, path):
    total = sum(b["dur"] for b in beats)
    mix = bed(total) * 0.35
    t = 0
    for b in beats:
        s = b.get("sfx", "pop")
        clip = {"ding": sfx_ding, "pop": sfx_pop, "trombone": sfx_trombone}.get(s)
        clip = clip() if clip else (sfx_tick(b["dur"]) if s == "tick" else None)
        if clip is not None:
            i = int(t * SR)
            if s == "trombone":
                mix[i:] *= 0.15  # duck the groove for the punchline
            mix[i:i + len(clip)] += clip[:len(mix) - i]
        t += b["dur"]
    fade = int(0.3 * SR)
    mix[-fade:] *= np.linspace(1, 0, fade)
    mix = mix / max(1e-6, np.abs(mix).max()) * 0.85
    pcm = (mix * 32767).astype(np.int16)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(pcm.tobytes())


# ---------------- encode ----------------
def render_reel(beats, folder, caption):
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    wav = folder / "_audio.wav"
    build_audio(beats, wav)
    cmd = [find_ffmpeg(), "-y", "-loglevel", "error",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{RW}x{RH}", "-r", str(FPS), "-i", "-",
           "-i", str(wav),
           "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-profile:v", "high",
           "-c:a", "aac", "-b:a", "128k", "-ar", str(SR), "-ac", "2",
           "-movflags", "+faststart", "-shortest", str(folder / "reel.mp4")]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for frame in render_frames(beats):
        p.stdin.write(frame.tobytes())
    p.stdin.close()
    if p.wait():
        raise SystemExit("ffmpeg failed")
    wav.unlink()
    make_cover(beats, folder / "cover.png")
    (folder / "caption.txt").write_text(caption.strip() + "\n", encoding="utf-8")
    import json
    (folder / "meta.json").write_text(json.dumps(
        {"type": "reel", "media": ["reel.mp4"], "cover": "cover.png"}, indent=2), encoding="utf-8")
    print("built reel", folder.name, f"{sum(b['dur'] for b in beats):.1f}s")
