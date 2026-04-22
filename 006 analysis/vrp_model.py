"""
VRP-modell for fortransport av slakteklar fisk – LOG650 G01
============================================================
Implementerer CVRPTW-modellen fra rapportens kap. 6:
  - Steg 1: Datalasting og sanity check
  - Steg 2: Greedy nearest-neighbor heuristikk (iterativt 1, 2, 3... biler)
  - Steg 3: MILP-formulering med PuLP/CBC
  - Steg 4: Sammenligning NN vs MILP
  - Steg 5: Scenarioanalyse (kap. 6.4)
"""

import io
import json
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

DATA_PATH = Path(__file__).parent.parent / "004 data" / "data.json"


def last_data(path: Path = DATA_PATH) -> dict:
    """Les datasett fra data.json."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def sanity_check(data: dict) -> None:
    """Steg 1: Skriv ut nøkkeltall og valider datagrunnlaget."""
    depot = data["depot"]
    lok = data["locations"]
    Q = data["capacity"]
    D = data["distance_matrix"]
    T = data["time_matrix"]

    print("=" * 60)
    print("STEG 1 – Datalasting og sanity check")
    print("=" * 60)

    print(f"\nDepot (slakteri): id={depot['id']}, pos=({depot['x']}, {depot['y']})")
    print(f"Depot tidsvindu: [{depot['time_window'][0]}, {depot['time_window'][1]}] min")
    print(f"  → T_max (maksimal rutevarighet) = {depot['time_window'][1]} min\n")

    print(f"Antall oppdrettslokaliteter: {len(lok)}")
    print(f"Kjøretøykapasitet Q = {Q} enheter\n")

    print(f"{'Node':<6}{'x':>5}{'y':>5}{'qᵢ':>6}{'sᵢ':>6}{'eᵢ':>6}{'lᵢ':>6}")
    print("-" * 40)
    total_demand = 0
    for n in lok:
        tw = n["time_window"]
        print(f"L{n['id']:<5}{n['x']:>5}{n['y']:>5}"
              f"{n['demand']:>6}{n['service_time']:>6}{tw[0]:>6}{tw[1]:>6}")
        total_demand += n["demand"]

    print("-" * 40)
    print(f"Sum etterspørsel = {total_demand} enheter")
    print(f"Minimum antall biler = ceil({total_demand}/{Q}) = {-(-total_demand // Q)}\n")

    n_nodes = len(lok) + 1
    assert len(D) == n_nodes, f"Avstandsmatrise feil dim: {len(D)} ≠ {n_nodes}"
    assert len(T) == n_nodes, f"Tidsmatrise feil dim: {len(T)} ≠ {n_nodes}"
    for i in range(n_nodes):
        assert D[i][i] == 0, f"D[{i}][{i}] ≠ 0"
        assert T[i][i] == 0, f"T[{i}][{i}] ≠ 0"
        for j in range(n_nodes):
            assert abs(D[i][j] - D[j][i]) < 1e-6, f"D usymmetrisk på ({i},{j})"
    print("✓ Matrise-sjekk OK (8×8, diagonal = 0, symmetrisk)")

    for n in lok:
        tw = n["time_window"]
        assert tw[0] <= tw[1], f"Node {n['id']}: tidsvindu ugyldig ({tw[0]} > {tw[1]})"
        assert n["demand"] <= Q, f"Node {n['id']}: qᵢ ({n['demand']}) > Q ({Q})"
    print("✓ Tidsvinduer og etterspørsel konsistente")

    avg_d = sum(D[0][j] for j in range(1, n_nodes)) / (n_nodes - 1)
    print(f"\nGjennomsnitt avstand depot → lokalitet: {avg_d:.1f} km")
    print(f"Maks avstand fra depot: {max(D[0][1:]):.1f} km (til L{D[0].index(max(D[0][1:]))})")


def nearest_neighbor(data: dict, K: int) -> dict:
    """
    Greedy nearest-neighbor heuristikk for CVRPTW med K kjøretøy.

    For hver bil:
      - start ved depot (node 0)
      - velg gjentatte ganger nærmeste ubesøkte lokalitet som oppfyller:
        * kapasitet  (load + qᵢ ≤ Q)
        * tidsvindu  (eᵢ ≤ ankomst ≤ lᵢ)
        * retur til depot innen T_max
      - returner til depot
    """
    lok = data["locations"]
    D = data["distance_matrix"]
    T = data["time_matrix"]
    Q = data["capacity"]
    T_max = data["depot"]["time_window"][1]
    loc = {n["id"]: n for n in lok}

    unvisited = set(loc.keys())
    routes = []
    total_distance = 0.0

    for k in range(1, K + 1):
        if not unvisited:
            break

        current = 0
        route_nodes = [0]
        route_dist = 0.0
        load = 0
        time_now = 0

        while True:
            best_j, best_d, best_arr = None, float("inf"), None
            for j in sorted(unvisited):
                node = loc[j]
                if load + node["demand"] > Q:
                    continue
                arrival = max(time_now + T[current][j], node["time_window"][0])
                if arrival > node["time_window"][1]:
                    continue
                end = arrival + node["service_time"] + T[j][0]
                if end > T_max:
                    continue
                if D[current][j] < best_d:
                    best_d, best_j, best_arr = D[current][j], j, arrival

            if best_j is None:
                break

            node = loc[best_j]
            route_nodes.append(best_j)
            route_dist += D[current][best_j]
            load += node["demand"]
            time_now = best_arr + node["service_time"]
            current = best_j
            unvisited.remove(best_j)

        route_dist += D[current][0]
        return_time = time_now + T[current][0]
        route_nodes.append(0)
        total_distance += route_dist

        routes.append({
            "vehicle": k,
            "nodes": route_nodes,
            "distance": route_dist,
            "load": load,
            "return_time": return_time,
        })

    return {
        "routes": routes,
        "total_distance": total_distance,
        "unvisited": sorted(unvisited),
        "feasible": len(unvisited) == 0,
    }


def print_nn_result(K: int, result: dict) -> None:
    """Formatert utskrift av én iterasjon."""
    print(f"\n--- K = {K} kjøretøy ---")
    for r in result["routes"]:
        seq = " → ".join(f"L{n}" if n else "D" for n in r["nodes"])
        print(f"  Bil {r['vehicle']}: {seq}")
        print(f"    kjørelengde = {r['distance']:.1f} km"
              f" | last = {r['load']}/{180} enheter"
              f" | retur kl. {r['return_time']:.0f} min")

    if result["unvisited"]:
        manglende = ", ".join(f"L{j}" for j in result["unvisited"])
        print(f"  ⚠ Ikke betjent: {manglende}")
    else:
        print(f"  ✓ Alle 7 lokaliteter betjent")

    print(f"  Total kjørelengde = {result['total_distance']:.2f} km")


def steg2_nn_iterativt(data: dict) -> None:
    """Steg 2: kjør NN med K=1, 2, 3, ... til feasible og stabil."""
    print("\n" + "=" * 60)
    print("STEG 2 – NN-heuristikk, iterativt 1, 2, 3, ... biler")
    print("=" * 60)

    results_per_K = []
    for K in range(1, 5):
        res = nearest_neighbor(data, K)
        print_nn_result(K, res)
        results_per_K.append((K, res))

        if res["feasible"]:
            if len(results_per_K) >= 2:
                prev = results_per_K[-2][1]
                if prev["feasible"] and res["total_distance"] >= prev["total_distance"]:
                    print(f"\n→ K={K} gir ikke kortere total kjørelengde enn K={K-1}."
                          f" Optimal K for NN = {K-1}.")
                    return
            else:
                print(f"\n→ K={K} er første feasible løsning. Prøver K={K+1} for sammenligning.")

    print("\n→ Grense nådd uten at NN stabiliserer. Se resultat over.")


if __name__ == "__main__":
    data = last_data()
    sanity_check(data)
    steg2_nn_iterativt(data)
