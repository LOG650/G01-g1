# Sjekkliste for videre arbeid – LOG650 G01

Sammenstilt 2026-04-20 fra **Mal prosjekt LOG650 v2** og skriveveilederen **main_SKRIVING (9. des. 2025)**.
Tilpasset oppgavetypen **Modellering** (VRPTWTD – Vehicle Routing Problem with Time Windows and Time Dependency).

Legende: `[ ]` gjenstår · `[~]` påbegynt · `[x]` ferdig

---

## 0. Pre-elementer (før hoveddel)

- [ ] **Forside/tittelside** – bruk malens forside uendret (tittel, forfattere, institusjon, studieprogram, dato)
- [ ] **Sammendrag** (norsk) – kort og presis sammenfatning av problem, metode, hovedfunn
- [ ] **Abstract** (engelsk) – speiler sammendraget
- [ ] **Forord/takk** (valgfritt) – ikke faglig innhold, ikke unnskyld svakheter
- [ ] **Innholdsfortegnelse** – generert automatisk fra overskriftsnivåer
- [ ] **Figurliste og tabelliste** (hvis nødvendig)

---

## 1. Introduksjon *(Alle)*

- [ ] Kort motivasjon for tema og faglig relevans
- [ ] **Presis problemstilling** formulert som spørsmål
- [ ] Forskningsmål og ev. forskningsspørsmål
- [ ] Tydelige, faglig begrunnede avgrensninger (én region, ett slakteri, syntetiske data)
- [ ] Kort om rapportens oppbygging (hvis det hjelper leseren)

**Unngå:** teorigjennomgang, casedetaljer, metode, resultater, konklusjoner, historikk om Lerøy, lengde over 2–3 sider, flere varianter av problemstillingen.

---

## 2. Teori og litteratur *(Alle)*

- [ ] Definisjon av sentrale begreper (VRP, VRPTW, VRPTWTD, ferskvare-perishability)
- [ ] Presentasjon av relevant forskning (Dantzig & Ramser 1959, Solomon 1987, Osvald & Stirn 2008)
- [ ] Syntese: hvordan kobler teorien til problemstillingen?
- [ ] Kildekritikk – styrker/svakheter ved tidligere studier
- [ ] Faglig begrunnelse for valg av VRPTWTD som rammeverk

**Unngå:** datainnsamlingsdetaljer, bedriftsbeskrivelse, matematisk modellformulering, egne resultater, lange litteraturreferater uten kobling til problemstillingen.

---

## 3. Casebeskrivelse *(Case/modell)*

- [ ] Kort beskrivelse av Lerøy Seafood Group og fortransport av slakteklar fisk
- [ ] Prosessflyt: fra oppdrettslokalitet til slakteri
- [ ] Nøkkeltall (syntetiske): 7 lokaliteter, 1 slakteri, kapasitet 180 tonn, etterspørsel 15–85 tonn
- [ ] Rammebetingelser: tidsvinduer, servicetid, arbeidstid (0–480 min)
- [ ] Aktuell utfordring koblet til problemstillingen
- [ ] Relevans: hvorfor egner caset seg for VRPTWTD?

**Unngå:** teoretisk rammeverk, modellformler, resultater.

---

## 4. Data og metode *(Alle)*

- [ ] Beskrivelse av datagrunnlaget – syntetisk, type, struktur, omfang
- [ ] Forskningsdesign (simulering/modellering, scenarioanalyse)
- [ ] Generering av posisjonsdata, avstander (euklidisk), tidsmatrise
- [ ] Datakvalitet – hvordan er syntetiske data utformet som realistiske?
- [ ] Analysemetoder: VRP-løser (f.eks. OR-Tools), sammenligning mot referanseløsning
- [ ] Faglig begrunnelse for design, data og metode
- [ ] **Reproduserbarhet**: verktøy (Python, VSCode, GitHub), kode tilgjengelig, prosedyre dokumentert
- [ ] Beskrivelse av KI-bruk i prosessen (jf. APA 7 for KI-verktøy)

**Unngå:** resultater, tolkning, modellformler, teoridiskusjon.

---

## 5. Modellering *(Modell – kjernekapittel for dere)*

- [ ] **Formål** med modellen (minimere transporttid/avstand)
- [ ] **Mengder**: N (noder), K (kjøretøy), depot 0
- [ ] **Parametre** eksplisitt definert: dᵢⱼ, tᵢⱼ, qᵢ, sᵢ, [eᵢ, lᵢ], Q (kapasitet)
- [ ] **Beslutningsvariabler**: xᵢⱼₖ, Tᵢ, ev. lastvariabler
- [ ] **Antakelser** listet og begrunnet (euklidisk distanse, konstant hastighet, ingen returlast)
- [ ] **Målfunksjon** – matematisk uttrykt
- [ ] **Restriksjoner** – kapasitet, tidsvinduer, flytbalans, retur til depot, subtour-eliminering
- [ ] **Symboltabell** (anbefalt)
- [ ] Modellvarianter/scenarioer (f.eks. antall biler, endret kapasitet)
- [ ] Kobling tilbake til problemstillingen

**Unngå:** numeriske verdier i formlene, resultater, kode/skjermbilder, teorihistorikk.

---

## 6. Analyse og resultater *(Fleste)*

- [ ] Resultater fra modellkjøring (ruter, total avstand, tidsbruk, bilutnyttelse)
- [ ] Sammenligning mot referanseløsning
- [ ] Scenario-/sensitivitetsanalyse
- [ ] Tabeller med tittel **over**, forklaring i tekst
- [ ] Figurer med figurtekst og kilde **under**
- [ ] Akser merket med enheter (km, min, tonn)
- [ ] Resultater koblet eksplisitt til problemstillingen

**Unngå:** tolkning ("dette betyr at..."), nye teorielementer, løsningsforslag, anbefalinger.

---

## 7. Diskusjon *(Alle)*

- [ ] Tolkning av hovedfunn i lys av problemstillingen
- [ ] Sammenligning med Solomon / Osvald & Stirn / annen litteratur
- [ ] Styrker og svakheter ved data, metode og modell
- [ ] Generaliserbarhet – overføring til reelle Lerøy-data
- [ ] Praktiske implikasjoner for oppdrettsnæringen
- [ ] **Refleksjon over KI-bruk** – muligheter og begrensninger (faglig gevinst)

**Unngå:** nye resultater/analyser, repetisjon av tall uten tolkning, konklusjoner.

---

## 8. Konklusjon *(Alle)*

- [ ] **Eksplisitt svar på problemstillingen**
- [ ] Kort oppsummering av hovedfunn
- [ ] Praktiske/teoretiske implikasjoner
- [ ] Forslag til videre arbeid (f.eks. reelle data, flere slakterier, stokastiske elementer)
- [ ] Kort refleksjon om prosjektets bidrag

**Unngå:** nye data/analyser, metode- eller teoridiskusjon, gjennomgang av hele rapporten.

---

## 9. Post-elementer (etter hoveddel)

- [ ] **Referanseliste** – APA 7, manuelt ført, alle kilder i teksten står i listen (og omvendt)
- [ ] **Referering til KI-verktøy** – i tekst + referanseliste + beskrivelse av KI-bruk i metodekapitlet
- [ ] **Vedlegg** – full kode, datasett, detaljerte tabeller, tekniske beregninger
- [ ] Sjekk at hvert vedlegg er eksplisitt referert i hovedteksten

---

## 10. Tverrgående kvalitet (A-nivå-sjekkliste)

- [ ] Problemstilling presis, avgrenset og undersøkelbar
- [ ] Tydelig kobling teori → metode → data → analyse → konklusjon
- [ ] Modell, data og antakelser er etterprøvbare
- [ ] Drøfting viser kritisk refleksjon
- [ ] Figurer og tabeller korrekt merket
- [ ] Språk klart, presist og logisk (unngå "mye", "mange", "viktig", "kanskje")
- [ ] Konsekvent personlig pronomen (vi-form akseptert)
- [ ] Konsekvent referansestil gjennom hele rapporten

---

## 11. Formelle krav (HiMolde)

- [ ] Bruk av offisiell mal (Word v2 eller Markdown-konvertert)
- [ ] Dokumentoppsett uendret fra malen
- [ ] Språkvalg konsekvent (norsk eller engelsk)
- [ ] Sidenummerering fra kapittel 1
- [ ] Innlevering innen **2026-05-24 kl. 17:00** (Fase 4 deadline)

---

## Prioritert rekkefølge for G01 fremover

1. Fullføre **Modellering (kap. 5)** – matematisk formulering
2. Kjøre modellen og bygge **Analyse og resultater (kap. 6)**
3. Skrive **Diskusjon (kap. 7)** og **Konklusjon (kap. 8)**
4. Ferdigstille **Introduksjon (kap. 1)** – skrives best til slutt
5. Sammendrag og abstract – helt til slutt
6. Referanseliste, vedlegg, finpuss
