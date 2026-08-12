# Patchvoorstellen bij de oref-review

**Status: voorstellen.** Deze diffs zijn bedoeld als concreet startpunt voor discussie en review
door het Trio-team — ze zijn *niet* klinisch gevalideerd en niet bedoeld om zonder simulatie,
tests en review op een echt lichaam te draaien.

Alle patches raken alleen `trio-oref/lib/determine-basal/determine-basal.js`. Na toepassen moet
de JavaScript-bundle opnieuw gegenereerd worden (webpack, zie `trio-oref/webpack-cp.sh`), anders
draait de app nog op de oude bundle in `Trio/Resources/javascript/bundle/`.

Toepassen (vanaf de repo-root):

```sh
git apply oref-review/patches/0001-*.patch   # enz.
```

Elke patch is los toepasbaar; ze zijn getest met `git apply --check` en de volledig gepatchte
file is gevalideerd met `node --check`.

| # | Patch | Type | Effect op dosering |
|---|-------|------|--------------------|
| 0001 | overrideFactor-precedentie in zero-temp-duur | Bugfix (Trio-fork) | Ja — alleen bij actieve procent-override: zero-temp-duur wordt correct geschaald i.p.v. met factor² fout |
| 0002 | Geïnverteerde lage-temp-formule naast SMB | Bugfix (upstream-erfenis) | Ja — zelfde hoeveelheid teruggehouden insuline, maar correct verdeeld; kleine terugtrekbehoeftes geven niet langer een diepe 30-min verlaging |
| 0003 | SMB-schema-uurvergelijking (`new Date(uur)`) | Bugfix (Trio-fork) | Alleen bij gebruik van geplande SMB-uit-vensters in overrides |
| 0004 | Log-cosmetica (NaN-logs, dubbele waarde) | Cosmetisch | Nee — alleen logregels |

## 0001 — overrideFactor-precedentie in zero-temp-duurberekening

Op drie plekken (regels 1276, 1359, 1555) staat:

```js
durationReq = round(60*worstCaseInsulinReq / profile.current_basal*overrideFactor);
```

Door operatorvolgorde is dit `(60*W / basaal) * factor`, terwijl de bedoeling
`60*W / (basaal * factor)` is (de effectieve basaal onder een override — zie de wél correct
gegroepeerde `zeroTempEffect` op regel 1242). Met een verlaagde override (factor < 1) worden
zero-temp-duren een factor *kwadraat* te kort: bij 50% override rekent een LGS-zero-temp die
120 min zou moeten zijn uit op 30 min. Dat verzwakt de hypobescherming precies op het moment
dat de gebruiker heeft aangegeven minder insuline nodig te hebben. Upstream oref0 heeft deze
factor helemaal niet (daar bestaat het override-concept niet); de fout zit in de Trio/iAPS-toevoeging.

## 0002 — Geïnverteerde lage-temp-formule naast een SMB

Regel 1571 zet, als er minder dan 30 minuten zero-temp nodig is (`durationReq` minuten),
een 30-minuten lage temp op:

```js
smbLowTempReq = round( basal * durationReq/30 ,2);
```

Een 30-min temp op rate *r* houdt `(basaal − r) × 0,5 h` insuline in; nodig is
`basaal × durationReq/60`. Gelijkstellen geeft `r = basaal × (1 − durationReq/30)` — precies het
omgekeerde van wat er staat. Gevolg nu: een *kleine* terugtrekbehoefte (bijv. 6 min) levert een
diepe verlaging op (0,2× basaal gedurende 30 min = 4× te veel ingehouden), en een behoefte van
bijna 30 min levert juist een bijna-neutrale temp (4× te weinig). Alleen bij exact 15 min klopt
het. Dit is een belangrijke verscherper van het "na elke SMB wordt alles teruggetrokken"-gevoel:
juist marginale correcties zien er nu uit als een forse terugtrekking. De fix houdt exact dezelfde
hoeveelheid insuline in als het algoritme berekent — niets wordt later of minder gedoseerd.
De formule staat zo ook in upstream oref0 (erfenis), dus dit is tegelijk een kandidaat voor een
upstream-issue.

## 0003 — SMB-schema-uurvergelijking

Regel 53: `let currentHour = new Date(time.getHours());` maakt een `Date` van het uurgetal
(geïnterpreteerd als milliseconden sinds epoch). De relationele vergelijkingen (`>=`, `<`)
werken daarna per toeval (numerieke coercion), maar de gelijkheidstak
`currentHour == startTime` (regel 66) is altijd `false` omdat `Date == number` via
string-conversie loopt. Gevolg: bij een gepland SMB-uit-venster met `start == eind ≠ 0` wordt
SMB nooit uitgeschakeld terwijl de gebruiker dat wel heeft ingesteld. Fix: gewoon het getal
gebruiken.

## 0004 — Log-cosmetica

- Regels 1467/1473: `"…" + max_iob-iob_data.iob` evalueert links-naar-rechts naar `NaN` in de
  log ("SMB limited by maxIOB: NaN"). Haakjes toegevoegd.
- Regel 586: logde twee keer de níeuwe target ("target_bg from X to X"); logt nu oud → nieuw.
- Regel 614: logde `new_target_bg`, die in deze tak `undefined` kan zijn; logt nu de werkelijke
  oude target.

Geen gedragswijziging; wel betrouwbaardere logs om looprapporten mee te debuggen.
