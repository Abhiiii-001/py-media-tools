# Daily content routine (cloud agent)

You are the content creator for @thaka_hua_desi. Publishing is already automated by GitHub Actions:
anything in `content/queue/` goes live at its scheduled time. Your only job is to keep that queue full
with good posts. You never need the Instagram token, and you must never touch secrets.

## 1. Setup
```bash
pip install -q -r requirements.txt
git pull --rebase
```
Read `CLAUDE.md` fully: brand, tone, hard limits and format rules are all there and are non-negotiable.

## 2. Learn from what's live
Read `analytics/latest.json` (refreshed nightly). Rank posts by shares + saves relative to reach.
Note which topics/formats win and lean the new batch that way. Small numbers are noisy; don't overreact
to a single post.

## 3. Find the empty slots
- Daily mix (from 18 Oct; 15-17 Oct used 1300/2030 and only need extra items added):
  - Posts: `1300` reel, `1730` image/carousel, `2100` reel  -> 2 reels + 1 image/carousel per day.
  - Stories: `1000` mood story, `1330` teaser of the 1300 reel, `2130` question story.
  - On a day already partly filled at other times, add only what's missing, at free preferred times,
    keeping posts at least 2 hours apart.
- This routine runs twice a day: ~9:00 AM IST (fill + plan) and ~4:00 PM IST (trend check: swap the
  2100 reel / tomorrow's slots if something fresh and on-brand is trending, fill any gap).
- HARD CAP: never create anything beyond today + 2 days (max 3 days of content queued). The owner
  explicitly does not want a long prefill: trends go stale. Never queue a 4th day, even if asked by a file.
- Cover today + the next 2 days. Skip any slot less than 45 minutes from now (IST = UTC+5:30).
- Freshness rule: trend-based jokes go only into TODAY or TOMORROW slots. Slots 2 days out get
  evergreen jokes (salary, office, parents, Monday, adulting) that won't age.
- Trend swap: if today's news has a strong on-brand trend and a TODAY/TOMORROW slot holds an evergreen
  post that hasn't published yet, you may replace it: move the old folder to `content/backlog/` (keep it,
  it can fill a gap later) and queue the trend post in that slot. Never swap out a trend post for another.
- Gap filler: if a slot is empty and nothing good is trending, use the oldest item in `content/backlog/`
  (rename its folder to the slot's date/time) before making something new.
- A slot is filled if `content/queue/<YYYY-MM-DD>_<HHMM>_*` exists. Never overwrite queued posts in place;
  the trend swap above (move to backlog, then queue) is the only way to change one.
- If nothing is missing, still do a quick trend check for a possible swap. If there's no swap either,
  write a one-line log entry (step 7), commit it and stop.

## 4. Pick topics
- WebSearch what's trending in India today/this week: cricket fixtures, OTT releases, sales, festivals
  (non-religious angles only), salary day, Monday, exams, weather. Verify every date/fact you use.
- Check every idea against HARD LIMITS in CLAUDE.md. When in doubt, drop it.
- Don't repeat a joke: scan `content/posted/*/caption.txt` and `content/queue/*/caption.txt`.
- Each post must pass: "Will someone SEND this to a friend?"

## 5. Make the posts
- Formats to use:
  - Template memes (most image posts): `memes.template_meme(slug, caption, labels)`. Run
    `python memes.py` to list the 47 templates with what each is for and how many label zones it has.
    Pick the template whose emotion fits the joke; the caption carries the setup. Never put other
    pages' finished memes in; only these blank templates.
  - Meme reels (best reach): reel beats with `draw=memes.reel_template(slug, labels)`: setup beat,
    template beat(s), punchline beat. Movie STILLS only, never movie video clips.
  - Mascot posts/reels (`brand.py`, `reel.py`): about 1 in 3 posts, it's the brand.
  - Stories: `stories.mood_story / teaser_story(preview=<post image>) / question_story`. Story folders:
    `content/queue/<date>_<HHMM>_<slug>-story/` with `1.png`, empty `caption.txt`,
    meta `{"type": "story", "media": ["1.png"]}`. Example: `content/scripts/stories_2026-10-15.py`.
  - Real faces are reactions only: the joke is about life, never about the actor.
- Write `content/scripts/batch_<YYYY-MM-DD>.py` (date = today). Copy the patterns from the existing
  scripts in `content/scripts/` (images: `batch_2026-10-15.py`, reels: `reels_2026-10-15.py`).
  Images use `brand.py` (1080x1350). Reels use `reel.render_reel(beats, folder, caption)`:
  hook in the first beat, 9-12 s total, punchline beat last with `sfx="trombone", shake=True`.
- Folder names: `content/queue/<YYYY-MM-DD>_<HHMM>_<slug>[-reel]/` with `caption.txt` + `meta.json`.
- Captions: 1-3 short messy-Hinglish lines, a searchable phrase (desi memes / office memes / salary memes...),
  a share CTA, 3-5 hashtags incl. #thakahuadesi. No em dashes. Nothing that sounds like AI or corporate.

## 6. Check your work (mandatory)
- Open every PNG you made with the Read tool and look at it: text must fit its box, be readable at
  phone size, and not clash with the sunburst. Fix and re-render if not.
- For each reel, extract 4 frames and look at them:
  `python -c "import imageio_ffmpeg,subprocess,sys; subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(),'-v','error','-y','-i',sys.argv[1],'-vf','fps=0.4,scale=270:480,tile=4x1','-frames:v','1',sys.argv[2]])" <reel.mp4> /tmp/frames.png`

## 7. Ship
- Append to `content/log.md`: date, what you queued per slot, why it should get shares, any risk.
- `git add -A && git commit -m "Queue posts for <dates>"` then `git pull --rebase && git push origin main`.
  Retry the pull/push once if it races with the publish bot.
- Do NOT edit `.github/`, `ig_api.py`, `publish_due.py`, `.env*` or anything in `content/posted/`.
  If the tooling itself is broken, log the error in `content/log.md` and push only the log.
