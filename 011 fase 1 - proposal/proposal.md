# Proposal LOG650

**Gruppemedlemmer:** 
Hanne Haugvaldstad 
Mira Wiem 
Marte Dolva 
Kenneth Sandvik


**Område:**
Prosjektet tilhører logistikkområdet nettverksdesign og ruteplanlegging. Dette området omhandler hvordan transportnettverk kan struktureres og hvordan ruter kan planlegges for å minimere kostnader eller andre ytelsesmål gitt gitte rammebetingelser. Fortransport i oppdrettsnæringen er et typisk eksempel på et ruteplanleggingsproblem der beslutninger tas på bakgrunn av lokasjoner, avstander, volumer og kapasitet.

**Bedrift (valgbart):**
Fortransport av slakteklar fisk fra oppdrettslokaliteter til slakteri er en sentral logistikkaktivitet i oppdrettsnæringen. Effektiv ruteplanlegging har stor betydning for transportkostnader, kjøretid, kapasitetsutnyttelse og miljøpåvirkning. Små forbedringer i rutevalg og planlegging kan gi betydelige gevinster, særlig i regioner med mange lokaliteter og varierende transportavstander. Samtidig er ruteplanlegging et komplekst beslutningsproblem som egner seg godt for kvantitative modeller og KI-støttet analyse.
Denne oppgaven tar utgangspunkt i fortransport i én region hos Lerøy og undersøker hvordan ruteplanlegging kan modelleres og analyseres ved hjelp av kvantitative metoder. Studien er avgrenset til transport fra et begrenset antall oppdrettslokaliteter til ett slakteri og fokuserer på kostnadsminimering som beslutningskriterium.


**Problemstilling:**
Hvordan kan kvantitative ruteplanleggingsmodeller, støttet av kunstig intelligens, bidra til mer effektiv fortransport av slakteklar fisk i én region hos Lerøy?

Forskningsspørsmål:
1: Hvordan kan fortransporten modelleres som et ruteplanleggingsproblem basert på tilgjengelige data om lokasjoner, avstander og transportvolumer?

2:Hvilke ruter gir lavest samlet transportkostnad sammenlignet med en enkel referanseløsning?

3.	Hvordan påvirkes den optimale ruten av endringer i transportvolum og antall oppdrettslokaliteter innenfor gitte rammebetingelser?

**Data:**
Kunstig intelligens benyttes som et verktøy for å støtte analyseprosessen, særlig innen databehandling, modellimplementering, beregning og visualisering. Studentene har ansvar for valg av område, problemstilling, modellstruktur, tolkning av resultater og faglige vurderinger. KI brukes som støtte, ikke som erstatning for faglig refleksjon.

**Beslutningsvariabler:**
Beslutningsvariablene i modellen representerer rekkefølgen oppdrettslokalitetene besøkes i, og hvilke forbindelser som etableres mellom lokasjonene. Modellen søker å identifisere den kombinasjonen av rutevalg som minimerer total transportkostnad.

**Målfunksjon:**
Målfunksjonen er å minimere total transportkostnad, definert som:

Total transportkostnad = sum (distanse mellom besøkte lokasjoner × kostnad per kilometer)

Ved å minimere denne funksjonen identifiseres den mest kostnadseffektive ruten innenfor modellens begrensninger.

**Avgrensninger:**
Oppgaven er avgrenset til én region i Lerøy-systemet og ett slakteri. Studien omfatter kun fortransport på land og én transporttype. Eksport, videre distribusjon og øvrige deler av verdikjeden inngår ikke. Datagrunnlaget baseres på syntetiske data som representerer et realistisk transportoppsett, konstruert ved hjelp av faktiske geografiske lokasjoner, åpne kilder og faglige antagelser. Prosjektet fokuserer på modellering og analyse av ruteplanlegging, ikke på detaljerte operative eller kontraktsmessige forhold