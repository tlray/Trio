# Deliverable 3 — Maatregelenlijst buiten het contract (geprioriteerd)

Doel: (a) algoritmes, datastructuren, documentatie en verrijkte data laten kwalificeren als **bedrijfsgeheim** (het vereiste van "redelijke maatregelen" uit art. 1 Wbb wordt door rechters serieus getoetst en is de meest voorkomende afwijzingsgrond), en (b) namaak bij een volgend incident **bewijsbaar** maken. Let op: de maatregelentoets kijkt naar het moment van de inbreuk — wat je nu regelt, beschermt de toekomst, niet met terugwerkende kracht.

## Prioriteit 1 — Deze maand (onmisbaar)

| # | Maatregel | Waarom / grondslag |
|---|---|---|
| 1 | **Bedrijfsgeheimenregister** aanleggen: per categorie (broncode, algoritmes/matching- en verrijkingslogica, datamodellen, koppelspecificaties, prijsmodellen, documentatie) een concrete omschrijving, vindplaats, waarde-onderbouwing, wie toegang heeft en welke maatregelen gelden. Leg vast dat **Brightmotive Services bv** de houder is (concern-check). | Rechters wijzen claims af bij vage afbakening (Hof Den Haag 2025, Corrosion) of onvoldoende onderbouwde handelswaarde (Rb. Midden-NL 2024, GraydonCreditsafe). De Wbb beschermt alleen de houder. |
| 2 | **Bewijs van de NDA-clickwrap veiligstellen**: logs van wie wanneer akkoord klikte en welke documentatie is bezocht, forensisch gekopieerd, gehasht en van een tijdstempel voorzien. Daarna structureel bewaren. | De clickwrap is de kern-"redelijke maatregel" én het anker onder art. 2 lid 2 Wbb (gebruik in strijd met geheimhoudingsplicht). Zonder log bestaat de maatregel juridisch niet. |
| 3 | **Canary-records** (verzonnen maar plausibele onderdelen/kruisverwijzingen) in de verrijkte catalogusdata, **uniek per klant-tenant**, plus een globale set. Gedateerd register bijhouden, extern verankerd (i-DEPOT of hash + gekwalificeerde tijdstempel), sets rouleerbaar houden. | Canary in de kloon = vrijwel onweerlegbaar bewijs van overname én herleidbaar wie lekte (vgl. HvJ Apis/Lakorda, C-545/07). Verankering vooraf pareert het verweer "achteraf geconstrueerd"; reken erop dat canaries in een procedure onthuld moeten worden. |
| 4 | **Documentatietoegang op persoonlijke accounts** (geen gedeelde logins), met logging per gebruiker; toegangsniveaus scheiden (publiek koppel-overzicht vs. NDA-diepte-documentatie). | Compartimentering + logging is het patroon dat in de rechtspraak wint (Rb. Den Haag 2019, Future Crops). |
| 5 | **Markering**: documentatie, exports, API-specificaties en offertes voorzien van "Vertrouwelijk — bedrijfsgeheim van Brightmotive Services bv"; clickwrap-tekst aanscherpen (zie deliverable 2, invoeringsnotitie 5). | Markering alleen is onvoldoende (Rb. Midden-NL 2018, Wärtsilä), maar bouwt de "wist of had moeten weten"-wetenschap van derden op (art. 2 lid 3 Wbb). |
| 6 | **IE-overdracht (ex-)freelancers repareren**: inventariseer alle externe bijdragers aan BrightCat en laat alsnog overdrachtsakten tekenen; standaard IE-overdracht + geheimhouding in alle nieuwe inhuurcontracten. | Auteursrecht van freelancers ligt bij henzelf tenzij bij akte overgedragen (art. 2 Aw; art. 7 Aw geldt alleen voor werknemers). Zonder overdracht mist Brightmotive vorderingsbevoegdheid — een gegarandeerd verweer van een kloner. |

## Prioriteit 2 — Komend kwartaal

| # | Maatregel | Waarom / grondslag |
|---|---|---|
| 7 | **Logging & anti-extractie op de dienst**: per-klant API-keys/tenant-ID's, volledige audit trail van zoek-/blader-/exportgedrag, rate limiting met alerts op afwijkende patronen (sequentieel doorlopen catalogus, nachtelijke bulk), logs append-only met hash-keten en betrouwbare tijdstempels. AVG-kant regelen (grondslag, bewaartermijn, vermelding). | Eigen logs zijn vrij bewijs (art. 152 Rv); art. 8.5 AV ("onze opgeslagen versie geldt behoudens tegenbewijs") is een geldige bewijsafspraak (art. 153 Rv) die deze logs extra gewicht geeft. |
| 8 | **Watermerken/fingerprints per klant** in gegenereerde documentatie/PDF's en (onzichtbaar) in API-responses (veldvolgorde, sortering, afrondingsvariaties per tenant). | Herleidt een lek naar de bron; staande praktijk (e-book-watermarking). |
| 9 | **i-DEPOT-routine** (BOIP, € 37 per depot per 5 jaar): per release of kwartaal een depot met code-hash, UI-screenshots van kernschermen, algoritme-/architectuurdocumentatie, datamodel en canary-register. Start met een **nulmeting van de huidige stand**. Automatiseer daarnaast **eIDAS-gekwalificeerde tijdstempels** op release-hashes in de CI/CD + ondertekende Git-tags. | Bewijst makerschap en prioriteit (jouw versie is ouder dan de kloon); gekwalificeerde tijdstempels genieten een wettelijk vermoeden van juistheid (eIDAS-verordening, art. 41). Een i-DEPOT geeft géén IE-recht — het is bewijs. |
| 10 | **EU-modeldepot op nieuwe UI**: registreer bij elke redesign de kernschermen en iconensets als EU-model (EUIPO; € 350 eerste model + € 125 per extra; meervoudige aanvraag). Agendeer de **respijttermijn van 12 maanden** per release — al langer openbare schermen zijn niet meer registreerbaar. | Registergebonden verbodsrecht tegen UI's die "geen andere algemene indruk" wekken — het directe wapen tegen "net andere icoontjes", zonder auteursrechtelijke werktoets-discussie. |
| 11 | **Merk "BrightCat"** registreren: Uniemerk klassen 9/35/42 (ca. € 1.050 aan taksen); eerst beschikbaarheidscheck. VK apart indien relevant. | Tegen naams-/domeinmisbruik en handhaving op platforms; ontbrak tot nu toe. |
| 12 | **Databankinvestering documenteren**: uren, licentiekosten en tooling voor het **verkrijgen, controleren en presenteren** van de catalogus- en verrijkingsdata administratief bijhouden (in die termen). TecDoc-licentie nalopen: wat mag Brightmotive claimen over de gecombineerde/verrijkte set? | Het eigen databankrecht op de verrijkte data staat of valt met bewijs van deze investering (HvJ British Horseracing: creëren telt niet, verkrijgen/controleren/presenteren wel). |

## Prioriteit 3 — Doorlopend / sterk aanbevolen

| # | Maatregel | Waarom |
|---|---|---|
| 13 | Geheimhoudingsbeleid op schrift (classificatie, wie mag wat delen) + korte jaarlijkse training, **aantoonbaar** (deelnamelog). | Consequente toepassing is beslissend; één ongeclausuleerde verstrekking kan fataal zijn (Wärtsilä). Onderzoek ook eenmalig of documentatie in het verleden ooit zonder NDA is verstrekt. |
| 14 | Geheimhoudingsbedingen in alle arbeidscontracten controleren; broncode in besloten repositories met 2FA en least-privilege; offboarding-checklist (toegangen intrekken). | Basis-hygiëne die rechters meewegen. |
| 15 | NDA-flow uitbreiden naar demo's van admin-functionaliteit, onboarding-sessies en leveranciersgesprekken; wederkerige geheimhouding met koppelpartners nalopen. | Dicht de informele lekkanalen. |
| 16 | Jaarlijkse review van register + maatregelen, vastgelegd. | Toont dat maatregelen "gezien de omstandigheden" worden onderhouden (art. 1 Wbb). |
| 17 | Vaste relaties en sjablonen klaarzetten: IE-advocaat, deurwaarder met IT-forensische ervaring, forensisch IT-bureau; concept-verlofverzoek bewijsbeslag, sommatie met onthoudingsverklaring, interne litigation-hold-instructie. | Bij een incident telt snelheid; zie deliverable 4. |
| 18 | Nice-to-have: DLP-/exfiltratiemonitoring, pentests met rapportage, clean-desk/bezoekersbeleid, auditrechten bij klanten met maatwerkkoppelingen. | Verdieping als 1–17 staan. |

**Kosten-indicatie jaar 1 (taksen):** merk ± € 1.050, zes EU-modellen ± € 975, i-DEPOT-routine ± € 150–300, tijdstempels verwaarloosbaar → totaal ca. € 2.200–3.500, exclusief advies- en bouwuren.

**Clickwrap voor eindgebruikers (garages):** het vermoeden uit de handover klopt — op termijn verdient een gebruikers-clickwrap (ook voor klanten-van-klanten) aanbeveling, vooral om scraping door eindgebruikers contractueel te dekken en de vertrouwelijkheidsketen rond te maken. Dit kan los van de AV-herziening en hoeft die niet op te houden.
