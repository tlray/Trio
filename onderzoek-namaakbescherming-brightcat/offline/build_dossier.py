#!/usr/bin/env python3
"""Bouwt één offline dossier (PDF + standalone HTML) uit de onderzoeksdeliverables."""
import re, pathlib, html as htmlmod
import markdown

SRC = pathlib.Path("/home/user/Trio/onderzoek-namaakbescherming-brightcat")
OUT = pathlib.Path("/home/user/Trio/onderzoek-namaakbescherming-brightcat/offline")
OUT.mkdir(exist_ok=True)

DOCS = [
    ("01-memo-beschermingsstrategie.md", "Memo — beschermingsstrategie", "Het advies: vier pijlers, weging van de twee zienswijzen, grenzen en restrisico's"),
    ("02-tekst-artikel-3-en-boetebeding.md", "Tekstvoorstel artikel 3 + boete", "De concrete clausules met toelichting per lid"),
    ("06-concept-voorwaarden-v3.11.md", "Concept Voorwaarden v3.11", "De volledige voorwaarden met alle wijzigingen ingebouwd"),
    ("03-maatregelenlijst.md", "Maatregelen buiten het contract", "Wat er feitelijk moet gebeuren, geprioriteerd met kosten"),
    ("04-draaiboek-incident.md", "Draaiboek volgend incident", "Eerste 30 dagen, stap voor stap"),
    ("05-bronnen-en-verificatie.md", "Bronnen en verificatie", "Status per bron, correcties op de handover, eindchecklist"),
]

LEESWIJZER = """
## Hoe je dit dossier leest

Dit is het volledige onderzoek in één bestand, bedoeld om offline in één zitting door te nemen.
Alles staat er in leesvolgorde in: eerst het waarom, dan de tekst, dan de uitvoering.

**Als je maar één ding leest:** hoofdstuk 1, paragraaf 1 ("De kern in het kort") en daarna
hoofdstuk 2 (de clausuletekst zelf). Samen zijn dat ongeveer tien minuten.

**De rode draad.** Het auteursrecht laat het nabouwen van functionaliteit grotendeels vrij, dus
het contract moet het werk doen — en dat mag, want buiten de bescherming van het IE-recht geldt
gewoon contractsvrijheid. Het nieuwe artikel 3 zet dat om in zeven losse, elk op zichzelf
houdbare verboden, met een boete die meeschaalt met de omvang van de klant. Daarnaast maken de
bedrijfsgeheimen-maatregelen en de canary-records een volgende zaak bewijsbaar, óók tegen de
externe bouwer die geen klant is.

### Beslispunten voor jou

Dit zijn de plekken waar het onderzoek een keuze openlaat die jij moet maken — handig om
onderweg over na te denken:

1. **Boetehoogte.** Het voorstel is twee keer de jaarvergoeding per overtreding, met een minimum
   van € 25.000 en een plafond van vier keer de jaarvergoeding. Meeschalend is juridisch het
   sterkst, maar je moet het wel aan een grote inkooporganisatie kunnen uitleggen. Er ligt een
   alternatief met vaste bedragen klaar (hoofdstuk 2, invoeringsnotitie 3).
2. **Lengte van artikel 6.** De overstapregeling is nu drie leden in de voorwaarden zelf. Dat is
   Data Act-conform maar maakt artikel 6 langer dan de Fineprint-stijl gewend is. Alternatief:
   een compact 6.4 dat naar een aparte annex "Overstapregeling" verwijst.
3. **Wanneer je klanten migreert.** Aankondiging kan via artikel 7.1 (twee maanden), maar bij
   grote klanten is het sterker om het nieuwe artikel 3 bij de eerstvolgende verlenging expliciet
   te laten aantekenen. Het incident is daarbij je commerciële verhaal.
4. **Volgorde van de maatregelen.** Hoofdstuk 4 zet zes dingen op "deze maand". Realistisch
   gezien is het bedrijfsgeheimenregister het meeste werk en de canary-records het meeste
   rendement per uur.
5. **De freelancer-inventarisatie.** Dit is het enige punt dat een bestaand risico blootlegt in
   plaats van een toekomstig: zonder overdrachtsakten mist Brightmotive vorderingsbevoegdheid op
   onderdelen van de eigen software.

### Eén voorbehoud, vooraf

De onderzoeksomgeving kon de primaire bronnen (rechtspraak.nl, wetten.overheid.nl, EUR-Lex) niet
rechtstreeks bereiken. De Data Act is integraal aan de authentieke verordeningstekst geverifieerd;
al het andere via meerdere onafhankelijke bronnen die elkaar bevestigen. In hoofdstuk 6 staat per
bron wat de status is, plus een lijst van vijf punten die een advocaat éénmaal moet naslaan
voordat dit in een sommatie of processtuk wordt gebruikt.
"""


def slug(text, seen={}):
    s = re.sub(r"[^\w\s-]", "", text.lower()).strip()
    s = re.sub(r"[\s_]+", "-", s)[:60] or "sec"
    n = seen.get(s, 0)
    seen[s] = n + 1
    return s if n == 0 else f"{s}-{n}"


def convert(md_text):
    return markdown.markdown(
        md_text, extensions=["tables", "sane_lists", "attr_list", "md_in_html"]
    )


def add_ids(html_str, chapter_no, toc):
    """Geef h2's een id en verzamel ze voor de inhoudsopgave."""
    def repl(m):
        level, inner = m.group(1), m.group(2)
        plain = re.sub(r"<[^>]+>", "", inner)
        sid = slug(f"{chapter_no}-{plain}")
        if level == "2":
            toc.append((sid, plain))
        return f'<h{level} id="{sid}">{inner}</h{level}>'
    return re.sub(r"<h([23])>(.*?)</h\1>", repl, html_str, flags=re.S)


chapters = []
toc_entries = []  # (level, id, label)

# Hoofdstuk 0: leeswijzer
lw_id = "leeswijzer"
lw_html = convert(LEESWIJZER)
sub = []
lw_html = add_ids(lw_html, "lw", sub)
lw_html = lw_html.replace("<h2>", '<h2 class="chapter-title">', 1)
chapters.append((lw_id, "Leeswijzer", "Hoe je dit dossier leest en welke keuzes openstaan", lw_html))
toc_entries.append((1, lw_id, "Leeswijzer"))
for sid, label in sub:
    toc_entries.append((2, sid, label))

for i, (fname, title, subtitle) in enumerate(DOCS, start=1):
    md_text = (SRC / fname).read_text(encoding="utf-8")
    # eerste H1 weghalen: de hoofdstuktitel komt uit de kop hierboven
    md_text = re.sub(r"^#\s+.*?\n", "", md_text, count=1)
    body = convert(md_text)
    # resterende h1's in de body (zoals "# Voorwaarden") verlagen naar h2,
    # zodat er per hoofdstuk één titel en één bladwijzerniveau is
    body = body.replace("<h1>", "<h2>").replace("</h1>", "</h2>")
    sub = []
    body = add_ids(body, str(i), sub)
    cid = f"h{i}"
    chapters.append((cid, title, subtitle, body))
    toc_entries.append((1, cid, f"{i}. {title}"))
    for sid, label in sub:
        toc_entries.append((2, sid, label))

CSS = """
@page {
  size: A4; margin: 22mm 20mm 20mm 20mm;
  @bottom-center { content: counter(page); font-family: "Liberation Sans", sans-serif;
                   font-size: 8.5pt; color: #8a8175; }
  @top-right { content: string(chaptertitle); font-family: "Liberation Sans", sans-serif;
               font-size: 8pt; color: #a29889; letter-spacing: .04em; }
}
@page cover { margin: 0; @bottom-center { content: none } @top-right { content: none } }
@page :first { @top-right { content: none } }

html { font-family: "Bitstream Charter", "DejaVu Serif", Georgia, serif;
       font-size: 10.6pt; line-height: 1.52; color: #23201c; }
body { margin: 0; hyphens: auto; }

/* ---------- omslag ---------- */
.cover { page: cover; height: 297mm; box-sizing: border-box; padding: 42mm 26mm 24mm;
         background: #1d2b34; color: #f4f0e8; break-after: page; }
.cover .kicker { font-family: "Liberation Sans", sans-serif; font-size: 9.5pt;
                 letter-spacing: .22em; text-transform: uppercase; color: #9dc0bc; }
.cover h1 { font-size: 33pt; line-height: 1.12; margin: 12mm 0 0; font-weight: 600;
            color: #fff; letter-spacing: -.01em; bookmark-label: "Omslag"; }
.cover .sub { font-size: 13pt; line-height: 1.45; margin-top: 8mm; color: #cdd8d6;
              max-width: 118mm; }
.cover .rule { width: 26mm; height: 2.5pt; background: #d8a657; margin: 11mm 0; }
.cover .meta { position: absolute; bottom: 24mm; font-family: "Liberation Sans", sans-serif;
               font-size: 9.5pt; line-height: 1.75; color: #a8bcb9; }
.cover .meta strong { color: #f4f0e8; font-weight: 600; }

/* ---------- inhoudsopgave ---------- */
.toc { break-after: page; }
.toc h2 { font-size: 15pt; margin: 0 0 7mm; }
.toc ol { list-style: none; margin: 0; padding: 0; }
.toc li { margin: 0; }
.toc a { text-decoration: none; color: #23201c; display: block;
         border-bottom: .4pt dotted #cdc4b6; padding: 1.7mm 0; }
.toc a::after { content: target-counter(attr(href), page);
                float: right; font-family: "Liberation Sans", sans-serif;
                font-size: 9pt; color: #8a8175; }
.toc .l1 > a { font-family: "Liberation Sans", sans-serif; font-weight: 600;
               font-size: 10.5pt; margin-top: 3.5mm; border-bottom-color: #a89c88; }
.toc .l2 > a { padding-left: 7mm; font-size: 9.6pt; color: #55504a; border-bottom: none;
               padding-top: .9mm; padding-bottom: .9mm; }

/* ---------- hoofdstukken ---------- */
.chapter { break-before: page; }
.chapter-head { margin-bottom: 9mm; padding-bottom: 5mm; border-bottom: 1.6pt solid #1d2b34; }
.chapter-head .num { font-family: "Liberation Sans", sans-serif; font-size: 9pt;
                     letter-spacing: .2em; text-transform: uppercase; color: #b08d3f; }
.chapter-head h1 { string-set: chaptertitle content(); font-size: 21pt; line-height: 1.18;
                   margin: 3mm 0 0; font-weight: 600; letter-spacing: -.01em; }
.chapter-head .sub { font-family: "Liberation Sans", sans-serif; font-size: 9.8pt;
                     color: #6b6459; margin-top: 3mm; }

h2 { font-family: "Liberation Sans", sans-serif; font-size: 13pt; font-weight: 600;
     margin: 8mm 0 3mm; break-after: avoid; color: #1d2b34; }
h3 { font-family: "Liberation Sans", sans-serif; font-size: 10.8pt; font-weight: 600;
     margin: 6mm 0 2mm; break-after: avoid; color: #33414a; }
h4 { font-family: "Liberation Sans", sans-serif; font-size: 10pt; margin: 5mm 0 1.5mm;
     break-after: avoid; }
p { margin: 0 0 2.6mm; orphans: 2; widows: 2; }
ul, ol { margin: 0 0 3mm; padding-left: 6.5mm; }
li { margin-bottom: 1.4mm; }
strong { font-weight: 600; }
em { font-style: italic; }
a { color: #1d5c6e; text-decoration: none; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: .86em;
       background: #f2efe8; padding: .4mm 1mm; border-radius: 1.5pt; }

/* clausuletekst */
blockquote { margin: 4mm 0; padding: 3.5mm 5mm; background: #f7f4ec;
             border-left: 2.5pt solid #d8a657; }
blockquote p { margin: 0 0 2mm; break-inside: avoid; }
blockquote p:last-child { margin-bottom: 0; }

table { width: 100%; border-collapse: collapse; margin: 4mm 0 5mm;
        font-family: "Liberation Sans", sans-serif; font-size: 8.6pt; line-height: 1.4; }
thead { display: table-header-group; }
th { text-align: left; background: #1d2b34; color: #f4f0e8; font-weight: 600;
     padding: 2mm 2.4mm; border: none; }
td { padding: 1.9mm 2.4mm; border-bottom: .4pt solid #ddd6c8; vertical-align: top; }
tr { break-inside: avoid; }
tbody tr:nth-child(even) { background: #faf8f3; }

hr { border: none; border-top: .5pt solid #ddd6c8; margin: 6mm 0; }

/* ---------- schermweergave (telefoon/laptop, offline in de browser) ---------- */
@media screen {
  html { font-size: 17px; line-height: 1.65; background: #f0ece4; }
  body { max-width: 46rem; margin: 0 auto; padding: 0 1.1rem 5rem;
         background: #fffdf9; box-shadow: 0 0 30px rgba(0,0,0,.07); }
  .cover { height: auto; padding: 3.2rem 1.4rem; margin: 0 -1.1rem 2rem;
           border-radius: 0 0 4px 4px; }
  .cover h1 { font-size: 2.1rem; }
  .cover .sub { font-size: 1rem; max-width: none; }
  .cover .meta { position: static; margin-top: 2.6rem; font-size: .85rem; }
  .toc { padding-top: .5rem; }
  .toc a::after { content: none; }
  .chapter { border-top: 1px solid #e6dfd2; padding-top: 2.2rem; margin-top: 2.4rem; }
  .chapter-head h1 { font-size: 1.55rem; }
  h2 { font-size: 1.2rem; margin: 2rem 0 .6rem; }
  h3 { font-size: 1.03rem; margin: 1.5rem 0 .4rem; }
  p { margin: 0 0 .85rem; }
  blockquote { margin: 1.1rem 0; padding: .9rem 1.1rem; border-radius: 3px; }
  table { font-size: .8rem; display: block; overflow-x: auto; white-space: normal; }
  a { color: #14606f; }
}
"""

def render_toc():
    parts = ['<div class="toc"><h2>Inhoud</h2><ol>']
    for level, sid, label in toc_entries:
        parts.append(f'<li class="l{level}"><a href="#{sid}">{htmlmod.escape(label)}</a></li>')
    parts.append("</ol></div>")
    return "".join(parts)

chapter_html = []
for idx, (cid, title, subtitle, body) in enumerate(chapters):
    num = "Leeswijzer" if idx == 0 else f"Hoofdstuk {idx}"
    chapter_html.append(
        f'<section class="chapter" id="{cid}">'
        f'<header class="chapter-head"><div class="num">{num}</div>'
        f"<h1>{htmlmod.escape(title)}</h1>"
        f'<div class="sub">{htmlmod.escape(subtitle)}</div></header>'
        f"{body}</section>"
    )

DOC = f"""<!DOCTYPE html>
<html lang="nl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Namaakbescherming BrightCat — onderzoeksdossier</title>
<style>{CSS}</style></head><body>
<div class="cover">
  <div class="kicker">Brightmotive Services bv · vertrouwelijk</div>
  <h1>Namaak&shy;bescherming<br>BrightCat</h1>
  <div class="rule"></div>
  <div class="sub">Onafhankelijk juridisch onderzoek naar de sterkst houdbare bescherming
  tegen het namaken van BrightCat door (ex-)klanten — met tekstvoorstel, maatregelen en draaiboek.</div>
  <div class="meta">
    <strong>Onderzoeksdossier · 18 augustus 2026</strong><br>
    Zeven parallelle onderzoekssporen met bronverificatie<br>
    Zes documenten · offline leesversie
  </div>
</div>
{render_toc()}
{''.join(chapter_html)}
</body></html>"""

html_path = OUT / "Namaakbescherming-BrightCat-dossier.html"
html_path.write_text(DOC, encoding="utf-8")

from weasyprint import HTML
pdf_path = OUT / "Namaakbescherming-BrightCat-dossier.pdf"
HTML(string=DOC, base_url=str(OUT)).write_pdf(str(pdf_path))
print("HTML:", html_path, html_path.stat().st_size // 1024, "kB")
print("PDF :", pdf_path, pdf_path.stat().st_size // 1024, "kB")
