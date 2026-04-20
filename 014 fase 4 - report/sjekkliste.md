# Sjekkliste for videre arbeid – LOG650 G01

Oppdatert 2026-04-20 etter gjennomgang av gruppens utkast (34 sider) sammenholdt med skriveveilederen **main_SKRIVING (9. des. 2025)**.

**Kildefiler:**
- [rapport.md](rapport.md) – **ekte Markdown-versjon** konvertert fra PDF 2026-04-20 (895 linjer). Bruk denne til videre redigering.
- [Mal prosjekt LOG650 v2.md](Mal prosjekt LOG650 v2.md) – originalen (PDF med feil .md-endelse).
- [kap4_casebeskrivelse.md](kap4_casebeskrivelse.md) – casebeskrivelsen som falt ut av PDF-eksport.

Legende: `[ ]` gjenstår · `[~]` påbegynt · `[x]` ferdig

## Hovedfunn fra sammenligningen

- **Kap. 1–3 og 5–6 har substansielt innhold** (innledning, litteratur, teori, metode, modellering).
- **Kap. 4 Casebeskrivelse** – tekst finnes i [kap4_casebeskrivelse.md](kap4_casebeskrivelse.md), men er ikke lagt inn i rapporten.
- **Kap. 7 Analyse, 8 Resultat, 9 Diskusjon, 10 Konklusjon er tomme** – kun veiledningstekst fra malen.
- **Sammendrag og Abstract mangler helt**.
- **Malens veiledningstekst ligger fortsatt inne** i flere kapitler (1.0, 1.3, 1.4, 2.0, 3.0 siste avsnitt, 4.0, 7.0, 8.0, 9.0, 10.0) – må fjernes før innlevering.
- **Vedlegg A og B er begge "Avstandsmatrise"** – B skal være tidsmatrise.
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

## 1. Innledning *(Alle)*

- [x] Motivasjon og faglig relevans skrevet
- [x] Problemstilling formulert som "hvordan"-spørsmål
- [x] 3 forskningsspørsmål definert
- [x] Avgrensinger begrunnet faglig (1.3)
- [x] Antagelser listet og begrunnet (1.4)
- [ ] **Fjern veiledningsteksten** fra malen (s. 10–13): "Introduksjonen bør ikke være for lang...", "Svar på følgende spørsmål...", spørsmålslistene, eksemplene om Maritech/lakseprisen
- [ ] 1.2 Delproblemer – enten skriv noe, eller slett overskriften (markert "valgfri")
- [ ] Vurder: skal delproblemer stå, eller dekkes det av forskningsspørsmålene i 1.1?

---

## 2. Litteratur *(Alle)*

- [x] Substansielt kapittel – 5-års utviklingstrekk beskrevet
- [x] Relevant forskning presentert (Archetti, Adamo, Liu, Bogyrbayeva)
- [x] Koblet til oppgavens problemstilling og metodevalg
- [ ] **Sjekk kildehenvisninger** – står "Archetti et al." uten årstall/sidetall flere steder i teksten
- [ ] **Fjern veiledningsteksten** ("Diskuter de viktigste bidragene de 5 siste årene...", kulepunktene om synsing)
- [ ] Vurder om kap. 2 og 3 kan slås sammen – skriveveilederen anbefaler ett samlet teori-/litteraturkapittel

---

## 3. Teori *(Alle)*

- [x] 3.1 VRP – definert og referert (Toth & Vigo 2014, Laporte 2009, Archetti 2026)
- [x] 3.2 VRPTW – Solomon 1987, Adamo 2024
- [x] 3.3 Eksakte metoder vs heuristikker
- [x] 3.4 Greedy/nearest neighbor (Cormen 2009)
- [x] 3.5 KI i ruteplanlegging
- [x] 3.6 Oppsummering og kobling til problemstilling
- [ ] **Fjern veiledningsteksten** på slutten ("Når du skal skrive en bacheloroppgave...")
- [ ] Sjekk at Cormen et al. 2009 faktisk er brukt i bibliografien (mangler nå)
- [ ] Vurder å integrere med kap. 2 (skriveveileder anbefaler det)

---

## 4. Casebeskrivelse *(Case/modell)* ✅ TEKST PÅ PLASS (sikret 2026-04-20)

Teksten falt ut av PDF-eksporten – sikret i [kap4_casebeskrivelse.md](kap4_casebeskrivelse.md). Må legges tilbake i kildedokumentet (Word) før ny eksport.

- [x] Beskriv Lerøy Seafood Group og fortransport av slakteklar fisk
- [x] Prosessflyt: fra oppdrettslokalitet til slakteri
- [x] Kontekst: havbruksnæringen i Norge
- [x] Rammebetingelser: geografisk spredning, kapasitet, tidskrav
- [x] Hvorfor er caset egnet for kvantitativ ruteplanlegging
- [ ] **Legg teksten tilbake i Word-dokumentet** som eksporteres til PDF
- [ ] **Fjern veiledningsteksten** fra malen ("Har skal problemstillingen utbroderes...", eksempelet om gjennomløpstid)
- [ ] Vurder utvidelse: nøkkeltall (syntetiske) – 7 lokaliteter, 1 slakteri, kapasitet 180 t

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
- [x] 5.4 Transportdata (volum + kostnadsparametere)
- [ ] **Beskriv KI-bruk i metodeprosessen** (kreves eksplisitt av skriveveilederen)
- [ ] Vurder om 5.2 og 5.3 overlapper – 5.2.2 "Velge region" og 5.3 "Samle geografiske data" sier delvis det samme
- [ ] Reproduserbarhet: henvis til kode på GitHub

---

## 6. Modellering *(Modell)* – kjernekapittel ✅ GODT UTKAST

- [x] 6.1.1 Beslutningsvariabler definert (xᵢⱼ binær)
- [x] 6.1.2 Målfunksjon (min Σ dᵢⱼ·xᵢⱼ)
- [x] 6.1.3 Begrensninger: kapasitet, tidsvinduer, besøk, flyt, retur til depot
- [x] 6.2 Python-implementering dokumentert
- [x] 6.3 Testing og validering
- [ ] **Legg til eksplisitt mengdedefinisjon** (N, K, V₀) og parametertabell (dᵢⱼ, tᵢⱼ, qᵢ, sᵢ, eᵢ, lᵢ, Q)
- [ ] **Skriv restriksjoner som formler**, ikke bare tekstlig
- [ ] Subtour-eliminering – nevnes den? (anbefalt for formell VRP-formulering)
- [ ] Modellvarianter/scenarier eksplisitt nevnt
- [ ] Flytt kodedetaljer til vedlegg hvis det blir for teknisk

---

## 7. Analyse *(Fleste)* ⚠️ TOMT

- [ ] Kjør modellen og hent resultater
- [ ] Presenter valgte ruter (med figur)
- [ ] Sammenlign med referanseløsning (baseline – f.eks. én rute per lokalitet)
- [ ] Scenarioanalyse (endre etterspørsel, kapasitet eller antall biler)
- [ ] Sensitivitetsanalyse
- [ ] **Fjern veiledningsteksten** ("Hvordan skrive bacheloroppgave...")
- [ ] Merk: ifølge skriveveileder skal 7 og 8 være objektive – ingen tolkning her

---

## 8. Resultat ⚠️ TOMT

- [ ] Presenter hovedfunn i tabeller og figurer
- [ ] Total avstand, tid per rute, antall biler, kapasitetsutnyttelse
- [ ] Kart/rutediagram som viser valgt løsning
- [ ] Forklarende tekst for **hver** figur og tabell
- [ ] Koble hvert resultat eksplisitt til forskningsspørsmålene (FS1, FS2, FS3)
- [ ] **Fjern veiledningsteksten**
- [ ] Vurder: bør 7 og 8 slås sammen til "Analyse og resultater" (jf. skriveveileder kap. 4.6)?

---

## 9. Diskusjon *(Alle)* ⚠️ TOMT

- [ ] Tolk hovedfunn i lys av problemstillingen og de 3 forskningsspørsmålene
- [ ] Sammenlign med Solomon, Adamo, Liu et al.
- [ ] Styrker og svakheter ved syntetisk data, euklidsk avstand, nearest-neighbor
- [ ] Generaliserbarhet – kan modellen overføres til reelle Lerøy-data?
- [ ] Praktiske implikasjoner for havbruksnæringen
- [ ] **Kritisk refleksjon om KI-bruk** – muligheter og begrensninger (faglig gevinst-diskusjon)
- [ ] **Fjern veiledningsteksten**

---

## 10. Konklusjon *(Alle)* ⚠️ TOMT

- [ ] Eksplisitt svar på problemstillingen (gjenta den)
- [ ] Svar på FS1, FS2, FS3
- [ ] Kort oppsummering av hovedfunn
- [ ] Praktiske/teoretiske implikasjoner
- [ ] Forslag til videre arbeid
- [ ] Refleksjon om KI-prosjektets bidrag
- [ ] **Fjern veiledningsteksten** ("Hva er det viktigste dere har funnet?...")

---

## 11. Bibliografi ⚠️ UFULLSTENDIG

- [ ] Konverter alle kilder til **APA 7**, ikke nakne URL-er
- [ ] Første 3 referanser mangler forfatter og år
- [ ] Legg inn **Toth & Vigo (2014)** – brukt i 3.1
- [ ] Legg inn **Laporte (2009)** – brukt i 3.1
- [ ] Legg inn **Solomon (1987)** – brukt i 3.2
- [ ] Legg inn **Cormen et al. (2009)** – brukt i 3.4
- [ ] Legg inn **Dantzig & Ramser (1959)** – brukt i 3.1
- [ ] **Referer KI-verktøy** (ChatGPT/Claude/Gemini) – versjon, dato, prompt-beskrivelse i metodekap.
- [ ] Sjekk DOI og URL for alle APA-oppføringer
- [ ] Alfabetisk rekkefølge

---

## 12. Vedlegg

- [x] 12.1 Vedlegg A – Avstandsmatrise (km)
- [ ] **12.2 Vedlegg B – rett overskrift** – skal være **Tidsmatrise (minutter)**, ikke duplikat av avstandsmatrisen
- [ ] Legg til tidsmatrise-dataene (fra [data.json](../004 data/data.json))
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
- [ ] **Kjør hele rapporten gjennom stavekontroll** – sett noen feil: "Innlefveringsdato" (s. 1), "oppgaven gjennomfres", "heurisktisk" (s. 12), "tilbærning" (s. 12), "overskrives" (s. 13 – skal være overskrides)

---

## Prioritert rekkefølge fremover

1. **Fjern all veiledningstekst** fra malen i kap. 1–10 (rask fix, stor effekt)
2. **Kjør modellen** → resultater for kap. 7–8
3. Skriv **Casebeskrivelse (kap. 4)** – relativt kort, men nødvendig
4. Skriv **Analyse + Resultat (kap. 7–8)**
5. Skriv **Diskusjon (kap. 9)** og **Konklusjon (kap. 10)**
6. Ryd opp i **Modellering (kap. 6)** – mer formell notasjon
7. Komplett **Bibliografi** i APA 7
8. **Sammendrag + Abstract** helt til slutt
9. Fyll inn forside, erklæringer, publiseringsavtale
10. Rett **Vedlegg B** (tidsmatrise)
11. Finpuss: korrektur, stavefeil, figurnummerering
