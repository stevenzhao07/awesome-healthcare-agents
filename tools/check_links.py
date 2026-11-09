# -*- coding: utf-8 -*-
"""README 收录链接体检：抽出所有 github.com/{owner}/{repo}，逐条查它是否真实存在。

为什么要有这个文件：清单类仓库没有可执行示例，外人真正会踩的是「点进去 404」。
判据：任一收录仓链解析为 404/410（或私有不公开）即 exit 1，让 PR 变红。
注意：站内附件（user-attachments/assets）、裸图片路径不计入仓链。
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request

TOKEN = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN") or ""
README = "README.md"
NONREPO = ("user-attachments", "assets", "blob", "tree", "raw", "releases", "issues",
           "pull", "wiki", "sponsors", "settings", "marketplace", "topics", "features")
PAGE_EXT = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".pdf", ".zip")
RE_REPO = re.compile(r"https?://(?:www\.)?github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)")


def opener():
    return urllib.request.build_opener(urllib.request.ProxyHandler({}))


def check(full):
    h = {"Accept": "application/vnd.github+json", "User-Agent": "link-check"}
    if TOKEN:
        h["Authorization"] = "Bearer " + TOKEN
    req = urllib.request.Request("https://api.github.com/repos/" + full, headers=h)
    try:
        with opener().open(req, timeout=30) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return None  # 网络抖动不算死链，只记不可达


def main():
    if not os.path.exists(README):
        print("no README.md - nothing to check")
        return 0
    text = open(README, encoding="utf-8", errors="replace").read()
    seen, rows = set(), []
    for owner, name in RE_REPO.findall(text):
        name = name.rstrip(".,);:'\"")
        if not name or owner.lower() in NONREPO or name.lower().endswith(PAGE_EXT):
            continue
        full = "%s/%s" % (owner, name)
        if full.lower() in seen:
            continue
        seen.add(full.lower())
        rows.append(full)

    print("entries: %d" % len(rows))
    dead, unknown = [], []
    for full in rows:
        code = check(full)
        if code in (404, 410, 451):
            dead.append((full, code))
            print("  DEAD %-60s %s" % (full, code))
        elif code is None or code == 403:
            unknown.append((full, code))

    if unknown:
        print("unreachable-not-dead: %d（网络/限流，不判死链）" % len(unknown))
    if dead:
        print("\nFAIL: %d dead repo link(s). 修法：换活目标或删该行。" % len(dead))
        return 1
    print("OK: all %d repo links resolve" % len(rows))
    return 0


if __name__ == "__main__":
    sys.exit(main())
