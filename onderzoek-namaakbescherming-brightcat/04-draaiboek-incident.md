# Deliverable 4 — Draaiboek volgend namaak-incident (eerste 30 dagen)

**Gouden regel: eerst stil bewijs veiligstellen, dán pas contact.** Elke vroege sommatie of boze e-mail is een kans voor de wederpartij om repositories, e-mails en data te wissen — terwijl het verlof voor bewijsbeslag juist steunt op de vrees voor verduistering. De fout uit het vorige incident (weinig kunnen uitrichten) begint meestal hier.

**Procesrechtelijk kader (sinds 1 januari 2025; primair geverifieerd tegen de geldende wettekst):** inzagerecht art. 194–195a Rv (art. 843a is vervallen); voorlopige bewijsverrichtingen art. 196–204 Rv (combineerbaar in één verzoekschrift); bewijsbeslag gecodificeerd in art. 205–206 Rv (IE-bewijsbeslag art. 1019b–1019d Rv blijft daarnaast bestaan); nieuw: deurwaarders-proces-verbaal van constateringen, art. 207 Rv — de dwingende bewijskracht daarvan komt uit art. 157 lid 1 Rv (authentieke akte), het verlof brengt de waarneming op een niet-openbare plaats binnen de ambtsbevoegdheid. Bewijsbeslag geeft **geen** inzage — dat is een aparte stap.

---

## Fase 0 — Dag 0–3: stil veiligstellen (géén contact met de wederpartij)

| Stap | Wat | Wie | Doel / valkuil |
|---|---|---|---|
| 0.1 | **Interne litigation hold**: niets wijzigen aan relevante logs en systemen; kring van ingewijden klein houden. | Directie + CTO | Integriteit van het eigen bewijs; loslippigheid richting de markt voorkomen. |
| 0.2 | **Forensische kopie** van eigen logs en tenant-data van de verdachte klant: toegangslogs, exportgedrag, documentatie-kliks, NDA-akkoorden. Hashen, tijdstempelen, chain of custody vastleggen. | Forensisch IT'er + CTO | Dit is het bewijs dat de klant toegang had tot wát — de basis onder contract- én Wbb-claims. |
| 0.3 | **Deurwaarders-pv van de kloon**: laat de deurwaarder het publiek waarneembare deel van de kloon-site/app vastleggen (kan zonder verlof; overweeg verlof ex art. 207 Rv voor dwingende bewijskracht en voor niet-openbare delen). | Deurwaarder | Momentopname vóórdat de wederpartij kan aanpassen. |
| 0.4 | **Canary- en fingerprint-check**: zoek de eigen canary-records, watermerken en fingerprints in de kloon en laat de deurwaarder de **vindplaatsen** in het pv constateren. | Eigen team + deurwaarder | Canaries in de kloon = vrijwel onweerlegbaar overnamebewijs, herleidbaar naar de lekkende klant. |
| 0.5 | **Alleen rechtmatige toegang**: publieke pagina's of een regulier account binnen de normale voorwaarden. **Nooit**: andermans inloggegevens, beveiliging omzeilen, "even in de kloon prikken". | Iedereen | Computervredebreuk is strafbaar en levert tegenclaims op. (Civielrechtelijk wordt onrechtmatig verkregen bewijs meestal wél toegelaten — HR 2014 — maar het risico is het nooit waard.) |

## Fase 1 — Dag 3–10: analyse en beslag

| Stap | Wat | Wie | Doel / valkuil |
|---|---|---|---|
| 1.1 | **Advocaat inschakelen; grondslagen ordenen**: contract/boete (art. 3 AV), bedrijfsgeheimen (Wbb), databankrecht op verrijkte data, auteursrecht op code/teksten/assets, onrechtmatige daad (tegen de bouwer). Routekeuze bepaalt ook het proceskostenregime (art. 1019h Rv snijdt aan twee kanten: verlies je op de IE-grondslag, dan betaal jij de volledige kosten van de wederpartij). | Advocaat | Niet alles op de IE-kaart zetten: nagebouwde functionaliteit is auteursrechtelijk zwak (SAS-leer); contract + boete + Wbb zijn hier meestal sterker. |
| 1.2 | **Verlofverzoek conservatoir bewijsbeslag** bij de voorzieningenrechter (IE-grondslag: art. 1019b–1019d Rv; overig: art. 205–206 Rv). Bepaald en gericht omschrijven: servers, repositories, e-mail tussen klant en bouwer, databasedumps. Bewaarder + forensische kopie-modaliteiten vragen. Wordt ex parte behandeld; tegen het verleende verlof staat geen hogere voorziening open (art. 205 lid 6 Rv). | Advocaat; uitvoering deurwaarder + onafhankelijk forensisch IT'er | Valkuilen: te breed formuleren (fishing expedition → afwijzing), en denken dat beslag leesrecht geeft — inzage is stap 2.2. |
| 1.3 | Overweeg in hetzelfde verzoekschrift **voorlopige bewijsverrichtingen** (art. 196 Rv): voorlopig getuigenverhoor van de bouwer, pv van constateringen. | Advocaat | Alles in één keer; verrassingseffect behouden. |
| 1.4 | Beslag laten leggen. | Deurwaarder + IT'er + bewaarder | Daarna niet stilzitten: termijnen voor de eis in de hoofdzaak bewaken. |

## Fase 2 — Dag 10–20: sommatie en inzage (pas ná het beslag)

| Stap | Wat | Wie | Doel / valkuil |
|---|---|---|---|
| 2.1 | **Sommatie aan klant én bouwer**: staken en gestaakt houden; onthoudingsverklaring met boete per overtreding/per dag; opgave van afnemers en omzet; bewaarplicht; beroep op art. 3 AV, de NDA en de Wbb; termijn 5–7 dagen. | Advocaat | De brief aan de bouwer **fixeert diens wetenschap** (art. 2 lid 3 Wbb): alles wat hij daarna nog doet (doorontwikkelen, opleveren, hosten) is evident onrechtmatig. Contractuele dagboetes vanaf nu niet stil laten oplopen — direct aanzeggen. |
| 2.2 | **Inzageverzoek** (art. 194/195 Rv; bij IE via art. 1019a Rv) op het beslagen materiaal: benoem bepaalde gegevens (de bestanden met jouw canaries, de communicatie over "voorbeelddata", de repository-historie) en stel een vertrouwelijkheidsregime voor (alleen advocaat + deskundige). | Advocaat | Van "beslagen" naar "bruikbaar" bewijs. Kan parallel aan schikkingsgesprekken lopen. |

## Fase 3 — Dag 20–30: routekeuze

| Route | Wanneer | Kern |
|---|---|---|
| **Ex parte verbod** (art. 1019e Rv, alleen IE-grondslagen — niet voor bedrijfsgeheimen) | Evidente 1-op-1-kopie (canaries!, overgenomen code/data) + echte superspoed (kloon wordt actief verkocht) | Verbod zonder dat de wederpartij wordt gehoord; strenge toets, volledige en eerlijke voorlichting van de rechter vereist. |
| **Kort geding** | Standaardroute bij lopende exploitatie | Verbod + dwangsom, gebod tot staken, opgave afnemers, eventueel voorschot op verbeurde boetes (terughoudende toets bij geldvorderingen); proceskosten ex art. 1019h bij IE-grondslag, art. 1019ie bij Wbb (discretionair; kwade trouw helpt). |
| **Bodemprocedure** | Voor het geld en de afwikkeling | Verbeurde boetes (het contract maakt schadebewijs overbodig), schadevergoeding/winstafdracht (art. 27a Aw, rekening en verantwoording), verklaring voor recht, vernietiging van de kloon-codebase (art. 6 Wbb). Bij voorafgaand kort geding op IE-grondslag: termijn eis in hoofdzaak bewaken. |
| **Schikking / vaststellingsovereenkomst** | Vaak rationeel richting een (ex-)klant | Onderhandel vanuit veiliggesteld bewijs; leg staking, controle-mechanisme en een nieuw boetebeding vast. |

## Veelgemaakte fouten (samengevat)

1. Eerst sommeren, dan pas aan bewijs denken — bewijs verdampt.
2. Zelf "inbreken" in de kloon — strafbaar risico, nooit nodig.
3. Alles op het auteursrecht zetten terwijl de functionaliteit-nabouw daar juist vrij is — contract/boete, Wbb en databankrecht zijn de dragende grondslagen.
4. Denken dat bewijsbeslag inzage geeft — inzage is een aparte, latere stap.
5. Canaries geheim willen houden voor de rechter — geheim bewijs telt niet; gebruik rouleerbare sets en een vertrouwelijkheidsregime.
6. Dagboetes stil laten oplopen — weegt bij matiging tegen je.
7. De bouwer vergeten als tweede gedaagde — jegens hem gelden Wbb, databankrecht, auteursrecht en onrechtmatige daad (profiteren van wanprestatie), plus via art. 3.4 AV de aansprakelijkheid van de klant voor zijn gedrag.
8. Het 1019h-kostenrisico onderschatten bij een wankele IE-grondslag.

## Vooraf klaarzetten (eenmalig, zie ook maatregelenlijst #17)

- Vaste IE-/procesadvocaat, deurwaarder met IT-forensische ervaring, forensisch IT-bureau, bewaarder.
- Sjablonen: litigation-hold-instructie, verlofverzoek bewijsbeslag, verzoek pv van constateringen, sommatie met onthoudingsverklaring.
- Contactenlijst + beslisboom (wie belt wie op dag 0) in het bedrijfsgeheimenregister.
- Werkinstructie wanbetaling: eerst opschorten (art. 4.7 AV) als drukmiddel; helpt dat niet, dan aanmanen met 14-dagentermijn en beëindigen via art. 6.6 AV (alles ineens opeisbaar, restant van de periode als beëindigingsvergoeding). Art. 6.6 geldt ook bij een artikel 3-overtreding en bij insolventie of staking van de klant.
- Werkinstructie overstap-aankondigingen (art. 6.4 AV): bij elke aankondiging het exportpakket klaarzetten en de termijnen bewaken (aankondigingstermijn vanaf de dag na ontvangst, overgangsperiode, eventuele verlenging — die moet de klant uiterlijk 14 dagen vóór het einde met een einddatum opgeven). De overeenkomst eindigt op de laatste dag van de overgangsperiode, of eerder zodra de voltooiing van de overstap schriftelijk is vastgesteld (art. 6.4): bevestig direct de einddatum schriftelijk en factureer, bij een einde vóór het einde van de lopende periode, de beëindigingsvergoeding over het restant. Wordt de overstap niet binnen de overgangsperiode voltooid, dan loopt de overeenkomst gewoon door en vervalt de 6.4-ondersteuning voor die aankondiging (nieuwe poging = nieuwe aankondiging); overweeg dan of Brightmotive zelf opzegt tegen het einde van de lopende periode (art. 6.2). Trage of steeds hervatte "migraties" zonder aantoonbare voortgang: aanschrijven op de goedetrouwverplichting van art. 27 Data Act, die ook op de klant rust.
