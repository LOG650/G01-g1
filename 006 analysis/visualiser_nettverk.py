import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

nodes = [
    {"id": 0, "navn": "Slakteri",     "x": 75, "y": 19, "etterspørsel": None, "tw": (0, 480)},
    {"id": 1, "navn": "Lokalitet 1",  "x": 54, "y": 81, "etterspørsel": 28,   "tw": (80, 126)},
    {"id": 2, "navn": "Lokalitet 2",  "x": 11, "y": 14, "etterspørsel": 39,   "tw": (19, 271)},
    {"id": 3, "navn": "Lokalitet 3",  "x": 70, "y": 93, "etterspørsel": 85,   "tw": (94, 207)},
    {"id": 4, "navn": "Lokalitet 4",  "x": 16, "y":  8, "etterspørsel": 44,   "tw": (62, 435)},
    {"id": 5, "navn": "Lokalitet 5",  "x": 17, "y": 10, "etterspørsel": 26,   "tw": (32, 275)},
    {"id": 6, "navn": "Lokalitet 6",  "x": 87, "y": 42, "etterspørsel": 15,   "tw": (21, 178)},
    {"id": 7, "navn": "Lokalitet 7",  "x": 96, "y": 87, "etterspørsel": 75,   "tw": (83, 423)},
]

depot = nodes[0]
lokaliteter = nodes[1:]

fig, axes = plt.subplots(1, 2, figsize=(16, 7))
fig.suptitle("Transportnettverk – Fortransport av slakteklar fisk (Lerøy case)", fontsize=13, fontweight="bold")

# --- Plott 1: Nettverk med noder ---
ax = axes[0]
ax.set_facecolor("#f7f9fc")
ax.set_title("Nodekart: Slakteri og lokaliteter", fontsize=11)

# Tegn linjer fra slakteri til alle lokaliteter
for n in lokaliteter:
    ax.plot([depot["x"], n["x"]], [depot["y"], n["y"]],
            color="#b0c4de", linewidth=0.8, zorder=1, linestyle="--")

# Lokaliteter – størrelse skalert etter etterspørsel
for n in lokaliteter:
    size = n["etterspørsel"] * 4
    ax.scatter(n["x"], n["y"], s=size, color="#3a7ebf", edgecolors="white",
               linewidths=1.5, zorder=3)
    ax.annotate(
        f"L{n['id']}\n{n['etterspørsel']} t",
        xy=(n["x"], n["y"]),
        xytext=(5, 5), textcoords="offset points",
        fontsize=8, color="#1a1a2e"
    )

# Slakteri (depot)
ax.scatter(depot["x"], depot["y"], s=250, color="#e63946", edgecolors="white",
           linewidths=2, zorder=4, marker="s")
ax.annotate("Slakteri\n(depot)", xy=(depot["x"], depot["y"]),
            xytext=(5, 5), textcoords="offset points",
            fontsize=8.5, fontweight="bold", color="#e63946")

ax.set_xlim(-5, 110)
ax.set_ylim(-5, 105)
ax.set_xlabel("X-koordinat")
ax.set_ylabel("Y-koordinat")
ax.grid(True, linestyle="--", alpha=0.4)

lokpatch = mpatches.Patch(color="#3a7ebf", label="Lokalitet (størrelse = etterspørsel)")
depotpatch = mpatches.Patch(color="#e63946", label="Slakteri (depot)")
ax.legend(handles=[depotpatch, lokpatch], fontsize=8, loc="upper left")

# --- Plott 2: Tidsvindu per lokalitet (horisontalt) ---
ax2 = axes[1]
ax2.set_facecolor("#f7f9fc")
ax2.set_title("Tidsvindu og etterspørsel per lokalitet", fontsize=11)

ids      = [f"L{n['id']}" for n in lokaliteter]
etterspørsel = [n["etterspørsel"] for n in lokaliteter]
tw_start = [n["tw"][0] for n in lokaliteter]
tw_slutt = [n["tw"][1] for n in lokaliteter]
tw_bredde = [sl - s for s, sl in zip(tw_start, tw_slutt)]

y_pos = np.arange(len(ids))

# Tidsvindu som horisontale stolper
bars_tw = ax2.barh(y_pos, tw_bredde, left=tw_start, color="#3a7ebf", alpha=0.6,
                   height=0.5, label="Tidsvindu [start, slutt]")

# Etterspørsel som tekst på stolpene
for i, (s, b, e) in enumerate(zip(tw_start, tw_bredde, etterspørsel)):
    midpoint = s + b / 2
    ax2.text(midpoint, i, f"{e} t", ha="center", va="center",
             fontsize=8, color="white", fontweight="bold")

ax2.set_yticks(y_pos)
ax2.set_yticklabels(ids)
ax2.set_xlabel("Tid (minutter fra oppstart)")
ax2.set_xlim(0, 500)
ax2.grid(True, axis="x", linestyle="--", alpha=0.4)
ax2.legend(fontsize=8)

plt.tight_layout()
plt.savefig("../004 data/nettverk_visualisering.png", dpi=150, bbox_inches="tight")
plt.show()
print("Lagret: 004 data/nettverk_visualisering.png")
