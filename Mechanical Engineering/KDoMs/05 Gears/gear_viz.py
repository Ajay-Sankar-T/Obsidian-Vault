"""Regenerates every figure used in 'Gear Formula Bank.md'  (python gear_viz.py [fig1 fig5 ... | anim])
Outputs go to ./assets  (Obsidian resolves ![[GFB-...png]] by file name)."""
import sys, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc, FancyArrowPatch, Polygon, Rectangle
from math import *
from gear_core import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
os.makedirs(OUT, exist_ok=True)
B, O, G, K, R = "#1f77b4", "#e8590c", "#7a7a7a", "#111111", "#d6204a"
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})

def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=110, bbox_inches="tight", facecolor="white")
    plt.close(fig); print("wrote", name)

def circ(ax, c, r, **kw):
    kw.setdefault("fill", False); ax.add_patch(Circle(c, r, **kw))

def dim(ax, p, q, text, off=(0, 0), color=K, fs=9, both=True):
    ax.annotate("", xy=q, xytext=p, arrowprops=dict(arrowstyle="<->" if both else "->", color=color, lw=1))
    ax.text((p[0]+q[0])/2+off[0], (p[1]+q[1])/2+off[1], text, color=color, fontsize=fs, ha="center", va="center",
            bbox=dict(fc="white", ec="none", pad=1))

def angle_arc(ax, c, r, t0, t1, text, rt=None, color=K):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=degrees(t0), theta2=degrees(t1), color=color, lw=1.2))
    tm = (t0+t1)/2; rt = rt or r*1.35
    ax.text(c[0]+rt*cos(tm), c[1]+rt*sin(tm), text, color=color, ha="center", va="center", fontsize=10)

# ------------------------------------------------------------------ fig1: terminology (rack + mating tooth)
def fig1():
    m, a_, al = 4.0, 4.0, radians(20); b_ = 1.25*m; p = pi*m; t = tan(al)
    fig, ax = plt.subplots(figsize=(9.5, 6.2))
    def tooth(xc, up):
        pts = [(xc-(p/4+b_*t), -b_), (xc-(p/4-a_*t), a_), (xc+(p/4-a_*t), a_), (xc+(p/4+b_*t), -b_)]
        return [(x, up*y) for x, y in pts]
    rack = []
    for k in range(-1, 3): rack += tooth(k*p, 1)
    ax.add_patch(Polygon(rack + [(2.6*p, -b_-3), (-1.7*p, -b_-3)], closed=True, fc="#cfe3f5", ec=B, lw=1.6))
    ax.add_patch(Polygon(tooth(p/2, -1), closed=True, fc="#fbd9c4", ec=O, lw=1.6, alpha=.92))
    ax.axhline(0, color=G, ls="-.", lw=1); ax.text(-1.65*p, -1.6, "pitch line", color=G, fontsize=9)
    ax.axhline(a_, color=B, ls=":", lw=.8); ax.axhline(-b_, color=B, ls=":", lw=.8); ax.axhline(-a_, color=O, ls=":", lw=.8)
    xr = 2.15*p
    dim(ax, (xr, 0), (xr, a_), "a = m", (2.4, 0), B); dim(ax, (xr, 0), (xr, -b_), "b = 1.25 m", (3.4, 0), B)
    dim(ax, (xr+4.8, -a_), (xr+4.8, -b_), "c = b − a = 0.25 m", (5.8, 0), R)
    y_p = -b_-6.3
    ax.annotate("", xy=(0, y_p), xytext=(p, y_p), arrowprops=dict(arrowstyle="<->", lw=1.1)); ax.text(p/2, y_p-1.6, "p = πm  (circular pitch)", ha="center")
    ax.plot([0, 0], [-b_-3, y_p], color=G, lw=.6, ls=":"); ax.plot([p, p], [-b_-3, y_p], color=G, lw=.6, ls=":")
    yt = a_+4.2
    ax.annotate("", xy=(-p/4, yt), xytext=(p/4, yt), arrowprops=dict(arrowstyle="<->", lw=1)); ax.text(0, yt+1.3, "tooth\np/2", ha="center", fontsize=9)
    ax.annotate("", xy=(p/4, yt), xytext=(3*p/4, yt), arrowprops=dict(arrowstyle="<->", lw=1)); ax.text(p/2, yt+1.3, "space\np/2", ha="center", fontsize=9)
    xp = p/4
    ax.plot([xp, xp], [-4.2, 4.2], color=K, lw=.8, ls="--")
    ax.add_patch(Arc((xp, 0), 6, 6, theta1=90-degrees(al), theta2=90, color=R, lw=1.4)); ax.text(xp+1.3, 3.6, "α", color=R, fontsize=11)
    ax.text(-1.0*p, a_+1.6, "rack tooth", color=B, ha="center"); ax.text(1.35*p, -a_-1.5, "mating tooth tip", color=O, ha="center", fontsize=9)
    ax.set_title("Rack tooth (blue) and mating tooth (orange): full-depth 20° system", fontsize=11, weight="bold", pad=14)
    ax.text(0.5*p, y_p-4.2, "m = d_p / N     P = N / d_p = 1/m     p·P = π", ha="center", color=K, fontsize=10.5)
    ax.set_xlim(-1.75*p, 3.0*p); ax.set_ylim(y_p-6, yt+4.6); ax.set_aspect("equal"); ax.axis("off"); save(fig, "GFB-fig1-terminology.png")

# ------------------------------------------------------------------ fig2: involute generation + properties
def fig2():
    rb = 1.0; al = radians(52)                    # tan(al) = psi (delta = 0)
    psi = tan(al)
    u = np.linspace(0, 2.4, 300)
    X = rb*(np.cos(u)+u*np.sin(u)); Y = rb*(np.sin(u)-u*np.cos(u))
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(11.5, 5.2), gridspec_kw=dict(width_ratios=[1.15, 1]))
    circ(ax, (0, 0), rb, ec=B, lw=1.6); ax.plot(X, Y, color=O, lw=2)
    for uu in (0.4, 0.8, 1.2, 1.6, 2.0):          # taut string snapshots
        T = rb*np.array([cos(uu), sin(uu)]); Q = T + rb*uu*np.array([sin(uu), -cos(uu)])
        ax.plot([T[0], Q[0]], [T[1], Q[1]], color=G, lw=.7)
    T = rb*np.array([cos(psi), sin(psi)]); Q = T + rb*psi*np.array([sin(psi), -cos(psi)])
    ax.plot([T[0], Q[0]], [T[1], Q[1]], color=K, lw=2); ax.plot(*Q, "o", color=R, ms=7); ax.plot(*T, "o", color=K, ms=5); ax.plot(0, 0, "ko", ms=4)
    ax.plot([0, Q[0]], [0, Q[1]], color=R, lw=1.3); ax.plot([0, 1], [0, 0], color=G, lw=1); ax.plot([0, T[0]], [0, T[1]], color=G, lw=.8, ls="--")
    ax.text(*(Q+np.array([.06, -.1])), "Q", color=R, fontsize=12); ax.text(T[0]-.12, T[1]+.1, "T", fontsize=11)
    ax.text(.5*(T[0]+Q[0])+.08, .5*(T[1]+Q[1])+.08, "ρ = r_b tan α\n= r_b(ψ+δ)", fontsize=9)
    angle_arc(ax, (0, 0), .28, 0, psi-atan(psi), "θ", .4, R)
    angle_arc(ax, (0, 0), .55, psi-atan(psi), psi, "α", .66, K)
    ax.text(.55, -.16, "r_b", color=B); ax.text(.35, .98, "ψ+δ", fontsize=9, color=G)
    ax.text(Q[0]/2-.45, Q[1]/2+.05, "r = r_b / cos α", color=R, rotation=degrees(atan2(Q[1], Q[0])), fontsize=9)
    ax.set_aspect("equal"); ax.set_xlim(-1.3, 3.4); ax.set_ylim(-1.4, 3.2); ax.axis("off")
    ax.set_title("Involute: path of a point on a taut string unwrapped from the base circle", fontsize=10)
    # right: inv(alpha) and r/rb plotted
    al_ = np.radians(np.linspace(0, 60, 200))
    bx.plot(np.degrees(al_), np.tan(al_)-al_, color=O, lw=2, label="inv α = tan α − α   (polar angle θ of Q)")
    bx.plot(np.degrees(al_), 1/np.cos(al_)-1, color=B, lw=2, label="r/r_b − 1 = 1/cos α − 1")
    for d in (14.5, 20, 25):
        bx.plot(d, tan(radians(d))-radians(d), "o", color=R); bx.annotate(f"inv {d}° = {inv(radians(d)):.5f}", (d, inv(radians(d))), ({14.5: 3, 20: 11, 25: 19}[d], {14.5: .3, 20: .2, 25: .1}[d] + .0), fontsize=8.5, arrowprops=dict(arrowstyle="-", color=G))
    bx.set_xlabel("pressure angle α at the point (°)"); bx.legend(fontsize=8.5, loc="upper left"); bx.grid(alpha=.3)
    bx.set_title("Involute function and radius growth", fontsize=10); save(fig, "GFB-fig2-involute.png")

# ------------------------------------------------------------------ fig3: fundamental law of gearing
def fig3():
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(12, 5.2), gridspec_kw=dict(width_ratios=[1, 1.1]))
    O2, O3, P = np.array([0., 0.]), np.array([6., 0.]), np.array([3.4, 0.])
    Q = np.array([2.7, 1.9]); n = (Q-P)/np.linalg.norm(Q-P)
    ax.plot([O2[0], O3[0]], [0, 0], color=G, lw=1, ls="-."); L = P + n*np.dot(O2-P, n)*1; Lf = P + n*np.dot(O2-P, n); Mf = P + n*np.dot(O3-P, n)
    ax.plot(*zip(P-3.2*n, P+4.2*n), color=K, lw=1.8); ax.text(*(P-3.2*n+np.array([.1, -.3])), "n", fontsize=11); ax.text(*(P+4.2*n+np.array([.05, .1])), "n", fontsize=11)
    ax.plot([O2[0], Lf[0]], [O2[1], Lf[1]], color=B, lw=1, ls="--"); ax.plot([O3[0], Mf[0]], [O3[1], Mf[1]], color=O, lw=1, ls="--")
    for pt, nm, c in ((O2, "O₂", B), (O3, "O₃", O), (P, "P", R), (Q, "Q", K), (Lf, "L", B), (Mf, "M", O)): ax.plot(*pt, "o", color=c, ms=5); ax.text(pt[0]+.1, pt[1]-.35 if nm in "O₂O₃P" else pt[1]+.12, nm, color=c, fontsize=11)
    w2 = 1.0; O2P, O3P = np.linalg.norm(P-O2), np.linalg.norm(P-O3); w3 = w2*O2P/O3P
    perp = lambda v: np.array([-v[1], v[0]])
    v2 = w2*perp(Q-O2); v3 = -w3*perp(Q-O3); s = .55
    ax.annotate("", xy=Q+s*v2, xytext=Q, arrowprops=dict(arrowstyle="->", color=B, lw=2)); ax.annotate("", xy=Q+s*v3, xytext=Q, arrowprops=dict(arrowstyle="->", color=O, lw=2))
    ax.text(*(Q+s*v2+np.array([-.1, .15])), "V_Q2 = ω₂·O₂Q", color=B, fontsize=9, ha="right"); ax.text(*(Q+s*v3+np.array([.15, .0])), "V_Q3 = ω₃·O₃Q", color=O, fontsize=9)
    for v, c in ((v2, B), (v3, O)):
        proj = Q + s*np.dot(v, n)*n; ax.plot([Q[0]+s*v[0], proj[0]], [Q[1]+s*v[1], proj[1]], color=c, lw=.8, ls=":")
    ax.text(2.0, -1.5, "V_Q2 cosφ = V_Q3 cosφ  (no relative motion along n–n)\nω₂/ω₃ = O₃Q cosφ / O₂Q cosφ = O₃M/O₂L = O₃P/O₂P", fontsize=9.5, ha="center")
    ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-3, 8.5); ax.set_ylim(-2.2, 5.4); ax.set_title("Fundamental law: common normal must cut O₂O₃ at a fixed P", fontsize=10)
    # (b) belt analogue
    r1, r2, Cc = 1.6, 2.4, 6.0; O1 = np.array([0., 0.]); O2b = np.array([Cc, 0.]); Pp = np.array([Cc*r1/(r1+r2), 0.])
    beta = asin(r1/np.linalg.norm(Pp-O1)); d = np.array([cos(beta), sin(beta)])
    A = Pp + d*np.dot(O1-Pp, d); Bp = Pp + d*np.dot(O2b-Pp, d)
    circ(bx, O1, r1, ec=B, lw=1.6); circ(bx, O2b, r2, ec=O, lw=1.6)
    circ(bx, O1, r1, ec=B, lw=0); bx.plot(*zip(A, Bp), color=K, lw=2); bx.plot([-.5, 6.5], [0, 0], color=G, ls="-.", lw=1)
    bx.plot(*A, "o", color=B, ms=5); bx.plot(*Bp, "o", color=O, ms=5); bx.plot(*Pp, "o", color=R, ms=6)
    for pt, nm, dxy in ((A, "A", (-.35, -.2)), (Bp, "B", (.15, .1)), (Pp, "P", (.1, -.45)), (O1, "O₁", (-.1, -.4)), (O2b, "O₂", (.0, -.4))): bx.text(pt[0]+dxy[0], pt[1]+dxy[1], nm, fontsize=11)
    def invol(Oc, rb, T0, sgn, uu):             # involute through the point at string length rb*uu from T0, free end toward sgn*(CCW tangent)
        th0 = atan2(T0[1]-Oc[1], T0[0]-Oc[0]); u = np.linspace(0, uu, 120)
        th = th0 + sgn*(uu-u)
        T = np.c_[Oc[0]+rb*np.cos(th), Oc[1]+rb*np.sin(th)]
        return T + (rb*u)[:, None]*sgn*np.c_[-np.sin(th), np.cos(th)]
    tA = np.array([-sin(atan2(A[1], A[0])), cos(atan2(A[1], A[0]))])
    sg = 1 if np.dot(tA, d) > 0 else -1
    Qs = Pp + d*0.5*np.linalg.norm(Bp-Pp)*0.5
    uA = np.linalg.norm(Qs-A)/r1; uB = np.linalg.norm(Bp-Qs)/r2
    c1 = invol(O1, r1, A, sg, uA); tB = np.array([-sin(atan2(Bp[1]-O2b[1], Bp[0]-O2b[0])), cos(atan2(Bp[1]-O2b[1], Bp[0]-O2b[0]))])
    sg2 = 1 if np.dot(tB, -d) > 0 else -1; c2 = invol(O2b, r2, Bp, sg2, uB)
    bx.plot(c1[:, 0], c1[:, 1], color=B, lw=2.2); bx.plot(c2[:, 0], c2[:, 1], color=O, lw=2.2); bx.plot(*Qs, "o", color=K, ms=6); bx.text(Qs[0]+.1, Qs[1]+.15, "Q", fontsize=11)
    bx.text(3.2, -3.6, "ω₁/ω₂ = r_b2 / r_b1 = r_p2 / r_p1   (9.4, 9.5)\nholds even if the centre distance changes", ha="center", fontsize=9.5)
    bx.text(1.1, 2.75, "line of action AB\n(common normal = pressure line)", fontsize=9)
    bx.set_aspect("equal"); bx.axis("off"); bx.set_xlim(-2, 9); bx.set_ylim(-4.0, 3.9); bx.set_title("Belt-and-pulley analogue → two involutes roll on each other", fontsize=10)
    save(fig, "GFB-fig3-fundamental-law.png")

# ------------------------------------------------------------------ mesh geometry shared by fig4 / animation
def mesh(rp1, rp2, ro1, ro2, a):
    C = rp1+rp2; rb1, rb2 = rp1*cos(a), rp2*cos(a)
    P = np.array([rp1, 0.]); d = np.array([sin(a), cos(a)]); n = np.array([cos(a), -sin(a)])
    O1, O2 = np.zeros(2), np.array([C, 0.])
    A = O1 + rb1*n; Bt = O2 - rb2*n
    sP = lambda X: float(np.dot(d, X-P))
    sF = sqrt(ro1**2-rb1**2) + sP(A)                         # distance from O1 foot A to F along d
    E = A + d*(sqrt(ro1**2-rb1**2) - 0) if False else None
    F = A + d*sqrt(ro1**2-rb1**2); Ept = Bt - d*sqrt(ro2**2-rb2**2)
    return dict(C=C, rb1=rb1, rb2=rb2, P=P, d=d, n=n, O1=O1, O2=O2, A=A, B=Bt, E=Ept, F=F)

def fig4():
    rp1, rp2, ro1, ro2, a = 51.5, 64.2, 57.5, 71.2, radians(20)
    g = mesh(rp1, rp2, ro1, ro2, a); Z = path_of_contact(rp1, rp2, ro1, ro2, a); mc = contact_ratio(rp1, rp2, ro1, ro2, a, 20)
    fig, (ax, zx) = plt.subplots(1, 2, figsize=(14, 6.4), gridspec_kw=dict(width_ratios=[1.45, 1]))
    for a_x in (ax, zx):
        for c, r, col, ls in ((g["O1"], rp1, B, "-."), (g["O1"], g["rb1"], B, "--"), (g["O1"], ro1, B, "-"), (g["O2"], rp2, O, "-."), (g["O2"], g["rb2"], O, "--"), (g["O2"], ro2, O, "-")):
            circ(a_x, c, r, ec=col, ls=ls, lw=1.3)
        a_x.plot(*zip(g["A"], g["B"]), color=K, lw=2); a_x.plot([g["O1"][0], g["O2"][0]], [0, 0], color=G, lw=.8, ls="-.")
        a_x.plot(*zip(g["E"], g["F"]), color=R, lw=7, alpha=.5, solid_capstyle="butt")
    big = {"A": (g["A"], (-4, -7)), "B": (g["B"], (3, 3)), "P": (g["P"], (1.5, -7)), "E": (g["E"], (-8, -2)), "F": (g["F"], (2, 2))}
    for k, (pt, off) in big.items():
        ax.plot(*pt, "o", color=R if k in "EF" else K, ms=5); ax.text(pt[0]+off[0], pt[1]+off[1], k, fontsize=11, weight="bold")
    zoff = {"A": (-1.5, -2.6), "B": (.8, .8), "P": (1, -3), "E": (-3, -.5), "F": (1, .5)}
    for k, (pt, _) in big.items():
        zx.plot(*pt, "o", color=R if k in "EF" else K, ms=7); zx.text(pt[0]+zoff[k][0], pt[1]+zoff[k][1], k, fontsize=13, weight="bold")
    ax.plot(*g["O1"], "ko", ms=4); ax.plot(*g["O2"], "ko", ms=4); ax.text(-6, -9, "O₁", fontsize=11); ax.text(g["O2"][0]+1, -9, "O₂", fontsize=11)
    ax.text(-58, 68, "blue gear 1:  r_p=51.5   r_b=48.39   r_o=57.5\norange gear 2:  r_p=64.2   r_b=60.33   r_o=71.2", fontsize=9, va="top")
    ax.add_patch(Rectangle((30, -24), 46, 54, fill=False, ec=G, ls=":")); ax.text(30, 33, "zoom →", fontsize=9, color=G)
    ax.set_aspect("equal"); ax.set_xlim(-62, 190); ax.set_ylim(-70, 78); ax.axis("off")
    zx.set_xlim(30, 76); zx.set_ylim(-24, 30); zx.set_aspect("equal"); zx.axis("off")
    zx.text(31, 28, "E → P : approach    P → F : recess\nred band = length of action EF", fontsize=9, color=R, va="top")
    fig.text(.5, .02, f"EF = √(r_o1²−r_b1²) + √(r_o2²−r_b2²) − C sinα = {Z:.1f} mm      m_c = EF / (2π r_b2 / N₂) = {mc:.2f}      p_b = {2*pi*g['rb2']/20:.2f} mm      (Problem 9.1: 29.3 mm, 1.55)", ha="center", fontsize=10.5, bbox=dict(fc="#fff6f7", ec=R))
    fig.suptitle("Path of contact and contact ratio   (dashed: base circles · dash-dot: pitch circles · solid: addendum circles)", fontsize=10.5)
    save(fig, "GFB-fig4-contact-ratio.png")

# ------------------------------------------------------------------ fig5: interference / minimum teeth
def fig5():
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(11.5, 4.8))
    lam = np.linspace(0.01, 1, 300)
    for f, ls in ((1.0, "-"), (0.8, "--")):
        for al, c in ((14.5, G), (20, B), (25, O)):
            ax.plot(lam, [n1min(l, f, radians(al)) for l in lam], ls=ls, color=c, lw=1.8, label=f"α={al}°, f={f}")
    ax.plot(16/18, n1min(16/18, 1, radians(14.5)), "o", color=R); ax.annotate("Problem 9.3\n22.94 → 23", (16/18, 22.94), (.45, 14.5), fontsize=9, arrowprops=dict(arrowstyle="->"))
    ax.plot(0, n1min_rack(1, radians(20)), "o", color=R); ax.text(.02, 15.2, "rack, 20°: 17.1 (P9.4)", fontsize=8.5, color=R)
    ax.set_xlabel("speed ratio λ = ω₂/ω₁ = N₁/N₂  (pinion = gear 1)"); ax.set_ylabel("N₁,min (pinion teeth)"); ax.grid(alpha=.3); ax.legend(fontsize=7.5, ncol=2)
    ax.set_title("Minimum pinion teeth before interference starts   (9.17)", fontsize=10); ax.set_ylim(0, 40)
    al = np.linspace(12, 30, 200)
    bx.plot(al, [n1min_rack(1, radians(x)) for x in al], color=B, lw=2, label="pinion vs rack  2f/sin²α  (f=1)")
    bx.plot(al, [n1min(1, 1, radians(x)) for x in al], color=O, lw=2, label="equal gears  λ=1,  f=1")
    bx.plot(al, [n1min_rack(.8, radians(x)) for x in al], color=B, lw=1.5, ls="--", label="rack, stub f=0.8")
    for x in (14.5, 20, 25): bx.axvline(x, color=G, lw=.6, ls=":")
    bx.set_xticks([12, 14.5, 17.5, 20, 22.5, 25, 27.5, 30])
    for x in (14.5, 20, 25): bx.plot(x, n1min_rack(1, radians(x)), "o", color=B, ms=4); bx.text(x+.3, n1min_rack(1, radians(x))+1, f"{n1min_rack(1, radians(x)):.1f}", fontsize=8, color=B)
    bx.set_xlabel("pressure angle α (°)"); bx.set_ylabel("N₁,min"); bx.grid(alpha=.3); bx.legend(fontsize=8); bx.set_title("Larger α or shorter addendum → fewer teeth possible", fontsize=10)
    save(fig, "GFB-fig5-min-teeth.png")

# ------------------------------------------------------------------ fig6: interference geometry (pinion tip vs tangent points)
def fig6():
    fig, axs = plt.subplots(1, 3, figsize=(15, 5.2))
    a = radians(20); rp = 1.0
    for ax, N, title in zip(axs, (7, 12.32, 20), ("N = 7  < N_min  → interference", "N = N_min = 12.32  → interference just starts", "N = 20  → no interference")):
        m = 2*rp/N; ro = rp+m; g = mesh(rp, rp, ro, ro, a)
        for c, r, col, ls in ((g["O1"], rp, B, "-."), (g["O1"], g["rb1"], B, "--"), (g["O1"], ro, B, "-"), (g["O2"], rp, O, "-."), (g["O2"], g["rb2"], O, "--"), (g["O2"], ro, O, "-")): circ(ax, c, r, ec=col, ls=ls, lw=1.2)
        ax.plot(*zip(g["A"]-g["d"]*.25, g["B"]+g["d"]*.25), color=K, lw=1.4)
        ax.plot(*g["A"], "s", color=K, ms=6); ax.plot(*g["B"], "s", color=K, ms=6)
        ax.text(g["A"][0]+.04, g["A"][1]-.12, "A", fontsize=11, weight="bold"); ax.text(g["B"][0]-.1, g["B"][1]+.06, "B", fontsize=11, weight="bold")
        ax.plot(*g["P"], "o", color=R, ms=5); ax.text(g["P"][0]+.05, g["P"][1]-.12, "P", color=R)
        sE = np.dot(g["E"]-g["A"], g["d"]); sF = np.dot(g["F"]-g["B"], g["d"])
        okE, okF = sE >= -1e-6, sF <= 1e-6
        for pt, nm, ok in ((g["E"], "E", okE), (g["F"], "F", okF)):
            ax.plot(*pt, "o", color=(B if ok else R), ms=8, zorder=5); ax.text(pt[0]-.1 if nm == "E" else pt[0]+.05, pt[1]+(-.12 if nm == "E" else .06), nm, color=(B if ok else R), fontsize=12, weight="bold")
        if not okE: ax.plot(*zip(g["A"], g["E"]), color=R, lw=6, alpha=.55)
        if not okF: ax.plot(*zip(g["B"], g["F"]), color=R, lw=6, alpha=.55)
        ax.text(1.0, -.98, "E beyond A, F beyond B → each tip cuts\ninto the non-involute part of the other gear" if not okE else "E and F lie between A and B\n→ contact stays on involute flanks", ha="center", fontsize=9, color=(R if not okE else B))
        ax.set_xlim(.15, 1.85); ax.set_ylim(-1.1, .8); ax.set_aspect("equal"); ax.axis("off"); ax.set_title(title, fontsize=10)
    fig.suptitle("Interference: an addendum circle cuts the pressure line beyond a tangent point (equal gears, f = 1, α = 20°;  A, B = tangent points)", fontsize=10.5, y=1.0)
    save(fig, "GFB-fig6-interference.png")

# ------------------------------------------------------------------ fig7: helical geometry
def fig7():
    p, psi = 10.0, radians(25); b = p/tan(psi)
    fig, ax = plt.subplots(figsize=(9, 6.4))
    W = 3.2*p
    rect = Rectangle((0, 0), W, b, fc="#f4f8fc", ec=G, lw=1.2); ax.add_patch(rect)
    for k in range(-6, 4):
        ln, = ax.plot([k*p, k*p+b*tan(psi)], [0, b], color=B, lw=1.8); ln.set_clip_path(rect)
    ax.annotate("", xy=(p, -1.8), xytext=(2*p, -1.8), arrowprops=dict(arrowstyle="<->", lw=1.2)); ax.text(1.5*p, -3.6, "p  (transverse circular pitch, in the plane of rotation)", ha="center")
    yy = b*0.2; P0 = np.array([p+yy*tan(psi), yy]); nvec = np.array([cos(psi), -sin(psi)]); foot = P0 + nvec*(p*cos(psi))
    ax.plot([P0[0], foot[0]], [P0[1], foot[1]], color=R, lw=2.4); ax.text(foot[0]+.6, foot[1]-.3, "p_n = p cosψ\n(normal pitch)", color=R, fontsize=10)
    ax.plot([0, p], [0, 0], color=O, lw=2.2); ax.plot([p, p], [0, b], color=O, lw=1.2, ls="--")
    ax.plot(0, 0, "o", color=O, ms=5); ax.plot(p, b, "o", color=O, ms=5)
    ax.text(p*0.2, b*0.62, "one tooth runs from\nthis edge...", color=O, fontsize=8.5)
    ax.text(p+.8, b*0.92, "...to here, exactly one pitch p further round", color=O, fontsize=8.5)
    ax.annotate("", xy=(W+1.5, 0), xytext=(W+1.5, b), arrowprops=dict(arrowstyle="<->", color=O, lw=1.6)); ax.text(W+4.5, b/2, "b_min = p / tanψ\n(AGMA: 1.15 × b_min)", rotation=90, va="center", ha="center", color=O, fontsize=10)
    ax.plot([0, 0], [0, b], color=G, lw=1, ls="--"); ax.text(-1.4, b/2, "axis direction", rotation=90, va="center", ha="center", color=G)
    ax.add_patch(Arc((0, 0), 13, 13, theta1=90-degrees(psi), theta2=90, color=R, lw=1.4)); ax.text(2.2, 7.6, "ψ", color=R, fontsize=12)
    ax.set_title("Unrolled pitch cylinder of a helical gear  (ψ = 25°, p = 10)", fontsize=11, weight="bold")
    ax.text(W/2, -8.2, "P_n = P / cosψ        p_n·P_n = π        lead angle = 90° − ψ", ha="center", fontsize=10.5)
    ax.set_xlim(-4, W+9); ax.set_ylim(-10, b+3); ax.set_aspect("equal"); ax.axis("off"); save(fig, "GFB-fig7-helical.png")

# ------------------------------------------------------------------ fig8: spiral gear shaft angle
def fig8():
    fig, axs = plt.subplots(1, 2, figsize=(11.5, 5.4))
    def panel(ax, al_d, be_d, same, title):
        al, be = radians(al_d), radians(be_d)
        rot = lambda v, ang: np.array([v[0]*cos(ang)-v[1]*sin(ang), v[0]*sin(ang)+v[1]*cos(ang)])
        t = np.array([0., 1.]); a1 = rot(t, -al); a2 = rot(t, +be) if same else rot(t, -be); L = 3.4
        ax.plot([0, 0], [-.5, L], color=K, lw=1.4, ls="--"); ax.text(-.15, L*.55, "common tooth direction", ha="right", fontsize=8.5)
        for v, c, nm in ((a1, B, "axis of gear 1"), (a2, O, "axis of gear 2")):
            ax.annotate("", xy=v*L, xytext=-v*.5, arrowprops=dict(arrowstyle="-|>", color=c, lw=2.2))
            ax.text(*(v*(L+.22)+np.array([.5 if c == B else -.5, 0])), nm, color=c, fontsize=10, ha="center", va="bottom")
        ax.plot(0, 0, "o", color=R, ms=6)
        ang = lambda v: atan2(v[1], v[0])
        def arc(r, v1, v2, col, lbl, rt):
            lo, hi = sorted((ang(v1), ang(v2))); ax.add_patch(Arc((0, 0), 2*r, 2*r, theta1=degrees(lo), theta2=degrees(hi), color=col, lw=1.8))
            mid = (lo+hi)/2; ax.text(rt*cos(mid), rt*sin(mid), lbl, color=col, fontsize=12, ha="center", va="center")
        arc(1.3, t, a1, B, "α", 1.6)
        arc(.8 if not same else 1.9, t, a2, O, "β", 1.05 if not same else 2.2)
        arc(2.6, a1, a2, R, "θ", 2.95)
        ax.set_title(title, fontsize=10); ax.set_aspect("equal"); ax.set_xlim(-3.4, 3.8); ax.set_ylim(-.9, 4.3); ax.axis("off")
    panel(axs[0], 25, 15, True, "same hand:   θ = α + β     (25° + 15° = 40°)   (9.40)")
    panel(axs[1], 25, 10, False, "opposite hand:   θ = α − β     (Problem 9.6: 25° − 10° = 15°)   (9.41)")
    save(fig, "GFB-fig8-spiral.png")

# ------------------------------------------------------------------ fig9: worm lead
def fig9():
    fig, axs = plt.subplots(1, 3, figsize=(13, 3.9), sharey=True)
    px = 1.0; Lh = 4.3
    for ax, N1 in zip(axs, (1, 2, 3)):
        l = px*N1; lam = atan(l/ (pi*1.6))
        ax.add_patch(Rectangle((0, 0), 5*px, Lh, fc="#f4f8fc", ec=G))
        # N1 threads, each rising 'l' axially per revolution; draw several revolutions side by side
        for k in range(N1):
            for rev in range(-4, 6):
                y0 = (k/N1)*l + rev*l
                ax.plot([0, 5*px], [y0, y0+ (5*px)*l/ (px*1.0*0+ 5*px) * 0 + 0], color=B, lw=0)
        # simple view: threads as parallel slanted lines. horizontal = along circumference (one rev = 5 px wide), vertical = axial
        slope = l/(5*px)                         # one revolution (width 5px) advances axially by lead l
        for k in range(N1):
            for off in np.arange(-6*l, Lh+l, l):
                y0 = off + k*px
                ax.plot([0, 5*px], [y0, y0+l], color=B if k == 0 else [O, "#2ca02c"][k-1], lw=1.7, clip_on=True)
        ax.set_xlim(0, 5*px); ax.set_ylim(0, Lh)
        x = 4.6; yy = 2.2
        dim(ax, (.15, .15), (.15, .15+px), "p_x", (.42, 0), K, 8.5)
        if N1 > 1: dim(ax, (.15, .15), (.15, .15+l), "", (0, 0), R)
        ax.text(2.5, 3.95, f"N₁ = {N1} thread{'s' if N1>1 else ''}:  l = p_x·N₁ = {N1}·p_x", ha="center", fontsize=10, color=R, bbox=dict(fc="white", ec="none"))
        ax.text(2.5, .2, f"ω₁/ω₂ = N₂/N₁ = N₂/{N1}", ha="center", fontsize=9.5)
        ax.axis("off")
    fig.suptitle("Worm: lead l = axial advance per revolution (unrolled worm cylinder, one revolution = one width).  Right-angle shafts: ω₁/ω₂ = πD_p2 / l", fontsize=10, y=1.02)
    save(fig, "GFB-fig9-worm.png")

# ------------------------------------------------------------------ fig10: epicyclic tabular method as stacked bars
def fig10():
    fig, axs = plt.subplots(1, 2, figsize=(12, 4.6))
    def bars(ax, names, x, ys, res, title, unit):
        i = np.arange(len(names)); w = .35
        ax.bar(i-w/2, x, w, color=B, label="step (i)  all locked to arm:  x"); ax.bar(i+w/2, ys, w, color=O, label="step (ii)  arm fixed:  y·(train ratio)")
        ax.plot(i, res, "D", color=R, ms=8, label="resultant = (i)+(ii)", zorder=5)
        for k, r in enumerate(res): ax.text(k+.42, r+(0.06*np.ptp(np.r_[x, ys, res]) if r >= 0 else -0.06*np.ptp(np.r_[x, ys, res])), f"= {r:g}", ha="left", va="center", color=R, fontsize=9.5, weight="bold", bbox=dict(fc="white", ec="none", pad=1, alpha=.85))
        ax.axhline(0, color=K, lw=.8); ax.set_xticks(i); ax.set_xticklabels(names); ax.set_ylabel(unit); ax.set_title(title, fontsize=10); ax.grid(axis="y", alpha=.3)
    bars(axs[0], ["Arm A", "B", "D", "E"], [1, 1, 1, 1], [0, -1, -50/49, -50/51], [1, 0, round(-1/49, 4), round(1/51, 4)], "Problem 9.7 (Ferguson's paradox): arm 1 CCW, B fixed → x=1, y=−1", "turns")
    bars(axs[1], ["Arm A", "B (input)", "C (fixed)", "F (output)"], [200, 200, 200, 200], [0, 800, -200, -250], [200, 1000, 0, -50], "Problem 9.8: n_B=1000, n_C=0 → x=200, y=800", "rpm")
    h, l = axs[0].get_legend_handles_labels(); fig.legend(h, l, loc="lower center", ncol=3, fontsize=9, bbox_to_anchor=(.5, -.04))
    save(fig, "GFB-fig10-epicyclic-table.png")

# ------------------------------------------------------------------ fig11: analytic conjugate synthesis (9.19-9.35)
def fig11():
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(12.5, 5.2))
    a = radians(20); rp1, rp2 = 1.0, 1.7; C = rp1+rp2; gam = 1+rp1/rp2
    th1 = np.linspace(-0.35, 0.55, 120)
    x1 = rp1*cos(a)*((th1+tan(a))*np.sin(th1+a)+np.cos(th1+a)); y1 = rp1*cos(a)*(np.sin(th1+a)-(th1+tan(a))*np.cos(th1+a))
    th2 = rp1*th1/rp2
    x2 = -rp2*cos(a)*((-th2+tan(a))*np.sin(-th2+a)+np.cos(-th2+a)); y2 = rp2*cos(a)*((-th2+tan(a))*np.cos(-th2+a)-np.sin(-th2+a))
    xt = (x1-C*np.cos(th1))*np.cos(gam*th1)+(y1-C*np.sin(th1))*np.sin(gam*th1); yt = -(x1-C*np.cos(th1))*np.sin(gam*th1)+(y1-C*np.sin(th1))*np.cos(gam*th1)
    ax.plot(x1, y1, color=B, lw=2.6, label="tooth profile of gear 1, (9.30)–(9.31)")
    tt = np.linspace(-.5, .8, 100); ax.plot(rp1*np.cos(tt), rp1*np.sin(tt), color=B, ls="-.", lw=1, label="pitch circle r_p1"); ax.plot(rp1*cos(a)*np.cos(tt), rp1*cos(a)*np.sin(tt), color=B, ls="--", lw=1, label="base circle r_b1 = r_p1 cosα")
    ax.plot(rp1, 0, "o", color=R, ms=6); ax.text(rp1+.02, -.06, "θ₁ = 0:  curve cuts pitch circle on the x₁-axis", color=R, fontsize=8.5)
    ax.set_aspect("equal"); ax.legend(fontsize=8, loc="upper left"); ax.set_title("Constant pressure angle ⇒ ODE (9.29) ⇒ the profile is an involute", fontsize=10)
    ax.set_xlim(.85, 1.5); ax.set_ylim(-.15, .55); ax.set_xlabel("x₁"); ax.set_ylabel("y₁")
    bx.plot(xt, yt, color=O, lw=3, label="gear-1 profile carried into gear-2 axes by (9.22), (9.23)")
    bx.plot(x2, y2, "--", color=K, lw=1.2, label="closed form (9.34), (9.35)  [(9.35) with the corrected sign]")
    tt = np.linspace(pi-.5, pi+.5, 100); bx.plot(rp2*np.cos(tt), rp2*np.sin(tt), color=O, ls="-.", lw=1); bx.plot(rp2*cos(a)*np.cos(tt), rp2*cos(a)*np.sin(tt), color=O, ls="--", lw=1)
    bx.set_aspect("equal"); bx.legend(fontsize=8, loc="lower right"); bx.set_title("Mating profile on gear 2 is also an involute, r_b2 = r_p2 cosα", fontsize=10)
    bx.set_xlim(-1.95, -1.45); bx.set_ylim(-.3, .45); bx.set_xlabel("x₂"); bx.set_ylabel("y₂")
    save(fig, "GFB-fig11-analytic-involute.png")

# ------------------------------------------------------------------ fig12: Problem 9.5 conjugate of a trapezoid (analytic method)
def fig12():
    rp1, rp2 = 12.5, 25.0; C = rp1+rp2; gam = 1+rp1/rp2; k = tan(radians(15))
    xD = rp1*(cos(radians(7.5))+sin(radians(7.5))/tan(radians(15))*1.0)*2*0 + 18.5
    yD = 0.0
    f = lambda x: -k*(x-xD)                                           # flank  y1 = 4.96 - 0.268 x1
    th = np.linspace(-0.55, 0.9, 700); N = []
    for t in th:                                                       # intersection of flank with PN line (9.24)
        # y = -k(x-xD);  y - rp sin t = (1/k)(x - rp cos t)      [slope of PN = -1/f' = 1/k]
        xs = (rp1*np.sin(t) + k*xD*0 - (rp1*np.cos(t))/k + 0) if False else None
        # solve -k x + k xD - rp sin t = (x - rp cos t)/k
        x = (k*xD - rp1*np.sin(t) + rp1*np.cos(t)/k) / (k + 1/k); y = f(x); N.append((x, y, t))
    N = np.array(N); x1, y1, t = N.T
    # keep the point of contact within the flank segment (addendum 1.25 above pitch, dedendum 1.60 below)
    rr = np.hypot(x1, y1); keep = (rr <= rp1+1.25+1e-9) & (rr >= rp1-1.6-1e-9)
    x2 = (x1-C*np.cos(t))*np.cos(gam*t)+(y1-C*np.sin(t))*np.sin(gam*t); y2 = -(x1-C*np.cos(t))*np.sin(gam*t)+(y1-C*np.sin(t))*np.cos(gam*t)
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(12.5, 5.4))
    xx = np.linspace(10.9, 13.75, 2); ax.plot(xx, f(xx), color=B, lw=2.5, label="given flank (trapezoid, ±15°)")
    circ(ax, (0, 0), rp1, ec=B, ls="-.", lw=1); circ(ax, (0, 0), rp1+1.25, ec=B, lw=.8); circ(ax, (0, 0), rp1-1.6, ec=B, lw=.8)
    tt = np.linspace(-.3, .5, 40); 
    for i in range(0, len(t), 140):
        if keep[i]: ax.plot([rp1*cos(t[i]), x1[i]], [rp1*sin(t[i]), y1[i]], color=G, lw=.7, ls=":")
    ax.plot(x1[keep], y1[keep], color=R, lw=1.6, label="point of contact N (line of action in gear-1 axes)")
    ax.set_xlim(9, 15.5); ax.set_ylim(-1, 6); ax.set_aspect("equal"); ax.legend(fontsize=8, loc="upper right"); ax.set_title("Gear 1 (12 teeth, r_p=12.5 cm): given tooth flank and contact points", fontsize=10)
    ax.set_xlabel("x₁ (cm)"); ax.set_ylabel("y₁ (cm)")
    bx.plot(x2[keep], y2[keep], color=O, lw=2.5, label="conjugate flank on gear 2 (24 teeth, r_p=25 cm)")
    circ(bx, (0, 0), rp2, ec=O, ls="-.", lw=1); bx.set_aspect("equal"); bx.legend(fontsize=8, loc="best"); bx.set_title("Mating profile from (9.22), (9.23):  γ = 1 + r_p1/r_p2 = 1.5", fontsize=10)
    bx.set_xlim(x2[keep].min()-2, x2[keep].max()+2); bx.set_ylim(y2[keep].min()-2, y2[keep].max()+2); bx.set_xlabel("x₂ (cm)"); bx.set_ylabel("y₂ (cm)")
    save(fig, "GFB-fig12-problem-9-5.png")

# ------------------------------------------------------------------ fig13: gear tooth outline helper + meshing frame + animation
def gear_poly(N, m, a, ad, de, c0, n_inv=14):
    rp = m*N/2; rb = rp*cos(a); ra = rp+ad*m; rf = rp-de*m
    hb = pi/(2*N)+inv(a)
    def flank(sign, r0):                                   # sign=+1: CCW-side flank, -1: CW-side
        r = np.linspace(max(rb, r0), ra, n_inv); ar = np.arccos(np.clip(rb/r, -1, 1)); th = hb - (np.tan(ar)-ar)
        return sign*th, r
    pts = []
    for k in range(N):
        c = c0 + 2*pi*k/N
        thr, rr = flank(+1, rf); thl, _ = flank(-1, rf)
        right = [(c+t, r) for t, r in zip(thr, rr)]; left = [(c-t, r) for t, r in zip(thl, rr)]
        if rf < rb: right = [(c+hb, rf)] + right; left = [(c-hb, rf)] + left
        tip = [(c+(hb-(tan(acos(rb/ra))-acos(rb/ra)))*s_, ra) for s_ in np.linspace(1, -1, 5)]
        seg = left[::-1] and []  # placeholder
        # order for CCW traversal: root gap start -> CW flank up -> tip arc (CW->CCW) -> CCW flank down
        up = [(c-t_, r_) for t_, r_ in [(t, r) for t, r in zip(thl, rr)]]
        up = [(c-hb+(tan(acos(rb/r))-acos(rb/r)), r) if r >= rb else (c-hb, r) for r in rr]
        if rf < rb: up = [(c-hb, rf)] + up
        dn = [(c+hb-(tan(acos(rb/r))-acos(rb/r)), r) if r >= rb else (c+hb, r) for r in rr][::-1]
        if rf < rb: dn = dn + [(c+hb, rf)]
        nxt = c+2*pi/N-hb
        pts += up + dn + [(c+hb, rf), (nxt, rf)]
    th = np.array([p[0] for p in pts]); r = np.array([p[1] for p in pts])
    return r*np.cos(th), r*np.sin(th)

def frame(ax, N1, N2, m, al, phi1, ad=1.0, de=1.25, annotate=True, colors=(B, O)):
    rp1, rp2 = m*N1/2, m*N2/2; ro1, ro2 = rp1+ad*m, rp2+ad*m; g = mesh(rp1, rp2, ro1, ro2, al)
    x, y = gear_poly(N1, m, al, ad, de, phi1); ax.fill(x, y, fc="#dbe9f6", ec=colors[0], lw=1.2)
    phi2 = -phi1*N1/N2
    x, y = gear_poly(N2, m, al, ad, de, pi+pi/N2+phi2); ax.fill(x+g["C"], y, fc="#fbe0d0", ec=colors[1], lw=1.2)
    ax.plot(*zip(g["A"], g["B"]), color=K, lw=1.2); ax.plot(*zip(g["E"], g["F"]), color=R, lw=4, alpha=.5, solid_capstyle="butt")
    circ(ax, g["O1"], rp1, ec=B, ls="-.", lw=.6); circ(ax, g["O2"], rp2, ec=O, ls="-.", lw=.6)
    # contact points: involute of tooth k starts at gamma0 = c_k + hb;  contact at rho = rb1*(gamma0 + a) along d from A
    hb = pi/(2*N1)+inv(al); cps = []
    rhoE = np.dot(g["E"]-g["A"], g["d"]); rhoF = np.dot(g["F"]-g["A"], g["d"])
    for k in range(N1):
        g0 = (phi1 + 2*pi*k/N1 + hb + al) % (2*pi)
        for gg in (g0, g0-2*pi):
            rho = g["rb1"]*gg
            if rhoE-1e-9 <= rho <= rhoF+1e-9: cps.append(g["A"]+g["d"]*rho)
    for c in cps: ax.plot(*c, "o", color=R, ms=7, zorder=6)
    ax.plot(*g["P"], "k+", ms=8)
    return g, len(cps)

def fig13():
    fig, ax = plt.subplots(figsize=(10, 6.2)); N1, N2, m, al = 20, 30, 10, radians(20)
    g, nc = frame(ax, N1, N2, m, al, 0.0)
    ax.set_aspect("equal"); ax.axis("off"); rp1, rp2 = m*N1/2, m*N2/2
    mc = contact_ratio(rp1, rp2, rp1+m, rp2+m, al, N2)
    ax.set_title(f"Standard 20° full-depth pair N₁=20, N₂=30, m=10 mm :  m_c = {mc:.2f}  (red band = path of contact E→F, dots = contacts)", fontsize=10)
    save(fig, "GFB-fig13-mesh.png")

def anim():
    from matplotlib.animation import FuncAnimation, PillowWriter
    N1, N2, m, al = 20, 30, 10, radians(20)
    fig, ax = plt.subplots(figsize=(8.6, 5.0)); ax.set_aspect("equal"); ax.axis("off")
    rp1, rp2 = m*N1/2, m*N2/2; mc = contact_ratio(rp1, rp2, rp1+m, rp2+m, al, N2); fr = 60
    def upd(i):
        ax.clear(); ax.set_aspect("equal"); ax.axis("off")
        phi = 2*pi/N1*i/fr + 0.0
        g, nc = frame(ax, N1, N2, m, al, phi)
        ax.set_xlim(-130, 420); ax.set_ylim(-190, 190)
        ax.text(150, -175, f"tooth pairs in contact now: {nc}      m_c = {mc:.2f}", ha="center", fontsize=11, color=R)
        ax.text(150, 172, "N₁=20 (driver, CCW)   N₂=30   m=10 mm   α=20°   E→F = path of contact", ha="center", fontsize=9)
    ani = FuncAnimation(fig, upd, frames=fr, interval=60)
    ani.save(os.path.join(OUT, "GFB-anim-mesh.gif"), writer=PillowWriter(fps=15), dpi=70); plt.close(fig); print("wrote GFB-anim-mesh.gif")

ALL = dict(fig1=fig1, fig2=fig2, fig3=fig3, fig4=fig4, fig5=fig5, fig6=fig6, fig7=fig7, fig8=fig8, fig9=fig9, fig10=fig10, fig11=fig11, fig12=fig12, fig13=fig13, anim=anim)
if __name__ == "__main__":
    check()
    for k in (sys.argv[1:] or ALL): ALL[k]()
