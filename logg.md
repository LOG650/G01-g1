# Detaljert Prosjektlogg: LOG650 - Logistikk og KI

Denne loggen gir en kronologisk og tematisk beskrivelse av prosjektets utvikling, fra de første strukturelle grepene til dagens avanserte integrering av KI-verktøy.

---

## Fase 1: Grunnsteinene legges (21. februar – 8. mars 2026)

Prosjektet ble initiert av **Bård Pettersen** den 21. februar med etableringen av et prosjektskjelett. Dette innebar opprettelsen av en standardisert mappestruktur for å sikre orden fra start. I de påfølgende dagene ble det lagt ned arbeid i å utforme prosjektforslaget (`proposal.md`).

**Kensan-89** overtok stafettpinnen tidlig i mars og begynte arbeidet med å knytte prosjektet til en konkret case: *Ruteplanlegging av fortransport hos Lerøy*. Dette innebar en betydelig oppdatering av forslaget og de første utkastene til selve prosjektrapporten (`rapport.md`). Parallelt ble de første strategiske planene for Fase 2 lagt, inkludert en foreløpig prosjektstyringsplan. Den 8. mars ble rapportstrukturen ytterligere formalisert med dedikerte mapper for dokumentasjon.

---

## Fase 2: Operasjonalisering og Modellering (12. – 15. mars 2026)

Dette var en av prosjektets mest aktive perioder, hvor fokus skiftet fra planlegging til teknisk gjennomføring og detaljert styring.

**Teknisk utvikling (Kensan-89):**
Den 12. mars ble det gjort store fremskritt i utviklingen av VRP-modellen (`vrp_model.py`). Modellen ble utvidet med kritiske begrensninger som "return-to-depot", og det ble startet et arbeid med å optimalisere antall kjøretøy for å øke effektiviteten. For å sikre et godt arbeidsmiljø ble det også konfigurert felles innstillinger for VS Code.

**Prosjektstyring og Planlegging (martedolva-ctrl, Hanne-hh, miraa-crypto):**
Samtidig ble det lagt ned en formidabel innsats i å strukturere Fase 2. **martedolva-ctrl** ledet arbeidet med å etablere en tydelig WBS (Work Breakdown Structure) og ryddet opp i midlertidige filer som oppstod under planleggingsfasen. **Hanne-hh** sørget for at milepælsplanene var oppdaterte og i tråd med prosjektets fremdrift. **miraa-crypto** hadde ansvaret for å holde den overordnede prosjektplanen i MS Project oppdatert, noe som resulterte i detaljerte Gantt-diagrammer og tidslinjer som ble eksportert for visuell kontroll.

---

## Fase 3: Visuell Kontroll og Kvalitetssikring (12. – 19. mars 2026)

Parallelt med modelleringen ble Fase 3 (Review) igangsatt. **Kensan-89** opprettet `visual_review.md` den 12. mars, et dokument som fungerer som en logg for kvalitative observasjoner. Her ble det dokumentert diskusjoner rundt bilpark-analyse og de logistikkmessige avveiningene mellom ventetid og "Just-In-Time"-prinsipper. 

Den 19. mars markerte **Hanne-hh** overgangen mot dypere analyse ved å opprette mappen `006 analysis`, som skulle huse resultatene fra modellkjøringene.

---

## Fase 4: Strukturering av Rapport og KI-integrasjon (3. april 2026)

Etter en periode med fokus på rådata og modellering, har arbeidet i dag (3. april) vært rettet mot å profesjonalisere sluttproduktet og utnytte potensialet i generativ KI.

**Modernisering av Malverk:**
**martedolva-ctrl** og **Kensan-89** startet dagen med å klargjøre den offisielle prosjektmalen. Gjennom Gemini CLI ble den tunge PDF-malen konvertert til et dynamisk Markdown-dokument. Dette ble gjort for å muliggjøre sømløs integrasjon av teoretiske tekster, KI-assisterte analyser og versjonskontrollert tekstproduksjon.

**Kunnskapssyntese og Teori (Gemini CLI):**
En sentral del av dagens arbeid har vært å bygge bro mellom teori og praksis. Ved å analysere vitenskapelige artikler fra Solomon og Osvald & Stirn, har KI-assistenten generert et omfattende teorikapittel i rapporten. Dette kapittelet setter våre modellvalg (VRPTWTD) i en akademisk kontekst, spesielt knyttet til distribusjon av ferskvarer og tidsavhengige reisetider.

**Transkripsjon og Dokumentasjon:**
For å sikre full åpenhet rundt verktøybruken, har vi transkribert visuelle retningslinjer for KI-bruk til prosjektet. Dette sikrer at alle teammedlemmer følger de samme etiske og akademiske standardene. Dagen avsluttes med en fullstendig oppdatering av denne loggen, som nå gir et helhetlig bilde av hele prosjektets reise fra idé til en teknisk avansert forskningsoppgave.

---

---

## 2026-04-19 – Sammenligning og sjekkliste for videre arbeid

**martedolva-ctrl** sammenliknet gjeldende rapportutkast med `main_SKRIVING` for å kartlegge hva som gjenstår. Gjennomgangen resulterte i en sjekkliste for videre arbeid frem mot innlevering.

---

## 2026-04-20 – Datavisualisering, PDF→MD-konvertering og ferdigstilling av kap. 1–3 (Claude Code)

**martedolva-ctrl** benyttet Claude Code (Sonnet 4.6) som faglig sparringspartner gjennom dagen. Arbeidet er dokumentert her for sporbarhet på KI-bruk:

**Datavisualisering:**
Claude genererte et Python-script ([006 analysis/visualiser_nettverk.py](006 analysis/visualiser_nettverk.py)) som leser [004 data/data.json](004 data/data.json) og produserer et tosidig plott ([004 data/nettverk_visualisering.png](004 data/nettverk_visualisering.png)): nodekart med depot + 7 lokaliteter (størrelse skalert etter etterspørsel), og horisontalt tidsvindu-diagram. Script og output er kontrollert og godkjent manuelt.

**Sammenligning mot skriveveileder:**
Claude ekstraherte struktur og kravpunkter fra `main_SKRIVING, (9. des, 2025).md` (124-siders skriveveileder for LOG650, levert som PDF) og fra rapportutkastet `Mal prosjekt LOG650 v2.md` (som egentlig var en PDF med feil endelse). Basert på dette ble [014 fase 4 - report/sjekkliste.md](014 fase 4 - report/sjekkliste.md) generert – en strukturert gjennomgang kapittel for kapittel.

**PDF→Markdown-konvertering:**
Det ble oppdaget at den "konverterte" malen fra Gemini CLI fortsatt var en PDF (bare med .md-endelse). Claude konverterte derfor PDF-en til ekte Markdown med `pymupdf4llm`, og resultatet ble [014 fase 4 - report/rapport.md](014 fase 4 - report/rapport.md) (895 linjer). Dette ble arbeidsdokumentet for videre redigering.

**Gjenoppretting av mistet tekst:**
Casebeskrivelsen i kap. 4 hadde falt ut av PDF-eksporten. Teksten ble sikret i [014 fase 4 - report/kap4_casebeskrivelse.md](014 fase 4 - report/kap4_casebeskrivelse.md) og limt tilbake inn i rapporten.

**Rydding og ferdigstilling av kap. 1–3 (Martes ansvar):**
- All veiledningstekst fra malen ble pakket inn i HTML-kommentarer (`<!-- ... -->`) i 12 kapitler, slik at teksten er skjult ved rendring men fortsatt synlig som referanse i Markdown-kilden.
- **Kap. 1 Innledning:** 1.2 Delproblemer fjernet, 1.3/1.4 renummerert til 1.2/1.3, stavefeil rettet (løsningsmetode, heuristisk tilnærming, metaheuristikker, reell, proporsjonal, overskrides), og begrunnelsen «vi er ikke matematikere eller programmerere» erstattet med en faglig formulering om transparens og etterprøvbarhet.
- **Kap. 2 Litteratur:** Kildehenvisninger rettet til APA 7-format – Archetti et al. (2026), Adamo et al. (2024), Liu et al. (2023), Bogyrbayeva et al. (2024).
- **Kap. 3 Teori:** Dantzig & Ramser (1959) lagt til som eksplisitt sitering i 3.1.
- **KI-merknadene** fra topp av kap. 2 og kap. 3 ble flyttet til et nytt delkapittel **5.5 Bruk av KI i forskningsprosessen** i metodekapittelet, med henvisning til prosjektloggen som **Vedlegg C**.
- **Bibliografi ryddet og komplettert:** tre nakne URL-er (ikke sitert i teksten) fjernet, og manglende kilder lagt til – Toth & Vigo (2014), Laporte (2009), Solomon (1987), Cormen et al. (2009), Dantzig & Ramser (1959). Sortert alfabetisk.
- **Vedlegg B** rettet fra duplikat avstandsmatrise til tidsmatrise (minutter), **Vedlegg C** opprettet for prosjektlogg og KI-bruksdokumentasjon.

**Versjonskontroll:**
Claude bistod med `git pull`, `git push` og statussjekker underveis for å holde lokal og remote branch i synk.

---

## 2026-04-22 – Innholdsbearbeiding av rapport (Claude Code Opus 4.7)

**Kensan-89** brukte Claude Code (Opus 4.7) som skrivepartner gjennom dagen for å arbeide systematisk gjennom åpne punkter i [014 fase 4 - report/sjekkliste.md](014 fase 4 - report/sjekkliste.md). All redigering gjort i Markdown direkte i [014 fase 4 - report/rapport.md](014 fase 4 - report/rapport.md).

**Kapittel 5 – Metode og data:**
Ny seksjon 5.4 «Bruk av KI i metodeprosessen» lagt til, som dokumenterer bruk av ChatGPT, Claude og Gemini i tråd med [003 references/Nye KI-retningslinjer.md](003 references/Nye KI-retningslinjer.md). Seksjonen inkluderer henvisning til prosjektets GitHub-repositorium for reproduserbarhet. Tidligere overlapp mellom 5.2 «Data» og 5.3 «Samle geografiske data» løst ved å absorbere 5.3 inn i 5.2 (nye 5.2.5–5.2.7), gammel 5.4 omnummerert til 5.3. Faktuell feil rettet: «breddegrad/lengdegrad» endret til «x- og y-koordinater» for å matche koordinattabellen i 5.1.2.

**Veiledningstekst fjernet:**
Alle 12 `<!-- VEILEDNING FRA MAL -->`-blokker fjernet fra kap. 1–10 (omkring 135 linjer). I tillegg ble «(kan splittes i to)» fjernet fra 5.0-overskriften og «( Kenneth )» fra 4.0-overskriften.

**Kapittel 4 – Casebeskrivelse:**
Utvidet fra 4 til 5 avsnitt. Lagt til prosessflyt (henting, tidsvinduer, kvalitet og dyrevelferd), rammebetingelses-avsnitt med nøkkeltall (7 lokaliteter, 1 slakteri, kapasitet 180 enheter, samlet etterspørsel 312 enheter), og eksplisitt egnethets-kobling til VRPTW fra kap. 3.

**Kapittel 6 – Modellering:**
Formalisert til CVRPTW-formulering basert på Toth & Vigo (2014). Lagt til mengde-tabell (N, V, K), parametertabell med syv symboler (dᵢⱼ, tᵢⱼ, qᵢ, sᵢ, eᵢ, lᵢ, Q, T_max), og restriksjoner skrevet som matematiske formler (besøk, flyt, kapasitet, tidsvinduer, retur til depot, MTZ subtour-eliminering, binær). PDF-eksport-artefakter (omitted picture-blokker og ødelagt formeltranskripsjon) erstattet med ren Unicode-notasjon. Ny seksjon 6.4 «Modellvarianter og scenarier» med fem scenarier (baseline, +20 % etterspørsel, redusert kapasitet, flere kjøretøy, strammere tidsvinduer).

**Stavefeil og vedlegg:**
Seks stavefeil rettet i kap. 1: «Innlefveringsdato», «løsningsmedote», «heurisktisk», «tilbærning», «metaheurestikker», «overskrives». Vedlegg B endret fra duplikat av avstandsmatrisen til faktisk tidsmatrise (minutter) hentet fra [004 data/data.json](004 data/data.json). Typo «Fra / tl» rettet til «Fra / til» i begge vedlegg.

**Bibliografi (kap. 11) – fullstendig opprydning:**
Erstattet 7 ufullstendige oppføringer med 16 APA 7-formaterte oppføringer, alfabetisk sortert. Lagt til 6 manglende klassiske kilder som var sitert i teksten: Toth & Vigo (2014), Laporte (2009), Solomon (1987), Cormen et al. (2009), Dantzig & Ramser (1959) og Miller, Tucker & Zemlin (1960). De tre tidligere ufullstendige oppføringene ble identifisert via WebFetch/WebSearch som Tan & Yeh (2021), Pangaribuan et al. (2025) og Clarke & Wright (1964 – savings-algoritmen). Liu (2023) supplert med fullt forfatternavn (Liu, Chen, Por, Ku) og full tittel. KI-verktøy lagt inn som generiske 2026-oppføringer.

**Sjekkliste-status:**
Av prioritert rekkefølge fremover er nå punkt 1, 3, 6, 7 og 10 ferdig. Punktene 2, 4, 5 og 8 (modellkjøring og påfølgende analyse, resultat, diskusjon, abstract) avventes til neste gruppemøte hvor Python-modellen utvikles felles. Punkt 9 (forside-elementer) krever input fra hele gruppen.

---

## 2026-04-22 (forts.) – Modellimplementering og kap. 7–9 (Claude Code Sonnet 4.6)

**martedolva-ctrl** brukte Claude Code (Sonnet 4.6) som sparringspartner for modellkjøring og skriving av analyse-, resultat- og diskusjonskapitlene.

**Beslutning om løsningsmetode:**
I samråd med Claude ble det besluttet å kjøre **både** MILP-eksakt løsning og NN-heuristikk, og bruke optimalitetsgap som kvalitetsmål på heuristikken. Tekstendringer som følge:
- Kap. 1.2 Avgrensinger – avgrensning mot eksakte metoder mykere formulert (nå sier den at MILP er inkludert som referanseoptimum, mens metaheuristikker er utenfor omfang).
- Kap. 6.2.4 (ny) – «Eksakt løsning (MILP)» lagt til, dokumenterer bruk av PuLP og CBC-løseren, definerer optimalitetsgap som gap = (z_NN − z_MILP) / z_MILP.
- Kap. 6.3.2 – validering utvidet til å dekke sammenligning mellom metodene.

**Python-implementering ([006 analysis/vrp_model.py](006 analysis/vrp_model.py)):**
Ett samlet script med fem steg:
1. **Datalasting og sanity check** – validerer [004 data/data.json](004 data/data.json), verifiserer symmetri i avstandsmatrisen, konsistens i tidsvinduer og kapasitet.
2. **NN-heuristikk iterativt** (K = 1, 2, 3, 4) – viser utregning per bil og stopper ved første K hvor ytterligere biler ikke reduserer total kjørelengde.
3. **MILP-modell med PuLP + CBC** – implementerer alle restriksjoner fra kap. 6.1.3 direkte (besøksbegrensning, flyt, kapasitet via load propagering, tidsvinduer via time propagering, retur til depot, MTZ-implisitt via monotoni).
4. **Sammenligning NN vs MILP** – tabell, rutekart og stolpediagram.
5. **Scenarioanalyse** – fem scenarier fra kap. 6.4, hver kjørt separat.

**Resultater (baseline):**
- MILP: 392,09 km, 2 kjøretøy (Bil 1 last 76 %, Bil 2 last 97 %)
- NN: 534,00 km, 3 kjøretøy
- **Optimalitetsgap: 36,2 %** – NN bruker én ekstra bil og kjører 142 km lengre enn optimum.

**Resultater (scenarioanalyse):** Når kapasiteten reduseres til Q = 120 konvergerer metodene fullstendig (gap 0 %). Strammere tidsvinduer (50 %) rammer NN hardest – metoden må bruke fire biler. Flere kjøretøy (K_max = 5) endrer ingenting, fordi tid og kapasitet er de bindende begrensningene.

**Figurer generert ([004 data/](004 data/)):**
- `sammenligning_NN_vs_MILP.png` – rutekart side ved side (NN vs MILP på baseline)
- `total_distanse_sammenligning.png` – stolpediagram med optimalitetsgap
- `scenarioanalyse.png` – stolpediagram med alle fem scenarier

**Rapporten – kap. 7, 8, 9 fylt ut:**
- **Kap. 7 Analyse:** 7.1 NN iterativt, 7.2 MILP-optimum (tabell 7.1), 7.3 scenarioparametre.
- **Kap. 8 Resultat:** 8.1 NN vs MILP baseline (tabell 8.1 + figur 8.1 og 8.2), 8.2 scenarioanalyse (tabell 8.2 + figur 8.3), 8.3 nøkkeltall koblet til FS1/FS2/FS3. Holdt objektivt uten tolkning.
- **Kap. 9 Diskusjon:** seks delkapitler – 9.1 tolkning av hovedfunn, 9.2 kobling til Solomon/Adamo/Archetti/Liu/Bogyrbayeva, 9.3 styrker/svakheter ved data, metode og modell, 9.4 generaliserbarhet, 9.5 praktiske implikasjoner, 9.6 refleksjon om KI-bruk i prosjektet.

**Sjekkliste ryddet:**
[014 fase 4 - report/sjekkliste.md](014 fase 4 - report/sjekkliste.md) restrukturert til tydelig «Ferdig»/«Gjenstår»-oversikt. Gjenstående punkter: kap. 10 Konklusjon (venter på godkjenning av hovedutkastet 27. april), sammendrag og abstract, forsideelementer, finpuss.

---

## Referanse: MILP vs. Nearest Neighbor (NN)

Denne seksjonen er ren lesestoff for gruppen, ment som bakgrunn for å forstå hva de to metodene er, hvor de ligner, og hvor de skiller seg. Den er ikke en logg-hendelse, men en forklarende notat knyttet til sammenligningsplottene i mappen 004 data (sammenligning_NN_vs_MILP.png og total_distanse_sammenligning.png).

Hva MILP er:
MILP står for Mixed Integer Linear Programming, på norsk blandet heltalls-lineær programmering. Det er en matematisk optimeringsmetode der man minimerer eller maksimerer en lineær målfunksjon, for eksempel total kjørelengde eller total kostnad, underlagt et sett med lineære begrensninger, for eksempel kapasitet, tidsvinduer og at hver kunde skal besøkes én gang. Det som gjør metoden "mixed integer" er at enkelte beslutningsvariabler må være heltall. I VRP-sammenheng er dette typisk binære variabler som tar verdien 1 hvis et kjøretøy kjører fra node A til node B, og 0 ellers. Andre variabler, som ankomsttider eller akkumulert last, kan være kontinuerlige. En MILP-løser, for eksempel CBC, Gurobi eller CPLEX, søker systematisk gjennom løsningsrommet og finner den beviselig beste løsningen gitt modellens forutsetninger.

Hva Nearest Neighbor er:
Nearest Neighbor, ofte forkortet NN, er en grådig heuristikk. Algoritmen starter i depotet og velger i hvert steg den nærmeste ubesøkte kunden som fortsatt kan betjenes uten å bryte kapasitet eller tidsvinduer. Når kjøretøyet er fullt eller ingen flere kunder kan betjenes, returnerer det til depotet, og et nytt kjøretøy starter. Algoritmen tar altså lokale valg uten å vurdere hvilke konsekvenser valget får lenger frem i ruten.

Hvor de ligner:
Begge metodene løser det samme underliggende problemet, nemlig å planlegge ruter for en flåte kjøretøy som skal betjene et sett kunder fra et depot. Begge respekterer de samme typene begrensninger, som kjøretøyskapasitet, tidsvinduer og at hver kunde besøkes én gang. Begge produserer konkrete ruter som kan sammenlignes direkte på total distanse, antall kjøretøy og betjent etterspørsel.

Hvor de skiller seg:
Den viktigste forskjellen ligger i optimalitet mot hastighet. MILP gir en matematisk optimal løsning, altså den beste mulige gitt modellen, men metoden er NP-hard og skalerer dårlig. For små instanser som vårt tilfelle med syv kunder løses problemet på sekunder eller minutter, men for hundrevis eller tusenvis av kunder blir beregningstiden upraktisk lang. NN er derimot svært rask og kjører på millisekunder selv for store problemer, men løsningen er vanligvis 10 til 30 prosent dårligere enn optimal, og kan i uheldige tilfeller være mye verre. En annen forskjell er fleksibilitet: MILP krever at alle regler kan uttrykkes som lineære begrensninger, mens NN lett kan utvides med ad hoc-regler, men mister da all garanti om kvalitet.

Hvorfor sammenligningen er nyttig for prosjektet:
Ved å kjøre begge metodene på samme datasett får vi to referanser. MILP gir det teoretiske taket, altså hva som er mulig å oppnå. NN gir et realistisk bilde av hva en enkel, raskt implementert løsning ville produsert i praksis. Gapet mellom dem, ofte kalt optimality gap, er et mål på hvor mye det er å tjene på å investere i en sofistikert optimeringsmodell kontra en tommelfingerregel. For Lerøy-casen gir dette et konkret beslutningsgrunnlag: dersom gapet er lite, er en enkel heuristikk god nok. Dersom gapet er stort, rettferdiggjør det kompleksiteten i MILP-tilnærmingen.

---

*Loggen er generert og vedlikeholdt med støtte fra Gemini CLI og Claude Code, basert på faktiske hendelser og git-historikk.*
