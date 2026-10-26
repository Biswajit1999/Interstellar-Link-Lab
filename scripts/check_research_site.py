"""Static-site packaging checks for the research observatory.

Pure standard library: verifies local links, local raster assets, PNG
signatures/dimensions, and the absence of SVG image references in landing pages.
This does not replace visual browser/screen-reader testing.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from struct import unpack

ROOT=Path(__file__).resolve().parents[1]
PAGES=[ROOT/"docs/index.html",ROOT/"docs/report.html"]
RASTERS=[ROOT/"docs/images/interstellar_hero.png",
         ROOT/"docs/images/photon_signal_chain.png",
         ROOT/"docs/images/bench_electronics.png"]

class Reader(HTMLParser):
    def __init__(self):
        super().__init__();self.links=[];self.ids=set();self.images=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if "id" in a:self.ids.add(a["id"])
        for attribute in ("href","src"):
            if attribute in a:self.links.append((tag,attribute,a[attribute]))
        if tag=="img":self.images.append(a)

def check():
    errs=[]
    for p in PAGES:
        if not p.exists():errs.append(f"missing {p}");continue
        h=Reader();h.feed(p.read_text(encoding="utf-8"))
        if not h.images:errs.append(f"{p.name} contains no native image assets")
        for tag,attr,url in h.links:
            parts=urlsplit(url)
            if parts.scheme in ("http","https","mailto","tel","data") or url.startswith("//"):
                continue
            if url.startswith("#") and parts.fragment not in h.ids:
                errs.append(f"{p}: missing local fragment {url}");continue
            target=(p.parent/unquote(parts.path)).resolve() if parts.path else p.resolve()
            if not target.is_relative_to(ROOT):
                errs.append(f"{p}: link escapes repo {url}");continue
            if not target.exists():
                errs.append(f"{p}: broken local {tag} {attr}: {url}");continue
            if tag=="img" and target.suffix.lower()==".svg":
                errs.append(f"{p}: SVG image referenced contrary to raster-only policy")
    for p in RASTERS:
        if not p.exists():errs.append(f"missing raster {p}");continue
        with p.open("rb") as f:head=f.read(24)
        if head[:8]!=b"\x89PNG\r\n\x1a\n" or len(head)<24:
            errs.append(f"{p}: not a PNG")
        else:
            w,h=unpack(">II",head[16:24])
            if w<300 or h<200:errs.append(f"{p}: image too small {w}x{h}")
    return errs

if __name__=="__main__":
    problems=check()
    if problems:
        raise SystemExit("\n".join(problems))
    print("Website: two pages, local links and three original PNGs verified.")
