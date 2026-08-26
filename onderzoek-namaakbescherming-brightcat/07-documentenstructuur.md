# Documentenstructuur Brightmotive

Kompas voor alle juridische documenten: welk document er is, voor wie, en volgens welke principes nieuwe documenten worden gebouwd. Vastgesteld 23-8-2026 naar aanleiding van het namaakbescherming-onderzoek.

## Het huis

| Document | Voor wie | Wat het regelt | Versiereeks / status |
|---|---|---|---|
| **Algemene voorwaarden** (naam blijft; functioneel: de paraplu voor alle diensten aan de klant) | Contractspartijen: grossiers en inkooporganisaties | Afname van BrightCat én uitbreidingsdiensten: gebruik, omzetafhankelijke vergoeding, aansprakelijkheid, duur, artikel 3 (namaak/geheimhouding/boete), overstap (Data Act), haakbepalingen 1.6 en 1.7 | v3.x — v3.04 actief, v3.11 in offerte gebruikt (bevroren), v3.12 concept (1.6-zorgplicht) |
| **Dienstmodules** (per uitbreidingsdienst, half A4) | Dezelfde klanten, per afgenomen uitbreiding | Alleen de afwijkingen: dienstomschrijving + prijsmodel, flow-down-beperkingen van de licentiegever (kernbeperkingen zelf opnemen), dienstspecifieke gebruiksregels (bijv. AVG-doelbinding bij kenteken/VIN), einde van de module | Nieuw; per dienst (HaynesPro, kenteken/VIN, …) |
| **Gebruikersvoorwaarden** (clickwrap) | Iedereen die feitelijk inlogt: garagemedewerkers, developers, documentatielezers, leveranciers-medewerkers | Gedragsregels, rol-onafhankelijk: doelbinding-per-toegang, universele verboden (namaak, geheimhouding, scraping, reverse engineering met carve-out), account persoonlijk, gerichte boete | v2.x gepland; vervangt Documentation Terms of Use v1.01 |
| **Leveranciersvoorwaarden** | Onderdelenleveranciers die betalen om voorraad/producten te laten verwerken en tonen | Tweede verkoopset (broertje van de AV): verwerkings-/listingvergoeding, datalicentie van leverancier aan Brightmotive (verwerken, verrijken, tonen aan de keten; behoud verrijkingslaag na einde), garanties + IE-vrijwaring (o.a. beeldrecht), artikel 3-kern, eigen overstap-/exportregeling (Data Act) | v1.x — schrijven zodra vergoedingsmodel en portaal concreet zijn |
| **Annexen** | Per overeenkomst | Verwerkersovereenkomst, eventueel SLA, eventueel Overstapregeling | Bestaand (Contract Annexes) |
| **Bouwstenen** (intern) | — | Gedeelde teksten: aansprakelijkheid, overmacht, wijzigingsprocedure, recht/forum, salvatorisch, en de artikel 3-kern (namaak/geheimhouding/scraping/boete) in per doelgroep passende zwaarte | Eén bron; wijziging begint hier |

## Rangorde

Getekende overeenkomst/order → annexen → dienstmodule (voor die dienst; art. 1.7) → Algemene voorwaarden → gebruikersvoorwaarden (art. 1.6). Elke set benoemt zijn eigen plek; nooit impliciet laten.

## Bouwprincipes

1. **Per doelgroep één zelfstandig document** — geen "algemene kern + verplichte modules"-gelaagdheid richting de wederpartij: één lezer, één document, één terhandstelling. Duplicatie wordt beheerst via de bouwstenen, niet via extra juridische lagen.
2. **Functioneel verwijzen** — nooit een documentnaam of versienummer in een ander document ("de voorwaarden die Brightmotive daarvoor hanteert", art. 3.4). Documenten kunnen dan zelfstandig doorontwikkelen.
3. **Haakbepalingen voor de toekomst** — art. 1.6 (aanvullende gebruiksvoorwaarden/clickwraps) en art. 1.7 (dienstmodules incl. licentiegeversvoorwaarden) maken nieuwe documenten "al voorziene regelingen" (art. 7.1): invoering is geen AV-aanpassing.
4. **De namaak-kern overal** — het regime uit het onderzoek (namaakverbod op hoofdlijnen, bedrijfsgeheim-kwalificatie, doelgebonden concurrentieverbod, extractieverbod, dwingend-recht-carve-outs, gerichte boete) wordt in elk doelgroep-document gespiegeld, in passende zwaarte. Eén beschermingsregime over de hele keten.
5. **Eén register** — de Contract Annexes-database in Notion is het versieregister voor alle sets (eigen versiereeks, status Draft/Active/Archived); dienstmodules krijgen daar een eigen categorie.
6. **Flow-down sluitend** — vóór het schrijven van een dienstmodule eerst het eigen inkoopcontract (HaynesPro, kentekenbron) nalopen op door te leggen verplichtingen; de module moet daar één-op-één op aansluiten.

## Besluiten

- **Naam "Algemene voorwaarden" blijft.** Juridisch is de titel irrelevant (uitleg gaat naar inhoud); de naam is ingeburgerd bij klanten en alle offertes verwijzen ernaar. Alleen de functie is vastgelegd: paraplu voor alle klantdiensten.
- **Bestaande aparte overeenkomsten** voor uitbreidingsdiensten lopen door en worden bij de eerstvolgende verlenging omgezet naar order + dienstmodule. Geen big bang.
- **Bestaande developer-akkoorden** (Documentation Terms of Use v1.01) blijven geldig tot de gebruikersvoorwaarden v2.0 ze vervangen (uitrol naar bestaande accounts kan via art. 13.2 van v1.01).

## Agendapunten

- **Voertuiggebonden orderhistorie (kenteken/VIN)**: zodra deze feature wordt gebouwd is Brightmotive voor dat gebruik zelf verwerkingsverantwoordelijke (art. 1.4). Dan regelen: belangenafweging op schrift, aanvulling privacyverklaring, carve-out in de verwerkersovereenkomst. Art. 3.8 staat het gebruik al toe (rem zit op herleidbaar delen, niet op intern gebruik); output toont nooit dat of wat een specifiek voertuig eerder bestelde.
- **Bestellingen behouden na vertrek van een klant**: niet de ruwe klantrecords bewaren, maar tijdens het contract een afgeleide laag opbouwen (voertuig ↔ onderdeel ↔ datum, losgeknipt van de klantidentiteit) op grond van art. 3.8. Die laag is verrijking van Brightmotive, valt in 6.5 buiten de exporteerbare gegevens en overleeft elk vertrek en wisverzoek; de ruwe orderdata van de vertrokken klant kan dan gewoon gewist worden. Vereist wél de verwerkersovereenkomst-carve-out en het AVG-huiswerk hierboven (kenteken/VIN blijft een persoonsgegeven). Bewust niets hierover in de AV.

- **Team-update opstellen** over de wijzigingen van v3.04 (actief) naar v3.11, vóór of bij publicatie. Basis: de vet-gemarkeerde concepten v3.05–v3.11 in voorwaarden-versies/ en de statusregels per versiebestand. **[GEDAAN 24-8: zie 10-teamupdate-voorwaarden.md]**
- **Demo-/testaccounts vóór ondertekening**: prospects krijgen soms al toegang vóórdat er een getekende overeenkomst is; de AV binden hen dan nog niet. Dekking in twee lagen: (1) de A2-12-zin in 6.1 laat de artikelen 1, 3, 5, 7 en 8 terugwerken tot het moment van eerste toegang, ook als die vóór de ondertekening lag — dekt iedereen die daarna tekent; (2) voor prospects die nooit tekenen: een gebruiksvoorwaarden-clickwrap op het demo-account (de artikel 1.6-route) met geheimhouding en gebruiksbeperkingen — meenemen in gebruikersvoorwaarden v2.0. Tot die tijd demo-toegang alleen verlenen na een getekende overeenkomst of een NDA.

- **Data Act-bijlage uitwerken** (besluit Ray 24-8): de overstapregeling is uit de AV gehaald (salience — klanten niet op ideeën brengen); voor deze versie/klant bewust weggelaten als risico-acceptatie. Later een aparte contractbijlage met neutrale titel opstellen (art. 25-contractinhoud: aankondigingstermijn, overgangsperiode, categorieën exporteerbare data, einde na voltooiing, ondersteuning; de rangorde in 7.4 dekt bijlagen al). Basis: de oude 6.4/6.5-teksten in de git-historie en document 09. Bij de advocaat-eindcheck laten toetsen; website-acties (maatregel 18) staan hier los van en blijven nodig.
- **2.4 geschrapt** (besluit Ray 24-8): het hele lid is vervallen — onderdeel-wijzigingen vallen onder 2.3, beëindiging van een onderdeel en leverancierskosten-doorberekening lopen via 7.1 (met het 7.2-opzegrecht van de klant bij een wezenlijke verzwaring als ingebouwd ventiel). De geparkeerde A2-11 en B2-3 zijn daarmee definitief vervallen.
- **Rechtstreeks betaalde features voor gebruikers (garages)** — toekomstplan, bewust NIET expliciet in de AV. Kan voor níeuwe features zonder toestemming van de grossier: de AV geven de klant geen exclusiviteit over zijn gebruikers en geen recht op alle toekomstige functionaliteit; de overeenkomst met de garage staat los van de klant-AV. Randvoorwaarden: (1) alleen nieuwe features — bestaande functionaliteit nooit achter een gebruikersbetaalmuur (7.2-opzegrecht + kanaalconflict); (2) AVG-rolverdeling: garage-accountgegevens worden nu als verwerker voor de klant verwerkt — actieve benadering via die gegevens mag niet; het aanbod dus in-app tonen en de koop via de gebruikersvoorwaarden v2.0 laten lopen, waarin de gebruiker zijn gegevens rechtstreeks aan Brightmotive als verantwoordelijke verstrekt; rolverdeling vastleggen in de verwerkersovereenkomst (advocaat, C2); (3) leverancierslicenties (bijv. HaynesPro) moeten directe verkoop aan eindgebruikers toestaan — contract checken per dataset; (4) de mits in 3.6 ("uitsluitend ... bestellen") knelde — de fix ("of voor ander gebruik dat Brightmotive hun toestaat") is op 24-8 geakkordeerd en doorgevoerd. Commercieel: vragen is verstandiger dan doorvoeren, juridisch niet vereist.

## Tekenblad-bouwsteen: meerjarige looptijd met prijsvoordeel

Bewust géén kortingsmechanisme in de AV (zet klanten op ideeën). Bij een incidentele deal met langere looptijd (bijv. 3 i.p.v. 2 jaar) op het tekenblad, twee varianten:

1. **Standaard**: alleen de afgesproken (lagere) prijs bij de langere looptijd vermelden, verder niets — de beëindigingsvergoeding van art. 6.4 beschermt de volledige contractwaarde al bij vroegtijdig vertrek via een overstap.
2. **Bij fors voordeel**: aflopend tarief (bijv. maand 1–12 hoger, daarna lager) met gelijk totaal. Het voordeel valt in latere maanden; wie vroeg vertrekt heeft het nooit genoten, dus er valt niets terug te vorderen en geen einde-clausule nodig.

Nooit een herrekening naar de normale prijs stapelen bóven de restant-vergoeding: samen meer claimen dan de volledige contractwaarde maakt de regeling onevenredig en aantastbaar.

**Ingangsdatum-discipline:** op het tekenblad is de ingangsdatum altijd een kalenderdatum, nooit gekoppeld aan go-live, oplevering of acceptatie — de voorwaarden (4.1, 6.1) rekenen vanaf die datum.

## Volgorde van uitwerking

1. **Gebruikersvoorwaarden v2.0** — dekt vanaf dag één alle rollen, incl. toekomstige leveranciers-medewerkers; neem de v1.02-punten mee (reikwijdte dienst zelf, namaakverbod op hoofdlijnen, scraping-verbod, "zolang geheim").
2. **Dienstmodules** voor de bestaande uitbreidingen (HaynesPro, kenteken/VIN) — na check van de inkoopcontracten; migratie bij verlenging.
3. **Leveranciersvoorwaarden v1.0** — zodra het vergoedingsmodel en het leveranciersportaal concreet zijn, tegen een echte casus schrijven.
