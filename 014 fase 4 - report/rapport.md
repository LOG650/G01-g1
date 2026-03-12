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
Datagrunnlaget etableres ved bruk av syntetiske, men realistiske data konstruert ved hjelp av faktiske geografiske lokasjoner i den valgte regionen. 
*   Geografiske koordinater for 7 oppdrettslokaliteter og 1 slakteri.
*   Avstandsmatrise mellom alle lokasjoner.
*   Transportvolumer (tonn fisk) ved hver lokalitet.

### 3.3 Modellering og analyse
Modellarbeidet innebærer implementering av algoritmer i Python for å finne kostnadseffektive ruter. Vi tester ulike løsninger og gjennomfører en scenarioanalyse for å dokumentere funnene. Resultatene sammenlignes med en definert baseline for å vurdere effektivitetsgevinsten.

### 3.4 Kvalitetssikring
Kvalitet i arbeidet sikres gjennom intern gjennomgang av kode og tekst, kontroll av kilder og jevn vurdering av framdrift. Det legges vekt på korrekt bruk av referanser etter APA 7. standard.

---

## 4. Analyse og resultater
I dette kapittelet presenteres resultatene fra modelleringen av ruteplanleggingsproblemet. Vi sammenligner en heuristisk løsning basert på en "greedy" algoritme med en enkel referanseløsning (baseline).

### 4.1 Sammenligning av løsninger
Modellen har analysert transport fra 7 oppdrettslokaliteter til ett slakteri (depot) med en bilkapasitet på 180 enheter.

| Parameter | Referanseløsning (Baseline) | Heuristisk løsning (Greedy) |
| :--- | :---: | :---: |
| Antall ruter | 7 | 3 |
| Total distanse | 839.28 km | 534.00 km |
| **Forbedring (%)** | - | **36.37%** |

### 4.2 Visualisering av ruter
Den heuristiske løsningen optimaliserer rutevalget ved å kombinere flere lokaliteter i samme rute, så lenge kapasitets- og tidsvindubegrensninger overholdes.

*   **Rute 1:** 0 -> 6 -> 7 -> 4 -> 0
*   **Rute 2:** 0 -> 5 -> 2 -> 0
*   **Rute 3:** 0 -> 1 -> 3 -> 0

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
- Laporte, G. (2009). Fifty years of vehicle routing. *Transportation Science*, 43(4), 408–416.
- Toth, P., & Vigo, D. (2014). *Vehicle routing: Problems, methods, and applications*. SIAM.
- Russell, S., & Norvig, P. (2021). *Artificial intelligence: A modern approach* (4th ed.). Pearson.
- Christopher, M. (2016). *Logistics and supply chain management* (5th ed.). Pearson.
