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


if __name__ == "__main__":
    data = last_data()
    sanity_check(data)
