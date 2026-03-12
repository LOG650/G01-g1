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

## 3. Konklusjon
Visualiseringene er konsistente med de underliggende dataene. Koordinatene (f.eks. Depot ved x=75, y=19) stemmer overens med kartet. Fargekodingen og pilene gjør det enkelt å følge flyten i hver rute. Disse figurene er egnet for bruk i sluttrapporten for å underbygge de kvantitative funnene.
