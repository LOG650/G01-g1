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
Fortransport av slakteklar fisk fra oppdrettslokaliteter til slakteri er en sentral logistikkaktivitet i oppdrettsnæringen. Effektiv ruteplanlegging har stor betydning for transportkostnader, kjøretid, kapasitetsutnyttelse og miljøpåvirkning. Små forbedringer i rutevalg og planlegging kan gi betydelige gevinster, særlig i regioner med mange lokaliteter og varierende transportavstander. Samtidig er ruteplanlegging et komplekst beslutningsproblem som egner seg godt for kvantitative modeller og KI-støttet analyse.

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
Hovedmålet med prosjektet er å utvikle og analysere en kvantitativ modell for ruteplanlegging av fortransport i oppdrettsnæringen, og å vurdere hvordan slike modeller kan fungere som beslutningsstøtte. Delmålene er å formulere et forenklet ruteplanleggingsproblem, finne kostnadseffektive ruter ved hjelp av kvantitative metoder (heuristikker), og analysere hvordan endringer i sentrale forutsetninger påvirker løsningen.

### 1.5 Avgrensninger
Oppgaven er avgrenset til én region i Lerøy-systemet og ett slakteri. Studien omfatter kun fortransport på land med én type transportmiddel. Eksport, videre distribusjon og øvrige deler av verdikjeden inngår ikke. Prosjektet fokuserer på modellering og analyse av ruteplanlegging, ikke på detaljerte operative eller kontraktsmessige forhold.

---

## 2. Teoretisk rammeverk
### 2.1 Logistikk og ruteplanlegging
Prosjektet tilhører logistikkområdet nettverksdesign og ruteplanlegging. Dette området omhandler hvordan transportnettverk kan struktureres og hvordan ruter kan planlegges for å minimere kostnader eller andre ytelsesmål gitt gitte rammebetingelser.

### 2.2 Vehicle Routing Problem (VRP)
VRP er en klassisk optimaliseringsutfordring som handler om å finne det optimale settet med ruter for en flåte av kjøretøy som skal levere til et spesifikt sett med kunder. I vårt tilfelle er "kundene" oppdrettslokalitetene som skal besøkes for henting av fisk.

### 2.3 Kunstig Intelligens i operasjonsanalyse
KI benyttes i dette prosjektet som et støtteverktøy for å løse komplekse ruteplanleggingsproblemer som ellers ville vært tidkrevende å beregne manuelt.

---

## 3. Metode
### 3.1 Forskningsdesign
Studien gjennomføres som en kvantitativ modellerings- og analyseoppgave. Vi benytter et eksplorativt og analytisk design for å teste hvordan ulike parametere påvirker den optimale ruten.

### 3.2 Datainnsamling og datagrunnlag
Prosjektet benytter syntetiske, men realistiske data konstruert ved hjelp av faktiske geografiske lokasjoner i den valgte regionen. 
*   Geografiske koordinater for 7 oppdrettslokaliteter og 1 slakteri.
*   Avstandsmatrise mellom alle lokasjoner.
*   Transportvolumer ved hver lokalitet.

### 3.3 Modellering og implementering
Modellen implementeres i Python. Vi benytter heuristiske metoder (f.eks. Nearest Neighbor eller mer avanserte algoritmer) for å identifisere gode løsninger på ruteplanleggingsproblemet.

### 3.4 Bruk av KI-verktøy
KI benyttes for støtte i koding, feilsøking, datagenerering og visualisering. Vi legger vekt på at alle faglige valg og tolkninger gjøres av studentgruppen selv.

---

## 4. Analyse og resultater
*(Her vil vi presentere den utviklede modellen, avstandsmatriser, visualisering av ruter og sammenligning med baseline-løsningen.)*

---

## 5. Diskusjon
*(Her vil vi diskutere resultatene i lys av teorien og de valgte forskningsspørsmålene.)*

---

## 6. Konklusjon
*(Her oppsummeres prosjektets bidrag og svar på problemstillingen.)*

---

## Referanser
*(Referanser føres i APA 7. stil.)*
- Laporte, G. (2009). Fifty years of vehicle routing. *Transportation Science*, 43(4), 408–416.
- Toth, P., & Vigo, D. (2014). *Vehicle routing: Problems, methods, and applications*. SIAM.
- Russell, S., & Norvig, P. (2021). *Artificial intelligence: A modern approach* (4th ed.). Pearson.
- Christopher, M. (2016). *Logistics and supply chain management* (5th ed.). Pearson.
