"""Regenerate the auto-maintained blocks in README.md.

Each block sits between <!-- BEGIN:name --> and <!-- END:name --> markers.
Everything outside the markers is hand-written and left alone.
Stdlib only; GITHUB_TOKEN is optional (raises the API rate limit).
"""
import json
import os
import re
import sys
import urllib.request
from html import unescape
from pathlib import Path

USER = "oaustegard"
FEED = "https://muninn.austegard.com/feed.xml"
README = Path(__file__).resolve().parent.parent / "README.md"

# Repos that are scaffolding, mirrors or test beds rather than work to show.
SKIP = {
    USER, "vanilla-ccotw", "container-layer-test", "blog-references",
    "jina-v5-nano-mirror",
}
SKIP_PREFIXES = ("PP-OCR", "fork-", "fork_")


def fetch(url, accept="application/vnd.github+json"):
    req = urllib.request.Request(url, headers={"User-Agent": USER, "Accept": accept})
    token = os.environ.get("GITHUB_TOKEN")
    if token and url.startswith("https://api.github.com/"):
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode()


def recent_repos(n=8):
    repos = json.loads(fetch(
        f"https://api.github.com/users/{USER}/repos?type=owner&sort=pushed&per_page=50"))
    rows = []
    for r in repos:
        name = r["name"]
        if (r["fork"] or r["archived"] or r["private"] or name in SKIP
                or name.startswith(SKIP_PREFIXES)):
            continue
        desc = (r["description"] or "").strip()
        if desc.startswith("DEPRECATED"):
            continue
        line = f"- **[{name}]({r['html_url']})**"
        if desc:
            line += f" — {desc}"
        rows.append(line + f" <sub>updated {r['pushed_at'][:10]}</sub>")
        if len(rows) == n:
            break
    return "\n".join(rows)


def recent_posts(n=6):
    xml = fetch(FEED, accept="application/atom+xml")
    rows = []
    for entry in re.findall(r"<entry>(.*?)</entry>", xml, re.S)[:n]:
        title = re.search(r"<title[^>]*>(.*?)</title>", entry, re.S)
        link = re.search(r'<link[^>]*href="([^"]+)"', entry)
        date = re.search(r"<(?:published|updated)>([^<]{10})", entry)
        if not (title and link):
            continue
        day = f" <sub>{date.group(1)}</sub>" if date else ""
        rows.append(f"- [{unescape(title.group(1)).strip()}]({link.group(1)}){day}")
    return "\n".join(rows)


def replace_block(text, name, body):
    pattern = re.compile(rf"(<!-- BEGIN:{name} -->).*?(<!-- END:{name} -->)", re.S)
    if not pattern.search(text):
        sys.exit(f"README.md has no {name} block")
    return pattern.sub(lambda m: f"{m.group(1)}\n{body}\n{m.group(2)}", text)


def main():
    text = README.read_text()
    new = replace_block(text, "recent-repos", recent_repos())
    new = replace_block(new, "recent-posts", recent_posts())
    if new != text:
        README.write_text(new)
        print("README.md updated")
    else:
        print("README.md unchanged")


if __name__ == "__main__":
    main()
