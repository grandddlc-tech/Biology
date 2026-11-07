#!/usr/bin/env python3
"""Build the offline web assets for the Android app.

- Writes android/app/src/main/assets/index.html from src/planner.html,
  replacing the Google Fonts links with the bundled fonts.
- With --fetch-fonts, downloads the latin Inter font files into
  android/app/src/main/assets/fonts/ (they are committed, so CI does not need this).
"""
import pathlib, re, sys, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
ASSETS = ROOT / "android/app/src/main/assets"
FONTS = ASSETS / "fonts"
CSS_URL = "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA})).read()

def fetch_fonts():
    FONTS.mkdir(parents=True, exist_ok=True)
    css = get(CSS_URL).decode()
    out = []
    seen = {}
    for subset, block in re.findall(r"/\* ([\w-]+) \*/\s*(@font-face \{.*?\})", css, re.S):
        if subset != "latin":
            continue
        fam = re.search(r"font-family: '([^']+)'", block).group(1).replace(" ", "")
        wt = re.search(r"font-weight: (\d+)", block).group(1)
        url = re.search(r"url\((https://[^)]+)\)", block).group(1)
        name = seen.setdefault(url, f"{fam}-{wt}-{subset}.woff2")  # a variable font serves several weights
        if not (FONTS / name).exists():
            (FONTS / name).write_bytes(get(url))
        out.append(block.replace(url, name))
    (FONTS / "fonts.css").write_text("\n".join(out) + "\n")
    print(f"fetched {len(out)} font files")

def build_html():
    src = (ROOT / "src/planner.html").read_text()
    src = re.sub(r'<link rel="preconnect"[^>]*>\n', "", src)
    src = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>',
                 '<link rel="stylesheet" href="fonts/fonts.css">', src)
    assert "googleapis" not in src
    html = ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            '</head><body>\n' + src + '\n</body></html>\n')
    (ASSETS / "index.html").write_text(html)
    print("wrote", ASSETS / "index.html")

if __name__ == "__main__":
    if "--fetch-fonts" in sys.argv:
        fetch_fonts()
    build_html()
