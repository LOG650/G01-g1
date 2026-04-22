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

## 2026-04-20 – Datavisualisering og strukturert sjekkliste (Claude Code)

**martedolva-ctrl** benyttet Claude Code (Sonnet 4.6) som faglig sparringspartner gjennom dagen. Arbeidet er dokumentert her for sporbarhet på KI-bruk:

**Datavisualisering:**
Claude genererte et Python-script ([006 analysis/visualiser_nettverk.py](006 analysis/visualiser_nettverk.py)) som leser [004 data/data.json](004 data/data.json) og produserer et tosidig plott ([004 data/nettverk_visualisering.png](004 data/nettverk_visualisering.png)): nodekart med depot + 7 lokaliteter (størrelse skalert etter etterspørsel), og horisontalt tidsvindu-diagram. Script og output er kontrollert og godkjent manuelt.

**Sammenligning mot skriveveileder:**
Claude ekstraherte struktur og kravpunkter fra `main_SKRIVING, (9. des, 2025).md` (124-siders skriveveileder for LOG650, levert som PDF) og fra rapportutkastet `Mal prosjekt LOG650 v2.md` (34-siders PDF). Basert på dette ble [014 fase 4 - report/sjekkliste.md](014 fase 4 - report/sjekkliste.md) generert – en strukturert gjennomgang kapittel for kapittel med markering av hva som er ferdig, påbegynt eller gjenstår. KI-en identifiserte blant annet at veiledningstekst fra malen fortsatt ligger inne i flere kapitler, at sammendrag/abstract mangler, og at Vedlegg B har feil overskrift.

**Versjonskontroll:**
Claude bistod også med `git pull`, `git push` og statussjekker underveis for å holde lokal og remote branch i synk.

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

*Loggen er generert og vedlikeholdt med støtte fra Gemini CLI og Claude Code, basert på faktiske hendelser og git-historikk.*
