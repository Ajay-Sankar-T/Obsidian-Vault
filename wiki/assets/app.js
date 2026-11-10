/* Engineering Notebook: reading progress, course tree and drawer, search, study mode, practice marking, link map. No dependencies. */
(function () {
  "use strict";
  var W = window.WIKI || { courses: [], notes: {}, colors: {}, titles: {}, graph: { n: [], l: [] }, back: {}, links: {} };
  var body = document.body, ROOT = body.dataset.root || "", PAGE = body.dataset.page, SLUG = body.dataset.slug, COURSE = body.dataset.course;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };
  var noteUrl = function (s) { return ROOT + "n/" + s + ".html"; };
  var colorOf = function (cid) { return (W.colors[cid] || ["#8a6a26", "#5a4318"])[0]; };
  var courseById = function (id) { return W.courses.filter(function (c) { return c.id === id; })[0]; };

  /* ------------------------------------------------------------------ store (browser only) */
  var KEY = "wiki.progress.v1";
  function load() { try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { return {}; } }
  var S = load();
  S.done = S.done || {}; S.solved = S.solved || {}; S.tasks = S.tasks || {}; S.recent = S.recent || [];
  function save() { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) {} }
  function markDone(slug) { var first = !S.done[slug]; S.done[slug] = Date.now(); save(); return first; }
  function pushRecent(slug) {
    S.recent = [slug].concat(S.recent.filter(function (s) { return s !== slug; })).filter(function (s) { return W.notes[s]; }).slice(0, 8);
    S.last = slug; save();
  }

  /* ------------------------------------------------------------------ right-hand outline toggle (the site is dark only) */
  var lb = $("#treeBtn");
  if (lb) lb.addEventListener("click", function () {
    var hide = !document.documentElement.classList.contains("no-tree");
    document.documentElement.classList.toggle("no-tree", hide);
    try { localStorage.setItem("wiki.tree", hide ? "0" : "1"); } catch (e) {}
    lb.setAttribute("aria-pressed", hide ? "false" : "true");
    lb.setAttribute("aria-label", hide ? "Show the left-hand contents" : "Hide the left-hand contents");
  });
  var tb = $("#tocBtn");
  if (tb && $(".toc")) {
    tb.hidden = false;
    var syncToc = function () {
      var hidden = document.documentElement.classList.contains("no-toc");
      tb.setAttribute("aria-pressed", hidden ? "false" : "true");
      tb.setAttribute("aria-label", hidden ? "Show the right-hand outline" : "Hide the right-hand outline");
    };
    tb.addEventListener("click", function () {
      var hide = !document.documentElement.classList.contains("no-toc");
      document.documentElement.classList.toggle("no-toc", hide);
      try { localStorage.setItem("wiki.toc", hide ? "0" : "1"); } catch (e) {}
      syncToc();
    });
    syncToc();
  }

  /* ------------------------------------------------------------------ contents tree and drawer */
  var tree = $("#tree"), menuBtn = $("#menuBtn"), scrim = $("#scrim");
  function lessonLabel(u, s) { return u.name === "Overview" ? "Course overview" : (W.notes[s] || ["?"])[0]; }
  function tl(s, c, label) { return "<a class='tl" + (s === SLUG ? " on" : "") + (S.done[s] ? " done" : "") + "' href='" + noteUrl(s) + "' style='--c:" + c.color + "'>" + esc(label) + "</a>"; }
  function buildTree() {
    if (!tree) return;
    var c = (PAGE === "note" || PAGE === "course") ? courseById(COURSE) : null, h = "";
    body.classList.toggle("has-tree", !!c);
    if (c) {
      h += "<div class='tree-h'>Contents</div><a class='tree-course' href='" + ROOT + "course/" + c.id + ".html' style='--c:" + c.color + ";--cd:" + c.dark + "'><small>" + esc(c.code || "Course") + "</small>" + esc(c.title) + "</a>";
      c.units.forEach(function (u, i) {
        var done = u.lessons.filter(function (s) { return S.done[s]; }).length, open = u.lessons.indexOf(SLUG) >= 0 || c.units.length === 1 || (PAGE === "course" && i === 0);
        h += "<details" + (open ? " open" : "") + "><summary>" + esc(u.name) + "<span class='cnt'>" + done + "/" + u.lessons.length + "</span></summary>" +
          u.lessons.map(function (s) { return tl(s, c, lessonLabel(u, s)); }).join("") + "</details>";
      });
      if (c.problems.length) {
        h += "<details" + (c.problems.indexOf(SLUG) >= 0 ? " open" : "") + "><summary>Problem sets<span class='cnt'>" + c.problems.length + "</span></summary>" +
          c.problems.map(function (s) { return tl(s, c, W.notes[s][0]); }).join("") + "</details>";
      }
    }
    h += "<div class='tree-lib'><div class='tree-h'>" + (c ? "Other books" : "All books") + "</div>" +
      W.courses.filter(function (x) { return !c || x.id !== c.id; }).map(function (x) { return "<a href='" + ROOT + "course/" + x.id + ".html' style='--c:" + x.color + "'><i></i>" + esc(x.title) + "</a>"; }).join("") +
      "<a href='" + ROOT + "index.html' style='--c:#8a6a26'><i></i>Library shelf</a></div>";
    tree.innerHTML = h;
  }
  function drawer(on) {
    body.classList.toggle("drawer-on", on);
    if (menuBtn) menuBtn.setAttribute("aria-expanded", on ? "true" : "false");
    if (on && tree) { var cur = $(".tl.on", tree); if (cur) tree.scrollTop = Math.max(0, cur.offsetTop - tree.clientHeight / 3); }
  }
  buildTree();
  if (menuBtn) menuBtn.addEventListener("click", function () { drawer(!body.classList.contains("drawer-on")); });
  if (scrim) scrim.addEventListener("click", function () { drawer(false); });
  if (tree) tree.addEventListener("click", function (e) { if (e.target.closest("a")) drawer(false); });
  (function () { var cur = tree && $(".tl.on", tree); if (cur && window.innerWidth > 1000) tree.scrollTop = Math.max(0, cur.offsetTop - tree.clientHeight / 3); })();

  /* ------------------------------------------------------------------ search */
  var searchEl = $("#search"), qEl = $("#q"), resEl = $("#results"), sel = 0, hits = [];
  function ensureIndex(cb) {
    if (window.WIKI_SEARCH) return cb();
    var s = document.createElement("script"); s.src = ROOT + "assets/search.js"; s.onload = cb; document.head.appendChild(s);
  }
  function recentList() {
    var r = S.recent.filter(function (s) { return W.notes[s]; });
    if (!r.length) return "<div class='res-hint'>Type to search titles, headings and text.</div>";
    return "<div class='res-hint'>Recently opened</div>" + r.map(function (s, i) { return "<a class='res" + (i ? "" : " sel") + "' style='--c:" + colorOf(W.notes[s][1]) + "' href='" + noteUrl(s) + "'><b>" + esc(W.notes[s][0]) + "</b><small>" + esc(W.titles[W.notes[s][1]] || "") + "</small></a>"; }).join("");
  }
  function openSearch(term) {
    if (!searchEl) return; drawer(false);
    searchEl.hidden = false; qEl.value = typeof term === "string" ? term : ""; resEl.innerHTML = ""; qEl.focus(); ensureIndex(function () { run(); });
  }
  function closeSearch() { if (searchEl) searchEl.hidden = true; }
  function run() {
    var q = qEl.value.trim().toLowerCase();
    if (!q) { resEl.innerHTML = recentList(); hits = []; sel = 0; return; }
    if (!window.WIKI_SEARCH) return;
    var toks = q.split(/\s+/); hits = [];
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
      return "<a class='res" + (i ? "" : " sel") + "' style='--c:" + colorOf(d.c) + "' href='" + noteUrl(d.s) + "'><b>" + esc(d.t) + "</b><small>" + esc(W.titles[d.c] || "") + (snip ? " · …" + snip + "…" : "") + "</small></a>";
    }).join("") || "<div class='res-hint'>No matches. Try fewer or different words.</div>";
  }
  ["#openSearch", "#openSearchDock"].forEach(function (id) { var b = $(id); if (b) b.addEventListener("click", function () { openSearch(); }); });
  var cs = $("#closeSearch"); if (cs) cs.addEventListener("click", closeSearch);
  if (location.hash.indexOf("#search=") === 0) openSearch(decodeURIComponent(location.hash.slice(8)));
  if (qEl) {
    qEl.addEventListener("input", run);
    qEl.addEventListener("keydown", function (e) {
      var items = $$("a.res", resEl);
      if (e.key === "ArrowDown" || e.key === "ArrowUp") { e.preventDefault(); sel = Math.max(0, Math.min(items.length - 1, sel + (e.key === "ArrowDown" ? 1 : -1))); items.forEach(function (r, i) { r.classList.toggle("sel", i === sel); }); if (items[sel]) items[sel].scrollIntoView({ block: "nearest" }); }
      if (e.key === "Enter" && items[sel]) location.href = items[sel].href;
    });
    searchEl.addEventListener("click", function (e) { if (e.target === searchEl) closeSearch(); });
  }
  document.addEventListener("keydown", function (e) {
    var tag = (document.activeElement || {}).tagName;
    if (e.key === "Escape") { closeSearch(); drawer(false); }
    if ((e.key === "/" && tag !== "INPUT" && tag !== "TEXTAREA" && tag !== "SELECT") || ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k")) { e.preventDefault(); openSearch(); }
  });

  /* ------------------------------------------------------------------ reading thread and back to top */
  var thread = $("#thread"), toTop = $("#toTop");
  function onScroll() {
    var y = window.pageYOffset || document.documentElement.scrollTop, h = document.documentElement.scrollHeight - window.innerHeight;
    if (thread && PAGE === "note") thread.style.width = (h > 0 ? Math.min(100, 100 * y / h) : 0) + "%";
    if (toTop) toTop.classList.toggle("on", y > 800);
  }
  window.addEventListener("scroll", onScroll, { passive: true }); onScroll();
  if (toTop) toTop.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: "smooth" }); });

  /* ------------------------------------------------------------------ library (home) */
  function courseProgress(c) {
    var all = []; c.units.forEach(function (u) { all = all.concat(u.lessons); });
    var d = all.filter(function (s) { return S.done[s]; }).length; return { done: d, total: all.length, all: all };
  }
  if (PAGE === "learn") {
    W.courses.forEach(function (c) {
      var el = $(".book[data-course='" + c.id + "'] .bar i"); if (!el) return;
      var p = courseProgress(c); el.style.width = p.total ? (100 * p.done / p.total) + "%" : "0";
    });
    var cont = $("#continue"), last = S.last && W.notes[S.last];
    var first = (W.courses.filter(function (c) { return !c.upcoming && c.units.length; })[0] || {});
    if (cont) {
      if (last) cont.innerHTML = "<small>Pick up where you left off</small><h3>" + esc(W.notes[S.last][0]) + "</h3><a class='btn' href='" + noteUrl(S.last) + "'>Continue reading</a>";
      else cont.innerHTML = "<small>New here?</small><h3>Start with " + esc(first.title || "the first book") + "</h3><a class='btn' href='course/" + (first.id || "") + ".html'>Open the book</a>";
    }
    var rc = $("#recent"), rh = $("#recentH"), rec = S.recent.filter(function (s) { return W.notes[s]; }).slice(0, 6);
    if (rc && rec.length) {
      rh.hidden = false;
      rc.innerHTML = rec.map(function (s) { return "<a style='--c:" + colorOf(W.notes[s][1]) + "' href='" + noteUrl(s) + "'>" + esc(W.notes[s][0]) + "</a>"; }).join("");
    }
  }

  /* ------------------------------------------------------------------ course page */
  if (PAGE === "course") {
    var c = courseById(COURSE);
    if (c) {
      var p = courseProgress(c), cur = null;
      $$(".node[data-slug]").forEach(function (n) {
        var done = !!S.done[n.dataset.slug]; n.classList.toggle("done", done);
        if (!done && !cur) { cur = n; n.classList.add("current"); }
      });
      $$(".pcard[data-slug]").forEach(function (n) { if (Object.keys(S.solved).some(function (k) { return k.indexOf(n.dataset.slug + "#") === 0; })) n.classList.add("done"); });
      var st = $(".stat b"); if (st) st.textContent = (p.total ? Math.round(100 * p.done / p.total) : 0) + "%";
    }
  }

  /* ------------------------------------------------------------------ note page */
  if (PAGE === "note") {
    pushRecent(SLUG);
    var md = $("#markDone");
    function paintDone() {
      if (!md) return; var d = !!S.done[SLUG];
      md.textContent = d ? "Read ✓" : "Mark as read"; md.classList.toggle("btn-done", d); md.classList.toggle("btn-ghost", !d);
      var t = $(".tl.on", tree || document); if (t) t.classList.toggle("done", d);
    }
    if (md) { md.addEventListener("click", function () { if (S.done[SLUG]) { delete S.done[SLUG]; save(); } else markDone(SLUG); paintDone(); }); paintDone(); }

    // inline formulas wider than the page scroll sideways instead of stretching the layout
    function fitMath() {
      $$(".body .katex").forEach(function (k) {
        if (k.closest(".katex-display") || k.closest(".kx-scroll")) return;
        var host = k.closest("p,li,td,th,summary,.sm,div") || k.parentNode, hr = host.getBoundingClientRect();
        if (k.getBoundingClientRect().right > hr.right + 1 && hr.width > 0) k.classList.add("kx-scroll");
      });
    }
    fitMath(); window.addEventListener("load", fitMath);

    // task checkboxes
    $$("input[data-task]").forEach(function (i) {
      var k = i.dataset.task; if (S.tasks[k] !== undefined) i.checked = S.tasks[k];
      i.addEventListener("change", function () { S.tasks[k] = i.checked; save(); });
    });

    // problems: mark solved (rubber stamp)
    $$(".prob").forEach(function (p) {
      var q = p.dataset.q, g = document.createElement("div"); g.className = "grade";
      g.innerHTML = "<span>How did it go?</span><button class='btn' type='button'>I solved it</button><button class='btn btn-ghost' type='button'>Revisit later</button>";
      p.appendChild(g);
      var yes = g.children[1];
      function paint() { var s = !!S.solved[q]; p.classList.toggle("solved", s); yes.textContent = s ? "Solved ✓" : "I solved it"; yes.classList.toggle("btn-done", s); }
      yes.addEventListener("click", function () { if (S.solved[q]) delete S.solved[q]; else S.solved[q] = Date.now(); save(); paint(); });
      g.children[2].addEventListener("click", function () { if (S.solved[q]) { delete S.solved[q]; save(); paint(); } });
      paint();
    });

    // "on this page": sidebar scrollspy plus a collapsible list on narrow screens
    var tocLinks = $$(".toc a");
    if (tocLinks.length) {
      var j = document.createElement("details"); j.className = "jump";
      j.innerHTML = "<summary>On this page</summary>" + tocLinks.map(function (a) { return "<a href='" + a.getAttribute("href") + "'>" + a.innerHTML + "</a>"; }).join("");
      var bodyEl = $(".body"); if (bodyEl) bodyEl.parentNode.insertBefore(j, bodyEl);
      j.addEventListener("click", function (e) { if (e.target.closest("a")) j.open = false; });
      if ("IntersectionObserver" in window) {
        var map = {}; tocLinks.forEach(function (a) { map[a.getAttribute("href").slice(1)] = a; });
        var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting && map[e.target.id]) { tocLinks.forEach(function (a) { a.classList.remove("on"); }); map[e.target.id].classList.add("on"); } }); }, { rootMargin: "-10% 0px -80% 0px" });
        $$(".body h2[id]").forEach(function (h) { io.observe(h); });
      }
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

    // small pin-board of this note's neighbours
    var mg = $("#miniGraph");
    if (mg) {
      var neigh = {}; (W.links[SLUG] || []).concat(W.back[SLUG] || []).forEach(function (s) { if (W.notes[s] && s !== SLUG) neigh[s] = 1; });
      var list = Object.keys(neigh).slice(0, 22), ctx = mg.getContext("2d"), dpr = window.devicePixelRatio || 1, Wd = 640, Hd = 320;
      mg.width = Wd * dpr; mg.height = Hd * dpr; ctx.scale(dpr, dpr);
      var pos = [{ s: SLUG, x: Wd / 2, y: Hd / 2, r: 12 }];
      list.forEach(function (s, i) { var a = (i / list.length) * Math.PI * 2 - Math.PI / 2; pos.push({ s: s, x: Wd / 2 + Math.cos(a) * 250, y: Hd / 2 + Math.sin(a) * 118, r: 8 }); });
      var col = function (s) { return colorOf(W.notes[s][1]); };
      var pin = function (c, x, y, r) {
        c.save(); c.shadowColor = "rgba(0,0,0,.5)"; c.shadowBlur = 5; c.shadowOffsetX = 2; c.shadowOffsetY = 3;
        c.fillStyle = col_; c.beginPath(); c.arc(x, y, r, 0, 7); c.fill(); c.restore();
        c.fillStyle = "rgba(255,255,255,.55)"; c.beginPath(); c.arc(x - r * .3, y - r * .32, r * .32, 0, 7); c.fill();
      };
      var col_ = "#999";
      var tag = function (c, text, x, y) {
        c.font = "700 11px system-ui,sans-serif"; var w = c.measureText(text).width + 12;
        c.fillStyle = "rgba(251,246,230,.96)"; c.shadowColor = "rgba(0,0,0,.35)"; c.shadowBlur = 3; c.shadowOffsetY = 1; c.fillRect(x - w / 2, y - 11, w, 17); c.shadowColor = "transparent";
        c.fillStyle = "#2a2318"; c.textAlign = "center"; c.fillText(text, x, y + 1);
      };
      var draw = function (hov) {
        ctx.clearRect(0, 0, Wd, Hd); ctx.lineWidth = 1.6;
        var thr = getComputedStyle(document.documentElement).getPropertyValue("--string").trim() || "rgba(150,38,32,.6)";
        pos.slice(1).forEach(function (p) { ctx.strokeStyle = thr; ctx.beginPath(); ctx.moveTo(pos[0].x, pos[0].y); ctx.lineTo(p.x, p.y); ctx.stroke(); });
        pos.forEach(function (p, i) {
          col_ = col(p.s); pin(ctx, p.x, p.y, p.r + (hov === i ? 3 : 0));
          if (i === 0 || hov === i) { var t = W.notes[p.s][0]; if (t.length > 34) t = t.slice(0, 32) + "…"; tag(ctx, t, Math.max(80, Math.min(Wd - 80, p.x)), p.y + (p.y > Hd / 2 || i === 0 ? 32 : -22)); }
        });
      };
      var hit = function (e) { var r = mg.getBoundingClientRect(), x = (e.clientX - r.left) * Wd / r.width, y = (e.clientY - r.top) * Hd / r.height, h = -1; pos.forEach(function (p, i) { if (Math.hypot(p.x - x, p.y - y) < p.r + 8) h = i; }); return h; };
      mg.addEventListener("mousemove", function (e) { var h = hit(e); mg.style.cursor = h > 0 ? "pointer" : "default"; draw(h); });
      mg.addEventListener("click", function (e) { var h = hit(e); if (h > 0) { if (e.pointerType === "touch" && mg.dataset.sel !== String(h)) { mg.dataset.sel = h; draw(h); } else location.href = pos[h].s + ".html"; } });
      draw(-1); document.addEventListener("themechange", function () { draw(-1); });
    }

    // study mode: one page at a time
    var sb = $("#startLesson");
    if (sb) sb.addEventListener("click", startStudy);
    if (sb && location.hash === "#lesson") startStudy();
    function startStudy() {
      var steps = $$(".body > .step"); if (steps.length < 1) return;
      var i = 0, color = getComputedStyle($(".note")).getPropertyValue("--c");
      var ov = document.createElement("div"); ov.className = "lesson";
      ov.innerHTML = "<div class='lesson-top'><button class='lesson-x' aria-label='Close study mode'>✕</button><div class='lesson-bar'><i></i></div><span class='lesson-count'></span></div><div class='lesson-main'><div class='lesson-card' style='--c:" + color + "'></div></div><div class='lesson-foot'><div class='in'><button class='btn btn-ghost' id='lBack'>◂ Back</button><button class='btn' id='lNext'>Next ▸</button></div></div>";
      document.body.appendChild(ov); body.classList.add("lesson-on");
      var card = $(".lesson-card", ov), bar = $(".lesson-bar i", ov), cnt = $(".lesson-count", ov), nextBtn = $("#lNext", ov), backBtn = $("#lBack", ov);
      function show() {
        var s = steps[i], h2 = $("h2", s), label = i === 0 && !h2 ? "Overview" : "Page " + (i + 1) + " of " + steps.length;
        card.innerHTML = "<div class='step-label'>" + label + "</div>" + s.innerHTML;
        $$(".widget", card).forEach(function (w) { w.innerHTML = ""; w.removeAttribute("data-init"); });
        if (window.initWidgets) window.initWidgets(card);
        $$("details.rv", card).forEach(function (d) { d.open = false; });
        bar.style.width = (100 * (i + 1) / steps.length) + "%"; cnt.textContent = (i + 1) + " / " + steps.length;
        nextBtn.textContent = i === steps.length - 1 ? "Finish" : "Next ▸"; backBtn.style.visibility = i ? "visible" : "hidden";
        $(".lesson-main", ov).scrollTop = 0;
      }
      function finish() {
        markDone(SLUG); paintDone(); bar.style.width = "100%";
        var nx = $(".pg-next"), href = nx ? nx.getAttribute("href") : null;
        card.innerHTML = "<div class='lesson-done'><div class='big'>✓</div><h2>Marked as read</h2><p>You went through all " + steps.length + " pages.</p></div>";
        $(".in", ov).innerHTML = "<button class='btn btn-ghost' id='lExit'>Back to the note</button>" + (href ? "<a class='btn' href='" + href + "'>Next page</a>" : "");
        $("#lExit", ov).addEventListener("click", close);
      }
      function close() { ov.remove(); body.classList.remove("lesson-on"); document.removeEventListener("keydown", key); }
      function go(d) { if (d > 0 && i === steps.length - 1) return finish(); i = Math.max(0, i + d); show(); }
      function key(e) { if (e.key === "Escape") close(); if (e.key === "ArrowRight" || e.key === "Enter") { var t = (document.activeElement || {}).tagName; if (t === "INPUT" || t === "SELECT" || t === "BUTTON") return; go(1); } if (e.key === "ArrowLeft") go(-1); }
      nextBtn.addEventListener("click", function () { go(1); }); backBtn.addEventListener("click", function () { go(-1); }); $(".lesson-x", ov).addEventListener("click", close);
      document.addEventListener("keydown", key); show();
    }
  }

  /* ------------------------------------------------------------------ practice / solve filters */
  function filters(itemSel) {
    var chips = $$(".fchip"), items = $$(itemSel), box = $("#sf"), cur = "all";
    function apply() {
      var q = box ? box.value.trim().toLowerCase() : "";
      items.forEach(function (it) {
        var ok = (cur === "all" || it.dataset.course === cur) && (!q || it.textContent.toLowerCase().indexOf(q) >= 0);
        it.style.display = ok ? "" : "none";
      });
      $$(".pgroup").forEach(function (g) { g.style.display = $$(".pcard", g).some(function (x) { return x.style.display !== "none"; }) ? "" : "none"; });
    }
    chips.forEach(function (c) { c.addEventListener("click", function () { chips.forEach(function (x) { x.classList.remove("on"); }); c.classList.add("on"); cur = c.dataset.f; apply(); }); });
    if (box) box.addEventListener("input", apply);
  }
  if (PAGE === "practice") {
    filters(".pcard");
    $$(".pcard[data-slug]").forEach(function (n) { if (Object.keys(S.solved).some(function (k) { return k.indexOf(n.dataset.slug + "#") === 0; })) n.classList.add("done"); });
    $$(".qs a[data-q]").forEach(function (a) { if (S.solved[a.dataset.q]) a.classList.add("done"); });
  }
  if (PAGE === "solve") filters(".scard");

  /* ------------------------------------------------------------------ link map: cork board, pins and thread */
  if (PAGE === "graph") {
    var cv = $("#graph"), ctx2 = cv.getContext("2d"), tip = $("#gtip"), N = W.graph.n, L = W.graph.l;
    var nodes = N.map(function (n, i) { var a = Math.random() * 6.283, r = 80 + Math.random() * 220; return { i: i, s: n[0], t: n[1], c: n[2], d: n[3], x: Math.cos(a) * r, y: Math.sin(a) * r, vx: 0, vy: 0 }; });
    var adj = N.map(function () { return []; }); L.forEach(function (e) { adj[e[0]].push(e[1]); adj[e[1]].push(e[0]); });
    var view = { x: 0, y: 0, k: 0.9 }, alpha = 1, hover = -1, dpr2 = window.devicePixelRatio || 1, drag = null;
    function size() { var r = cv.getBoundingClientRect(); cv.width = r.width * dpr2; cv.height = r.height * dpr2; }
    window.addEventListener("resize", size); size();
    if (window.innerWidth < 700) view.k = 0.62;
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
    function rad(n) { return 3.5 + Math.sqrt(n.d) * 1.5; }
    function draw() {
      var thr = getComputedStyle(document.documentElement).getPropertyValue("--string").trim() || "rgba(150,38,32,.6)";
      ctx2.setTransform(1, 0, 0, 1, 0, 0); ctx2.clearRect(0, 0, cv.width, cv.height);
      ctx2.setTransform(dpr2 * view.k, 0, 0, dpr2 * view.k, dpr2 * (cv.width / dpr2 / 2 + view.x), dpr2 * (cv.height / dpr2 / 2 + view.y));
      var hl = hover >= 0 ? adj[hover] : [];
      ctx2.lineCap = "round";
      L.forEach(function (e) {
        var on = hover >= 0 && (e[0] === hover || e[1] === hover);
        ctx2.strokeStyle = on ? "#d8301f" : thr; ctx2.lineWidth = (on ? 2.4 : 1.2) / view.k; ctx2.globalAlpha = hover >= 0 && !on ? 0.18 : 0.9;
        ctx2.beginPath(); ctx2.moveTo(nodes[e[0]].x, nodes[e[0]].y); ctx2.lineTo(nodes[e[1]].x, nodes[e[1]].y); ctx2.stroke();
      });
      nodes.forEach(function (n) {
        var dim = hover >= 0 && n.i !== hover && hl.indexOf(n.i) < 0, r = rad(n) + (n.i === hover ? 2 : 0);
        ctx2.globalAlpha = dim ? 0.3 : 1;
        ctx2.save(); ctx2.shadowColor = "rgba(0,0,0,.5)"; ctx2.shadowBlur = 4 * dpr2; ctx2.shadowOffsetX = 2 * dpr2; ctx2.shadowOffsetY = 3 * dpr2;
        ctx2.fillStyle = colorOf(n.c); ctx2.beginPath(); ctx2.arc(n.x, n.y, r, 0, 7); ctx2.fill(); ctx2.restore();
        ctx2.fillStyle = "rgba(255,255,255,.55)"; ctx2.beginPath(); ctx2.arc(n.x - r * .3, n.y - r * .32, r * .32, 0, 7); ctx2.fill();
      });
      ctx2.globalAlpha = 1; var fs = 11 / view.k; ctx2.font = "700 " + fs + "px system-ui,sans-serif"; ctx2.textAlign = "center";
      nodes.forEach(function (n) {
        if ((n.d >= 28 && view.k > 0.6) || n.i === hover || (hover >= 0 && hl.indexOf(n.i) >= 0 && view.k > 1) || view.k > 2.2) {
          var t = n.t.length > 30 ? n.t.slice(0, 28) + "…" : n.t, w = ctx2.measureText(t).width + 8 / view.k, y = n.y - rad(n) - 6 / view.k;
          ctx2.fillStyle = "rgba(251,246,230,.96)"; ctx2.fillRect(n.x - w / 2, y - fs, w, fs + 5 / view.k);
          ctx2.fillStyle = "#2a2318"; ctx2.fillText(t, n.x, y);
        }
      });
    }
    function loop() { if (alpha > 0.02) { for (var s = 0; s < 3; s++) tick(); } draw(); requestAnimationFrame(loop); }
    function toWorld(e) { var r = cv.getBoundingClientRect(); return { x: (e.clientX - r.left - r.width / 2 - view.x) / view.k, y: (e.clientY - r.top - r.height / 2 - view.y) / view.k }; }
    function pick(e) { var p = toWorld(e), h = -1, best = 1e9; nodes.forEach(function (n) { var d = Math.hypot(n.x - p.x, n.y - p.y); if (d < rad(n) + 6 && d < best) { best = d; h = n.i; } }); return h; }
    // pointer events: mouse drag/hover, one-finger pan, two-finger pinch, tap to preview then tap again to open
    var pts = {}, pinch = null;
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
      if (d.touch && hover !== h) { hover = h; showTip(e, h); }
      else location.href = noteUrl(nodes[h].s);
    }
    cv.addEventListener("pointerup", pend);
    cv.addEventListener("pointercancel", function (e) { delete pts[e.pointerId]; pinch = null; drag = null; });
    cv.addEventListener("wheel", function (e) { e.preventDefault(); var k = Math.max(0.3, Math.min(5, view.k * (e.deltaY < 0 ? 1.12 : 0.89))); view.k = k; }, { passive: false });
    for (var warm = 0; warm < 320; warm++) tick();
    loop();
  }
})();
