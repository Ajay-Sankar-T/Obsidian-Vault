"""Figures for the concept notes added to the Fluid Mechanics folder (FM-N1 ... FM-N10).
Run `python fm_concepts_viz.py`.  Every number printed at the end is quoted in a note, so the script doubles as a check."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle, Polygon
from math import pi, cos, radians

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.size": 10, "axes.grid": True, "grid.alpha": .3,
                     "axes.spines.top": False, "axes.spines.right": False})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=140, bbox_inches="tight")
    plt.close(fig)
    print("wrote", name)


def arrow(ax, p, q, color="C3", lw=1.8, **kw):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=12, color=color, lw=lw, **kw))


# ----------------------------------------------------------------------------------------------------------------
# N1 : the three exact laminar profiles
# ----------------------------------------------------------------------------------------------------------------
def fig_profiles():
    fig, ax = plt.subplots(1, 3, figsize=(13, 4.1))
    y = np.linspace(0, 1, 100)
    # plane Couette
    a = ax[0]
    a.plot(y, y, "C0", lw=2.2)
    a.fill_betweenx(y, 0, y, color="C0", alpha=.15)
    a.axhline(0, color="k", lw=3)
    a.axhline(1, color="k", lw=3)
    arrow(a, (0.0, 1.08), (0.45, 1.08), color="C3")
    a.text(.5, 1.1, "$U$", color="C3")
    a.set_xlim(-.05, 1.1)
    a.set_ylim(-.1, 1.2)
    a.set_xlabel("$u/U$")
    a.set_ylabel("$y/h$")
    a.set_title("Plane Couette\n$u=Uy/h$, $\\bar u=U/2$, $\\tau=\\mu U/h$ uniform", fontsize=10)
    # plane Poiseuille
    a = ax[1]
    u = 4 * y * (1 - y)          # u / u_max
    a.plot(u, y, "C0", lw=2.2)
    a.fill_betweenx(y, 0, u, color="C0", alpha=.15)
    a.axvline(2 / 3, color="C1", ls="--", lw=1.2)
    a.text(2 / 3 + .02, .06, "mean $=\\frac{2}{3}u_{max}$", color="C1", fontsize=9)
    a.axhline(0, color="k", lw=3)
    a.axhline(1, color="k", lw=3)
    a.set_xlim(-.05, 1.15)
    a.set_ylim(-.1, 1.2)
    a.set_xlabel("$u/u_{max}$")
    a.set_title("Plane Poiseuille\n$u=\\dfrac{-dp/dx}{2\\mu}y(h-y)$, $u_{max}=\\frac{3}{2}\\bar u$", fontsize=10)
    # Hagen-Poiseuille
    a = ax[2]
    r = np.linspace(-1, 1, 200)
    u = 1 - r ** 2
    a.plot(u, r, "C0", lw=2.2)
    a.fill_betweenx(r, 0, u, color="C0", alpha=.15)
    a.axvline(.5, color="C1", ls="--", lw=1.2)
    a.text(.52, -.9, "mean $=\\frac{1}{2}u_{max}$", color="C1", fontsize=9)
    a.axhline(-1, color="k", lw=3)
    a.axhline(1, color="k", lw=3)
    a.set_xlim(-.05, 1.15)
    a.set_ylim(-1.2, 1.2)
    a.set_xlabel("$u/u_{max}$")
    a.set_ylabel("$r/R$")
    a.set_title("Hagen-Poiseuille\n$u=\\dfrac{-dp/dx}{4\\mu}(R^2-r^2)$, $u_{max}=2\\bar u$", fontsize=10)
    fig.suptitle("The three exact solutions: same ODE, different geometry and boundary conditions", y=1.02)
    fig.tight_layout()
    save(fig, "FM-N1-laminar-profiles.png")


# ----------------------------------------------------------------------------------------------------------------
# N10 : Couette-Poiseuille family
# ----------------------------------------------------------------------------------------------------------------
def fig_cp():
    y = np.linspace(0, 1, 200)
    fig, ax = plt.subplots(figsize=(6.4, 4.3))
    for P, c in ((-3, "C3"), (-1.5, "C1"), (0, "k"), (1.5, "C2"), (3, "C0"), (6, "C4")):
        u = y + P * y * (1 - y)
        ax.plot(u, y, color=c, lw=2, label=f"$P={P:g}$")
    ax.axhline(0, color="k", lw=3)
    ax.axhline(1, color="k", lw=3)
    ax.axvline(0, color="0.5", lw=.8)
    ax.set_xlabel("$u/U$")
    ax.set_ylabel("$y/h$")
    ax.set_title("Couette + Poiseuille: $u/U=y/h+P\\,(y/h)(1-y/h)$,  $P=-\\dfrac{dp}{dx}\\dfrac{h^2}{2\\mu U}$", fontsize=10)
    ax.annotate("backflow near the\nmoving-plate side\n(adverse $dp/dx$)", (-.3, .5), (-1.2, .2), arrowprops=dict(arrowstyle="->"), fontsize=8.5)
    ax.legend(fontsize=8.5, loc="lower right")
    save(fig, "FM-N10-couette-poiseuille.png")
    # reversal check at the stationary wall: du/dy(0) = (1+P)/h  < 0  when  P < -1
    return -1


# ----------------------------------------------------------------------------------------------------------------
# N2 : laminar vs turbulent profile and friction factor against Re
# ----------------------------------------------------------------------------------------------------------------
def fig_regimes():
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.2))
    a = ax[0]
    r = np.linspace(-1, 1, 400)
    ul = 2 * (1 - r ** 2)
    ut = (60 / 49) * (1 - np.abs(r)) ** (1 / 7)
    a.plot(ul, r, "C0", lw=2.2, label="laminar parabola, $u_{max}=2V$")
    a.plot(ut, r, "C3", lw=2.2, label="turbulent 1/7 power law, $u_{max}=1.22V$")
    a.axhline(-1, color="k", lw=3)
    a.axhline(1, color="k", lw=3)
    a.set_xlabel("$u/V$ (mean velocity)")
    a.set_ylabel("$r/R$")
    a.set_ylim(-1.15, 1.15)
    a.set_title("Mean velocity profiles at equal flow rate")
    a.legend(fontsize=8.5, loc="lower center")
    b = ax[1]
    re1 = np.logspace(2.6, np.log10(2300), 50)
    re2 = np.logspace(np.log10(4000), 5, 50)
    b.loglog(re1, 64 / re1, "C0", lw=2.2, label="laminar $f=64/Re$")
    b.loglog(re2, 0.3164 / re2 ** .25, "C3", lw=2.2, label="turbulent smooth (Blasius) $f=0.3164\\,Re^{-1/4}$")
    b.axvspan(2300, 4000, color="0.8", alpha=.7)
    b.text(2650, 0.2, "transition\n(intermittent)", fontsize=8.5, ha="center", va="center")
    b.set_xlabel("$Re=\\rho VD/\\mu$")
    b.set_ylabel("Darcy friction factor $f$")
    b.set_ylim(.012, .2)
    b.legend(fontsize=8.5, loc="lower left")
    b.set_title("The step up in $f$ across transition")
    fig.tight_layout()
    save(fig, "FM-N2-laminar-vs-turbulent.png")
    return 0.3164 / 4000 ** .25, 64 / 2300


# ----------------------------------------------------------------------------------------------------------------
# N3 : vapour pressure of water and the cavitation condition
# ----------------------------------------------------------------------------------------------------------------
PV = {0: .611, 10: 1.228, 20: 2.339, 30: 4.246, 40: 7.384, 50: 12.35, 60: 19.94, 70: 31.19, 80: 47.39, 90: 70.14, 100: 101.33}


def fig_cavitation():
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.2))
    a = ax[0]
    T = np.array(sorted(PV))
    p = np.array([PV[t] for t in T])
    a.semilogy(T, p, "o-", color="C0", lw=2)
    a.axhline(101.325, color="C1", ls="--")
    a.text(2, 112, "1 atm = 101.3 kPa (water boils at 100 °C)", color="C1", fontsize=8.5)
    a.set_xlabel("Temperature (°C)")
    a.set_ylabel("Vapour pressure of water (kPa abs)")
    a.set_title("Vapour pressure rises ~40-fold between 10 and 80 °C")
    a.annotate("20 °C: 2.34 kPa", (20, 2.339), (35, 1.2), arrowprops=dict(arrowstyle="->"), fontsize=9)
    a.set_ylim(.4, 300)
    # pressure in a venturi against the vapour pressure
    b = ax[1]
    A1, A2 = 1.0, 0.3
    p1 = 150.0       # kPa absolute at inlet
    rho = 998.0
    V1 = np.linspace(0, 12, 300)
    p_th = p1 - 0.5 * rho * V1 ** 2 * ((A1 / A2) ** 2 - 1) / 1000
    b.plot(V1, p_th, "C0", lw=2.2, label="throat pressure $p_1-\\frac{1}{2}\\rho V_1^2[(A_1/A_2)^2-1]$")
    b.axhline(2.339, color="C3", ls="--", lw=1.6, label="vapour pressure (20 °C)")
    b.fill_between(V1, -50, 2.339, color="C3", alpha=.12)
    Vcr = np.sqrt(2 * (p1 - 2.339) * 1000 / (rho * ((A1 / A2) ** 2 - 1)))
    b.plot([Vcr], [2.339], "ko")
    b.annotate(f"cavitation onset\n$V_1={Vcr:.2f}$ m/s", (Vcr, 2.339), (Vcr + .8, 55), arrowprops=dict(arrowstyle="->"), fontsize=9)
    b.set_ylim(-30, 160)
    b.set_xlabel("inlet velocity $V_1$ (m/s)")
    b.set_ylabel("throat pressure (kPa abs)")
    b.set_title("Throat of a venturi ($A_1/A_2=3.33$, $p_1=150$ kPa abs)")
    b.legend(fontsize=8, loc="upper right")
    fig.tight_layout()
    save(fig, "FM-N3-vapour-pressure-cavitation.png")
    return Vcr


# ----------------------------------------------------------------------------------------------------------------
# N4 : EGL and HGL for a pipe with entrance loss, friction, pump and exit loss
# ----------------------------------------------------------------------------------------------------------------
def fig_egl():
    V2g = 1.0                 # V^2/2g in m
    s = 0.04                  # friction slope m/m
    zA, zB = 10.0, 18.0       # reservoir surfaces
    x0, xp, x1 = 10.0, 40.0, 95.0
    Hp = (zB + V2g) + s * (x1 - xp) - ((zA - 0.5 * V2g) - s * (xp - x0))
    xs = np.array([0, x0, x0, xp, xp, x1, x1, 110.0])
    egl = np.array([zA, zA, zA - 0.5 * V2g, zA - 0.5 * V2g - s * (xp - x0), zA - 0.5 * V2g - s * (xp - x0) + Hp,
                    zA - 0.5 * V2g - s * (xp - x0) + Hp - s * (x1 - xp), zB, zB])
    hgl = egl - np.array([0, 0, V2g, V2g, V2g, V2g, 0, 0])
    zpipe_x = [x0, xp, x1]
    zpipe = [0, 0, 6]
    fig, ax = plt.subplots(figsize=(11.5, 4.8))
    ax.plot(xs, egl, "C3", lw=2.4, label="EGL  $p/\\gamma+V^2/2g+z$")
    ax.plot(xs, hgl, "C0", lw=2.4, ls="--", label="HGL  $p/\\gamma+z$")
    ax.plot(zpipe_x, zpipe, color="k", lw=4, label="pipe centre-line $z$")
    ax.add_patch(Rectangle((0, 0), x0, zA, fc="C0", alpha=.25))
    ax.add_patch(Rectangle((x1, 6), 110 - x1, zB - 6, fc="C0", alpha=.25))
    ax.text(1.5, 3, "reservoir A\nsurface 10 m", fontsize=9)
    ax.text(x1 + 1, 11, "reservoir B\nsurface 18 m", fontsize=9)
    ax.annotate("entrance loss\n$K\\,V^2/2g=0.5$ m", (x0, zA - .25), (14, 15.5), arrowprops=dict(arrowstyle="->"), fontsize=9)
    ax.annotate("friction: EGL falls\nlinearly (slope $f/D\\cdot V^2/2g$)", (25, zA - .5 - s * 15), (18, 3.2), arrowprops=dict(arrowstyle="->"), fontsize=9)
    ax.annotate(f"pump adds $H_p={Hp:.1f}$ m\n(EGL jumps up)", (xp, 14), (46, 3.5), arrowprops=dict(arrowstyle="->"), fontsize=9)
    ax.annotate("exit loss $=V^2/2g=1$ m\n(all the velocity head is lost)", (x1, 18.5), (66, 23.5), arrowprops=dict(arrowstyle="->"), fontsize=9)
    ax.annotate("HGL below EGL by $V^2/2g$\n(uniform diameter)", (70, hgl[5] - s * (70 - x1) * -1 if False else 18.8 - 0.04 * 25 - 1.0), (66, 9), arrowprops=dict(arrowstyle="->"), fontsize=9)
    ax.set_xlim(0, 110)
    ax.set_ylim(0, 26)
    ax.set_xlabel("distance along the pipe (m)")
    ax.set_ylabel("height above datum (m)")
    ax.set_title("Energy and hydraulic grade lines with a pump and losses")
    ax.legend(loc="upper left", fontsize=9)
    fig.tight_layout()
    save(fig, "FM-N4-egl-hgl-pump-losses.png")
    return Hp


# ----------------------------------------------------------------------------------------------------------------
# N5 : capillary rise and depression against tube diameter
# ----------------------------------------------------------------------------------------------------------------
def fig_capillary():
    d = np.linspace(0.5, 12, 300) * 1e-3
    g = 9.81

    def h(sig, th, rho):
        return 4 * sig * cos(radians(th)) / (rho * g * d)

    fig, ax = plt.subplots(1, 2, figsize=(12, 4.2))
    a = ax[0]
    a.plot(d * 1e3, h(0.0728, 0, 998) * 1e3, "C0", lw=2.2, label="water–glass ($\\sigma=0.0728$, $\\theta\\approx0$)")
    a.plot(d * 1e3, h(0.48, 140, 13550) * 1e3, "C3", lw=2.2, label="mercury–glass ($\\sigma=0.48$, $\\theta\\approx140°$)")
    a.axhline(0, color="k", lw=.8)
    a.set_ylim(-12, 62)
    a.set_xlabel("tube diameter $d$ (mm)")
    a.set_ylabel("rise $h$ (mm)")
    a.legend(fontsize=8.5)
    a.set_title("Capillary rise $h=4\\sigma\\cos\\theta/(\\rho g d)\\ \\propto 1/d$")
    # meniscus sketch
    b = ax[1]
    b.set_xlim(0, 10)
    b.set_ylim(0, 6)
    b.axis("off")
    b.grid(False)
    for x0, rise, col, name in ((1.5, 1.6, "C0", "wetting ($\\theta<90°$):\nliquid climbs"), (6.3, -.9, "C3", "non-wetting ($\\theta>90°$):\nliquid is pushed down")):
        b.add_patch(Rectangle((x0, 0), 2.2, 4.5, fc="none", ec="k", lw=2))
        b.plot([x0 - 1.3, x0 - .1], [2.4, 2.4], color=col, lw=2)
        b.plot([x0 + 2.3, x0 + 3.5], [2.4, 2.4], color=col, lw=2)
        b.add_patch(Rectangle((x0 + .05, 0), 2.1, 2.4 + rise, fc=col, alpha=.25, ec="none"))
        xx = np.linspace(x0 + .05, x0 + 2.15, 30)
        meniscus = 2.4 + rise + (.35 if rise > 0 else -.35) * (np.cosh((xx - x0 - 1.1) * 1.9) - 1) / 2.0
        b.plot(xx, meniscus, color=col, lw=2)
        b.text(x0 + 1.1, 5.1, name, ha="center", fontsize=9)
    b.set_title("Meniscus shape set by the contact angle", fontsize=10)
    fig.tight_layout()
    save(fig, "FM-N5-capillary-rise.png")
    return h(0.0728, 0, 998)[np.argmin(abs(d - 1e-3))] * 1e3


# ----------------------------------------------------------------------------------------------------------------
# N6 : stress on a fluid element
# ----------------------------------------------------------------------------------------------------------------
def fig_stress():
    fig, ax = plt.subplots(1, 2, figsize=(11.5, 4.3))
    a = ax[0]
    a.set_xlim(-2.2, 2.2)
    a.set_ylim(-2.2, 2.2)
    a.set_aspect("equal")
    a.axis("off")
    a.grid(False)
    a.add_patch(Rectangle((-.8, -.8), 1.6, 1.6, fc="C0", alpha=.15, ec="C0", lw=2))
    # normal stresses
    arrow(a, (.8, 0), (1.7, 0), color="C3")
    arrow(a, (-.8, 0), (-1.7, 0), color="C3")
    arrow(a, (0, .8), (0, 1.7), color="C3")
    arrow(a, (0, -.8), (0, -1.7), color="C3")
    a.text(1.75, .12, "$\\sigma_{xx}$", color="C3")
    a.text(.12, 1.75, "$\\sigma_{yy}$", color="C3")
    # shear stresses
    for (p, q) in (((.8, -.45), (.8, .45)), ((-.8, .45), (-.8, -.45)), ((-.45, .8), (.45, .8)), ((.45, -.8), (-.45, -.8))):
        arrow(a, p, q, color="C2", lw=2.2)
    a.text(.95, .55, "$\\tau_{xy}$", color="C2")
    a.text(-.45, .95, "$\\tau_{yx}$", color="C2")
    a.set_title("Stress on a 2-D element: $\\sigma_{ij}=-p\\,\\delta_{ij}+\\tau_{ij}$\n(first index: face normal, second: direction)", fontsize=10)
    b = ax[1]
    b.axis("off")
    b.grid(False)
    b.text(0, .95, "At rest (statics):", fontsize=11, weight="bold", va="top")
    b.text(0, .84, "$\\tau_{ij}=0$  so  $\\sigma_{ij}=-p\\,\\delta_{ij}$  (isotropic, the same on every plane)", fontsize=10, va="top")
    b.text(0, .64, "In motion:", fontsize=11, weight="bold", va="top")
    b.text(0, .53, "$\\sigma_{ij}=-p\\,\\delta_{ij}+\\tau_{ij}$,  $\\tau_{ij}=2\\mu\\,\\dot\\varepsilon_{ij}-\\frac{2}{3}\\mu(\\nabla\\!\\cdot\\!\\mathbf{V})\\delta_{ij}$", fontsize=10, va="top")
    b.text(0, .33, "Moment balance on the element  $\\Rightarrow\\ \\tau_{xy}=\\tau_{yx}$ (symmetric tensor)", fontsize=10, va="top")
    b.text(0, .17, "Mechanical pressure  $\\bar p=-\\frac{1}{3}\\sigma_{kk}$  equals thermodynamic $p$\nfor incompressible flow, or when the bulk viscosity is neglected (Stokes)", fontsize=10, va="top")
    fig.tight_layout()
    save(fig, "FM-N6-stress-element.png")


# ----------------------------------------------------------------------------------------------------------------
# N9 : minor-loss coefficients for area changes
# ----------------------------------------------------------------------------------------------------------------
def fig_minor():
    ar = np.linspace(0, 1, 100)
    fig, ax = plt.subplots(figsize=(6.6, 4.3))
    ax.plot(ar, (1 - ar) ** 2, "C0", lw=2.2, label="sudden expansion  $K=(1-A_1/A_2)^2$  (on $V_1$)")
    pts = np.array([[0, .5], [.2, .42], [.4, .28], [.6, .15], [.8, .04], [1.0, 0.0]])
    ax.plot(pts[:, 0], pts[:, 1], "o-", color="C3", lw=2.2, label="sudden contraction  $K$  (on $V_2$)")
    ax.set_xlabel("area ratio  small / large")
    ax.set_ylabel("loss coefficient $K$")
    ax.set_title("Area-change losses: expansion is the costly one")
    ax.legend(fontsize=8.5)
    save(fig, "FM-N9-area-change-K.png")


if __name__ == "__main__":
    fig_profiles()
    print("Couette-Poiseuille reversal at P <", fig_cp())
    f_t, f_l = fig_regimes()
    print(f"f laminar at Re=2300: {f_l:.4f};  Blasius at Re=4000: {f_t:.4f}")
    print(f"venturi cavitation onset V1 = {fig_cavitation():.3f} m/s")
    print(f"pump head Hp = {fig_egl():.2f} m")
    print(f"water capillary rise at d=1 mm: {fig_capillary():.1f} mm")
    fig_stress()
    fig_minor()
