---
tags: [EE1100, tutorial-solution, DC-circuits, thevenin, maximum-power, dependent-source]
tutorial: 1
up: "[[Tutorial 1 - Circuit Laws and Theorems]]"
---

# T1-Q5: Maximum Power with a Dependent Source

Hub: [[Tutorial 1 - Circuit Laws and Theorems]] · Theory: [[Theory - Circuit Laws and Network Theorems]] · Previous: [[T1-Q4 - Dependent Source and Power Balance]] · Next: [[T1-Q6 - Superposition]]

> [!question] (a) Find $R_L$ for maximum power transfer, (b) the voltage across $R_L$ (positive at top). The network has a $20\ \Omega$ resistor in series with a dependent voltage source $10i_1$, a $40\ \Omega$ resistor in series with a 50 V source, and $i_1$ is the current in the $40\ \Omega$ branch. *[Sheet: $R_L=R_{th}=16\ \Omega$, $V_{R_L}=5$ V]*

**Tests:** Thevenin equivalent with a **dependent source** (test-source method), [[Theory - Circuit Laws and Network Theorems#9. Maximum power transfer|maximum power transfer]].

## Given
Left branch: $20\ \Omega$ in series with a dependent voltage source $10\,i_1$ ($+$ at the top). Right branch: $40\ \Omega$ in series with a 50 V source ($+$ at the top), carrying $i_1$ towards the right. $R_L$ connects the two rails.

## Principle and why it applies
The load sees a linear network, so it can be replaced by $(V_{th},R_{th})$ and maximum power occurs at $R_L=R_{th}$. Because the network contains a **dependent source whose control $i_1$ lives inside the network**, we cannot find $R_{th}$ by "turning sources off and combining resistors"; the dependent source stays and must be accounted for. Use the **test-source method**: switch off only the *independent* source (50 V → short), apply $v_t$ at the terminals, and measure the current $i_t$.

## Diagram
![[T1-Q5-circuit.png]]

## Solution
**Open-circuit voltage** ($R_L$ removed). Let the top node be at $V$. The right branch gives $i_1=(V-50)/40$, i.e. $V=50+40i_1$. With nothing flowing into $R_L$, the current $i_1$ leaving through the right branch is supplied entirely by the left branch, so in the left branch the dependent source's voltage is the node voltage plus the drop in the $20\ \Omega$: $10i_1=V+20\,i_1$. Substituting,
$$10i_1=50+40i_1+20i_1\ \Rightarrow\ i_1=-1\ \text{A},\qquad V_{oc}=50+40(-1)=10\ \text{V}.$$

**Thevenin resistance** (50 V shorted, test source $v_t$ at the terminals). Now $i_1=v_t/40$ and the dependent source is $10i_1=v_t/4$. The test source supplies the current through the left branch plus that through the $40\ \Omega$:
$$i_t=\frac{v_t-v_t/4}{20}+\frac{v_t}{40}=\frac{3v_t}{80}+\frac{2v_t}{80}=\frac{v_t}{16},$$
so
$$R_{th}=\frac{v_t}{i_t}=16\ \Omega.$$

**Maximum power:** $R_L=R_{th}=16\ \Omega$. Then $V_{R_L}=V_{oc}\dfrac{R_L}{R_L+R_{th}}=10\times\dfrac12=5$ V and $P_{\max}=V_{oc}^2/4R_{th}=100/64=1.56$ W.

## Result
$$\boxed{R_L=16\ \Omega,\qquad V_{R_L}=5\ \text{V},\qquad P_{\max}\approx1.56\ \text{W}}$$

## Check
Short-circuit current: $V=0$ gives $i_1=-50/40=-1.25$ A, the left branch supplies $10i_1/20=-0.625$ A, and the right branch supplies $1.25$ A, so $i_{sc}=1.25-0.625=0.625$ A. Then $V_{oc}/i_{sc}=10/0.625=16\ \Omega$ ✓. Both Thevenin methods agree.

## Trap / alternative
- Turning off the dependent source would give $R_{th}=20\parallel40=13.3\ \Omega$, wrong.
- With dependent sources $R_{th}$ can even come out **negative**; here it is positive because $10i_1$ opposes the voltage across the resistor.
- The sign of the dependent source matters: reversing it changes $R_{th}$ and $V_{oc}$, so read the polarity marks.

## Concepts used
- Thevenin / Norton with dependent sources, maximum power transfer ([[Theory - Circuit Laws and Network Theorems]])
