# Review gebruiksvoorwaarden (Terms of Use v1.01)

**Aan:** Ray (Brightmotive Services bv)
**Datum:** 26 augustus 2026
**Onderwerp:** doet de bestaande clickwrap wat hij moet doen, sluit hij aan op de klant-AV v3.11, hoe maken we hem geschikt voor álle gebruikers (garages voorop), en kan invoering nu al
**Bronnen:** `12-gebruiksvoorwaarden-v1.01-huidig.md` (verbatim tekst), `voorwaarden-versies/Voorwaarden-v3.11.md`, `voorwaarden-versies/Voorwaarden-v3.04.md`, `01-memo-beschermingsstrategie.md`, `07-documentenstructuur.md`

---

## Kernbevindingen

1. **Het document doet zijn belangrijkste werk wél.** Klikken op een vinkje is naar Nederlands recht een geldige manier om een contract te sluiten, en dit document is precies de "redelijke geheimhoudingsmaatregel" die de Wet bescherming bedrijfsgeheimen eist. Niet weggooien — repareren en uitbreiden.
2. **Maar het is geschreven voor developers.** Engelstalig, NDA-zwaar, met plichten (teruggeven, vernietigen, meewerken aan inspectie) die voor een garagemonteur zinloos en onuitvoerbaar zijn.
3. **De boete is het zwakste punt.** € 10.000 per overtreding plus € 3.000 per dag, op élke verplichting — ook op "je e-mailadres niet actueel houden". Tegen een individuele medewerker is dat vrijwel zeker niet inbaar (de rechter matigt), waarschijnlijk vernietigbaar, en commercieel schadelijk. Bovendien overbodig: via de nieuwe AV is de klánt al aansprakelijk voor alles wat via zijn accounts gebeurt.
4. **De medewerker bindt zijn werkgever niet.** Een monteur die klikt, tekent voor zichzelf. De brug naar het bedrijf loopt via artikel 1.2 van de AV — en die brug bestaat alleen als dat bedrijf klant is. Bij garages is dat niet zo.
5. **Vier gebreken die je hoe dan ook moet repareren:** de aansprakelijkheidsuitsluiting sluit ook opzet uit (houdt geen stand); artikel 6.3 verklaart met terugwerkende kracht álles geheim wat ooit openbaar op de docs-site stond (onbepaalbaar en feitelijk onjuist); er is geen enkele verwijzing naar een privacyverklaring terwijl je voor accountgegevens zelf verantwoordelijke bent; en de dwingend-rechtelijke uitzonderingen die in AV 3.6 wél staan, ontbreken hier volledig.
6. **Aansluiting op v3.11: geen ramp, wel drie botsingen** — rangorde (de ToU presenteert zichzelf als de hele overeenkomst, de AV zeggen dat zíj voorgaan), boetestapeling (klant én medewerker beboet voor hetzelfde feit) en forum (90 dagen verplicht overleg/mediation in de ToU, direct naar de rechter in de AV). Alle drie op te lossen met een handvol zinnen.
7. **Voorstel: twee documenten in plaats van één.** Een lichte set voor iedereen die inlogt (account, doelbinding, geen scraping/AI, lichte geheimhouding, privacy, handhaving zónder persoonlijke boete) en een zware set voor wie developer- of admindocumentatie opent (de huidige NDA, gerepareerd, met een herontworpen boete).
8. **Invoeren kan nu, ook bij klanten op v3.04.** De gebruiksvoorwaarden zijn een eigen contract tussen Brightmotive en de gebruiker; de klant is daar geen partij bij. Er draait bovendien al jaren een clickwrap zonder haakbepaling. Het risico is een zwak verwijt van een ontevreden klant, geen juridisch gat.
9. **Eén harde voorwaarde bij de uitrol:** leg vast wie wanneer op welke tekstversie akkoord klikte. Zonder dat logbewijs bestaat de hele maatregel juridisch niet en is de invoering weggegooid werk.
10. **Eén reparatie in v3.11 zelf:** de zin "U zorgt ervoor dat uw gebruikers die voorwaarden aanvaarden en naleven" is bij het inkorten uit artikel 1.6 verdwenen. Terugzetten vóór publicatie — nu gratis, later een AV-wijziging.

---

## A. Juridische toets van de huidige v1.01

### A.1 Totstandkoming: de klik werkt, de rest niet

**Wat goed is.** Naar Nederlands recht is er geen vormvereiste voor een contract als dit. Een aanbod (het acceptatiescherm) en een aanvaarding (het aanvinken en doorklikken) leveren een geldige overeenkomst op (art. 6:217 BW). Dat een clickwrap werkt, is in Nederland niet omstreden. De formulering van de aanhef — "By checking the box … you agree to be bound" — is precies wat je wilt: een actieve, ondubbelzinnige handeling.

**Wat niet werkt: het browsewrap-deel.** De aanhef en artikel 2.1 zeggen óók dat de voorwaarden tot stand komen "by accessing or using the Documentation in any way", dus enkel door te kijken. Dat is naar Nederlands recht in beginsel geen wilsuiting (art. 3:33 BW) en de gebruiker heeft ook geen gerechtvaardigd vertrouwen gewekt (art. 3:35 BW) als hij de tekst nooit heeft gezien. Dit deel is vooral sier. Praktische consequentie: zorg dat de documentatie technisch onbereikbaar is zonder klik. Alles wat langs de klik heen te lezen is, valt buiten het contract — en verzwakt bovendien je bedrijfsgeheimenclaim (zie A.10).

**Elektronische contractsluiting (art. 6:227a–c BW).** Art. 6:227a BW stelt de elektronische overeenkomst gelijk aan een schriftelijke, mits de tekst raadpleegbaar is, de authenticiteit voldoende is gewaarborgd, het moment van totstandkoming vaststaat en de identiteit van partijen vaststelbaar is. Die vier eisen zijn een checklist voor je acceptatiescherm, en ze vallen samen met het bewijspunt hieronder. Art. 6:227b (informatieplichten) en 6:227c BW (onder meer: de mogelijkheid om invoerfouten te herstellen vóór aanvaarding) gelden ook hier; jegens niet-consumenten mogen ze contractueel worden uitgesloten (art. 6:227b lid 6 en 6:227c lid 5 BW), maar de ToU doet dat niet. Niet-naleving van art. 6:227c lid 1 maakt de overeenkomst **vernietigbaar** (lid 4). Dat is met twee regels op te lossen: (i) neem de uitsluitingszin op voor zakelijke gebruikers, én (ii) bouw hoe dan ook een bevestigingsstap in — die is technisch triviaal en haalt het hele risico weg.

**Bewijs van acceptatie is het echte punt.** Wie zich op een contract beroept, moet het bewijzen (art. 150 Rv). Nodig, en nu voor zover bekend niet structureel ingericht:
- per acceptatie: gebruikers-id, naam, e-mailadres, organisatie, tijdstempel, IP-adres, en de **hash of het versienummer van de exacte tekst** die op dat moment werd getoond;
- een onveranderlijk versiearchief van alle teksten (de pagina is een bestand in de `brightmotive-docs`-repository — koppel het acceptatielog aan de commit-hash, dat is de goedkoopste sluitende oplossing);
- een bewaartermijn die aansluit bij de verjaringstermijnen (art. 3:307/3:310 BW), dus minimaal vijf jaar na het einde van het account.

Dit staat al als maatregel 2 op de maatregelenlijst en als waarschuwing in memo §4.2. Het is de enige stap die zónder tekstwijziging al waarde toevoegt, en zonder deze stap is elke tekstwijziging waardeloos.

**Wijziging via artikel 13.2 (voortgezet gebruik = aanvaarding).** Dit is een gebruikelijk beding, maar als zelfstandige grondslag voor gebondenheid aan een nieuwe versie is het zwak: er is geen wilsuiting, alleen stilzitten. Jegens een gebruiker die als quasi-consument kan worden aangemerkt, valt zo'n eenzijdige wijzigingsbevoegdheid bovendien in de buurt van de grijze lijst (art. 6:237 sub c BW). Advies: gebruik 13.2 alleen voor redactionele wijzigingen en laat bij elke materiële wijziging opnieuw klikken. Dat is technisch niets en juridisch alles.

### A.2 Dit document is zélf een set algemene voorwaarden

**Kwalificatie.** Art. 6:231 sub a BW: bedingen die zijn opgesteld om in een aantal overeenkomsten te worden opgenomen, met uitzondering van de kernbedingen. Dat is dit document precies. De titel "Terms of Use" verandert daar niets aan; de uitleg gaat naar de inhoud. Gevolg: de hele afdeling 6.5.3 BW is van toepassing.

**Terhandstelling / beschikbaarstelling (art. 6:233 sub b jo. 6:234 BW).** Bij een langs elektronische weg gesloten overeenkomst voldoe je aan de informatieplicht door de voorwaarden vóór of bij het sluiten "op zodanige wijze langs elektronische weg ter beschikking te stellen dat deze door hem kunnen worden opgeslagen en toegankelijk zijn ten behoeve van latere kennisneming" (art. 6:234 lid 2 BW). Een webpagina die de gebruiker moet doorscrollen voldoet daar niet vanzelf aan: hij kan de tekst niet opslaan en na blokkering van zijn account is de pagina mogelijk onbereikbaar. Reparatie is klein en volledig effectief:
- een downloadbare PDF met versienummer op het acceptatiescherm, én
- automatische toezending van de tekst per e-mail direct na acceptatie (dat levert meteen het bewijsstuk op).

**Vernietigbaarheid.** Bij niet-naleving kan de wederpartij het beding vernietigen (art. 6:233 sub b BW), maar alleen als hij geen "grote partij" is in de zin van art. 6:235 lid 1 BW (publicatieplichtige jaarrekening of meer dan 50 werknemers). Een individuele garagemedewerker, een zzp-monteur en een kleine garage vallen daar **niet** onder en kunnen dus wél vernietigen. Grote grossiers en inkooporganisaties meestal wel. Kortom: precies bij de groep die je nu wilt toevoegen, is het vernietigingsrisico het grootst.

**De open toets van art. 6:233 sub a BW.** Een beding is onredelijk bezwarend gelet op de aard en overige inhoud van de overeenkomst, de wijze van totstandkoming, de wederzijds kenbare belangen en de overige omstandigheden. Bij een niet-onderhandelde, Engelstalige set met een boete van € 10.000 tegenover een medewerker die er zelf niets aan verdient, is die toets een reëel risico — niet theoretisch.

**Zwarte en grijze lijst: de kwalificatievraag.** Art. 6:236/6:237 BW gelden alleen voor consumenten (natuurlijke personen die niet handelen in de uitoefening van beroep of bedrijf). Een garagemedewerker handelt in de uitoefening van het bedrijf van zijn wérkgever, niet van een eigen bedrijf. Er valt daarom serieus te betogen dat hij, wanneer hij persoonlijk gebonden wordt, als consument kwalificeert. Dat is niet uitgemaakt, maar zelfs als een rechter dat niet aanneemt, werkt de grijze lijst door als gezichtspunt in de open toets van 6:233 sub a (reflexwerking). Relevant zijn dan met name:
- **art. 6:237 sub i BW** — een beding dat de wederpartij bij niet-nakoming een geldsom laat betalen, tenzij het een redelijke schadevergoeding betreft: dat is artikel 9.2, en het staat daarmee onder een vermoeden van onredelijke bezwarendheid;
- **art. 6:237 sub f BW** — beperking van de aansprakelijkheid van de gebruiker van de voorwaarden: dat is artikel 10;
- **art. 6:236 sub n BW** (zwarte lijst) — een beding dat geschilbeslechting aan een ander dan de rechter opdraagt: dat is de SGOA-arbitrage van artikel 12.6.

### A.3 Het boetebeding van artikel 9.2 — de grootste zwakte

De tekst: bij het niet nakomen van **"one or more of the obligations under the Terms of Use"** verbeurt de gebruiker, **zonder toerekenbaarheid en zonder ingebrekestelling**, direct € 10.000 per overtreding plus € 3.000 per dag dat de overtreding voortduurt, zonder plafond.

**Ontwerpfout 1: één eenheidsboete op alle verplichtingen.** Dit is exact het patroon dat de matigingsrechtspraak afstraft. In HR Turan/Easystaff (ECLI:NL:HR:2018:207) werd van € 1,23 mln. gevorderde boete € 21.150 toegewezen, juist omdat één uniform bedrag gold voor sterk uiteenlopende overtredingen. Hier geldt hetzelfde bedrag voor "documentatie doorspelen aan een concurrerende bouwer" en voor "je e-mailadres niet actueel houden" (art. 4.1) of "niet meewerken aan een inspectie" (art. 7.3 sub c). Vergelijk artikel 3.7 van v3.11: dat hangt de boete alleen aan een afgebakend cluster (3.1 t/m 3.5 en 3.9), differentieert naar zwaarte, en kent een plafond. Het verschil in kwaliteit is groot en zichtbaar.

**Ontwerpfout 2: een onbegrensde dagboete die stil oploopt.** € 3.000 per dag is ruim € 1,09 mln. per jaar, en de dagboete begint te lopen zonder dat de gebruiker weet dat hij in overtreding is. Ook dit is een bekende matigingsgrond. Artikel 3.7 AV doet het beter: de dagboete loopt pas vanaf de dag ná de schriftelijke melding, en er is een totaalplafond.

**Ontwerpfout 3: geen enkele relatie tot de contractswaarde.** De gebruiker betaalt niets. Er is dus geen enkel aanknopingspunt voor proportionaliteit — terwijl juist het meeschalen met de jaarvergoeding de kern is van het matigingsbestendige ontwerp van artikel 3.7 (memo §4.1).

**Ontwerpfout 4: verschuldigd zonder toerekenbaarheid.** "Without imputability … being required" betekent dat de boete óók verschuldigd is als de gebruiker geen enkel verwijt treft. Contractueel mag je van art. 6:75 BW afwijken, maar het versterkt zowel het matigings- als het onredelijk-bezwarend-verwijt aanzienlijk.

**Matiging (art. 6:94 BW).** De matigingsbevoegdheid kan niet worden weggecontracteerd (lid 3, dwingend recht). De maatstaf is terughoudend: matiging alleen als de billijkheid dit klaarblijkelijk eist, dat wil zeggen als toepassing van het beding tot een "buitensporig en daarom onaanvaardbaar resultaat" leidt (HR Intrahof/Bart Smit, ECLI:NL:HR:2007:AZ6638). De rechter kijkt daarbij naar de verhouding tussen werkelijke schade en boete, de aard van de overeenkomst, de inhoud en strekking van het beding en de omstandigheden van het geval. Een niet-onderhandelde eenheidsboete van € 10.000 plus een onbegrensde dagboete, tegenover een natuurlijk persoon zonder eigen commercieel belang bij de overtreding, scoort op vrijwel elk gezichtspunt slecht. **Realistische verwachting: forse matiging, mogelijk tot nihil.**

**Bindt het de werkgever?** Waarschijnlijk niet. De medewerker die klikt, verbindt in beginsel alleen zichzelf. Om de garage of grossier te binden is vertegenwoordigingsbevoegdheid nodig (art. 3:60 e.v. BW), en een monteur heeft doorgaans geen volmacht om zijn werkgever aan een NDA met een boete van € 10.000 te binden. Op art. 3:61 lid 2 BW (schijn van volmacht) valt soms een beroep te doen — bijvoorbeeld als de werkgever de uitnodiging zelf verstuurde — maar dat is per geval feitelijk en niet iets waarop je een handhavingsstrategie bouwt. Artikel 2.2 van de ToU ("the User declares and guarantees that the actions … have taken place by an authorised person") helpt hier niet: dat is een garantie **van de klikkende medewerker zelf**. Wordt zij geschonden, dan heb je een vordering op diezelfde medewerker — niet op zijn werkgever. Conclusie: de ToU bindt in de praktijk de persoon, niet het bedrijf. De brug naar het bedrijf loopt uitsluitend via artikel 1.2 van de AV, en bestaat dus alleen bij klanten. Bij garage-gebruikers, die géén contractspartij van Brightmotive zijn, ontbreekt die brug volledig.

**Arbeidsrechtelijke context.** Art. 7:650/7:651 BW (boetebeding in de arbeidsovereenkomst, met vormvereisten en een maximum) zijn hier niet rechtstreeks van toepassing: Brightmotive is niet de werkgever. Maar de ratio — de wetgever beschermt de individuele werknemer tegen boetes van zijn contractuele wederpartij — kleurt wel de redelijkheidstoets, en dezelfde beschermingsgedachte zie je in art. 7:661 BW (de werknemer is jegens zijn werkgever alleen aansprakelijk bij opzet of bewuste roekeloosheid). Een rechter die een € 10.000-boete tegen een monteur moet beoordelen, heeft dat hele systeem in zijn achterhoofd.

**Commercieel.** Een acceptatiescherm met een boete van € 10.000 is een drempel. De garage is klant van de grossier; de grossier heeft BrightCat gekocht om zíjn klanten te bedienen. Minder actieve garage-accounts betekent minder orders, en dat raakt via de omzetgebonden vergoeding rechtstreeks Brightmotive zelf. En het maakt de grossier tot boodschapper van slecht nieuws bij zijn eigen klanten.

**Wat wél werkt.** Zie C: geen persoonlijke boete voor gewone gebruikers, wél een gerichte en herontworpen boete voor de documentatielaag, en voor alles daarbuiten leunen op de aansprakelijkheid van de klant via AV 1.2 + 3.7.

### A.4 De 10-jaarstermijn (artikel 7.1)

Er is geen wettelijk maximum aan een contractuele geheimhoudingstermijn, dus 10 jaar is op zichzelf toelaatbaar. Het probleem is dat de termijn twee kanten op verkeerd is:
- **Te kort voor echte bedrijfsgeheimen.** De Wbb beschermt informatie zolang zij geheim is — zonder termijn. Artikel 3.2 van v3.11 volgt die lijn correct ("zolang de informatie niet openbaar is"). Een harde einddatum van 10 jaar nodigt uit tot de a-contrario-redenering dat daarna alles vrij is, óók de matching- en verrijkingslogica. Dat ondermijnt precies wat artikel 3.2 wil vastleggen.
- **Te zwaar voor een gewone gebruiker.** Een monteur die tien jaar lang aan een geheimhoudingsplicht met bijbehorende bewaar-, teruggeef- en inspectieplichten vastzit voor het opzoeken van remblokken, is een beding dat de open toets van art. 6:233 sub a BW moeilijk overleeft.

Hetzelfde geldt voor de nevenverplichtingen: artikel 7.3 sub b (informatie teruggeven of, na schriftelijke toestemming, vernietigen) en sub c (meewerken aan toezicht door of namens Brightmotive op de opslag en het gebruik) zijn zinvol jegens een externe softwarebouwer en zinledig jegens een garagemedewerker.

**Advies:** vervang "plus a period of 10 years" door "zolang de informatie niet openbaar is", en verplaats de nevenverplichtingen naar de zware laag.

### A.5 De definitie-opbouw

- **"Documentation" is circulair en te breed.** "Any and all documentation related to the Brightmotive Services, including but not limited to the (source) code" — broncode is geen documentatie. De definitie claimt bij voorbaat meer dan het document feitelijk beschermt, en bij niet-onderhandelde voorwaarden wordt overwegend objectief uitgelegd (glijdende schaal DSM/Fox, ECLI:NL:HR:2004:AO1427). Onduidelijkheid werkt daarbij ten nadele van de opsteller (contra proferentem; voor consumenten dwingend in art. 6:238 lid 2 BW, daarbuiten als gezichtspunt).
- **"Confidential Information" is werkbaar.** Sub (i) is zeer breed maar heeft de gebruikelijke uitzondering voor vrij beschikbare informatie; sub (iii) is de standaard vangnetbepaling. Wat ontbreekt is een **categorielijst** van wat je hoe dan ook als bedrijfsgeheim aanmerkt. Artikel 3.2 van v3.11 heeft die wél (koppel- en API-specificaties, datastructuren, algoritmes, verrijkings- en matchinglogica, prijs- en voorraadlogica). Die lijst is Wbb-technisch waardevol: te vage afbakening is een bekende afwijzingsgrond (Corrosion-lijn, 2025). Neem hem over.
- **"User" is te ruim en daardoor leeg.** De definitie omvat ook "the natural or legal person who uses the Brightmotive Services … in any way" — dat trekt élke BrightCat-gebruiker onder een documentatie-NDA, ook wie nooit documentatie opent en nooit heeft geklikt. Naar Nederlands recht bindt dat niemand zonder aanvaarding. Het is dus een lege claim, en lege claims schaden de geloofwaardigheid van het document bij een rechter.
- **"Agreement" trekt de klant-AV impliciet mee naar binnen.** "The entirety of agreements made between Brightmotive and the User in relation to the Brightmotive Services and the Documentation, including the provisions of these Terms of Use" — daarmee presenteert de ToU zich als de overkoepelende regeling, terwijl AV 1.6 en 7.4 het omgekeerde bepalen. Zie B.1.

### A.6 Artikel 6.3 — de terugwerkende geheimverklaring

> "Under Confidential Information falls – in any way – all information that used to be available on the website https://docs.brightmotive.com."

Twee zelfstandige problemen:

1. **Feitelijk onjuist naar Wbb-maatstaven.** Art. 1 Wbb eist dat de informatie geheim is: niet algemeen bekend of gemakkelijk toegankelijk voor personen binnen de kringen die zich gewoonlijk met dit soort informatie bezighouden. Informatie die openbaar op een website heeft gestaan, voldoet daar per definitie niet aan. Openbaarheid is niet contractueel terug te draaien. Dit beding kan dus nooit een bedrijfsgeheimenclaim dragen.
2. **Onbepaalbaar als contractuele verplichting.** Tussen partijen mág je geheimhouding afspreken over informatie die openbaar is — dat is contractsvrijheid. Maar de gebruiker kan onmogelijk weten wát er ooit op die site heeft gestaan. Een verbintenis moet bepaalbaar zijn (art. 6:227 BW), en een beding dat je niet kunt naleven omdat je de inhoud niet kent, is bovendien onredelijk bezwarend (art. 6:233 sub a BW) — laat staan handhaafbaar met € 10.000 per overtreding.

Hetzelfde geldt in mindere mate voor artikel 6.2 ("information … can, at a later date, become Confidential Information"): zonder kennisgevingsmechanisme is dat niet naleefbaar. Repareer met: "zodra Brightmotive dat schriftelijk meedeelt, en vanaf dat moment".

**Advies:** artikel 6.3 schrappen. Vervang door de bepaalbare formulering van AV 3.2: alles wat alleen na inloggen toegankelijk is, plus de categorielijst. Dat is zowel bepaalbaar als bewijsbaar.

### A.7 Arbitrage en mediationplicht (artikel 12)

**Geldigheid.** Een arbitraal beding kan in algemene voorwaarden worden opgenomen (art. 1021 Rv). Het splitsingsmodel — EU/EER plus Zwitserland naar de rechtbank Midden-Nederland, daarbuiten SGOA-arbitrage — is op zichzelf houdbaar en voor niet-EU-partijen zelfs verstandig, omdat een arbitraal vonnis via het Verdrag van New York veel makkelijker te executeren is dan een Nederlands rechterlijk vonnis. Maar jegens een gebruiker die als consument kwalificeert, staat een arbitragebeding op de zwarte lijst (art. 6:236 sub n BW) en is het dus onherroepelijk vernietigbaar.

**Het echte bezwaar: de verplichte voorfase.** De artikelen 12.2 tot en met 12.4 schrijven eerst 30 dagen minnelijk overleg voor en daarna 60 dagen mediation, vóórdat je naar de rechter of arbiter mag. Dat is 90 dagen. Het draaiboek voor een incident (`04-draaiboek-incident.md`) draait juist om snelheid: stil bewijs veiligstellen, dan bewijsbeslag of een deurwaarders-proces-verbaal van constateringen (art. 205–207 Rv), dan een verbod. Artikel 12.7 redt dat gedeeltelijk door "precautionary measures and/or interim relief" uit te zonderen, maar dat opent een discussie over wat daaronder valt — en die discussie wil je niet voeren op de dag dat er een kloon op straat ligt.

**Advies:** de mediationfase optioneel maken, en in elk geval uitdrukkelijk uitzonderen voor vorderingen wegens schending van geheimhouding of intellectuele eigendom en voor bewijs- en inzagemaatregelen. Voor gewone gebruikers: arbitrage helemaal weglaten en het forum gelijktrekken met AV 8.2. Voor niet-EU-gebruikers van de documentatielaag: SGOA-arbitrage bewust behouden.

### A.8 De eigen aansprakelijkheidsregeling (artikel 10)

**Lid 1 sluit alle aansprakelijkheid uit — ook voor opzet.** Dat is het probleem. Een exoneratie die ook opzet en bewuste roekeloosheid van de bedrijfsleiding dekt, wordt naar vaste rechtspraak buiten toepassing gelaten wegens strijd met de redelijkheid en billijkheid (art. 6:248 lid 2 BW; de lijn van HR Telfort/Scaramea, ECLI:NL:HR:2007:BA9610), en kan zelfs op art. 3:40 BW stranden. Het risico is niet dat je een procedure over opzet verliest — dat zou je toch verliezen — maar dat de rechter het hele artikel als te ruim aanmerkt en ook de nuttige beperking van lid 2 laat vallen.

Vergelijk AV 5.1 van v3.11: die begint mét de carve-out ("Behoudens in geval van opzet of bewuste roekeloosheid van de bedrijfsleiding van Brightmotive"). De ToU is hier gewoon ouder en slechter.

**Overige punten:**
- lid 2 kent een cap van € 5.000 per gebeurtenis maar **geen jaarplafond** en geen samentrekking van samenhangende gebeurtenissen; AV 5.1 regelt beide wél;
- er is geen uitzondering voor letselschade en overlijden (nooit uit te sluiten) en geen voor schade uit hoofde van art. 82 AVG;
- de opbouw "eerst alles uitsluiten, dan subsidiair beperken" is een bekend anti-patroon: het maakt de bepaling kwetsbaar zonder dat het iets oplevert.
- inhoudelijk-commercieel: tegenover een gebruiker die niets betaalt, is een cap van € 5.000 royaal. Er is geen enkele reden om hier scherp aan de wind te zeilen.

### A.9 De ontbrekende privacyverklaring (AVG)

Het account wordt door de gebruiker zélf bij Brightmotive aangemaakt, met naam, zakelijk e-mailadres en bedrijfsgegevens, en Brightmotive logt het gebruik. Dat is een verwerking van persoonsgegevens waarvoor **Brightmotive zelf verwerkingsverantwoordelijke** is (art. 4 sub 7 AVG) — niet verwerker. De informatieplicht van art. 13 AVG (identiteit, doeleinden, grondslag, ontvangers, bewaartermijnen, rechten van betrokkene, klachtrecht bij de AP) moet worden nagekomen op het moment van verkrijging, dus op het acceptatiescherm. De ToU zwijgt hier volledig over: geen privacyverklaring, geen link, geen woord. Dat is structurele non-compliance, en zij is zichtbaar op precies de plek waar je vertrouwen wilt wekken.

**Grondslagen:** uitvoering van de overeenkomst (art. 6 lid 1 sub b AVG) voor het account zelf; gerechtvaardigd belang (sub f) voor beveiligingslogging en voor het acceptatielog als bewijsmiddel. Gebruik **geen** toestemming — die is intrekbaar en dus ongeschikt voor bewijsdoeleinden. (Ter zijde: art. 1.4 van v3.04 doet dat wél fout; art. 1.3 van v3.11 repareert het voor de klantrelatie.)

**De rolverdeling die je expliciet moet maken.** Garage-accounts in de omgeving van een grossier worden op dit moment verwerkt als **verwerker** namens die grossier (AV 1.3). Zodra Brightmotive met diezelfde gebruiker een eigen overeenkomst sluit, zelf logt en handhaaft — en zeker zodra de rechtstreeks betaalde features van de agenda in `07-documentenstructuur.md` er zijn — wordt Brightmotive voor dát deel zelf verantwoordelijke. Die knip moet op drie plaatsen tegelijk worden vastgelegd:
1. in de gebruiksvoorwaarden zelf (één alinea: welke gegevens verwerken wij voor onszelf, welke voor de organisatie die je uitnodigde);
2. in een eigen privacyverklaring voor gebruikers;
3. als carve-out in de verwerkersovereenkomst met de klant.

Dit is dezelfde randvoorwaarde 2 die in `07-documentenstructuur.md` bij de rechtstreeks betaalde features staat. Het is geen bijzaak: zonder die knip is de directe klantrelatie met garages AVG-technisch niet op te bouwen.

**Bewaartermijn van het acceptatielog** apart vastleggen — het is zelf een verwerking, en je wilt het lang bewaren (zie A.1).

### A.10 De rol onder de Wet bescherming bedrijfsgeheimen — dit is de kernwaarde

Art. 1 Wbb (implementatie van Richtlijn (EU) 2016/943) eist drie dingen: de informatie is geheim, zij heeft daardoor handelswaarde, en zij is **onderworpen aan redelijke maatregelen om haar geheim te houden**. Die derde eis is waar bedrijfsgeheimenclaims in de praktijk op stuklopen. Een clickwrap-NDA vóór de toegang is een van de sterkste maatregelen die er zijn: hij is per persoon, vóór het moment van toegang, en bewijsbaar. Dit document is dus geen formaliteit maar een dragend onderdeel van pijler 2 uit de memo.

Bovendien is het de sleutel tot de **derdenwerking** van art. 2 lid 3 Wbb: de externe bouwer die wist of had moeten weten dat hij met onrechtmatig gedeelde informatie werkte, handelt zelf onrechtmatig. Een developer van die bouwer die persoonlijk op "akkoord" heeft geklikt, kan zich niet op onwetendheid beroepen. Dat is precies het gat dat bij het vorige incident open stond.

**Drie voorwaarden waaraan je moet blijven voldoen:**
1. **Bewijs** — zonder acceptatielog bestaat de maatregel juridisch niet (A.1).
2. **Consistentie** — één keer documentatie of specificaties delen buiten de clickwrap om (per e-mail, via Teams, in een offerte-bijlage) ondermijnt de hele claim; dat is de Wärtsilä/Aegir-les uit de memo. Sluit dus ook de zijkanalen.
3. **Afbakening** — een vage "alles is geheim"-formulering werkt tegen je, een expliciete categorielijst vóór je (Corrosion-lijn). Neem de lijst van AV 3.2 over.

**Timing.** De maatregelentoets kijkt naar het moment van de inbreuk. Elke maand uitstel is een maand waarin een toekomstig incident zonder deze maatregel wordt beoordeeld. Dat is een zelfstandig argument om nu in te voeren (zie D).

### A.11 De taal

Het document is Engelstalig. De doelgroep die je er nu bij wilt halen bestaat uit Nederlandse (en, gezien de Franse AV-versie, ook Franstalige) garagemedewerkers. Gevolgen:
- **Uitleg.** Bij niet-onderhandelde voorwaarden wordt overwegend objectief uitgelegd, maar of de wederpartij de tekst redelijkerwijs heeft kunnen begrijpen is wel een gezichtspunt. Onduidelijkheid komt voor rekening van de opsteller.
- **Terhandstelling.** In de feitenrechtspraak wordt terhandstelling in een taal die de wederpartij niet beheerst regelmatig gelijkgesteld met niet-terhandstelling. Geen harde regel, wel een reëel extra vernietigingsrisico bovenop A.2.
- **Toets art. 6:233 sub a BW.** Een Engelstalige NDA met een boete van € 10.000 voor een Nederlandse monteur is precies het type beding waarvan de "wijze van totstandkoming" zwaar tegen de opsteller weegt.
- **Commercieel.** Wie het niet begrijpt, klikt niet — of belt zijn grossier.

**Advies:** Nederlands als primaire versie voor de lichte laag, met Engels en Frans ernaast; per taalversie geldt de versie die de gebruiker heeft aanvaard. De zware documentatielaag mag Engelstalig blijven: die doelgroep is internationaal en technisch.

### A.12 Overige punten, kort

- **Artikel 5.1** ("The Documentation is exclusively intended for connecting with or to provide data to the Brightmotive Services") is een doelbinding die alleen bij developers past. Voor gewone documentatie op adminland klopt zij niet — die is bedoeld om te leren hoe je het platform gebruikt. Dit is de kern van de mismatch die C oplost.
- **Artikel 5.2 sub b** verbiedt downloaden, kopiëren, exporteren, printen en "otherwise reproducing". Technisch onhoudbaar (elke browser maakt kopieën) en voor een gewone gebruiker onwerkbaar. Herformuleer als "niet verspreiden of buiten je organisatie brengen" in plaats van "niet reproduceren".
- **De dwingend-rechtelijke carve-outs ontbreken.** Alleen artikel 5.2 sub d kent een uitzondering, en die geldt alleen voor reverse engineering. Er is niets over de artikelen 45j–45m Aw, over de rechten van de rechtmatige databankgebruiker, over de Data Act, en niets over onafhankelijke eigen ontwikkeling. AV 3.6 heeft die carve-out wél, generiek. Dit is de goedkoopste versterking die er is: het kost een alinea en het neemt de belangrijkste nietigheidsverweren weg. Memo §5 legt uit waarom.
- **Wat de ToU mist ten opzichte van AV artikel 3** — en dit is de andere kant van de medaille: het document is niet alleen te zwaar op de verkeerde plek, het is ook te licht op de goede plek. Er is geen namaakverbod op hoofdlijnen (AV 3.1), geen doelgebonden kennisgebruiksverbod (3.3), geen scraping-/AI-verbod (3.5), geen onderzoeksrecht (3.10) en geen bewijsvermoeden (3.11). Dat is precies de "v1.02-lijst" die in `07-documentenstructuur.md` bij de volgorde van uitwerking staat.
- **Artikel 8.3** (overdracht bij voorbaat van IE-rechten die de gebruiker onverhoopt verkrijgt) is voor een developer relevant en voor een garagegebruiker zinledig. Let bovendien op art. 2 lid 3 Aw: overdracht van auteursrecht vereist een akte. Of een clickwrap als onderhandse akte kwalificeert, is niet uitgemaakt; bij een echte samenwerking met een externe bouwer moet je dit hoe dan ook apart en ondertekend regelen, niet via een vinkje.
- **Artikel 13.1** (overdracht van de overeenkomst met vooraf gegeven onherroepelijke toestemming) spiegelt AV 8.6 en is prima. Noem voor de zekerheid expliciet "medewerking aan contractsoverneming in de zin van art. 6:159 BW".
- **Artikel 3.3** maakt de gebruiker verantwoordelijk voor "any and all persons connected to the User, including his personnel and/or customers". Voor een garagemonteur is dat betekenisloos: hij heeft geen personeel. Voor een klant-rechtspersoon is het nuttig, maar dat regelt AV 1.2 al beter.

---

## B. Aansluiting op de klant-AV v3.11

### B.1 Rangorde: de ToU erkent de AV niet

**De AV-kant is op orde.** Artikel 1.6 van v3.11: "Voor de toegang tot of het gebruik van (onderdelen van) de diensten, systemen of documentatie kunnen aanvullende gebruiksregels of gebruiksvoorwaarden gelden, die bij de toegang of het gebruik worden aanvaard. Bij strijd met deze voorwaarden gaan deze voorwaarden voor." Artikel 7.4 herhaalt dat in de rangordeketen: de aanvullende gebruiksvoorwaarden staan onderaan.

**De ToU-kant erkent dat nergens.** Sterker: de definitie van "Agreement" (art. 1.1.2) omvat "the entirety of agreements … including the provisions of these Terms of Use", en artikel 11.6 laat een lange lijst bepalingen de overeenkomst overleven zonder enige verwijzing naar een andere set. Het document presenteert zichzelf als de volledige regeling.

**Hoe erg is dat?** Minder erg dan het lijkt, en om een reden die belangrijk is voor het hele dossier: het zijn **twee verschillende contracten tussen verschillende partijen**. De AV binden Brightmotive en de klant; de ToU bindt Brightmotive en de individuele gebruiker. Een rangordebepaling werkt alleen binnen één contractsverhouding — de AV van klant X kunnen niet zomaar de inhoud bepalen van een contract tussen Brightmotive en werknemer Y.

**Waar het wél botst:** zodra dezelfde partij aan beide sets gebonden is. Dat gebeurt structureel bij (i) een DGA of directeur van een klant die zelf een documentatie-account aanmaakt, (ii) een klant-rechtspersoon die via de ruime "User"-definitie als gebruiker wordt aangemerkt, en (iii) elk geschil waarin Brightmotive zich op de ene set beroept en de wederpartij op de andere.

**Fix (één zin in de gebruiksvoorwaarden):**
> "Heeft de organisatie waarvoor u het platform gebruikt een overeenkomst met Brightmotive, dan gaan de voorwaarden van die overeenkomst bij strijdigheid vóór deze gebruiksvoorwaarden."

Dat spiegelt AV 1.6 vanuit de andere kant en maakt de stapel sluitend. Het neemt bovendien het belangrijkste verweer weg dat een klant tegen de invoering kan aanvoeren (zie D).

**Fix aan de AV-kant — één concrete bevinding.** In het conceptvoorstel voor de haakbepaling (`02-tekst-artikel-3-en-boetebeding.md`, onderdeel C) stond een derde zin: *"U zorgt ervoor dat uw gebruikers die voorwaarden aanvaarden en naleven."* Die zin staat **niet** in de vastgestelde tekst van artikel 1.6 v3.11 — hij is bij de vereenvoudigingsronde weggevallen. Daarmee ontbreekt de contractuele plicht van de klant om zijn gebruikers te laten klikken en zich aan de regels te houden. Dat is precies de hefboom die je bij de garage-uitrol nodig hebt: het maakt de grossier je partner in de uitrol in plaats van een toeschouwer. AV 1.2 (toerekening) en 3.9 (afnemersgebruik) dekken het gedeeltelijk, maar niet expliciet. **Advies: die zin terugzetten vóór publicatie van v3.11.** Nu kost het niets; later kost het een AV-wijziging met een opzegvenster.

**Administratief:** `07-documentenstructuur.md` verwijst op drie plaatsen nog naar "art. 1.8 / 1.9" terwijl v3.11 de haakbepalingen in 1.6 en 1.7 heeft. Bij de eerstvolgende bewerking gelijktrekken, anders raakt de verwijzing zoek zodra iemand het document los leest.

### B.2 Boetestapeling: klant én medewerker voor hetzelfde feit

**Het scenario.** Een medewerker van klant X deelt de API-documentatie met een externe bouwer, zonder de toestemming van AV 3.4.

- **Via de AV:** de handeling van de gebruiker geldt op grond van artikel 1.2 als handeling van de klant ("daarbij begane overtredingen gelden als uw overtredingen"), en artikel 3.4 slot zegt hetzelfde over derden. De klant verbeurt de boete van artikel 3.7: twee keer de jaarvergoeding met een minimum van € 25.000, plus € 1.000 per dag — of, als de overtreding uitsluitend uit het ontbreken van de toestemming bestaat, € 10.000 plus € 500 per dag.
- **Via de ToU:** dezelfde medewerker verbeurt persoonlijk € 10.000 plus € 3.000 per dag (art. 9.2).

**Juridisch is dat geen verboden cumulatie:** twee schuldenaren, twee contracten, twee zelfstandige boetebedingen (art. 6:91 e.v. BW). Maar drie praktische problemen:
1. **Het versterkt de matiging van beide boetes.** De rechter beoordeelt "buitensporig en daarom onaanvaardbaar" naar de omstandigheden van het geval, en één feitencomplex dat via twee routes ruim € 35.000 plus € 4.000 per dag oplevert, is precies zo'n omstandigheid.
2. **Het levert een regres-rommel op.** Betaalt de klant de boete van zijn medewerker? Vordert hij die op hem terug? Art. 7:661 BW beschermt de werknemer jegens zijn werkgever bij schade aan derden, maar hier gaat het om een eigen contractuele boete — een onopgeloste puzzel die je niet wilt hebben.
3. **Het geeft de klant een argument.** "Wij zijn al beboet" is commercieel lastig te weerleggen.

**Fixes (alle drie kort):**
- een anti-cumulatiebepaling in de gebruiksvoorwaarden: *"Heeft Brightmotive voor hetzelfde feitencomplex al een boete ontvangen op grond van de overeenkomst met de organisatie van de gebruiker, dan wordt die in mindering gebracht op de boete van deze voorwaarden, en omgekeerd."*
- de regel "een samenhangend geheel van handelingen geldt als één overtreding" overnemen uit AV 3.7 (staat daar al, ontbreekt in de ToU);
- geen persoonlijke boete voor gewone gebruikers (C).

### B.3 Aansprakelijkheid: twee regimes over elkaar heen

| | ToU art. 10 | AV v3.11 art. 5 |
|---|---|---|
| Uitgangspunt | volledige uitsluiting, óók opzet | uitsluiting **behoudens** opzet/bewuste roekeloosheid bedrijfsleiding |
| Cap | € 5.000 per gebeurtenis | vergoeding over 3 maanden, minimaal € 5.000 |
| Jaarplafond | ontbreekt | aanwezig (art. 5.1 slot) |
| Samenhangende reeks | ontbreekt | geldt als één gebeurtenis |
| Vervaltermijn | ontbreekt | melding binnen 2 maanden; verval na 12 maanden (art. 5.3) |
| Reikwijdte | alleen deze ToU | ook SLA en aanvullende dienst- en gebruiksvoorwaarden (art. 5.6) |

**Wat er gebeurt.** AV 5.6 verklaart de AV-beperkingen uitdrukkelijk óók van toepassing op de gebruiksvoorwaarden. In de relatie met een klant die zowel aan de AV als (via zijn medewerkers) aan de ToU raakt, wint bij strijd de AV (art. 1.6). Materieel wordt de ToU-cap daar dus vervangen door het AV-regime — dat is geen ramp, maar het betekent dat de ToU-tekst voor die relatie grotendeels dode letter is en de indruk wekt van een regeling die niet geldt.

**Voor gebruikers die géén klant zijn** (garagemedewerkers, prospects met een demo-account, medewerkers van externe bouwers) geldt alleen de ToU. Daar is de cap van € 5.000 tegenover iemand die niets betaalt ruim voldoende; het echte probleem is en blijft de te ruime uitsluiting van lid 1 (A.8).

**Fix:** trek de tekst gelijk met AV 5.1–5.3 en 5.6, met dezelfde opzet-carve-out, hetzelfde jaarplafond en dezelfde vervaltermijn. Eén formulering, twee documenten — dat is precies waarvoor de "bouwstenen" uit `07-documentenstructuur.md` bedoeld zijn.

### B.4 Forum

| | ToU art. 12 | AV v3.11 art. 8.2 |
|---|---|---|
| Voorfase | 30 dagen overleg + 60 dagen mediation, verplicht | geen |
| Forum EU/EER/CH | rechtbank Midden-Nederland, locatie Utrecht | bevoegde rechter in het arrondissement van Brightmotive (= Midden-Nederland) |
| Forum daarbuiten | SGOA-arbitrage, Den Haag | idem als hierboven: de Nederlandse rechter |
| Spoedmaatregelen | uitgezonderd (art. 12.7) | volgt uit de wet |

Voor Nederlandse partijen is het forum materieel hetzelfde. De echte botsingen zijn:
1. **De voorfase.** Bij één feitencomplex kun je de klant meteen dagvaarden en moet je 90 dagen wachten voordat je de gebruiker kunt aanspreken — terwijl de gebruiker degene is die het bewijs vasthoudt en de documentatie in handen heeft. Dat is precies verkeerd om.
2. **De splitsing bij een internationale zaak.** Klant in Nederland (AV: Nederlandse rechter), developer van de externe bouwer in bijvoorbeeld India (ToU: SGOA-arbitrage). Eén feitencomplex, twee fora, en het risico op tegenstrijdige uitspraken. Bovendien: SGOA-arbitragekosten lopen snel in de tienduizenden, wat de drempel om daadwerkelijk te handhaven hoog maakt.

**Fix:** forum gelijktrekken met AV 8.2; mediation optioneel; expliciete uitzondering voor geheimhoudings-, IE- en bewijsvorderingen; SGOA-arbitrage alleen behouden voor niet-EU-gebruikers van de zware documentatielaag, als bewuste keuze wegens de executievoordelen van het Verdrag van New York.

### B.5 Terminologie

De ToU werkt met gedefinieerde Engelse begrippen (*Brightmotive Services, Documentation, User, Account, Confidential Information*); v3.11 is bewust in gewone Nederlandse taal geschreven en definieert bijna niets ("de diensten", "documentatie", "vertrouwelijke informatie", "toegangsmiddelen", "uw organisatie(s)", "afnemers"). Twee risico's:

1. **Uitlegrisico.** "Documentation" in de ToU omvat uitdrukkelijk de broncode; "documentatie" in de AV staat naast software en data en betekent dus iets anders. Wie zich op de ene set beroept, krijgt de definitie uit de andere tegengeworpen.
2. **Onderhoudsrisico.** Bouwprincipe 2 uit `07-documentenstructuur.md` is functioneel verwijzen zonder documentnamen — goed — maar dat werkt alleen als beide sets dezelfde wóórden gebruiken.

**Fix:** schrijf de nieuwe sets in dezelfde stijl en met dezelfde termen als v3.11. Definieer alleen wat echt nodig is, en neem voor "vertrouwelijke informatie" de categorielijst van AV 3.2 letterlijk over. Voor de zware laag mag daarnaast een Engelse versie bestaan, mits de begrippen één-op-één corresponderen.

### B.6 Toerekening (AV 1.2) naast een eigen contract met de gebruiker

**Wat AV 1.2 doet.** "Alles wat met uw toegangsmiddelen gebeurt, geldt als door u en onder uw leiding en toezicht verricht … u bent daarvoor aansprakelijk en daarbij begane overtredingen gelden als uw overtredingen." Dat is de sterkste route die je hebt: één solvabele wederpartij, een omzetgebonden boete (3.7), een auditrecht (3.10) en een bewijsvermoeden (3.11). Daar moet je nooit vanaf.

**Wat een eigen contract met de gebruiker dáárbovenop toevoegt** — drie dingen die de AV principieel niet kunnen:
1. **Een aanspraak op personen die geen klant zijn en dat nooit worden.** Garagemedewerkers, prospects met een demo-account (het agendapunt in `07-documentenstructuur.md`) en medewerkers van externe bouwers vallen buiten elke AV. De AV kunnen over hen niets regelen; een clickwrap wel.
2. **Bewijs van wetenschap voor de Wbb-derdenwerking** (art. 2 lid 3 Wbb). Dit is het spoor dat bij het vorige incident ontbrak en dat de externe bouwer raakt (memo §4.2).
3. **De "redelijke maatregel" van art. 1 Wbb**, bewijsbaar per persoon en per moment.

**De spanning, en hoe je die oplost.** Een eigen contract met de gebruiker mag de AV-route niet verzwakken. Twee concrete valkuilen:
- als de gebruiksvoorwaarden de gebruiker als de verantwoordelijke aanwijzen, kan een klant zeggen "spreek mijn medewerker maar aan";
- als je de gebruiker een eigen aansprakelijkheidsplafond geeft, mag dat niet doorwerken naar de klant.

**Fix (één zin, in beide lagen):**
> "Deze voorwaarden laten onverlet wat Brightmotive is overeengekomen met de organisatie waarvoor u het platform gebruikt; die organisatie blijft jegens Brightmotive verantwoordelijk en aansprakelijk voor het gebruik via haar toegangsmiddelen."

---

## C. Geschikt maken voor alle gebruikers, garage-gebruikers voorop

### C.1 De ontwerpkeuze: twee zelfstandige documenten, twee acceptatiemomenten

`07-documentenstructuur.md` legt als bouwprincipe 1 vast: **per doelgroep één zelfstandig document**, geen gelaagdheid richting de wederpartij. Dat principe wijst hier de weg. Eén document met een hoofdstuk dat "alleen voor sommigen" geldt, is juridisch het slechtste van twee werelden: de gewone gebruiker krijgt bepalingen te zien die niet voor hem gelden (slecht voor de begrijpelijkheidstoets van art. 6:233 sub a BW), en bij een geschil moet je bewijzen welk deel wél op wie van toepassing was.

Dus:

| | **Laag 1 — Gebruiksvoorwaarden** | **Laag 2 — Documentatievoorwaarden** |
|---|---|---|
| Voor wie | iedereen die inlogt: garagemedewerkers, medewerkers van klanten, leveranciers-medewerkers, prospects met een demo-account | wie developer-documentatie (partners) of admindocumentatie (adminland) opent |
| Acceptatiemoment | eerste inlog | de eerste keer dat de documentatieomgeving wordt geopend ("just-in-time") |
| Omvang | ± 1 A4, gewone taal, Nederlands primair | de huidige NDA, gerepareerd; Engels mag |
| Boete | **geen** | ja, herontworpen |
| Vervangt | niets (nieuw) | Terms of Use v1.01 |

**Waarom just-in-time acceptatie voor laag 2.** Het is juridisch sterker (de gebruiker weet waarvoor hij tekent, op het moment dat het relevant is) en bewijstechnisch sterker (het klikmoment ligt direct naast het toegangsmoment, wat bij een incident precies de vraag is). En het houdt laag 2 weg bij de 95% van de gebruikers voor wie hij niet bedoeld is.

### C.2 Laag 1 — de lichte laag voor álle gebruikers

Kerninhoud, in deze volgorde (nog geen definitieve tekst, wel de bouwstenen):

1. **Wie is wie.** Dit zijn afspraken tussen jou en Brightmotive. De organisatie die je heeft uitgenodigd heeft een eigen contract met ons; bij strijd gaan die afspraken voor (B.1) en die organisatie blijft verantwoordelijk voor het gebruik via haar toegangsmiddelen (B.6).
2. **Je account is van jou alleen.** Eigen account, wachtwoord geheim, niet delen of uitlenen, tweefactor gebruiken als dat wordt aangeboden, misbruik direct melden. Spiegelt AV 1.2 — en dat is precies de reden dat deze laag ook voor klanten zinvol is: hij maakt de toerekeningsregel van 1.2 kenbaar bij de persoon die hem moet naleven.
3. **Waarvoor je het platform gebruikt.** Voor het opzoeken van onderdelen en voertuiginformatie en het bestellen bij de organisatie die je heeft uitgenodigd — en voor ander gebruik dat Brightmotive toestaat. Die laatste zinsnede is bewust gelijk aan AV 3.9 en houdt de deur open voor de rechtstreeks betaalde features uit `07-documentenstructuur.md`.
4. **Geen scraping, geen AI-hergebruik.** Letterlijk gespiegeld op AV 3.5: geen geautomatiseerd of stelselmatig opvragen, kopiëren of hergebruiken van (delen van) de catalogus, data of datastructuren, ook niet via of met behulp van AI-systemen of voor het trainen daarvan, en ongeacht of de gegevens wettelijk als databank beschermd zijn. **Dit is de belangrijkste toevoeging voor deze groep** — het gat dat de maatregelenlijst bij de clickwrap voor eindgebruikers benoemt. Vandaag is een garage-account dat de hele catalogus doorloopt contractueel nergens door gedekt behalve via de omweg van de AV van de grossier.
5. **Geen namaak.** Eén zin, gespiegeld op AV 3.1 en 3.3: je gebruikt wat je hier ziet niet om zelf of via anderen een concurrerend of vervangend systeem te (laten) bouwen.
6. **Vertrouwelijkheid, licht.** Wat je alleen na inloggen ziet — met name prijzen, kortingen, beschikbaarheid en de manier waarop het platform werkt — houd je binnen je werk en deel je niet buiten je organisatie, zolang het niet openbaar is. **Geen** 10-jaarstermijn, **geen** teruggeef- of vernietigingsplicht, **geen** inspectieplicht. Dit is licht genoeg om redelijk te zijn en zwaar genoeg om de prijsinformatie van de grossier te beschermen — wat een verkoopargument richting de klant is.
7. **Intellectueel eigendom, kort.** Het platform, de software, de data en de documentatie zijn van Brightmotive en haar licentiegevers; je krijgt een persoonlijk, niet-overdraagbaar gebruiksrecht zolang je account bestaat.
8. **Privacy.** Welke gegevens Brightmotive voor zichzelf verwerkt (account, gebruikslogs, beveiliging) en welke namens de organisatie die je uitnodigde, met een link naar de privacyverklaring voor gebruikers (A.9).
9. **Wat er gebeurt bij overtreding — zonder persoonlijke boete.** Brightmotive kan je account beperken, blokkeren of beëindigen, de organisatie die je heeft uitgenodigd informeren, en schade verhalen volgens de wet. Dat is het.
10. **Wijzigingen.** Bij een materiële wijziging vragen we opnieuw akkoord; verder informeren we je.
11. **Beschikbaarheid en aansprakelijkheid, netjes.** Inspanningsverplichting, uitsluiting behoudens opzet of bewuste roekeloosheid van de bedrijfsleiding, cap € 5.000 per gebeurtenis met jaarplafond, meldtermijn — gelijkgetrokken met AV 5 (B.3).
12. **Recht en rechter.** Nederlands recht, rechtbank Midden-Nederland. Geen arbitrage, geen verplichte mediation.

### C.3 Waarom géén boete van € 10.000 voor een garagemonteur

Dit is een expliciete aanbeveling en het verdient een expliciete motivering.

**Juridisch:**
- **Het beding is vrijwel zeker niet inbaar.** Alle vier de ontwerpfouten uit A.3 komen hier samen: één eenheidsboete op alle verplichtingen, een onbegrensde dagboete, geen relatie tot enige tegenprestatie (de gebruiker betaalt niets), en verschuldigdheid zonder toerekenbaarheid. Dat is precies het profiel waarop art. 6:94 BW wordt toegepast.
- **Het beding staat onder een vermoeden van onredelijke bezwarendheid.** Rechtstreeks via art. 6:237 sub i BW als de gebruiker als consument kwalificeert; anders via reflexwerking in de open toets van art. 6:233 sub a BW (A.2).
- **Het besmet de rest.** Een rechter die het boetebeding als onredelijk aanmerkt, kijkt met andere ogen naar de rest van de set — inclusief de geheimhoudingsbepalingen die je juist wél nodig hebt.
- **Het is overbodig.** De echte, solvabele wederpartij is de klant, en die is via AV 1.2 al aansprakelijk voor exact dezelfde handelingen, met een boete (3.7) die wél meeschaalt met de jaarvergoeding, wél differentieert en wél een plafond kent. De boete in de gebruiksvoorwaarden voegt geen bescherming toe; hij dupliceert een sterkere regeling met een zwakkere.

**Commercieel:**
- **Het is een acceptatiedrempel op het inlogscherm.** Minder actieve garage-accounts betekent minder orders, en de vergoeding van Brightmotive is omzetgebonden (AV 4.2). Je beschadigt je eigen omzetbasis.
- **Het maakt de grossier de boodschapper van slecht nieuws** bij zijn eigen klanten. Dat is precies de rol waarin je hem niet wilt zetten als je hem ook nog wilt vragen zijn gebruikers te laten klikken (B.1).
- **Het staat haaks op het plan voor rechtstreeks betaalde features.** Je wilt een directe klantrelatie met garages opbouwen. Die begin je niet met een boetebeding van € 10.000.
- **Je hebt het niet nodig als afschrikmiddel.** Accountblokkade plus een melding aan de grossier is onmiddellijk voelbaar, kost niets en is niet aantastbaar.

**Wat je overhoudt** als je de boete weglaat: schadevergoeding op grond van art. 6:74 BW, een vordering uit onrechtmatige daad, de volledige Wbb-gereedschapskist (verbod, terugroeping, vernietiging van de codebase, art. 6 Wbb) — en het belangrijkste: de aansprakelijkheid van de klant via AV 1.2. Dat is meer dan genoeg.

**Bewuste optie voor later.** Mocht er ooit een scraping-incident via een garage-account komen, dan kun je alsnog één gerichte, kleine boete op uitsluitend het scraping- en namaakcluster invoeren via het wijzigingsmechanisme. Dat is een betere volgorde dan nu preventief te zwaar inzetten.

### C.4 Laag 2 — de zware documentatielaag

Doelgroep: developers van klanten, externe softwarebouwers die door klanten worden ingeschakeld (de AV 3.4-route), en beheerders die adminland gebruiken. De bestaande NDA-kern blijft — dit is en blijft de kroonjuwelenbescherming — maar gerepareerd:

**a. Vertrouwelijkheid, bepaalbaar en zonder einddatum.** Alles wat alleen na inloggen toegankelijk is, plus de categorielijst van AV 3.2 (koppel- en API-specificaties, datastructuren, algoritmes, verrijkings- en matchinglogica, prijs- en voorraadlogica). Duur: zolang de informatie niet openbaar is (in plaats van 10 jaar, A.4).

**b. Artikel 6.3 schrappen.** Vervangen door "alles wat je via de documentatieomgeving hebt gezien"; artikel 6.2 alleen met kennisgeving en voor de toekomst (A.6).

**c. Doelbinding.** Uitsluitend voor het koppelen of beheren van de systemen van de organisatie die je vertegenwoordigt. Nooit voor eigen productontwikkeling.

**d. De verbodenlijst, gespiegeld op AV artikel 3.** Niet verspreiden of buiten je organisatie brengen (in plaats van het onhoudbare "niet reproduceren", A.12); niet delen met derden zonder voorafgaande schriftelijke toestemming; geen scraping of AI-hergebruik (3.5); geen namaak op hoofdlijnen (3.1); doelgebonden kennisgebruiksverbod, looptijd plus één jaar, en voor de vertrouwelijke informatie onbeperkt zolang zij niet openbaar is (3.3).

**e. Carve-outs voor dwingend recht.** De generieke formulering van AV 3.6 overnemen: dwingende gebruikersrechten (art. 45j–45m Aw), de rechten van de rechtmatige databankgebruiker, de Data Act, en het uitdrukkelijke recht om zonder Brightmotive-materiaal een eigen of concurrerend systeem te ontwikkelen. Plus de zelfstandigheidsclausule ("ieder onderdeel geldt als een afzonderlijk beding") — die is er niet voor de sier: bij een te ruim mededingingsbeding mag de rechter niet terugsnoeien naar het toelaatbare (memo §4.1). Dit is de goedkoopste versterking in het hele pakket.

**f. Wie vertegenwoordig je.** Verplicht veld bij de acceptatie: "ik open deze documentatie namens [organisatie]", met de garantie dat je daartoe bevoegd bent en dat die organisatie de toestemming van AV 3.4 heeft. Dit is precies wat bij het incident ontbrak: het maakt de keten gebruiker → organisatie → klant bewijsbaar, en het legt de wetenschap vast die art. 2 lid 3 Wbb tegen de externe bouwer nodig heeft.

**g. IE-overdracht bij voorbaat** (het huidige artikel 8.3) alleen hier houden — daar hoort hij thuis. Voor een echte samenwerking met een externe bouwer blijft een ondertekende akte nodig (A.12).

**h. De boete: behouden, maar herontwerpen.** De boete is hier wél op zijn plaats: dit zijn de mensen die daadwerkelijk bij de kroonjuwelen kunnen, en de afschrikkende werking is de kern van de maatregel. Het ontwerp moet dan wel de matigingsrechtspraak volgen — dezelfde logica als artikel 3.7 AV:
- **alleen op een afgebakend cluster** (geheimhouding, verspreiding aan derden, namaak, scraping) — niet op "een of meer van de verplichtingen";
- **gedifferentieerd naar zwaarte:** een lager bedrag voor het ontbreken van een toestemming, een hoger bedrag voor doorgeven aan een bouwer of daadwerkelijk nabouwen;
- **een plafond** op de dagboete én op het totaal;
- **de dagboete pas vanaf de dag ná de schriftelijke melding** (zoals AV 3.7 al doet);
- **"een samenhangend geheel van handelingen geldt als één overtreding"**;
- **anti-cumulatie** met AV 3.7 (B.2);
- **uitdrukkelijk naast** staking en aanvullende schadevergoeding — anders vervangt de boete de schadevergoeding (art. 6:92 lid 2 BW);
- **onderscheid natuurlijke persoon / rechtspersoon:** richt de boete primair op de organisatie die de gebruiker vertegenwoordigt (die aanvaardt mee bij de acceptatie van punt f) en houd de natuurlijke persoon alleen persoonlijk aansprakelijk bij opzet.

Als ordegrootte voor het gesprek met de advocaat, uitdrukkelijk als ontwerpindicatie en niet als vaststaand: voor de organisatie € 25.000 basis plus € 1.000 per dag met een totaalplafond van € 100.000; voor de natuurlijke persoon bij opzet € 10.000 plus € 250 per dag met een plafond van € 50.000. De bedragen zijn een keuze; de **structuur** is wat de matigingsbestendigheid bepaalt.

**i. Forum en aansprakelijkheid** gelijktrekken zoals in B.3 en B.4.

### C.5 Wat dit betekent voor de bestaande "terms"-pagina

1. **De pagina blijft bestaan, maar krijgt een andere rol.** Hij wordt laag 2, de Documentatievoorwaarden. Laag 1 hoort niet in de documentatie thuis maar in de applicatie: een acceptatiescherm bij de eerste inlog, op partners, adminland én in BrightCat zelf.
2. **Volgorde van uitrol:** eerst laag 1 bouwen en uitrollen (die raakt de grootste groep en het kleinste risico), daarna de terms-pagina herschrijven naar laag 2 met een **nieuw akkoordmoment** voor bestaande accounts. Leun daarbij niet uitsluitend op artikel 13.2 v1.01 (A.1) — opnieuw laten klikken is technisch triviaal en bewijstechnisch veel sterker.
3. **v1.01 archiveren, niet weggooien.** Bestaande akkoorden blijven geldig (besluit in `07-documentenstructuur.md`), en de tekst blijft nodig als bewijs voor incidenten uit de periode waarin hij gold. Archiveren met datum in het versieregister in de Contract Annexes-database (bouwprincipe 5), en `12-gebruiksvoorwaarden-v1.01-huidig.md` bewaren als momentopname.
4. **Koppel het versiebewijs aan de repository.** De pagina is een bestand in `brightmotive-docs`; leg per acceptatie de commit-hash of het versienummer van de getoonde tekst vast (A.1). Dat is de goedkoopste manier om het versiebewijs sluitend te krijgen en het maakt het onmogelijk om later te betwisten welke tekst iemand heeft aanvaard.
5. **Sluit de zijkanalen.** Zolang documentatie of API-specificaties ook per e-mail, via Teams of als offertebijlage rondgaan zonder acceptatie, ondermijnt dat de hele Wbb-claim (A.10, consistentie-eis).
6. **Talen.** Laag 1 in het Nederlands, met Engels en Frans ernaast (de AV bestaan al in EN en FR); laag 2 mag Engelstalig blijven.

---

## D. Invoering nu, vóór alle klanten op v3.11 zitten

### D.1 De hoofdregel: de gebruiksvoorwaarden staan op eigen benen

De gebruiksvoorwaarden zijn een **eigen overeenkomst tussen Brightmotive en de gebruiker**. Voor de geldigheid daarvan is de klant-AV niet nodig: aanbod (het acceptatiescherm) plus aanvaarding (de klik) is voldoende (art. 6:217 BW). De klant hoeft niet mee te werken, kan de overeenkomst niet vernietigen — hij is er geen partij bij — en kan de gebruiker ook niet verbieden hem aan te gaan. Dat is niet alleen theorie: het is precies waarom deze route de enige is die werkt voor personen die nooit klant worden (B.6).

### D.2 Onder v3.11: al voorzien, dus schoon

Artikel 1.6 zegt dat aanvullende gebruiksvoorwaarden kunnen gelden en dat ze bij de toegang worden aanvaard. Artikel 7.1 slotzin zegt: "Het toepassen van een regeling die al in de overeenkomst of deze voorwaarden is voorzien, geldt niet als aanpassing." Invoering is dus geen wijziging van de AV: geen aankondigingstermijn van twee maanden, geen opzegrecht op grond van artikel 7.2. Dat was ook de bedoeling van de haakbepaling (`02-tekst-artikel-3-en-boetebeding.md`, onderdeel C). Volledig schoon.

### D.3 Onder v3.04: geen haak, maar ook geen echt gat

v3.04 kent geen haakbepaling. Wat kan een klant dan tegenwerpen? Drie mogelijke verwijten, in volgorde van kracht:

**a. "Dit is een eenzijdige wijziging van de voorwaarden."** Zwak. Artikel 7.1 van v3.04 geeft Brightmotive juist een ruime bevoegdheid: "Brightmotive mag onverminderd alle overige rechten deze voorwaarden, **gebruiksregels**, de vergoeding en betalingstermijn eenzijdig aanpassen." Het woord "gebruiksregels" staat er letterlijk, en het invoeren van gebruiksregels voor gebruikers past daar tekstueel binnen. Het gevolg zou hooguit zijn dat artikel 7.2 v3.04 wordt geactiveerd: de klant kan tot de datum van inwerkingtreding opzeggen met een opzegtermijn van twee maanden. **Dat is het enige reële risico: een toch al ontevreden klant grijpt de invoering aan om eruit te stappen.** Dat risico is klein zolang laag 1 licht is en géén nieuwe lasten voor de klánt bevat — en dat is precies waarom de keuze in C.3 (geen boete voor gewone gebruikers) niet alleen een juridische maar ook een invoeringskeuze is.

**b. "U legt mijn klanten verplichtingen op zonder mijn toestemming."** Geen juridische grond. De AV geven de klant geen exclusiviteit over zijn gebruikers — dat is al vastgesteld bij de analyse van de rechtstreeks betaalde features in `07-documentenstructuur.md` — en de gebruikers zijn geen partij bij de AV. Commercieel is het wél een gesprek, en dat gesprek voer je vooraf (D.5).

**c. "De gebruiksvoorwaarden zijn strijdig met mijn AV."** Alleen reëel als laag 1 iets regelt wat de AV anders regelen, bijvoorbeeld aansprakelijkheid of boetes richting de klant. De fix uit B.1 haalt dit verwijt volledig weg: zet in laag 1 dat de voorwaarden van de organisatie bij strijdigheid voorgaan. Dan is er per definitie geen strijd die de klant kan aangrijpen.

### D.4 Twee argumenten die zwaarder wegen dan het restrisico

1. **De bestaande praktijk.** Er draait al jaren een documentatie-clickwrap (v1.01) — onder v3.01 tot en met v3.04, dus zonder haakbepaling, zonder klachten. Het invoeren van een lichtere variant voor een grotere groep is geen breuk maar een uitbreiding van staand gebruik. Dat is een sterk feitelijk verweer als een klant er ooit iets van zegt: je doet wat je altijd al deed, alleen zorgvuldiger.
2. **De Wbb-klok tikt.** De maatregelentoets van art. 1 Wbb kijkt naar het moment van de inbreuk (memo §4.2). Elke maand uitstel is een maand waarin een toekomstig incident wordt beoordeeld zónder deze maatregel. Wachten kost dus bescherming, en die kosten lopen stil op.

### D.5 De grens die je wél moet respecteren

Laag 2 legt echte lasten op. Voor een klant die zelf op v3.04 zit en wiens developer laag 2 accepteert, valt dat eerder als een verzwaring aan te merken dan laag 1. Twee mitigaties:
- **Het is voor die groep geen nieuwe last.** Zij accepteren al v1.01, met een zwaardere boete dan wat je in de plaats stelt. De route van artikel 13.2 v1.01 is precies waarvoor dat beding is bedoeld (en die route is al vastgelegd als besluit in `07-documentenstructuur.md`) — met de aanbeveling uit A.1 om desondanks opnieuw te laten klikken.
- **De zwaarste elementen horen contractueel primair bij de klant thuis.** Voor v3.04-klanten leun je op wat je hebt (artikel 3.1 van v3.04, plus de Wbb en het databankenrecht) en accepteer je bewust dat de gebruikerslaag daar dunner is tot v3.11 is uitgerold.

### D.6 Concreet advies

**Ja, nu invoeren.** In deze volgorde:

1. **Nu — acceptatielog en versiearchief inrichten.** Harde voorwaarde, vóór of gelijk met de uitrol. Zonder dit levert de hele operatie juridisch niets op (A.1, A.10).
2. **Nu — laag 1 bouwen en uitrollen** voor álle gebruikers, ongeacht welke AV-versie hun organisatie heeft. Met de voorrangszin (B.1), de onverlet-zin (B.6), zonder persoonlijke boete (C.3), in het Nederlands. Restrisico onder v3.04: verwaarloosbaar.
3. **Gelijktijdig — de privacyverklaring voor gebruikers publiceren** en de AVG-rolverdeling vastleggen, inclusief de carve-out in de verwerkersovereenkomst (A.9). Dit mag niet achterlopen: het staat op het acceptatiescherm zelf.
4. **Kort daarna — laag 2 vervangt v1.01** op de terms-pagina, met een nieuw akkoordmoment voor bestaande accounts.
5. **Bij verlenging — v3.11 uitrollen** naar bestaande klanten. Vanaf dat moment is artikel 1.6 de formele grondslag en verdwijnt het restrisico van D.3 vanzelf.

**Over de aankondiging aan klanten.** Kondig laag 1 vier tot zes weken vooraf aan, met het aanbod de tekst vooraf te lezen, en met het commerciële argument: het beschermt hun prijsinformatie en hun catalogusdata tegen scraping door hun eigen afnemers. Doe dat **als informatie, niet als "wijziging ex artikel 7.1"**. Reden: laag 1 verandert voor de klant zelf niets — er is geen bepaling van zijn AV die wordt aangepast. Het formeel als 7.1-wijziging aankondigen zou het juist netjes maken, maar activeert bij v3.04-klanten het opzegvenster van artikel 7.2 zonder dat daar noodzaak toe is. Voor laag 2 geldt hetzelfde, met daarbij de verwijzing naar artikel 13.2 v1.01 als grondslag voor de vervanging van de bestaande set.

---

## E. Beslispunten voor Ray

1. **Splitsen in twee zelfstandige documenten** (licht voor iedereen, zwaar voor de documentatie) in plaats van één document met lagen?
 → **Advies: ja.** Volgt het bouwprincipe "per doelgroep één document", houdt de zware tekst weg bij 95% van de gebruikers en maakt de acceptatie per laag bewijsbaar.

2. **Persoonlijke boete voor gewone gebruikers?**
 → **Advies: nee, schrappen.** Vrijwel zeker niet inbaar, vermoedelijk onredelijk bezwarend, commercieel schadelijk en overbodig naast AV 1.2 + 3.7. Handhaving via blokkade, melding aan de klant en de wettelijke schadevergoeding.

3. **Boete in de documentatielaag: behouden of herontwerpen?**
 → **Advies: behouden, maar herontwerpen** naar het model van AV 3.7 (afgebakend cluster, differentiatie, plafond, dagboete na melding, anti-cumulatie, primair op de organisatie). € 10.000 + € 3.000/dag ongewijzigd laten staan is de slechtste van de drie opties.

4. **Nu invoeren, ook bij klanten op v3.04?**
 → **Advies: ja voor laag 1**, met de voorrangszin. Het risico is een zwak verwijt van een ontevreden klant; het uitstel kost bescherming onder de Wbb.

5. **Acceptatielog en versiearchief: voorwaarde of parallel traject?**
 → **Advies: harde voorwaarde.** Zonder logbewijs bestaat de maatregel juridisch niet en is de hele uitrol weggegooid werk. Dit is de eerste bouwtaak, niet de laatste.

6. **Privacyverklaring en AVG-rolverdeling vóór de uitrol?**
 → **Advies: ja, vóór.** Verwijzing in beide lagen, een eigen privacyverklaring voor gebruikers en een carve-out in de verwerkersovereenkomst. Zonder die knip is de directe relatie met garages niet op te bouwen.

7. **Taal: Nederlands als primaire versie?**
 → **Advies: ja voor laag 1** (met Engels en Frans ernaast); laag 2 mag Engelstalig blijven.

8. **De 10-jaarstermijn vervangen door "zolang de informatie niet openbaar is"?**
 → **Advies: ja.** Sluit aan op AV 3.2 en voorkomt de a-contrario-redenering dat na tien jaar alles vrij is.

9. **Artikel 6.3 (terugwerkende geheimverklaring van docs.brightmotive.com) schrappen?**
 → **Advies: ja.** Onbepaalbaar en naar Wbb-maatstaven onjuist. Vervangen door de categorielijst van AV 3.2, die wél bepaalbaar en bewijsbaar is.

10. **Aansprakelijkheid gelijktrekken met AV artikel 5** (opzet-carve-out, jaarplafond, vervaltermijn)?
 → **Advies: ja.** De huidige totaaluitsluiting inclusief opzet is aantastbaar en sleept de nuttige beperking mee in haar val.

11. **Mediationplicht en arbitrage aanpassen?**
 → **Advies: ja.** Forum gelijktrekken met AV 8.2, mediation optioneel, uitdrukkelijke uitzondering voor geheimhoudings-, IE- en bewijsvorderingen. SGOA-arbitrage alleen behouden voor niet-EU-gebruikers van laag 2.

12. **AV-reparatie: de zin "U zorgt ervoor dat uw gebruikers die voorwaarden aanvaarden en naleven" terugzetten in artikel 1.6 v3.11?**
 → **Advies: ja, vóór publicatie.** Hij is bij het inkorten weggevallen en is juist bij de garage-uitrol de hefboom die de klant tot partner maakt. Nu gratis, later een AV-wijziging met opzegvenster.

13. **De nieuwe teksten meenemen in dezelfde advocaat-eindcheck als v3.11?**
 → **Advies: ja.** Eén ronde, één beoordeling van het samenhangende pakket — dat is ook goedkoper dan twee losse checks, en de samenloopvragen uit onderdeel B zijn juist wat een externe blik moet zien.
