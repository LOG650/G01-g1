# PROSJEKTSTYRINGSPLAN – FASE 2
**LOG650 – Forskningsprosjekt: Logistikk og kunstig intelligens**

**Prosjekttittel:** Ruteplanlegging av fortransport hos Lerøy
**Prosjektperiode:** Februar–Juni 2026
**Prosjektgruppe:** 4 studenter (Hanne Haugvaldstad, Mira Viem, Marte Dolva, Kenneth Sandvik)

---

## 1. Sammendrag
Prosjektet etablerer en kvantitativ ruteoptimaliseringsmodell for fortransport av slakteklar fisk. Modellen struktureres som et Vehicle Routing Problem (VRP) og analyserer kostnadsminimering under kapasitetsbegrensninger. Prosjektet kombinerer operasjonsanalyse og KI-støttet utviklingsmetodikk. Studien undersøker hvordan optimaliserte ruter påvirker transportkostnader sammenlignet med en referanseløsning.

## 2. Forskningsdesign og metodisk forankring
Studien gjennomføres som et kvantitativt modellbasert forskningsprosjekt. Forskningsdesignet er eksplorativt og analytisk, hvor en syntetisk, men realistisk datastruktur benyttes for å teste optimaliseringsalgoritmens ytelse. Metodisk forankres studien i operasjonsanalyse og heuristisk optimalisering.

## 3. Suksesskriterier (SMART)
*   **Spesifikt:** Utvikle VRP-modell for 7 lokaliteter og 1 slakteri.
*   **Målbart:** Dokumentere kostnadsreduksjon sammenlignet med baseline.
*   **Oppnåelig:** Implementeres i Python innen semesterets rammer.
*   **Relevant:** Bidrar til logistikkoptimalisering i havbruk.
*   **Tidsavgrenset:** Fullføres innen 1. juni 2026.

## 4. Arbeidsnedbrytningsstruktur (WBS)
1.  Initiering og proposal
2.  Datamodellering og parametere
3.  Avstandsmatrise
4.  Implementering av heuristisk algoritme
5.  Scenarioanalyse
6.  Resultatanalyse
7.  Rapportskriving
8.  Kvalitetssikring og peer-review
9.  Presentasjon

## 5. Kritisk linje-analyse
Kritisk linje består av følgende sekvens: Datamodellering → Implementering → Scenarioanalyse → Resultatanalyse → Rapportskriving. Forsinkelser i disse aktivitetene vil direkte påvirke prosjektets sluttdato.

## 6. Milepæler
| Milepæl | Dato |
| :--- | :--- |
| Godkjent proposal | 2026-02-15 |
| Godkjent prosjektplan | 2026-03-01 |
| Ferdig modell | 2026-04-01 |
| Scenarioanalyse ferdig | 2026-04-20 |
| Hovedutkast levert | 2026-05-01 |
| Endelig levering | 2026-06-01 |

## 7. Risikoanalyse (kvantitativ)
| Risiko | Sannsynlighet | Konsekvens | Risikoscore |
| :--- | :---: | :---: | :---: |
| Begrenset Python-kompetanse | 3 | 4 | 12 |
| Tidsmangel | 4 | 5 | 20 |
| Modellforenkling | 2 | 3 | 6 |
| Datavaliditet | 3 | 3 | 9 |

*(Risikoscore = Sannsynlighet × Konsekvens)*

## 8. Kvalitet og vurderingskriterier
For å møte vurderingskriteriene i LOG650 vektlegges: (1) tydelig avgrensning, (2) metodisk konsistens mellom forskningsspørsmål og modell, (3) reproduserbarhet, (4) analytisk dybde i scenarioanalyse, (5) korrekt og konsistent bruk av APA 7.

| Krav-ID | Beskrivelse |
| :--- | :--- |
| KR1 | Alle oppdrettslokaliteter skal besøkes én gang i ruten |
| KR2 | Transporten skal starte og avsluttes ved slakteriet |
| KR3 | Kjøretøyets kapasitetsbegrensning skal ikke overskrides |
| KR4 | Modellen skal kunne beregne totale transportkostnader |
| KR5 | Resultatene skal være reproduserbare ved bruk av samme datasett |

## Referanser
*   Laporte, G. (2009). Fifty years of vehicle routing. *Transportation Science*, 43(4), 408–416.
*   Toth, P., & Vigo, D. (2014). *Vehicle routing: Problems, methods, and applications*. SIAM.
*   Russell, S., & Norvig, P. (2021). *Artificial intelligence: A modern approach* (4th ed.). Pearson.
*   Christopher, M. (2016). *Logistics and supply chain management* (5th ed.). Pearson.
