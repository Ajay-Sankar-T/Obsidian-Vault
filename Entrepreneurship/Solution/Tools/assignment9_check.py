"""Assignment 9: sponsored search market (Pricing-1.pdf, slides 54-57). Verifies every number in the note and draws the figures.
Run: python assignment9_check.py   (figures -> ../assets/A9-*.png)"""
import os, itertools
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "..", "assets"); os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.size": 10, "axes.grid": True, "grid.alpha": .3, "axes.spines.top": False, "axes.spines.right": False})
C = ["#1f77b4", "#d62728", "#2ca02c", "#ff7f0e"]
def save(fig, name): fig.savefig(os.path.join(OUT, name), dpi=150, bbox_inches="tight"); plt.close(fig); print("wrote", name)

class Market:
    def __init__(self, ctr, val):
        self.ctr, self.val = ctr, val; self.slots = list(ctr); self.adv = list(val)
    def v(self, s, a): return 0 if a is None else self.ctr[s]*self.val[a]                     # valuation of advertiser a for slot s (per slot, all clicks)
    def optimum(self):
        # all ways to give slots to advertisers (each advertiser at most one slot, each slot one advertiser)
        best, arg = -1, None
        for perm in itertools.permutations(self.adv, len(self.slots)):
            tot = sum(self.v(s, a) for s, a in zip(self.slots, perm))
            if tot > best: best, arg = tot, dict(zip(self.slots, perm))
        return best, arg
    def vcg(self):
        tot, alloc = self.optimum(); price = {}
        for s, a in alloc.items():
            others_now = tot-self.v(s, a)
            rest = [x for x in self.adv if x != a]; rest += [None]*(len(self.slots)-len(rest))   # empty slots are worth 0
            without = max(sum(self.v(sl, x) for sl, x in zip(self.slots, perm)) for perm in itertools.permutations(rest, len(self.slots)))
            price[a] = (s, without-others_now)
        return tot, alloc, price
    def gsp(self, bids):
        order = sorted(self.adv, key=lambda n: (-bids[n], self.adv.index(n)))
        res, rev = {}, 0
        for i, n in enumerate(order):
            s = self.slots[i]; nxt = bids[order[i+1]] if i+1 < len(order) else 0
            pay = self.ctr[s]*nxt; res[n] = (s, nxt, pay, self.v(s, n)-pay); rev += pay
        welfare = sum(self.v(self.slots[i], n) for i, n in enumerate(order))
        return order, res, rev, welfare
    def is_nash(self, bids, grid):
        _, res, _, _ = self.gsp(bids)
        return all(self.gsp({**bids, n: d})[1][n][3] <= res[n][3]+1e-9 for n in self.adv for d in grid)

# ------------------------------------------------ warm-up: slides 55-56
M1 = Market({"a": 10, "b": 5, "c": 2}, {"x": 3, "y": 2, "z": 1})
t1, al1, p1 = M1.vcg()
assert t1 == 42 and p1["x"][1] == 13 and p1["y"][1] == 3 and p1["z"][1] == 0          # the slide's "harm of 13" and "harm of 3"

# ------------------------------------------------ slide 57 market
M = Market({"a": 10, "b": 4, "c": 0}, {"x": 7, "y": 6, "z": 1})
tot, alloc, price = M.vcg()
assert tot == 94 and alloc == {"a": "x", "b": "y", "c": "z"}
assert price["x"] == ("a", 40) and price["y"] == ("b", 4) and price["z"] == ("c", 0)
vcg_rev = sum(p for _, p in price.values()); assert vcg_rev == 44                       # slide 59
# every assignment (for the table)
assign = []
for perm in itertools.permutations("xyz"):
    assign.append((perm, sum(M.v(s, a) for s, a in zip("abc", perm))))
assert sorted(t for _, t in assign) == [34, 38, 64, 74, 88, 94]

# GSP truthful
o, res, rev, w = M.gsp({"x": 7, "y": 6, "z": 1})
assert o == ["x", "y", "z"] and res["x"][3] == 10 and res["y"][3] == 20 and res["z"][3] == 0 and rev == 64 and w == 94      # slide 58: payoff 10
# deviation: x bids 5
o5, r5, rev5, w5 = M.gsp({"x": 5, "y": 6, "z": 1}); assert r5["x"][3] == 24 and o5 == ["y", "x", "z"]                         # slide 58: payoff 24
payoff_vs_bid = [(b, M.gsp({"x": b, "y": 6, "z": 1})[1]["x"][3]) for b in np.arange(0, 10.01, .05)]
dev = [i/2 for i in range(0, 25)]
assert not M.is_nash({"x": 7, "y": 6, "z": 1}, dev)
# equilibria of slide 58
e1 = {"x": 5, "y": 4, "z": 2}; e2 = {"x": 3, "y": 5, "z": 1}
assert M.is_nash(e1, dev) and M.is_nash(e2, dev)
o1, r1, rev1, w1 = M.gsp(e1); o2, r2, rev2, w2 = M.gsp(e2)
assert o1 == ["x", "y", "z"] and rev1 == 48 and w1 == 94 and (r1["x"][3], r1["y"][3], r1["z"][3]) == (30, 16, 0)
assert o2 == ["y", "x", "z"] and rev2 == 34 and w2 == 88 and (r2["y"][3], r2["x"][3], r2["z"][3]) == (30, 24, 0)
# VCG payoffs
vcg_pay = {a: M.v(s, a)-p for a, (s, p) in price.items()}; assert vcg_pay == {"x": 30, "y": 20, "z": 0}
# truthful bidding in VCG is dominant: x cannot gain by misreporting its value (re-run VCG with a fake value)
for fake in np.arange(0, 12.01, .25):
    Mf = Market(M.ctr, {**M.val, "x": fake}); _, alf, pf = Mf.vcg()
    s, p = pf["x"]; gain = M.v(s, "x")-p
    assert gain <= vcg_pay["x"]+1e-9, (fake, gain)
for who in ("y", "z"):
    for fake in np.arange(0, 12.01, .25):
        Mf = Market(M.ctr, {**M.val, who: fake}); _, alf, pf = Mf.vcg(); s, p = pf[who]; assert M.v(s, who)-p <= vcg_pay[who]+1e-9

# brute-force pure equilibria on integer bids 0..9
cnt = {}; G = range(0, 10); dev = [i/2 for i in range(0, 25)]
for bx, by, bz in itertools.product(G, G, G):
    b = {"x": bx, "y": by, "z": bz}
    if M.is_nash(b, dev):
        o_, _, r_, w_ = M.gsp(b); cnt.setdefault(tuple(o_), []).append((r_, b))
NO_ORDER = {k: (len(v), min(r for r, _ in v), max(r for r, _ in v)) for k, v in cnt.items()}
cnt2 = {}
for bx in range(0, 8):
    for by in range(0, 7):
        for bz in range(0, 2):
            b = {"x": bx, "y": by, "z": bz}
            if M.is_nash(b, dev): o_, _, r_, _ = M.gsp(b); cnt2.setdefault(tuple(o_), []).append(r_)
NO_OVER = {k: (len(v), min(v), max(v)) for k, v in cnt2.items()}
if __name__ == "__main__":
    print("warm-up VCG", p1); print("slide-57 VCG", price, "revenue", vcg_rev, "welfare", tot); print("assignments", sorted(assign, key=lambda t: -t[1]))
    print("GSP truthful", res, rev); print("x bids 5", r5["x"]); print("eq1", r1, rev1, w1); print("eq2", r2, rev2, w2)
    print("integer-grid equilibria (bids 0-9):", NO_ORDER); print("with bids <= own value:", NO_OVER)

    # ------------------------------------------------ figures
    fig, ax = plt.subplots(figsize=(7.5, 3.9)); bb = [b for b, _ in payoff_vs_bid]; pp = [p for _, p in payoff_vs_bid]
    ax.step(bb, pp, where="post", color=C[0], lw=2.4); ax.plot([7], [10], "o", color=C[1], ms=9); ax.plot([5], [24], "o", color=C[2], ms=9)
    ax.annotate("truthful bid 7: payoff 10", (7, 10), (7.2, 15), arrowprops=dict(arrowstyle="->"), color=C[1]); ax.annotate("bid 5: payoff 24", (5, 24), (1.2, 27), arrowprops=dict(arrowstyle="->"), color=C[2])
    ax.axvline(6, color="grey", ls=":"); ax.text(6.05, 1.5, "y's bid 6", fontsize=8.5, color="grey"); ax.axvline(1, color="grey", ls=":"); ax.text(1.05, 1.5, "z's bid 1", fontsize=8.5, color="grey")
    ax.set_xlabel("x's bid (y bids 6, z bids 1)"); ax.set_ylabel("x's payoff"); ax.set_ylim(-1, 31); ax.set_title("GSP: advertiser x gains by shading its bid below y's")
    save(fig, "A9-fig2-payoff-vs-bid.png")

    print("all checks passed")
