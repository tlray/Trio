# Memo — De sterkste beschermingsstrategie tegen namaak van BrightCat

**Aan:** Ray (Brightmotive Services bv)
**Datum:** 18 augustus 2026
**Status:** Onafhankelijk onderzoek, uitgevoerd in zeven parallelle sporen met bronverificatie. Zie `05-bronnen-en-verificatie.md` voor de verificatiestatus per bron en één belangrijk voorbehoud over de verificatiemethode.

---

## 1. De kern in het kort

1. **Wat het incident pijnlijk blootlegde, klopt juridisch:** het auteursrecht beschermt de broncode van BrightCat, maar níet de functionaliteit, de werkwijze, de algoritme-ideeën of de bestandsformaten. Wie BrightCat nabouwt op basis van wat hij ziet — zelfde schermen, net andere icoontjes, zelfde werkwijze — pleegt in beginsel géén auteursrechtinbreuk. Dat is Europese vaste rechtspraak (SAS Institute) en in Nederland bevestigd (Diplomatic Card/Forax). **Daarom is het contract niet een extraatje, maar het hoofdinstrument.**
2. **Het goede nieuws:** wat het IE-recht vrijlaat, mag je jegens je eigen klant vrijwel volledig contractueel dichtzetten (Ryanair/PR Aviation), zolang je een paar dwingende grenzen respecteert. Grote B2B-SaaS-partijen (Salesforce, AWS) doen dit standaard met "competitive use"-clausules.
3. **De twee juristen hadden allebei half gelijk** over het oude beding ("op enigerlei wijze kopiëren of namaken"). Zie §3. De les: niet procederen op vage woorden, maar expliciet opschrijven wat je bedoelt — dan is er niets uit te leggen.
4. **De strategie rust op vier pijlers** die elkaar overlappen, zodat er geen enkel "single point of failure" is: (i) een gelaagd contractueel verbod met **boete**, (ii) het **bedrijfsgeheimenspoor** (Wbb) dat óók de externe bouwer raakt, (iii) **IE-versterking** waar die echt werkt (databankrecht op verrijkte data, modeldepots op nieuwe schermen, i-DEPOT als bewijs), en (iv) een **vooraf ingerichte bewijspositie** (canary-records, logging, watermerken) plus een draaiboek.
5. **De boete is het antwoord op het schadebewijsprobleem** uit het incident: een goed ontworpen boete is direct opeisbaar zonder dat je schade hoeft te bewijzen, en is matigingsbestendig te maken door hem te laten meeschalen met de omvang van de klant.
6. **Eén waarschuwing die verder gaat dan de vraag:** de Data Act (Verordening (EU) 2023/2854) geldt sinds 12 september 2025 ook voor BrightCat. Het huidige art. 6.4 voldoet daar zelf niet aan, en een té breed namaakverbod (dat de klant verbiedt ooit een eigen vervangend systeem te bouwen) kan een verboden "overstapbelemmering" zijn. De voorgestelde tekst lost dit op met een expliciete uitzondering.

---

## 2. Waarom Brightmotive bij het incident weinig kon

Drie factoren vielen samen:

- **Het beding van v3.01 was te dun.** "Kopiëren of namaken op enigerlei wijze" zonder definitie, zonder kennisgebruiksverbod, zonder derdenregeling en zonder boete.
- **Het IE-recht liet de kern vrij.** De nagebouwde functionaliteit, algoritmes en werkwijze zijn geen auteursrechtelijk beschermde "uitdrukkingswijze". De UI-route (look & feel als "gewoon" werk) bestaat in theorie, maar Nederlandse rechters wijzen die bij branchegebruikelijke catalogus-/webshop-UI's vrijwel altijd af (Betsoft; Vendic/Meubelplaats). Winbaar waren hooguit letterlijk overgenomen teksten, iconen en assets — en de **datakant** (zie §4.3).
- **De schade was niet hard te maken.** Winstafdracht en licentie-analogie bestaan (art. 27a Aw, art. 6:97 BW), maar vergen cijfers uit het kamp van de wederpartij en een lange procedure.

De strategie hieronder repareert alle drie.

---

## 3. De twee zienswijzen gewogen (onderzoeksvraag 1)

**Zienswijze 1 (breed):** "op enigerlei wijze" kan breed worden uitgelegd. **Zienswijze 2 (eng):** het beding staat in een IE-artikel en moet binnen het IE-recht eng worden gelezen.

Weging naar Nederlands uitlegrecht: algemene voorwaarden zijn niet uitonderhandeld en bestemd voor veel klanten; ze worden dan overwegend **objectief** uitgelegd (glijdende schaal DSM/Fox, ECLI:NL:HR:2004:AO1427; Lundiform/Mexx, ECLI:NL:HR:2013:BY8101 — let op: in de handover stond een onjuist ECLI, zie bronnendocument). Objectief-taalkundig heeft "namaken" zelfstandige betekenis naast "kopiëren" (anders is het woord zinledig) en signaleert "op enigerlei wijze" een ruime bedoeling. Daar staat tegenover dat de IE-context het beding inkleurt, en dat onduidelijkheid in niet-onderhandelde voorwaarden in de weging ten nadele van de opsteller werkt.

**Ons oordeel: geen van beiden wint volledig.** Een rechter brengt het vrijwel één-op-één nabouwen van BrightCat (zelfde schermopbouw, werkwijze en dataverwerking met cosmetische verschillen) waarschijnlijk wél onder "namaken" — dat is gewoon Nederlands. Maar zuiver functionele inspiratie of eigen herbouw van vrije ideeën valt er zonder explicietere tekst niet onder, en de klant heeft met de SAS-lijn een serieus verweer op het functionele deel (procesrisico geschat op 40–50%). **Conclusie:** het oude beding is bruikbaar als terugval-anker voor het reeds gebeurde incident, maar voor de toekomst te dun. De oplossing is geen keuze tussen "streng-breed" (v3.05) en "middelen-gericht" (het review-voorstel), maar een **derde route**: expliciet, doelgebonden en gelaagd — zie §4.1 en het tekstvoorstel in `02-tekst-artikel-3-en-boetebeding.md`.

Over het eerdere review-voorstel (kritisch getoetst, zoals gevraagd): de richting was juist (dwingend softwarerecht respecteren, 1 jaar postcontractueel, knowhow onbeperkt), maar het bevatte drie zwaktes die wij hebben gerepareerd: (1) "de kennis die u door het gebruik opdoet" was niet beperkt tot **niet-openbare** informatie — daardoor werkt het als verkapt concurrentieverbod dat nooit onder de groepsvrijstelling kan vallen en bij nietigheid niet wordt "afgeknipt op het toelaatbare" (conversieverbod, HR BP/Benschop, ECLI:NL:HR:2013:2123); (2) er ontbrak een uitzondering voor onafhankelijke eigen ontwikkeling en voor de Data Act-overstap; (3) er was geen boete, terwijl het schadebewijsprobleem juist hét praktische probleem was.

---

## 4. De vier pijlers, met grondslag en houdbaarheid

### 4.1 Pijler 1 — Het contract: gelaagd verbod + boete (houdbaarheid: hoog, mits gelaagd)

Het nieuwe artikel 3 (volledige tekst in deliverable 2) bestaat uit **zelfstandige, opgeknipte leden**. Dat is geen stilistische keuze: als één laag ooit (deels) nietig blijkt, blijven de andere staan (partiële nietigheid, art. 3:41 BW), en de rechter mag een te ruim mededingingsbeding niet zelf terugsnoeien naar het toelaatbare (HR BP/Benschop) — dus moet elk deelverbod op zichzelf al houdbaar zijn.

| Laag | Wat het regelt | Grondslag houdbaarheid | Inschatting |
|---|---|---|---|
| Namaakverbod met definitie | Verbiedt ook nabouwen "op hoofdlijnen" met andere vormgeving | Contractsvrijheid buiten IE-beschermingsomvang (Ryanair, C-30/14); raakt geen dwingend gebruikersrecht | Hoog |
| Vertrouwelijkheid/bedrijfsgeheim | Alles achter de inlog + documentatie = geheim, ook ná de overeenkomst zolang niet openbaar | Wbb; VBER art. 5 lid 3 slotzin staat een tijds-onbeperkt knowhow-verbod expliciet toe | Hoog |
| Doelgebonden kennisgebruiksverbod | Dienst/documentatie/data niet gebruiken om een concurrent van BrightCat te (laten) bouwen; looptijd + 1 jaar; vertrouwelijke info onbeperkt | Verbiedt niet het concurreren als zodanig maar het concurreren mét onze middelen (nevenrestrictie-leer, Pronuptia); binnen VBER-kaders; benchmark: Salesforce/AWS doen hetzelfde | Hoog, mits doelgebonden |
| Derdenregeling | Bouwers alleen na toestemming + eigen geheimhouding rechtstreeks jegens Brightmotive; overtredingen van de derde gelden als die van de klant | Contractsvrijheid; dicht het gat waardoor de bouwer bij het incident buiten schot bleef; activeert bovendien de derdenwerking van de Wbb (wetenschap) | Hoog |
| Data-extractieverbod (tweetraps) | Geen geautomatiseerd/stelselmatig opvragen of hergebruiken, "ongeacht of de databank wettelijk beschermd is" | Beschermde databank: databankrecht zelf; onbeschermde databank: volledige contractsvrijheid (Ryanair) — beide scenario's gedekt | Hoog |
| Carve-outs | Dwingend recht (art. 45j–45m Aw, databankgebruikersrechten, Data Act) + onafhankelijke ontwikkeling blijft toegestaan | Voorkomt precies de nietigheden die het oude beding bedreigden; sterkste troef tegen herkwalificatie als concurrentie- of overstapbelemmering | — |
| Boete | 2× jaarvergoeding per overtreding (min. € 25.000) + € 1.000/dag, plafond 4× jaarvergoeding, naast staking en aanvullende schadevergoeding | Art. 6:91–94 BW; ontwerp volgt de matigingsrechtspraak (zie hieronder) | Hoog |

**Waarom dit boete-ontwerp.** Matiging kan nooit worden uitgesloten (art. 6:94 lid 3 BW is dwingend), maar de rechter matigt alleen bij een "buitensporig en daarom onaanvaardbaar resultaat" (HR Intrahof/Bart Smit, ECLI:NL:HR:2007:AZ6638). De bewezen ontwerpfouten uit de rechtspraak zijn: één eenheidsboete op alle mogelijke overtredingen (HR Turan/Easystaff, ECLI:NL:HR:2018:207: € 1,23 mln gevorderd, € 21.150 overgehouden), onbegrensde dagboetes die stil oplopen, en bedragen zonder relatie tot de contractswaarde (Rb. Midden-Nederland 2026: € 2 mln gevorderd, nul toegewezen). Ons ontwerp vermijdt alle drie: de boete hangt **alleen** aan het namaak-cluster, **schaalt mee** met de jaarvergoeding (die al een promillage van de klantomzet is — automatische proportionaliteit, van zzp-grossier tot inkooporganisatie), heeft een **plafond**, en benoemt zijn eigen strekking (schade bij namaak is naar haar aard niet te bewijzen). Belangrijk: "onverminderd schadevergoeding voor zover de schade hoger is" moet er expliciet in, anders vervangt de boete de schadevergoeding (art. 6:92 lid 2 BW). En: neem de boete ook zichtbaar in de offerte op — dat ondergraaft elk "verstopt beding"-verweer en is commercieel uitlegbaar met verwijzing naar het incident.

**Mededingingsrechtelijke houdbaarheid (getoetst):** het kennisgebruiksverbod is primair prestatie-/knowhowbescherming en valt buiten het kartelverbod (nevenrestricties; Pronuptia). Zelfs bij herkwalificatie als niet-concurrentiebeding: tijdens de looptijd groepsvrijgesteld tot 5 jaar (VBER 2022/720, marktaandelen ≤30%); postcontractueel is een écht exploitatieverbod voor SaaS nooit vrijgesteld (de "ruimten en terreinen"-eis van art. 5 lid 3 is online onvervulbaar), maar een gebruiksverbod van **niet-openbare** knowhow mag onbeperkt — precies zo is de tekst opgebouwd. En wie zich als klant op nietigheid wil beroepen, draagt een zware stelplicht inclusief marktafbakening (HR ANVR/IATA, ECLI:NL:HR:2012:BX0345).

**Wat je bewust níet moet opschrijven** (nietig of riskant): een verbod op observeren/bestuderen/testen van de software tijdens normaal gebruik (art. 45l Aw jo. art. 8 Softwarerichtlijn; SAS), een absoluut decompilatie-/foutverbeteringsverbod (art. 45m Aw; Top System, C-13/20), een verbod op reservekopieën (art. 45k Aw), een onbegrensd "geen ideeën of concepten gebruiken", en een algeheel concurrentieverbod. In een pure SaaS-situatie is de klant naar heersende leer overigens geen "rechtmatige verkrijger van een exemplaar", zodat die dwingende rechten waarschijnlijk niet eens van toepassing zijn — maar dat is niet uitgeprocedeerd, en de carve-out kost niets en voorkomt de hele discussie.

### 4.2 Pijler 2 — Bedrijfsgeheimen (Wbb): het spoor dat óók de bouwer raakt (houdbaarheid: hoog, mits maatregelen op orde)

De Wet bescherming bedrijfsgeheimen beschermt informatie die (a) geheim is, (b) daardoor handelswaarde heeft en (c) met **redelijke maatregelen** geheim wordt gehouden (art. 1 Wbb). Voor BrightCat kwalificeren: broncode, algoritmes en matching-/verrijkingslogica, datamodellen, koppelspecificaties, interne documentatie en prijsmodellen. Níet: wat elke gebruiker in de gewone front-end ziet. Wel weer: het **samenstel** van architectuur, datamodel en werkwijze zoals dat alleen uit documentatie en admin-laag samen kenbaar is (samenstel-leer, o.a. Hof Arnhem-Leeuwarden 2025).

Waarom dit spoor zo waardevol is:

- **Derdenwerking:** de externe bouwer die wist of had moeten weten dat hij met onrechtmatig gedeelde informatie werkte, handelt zélf onrechtmatig (art. 2 lid 3 Wbb). Een professionele softwarebouwer die documentatie en specificaties van andermans platform krijgt om dat platform na te bouwen, kan zich moeilijk op onwetendheid beroepen — en een sommatiebrief fixeert zijn wetenschap vanaf ontvangst. Dit dicht het "derden-gat" (onderzoeksvraag 6) beter dan welk contract ook.
- **De kloon zelf is een "inbreukmakend goed"** (art. 2 lid 4 Wbb): je kunt terugroeping en **vernietiging van de codebase** vorderen (art. 6 Wbb).
- **Procederen zonder je geheimen prijs te geven** kan via de speciale procesregels (art. 1019ib/1019ic Rv); volledige proceskosten zijn mogelijk bij kwade trouw (art. 1019ie Rv; HR Heraeus/Biomet, ECLI:NL:HR:2020:830 — discretionair).
- **De bestaande NDA-clickwrap op de documentatie is goud waard.** Gebruik van die informatie voor een kloon is onrechtmatig gebruik, delen met de bouwer onrechtmatig openbaar maken (art. 2 lid 2 Wbb). Maar: bewaar het bewijs van wie wanneer heeft geklikt — zonder dat bewijs bestaat de "redelijke maatregel" juridisch niet.

De valkuil is het maatregelenvereiste: de rechtspraak wijst claims vooral af wegens inconsequente geheimhouding (één keer documentatie zonder NDA delen kan fataal zijn — Wärtsilä/Aegir) of een te vage afbakening van wát het geheim is (Corrosion, 2025). Het winnende patroon is: NDA + expliciete communicatie + compartimentering + logging (Future Crops/Certhon). Daarom staat het **bedrijfsgeheimenregister** bovenaan de maatregelenlijst (deliverable 3). Let op: de maatregelentoets kijkt naar het moment van de inbreuk — nieuwe maatregelen helpen de toekomst, niet met terugwerkende kracht.

**Reverse engineering:** de Wbb staat toe dat je onderzoek aan de dienst contractueel beperkt (art. 3 lid 1 sub b: "tenzij anders overeengekomen"), en bij SaaS heeft de klant het product niet eens "in bezit". Alleen het observeren van het *computerprogramma* tijdens rechtmatig gebruik is dwingendrechtelijk vrij — vandaar dat het verbod als doelbeperking is geformuleerd (geen nabouw, geen scraping, geen derden), niet als kaal kijkverbod.

### 4.3 Pijler 3 — IE-versterking: inzetten waar het werkt (houdbaarheid: gemengd, zie per onderdeel)

- **Databankenrecht op de verrijkte data — de sterkste buitencontractuele kaart (hoog).** Naast de TecDoc-licentie kan Brightmotive een **eigen** databankrecht hebben op haar verrijkte en gecombineerde catalogusdatabank, mits de substantiële investering in het *verkrijgen, controleren en presenteren* van de data wordt gedocumenteerd (niet: het creëren — British Horseracing, C-203/02; leg de investering dus administratief vast in die termen: uren, licentiekosten, tooling). Een kloon die de verrijkte data overneemt en het platform vervangt, raakt per definitie de terugverdienmogelijkheid (CV-Online, C-762/19). En blijkt de databank onverhoopt níet beschermd, dan geldt juist volledige contractsvrijheid (Ryanair) — vandaar de tweetrapsclausule in het contract. Actiepunt: loop de TecDoc-licentie na op wat Brightmotive over de gecombineerde set mag claimen.
- **Auteursrecht (gemiddeld):** sterk voor broncode en voor letterlijk overgenomen teksten, iconen en assets; zwak voor look & feel en architectuur. Repareer wel het makerschap: auteursrecht van **freelancers** ligt bij henzelf tenzij schriftelijk overgedragen (art. 2 Aw; art. 7 Aw geldt alleen voor werknemers) — zonder overdrachtsakten mist Brightmotive straks vorderingsbevoegdheid op onderdelen.
- **Modeldepot op nieuwe UI (hoog voor de toekomst):** een geregistreerd EU-model op schermontwerpen en iconensets geeft een registergebonden verbodsrecht tegen UI's die "geen andere algemene indruk" wekken — precies het wapen tegen "net andere icoontjes", zonder de zware werktoets van het auteursrecht. Let op: bestaande, al jaren openbare schermen zijn niet meer registreerbaar (nieuwheidseis); elk nieuw scherm/redesign wél, binnen de respijttermijn van 12 maanden. Kosten: € 350 + € 125 per extra model (EUIPO).
- **i-DEPOT en tijdstempels (bewijs, geen recht):** per release een i-DEPOT (€ 37 per 5 jaar) met code-hash, UI-screenshots, algoritme-documentatie en datamodel, plus automatische eIDAS-tijdstempels in de CI/CD. Daarmee bewijs je later makerschap en dat jouw versie ouder is dan de kloon.
- **Slaafse nabootsing (laag als hoofdroute, nuttig als aanvulling):** vergt "eigen gezicht" en verwarringsgevaar (All Round/Simstars, ECLI:NL:HR:2017:938); voor B2B-platform-UI is dat zelden haalbaar — het review-voorstel had dat goed. Maar de **onrechtmatige-daad-route is hier sterker dan gemiddeld** door bijkomende omstandigheden: klantrelatie, toegang onder NDA, en een bouwer die bewust profiteert van andermans wanprestatie. Als drukmiddel tegen de bouwer, naast de Wbb, zeker bruikbaar.

### 4.4 Pijler 4 — Bewijs vooraf inrichten (essentieel; dit besliste het vorige incident)

Sinds 1 januari 2025 is het bewijsrecht vernieuwd: het inzagerecht staat nu in art. 194–195a Rv (voorheen 843a), bewijsbeslag is voor alle zaken gecodificeerd (art. 205–206 Rv), en er is een nieuw instrument: het **deurwaarders-proces-verbaal van constateringen** (art. 207 Rv), met rechterlijk verlof zelfs met dwingende bewijskracht. Al die instrumenten werken alleen als je concreet kunt maken *wat* is overgenomen en *waar* het zit. Daarom, vooraf:

1. **Canary-records** (verzonnen maar plausibele records) in de verrijkte data, **uniek per klant** — duikt jouw canary op in een kloon, dan is overname vrijwel onweerlegbaar én herleidbaar wie lekte (vgl. HvJ Apis/Lakorda, C-545/07: meegekopieerde kenmerken als bewijs van extractie). Houd een gedateerd, extern verankerd register bij (anders is het verwijt "achteraf geconstrueerd") en reken erop dat je canaries in een procedure moet onthullen — gebruik rouleerbare sets.
2. **Logging en rate limiting**: per-klant API-keys, audit trail van zoek-/export­gedrag, alerts op stelselmatig doorlopen van de catalogus, logs append-only met tijdstempels. Het AV-beding "onze opgeslagen versie geldt behoudens tegenbewijs" (art. 8.5, al aanwezig) is een geldige bewijsafspraak (art. 153 Rv) en maakt die logs extra waardevol.
3. **Watermerken/fingerprints per klant** in documentatie en API-responses.
4. **Eigen ontwikkelgeschiedenis vastleggen** (signed commits, releases, i-DEPOT) — weerlegt het klassieke verweer "wij hebben het zelf ontwikkeld".

Het volledige stappenplan voor een volgend incident staat in deliverable 4. De belangrijkste les daaruit: **eerst stil bewijs veiligstellen, dán pas sommeren** — elke vroege boze e-mail is een kans voor de wederpartij om bewijs te wissen, terwijl het beslagverlof juist op verduisteringsvrees steunt.

---

## 5. De grenzen die je niet mag oprekken (onderzoeksvraag 7)

1. **Dwingend softwarerecht** (alleen relevant voor zover de klant een kopie heeft, maar respecteer het altijd): observeren/bestuderen/testen tijdens rechtmatig gebruik, reservekopie, foutverbetering en interoperabiliteits-decompilatie (art. 45j slotzin, 45k, 45l, 45m Aw; art. 8 Richtlijn 2009/24: strijdige bedingen nietig).
2. **Rechten van de rechtmatige databankgebruiker**: opvragen/hergebruiken van niet-substantiële delen tijdens de licentie (art. 3 Databankenwet; art. 24a lid 3 Aw).
3. **Data Act, hoofdstuk VI** (sinds 12-9-2025, ook voor lopende contracten; toezichthouder: ACM, boetes tot AVG-niveau): geen enkele contractuele belemmering van een overstap naar een andere aanbieder **of naar een eigen (on-premises) systeem** — dus nooit een verbod op het bouwen van een eigen vervangend systeem *als zodanig*, alleen op het gebruik van Brightmotive-materialen en -geheimen daarbij. Kennisgevingstermijn max. 2 maanden, transitieperiode 30 dagen, retrieval ≥30 dagen, overstapkosten vanaf 12 januari 2027 nul. Wat je **niet** hoeft af te geven: de software, algoritmes en verrijkingslogica — "exporteerbare data" sluit IE- en bedrijfsgeheim-activa van de aanbieder én van derden (TecDoc) uit (art. 2 punt 38).
4. **Data Act art. 13**: eenzijdig opgelegde B2B-databedingen mogen niet "oneerlijk" zijn — raakt vooral art. 3.2 (het datagebruiksrecht van Brightmotive): houd dat doelgebonden en laat de klant altijd een kopie van zijn eigen data houden.
5. **Mededingingsrecht**: geen algeheel (post-contractueel) concurrentieverbod; wel doelgebonden knowhowbescherming (onbeperkt voor niet-openbare informatie).
6. **Matiging van boetes** (art. 6:94 BW) is niet weg te contracteren — vandaar het meeschaal-ontwerp.

**Actiepunt buiten de directe vraag:** vervang art. 6.4 door een volwaardige exit-regeling (checklist in deliverable 2, bijlage) en maak art. 3.2 Data Act-proof. Een namaakverbod dat naast een non-conforme exit-regeling staat, is voor een klant-advocaat een gemakkelijk aanvalspunt ("het hele artikel 3/6 ademt lock-in") — de geloofwaardigheid van het pakket als geheel telt.

---

## 6. Restrisico's en aannames

- **Verificatievoorbehoud:** de onderzoeksomgeving blokkeerde rechtstreekse toegang tot wetten.overheid.nl, rechtspraak.nl en EUR-Lex. Alle bronnen zijn geverifieerd via meervoudige, onafhankelijke secundaire bronnen (en de Data Act via de integrale authentieke Engelse verordeningstekst); de status per bron staat in deliverable 5. **Laat vóór gebruik in een sommatie of processtuk de gemarkeerde punten éénmaal primair nalopen door de advocaat.**
- **SaaS en "rechtmatige verkrijger":** of de dwingende softwaregebruikersrechten überhaupt gelden voor een klant met alleen browsertoegang is niet uitgeprocedeerd. De voorgestelde tekst is zo opgezet dat hij onder béide scenario's overeind blijft.
- **De grens tussen namaakverbod en Data Act-overstapbelemmering** is nog door geen rechter of de ACM getrokken; de voorgestelde carve-out is tekst- en systeemgetrouwe uitleg, geen vaste lijn.
- **De kwalificatie van de verrijkte databank** hangt af van de gedocumenteerde investering en van de TecDoc-licentie; beide vergen intern huiswerk (maatregelenlijst).
- **Boetebedragen** zijn onderbouwde ontwerpkeuzes op basis van de gevonden rechtspraakbandbreedte, geen garanties: matiging blijft altijd mogelijk; het ontwerp minimaliseert de kans.
- **Buitenlandse klanten:** dit advies is Nederlands recht met Nederlandse forumkeuze (art. 8.1/8.2 dekt dat). Voor UK-klanten geldt post-Brexit deels ander recht (vergelijkbare, niet identieke regels); niet verder onderzocht.

## 7. Vervolgstappen (samengevat; detail in deliverables 2–4)

1. Art. 3 vervangen door de voorgestelde tekst; boete ook in de offerte benoemen (commercieel uitlegbaar via het incident).
2. Art. 6.4 vervangen door een Data Act-conforme exit-regeling; art. 3.2 doelgebonden maken.
3. Maatregelenlijst uitvoeren, te beginnen met het bedrijfsgeheimenregister, de NDA-logbewijzen en de canary-records (deliverable 3).
4. Draaiboek klaarzetten met vaste advocaat/deurwaarder/forensisch IT'er (deliverable 4).
5. Eenmalige primaire bronnencheck door de advocaat op de gemarkeerde punten (deliverable 5).
