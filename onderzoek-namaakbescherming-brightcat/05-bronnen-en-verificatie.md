# Deliverable 5 — Bronnen, verificatiestatus en correcties

## Verificatiemethode en één belangrijk voorbehoud

De opdracht eiste verificatie van alle rechtspraak aan de bron. De onderzoeksomgeving bleek echter **rechtstreekse toegang tot de primaire bronnen te blokkeren** (uitgaand verkeer naar wetten.overheid.nl, uitspraken.rechtspraak.nl, data.rechtspraak.nl, eur-lex.europa.eu en curia.europa.eu werd door de netwerkproxy geweigerd; meermaals getest in alle zeven sporen). Daarom is als volgt geverifieerd:

- **Data Act (Verordening 2023/2854):** integraal geverifieerd op de **authentieke Engelse verordeningstekst** (Publicatiebureau-corpus, CELEX 32023R2854) — de sterkste verificatie in dit onderzoek; alle EU-taalversies zijn gelijkelijk authentiek. Alleen de letterlijke Nederlandse bewoordingen zijn via secundaire bronnen gecorroboreerd.
- **Alle overige wetteksten en uitspraken:** geverifieerd via **meerdere onafhankelijke, convergerende secundaire bronnen** (zoeksnippets van rechtspraak.nl/EUR-Lex zelf, Boek9/IEPT, IE-Forum, Cassatieblog, NJ-vindplaatsen, kamerstukken, ACM-publicaties, gerenommeerde kantooranalyses). ECLI's, data, partijen en kernoverwegingen zijn consistent over die bronnen bevestigd.

**Consequentie:** de kans op materiële afwijking is klein (kernnormen worden overal gelijkluidend geciteerd), maar **vóór gebruik in een sommatie of processtuk moet een advocaat de hieronder gemarkeerde punten éénmaal op de primaire bron naslaan.** Niets in dit onderzoek berust op ongeverifieerde trainingskennis zonder dat dit expliciet is gemarkeerd.

## Correcties op de handover / het eerdere advies

1. **Onjuist ECLI in de handover:** Lundiform/Mexx = HR 5 april 2013, **ECLI:NL:HR:2013:BY8101** (niet BZ3749; dat is HR 14 juni 2013, Koersplan/Aegon). Dit ECLI stond ook in het eerdere AV-reviewmateriaal.
2. **Nuance op het eerdere advies over de VBER:** "postcontractueel max. 1 jaar onder voorwaarden" is onvolledig — art. 5 lid 3 VBER eist óók beperking tot de fysieke "ruimten en terreinen" van de afnemer, wat voor SaaS onvervulbaar is. Een postcontractueel exploitatieverbod is dus nooit groepsvrijgesteld; alleen het gebruiksverbod van **niet-openbare knowhow** mag (dan wel onbeperkt in tijd). De voorgestelde tekst is daarop gebouwd.
3. **Nuance op "deels nietig wegens dwingende gebruikersrechten":** die rechten gelden voor de "rechtmatige verkrijger/gebruiker van een exemplaar/kopie". Bij pure SaaS (alleen browsertoegang) is naar heersende leer géén sprake van zo'n verkrijger, zodat de nietigheid waarschijnlijk niet eens speelt — maar dit is niet uitgeprocedeerd; de carve-out in art. 3.6 vangt beide scenario's af.
4. **Bevestigd uit het eerdere advies:** SAS Institute, Top System, Ryanair/PR Aviation, All Round/Simstars en de inschatting dat slaafse nabootsing voor B2B-platform-UI zelden haalbaar is, kloppen allemaal (ECLI's geverifieerd zoals hieronder).
5. **Nieuw t.o.v. beide eerdere adviezen:** het bewijsrecht is per 1-1-2025 herzien (843a Rv vervangen door art. 194 e.v. Rv; bewijsbeslag gecodificeerd; nieuw art. 207 Rv), en de Data Act stelt sinds 12-9-2025 eisen die het huidige art. 6.4 niet haalt.

## Kernbronnen per onderwerp (met verificatiestatus)

Legenda: ✅ = meervoudig geverifieerd via convergerende bronnen (of, bij de Data Act, integrale authentieke tekst); ⚠️ = kern bevestigd, detail (r.o.-nummer, dictum of exact bedrag) primair nalopen; ❌ = niet geverifieerd, niet op steunen.

### EU-rechtspraak (software/IE/data)
| Bron | Kern | Status |
|---|---|---|
| HvJ EU 2-5-2012, C-406/10, ECLI:EU:C:2012:259 (SAS Institute) | Functionaliteit, programmeertaal, bestandsformaten niet beschermd; verbod op observeren/bestuderen/testen tijdens rechtmatig gebruik nietig | ✅ |
| HvJ EU 22-12-2010, C-393/09, ECLI:EU:C:2010:816 (BSA) | GUI geen computerprogramma; mogelijk wel "gewoon" werk | ✅ |
| HvJ EU 6-10-2021, C-13/20, ECLI:EU:C:2021:811 (Top System) | Decompilatie voor foutverbetering niet volledig uitsluitbaar; modaliteiten wel regelbaar | ✅ (r.o. 66-67 ⚠️) |
| HvJ EU 15-1-2015, C-30/14, ECLI:EU:C:2015:10 (Ryanair/PR Aviation) | Onbeschermde databank → volledige contractsvrijheid; HR-vervolg ECLI:NL:HR:2016:390 | ✅ |
| HvJ EU 9-11-2004, C-203/02 (British Horseracing) | Investering in creëren telt niet mee voor databankrecht | ✅ |
| HvJ EU 3-6-2021, C-762/19, ECLI:EU:C:2021:434 (CV-Online/Melons) | Verbodsrecht bij afbreuk aan terugverdienmogelijkheid investering | ✅ |
| HvJ EU 19-12-2013, C-202/12, ECLI:EU:C:2013:850 (Innoweb/Gaspedaal) | Dedicated metazoekmachine = hergebruik | ✅ |
| HvJ EU 5-3-2009, C-545/07 (Apis/Lakorda) | Meegekopieerde kenmerken (vgl. canaries) als bewijs van extractie | ✅ |
| HvJ EU 17-10-2024, C-159/23, ECLI:EU:C:2024:887 (Sony/Datel) | Runtime-variabelen buiten softwarebescherming | ⚠️ |
| HvJ Remia (42/84) en Pronuptia (161/84) | Nevenrestrictie-leer: knowhowbescherming buiten kartelverbod | ✅ (r.o.-nrs ⚠️) |
| Infopaq C-5/08; Cofemel C-683/17 | Werkbegrip: eigen intellectuele schepping | ✅ |

### Nederlandse rechtspraak
| Bron | Kern | Status |
|---|---|---|
| HR 5-4-2013, ECLI:NL:HR:2013:BY8101 (Lundiform/Mexx) | Uitleg commerciële contracten; taalkundige betekenis geen automatisme | ✅ |
| HR 20-2-2004, ECLI:NL:HR:2004:AO1427 (DSM/Fox) | Glijdende schaal subjectieve/objectieve uitleg | ✅ |
| HR 13-3-1981, ECLI:NL:HR:1981:AG4158 (Haviltex) | Uitlegmaatstaf | ✅ |
| HR 19-1-2018, ECLI:NL:HR:2018:56 (Diplomatic Card/Forax) | Functionele specs/nabouw functionaliteit auteursrechtelijk vrij | ✅ |
| HR 19-5-2017, ECLI:NL:HR:2017:938 (All Round/Simstars) | Slaafse nabootsing: eigen gezicht + nodeloze verwarring | ✅ |
| HR 27-4-2007, ECLI:NL:HR:2007:AZ6638 (Intrahof/Bart Smit) | Matigingsmaatstaf boetes: "buitensporig en daarom onaanvaardbaar" | ✅ (r.o. 5.3 ⚠️) |
| HR 16-2-2018, ECLI:NL:HR:2018:207 (Turan/Easystaff) | Forse matiging eenheidsboete B2B in stand | ✅ |
| HR 13-7-2012, ECLI:NL:HR:2012:BW4986 | Hoedanigheid partijen = gezichtspunt bij matiging | ✅ |
| HR 20-12-2013, ECLI:NL:HR:2013:2123 (BP/Benschop) | Geen conversie van met art. 6 Mw strijdig beding | ✅ |
| HR 21-12-2012, ECLI:NL:HR:2012:BX0345 (ANVR/IATA) | Zware stelplicht bij beroep op mededingingsrecht | ✅ |
| HR 13-9-2013, ECLI:NL:HR:2013:BZ9958 (Molenbeek Invest) | Bewijsbeslag buiten IE-zaken (per 2025 gecodificeerd) | ✅ |
| HR 18-4-2014, ECLI:NL:HR:2014:942 | Onrechtmatig verkregen bewijs civiel in beginsel toelaatbaar | ✅ |
| HR 1-5-2020, ECLI:NL:HR:2020:830 (Heraeus/Biomet) | Art. 1019ie Rv proceskosten discretionair | ✅ |
| HR 14-4-2000, ECLI:NL:HR:2000:AA5519 (HBS/Danestyle) | Verhouding schadevergoeding/winstafdracht | ⚠️ |
| Hof Den Bosch 9-7-2013, ECLI:NL:GHSHE:2013:2993 (Betsoft) | Look & feel afgewezen; wapperverbod bij te brede claim | ✅ |
| Vzr. Rb. Overijssel 4-6-2020, ECLI:NL:RBOVE:2020:1932 (Vendic) | Webshopvormgeving: onvoldoende eigen karakter | ✅ |
| Rb. Midden-NL 31-7-2019, ECLI:NL:RBMNE:2019:3649 | Letterlijk overgenomen teksten wél inbreuk | ⚠️ |
| Rb. Midden-NL 8-8-2018, ECLI:NL:RBMNE:2018:3715 (Wärtsilä) | Inconsequente geheimhouding fataal voor Wbb-claim | ✅ |
| Rb. Den Haag 20-3-2019, ECLI:NL:RBDHA:2019:2729 (Future Crops) | NDA + communicatie + compartimentering + controle = voldoende maatregelen | ✅ |
| Rb. Noord-Holland 12-12-2022, ECLI:NL:RBNHO:2022:10719 (Locus/HAI) | (Semi)publiek reconstrueerbaar = geen geheim | ✅ |
| Rb. Midden-NL 30-10-2024, ECLI:NL:RBMNE:2024:7789 | Handelswaarde substantiëren | ✅ |
| Hof Den Haag 8-4-2025, ECLI:NL:GHDHA:2025:498 (Corrosion) | Geheimen precies afbakenen; alleen de houder vordert | ✅ |
| Hof Arnhem-Leeuwarden 2025, ECLI:NL:GHARL:2025:7218 | Samenstel/ordening kan geheim zijn | ✅ |
| Rb. Amsterdam 11-6-2026, ECLI:NL:RBAMS:2026:5976 (TMU) | Database als geheim; staken + opgave omzet/winst | ⚠️ |
| Hof Arnhem-Leeuwarden 26-4-2016, ECLI:NL:GHARL:2016:3399 | B2B-geheimhoudingsboete: matiging verworpen | ⚠️ (toegewezen bedrag onzeker) |
| Hof Arnhem-Leeuwarden 2024, ECLI:NL:GHARL:2024:2397 | Boetes fors gematigd; dagboetes geschrapt | ✅ |
| Rb. Midden-NL 17-6-2026, ECLI:NL:RBMNE:2026:3733 | € 2 mln NDA-boetes integraal afgewezen (beding te ruim/ongekoppeld) | ✅ |
| Rb. Midden-NL 19-7-2023, ECLI:NL:RBMNE:2023:2822 | Boetestructuur bevestigd; **dictum onzeker** | ⚠️ |
| HR 27-6-1986 (Decca, NJ 1987/191); HR 23-10-1987 (KNVB/NOS, NJ 1988/310) | Prestatiebescherming: hoge lat (pre-ECLI) | ✅ via NJ-vindplaatsen |
| "Siemens-licentiezaak 2016" | Illustratief; **geen ECLI gevonden** | ❌ niet gebruiken |

### Wet- en regelgeving
| Bron | Kern | Status |
|---|---|---|
| Art. 45i–45n Auteurswet | Dwingend: 45j slotzin (laden/foutverbetering), 45k (reservekopie), 45l (observeren/bestuderen/testen), 45m (decompilatie); gekoppeld aan "exemplaar" | ✅ (45k/45m leden 2-3 ⚠️) |
| Richtlijn 2009/24/EG art. 5, 6, 8 | Art. 8 tweede alinea: strijdige bedingen nietig | ✅ |
| Databankenwet art. 1, 2, 3; art. 24a Aw | Sui generis recht; dwingende gebruikersrechten (sanctie nietig/vernietigbaar: onuitgemaakt) | ✅/⚠️ |
| Wet bescherming bedrijfsgeheimen art. 1, 2, 3, 5–9 | Definitie, onrechtmatigheid, derdenwerking, maatregelen | ✅ |
| Art. 1019–1019ie Rv | IE-handhaving; Wbb-titel 15A; 1019h/1019ie kosten | ✅ (actuele tekst 1019a ⚠️) |
| **Art. 194–207 Rv (nieuw bewijsrecht per 1-1-2025**, wet 35498**)** | Inzage 194–195a; voorlopige verrichtingen 196–204; bewijsbeslag 205–206; pv van constateringen 207 | ✅ hoofdlijn; **exacte ledenindeling primair nalopen** |
| Art. 6:91–94 BW (boete), 6:233/235/247/248 BW (AV), 3:40–3:42 BW (nietigheid) | Ontwerpkader boete en AV | ✅ |
| Art. 6 en 7 Mededingingswet; art. 101 VWEU | Kartelverbod, bagatel, nietigheid van rechtswege | ✅ (drempels art. 7 ⚠️) |
| VBER (EU) 2022/720 art. 1(1)(f), 3, 5 | Niet-concurrentiebedingen; art. 5 lid 3 slotzin: knowhow-verbod onbeperkt | ✅ (2x onafhankelijk; letterlijke NL-tekst ⚠️) |
| **Data Act (EU) 2023/2854** art. 1, 2, 13, 23–31, 40, 50 | Overstap, exporteerbare data, oneerlijke bedingen | ✅ **integrale authentieke EN-tekst gelezen** (NL-bewoordingen ⚠️) |
| Uitvoeringswet dataverordening (Stb. 2025, 372; i.w. 21-11-2025; ACM bevoegd) | NL-handhaving Data Act | ✅ via officiële vindplaatsen (boetemaximum ⚠️) |
| eIDAS-verordening 910/2014 art. 41 | Wettelijk vermoeden gekwalificeerde tijdstempels | ✅ |
| Richtlijn 2016/943 (bedrijfsgeheimen), overw. 14/16 | Samenstel-leer; reverse engineering contractueel beperkbaar | ✅ |

### Niet geverifieerd (expliciet, conform opdracht)
- Art. 138ab Sr (computervredebreuk), art. 29b Aw (rechtenbeheersinformatie), art. 1019i Rv (termijn eis in hoofdzaak), art. 4 Aw (makerschapsvermoeden), art. 6:247 lid 2 BW (internationale B2B buiten AV-afdeling), art. 3:310d BW (verjaring Wbb-vorderingen), schade-artikel Databankenwet, UK-recht (CDPA/VABEO), exacte BOIP/EUIPO-tarieven per datum van indiening, indicatietarieven IE 2026. Deze punten dragen het advies niet zelfstandig; waar ze genoemd worden is dat gemarkeerd.

## Prioriteitenlijstje voor de primaire eindcheck door de advocaat
1. Art. 194–207 Rv: exacte artikel- en ledenindeling nieuw bewijsrecht (dragend voor deliverable 4).
2. Art. 5 VBER letterlijke NL-tekst (dragend voor de duurkeuzes in art. 3.3).
3. NL-taalversie Data Act art. 2 punt 38, 23, 25 (dragend voor art. 3.6 en de 6.4-aanbeveling) + boetemaximum Uitvoeringswet (Stb. 2025, 372).
4. R.o. 5.3 Intrahof/Bart Smit en het dictum van ECLI:NL:RBMNE:2023:2822 (alleen als die zaak wordt aangehaald).
5. Sanctie op strijd met art. 3 lid 2 Databankenwet (nietigheid vs. vernietigbaarheid) — alleen relevant als de databank-route wordt geprocedeerd.
