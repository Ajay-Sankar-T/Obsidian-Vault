"""EE1100 Tutorials 1, 2, 3, 4 and 8: every number in the solution notes is recomputed here and compared with the
answer printed on the tutorial sheet.   Run:  python ee_t1_t4_t8.py
Prints OK where the sheet agrees (within the stated tolerance) and DIFF where it does not (those are discussed in the notes)."""
import cmath
import itertools
import math
import numpy as np

RESULTS = []


def chk(name, got, printed, tol=0.005, note=""):
    """compare with a printed answer; tol is a relative tolerance"""
    ok = abs(got - printed) <= tol * max(abs(printed), 1e-12)
    RESULTS.append((ok, name, got, printed, note))


def P(z):
    return abs(z), math.degrees(cmath.phase(z))


def mna(elems, nodes, ground):
    """modified nodal analysis, complex: ('R',a,b,r) ('V',plus,minus,v) ('I',a,b,i)  (I flows a->b through the source)"""
    idx = {n: i for i, n in enumerate([n for n in nodes if n != ground])}
    vs = [e for e in elems if e[0] == "V"]
    n, m = len(idx), len(vs)
    A = np.zeros((n + m, n + m), dtype=complex); z = np.zeros(n + m, dtype=complex)
    g = idx.get
    def add(i, j, v):
        if i is not None and j is not None:
            A[i, j] += v
    for e in elems:
        if e[0] == "R":
            _, a, b, r = e; y = 1 / r
            add(g(a), g(a), y); add(g(b), g(b), y); add(g(a), g(b), -y); add(g(b), g(a), -y)
        elif e[0] == "I":
            _, a, b, i = e
            if g(a) is not None: z[g(a)] -= i
            if g(b) is not None: z[g(b)] += i
    for k, (_, p, q, v) in enumerate(vs):
        r = n + k
        if g(p) is not None: A[r, g(p)] += 1; A[g(p), r] += 1
        if g(q) is not None: A[r, g(q)] -= 1; A[g(q), r] -= 1
        z[r] = v
    x = np.linalg.solve(A, z)
    V = {ground: 0}; V.update({nd: x[i] for nd, i in idx.items()})
    return V, x[n:]


# =============================================================== Tutorial 1
def t1():
    r = {}
    # Q1 R-2R ladder (VR = 1, R = 1)
    I1 = 1 / 2; V2 = 1 - I1; I2 = V2 / 2; V3 = V2 - I2; I3 = V3 / 2; V4 = V3 - I3; I4 = V4 / 2
    r["Q1 V"] = (1, V2, V3, V4); r["Q1 I"] = (I1, I2, I3, I4)
    chk("T1Q1 V2", V2, 0.5); chk("T1Q1 V3", V3, 0.25); chk("T1Q1 V4", V4, 0.125); chk("T1Q1 I4", I4, 1 / 16)
    # Q2
    # unknown node voltages A (after 3 ohm), B (after 6 ohm); every emf is 10 V
    V, _ = mna([("V", "S1", "0", 10), ("R", "S1", "A", 3), ("V", "E2", "0", 10), ("R", "A", "E2", 8), ("R", "A", "B", 6),
                ("R", "B", "0", 12), ("V", "B", "0", 10)], ["S1", "A", "E2", "B"], "0")
    r["Q2"] = ((V["S1"] - V["A"]) / 3, (V["A"] - V["E2"]) / 8, (V["A"] - V["B"]) / 6, V["B"] / 12)
    chk("T1Q2 I12", V["B"].real / 12, 0.833, 0.002)
    # Q3
    V0 = (2 - 8) / (1 / 6 + 1 / 3)
    r["Q3"] = (V0, V0 / 6, V0 / 3, (V0 / 6) ** 2 * 6)
    chk("T1Q3 V0 (sheet prints -6)", V0, -6, note="sheet's -6 V contradicts its own I1=-2 A and P=24 W; V0 = 6*I1 = -12 V")
    chk("T1Q3 I1", V0 / 6, -2); chk("T1Q3 I2", V0 / 3, -4); chk("T1Q3 P6", (V0 / 6) ** 2 * 6, 24)
    # Q4  (V = 12 across everything)
    for K, tag in ((2, "a"), (-2, "b")):
        Ir1 = 12 / 6; Ir2 = 12 / 3; Ik = K * Ir1; Is = Ir1 + Ir2 - Ik
        r["Q4" + tag] = dict(Ps=12 * Is, P6=12 * Ir1, P3=12 * Ir2, Pdep_delivered=12 * Ik, Is=Is)
    chk("T1Q4a P12V", r["Q4a"]["Ps"], 24); chk("T1Q4b P12V", r["Q4b"]["Ps"], 120)
    chk("T1Q4a PKI", r["Q4a"]["Pdep_delivered"], 48); chk("T1Q4b PKI", r["Q4b"]["Pdep_delivered"], -48)
    # Q5
    Voc = 10.0; Rth = 16.0
    # open circuit: V = e + 40 i1 ; E_d = V + 20 i1 = 10 i1  with e = 50 -> i1 = -e/50
    e = 50; i1 = -e / 50; Vo = e + 40 * i1
    # test source
    Vt = 1.0; i1t = Vt / 40; Ed = 10 * i1t; It = (Vt - Ed) / 20 + Vt / 40
    r["Q5"] = dict(Voc=Vo, Rth=Vt / It, VRL=Vo * 16 / 32, Pmax=Vo ** 2 / (4 * 16))
    chk("T1Q5 Rth", Vt / It, 16); chk("T1Q5 VRL", Vo * 16 / 32, 5)
    # Q6 superposition
    V, _ = mna([("V", "s1", "0", 24), ("R", "s1", "n1", 10), ("I", "0", "n1", 2), ("R", "n1", "n2", 20), ("R", "n2", "0", 30),
                ("R", "n2", "s2", 45), ("V", "s2", "0", 48)], ["s1", "n1", "n2", "s2"], "0")
    r["Q6"] = (V["n1"] - V["n2"]).real
    chk("T1Q6 Vx (sheet 10.4)", r["Q6"], 10.4, 0.01, note="exact 10.333 V (10 - 8 + 8.333)")
    # Q7
    I1, I3 = 10, -4; I2 = (I1 + 0.5 * I3) / 4
    r["Q7"] = (I1, I2, I3, 1 * (I1 - I2), 0.5 * (I2 - I3))
    chk("T1Q7 I2", I2, 2); chk("T1Q7 V1", 1 * (I1 - I2), 8); chk("T1Q7 V2", 0.5 * (I2 - I3), 3)
    # Q8
    V, _ = mna([("V", "T", "L", 45), ("V", "T", "TR", 120), ("R", "TR", "R", 15), ("R", "L", "b", 10), ("R", "b", "R", 5),
                ("V", "L", "mid", 20), ("R", "mid", "R", 5)], ["T", "L", "TR", "R", "b", "mid"], "b")
    Rth8 = 1 / (1 / 10 + 1 / (5 + 1 / (1 / 15 + 1 / 5)))
    r["Q8"] = (V["T"].real, Rth8)
    chk("T1Q8 VTh", V["T"].real, 63); chk("T1Q8 Rth", Rth8, 4.67, 0.002)
    # Q9
    el = [("V", "x0", "0", 120), ("R", "x0", "X", 30), ("R", "X", "0", 60), ("V", "X", "Y", -40), ("R", "Y", "a", 10), ("R", "a", "0", 30),
          ("V", "b", "0", -10), ("R", "a", "b", 1e-9)]
    V, _ = mna(el, ["x0", "X", "Y", "a", "b"], "0")
    Isc = ((V["a"] - V["b"]) / 1e-9).real
    RN = 1 / (1 / 30 + 1 / (1 / (1 / 30 + 1 / 60) + 10))
    r["Q9"] = (Isc, RN)
    chk("T1Q9 IN", Isc, 4.67, 0.002); chk("T1Q9 RN", RN, 15)
    # Q10
    Vth10 = 15.0; Rth10 = 1.0
    r["Q10"] = dict(P3=(Vth10 / (Rth10 + 3)) ** 2 * 3, Pmax=Vth10 ** 2 / (4 * Rth10), RLhalf=(3 + 2 * math.sqrt(2), 3 - 2 * math.sqrt(2)))
    chk("T1Q10 P(3)", r["Q10"]["P3"], 42.18, 0.001); chk("T1Q10 RL half", r["Q10"]["RLhalf"][0], 5.8, 0.01)
    chk("T1Q10 RL half2", r["Q10"]["RLhalf"][1], 0.172, 0.01)
    # Q11 supernode network
    el = [("R", "a", "b", 12.5), ("R", "c", "d", 20), ("R", "d", "e", 25), ("R", "c", "e", 10), ("V", "a", "c", 100), ("V", "b", "d", 150),
          ("I", "d", "a", 5), ("I", "e", "b", 10)]
    V, _ = mna(el, list("abcde"), "e")
    r["Q11"] = dict(v4=V["d"].real, Iba=((V["b"] - V["a"]) / 12.5).real, Icd=((V["c"] - V["d"]) / 20).real, Ice=(V["c"] / 10).real,
                    Ide=((V["d"]) / 25).real)
    chk("T1Q11 v4", V["d"].real, 63.06); chk("T1Q11 Iba", r["Q11"]["Iba"], 3.063); chk("T1Q11 Icd", r["Q11"]["Icd"], 0.586, 0.002)
    chk("T1Q11 Ice", r["Q11"]["Ice"], 7.477); chk("T1Q11 Ide", r["Q11"]["Ide"], 2.523, 0.002)
    # Q12
    el = [("R", "a", "p", 2), ("I", "p", "d", 4.5), ("R", "a", "q", 3), ("V", "q", "b", 5), ("V", "a", "e", -2.2), ("R", "d", "e", 9),
          ("R", "e", "b", 4), ("I", "e", "c", 2), ("R", "d", "r", 3), ("V", "r", "c", 3), ("R", "b", "s", 6), ("R", "s", "c", 1)]
    V, iv = mna(el, ["a", "b", "c", "d", "e", "p", "q", "r", "s"], "c")
    Iba = ((V["q"] - V["a"]) / 3).real  # current from b side through 3 ohm toward a
    Ibe = ((V["b"] - V["e"]) / 4).real; Ide = ((V["d"] - V["e"]) / 9).real; Idc = ((V["d"] - V["r"]) / 3).real; Icb = ((V["c"] - V["s"]) / 1).real
    # power DELIVERED by a source = (voltage rise in the direction of its current) x current
    P45 = 4.5 * (V["d"] - V["p"]).real          # 4.5 A flows p -> d through the source
    P2 = 2 * (V["c"] - V["e"]).real             # 2 A flows e -> c through the source
    P5 = 5 * Iba                                # b -> q through the 5 V source: enters at the - terminal, leaves at +  => delivers
    Iea = 4.5 - Iba                             # KCL at a (4.5 A leaves a towards d)
    P22 = -2.2 * Iea                            # + terminal is at e, current e -> a enters + => absorbs
    P3 = -3 * Idc                               # + terminal at r, current d -> r -> c enters + => absorbs
    r["Q12"] = dict(Iba=Iba, Ibe=Ibe, Ide=Ide, Idc=Idc, Icb=Icb, Iea=Iea, P45=P45, P2=P2, P5=P5, P22=P22, P3=P3)
    tot_del = P45 + P2 + P5 + max(P22, 0) + max(P3, 0)
    # resistor losses
    PR = 4.5 ** 2 * 2 + Iba ** 2 * 3 + Ide ** 2 * 9 + Ibe ** 2 * 4 + Idc ** 2 * 3 + Icb ** 2 * 7
    r["Q12"]["PR"] = PR
    chk("T1Q12 Iba", Iba, 2.839); chk("T1Q12 Ibe", Ibe, 0.329, 0.003); chk("T1Q12 Ide", Ide, 3.332); chk("T1Q12 Icd", Idc, 1.168); chk("T1Q12 Icb", Icb, 3.168)
    chk("T1Q12 Iea", Iea, 1.661, 0.002); chk("T1Q12 P4.5A", P45, 185.363, 0.002); chk("T1Q12 P2A", P2, 46.978, 0.002); chk("T1Q12 P5V", P5, 14.193, 0.002)
    chk("T1Q12 P2.2V", P22, -3.655, 0.003); chk("T1Q12 P3V", P3, -3.503, 0.003); chk("T1Q12 total", PR, 239.376, 0.002)
    # Q13
    R = [("R", "A", "C", 5), ("R", "C", "B", 5), ("R", "A", "B", 5), ("R", "A", "A'", 4.75), ("R", "B", "B'", 4.5), ("R", "C", "C'", 3.25),
         ("R", "A'", "C'", 1.5), ("R", "B'", "C'", 2.5), ("R", "A'", "B'", 1.0)]
    V, _ = mna(R + [("I", "B", "A", 1)], ["A", "B", "C", "A'", "B'", "C'"], "B")
    r["Q13"] = V["A"].real
    chk("T1Q13 RAB", V["A"].real, 2.5, 0.002)
    # inner delta -> star
    d = (1.0, 1.5, 2.5); S = sum(d)
    r["Q13 star"] = (1.0 * 1.5 / S, 1.0 * 2.5 / S, 1.5 * 2.5 / S)
    # Q14
    V, iv = mna([("R", "c", "a", 15), ("R", "a", "b", 20), ("R", "c", "b", 35), ("R", "c", "d", 8), ("R", "b", "d", 25), ("V", "a", "d", 180)],
                ["a", "b", "c", "d"], "d")
    cur = dict(Iac=((V["a"] - V["c"]) / 15).real, Iab=((V["a"] - V["b"]) / 20).real, Ibc=((V["b"] - V["c"]) / 35).real,
               Icd=(V["c"] / 8).real, Ibd=(V["b"] / 25).real)
    cur["Is"] = cur["Iac"] + cur["Iab"]
    r["Q14"] = dict(cur, Vb=V["b"].real, Vc=V["c"].real)
    # star-delta check on a-c-b delta
    Ra, Rb_, Rc_ = 15 * 20 / 70, 20 * 35 / 70, 15 * 35 / 70    # star legs: a-leg, b-leg, c-leg for delta (ca=15, ab=20, bc=35)
    Rtot = Ra + 1 / (1 / (Rb_ + 25) + 1 / (Rc_ + 8))
    r["Q14"]["Rtot_star_delta"] = Rtot; r["Q14"]["star"] = (Ra, Rb_, Rc_)
    chk("T1Q14 Isource", cur["Is"], 11.978, 0.001); chk("T1Q14 Iac", cur["Iac"], 7.573, 0.001); chk("T1Q14 Iab", cur["Iab"], 4.405, 0.001)
    chk("T1Q14 Ibc", cur["Ibc"], 0.729, 0.003); chk("T1Q14 Icd", cur["Icd"], 8.301, 0.001); chk("T1Q14 Ibd", cur["Ibd"], 3.676, 0.001)
    chk("T1Q14 R_total=E/I", Rtot, 180 / 11.978, 0.002)
    r["Q14"]["P"] = {k: cur[k] ** 2 * R_ for k, R_ in (("Iac", 15), ("Iab", 20), ("Ibc", 35), ("Icd", 8), ("Ibd", 25))}
    r["Q14"]["Ptot"] = sum(r["Q14"]["P"].values()); r["Q14"]["Psup"] = 180 * cur["Is"]
    return r


# =============================================================== Tutorial 2
def t2():
    r = {}
    # Q1 capacitor 8 uF, i = 20 mA (0-4 ms), 0 (4-8), -10 mA (8-16)
    C = 8e-6
    vC4 = 20e-3 * 4e-3 / C; vC16 = vC4 + (-10e-3) * 8e-3 / C
    r["Q1a"] = dict(vC4=vC4, vC16=vC16, pmax=vC4 * 20e-3, pmin=vC4 * -10e-3)
    chk("T2Q1a v(4ms)", vC4, 10); chk("T2Q1a v(16ms)", vC16, 0, 1, "zero"); chk("T2Q1a p+", vC4 * 20e-3, 0.2)
    L = 40e-3
    iL4 = 20e-3 * 4e-3 / L; iL16 = iL4 + (-10e-3) * 8e-3 / L
    r["Q1b"] = dict(iL4=iL4, iL16=iL16, pmax=iL4 * 20e-3, pmin=iL4 * -10e-3)
    chk("T2Q1b i(4ms)", iL4, 2e-3); chk("T2Q1b p+ uW", iL4 * 20e-3 * 1e6, 40); chk("T2Q1b p- uW", iL4 * -10e-3 * 1e6, -20)
    # Q2
    Iin = 15 / 30; V1 = Iin * 20; V2 = Iin * 10; Cval = (5e-3 - 0.5 * 16e-3 * Iin ** 2) / (0.5 * V1 ** 2)
    r["Q2"] = dict(Iin=Iin, V1=V1, V2=V2, C=Cval, EL=0.5 * 16e-3 * Iin ** 2)
    chk("T2Q2 Iin", Iin, 0.5); chk("T2Q2 C uF", Cval * 1e6, 60)
    # Q3
    r["Q3"] = dict(Vin=2 * 10, I1=2, I2=0, EL=0.5 * 5e-3 * 4, EC=0.5 * 25e-6 * 20 ** 2)
    chk("T2Q3 EL mJ", 0.5 * 5e-3 * 4 * 1e3, 10); chk("T2Q3 EC mJ", 0.5 * 25e-6 * 400 * 1e3, 5)
    # Q4
    R4 = 120 / 30; L4 = R4 / 50; tau = 1 / 50; E0 = 0.5 * L4 * 30 ** 2; t50 = math.log(2) / 100
    r["Q4"] = dict(R=R4, L=L4, tau=tau, E0=E0, t50=t50)
    chk("T2Q4 L", L4, 0.08); chk("T2Q4 E0", E0, 36); chk("T2Q4 t50 ms", t50 * 1e3, 6.93, 0.001)
    # Q5 switch opens
    # before: node S: 2 = V/12 + V/20 + (V-20)/5 + V/6
    VS = (2 + 20 / 5) / (1 / 12 + 1 / 20 + 1 / 5 + 1 / 6); iL0 = VS / 6
    Rth = 1 / (1 / 20 + 1 / 5); Voc = 20 * Rth / 5; Rtot = Rth + 6; iLf = Voc / Rtot; tau5 = 0.5 / Rtot
    r["Q5"] = dict(VS=VS, iL0=iL0, Rth=Rth, Voc=Voc, Rtot=Rtot, iLf=iLf, tau=tau5, v0=0.5 * (-1 / tau5) * (iL0 - iLf))
    chk("T2Q5 iL0", iL0, 2); chk("T2Q5 tau", tau5, 0.05); chk("T2Q5 v(0+)", r["Q5"]["v0"], -4)
    # Q6
    r["Q6"] = dict(vC0=10e-3 * 4e3, tau=(4e3 + 6e3) * 10e-6, iC0=-40 / 10e3)
    chk("T2Q6 vC0", 40, 40); chk("T2Q6 iC0 mA", -4, -4)
    # Q7
    R7, L7, C7, V7 = 200, 2, 5e-6, 10
    a = R7 / (2 * L7); w0 = 1 / math.sqrt(L7 * C7); wd = math.sqrt(w0 ** 2 - a ** 2); Rc = 2 * math.sqrt(L7 / C7)
    r["Q7"] = dict(alpha=a, w0=w0, wd=wd, amp=V7 / (wd * L7), Rc=Rc, Rext=Rc - R7)
    chk("T2Q7 wd", wd, 312.25, 0.0005); chk("T2Q7 amp", V7 / (wd * L7), 0.01601, 0.001); chk("T2Q7 Rext", Rc - R7, 1064.9, 0.0005)
    R7f, L7f, C7f = 100, 1, 10e-6
    r["Q7 figure"] = dict(amp=V7 / (math.sqrt(1 / (L7f * C7f) - (R7f / 2 / L7f) ** 2) * L7f), Rext=2 * math.sqrt(L7f / C7f) - R7f)
    # Q8
    Rb = 250 + 600 + 1 / (1 / 2000 + 1 / 500); Req = 1 / (1 / 1250 + 1 / Rb); tau8 = Req * 4e-6
    vo_after0 = 100 / Rb * 400 * (400 / 500) * 1  # not used
    iloop = 100 / Rb; vR = iloop * (1 / (1 / 2000 + 1 / 500)); vo0 = vR * 400 / 500
    r["Q8"] = dict(pre=(120 * 1250 / 1500, 120 * 400 / 1000 * 400 / 500), vo0p=vo0, tau=tau8, vc13=100 * math.exp(-1.3e-3 / tau8),
                   vo13=vo0 * math.exp(-1.3e-3 / tau8), Req=Req, Rb=Rb)
    chk("T2Q8 vc(0-)", 100, 100); chk("T2Q8 vo(0-)", 38.4, 38.4); chk("T2Q8 vo(0+)", vo0, 25.6); chk("T2Q8 vc(1.3ms)", r["Q8"]["vc13"], 59.45, 0.001)
    chk("T2Q8 vo(1.3ms) (sheet 25.6)", r["Q8"]["vo13"], 25.6, 0.01, "sheet's 25.6 V cannot be right: vo decays with the same time constant")
    # Q9
    Rth9 = 1 / (1 / 1250 + 1 / 250); tau9 = Rth9 * 4e-6; vc13 = 100 * (1 - math.exp(-1.3e-3 / tau9))
    r["Q9"] = dict(Rth=Rth9, tau=tau9, vc13=vc13)
    chk("T2Q9 vo(0+)", 38.4, 38.4); chk("T2Q9 vc(1.3ms) (sheet 70.0)", vc13, 70.0, 0.01, "sheet's 70.0 V does not follow from tau=0.833 ms; exact 78.99 V")
    # Q10
    R, L, C, V = 50, 0.1, 50e-6, 100
    a = R / (2 * L); w0 = 1 / math.sqrt(L * C); wd = math.sqrt(w0 ** 2 - a ** 2); Rc = 2 * math.sqrt(L / C)
    r["Q10"] = dict(Rc=Rc, zeta=R / Rc, w0=w0, wd=wd, alpha=a, A=V / (wd * L), vL=(V, a * V / wd), phase=math.degrees(math.atan2(wd, a)))
    chk("T2Q10 Rc", Rc, 89.44, 0.001); chk("T2Q10 zeta", R / Rc, 0.559, 0.001); chk("T2Q10 wn", w0, 447.2, 0.001); chk("T2Q10 wd", wd, 370.8, 0.001)
    chk("T2Q10 A", V / (wd * L), 2.7, 0.002)
    # Q11
    Lq, Rq, Cq = 2, 36, 1 / 450
    a = Rq / (2 * Lq); w0 = math.sqrt(1 / (Lq * Cq)); wd = math.sqrt(w0 ** 2 - a ** 2)
    i0 = 10; di0 = (900 - Rq * i0 - 70) / Lq; B = (di0 + a * i0) / wd
    r["Q11"] = dict(alpha=a, w0=w0, wd=wd, di0=di0, B=B, amp=math.hypot(i0, B), ph=math.degrees(math.atan2(i0, B)))
    chk("T2Q11 amp", math.hypot(i0, B), 28.87, 0.001); chk("T2Q11 phase", math.degrees(math.atan2(i0, B)), 20.27, 0.001)
    # Q12
    R, L, C = 5, 0.1e-3, 8e-6
    a = 1 / (2 * R * C); w0 = 1 / math.sqrt(L * C); wd = math.sqrt(w0 ** 2 - a ** 2); z = a / w0
    r["Q12"] = dict(alpha=a, w0=w0, wd=wd, zeta=z, Vamp=10 / (C * wd), th=math.degrees(math.acos(z)), k=1 / math.sqrt(1 - z * z))
    chk("T2Q12 alpha", a, 12500); chk("T2Q12 wd (sheet 33119.1)", wd, 33119.1, 0.002, "sheet rounds zeta to 0.35; exact 33071.9")
    chk("T2Q12 Vamp (sheet 37.74)", 10 / (C * wd), 37.74, 0.003, "exact 37.80 V")
    return r


# =============================================================== Tutorial 3
def t3():
    r = {}
    r["Q2"] = dict(avg=(10 + 20) / 3, rms=math.sqrt((100 + 400) / 3), P=(100 + 400) / 3 / 10)
    chk("T3Q2 rms", r["Q2"]["rms"], 12.909, 0.0005); chk("T3Q2 P", r["Q2"]["P"], 16.667, 0.0005)
    Z = 9 + 12j; Vm = 28.3 * abs(Z)
    r["Q3"] = dict(Z=P(Z), Vm=Vm, L=12 / 377)
    chk("T3Q3 Vm", Vm, 424.5, 0.0005); chk("T3Q3 L mH", 12 / 377 * 1e3, 31.83, 0.0005)
    Vrms = 170 / math.sqrt(2)
    r["Q4"] = dict(Vrms=Vrms, VR=Vrms * math.cos(math.radians(30)), VC=Vrms * math.sin(math.radians(30)))
    chk("T3Q4 VR", r["Q4"]["VR"], 104.103, 0.0005); chk("T3Q4 VC", r["Q4"]["VC"], 60.14, 0.001, "sheet 60.14 V; exact 60.10 V")
    Z = 6 - 8j; V = 141 / math.sqrt(2); I = V / abs(Z); S = V * V / np.conj(Z)
    r["Q5"] = dict(Irms=I, S=S, pf=6 / 10, C=1 / (377 * 8))
    chk("T3Q5 Irms", I, 9.97, 0.001); chk("T3Q5 S real", S.real, 596.41, 0.001); chk("T3Q5 S imag", S.imag, -795.2, 0.001)
    chk("T3Q5 pf (sheet 0.596)", 0.6, 0.596, 0.01, "pf = cos(53.13 deg) = 0.600 exactly; 0.596 is the sheet's rounding")
    chk("T3Q5 C uF", 1e6 / (377 * 8), 331.56, 0.0005)
    i1 = 10 * cmath.exp(-1j * math.radians(45)); i2 = 20 * cmath.exp(1j * math.radians(30)); i3 = 5 * cmath.exp(1j * math.radians(60))
    It = i1 + i2 + i3; r["Q6"] = dict(I=P(It), Im=abs(It) * math.sqrt(2))
    chk("T3Q6 |I|", abs(It), 27.85, 0.001); chk("T3Q6 phase", P(It)[1], 15.10, 0.002); chk("T3Q6 Im", abs(It) * math.sqrt(2), 39.39, 0.001)
    R, L, C, w, Vm = 40, 0.13, 10e-6, 1000, 150
    XL, XC = w * L, 1 / (w * C); Z = R + 1j * (XL - XC); Vr = Vm / math.sqrt(2); Ic = Vr / Z
    r["Q7"] = dict(Z=P(Z), I=P(Ic), VL=abs(Ic) * XL, VC=abs(Ic) * XC, VLpk=abs(Ic) * XL * math.sqrt(2), VCpk=abs(Ic) * XC * math.sqrt(2))
    chk("T3Q7 |I|", abs(Ic), 2.12, 0.002); chk("T3Q7 VC peak", r["Q7"]["VCpk"], 300, 0.001)
    chk("T3Q7 VL peak (sheet 389.75)", r["Q7"]["VLpk"], 389.75, 0.001, "exact 389.99 V (sheet rounds I to 2.12 A)")
    I2 = abs(Ic) ** 2
    r["Q8"] = dict(P=I2 * R, Q=I2 * (XL - XC), QC=-I2 * XC, QL=I2 * XL, pf=R / abs(Z))
    chk("T3Q8 P (sheet 179.79)", I2 * R, 179.79, 0.002); chk("T3Q8 Q", I2 * (XL - XC), 134.8, 0.002); chk("T3Q8 pf", R / abs(Z), 0.8, 0.0001)
    V1 = 100; V2 = 100 * cmath.exp(-1j * math.radians(60)); Z1 = 6 + 8j; Z2 = 6 - 8j; Z3 = 10j
    Vn = (V1 / Z1 + V2 / Z2) / (1 / Z1 + 1 / Z2 + 1 / Z3)
    r["Q9"] = dict(Vn=P(Vn), I3=P(Vn / Z3), I1=P((V1 - Vn) / Z1), I2=P((V2 - Vn) / Z2))
    chk("T3Q9 |I3|", abs(Vn / Z3), 11.774, 0.0005); chk("T3Q9 phase", P(Vn / Z3)[1], -80.2, 0.001)
    # Q10
    w = 400; XL = w * 0.1; XC = 1 / (w * 25e-6)
    Zrc = 100 - 1j * XC; Zab = 1 / (1 / Zrc + 1 / (1j * XL))
    X = -Zab.imag; Cn = 1 / (w * abs(X)); Itot = 141 / (3 + Zab.real)
    r["Q10"] = dict(XL=XL, XC=XC, Zab=Zab, X=X, C=Cn, Ipk=Itot)
    chk("T3Q10 Zab real", Zab.real, 11.7647, 0.0005); chk("T3Q10 Zab imag", Zab.imag, 47.05, 0.001); chk("T3Q10 C uF", Cn * 1e6, 53.13, 0.001)
    chk("T3Q10 Ipk (sheet 9.5487)", Itot, 9.5487, 0.0015)
    # Q11, Q12
    Z1 = 1 + 1j; Z2 = 1 - 1j; Z3 = 1 + 2j; V1 = 10; V2 = 10 * cmath.exp(-1j * math.radians(60))
    A = np.array([[Z1 + Z3, -Z3], [-Z3, Z2 + Z3]]); b = np.array([V1, -V2])
    I1, I2 = np.linalg.solve(A, b); Iz = I1 - I2
    Zth = Z1 * Z2 / (Z1 + Z2); Vth = (V1 * Z2 + V2 * Z1) / (Z1 + Z2)
    r["Q11"] = dict(I1=P(I1), I2=P(I2), Iz=P(Iz), Zth=Zth, Vth=P(Vth))
    chk("T3Q11 |I1|", abs(I1), 1.58, 0.005); chk("T3Q11 |I2|", abs(I2), 6.05, 0.002); chk("T3Q11 |Iz|", abs(Iz), 4.82, 0.003)
    Vn = (V1 / Z1 + V2 / Z2) / (1 / Z1 + 1 / Z2 + 1 / Z3)
    chk("T3Q11 nodal = mesh", abs((Vn / Z3) - Iz), 0, 1, "equal")
    S1 = V1 * np.conj((V1 - Vn) / Z1); S2 = V2 * np.conj((V2 - Vn) / Z2)
    r["Q12"] = dict(S1=S1, S2=S2)
    chk("T3Q12 P1", S1.real, 7.92, 0.002); chk("T3Q12 P2", S2.real, 54.57, 0.002)
    chk("T3Q12 Q1 (sheet +26)", S1.imag, 26.0, 0.01, "sheet swaps the Q and S entries of the two sources: Q1 = -13.73 VAr, S1 = 15.85 VA")
    chk("T3Q12 S1 (sheet 60.5)", abs(S1), 60.5, 0.01, "S1 = 15.85 VA; 60.55 VA is source 2")
    Z3m = np.conj(Zth); Iz = Vth / (Zth + Z3m); Pmax = abs(Iz) ** 2 * Z3m.real
    Vn = (V1 / Z1 + V2 / Z2) / (1 / Z1 + 1 / Z2 + 1 / Z3m)
    S1m = V1 * np.conj((V1 - Vn) / Z1); S2m = V2 * np.conj((V2 - Vn) / Z2)
    r["Q12 max"] = dict(Z3=Z3m, Pmax=Pmax, S1=S1m, S2=S2m)
    chk("T3Q12 Pmax", Pmax, 46.65, 0.001); chk("T3Q12 P each source at max (sheet 23.32)", S1m.real, 23.32, 0.01, "each source delivers 37.5 W; 23.3 W is half of Pmax")
    return r


# =============================================================== Tutorial 4
def t4():
    r = {}
    def band(w0, Q):
        s = math.sqrt(1 + 1 / (4 * Q * Q)); return w0 * (s - 1 / (2 * Q)), w0 * (s + 1 / (2 * Q))
    w0 = 1 / math.sqrt(0.01 * 100e-6); Q = w0 * 0.01 / 10; BW = w0 / Q; w1, w2 = band(w0, Q)
    r["Q1"] = (w0, Q, BW, w1, w2); chk("T4Q1 w1", w1, 618.03, 0.0005); chk("T4Q1 w2", w2, 1618.03, 0.0005)
    w0 = 1 / math.sqrt(1 * 1e-6); Q = 10 * math.sqrt(1e-6 / 1); BW = w0 / Q; w1, w2 = band(w0, Q)
    r["Q2"] = (w0, Q, BW, w1, w2); chk("T4Q2 Q", Q, 0.01, 0.001); chk("T4Q2 BW", BW, 1e5, 0.001); chk("T4Q2 w1", w1, 10, 0.01); chk("T4Q2 w2", w2, 100010, 0.001)
    r["Q3"] = dict(Q=50, w0=50 * 400, L=50 * 100 / 20000, C=1 / (20000 ** 2 * 0.25))
    chk("T4Q3 L", r["Q3"]["L"], 0.25); chk("T4Q3 C nF", r["Q3"]["C"] * 1e9, 10)
    chk("T4Q4 R", 1 / (2 * math.pi * 1000 * 1.6e-6), 100, 0.01)
    chk("T4Q5 C nF", 1e9 / (2 * math.pi * 20000 * 1000), 7.95, 0.002)
    w0 = 1 / math.sqrt(1 * 1e-6); Q = w0 * 1 / 1000; BW = 1000 / 1; w1, w2 = band(w0, Q)
    r["Q6"] = (w0, Q, BW, w1, w2); chk("T4Q6 w1", w1, 618, 0.001); chk("T4Q6 w2 (sheet 1818)", w2, 1818, 0.01, "sheet's 1818 is a typo: w2 = w1 + BW = 1618")
    w07 = 2 * math.pi * 400; L7 = 1 / (w07 ** 2 * 200e-6); r["Q7"] = L7; chk("T4Q7 L uH", L7 * 1e6, 791.6, 0.0005)
    x = 1.02; Q8 = math.sqrt(99) / (x - 1 / x); x2 = 0.98; Q8b = math.sqrt(99) / (1 / x2 - x2)
    w08 = 2 * math.pi * 100e6; L8 = Q8 * 100 / w08; C8 = 1 / (w08 ** 2 * L8)
    r["Q8"] = dict(Q102=Q8, Q98=Q8b, L=L8, C=C8)
    chk("T4Q8 Q", Q8, 251.2, 0.001); chk("T4Q8 L uH", L8 * 1e6, 39.98, 0.001); chk("T4Q8 C pF", C8 * 1e12, 0.0634, 0.002)
    # three phase
    Iab = 10 * cmath.exp(-1j * math.radians(30)); Ia = Iab * math.sqrt(3) * cmath.exp(-1j * math.radians(30))
    S = 3 * 220 * 10 * cmath.exp(1j * math.radians(30)); Zph = 220 / 10
    r["Q9"] = dict(Ia=P(Ia), S=S, R=Zph * math.cos(math.radians(30)), X=Zph * math.sin(math.radians(30)))
    chk("T4Q9 P", S.real, 5715.6, 0.0005); chk("T4Q9 Q (sheet 2857.8)", S.imag, 2857.8, 0.01, "sheet's Q is P/2; correct Q = S sin30 = 3300 VAr")
    chk("T4Q9 R", Zph * math.cos(math.radians(30)), 19.05, 0.001)
    Zd = 15 + 20j; Iph = 220 / abs(Zd); Ph = Iph ** 2 * 15; Qh = Iph ** 2 * 20
    r["Q10"] = dict(Iph=Iph, Iline=Iph * math.sqrt(3), Ph=Ph, Qh=Qh)
    chk("T4Q10 Pph", Ph, 1161.6, 0.001); chk("T4Q10 Qph", Qh, 1548.8, 0.001)
    Vl, P3, Il = 208, 1800, 10; cphi = P3 / (math.sqrt(3) * Vl * Il); Zp = Vl / math.sqrt(3) / Il
    r["Q11"] = dict(cphi=cphi, Zp=Zp, R=Zp * cphi, X=Zp * math.sqrt(1 - cphi ** 2))
    chk("T4Q11 R", Zp * cphi, 6, 0.003); chk("T4Q11 X", Zp * math.sqrt(1 - cphi ** 2), 10.39, 0.003)
    Van = 20 * cmath.exp(1j * math.radians(30)); Vcn = 20 * cmath.exp(1j * math.radians(150)); Vac = Van - Vcn
    r["Q12"] = dict(Ia=P(Van / (4 * cmath.exp(1j * math.radians(60)))), Vac=P(Vac))
    chk("T4Q12 Vac", abs(Vac), 34.64, 0.001)
    return r


# =============================================================== Tutorial 8
def t8():
    r = {}
    # Q6, Q7
    f = 50; ns = 120 * f / 4; r["Q6"] = dict(ns=ns, nr=ns * 0.94, f2=0.06 * f)
    chk("T8Q6 nr", ns * 0.94, 1410); chk("T8Q6 f2", 0.06 * f, 3)
    r["Q7"] = dict(P=4, s=(1500 - 1440) / 1500, f2=(1500 - 1440) / 1500 * 50)
    chk("T8Q7 s", 0.04, 0.04); chk("T8Q7 f2", 2.0, 2)
    # Q8
    ws = 2 * math.pi * 1500 / 60; E = 120; R2 = 0.2; X20 = 1.0
    def rotor(s, Rext=0.0):
        R = R2 + Rext; Z = R + 1j * s * X20; I = s * E / abs(Z); pf = R / abs(Z); T = 3 * I ** 2 * R / s / ws
        return I, pf, T
    I, pf, T = rotor(1); r["Q8 start"] = (I, pf, T)
    chk("T8Q8 start I", I, 117.67, 0.001); chk("T8Q8 start pf", pf, 0.196, 0.002); chk("T8Q8 start T", T, 52.9, 0.001)
    I, pf, T = rotor(0.04); r["Q8 FL"] = (I, pf, T)
    chk("T8Q8 FL I", I, 23.53, 0.001); chk("T8Q8 FL pf", pf, 0.98, 0.001); chk("T8Q8 FL T", T, 52.87, 0.001)
    I, pf, T = rotor(1, 1.0); r["Q8b"] = (I, pf, T)
    chk("T8Q8b I", I, 76.82, 0.001); chk("T8Q8b pf", pf, 0.768, 0.001); chk("T8Q8b T", T, 135.25, 0.001)
    # Q9
    Pcu0 = 3 * (8 / math.sqrt(3)) ** 2 * 1.2; core = 660 - Pcu0 - 420
    Pcu1 = 3 * (18 / math.sqrt(3)) ** 2 * 1.2; Pg = 11200 - Pcu1 - core
    Prot = Pg - 10000; Poh = Prot - 420; s = Poh / Pg; N = 1500 * (1 - s)
    ws = 2 * math.pi * 1500 / 60; Tint = Pg / ws; Tsh = 10000 / (2 * math.pi * N / 60)
    r["Q9"] = dict(Pcu0=Pcu0, core=core, Pcu1=Pcu1, Pg=Pg, Prot=Prot, Poh=Poh, s=s, N=N, Tint=Tint, Tsh=Tsh, eta=10000 / 11200)
    chk("T8Q9 core", core, 163.3, 0.001); chk("T8Q9 Prot", Prot, 648, 0.001); chk("T8Q9 Poh", Poh, 228, 0.001)
    chk("T8Q9 N (sheet 1468.2)", N, 1468.2, 0.0005); chk("T8Q9 Tint", Tint, 67.8, 0.001); chk("T8Q9 Tsh", Tsh, 65, 0.001); chk("T8Q9 eta", 100 * 10000 / 11200, 89.2, 0.002)
    # Q10
    Vph = 440 / math.sqrt(3); ns = 120 * 60 / 4; ws = 2 * math.pi * ns / 60; s = 0.025
    r1, x1, r2, x2 = 0.10, 0.35, 0.12, 0.40
    Z2 = (r1 + r2 / s) + 1j * (x1 + x2); I2 = Vph / Z2; I0 = 18 * (0.089 - 1j * math.sqrt(1 - 0.089 ** 2)); I1 = I2 + I0
    Pg = 3 * abs(I2) ** 2 * r2 / s; T = Pg / ws; Pm = Pg * (1 - s); Pout = Pm - 950
    Pcu1 = 3 * abs(I1) ** 2 * r1; Pcu2 = s * Pg; loss = Pcu1 + Pcu2 + 1200 + 950; eta = Pout / (Pout + loss)
    Pin_direct = 3 * Vph * abs(I1) * math.cos(cmath.phase(I1))
    r["Q10"] = dict(I2=P(I2), I1=P(I1), pf=math.cos(cmath.phase(I1)), Pg=Pg, T=T, Pm=Pm, Pout=Pout, hp=Pout / 746, eta=eta, Pin_direct=Pin_direct,
                    eta_direct=Pout / Pin_direct, loss=loss, Pcu1=Pcu1, Pcu2=Pcu2)
    chk("T8Q10 I1", abs(I1), 58.2, 0.001); chk("T8Q10 pf", math.cos(cmath.phase(I1)), 0.895, 0.005); chk("T8Q10 T", T, 201, 0.005)
    chk("T8Q10 hp (sheet 48.25)", Pout / 746, 48.25, 0.003); chk("T8Q10 eta (sheet 89.6)", 100 * eta, 89.6, 0.002)
    # Q11 exact circuit with Thevenin equivalent
    Vph = 400 / math.sqrt(3); ws = 2 * math.pi * 1500 / 60
    r1, x1, r2, x2, xm = 0.15, 0.45, 0.12, 0.45, 0.0,
    r1, x1, r2, x2, xm = 0.15, 0.45, 0.12, 0.45, 28.5; Fix = 400; a = 1.2
    def exact(s, rext=0):
        Zr = (r2 + rext) / s + 1j * x2; Zp = 1 / (1 / (1j * xm) + 1 / Zr); Zin = r1 + 1j * x1 + Zp; I1 = Vph / Zin; I2 = I1 * Zp / Zr
        return I1, I2
    Zth = (1j * xm) * (r1 + 1j * x1) / (r1 + 1j * (x1 + xm)); Vth = Vph * 1j * xm / (r1 + 1j * (x1 + xm)); Rth, Xth = Zth.real, Zth.imag
    Zk = math.sqrt(Rth ** 2 + (Xth + x2) ** 2)
    I1, I2 = exact(0.04); Pg = 3 * abs(I2) ** 2 * r2 / 0.04; Pm = Pg * 0.96; Pout = Pm - Fix; Pin = 3 * (Vph * np.conj(I1)).real
    Tout = Pout / (ws * 0.96)
    sm = r2 / Zk; Tmax = 3 / (2 * ws) * abs(Vth) ** 2 / (Rth + Zk); Pm_max = Tmax * ws * (1 - sm)
    Is, I2s = exact(1.0); Ts = 3 * abs(I2s) ** 2 * r2 / ws
    Rext = (Zk - r2) / a ** 2
    r["Q11"] = dict(Zth=Zth, Vth=abs(Vth), I1=P(I1), I2=P(I2), Pg=Pg, Tdev=Pg / ws, Tout=Tout, eta=Pout / Pin, sm=sm, Tmax=Tmax, Pm_max=Pm_max,
                    Pout_max=Pm_max - Fix, Is=P(Is), I2s=P(I2s), Ts=Ts, Rext=Rext, Rext_ref=Zk - r2, Pin=Pin, Pout=Pout)
    chk("T8Q11 I1", abs(I1), 71.06, 0.002); chk("T8Q11 Tout (sheet 274.12)", Tout, 274.12, 0.002); chk("T8Q11 eta", 100 * Pout / Pin, 90.36, 0.001)
    chk("T8Q11 sm", sm, 0.1326, 0.002); chk("T8Q11 Tmax (sheet 469.1)", Tmax, 469.1, 0.002); chk("T8Q11 Pout at Tmax (sheet 63515)", Pm_max - Fix, 63515.3, 0.01)
    chk("T8Q11 I2 start (sheet 243.94)", abs(I2s), 243.94, 0.001); chk("T8Q11 Tstart", Ts, 136.4, 0.002); chk("T8Q11 Rext", Rext, 0.5452, 0.001)
    return r


def main():
    out = {"T1": t1(), "T2": t2(), "T3": t3(), "T4": t4(), "T8": t8()}
    bad = [x for x in RESULTS if not x[0]]
    print(f"{len(RESULTS)} comparisons with the printed answers: {len(RESULTS) - len(bad)} agree, {len(bad)} differ")
    for ok, name, got, printed, note in RESULTS:
        if not ok:
            print(f"  DIFF {name}: computed {got:.4f} vs printed {printed}   {note}")
    return out


if __name__ == "__main__":
    import json, sys
    o = main()
    if "-v" in sys.argv:
        for k, v in o.items():
            print(k, v)
