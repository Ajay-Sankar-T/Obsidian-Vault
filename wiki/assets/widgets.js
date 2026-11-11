/* Interactive explorers attached to notes.  Each widget: sliders on the right, live plot on the left, readouts, one-line takeaway. */
(function () {
  "use strict";
  var DPR = window.devicePixelRatio || 1, PW = 720, PH = 360;
  function css(v) { return getComputedStyle(document.documentElement).getPropertyValue(v).trim(); }
  function h(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function fmt(v, d) { d = d == null ? 3 : d; if (!isFinite(v)) return "—"; var a = Math.abs(v); return (a !== 0 && (a >= 1e4 || a < 1e-3)) ? v.toExponential(2) : (+v.toFixed(d)).toString(); }

  /* ---------- UI building blocks */
  function slider(box, label, min, max, step, val, unit, onchange) {
    var row = h("div", "w-row"), id = "s" + Math.random().toString(36).slice(2, 8);
    row.innerHTML = "<label for='" + id + "'><span>" + label + "</span><b></b></label><input id='" + id + "' type='range' min='" + min + "' max='" + max + "' step='" + step + "' value='" + val + "'>";
    var inp = row.querySelector("input"), out = row.querySelector("b");
    function upd() { out.textContent = fmt(+inp.value, 2) + (unit ? " " + unit : ""); }
    inp.addEventListener("input", function () { upd(); onchange(); }); upd(); box.appendChild(row);
    return { get: function () { return +inp.value; }, set: function (v) { inp.value = v; upd(); }, row: row };
  }
  function select(box, label, opts, onchange) {
    var row = h("div", "w-row"), s = h("select"); s.innerHTML = opts.map(function (o, i) { return "<option value='" + i + "'>" + o + "</option>"; }).join("");
    row.innerHTML = "<label><span>" + label + "</span></label>"; row.appendChild(s); s.addEventListener("change", onchange); box.appendChild(row);
    return { get: function () { return +s.value; }, row: row };
  }
  function frame(root, note) {
    var plot = h("div", "w-plot"), ctrl = h("div", "w-ctrl"), cv = h("canvas");
    cv.width = PW * DPR; cv.height = PH * DPR; cv.style.aspectRatio = PW + "/" + PH; plot.appendChild(cv);
    var out = h("div", "w-out"); root.appendChild(plot); root.appendChild(ctrl);
    var n = h("p", "w-note", note); root.appendChild(n);
    return { plot: plot, ctrl: ctrl, cv: cv, out: out, ctx: cv.getContext("2d") };
  }

  /* ---------- plotting */
  function draw(f, cfg, series) {
    var ctx = f.ctx; ctx.setTransform(DPR, 0, 0, DPR, 0, 0); ctx.clearRect(0, 0, PW, PH);
    var m = { l: 52, r: 14, t: 14, b: 38 }, w = PW - m.l - m.r, hh = PH - m.t - m.b;
    var X = function (x) { return m.l + (cfg.logx ? (Math.log10(x) - Math.log10(cfg.xmin)) / (Math.log10(cfg.xmax) - Math.log10(cfg.xmin)) : (x - cfg.xmin) / (cfg.xmax - cfg.xmin)) * w; };
    var Y = function (y) { return m.t + hh - (y - cfg.ymin) / (cfg.ymax - cfg.ymin) * hh; };
    var line = css("--line"), muted = css("--muted"), text = css("--text");
    ctx.font = "700 12px Nunito,sans-serif"; ctx.lineWidth = 1; ctx.strokeStyle = line; ctx.fillStyle = muted; ctx.textAlign = "center";
    var nx = cfg.xticks || 6, ny = cfg.yticks || 5, i, v;
    // round tick values: a step of 1, 2 or 5 times a power of ten
    function nice(lo, hi, n) {
      var rough = (hi - lo) / n, mag = Math.pow(10, Math.floor(Math.log10(rough))), r = rough / mag, step = (r < 1.5 ? 1 : r < 3 ? 2 : r < 7 ? 5 : 10) * mag, out = [];
      for (var t = Math.ceil(lo / step - 1e-9) * step; t <= hi + step * 1e-9; t += step) out.push(+t.toPrecision(12));
      return { vals: out, dec: Math.max(0, Math.ceil(-Math.log10(step) - 1e-9)) };
    }
    var tx = cfg.logx ? null : nice(cfg.xmin, cfg.xmax, nx), ty = nice(cfg.ymin, cfg.ymax, ny);
    var xv = cfg.logx ? Array.apply(null, Array(nx + 1)).map(function (_, k) { return Math.pow(10, Math.log10(cfg.xmin) + k / nx * (Math.log10(cfg.xmax) - Math.log10(cfg.xmin))); }) : tx.vals;
    xv.forEach(function (v) {
      ctx.beginPath(); ctx.moveTo(X(v), m.t); ctx.lineTo(X(v), m.t + hh); ctx.stroke(); ctx.fillText(fmt(v, cfg.logx ? 0 : tx.dec), X(v), PH - 20);
    });
    ctx.textAlign = "right";
    ty.vals.forEach(function (v) { ctx.beginPath(); ctx.moveTo(m.l, Y(v)); ctx.lineTo(m.l + w, Y(v)); ctx.stroke(); ctx.fillText(fmt(v, ty.dec), m.l - 6, Y(v) + 4); });
    ctx.textAlign = "center"; ctx.fillStyle = muted;
    if (cfg.xlabel) ctx.fillText(cfg.xlabel, m.l + w / 2, PH - 4);
    if (cfg.ylabel) { ctx.save(); ctx.translate(12, m.t + hh / 2); ctx.rotate(-Math.PI / 2); ctx.fillText(cfg.ylabel, 0, 0); ctx.restore(); }
    ctx.strokeStyle = muted; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.moveTo(m.l, m.t); ctx.lineTo(m.l, m.t + hh); ctx.lineTo(m.l + w, m.t + hh); ctx.stroke();
    ctx.save(); ctx.beginPath(); ctx.rect(m.l, m.t - 4, w, hh + 8); ctx.clip();
    series.forEach(function (s) {
      ctx.strokeStyle = s.color || css("--blue"); ctx.fillStyle = s.color || css("--blue"); ctx.lineWidth = s.width || 3; ctx.setLineDash(s.dash || []);
      if (s.hline != null) { ctx.beginPath(); ctx.moveTo(m.l, Y(s.hline)); ctx.lineTo(m.l + w, Y(s.hline)); ctx.stroke(); }
      if (s.vline != null) { ctx.beginPath(); ctx.moveTo(X(s.vline), m.t); ctx.lineTo(X(s.vline), m.t + hh); ctx.stroke(); }
      if (s.pts) { ctx.beginPath(); s.pts.forEach(function (p, k) { var px = X(p[0]), py = Y(p[1]); if (k) ctx.lineTo(px, py); else ctx.moveTo(px, py); }); ctx.stroke(); }
      if (s.fillTo != null && s.pts) { ctx.globalAlpha = 0.12; ctx.lineTo(X(s.pts[s.pts.length - 1][0]), Y(s.fillTo)); ctx.lineTo(X(s.pts[0][0]), Y(s.fillTo)); ctx.fill(); ctx.globalAlpha = 1; }
      ctx.setLineDash([]);
      (s.dots || []).forEach(function (p) { ctx.beginPath(); ctx.arc(X(p[0]), Y(p[1]), s.r || 5, 0, 7); ctx.fill(); });
      if (s.label) { ctx.fillStyle = s.color || text; ctx.textAlign = "left"; ctx.font = "800 12px Nunito,sans-serif"; ctx.fillText(s.label[2], X(s.label[0]) + 6, Y(s.label[1]) - 6); }
    });
    ctx.restore();
  }
  function sample(fn, a, b, n) { var p = [], i; for (i = 0; i <= n; i++) { var x = a + (b - a) * i / n; p.push([x, fn(x)]); } return p; }
  function out(f, rows) { f.out.innerHTML = rows.join("<br>"); }

  /* ---------- widgets */
  var W = {};

  W.oscillator = function (root) {
    var f = frame(root, "Underdamped (ζ<1) rings and overshoots, critically damped (ζ=1) is the fastest without overshoot, overdamped (ζ>1) creeps. The same picture describes a series RLC circuit, a spring-mass-damper and a servo loop.");
    var zeta = slider(f.ctrl, "Damping ratio ζ", 0, 2, 0.01, 0.3, "", up), wn = slider(f.ctrl, "Natural frequency ωₙ", 1, 10, 0.1, 4, "rad/s", up); f.ctrl.appendChild(f.out);
    function y(t, z, w) {
      if (z < 1) { var wd = w * Math.sqrt(1 - z * z); return 1 - Math.exp(-z * w * t) * (Math.cos(wd * t) + z / Math.sqrt(1 - z * z) * Math.sin(wd * t)); }
      if (Math.abs(z - 1) < 1e-6) return 1 - (1 + w * t) * Math.exp(-w * t);
      var r = Math.sqrt(z * z - 1), s1 = -w * (z - r), s2 = -w * (z + r); return 1 - (s2 * Math.exp(s1 * t) - s1 * Math.exp(s2 * t)) / (s2 - s1);
    }
    function up() {
      var z = zeta.get(), w = wn.get(), tmax = Math.min(40, Math.max(6 / w, 5 / (Math.max(z, 0.08) * w) * (z > 1 ? 1.4 : 1))), pts = sample(function (t) { return y(t, z, w); }, 0, tmax, 400);
      var ymax = Math.max(1.2, Math.max.apply(null, pts.map(function (p) { return p[1]; })) * 1.05);
      draw(f, { xmin: 0, xmax: tmax, ymin: 0, ymax: ymax, xlabel: "time (s)", ylabel: "response" }, [{ hline: 1, color: css("--muted"), dash: [6, 5], width: 1.5 }, { hline: 1.02, color: css("--line"), width: 1 }, { hline: 0.98, color: css("--line"), width: 1 }, { pts: pts, color: css("--green"), fillTo: 0 }]);
      var reg = z === 0 ? "undamped" : z < 1 ? "underdamped" : Math.abs(z - 1) < 0.005 ? "critically damped" : "overdamped";
      out(f, ["<b>" + reg + "</b>", z < 1 && z > 0 ? "overshoot <b>" + fmt(100 * Math.exp(-Math.PI * z / Math.sqrt(1 - z * z)), 1) + " %</b>, ω<sub>d</sub> = " + fmt(w * Math.sqrt(1 - z * z), 2) + " rad/s" : "no overshoot", z > 0 ? "2% settling ≈ <b>" + fmt(z < 1 ? 4 / (z * w) : 4.6 / (w * (z - Math.sqrt(z * z - 1))), 2) + " s</b>" : "never settles"]);
    }
    up();
  };

  W.decay = function (root) {
    var f = frame(root, "After one time constant τ a charging quantity has covered 63.2% of the way; after 5τ it is within 1%. Same curve for an RC circuit, a cooling body and a sensor lag.");
    var mode = select(f.ctrl, "Process", ["Decay  e^(−t/τ)", "Charge  1 − e^(−t/τ)", "Growth  e^(t/τ)"], up), tau = slider(f.ctrl, "Time constant τ", 0.2, 5, 0.05, 1.5, "s", up); f.ctrl.appendChild(f.out);
    function up() {
      var m = mode.get(), t = tau.get(), fn = m === 0 ? function (x) { return Math.exp(-x / t); } : m === 1 ? function (x) { return 1 - Math.exp(-x / t); } : function (x) { return Math.exp(x / t); }, tmax = 8, pts = sample(fn, 0, tmax, 300);
      var ymax = m === 2 ? Math.min(30, fn(tmax)) : 1.05;
      draw(f, { xmin: 0, xmax: tmax, ymin: 0, ymax: ymax, xlabel: "time (s)", ylabel: "value" }, [{ vline: t, color: css("--muted"), dash: [6, 5], width: 1.5 }, { pts: pts, color: css("--blue"), fillTo: 0 }, { dots: [[t, fn(t)]], color: css("--orange"), r: 6 }, { label: [t, fn(t), "t = τ: " + fmt(fn(t), 3)], color: css("--orange") }]);
      out(f, ["value at τ: <b>" + fmt(fn(t), 3) + "</b>", "value at 3τ: <b>" + fmt(fn(3 * t), 3) + "</b>", "value at 5τ: <b>" + fmt(fn(5 * t), 3) + "</b>", m === 2 ? "doubling time = τ ln 2 = <b>" + fmt(t * Math.LN2, 2) + " s</b>" : "half-life = τ ln 2 = <b>" + fmt(t * Math.LN2, 2) + " s</b>"]);
    }
    up();
  };

  W.lumped = function (root) {
    var f = frame(root, "τ = ρcL_c / h: more thermal mass or a thinner film coefficient means slower cooling. The one-time-constant picture is valid only while Bi = hL_c/k stays below about 0.1.");
    var hh = slider(f.ctrl, "Film coefficient h", 5, 500, 5, 50, "W/m²K", up), lc = slider(f.ctrl, "Length V/A", 1, 50, 1, 10, "mm", up), k = slider(f.ctrl, "Conductivity k", 0.2, 400, 0.2, 40, "W/mK", up), rc = slider(f.ctrl, "ρc", 1, 4, 0.1, 3.5, "MJ/m³K", up); f.ctrl.appendChild(f.out);
    function up() {
      var L = lc.get() / 1000, tau = rc.get() * 1e6 * L / hh.get(), Bi = hh.get() * L / k.get(), tmax = 4 * tau;
      draw(f, { xmin: 0, xmax: tmax, ymin: 0, ymax: 1.05, xlabel: "time (s)", ylabel: "(T − T∞)/(T₀ − T∞)" }, [{ vline: tau, color: css("--muted"), dash: [6, 5], width: 1.5 }, { pts: sample(function (t) { return Math.exp(-t / tau); }, 0, tmax, 200), color: Bi < 0.1 ? css("--green") : css("--orange"), fillTo: 0 }, { dots: [[tau, Math.exp(-1)]], color: css("--blue") }]);
      out(f, ["τ = <b>" + fmt(tau, 1) + " s</b>", "Biot number <b>" + fmt(Bi, 3) + "</b>", Bi < 0.1 ? "<b style='color:var(--green-d)'>lumped model valid</b>" : "<b style='color:var(--orange)'>Bi > 0.1: temperature varies inside the body; use charts or a series solution</b>"]);
    }
    up();
  };

  W.mohr = function (root) {
    var f = frame(root, "The two extreme normal stresses are the principal stresses σ₁, σ₂ and occur where the shear is zero. The point for a plane rotated by θ moves twice as fast (2θ) around the circle.");
    var sx = slider(f.ctrl, "σₓ", -100, 100, 1, 80, "MPa", up), sy = slider(f.ctrl, "σᵧ", -100, 100, 1, -20, "MPa", up), tx = slider(f.ctrl, "τₓᵧ", -80, 80, 1, 40, "MPa", up), th = slider(f.ctrl, "Plane angle θ", 0, 180, 1, 0, "°", up); f.ctrl.appendChild(f.out);
    function up() {
      var a = sx.get(), b = sy.get(), t = tx.get(), c = (a + b) / 2, R = Math.sqrt(((a - b) / 2) * ((a - b) / 2) + t * t), tr = th.get() * Math.PI / 180;
      var sp = c + ((a - b) / 2) * Math.cos(2 * tr) + t * Math.sin(2 * tr), tp = -((a - b) / 2) * Math.sin(2 * tr) + t * Math.cos(2 * tr), lim = Math.max(60, Math.ceil((Math.abs(c) + R) / 20) * 20 + 10);
      // equal scales on both axes (the plot area is 654 x 308 px), centred near the circle, origin always in view
      var k = 308 / 654, cx = Math.round(c / 20) * 20, H = Math.ceil(Math.max(1.15 * R / k, Math.abs(c - cx) + R + 5, Math.abs(cx) + 10) / 20) * 20;
      var cfg = { xmin: cx - H, xmax: cx + H, ymin: -H * k, ymax: H * k, xlabel: "σ (MPa)", ylabel: "τ (MPa)", xticks: 8, yticks: 4, dec: 0 };
      var pts = []; for (var i = 0; i <= 120; i++) { var q = i / 120 * 2 * Math.PI; pts.push([c + R * Math.cos(q), R * Math.sin(q)]); }
      draw(f, cfg, [{ hline: 0, color: css("--muted"), width: 1.5 }, { pts: pts, color: css("--blue") }, { pts: [[a, t], [b, -t]], color: css("--muted"), dash: [5, 5], width: 1.5 }, { pts: [[c, 0], [sp, tp]], color: css("--orange"), width: 2 },
        { dots: [[a, t], [b, -t]], color: css("--green") }, { dots: [[c + R, 0], [c - R, 0]], color: css("--red"), r: 6 }, { dots: [[sp, tp]], color: css("--orange"), r: 6 }]);
      out(f, ["σ₁ = <b>" + fmt(c + R, 1) + "</b>, σ₂ = <b>" + fmt(c - R, 1) + "</b> MPa", "τ<sub>max</sub> = <b>" + fmt(R, 1) + "</b> MPa", "principal angle θ<sub>p</sub> = <b>" + fmt(0.5 * Math.atan2(2 * t, a - b) * 180 / Math.PI, 1) + "°</b>", "on the θ-plane: σ = <b>" + fmt(sp, 1) + "</b>, τ = <b>" + fmt(tp, 1) + "</b>"]);
    }
    up();
  };

  W.beam = function (root) {
    var f = frame(root, "Deflection grows with the cube (point load) or fourth power (distributed load) of the span, and falls linearly with EI. Curves are scaled to the maximum so the shape is visible; the coefficient gives the real size.");
    var type = select(f.ctrl, "Beam and load", ["Simply supported, point load", "Simply supported, uniform load", "Cantilever, tip load", "Cantilever, uniform load"], up), pos = slider(f.ctrl, "Load position a/L", 0.05, 0.95, 0.01, 0.5, "", up); f.ctrl.appendChild(f.out);
    function up() {
      var t = type.get(), a = pos.get(), L = 1, fn, mx, xm, coef, txt;
      pos.row.style.display = t === 0 ? "" : "none";
      if (t === 0) {
        var b = L - a;
        fn = function (x) { return x <= a ? b * x * (L * L - b * b - x * x) / (6 * L) : a * (L - x) * (L * L - a * a - (L - x) * (L - x)) / (6 * L); };
        xm = a >= 0.5 ? Math.sqrt((L * L - b * b) / 3) : L - Math.sqrt((L * L - a * a) / 3); coef = fn(xm); txt = "δ<sub>max</sub> = <b>" + fmt(coef, 4) + "</b> PL³/EI at x = <b>" + fmt(xm, 3) + "</b> L";
      } else if (t === 1) { fn = function (x) { return x * (1 - 2 * x * x + x * x * x) / 24; }; xm = 0.5; coef = 5 / 384; txt = "δ<sub>max</sub> = <b>5/384 = " + fmt(coef, 4) + "</b> wL⁴/EI at midspan"; }
      else if (t === 2) { fn = function (x) { return x * x * (3 - x) / 6; }; xm = 1; coef = 1 / 3; txt = "δ<sub>max</sub> = <b>1/3</b> PL³/EI at the free end"; }
      else { fn = function (x) { return x * x * (6 - 4 * x + x * x) / 24; }; xm = 1; coef = 1 / 8; txt = "δ<sub>max</sub> = <b>1/8</b> wL⁴/EI at the free end"; }
      mx = fn(xm); var pts = sample(function (x) { return -fn(x) / mx; }, 0, 1, 300);
      var simple = t < 2;
      draw(f, { xmin: 0, xmax: 1, ymin: -1.25, ymax: 0.35, xlabel: "x / L", ylabel: "deflection (scaled)", yticks: 4 }, [{ hline: 0, color: css("--muted"), width: 2 }, { pts: pts, color: css("--green"), fillTo: 0 }, { dots: [[xm, -1]], color: css("--red"), r: 6 }, { dots: simple ? [[0, 0], [1, 0]] : [[0, 0]], color: css("--head") || "#000", r: 7 }].concat(t === 0 ? [{ vline: a, color: css("--orange"), dash: [6, 5], width: 2 }] : []));
      out(f, [txt, t === 0 ? "load at a = <b>" + fmt(a, 2) + "</b> L, the maximum moves toward the load" : "the Macaulay and Castigliano results of Tutorial 8 use these formulas"]);
    }
    up();
  };

  W.euler = function (root) {
    var f = frame(root, "A slender column fails by buckling at P_cr = π²EI/(KL)², long before the material yields; a stocky one crushes first. The curve shows the smaller of the two.");
    var mat = select(f.ctrl, "Material", ["Steel (E 200 GPa, σy 250 MPa)", "Aluminium (E 70 GPa, σy 120 MPa)", "Timber (E 11 GPa, σy 30 MPa)"], up);
    var end = select(f.ctrl, "End conditions", ["Pinned–pinned (K = 1)", "Fixed–free (K = 2)", "Fixed–pinned (K = 0.7)", "Fixed–fixed (K = 0.5)"], up);
    var Ls = slider(f.ctrl, "Length L", 0.1, 4, 0.05, 1.2, "m", up), d = slider(f.ctrl, "Round bar diameter d", 10, 80, 1, 30, "mm", up); f.ctrl.appendChild(f.out);
    var M = [[200e9, 250e6], [70e9, 120e6], [11e9, 30e6]], K = [1, 2, 0.7, 0.5];
    function up() {
      var E = M[mat.get()][0], sy = M[mat.get()][1], k = K[end.get()], dd = d.get() / 1000, I = Math.PI * Math.pow(dd, 4) / 64, A = Math.PI * dd * dd / 4, Py = sy * A;
      function Pcr(L) { return Math.PI * Math.PI * E * I / Math.pow(k * L, 2); }
      var L0 = Ls.get(), P1 = Pcr(L0), cap = Py / 1000 * 1.3, r = dd / 4;
      var pts = sample(function (L) { return Math.min(Pcr(L), Py) / 1000; }, 0.1, 4, 200), eul = sample(function (L) { return Pcr(L) / 1000; }, 0.1, 4, 200);
      draw(f, { xmin: 0.1, xmax: 4, ymin: 0, ymax: cap, xlabel: "length L (m)", ylabel: "load (kN)" }, [{ pts: eul, color: css("--blue"), dash: [6, 5], width: 2 }, { hline: Py / 1000, color: css("--orange"), dash: [6, 5], width: 2 }, { pts: pts, color: css("--green"), width: 4 }, { dots: [[L0, Math.min(P1, Py) / 1000]], color: css("--red"), r: 7 }]);
      out(f, ["slenderness KL/r = <b>" + fmt(k * L0 / r, 0) + "</b>", "P<sub>cr</sub> (Euler) = <b>" + fmt(P1 / 1000, 2) + " kN</b>", "yield load σ<sub>y</sub>A = <b>" + fmt(Py / 1000, 2) + " kN</b>", P1 < Py ? "<b style='color:var(--red)'>buckles first</b>" : "<b style='color:var(--orange)'>crushes first (Euler not valid here)</b>"]);
    }
    up();
  };

  /* coefficients by Simpson's rule */
  function simpson(g, a, b, n) { n = n || 2000; var hh = (b - a) / n, s = g(a) + g(b), i; for (i = 1; i < n; i++) s += g(a + i * hh) * (i % 2 ? 4 : 2); return s * hh / 3; }
  function legendreAll(x, N) { var P = [1, x], n; for (n = 1; n < N; n++) P.push(((2 * n + 1) * x * P[n] - n * P[n - 1]) / (n + 1)); return P; }
  W.series = function (root) {
    var f = frame(root, "Add one eigenfunction at a time: the approximation improves in the mean-square sense, overshoots at jumps (Gibbs), and converges fastest when the function already obeys the boundary conditions.");
    var mode = select(f.ctrl, "Basis", ["sin((n−½)πx) on [0,1]  (y(0)=0, y′(1)=0)", "sin(nπx) on [0,1]  (Dirichlet)", "Legendre Pₙ on [−1,1]"], fixsel);
    var fun = select(f.ctrl, "Function", ["", "", ""], up), N = slider(f.ctrl, "Terms N", 1, 40, 1, 3, "", up); f.ctrl.appendChild(f.out);
    var FS = [[["f = 1", function (x) { return 1; }], ["f = x", function (x) { return x; }], ["f = 1 − x", function (x) { return 1 - x; }], ["step: 1 on [0, ½)", function (x) { return x < 0.5 ? 1 : 0; }]],
      [["f = 1 (square wave)", function (x) { return 1; }], ["f = x (sawtooth)", function (x) { return x; }], ["f = x(1−x)", function (x) { return x * (1 - x); }], ["step: 1 on [0, ½)", function (x) { return x < 0.5 ? 1 : 0; }]],
      [["f = |x|", Math.abs], ["f = eˣ", Math.exp], ["f = sign(x)", function (x) { return x < 0 ? -1 : 1; }], ["f = x³ + x", function (x) { return x * x * x + x; }]]];
    function fixsel() { var m = mode.get(), s = fun.row.querySelector("select"); s.innerHTML = FS[m].map(function (o, i) { return "<option value='" + i + "'>" + o[0] + "</option>"; }).join(""); up(); }
    var cache = {};
    function coeffs(m, fi) {
      var key = m + ":" + fi; if (cache[key]) return cache[key]; var g = FS[m][fi][1], c = [], n;
      for (n = 0; n < 60; n++) {
        if (m === 0) c.push(2 * simpson(function (x) { return g(x) * Math.sin((n + 0.5) * Math.PI * x); }, 0, 1));
        else if (m === 1) c.push(2 * simpson(function (x) { return g(x) * Math.sin((n + 1) * Math.PI * x); }, 0, 1));
        else c.push((2 * n + 1) / 2 * simpson(function (x) { return g(x) * legendreAll(x, n + 1)[n]; }, -1, 1, 1200));
      }
      return cache[key] = c;
    }
    function up() {
      var m = mode.get(), fi = fun.get(), g = FS[m][fi][1], c = coeffs(m, fi), n = N.get(), a = m === 2 ? -1 : 0, b = 1, xs = sample(function (x) { return x; }, a, b, 400);
      function S(x) { var s = 0, k, P; if (m === 2) { P = legendreAll(x, n); for (k = 0; k < n; k++) s += c[k] * P[k]; } else for (k = 0; k < n; k++) s += c[k] * Math.sin((m === 0 ? k + 0.5 : k + 1) * Math.PI * x); return s; }
      var tgt = xs.map(function (p) { return [p[0], g(p[0])]; }), app = xs.map(function (p) { return [p[0], S(p[0])]; });
      var ys = tgt.concat(app).map(function (p) { return p[1]; }), lo = Math.min.apply(null, ys), hi = Math.max.apply(null, ys), pad = 0.15 * (hi - lo || 1);
      draw(f, { xmin: a, xmax: b, ymin: lo - pad, ymax: hi + pad, xlabel: "x", ylabel: "f(x)" }, [{ pts: tgt, color: css("--muted"), width: 3, dash: [2, 0] }, { pts: app, color: css("--green"), width: 3 }]);
      var err = Math.sqrt(simpson(function (x) { var d = g(x) - S(x); return d * d; }, a, b, 800) / (b - a));
      out(f, ["N = <b>" + n + "</b> terms", "r.m.s. error = <b>" + fmt(err, 4) + "</b>", "last coefficient |a<sub>N</sub>| = <b>" + fmt(Math.abs(c[n - 1]), 4) + "</b>"]);
    }
    fixsel();
  };

  /* special functions */
  function besselInt(n, x) { return simpson(function (t) { return Math.cos(n * t - x * Math.sin(t)); }, 0, Math.PI, 300) / Math.PI; }
  function bessel(nu, x) {
    if (nu === 0.5) return Math.sqrt(2 / (Math.PI * x)) * Math.sin(x);
    if (nu === 1.5) return Math.sqrt(2 / (Math.PI * x)) * (Math.sin(x) / x - Math.cos(x));
    return besselInt(nu, x);
  }
  W.special = function (root) {
    var f = frame(root, "Bessel functions behave like decaying cosines (envelope ∝ x^(−1/2)); the dashed curve is the large-x asymptote. Legendre polynomials of degree n have n simple zeros inside (−1, 1).");
    var fam = select(f.ctrl, "Family", ["Bessel Jν(x)", "Legendre Pₙ(x)"], up), nu = slider(f.ctrl, "Order", 0, 6, 0.5, 1, "", up); f.ctrl.appendChild(f.out);
    function up() {
      var fm = fam.get(), v = nu.get();
      if (fm === 0) {
        var ok = v === Math.floor(v) || v === 0.5 || v === 1.5, vv = ok ? v : Math.round(v);
        var pts = sample(function (x) { return x === 0 ? (vv === 0 ? 1 : 0) : bessel(vv, x); }, 0.0001, 20, 400), zeros = [], prev = pts[0];
        pts.forEach(function (p) { if (prev[1] * p[1] < 0 && zeros.length < 8) zeros.push((prev[0] + p[0]) / 2); prev = p; });
        draw(f, { xmin: 0, xmax: 20, ymin: -0.6, ymax: 1.05, xlabel: "x", ylabel: "Jν(x)" }, [{ hline: 0, color: css("--muted"), width: 1.5 }, { pts: sample(function (x) { return Math.sqrt(2 / (Math.PI * x)) * Math.cos(x - vv * Math.PI / 2 - Math.PI / 4); }, 2, 20, 200), color: css("--orange"), dash: [5, 5], width: 2 }, { pts: pts, color: css("--blue") }, { dots: zeros.map(function (z) { return [z, 0]; }), color: css("--red") }]);
        out(f, ["order ν = <b>" + vv + "</b>" + (ok ? "" : " (integer orders and ½, 3⁄2 only)"), "first zeros: <b>" + zeros.slice(0, 4).map(function (z) { return fmt(z, 2); }).join(", ") + "</b>", vv === 0.5 ? "J<sub>½</sub> = √(2/πx) sin x exactly" : "J<sub>ν−1</sub> + J<sub>ν+1</sub> = (2ν/x) J<sub>ν</sub>"]);
      } else {
        var n = Math.round(v), pts2 = sample(function (x) { return legendreAll(x, n + 1)[n]; }, -1, 1, 400), z2 = [], pv = pts2[0];
        pts2.forEach(function (p) { if (pv[1] * p[1] < 0) z2.push((pv[0] + p[0]) / 2); pv = p; });
        draw(f, { xmin: -1, xmax: 1, ymin: -1.1, ymax: 1.1, xlabel: "x", ylabel: "Pₙ(x)" }, [{ hline: 0, color: css("--muted"), width: 1.5 }, { pts: pts2, color: css("--blue") }, { dots: z2.map(function (z) { return [z, 0]; }), color: css("--red") }]);
        out(f, ["degree n = <b>" + n + "</b>, P<sub>n</sub>(1) = 1", "zeros found: <b>" + z2.length + "</b> (= n)", "parity: P<sub>n</sub>(−x) = (−1)<sup>n</sup> P<sub>n</sub>(x)"]);
      }
    }
    up();
  };

  W.resonance = function (root) {
    var f = frame(root, "A series RLC circuit passes current best at ω₀ = 1/√(LC). A larger R lowers the quality factor Q = ω₀L/R and widens the band.");
    var R = slider(f.ctrl, "Resistance R", 1, 100, 1, 10, "Ω", up), L = slider(f.ctrl, "Inductance L", 1, 100, 1, 20, "mH", up), C = slider(f.ctrl, "Capacitance C", 1, 100, 1, 10, "µF", up); f.ctrl.appendChild(f.out);
    function up() {
      var r = R.get(), l = L.get() / 1000, c = C.get() / 1e6, w0 = 1 / Math.sqrt(l * c), Q = w0 * l / r, f0 = w0 / (2 * Math.PI);
      function I(fr) { var w = 2 * Math.PI * fr; return r / Math.sqrt(r * r + Math.pow(w * l - 1 / (w * c), 2)); }
      draw(f, { xmin: 10, xmax: 10000, ymin: 0, ymax: 1.05, logx: true, xlabel: "frequency (Hz, log)", ylabel: "|I| / |I|max", xticks: 3 }, [{ hline: 0.7071, color: css("--muted"), dash: [6, 5], width: 1.5 }, { pts: sample(function (x) { return I(Math.pow(10, x)); }, 1, 4, 400).map(function (p) { return [Math.pow(10, p[0]), p[1]]; }), color: css("--purple"), fillTo: 0 }, { vline: f0, color: css("--orange"), dash: [6, 5], width: 1.5 }]);
      out(f, ["f₀ = <b>" + fmt(f0, 1) + " Hz</b>", "Q = <b>" + fmt(Q, 2) + "</b>", "bandwidth = R/(2πL) = <b>" + fmt(r / (2 * Math.PI * l), 1) + " Hz</b>"]);
    }
    up();
  };

  W.auction = function (root) {
    var plot = h("div", "w-plot"), ctrl = h("div", "w-ctrl"), tab = h("div", "w-out"); tab.style.margin = "10px"; plot.appendChild(tab); root.appendChild(plot); root.appendChild(ctrl);
    root.appendChild(h("p", "w-note", "Values per click are x = 7, y = 6, z = 1 and slot click rates are 10, 4, 0. Truthful bidding is not an equilibrium of GSP; try x = 5, y = 4, z = 2 and x = 3, y = 5, z = 1."));
    var bx = slider(ctrl, "x bids", 0, 10, 0.5, 7, "", up), by = slider(ctrl, "y bids", 0, 10, 0.5, 6, "", up), bz = slider(ctrl, "z bids", 0, 10, 0.5, 1, "", up);
    var pre = h("div", "w-row"); pre.innerHTML = "<button class='fchip' data-p='7,6,1'>truthful</button> <button class='fchip' data-p='5,4,2'>equilibrium 1</button> <button class='fchip' data-p='3,5,1'>equilibrium 2</button>"; ctrl.appendChild(pre);
    Array.prototype.forEach.call(pre.querySelectorAll("button"), function (b) { b.addEventListener("click", function () { var p = b.dataset.p.split(",").map(Number); bx.set(p[0]); by.set(p[1]); bz.set(p[2]); up(); }); });
    var V = { x: 7, y: 6, z: 1 }, CTR = [10, 4, 0], VCG = { x: 30, y: 20, z: 0 };
    function up() {
      var bids = { x: bx.get(), y: by.get(), z: bz.get() }, order = ["x", "y", "z"].sort(function (a, b) { return bids[b] - bids[a] || (a < b ? -1 : 1); }), rev = 0, wel = 0, rows = "";
      order.forEach(function (n, i) { var nxt = i + 1 < 3 ? bids[order[i + 1]] : 0, pay = CTR[i] * nxt, pf = CTR[i] * V[n] - pay; rev += pay; wel += CTR[i] * V[n]; rows += "<tr><td><b>" + n + "</b></td><td>slot " + "abc"[i] + "</td><td>" + fmt(pay, 1) + "</td><td>" + fmt(pf, 1) + "</td><td>" + VCG[n] + "</td></tr>"; });
      tab.innerHTML = "<table style='width:100%;border-collapse:collapse;text-align:left'><tr><th>Bidder</th><th>Gets</th><th>GSP pays</th><th>GSP payoff</th><th>VCG payoff</th></tr>" + rows + "</table><div style='margin-top:8px'>GSP revenue <b>" + fmt(rev, 1) + "</b> (VCG: 44) · welfare <b>" + wel + "</b> (efficient: 94)</div>";
    }
    up();
  };

  /* ---------- Physics I explorers */
  W.freeosc = function (root) {
    var f = frame(root, "Release the mass and watch it ring (underdamped), return fastest without overshoot (critical) or creep (overdamped). The dotted envelope is e^(−βt); the damped frequency ω₁ is always a little below ω₀.");
    var w0s = slider(f.ctrl, "Natural frequency ω₀", 1, 10, 0.1, 4, "rad/s", up), zs = slider(f.ctrl, "Damping ratio β/ω₀", 0, 3, 0.01, 0.15, "", up);
    var xs = slider(f.ctrl, "Start position x₀", -1, 1, 0.05, 1, "", up), vs = slider(f.ctrl, "Start velocity v₀", -6, 6, 0.1, 0, "", up); f.ctrl.appendChild(f.out);
    function up() {
      var w0 = w0s.get(), z = zs.get(), x0 = xs.get(), v0 = vs.get(), b = z * w0, r, fn, A = 0, reg;
      if (z < 0.999) { var w1 = w0 * Math.sqrt(1 - z * z), c2 = (v0 + b * x0) / w1; A = Math.sqrt(x0 * x0 + c2 * c2); fn = function (t) { return Math.exp(-b * t) * (x0 * Math.cos(w1 * t) + c2 * Math.sin(w1 * t)); }; reg = z === 0 ? "undamped (SHM)" : "underdamped"; }
      else if (z <= 1.001) { fn = function (t) { return Math.exp(-b * t) * (x0 + (v0 + b * x0) * t); }; reg = "critically damped"; }
      else { r = Math.sqrt(b * b - w0 * w0); var r1 = -b + r, r2 = -b - r; fn = function (t) { return ((v0 - r2 * x0) * Math.exp(r1 * t) - (v0 - r1 * x0) * Math.exp(r2 * t)) / (r1 - r2); }; reg = "overdamped"; }
      var tmax = Math.min(40, Math.max(6 * Math.PI / w0, b > 0.02 ? 5 / b : 40)), pts = sample(fn, 0, tmax, 700), m = Math.max(0.3, Math.max.apply(null, pts.map(function (p) { return Math.abs(p[1]); })) * 1.15);
      var env = z < 0.999 && z > 0 ? [{ pts: sample(function (t) { return A * Math.exp(-b * t); }, 0, tmax, 120), color: css("--muted"), dash: [4, 4], width: 1.4 }, { pts: sample(function (t) { return -A * Math.exp(-b * t); }, 0, tmax, 120), color: css("--muted"), dash: [4, 4], width: 1.4 }] : [];
      draw(f, { xmin: 0, xmax: tmax, ymin: -m, ymax: m, xlabel: "time (s)", ylabel: "x(t)" }, [{ hline: 0, color: css("--line"), width: 1.5 }].concat(env, [{ pts: pts, color: css("--blue") }]));
      out(f, ["<b>" + reg + "</b>", z < 0.999 ? "ω₁ = " + fmt(w0 * Math.sqrt(1 - z * z), 2) + " rad/s, Q = " + (z > 0 ? fmt(1 / (2 * z), 2) : "∞") : "no oscillation", b > 0 ? "amplitude falls to 1/e in 1/β = <b>" + fmt(1 / b, 2) + " s</b>" : "no decay"]);
    }
    up();
  };

  W.driven = function (root) {
    var f = frame(root, "Steady-state amplitude of a driven oscillator, in units of the static deflection F₀/k. Light damping gives a tall narrow peak near ω₀ whose height is the quality factor Q; the dot is the frequency you are driving at.");
    var zs = slider(f.ctrl, "Damping ratio β/ω₀", 0.02, 1, 0.01, 0.1, "", up), rs = slider(f.ctrl, "Drive frequency ω/ω₀", 0.1, 2.2, 0.01, 0.9, "", up); f.ctrl.appendChild(f.out);
    function up() {
      var z = zs.get(), r0 = rs.get(), A = function (r) { return 1 / Math.sqrt(Math.pow(1 - r * r, 2) + Math.pow(2 * z * r, 2)); }, Q = 1 / (2 * z), rp = z < 0.7071 ? Math.sqrt(1 - 2 * z * z) : 0, peak = A(rp || 0.001);
      draw(f, { xmin: 0, xmax: 2.2, ymin: 0, ymax: Math.min(12, Math.max(2, peak * 1.15)), xlabel: "driving frequency ω/ω₀", ylabel: "amplitude / (F₀/k)" }, [{ vline: 1, color: css("--muted"), dash: [6, 5], width: 1.5 }, { pts: sample(A, 0.01, 2.2, 500), color: css("--blue"), fillTo: 0 }, { dots: [[r0, A(r0)]], color: css("--red"), r: 6 }]);
      var dl = Math.atan2(2 * z * r0, 1 - r0 * r0) * 180 / Math.PI;
      out(f, ["amplitude at your ω: <b>" + fmt(A(r0), 2) + "×</b> static", "phase lag: <b>" + fmt(dl, 0) + "°</b>", "Q = <b>" + fmt(Q, 2) + "</b>, peak <b>" + fmt(peak, 2) + "×</b> at ω/ω₀ = " + fmt(rp, 3), "width ≈ ω₀/Q = " + fmt(2 * z, 2) + " ω₀"]);
    }
    up();
  };

  W.phase = function (root) {
    var f = frame(root, "Phase portrait (angle against angular speed) of a pendulum, in units where ω₀ = 1. The red dashed curve is the separatrix E = mgl: start inside and it swings, start outside and it spins over the top. Add damping and the path spirals in.");
    var ts = slider(f.ctrl, "Start angle θ₀", 5, 175, 1, 60, "°", up), os = slider(f.ctrl, "Start speed θ̇₀", 0, 3, 0.05, 0, "ω₀", up), bs = slider(f.ctrl, "Damping β/ω₀", 0, 0.4, 0.01, 0, "", up); f.ctrl.appendChild(f.out);
    function up() {
      var th = ts.get() * Math.PI / 180, w = os.get(), b = bs.get(), dt = 0.02, N = 3500, i, segs = [[]], cur = segs[0], wrap = function (a) { return a - 2 * Math.PI * Math.round(a / (2 * Math.PI)); };
      function acc(a, v) { return -Math.sin(a) - 2 * b * v; }
      var a0 = th, v0 = w, last = wrap(a0); cur.push([last, v0]);
      for (i = 0; i < N; i++) {
        var k1a = v0, k1v = acc(a0, v0), k2a = v0 + dt / 2 * k1v, k2v = acc(a0 + dt / 2 * k1a, v0 + dt / 2 * k1v), k3a = v0 + dt / 2 * k2v, k3v = acc(a0 + dt / 2 * k2a, v0 + dt / 2 * k2v), k4a = v0 + dt * k3v, k4v = acc(a0 + dt * k3a, v0 + dt * k3v);
        a0 += dt / 6 * (k1a + 2 * k2a + 2 * k3a + k4a); v0 += dt / 6 * (k1v + 2 * k2v + 2 * k3v + k4v);
        var wv = wrap(a0); if (Math.abs(wv - last) > Math.PI) { cur = []; segs.push(cur); } cur.push([wv, v0]); last = wv;
      }
      var sep = function (s) { return sample(function (x) { return s * 2 * Math.cos(x / 2); }, -Math.PI, Math.PI, 120); };
      var series = [{ pts: sep(1), color: css("--red"), dash: [6, 5], width: 2 }, { pts: sep(-1), color: css("--red"), dash: [6, 5], width: 2 }, { dots: [[0, 0]], color: css("--green"), r: 5 }];
      segs.forEach(function (s) { if (s.length > 1) series.push({ pts: s, color: css("--blue"), width: 2.2 }); });
      series.push({ dots: [[wrap(th), w]], color: css("--orange"), r: 6 });
      draw(f, { xmin: -Math.PI, xmax: Math.PI, ymin: -3, ymax: 3, xlabel: "angle θ (rad), wrapped to ±π", ylabel: "θ̇ / ω₀", xticks: 6 }, series);
      var E = w * w / 2 - Math.cos(th), reg = Math.abs(E - 1) < 0.01 ? "on the separatrix (takes forever)" : E < 1 ? "libration (swinging)" : "rotation (over the top)";
      var rows = ["energy E = <b>" + fmt(E, 3) + "</b> (separatrix at 1)", "<b>" + reg + "</b>"];
      if (w === 0 && b === 0) { var a = 1, g = Math.cos(th / 2), s; for (s = 0; s < 12; s++) { var an = (a + g) / 2; g = Math.sqrt(a * g); a = an; } rows.push("period = <b>" + fmt(1 / a, 4) + "</b> × small-angle period"); }
      out(f, rows);
    }
    up();
  };

  W.orbit = function (root) {
    var f = frame(root, "Every Kepler orbit is r = ℓ/(1 + e cos φ) with the Sun at the focus (dot at the origin). Increase e to stretch the circle into an ellipse, a parabola and a hyperbola; drag the angle to see the speed change (fast near the Sun, slow far away).");
    var es = slider(f.ctrl, "Eccentricity e", 0, 1.8, 0.01, 0.5, "", up), ps = slider(f.ctrl, "Position angle φ", 0, 360, 1, 40, "°", up); f.ctrl.appendChild(f.out);
    function up() {
      var e = es.get(), ph0 = ps.get() * Math.PI / 180, rr = function (p) { return 1 / (1 + e * Math.cos(p)); }, pts = [], p, lim = e > 1 ? Math.acos(-1 / e) * 0.985 : Math.PI;
      for (p = -lim; p <= lim + 1e-9; p += lim / 200) { var r = rr(p); pts.push([r * Math.cos(p), r * Math.sin(p)]); }
      var ok = e <= 1 || Math.cos(ph0) > -1 / e + 0.02, series = [{ pts: pts, color: css("--blue"), width: 2.6 }, { dots: [[0, 0]], color: css("--orange"), r: 8 }];
      if (ok) { var r1 = rr(ph0), px = r1 * Math.cos(ph0), py = r1 * Math.sin(ph0); series.push({ pts: [[0, 0], [px, py]], color: css("--muted"), width: 1.5, dash: [4, 4] }); series.push({ dots: [[px, py]], color: css("--red"), r: 6 }); }
      draw(f, { xmin: -6.6, xmax: 2.2, ymin: -2.2, ymax: 2.2, xlabel: "x / ℓ", ylabel: "y / ℓ", xticks: 6 }, series);
      var typ = e < 0.005 ? "circle" : e < 0.995 ? "ellipse" : e < 1.005 ? "parabola" : "hyperbola", rows = ["<b>" + typ + "</b>, energy E = <b>" + fmt((e * e - 1) / 2, 3) + "</b> (units mk²/L²)"];
      if (e < 0.995) { var a = 1 / (1 - e * e); rows.push("a = " + fmt(a, 2) + " ℓ, pericentre " + fmt(1 / (1 + e), 3) + " ℓ, apocentre " + fmt(1 / (1 - e), 2) + " ℓ", "T ∝ a^(3/2) = " + fmt(Math.pow(a, 1.5), 2) + ", v_peri / v_apo = " + fmt((1 + e) / (1 - e), 2)); } else rows.push("unbound: it passes the Sun once and leaves");
      if (ok) rows.push("speed here: <b>" + fmt(Math.sqrt(Math.max(0, 2 / rr(ph0) - (1 - e * e))), 3) + "</b> (units √(GM/ℓ))");
      out(f, rows);
    }
    up();
  };

  W.vfield = function (root) {
    var f = frame(root, "The field F = (ax − by, bx + ay). Its divergence is 2a (how much it spreads) and its curl is 2b (how much it swirls). Over the unit circle (red), the flux out equals divergence × area and the circulation equals curl × area: the divergence and Stokes theorems in one picture.");
    var as = slider(f.ctrl, "Spread  a", -2, 2, 0.05, 1, "", up), bs = slider(f.ctrl, "Swirl  b", -2, 2, 0.05, 0.5, "", up); f.ctrl.appendChild(f.out);
    function up() {
      var a = as.get(), b = bs.get(), ctx = f.ctx, X = function (x) { return PW / 2 + x * (PW / 7.2); }, Y = function (y) { return PH / 2 - y * (PW / 7.2); }, i, j;
      ctx.setTransform(DPR, 0, 0, DPR, 0, 0); ctx.clearRect(0, 0, PW, PH);
      ctx.strokeStyle = css("--line"); ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(0, Y(0)); ctx.lineTo(PW, Y(0)); ctx.moveTo(X(0), 0); ctx.lineTo(X(0), PH); ctx.stroke();
      var sc = 0.5 / Math.max(1, Math.hypot(a, b) * 3.4);
      for (i = -3; i <= 3; i += 0.6) for (j = -1.6; j <= 1.6; j += 0.55) {
        var u = a * i - b * j, v = b * i + a * j, m = Math.hypot(u, v); if (m < 1e-6) continue;
        var L = Math.min(0.55, m * sc * 1.2), x1 = X(i), y1 = Y(j), dx = u / m * L * (PW / 7.2), dy = -v / m * L * (PW / 7.2);
        ctx.strokeStyle = css("--blue"); ctx.fillStyle = css("--blue"); ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x1 + dx, y1 + dy); ctx.stroke();
        var ang = Math.atan2(dy, dx); ctx.beginPath(); ctx.moveTo(x1 + dx, y1 + dy); ctx.lineTo(x1 + dx - 6 * Math.cos(ang - 0.45), y1 + dy - 6 * Math.sin(ang - 0.45)); ctx.lineTo(x1 + dx - 6 * Math.cos(ang + 0.45), y1 + dy - 6 * Math.sin(ang + 0.45)); ctx.fill();
      }
      ctx.strokeStyle = css("--red"); ctx.lineWidth = 3; ctx.beginPath(); ctx.arc(X(0), Y(0), PW / 7.2, 0, 7); ctx.stroke();
      var div = 2 * a, curl = 2 * b, kind = Math.abs(a) < 0.03 && Math.abs(b) < 0.03 ? "zero field" : Math.abs(b) < 0.03 ? (a > 0 ? "pure source" : "pure sink") : Math.abs(a) < 0.03 ? (b > 0 ? "pure anticlockwise swirl" : "pure clockwise swirl") : (a > 0 ? "source with swirl: outward spiral" : "sink with swirl: inward spiral");
      out(f, ["<b>" + kind + "</b>", "div F = <b>" + fmt(div, 2) + "</b>, curl F = <b>" + fmt(curl, 2) + "</b>", "flux out of unit circle = div × π = <b>" + fmt(div * Math.PI, 2) + "</b>", "circulation round it = curl × π = <b>" + fmt(curl * Math.PI, 2) + "</b>"]);
    }
    up();
  };

  W.fourbar = function (root) {
    var f = frame(root, "Drag the four link lengths. The rule: s + l < p + q (shortest plus longest less than the other two) lets the shortest link turn fully. The purple curve is the path of the coupler midpoint while the input link goes round; if the crank cannot go all the way round, only part of the curve exists.");
    var gs = slider(f.ctrl, "Ground link g", 2, 7, 0.1, 4.5, "", up), bs = slider(f.ctrl, "Input crank b", 1, 7, 0.1, 2.0, "", up), cs = slider(f.ctrl, "Coupler c", 2, 7, 0.1, 5.0, "", up), ds = slider(f.ctrl, "Follower d", 2, 7, 0.1, 4.0, "", up), ts = slider(f.ctrl, "Input angle", 0, 360, 1, 50, "°", up);
    var brs = select(f.ctrl, "Assembly", ["open", "crossed"], up); f.ctrl.appendChild(f.out);
    function ci(p0, r0, p1, r1, sg) {
      var dx = p1[0] - p0[0], dy = p1[1] - p0[1], d = Math.hypot(dx, dy);
      if (d > r0 + r1 || d < Math.abs(r0 - r1) || d === 0) return null;
      var a = (r0 * r0 - r1 * r1 + d * d) / (2 * d), hh = Math.sqrt(Math.max(r0 * r0 - a * a, 0)), ex = dx / d, ey = dy / d;
      return [p0[0] + a * ex - sg * hh * ey, p0[1] + a * ey + sg * hh * ex];
    }
    function up() {
      var g = gs.get(), b = bs.get(), c = cs.get(), d = ds.get(), sg = brs.get() ? -1 : 1, th = ts.get() * Math.PI / 180;
      var A = [b * Math.cos(th), b * Math.sin(th)], B = ci(A, c, [g, 0], d, sg), series = [], segs = [], cur = [], t, ok = [], bb = [[0, 0], [g, 0], A];
      for (t = 0; t <= 360; t += 2) {
        var a1 = [b * Math.cos(t * Math.PI / 180), b * Math.sin(t * Math.PI / 180)], b1 = ci(a1, c, [g, 0], d, sg);
        if (b1) { cur.push([(a1[0] + b1[0]) / 2, (a1[1] + b1[1]) / 2]); ok.push(t); bb.push(a1, b1); } else { bb.push(a1); if (cur.length) { segs.push(cur); cur = []; } }
      }
      if (cur.length) segs.push(cur);
      segs.forEach(function (s) { if (s.length > 1) series.push({ pts: s, color: css("--purple") || "#8e6bd6", width: 1.8, dash: [5, 4] }); });
      series.push({ pts: [[0, 0], [g, 0]], color: css("--muted"), width: 6 });
      if (B) {
        series.push({ pts: [[0, 0], A], color: css("--blue"), width: 4 }, { pts: [A, B], color: css("--green"), width: 4 }, { pts: [B, [g, 0]], color: css("--orange"), width: 4 });
        series.push({ dots: [[0, 0], [g, 0], A, B], color: css("--text"), r: 5 });
      } else series.push({ pts: [[0, 0], A], color: css("--blue"), width: 4 }, { dots: [[0, 0], [g, 0], A], color: css("--text"), r: 5 });
      var x0 = Math.min.apply(null, bb.map(function (q) { return q[0]; })), x1 = Math.max.apply(null, bb.map(function (q) { return q[0]; })), y0 = Math.min.apply(null, bb.map(function (q) { return q[1]; })), y1 = Math.max.apply(null, bb.map(function (q) { return q[1]; }));
      var hw = Math.max((x1 - x0) / 2, (y1 - y0) / 2 * 2.12) + 0.8, cx = (x0 + x1) / 2, cy = (y0 + y1) / 2;
      draw(f, { xmin: cx - hw, xmax: cx + hw, ymin: cy - hw / 2.12, ymax: cy + hw / 2.12, xlabel: "link-length units", ylabel: "", xticks: 6, yticks: 4 }, series);
      var L = [g, b, c, d], srt = L.slice().sort(function (x, y) { return x - y; }), s = srt[0], l = srt[3], pq = srt[1] + srt[2], G = s + l - pq, eq = function (x, y) { return Math.abs(x - y) < 1e-6; };
      var kind, turn;
      if (Math.abs(G) < 1e-6) kind = "change point (s + l = p + q): the chain can fold flat";
      else if (G > 0) kind = "non-Grashof: triple rocker, no link turns fully";
      else if (eq(g, s)) kind = "Grashof, fixed link is the shortest: <b>drag link</b> (double crank)";
      else if (eq(c, s)) kind = "Grashof, fixed link opposite the shortest: <b>double rocker</b>";
      else kind = "Grashof, shortest link next to the fixed one: <b>crank-rocker</b>";
      turn = (G < -1e-6 && (eq(b, s) || eq(g, s))) ? "the input crank <b>can</b> turn 360°" : "the input crank <b>cannot</b> turn 360°";
      var rows = ["s + l = <b>" + fmt(s + l, 2) + "</b> &nbsp; p + q = <b>" + fmt(pq, 2) + "</b> &nbsp; (difference " + fmt(G, 2) + ")", kind, turn];
      if (!B) rows.push("<span style='color:" + css("--red") + "'>at " + Math.round(ts.get()) + "° the links cannot close; move the angle</span>");
      else if (ok.length && ok.length < 181) rows.push("the crank reaches " + ok.length * 2 + "° of the 360° only");
      out(f, rows);
    }
    up();
  };

  /* ---------- PDE explorers */
  W.heat = function (root) {
    var f = frame(root, "A rod with both ends held at 0. Each sine mode decays as e^(−n²s): the n-th mode dies n² times faster than the first, so every start shape relaxes to the same single half-sine. Slide s to watch the sharp features go first.");
    var shape = select(f.ctrl, "Initial temperature", ["Uniform block (1)", "Triangle (peak 1)", "Parabola 4x(1−x)", "Hot patch 0.4 < x < 0.6"], up);
    var ss = slider(f.ctrl, "Time s = t/τ₁", 0, 2, 0.005, 0.02, "", up), ns = slider(f.ctrl, "Modes kept N", 1, 60, 1, 25, "", up); f.ctrl.appendChild(f.out);
    function coef(k, n) {
      var P = Math.PI;
      if (k === 0) return n % 2 ? 4 / (n * P) : 0;
      if (k === 1) return 8 / (n * n * P * P) * Math.sin(n * P / 2);
      if (k === 2) return n % 2 ? 32 / Math.pow(n * P, 3) : 0;
      return 2 * (Math.cos(0.4 * n * P) - Math.cos(0.6 * n * P)) / (n * P);
    }
    function u(k, s, N, x) { var v = 0, n; for (n = 1; n <= N; n++) v += coef(k, n) * Math.exp(-n * n * s) * Math.sin(n * Math.PI * x); return v; }
    function up() {
      var k = shape.get(), s = ss.get(), N = ns.get(), now = sample(function (x) { return u(k, s, N, x); }, 0, 1, 300), init = sample(function (x) { return u(k, 0, 60, x); }, 0, 1, 300);
      var ym = Math.max(1.2, Math.max.apply(null, init.map(function (p) { return p[1]; })) * 1.1);
      draw(f, { xmin: 0, xmax: 1, ymin: -0.2, ymax: ym, xlabel: "position x/L", ylabel: "temperature u" }, [{ hline: 0, color: css("--line"), width: 1.5 }, { pts: init, color: css("--muted"), dash: [5, 5], width: 1.6 }, { pts: now, color: css("--orange"), fillTo: 0 }]);
      var mx = Math.max.apply(null, now.map(function (p) { return p[1]; })), b1 = coef(k, 1) * Math.exp(-s);
      out(f, ["hottest point: <b>" + fmt(mx, 3) + "</b>", "mode 1 has kept <b>" + fmt(Math.exp(-s) * 100, 1) + " %</b> of its size, mode 2 only <b>" + fmt(Math.exp(-4 * s) * 100, 1) + " %</b>, mode 3 <b>" + fmt(Math.exp(-9 * s) * 100, 1) + " %</b>", s > 0.8 ? "now a pure half-sine, decaying with τ₁ = L²/(π²c²)" : s < 0.01 ? "initial shape, with " + N + " modes" + (N < 60 && k !== 2 ? " (ripples are the Gibbs overshoot)" : "") : "higher modes are fading"]);
    }
    up();
  };

  W.dalembert = function (root) {
    var f = frame(root, "d'Alembert: u = ½[f(x−ct) + f(x+ct)]. The starting pulse splits into two half-height copies moving apart. At a fixed wall the mirror image (odd extension) arrives inverted; at a free end the image is even and the pulse comes back upright.");
    var bc = select(f.ctrl, "Left end x = 0", ["No wall (infinite string)", "Fixed wall: u = 0", "Free end: u_x = 0"], up), ts = slider(f.ctrl, "Time t", 0, 8, 0.02, 0, "s", up), ws = slider(f.ctrl, "Pulse width", 0.3, 1.5, 0.05, 0.6, "", up); f.ctrl.appendChild(f.out);
    var X0 = 3.5;
    function up() {
      var m = bc.get(), t = ts.get(), w = ws.get();
      var F = function (x) { return Math.exp(-Math.pow((x - X0) / w, 2)); };
      var E = function (x) { return (m === 0 || x >= 0) ? F(x) : (m === 1 ? -F(-x) : F(-x)); };   // odd or even extension about the wall
      var R = function (x) { return 0.5 * (E(x - t) + E(x + t)); };
      var pts = sample(R, 0, 10, 500);
      var dash = [{ pts: sample(function (x) { return 0.5 * E(x - t); }, 0, 10, 300), color: css("--blue"), dash: [4, 4], width: 1.5 }, { pts: sample(function (x) { return 0.5 * E(x + t); }, 0, 10, 300), color: css("--red"), dash: [4, 4], width: 1.5 }];
      draw(f, { xmin: 0, xmax: 10, ymin: -1.1, ymax: 1.1, xlabel: "position x", ylabel: "displacement u" }, [{ hline: 0, color: css("--line"), width: 1.5 }].concat(dash, [{ pts: pts, color: css("--green"), fillTo: 0 }]));
      var wallT = X0;
      out(f, ["c = 1: each half-pulse travels <b>" + fmt(t, 2) + "</b> units", m === 0 ? "blue ½f(x−ct) goes right, red ½f(x+ct) goes left" : "the pulse reaches the wall at t = <b>" + fmt(wallT, 1) + "</b>", m === 1 ? "after reflection the pulse is inverted" : m === 2 ? "after reflection the pulse keeps its sign" : "peak height now <b>" + fmt(Math.max.apply(null, pts.map(function (p) { return p[1]; })), 2) + "</b>"]);
    }
    up();
  };

  W.laplace = function (root) {
    var f = frame(root, "Laplace's equation in a disk: the boundary harmonic aₖcos kθ + bₖsin kθ is multiplied by rᵏ inside. Move inward and sharp features of the boundary data are smoothed out; at the centre only the average survives (the mean value property).");
    var shape = select(f.ctrl, "Boundary temperature g(θ)", ["Square wave ±1", "Sawtooth θ/π", "Heated arc |θ| < 60°"], up), rs = slider(f.ctrl, "Radius r (boundary = 1)", 0, 0.99, 0.01, 0.6, "", up); f.ctrl.appendChild(f.out);
    var NK = 150;
    function parts(k, j) {   // returns [a_j, b_j]
      var P = Math.PI;
      if (k === 0) return [0, j % 2 ? 4 / (P * j) : 0];
      if (k === 1) return [0, 2 * (j % 2 ? 1 : -1) / (P * j)];
      return [2 * Math.sin(j * P / 3) / (j * P), 0];
    }
    function a0(k) { return k === 2 ? 1 / 3 : 0; }
    function u(k, r, th) { var v = a0(k), j, p; for (j = 1; j <= NK; j++) { p = parts(k, j); v += Math.pow(r, j) * (p[0] * Math.cos(j * th) + p[1] * Math.sin(j * th)); } return v; }
    function up() {
      var k = shape.get(), r = rs.get(), bd = sample(function (t) { return u(k, 0.9995, t); }, -Math.PI, Math.PI, 400), inn = sample(function (t) { return u(k, r, t); }, -Math.PI, Math.PI, 400);
      draw(f, { xmin: -Math.PI, xmax: Math.PI, ymin: -1.3, ymax: 1.3, xlabel: "angle θ (rad)", ylabel: "temperature", xticks: 6 }, [{ hline: 0, color: css("--line"), width: 1.5 }, { pts: bd, color: css("--muted"), dash: [5, 5], width: 1.6 }, { pts: inn, color: css("--purple"), fillTo: 0 }]);
      var vs = inn.map(function (p) { return p[1]; });
      out(f, ["at r = <b>" + fmt(r, 2) + "</b>: max <b>" + fmt(Math.max.apply(null, vs), 3) + "</b>, min <b>" + fmt(Math.min.apply(null, vs), 3) + "</b>", "centre value = average of g = <b>" + fmt(a0(k), 3) + "</b>", "mode k is scaled by r<sup>k</sup>: k = 5 keeps " + fmt(100 * Math.pow(r, 5), 1) + " %"]);
    }
    up();
  };

  function init(rootEl) {
    Array.prototype.forEach.call((rootEl || document).querySelectorAll(".widget[data-widget]:not([data-init])"), function (el) {
      el.dataset.init = "1"; var fn = W[el.dataset.widget]; if (fn) { try { fn(el); } catch (e) { el.innerHTML = "<p class='w-note'>Widget failed: " + e.message + "</p>"; } }
    });
  }
  window.initWidgets = init; init(document);
  document.addEventListener("themechange", function () { Array.prototype.forEach.call(document.querySelectorAll(".widget[data-widget]"), function (el) { var i = el.querySelector("input,select"); if (i) i.dispatchEvent(new Event(i.tagName === "SELECT" ? "change" : "input")); }); });
})();
