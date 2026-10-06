"""Figures for the three Fluid Mechanics formula banks.  Run `python fm_viz.py` (runs the checks first)."""
import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyArrowPatch, Rectangle
from math import *
import fm_core

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets"); os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.size": 10, "axes.grid": True, "grid.alpha": .3, "axes.spines.top": False, "axes.spines.right": False})
def save(fig, name): fig.savefig(os.path.join(OUT, name), dpi=140, bbox_inches="tight"); plt.close(fig); print("wrote", name)

# ---------------------------------------------------------------------------------------------------------------------
# D1 : Reynolds and Froude cannot both be matched in a scale model (eqs 5.31-5.35)
# ---------------------------------------------------------------------------------------------------------------------
def fig_scaling():
    al = np.logspace(-3, 0, 200); fig, ax = plt.subplots(1, 2, figsize=(10.5, 4.2))
    a = ax[0]; a.loglog(al, al**1.5, "C0", lw=2, label=r"required $\nu_m/\nu_p=\alpha^{3/2}$  (Re and Fr both matched)")
    for nu, nm, c in ((1.0, "same fluid (water in water)", "C3"), (0.115, "mercury model, water prototype", "C1")):
        a.axhline(nu, color=c, ls="--", lw=1.3); a.text(1.2e-3, nu*1.12, nm+f"  ($\\nu_m/\\nu_p$={nu:g})", color=c, fontsize=8.5)
    a.plot(0.1, 0.1**1.5, "ko"); a.annotate("1:10 model needs\n$\\nu_m/\\nu_p$ = 0.032", (0.1, 0.0316), (0.0022, 0.0024), arrowprops=dict(arrowstyle="->"), fontsize=9)
    a.set_xlabel(r"length ratio  $\alpha=L_m/L_p$"); a.set_ylabel(r"kinematic-viscosity ratio $\nu_m/\nu_p$"); a.set_ylim(5e-5, 3); a.legend(loc="lower right", fontsize=8)
    a.set_title("Re + Fr matching is impossible with ordinary fluids")
    b = ax[1]; al_ = np.array([.02, .05, .1, .2, .5, 1]); b.loglog(al_, al_**.5, "o-", label=r"$V_m/V_p=T_m/T_p=\alpha^{1/2}$"); b.loglog(al_, al_**2.5, "s-", label=r"$Q_m/Q_p=\alpha^{5/2}$")
    b.loglog(al_, al_**3, "^-", label=r"$F_m/F_p=\alpha^{3}$ (same $\rho$)"); b.set_xlabel(r"length ratio $\alpha$"); b.set_ylabel("model / prototype"); b.legend(fontsize=8.5); b.set_title("Froude-scaling laws (same fluid)")
    fig.tight_layout(); save(fig, "FM-D1-scaling.png")

# ---------------------------------------------------------------------------------------------------------------------
# K1 : the four elementary motions of a fluid element;  K2 : shear flow = rotation + pure strain
# ---------------------------------------------------------------------------------------------------------------------
def advect(corners, Lmat, shift, tt, n=1):
    from scipy.linalg import expm
    return (expm(Lmat*tt)@corners.T).T+shift*tt
SQ = np.array([[-.5, -.5], [.5, -.5], [.5, .5], [-.5, .5]])
def draw_el(ax, c0, c1, title, eq, note):
    ax.add_patch(Polygon(c0, closed=True, fc="none", ec="0.55", ls="--", lw=1.4)); ax.add_patch(Polygon(c1, closed=True, fc="C0", alpha=.35, ec="C0", lw=2))
    ax.set_xlim(-1.4, 1.9); ax.set_ylim(-1.2, 1.2); ax.set_aspect("equal"); ax.set_title(title, fontsize=10); ax.set_xticks([]); ax.set_yticks([]); ax.grid(False)
    ax.text(0.5, -0.07, eq, transform=ax.transAxes, ha="center", va="top", fontsize=9); ax.text(0.5, -0.22, note, transform=ax.transAxes, ha="center", va="top", fontsize=8.5, color="0.3")
def fig_elements():
    fig, ax = plt.subplots(1, 4, figsize=(14, 4.3)); Z = np.zeros((2, 2))
    draw_el(ax[0], SQ, advect(SQ, Z, np.array([1.0, 0.25]), 1), "Translation", r"$\mathbf{V}=(U,V)$", "element moves,\nshape and orientation fixed")
    draw_el(ax[1], SQ, advect(SQ, np.array([[0, -1.], [1., 0]]), np.zeros(2), 0.6), "Rotation", r"$\omega_z=\frac{1}{2}\left(\partial_x v-\partial_y u\right)$", "solid-body turn,\nno deformation")
    draw_el(ax[2], SQ, advect(SQ, np.array([[.7, 0], [0, -.7]]), np.zeros(2), .6), "Linear deformation", r"$\varepsilon_{xx}=\partial_x u,\ \varepsilon_{yy}=\partial_y v$", "stretch in x, squeeze in y;\narea changes by $\\nabla\\!\\cdot\\!\\mathbf{V}$ (here 0)")
    draw_el(ax[3], SQ, advect(SQ, np.array([[0, .7], [.7, 0]]), np.zeros(2), .6), "Angular deformation", r"$\dot\gamma_{xy}=\partial_x v+\partial_y u$", "right angle closes;\nno net rotation of the axes")
    fig.suptitle("Motion of a fluid element: dashed = at t, filled = at t + dt (exaggerated)", y=1.0, fontsize=11); fig.tight_layout(); save(fig, "FM-K1-element-motion.png")
def fig_shear():
    fig, ax = plt.subplots(1, 3, figsize=(12.5, 3.9)); g = 1.0; tt = .5
    L = np.array([[0, g], [0, 0]]); Om = .5*(L-L.T); S = .5*(L+L.T)
    draw_el(ax[0], SQ, advect(SQ, L, np.zeros(2), tt), "Simple shear  $u=\\dot\\gamma y$", r"$\nabla\mathbf{V}=\mathbf{S}+\mathbf{R}$", "")
    draw_el(ax[1], SQ, advect(SQ, Om, np.zeros(2), tt), "rotation part", r"$\omega_z=-\dot\gamma/2$ (clockwise)", "")
    draw_el(ax[2], SQ, advect(SQ, S, np.zeros(2), tt), "pure-strain part", r"$\dot\varepsilon_{xy}=\dot\gamma/2$, principal axes at 45°", "")
    ax[0].text(0.5, -0.20, "vorticity $\\zeta_z=-\\dot\\gamma$,  shear-strain rate $=\\dot\\gamma$", transform=ax[0].transAxes, ha="center", fontsize=9, color="0.3")
    fig.suptitle("A shear flow is rotational: it contains a rotation AND a deformation", y=1.0); fig.tight_layout(); save(fig, "FM-K2-shear-decomposition.png")

# ---------------------------------------------------------------------------------------------------------------------
# K3 : vortices - solid-body, free (irrotational) and Rankine
# ---------------------------------------------------------------------------------------------------------------------
def fig_vortices():
    Om, Rc = 1.0, 1.0; r = np.linspace(1e-3, 3.2, 600); G = 2*pi*Om*Rc**2
    vs, vf = Om*r, G/(2*pi*r); vr = np.where(r < Rc, Om*r, G/(2*pi*r))
    zr = np.where(r < Rc, 2*Om, 0.); Gs = 2*pi*r*vs; Gf = np.full_like(r, G); Gr = 2*pi*r*vr
    fig, ax = plt.subplots(1, 3, figsize=(13.5, 3.9))
    ax[0].plot(r, vs, "C1", label="solid-body  $v_\\theta=\\Omega r$"); ax[0].plot(r, vf, "C2", label="free vortex  $v_\\theta=\\Gamma/2\\pi r$"); ax[0].plot(r, vr, "k", lw=2.2, label="Rankine (core $R_c$)")
    ax[0].set_ylim(0, 3); ax[0].set_xlabel("$r/R_c$"); ax[0].set_ylabel("$v_\\theta/(\\Omega R_c)$"); ax[0].legend(fontsize=8); ax[0].set_title("velocity")
    ax[1].plot(r, np.full_like(r, 2*Om), "C1"); ax[1].plot(r, np.zeros_like(r), "C2"); ax[1].plot(r, zr, "k", lw=2.2); ax[1].set_ylim(-.3, 2.6)
    ax[1].set_xlabel("$r/R_c$"); ax[1].set_ylabel("vorticity $\\zeta_z/\\Omega$"); ax[1].set_title("vorticity:  $\\zeta=\\frac{1}{r}\\,d(rv_\\theta)/dr$"); ax[1].text(1.4, 0.25, "irrotational", color="C2"); ax[1].text(.05, 2.1, "$\\zeta=2\\Omega$", color="C1")
    ax[2].plot(r, Gs/G, "C1"); ax[2].plot(r, Gf/G, "C2"); ax[2].plot(r, Gr/G, "k", lw=2.2); ax[2].set_xlabel("$r/R_c$"); ax[2].set_ylabel("circulation $\\Gamma(r)/\\Gamma_\\infty$"); ax[2].set_title("circulation around circle of radius r"); ax[2].set_ylim(0, 4.5)
    ax[2].text(1.6, 1.12, "free vortex: $\\Gamma$ = const\n(all vorticity at the axis)", color="C2", fontsize=8.5)
    fig.tight_layout(); save(fig, "FM-K3-vortices.png")

# ---------------------------------------------------------------------------------------------------------------------
# K4 : Problem 4.59, V = x i - y j : a fluid element deforms but stays rectangular, area conserved
# ---------------------------------------------------------------------------------------------------------------------
def fig_p459():
    fig, ax = plt.subplots(figsize=(6.2, 5.6)); xs = np.linspace(.25, 5.5, 200)
    for c in (1, 2, 3, 4, 6, 9, 12, 16): ax.plot(xs, c/xs, color="0.8", lw=1)
    el0 = np.array([[2, 2], [3, 2], [3, 3], [2, 3]], float); e = exp(.5); el1 = el0*np.array([e, 1/e])
    ax.add_patch(Polygon(el0, closed=True, fc="C0", alpha=.35, ec="C0", lw=2, label="t = 0 (1 × 1, area 1)")); ax.add_patch(Polygon(el1, closed=True, fc="C3", alpha=.35, ec="C3", lw=2, label="t = 0.5 (1.65 × 0.61, area 1)"))
    for i in range(4): ax.add_patch(FancyArrowPatch(el0[i], el1[i], arrowstyle="->", mutation_scale=12, color="0.35"))
    ax.set_xlim(0, 5.5); ax.set_ylim(0, 3.8); ax.set_aspect("equal"); ax.set_xlabel("x"); ax.set_ylabel("y"); ax.legend(loc="upper right", fontsize=8.5)
    ax.set_title("P4.59   $\\mathbf{V} = x\\,\\mathbf{i} - y\\,\\mathbf{j}$:  grey = streamlines  $xy$ = const"); fig.tight_layout(); save(fig, "FM-K4-p459-element.png")

# ---------------------------------------------------------------------------------------------------------------------
# B1 : Pitot-static tube schematic with the pressures along the stagnation streamline
# ---------------------------------------------------------------------------------------------------------------------
from fm_pitot import fig_pitot

# ---------------------------------------------------------------------------------------------------------------------
# B2 : venturi (FE3.9) - velocity, pressure, EGL, HGL
# ---------------------------------------------------------------------------------------------------------------------
def fig_venturi():
    D1, D2, Q = .06, .03, 155*fm_core.GAL; p1 = 120e3; rho = fm_core.RHO_W
    xs = np.linspace(0, 1, 400); Dx = np.where(xs < .25, D1, np.where(xs < .45, D1+(D2-D1)*(xs-.25)/.2, np.where(xs < .6, D2, np.where(xs < .9, D2+(D1-D2)*(xs-.6)/.3, D1))))
    V = Q/(pi*Dx**2/4); p = p1-0.5*rho*(V**2-V[0]**2); p0 = p1+0.5*rho*V[0]**2; head = lambda q: q/(rho*fm_core.G)
    fig, ax = plt.subplots(2, 1, figsize=(8.6, 6.2), sharex=True, gridspec_kw=dict(height_ratios=[1, 1.6]))
    ax[0].fill_between(xs, -Dx*500, Dx*500, color="C0", alpha=.25); ax[0].plot(xs, Dx*500, "C0"); ax[0].plot(xs, -Dx*500, "C0"); ax[0].set_ylabel("pipe (mm radius)"); ax[0].set_ylim(-35, 35); ax[0].set_title("Venturi (FE3.9):  6 cm -> 3 cm, 155 gal/min of water, $p_1$ = 120 kPa")
    ax[1].plot(xs, head(p0+0*xs), "C3", lw=2, label="EGL = $p_0/\\rho g$ (constant, no loss)"); ax[1].plot(xs, head(p)+0*xs, "C0", lw=2, label="HGL = $p/\\rho g$ (+z, z=0)")
    ax[1].set_ylabel("head, m of water"); ax[1].set_xlabel("distance along the venturi (arbitrary)"); ax[1].legend(loc="lower left", fontsize=8.5)
    th = np.searchsorted(xs, .5); ax[1].annotate(f"throat: V = {V[th]:.2f} m/s\np = {p[th]/1e3:.1f} kPa", (xs[th], head(p[th])), (.62, head(p[th])+2.2), arrowprops=dict(arrowstyle="->"), fontsize=9)
    ax[1].text(.02, head(p[0])+1.0, f"V = {V[0]:.2f} m/s", fontsize=9); ax[1].text(.02, head(p0)+.6, "$V^2/2g$ gap shrinks where the tube widens", fontsize=8, color="0.35")
    fig.tight_layout(); save(fig, "FM-B2-venturi-EGL-HGL.png")

# ---------------------------------------------------------------------------------------------------------------------
# B3 : specific-energy curve  -> two alternate depths (hydraulic-drop problem)
# ---------------------------------------------------------------------------------------------------------------------
def fig_alternate():
    q = 3.0*1.5; E = 1.5+9/(2*9.81)+4.0; h = np.linspace(.15, 7, 500); Es = h+q**2/(2*9.81*h**2)
    r = fm_core.check()["roots"]; fig, ax = plt.subplots(figsize=(6.6, 4.6))
    ax.plot(Es, h, "C0", lw=2); ax.axvline(E, color="C3", ls="--"); ax.text(E-2.3, 6.5, f"E = {E:.2f} m", color="C3")
    for rr in r: ax.plot(E, rr, "ko"); ax.annotate(f"h2 = {rr:.2f} m\nV2 = {q/rr:.2f} m/s", (E, rr), (E+1.3, rr+(.2 if rr > 1 else -.2)), arrowprops=dict(arrowstyle="->"), fontsize=9)
    hc = (q**2/9.81)**(1/3); ax.plot(1.5*hc, hc, "g^"); ax.annotate("critical depth\n(Fr = 1)", (1.5*hc, hc), (2.0, 2.9), arrowprops=dict(arrowstyle="->"), color="g", fontsize=9)
    ax.set_xlim(0, 10); ax.set_ylim(0, 7); ax.set_xlabel("specific energy  $E = h + V^2/2g$  (m)"); ax.set_ylabel("depth h (m)"); ax.set_title("Bernoulli + continuity for open-channel flow:\nsame E, two possible depths ($q=V_1h_1=4.5$ m²/s)")
    fig.tight_layout(); save(fig, "FM-B3-alternate-depths.png")

# ---------------------------------------------------------------------------------------------------------------------
# B4 : Pitot compressibility correction
# ---------------------------------------------------------------------------------------------------------------------
def fig_pitot_comp():
    Ma = np.linspace(0.001, 1.0, 300); k = 1.4; q = 0.5*k*Ma**2
    ratio = (fm_core.isentropic_p0_over_p(Ma)-1)/q          # (p0-p)/(1/2 rho V^2)
    fig, ax = plt.subplots(figsize=(6.4, 4.2)); ax.plot(Ma, ratio, "C3", lw=2, label="isentropic: $(p_0-p)/\\frac{1}{2}\\rho V^2$"); ax.plot(Ma, 1+Ma**2/4, "C0--", label="series  $1+Ma^2/4$"); ax.axhline(1, color="k", lw=1, label="incompressible Bernoulli")
    ax.axvline(.3, color="0.5", ls=":"); ax.text(.31, 1.02, "Ma = 0.3\n(+2.3 %)", fontsize=8.5); ax.set_xlabel("Mach number"); ax.set_ylabel("measured $(p_0-p)$ / incompressible $\\frac{1}{2}\\rho V^2$"); ax.legend(fontsize=8.5); ax.set_title("Why Pitot readings need a correction at high speed")
    fig.tight_layout(); save(fig, "FM-B4-pitot-compressibility.png")

if __name__ == "__main__":
    fm_core.check()
    for f in (fig_scaling, fig_elements, fig_shear, fig_vortices, fig_p459, fig_pitot, fig_venturi, fig_alternate, fig_pitot_comp): f()
