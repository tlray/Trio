# Implementatiespecificatie clickwrap v2.0 — acceptatielog, versiearchief en acceptatieflows

*Opgesteld 26-8-2026 (Fable-agentronde gebruiksvoorwaarden, implementatie-architect). Bouwt voort op de bestaande flow (akkoord → e-mail met IP, PDF en bevestiging); die blijft en wordt versterkt. Bron van waarheid voor tekst en versie: de brightmotive-docs-repository. Stack-agnostisch; het team vult de techniek in.*

## 1. Het acceptatielog

### 1.1 Kerntabel `terms_acceptance` (append-only)

Eén rij per definitief akkoord (of weigering). Velden: `id` (UUID); `decision` (accepted/declined — ook weigeringen loggen); `user_id`; `user_name_snapshot` en `user_email_snapshot` (naam/e-mail op het moment van klikken — geen join achteraf); `account_type` (regulier/demo/service); `tenant_context` (omgeving/grossier); `stated_organisation` (laag 2: het "namens welke organisatie"-veld, verbatim zoals ingetypt); `stated_org_kvk` (optioneel); `authority_confirmed` (laag 2: het bevoegdheidsvinkje, apart van het akkoord-vinkje); `document_type`; `document_version`; `language_shown` (nl/en/fr — de taalversie die op het scherm stond); `docs_commit_hash`; `text_sha256`; `pdf_sha256`; `flow` (first_login/just_in_time/re_acceptance/migration); `review_step_confirmed_at` (bewijs 6:227c-controlescherm); `accepted_at` (UTC, server-side, NTP); `ip_address` (uit vertrouwde proxy-keten, ruwe XFF apart); `user_agent`; `session_id`/`auth_method`; `source` (live/v1.01_legacy); `prev_hash`/`record_hash` (hash-keten).

### 1.2 Onveranderlijkheid

1. Databaserol alleen INSERT+SELECT; UPDATE/DELETE op databaseniveau geweigerd (revoke + trigger).
2. Hash-keten: `record_hash = SHA-256(canonieke rij + prev_hash)`.
3. Externe verankering: dagelijkse dag-digest (laatste hash + rijenteller) naar WORM-bucket (S3 Object Lock, compliance mode) én per mail naar een administratie-postbus.
4. Bijzaken (mail verzonden/bounce/export gedraaid) in aparte append-only event-tabel `terms_acceptance_event`.

### 1.3 Bewaartermijn en AVG

- Verwijderen op zijn vroegst 5 jaar na accountsluiting (parameter; sluit aan op verjaring 3:307/3:310 BW); purge-job maandelijks via aparte geprivilegieerde rol, logt zichzelf.
- Niet wissen bij AVG-verwijderverzoek; grondslag gerechtvaardigd belang (bewijs) — expliciet in privacyverklaring en verwerkingsregister.
- Leestoegang beperkt tot admin-rol; elk gelezen bewijsdossier wordt gelogd.

### 1.4 Bewijsdossier-export

Adminfunctie: per acceptatie één ZIP met rij-JSON, exacte PDF (hash-gecontroleerd), versiemetadata incl. commit-hash en geldigheidsperiode, hash-keten-verificatierapport en e-mail-events (message-id). Jaarlijkse oefening: drie steekproefdossiers reproduceren.

## 2. Het versiearchief

### 2.1 Bron: brightmotive-docs

`terms/gebruikersvoorwaarden/{nl,en,fr}.md` en `terms/documentatievoorwaarden/en.md`, met per document front-matter/terms.json: versienummer, `material_change`, beoogde ingangsdatum, talen.

### 2.2 Publicatiepipeline (CI)

Publiceren = merge naar main + git-tag (gv-v2.0, dv-v2.0). Pipeline: (1) PDF per taal met versienummer/ingangsdatum/titel in de voettekst (deterministische build); (2) text_sha256 + pdf_sha256; (3) upload naar geversioneerde object-locked bucket; (4) rij in `terms_version` (document_type, version, language, docs_commit_hash, hashes, pdf_uri, material_change, effective_from/until, superseded_by). Releasegate: een laag-1-versie wordt pas effective als alle drie de talen gebouwd zijn. Rijen nooit verwijderen; `terms_version` is de gezaghebbende tijdlijn; de Notion Contract Annexes-database spiegelt status maar is niet de runtime-bron.

### 2.3 Retro-archivering v1.01

Eénmalig v1.01 als rij opnemen met commit-hash, PDF en werkelijke geldigheidsperiode (tot de laag-2-livegang).

## 3. De acceptatieflows

### 3.1 Centrale dienst

Eén terms-service voor alle drie de applicaties: `GET /terms/status`, `GET /terms/current?doc&lang`, `POST /terms/intent` (pint versie/taal/hash, retourneert kortlevend intent-token), `POST /terms/acceptances` (alleen met geldig intent-token: getoond = aanvaard), `GET /me/acceptances` (+ /{id}/pdf). Middleware checkt terms/status op elk request (gecachet, korte TTL) — ook langlopende sessies worden gevangen.

### 3.2 Laag 1 — eerste inlog

Blokkerend interstitial na authenticatie in BrightCat, partners én adminland: scherm 1 (volledige tekst scrollbaar, taalwissel, Download PDF, privacyverklaring-link, akkoord-vinkje standaard uit) → scherm 2 (controlescherm, §4). Eén acceptatie geldt platformbreed.

### 3.3 Laag 2 — just-in-time bij de documentatie

Trigger: eerste keer openen documentatieomgeving, altijd ná laag 1. Extra: verplicht organisatieveld (vrije tekst, optionele pre-fill maar gebruiker bevestigt zelf; optioneel KvK-veld; verbatim opslaan) en apart bevoegdheidsvinkje met de artikel 1-verklaring. Technische afdwinging (harde eis): geen docroute of bestand bereikbaar zonder de gate — server-side middleware op álle routes, bestanden alleen via kortlevende signed URLs ná gate-check, zoekresultaten achter de gate, Cache-Control: private, noindex. Alles wat langs de klik heen leesbaar is valt buiten het contract én verzwakt de bedrijfsgeheimenclaim.

### 3.4 Her-acceptatie bij inhoudelijke wijziging

`material_change = true` → bestaande acceptaties verouderen; blokkerend scherm bij eerstvolgend request, geen "later herinneren". Weigeren: declined-rij, informatiescherm met PDF + contactoptie, sessie-einde. Laag 1-weigering blokkeert de applicatie; laag 2-weigering alleen de documentatie. Account blijft bestaan; alsnog accepteren kan; na 30 dagen actieve weigeraar op supportrapportage. Redactioneel (`material_change = false`): geen her-klik, eenmalige melding + wijzigingsoverzicht.

### 3.5 Meertaligheid

Laag 1 NL/EN/FR; getoonde taal volgt UI-voorkeur (fallback NL→EN), wisselbaar op het scherm; vastgelegd wordt de taalversie die bij het definitieve akkoord op het scherm stond. Drie talen van één versienummer altijd samen releasen; anders alleen cohort-uitrol per locale. Laag 2: gepubliceerde versie Engels (één bindende taal); language_shown toch loggen.

### 3.6 Migratie bestaande accounts

Go-live: iedereen krijgt de eerste-inlogflow bij eerstvolgend gebruik — geen e-mailacceptatie, geen stille conversie. Bestaande v1.01-acceptanten klikken bij eerstvolgend documentatiebezoek opnieuw op laag 2. Oude akkoorden importeren als source = v1.01_legacy.

## 4. De 6:227c-bevestigingsstap en terhandstelling

### 4.1 Controlescherm (verplichte tweede stap)

"U staat op het punt akkoord te gaan met [document], versie [x] ([taal])" + te controleren gegevens (naam, e-mail; laag 2: organisatie + bevoegdheidsvinkje). Knoppen "Wijzigen" (terug mét behoud invoer — de 6:227c-herstelmogelijkheid) en "Definitief akkoord" (pas die schrijft de rij); review_step_confirmed_at bewijst de stap; intent-token pint versie/taal/hash. Melding aan juridisch: de v2.0-teksten missen nog de 6:227b/c-uitsluitingszin voor zakelijke gebruikers — tekstbeslissing voor de advocaat-eindcheck; de stap wordt hoe dan ook gebouwd.

### 4.2 Terhandstelling

Twee kanalen, beide verplicht (6:234 lid 2 BW): (1) downloadbare versie-PDF op scherm 1 én het controlescherm, vóór het akkoord; (2) e-mail direct na acceptatie (bestaande flow, versterkt): bevestiging, tijdstempel UTC+lokaal, IP, versienummer, taal, pdf_sha256, PDF als bijlage, link naar "Mijn akkoorden"; queue met retries; message-id en aflever-/bounce-events gelogd; SPF/DKIM/DMARC op orde. De e-mail versterkt het bewijs maar is niet constitutief.

## 5. Permanente raadpleegbaarheid

1. Voettekst-link "Voorwaarden" in alle drie de apps → voorwaardenpagina (achter login altijd bereikbaar): actuele versies per document/taal + versiegeschiedenis uit terms_version.
2. Accountpagina "Mijn akkoorden": per akkoord document, versie, taal, datum/tijd, (laag 2) organisatie, download van exact de aanvaarde PDF, knop "bevestigingsmail opnieuw versturen".
3. Laag 1 óók publiek zonder login — advies ja: niets vertrouwelijks, ondersteunt terhandstelling vóór accountaanvraag en meelezen door juristen van klanten. Met expliciete zin: lezen is geen aanvaarding; aanvaarding gebeurt bij de eerste inlog. Laag 2: standaard achter login (tekst is niet geheim; op verzoek deelbaar) — beslispunt, default niet publiek.

## 6. Randgevallen

1. **API-sleutels/koppelingen zonder UI**: machineverkeer accepteert niets; de mens in de lifecycle wel. API-credentials alleen aan te maken/bekijken/verlengen in het partnersportaal achter de laag-2-gate; log key.created_by → acceptance. Bestaande of namens een partij uitgegeven sleutels: activering/verlenging pas na laag-2-flow door benoemde technische contactpersoon. Nooit lopend API-verkeer blokkeren op acceptatie; de organisatie is via de klant-AV al gebonden.
2. **Gedeelde accounts**: log van IP/user-agent per klik is de mitigatie; detectie gelijktijdige sessies → nudge; voor laag 2 strenger: service-/gedeelde accounts standaard geen documentatietoegang. Bewuste beperking documenteren.
3. **E-mailbounces**: webhook → event; retry bij soft bounce; bij hard bounce blijft het akkoord geldig, gebruiker krijgt in-app-taak + beheerdersrapportage; bounce-bewijs bewaren.
4. **Accounts zonder e-mail**: flow werkt zonder mailstap (vlag in log, nadruk op PDF-download); nieuwe accounts vereisen e-mail.
5. **Demo-accounts**: laag 1 verplicht (dekt het prospects-gat), account_type = demo; standaard geen documentatietoegang.
6. **Request account-flow**: alleen informeren (link naar publieke laag-1-pagina + zin dat bij eerste inlog akkoord wordt gevraagd); geen acceptatie bij de aanvraag.
7. **Legacy-bewijs**: bestaande akkoord-e-mails/logs importeren als v1.01_legacy-rijen, gekoppeld aan de v1.01-versierij; onvolledigheid markeren, niet verzinnen.
8. **Support-impersonatie**: "inloggen als gebruiker" triggert nooit een acceptatiescherm en kan nooit een akkoord vastleggen; impersonatiesessies auditen. Eigen personeel valt onder de arbeidsrelatie, niet onder deze clickwraps.

## 7. Gefaseerd uitrolplan

- **Fase 0 — fundament (blokkerend)**: terms_version + pipeline, acceptatielog + hash-keten + WORM, versterkte mailflow + bounce-webhooks, retro-archivering v1.01 + legacy-import, bewijsdossier-export. Gates voor fase 1: teksten definitief ná advocaat-eindcheck; privacyverklaring voor gebruikers live (staat op het scherm); EN/FR-vertalingen laag 1 gereed of besluit cohort-uitrol.
- **Fase 1 — laag 1 live**: terms-service + middleware in drie apps, tweestapsflow, voettekstlinks, "Mijn akkoorden", publieke laag-1-pagina, migratie via eerste inlog. Klanten 4–6 weken vooraf informeren — als informatie, níet als 7.1-wijziging. Monitoring: acceptatiegraad, weigeringen, bounces.
- **Fase 2 — laag 2 vervangt v1.01**: just-in-time-gate incl. volledige server-side afgrendeling (signed URLs, zoekindex, caching), organisatieveld + bevoegdheidsvinkje, her-klik v1.01-acceptanten, API-sleutel-lifecycle-gate, terms-pagina herschrijven. Daarna v1.01 op effective_until.
- **Fase 3 — beheer**: her-acceptatie beproeven met gesimuleerde materiële wijziging, purge-job, jaarlijkse bewijsdossier-oefening, dashboard, beheerprocedure versiebeheer (wie zet material_change, wie keurt release).

Volgorde dwingend 0 → 1 → 2; fase 3 mag parallel aan 2. Niets live zolang fase 0 niet draait.

## De vijf punten waar juridisch het meeste van afhangt

1. Het bewijslog zelf: append-only met hash-keten en externe verankering, per akkoord commit-hash én tekst-/PDF-hash van exact de getoonde taalversie, ≥ 5 jaar na accountsluiting. Zonder dit bestaat de maatregel juridisch niet.
2. De sluitende technische gate op de documentatie — geen deep links, geen ongesignde bestanden, geen zoeklek — plus organisatorisch de zijkanalen dicht. Dit draagt de "redelijke maatregel" van art. 1 Wbb.
3. Het controlescherm plus de dubbele terhandstelling (PDF vóór het akkoord + e-mail met PDF erna): neemt de vernietigbaarheid van 6:227c lid 4 en 6:233 sub b weg — juist bij de groep die wél kan vernietigen (6:235).
4. Het organisatieveld en bevoegdheidsvinkje van laag 2, verbatim vastgelegd: maakt de keten gebruiker → organisatie → klant bewijsbaar en levert de wetenschap voor art. 2 lid 3 Wbb tegen een externe bouwer.
5. Her-klik bij elke materiële wijziging en vastlegging van de aanvaarde taalversie: geen gebondenheid via "voortgezet gebruik", per gebruiker staat vast welke tekst in welke taal geldt. Gate daarnaast: de privacyverklaring moet live zijn vóór het eerste acceptatiescherm.
