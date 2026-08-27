#!/usr/bin/env python3
"""
Render one Open Graph card per page, so a link to the mobile practice shows
the mobile practice rather than the homepage headline.

    pip install playwright && playwright install chromium
    python3 tools/fetch-fonts.py     # run this FIRST — see below
    python3 tools/make-og.py
    python3 build/make.py

Run it from the project root. Writes 1200x630 JPEGs into
public/assets/brand/og/, named after each page. The build picks them up
automatically; pages without one fall back to the shared og.jpg.

Run fetch-fonts.py first and it is not optional in spirit: these cards are
mostly type. Without the real Newsreader and IBM Plex Mono the renderer
substitutes whatever the machine has, and the cards go out in the wrong
typeface — which is worse than one generic card, because it is wrong in
public, on every share.
"""
import os, re, sys, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB = os.path.join(ROOT, "public")
OUT = os.path.join(PUB, "assets", "brand", "og")

TEMPLATE = """<!doctype html><meta charset="utf-8">
<link rel="stylesheet" href="file://{css}">
<style>
  html,body{{margin:0;padding:0}}
  .og{{width:1200px;height:630px;position:relative;overflow:hidden;
      background:#04212C;color:#EAF2F4;
      font-family:"Archivo","Helvetica Neue",Arial,sans-serif}}
  .og::before{{content:"";position:absolute;inset:0;
      background:radial-gradient(62% 150% at 10% 8%,rgba(0,121,202,.42),transparent 62%),
                 radial-gradient(48% 130% at 78% 96%,rgba(38,199,143,.26),transparent 66%),
                 radial-gradient(40% 120% at 96% 6%,rgba(31,166,184,.20),transparent 70%)}}
  .og::after{{content:"";position:absolute;inset:0;
      background-image:radial-gradient(rgba(234,242,244,.055) 1px,transparent 1px);
      background-size:6px 6px;
      -webkit-mask-image:linear-gradient(100deg,transparent 36%,#000 100%)}}
  .in{{position:relative;z-index:2;padding:64px 72px;height:100%;
      display:flex;flex-direction:column}}
  .logo{{height:44px;width:auto;display:block}}
  .eyebrow{{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:15px;
      letter-spacing:.24em;text-transform:uppercase;color:#79C6F4;
      margin:44px 0 22px;display:flex;align-items:center;gap:16px}}
  .eyebrow i{{display:block;height:1px;flex:1;max-width:120px;
      background:linear-gradient(90deg,#0079CA,#26C78F)}}
  h1{{font-family:"Newsreader",Georgia,serif;font-weight:300;font-size:{size}px;
      line-height:1.08;letter-spacing:-.022em;margin:0;max-width:20ch}}
  h1 em{{font-style:italic;color:#6FEDC4}}
  .foot{{margin-top:auto;font-family:"IBM Plex Mono",ui-monospace,monospace;
      font-size:14px;letter-spacing:.16em;text-transform:uppercase;color:#7194A0}}
  .edge{{position:absolute;left:0;right:0;bottom:0;height:5px;z-index:3;
      background:linear-gradient(90deg,#0079CA,#1FA6B8 52%,#26C78F)}}
</style>
<div class="og">
  <div class="in">
    <img class="logo" src="file://{logo}" alt="">
    <p class="eyebrow">{eyebrow}<i></i></p>
    <h1>{headline}</h1>
    <p class="foot">{foot}</p>
  </div>
  <div class="edge"></div>
</div>"""


def cards():
    """Take the eyebrow and h1 each page already has, rather than inventing
    a second set of titles that would drift from the pages themselves."""
    out = []
    for root, _d, files in os.walk(PUB):
        for f in sorted(files):
            if not f.endswith(".html"):
                continue
            rel = os.path.relpath(os.path.join(root, f), PUB).replace(os.sep, "/")
            if rel in ("404.html", "admin.html"):
                continue
            src = open(os.path.join(root, f), encoding="utf-8").read()
            m = re.search(r"<h1[^>]*>(.*?)</h1>", src, re.S)
            if not m:
                continue
            headline = re.sub(r"<(?!/?em\b)[^>]+>", "", m.group(1))
            headline = re.sub(r"\s+", " ", headline).strip()
            e = re.search(r'<p class="(?:eyebrow|crumb)[^"]*"[^>]*>(.*?)</p>', src, re.S)
            eyebrow = re.sub(r"<[^>]+>", " ", e.group(1)) if e else "Windsor Harlow"
            eyebrow = re.sub(r"\s+", " ", eyebrow).strip(" /·")
            out.append((rel, eyebrow, headline))
    return out


def main():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit("pip install playwright && playwright install chromium")

    css = os.path.join(PUB, "assets", "css", "wh.css")
    logo = os.path.join(PUB, "assets", "brand", "logo-reverse.svg")
    os.makedirs(OUT, exist_ok=True)
    rows = cards()

    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1200, "height": 630},
                        device_scale_factor=1)
        for rel, eyebrow, headline in rows:
            plain = re.sub(r"<[^>]+>", "", headline)
            size = 62 if len(plain) < 52 else (54 if len(plain) < 78 else 46)
            pg.set_content(TEMPLATE.format(
                css=css, logo=logo, size=size,
                eyebrow=html.escape(eyebrow), headline=headline,
                foot="AI &amp; ML / Salesforce / Cloud / DevOps / Web / Mobile"))
            pg.wait_for_timeout(400)
            try:
                pg.wait_for_function("document.fonts.ready.then(()=>true)")
            except Exception:
                pass
            name = rel.replace("/", "-").replace(".html", "") + ".jpg"
            pg.screenshot(path=os.path.join(OUT, name), type="jpeg", quality=88)
            print(f"  {name:38s} {headline[:44]}")
        b.close()

    print(f"\n{len(rows)} cards → public/assets/brand/og/")
    print("Now run:  python3 build/make.py")


if __name__ == "__main__":
    main()
