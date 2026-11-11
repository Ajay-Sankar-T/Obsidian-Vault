"""Shared style for the Physics I figures. Every ph_fig_*.py script imports this and saves into ../assets/PH-<name>.png."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.normpath(os.path.join(HERE, "..", "assets"))
os.makedirs(ASSETS, exist_ok=True)

BLUE, ORANGE, GREEN, RED, PURPLE, GREY, TEAL, GOLD = "#2b6cb0", "#dd6b20", "#2f855a", "#c53030", "#6b46c1", "#718096", "#2c7a7b", "#b7791f"
INK = "#1a202c"

plt.rcParams.update({
    "figure.dpi": 150, "savefig.dpi": 150, "font.size": 10, "axes.titlesize": 11, "axes.labelsize": 10,
    "axes.spines.top": False, "axes.spines.right": False, "axes.edgecolor": "#4a5568", "axes.linewidth": 1.1,
    "axes.grid": True, "grid.color": "#e2e8f0", "grid.linewidth": 0.8, "axes.axisbelow": True,
    "font.family": "DejaVu Sans", "mathtext.fontset": "dejavusans", "legend.frameon": False,
    "axes.prop_cycle": matplotlib.cycler(color=[BLUE, ORANGE, GREEN, RED, PURPLE, TEAL]),
})


def save(fig, name):
    path = os.path.join(ASSETS, "PH-%s.png" % name)
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", os.path.basename(path))


def arrow(ax, x0, y0, x1, y1, color=INK, lw=2, style="-|>", ms=14, **kw):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0), arrowprops=dict(arrowstyle=style, color=color, lw=lw, mutation_scale=ms, shrinkA=0, shrinkB=0, **kw))


def blank(ax, lim=None, equal=True):
    """axes for pure diagrams: no spines, ticks or grid"""
    ax.set_axis_off()
    if equal:
        ax.set_aspect("equal")
    if lim:
        ax.set_xlim(lim[0], lim[1]); ax.set_ylim(lim[2], lim[3])
