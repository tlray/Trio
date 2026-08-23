# Agentronde v3.11 — bevindingen en voorstellen (23-8-2026)

Acht parallelle reviews (Opus 5): vijf brillen (klant-jurist, rechter, Data Act/AVG tegen de verordeningstekst, vergelijking met gangbare NL SaaS-voorwaarden, klant-eigenaar) en drie scenario-lopers (tekenen/betalen/groei; storing/namaak/derden; einde/overstap/faillissement). Bevindingen ontdubbeld, tegen de bewuste ontwerpkeuzes gelegd en gewogen. "×N" = door N brillen onafhankelijk gevonden. Niets is doorgevoerd; per punt staat een concreet tekstvoorstel.

**Triage:** Blok A = echte fouten, goedkoop te dichten, bij voorkeur vóór verzending. Blok B = beslispunten waar een bewuste keuze onder druk staat. Blok C = waardevol voor v3.12. Blok D = gemeld maar bewust geen actie.

---

## Blok A — aanbevolen vóór verzending

**A1. Boete-rekenmechaniek 3.7 (×4) — ernst hoog.** (i) Bij een jaarvergoeding onder ± € 6.250 ligt het plafond (4×) ónder het minimum van € 25.000: interne tegenstrijdigheid, uitleg tegen de opsteller. (ii) Bij een ex-klant is "de vergoeding over de twaalf maanden vóór de overtreding" nul — boete én plafond imploderen in precies het doelscenario. (iii) "samen tot ten hoogste" is dubbelzinnig (per overtreding of totaal).
*Fix — vervang de tweede en derde volzin van 3.7:*
> Daarom betaalt u ons bij overtreding van artikel 3.1 tot en met 3.5 per overtreding direct en zonder ingebrekestelling een boete van twee keer uw jaarvergoeding, met een minimum van € 25.000, plus € 1.000 per dag dat de overtreding voortduurt. Per overtreding bedraagt de boete in totaal ten hoogste vier keer uw jaarvergoeding, met een minimum van € 50.000. Uw jaarvergoeding is de vergoeding die u aan Brightmotive verschuldigd was over de laatste twaalf maanden waarin de overeenkomst liep; liep de overeenkomst in totaal korter dan twaalf maanden, dan wordt de vergoeding over de werkelijke looptijd herrekend naar twaalf maanden.

**A2. Nawerking na het einde van de overeenkomst (×3) — hoog.** Alleen 3.2 en 3.3 regelen hun nawerking; a contrario eindigen 3.1, 3.4, 3.5 en 3.7 (en artikel 5, 8.2) mét de overeenkomst — het ex-klant-kloonscenario.
*Fix — nieuw 8.8:*
> 8.8 Bepalingen die naar hun aard bestemd zijn om na het einde van de overeenkomst te blijven gelden, blijven daarna van kracht, waaronder in ieder geval de artikelen 1.7, 3, 5, 6.4, 6.5 en 8. Een overtreding die vóór het einde is begonnen en daarna voortduurt, blijft een overtreding.

**A3 (geconsolideerd, omvat ook het oude A4). Alle artikel 3-uitzonderingen in één herschreven 3.6 (×3+×3) — hoog.** Vier problemen met één oorzaak: letterlijk zijn de eigen prijzen/orders van de klant "bedrijfsgeheim van Brightmotive" (3.2), is de eigen ERP-koppeling verboden extractie met boete (3.5, bovendien het type beding dat art. 13 lid 5 Data Act niet-bindend maakt), en mag de klant zijn garages geen toegang geven (3.4 toestemmingseis; 3.9 "aan derden in gebruik geven") terwijl 4.4 en het bedrijfsmodel dat veronderstellen. In plaats van losse reparatiezinnen per lid: alle uitzonderingen op de natuurlijke plek, het bestaande uitzonderingenlid 3.6. "Dit artikel beperkt niet…" werkt over alle leden tegelijk. De losse eigen-gegevens-zin in 3.1 (van 23-8) vervalt daarbij weer — die gaat hierin op.
*Fix — vervang 3.6 door:*
> 3.6 Dit artikel beperkt niet de rechten die u op grond van dwingend recht toekomen. Uw eigen gegevens (artikelen 3.8 en 6.5) zijn geen vertrouwelijke informatie of bedrijfsgeheim van Brightmotive; u mag ze vrij gebruiken en opvragen, ook via de daarvoor bestemde koppelingen. Bestellen bij uw organisatie(s) door uw afnemers geldt als uw eigen gebruik van de diensten; op die afnemers zien de gebruiksvoorwaarden van artikel 1.8. Dit artikel belet u niet om een eigen of concurrerend systeem te (laten) ontwikkelen of af te nemen zonder daarvoor de diensten, documentatie, data of vertrouwelijke informatie van Brightmotive te gebruiken, en evenmin om over te stappen (artikel 6.4). Ieder onderdeel van dit artikel geldt als een afzonderlijk beding.

*Afweging bij het schrappen van de wetsverwijzingen (45j–45m Aw, databankrecht, Verordening 2023/2854): het generieke "dwingend recht" dekt ze alle drie en doet hetzelfde juridische werk; de opsomming was vooral demonstratief pantser. Desgewenst kan de advocaat dit bij de eindcheck terugwegen.*
*Plus: in 3.1 de zin "Uw eigen gegevens (artikelen 3.8 en 6.5) vallen hier niet onder." schrappen.*

**A4. Vervallen — opgegaan in A3.**

**A5. Beëindigingsrecht voor Brightmotive ontbreekt volledig (×5 — vaakst gevonden gat) — hoog.** Geen grond om er zelf uit te kunnen bij wanbetaling, namaak of insolventie/staking van de klant; terugval op de wettelijke ontbinding betekent ingebrekestelling, rechterlijke toets én ongedaanmaking van vooruitbetaalde kwartalen.
*Fix — nieuw 6.6:*
> 6.6 Brightmotive kan de overeenkomst geheel of gedeeltelijk met onmiddellijke ingang schriftelijk beëindigen, zonder ingebrekestelling en zonder tot schadevergoeding gehouden te zijn, indien u een opeisbaar bedrag niet betaalt binnen 14 dagen na aanmaning, indien u artikel 3 overtreedt, of indien u surseance van betaling of faillissement aanvraagt of daarin komt te verkeren, uw onderneming staakt of overdraagt, of op een aanmerkelijk deel van uw vermogen beslag wordt gelegd. Alles wat u aan Brightmotive verschuldigd bent is dan direct opeisbaar, geleverde diensten worden niet ongedaan gemaakt en de vergoeding over het restant van de lopende periode blijft u als beëindigingsvergoeding verschuldigd.

**A6. Data-afwikkeling bij een einde zónder overstap + slotzin 3.8 (×2) — hoog.** 6.5 hangt volledig aan de overgangsperiode van 6.4; bij een gewone opzegging is er geen ophaal- of wisregime. En de slotzin van 3.8 geeft een onbegrensd kopie-recht "tijdens en na de overeenkomst" dat elk venster doorkruist.
*Fix — geen nieuw lid; vervang de vierde en vijfde zin van 6.5 door:* "Overige exporteerbare gegevens stellen wij op verzoek als export beschikbaar in een gangbaar, machineleesbaar formaat, bijvoorbeeld CSV. De export blijft beschikbaar tot 30 kalenderdagen na het einde van de overgangsperiode of, eindigt de overeenkomst zonder overstap, tot 30 kalenderdagen na de einddatum; daarna zullen wij deze data wissen."
*Fix — slotzin 3.8:* "Dit beperkt niet uw recht om uw eigen gegevens te gebruiken en daarvan tijdens en na de overeenkomst een kopie te ontvangen; daarvoor geldt artikel 6.5."

**A7. Herstel duurzin 3.3 (rechter) — hoog, gratis.** De vandaag ingekorte zin kan zo worden gelezen dat óók het onbeperkte geheimhoudingsdeel na één jaar stopt — de kern van de bescherming.
*Fix:* "Voor de diensten, documentatie en data geldt dit tijdens de overeenkomst en tot één jaar daarna. Voor de vertrouwelijke informatie van artikel 3.2 blijft dit zonder tijdsbeperking gelden, zolang zij niet openbaar is."

**A8. Fatale-termijnen-boemerang 8.3 (klant-jurist) — hoog.** "Overeengekomen termijnen zijn geen fatale termijnen" geldt naar de letter ook voor de termijnen van de klánt (omzetopgave, meldplicht 4.4, schademelding 5.3, aankondiging 6.4) — en pardonneert dus zijn overschrijdingen, inclusief de grondslag onder de 25%-opslag.
*Fix — vervang 8.3:* "Termijnen die voor Brightmotive gelden zijn geen fatale termijnen, tenzij uitdrukkelijk anders overeengekomen. Termijnen die voor u gelden, waaronder betalingstermijnen en de termijnen in de artikelen 4, 5.3, 6 en 7, verstrijken van rechtswege."

**A9. Afwijzing inkoopvoorwaarden + rangorde ontbreken (×2) — hoog.** Grossiers en inkoopcombinaties verwijzen standaard naar eigen inkoopvoorwaarden; onder de first-shot-regel (art. 6:225 lid 3 BW) winnen díe dan, en sneuvelt het hele bouwwerk. Er is ook geen rangorde tussen tekenblad, verwerkersovereenkomst en deze voorwaarden.
*Fix — nieuw 7.4:*
> 7.4 De toepasselijkheid van uw eigen inkoop- of andere voorwaarden wijzen wij uitdrukkelijk van de hand, ook als wij daartegen niet telkens opnieuw protesteren. Bij strijdigheid geldt deze rangorde: de ondertekende overeenkomst, de verwerkersovereenkomst (voor de verwerking van persoonsgegevens), aanvullende dienstvoorwaarden (artikel 1.9), deze voorwaarden, aanvullende gebruiksvoorwaarden (artikel 1.8).

**A10. Ingangsdatum 6.1 eenduidig (×2; direct relevant voor de lopende offerte) — hoog.** 6.1 kent twee ingangsmomenten zonder voorrangsregel én een vaste "twee jaar" die met een driejarig tekenblad botst zonder rangorde (die komt uit A9).
*Fix — vervang 6.1:* "De overeenkomst gaat in op de ingangsdatum die in de overeenkomst is vermeld of, als die ontbreekt, op de dag van ondertekening door beide partijen, en heeft de in de overeenkomst vermelde looptijd of anders een looptijd van twee jaar."
*Plus — toevoegen aan 4.1 (gangbare standaardzin, lage salience):* "U mag uw betalingsverplichting niet opschorten en niet verrekenen."
*Plus — tekenblad-discipline (bouwsteen, niet in de AV): de ingangsdatum op het tekenblad is altijd een kalenderdatum, nooit gekoppeld aan go-live, oplevering of acceptatie.*

**A11. Aansprakelijkheidsplafond 5.1 dichttimmeren (klant-jurist) — hoog.** (i) "opzet of bewuste roekeloosheid van Brightmotive óf haar bedrijfsleiding": via toerekening telt opzet van élke medewerker als opzet "van Brightmotive" en valt het plafond weg — de standaard is alleen de bedrijfsleiding. (ii) Het jaarplafond ("het hiervoor bedoelde bedrag") is bij meerdere gebeurtenissen onbepaald.
*Fix — vervang 5.1:* "Behoudens in geval van opzet of bewuste roekeloosheid van de bedrijfsleiding van Brightmotive is de aansprakelijkheid van Brightmotive beperkt tot het bedrag dat u aan Brightmotive verschuldigd was over de drie maanden voorafgaand aan de schade toebrengende gebeurtenis, met een minimum van € 5.000. Een samenhangende reeks gebeurtenissen geldt als één gebeurtenis. De totale aansprakelijkheid van Brightmotive bedraagt per kalenderjaar ten hoogste het bedrag dat volgens de eerste zin geldt voor de eerste gebeurtenis in dat kalenderjaar." *(De bodem van € 5.000 voorkomt het "illusoir plafond"-argument: een plafond dat feitelijk nul kan zijn, riskeert integrale terzijdestelling — en dan is de aansprakelijkheid onbeperkt.)*

**A12. Zelfverwijzing 1.8 en verhouding 1.9 (×2) — middel, gratis.**
*Fix — slot 1.8:* "Bij strijd tussen die gebruiksvoorwaarden en deze voorwaarden gaan deze voorwaarden voor."
*Fix — slot 1.9:* "Voor die dienst gaan zij vóór deze voorwaarden, voor zover zij daar uitdrukkelijk van afwijken."

**A13. "Optimale beschikbaarheid" in 2.1 ontscherpen (×2) — middel.** "Optimaal" en "snel" zijn objectiveerbaar; een klant laat een deskundige invullen wat "optimaal" is en verwijt een tekortkoming zonder dat er ooit een SLA was. Deze fix beschermt juist de bewuste geen-SLA-keuze.
*Fix — vervang de eerste twee zinnen van 2.1:* "Brightmotive spant zich naar redelijkheid in voor de beschikbaarheid en de responstijd van de systemen en om deze zoveel mogelijk vrij te houden van fouten, gebreken en virussen. Gegarandeerde niveaus gelden alleen indien en voor zover partijen die in een afzonderlijke Service Level Agreement zijn overeengekomen."

---

## Blok B — beslispunten (bewuste keuzes onder druk)

**B1. Hoogte beëindigingsvergoeding / de verlengingsval (×3).** Het restant van een stilzwijgend verlengde periode (tot ± 23 maanden) wordt door drie brillen als vrijwel zeker matigbaar en als overstapbelemmering (art. 23 Data Act, ACM) beoordeeld; de koppeling met een 7.2-opzegging maakt het erger. Opties: (a) laten en het procesrisico accepteren; (b) beperken tot het restant van de periode die liep op het moment van de aankondiging, met uitzonderingen voor opzegging o.g.v. 6.3 en 7.2; (c) een plafond (bijv. zes maandvergoedingen). Sowieso nodig: een berekeningsregel bij een dynamische vergoeding (gemiddelde van de laatste twaalf gefactureerde maanden). *Advies: (b) + de berekeningsregel; (c) als extra zekerheid.* **BESLOTEN 23-8: optie (b) doorgevoerd** — anker op het aankondigingsmoment, opeisbaar op de einddatum, twaalfmaandsgemiddelde bij dynamische vergoeding, geen vergoeding bij opzegging o.g.v. 6.3 of 7.2.

**B2. 3.8 en persoonsgegevens (×3).** [BESLOTEN 23-8: doorgevoerd] De vandaag geschrapte verwerkers-zin blijkt dragend: zonder haar bepaalt Brightmotive zelf het doel ("verbetering en ontwikkeling") en wordt zij voor die verwerking verwerkingsverantwoordelijke (art. 28 lid 10 AVG), in tegenspraak met 1.4 — een hefboom voor elke klant-FG. *Advies: één laag-saliente zin terug:* "Voor zover Brightmotive daarbij persoonsgegevens verwerkt, gebeurt dit volgens de afspraken over persoonsgegevens (artikel 1.4)." Het voertuighistorie-plan blijft intact; de echte regeling komt in de verwerkersovereenkomst-carve-out (staat geagendeerd).

**B3. "Niet nogmaals exporteren" (6.5, derde zin).** [BESLOTEN 23-8: zin geheel geschrapt] Bewuste keuze, maar art. 30 lid 5 Data Act eist álle exporteerbare data op verzoek; als weigeringsrecht geformuleerd is de zin niet-conform. *Advies-variant die het doel (geen dubbel werk) behoudt:* "Gegevens die u zelf heeft aangeleverd of die u doorlopend via de koppeling met uw eigen systemen ontvangt, leveren wij alleen op uw verzoek mee."

**B4. Doelbinding van het verlengingsrecht (6.4).** [BESLOTEN 23-8: doelbinding geschrapt, einddatum-opgave behouden] Mijn toevoeging van vandaag ("ten behoeve van het voltooien van de overstap") beperkt een wettelijk onvoorwaardelijk recht (art. 25 lid 5: "een periode die de klant voor zijn eigen doeleinden geschikter acht"). *Advies: doelbinding schrappen, de einddatum-opgave houden.*

**B5. De 14-werkdagenmelding (6.4).** [BESLOTEN 23-8: doorgevoerd] Art. 25 lid 4 eist: melding binnen 14 werkdagen ná het verzoek, mét motivering, waarbij wíj de alternatieve duur noemen. De huidige zin laat de zeven maanden bovendien "van rechtswege" intreden — dat kan tegen ons worden gelezen. *Advies:* "Is dat technisch niet haalbaar, dan melden wij dit gemotiveerd binnen 14 werkdagen na uw aankondiging en noemen wij daarbij de langere overgangsperiode, van ten hoogste zeven maanden."

**B6. Indexering definiëren (4.8) (×3).** [BESLOTEN 23-8: afgewezen — 4.8 blijft zoals hij is] De vaagheid werkt tégen ons: de klant claimt de laagste index of onbepaalbaarheid. *Advies:* "Brightmotive heeft het recht de vergoedingen jaarlijks per 1 januari te verhogen met de stijging van het CBS-consumentenprijsindexcijfer, met een minimum van 3%; een daling verlaagt de vergoeding niet. Dit geldt naast artikel 4.2 en is een voorziene regeling als bedoeld in artikel 7.1."

**B7. Hacks als overmacht kwalificeren (5.4) (×3).** [BESLOTEN 23-8: doorgevoerd, zonder "passend"] De kale opsomming sneuvelt toch (art. 6:75 BW) en ondermijnt het eigen beveiligingsverhaal. *Advies — in de opsomming:* "virussen, hacks en andere onrechtmatige inbreuken die plaatsvinden ondanks passende beveiligingsmaatregelen van Brightmotive".

**B8. Prijsmechaniek artikel 4 (×4).** [BESLOTEN 23-8: alle vijf onderdelen doorgevoerd] Samenhangend pakket: (i) terugwerkende kracht van de jaarlijkse omzetaanpassing tot 1 januari, ook bij tijdige-maar-late opgave; (ii) ingangsmoment van de overname-verhoging (eerste dag van de maand na de transactie, naar rato); (iii) "kan gebaseerd zijn" → "is … indien overeengekomen; de tabel/het promillage maakt deel uit van de overeenkomst"; (iv) expliciet dat de omzetgebaseerde vergoeding een vaste periodieke vergoeding is (kwartaal vooraf, naar rato bij gebroken start); (v) de dode verwijzing in 4.4 ("zonder dat dit als toestemming geldt") koppelen aan een echt toestemmingsvereiste. *Advies: doorvoeren als één pakket.*

**B9. Artikel 7 aanscherpen (×2).** [BESLOTEN 23-8: doorgevoerd] (i) Slotzin 7.2 ("gebruik geldt als acceptatie") schrappen — a contrario is geen gebruik geen acceptatie; de wijziging geldt gewoon vanaf inwerkingtreding tenzij tijdig opgezegd. (ii) 7.3: afwijkingen alleen bindend bij uitdrukkelijke aanvaarding door een vertegenwoordigingsbevoegde — anders is elke supportmail (8.4: e-mail = schriftelijk) een bindende afwijking.

---

## Blok C — voor v3.12 (waardevol, niet urgent)

1. [DEELS BESLOTEN 23-8: continuïteitsrisico-informatie, beveiligingsniveau en "gestructureerd" doorgevoerd; overstapkosten-zin en bestemmingsaanbieder-carve-out afgewezen/geparkeerd; website-vermelding wacht op maatregel 18] Data Act-detailelementen: continuïteitsrisico-informatie en beveiligingsniveau tijdens de overstap (art. 25 lid 2 punt a onder iii/iv); het overstapkosten-element (punt i — "wij brengen geen overstapkosten in rekening"); "gestructureerd" toevoegen aan het exportformaat (art. 30 lid 5); toegang voor de bestemmingsaanbieder als gemachtigde derde carve-outen in 3.2/3.4; de website-vermelding van art. 28 lid 2 zodra de pagina bestaat (maatregel 18).
2. Nieuw 2.4: onderdelen van de dienst wijzigen/beëindigen als een databron (TecDoc, HaynesPro, RDW) wegvalt of zijn voorwaarden wijzigt, met evenredige vergoedingsaanpassing en zonder ontbindingsrecht voor het overige.
3. Overmacht-afwikkeling: opschorting, doorlopende betaling voor het geleverde, wederzijdse uitweg na 60 dagen zonder restitutie.
4. Artikel 5: doorbelaste afnemersclaims expliciet in de 5.2-uitsluiting; ontdekkingsmoment bij derdenclaims; absolute vervaltermijn van 12 maanden; derdenbeding (medewerkers/bestuurders/hulppersonen) en gelding voor alle grondslagen en annexen.
5. 1.2 verbreden naar alle toegangsmiddelen (API-sleutels, SSO, tokens, koppelingen) met toerekeningszin; toerekening van gebruikers in 1.8; persoonsgebonden accounts (ook Wbb-maatregel).
6. Handhaving artikel 3: nalevingsverklaring op verzoek, onderzoek door onafhankelijke deskundige bij concrete aanwijzingen, vergoeding van werkelijke onderzoeks- en rechtsbijstandskosten (contractuele vorderingen krijgen géén volledige proceskostenvergoeding ex art. 1019h Rv).
7. Bewijsvermoeden bij het "zelfstandig ontwikkeld"-verweer (toegang gehad + op hoofdlijnen gelijk → vermoeden; te weerleggen met gedateerde ontwikkeldocumentatie).
8. Vervallen — opgegaan in A3 (het woord "daarvoor" in de slotzin van het nieuwe 3.6 lost de door de rechter-bril gesignaleerde dubbelzinnigheid op).
9. 8.4: ontvangstregeling e-mail (laatst opgegeven adres; geldt als ontvangen op de dag van verzending behoudens foutmelding; contactgegevens actueel houden).
10. 8.6: spiegelverbod (klant draagt niet over zonder toestemming) + meld- en beëindigingsrecht bij overname van de klant door een concurrent-cataloguspartij.
11. 6.3 opschonen (dode letter over de houdstermaatschappij concretiseren of schrappen; geen beëindigingsvergoeding bij faillissement Brightmotive).
12. Stijl: "wij/ons" vs. "Brightmotive/zij" gelijktrekken; kleine taalfixes (responstijd/responsetijd, "gebruiksvergoedingspromillage", "ervan uitgaan").

---

## Blok D — gemeld, bewust geen actie

- Concept-kop en vetmarkeringen in de bijlage: al ondervangen (de Notion-PDF is schoon; de agent las het repo-bestand).
- SLA-niveaus, hogere aansprakelijkheid, lagere boete, audit-begrenzing: klantwensen; bewuste eenzijdigheid blijft.
- 3.1 middelen-gebonden maken (rechter-voorstel): verzwakt het kroonjuweel; in plaats daarvan de 3.6-verduidelijking (C8).
- Minimumvergoeding bij omzetdaling: geen fout maar een commerciële keuze; desgewenst later.

---

*Advies over de lopende offerte: Blok A is in ± een uur door te voeren en juist een concernklant met juristen raakt A1, A4, A5, A9 en A10. Liefst eerst A, dan versturen. Blok B vergt per punt een keuze; Blok C kan rustig naar v3.12 met de advocaat-eindcheck.*
