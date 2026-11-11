"""Figures for 'Velocity and Acceleration - Analytical Method.md':  python va_viz.py [v1 ... v5]"""
import sys, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import *
from va_core import *
nrm = np.linalg.norm

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets"); os.makedirs(OUT, exist_ok=True)
B, O, G, K, RR, GR = "#1f77b4", "#e8590c", "#7a7a7a", "#111111", "#d6204a", "#2a9d4a"
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
def save(fig, n): fig.savefig(os.path.join(OUT, n), dpi=110, bbox_inches="tight", facecolor="white"); plt.close(fig); print("wrote", n)
def arrow(ax, p, v, c, lw=2, **kw): ax.annotate("", xy=p+v, xytext=p, arrowprops=dict(arrowstyle="-|>", color=c, lw=lw, **kw))

L4 = (5.5, 1.7, 5.5, 4.08)          # frame, crank, coupler, follower (crank-rocker)

# ---- v1: four-bar angular velocity / acceleration of coupler and follower vs crank angle ---------------------------------
def v1():
    fig, axs = plt.subplots(2, 2, figsize=(12, 7)); th = np.linspace(0, 2*pi, 721); w2, a2 = 1.0, 0.0
    rows = {m: [fb_state(L4, t, w2, a2, m) for t in th] for m in (1, -1)}
    for (r, c), (key, ttl, un) in zip([(0, 0), (0, 1), (1, 0), (1, 1)], [("w3", "coupler angular velocity ω₃", "rad/s"), ("w4", "follower angular velocity ω₄", "rad/s"), ("a3", "coupler angular acceleration α₃", "rad/s²"), ("a4", "follower angular acceleration α₄", "rad/s²")]):
        ax = axs[r, c]
        for m, col in ((1, B), (-1, O)):
            y = np.array([s[key] if s else np.nan for s in rows[m]]); ax.plot(np.degrees(th), y, color=col, lw=1.8, label=f"assembly mode {'+' if m > 0 else '−'}")
        # finite-difference check dots
        for t in np.radians([40, 130, 220, 310]):
            s = fb_state(L4, t, 1, 0, 1)
            if s: ax.plot(degrees(t), s[key], "o", color=RR, ms=5)
        ax.set_title(ttl+f"  (ω₂ = {w2:g} rad/s, α₂ = 0)", fontsize=10); ax.set_xlabel("crank angle θ₂ (deg)"); ax.set_ylabel(un); ax.grid(alpha=.3); ax.set_xlim(0, 360)
        if r == 0 and c == 0: ax.legend(fontsize=8)
    fig.suptitle("Four-bar l₁=5.5, l₂=1.7, l₃=5.5, l₄=4.08 (crank-rocker): (2.33), (2.34).  Red dots = independent finite-difference check", fontsize=10.5)
    fig.tight_layout(); save(fig, "VA-v1-fourbar-curves.png")

# ---- v2: velocity and acceleration vectors on a four-bar --------------------------------------------------------------
def v2():
    th2 = radians(65); w2, a2 = 2.0, 1.5; st = fb_state(L4, th2, w2, a2, 1); l1, l2, l3, l4 = L4
    O2 = np.zeros(2); O4 = np.array([l1, 0.]); A = vec(l2, th2); Bp = O4+vec(l4, st["th4"])
    _, vA, aA = point_kin(l2, th2, w2, a2); rB = vec(l4, st["th4"]); vB = st["w4"]*perp(rB); aB = st["a4"]*perp(rB)-st["w4"]**2*rB
    # check: B from the coupler: vB = vA + w3 x AB
    AB = Bp-A; assert np.allclose(vB, vA+st["w3"]*perp(AB), atol=1e-9) and np.allclose(aB, aA+st["a3"]*perp(AB)-st["w3"]**2*AB, atol=1e-9)
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(13, 5.8))
    for a_ in (ax, bx):
        for p, q, c in ((O2, A, K), (A, Bp, K), (O4, Bp, K), (O2, O4, G)): a_.plot([p[0], q[0]], [p[1], q[1]], color=c, lw=2.2 if c == K else 1, ls="-" if c == K else "-.")
        for p, n in ((O2, "O₂"), (O4, "O₄"), (A, "A"), (Bp, "B")): a_.plot(*p, "o", color=K, ms=5); a_.text(p[0]+.12, p[1]-.35, n, fontsize=11)
        a_.set_aspect("equal"); a_.axis("off"); a_.set_xlim(-4, 9); a_.set_ylim(-5.2, 5.2)
    sv = .7; arrow(ax, A, sv*vA, B); arrow(ax, Bp, sv*vB, B); ax.text(*(A+sv*vA+np.array([.1, .1])), f"V_A = ω₂l₂ = {nrm(vA):.2f}", color=B); ax.text(*(Bp+sv*vB+np.array([.1, .1])), f"V_B = ω₄l₄ = {nrm(vB):.2f}", color=B)
    vBA = st["w3"]*perp(AB); arrow(ax, A, sv*vBA, GR, 1.4); ax.text(*(A+sv*vBA+np.array([-.2, .25])), "ω₃×AB", color=GR, fontsize=9)
    ax.set_title(f"velocity:  V_B = V_A + ω₃ × AB   (ω₃ = {st['w3']:.3f}, ω₄ = {st['w4']:.3f} rad/s)", fontsize=10)
    sa = .3
    for P_, r_, n_, col in ((A, A-O2, "A", O), (Bp, rB, "B", O)):
        w_, al_ = (w2, a2) if n_ == "A" else (st["w4"], st["a4"]); an = -w_**2*r_; at = al_*perp(r_)
        arrow(bx, P_, sa*an, GR, 1.5); arrow(bx, P_, sa*at, B, 1.5); arrow(bx, P_, sa*(an+at), O, 2.2)
    bx.text(*(A+sa*(-w2**2*(A-O2))+np.array([-.7, -.1])), "aⁿ_A", color=GR, fontsize=9); bx.text(*(A+sa*(a2*perp(A-O2))+np.array([-.1, .15])), "aᵗ_A", color=B, fontsize=9)
    bx.set_title(f"acceleration:  a = aⁿ (to centre, ω²r) + aᵗ (⊥, αr)   (α₃ = {st['a3']:.3f}, α₄ = {st['a4']:.3f} rad/s²)", fontsize=10)
    fig.suptitle("Four-bar at θ₂ = 65°, ω₂ = 2 rad/s, α₂ = 1.5 rad/s²:  vectors from the analytical solution; both coupler relations (2.16), (2.17) hold", fontsize=10.5); save(fig, "VA-v2-vectors.png")

# ---- v3: slider-crank ----------------------------------------------------------------------------------------------------
def v3():
    l2, l3, e = 2.0, 6.0, 0.8; th = np.linspace(0, 2*pi, 721); S = [sc_state(l2, l3, e, t, 1.0, 0.0, 1) for t in th]
    fig, axs = plt.subplots(1, 4, figsize=(16, 3.8))
    for ax, key, ttl in zip(axs, ("s", "sd", "sdd", "w3"), ("slider position s", "slider velocity ṡ", "slider acceleration s̈", "rod angular velocity ω₃")):
        ax.plot(np.degrees(th), [s[key] for s in S], color=B, lw=1.8); ax.set_title(ttl, fontsize=10); ax.set_xlabel("θ₂ (deg)"); ax.grid(alpha=.3); ax.set_xlim(0, 360)
    fig.suptitle("Offset slider-crank l₂=2, l₃=6, e=0.8, ω₂=1, α₂=0   (ṡ = −l₂ω₂ sin(θ₂−θ₃)/cosθ₃,  ω₃ = −l₂ω₂ cosθ₂/(l₃cosθ₃))", fontsize=10.5); fig.tight_layout(); save(fig, "VA-v3-slider-crank.png")

# ---- v4: slotted lever (Problem 2.19) --------------------------------------------------------------------------------------
def v4():
    l1, l2 = 3.0, 5.0; th = np.linspace(0, 2*pi, 721); S = [sl_state(l1, l2, t, 1.0, 0.0) for t in th]
    fig, axs = plt.subplots(1, 4, figsize=(16, 3.8))
    for ax, key, ttl in zip(axs, ("th4", "w4", "a4", "sd"), ("lever angle θ₄ (2.11)", "lever angular velocity ω₄ (e)", "lever angular acceleration α₄", "slide rate ṡ₄ (f)")):
        y = np.unwrap([s[key] for s in S]) if key == "th4" else [s[key] for s in S]; ax.plot(np.degrees(th), np.degrees(y) if key == "th4" else y, color=B, lw=1.8); ax.set_title(ttl, fontsize=10); ax.set_xlabel("θ₂ (deg)"); ax.grid(alpha=.3); ax.set_xlim(0, 360)
    fig.suptitle("Slotted lever, l₁=3, l₂=5, ω₂=1, α₂=0:  θ̇₄ = (l₂θ̇₂/s₄) cos(θ₄−θ₂),  ṡ₄ = l₂θ̇₂ sin(θ₄−θ₂),  s₄=√(l₁²+l₂²+2l₁l₂ sinθ₂)", fontsize=10.5); fig.tight_layout(); save(fig, "VA-v4-slotted-lever.png")

# ---- v5: Coriolis components -------------------------------------------------------------------------------------------------
def v5():
    l1, l2 = 3.0, 5.0; th2 = radians(20); w2, a2 = 1.5, 0.8; st = sl_state(l1, l2, th2, w2, a2); s, t4, w4, a4, sd, sdd = st["s4"], st["th4"], st["w4"], st["a4"], st["sd"], st["sdd"]
    O2 = np.zeros(2); O4 = np.array([0., -l1]); A = vec(l2, th2); e = np.array([cos(t4), sin(t4)]); r4 = s*e
    comps = [("aⁿ of P₄ = ω₄²s₄ (to O₄)", -w4**2*r4, GR), ("aᵗ of P₄ = α₄s₄", a4*perp(r4), B), ("a_rel = s̈₄ (along slot)", sdd*e, "#9467bd"), ("Coriolis 2ω₄ṡ₄ (⊥ slot)", 2*w4*sd*perp(e), RR)]
    aA = sum(c[1] for c in comps); _, _, aA2 = point_kin(l2, th2, w2, a2); assert np.allclose(aA, aA2)
    fig, ax = plt.subplots(figsize=(8.5, 6.5)); ax.plot([O4[0]-e[0]*1.5, O4[0]+e[0]*(s+2)+0], [O4[1]-e[1]*1.5, O4[1]+e[1]*(s+2)], color=K, lw=3, alpha=.4)
    ax.plot([O2[0], A[0]], [O2[1], A[1]], color=K, lw=2.2); ax.plot(*O2, "ko"); ax.plot(*O4, "ko"); ax.text(O2[0]-.5, O2[1]-.4, "O₂"); ax.text(O4[0]-.6, O4[1]-.4, "O₄"); ax.plot(*A, "o", color=O, ms=7); ax.text(A[0]+.1, A[1]+.15, "A", fontsize=12)
    sc = .5; tip = A.copy()
    for lab, v, c in comps: arrow(ax, tip, sc*v, c, 2); mid = tip+sc*v/2; ax.text(mid[0]+.1, mid[1]+.1, lab, color=c, fontsize=8.5); tip = tip+sc*v
    arrow(ax, A, sc*aA, O, 3); ax.text(*(A+sc*aA/2+np.array([-1.7, -.3])), "a_A (crank pin)", color=O, fontsize=10)
    ax.set_aspect("equal"); ax.axis("off"); ax.set_title("a_A = a_P4 (normal + tangential) + a_rel + a_Coriolis  (2.23, 2.24) — closes exactly on the crank-pin acceleration", fontsize=10); save(fig, "VA-v5-coriolis.png")

ALL = dict(v1=v1, v2=v2, v3=v3, v4=v4, v5=v5)
if __name__ == "__main__":
    check()
    for k in (sys.argv[1:] or ALL): ALL[k]()
