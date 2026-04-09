# LOG650: Forskningsprosjekt - Logistikk og kunstig intelligens

**Tittel:** Ruteplanlegging av fortransport hos Lerøy ved bruk av kvantitative metoder og KI-støttet analyse

**Dato:** Mars 2026
**Gruppe:** 4
**Medlemmer:** Hanne Haugvaldstad, Mira Viem, Marte Dolva, Kenneth Sandvik

---

## Sammendrag
*(Dette avsnittet skrives når rapporten er ferdig og oppsummerer hele prosjektet, metoden og de viktigste funnene.)*

---

## 1. Innledning
### 1.1 Bakgrunn
Fortransport av slakteklar fisk fra oppdrettslokaliteter til slakteri er en sentral logistikkaktivitet i havbruksnæringen. Effektiv ruteplanlegging har stor betydning for transportkostnader, kjøretid, kapasitetsutnyttelse og miljøpåvirkning. Dette prosjektet omhandler en kvantitativ analyse av transportlogistikken hos Lerøy, med mål om å organisere transporten mer effektivt ved hjelp av digitale verktøy og logistiske metoder.

### 1.2 Bedriftspresentasjon
Denne oppgaven tar utgangspunkt i fortransport i én region hos Lerøy. Lerøy Seafood Group er en av verdens største produsenter av laks og ørret, og effektivitet i fortransporten er kritisk for å sikre ferskhet og kostnadskontroll i verdikjeden.

### 1.3 Problemstilling og forskningsspørsmål
Hovedproblemstillingen for dette prosjektet er:
*Hvordan kan kvantitative ruteplanleggingsmodeller, støttet av kunstig intelligens, bidra til mer effektiv fortransport av slakteklar fisk i én region hos Lerøy?*

For å besvare denne problemstillingen har vi definert følgende forskningsspørsmål:
1. Hvordan kan fortransporten modelleres som et ruteplanleggingsproblem (Vehicle Routing Problem) basert på tilgjengelige data om lokasjoner, avstander og transportvolumer?
2. Hvilke ruter gir lavest samlet transportkostnad sammenlignet med en enkel referanseløsning (baseline)?
3. Hvordan påvirkes den optimale ruten av endringer i transportvolum og antall oppdrettslokaliteter innenfor gitte rammebetingelser?

### 1.4 Målsetting
Hovedmålet med prosjektet er å utvikle og analysere en kvantitativ modell for ruteplanlegging av fortransport i oppdrettsnæringen, og å vurdere hvordan slike modeller kan fungere som beslutningsstøtte. Arbeidet skal resultere i en analyse av hvordan transporten kan optimaliseres ved hjelp av digitale verktøy.

### 1.5 Avgrensninger
Oppgaven er avgrenset til én region i Lerøy-systemet og ett slakteri. Studien omfatter kun fortransport på land med én type transportmiddel. Eksport, videre distribusjon og øvrige deler av verdikjeden inngår ikke. Prosjektet fokuserer på modellering og analyse av ruteplanlegging, ikke på detaljerte operative eller kontraktsmessige forhold.

---

## 2. Teoretisk rammeverk
### 2.1 Logistikk og ruteplanlegging
Prosjektet tilhører logistikkområdet nettverksdesign og ruteplanlegging. Dette området omhandler hvordan transportnettverk kan struktureres og hvordan ruter kan planlegges for å minimere kostnader eller andre ytelsesmål gitt gitte rammebetingelser.

### 2.2 Vehicle Routing Problem (VRP)
VRP er en klassisk optimaliseringsutfordring som handler om å finne det optimale settet med ruter for en flåte av kjøretøy som skal levere til et spesifikt sett med kunder. I vårt tilfelle er "kundene" oppdrettslokalitetene som skal besøkes for henting av fisk.

### 2.3 Kunstig Intelligens i operasjonsanalyse
KI benyttes i dette prosjektet som et støtteverktøy for å løse komplekse ruteplanleggingsproblemer som ellers ville vært tidkrevende å beregne manuelt, særlig i forbindelse med koding, feilsøking og visualisering.

---

## 3. Metode
### 3.1 Forskningsdesign
Studien gjennomføres som en kvantitativ modellerings- og analyseoppgave. Arbeidet følger en gradvis utvikling der hver fase bygger på resultatene fra den forrige. Forskningsdesignet er eksplorativt og analytisk, med fokus på å teste hvordan ulike parametere påvirker den optimale ruten.

### 3.2 Datainnsamling og datagrunnlag
Datagrunnlaget i prosjektet er basert på et syntetisk, men konsistent datasett generert av faglærer. Datasettet representerer ett depot (slakteri) og sju oppdrettslokaliteter, og er utviklet for å gi et realistisk grunnlag for modellering av ruteplanlegging med kapasitets- og tidsbegrensninger.

Datasettet består av følgende elementer:
- koordinater for 1 slakteri og 7 lokaliteter
- etterspørsel per lokalitet
- lastetid per lokalitet
- tidsvinduer for henting
- avstandsmatrise mellom alle noder
- tidsmatrise mellom alle noder
- kapasitet på kjøretøy

Koordinatene er oppgitt i et todimensjonalt koordinatsystem. Avstandene mellom lokasjonene er beregnet som euklidske luftlinjeavstander. Tidsmatrisen er generert ved å runde ned avstandene til hele minutter. Dette er en forenkling, men vurderes som hensiktsmessig i en avgrenset modellstudie.

Etterspørsel og lastetid brukes for å representere hvor mye som skal hentes ved hver lokalitet og hvor lang tid hvert stopp tar. Tidsvinduene angir når en lokalitet kan betjenes. Disse variablene er sentrale fordi modellen er formulert som et ruteplanleggingsproblem med tidsvinduer (VRPTW).

Kjøretøykapasiteten er satt til 180 enheter. Samlet etterspørsel i datasettet er 312 enheter, noe som innebærer at alle lokaliteter ikke kan betjenes i én enkelt rute. Dette gjør det nødvendig å analysere flere ruter og scenarioer for antall biler.

#### 3.2.1 Oversikt over inputdata

| Node | Rolle | x | y | Etterspørsel | Lastetid (min) | Tidsvindu start | Tidsvindu slutt |
|---|---|---:|---:|---:|---:|---:|---:|
| 0 | Slakteri    | 75 | 19 | - | - | 0 | 480 |
| 1 | Lokalitet 1 | 54 | 81 | 28 | 43 | 80 | 126 |
| 2 | Lokalitet 2 | 11 | 14 | 39 | 54 | 19 | 271 |
| 3 | Lokalitet 3 | 70 | 93 | 85 | 100 | 94 | 207 |
| 4 | Lokalitet 4 | 16 | 8 | 44 | 59 | 62 | 435 |
| 5 | Lokalitet 5 | 17 | 10 | 26 | 41 | 32 | 275 |
| 6 | Lokalitet 6 | 87 | 42 | 15 | 30 | 21 | 178 |
| 7 | Lokalitet 7 | 96 | 87 | 75 | 90 | 83 | 423 |

#### 3.2.2 Avstands- og tidsmatriser

Avstandsmatrisen er brukt som grunnlag for beregning av transportkostnad, mens tidsmatrisen er brukt for å kontrollere gjennomførbarhet opp mot tidsvinduer og maksimal rutevarighet. Avstandene er symmetriske, og diagonalen i matrisen er lik 0. Tidsmatrisen er avledet fra avstandsmatrisen ved å runde ned avstandene til hele minutter.

Full avstandsmatrise er vist i vedlegg A, og full tidsmatrise er vist i vedlegg B.

### 3.3 Modellering og analyse
Modellarbeidet innebærer implementering av algoritmer i Python for å finne kostnadseffektive ruter. Vi benytter en "Greedy" (grådig) heuristikk for å løse et Vehicle Routing Problem with Time Windows (VRPTW). Modellen bruker avstandsmatrise, tidsmatrise, etterspørsel, lastetid, tidsvinduer og kjøretøykapasitet som input.

Modellen inkluderer en hard retur-til-depot-begrensning, som sikrer at ingen lokasjon blir inkludert i en rute med mindre kjøretøyet beviselig rekker å returnere til slakteriet innen den maksimale tidsrammen på 480 minutter. Vi tester ulike løsninger og gjennomfører scenarioanalyse for å dokumentere funnene. Resultatene sammenlignes med en definert baseline for å vurdere effektivitetsgevinsten.

### 3.4 Kvalitetssikring
Kvalitet i arbeidet sikres gjennom intern gjennomgang av kode og tekst, kontroll av kilder og jevn vurdering av framdrift. Ved å bygge inn logiske sikkerhetsmekanismer direkte i koden (som f.eks. sjekk av returtid før hvert besøk), reduseres risikoen for urealistiske rutevalg. Det legges vekt på korrekt bruk av referanser etter APA 7. standard.

---

## 4. Analyse og resultater
I dette kapittelet presenteres resultatene fra modelleringen av ruteplanleggingsproblemet. Vi sammenligner en heuristisk løsning basert på en "greedy" algoritme med en enkel referanseløsning (baseline). Den heuristiske modellen er programmert til å alltid prioritere overholdelse av tidsvinduer og returfrist fremfor maksimal utnyttelse av bilens kapasitet.

### 4.1 Sammenligning av løsninger
Modellen har analysert transport fra 7 oppdrettslokaliteter til ett slakteri (depot) med en bilkapasitet på 180 enheter.

| Parameter | Referanseløsning (Baseline) | Heuristisk løsning (Greedy) |
| :--- | :---: | :---: |
| Antall ruter | 7 | 3 |
| Total distanse | 839.28 km | 534.00 km |
| **Forbedring (%)** | - | **36.37%** |

### 4.2 Visualisering og tidsbruk per rute
Den heuristiske løsningen optimaliserer rutevalget ved å kombinere flere lokaliteter i samme rute, så lenge kapasitets- og tidsvindubegrensninger overholdes. Algoritmen garanterer nå at samtlige ruter returnerer til slakteriet (depot) innen tidsrammen på 480 minutter (8 timer).

*   **Rute 1:** 0 -> 6 -> 7 -> 4 -> 0
    *   Last: 134 tonn
    *   Ankomst slakteri: **422,0 min** (7,0 timer)
*   **Rute 2:** 0 -> 5 -> 2 -> 0
    *   Last: 65 tonn
    *   Ankomst slakteri: **224,0 min** (3,7 timer)
*   **Rute 3:** 0 -> 1 -> 3 -> 0
    *   Last: 113 tonn
    *   Ankomst slakteri: **317,0 min** (5,3 timer)

*(Visualiseringer er generert og lagret som rute_visualisering.png og baseline_visualisering.png i prosjektmappen.)*

### 4.3 Analyse av tidsvinduer og kapasitet
Gjennom den heuristiske tilnærmingen ser vi at tidsvinduene er en kritisk begrensning. Selv om bilens kapasitet på 180 tillater flere stopp, begrenses rute 2 og 3 av når lokalitetene er tilgjengelige for henting. Dette illustrerer viktigheten av koordinering mellom slakteri og oppdrettslokaliteter.

### 4.4 Scenarioanalyse: Antall biler
For å undersøke den operative fleksibiliteten har vi analysert hvor mange biler som er nødvendig for å dekke alle lokasjoner gitt de faste begrensningene for kapasitet og tidsvinduer.

| Scenario | Status | Besøkte lokasjoner | Total distanse |
| :--- | :---: | :---: | :---: |
| 1 Bil | Inkomplett | 3 / 7 | 244.28 km |
| 2 Biler | Inkomplett | 5 / 7 | 374.37 km |
| **3 Biler** | **Fullført** | **7 / 7** | **534.00 km** |

Analysen viser at 3 biler er minimumskravet for å betjene alle oppdrettslokalitetene i denne regionen. Begrensningen ligger primært i tidsvinduene for når fisken kan hentes, kombinert med kjøretid mellom lokasjonene. Selv om én bil har kapasitet til å frakte mer volum, rekker den ikke over alle geografiske punkter innenfor de gitte tidsrammene.

---

## 5. Diskusjon
Resultatene viser en betydelig effektivitetsgevinst ved å bruke en heuristisk tilnærming sammenlignet med en enkel referanseløsning. En reduksjon i total kjørelengde på over 36% vil ha direkte innvirkning på både transportkostnader og miljøutslipp.

Scenarioanalysen av antall biler understreker at logistikken i havbruksnæringen er tidsfølsom. Valget av 3 biler fremstår som den mest kostnadseffektive løsningen som samtidig ivaretar alle leveransekrav.

---

## 6. Konklusjon
*(Her oppsummeres prosjektets bidrag og svar på problemstillingen.)*

---

## Referanser
- Christopher, M. (2016). *Logistics & supply chain management* (5th ed.). Pearson.
- Laporte, G. (2009). Fifty years of vehicle routing. *Transportation Science, 43*(4), 408–416. https://doi.org/10.1287/trsc.1090.0301
- Osvald, A., & Zadnik Stirn, L. (2008). A vehicle routing algorithm for the distribution of fresh vegetables and similar perishable food. *Journal of Food Engineering, 85*(2), 285–295. https://doi.org/10.1016/j.jfoodeng.2007.07.008
- Oyola, J., Arntzen, H., & Woodruff, D. L. (2018). The stochastic vehicle routing problem, a literature review, part I: Models. *EURO Journal on Transportation and Logistics, 7*(3), 193–221. https://doi.org/10.1007/s13676-016-0100-5
- Russell, S., & Norvig, P. (2021). *Artificial intelligence: A modern approach* (4th ed.). Pearson.
- Solomon, M. M. (1987). Algorithms for the vehicle routing and scheduling problems with time window constraints. *Operations Research, 35*(2), 254–265. https://doi.org/10.1287/opre.35.2.254
- Toth, P., & Vigo, D. (2014). *Vehicle routing: Problems, methods, and applications* (2nd ed.). SIAM.
- Utama, D. M., Dewi, S. K., Wahid, A., & Santoso, I. (2020). The vehicle routing problem for perishable goods: A systematic review. *Cogent Engineering, 7*(1), Article 1816148. https://doi.org/10.1080/23311916.2020.1816148

---

## Vedlegg

### Vedlegg A – Avstandsmatrise (km)

| Fra / til | Slakteri | Lok. 1 | Lok. 2 | Lok. 3 | Lok. 4 | Lok. 5 | Lok. 6 | Lok. 7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **Slakteri** | 0.0 | 65.5 | 64.2 | 74.2 | 60.0 | 58.7 | 25.9 | 71.2 |
| **Lokalitet 1** | 65.5 | 0.0 | 79.6 | 20.0 | 82.3 | 80.1 | 51.1 | 42.4 |
| **Lokalitet 2** | 64.2 | 79.6 | 0.0 | 98.6 | 7.8 | 7.2 | 81.0 | 112.0 |
| **Lokalitet 3** | 74.2 | 20.0 | 98.6 | 0.0 | 100.7 | 98.5 | 53.8 | 26.7 |
| **Lokalitet 4** | 60.0 | 82.3 | 7.8 | 100.7 | 0.0 | 2.2 | 78.7 | 112.4 |
| **Lokalitet 5** | 58.7 | 80.1 | 7.2 | 98.5 | 2.2 | 0.0 | 77.0 | 110.3 |
| **Lokalitet 6** | 25.9 | 51.1 | 81.0 | 53.8 | 78.7 | 77.0 | 0.0 | 45.9 |
| **Lokalitet 7** | 71.2 | 42.4 | 112.0 | 26.7 | 112.4 | 110.3 | 45.9 | 0.0 |

### Vedlegg B – Tidsmatrise (minutter)

| Fra / til | Slakteri | Lok. 1 | Lok. 2 | Lok. 3 | Lok. 4 | Lok. 5 | Lok. 6 | Lok. 7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **Slakteri** | 0 | 65 | 64 | 74 | 60 | 58 | 25 | 71 |
| **Lokalitet 1** | 65 | 0 | 79 | 20 | 82 | 80 | 51 | 42 |
| **Lokalitet 2** | 64 | 79 | 0 | 98 | 7 | 7 | 80 | 112 |
| **Lokalitet 3** | 74 | 20 | 98 | 0 | 100 | 98 | 53 | 26 |
| **Lokalitet 4** | 60 | 82 | 7 | 100 | 0 | 2 | 78 | 112 |
| **Lokalitet 5** | 58 | 80 | 7 | 98 | 2 | 0 | 76 | 110 |
| **Lokalitet 6** | 25 | 51 | 80 | 53 | 78 | 76 | 0 | 45 |
| **Lokalitet 7** | 71 | 42 | 112 | 26 | 112 | 110 | 45 | 0 |