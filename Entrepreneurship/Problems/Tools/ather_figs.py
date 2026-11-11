"""Figures for Assignment 8.1 (Six Ds analysis of Ather Energy). Run `python ather_figs.py`.
   All numbers are quoted from the sources listed in the note (company results as reported by Inc42 / Business Standard /
   Entrackr / The Machine Maker, BNEF via ESS News, Ather press); the 6-D scores are the author's judgement."""
import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets"); os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.size": 10, "axes.grid": True, "grid.alpha": .3, "axes.spines.top": False, "axes.spines.right": False})
C = ["#1f77b4", "#d62728", "#2ca02c", "#ff7f0e", "#9467bd", "#17becf"]
def save(fig, name): fig.savefig(os.path.join(OUT, name), dpi=150, bbox_inches="tight"); plt.close(fig); print("wrote", name)

def fig_evidence():
    fig, ax = plt.subplots(2, 2, figsize=(11.5, 7.6))
    a = ax[0, 0]
    fy = np.array([2020, 2024, 2025, 2026]); rev = np.array([79.8, 1754, 2255, 3671.8])
    a.semilogy(fy, rev, "o-", color=C[0], lw=2)
    for x, y in zip(fy, rev): a.annotate(f"₹{y:,.0f} Cr", (x, y), (x, y*1.35), ha="center", fontsize=9)
    a.set_ylim(40, 9000); a.set_xticks(fy); a.set_xticklabels([f"FY{str(v)[2:]}" for v in fy])
    cagr = (3671.8/79.8)**(1/6)-1
    a.set_title(f"Revenue from operations (log scale): ~46× in six years,\nCAGR ≈ {cagr*100:.0f}% (FY20→FY26)", fontsize=10)
    a.text(2020.1, 55, "FY21–FY23 not plotted (not in the sources used)", fontsize=7.5, color="grey")
    a = ax[0, 1]
    q = ["Q1 FY25", "Q2 FY25", "Q4 FY25", "Q1 FY26", "Q2 FY26"]; sh = [9, 12.1, 13.3, 14.3, 17.4]
    a.plot(range(5), sh, "o-", color=C[1], lw=2)
    for i, v in enumerate(sh): a.annotate(f"{v}%", (i, v), (i, v+.9), ha="center", fontsize=9)
    a.set_xticks(range(5)); a.set_xticklabels(q, fontsize=8.5); a.set_ylim(5, 21); a.set_title("Share of the Indian electric two-wheeler market\n(quarterly)", fontsize=10)
    a = ax[1, 0]
    yrs = ["FY24", "FY25", "FY26"]; loss = [1059.7, 812.3, 517.2]
    b = a.bar(yrs, loss, color=C[3]); a.bar_label(b, labels=[f"₹{v:,.0f} Cr" for v in loss], padding=3, fontsize=9)
    a.set_ylim(0, 1250); a.set_title("Net loss: shrinking while revenue grows\n(the non-exponential constraint: capital)", fontsize=10)
    a = ax[1, 1]
    lab = ["Oct 2022", "Jul 2025", "latest\n(undated blog)"]; pts = [580, 3300, 5900]
    a.semilogy(range(3), pts, "o-", color=C[2], lw=2)
    for i, v in enumerate(pts): a.annotate(f"{v:,}{'+' if i else ''}", (i, v), (i, v*1.35), ha="center", fontsize=9)
    a.set_xticks(range(3)); a.set_xticklabels(lab, fontsize=8.5); a.set_ylim(300, 15000); a.set_title("Ather Grid fast-charging points\n(~10× in about three years)", fontsize=10)
    fig.tight_layout(); save(fig, "E8-fig1-evidence.png")

def fig_scorecard():
    ds = ["1 Digitized", "2 Deceptive", "3 Disruptive", "4 Dematerialized", "5 Demonetized", "6 Democratized"]
    lvl = [3, 3, 2, 1, 2, 2]
    tag = ["Leveraged: the scooter is a connected software product", "Leveraged: the slow 2013–2018 phase is behind it",
           "Partly: wins inside e-2W (17.4%), not yet vs. petrol overall", "Not yet: the vehicle stays physical, only some functions fold in",
           "Partly: battery cost curve helps; vehicle price still ≫ 0", "Partly: Rizta/EL platform, new regions; mass market still ahead"]
    col = {3: C[2], 2: C[3], 1: C[1]}
    fig, a = plt.subplots(figsize=(10.5, 4.3)); a.grid(False)
    for i, (d, l, t) in enumerate(zip(ds, lvl, tag)):
        y = len(ds)-1-i
        a.barh(y, 3, color="#eeeeee", edgecolor="none"); a.barh(y, l, color=col[l]); a.text(3.08, y, t, va="center", fontsize=9)
    a.set_yticks(range(len(ds))); a.set_yticklabels(ds[::-1]); a.set_xlim(0, 7.8); a.set_xticks([0.5, 1.5, 2.5]); a.set_xticklabels(["not yet", "partly", "leveraged"], fontsize=9)
    a.spines["left"].set_visible(False); a.spines["bottom"].set_visible(False); a.tick_params(length=0)
    a.set_title("Ather Energy on the 6 Ds — author's scoring from the evidence in the note", fontsize=11)
    fig.tight_layout(); save(fig, "E8-fig2-six-ds-scorecard.png")

def fig_system():
    fig, a = plt.subplots(figsize=(11.5, 5.2)); a.set_xlim(0, 12); a.set_ylim(0, 6); a.axis("off")
    def box(x, y, w, h, title, body, c):
        a.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05,rounding_size=0.15", fc=c, ec="#444", alpha=.9))
        a.text(x+w/2, y+h-.28, title, ha="center", va="top", fontweight="bold", fontsize=10); a.text(x+w/2, y+h-.75, body, ha="center", va="top", fontsize=8.3)
    box(.2, 1.6, 2.4, 2.8, "USER", "urban commuter,\nfamily rider (Rizta),\nperformance rider;\nexpanding from the\nsouth to middle India", "#dbe9f6")
    box(3.3, 1.6, 2.6, 2.8, "PRODUCT / SERVICE", "scooter + battery + BMS\ntouchscreen dashboard\nAther app, OTA updates\nAtherStack Pro\nEL platform → more models", "#fde8cc")
    box(6.6, 1.6, 2.6, 2.8, "INFRASTRUCTURE\n/ PARTNERS", "Ather Grid fast chargers\nLECCS-compatible network\nHosur plants, Bidkin plant\ncell & component suppliers\nexperience centres, service", "#dcefd8")
    box(9.7, 1.6, 2.2, 2.8, "VALUE / REVENUE", "vehicle sales\nAtherStack Pro subscription\nspares, accessories,\ncharging (≈12% non-vehicle\nin Q2 FY26)", "#eadcf3")
    for x0, x1 in ((2.6, 3.3), (5.9, 6.6), (9.2, 9.7)):
        a.add_patch(FancyArrowPatch((x0, 3.0), (x1, 3.0), arrowstyle="-|>", mutation_scale=16, color="#333", lw=1.6))
    a.add_patch(FancyArrowPatch((10.8, 1.55), (4.6, 1.55), connectionstyle="arc3,rad=-0.25", arrowstyle="-|>", mutation_scale=16, color=C[1], lw=1.5))
    a.text(7.7, .35, "learning loop (Wright): volume → cheaper cells & better yields → lower price → more users;\ndata loop (Kryder/Metcalfe): ride + battery data → better BMS, range estimates, OTA features, charger siting", ha="center", fontsize=8.6, color=C[1])
    a.add_patch(FancyArrowPatch((7.9, 4.5), (4.6, 4.5), connectionstyle="arc3,rad=0.25", arrowstyle="<|-|>", mutation_scale=14, color=C[2], lw=1.5))
    a.text(6.25, 5.35, "network effect (Metcalfe): more chargers ↔ more riders ↔ more charger investment", ha="center", fontsize=8.6, color=C[2])
    a.set_title("Ather as a system: user → product/service → infrastructure/partners → value/revenue", fontsize=11, pad=2)
    fig.tight_layout(); save(fig, "E8-fig3-system-map.png")

if __name__ == "__main__":
    fig_evidence(); fig_scorecard(); fig_system()
