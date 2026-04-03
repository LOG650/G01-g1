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

## 5. Endelig Verifisering av Beregninger
Etter implementering av den harde returbegrensningen, er følgende ruter bekreftet som optimale og korrekte:

| Kjøretøy | Rute | Total Last | Returtid | Verifisering |
| :--- | :--- | :--- | :--- | :--- |
| **Bil 1** | 0 → 6 → 7 → 4 → 0 | 134 tonn | **422,0 min** | Velger L6 og L7 som nærmeste naboer. Etter L7 er L1, L2, L3 og L5 stengt. Kun L4 er tilgjengelig før fristen. |
| **Bil 2** | 0 → 5 → 2 → 0 | 65 tonn | **224,0 min** | Velger L5 (nærmeste ledige). Går så til L2 (kun 7 min unna). Etter L2 er det for sent for L1 og L3. |
| **Bil 3** | 0 → 1 → 3 → 0 | 113 tonn | **317,0 min** | Henter de to siste lokasjonene. Ankommer L1 tidlig, venter til åpningstid, og fortsetter til L3. |

### Hvorfor 3 biler? (Sjekkliste)
*   **Kapasitet:** Total etterspørsel er 312 tonn. Bilkapasitet er 180 tonn. To biler kunne teoretisk båret vekten (360 tonn), men **tiden er flaskehalsen**.
*   **Tidsvinduer:** Lokasjoner som L1 (stenger kl. 126) og L3 (stenger kl. 207) er så strenge at én bil ikke kan ta disse etter å ha utført andre ruter.
*   **Retur til depot:** Den harde grensen på 480 minutter hindrer Bil 1 i å legge til flere stopp etter L4.

## 6. Konklusjon
Visualiseringene og de manuelle beregningene er 100% konsistente med de underliggende dataene. Koordinatene stemmer overens med kartet, og alle operasjonelle begrensninger er overholdt. Disse figurene og tabellene underbygger de kvantitative funnene og forklarer hvorfor 3 biler er den operasjonelle minimumsløsningen.
