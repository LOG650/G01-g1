# Todo etter peer-review fra G02

Basert på [Peer-review G01 3 (1).pdf](Peer-review%20G01%203%20(1).pdf) datert 2. mai 2026.

G2 sin samlede vurdering: faglig solid, sterk diskusjon, dual-metoden er en klar styrke. Tre hovedutfordringer + noen mindre punkter.

---

## Må fikses før innlevering (kritisk)

### 1. Skriv konklusjon (kap. 10)
- **Status:** Tom, kun overskrift
- **Hva trengs:** Oppsummer hovedfunn fra FS1–FS3, knytt tilbake til problemstillingen, kort om implikasjoner og videre arbeid
- **Eier:**
- **Estimert tid:** 1–2 timer

### 2. Skriv sammendrag (norsk) + abstract (engelsk)
- **Status:** Begge mangler
- **Hva trengs:** ~200 ord hver. Skrives til slutt når konklusjon er på plass
- **Eier:**
- **Estimert tid:** 1 time

### 3. Fiks MTZ-motsigelsen
- **Status:** Kap. 6.1.3 sier eksplisitt MTZ (`uᵢ − uⱼ + |V| · xᵢⱼ ≤ |V| − 1`), kap. 9.3 sier implisitt via monoton propagering av tid/last
- **Hva trengs:** Sjekk hva som faktisk kjøres i [006 analysis/vrp_model.py](../006%20analysis/vrp_model.py). Behold riktig versjon, rett opp den andre
- **Eier:**
- **Estimert tid:** 30 min

---

## Viktig, men ikke kritisk

### 4. Legg til avsnitt om validitet, reliabilitet og etikk
- **Status:** Reliabilitet er indirekte dekket (GitHub, prosjektlogg), men validitet og etikk mangler eget avsnitt
- **Hva trengs:** Kort avsnitt i metodekapittelet om
  - Validitet: hvor godt modellen måler det den skal
  - Etikk: KI-bruk og bruk av syntetiske data
- **Eier:**
- **Estimert tid:** 30–45 min

### 5. Avklar FS3 vs scenarier
- **Status:** FS3 sier "endringer i transportvolum og antall oppdrettslokaliteter", men scenariene i kap. 6.4/8.2 dekker også kapasitet, kjøretøytilgjengelighet og tidsvinduer
- **Hva trengs:** Enten omformuler FS3 til å dekke alle fem scenariene, eller kutt scenarier ned til det FS3 lover
- **Eier:**
- **Estimert tid:** 15 min

### 6. Avklar syntetiske data tidligere
- **Status:** Kommer først frem i kap. 5.1.1
- **Hva trengs:** Kort setning i innledningen eller casebeskrivelsen: caset er Lerøy-inspirert, men dataene er syntetiske
- **Eier:**
- **Estimert tid:** 10 min

---

## Småfeil

### 7. Rydd opp i bibliografien
- **Status:** Pangaribuan et al. (2025) og Tan & Yeh (2021) er oppført, men ikke sitert i teksten
- **Hva trengs:** Enten siter dem (f.eks. i litteraturkapittelet) eller fjern fra bibliografien
- **Eier:**
- **Estimert tid:** 10 min

### 8. Forklar CVRPTW-akronymet
- **Status:** VRP og VRPTW er introdusert, men CVRPTW dukker opp i kap. 6.1 uten at "C-en" (Capacitated) er forklart
- **Hva trengs:** En setning ved første bruk
- **Eier:**
- **Estimert tid:** 5 min

### 9. Rydd opp i overlapp mellom avgrensninger (1.2) og antagelser (1.3)
- **Status:** Euklidsk avstand og konstant kjørehastighet er listet som antagelser, men effekten beskrives også som avgrensning
- **Hva trengs:** Skill tydelig: valg av modell = avgrensning, forenkling av virkeligheten = antagelse. Eventuelt slå sammen
- **Eier:**
- **Estimert tid:** 20 min

---

## Forslag til arbeidsdeling (4 personer)

| Person | Oppgaver | Total tid |
|--------|----------|-----------|
| 1 | Konklusjon (1) + sammendrag/abstract (2) | ~2–3 t |
| 2 | MTZ-fiks (3) + validitet/reliabilitet/etikk (4) | ~1 t |
| 3 | FS3 vs scenarier (5) + syntetiske data tidligere (6) + avgrensninger/antagelser (9) | ~45 min |
| 4 | Bibliografi (7) + CVRPTW (8) + korrekturlesing av endringene over | ~1 t |

Person 1 har mest tekst å skrive — kan delvis avlastes ved at andre starter med sine punkter først.

---

## Ikke nevnt av G2, men verdt å vurdere

- G2 fant **ingen åpenbare svakheter** i kap. 7 og 8 (analyse/resultater). Disse trenger ingen endringer.
- Kap. 9 (diskusjon) ble fremhevet som rapportens sterkeste kapittel — kun MTZ-motsigelsen trenger oppretting der.
