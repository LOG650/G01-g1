# Selvvurdering – rapport mot peer-review-kriterier

Sammenstilt 2026-04-29 etter [veiledning peer-review LOG650.pdf](veiledning peer-review LOG650.pdf), kryssjekket mot [014 fase 4 - report/rapport.md](../014 fase 4 - report/rapport.md).

Hensikt: identifisere svake punkter før rapporten går til peer-review, slik at gruppen får så konstruktiv tilbakemelding som mulig.

Skala per punkt: ✅ dekket · ⚠️ delvis · ❌ mangler

---

## ⚠️ Kritisk feil: Kap. 1 har ødelagt nummerering

I siste versjon av [rapport.md](../014 fase 4 - report/rapport.md) finnes:

- 1.2 Delproblemer (valgfri) — tom overskrift, skulle ha vært slettet
- 1.3 Avgrensinger
- 1.3 Antagelser ← **duplikatnummer**

Sannsynligvis et merge-uhell. Må rettes til 1.2 Avgrensinger og 1.3 Antagelser før peer-review.

---

## 1. Innledning

| Kriterium | Status | Kommentar |
|-----------|--------|-----------|
| Bakgrunn og kontekst | ✅ | Fortransport av slakteklar fisk er godt etablert i 1.0 |
| Problemstilling | ✅ | Tydelig "hvordan"-formulering i 1.1 |
| Forskningsmål/-spørsmål | ✅ | Tre konkrete FS i 1.1 |
| Studiens betydning og relevans | ⚠️ | Antydes ("har stor betydning for transportkostnader, kjøretid, kapasitetsutnyttelse og miljøpåvirkning"), men kunne vært løftet eksplisitt – f.eks. ett avsnitt som forklarer hvorfor ruteplanlegging i havbruk er underforsket / praktisk verdifullt |
| Sammenheng mål ↔ betydning | ⚠️ | Implisitt, ikke eksplisitt argumentert |

**Konkrete forbedringer:**
- Legg til 1–2 setninger om hvorfor akkurat dette caset er verdt å undersøke (samfunnsmessig, faglig hull, praktisk gevinst).

---

## 2. Litteraturgjennomgang og teoretisk forankring

| Kriterium | Status | Kommentar |
|-----------|--------|-----------|
| Relevant forskning | ✅ | Kap. 2 dekker 5-års utvikling, Solomon, Adamo, Liu, Bogyrbayeva, Archetti |
| Teoretiske/begrepsmessige hull | ⚠️ | Antydes ("Vår oppgave ligger nærmere denne forskningsretningen"), men aldri eksplisitt formulert som *"litteraturen mangler X"* |
| Gjennomgang av metoder + begrunnelse | ✅ | Kap. 3.3 og 3.4 dekker eksakte vs. heuristikker, valg er begrunnet |

**Konkrete forbedringer:**
- Legg til én eksplisitt setning om hvilket gap dere bidrar til – f.eks. "Lite litteratur kobler eksplisitt VRPTW til norsk havbruksfortransport," eller "Få studier sammenligner enkle heuristikker med MILP på små, tidskritiske case."

---

## 3. Metode

| Kriterium | Status | Kommentar |
|-----------|--------|-----------|
| Metodevalg plausible og sammenhengende | ✅ | NN + MILP er begrunnet og henger sammen med problemstillingen |
| Detaljer i analytisk rammeverk | ✅ | Kap. 6 har formelt rammeverk med mengder, parametere, formler |
| Beskrivelse av data | ✅ | Kap. 5.1 og 5.2 dekker syntetisk datasett, struktur, generering |
| **Validitet, reliabilitet, etikk** | ⚠️ | **Ikke eksplisitt forklart med disse begrepene.** Reproduserbarhet er nevnt (5.4), KI-bruk er dokumentert. Validitet og reliabilitet bør likevel adresseres med navn |

**Konkrete forbedringer:**
- Legg til en kort seksjon (5.5 eller del av 5.4) om validitet, reliabilitet og etiske hensyn:
  - **Validitet**: i hvilken grad måler modellen det den skal? (matematisk korrekt formulering, samsvar med VRPTW-litteraturen)
  - **Reliabilitet**: kan andre reprodusere resultatene? (kode på GitHub, syntetisk datasett, deterministisk løsning)
  - **Etikk**: ingen personopplysninger; bruk av KI er åpent dokumentert i logg

---

## 4. Analyse og resultater

| Kriterium | Status | Kommentar |
|-----------|--------|-----------|
| Analysen er korrekt utført | ✅ | NN iterativt, MILP eksakt, scenarioanalyse konsekvent |
| Internt konsistente resultater | ✅ | Tall stemmer på tvers av tabeller |
| Logisk knyttet til FS | ✅ | Kap. 8.3 mapper hver FS til konkret nøkkeltall |

**Generelt sterk seksjon.** Ingen større endringer anbefalt.

---

## 5. Diskusjon

| Kriterium | Status | Kommentar |
|-----------|--------|-----------|
| Tolkning av forventede + uventede funn | ✅ | 9.1 forklarer hvorfor gap er stort; 9.2–9.4 reflekterer over teori og metode |
| Knyttet tilbake til FS | ✅ | Implisitt gjennom kap. 9.1 og 9.5, men kunne vært enda tydeligere "FS1 viser at...", "FS2 viser at..." |
| Implikasjoner for praksis/teori/policy | ✅ | Kap. 9.5 har tre konkrete praksisimplikasjoner |

**Konkret forbedring:**
- Vurder å åpne 9.1 med en setning som uttrykkelig knytter funn til hver av FS1, FS2, FS3.

---

## 6. Konklusjon

| Kriterium | Status | Kommentar |
|-----------|--------|-----------|
| Konsis oppsummering av sentrale funn | ❌ | **Kapittelet er tomt** |
| Studiens bidrag | ❌ | Mangler |
| Begrensninger | ❌ | Mangler (men er dekket i 9.3 – kan oppsummeres her) |
| Forslag til videre forskning | ❌ | Mangler |

**Status:** Kap. 10 må skrives før peer-review. Ifølge gruppen avventes godkjenning av hovedutkastet 27. april.

**Anbefaling:** Skriv en kort, foreløpig konklusjon (½–1 side) som besvarer problemstillingen og FS1/FS2/FS3, slik at peer-reviewerne kan vurdere helheten.

---

## 7. Skriveflyt, formelle aspekter og helhetsvurdering

| Kriterium | Status | Kommentar |
|-----------|--------|-----------|
| Klarhet i språk og struktur | ✅ | Stort sett god struktur, men se nummereringsbug i kap. 1 |
| Korrekt APA 7 og kryssreferanser | ✅ | Bibliografi i APA 7, alle tabeller/figurer kryssrefererert i tekst |
| Klarhet og kvalitet på figurer/tabeller | ✅ | Tre figurer er rent designet, akser merket med enheter, tabeller har titler |
| Bruk av forkortelser | ⚠️ | VRP, VRPTW, CVRPTW, MILP, MTZ, CBC introduseres riktig. **NN brukes uten å være innført som forkortelse for "Nearest Neighbor"**. Likeså **FS1/FS2/FS3** mangler en introduksjon (f.eks. "I det videre brukes FS1, FS2 og FS3 om de tre forskningsspørsmålene") |
| Originalitet | ⚠️ | Caset (havbruksfortransport) og dual-method-sammenligning (NN+MILP) er originalitet i kontekst, men kunne vært tydeligere fremhevet i innledningen |

**Konkrete forbedringer:**
- Første gang NN brukes (i kap. 6.2.2 eller tidligere): skriv ut "Nearest Neighbor (NN)".
- Innfør "FS1", "FS2", "FS3" eksplisitt i 1.1 etter forskningsspørsmålene.

---

## Pre-elementer (ikke eksplisitt vurderingsområde, men formelt nødvendig)

- ❌ **Forside**: tittel, forfattere, antall sider, dato ikke fylt inn
- ❌ **Egenerklæring**: ikke huket av
- ❌ **Personvern/NSD**: ikke krysset
- ❌ **Publiseringsavtale**: veileder/studiepoeng/fullmakt ikke fylt
- ❌ **Sammendrag** (norsk): mangler
- ❌ **Abstract** (engelsk): mangler

---

## Kort sammendrag (det reviewerne mest sannsynlig vil flagge)

**Tre kritiske mangler før peer-review:**
1. Kap. 1 nummereringsbug (1.2 Delproblemer + duplikat 1.3)
2. Kap. 10 Konklusjon helt tom
3. Forsideelementer + sammendrag + abstract mangler

**Mindre, men konkrete forbedringer:**
4. Innledning: ett avsnitt om studiens betydning
5. Litteratur: én eksplisitt setning om gapet dere bidrar til
6. Metode: kort omtale av validitet, reliabilitet og etikk med disse begrepene
7. Forkortelser: introduser NN og FS1–FS3 første gang de brukes

**Sterke sider å beholde:**
- Formell modellering (kap. 6) er gjennomarbeidet
- Resultater er rikt og objektivt presentert (kap. 7–8)
- Diskusjonen er nyansert og bruker litteraturen aktivt
- KI-bruk er åpent og grundig dokumentert
- Reproduserbarhet via GitHub
