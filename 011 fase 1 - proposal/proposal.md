# Proposal LOG650: Ruteplanlegging av fortransport hos Lerøy ved bruk av kvantitative metoder og KI-støttet analyse

**Gruppemedlemmer:** 
Hanne Haugvaldstad 
Mira Wiem 
Marte Dolva 
Kenneth Sandvik

---

## Innledning og bakgrunn
Fortransport av slakteklar fisk fra oppdrettslokaliteter til slakteri er en sentral logistikkaktivitet i oppdrettsnæringen. Effektiv ruteplanlegging har stor betydning for transportkostnader, kjøretid, kapasitetsutnyttelse og miljøpåvirkning. Små forbedringer i rutevalg og planlegging kan gi betydelige gevinster, særlig i regioner med mange lokaliteter og varierende transportavstander. Samtidig er ruteplanlegging et komplekst beslutningsproblem som egner seg godt for kvantitative modeller og KI-støttet analyse.

Denne oppgaven tar utgangspunkt i fortransport i én region hos Lerøy og undersøker hvordan ruteplanlegging kan modelleres og analyseres ved hjelp av kvantitative metoder. Studien er avgrenset til transport fra 7 oppdrettslokaliteter til ett slakteri og fokuserer på kostnadsminimering som beslutningskriterium.

## Område
Prosjektet tilhører logistikkområdet nettverksdesign og ruteplanlegging. Dette området omhandler hvordan transportnettverk kan struktureres og hvordan ruter kan planlegges for å minimere kostnader eller andre ytelsesmål gitt gitte rammebetingelser. Fortransport i oppdrettsnæringen er et typisk eksempel på et ruteplanleggingsproblem der beslutninger tas på bakgrunn av lokasjoner, avstander, volumer og kapasitet.

## Problemstilling
Hvordan kan kvantitative ruteplanleggingsmodeller, støttet av kunstig intelligens, bidra til mer effektiv fortransport av slakteklar fisk i én region hos Lerøy?

### Forskningsspørsmål:
1. Hvordan kan fortransporten modelleres som et ruteplanleggingsproblem (Vehicle Routing Problem) basert på tilgjengelige data om lokasjoner, avstander og transportvolumer?
2. Hvilke ruter gir lavest samlet transportkostnad sammenlignet med en enkel referanseløsning (baseline)?
3. Hvordan påvirkes den optimale ruten av endringer i transportvolum og antall oppdrettslokaliteter innenfor gitte rammebetingelser?

## Mål
Hovedmålet med prosjektet er å utvikle og analysere en kvantitativ modell for ruteplanlegging av fortransport i oppdrettsnæringen, og å vurdere hvordan slike modeller kan fungere som beslutningsstøtte. Delmålene er å formulere et forenklet ruteplanleggingsproblem, finne kostnadseffektive ruter ved hjelp av kvantitative metoder (heuristikker), og analysere hvordan endringer i sentrale forutsetninger påvirker løsningen.

## Data
Prosjektet benytter syntetiske, men realistiske data konstruert ved hjelp av faktiske geografiske lokasjoner i den valgte regionen og faglige antagelser. Følgende datatyper er nødvendige:
- Geografiske koordinater for 7 oppdrettslokaliteter og 1 slakteri.
- Avstandsmatrise mellom alle lokasjoner basert på reelle veiafstander eller euklidsk distanse.
- Transportvolumer (tonn fisk) ved hver lokalitet.
- Kostnadsparametere (f.eks. kostnad per kjørte kilometer).
- Kjøretøyets lastekapasitet.

## Målfunksjon
Målfunksjonen er å minimere den totale transportkostnaden. Dette beregnes som summen av alle distansene mellom de besøkte lokasjonene i ruten, multiplisert med en fastsatt kostnad per kilometer. Ved å minimere denne funksjonen identifiseres den mest kostnadseffektive ruten innenfor modellens begrensninger (som kapasitet og krav om at alle lokasjoner skal besøkes én gang).

## Avgrensninger
Oppgaven er avgrenset til én region i Lerøy-systemet og ett slakteri. Studien omfatter kun fortransport på land med én type transportmiddel. Eksport, videre distribusjon og øvrige deler av verdikjeden inngår ikke. Prosjektet fokuserer på modellering og analyse av ruteplanlegging, ikke på detaljerte operative eller kontraktsmessige forhold.

## Teoretisk ramme og metode
Prosjektet bygger på teori innen logistikk og operasjonsanalyse, med særlig vekt på Vehicle Routing Problem (VRP). Studien gjennomføres som en kvantitativ modellerings- og analyseoppgave. Modellen implementeres i Python ved bruk av heuristiske metoder for å løse optimaliseringsproblemet. Resultatene evalueres gjennom en scenarioanalyse for å undersøke modellens følsomhet for endringer i parametere.

## Bruk av kunstig intelligens
Kunstig intelligens benyttes som et verktøy for å støtte analyseprosessen, særlig innen databehandling, modellimplementering (koding i Python), beregning og visualisering av ruter. Studentene har ansvar for alle faglige vurderinger, tolkning av resultater og valg av modellstruktur. KI brukes som støtte for effektivisering, ikke som erstatning for faglig refleksjon og logistikkfaglig forståelse.
