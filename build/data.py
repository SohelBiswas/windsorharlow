# -*- coding: utf-8 -*-
"""Generates public/assets/js/data.js from the Python sources.

Why this exists: the capability tables were previously written twice — once in
practices.py for the practice pages, once by hand in data.js for the home-page
explorer. They drifted, so the same practice showed different capabilities
depending on which page you were on. Now there is one source of truth
(practices.py + content.py) and data.js is generated from it.

Do not edit public/assets/js/data.js directly — it is overwritten on build.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from practices import P
from content import INDEX, WORK, PRACTICE_META, PRACTICE_ORDER

OUT = os.path.join(os.path.dirname(__file__), "..", "public",
                   "assets", "js", "data.js")


def strip_tags(s):
    """practices.py stores headlines with <em> emphasis; JS wants plain text."""
    import re
    return re.sub(r"<[^>]+>", "", s)


def unescape(s):
    """HTML entities are correct in markup but wrong inside a JS string."""
    return (s.replace("&amp;", "&").replace("&mdash;", "\u2014")
             .replace("&ndash;", "\u2013").replace("&hellip;", "\u2026")
             .replace("&middot;", "\u00b7").replace("&nbsp;", " "))


def js(value):
    return json.dumps(value, ensure_ascii=False)


def build():
    order = {pid: i for i, pid in enumerate(PRACTICE_ORDER)}
    practices = sorted(P, key=lambda p: order.get(p["id"], 99))

    out = ["/* GENERATED FILE — do not edit.",
           " * Rebuild with:  cd build && python3 make.py",
           " * Sources: build/practices.py (capabilities) and build/content.py",
           " * (index, blurbs, order, placeholder case studies).",
           " */",
           "",
           "const PRACTICES = ["]

    for p in practices:
        meta = PRACTICE_META.get(p["id"], {})
        out.append("  {")
        out.append(f'    id: {js(p["id"])}, short: {js(unescape(p["short"]))},')
        out.append(f'    label: {js(unescape(p["label"]))},')
        out.append(f'    title: {js(unescape(strip_tags(p["h1"])))},')
        out.append(f'    lede: {js(unescape(p["lede"]))},')
        out.append(f'    href: {js(meta.get("href", ""))},')
        out.append(f'    lead: {"true" if meta.get("lead") else "false"},')
        out.append(f'    blurb: {js(unescape(meta.get("blurb", "")))},')
        out.append("    stack: [")
        for k, v in p["stack"]:
            out.append(f"      [{js(unescape(k))}, {js(unescape(v))}],")
        out.append("    ],")
        out.append("  },")
    out += ["];", ""]

    out.append("const INDEX = [")
    for name, cat in INDEX:
        out.append(f"  [{js(name)}, {js(cat)}],")
    out += ["];", ""]

    out.append("const WORK = [")
    for w in WORK:
        out.append("  {")
        for key in ("tag", "cat", "title", "body", "foot"):
            out.append(f"    {key}: {js(unescape(w[key]))},")
        if w.get("href"):
            out.append(f'    href: {js(w["href"])},')
        out.append("  },")
    out += ["];", ""]

    text = "\n".join(out)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(text)

    leads = [p["id"] for p in practices if PRACTICE_META.get(p["id"], {}).get("lead")]
    print(f"  wrote assets/js/data.js  ({len(text)//1024} KB)")
    print(f"    {len(practices)} practices, order: {', '.join(p['id'] for p in practices)}")
    print(f"    lead: {', '.join(leads)}")
    print(f"    {len(INDEX)} index entries, {len(WORK)} placeholder case studies")


build()
