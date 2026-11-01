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

  function init(rootEl) {
    Array.prototype.forEach.call((rootEl || document).querySelectorAll(".widget[data-widget]:not([data-init])"), function (el) {
      el.dataset.init = "1"; var fn = W[el.dataset.widget]; if (fn) { try { fn(el); } catch (e) { el.innerHTML = "<p class='w-note'>Widget failed: " + e.message + "</p>"; } }
    });
  }
  window.initWidgets = init; init(document);
  document.addEventListener("themechange", function () { Array.prototype.forEach.call(document.querySelectorAll(".widget[data-widget]"), function (el) { var i = el.querySelector("input,select"); if (i) i.dispatchEvent(new Event(i.tagName === "SELECT" ? "change" : "input")); }); });
})();
