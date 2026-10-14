"""Instagram Graph API helper for Thaka Hua Desi.

Supports both flavours of the Instagram Graph API (set IG_LOGIN in .env):
  facebook  - Instagram API with Facebook Login (graph.facebook.com). Needs a linked
              Facebook Page. Adds hashtag search, business discovery, Stories (Business acct).
  instagram - Instagram API with Instagram Login (graph.instagram.com).
Reads credentials from .env in this folder.

Usage:
  python ig_api.py whoami
  python ig_api.py refresh-token
  python ig_api.py publish-image <image_url> <caption_file>
  python ig_api.py publish-carousel <caption_file> <url1> <url2> [...]
  python ig_api.py publish-reel <video_url> <caption_file> [cover_url]
  python ig_api.py publish-story <image_or_video_url>            (facebook, Business acct)
  python ig_api.py hashtag-top <hashtag_without_#> [limit]       (facebook only)
  python ig_api.py discover <username>                           (facebook only)
  python ig_api.py upload <local_file>          -> public URL via Cloudinary
  python ig_api.py post <queue_folder>          -> upload media + publish from meta.json
  python ig_api.py report [limit]               -> recent posts with insights (for analytics/latest.json)
  python ig_api.py recent [limit]
  python ig_api.py comments <media_id>
  python ig_api.py reply <comment_id> <message>
  python ig_api.py insights <media_id>
  python ig_api.py account-insights
"""
import hashlib
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

import requests

ROOT = Path(__file__).parent
ENV_PATH = ROOT / ".env"
LOG_PATH = ROOT / "logs" / "api.log"


def load_env():
    if not ENV_PATH.exists():
        # GitHub Actions: secrets come in as environment variables
        env = {k: v for k, v in os.environ.items() if k.startswith(("IG_", "FB_", "CLOUDINARY_"))}
        if not env.get("IG_ACCESS_TOKEN"):
            sys.exit("Missing .env - copy .env.example to .env and fill it in.")
        return env
    env = {}
    for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    if not env.get("IG_ACCESS_TOKEN"):
        sys.exit("IG_ACCESS_TOKEN is empty in .env")
    return env


ENV = load_env()
TOKEN = ENV["IG_ACCESS_TOKEN"]
VERSION = ENV.get("IG_API_VERSION") or "v23.0"
LOGIN = (ENV.get("IG_LOGIN") or "facebook").lower()
HOST = "graph.facebook.com" if LOGIN == "facebook" else "graph.instagram.com"
BASE = f"https://{HOST}/{VERSION}"


def log(msg):
    LOG_PATH.parent.mkdir(exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(f"{datetime.now().isoformat(timespec='seconds')} {msg}\n")


def call(method, path, **params):
    params["access_token"] = TOKEN
    url = path if path.startswith("http") else f"{BASE}/{path}"
    r = requests.request(method, url, params=params if method == "GET" else None,
                         data=params if method != "GET" else None, timeout=60)
    data = r.json()
    if "error" in data:
        log(f"ERROR {method} {path}: {data['error']}")
        sys.exit(f"API error: {data['error'].get('message')}")
    return data


_UID = None


def user_id():
    global _UID
    if _UID:
        return _UID
    _UID = ENV.get("IG_USER_ID")
    if not _UID and LOGIN == "facebook":
        pages = call("GET", "me/accounts", fields="name,instagram_business_account")["data"]
        linked = [p["instagram_business_account"]["id"] for p in pages
                  if p.get("instagram_business_account")]
        if not linked:
            sys.exit("No Instagram account linked to your Facebook Pages.")
        _UID = linked[0]
    elif not _UID:
        _UID = call("GET", "me", fields="user_id")["user_id"]
    return _UID


def facebook_only(cmd):
    if LOGIN != "facebook":
        sys.exit(f"{cmd} needs IG_LOGIN=facebook")


def wait_until_ready(container_id, timeout=600):
    start = time.time()
    while time.time() - start < timeout:
        status = call("GET", container_id, fields="status_code")["status_code"]
        if status == "FINISHED":
            return
        if status in ("ERROR", "EXPIRED"):
            sys.exit(f"Container {container_id} failed: {status}")
        time.sleep(10)
    sys.exit(f"Container {container_id} not ready after {timeout}s")


def publish(container_id):
    wait_until_ready(container_id)
    media = call("POST", f"{user_id()}/media_publish", creation_id=container_id)
    log(f"PUBLISHED media_id={media['id']}")
    return media["id"]


def read_caption(path):
    return Path(path).read_text(encoding="utf-8").strip()


def publish_image(image_url, caption_file):
    c = call("POST", f"{user_id()}/media", image_url=image_url,
             caption=read_caption(caption_file))
    return publish(c["id"])


def publish_carousel(caption_file, urls):
    if not 2 <= len(urls) <= 10:
        sys.exit("Carousel needs 2-10 items")
    children = []
    for u in urls:
        kind = {"video_url": u, "media_type": "VIDEO"} if u.lower().endswith((".mp4", ".mov")) \
            else {"image_url": u}
        child = call("POST", f"{user_id()}/media", is_carousel_item="true", **kind)
        children.append(child["id"])
    for cid in children:
        wait_until_ready(cid)
    c = call("POST", f"{user_id()}/media", media_type="CAROUSEL",
             children=",".join(children), caption=read_caption(caption_file))
    return publish(c["id"])


def publish_reel(video_url, caption_file, cover_url=None):
    params = dict(media_type="REELS", video_url=video_url,
                  caption=read_caption(caption_file), share_to_feed="true")
    if cover_url:
        params["cover_url"] = cover_url
    c = call("POST", f"{user_id()}/media", **params)
    return publish(c["id"])


def publish_story(url):
    kind = {"video_url": url} if url.lower().endswith((".mp4", ".mov")) else {"image_url": url}
    c = call("POST", f"{user_id()}/media", media_type="STORIES", **kind)
    return publish(c["id"])


def refresh_token():
    if LOGIN == "facebook":
        out = call("GET", "oauth/access_token", grant_type="fb_exchange_token",
                   client_id=ENV.get("FB_APP_ID"), client_secret=ENV.get("FB_APP_SECRET"),
                   fb_exchange_token=TOKEN)
    else:
        out = call("GET", "https://graph.instagram.com/refresh_access_token",
                   grant_type="ig_refresh_token")
    text = ENV_PATH.read_text(encoding="utf-8")
    ENV_PATH.write_text(text.replace(TOKEN, out["access_token"]), encoding="utf-8")
    log("Token refreshed")
    return {"refreshed": True, "expires_in_days": out.get("expires_in", 0) // 86400}


def cloudinary(endpoint, files=None, **params):
    cloud = ENV.get("CLOUDINARY_CLOUD_NAME")
    if not cloud:
        sys.exit("Cloudinary keys missing in .env")
    params["timestamp"] = str(int(time.time()))
    to_sign = "&".join(f"{k}={v}" for k, v in sorted(params.items()))
    params["signature"] = hashlib.sha1((to_sign + ENV["CLOUDINARY_API_SECRET"]).encode()).hexdigest()
    params["api_key"] = ENV["CLOUDINARY_API_KEY"]
    r = requests.post(f"https://api.cloudinary.com/v1_1/{cloud}/{endpoint}",
                      data=params, files=files, timeout=300).json()
    if "error" in r:
        log(f"CLOUDINARY ERROR {endpoint}: {r['error']}")
        sys.exit(f"Cloudinary error: {r['error'].get('message')}")
    return r


def upload(path):
    path = Path(path)
    kind = "video" if path.suffix.lower() in (".mp4", ".mov") else "image"
    with path.open("rb") as f:
        r = cloudinary(f"{kind}/upload", files={"file": f}, folder="thaka_hua_desi")
    log(f"UPLOADED {path.name} -> {r['secure_url']}")
    return r["secure_url"]


def post_folder(folder):
    """Publish a queue folder: meta.json {"type": image|carousel|reel, "media": [...], "cover": opt}."""
    folder = Path(folder)
    meta = json.loads((folder / "meta.json").read_text(encoding="utf-8"))
    if meta.get("media_id"):
        sys.exit(f"Already published: {meta['media_id']}")
    caption = folder / "caption.txt"
    urls = [upload(folder / m) for m in meta["media"]]
    if meta["type"] == "image":
        media_id = publish_image(urls[0], caption)
    elif meta["type"] == "carousel":
        media_id = publish_carousel(caption, urls)
    elif meta["type"] == "reel":
        cover = upload(folder / meta["cover"]) if meta.get("cover") else None
        media_id = publish_reel(urls[0], caption, cover)
    else:
        sys.exit(f"Unknown type {meta['type']}")
    meta["media_id"] = media_id
    meta["permalink"] = call("GET", media_id, fields="permalink")["permalink"]
    meta["published_at"] = datetime.now().isoformat(timespec="seconds")
    (folder / "meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    dest = ROOT / "content" / "posted" / folder.name
    folder.rename(dest)
    return {"media_id": media_id, "permalink": meta["permalink"], "moved_to": str(dest)}


def media_insights(media_id):
    base = "reach,likes,comments,shares,saved,total_interactions"
    for metrics in (base + ",views", base):
        params = {"metric": metrics, "access_token": TOKEN}
        r = requests.get(f"{BASE}/{media_id}/insights", params=params, timeout=60).json()
        if "data" in r:
            return {m["name"]: m["values"][0]["value"] for m in r["data"]}
    return {}


def report(limit=30):
    acct = call("GET", user_id(), fields="username,followers_count,media_count")
    media = call("GET", f"{user_id()}/media", limit=limit,
                 fields="id,caption,media_type,permalink,timestamp")["data"]
    for m in media:
        m["caption"] = (m.get("caption") or "").splitlines()[0][:120] if m.get("caption") else ""
        m["insights"] = media_insights(m["id"])
    return {"generated_at": datetime.now().isoformat(timespec="seconds"), "account": acct, "media": media}


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "whoami":
        out = call("GET", user_id(), fields="id,username,name,followers_count,follows_count,media_count")
    elif cmd == "refresh-token":
        out = refresh_token()
    elif cmd == "publish-story":
        out = {"media_id": publish_story(args[0])}
    elif cmd == "hashtag-top":
        facebook_only(cmd)
        tag = call("GET", "ig_hashtag_search", user_id=user_id(), q=args[0])["data"][0]["id"]
        out = call("GET", f"{tag}/top_media", user_id=user_id(), limit=args[1] if len(args) > 1 else 25,
                   fields="id,caption,media_type,permalink,timestamp,like_count,comments_count")
    elif cmd == "discover":
        facebook_only(cmd)
        out = call("GET", user_id(), fields=(
            f"business_discovery.username({args[0]}){{username,name,followers_count,media_count,"
            "media.limit(12){caption,media_type,permalink,timestamp,like_count,comments_count}}"))
    elif cmd == "publish-image":
        out = {"media_id": publish_image(args[0], args[1])}
    elif cmd == "publish-carousel":
        out = {"media_id": publish_carousel(args[0], args[1:])}
    elif cmd == "publish-reel":
        out = {"media_id": publish_reel(args[0], args[1], args[2] if len(args) > 2 else None)}
    elif cmd == "upload":
        out = {"url": upload(args[0])}
    elif cmd == "post":
        out = post_folder(args[0])
    elif cmd == "report":
        out = report(int(args[0]) if args else 30)
    elif cmd == "recent":
        out = call("GET", f"{user_id()}/media", limit=args[0] if args else 10,
                   fields="id,caption,media_type,permalink,timestamp,like_count,comments_count")
    elif cmd == "comments":
        out = call("GET", f"{args[0]}/comments",
                   fields="id,text,username,timestamp,replies{id,text,username}")
    elif cmd == "reply":
        out = call("POST", f"{args[0]}/replies", message=" ".join(args[1:]))
        log(f"REPLIED comment={args[0]}")
    elif cmd == "insights":
        out = call("GET", f"{args[0]}/insights",
                   metric="reach,likes,comments,shares,saved,total_interactions")
    elif cmd == "account-insights":
        out = call("GET", f"{user_id()}/insights", period="day", metric_type="total_value",
                   metric="reach,profile_views,accounts_engaged,total_interactions,follows_and_unfollows")
    else:
        sys.exit(__doc__)
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
