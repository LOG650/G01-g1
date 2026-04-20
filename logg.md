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

*Loggen er generert og vedlikeholdt med støtte fra Gemini CLI og Claude Code, basert på faktiske hendelser og git-historikk.*
