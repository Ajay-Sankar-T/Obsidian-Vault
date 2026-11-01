/* wiki app: progress (XP, streak), search, lesson mode, practice grading, course paths, graph. No dependencies. */
(function () {
  "use strict";
  var W = window.WIKI || { courses: [], notes: {}, colors: {}, titles: {}, graph: { n: [], l: [] }, back: {}, links: {} };
  var body = document.body, ROOT = body.dataset.root || "", PAGE = body.dataset.page, SLUG = body.dataset.slug, COURSE = body.dataset.course;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };
  var noteUrl = function (s) { return ROOT + "n/" + s + ".html"; };

  /* ------------------------------------------------------------------ store */
  var KEY = "wiki.progress.v1";
  function load() { try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { return {}; } }
  var S = load();
  S.done = S.done || {}; S.solved = S.solved || {}; S.days = S.days || {}; S.xp = S.xp || 0; S.tasks = S.tasks || {};
  function save() { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) {} }
  function today(d) { d = d || new Date(); return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0"); }
  function addXP(n) { S.xp += n; S.days[today()] = (S.days[today()] || 0) + n; save(); header(); }
  function streak() {
    var d = new Date(), n = 0;
    if (!S.days[today(d)]) d.setDate(d.getDate() - 1);
    while (S.days[today(d)]) { n++; d.setDate(d.getDate() - 1); }
    return n;
  }
  function header() {
    var x = $("#xp"), s = $("#streak");
    if (x) x.textContent = "⚡ " + S.xp + " XP";
    if (s) s.textContent = "🔥 " + streak();
    var side = $("#sideStats");
    if (side) {
      var goal = 30, t = Math.min(S.days[today()] || 0, goal), done = Object.keys(S.done).length;
      var total = Object.keys(W.notes).filter(function (k) { return W.notes[k][2] === "concept"; }).length;
      side.innerHTML = "<b>Daily goal</b>" + t + " / " + goal + " XP today<div class='meter'><i style='width:" + (100 * t / goal) + "%'></i></div><div style='margin-top:10px'>" + done + " of " + total + " lessons learned</div><button class='fchip' id='resetP' type='button' style='margin-top:10px'>Reset progress</button>";
      var rb = $("#resetP"); if (rb) rb.onclick = function () { if (confirm("Clear all XP, streak and completed lessons on this device?")) { try { localStorage.removeItem(KEY); } catch (e) {} location.reload(); } };
    }
  }
  function markDone(slug) {
    var first = !S.done[slug];
    S.done[slug] = Date.now(); save();
    if (first) addXP(10); else header();
    return first;
  }

  /* ------------------------------------------------------------------ theme */
  var tb = $("#themeBtn");
  function themeIcon() { if (tb) tb.textContent = document.documentElement.dataset.theme === "dark" ? "🌞" : "🌙"; }
  if (tb) tb.addEventListener("click", function () {
    var t = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
    document.documentElement.dataset.theme = t; try { localStorage.setItem("wiki.theme", t); } catch (e) {}
    themeIcon(); if (window.__remermaid) window.__remermaid();
    document.dispatchEvent(new Event("themechange"));
  });
  themeIcon(); header();

  /* ------------------------------------------------------------------ search */
  var searchEl = $("#search"), qEl = $("#q"), resEl = $("#results"), sel = 0, hits = [];
  function ensureIndex(cb) {
    if (window.WIKI_SEARCH) return cb();
    var s = document.createElement("script"); s.src = ROOT + "assets/search.js"; s.onload = cb; document.head.appendChild(s);
  }
  function openSearch(term) { if (!searchEl) return; searchEl.hidden = false; qEl.value = typeof term === "string" ? term : ""; resEl.innerHTML = ""; qEl.focus(); ensureIndex(function () { run(); }); }
  function closeSearch() { if (searchEl) searchEl.hidden = true; }
  function run() {
    var q = qEl.value.trim().toLowerCase(); if (!q || !window.WIKI_SEARCH) { resEl.innerHTML = q ? "" : "<div class='res'><small>Type to search titles, headings and text.</small></div>"; hits = []; return; }
    var toks = q.split(/\s+/);
    hits = [];
    window.WIKI_SEARCH.forEach(function (d) {
      var t = d.t.toLowerCase(), h = d.h.join(" ").toLowerCase(), x = d.x.toLowerCase(), score = 0, ok = true;
      for (var i = 0; i < toks.length; i++) {
        var k = toks[i], s = 0;
        if (t.indexOf(k) >= 0) s += 12 + (t.indexOf(k) === 0 ? 4 : 0);
        if (h.indexOf(k) >= 0) s += 5;
        var p = x.indexOf(k); if (p >= 0) { s += 1; if (x.indexOf(k, p + 1) >= 0) s += 1; }
        if (!s) { ok = false; break; } score += s;
      }
      if (ok) hits.push({ d: d, score: score });
    });
    hits.sort(function (a, b) { return b.score - a.score; }); hits = hits.slice(0, 30); sel = 0;
    resEl.innerHTML = hits.map(function (h, i) {
      var d = h.d, x = d.x, p = x.toLowerCase().indexOf(toks[0]), snip = "";
      if (p >= 0) { var a = Math.max(0, p - 40), seg = x.slice(a, a + 140); snip = esc(seg).replace(new RegExp("(" + toks[0].replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "ig"), "<mark>$1</mark>"); }
      return "<a class='res" + (i ? "" : " sel") + "' href='" + noteUrl(d.s) + "'><b>" + esc(d.t) + "</b><small>" + esc(W.titles[d.c] || "") + (snip ? " · …" + snip + "…" : "") + "</small></a>";
    }).join("") || "<div class='res'><small>No matches.</small></div>";
  }
  var openers = [$("#openSearch")]; openers.forEach(function (b) { if (b) b.addEventListener("click", function () { openSearch(); }); });
  if (location.hash.indexOf("#search=") === 0) openSearch(decodeURIComponent(location.hash.slice(8)));
  if (qEl) {
    qEl.addEventListener("input", run);
    qEl.addEventListener("keydown", function (e) {
      var items = $$(".res", resEl).filter(function (r) { return r.href; });
      if (e.key === "ArrowDown" || e.key === "ArrowUp") { e.preventDefault(); sel = Math.max(0, Math.min(items.length - 1, sel + (e.key === "ArrowDown" ? 1 : -1))); items.forEach(function (r, i) { r.classList.toggle("sel", i === sel); }); if (items[sel]) items[sel].scrollIntoView({ block: "nearest" }); }
      if (e.key === "Enter" && items[sel]) location.href = items[sel].href;
    });
    searchEl.addEventListener("click", function (e) { if (e.target === searchEl) closeSearch(); });
  }
  document.addEventListener("keydown", function (e) {
    var tag = (document.activeElement || {}).tagName;
    if (e.key === "Escape") closeSearch();
    if ((e.key === "/" && tag !== "INPUT" && tag !== "TEXTAREA") || ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k")) { e.preventDefault(); openSearch(); }
  });

  /* ------------------------------------------------------------------ home */
  function courseProgress(c) {
    var all = []; c.units.forEach(function (u) { all = all.concat(u.lessons); });
    var d = all.filter(function (s) { return S.done[s]; }).length; return { done: d, total: all.length, all: all };
  }
  if (PAGE === "learn") {
    W.courses.forEach(function (c) {
      var el = $(".ccard[data-course='" + c.id + "'] .bar i"); if (!el) return;
      var p = courseProgress(c); el.style.width = p.total ? (100 * p.done / p.total) + "%" : "0";
    });
    var cont = $("#continue"), last = S.last && W.notes[S.last];
    var first = (W.courses.filter(function (c) { return !c.upcoming && c.units.length; })[0] || {});
    if (cont) {
      if (last) cont.innerHTML = "<small>Continue</small><h3>" + esc(W.notes[S.last][0]) + "</h3><a class='btn' href='" + noteUrl(S.last) + "'>Continue</a>";
      else cont.innerHTML = "<small>Start here</small><h3>" + esc(first.title || "Pick a course") + "</h3><a class='btn' href='course/" + (first.id || "") + ".html'>Start</a>";
    }
  }

  /* ------------------------------------------------------------------ course page */
  if (PAGE === "course") {
    var c = W.courses.filter(function (x) { return x.id === COURSE; })[0];
    if (c) {
      var p = courseProgress(c), cur = null;
      $$(".node").forEach(function (n) {
        var done = !!S.done[n.dataset.slug]; n.classList.toggle("done", done);
        if (!done && !cur) { cur = n; n.classList.add("current"); }
      });
      $$(".pcard[data-slug]").forEach(function (n) { if (S.solved && Object.keys(S.solved).some(function (k) { return k.indexOf(n.dataset.slug + "#") === 0; })) n.classList.add("done"); });
      var ring = $(".ring"); if (ring) { var pct = p.total ? Math.round(100 * p.done / p.total) : 0; ring.style.setProperty("--p", pct); ring.innerHTML = "<b>" + pct + "%</b>"; }
    }
  }

  /* ------------------------------------------------------------------ note page */
  if (PAGE === "note") {
    var meta = W.notes[SLUG] || [];
    S.last = SLUG; save();
    var md = $("#markDone");
    function paintDone() { if (!md) return; var d = !!S.done[SLUG]; md.textContent = d ? "Learned ✓" : "Mark as learned"; md.classList.toggle("btn-done", d); md.classList.toggle("btn-ghost", !d); }
    if (md) { md.addEventListener("click", function () { if (S.done[SLUG]) { delete S.done[SLUG]; save(); header(); } else markDone(SLUG); paintDone(); }); paintDone(); }

    // task checkboxes
    $$("input[data-task]").forEach(function (i) {
      var k = i.dataset.task; if (S.tasks[k] !== undefined) i.checked = S.tasks[k];
      i.addEventListener("change", function () { S.tasks[k] = i.checked; save(); });
    });

    // problems: grading
    $$(".prob").forEach(function (p) {
      var q = p.dataset.q, g = document.createElement("div"); g.className = "grade";
      g.innerHTML = "<span>How did it go?</span><button class='btn' type='button'>I got it · +15 XP</button><button class='btn btn-ghost' type='button'>Review later</button>";
      p.appendChild(g);
      var yes = g.children[1];
      function paint() { var s = !!S.solved[q]; p.classList.toggle("solved", s); yes.textContent = s ? "Solved ✓" : "I got it · +15 XP"; yes.classList.toggle("btn-done", s); }
      yes.addEventListener("click", function () { if (S.solved[q]) { delete S.solved[q]; save(); } else { S.solved[q] = Date.now(); save(); addXP(15); } paint(); });
      g.children[2].addEventListener("click", function () { if (S.solved[q]) { delete S.solved[q]; save(); paint(); } });
      paint();
    });

    // toc scrollspy
    var tocLinks = $$(".toc a");
    if (tocLinks.length && "IntersectionObserver" in window) {
      var map = {}; tocLinks.forEach(function (a) { map[a.getAttribute("href").slice(1)] = a; });
      var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting && map[e.target.id]) { tocLinks.forEach(function (a) { a.classList.remove("on"); }); map[e.target.id].classList.add("on"); } }); }, { rootMargin: "-10% 0px -80% 0px" });
      $$(".body h2[id]").forEach(function (h) { io.observe(h); });
    }

    // mermaid
    if (window.mermaid) {
      var dark = function () { return document.documentElement.dataset.theme === "dark"; };
      var src = $$("pre.mermaid").map(function (e) { return e.textContent; });
      window.__remermaid = function () {
        $$("pre.mermaid").forEach(function (e, i) { e.removeAttribute("data-processed"); e.textContent = src[i]; });
        window.mermaid.initialize({ startOnLoad: false, theme: dark() ? "dark" : "neutral", securityLevel: "loose" });
        window.mermaid.run({ querySelector: "pre.mermaid" }).catch(function () {});
      };
      window.__remermaid();
    }

    // mini graph
    var mg = $("#miniGraph");
    if (mg) {
      var neigh = {}; (W.links[SLUG] || []).concat(W.back[SLUG] || []).forEach(function (s) { if (W.notes[s] && s !== SLUG) neigh[s] = 1; });
      var list = Object.keys(neigh).slice(0, 22), ctx = mg.getContext("2d"), dpr = window.devicePixelRatio || 1, Wd = 640, Hd = 320;
      mg.width = Wd * dpr; mg.height = Hd * dpr; ctx.scale(dpr, dpr);
      var pos = [{ s: SLUG, x: Wd / 2, y: Hd / 2, r: 12 }];
      list.forEach(function (s, i) { var a = (i / list.length) * Math.PI * 2 - Math.PI / 2; pos.push({ s: s, x: Wd / 2 + Math.cos(a) * 250, y: Hd / 2 + Math.sin(a) * 118, r: 7 }); });
      function col(s) { return (W.colors[W.notes[s][1]] || ["#999"])[0]; }
      function draw(hov) {
        ctx.clearRect(0, 0, Wd, Hd); ctx.lineWidth = 2;
        var css = getComputedStyle(document.documentElement), line = css.getPropertyValue("--line").trim(), txt = css.getPropertyValue("--text").trim();
        pos.slice(1).forEach(function (p) { ctx.strokeStyle = line; ctx.beginPath(); ctx.moveTo(pos[0].x, pos[0].y); ctx.lineTo(p.x, p.y); ctx.stroke(); });
        ctx.font = "800 11px Nunito, sans-serif"; ctx.textAlign = "center";
        pos.forEach(function (p, i) {
          ctx.fillStyle = col(p.s); ctx.beginPath(); ctx.arc(p.x, p.y, p.r + (hov === i ? 3 : 0), 0, 7); ctx.fill();
          if (i === 0 || hov === i) { ctx.fillStyle = txt; var t = W.notes[p.s][0]; if (t.length > 34) t = t.slice(0, 32) + "…"; ctx.fillText(t, Math.max(70, Math.min(Wd - 70, p.x)), p.y + (p.y > Hd / 2 || i === 0 ? 28 : -16)); }
        });
      }
      function hit(e) { var r = mg.getBoundingClientRect(), x = (e.clientX - r.left) * Wd / r.width, y = (e.clientY - r.top) * Hd / r.height, h = -1; pos.forEach(function (p, i) { if (Math.hypot(p.x - x, p.y - y) < p.r + 6) h = i; }); return h; }
      mg.addEventListener("mousemove", function (e) { var h = hit(e); mg.style.cursor = h > 0 ? "pointer" : "default"; draw(h); });
      mg.addEventListener("click", function (e) { var h = hit(e); if (h > 0) location.href = pos[h].s + ".html"; });
      draw(-1); document.addEventListener("themechange", function () { draw(-1); });
    }

    // lesson mode
    var sb = $("#startLesson");
    if (sb) sb.addEventListener("click", startLesson);
    if (sb && location.hash === "#lesson") startLesson();
    function startLesson() {
      var steps = $$(".body > .step"); if (steps.length < 1) return;
      var i = 0, color = getComputedStyle($(".note")).getPropertyValue("--c");
      var ov = document.createElement("div"); ov.className = "lesson";
      ov.innerHTML = "<div class='lesson-top'><button class='lesson-x' aria-label='Exit lesson'>✕</button><div class='lesson-bar'><i></i></div></div><div class='lesson-main'><div class='lesson-card' style='--c:" + color + "'></div></div><div class='lesson-foot'><div class='in'><button class='btn btn-ghost' id='lBack'>Back</button><button class='btn' id='lNext'>Continue</button></div></div>";
      document.body.appendChild(ov); body.classList.add("lesson-on");
      var card = $(".lesson-card", ov), bar = $(".lesson-bar i", ov), nextBtn = $("#lNext", ov), backBtn = $("#lBack", ov);
      function show() {
        var s = steps[i], h2 = $("h2", s), label = i === 0 && !h2 ? "Overview" : "Step " + (i + 1) + " of " + steps.length;
        card.innerHTML = "<div class='step-label'>" + label + "</div>" + s.innerHTML;
        $$(".widget", card).forEach(function (w) { w.innerHTML = ""; w.removeAttribute("data-init"); });
        if (window.initWidgets) window.initWidgets(card);
        $$("details.rv", card).forEach(function (d) { d.open = false; });
        bar.style.width = (100 * i / steps.length) + "%";
        nextBtn.textContent = i === steps.length - 1 ? "Finish" : "Continue"; backBtn.style.visibility = i ? "visible" : "hidden";
        $(".lesson-main", ov).scrollTop = 0;
      }
      function finish() {
        var first = markDone(SLUG); bar.style.width = "100%";
        var nx = $(".pg-next"), href = nx ? nx.getAttribute("href") : null;
        card.innerHTML = "<div class='lesson-done'><div class='big'>🎉</div><h2>Lesson complete</h2><p>" + (first ? "+10 XP" : "Already learned") + "</p></div>";
        $(".in", ov).innerHTML = "<button class='btn btn-ghost' id='lExit'>Back to note</button>" + (href ? "<a class='btn' href='" + href + "'>Next lesson</a>" : "");
        $("#lExit", ov).addEventListener("click", close); paintDone();
      }
      function close() { ov.remove(); body.classList.remove("lesson-on"); document.removeEventListener("keydown", key); }
      function go(d) { if (d > 0 && i === steps.length - 1) return finish(); i = Math.max(0, i + d); show(); }
      function key(e) { if (e.key === "Escape") close(); if (e.key === "ArrowRight" || e.key === "Enter") { if (document.activeElement && document.activeElement.tagName === "INPUT") return; go(1); } if (e.key === "ArrowLeft") go(-1); }
      nextBtn.addEventListener("click", function () { go(1); }); backBtn.addEventListener("click", function () { go(-1); }); $(".lesson-x", ov).addEventListener("click", close);
      document.addEventListener("keydown", key); show();
    }
  }

  /* ------------------------------------------------------------------ practice / solve filters */
  function filters(listSel, itemSel) {
    var chips = $$(".fchip"), items = $$(itemSel), box = $("#sf"), cur = "all";
    function apply() {
      var q = box ? box.value.trim().toLowerCase() : "";
      items.forEach(function (it) {
        var ok = (cur === "all" || it.dataset.course === cur) && (!q || it.textContent.toLowerCase().indexOf(q) >= 0);
        it.style.display = ok ? "" : "none";
      });
      $$(".pgroup").forEach(function (g) {
        g.style.display = $$(".pcard", g).some(function (x) { return x.style.display !== "none"; }) ? "" : "none";
      });
    }
    chips.forEach(function (c) { c.addEventListener("click", function () { chips.forEach(function (x) { x.classList.remove("on"); }); c.classList.add("on"); cur = c.dataset.f; apply(); }); });
    if (box) box.addEventListener("input", apply);
  }
  if (PAGE === "practice") {
    filters(".pgrid", ".pcard");
    $$(".pcard[data-slug]").forEach(function (n) { if (Object.keys(S.solved).some(function (k) { return k.indexOf(n.dataset.slug + "#") === 0; })) n.classList.add("done"); });
    $$(".qs a[data-q]").forEach(function (a) { if (S.solved[a.dataset.q]) a.classList.add("done"); });
  }
  if (PAGE === "solve") filters(".scards", ".scard");

  /* ------------------------------------------------------------------ graph page */
  if (PAGE === "graph") {
    var cv = $("#graph"), ctx2 = cv.getContext("2d"), tip = $("#gtip"), N = W.graph.n, L = W.graph.l;
    var nodes = N.map(function (n, i) { var a = Math.random() * 6.283, r = 80 + Math.random() * 220; return { i: i, s: n[0], t: n[1], c: n[2], d: n[3], x: Math.cos(a) * r, y: Math.sin(a) * r, vx: 0, vy: 0 }; });
    var adj = N.map(function () { return []; }); L.forEach(function (e) { adj[e[0]].push(e[1]); adj[e[1]].push(e[0]); });
    var view = { x: 0, y: 0, k: 0.9 }, alpha = 1, hover = -1, dpr2 = window.devicePixelRatio || 1, drag = null;
    function size() { var r = cv.getBoundingClientRect(); cv.width = r.width * dpr2; cv.height = r.height * dpr2; }
    window.addEventListener("resize", size); size();
    function tick() {
      var n = nodes.length;
      for (var i = 0; i < n; i++) {
        var a = nodes[i];
        for (var j = i + 1; j < n; j++) {
          var b = nodes[j], dx = a.x - b.x, dy = a.y - b.y, d2 = dx * dx + dy * dy + 40;
          if (d2 > 160000) continue;
          var f = 2400 / d2, d = Math.sqrt(d2); dx = dx / d * f; dy = dy / d * f; a.vx += dx; a.vy += dy; b.vx -= dx; b.vy -= dy;
        }
        a.vx -= a.x * 0.0022; a.vy -= a.y * 0.0022;
      }
      L.forEach(function (e) {
        var a = nodes[e[0]], b = nodes[e[1]], dx = b.x - a.x, dy = b.y - a.y, d = Math.sqrt(dx * dx + dy * dy) + 0.01, f = (d - 60) * 0.012;
        dx = dx / d * f; dy = dy / d * f; a.vx += dx; a.vy += dy; b.vx -= dx; b.vy -= dy;
      });
      nodes.forEach(function (a) { a.vx *= 0.82; a.vy *= 0.82; a.x += a.vx * alpha; a.y += a.vy * alpha; });
      alpha *= 0.992;
    }
    function rad(n) { return 3 + Math.sqrt(n.d) * 1.5; }
    function draw() {
      var css = getComputedStyle(document.documentElement), line = css.getPropertyValue("--line").trim(), txt = css.getPropertyValue("--text").trim();
      ctx2.setTransform(1, 0, 0, 1, 0, 0); ctx2.clearRect(0, 0, cv.width, cv.height);
      ctx2.setTransform(dpr2 * view.k, 0, 0, dpr2 * view.k, dpr2 * (cv.width / dpr2 / 2 + view.x), dpr2 * (cv.height / dpr2 / 2 + view.y));
      var hl = hover >= 0 ? adj[hover] : [];
      ctx2.lineWidth = 1 / view.k;
      L.forEach(function (e) {
        var on = hover >= 0 && (e[0] === hover || e[1] === hover);
        ctx2.strokeStyle = on ? "#1cb0f6" : line; ctx2.globalAlpha = hover >= 0 && !on ? 0.25 : 0.9;
        ctx2.beginPath(); ctx2.moveTo(nodes[e[0]].x, nodes[e[0]].y); ctx2.lineTo(nodes[e[1]].x, nodes[e[1]].y); ctx2.stroke();
      });
      nodes.forEach(function (n) {
        var dim = hover >= 0 && n.i !== hover && hl.indexOf(n.i) < 0;
        ctx2.globalAlpha = dim ? 0.25 : 1; ctx2.fillStyle = (W.colors[n.c] || ["#999"])[0];
        ctx2.beginPath(); ctx2.arc(n.x, n.y, rad(n) + (n.i === hover ? 2 : 0), 0, 7); ctx2.fill();
      });
      ctx2.globalAlpha = 1; ctx2.fillStyle = txt; ctx2.font = "800 " + (11 / view.k) + "px Nunito,sans-serif"; ctx2.textAlign = "center";
      nodes.forEach(function (n) { if ((n.d >= 28 && view.k > 0.6) || n.i === hover || (hover >= 0 && hl.indexOf(n.i) >= 0 && view.k > 1) || view.k > 2.2) ctx2.fillText(n.t.length > 30 ? n.t.slice(0, 28) + "…" : n.t, n.x, n.y - rad(n) - 4); });
    }
    function loop() { if (alpha > 0.02) { for (var s = 0; s < 3; s++) tick(); } draw(); requestAnimationFrame(loop); }
    function toWorld(e) { var r = cv.getBoundingClientRect(); return { x: (e.clientX - r.left - r.width / 2 - view.x) / view.k, y: (e.clientY - r.top - r.height / 2 - view.y) / view.k }; }
    function pick(e) { var p = toWorld(e), h = -1, best = 1e9; nodes.forEach(function (n) { var d = Math.hypot(n.x - p.x, n.y - p.y); if (d < rad(n) + 5 && d < best) { best = d; h = n.i; } }); return h; }
    // pointer events: mouse drag/hover, one-finger pan, two-finger pinch, tap to preview then tap again to open
    var pts = {}, pinch = null;
    cv.style.touchAction = "none";
    function showTip(e, i) { var r = cv.getBoundingClientRect(); tip.textContent = nodes[i].t + " · " + (W.titles[nodes[i].c] || ""); tip.style.left = Math.max(4, Math.min(r.width - 230, e.clientX - r.left + 12)) + "px"; tip.style.top = Math.max(4, e.clientY - r.top + 12) + "px"; tip.style.opacity = 1; }
    function pdist() { var k = Object.keys(pts); return Math.hypot(pts[k[0]].x - pts[k[1]].x, pts[k[0]].y - pts[k[1]].y) || 1; }
    cv.addEventListener("pointerdown", function (e) {
      try { cv.setPointerCapture(e.pointerId); } catch (x) {}
      pts[e.pointerId] = { x: e.clientX, y: e.clientY };
      var n = Object.keys(pts).length;
      if (n === 1) drag = { x: e.clientX, y: e.clientY, vx: view.x, vy: view.y, moved: false, touch: e.pointerType !== "mouse" };
      else if (n === 2) { drag = null; pinch = { d: pdist(), k: view.k }; }
    });
    cv.addEventListener("pointermove", function (e) {
      if (pts[e.pointerId]) pts[e.pointerId] = { x: e.clientX, y: e.clientY };
      if (pinch && Object.keys(pts).length === 2) { view.k = Math.max(0.3, Math.min(5, pinch.k * pdist() / pinch.d)); return; }
      if (drag) {
        var dx = e.clientX - drag.x, dy = e.clientY - drag.y;
        if (!drag.moved && Math.hypot(dx, dy) > 5) drag.moved = true;
        if (drag.moved) { view.x = drag.vx + dx; view.y = drag.vy + dy; tip.style.opacity = 0; }
        return;
      }
      if (e.pointerType === "mouse") {
        hover = pick(e); cv.style.cursor = hover >= 0 ? "pointer" : "grab";
        if (hover >= 0) showTip(e, hover); else tip.style.opacity = 0;
      }
    });
    function pend(e) {
      var d = drag; delete pts[e.pointerId];
      if (Object.keys(pts).length < 2) pinch = null;
      drag = null;
      if (!d || d.moved) return;
      var h = pick(e);
      if (h < 0) { if (d.touch) { hover = -1; tip.style.opacity = 0; } return; }
      if (d.touch && hover !== h) { hover = h; showTip(e, h); }   // first tap: highlight and name the note
      else location.href = noteUrl(nodes[h].s);                    // mouse click, or second tap on the same note
    }
    cv.addEventListener("pointerup", pend);
    cv.addEventListener("pointercancel", function (e) { delete pts[e.pointerId]; pinch = null; drag = null; });
    cv.addEventListener("wheel", function (e) { e.preventDefault(); var k = Math.max(0.3, Math.min(5, view.k * (e.deltaY < 0 ? 1.12 : 0.89))); view.k = k; }, { passive: false });
    for (var warm = 0; warm < 320; warm++) tick();
    loop();
  }
})();
