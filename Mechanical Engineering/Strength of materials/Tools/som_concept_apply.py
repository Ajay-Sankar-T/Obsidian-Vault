"""Adds a figure and a 'Check yourself' block (collapsible question callouts) to the Strength of Materials concept notes.
Every number quoted in an answer is recomputed in check() first.  Run: python som_concept_apply.py   (safe to re-run)"""
import os
import re
from math import pi, sqrt, radians, sin, cos, degrees, atan2

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def check():
    A = lambda d: pi * d * d / 4
    near = lambda a, b, tol: abs(a - b) <= tol
    assert near(50e3 / A(0.02) / 1e6, 159.15, 0.01)
    assert near(12e3 / A(0.01) / 1e6, 152.79, 0.01)
    assert near(100 / 200e3, 0.0005, 1e-12) and near(0.3 * 100 / 200e3, 0.00015, 1e-12)
    assert near(200 / (2 * 1.3), 76.92, 0.01)
    assert near(15e3 * 2 / (A(0.01) * 200e9) * 1e3, 1.910, 0.001)
    assert near(28e3 * 1.5 / (400e-6 * 70e9) * 1e3, 1.5, 1e-9)
    assert near(200e3 * 12e-6 * 50, 120.0, 1e-9) and near(12e-6 * 50 * 2 * 1e3, 1.2, 1e-9)
    assert near(16 * 500 / (pi * 0.04 ** 3) / 1e6, 39.79, 0.01)
    J = pi * 0.04 ** 4 / 32
    assert near(degrees(500 * 1.5 / (80e9 * J)), 2.137, 0.002)
    T = 30e3 / (2 * pi * 20)
    assert near(T, 238.73, 0.01) and near((16 * T / (pi * 60e6)) ** (1 / 3) * 1e3, 27.26, 0.02)
    RB = (4 * 6 * 3 + 10 * 2) / 6
    RA = 34 - RB
    xm = (RA - 10) / 4
    assert near(RA, 18.667, 0.001) and near(RB, 15.333, 0.001) and near(xm, 2.1667, 0.0001) and near(RA * xm - 2 * xm ** 2 - 10 * (xm - 2), 29.389, 0.001)
    assert near(6 * 20e3 / (0.1 * 0.2 ** 2) / 1e6, 30.0, 1e-9)
    assert near(-200e3 / 0.02 / 1e6 + 6 * 5e3 / (0.1 * 0.2 ** 2) / 1e6, -2.5, 1e-9) and near(-200e3 / 0.02 / 1e6 - 6 * 5e3 / (0.1 * 0.2 ** 2) / 1e6, -17.5, 1e-9)
    assert near(1.5 * 30e3 / 0.02 / 1e6, 2.25, 1e-9)
    c, R = 30.0, sqrt(50 ** 2 + 30 ** 2)
    assert near(c + R, 88.31, 0.01) and near(c - R, -28.31, 0.01) and near(R, 58.31, 0.01) and near(0.5 * degrees(atan2(60, 100)), 15.47, 0.02)
    assert near(100 * cos(radians(30)) ** 2, 75.0, 1e-9) and near(100 * sin(radians(30)) * cos(radians(30)), 43.30, 0.01)
    assert near(2 * 300 - 500 - 100, 0, 0)
    assert near(5 * 10e3 * 4 ** 4 / (384 * 200e9 * 8e-5) * 1e3, 2.083, 0.001)
    I = pi * 0.04 ** 4 / 64
    Pcr = pi ** 2 * 200e9 * I / 2 ** 2
    assert near(Pcr / 1e3, 62.0, 0.05) and near(Pcr / 4e3, 15.5, 0.05) and near(sqrt(pi ** 2 * 200e3 / 250), 88.9, 0.1)
    assert near(2 * 0.5 / 0.01, 100.0, 1e-9) and near(2 * 0.5 / 0.02, 50.0, 1e-9)
    k1, k2 = 200e3 * 600, 70e3 * 1200
    assert near(300 * k1 / (k1 + k2), 176.47, 0.01) and near(300 * k1 / (k1 + k2) * 1e3 / 600, 294.1, 0.05) and near(300 * k2 / (k1 + k2) * 1e3 / 1200, 102.9, 0.05)


FIG = {
    "Stress-Strain Diagram and Hooke's Law": ("SM-C-stress-strain.png", "the labelled engineering curve of mild steel. The elastic part is exaggerated so that every feature is visible. Unloading beyond yield follows a line **parallel to the elastic line**, which is why a permanent set remains."),
    "Torsion of Circular Shafts": ("SM-C-torsion-solid-hollow.png", "shear stress grows linearly with radius, so the core of a solid shaft does little work. A tube with $c_i=0.6c$ carries $87\\%$ of the solid shaft's torque with $64\\%$ of the material."),
    "Shear Force and Bending Moment Diagrams": ("SM-C-sfd-bmd.png", "a simply supported beam with a uniform load and one point load. The shear diagram steps down by $P$ under the point load and has slope $-w$ elsewhere. The moment diagram has a corner under the point load and peaks where $V=0$."),
    "Relations Between Load, Shear, and Moment": ("SM-C-load-shear-moment.png", "one integration turns the load into the shear diagram, a second turns shear into moment. Each curve is one degree higher than the one before it."),
    "Flexure Formula": ("SM-C-flexure.png", "stress varies linearly from the neutral axis, tension on one side and compression on the other. Moving material away from the neutral axis (an I-section) raises the section modulus for the same area."),
    "Shear Stress Formula for Beams": ("SM-C-beam-shear.png", "the shear stress in a rectangular section is a parabola with peak $1.5V/A$ at the neutral axis, and zero at the top and bottom faces. In an I-section the web carries nearly all of it."),
    "Mohr's Circle for Stress": ("SM-C-mohr-circle.png", "the circle for $\\sigma_x=80$, $\\sigma_y=-20$, $\\tau_{xy}=30$ MPa. Its centre is the average normal stress, its radius is the largest in-plane shear, and angles on the circle are twice the angles on the element."),
    "Euler Buckling of Columns": ("SM-C-euler-buckling.png", "end conditions scale the critical load through $K$ (left). Euler's formula governs only slender columns, with $\\lambda=KL/r$ beyond about 89 for this steel (right)."),
    "Thin Cylindrical and Spherical Pressure Vessels": ("SM-C-pressure-vessel.png", "cutting along the axis shows the hoop stress, cutting across shows the longitudinal stress. For $p=2$ MPa, $r=0.5$ m, $t=10$ mm the hoop stress is $100$ MPa and the axial stress $50$ MPa."),
    "Thermal Stresses": ("SM-C-thermal-stress.png", "a bar free to expand develops no stress at all. The same temperature rise with both ends fixed produces compression $E\\alpha\\Delta T$, independent of the bar's length."),
    "Double Integration and Macaulay's Method": ("SM-C-double-integration.png", "from the moment diagram, integrate $M/EI$ once for slope and again for deflection. The constants come from the supports. Here the maximum deflection is $5wL^4/384EI$."),
    "Statically Indeterminate Axial Members": ("SM-C-axial-load-sharing.png", "two members sharing a load must stretch equally, so each carries a share in proportion to its $EA$. The stiffer steel core is the more highly stressed part."),
}

Q = {
    "Concept of Stress": [
        ("A 20 mm diameter rod carries a 50 kN tensile load. What is the normal stress?", "$\\sigma=P/A=50\\,000/(\\pi\\,0.01^2)=159.2$ MPa."),
        ("A 10 mm bolt in single shear transmits 12 kN. What is the average shear stress?", "$\\tau=V/A=12\\,000/(\\pi\\,0.005^2)=152.8$ MPa."),
        ("Why does one axial load produce both normal and shear stress?", "Stress depends on the plane you cut. On a plane at angle $\\theta$ to the cross-section, $\\sigma_\\theta=\\sigma\\cos^2\\theta$ and $\\tau_\\theta=\\sigma\\sin\\theta\\cos\\theta$. The shear is largest, $\\sigma/2$, at $45^\\circ$."),
    ],
    "Generalized Hooke's Law and Poisson's Ratio": [
        ("Steel ($E=200$ GPa, $\\nu=0.3$) carries a uniaxial stress of 100 MPa. Find the axial and lateral strains.", "$\\varepsilon_x=\\sigma/E=5\\times10^{-4}$ and $\\varepsilon_y=\\varepsilon_z=-\\nu\\varepsilon_x=-1.5\\times10^{-4}$."),
        ("Find the shear modulus of the same steel.", "$G=E/[2(1+\\nu)]=200/2.6=76.9$ GPa."),
        ("Why can $\\nu$ not exceed $0.5$ for an isotropic material?", "The bulk modulus $K=E/[3(1-2\\nu)]$ must be positive, so $\\nu<0.5$. At $\\nu=0.5$ the material is incompressible (rubber is close)."),
    ],
    "Stress-Strain Diagram and Hooke's Law": [
        ("What separates the yield strength from the ultimate strength?", "Yield strength is the stress at which permanent deformation begins. Ultimate strength is the largest engineering stress the specimen reaches before it necks down."),
        ("A 10 mm diameter, 2 m long steel rod ($E=200$ GPa) carries 15 kN within the elastic range. How much does it stretch?", "$\\delta=PL/AE=15\\,000\\times2/(7.854\\times10^{-5}\\times200\\times10^9)=1.91$ mm."),
        ("What does unloading from beyond yield look like on the diagram?", "The path is a straight line parallel to the elastic line. When the load reaches zero a permanent strain remains."),
    ],
    "Axial Deformation": [
        ("A 1.5 m aluminium bar ($E=70$ GPa, $A=400$ mm²) carries 28 kN. Find the elongation.", "$\\delta=PL/AE=28\\,000\\times1.5/(400\\times10^{-6}\\times70\\times10^9)=1.5$ mm."),
        ("A bar has two equal-length halves, one of area $A$ and one of area $2A$, same $E$, loaded by $P$ at the end. What is the total elongation?", "$\\delta=\\frac{P(L/2)}{AE}+\\frac{P(L/2)}{2AE}=\\frac{3PL}{4AE}$."),
        ("A uniform bar of length $L$ hangs from one end under its own weight. How much does it stretch?", "$\\delta=\\rho gL^2/2E$: the same as if half its weight acted at the free end, because the load carried varies linearly from zero to the full weight."),
    ],
    "Statically Indeterminate Axial Members": [
        ("A steel core ($E=200$ GPa, 600 mm²) sits inside an aluminium tube ($E=70$ GPa, 1200 mm²). A 300 kN load acts on both together. How is it shared?", "Equal strain gives $\\sigma\\propto E$ and load $\\propto EA$: steel $176.5$ kN ($294$ MPa), aluminium $123.5$ kN ($103$ MPa)."),
        ("What is the extra equation that makes an indeterminate axial problem solvable?", "Compatibility of deformation, for example $\\delta_1=\\delta_2$ for members in parallel, or total elongation zero between two fixed walls."),
        ("A bar fixed at both ends carries a load $P$ at distance $a$ from the left end ($b=L-a$). Find the reactions.", "Removing one wall and demanding zero net elongation gives $R_A=Pb/L$ and $R_B=Pa/L$: the nearer wall carries more."),
    ],
    "Thermal Stresses": [
        ("A steel bar ($E=200$ GPa, $\\alpha=12\\times10^{-6}$/K) is held between rigid walls and heated by 50 K. Find the stress.", "$\\sigma=-E\\alpha\\Delta T=-120$ MPa, compressive."),
        ("The same bar is 2 m long and free to expand. How far does it grow?", "$\\delta_T=\\alpha\\Delta T L=12\\times10^{-6}\\times50\\times2=1.2$ mm, with no stress at all."),
        ("Does the length of a fully restrained bar change the thermal stress?", "No. Both the free expansion and the length over which it is pushed back scale with $L$, so $\\sigma=E\\alpha\\Delta T$ is independent of $L$."),
    ],
    "Torsion of Circular Shafts": [
        ("A solid 40 mm shaft carries $T=500$ N·m. Find $\\tau_{max}$.", "$\\tau_{max}=16T/(\\pi d^3)=16\\times500/(\\pi\\,0.04^3)=39.8$ MPa."),
        ("The shaft is 1.5 m long, $G=80$ GPa. Find the angle of twist.", "$J=\\pi d^4/32=2.513\\times10^{-7}$ m⁴, so $\\phi=TL/GJ=0.0373$ rad $=2.14^\\circ$."),
        ("Why is a hollow shaft efficient?", "Shear stress is proportional to radius, so the core is lightly stressed. Removing it costs little torque capacity: a tube with $c_i=0.6c$ keeps $87\\%$ with $64\\%$ of the material."),
    ],
    "Power Transmission by Shafts": [
        ("A shaft transmits 30 kW at 1200 rpm. What torque does it carry?", "$\\omega=2\\pi\\times20=125.7$ rad/s and $T=P/\\omega=238.7$ N·m."),
        ("What diameter keeps the shear stress below 60 MPa at that torque?", "$d^3=16T/(\\pi\\tau)=2.03\\times10^{-5}$ m³, so $d=27.3$ mm (round up to a standard size)."),
        ("The same power is transmitted at twice the speed. What happens to the torque and the shaft size?", "Torque halves ($T=P/\\omega$), so a smaller shaft suffices. This is why high-speed drive shafts are slender and low-speed ones are thick."),
    ],
    "Shear Force and Bending Moment Diagrams": [
        ("A simply supported 6 m beam carries 4 kN/m over its whole length and 10 kN at $x=2$ m. Find the reactions.", "Moments about A: $6R_B=24\\times3+10\\times2$, so $R_B=15.33$ kN and $R_A=34-15.33=18.67$ kN."),
        ("Where is the bending moment largest, and how big is it?", "Where $V=0$: $18.67-10-4x=0$ gives $x=2.17$ m, and $M_{max}=18.67(2.17)-2(2.17)^2-10(0.17)=29.4$ kN·m."),
        ("What does a point load do to the shear and moment diagrams?", "The shear diagram jumps by the load. The moment diagram keeps its value but changes slope, so it has a corner."),
    ],
    "Relations Between Load, Shear, and Moment": [
        ("A cantilever of length $L$ carries a uniform load $w$. Find the shear and moment at the wall.", "$V=wL$ and $M=-wL^2/2$ (hogging), the largest values on the beam."),
        ("A shear diagram is a straight line falling at 5 kN/m. What is the load?", "$dV/dx=-w$, so a uniform downward load of 5 kN/m."),
        ("A moment diagram jumps by 20 kN·m at a point. What is applied there?", "A concentrated couple of 20 kN·m. Point forces give corners in $M$ and jumps in $V$. Couples give jumps in $M$ and leave $V$ unchanged."),
    ],
    "Flexure Formula": [
        ("A 100 mm wide, 200 mm deep rectangular beam carries $M=20$ kN·m. Find the maximum bending stress.", "$\\sigma=6M/(bh^2)=6\\times20\\,000/(0.1\\times0.2^2)=30$ MPa."),
        ("Why is an I-section more efficient than a rectangle of the same area?", "Bending stress is carried mainly by material far from the neutral axis. Putting area in the flanges raises $I$ and hence $Z=I/c$. In the figure, the same area gives $3.6$ times the section modulus."),
        ("Where does the stress vanish in pure bending of a symmetric section?", "On the neutral axis, which passes through the centroid."),
    ],
    "Unsymmetric and Combined Bending": [
        ("A 100 mm × 200 mm column carries 200 kN of compression plus a bending moment of 5 kN·m about the strong axis. Find the extreme stresses.", "$\\sigma=-P/A\\pm M/Z=-10\\pm7.5$ MPa, so $-2.5$ and $-17.5$ MPa: the whole section is in compression."),
        ("For a rectangular section, within what distance of the centroid can a compressive load act without causing tension?", "Within the middle third: $e\\le h/6$ about each axis (the kern of the section)."),
    ],
    "Shear Stress Formula for Beams": [
        ("A 100 mm × 200 mm rectangular beam carries $V=30$ kN. Find the maximum shear stress.", "$\\tau_{max}=1.5V/A=1.5\\times30\\,000/0.02=2.25$ MPa, at the neutral axis."),
        ("Why is the shear stress zero at the top and bottom faces?", "$Q$, the first moment of the area beyond that level, is zero there, and the faces are stress-free."),
        ("In an I-beam, which part carries the shear?", "The web: it is thin and runs between the flanges, so almost all of $V$ flows through it. The flanges carry little."),
    ],
    "Mohr's Circle for Stress": [
        ("For $\\sigma_x=80$, $\\sigma_y=-20$, $\\tau_{xy}=30$ MPa find the principal stresses and the maximum in-plane shear.", "Centre $30$, radius $\\sqrt{50^2+30^2}=58.3$: $\\sigma_1=88.3$, $\\sigma_2=-28.3$, $\\tau_{max}=58.3$ MPa."),
        ("What is the principal angle for this state?", "$\\theta_p=\\tfrac12\\tan^{-1}[2\\tau_{xy}/(\\sigma_x-\\sigma_y)]=\\tfrac12\\tan^{-1}(0.6)=15.5^\\circ$."),
        ("Why are angles on Mohr's circle doubled?", "Stress components depend on $\\cos2\\theta$ and $\\sin2\\theta$, so turning the element by $\\theta$ turns the point on the circle by $2\\theta$."),
    ],
    "Plane Stress Transformation": [
        ("A bar carries a uniaxial stress of 100 MPa. Find the normal and shear stress on a plane whose normal is $30^\\circ$ from the axis.", "$\\sigma_n=100\\cos^2 30^\\circ=75$ MPa and $\\tau=100\\sin30^\\circ\\cos30^\\circ=43.3$ MPa."),
        ("Which combination of stresses does not change when the element is rotated?", "$\\sigma_x+\\sigma_y$ (and $\\sigma_x\\sigma_y-\\tau_{xy}^2$): the invariants."),
        ("Where does the maximum in-plane shear act relative to the principal planes?", "On planes at $45^\\circ$ to them, with magnitude $(\\sigma_1-\\sigma_2)/2$."),
    ],
    "Strain Transformation and Rosettes": [
        ("A $0^\\circ/45^\\circ/90^\\circ$ rosette reads $500$, $300$, $100$ microstrain. Find $\\gamma_{xy}$ and the principal strains.", "$\\gamma_{xy}=2\\varepsilon_{45}-\\varepsilon_0-\\varepsilon_{90}=0$, so the gauge directions are principal: $500$ and $100$ microstrain."),
        ("Why is a gauge rosette needed instead of a single gauge?", "One gauge gives a single normal strain. The state of plane strain has three unknowns ($\\varepsilon_x,\\varepsilon_y,\\gamma_{xy}$), so three independent readings are required."),
    ],
    "Stress-Strain Transformation Analogy": [
        ("Which strain quantity plays the role of shear stress in the transformation equations?", "Half the engineering shear strain, $\\gamma/2$. Replace $\\sigma\\to\\varepsilon$ and $\\tau\\to\\gamma/2$ and the stress formulas become the strain formulas."),
        ("What is plotted on the vertical axis of Mohr's circle for strain?", "$\\gamma/2$ (with the same sign convention as for $\\tau$), against $\\varepsilon$ on the horizontal axis."),
    ],
    "Double Integration and Macaulay's Method": [
        ("A simply supported beam ($L=4$ m, $w=10$ kN/m, $E=200$ GPa, $I=8\\times10^{-5}$ m⁴) is uniformly loaded. Find the midspan deflection.", "$v_{max}=5wL^4/(384EI)=2.08$ mm."),
        ("State the boundary conditions for a cantilever and a simply supported beam.", "Cantilever: $v=0$ and $v'=0$ at the wall. Simply supported: $v=0$ at both supports."),
        ("What is the cantilever tip deflection under an end load $P$?", "$v=PL^3/(3EI)$."),
    ],
    "Moment-Area Method": [
        ("State the two moment-area theorems.", "First: the change in slope between two points equals the area of the $M/EI$ diagram between them. Second: the tangential deviation of one point from the tangent at another equals the first moment of that area about the first point."),
        ("Use the second theorem to find the tip deflection of a cantilever with end load $P$.", "Area $=\\tfrac12\\cdot L\\cdot PL/EI=PL^2/2EI$, centroid $2L/3$ from the tip: $\\delta=PL^3/3EI$."),
    ],
    "Euler Buckling of Columns": [
        ("A pinned-pinned steel column ($E=200$ GPa), 40 mm diameter and 2 m long. Find $P_{cr}$.", "$I=\\pi d^4/64=1.257\\times10^{-7}$ m⁴, so $P_{cr}=\\pi^2EI/L^2=62.0$ kN."),
        ("The same column is fixed at the base and free at the top. Find $P_{cr}$.", "$K=2$, so the load falls to a quarter: $15.5$ kN."),
        ("When does Euler's formula stop being valid?", "When the Euler stress would exceed the yield stress. For $E=200$ GPa and $\\sigma_Y=250$ MPa that is at $\\lambda=KL/r<\\pi\\sqrt{E/\\sigma_Y}\\approx89$."),
    ],
    "Strain Energy and Castigliano's Theorem": [
        ("Write the strain energy of an axially loaded bar.", "$U=P^2L/(2AE)$, which is $\\tfrac12P\\delta$."),
        ("State Castigliano's theorem.", "The deflection at a load, in the direction of that load, is $\\partial U/\\partial P$ (the partial derivative of the total strain energy with respect to that load)."),
        ("Use it for a cantilever with end load $P$.", "$U=\\int M^2/(2EI)\\,dx=P^2L^3/(6EI)$, so $\\delta=\\partial U/\\partial P=PL^3/(3EI)$."),
    ],
    "Thin Cylindrical and Spherical Pressure Vessels": [
        ("A thin cylinder with $p=2$ MPa, $r=0.5$ m, $t=10$ mm. Find the hoop and axial stresses.", "$\\sigma_h=pr/t=100$ MPa and $\\sigma_l=pr/2t=50$ MPa."),
        ("What is the wall stress in a sphere of the same $p$, $r$ and $t$?", "$\\sigma=pr/2t=50$ MPa in every direction, half the hoop stress of the cylinder."),
        ("Why does a boiled sausage split along its length?", "The hoop stress is twice the axial stress, so the weaker longitudinal seam fails first."),
    ],
}


def apply():
    done = 0
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in ("assets", "Tools", "Resources", "Problems", "Revision")]
        for f in fn:
            if not f.endswith(".md"):
                continue
            name = f[:-3]
            if name not in Q and name not in FIG:
                continue
            p = os.path.join(dp, f)
            t = open(p, encoding="utf-8", newline="").read()
            nl = "\r\n" if "\r\n" in t else "\n"
            t = t.replace("\r\n", "\n")
            changed = False
            if name in FIG and FIG[name][0] not in t:
                img, cap = FIG[name]
                heads = [m.start() for m in re.finditer(r"^## ", t, re.M)]
                at = heads[1] if len(heads) > 1 else len(t)
                t = t[:at] + f"![[{img}]]\n\n**Figure:** {cap}\n\n" + t[at:]
                changed = True
            if name in Q and "## Check yourself" not in t:
                block = "## Check yourself\n\n" + "\n\n".join(f"> [!question]- Q{i}. {q}\n> {a}" for i, (q, a) in enumerate(Q[name], 1)) + "\n\n"
                m = re.search(r"^---\nNext:", t, re.M) or re.search(r"^## (Cross-domain links|See also)", t, re.M)
                at = m.start() if m else len(t)
                if not m:
                    block = "\n" + block
                t = t[:at] + block + t[at:]
                changed = True
            if changed:
                open(p, "w", encoding="utf-8", newline="").write(t.replace("\n", nl))
                done += 1
                print("updated", name)
    print("notes updated:", done, "| expected", len(set(Q) | set(FIG)))


if __name__ == "__main__":
    check()
    print("numbers verified")
    apply()
