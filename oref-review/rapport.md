# Beoordeling van het oref-algoritme in Trio

*Datum: 12 augustus 2026 · Basis: Trio 0.8.4 (`29350e3`), trio-oref `dev @ 8282ce7` (fork van openaps/oref0)*

**Scope:** de volledige beslisketen — `determine-basal` (incl. SMB/UAM en dynamic ISF), de vier
voorspellingscurves, IOB-berekening, meal/COB, autosens, en de Swift↔JavaScript-bridge
(`OpenAPS.swift` e.o.). Weging op een gebruiker met **SMB + UAM aan** (zonder dynamic ISF, tenzij
anders vermeld).

**Methode:** zeven parallelle code-lezers (één per deelmodule), elke bevinding daarna adversarieel
geverifieerd tegen de code en waar relevant tegen upstream oref0 (master); de autosens- en
bridge-bevindingen zijn handmatig regel-voor-regel nagelopen. Verdicten in dit rapport:
**BEVESTIGD** (claim klopt aantoonbaar in de code), **DEELS** (kern klopt, details genuanceerd).
Weerlegde claims zijn weggelaten. In totaal zijn 71 kandidaat-bevindingen beoordeeld.

---

## TL;DR

Het algoritme is in de kern **goed doordacht en veiligheidsgericht**: de gelaagde vangnetten
(minGuardBG, threshold, maxIOB, maxSafeBasal, maxBolus, SMB-interval) zijn stuk voor stuk zinnig,
en het beruchte "bolus geven en meteen alles terugtrekken" is géén besluiteloosheid maar bewust
ontwerp (§1.3). Tegelijk klopt je gevoel dat delen **arbitrair** zijn: het bestand staat vol
magische constantes zonder afleiding, waarvan de meeste "arbitrair maar conservatief" zijn — en
een handvol "arbitrair én consequentieel" (§1.1). Daarnaast heeft de audit **een reeks echte bugs**
opgeleverd, waarvan er drie de moeite van direct repareren waard zijn (patches meegeleverd in
`oref-review/patches/`) en een paar grotere die teamdiscussie verdienen — met als belangrijkste:
zero-temp-duren die onder een procent-override kwadratisch te kort uitpakken, een geïnverteerde
lage-temp-formule die het terugtrek-gevoel onnodig verscherpt, een vastgelopen-CGM-detectie die
wel logt maar niets meer dóet, en verlopen overrides die in de achtergrond blijven doorsturen.

---

## 1. Jouw drie vragen

### 1.1 "Het voelt op sommige plekken arbitrair" — klopt dat?

Ja en nee. Het is nuttig om drie categorieën te onderscheiden die in de code door elkaar lopen:

**a) Goed onderbouwd.** De exponentiële insuline-activiteitscurve is netjes afgeleid
(`iob/calculate.js:123-134`, LoopKit-afleiding met peak/DIA als parameters). De
threshold-formule `min_bg − 0,5·(min_bg − 40)` (regel 621) schaalt logisch mee met de target. De
temp-basaal-hysterese (±20%-band in `basal-set-temp.js:31`) en `maxSafeBasal = min(max_basal,
3× max-dagbasaal, 4× huidige basaal)` zijn beproefde anti-jojo- en veiligheidsmechanismen.

**b) Arbitrair maar conservatief.** Dit is de grootste categorie, en grotendeels acceptabel
*omdat de loop elke 5 minuten opnieuw beslist* — een te voorzichtige constante kost hooguit wat
snelheid, geen veiligheid. Voorbeelden: `smb_delivery_ratio` 0,5 (elke cyclus de helft van wat
nodig lijkt — een geometrische benadering die overshoot bij foute voorspellingen halveert),
SMB-interval 3 min, de 2×-versnelling van lage temps (regel 1322), deviation-horizon 30 min,
expectedDelta-horizon 2 uur, de UAM-vervalconstantes (afbouw met minstens ⅓ van de
opbouwhelling, 3-uurs-fallback), `min_5m_carbimpact` 8, `maxCOB` 120, de
remainingCATime-constanten (3 h minimum, 20/30 g/h), en vrijwel alle autosens-drempels
(45 min exclusie na koolhydraten, 5 h maaltijdvenster, neutrale deviatie elke 2 uur, demping bij
< 8 h data). Geen ervan heeft een zichtbare afleiding, maar de foutrichting is steeds "minder/later
insuline" of "signaal dempen".

**c) Arbitrair én consequentieel.** Hier zit het echte verbeterpotentieel:

- **`maxDelta > 20% van BG` schakelt SMB binair uit** (regel 1227). Relatief aan BG betekent dit:
  bij BG 180 mag een stijging tot 36 mg/dl/5min door, bij BG 90 maar 18 — terwijl een échte snelle
  maaltijdstijging juist het moment is waarop je SMB wilt. Omgekeerd vangt hij trage
  compressie-drift niet. Het is een kalibratie-artefact-detector die zich voordoet als
  stijgingsbegrenzer. (BEVESTIGD)
- **De minPredBG-wachttijd is hard 90 min** (regels 967-973: eerst 60, direct overschreven met
  90), ongeacht insulinetype — terwijl Trio elders wél een instelbare `insulinPeakTime` heeft.
  Voor Lyumjev-gebruikers is 90 min conservatiever dan nodig; het remt SMB's structureel af.
  (BEVESTIGD)
- **Bij dynamic ISF (log-modus): `insulinFactor = 120 − piektijd`** koppelt een
  PK-instelling dimensieloos (mg/dl gedeeld door minuten) aan de globale doseersterkte —
  sneller insuline instellen *verzwakt* paradoxaal alle correcties met ~15-25%. (DEELS, mechanisme
  bevestigd)
- **De sentinel `overrideTarget != 6`** (regel 145) — het getal 6 als magische
  "geen-target"-marker, vermoedelijk een mmol-erfenis — is ondoorgrondelijk en foutgevoelig.
  (BEVESTIGD)

Kortom: je intuïtie klopt, maar het meeste arbitraire is bewust richting veilig afgerond. De lijst
onder (c) plus de bugs in §3 zijn waar aandacht loont.

### 1.2 "Vooral de laatste metingen tellen zwaar mee" — hoe zwaar precies?

De invloed van de laatste metingen is **asymmetrisch ontworpen**, en dat is grotendeels goed
nieuws:

**Het niveau (de laatste BG-waarde) is de minst gefilterde input.** `glucose-get-last.js` middelt
alleen metingen die < 2,5 min uit elkaar liggen (dubbele bronnen); één 5-minuten-meting gaat
verder rauw de keten in. Die waarde zaait `naive_eventualBG = bg − iob·sens` (regel 711) én alle
vier de voorspellingscurves (regels 758-761). Een uitschieter van +15 mg/dl bij ISF 50 wordt dus
~0,3 U extra `insulinReq`, waarvan de helft (smb_ratio) als SMB geleverd wordt: **~0,15 U per
foute meting** — begrensd door maxBolus en de volgende cyclus gecorrigeerd door de dan negatieve
delta. Vervelend, niet gevaarlijk.

**De helling (delta) is wél slim gedempt, en asymmetrisch:**

- Omhoog: het algoritme gebruikt `minDelta = min(delta, short_avgdelta)` (regel 411) — een
  opwaartse piek in de laatste meting wordt geklemd op het 15-minuten-gemiddelde (weging van een
  meetfout in de laatste waarde: ~0,61 i.p.v. 1,0).
- Omlaag: als de deviatie negatief uitpakt, wordt progressief hergemiddeld met
  `minAvgDelta` en daarna `long_avgdelta` (regels 700-706) — een expliciete upstream-verdediging
  tegen één grote valse daling.
- Maar richting *stoppen* is één meting genoeg: BG of minGuardBG één keer onder threshold →
  direct zero-temp (regel 1265). Eén-monster-gevoelig, bewust, in de veilige richting.

**De gaten:** (1) er is nergens outlier-rejectie op de ruwe reeks — de laatste meting is het
gedeelde eindpunt van álle delta-metrieken, dus een meetfout verschuift delta met factor 1,0,
short_avgdelta met ~0,61 en long_avgdelta met ~0,18 tegelijk (BEVESTIGD/DEELS); (2) de
`noise`-vangnetten van oref (target +30% bij noise ≥ 2, stop bij ≥ 3) zijn in Trio **permanent
dood** omdat de Swift-bridge het noise-veld simpelweg niet meestuurt
(`AlgorithmGlucose.swift`, encoder zonder `noise`-key — BEVESTIGD); en (3) de
vastgelopen-sensor-detectie logt nog wel maar onderneemt niets meer (§3.1, punt 3).

Praktisch advies los van codewijzigingen: Trio's eigen glucose-smoothing-optie ondervangt het
niveau-probleem deels; een 3-punts-mediaanfilter vóór de delta-berekening zou de goedkoopste
structurele verharding zijn (vertraagt een echte trend hooguit één meting).

### 1.3 "Elke keer van bolus naar alles terugtrekken" — kan dat beter?

**Wat je ziet is bewust ontwerp.** Na elke SMB berekent regel 1552-1573 een compenserende
zero-/lage temp uit `worstCaseInsulinReq = (target − (naive_eventualBG + minIOBPredBG)/2)/sens`.
Beide inputs negeren *met opzet* de COB/UAM-absorptievoorspelling die de SMB rechtvaardigde: het
is de IOB-only-blik ("wat als de absorptie nú stopt?"). Zodra een SMB de IOB verhoogt, duikt die
blik onder target en komt er een zero-temp naast te staan. De bedoeling (upstream oref0):
**insuline naar voren schuiven** — basaal-equivalente insuline vroeg als bolus leveren en de pomp
tegelijk in de faalveilige stand parkeren. Stokt de absorptie, of valt de telefoon/loop uit
midden in het venster, dan loopt de suspensie al. Netto over het venster is het ongeveer dezelfde
insuline, alleen eerder. De terugtrekking is boekhouding, geen spijt. De vervolgcycli houden de
zero-temp bewust in stand ("if in SMB mode, don't cancel SMB zero temp", regels 1403 en 1429).

**Maar het patroon is in deze code scherper dan het hoeft te zijn.** Vier verscherpers, waarvan
twee direct repareerbaar zonder ook maar iets later of minder te doseren:

1. **De geïnverteerde lage-temp-formule** (regel 1571, upstream-erfenis, BEVESTIGD): kleine
   terugtrekbehoeftes (paar minuten) worden nu afgebeeld op een *diepe* 30-min-verlaging, grote
   juist op een bijna-neutrale. Correct is `basaal × (1 − durationReq/30)`. Dit is vermoedelijk
   de grootste bijdrage aan jouw "hij trekt álles terug"-gevoel bij marginale correcties.
   → **patch 0002**.
2. **De overrideFactor-precedentiebug** (BEVESTIGD, Trio-fork): schaalt zero-temp-duren met
   factor² fout zodra een procent-override actief is. → **patch 0001**.
3. **De targetband heeft breedte nul.** Trio zet `max_bg` gelijk aan de target (regels 483-485),
   dus élke cyclus valt per definitie in óf de doseer- óf de terugtrek-tak; een neutrale band
   bestaat niet. (Toetsing wees uit: bewuste Trio-keuze, en een dead band zou doseren vertragen —
   dus geen patch, wel context bij het waarom van het schakelgedrag.)
4. **30-minuten-kwantisatie** van temp-duren (regel 1567) maakt de textuur grof: 31 min behoefte
   wordt 30 of 60.

Bij **dynamic ISF (log-modus)** komt er nog een verscherper bij: de voorspellingscurves gebruiken
een *ongeclampte* dynamische ISF terwijl de dosering de geclampte gebruikt (regels 903-951 vs.
635) — voorspellingen vallen daardoor steiler dan de doseerlogica aanneemt, wat extra
SMB-aan/uit-gewissel geeft (DEELS, mechanisme bevestigd).

**Wat je níet moet willen** (bewust geen voorstel): een dode band rond target of het uitsmeren van
zero-temps naar langere gedeeltelijke verlagingen. Beide maken het beeld rustiger, maar doseren
per definitie later — precies wat je zelf al als bezwaar benoemde. Met patches 0001+0002 wordt
het patroon eerlijker en minder schokkerig zonder die prijs.

---

## 2. Hoe de keten in elkaar zit (voor de leesbaarheid van §3)

1. **Swift-bridge** (`OpenAPS.swift`) verzamelt glucose (laatste 72 punten), pomphistorie, carbs,
   profiel, TDD-statistieken en override-instellingen, en voert die als JSON aan een
   JavaScriptCore-context met de gebundelde oref-scripts.
2. **`glucose-get-last.js`** maakt `glucose`, `delta` (~laatste 5 min), `short_avgdelta`
   (~5-17,5 min), `long_avgdelta` (~20-42,5 min).
3. **IOB** (`lib/iob/`): pomphistorie → discrete doses (temp-basalen in 0,05 U-pseudobolussen) →
   exponentiële activiteitscurve → `iobArray` met per-5-min activiteit, incl. parallelle
   `iobWithZeroTemp`-reeks.
4. **Meal/COB** (`lib/meal/`, `cob.js`): koolhydraatinvoer + deviatie-gebaseerde absorptie →
   `mealCOB`, absorptiehellingen.
5. **Autosens** (`autosens.js`): 8 h/24 h deviatie-analyse (maaltijd- en UAM-vensters
   uitgesloten) → ratio die ISF/basaal/target schaalt; de laagste van beide vensters wint.
6. **`determine-basal.js`**: bouwt vier voorspellingscurves (IOB, ZT, COB, UAM), destilleert
   daaruit `eventualBG`, `minPredBG` (doseerbasis) en `minGuardBG` (waakvloer), en loopt dan een
   beslissingscascade af: CGM-foutcondities → LGS/zero-temp → onder target → dalend →
   in range → boven target (SMB + compenserende temp, of hoge temp).

---

## 3. Bevindingen

### 3.1 Bevestigde bugs, op volgorde van gewicht

| # | Bevinding | Waar | Ernst | Herkomst |
|---|-----------|------|-------|----------|
| 1 | Zero-temp-duren onder override factor² te kort | `determine-basal.js:1276,1359,1555` | Hoog | Trio-fork |
| 2 | Verlopen overrides blijven dosering sturen in achtergrond | `OpenAPS.swift:512-517` + `HomeRootView.swift:~258` | Hoog | Trio |
| 3 | Vastgelopen-CGM-detectie uit het actiepad; restant is dode code | `determine-basal.js:424-443` | Hoog | Trio-fork (bewust, half af) |
| 4 | Geïnverteerde lage-temp-formule naast SMB | `determine-basal.js:1571` | Middel | upstream |
| 5 | CGM-`noise`-veld wordt niet gebridged; ruis-vangnetten permanent dood | `AlgorithmGlucose.swift` (encoder) | Middel | Trio |
| 6 | TDD-berekening: 24 h-fetch gecapt op 288 events | `PumpHistoryStorage.swift:271-279` | Middel | Trio |
| 7 | SMB-uit-schema: `new Date(uur)` + kapotte gelijkheidstak | `determine-basal.js:53-69` | Middel | Trio-fork |
| 8 | Synthetische zero-temp-events zonder timestamp → verkeerde basaal in ZT-predicties | `iob/history.js:368-378,518-521` | Middel | upstream |
| 9 | `'use strict'`/var-declaraties verwijderd + JSContext-pool nooit gereset | `iob/*`, `JavaScriptWorker.swift` | Middel | Trio-fork |
| 10 | 0,05 U-pseudobolus-dode band wist kleine netto-tempinsuline uit IOB | `iob/history.js:551-563` | Middel | upstream |
| 11 | Temp-target-sortering met boolean-comparator | `autosens.js:429` | Laag | upstream |
| 12 | Carb-dedupe vergelijkt verkeerd tijdstempelveld | `meal/history.js:72-93` | Laag | upstream |
| 13 | `insulinForManualBolus` mengt mg/dl en mmol (vestigiaal) | `determine-basal.js:1213,1400,1422` | Laag | Trio-fork |
| 14 | Divers klein: NaN-logs, dubbele logwaarde, fantoom-0g-carbentry per loop, weggegooide Swift-klok, dubbel identiek profiel, nil-datum→"nu" | zie §3.1-detail | Laag | gemengd |

**Detail bij de belangrijkste:**

**1. overrideFactor-precedentie** — zie `patches/README.md` (patch 0001). Bij 50% override wordt
een LGS-zero-temp die 120 min zou moeten duren op 30 min uitgerekend; de `Math.max(30,…)`-klem
redt het minimum, maar de bescherming bij een stilgevallen loop is dan alsnog 4× te kort.

**2. Override-verval alleen in de view-laag.** `prepareTrioCustomOrefVariables` neemt
`useOverride` rechtstreeks over uit de Core-Data-vlag `enabled`; het predicaat
(`OverrideStored+helper.swift:9-18`) checkt niet of de duur verstreken is, en de enige plek die
een afgelopen override op `enabled = false` zet is SwiftUI-code in `HomeRootView` die pas draait
als het Home-scherm rendert. Draait de app in de achtergrond door (het normale regime), dan
blijven percentage, target en SMB-uit van een verlopen override de dosering sturen tot de
gebruiker de app opent. Fix-richting: verval afdwingen in het doseerpad zelf — in
`fetchActiveOverrides` of direct na de fetch `date + duration` tegen "nu" toetsen (en de JS krijgt
`duration` al aangeleverd, maar doet er ook niets mee).

**3. Vastgelopen sensor.** Upstream zet `tooflat=true` (BG > 60, delta 0, korte/lange gemiddelden
binnen ±1) en neemt dat mee in de actie-gate die hoge temps neutraliseert. In de fork logt de
conditie alleen nog voor `fakecgm`; de strengere resttak (regel 435) zet enkel `rT.reason`, die
op regel 1157 onvoorwaardelijk wordt overschreven — netto nul effect. De fork-commit
("Remove short and long delta condition to avoid early exit breaking loop") suggereert dat de
oude gate vals-positief was, mogelijk mede door Trio's eigen smoothing — maar het huidige
resultaat is dat een sensor die met verse tijdstempels dezelfde waarde blijft sturen (reëel
xDrip/bridge-faalpatroon dat de `minAgo > 12`-check niet vangt) gewoon doorgedoseerd wordt,
inclusief lopende hoge temps. Aanbeveling: de vlag herstellen in de gate, eventueel uitgezonderd
wanneer smoothing actief is; minimaal de dode tak verwijderen zodat de code niet suggereert te
beschermen waar hij dat niet doet.

**6. TDD-cap 288.** Een SMB+UAM-gebruiker produceert makkelijk > 288 pompevents per etmaal (elke
cyclus een temp-event plus regelmatig een SMB). De fetch pakt de nieuwste 288, dus het
TDD-venster krimpt stilzwijgend onder de 24 h en `currentTDD`/`weightedAverage` onderschatten.
Richting is conservatief (dynISF wordt zwakker), maar het vertekent ook `tdd24h_14d_Ratio` en
daarmee `tddAdjBasal`. Fix is triviaal: limiet weg (het 24 h-predicaat begrenst al) of normeren op
het wél berekende maar ongebruikte `calculatePumpDataHours`.

**8. Timestamp-loze synthetische events.** De kunstmatige toekomst-zero-temp waarmee
`iobWithZeroTemp` (de basis van de ZT-waakcurve!) wordt gebouwd, mist een `.timestamp`;
`basalLookup(new Date(undefined))` faalt stil naar het *laatste* basaalsegment van de dag. De
eerste 30 min van elke geprojecteerde zero-temp rekent dus met een mogelijk verkeerd
basaaltarief. Wie 's avonds een hoger segment heeft, krijgt een te optimistische ZT-curve op
andere momenten van de dag.

**9. Implicit globals + contextpool.** De fork verwijderde `'use strict'` en enkele
`var`-declaraties (pure regressies t.o.v. upstream); tegelijk hergebruikt `JavaScriptWorker` vijf
JSContexts eeuwig zonder reset, en pint `inCommonContext` niet werkelijk één context — de
volgorde klopt alleen door LIFO-toeval zolang niets concurrent draait. Stale globals uit een
vorige run kunnen zo een volgende run in lekken. Fix: declaraties terug, en de gepinde context
echt doorgeven (of per invocatie een verse context).

**14. Divers klein (allemaal bevestigd):** NaN in de maxIOB-logregels (patch 0004); "target_bg
from X to X"-log (patch 0004); elke echte loop krijgt een fantoom-carbentry van 0 g met tijdstempel
"nu" aangehangen (`simulatedCarbsAmount ?? 0` maakt de optional non-nil) — nu onschadelijk door
JS-truthiness, maar fragiel; de prepare-shim overschrijft de door Swift meegegeven klok met
`new Date()` (regel 5 van `prepare/determine-basal.js`), wat backdating/simulatie-consistentie
breekt; `createProfiles` genereert twee byte-identieke profielen met autotune hard op null;
glucose-entries zonder datum krijgen bij het encoden "nu" als tijdstempel.

### 3.2 Dynamic ISF — aparte vermelding (alleen relevant als je het aanzet)

De dynISF-laag is het minst volwassen deel van de keten. Bevestigde kern per bevinding
(alle DEELS: mechanisme klopt, effectgrootte hangt van instellingen af):

- **Profiel-ISF en overrides vallen algebraïsch weg** in de log-modus: binnen het clampvenster is
  de effectieve ISF exact `1800/(AF·TDD·ln(BG/insulinFactor+1))` — je profiel-ISF bepaalt alleen
  nog wáár de autosens-min/max-klemmen bijten. Wie zijn ISF tunet en denkt dat dat doorwerkt,
  vergist zich. Bovendien satureert de ratio bij gangbare waardes al rond BG ~150 op de
  autosens_max-rail: het "dynamische" is in de praktijk vaak een stapfunctie.
- **`insulinFactor = 120 − piektijd`**: zie §1.1c.
- **Voorspellingen vs. dosering inconsistent**: ongeclampte dynISF in de predicties (regels
  903-951), geclampte in de dosering (regel 635) → extra SMB-flip-flop; sigmoid-gebruikers
  krijgen in de predicties zelfs helemaal geen dynISF.
- **Het recente-TDD-signaal telt dubbel** (ISF-formule én `tddAdjBasal` én sigmoid-exponent
  delen dezelfde bron): meer insuline vandaag → hogere TDD → sterkere dosering morgen — een
  positieve terugkoppeling, begrensd alleen door de clamps.
- **Autosens wordt onvoorwaardelijk overschreven** (regel 342) zodra dynISF aanstaat — de hele
  24 h-deviatie-analyse draait dan voor niets (en `sensitivityRatio` is via een uitgecommentarieerde
  declaratie stiekem een implicit global geworden, regel 499/517).

Advies: dynISF-gebruik goed begrijpen vóór aanzetten; architectureel zou blenden met (i.p.v.
vervangen van) profiel-ISF en één gedeeld sensitiviteitsmodel voor predicties én dosering veel
oplossen.

### 3.3 Autosens — degelijk, met één structurele kanttekening

De opzet (deviatie-percentielen, maaltijdexclusie, demping bij weinig data, laagste van 8 h/24 h
wint) is verdedigbaar en conservatief. Twee punten verdienen aandacht:

- **De hoge-IOB-exclusie** (`iob > 2× huidige basaal` → datapunt telt als "UAM" en wordt
  weggegooid, regel 274) gooit óók negatieve deviaties weg — juist de sensitiviteitssignalen.
  Een SMB+UAM-gebruiker zit na maaltijden urenlang boven die drempel, dus autosens ziet bij hen
  structureel weinig data en drijft door de nul-padding richting 1,0. Bewuste
  confounder-exclusie (maaltijdruis hoort er niet in), maar het maakt autosens traag/inert voor
  precies deze gebruikersgroep. (Door mij bevestigd)
- **De normalisatie** `ratio = 1 + basalOff/max_daily_basal` deelt door het *piek*-basaaltarief
  van de dag — wie een piekerig basaalprofiel heeft krijgt gedempte ratio's; en de
  percentiel-50-keuze plus schaling via één scalaire `profile.sens` zijn onafgeleid. Werkt in de
  praktijk, maar statistisch huisvlijt. (Door mij bevestigd)
- Klein: de temp-target-sortering met boolean-comparator (regel 429, kapot maar zelden geraakt),
  de prepare-shim draait de detectie twee keer op gedeelde muteerbare glucose-objecten (de
  24 h-run ziet door de 8 h-run gemiddelde waardes bij sub-2-min-metingen), en de rewind-scan
  slaat `history[0]` over.

### 3.4 Wat goed in elkaar zit (en met rust gelaten kan worden)

Voor de balans: de gelaagdheid minGuardBG → threshold → maxIOB → maxBolus → maxSafeBasal →
SMB-interval is een robuust diepteverdedigingsontwerp; de asymmetrische delta-demping (§1.2) is
slim; de carbsReq-reddingsberekening (regel 1233-1254) is een onderschat vangnet; de
COB/UAM-blending op `fractionCarbsLeft` (regel 1056-1128) is een verstandige middenweg tussen
aangekondigde en niet-aangekondigde maaltijden; en de exponentiële IOB-curve met parallelle
zero-temp-projectie is de juiste architectuur voor de waakvloer.

---

## 4. Patchvoorstellen

In `oref-review/patches/`, elk los toepasbaar, met uitgebreide toelichting in de README aldaar:

1. **0001** — overrideFactor-precedentie in zero-temp-duren (bugfix, veiligheidsherstel).
2. **0002** — lage-temp-formule naast SMB ontinverteren (bugfix; direct effect op het
   terugtrek-gevoel, zonder later/minder te doseren; tevens upstream-issue-kandidaat).
3. **0003** — SMB-schema-uurvergelijking repareren (bugfix).
4. **0004** — logcosmetica (NaN-logs e.d.).

Nadrukkelijk: voorstellen ter review, niet klinisch gevalideerd. Na toepassen bundle regenereren.

## 5. Aanbevelingen zonder patch (teamdiscussie nodig)

Op volgorde van verwacht rendement:

1. **Override-verval in het doseerpad afdwingen** (§3.1-2) — Swift-wijziging, klein maar raakt
   gedragssemantiek.
2. **Vastgelopen-CGM-gate herstellen of dode code verwijderen** (§3.1-3) — vereist een besluit
   over de interactie met Trio's smoothing.
3. **`noise`-veld bridgen** of de dode ruis-vangnetten expliciet documenteren als
   niet-functioneel (§1.2).
4. **TDD-fetchlimiet 288 weghalen** (§3.1-6) — triviale fix.
5. **Timestamps op synthetische pompevents** (§3.1-8).
6. **`'use strict'` terug + contextpool-hygiëne** (§3.1-9).
7. **minPredBG-wachttijd koppelen aan `insulinPeakTime`** i.p.v. hard 90 min (§1.1c) — kleine
   wijziging, wél gedragseffect: sneller SMB-herstel bij snelle insulines; eerst simuleren.
8. **Mediaanfilter of smoothing-advies voor de delta-keten** (§1.2).
9. **dynISF-architectuur** (§3.2) — het grootste maar meest ingrijpende punt; minimaal de
   predictie/dosering-inconsistentie gelijktrekken en de profiel-ISF-cancelling documenteren.
10. `insulinForManualBolus`-eenhedenmix opruimen of het veld verwijderen (vestigiaal; de echte
    boluscalculator rekent in Swift en gebruikt het niet).

## 6. Wat niet (diepgaand) is onderzocht

Autotune (staat in Trio effectief uit — de bridge levert altijd `null`), de profielopbouw
(`lib/profile/`), temp-target-gedrag end-to-end, pump-suspend-randgevallen in de praktijk,
Nightscout-upload/remote-carbs, de Live Activity/watch-paden, en gedragssimulatie met echte
CGM-datasets (de logische vervolgstap om patches 0001/0002 en aanbeveling 7 te valideren vóór
enige inzet op een lichaam).

---

*Methodologische voetnoot: 7 module-lezers → 71 kandidaat-bevindingen → adversariële verificatie
per bevinding (met upstream-oref0-vergelijking waar relevant); autosens- en bridge-verificaties
handmatig uitgevoerd. Weerlegde claims (o.a. "zero-width targetband is een bug" — het is een
bewuste keuze) zijn niet in dit rapport opgenomen, behalve waar het waarom leerzaam was.*
