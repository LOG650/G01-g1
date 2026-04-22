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


def milp_solve(data: dict, K_max: int = 4) -> dict:
    """
    Eksakt MILP-løsning av CVRPTW (kap. 6.1).
    Bruker PuLP med CBC-løseren.
    Implementerer alle restriksjoner fra kap. 6.1.3:
      - besøk én gang (inn/ut-grad = 1 for alle kunder)
      - flyt i depot (antall biler ut = antall biler inn)
      - tidsvindu (eᵢ ≤ aᵢ ≤ lᵢ)
      - tids-propagering (big-M, hindrer subtours i tid)
      - retur til depot innen T_max
      - kapasitets-propagering (big-M, hindrer subtours i last)
    """
    from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary, PULP_CBC_CMD

    lok = data["locations"]
    D = data["distance_matrix"]
    T = data["time_matrix"]
    Q = data["capacity"]
    T_max = data["depot"]["time_window"][1]

    N = list(range(len(lok) + 1))
    V = list(range(1, len(lok) + 1))
    loc = {n["id"]: n for n in lok}

    prob = LpProblem("CVRPTW", LpMinimize)

    x = {(i, j): LpVariable(f"x_{i}_{j}", cat=LpBinary)
         for i in N for j in N if i != j}
    a = {i: LpVariable(f"a_{i}", lowBound=0, upBound=T_max) for i in N}
    L = {i: LpVariable(f"L_{i}", lowBound=0, upBound=Q) for i in N}

    prob += lpSum(D[i][j] * x[(i, j)] for (i, j) in x)

    for i in V:
        prob += lpSum(x[(i, j)] for j in N if j != i) == 1
        prob += lpSum(x[(j, i)] for j in N if j != i) == 1

    prob += lpSum(x[(0, j)] for j in V) <= K_max
    prob += lpSum(x[(0, j)] for j in V) == lpSum(x[(i, 0)] for i in V)

    for i in V:
        prob += a[i] >= loc[i]["time_window"][0]
        prob += a[i] <= loc[i]["time_window"][1]
    prob += a[0] == 0

    M_time = T_max + max(n["service_time"] for n in lok) + 500
    for i in N:
        si = loc[i]["service_time"] if i != 0 else 0
        for j in V:
            if i != j:
                prob += a[i] + si + T[i][j] - M_time * (1 - x[(i, j)]) <= a[j]

    for i in V:
        si = loc[i]["service_time"]
        prob += a[i] + si + T[i][0] <= T_max + M_time * (1 - x[(i, 0)])

    prob += L[0] == 0
    M_load = Q + 500
    for i in N:
        for j in V:
            if i != j:
                prob += L[i] + loc[j]["demand"] - M_load * (1 - x[(i, j)]) <= L[j]
    for j in V:
        prob += L[j] >= loc[j]["demand"]

    prob.solve(PULP_CBC_CMD(msg=0))

    if prob.status != 1:
        return {"feasible": False, "status": prob.status}

    used = [(i, j) for (i, j), v in x.items() if v.varValue and v.varValue > 0.5]
    starts = sorted(j for (i, j) in used if i == 0)
    routes = []
    for s in starts:
        route = [0, s]
        current = s
        while current != 0:
            nxt_list = [j for (i, j) in used if i == current]
            if not nxt_list:
                break
            nxt = nxt_list[0]
            route.append(nxt)
            current = nxt
        dist = sum(D[route[k]][route[k + 1]] for k in range(len(route) - 1))
        load = sum(loc[n]["demand"] for n in route if n != 0)
        last = route[-2]
        ret = a[last].varValue + loc[last]["service_time"] + T[last][0]
        routes.append({
            "vehicle": len(routes) + 1,
            "nodes": route,
            "distance": dist,
            "load": load,
            "return_time": ret,
        })

    return {
        "feasible": True,
        "routes": routes,
        "total_distance": prob.objective.value(),
        "n_vehicles": len(routes),
    }


def steg3_milp(data: dict) -> dict:
    print("\n" + "=" * 60)
    print("STEG 3 – Eksakt MILP-løsning (PuLP + CBC)")
    print("=" * 60)

    result = milp_solve(data, K_max=4)
    if not result["feasible"]:
        print(f"  ⚠ Ingen løsning funnet (status {result.get('status')})")
        return result

    print(f"\nOptimal løsning funnet med {result['n_vehicles']} kjøretøy")
    for r in result["routes"]:
        seq = " → ".join(f"L{n}" if n else "D" for n in r["nodes"])
        print(f"  Bil {r['vehicle']}: {seq}")
        print(f"    kjørelengde = {r['distance']:.2f} km"
              f" | last = {r['load']}/{180}"
              f" | retur kl. {r['return_time']:.0f} min")
    print(f"\n  ✓ Total kjørelengde (OPTIMUM) = {result['total_distance']:.2f} km")
    return result


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


def steg4_sammenlign(data: dict, nn_result: dict, milp_result: dict,
                    save_figures: bool = True) -> None:
    """Steg 4: formell sammenligning NN vs MILP + tabeller og figurer."""
    import matplotlib.pyplot as plt

    print("\n" + "=" * 60)
    print("STEG 4 – Sammenligning NN-heuristikk vs MILP-optimum")
    print("=" * 60)

    nn_total = nn_result["total_distance"]
    milp_total = milp_result["total_distance"]
    gap_pct = (nn_total - milp_total) / milp_total * 100

    print(f"\n{'Metode':<25}{'Biler':>8}{'Total km':>12}{'Gap vs optimum':>18}")
    print("-" * 63)
    print(f"{'MILP (optimum)':<25}{milp_result['n_vehicles']:>8}"
          f"{milp_total:>12.2f}{'0.00 %':>18}")
    print(f"{'NN-heuristikk':<25}{len(nn_result['routes']):>8}"
          f"{nn_total:>12.2f}{gap_pct:>16.2f} %")
    print("-" * 63)

    print("\nPer bil (MILP):")
    for r in milp_result["routes"]:
        ut = r["load"] / 180 * 100
        print(f"  Bil {r['vehicle']}: {r['distance']:>6.1f} km"
              f" | last {r['load']:>3}/180 ({ut:.0f} %)"
              f" | retur {r['return_time']:.0f} min")

    print("\nPer bil (NN):")
    for r in nn_result["routes"]:
        ut = r["load"] / 180 * 100
        print(f"  Bil {r['vehicle']}: {r['distance']:>6.1f} km"
              f" | last {r['load']:>3}/180 ({ut:.0f} %)"
              f" | retur {r['return_time']:.0f} min")

    print("\nHovedfunn:")
    diff_km = nn_total - milp_total
    diff_biler = len(nn_result["routes"]) - milp_result["n_vehicles"]
    print(f"  • NN bruker {diff_biler} flere bil(er) enn optimum")
    print(f"  • NN kjører {diff_km:.1f} km lengre ({gap_pct:.1f} % over optimum)")
    print(f"  • MILP utnytter kapasiteten bedre "
          f"(snitt {sum(r['load'] for r in milp_result['routes']) / len(milp_result['routes']):.0f}"
          f" mot {sum(r['load'] for r in nn_result['routes']) / len(nn_result['routes']):.0f} enheter)")

    if not save_figures:
        return

    fig, axes = plt.subplots(1, 2, figsize=(15, 7))
    fig.suptitle("Sammenligning av løsninger – NN-heuristikk vs. MILP-optimum",
                 fontsize=13, fontweight="bold")

    colors = ["#3a7ebf", "#e63946", "#2a9d8f", "#f4a261", "#9b5de5"]
    lok = {n["id"]: n for n in data["locations"]}
    depot = data["depot"]

    for ax, result, title in [(axes[0], nn_result, f"NN-heuristikk ({len(nn_result['routes'])} biler, {nn_total:.1f} km)"),
                              (axes[1], milp_result, f"MILP-optimum ({milp_result['n_vehicles']} biler, {milp_total:.1f} km)")]:
        ax.set_facecolor("#f7f9fc")
        ax.set_title(title, fontsize=11)

        for idx, r in enumerate(result["routes"]):
            xs = [depot["x"] if n == 0 else lok[n]["x"] for n in r["nodes"]]
            ys = [depot["y"] if n == 0 else lok[n]["y"] for n in r["nodes"]]
            c = colors[idx % len(colors)]
            ax.plot(xs, ys, "-o", color=c, linewidth=2, markersize=8,
                    label=f"Bil {r['vehicle']} ({r['distance']:.0f} km)", zorder=3)

        for n in data["locations"]:
            ax.annotate(f"L{n['id']}", xy=(n["x"], n["y"]),
                        xytext=(6, 6), textcoords="offset points", fontsize=9)

        ax.scatter(depot["x"], depot["y"], s=220, color="black",
                   marker="s", zorder=5, edgecolors="white", linewidths=1.5)
        ax.annotate("Slakteri", xy=(depot["x"], depot["y"]),
                    xytext=(6, 6), textcoords="offset points",
                    fontsize=9, fontweight="bold")

        ax.set_xlim(-5, 110)
        ax.set_ylim(-5, 105)
        ax.set_xlabel("X-koordinat")
        ax.set_ylabel("Y-koordinat")
        ax.grid(True, linestyle="--", alpha=0.4)
        ax.legend(fontsize=8, loc="upper left")

    plt.tight_layout()
    out = Path(__file__).parent.parent / "004 data" / "sammenligning_NN_vs_MILP.png"
    plt.savefig(out, dpi=150, bbox_inches="tight")
    print(f"\nFigur lagret: {out.relative_to(Path(__file__).parent.parent)}")

    fig2, ax = plt.subplots(figsize=(8, 5))
    metoder = ["MILP\n(optimum)", "NN-heuristikk"]
    verdier = [milp_total, nn_total]
    biler = [milp_result["n_vehicles"], len(nn_result["routes"])]
    farger = ["#2a9d8f", "#e63946"]

    bars = ax.bar(metoder, verdier, color=farger, edgecolor="white", linewidth=2)
    for bar, v, b in zip(bars, verdier, biler):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 5,
                f"{v:.1f} km\n{b} biler",
                ha="center", fontsize=10, fontweight="bold")

    ax.set_ylabel("Total kjørelengde (km)")
    ax.set_title(f"Total kjørelengde per løsningsmetode\n"
                 f"(optimalitetsgap = {gap_pct:.1f} %)",
                 fontsize=11, fontweight="bold")
    ax.set_ylim(0, max(verdier) * 1.2)
    ax.grid(True, axis="y", linestyle="--", alpha=0.4)
    ax.set_axisbelow(True)

    plt.tight_layout()
    out2 = Path(__file__).parent.parent / "004 data" / "total_distanse_sammenligning.png"
    plt.savefig(out2, dpi=150, bbox_inches="tight")
    print(f"Figur lagret: {out2.relative_to(Path(__file__).parent.parent)}")


def run_both(data: dict, K_max: int = 4) -> tuple[dict, dict]:
    """Kjør NN iterativt til feasible + MILP, returner begge resultater."""
    nn_best = None
    for K in range(1, K_max + 1):
        r = nearest_neighbor(data, K)
        if r["feasible"]:
            if nn_best is None or r["total_distance"] < nn_best["total_distance"]:
                nn_best = r
            else:
                break
    milp = milp_solve(data, K_max=K_max)
    return nn_best, milp


def lag_scenario(base: dict, navn: str, **endringer) -> dict:
    """Lag modifisert datasett for scenarioanalyse."""
    import copy
    d = copy.deepcopy(base)
    d["_scenario"] = navn

    if "etterspørsel_faktor" in endringer:
        f = endringer["etterspørsel_faktor"]
        for loc in d["locations"]:
            loc["demand"] = round(loc["demand"] * f)

    if "kapasitet" in endringer:
        d["capacity"] = endringer["kapasitet"]

    if "tidsvindu_faktor" in endringer:
        f = endringer["tidsvindu_faktor"]
        for loc in d["locations"]:
            e, l = loc["time_window"]
            mid = (e + l) / 2
            bredde = (l - e) * f
            loc["time_window"] = [round(mid - bredde / 2), round(mid + bredde / 2)]

    return d


def steg5_scenarioanalyse(base_data: dict) -> None:
    """Steg 5: Kjør alle scenarier fra kap. 6.4, samle og presenter resultater."""
    print("\n" + "=" * 60)
    print("STEG 5 – Scenarioanalyse (kap. 6.4)")
    print("=" * 60)

    scenarier = [
        ("Baseline",            {}),
        ("Økt etterspørsel +20 %", {"etterspørsel_faktor": 1.20}),
        ("Redusert kapasitet (Q=120)", {"kapasitet": 120}),
        ("Flere kjøretøy (K_max=5)", {}),
        ("Strammere tidsvinduer (50 %)", {"tidsvindu_faktor": 0.5}),
    ]

    resultater = []
    for navn, endringer in scenarier:
        data_s = lag_scenario(base_data, navn, **endringer)
        sum_dem = sum(loc["demand"] for loc in data_s["locations"])
        Q_s = data_s["capacity"]
        print(f"\n--- {navn} ---")
        print(f"  Sum etterspørsel: {sum_dem} | Kapasitet: {Q_s}"
              f" | Min biler (kap.): {-(-sum_dem // Q_s)}")

        K_max = 5 if "Flere kjøretøy" in navn else 4
        nn, milp = run_both(data_s, K_max=K_max)

        if nn is None:
            nn_str = "INFEASIBLE"
            nn_km = None
            nn_K = None
        else:
            nn_km = nn["total_distance"]
            nn_K = len(nn["routes"])
            nn_str = f"{nn_km:.1f} km / {nn_K} biler"

        if milp and milp.get("feasible"):
            milp_km = milp["total_distance"]
            milp_K = milp["n_vehicles"]
            milp_str = f"{milp_km:.1f} km / {milp_K} biler"
            if nn_km is not None:
                gap = (nn_km - milp_km) / milp_km * 100
                gap_str = f"{gap:.1f} %"
            else:
                gap_str = "n/a"
        else:
            milp_str = "INFEASIBLE"
            gap_str = "n/a"

        print(f"  NN:   {nn_str}")
        print(f"  MILP: {milp_str}")
        print(f"  Gap:  {gap_str}")

        resultater.append({
            "scenario": navn,
            "sum_demand": sum_dem,
            "kapasitet": Q_s,
            "nn": nn,
            "milp": milp,
        })

    print("\n" + "=" * 60)
    print("OPPSUMMERINGSTABELL (steg 5)")
    print("=" * 60)
    print(f"\n{'Scenario':<32}{'MILP km':>10}{'MILP K':>8}"
          f"{'NN km':>10}{'NN K':>7}{'Gap':>9}")
    print("-" * 76)
    for r in resultater:
        milp = r["milp"]
        nn = r["nn"]
        if milp and milp.get("feasible"):
            mk, mK = f"{milp['total_distance']:.1f}", str(milp["n_vehicles"])
        else:
            mk, mK = "inf.", "—"
        if nn is not None:
            nk, nK = f"{nn['total_distance']:.1f}", str(len(nn["routes"]))
        else:
            nk, nK = "inf.", "—"
        gap = "—"
        if nn is not None and milp and milp.get("feasible"):
            gap = f"{(nn['total_distance'] - milp['total_distance']) / milp['total_distance'] * 100:.1f} %"
        print(f"{r['scenario']:<32}{mk:>10}{mK:>8}{nk:>10}{nK:>7}{gap:>9}")
    print("-" * 76)

    lag_scenario_figur(resultater)
    return resultater


def lag_scenario_figur(resultater: list) -> None:
    """Stolpediagram: MILP vs NN total km per scenario."""
    import matplotlib.pyplot as plt
    import numpy as np

    navn = [r["scenario"] for r in resultater]
    milp_km = [r["milp"]["total_distance"] if r["milp"] and r["milp"].get("feasible") else 0
               for r in resultater]
    nn_km = [r["nn"]["total_distance"] if r["nn"] is not None else 0 for r in resultater]

    x = np.arange(len(navn))
    w = 0.38
    fig, ax = plt.subplots(figsize=(12, 6))
    bars_m = ax.bar(x - w / 2, milp_km, w, color="#2a9d8f", label="MILP (optimum)",
                    edgecolor="white")
    bars_n = ax.bar(x + w / 2, nn_km, w, color="#e63946", label="NN-heuristikk",
                    edgecolor="white")

    for bar, v in zip(bars_m, milp_km):
        if v > 0:
            ax.text(bar.get_x() + bar.get_width() / 2, v + 8, f"{v:.0f}",
                    ha="center", fontsize=9, fontweight="bold")
    for bar, v in zip(bars_n, nn_km):
        if v > 0:
            ax.text(bar.get_x() + bar.get_width() / 2, v + 8, f"{v:.0f}",
                    ha="center", fontsize=9, fontweight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels(navn, rotation=15, ha="right", fontsize=9)
    ax.set_ylabel("Total kjørelengde (km)")
    ax.set_title("Scenarioanalyse – total kjørelengde per scenario og metode",
                 fontsize=12, fontweight="bold")
    ax.legend(loc="upper left", fontsize=10)
    ax.grid(True, axis="y", linestyle="--", alpha=0.4)
    ax.set_axisbelow(True)
    ax.set_ylim(0, max(max(nn_km), max(milp_km)) * 1.2)

    plt.tight_layout()
    out = Path(__file__).parent.parent / "004 data" / "scenarioanalyse.png"
    plt.savefig(out, dpi=150, bbox_inches="tight")
    print(f"\nFigur lagret: {out.relative_to(Path(__file__).parent.parent)}")


if __name__ == "__main__":
    data = last_data()
    sanity_check(data)
    steg2_nn_iterativt(data)
    nn_best, milp_best = run_both(data)
    steg3_milp(data)
    steg4_sammenlign(data, nn_best, milp_best)
    steg5_scenarioanalyse(data)
