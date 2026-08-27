# -*- coding: utf-8 -*-
"""Single entry point: python3 make.py  →  rebuilds everything."""
import data      # regenerates assets/js/data.js from practices.py + content.py
import build2    # home, practice pages, contact, admin, brand, privacy, 404
import services  # services.html
import casestudies  # work/*.html
import sitemap  # sitemap.xml + robots.txt (last: it walks what was written)
print("\nAll pages built.")
