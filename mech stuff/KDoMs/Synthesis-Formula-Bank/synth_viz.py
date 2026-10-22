"""Regenerates the figures of the two synthesis formula banks:  python synth_viz.py [g1 g2 ... a3]"""
import sys, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, Arc
from math import *
from synth_core import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
os.makedirs(OUT, exist_ok=True)
B, O, G, K, RR, GR = "#1f77b4", "#e8590c", "#7a7a7a", "#111111", "#d6204a", "#2a9d4a"
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
def save(fig, name): fig.savefig(os.path.join(OUT, name), dpi=110, bbox_inches="tight", facecolor="white"); plt.close(fig); print("wrote", name)
def circ(ax, c, r, **kw): kw.setdefault("fill", False); ax.add_patch(Circle(c, r, **kw))
def pt(ax, p, name, c=K, off=(.12, .12), fs=10, ms=5): ax.plot(*p, "o", color=c, ms=ms, zorder=5); ax.text(p[0]+off[0], p[1]+off[1], name, color=c, fontsize=fs)
def seg(ax, p, q, **kw): ax.plot([p[0], q[0]], [p[1], q[1]], **kw)
def fit(ax, pts, m=1.0):
    p = np.array([q for q in pts if np.all(np.isfinite(q))]); ax.set_xlim(p[:, 0].min()-m, p[:, 0].max()+m); ax.set_ylim(p[:, 1].min()-m, p[:, 1].max()+m)
def tidy(ax, title): ax.set_aspect("equal"); ax.axis("off"); ax.set_title(title, fontsize=10)

BODY = np.array([[-.4, -.5], [4.4, -.5], [4.4, .9], [-.4, .9]])          # coupler outline (body coordinates)
def body_poly(pose): return np.array([to_world(pose, q) for q in BODY])

POSES = [(0, 0, .25), (2.6, 2.3, .95), (1.2, 4.6, 1.75)]
A_B, B_B = (0, 0), (4, 0)

# ------------------------------------------------------------------ G1  motion generation, free pivots
def g1():
    fig, ax = plt.subplots(figsize=(8.6, 7))
    O2, O4 = motion_free(POSES, A_B, B_B); A = [to_world(p, A_B) for p in POSES]; Bp = [to_world(p, B_B) for p in POSES]
    for k, p in enumerate(POSES):
        ax.add_patch(Polygon(body_poly(p), fc="#cfe3f5" if k == 0 else "none", ec=B, lw=1.6 if k == 0 else 1, alpha=1 if k == 0 else .8, ls="-" if k == 0 else "--"))
        seg(ax, A[k], Bp[k], color=B, lw=2)
        pt(ax, A[k], f"A{k+1}", O, (-.5, .15)); pt(ax, Bp[k], f"B{k+1}", GR, (.1, .15))
    circ(ax, O2, np.linalg.norm(A[0]-O2), ec=O, ls="--", lw=1); circ(ax, O4, np.linalg.norm(Bp[0]-O4), ec=GR, ls="--", lw=1)
    pt(ax, O2, "O₂", K, (-.6, -.3), 12, 7); pt(ax, O4, "O₄", K, (.15, -.3), 12, 7)
    seg(ax, O2, A[0], color=O, lw=2.4); seg(ax, O4, Bp[0], color=GR, lw=2.4); seg(ax, O2, O4, color=K, lw=1, ls="-.")
    ax.text(O2[0]-1.8, O2[1]-.9, "centre of circle\nthrough A₁A₂A₃", color=O, fontsize=9); ax.text(O4[0]+.3, O4[1]+.5, "centre of circle\nthrough B₁B₂B₃", color=GR, fontsize=9)
    tidy(ax, "Motion generation, three positions: ground pivots = circle centres (free pivots)")
    fit(ax, A+Bp+[O2, O4]+[q for p in POSES for q in body_poly(p)], 1.3)
    save(fig, "SFB-g1-motion-free.png")

# ------------------------------------------------------------------ G2  motion generation, given pivots (inversion)
def g2():
    O2 = np.array([-3.5, 1.0]); O4 = np.array([-3.8, 6.5])
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(13, 6.4))
    for k, p in enumerate(POSES):
        ax.add_patch(Polygon(body_poly(p), fc="none", ec=B, lw=1.5, ls="-" if k == 0 else "--")); ax.text(*to_world(p, (2, .2)), f"{['I','II','III'][k]}", color=B, fontsize=11, ha="center")
    pt(ax, O2, "O₂", K, (-.7, -.2), 12, 7); pt(ax, O4, "O₄", K, (-.7, .1), 12, 7); tidy(ax, "(a) prescribed coupler positions I, II, III and ground pivots")
    ax.set_xlim(-6, 8); ax.set_ylim(-1, 9)
    A1, B1 = motion_pivots(POSES, O2, O4); i2 = inverted_positions(POSES, O2); i4 = inverted_positions(POSES, O4)
    ax.plot(*zip(*[O2, O4]), "k:", lw=.8)
    bx.add_patch(Polygon(body_poly(POSES[0]), fc="#cfe3f5", ec=B, lw=1.6))
    for lst, c, nm, cen in ((i2, O, "O₂", A1), (i4, GR, "O₄", B1)):
        for k, q in enumerate(lst):
            pt(bx, q, f"{nm}$^{{1}}_{{{k+1}}}$", c, (.12, .12), 10)
        circ(bx, cen, np.linalg.norm(lst[0]-cen), ec=c, ls="--", lw=1)
    pt(bx, A1, "A₁", O, (-.5, -.5), 12, 7); pt(bx, B1, "B₁", GR, (.1, -.5), 12, 7)
    seg(bx, O2, A1, color=O, lw=2.4); seg(bx, O4, B1, color=GR, lw=2.4); seg(bx, A1, B1, color=B, lw=2.4)
    tidy(bx, "(b) coupler held fixed in position I: inverted pivots → A₁, B₁ are circle centres")
    fit(bx, i2+i4+[A1, B1]+[q for q in body_poly(POSES[0])], 1.3)
    save(fig, "SFB-g2-motion-pivots.png")

# ------------------------------------------------------------------ G3  path generation by inversion
CP = [(0, 0), (3, 1), (6, 0)]; PO2 = np.array([-3., -4.]); PO4 = np.array([4., -4.]); PB1 = np.array([0., -3.])
def g3():
    A1, poses, Bk = path_gen3(CP, PO2, PO4, PB1); C = [np.array(c, float) for c in CP]
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(13, 5.6))
    circ(ax, PO4, np.linalg.norm(PB1-PO4), ec=GR, ls="--", lw=1)
    for k in range(3):
        pt(ax, C[k], f"C{k+1}", RR, (.1, .15), 11); seg(ax, Bk[k], C[k], color=B, lw=1.4, ls="-" if k == 0 else ":"); pt(ax, Bk[k], f"B{k+1}", GR, (.1, -.45))
    seg(ax, PO4, Bk[0], color=GR, lw=2.2); pt(ax, PO4, "O₄", K, (.1, -.5), 11, 7); pt(ax, PO2, "O₂", K, (-.6, -.5), 11, 7)
    ax.text(-3.2, 2.0, "chosen: O₂, O₄, B₁\nB₂, B₃ from |O₄B| and |BC| = const", fontsize=9)
    tidy(ax, "(a) given C₁, C₂, C₃; choose O₂, O₄, B₁ → B₂, B₃ follow"); fit(ax, [PO4+np.array([0, -np.linalg.norm(PB1-PO4)]), PO4+np.array([np.linalg.norm(PB1-PO4), 0]), PO2, C[1], C[2], PB1], 1.2)
    inv = [to_body(p, PO2) for p in poses]
    seg(bx, Bk[0], C[0], color=B, lw=2.4); pt(bx, C[0], "C₁", RR, (.1, .15), 11); pt(bx, Bk[0], "B₁", GR, (.1, -.5), 11)
    for k, q in enumerate(inv): pt(bx, q, f"O₂$^{{1}}_{{{k+1}}}$", O, (.12, .12), 10)
    circ(bx, A1, np.linalg.norm(inv[0]-A1), ec=O, ls="--", lw=1); pt(bx, A1, "A₁", O, (.12, -.5), 12, 7)
    seg(bx, PO2, A1, color=O, lw=2.4); seg(bx, A1, Bk[0], color=B, lw=2.4); seg(bx, A1, C[0], color=B, lw=1.2); seg(bx, PO4, Bk[0], color=GR, lw=2.4); pt(bx, PO4, "O₄", K, (.1, -.5), 11, 7)
    tidy(bx, "(b) coupler fixed at position 1 (inversion): A₁ = centre of circle through O₂, O₂¹₂, O₂¹₃"); fit(bx, inv+[A1, PO2, PO4, Bk[0], C[0]], 1.5)
    save(fig, "SFB-g3-path-inversion.png")

# ------------------------------------------------------------------ G4  poles and relative poles
def g4():
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(13, 6.2))
    th = .8; Pc = np.array([1.0, 2.5]); mv = lambda p: Pc+R(th)@(p-Pc)
    A1, B1 = np.array([-2., -1.]), np.array([2.5, -2.0]); A2, B2 = mv(A1), mv(B1); P12 = pole(A1, A2, B1, B2)
    for P_, Q_, c in ((A1, A2, O), (B1, B2, GR)):
        m = (P_+Q_)/2; seg(ax, P_, Q_, color=c, lw=1, ls=":"); d = Q_-P_; n = np.array([-d[1], d[0]])/np.linalg.norm(d); seg(ax, m-n*1.5, P12+(P12-m)*0.1, color=c, lw=1.2, ls="--"); seg(ax, m, P12, color=c, lw=1.2, ls="--")
    seg(ax, A1, B1, color=B, lw=2.4); seg(ax, A2, B2, color=B, lw=2.4, ls="--")
    for p, n, c in ((A1, "A₁", O), (A2, "A₂", O), (B1, "B₁", GR), (B2, "B₂", GR)): pt(ax, p, n, c, (.1, .1), 11)
    pt(ax, P12, "P₁₂", RR, (.15, -.4), 12, 7); seg(ax, P12, A1, color=K, lw=.8); seg(ax, P12, A2, color=K, lw=.8); seg(ax, P12, B1, color=K, lw=.8); seg(ax, P12, B2, color=K, lw=.8)
    ax.add_patch(Arc(P12, 1.8, 1.8, theta1=degrees(atan2(*(A1-P12)[::-1])), theta2=degrees(atan2(*(A2-P12)[::-1])), color=O, lw=1.6)); ax.add_patch(Arc(P12, 2.6, 2.6, theta1=degrees(atan2(*(B1-P12)[::-1])), theta2=degrees(atan2(*(B2-P12)[::-1])), color=GR, lw=1.6))
    ax.text(P12[0]-1.0, P12[1]+1.3, "∠A₁P₁₂A₂ = ∠B₁P₁₂B₂ = θ₃¹²", fontsize=9.5)
    tidy(ax, "(a) pole P₁₂ of a coupler displacement: intersection of the mid-normals of A₁A₂ and B₁B₂"); ax.set_xlim(-5, 7); ax.set_ylim(-4, 6)
    O2 = np.array([0., 0]); O4 = np.array([6., 0]); l2, l3, l4 = 2., 5., 4.; t1, t2 = .9, 1.6
    a1, b1 = fourbar(O2, O4, l2, l3, l4, t1); a2, b2 = fourbar(O2, O4, l2, l3, l4, t2)
    d2 = t2-t1; d4 = atan2(*(b2-O4)[::-1])-atan2(*(b1-O4)[::-1]); O4p = O2+R(-d2)@(O4-O2); b2p = O2+R(-d2)@(b2-O2); R12 = pole(b1, b2p, O4, O4p)
    seg(bx, O2, O4, color=K, lw=1.4); seg(bx, O2, a1, color=O, lw=2.4); seg(bx, a1, b1, color=B, lw=2.4); seg(bx, O4, b1, color=GR, lw=2.4); seg(bx, O2, a2, color=O, lw=1.2, ls="--"); seg(bx, a2, b2, color=B, lw=1.2, ls="--"); seg(bx, O4, b2, color=GR, lw=1.2, ls="--")
    seg(bx, O2, R12, color=RR, lw=1.2); seg(bx, O4, R12, color=RR, lw=1.2); seg(bx, R12, a1, color=G, lw=.8, ls=":"); seg(bx, R12, b1, color=G, lw=.8, ls=":")
    for p, n, c, o in ((O2, "O₂", K, (-.5, -.4)), (O4, "O₄", K, (.1, -.4)), (a1, "A₁", O, (-.1, .2)), (b1, "B₁", GR, (.1, .15)), (R12, "R₁₂", RR, (-.2, .3))): pt(bx, p, n, c, o, 11)
    bx.text(-3.6, -1.9, f"N₁ at O₂: −θ₂¹²/2 = {degrees(-d2/2):.1f}° from O₂O₄\nN₂ at O₄: −θ₄¹²/2 = {degrees(-d4/2):.1f}° from O₄O₂\n∠O₂R₁₂O₄ = ∠A₁R₁₂B₁ = {degrees(abs(ang(R12, O2, O4))):.1f}°\n∠O₂R₁₂A₁ = ∠O₄R₁₂B₁ = {degrees(abs(ang(R12, O2, a1))):.1f}°", fontsize=9, va="top", bbox=dict(fc="#fff6f7", ec=RR))
    tidy(bx, "(b) relative pole R₁₂ of a 4R linkage (θ₂¹² = 40.1°, θ₄¹² = 14.7°): equal angles at R₁₂"); bx.set_xlim(-6, 8); bx.set_ylim(-5, 4.5)
    save(fig, "SFB-g4-poles.png")

# ------------------------------------------------------------------ G5  point-position reduction: 4-point path generation
def g5():
    C = [np.array(c, float) for c in [(0, 0), (3, 1), (6, 0), (8, -2)]]; O4 = np.array([4., -4.]); B1 = np.array([0., -3.]); rB = np.linalg.norm(B1-O4); bc = np.linalg.norm(C[0]-B1)
    Bk = [B1]
    for k in (1, 2, 3): Bk.append(circle_circle(O4, rB, C[k], bc, Bk[-1]))
    P13 = pole(Bk[0], Bk[2], C[0], C[2]); O2 = P13
    ang0 = atan2(*(C[0]-Bk[0])[::-1]); poses = []
    for k in range(4):
        ph = atan2(*(C[k]-Bk[k])[::-1])-ang0; t = C[k]-R(ph)@C[0]; poses.append((t[0], t[1], ph))
    inv = [to_body(p, O2) for p in poses]; A1 = circumcenter(inv[0], inv[1], inv[3])
    fig, ax = plt.subplots(figsize=(9.5, 7.5))
    for k in range(4): pt(ax, C[k], f"C{k+1}", RR, (.12, .2), 11); pt(ax, Bk[k], f"B{k+1}", GR, (.1, -.5), 10); seg(ax, Bk[k], C[k], color=B, lw=1.2, ls=":")
    pt(ax, O2, "O₂ = P₁₃", K, (-1.8, -.6), 11, 7); pt(ax, O4, "O₄", K, (.15, -.5), 11, 7); circ(ax, O4, rB, ec=GR, ls="--", lw=.9)
    for k, q in enumerate(inv): pt(ax, q, f"O₂$^{{1}}_{{{k+1}}}$", O, (.1, .1), 9)
    circ(ax, A1, np.linalg.norm(inv[0]-A1), ec=O, ls="--", lw=.9); pt(ax, A1, "A₁", O, (.1, -.6), 11, 7)
    seg(ax, O2, A1, color=O, lw=2.4); seg(ax, A1, B1, color=B, lw=2.4); seg(ax, O4, B1, color=GR, lw=2.4); seg(ax, A1, C[0], color=B, lw=1.2)
    # check: all four A_k on a circle about O2, B_k about O4
    Ak = [move(p, A1) for p in poses]; err = max(abs(np.linalg.norm(a-O2)-np.linalg.norm(Ak[0]-O2)) for a in Ak)
    ax.text(O2[0]-3.5, C[1][1]+1.8, f"O₂ placed at the pole P₁₃ ⇒ O₂¹₁ = O₂¹₃ (two inverted positions coincide)\nA₁ = centre of circle through O₂¹₁, O₂¹₂, O₂¹₄   (check: |O₂A_k| constant to {err:.1e})", fontsize=9)
    tidy(ax, "Point-position reduction: coupler point through four prescribed points C₁…C₄"); fit(ax, inv+C+Bk+[A1, O4, O2], 2.0)
    save(fig, "SFB-g5-point-position-reduction.png")

# ------------------------------------------------------------------ G6  straight-line mechanisms
def peaucellier(ax):
    O = np.zeros(2); Op = np.array([2.5, 0.]); OA, AP = 5., 2.; k = OA**2-AP**2; Qs = []
    for t in np.linspace(-1.2, 1.2, 25):
        P = Op+2.5*np.array([cos(t), sin(t)]); u = P/np.linalg.norm(P); Qs.append(u*k/np.linalg.norm(P))
    for t, c, lw in ((-.7, G, .9), (.55, RR, 1.8)):
        P = Op+2.5*np.array([cos(t), sin(t)]); u = P/np.linalg.norm(P); OP = np.linalg.norm(P); Q = u*k/OP; OC = (OP+k/OP)/2; h = sqrt(max(OA**2-OC**2, 0)); n = np.array([-u[1], u[0]]); A, Bb = u*OC+n*h, u*OC-n*h
        for p, q in ((A, P), (P, Bb), (Bb, Q), (Q, A), (O, A), (O, Bb), (Op, P)): seg(ax, p, q, color=c, lw=lw)
        pt(ax, P, "P", c, (.1, .1), 9, 4); pt(ax, Q, "Q", c, (.1, .1), 9, 4)
    Qs = np.array(Qs); ax.plot(Qs[:, 0], Qs[:, 1], color=RR, lw=2.2); ax.axvline(k/5, color=RR, lw=.7, ls=":")
    pt(ax, O, "O", K, (-.5, -.5), 11, 6); pt(ax, Op, "O_p", K, (.1, -.5), 10, 6)
    ax.set_xlim(-3, 8); ax.set_ylim(-6.5, 6.5); tidy(ax, "Peaucellier: OA = OB, rhombus APBQ ⇒ OP·OQ = OA² − AP² = const ⇒ Q on a straight line"); ax.title.set_fontsize(8.8)

def g6():
    fig, axs = plt.subplots(2, 3, figsize=(15, 9)); axs = axs.ravel(); peaucellier(axs[0]); axs[5].axis("off")
    L, a = 2.5, 2.0
    cases = [("Watt (a):  O₂A = O₄B, AC = BC;  O₂O₄ : O₂A : AB = 10.77 : 5 : 4", dict(O4=(10.77, 0), l2=5., l3=4., l4=5., u=2., v=0.)),
             ("Evans (b):  AB = O₄B = BC;  O₂A : AB : O₂O₄ = 2 : 2.5 : 5.39", dict(O4=(5.39, 0), l2=2., l3=2.5, l4=2.5, u=5., v=0.)),
             ("Roberts (c):  O₂O₄ = 2AB;  O₂A = AC = BC = O₄B", dict(O4=(2*a, 0), l2=L, l3=a, l4=L, u=a/2, v=-sqrt(L*L-a*a/4))),
             ("Chebyshev (d):  AB : O₂O₄ : O₂A : O₄B = 1 : 2 : 2.5 : 2.5", dict(O4=(2., 0), l2=2.5, l3=1., l4=2.5, u=.5, v=0.))]
    for ax, (title, p) in zip(axs[1:], cases):
        O2 = np.zeros(2); O4 = np.array(p["O4"], float)
        for br, col in ((1, B), (-1, O)):
            cc = coupler_curve(O2, O4, p["l2"], p["l3"], p["l4"], p["u"], p["v"], br); ax.plot(cc[:, 0], cc[:, 1], color=col, lw=1.8 if br == 1 else 1, alpha=1 if br == 1 else .5)
        r = fourbar(O2, O4, p["l2"], p["l3"], p["l4"], 1.0, 1)
        if r:
            A_, B_ = r; Cc = coupler_point(A_, B_, p["u"], p["v"]); seg(ax, O2, A_, color=K, lw=1.5); seg(ax, A_, B_, color=K, lw=1.5); seg(ax, O4, B_, color=K, lw=1.5); seg(ax, A_, Cc, color=K, lw=.8, ls=":"); seg(ax, B_, Cc, color=K, lw=.8, ls=":"); pt(ax, Cc, "C", RR, (.1, .1), 10)
        pt(ax, O2, "O₂", K, (-.3, -.5), 10, 5); pt(ax, O4, "O₄", K, (.1, -.5), 10, 5); tidy(ax, title); ax.title.set_fontsize(8.8)
        c1 = coupler_curve(O2, O4, p["l2"], p["l3"], p["l4"], p["u"], p["v"], 1); fit(ax, list(c1)+[O2, O4], .6)
    fig.suptitle("Special straight-line mechanisms (path generation of a straight line): one exact, four approximate (coupler-point curves; orange = other assembly)", fontsize=11)
    save(fig, "SFB-g6-straight-line.png")

# ------------------------------------------------------------------ A1  Chebyshev spacing + Freudenstein (Problem 3.5)
def solve_th4(Kc, th2, guess):
    """Freudenstein (3.6) rewritten as (K1 - cos th2) cos th4 - sin th2 sin th4 = K2 cos th2 - K3"""
    a, b, rhs = Kc[0]-cos(th2), -sin(th2), Kc[1]*cos(th2)-Kc[2]; Rm = hypot(a, b); ph = atan2(-b, a)
    if abs(rhs/Rm) > 1: return np.nan
    c = [-ph+acos(rhs/Rm), -ph-acos(rhs/Rm)]
    return min((x+2*pi*n for x in c for n in (-1, 0, 1)), key=lambda x: abs(x-guess))

def a1():
    fig, axs = plt.subplots(1, 3, figsize=(16, 4.8))
    for ax, k in zip(axs[:2], (3, 4)):
        a, h = 5.5, 4.5; t = np.linspace(0, pi, 200); ax.plot(a+h*np.cos(t), h*np.sin(t), color=G, lw=1)
        verts = [pi/(2*k)+j*pi/k for j in range(k)]
        pv = [(a+h*cos(v), h*sin(v)) for v in verts]; ax.plot([p[0] for p in pv], [p[1] for p in pv], "o-", color=B, lw=1, ms=5)
        for l, v in enumerate(verts):
            x = a+h*cos(v); ax.plot([x, x], [0, h*sin(v)], color=O, lw=1, ls=":"); ax.plot(x, 0, "s", color=RR, ms=6); ax.text(x, -.55, f"x{l+1}={x:.2f}", ha="center", fontsize=8.5, color=RR)
        ax.plot([1, 10], [0, 0], color=K, lw=1); ax.set_aspect("equal"); ax.axis("off"); ax.set_title(f"Chebyshev spacing, k = {k}, interval 1…10 (a = 5.5, h = 4.5)", fontsize=10)
    Kc = np.array([2, -0.703, 1.078]); xs = np.linspace(1, 10, 300); yt = np.log10(xs); yg = []
    for x in xs:
        th2 = radians(45+60/9*(x-1)); t4 = solve_th4(Kc, th2, radians(135+90*log10(x))); yg.append((degrees(t4)-135)/90)
    yg = np.array(yg); ax = axs[2]; ax.plot(xs, yt, color=K, lw=2, label="desired  y = log₁₀ x"); ax.plot(xs, yg, color=O, lw=1.6, ls="--", label="four-bar output (3 accuracy points)")
    ax2 = ax.twinx(); ax2.plot(xs, yt-yg, color=RR, lw=1.2, label="structural error E(x) = f − F"); ax2.axhline(0, color=RR, lw=.5)
    for x in chebyshev(1, 10, 3): ax.axvline(x, color=G, lw=.6, ls=":")
    ax2.set_ylabel("E(x)", color=RR); ax.set_xlabel("x"); ax.set_ylabel("y"); ax.legend(loc="upper left", fontsize=8); ax2.legend(loc="lower right", fontsize=8); ax.set_title("Problem 3.5: E(x) vanishes at the three accuracy points", fontsize=10)
    ax2.spines["right"].set_visible(True); save(fig, "SFB-a1-chebyshev-freudenstein.png")

# ------------------------------------------------------------------ A2  slider-crank function generator (Problem 3.6)
def a2():
    Kc = slider_K([(radians(128.7), 3.95), (radians(90), 8.26), (radians(51.3), 9.97)]); C = -7/8100
    th = np.linspace(45, 135, 300); target = 10+C*(th-45)**2
    s = []
    for t in th:
        r = radians(t); b = Kc[0]*cos(r); c = Kc[2]-Kc[1]*sin(r); disc = b*b-4*c
        roots = [(b+e*sqrt(disc))/2 for e in (1, -1)] if disc >= 0 else [np.nan]; s.append(min(roots, key=lambda x: abs(x-(10+C*(t-45)**2))))
    s = np.array(s); fig, ax = plt.subplots(figsize=(7.5, 4.8)); ax.plot(th, target, color=K, lw=2, label="desired  s = sⁱ + C(θ₂ − θ₂ⁱ)²"); ax.plot(th, s, "--", color=O, lw=1.6, label="slider-crank (3 accuracy points)")
    for a_, sv in ((128.7, 3.95), (90, 8.26), (51.3, 9.97)): ax.plot(a_, sv, "o", color=RR, ms=7)
    ax.set_xlabel("crank angle θ₂ (deg)"); ax.set_ylabel("slider position s (cm)"); ax.grid(alpha=.3); ax.legend(fontsize=9); ax.set_title("Problem 3.6: l₂ = 4.805, l₄ = 13.6, l₃ = 12.05 cm", fontsize=10)
    save(fig, "SFB-a2-slider-crank.png")

# ------------------------------------------------------------------ A3  dyad (standard-form) method
def a3():
    O2 = np.zeros(2); O4 = np.array([5., 0.]); l2, l3, l4 = 2., 4.5, 3.5; u, v = 2., 1.5
    ts = [radians(70), radians(95), radians(120)]; Ac, Bc, Cc = [], [], []
    for t in ts:
        a, b = fourbar(O2, O4, l2, l3, l4, t, 1); Ac.append(a); Bc.append(b); Cc.append(coupler_point(a, b, u, v))
    z = lambda p: complex(*p)
    th2 = [ts[j]-ts[0] for j in (1, 2)]; th4 = [atan2(*(Bc[j]-O4)[::-1])-atan2(*(Bc[0]-O4)[::-1]) for j in (1, 2)]
    th3 = [atan2(*(Bc[j]-Ac[j])[::-1])-atan2(*(Bc[0]-Ac[0])[::-1]) for j in (1, 2)]; dl = [z(Cc[j]-Cc[0]) for j in (1, 2)]
    L, Ls = dyad_solve(dl, th2, th3); Rr, Rs = dyad_solve(dl, th4, th3)
    assert abs(L-z(Ac[0]-O2)) < 1e-8 and abs(Rr-z(Bc[0]-O4)) < 1e-8      # the dyads recover the linkage the data came from
    fig, ax = plt.subplots(figsize=(9.5, 7)); P = lambda w: np.array([w.real, w.imag]); O2c = z(Cc[0])-L-Ls
    for j in range(3):
        st = dict(color=B if j == 0 else G, lw=2.2 if j == 0 else 1.1, ls="-" if j == 0 else "--")
        seg(ax, O2, Ac[j], **st); seg(ax, Ac[j], Bc[j], **st); seg(ax, O4, Bc[j], **st); seg(ax, Ac[j], Cc[j], **st); seg(ax, Bc[j], Cc[j], **st)
        pt(ax, Cc[j], f"C{j+1}", RR, (.1, .12), 11); pt(ax, Ac[j], f"A{j+1}", O, (-.45, .05), 9); pt(ax, Bc[j], f"B{j+1}", GR, (.1, .05), 9)
    cc = coupler_curve(O2, O4, l2, l3, l4, u, v, 1); ax.plot(cc[:, 0], cc[:, 1], color=RR, lw=.8, alpha=.5)
    pt(ax, O2, "O₂", K, (-.5, -.5), 11, 7); pt(ax, O4, "O₄", K, (.1, -.5), 11, 7)
    ax.text(*(Ac[0]+O2)/2+np.array([-.45, 0]), "L", color=O, fontsize=12); ax.text(*(Ac[0]+Cc[0])/2+np.array([-.4, .1]), "L*", color=O, fontsize=12)
    ax.text(*(Bc[0]+O4)/2+np.array([.15, 0]), "R", color=GR, fontsize=12); ax.text(*(Bc[0]+Cc[0])/2+np.array([.15, .1]), "R*", color=GR, fontsize=12)
    ax.text(-1.5, -2.6, "Standard form (3.18):  L(e^{iθ₂ʲ}−1) + L*(e^{iθ₃ʲ}−1) = δⱼ        right dyad (3.19):  R(e^{iθ₄ʲ}−1) + R*(e^{iθ₃ʲ}−1) = δⱼ\n"
            f"data: θ₂ = {degrees(th2[0]):.0f}°, {degrees(th2[1]):.0f}°   θ₃ = {degrees(th3[0]):.1f}°, {degrees(th3[1]):.1f}°   θ₄ = {degrees(th4[0]):.1f}°, {degrees(th4[1]):.1f}°   δ₂ = {dl[0]:.2f},  δ₃ = {dl[1]:.2f}\n"
            f"solved: L = {L:.2f}, L* = {Ls:.2f}, R = {Rr:.2f}, R* = {Rs:.2f}  ⇒  O₂A = {abs(L):.2f}, AC = {abs(Ls):.2f}, O₄B = {abs(Rr):.2f}, BC = {abs(Rs):.2f}", fontsize=8.5, va="top")
    tidy(ax, "Path generation by dyads (reverse test: C₁, C₂, C₃ and rotations taken from a known 4R, which the equations recover)"); fit(ax, Ac+Bc+Cc+[O2, O4, np.array([0, -4.0])], 1.2)
    save(fig, "SFB-a3-dyads.png")

ALL = dict(g1=g1, g2=g2, g3=g3, g4=g4, g5=g5, g6=g6, a1=a1, a2=a2, a3=a3)
if __name__ == "__main__":
    check()
    for k in (sys.argv[1:] or ALL): ALL[k]()
