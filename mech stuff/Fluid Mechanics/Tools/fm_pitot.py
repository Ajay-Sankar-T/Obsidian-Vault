"""Pitot-static tube schematic (FM-B1)."""
import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")

def fig_pitot():
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(10.5, 6.8), gridspec_kw=dict(height_ratios=[2.3, 1]))
    ax.set_xlim(0, 11.5); ax.set_ylim(-0.3, 4.8); ax.axis("off")
    # probe: thin tube with a hemispherical-ish nose, total-head hole in the nose, static ports on the side
    ax.add_patch(Polygon([[3.2, 1.55], [7.4, 1.55], [7.4, 0.95], [3.2, 0.95]], closed=True, fc="0.88", ec="k"))
    ax.add_patch(Polygon([[2.5, 1.25], [3.2, 1.55], [3.2, 0.95]], closed=True, fc="0.88", ec="k"))
    ax.plot([2.5, 7.4], [1.25, 1.25], "k:", lw=.8)
    for xx in (4.4, 4.6):
        ax.plot(xx, 1.55, "ko", ms=3.5); ax.plot(xx, 0.95, "ko", ms=3.5)
    for yy in (0.1, 0.55, 1.95, 2.4):
        ax.annotate("", (2.1, yy), (0.4, yy), arrowprops=dict(arrowstyle="->", color="C0"))
    ax.annotate("", (2.5, 1.25), (0.4, 1.25), arrowprops=dict(arrowstyle="->", color="C0", lw=2.4))
    ax.text(0.4, 2.85, "free stream  $V,\\ p_s$", color="C0", fontsize=11)
    ax.annotate("total-head hole\n(stagnation point)\n$p_0$, $V=0$", (2.5, 1.25), (1.0, 3.7), arrowprops=dict(arrowstyle="->"), fontsize=9.5)
    ax.annotate("static ports, wall tangent\nto the flow: they sense $p_s$", (4.5, 1.55), (4.0, 3.3), arrowprops=dict(arrowstyle="->"), fontsize=9.5)
    # the two pressures go to a U-tube differential manometer
    ax.plot([7.4, 8.1, 8.1], [1.25, 1.25, 2.4], "k", lw=1.2); ax.plot([7.4, 9.3, 9.3], [1.55, 1.55, 2.4], "k", lw=1.2)
    ax.add_patch(Rectangle((8.0, 2.4), .2, 1.3, fc="w", ec="k")); ax.add_patch(Rectangle((9.2, 2.4), .2, 1.3, fc="w", ec="k"))
    ax.add_patch(Rectangle((8.0, 2.4), .2, .5, fc="C0", alpha=.5, lw=0)); ax.add_patch(Rectangle((9.2, 2.4), .2, 1.0, fc="C0", alpha=.5, lw=0))
    ax.plot([8.1, 9.3], [2.4, 2.4], "k", lw=.8)
    ax.annotate("", (9.65, 3.4), (9.65, 2.9), arrowprops=dict(arrowstyle="<->")); ax.text(9.8, 3.05, "$h$", fontsize=11)
    ax.text(7.6, 4.2, "differential manometer:  $p_0-p_s=(\\gamma_m-\\gamma)\\,h$", fontsize=9.5)
    ax.text(5.7, 4.65, "$V=\\sqrt{2\\,(p_0-p_s)/\\rho}$   (Bernoulli along the stagnation streamline)", ha="center", fontsize=11.5, bbox=dict(fc="#fff3cd", ec="0.6"))
    ax.set_title("Pitot-static tube", fontsize=12, pad=26)
    # schematic pressure along the stagnation streamline (V falls to zero at the nose)
    s_ = np.linspace(0, 1, 300); Vr = np.tanh(3.2*(1-s_)); pr = 1+.5*(1-Vr**2)
    bx.plot(s_, pr, "C3", lw=2.4); bx.axhline(1, color="C0", ls="--", lw=1); bx.axhline(1.5, color="C3", ls="--", lw=1)
    bx.text(.01, 1.03, "$p_s$ (free stream)", color="C0", fontsize=9)
    bx.text(.01, 1.47, "$p_0=p_s+\\frac{1}{2}\\rho V^2$ at the stagnation point", color="C3", fontsize=9, va="top")
    bx.set_xlabel("position along the stagnation streamline, approaching the nose (schematic)"); bx.set_ylabel("pressure")
    bx.set_yticks([]); bx.set_xticks([]); bx.set_ylim(.9, 1.6)
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "FM-B1-pitot-static.png"), dpi=140, bbox_inches="tight"); plt.close(fig); print("wrote FM-B1-pitot-static.png")

if __name__ == "__main__":
    fig_pitot()
