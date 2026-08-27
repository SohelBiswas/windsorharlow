# -*- coding: utf-8 -*-
"""sitemap.xml and robots.txt, generated from what the build actually wrote.

Written last, so it can walk public/ rather than keep a second list of pages
that would drift out of step with the real one.
"""
import os, datetime
from shell import SITE
from build import write, OUT

# Pages that exist but should not be indexed. 404 is not a destination, and
# admin is an internal console.
EXCLUDE = {"404.html", "admin.html"}

# Everything else is equal in the eyes of the crawler except the front door
# and the page people arrive at from search.
PRIORITY = {"index.html": "1.0", "services.html": "0.9", "contact.html": "0.8"}


def collect():
    pages = []
    for root, _dirs, files in os.walk(OUT):
        for f in sorted(files):
            if not f.endswith(".html"):
                continue
            rel = os.path.relpath(os.path.join(root, f), OUT).replace(os.sep, "/")
            if rel in EXCLUDE:
                continue
            pages.append(rel)
    # Front door first, then the rest alphabetically — a sitemap is read by
    # machines but reviewed by people.
    pages.sort(key=lambda p: (p != "index.html", p))
    return pages


def build_sitemap(pages, today):
    rows = []
    for rel in pages:
        loc = SITE + "/" + ("" if rel == "index.html" else rel)
        rows.append(
            "  <url>\n"
            f"    <loc>{loc}</loc>\n"
            f"    <lastmod>{today}</lastmod>\n"
            f"    <priority>{PRIORITY.get(rel, '0.7')}</priority>\n"
            "  </url>"
        )
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "\n".join(rows) + "\n</urlset>\n")


def build_robots():
    return (
        "User-agent: *\n"
        "Allow: /\n"
        "\n"
        "# Internal console — not for indexing.\n"
        "Disallow: /admin.html\n"
        "\n"
        f"Sitemap: {SITE}/sitemap.xml\n"
    )


pages = collect()
today = datetime.date.today().isoformat()
write("sitemap.xml", build_sitemap(pages, today))
write("robots.txt", build_robots())
print(f"sitemap: {len(pages)} pages, {len(EXCLUDE)} excluded")
