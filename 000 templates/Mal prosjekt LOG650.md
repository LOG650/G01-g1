# Prosjektoppgave
**LOG650 Forskningsprosjekt: Logistikk og KI**

**Tittel (norsk og/eller engelsk)**

**Forfatter(e)**

Molde, Innleveringsdato

---

## Sammendrag

---

## Abstract

---

# 2 Teorigrunnlag

## 2.1 Vehicle Routing Problem (VRP)
Vehicle Routing Problem (VRP) er en sentral optimaliseringsutfordring innen logistikk og transportplanlegging. Problemet ble først formelt beskrevet av Dantzig og Ramser i 1959 som "The Truck Dispatching Problem". Kjernen i problemet er å finne den mest kostnadseffektive måten å distribuere varer fra et sentralt depot til et sett med geografisk spredte kunder ved bruk av en flåte med kjøretøy (Laporte, u.å.). Målet er vanligvis å minimere totale transportkostnader, som ofte er en funksjon av kjørt distanse, antall biler eller tidsbruk.

## 2.2 VRP med tidsvinduer (VRPTW)
En av de mest studerte utvidelsene av VRP er Vehicle Routing Problem with Time Windows (VRPTW). Her legges det til en tidsbegrensning for hver kunde, hvor tjenesten må starte innenfor et spesifikt tidsintervall $[e_i, l_i]$. Solomon (1987) la grunnlaget for mye av den moderne forskningen på dette feltet ved å systematisere innsettingsheuristikker som balanserer både romlige (distanse) og temporale (tid) faktorer. Solomon påpekte at VRPTW er et NP-hardt problem, noe som betyr at det er beregningsmessig svært vanskelig å finne optimale løsninger for store flåter, og man er derfor ofte avhengig av avanserte heuristikker for å finne gode løsninger innen rimelig tid.

## 2.3 Tidsavhengighet og distribusjon av ferskvarer
I praktiske anvendelser er reisetiden mellom to punkter sjelden konstant. Reisetiden påvirkes av faktorer som kø og rushtrafikk, noe som fører til tidsavhengige reisetider (VRPTWTD). For varer med kort holdbarhet, som ferske grønnsaker, er tid en spesielt kritisk faktor. 

Osvald og Stirn (2008) utvidet Solomons modeller ved å inkludere kostnaden for kvalitetstap (perishability) direkte i objektfunksjonen. Deres forskning viser at ved å kombinere tidsavhengige reisedata med modeller for vareforringelse, kan man redusere svinn betydelig. For ferskvarer betyr dette at den optimale ruten ikke nødvendigvis er den korteste i distanse, men den som best bevarer varens kommersielle verdi frem til kunden.

---

## Innhold
*(Innholdsfortegnelse)*

---

# 1 Hovedkapittel (Heading 1)
På denne siden starter sidenummerering og selve besvarelsen (med overskrifter og normaltekst 1,5 linjeavstand). På hjemmesiden til høgskolen finner du Word-veiledninger for bruk av våre dokumentmaler, for eksempel om innholdsfortegnelse og overskrifter. Slett dette avsnittet og overskriftene/innholdet ellers på denne siden, og du kan starte skriving av (eller kopiere inn) din besvarelse.

## 1.1 Underkapittel (Heading 2)

### 1.1.1 Underkapittel (Heading 3)

#### 1.1.1.1 Heading 4

##### 1.1.1.1.1 Heading 5

###### 1.1.1.1.1.1 Heading 6
