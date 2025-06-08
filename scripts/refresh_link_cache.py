#!/usr/bin/env python3
"""Refresh docs/link_cache.txt with current HTTP status codes."""
import os
import re
import urllib.request
import urllib.error

CACHE_FILE = os.path.join('docs', 'link_cache.txt')
ROOT = os.path.join('docs', 'external')

def collect_links():
    links = set()
    for dirpath, _, filenames in os.walk(ROOT):
        for name in filenames:
            if not name.endswith('.md'):
                continue
            with open(os.path.join(dirpath, name), 'r', encoding='utf-8') as f:
                for match in re.findall(r'https?://[^\s)"\',]+', f.read()):
                    links.add(match)
    return sorted(links)

def check_link(url: str) -> int:
    """Return the HTTP status code for ``url``.

    First issues a ``HEAD`` request. Some servers respond with errors for ``HEAD``
    requests, so if the status code is 403, 404 or 405 a ``GET`` request is
    retried using a standard ``User-Agent`` header.
    """

    request = urllib.request.Request(url, method="HEAD")
    try:
        with urllib.request.urlopen(request, timeout=10) as resp:
            return resp.getcode()
    except urllib.error.HTTPError as e:
        code = e.code
        if code in {403, 404, 405}:
            get_request = urllib.request.Request(
                url,
                method="GET",
                headers={"User-Agent": "Mozilla/5.0"},
            )
            try:
                with urllib.request.urlopen(get_request, timeout=10) as resp:
                    return resp.getcode()
            except urllib.error.HTTPError as e2:
                return e2.code
            except Exception:
                return 0
        return code
    except Exception:
        return 0

def main() -> None:
    links = collect_links()
    with open(CACHE_FILE, 'w', encoding='utf-8') as cache:
        for url in links:
            status = check_link(url)
            cache.write(f"{url} {status}\n")
    print(f"Updated {CACHE_FILE} with {len(links)} entries")

if __name__ == '__main__':
    main()
