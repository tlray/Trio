#!/usr/bin/env python3
"""Bouwt de voorwaarden-versies tot één vergelijkingsbundel + zes losse PDF's."""
import re, pathlib, html as htmlmod
import markdown
from weasyprint import HTML

BASE = pathlib.Path("/home/user/Trio/onderzoek-namaakbescherming-brightcat")
SRC = BASE / "voorwaarden-versies"
OUT = BASE / "offline"
OUT.mkdir(exist_ok=True)

VERSIES = [
    ("3.01", "Archived", "Gold bij het namaak-incident. Artikel 3.1: alleen “kopiëren of namaken op enigerlei wijze”."),
    ("3.03", "Archived", "Betalingstermijn verduidelijkt; overeenkomst gaat in bij ondertekening in plaats van bij eerste gebruik."),
    ("3.04", "Active", "De versie die nu geldt. Artikel 3.1 uitgebreid met “functionele nabootsing” en “keuzes of elementen”."),
    ("3.05", "Draft", "Verwerkersovereenkomst, omzetdefinitie en overnameregeling toegevoegd."),
    ("3.10", "Draft", "Grote herziening (aansprakelijkheid, vergoeding, wijzigingen, Data Act). Artikel 3.1 bewust opengelaten."),
    ("3.11", "Draft", "Concept uit dit onderzoek: nieuw artikel 3 met boete, volwaardige overstapregeling, afbouwregel."),
]

def slug(text, seen={}):
    s = re.sub(r"[^\w\s-]", "", text.lower()).strip()
    s = re.sub(r"[\s_]+", "-", s)[:60] or "sec"
    n = seen.get(s, 0); seen[s] = n + 1
    return s if n == 0 else f"{s}-{n}"

def convert(md_text):
    return markdown.markdown(md_text, extensions=["tables", "sane_lists", "attr_list"])

def read(v):
    return (SRC / f"Voorwaarden-v{v}.md").read_text(encoding="utf-8")

def split_head(md_text):
    """Scheidt de kop/notitie van de eigenlijke voorwaardentekst."""
    lines = md_text.splitlines()
    body_start = next(i for i, l in enumerate(lines)
                      if l.startswith("De onderstaande voorwaarden"))
    note = "\n".join(l for l in lines[1:body_start] if l.strip())
    return note, "\n".join(lines[body_start:])

def artikel_31(md_text):
    """Haalt de tekst van artikel 3.1 uit een versie (voor de vergelijking)."""
    m = re.search(r"^3\.1 (.+?)(?=\n\n)", md_text, re.S | re.M)
    return m.group(1).replace("\n", " ").strip() if m else "(niet gevonden)"

CSS = """
@page { size: A4; margin: 22mm 20mm 20mm 20mm;
  @bottom-center { content: counter(page); font-family: "Liberation Sans", sans-serif;
                   font-size: 8.5pt; color: #8a8175; }
  @top-right { content: string(chaptertitle); font-family: "Liberation Sans", sans-serif;
               font-size: 8pt; color: #a29889; letter-spacing: .04em; } }
@page cover { margin: 0; @bottom-center { content: none } @top-right { content: none } }

html { font-family: "Bitstream Charter", "DejaVu Serif", Georgia, serif;
       font-size: 10.6pt; line-height: 1.52; color: #23201c; }
body { margin: 0; hyphens: auto; }

.cover { page: cover; height: 297mm; box-sizing: border-box; padding: 42mm 26mm 24mm;
         background: #2c2419; color: #f6f1e6; break-after: page; }
.cover .kicker { font-family: "Liberation Sans", sans-serif; font-size: 9.5pt;
                 letter-spacing: .22em; text-transform: uppercase; color: #c9b98f; }
.cover h1 { font-size: 33pt; line-height: 1.12; margin: 12mm 0 0; font-weight: 600;
            color: #fff; bookmark-label: "Omslag"; }
.cover .sub { font-size: 13pt; line-height: 1.45; margin-top: 8mm; color: #ded4bf; max-width: 118mm; }
.cover .rule { width: 26mm; height: 2.5pt; background: #d8a657; margin: 11mm 0; }
.cover .meta { position: absolute; bottom: 24mm; font-family: "Liberation Sans", sans-serif;
               font-size: 9.5pt; line-height: 1.75; color: #bdb096; }
.cover .meta strong { color: #f6f1e6; font-weight: 600; }

.toc { break-after: page; }
.toc h2 { font-size: 15pt; margin: 0 0 7mm; }
.toc ol { list-style: none; margin: 0; padding: 0; }
.toc a { text-decoration: none; color: #23201c; display: block;
         border-bottom: .4pt dotted #cdc4b6; padding: 2mm 0;
         font-family: "Liberation Sans", sans-serif; font-size: 10.5pt; }
.toc a::after { content: target-counter(attr(href), page); float: right;
                font-size: 9pt; color: #8a8175; font-weight: 400; }
.toc .l1 > a { font-weight: 600; }
.toc .l2 > a { padding-left: 7mm; font-size: 9.4pt; color: #55504a; border-bottom: none;
               font-weight: 400; padding-top: 1mm; padding-bottom: 1mm; }

.chapter { break-before: page; }
.chapter-head { margin-bottom: 9mm; padding-bottom: 5mm; border-bottom: 1.6pt solid #2c2419; }
.chapter-head .num { font-family: "Liberation Sans", sans-serif; font-size: 9pt;
                     letter-spacing: .2em; text-transform: uppercase; color: #b08d3f; }
.chapter-head h1 { string-set: chaptertitle content(); font-size: 21pt; margin: 3mm 0 0;
                   font-weight: 600; }
.chapter-head .sub { font-family: "Liberation Sans", sans-serif; font-size: 9.6pt;
                     color: #6b6459; margin-top: 3mm; line-height: 1.45; }

h2 { font-family: "Liberation Sans", sans-serif; font-size: 12.5pt; font-weight: 600;
     margin: 7mm 0 3mm; break-after: avoid; color: #2c2419; }
h3 { font-family: "Liberation Sans", sans-serif; font-size: 10.6pt; font-weight: 600;
     margin: 6mm 0 2mm; break-after: avoid; color: #40372a;
     border-left: 2.5pt solid #d8a657; padding-left: 3mm; }
p { margin: 0 0 2.4mm; orphans: 2; widows: 2; }
strong { font-weight: 600; }
em { font-style: italic; color: #5c554b; }
.note { font-size: 9.2pt; color: #5c554b; background: #f7f4ec; padding: 3mm 4mm;
        border-left: 2pt solid #cdc4b6; margin-bottom: 6mm; }
.note em { color: inherit; }

table { width: 100%; border-collapse: collapse; margin: 4mm 0 5mm;
        font-family: "Liberation Sans", sans-serif; font-size: 8.6pt; line-height: 1.42; }
thead { display: table-header-group; }
th { text-align: left; background: #2c2419; color: #f6f1e6; font-weight: 600; padding: 2mm 2.4mm; }
td { padding: 1.9mm 2.4mm; border-bottom: .4pt solid #ddd6c8; vertical-align: top; }
tr { break-inside: avoid; }
tbody tr:nth-child(even) { background: #faf8f3; }
th:first-child, td:first-child, th:nth-child(2), td:nth-child(2) { white-space: nowrap; }

.clausule { background: #f7f4ec; border-left: 2.5pt solid #d8a657; padding: 3mm 4mm;
            margin: 0 0 4mm; font-size: 9.6pt; break-inside: avoid; }
.clausule .v { font-family: "Liberation Sans", sans-serif; font-size: 8.5pt; font-weight: 600;
               color: #8a6d24; letter-spacing: .06em; display: block; margin-bottom: 1.5mm; }
hr { border: none; border-top: .5pt solid #ddd6c8; margin: 6mm 0; }

@media screen {
  html { font-size: 17px; line-height: 1.65; background: #f0ece4; }
  body { max-width: 46rem; margin: 0 auto; padding: 0 1.1rem 5rem; background: #fffdf9; }
  .cover { height: auto; padding: 3rem 1.4rem; margin: 0 -1.1rem 2rem; }
  .cover h1 { font-size: 2.1rem; } .cover .meta { position: static; margin-top: 2.4rem; }
  .toc a::after { content: none; }
  .chapter { border-top: 1px solid #e6dfd2; padding-top: 2rem; margin-top: 2.2rem; }
  .chapter-head h1 { font-size: 1.5rem; }
  table { font-size: .8rem; display: block; overflow-x: auto; }
}
"""
# ---------- vergelijkingshoofdstuk ----------
rows = "".join(
    f"<tr><td><strong>v{v}</strong></td><td>{st}</td><td>{htmlmod.escape(d)}</td></tr>"
    for v, st, d in VERSIES)
overzicht = f"""
<h2 id="overzicht">De zes versies naast elkaar</h2>
<p>Dit is de reeks zoals die in de Contract Annexes-database in Notion staat. Elke versie is
hieronder integraal opgenomen, in dezelfde opmaak, zodat verschillen opvallen in plaats van
weg te vallen in verschillende lay-outs.</p>
<table><thead><tr><th>Versie</th><th>Status</th><th>Wat er in deze versie veranderde</th></tr></thead>
<tbody>{rows}</tbody></table>
<h2 id="art31">Artikel 3.1 door de jaren heen</h2>
<p>Dit is het beding waar het onderzoek om draaide. Hieronder staat de kern ervan per versie,
letterlijk overgenomen, zodat je in één oogopslag ziet hoe het zich ontwikkelde — van één zin
in v3.01, via de verbreding in v3.04, naar het gelaagde artikel in v3.11.</p>
"""
for v, _, _ in VERSIES:
    txt = artikel_31(read(v))
    if len(txt) > 900:
        txt = txt[:880].rsplit(" ", 1)[0] + " […]"
    overzicht += (f'<div class="clausule"><span class="v">v{v} — artikel 3.1</span>'
                  f"{htmlmod.escape(txt)}</div>")
overzicht += ("<p><em>De volledige tekst van elk artikel 3 staat in het bijbehorende hoofdstuk. "
              "In v3.11 is artikel 3 uitgegroeid tot zeven leden; hierboven staat alleen 3.1.</em></p>")

toc_entries = [(1, "vergelijking", "Vergelijking"), (2, "overzicht", "De zes versies naast elkaar"),
               (2, "art31", "Artikel 3.1 door de jaren heen")]
chapters = [("vergelijking", "Vergelijking", "Wat er per versie veranderde, en hoe artikel 3.1 zich ontwikkelde", overzicht)]

for v, status, desc in VERSIES:
    md_text = read(v)
    note, body_md = split_head(md_text)
    body = convert(body_md)
    sub = []
    def repl(m, _v=v, _sub=sub):
        lvl, inner = m.group(1), m.group(2)
        plain = re.sub(r"<[^>]+>", "", inner)
        sid = slug(f"{_v}-{plain}")
        if lvl == "3":
            _sub.append((sid, plain))
        return f'<h{lvl} id="{sid}">{inner}</h{lvl}>'
    body = re.sub(r"<h([23])>(.*?)</h\1>", repl, body, flags=re.S)
    note_html = f'<div class="note">{convert(note)}</div>' if note else ""
    cid = f"v{v.replace('.','')}"
    chapters.append((cid, f"Voorwaarden v{v}", f"{status} — {desc}", note_html + body))
    toc_entries.append((1, cid, f"Voorwaarden v{v}"))
    for sid, label in sub:
        toc_entries.append((2, sid, label))

toc_html = '<div class="toc"><h2>Inhoud</h2><ol>' + "".join(
    f'<li class="l{lv}"><a href="#{sid}">{htmlmod.escape(lb)}</a></li>'
    for lv, sid, lb in toc_entries) + "</ol></div>"

chapter_html = "".join(
    f'<section class="chapter" id="{cid}"><header class="chapter-head">'
    f'<div class="num">{"Vergelijking" if i == 0 else "Versie"}</div>'
    f"<h1>{htmlmod.escape(t)}</h1><div class=\"sub\">{htmlmod.escape(s)}</div></header>{b}</section>"
    for i, (cid, t, s, b) in enumerate(chapters))

DOC = f"""<!DOCTYPE html><html lang="nl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Brightmotive Voorwaarden — alle versies</title><style>{CSS}</style></head><body>
<div class="cover">
  <div class="kicker">Brightmotive Services bv · Legal Wiki</div>
  <h1>Voorwaarden<br>alle versies</h1>
  <div class="rule"></div>
  <div class="sub">v3.01, v3.03, v3.04, v3.05, v3.10 en v3.11 integraal naast elkaar,
  met een vergelijking van artikel 3.1 door de jaren heen.</div>
  <div class="meta"><strong>Offline leesversie · 18 augustus 2026</strong><br>
  Overgenomen uit de Contract Annexes-database in Notion<br>
  v3.04 is de actieve versie · v3.11 is het concept uit dit onderzoek</div>
</div>
{toc_html}{chapter_html}</body></html>"""

(OUT / "Brightmotive-Voorwaarden-alle-versies.html").write_text(DOC, encoding="utf-8")
HTML(string=DOC).write_pdf(str(OUT / "Brightmotive-Voorwaarden-alle-versies.pdf"))
print("bundel klaar")

# ---------- losse PDF's per versie ----------
LOS = OUT / "voorwaarden-per-versie"
LOS.mkdir(exist_ok=True)
for v, status, desc in VERSIES:
    note, body_md = split_head(read(v))
    doc = f"""<!DOCTYPE html><html lang="nl"><head><meta charset="utf-8">
<title>Brightmotive Voorwaarden v{v}</title><style>{CSS}</style></head><body>
<section class="chapter" style="break-before:auto"><header class="chapter-head">
<div class="num">Brightmotive Services bv · versie {v} · {status}</div>
<h1>Voorwaarden v{v}</h1></header>
<div class="note">{convert(note)}</div>{convert(body_md)}</section></body></html>"""
    HTML(string=doc).write_pdf(str(LOS / f"Brightmotive-Voorwaarden-v{v}.pdf"))
    print("  losse PDF v" + v)
