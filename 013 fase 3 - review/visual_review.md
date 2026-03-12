# Review av Visualiseringer

**Dato:** 12.03.2026
**Status:** Godkjent

Denne filen dokumenterer gjennomgangen av de genererte visualiseringene for ruteplanleggingsprosjektet. Formålet var å bekrefte at de visuelle fremstillingene stemmer overens med dataene i `data.json`, resultatene fra `vrp_model.py` og analysen i `rapport.md`.

## 1. Baseline Visualisering (`baseline_visualisering.png`)
*   **Observert mønster:** "Stjerneform" (Star topology).
*   **Beskrivelse:** Figuren viser 7 individuelle ruter som stråler ut fra depotet (rød firkant) til hver enkelt oppdrettslokalitet (blå sirkler) og direkte tilbake.
*   **Innsikt:**
    *   Illustrerer tydelig ineffektiviteten ved "en bil per kunde"-strategien.
    *   Mye overlappende kjøring frem og tilbake på samme strekninger.
    *   Bekrefter at referanseløsningen bruker 7 biler og kjører totalt 839 km.

## 2. Heuristisk Løsning Visualisering (`rute_visualisering.png`)
*   **Observert mønster:** 3 distinkte løkker (Clusters).
*   **Beskrivelse:** Figuren viser hvordan lokalitetene er gruppert i logiske klynger basert på nærhet:
    *   **Rute 1 (Grønn):** En stor løkke som dekker østsiden (L6, L7) og svinger innom L4.
    *   **Rute 2 (Oransje):** En effektiv tur-retur som dekker de vestlige punktene L5 og L2.
    *   **Rute 3 (Lilla):** En nordlig rute som tar for seg L1 og L3.
*   **Innsikt:**
    *   Viser tydelig hvordan ruteplanleggeren sparer kjørelengde ved å besøke nabopunkter i sekvens.
    *   Ingen unødvendige returer til depotet midt i en rute.
    *   Bekrefter reduksjonen til 3 biler og 534 km total kjørelengde.

## 3. Analyse av antall biler: Hvorfor ikke 1 bil?
Selv om en lastebil har en kapasitet på 180 tonn (som er nok til å bære hele regionens volum på 312 tonn i bare to turer), viser beregningene at vi trenger **3 biler** på grunn av tidsbegrensninger:

*   **Tidsvinduer:** Mange lokasjoner har overlappende eller tidlige tidsvinduer (f.eks. L1 som stenger kl. 126 min). Én bil rekker ikke å kjøre innom alle disse før vinduene lukkes.
*   **Retur til depot:** Den harde grensen på 480 minutter (8 timer) betyr at en bil som har besøkt 3 lokasjoner (som i Rute 1) allerede har brukt 422 minutter. Det er ikke nok tid igjen til å besøke flere steder og returnere trygt.
*   **Kapasitet vs. Tid:** Selv om bilen har ledig plass, er det "tiden som går ut" før lastekapasiteten er fullt utnyttet.

| Antall biler | Status | Årsak |
| :--- | :--- | :--- |
| **1 Bil** | **Ikke mulig** | Rekker kun 3 av 7 lokasjoner før tidsvinduer stenger eller returfristen nås. |
| **2 Biler** | **Ikke mulig** | Rekker 5 av 7 lokasjoner. De to siste lokasjonene ligger geografisk slik til at tidsbruken overskrider 480 min. |
| **3 Biler** | **Optimalt** | Alle 7 lokasjoner besøkes, og alle biler er tilbake på slakteriet innenfor fristen. |

## 4. Drøfting: Ventetid vs. Just-In-Time (JIT)
I løpet av reviewen har vi vurdert hvordan modellen håndterer ankomsttider i forhold til tidsvinduenes åpningstid.

*   **Nåværende logikk:** Modellen tillater at en bil ankommer *før* tidsvinduet åpner. I slike tilfeller "venter" bilen ved lokasjonen til åpningstid (f.eks. kl. 08:00) før lasteprosessen starter. Dette maksimerer utnyttelsen av tiden, da bilen allerede er på plass når vinduet åpner.
*   **Vurdert alternativ (JIT):** Vi har vurdert en strengere begrensning der bilen ikke kan ankomme før åpningstid. Dette ville betydd at bilen måtte vente ved forrige lokasjon eller depotet. 
*   **Konsekvens:** En JIT-tilnærming ville sannsynligvis ha forskjøvet hele ruteplanen senere på dagen. Dette ville gjort det enda vanskeligere å overholde den harde 480-minutters returfristen til depotet, og kunne potensielt ha krevd enda flere biler. 

Nåværende løsning med "venting ved lokasjon" anses som den mest realistiske og effektive tilnærmingen for fortransport i denne regionen.

## 5. Konklusjon
Visualiseringene er konsistente med de underliggende dataene. Koordinatene (f.eks. Depot ved x=75, y=19) stemmer overens med kartet. Fargekodingen og pilene gjør det enkelt å følge flyten i hver rute. Disse figurene er egnet for bruk i sluttrapporten for å underbygge de kvantitative funnene og forklare hvorfor 3 biler er den operasjonelle minimumsløsningen.
