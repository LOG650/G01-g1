# Sjekkliste for videre arbeid – LOG650 G01

Oppdatert 2026-04-20 etter gjennomgang av gruppens utkast (34 sider) sammenholdt med skriveveilederen **main_SKRIVING (9. des. 2025)**.

**Kildefiler:**
- [rapport.md](rapport.md) – **ekte Markdown-versjon** konvertert fra PDF 2026-04-20 (895 linjer). Bruk denne til videre redigering.
- [Mal prosjekt LOG650 v2.md](Mal prosjekt LOG650 v2.md) – originalen (PDF med feil .md-endelse).
- ~~kap4_casebeskrivelse.md~~ – innholdet ble integrert i [rapport.md](rapport.md) og filen slettet i commit `5026980`.

Legende: `[ ]` gjenstår · `[~]` påbegynt · `[x]` ferdig

## Hovedfunn fra sammenligningen

- **Kap. 1, 2 og 3 er ferdigstilt** (2026-04-20).
- **Bibliografi er ryddet og komplettert** med alle siterte kilder (2026-04-20).
- **Løsningsmetode utvidet til MILP + NN-heuristikk** (2026-04-22): kap. 1.2 mykere avgrensning, nytt kap. 6.2.4 om MILP (PuLP/CBC), kap. 6.3.2 utvidet til å dekke optimalitetsgap.
- **Kap. 7 Analyse og 8 Resultat er fylt ut** (2026-04-22): baseline-sammenligning NN vs MILP (gap 36,2 %), scenarioanalyse for alle 5 scenarier, 3 figurer generert.
- **Kap. 5 og 6 har substansielt innhold** (metode, modellering) – må ryddes.
- **Kap. 4 Casebeskrivelse** – tekst finnes i [kap4_casebeskrivelse.md](kap4_casebeskrivelse.md), men er ikke lagt inn i rapporten.
- **Kap. 7 Analyse, 8 Resultat, 9 Diskusjon, 10 Konklusjon er tomme** – kun veiledningstekst fra malen.
- **Sammendrag og Abstract mangler helt**.
- **Malens veiledningstekst ligger fortsatt inne** i flere kapitler (1.0, 1.3, 1.4, 2.0, 3.0 siste avsnitt, 4.0, 7.0, 8.0, 9.0, 10.0) – må fjernes før innlevering.
- **Vedlegg B korrigert til tidsmatrise** (2026-04-20). **Vedlegg C – Prosjektlogg/KI-bruk** lagt til.
- **Bibliografi er delvis** og ikke konsekvent APA 7 (nakne URL-er, manglende info).
- **Forside-elementer** (egenerklæring, publiseringsavtale) ble eksportert som bilder i PDF og ligger nå som transkriberte tekstblokker i [rapport.md](rapport.md) – kan ryddes bort.

---

## 0. Pre-elementer (før hoveddel)

- [ ] **Forside** – fyll inn tittel (norsk + engelsk), forfattere, antall sider, dato
- [ ] **Egenerklæring** – huk av alle 6 punkter, signer
- [ ] **Personvern/NSD** – krysse av (trolig "nei", prosjektet er ikke-personopplysninger)
- [ ] **Publiseringsavtale** – veileder, studiepoeng, fullmakt
- [ ] **Sammendrag** (s. 6) – helt tomt, må skrives (norsk, 200–300 ord)
- [ ] **Abstract** (s. 7) – helt tomt, må skrives (engelsk, speiler sammendraget)
- [ ] **Antall ord / forfattererklæring** (s. 5) – fjern malteksten eller fyll inn
- [x] Innholdsfortegnelse – genereres automatisk

---

## 1. Innledning *(Alle)* ✅ FERDIG (2026-04-20)

- [x] Motivasjon og faglig relevans skrevet
- [x] Problemstilling formulert som "hvordan"-spørsmål
- [x] 3 forskningsspørsmål definert
- [x] Avgrensinger begrunnet faglig (1.3)
- [x] Antagelser listet og begrunnet (1.4)
- [x] **Fjern veiledningsteksten** fra malen (fjernet 2026-04-22: 4 blokker i kap. 1 – introduksjon, problemstilling, avgrensninger, antagelser)
- [x] Begrunnelse "ikke matematikere/programmerere" erstattet med faglig formulering om transparens og etterprøvbarhet (merge 2026-04-22)
- [x] Stavefeil rettet (løsningsmetode, heuristisk tilnærming, metaheuristikker, reell, proporsjonal, overskrides)
- [ ] 1.2 Delproblemer – enten skriv noe, eller slett overskriften (markert "valgfri")
- [ ] Vurder: skal delproblemer stå, eller dekkes det av forskningsspørsmålene i 1.1?

---

## 2. Litteratur *(Alle)* ✅ FERDIG (2026-04-20)

- [x] Substansielt kapittel – 5-års utviklingstrekk beskrevet
- [x] Relevant forskning presentert (Archetti, Adamo, Liu, Bogyrbayeva)
- [x] Koblet til oppgavens problemstilling og metodevalg
- [x] Kildehenvisninger rettet til APA-format (Archetti et al. (2026), Adamo et al. (2024), Liu et al. (2023), Bogyrbayeva et al. (2024))
- [x] **Fjern veiledningsteksten** (fjernet 2026-04-22)
- [x] KI-merknad flyttet til kap. 5.4 Bruk av KI i metodeprosessen
- [ ] ~~Vurder om kap. 2 og 3 kan slås sammen~~ – utsatt til etter tilbakemelding fra faglærerne

---

## 3. Teori *(Alle)* ✅ FERDIG (2026-04-20)

- [x] 3.1 VRP – definert og referert (Dantzig & Ramser 1959, Toth & Vigo 2014, Laporte 2009, Archetti 2026)
- [x] 3.2 VRPTW – Solomon 1987, Adamo 2024
- [x] 3.3 Eksakte metoder vs heuristikker
- [x] 3.4 Greedy/nearest neighbor (Cormen 2009, Liu 2023)
- [x] 3.5 KI i ruteplanlegging (Bogyrbayeva 2024)
- [x] 3.6 Oppsummering og kobling til problemstilling
- [x] **Fjern veiledningsteksten** på slutten (fjernet 2026-04-22)
- [x] KI-merknad flyttet til kap. 5.4
- [x] Dantzig & Ramser (1959) lagt til som eksplisitt sitering i 3.1
- [x] Cormen et al. 2009 inkludert i bibliografi (merge 2026-04-22)
- [x] ~~Vurder å integrere med kap. 2~~ – utsatt til etter tilbakemelding fra faglærerne

---

## 4. Casebeskrivelse *(Case/modell)* ✅ UTVIDET 2026-04-22

Teksten er integrert i [rapport.md](rapport.md) og utvidet med prosessflyt, rammebetingelser med nøkkeltall og eksplisitt kobling til VRPTW.

- [x] Beskriv Lerøy Seafood Group og fortransport av slakteklar fisk
- [x] Prosessflyt: fra oppdrettslokalitet til slakteri (utvidet – henting, tidsvinduer, kvalitet/dyrevelferd)
- [x] Kontekst: havbruksnæringen i Norge
- [x] Rammebetingelser: geografisk spredning, kapasitet, tidskrav
- [x] Hvorfor er caset egnet for kvantitativ ruteplanlegging (kobling til VRPTW fra kap. 3)
- [x] ~~Legg teksten tilbake i Word-dokumentet~~ – foreldet, rapport.md er nå kilden
- [x] **Fjern veiledningsteksten** fra malen (fjernet 2026-04-22)
- [x] Utvidelse med nøkkeltall: 7 lokaliteter, 1 slakteri, kapasitet 180 t, etterspørsel 312 t (lagt til 2026-04-22)

---

## 5. Metode og data *(Alle)* 

- [x] 5.1.1 Datagrunnlag beskrevet (syntetisk datasett fra faglærer)
- [x] 5.1.2 Lokasjoner og koordinater – tabell inkludert
- [x] 5.1.3 Avstandsmetode (euklidsk) begrunnet
- [x] 5.1.4 Avstandsmatrise referert til vedlegg
- [x] 5.1.5 Tidsmatrise referert til vedlegg
- [x] 5.1.6 Validering av avstander
- [x] 5.1.7 Øvrige inputdata (kapasitet 180, samlet etterspørsel 312)
- [x] 5.2 Data – identifisering av lokasjoner/region/slakteri
- [x] 5.3 Geografiske data
- [x] 5.4 Transportdata (volum + kostnadsparametere) *(nå 5.3 etter restrukturering 2026-04-22)*
- [x] **Beskriv KI-bruk i metodeprosessen** – lagt til som nytt kap. 5.4
- [x] 5.2 og 5.3 overlapp løst – 5.3 slått inn i 5.2 (5.2.5–5.2.7), tidligere 5.4 er nå 5.3
- [x] Reproduserbarhet: henvist til GitHub-repositorium (github.com/LOG650/G01-g1) i kap. 5.4

---

## 6. Modellering *(Modell)* – kjernekapittel ✅ FORMALISERT 2026-04-22

- [x] 6.1.1 Beslutningsvariabler definert (xᵢⱼ binær + hjelpevariabler aᵢ, uᵢ)
- [x] 6.1.2 Målfunksjon (min Σ dᵢⱼ·xᵢⱼ)
- [x] 6.1.3 Begrensninger: besøk, flyt, kapasitet, tidsvinduer, retur til depot, MTZ, binær
- [x] 6.2 Python-implementering dokumentert
- [x] 6.3 Testing og validering
- [x] **Mengdedefinisjon** (N, V, K) og **parametertabell** (dᵢⱼ, tᵢⱼ, qᵢ, sᵢ, eᵢ, lᵢ, Q, T_max) lagt til i 6.1
- [x] **Restriksjoner som formler** – alle 7 begrensninger skrevet matematisk i 6.1.3
- [x] Subtour-eliminering – lagt til som MTZ (Miller, Tucker og Zemlin, 1960) i 6.1.3
- [x] Modellvarianter/scenarier eksplisitt nevnt – nytt kap. 6.4 med 5 scenarier
- [ ] Flytt kodedetaljer til vedlegg hvis det blir for teknisk *(vurdert OK som-er)*
- [x] **Miller, Tucker & Zemlin (1960)** lagt til i bibliografi 2026-04-22

---

## 7. Analyse *(Fleste)* ✅ FERDIG (2026-04-22)

- [x] Kjør modellen og hent resultater (vrp_model.py, 5 scenarier + baseline)
- [x] 7.1 NN-heuristikk iterativt (K=1 → 4)
- [x] 7.2 MILP-optimum baseline
- [x] 7.3 Scenarioanalyse – parametertabell
- [x] Veiledningstekst fjernet

---

## 8. Resultat ✅ FERDIG (2026-04-22)

- [x] 8.1 Sammenligning NN vs MILP (tabell + 2 figurer)
- [x] 8.2 Scenarioanalyse (tabell + figur)
- [x] 8.3 Nøkkeltall knyttet til FS1, FS2, FS3
- [x] Figurer lagret: sammenligning_NN_vs_MILP.png, total_distanse_sammenligning.png, scenarioanalyse.png
- [x] Kart/rutediagram inkludert
- [ ] Forklarende tekst for **hver** figur og tabell
- [ ] Koble hvert resultat eksplisitt til forskningsspørsmålene (FS1, FS2, FS3)
- [x] **Fjern veiledningsteksten** (fjernet 2026-04-22)
- [ ] Vurder: bør 7 og 8 slås sammen til "Analyse og resultater" (jf. skriveveileder kap. 4.6)?

---

## 9. Diskusjon *(Alle)* ⚠️ TOMT

- [ ] Tolk hovedfunn i lys av problemstillingen og de 3 forskningsspørsmålene
- [ ] Sammenlign med Solomon, Adamo, Liu et al.
- [ ] Styrker og svakheter ved syntetisk data, euklidsk avstand, nearest-neighbor
- [ ] Generaliserbarhet – kan modellen overføres til reelle Lerøy-data?
- [ ] Praktiske implikasjoner for havbruksnæringen
- [ ] **Kritisk refleksjon om KI-bruk** – muligheter og begrensninger (faglig gevinst-diskusjon)
- [x] **Fjern veiledningsteksten** (fjernet 2026-04-22)

---

## 10. Konklusjon *(Alle)* ⚠️ TOMT

- [ ] Eksplisitt svar på problemstillingen (gjenta den)
- [ ] Svar på FS1, FS2, FS3
- [ ] Kort oppsummering av hovedfunn
- [ ] Praktiske/teoretiske implikasjoner
- [ ] Forslag til videre arbeid
- [ ] Refleksjon om KI-prosjektets bidrag
- [x] **Fjern veiledningsteksten** (fjernet 2026-04-22)

---

## 11. Bibliografi ✅ KOMPLETTERT 2026-04-22

- [x] Konverter alle kilder til **APA 7** – 16 oppføringer i konsistent format
- [x] Første 3 referanser fikset: Tan & Yeh (2021), Pangaribuan et al. (2025), Clarke & Wright (1964)
- [x] Legg inn **Toth & Vigo (2014)**
- [x] Legg inn **Laporte (2009)**
- [x] Legg inn **Solomon (1987)**
- [x] Legg inn **Cormen et al. (2009)**
- [x] Legg inn **Dantzig & Ramser (1959)**
- [x] Legg inn **Miller, Tucker & Zemlin (1960)** (brukt i 6.1)
- [x] **Referer KI-verktøy** (ChatGPT, Claude, Gemini) – generiske 2026-oppføringer
- [x] Liu (2023) fikset – fullt forfatternavn (Liu, Chen, Por, Ku) og full tittel
- [x] DOI lagt til der tilgjengelig
- [x] Alfabetisk rekkefølge
- [x] Tre nakne URL-er fjernet (ikke sitert i teksten)
- [ ] Sjekk DOI-lenker fungerer før innlevering
- [ ] *Til vurdering: konkret versjon/dato for KI-verktøy hvis dere vil ha mer presisjon*
- [ ] *Til vurdering: i kap. 5.4 – beskriv prompt-typer/eksempler hvis veileder krever det*

---

## 12. Vedlegg

- [x] 12.1 Vedlegg A – Avstandsmatrise (km) (fikset «Fra / tl» → «Fra / til»)
- [x] **12.2 Vedlegg B – Tidsmatrise (minutter)** – overskrift rettet 2026-04-22
- [x] Tidsmatrise-data lagt inn fra [data.json](../004 data/data.json)
- [x] 12.3 Vedlegg C – Prosjektlogg og dokumentasjon av KI-bruk – lagt til (merge 2026-04-22)
- [ ] Vurder flere vedlegg: Python-kode, full noderegistrering, scenarioresultater

---

## Tverrgående kvalitet (A-nivå)

- [ ] Problemstillingen besvares eksplisitt i konklusjonen
- [ ] Tydelig kobling teori → metode → data → analyse → konklusjon
- [ ] Alle antakelser er etterprøvbare
- [ ] Drøfting viser kritisk refleksjon (kommer i kap. 9)
- [ ] Figurer har figurtekst og kilde **under**; tabeller har tittel **over**
- [ ] Akser merket med enheter (km, min, tonn)
- [ ] Konsekvent språk og referansestil
- [ ] Ingen "veldig", "mye", "kanskje" – unngå upresise ord
- [~] **Kjør hele rapporten gjennom stavekontroll** – fikset 2026-04-22: Innlefveringsdato, heurisktisk, tilbærning, overskrives, pluss løsningsmedote og metaheurestikker. («gjennomfres» fantes ikke i rapporten.) Bør fortsatt kjøres en full pass før innlevering.

---

## Prioritert rekkefølge fremover

1. ~~**Fjern all veiledningstekst** fra malen i kap. 1–10~~ ✅ ferdig 2026-04-22
2. **Kjør modellen** → resultater for kap. 7–8
3. ~~Skriv **Casebeskrivelse (kap. 4)** – relativt kort, men nødvendig~~ ✅ ferdig 2026-04-22 (utvidet med prosessflyt og nøkkeltall)
4. Skriv **Analyse + Resultat (kap. 7–8)**
5. Skriv **Diskusjon (kap. 9)** og **Konklusjon (kap. 10)**
6. ~~Ryd opp i **Modellering (kap. 6)** – mer formell notasjon~~ ✅ ferdig 2026-04-22 (mengder, parametertabell, formler, MTZ, scenarier)
7. ~~Komplett **Bibliografi** i APA 7~~ ✅ ferdig 2026-04-22 (16 APA 7-oppføringer, alfabetisert)
8. **Sammendrag + Abstract** helt til slutt
9. Fyll inn forside, erklæringer, publiseringsavtale
10. ~~Rett **Vedlegg B** (tidsmatrise)~~ ✅ ferdig 2026-04-22
11. Finpuss: korrektur, stavefeil, figurnummerering
