/* Engineering Notes: theme, contents, search, reading progress, study mode, practice marking, link map.
   No dependencies. Everything personal (progress, flags, theme) lives in this browser's localStorage. */
(function () {
  "use strict";
  const W = window.WIKI || { courses: [], notes: {}, colors: {}, titles: {}, graph: { n: [], l: [] }, back: {}, links: {}, cards: [] };
  const root = document.documentElement, body = document.body;
  const ROOT = body.dataset.root || "", PAGE = body.dataset.page, SLUG = body.dataset.slug, COURSE = body.dataset.course;
  const $ = (s, r) => (r || document).querySelector(s);
  const $$ = (s, r) => Array.from((r || document).querySelectorAll(s));
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const rxEsc = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  const noteUrl = (s) => ROOT + "n/" + s + ".html";
  const colorOf = (cid) => (W.colors[cid] || ["#888"])[0];
  const courseById = (id) => W.courses.find((c) => c.id === id);
  const tile = (c) => "<span class='tile' style='--c:" + c.color + "' aria-hidden='true'>" + esc(c.tag || "") + "</span>";
  const portraits = W.portraits || [];
  const portrait = (i, px, small) => { const p = portraits[((i % portraits.length) + portraits.length) % portraits.length]; return p ? "<img class='av' src='" + ROOT + "assets/waifu/" + p[0] + ".webp' alt='" + esc(p[1]) + "' width='" + px + "' height='" + px + "'" + (small ? " style='--s:" + px + "px'" : "") + " loading='lazy'>" : ""; };
  const css = (v) => getComputedStyle(root).getPropertyValue(v).trim();

  /* ------------------------------------------------------------------ browser-only store */
  const KEY = "wiki.progress.v1", CARDS_KEY = "wiki.cards.v1";
  const read = (k) => { try { return JSON.parse(localStorage.getItem(k)) || {}; } catch (e) { return {}; } };
  const S = read(KEY);
  S.done = S.done || {}; S.solved = S.solved || {}; S.tasks = S.tasks || {}; S.recent = S.recent || []; S.weak = S.weak || {};
  const save = () => { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) {} };
  const markDone = (slug) => { S.done[slug] = Date.now(); save(); };
  const pushRecent = (slug) => { S.recent = [slug].concat(S.recent.filter((s) => s !== slug)).filter((s) => W.notes[s]).slice(0, 8); S.last = slug; save(); };
  const lessonsOf = (c) => c.units.reduce((a, u) => a.concat(u.lessons), []);
  const progressOf = (c) => { const all = lessonsOf(c), d = all.filter((s) => S.done[s]).length; return { done: d, total: all.length, all }; };
  const anySolved = (slug) => Object.keys(S.solved).some((k) => k.indexOf(slug + "#") === 0);

  /* ------------------------------------------------------------------ theme */
  const repaint = [];                                   // functions that redraw canvases when the theme changes
  function setTheme(t) {
    root.dataset.theme = t;
    try { localStorage.setItem("wiki.theme", t); } catch (e) {}
    $$(".widget").forEach((w) => { const el = $("input[type=range]", w); if (el) el.dispatchEvent(new Event("input", { bubbles: true })); });
    if (window.__remermaid) window.__remermaid();
    repaint.forEach((f) => f());
  }
  const themeBtn = $("#themeBtn");
  if (themeBtn) themeBtn.addEventListener("click", () => setTheme(root.dataset.theme === "dark" ? "light" : "dark"));
  const mq = window.matchMedia && matchMedia("(prefers-color-scheme: dark)");
  if (mq && mq.addEventListener) mq.addEventListener("change", (e) => { try { if (localStorage.getItem("wiki.theme")) return; } catch (x) {} setTheme(e.matches ? "dark" : "light"); });

  /* ------------------------------------------------------------------ contents column and drawer */
  const side = $("#side"), menuBtn = $("#menuBtn"), scrim = $("#scrim");
  function drawer(on) {
    const was = body.classList.contains("drawer");
    body.classList.toggle("drawer", on);
    body.classList.toggle("locked", on || !!$(".lesson") || (!$("#search").hidden));
    const phone = innerWidth <= 900;
    if (menuBtn) { menuBtn.setAttribute("aria-expanded", on ? "true" : "false"); if (phone) menuBtn.setAttribute("aria-label", on ? "Close menu" : "Open menu"); }
    if (side) { if (phone) side.inert = !on; else side.inert = false; }
    if (on && side) {
      const cur = $("[aria-current]", side); if (cur) side.scrollTop = Math.max(0, cur.offsetTop - side.clientHeight / 3);
      const x = $(".side-x", side); if (x) x.focus({ preventScroll: true });
    } else if (was && menuBtn && side && side.contains(document.activeElement)) menuBtn.focus({ preventScroll: true });
  }
  function lessonLink(s, label) {
    const cls = (S.done[s] ? "done " : "") + (S.weak[s] ? "weak" : "");
    return "<a class='" + cls + "' href='" + noteUrl(s) + "'" + (s === SLUG ? " aria-current='page'" : "") + ">" + esc(label) + "</a>";
  }
  function buildSide() {
    if (!side) return;
    const c = (PAGE === "note" || PAGE === "course") ? courseById(COURSE) : null;
    let h = "<div class='side-top'><b>Menu</b><button type='button' class='ib side-x' aria-label='Close menu'>✕</button></div><nav class='side-nav' aria-label='Site'>" +
      $$(".nav a").map((a) => "<a href='" + a.getAttribute("href") + "'" + (a.hasAttribute("aria-current") ? " aria-current='page'" : "") + ">" + a.innerHTML + "</a>").join("") + "</nav>";
    if (c) {
      h += "<a class='side-course' href='" + ROOT + "course/" + c.id + ".html'" + (PAGE === "course" ? " aria-current='page'" : "") + ">" + tile(c) + "<span><small>" + esc(c.code || "Course") + "</small>" + esc(c.title) + "</span></a>";
      c.units.forEach((u, i) => {
        const n = u.lessons.filter((s) => S.done[s]).length;
        const open = u.lessons.indexOf(SLUG) >= 0 || c.units.length === 1 || (PAGE === "course" && i === 0);
        h += "<details" + (open ? " open" : "") + "><summary>" + esc(u.name) + "<span class='cnt'>" + n + "/" + u.lessons.length + "</span></summary>" +
          u.lessons.map((s) => lessonLink(s, u.name === "Overview" ? "Course overview" : W.notes[s][0])).join("") + "</details>";
      });
      if (c.problems.length) {
        h += "<details" + (c.problems.indexOf(SLUG) >= 0 ? " open" : "") + "><summary>Problem sets<span class='cnt'>" + c.problems.length + "</span></summary>" +
          c.problems.map((s) => lessonLink(s, W.notes[s][0])).join("") + "</details>";
      }
    }
    h += "<div class='side-h'>" + (c ? "Other courses" : "Courses") + "</div><div class='side-all'>" +
      W.courses.filter((x) => !c || x.id !== c.id).map((x) => "<a href='" + ROOT + "course/" + x.id + ".html'>" + tile(x) + esc(x.title) + "</a>").join("") + "</div>";
    side.innerHTML = h;
    const cur = $("[aria-current]", side);
    if (cur && innerWidth > 900) side.scrollTop = Math.max(0, cur.offsetTop - side.clientHeight / 3);
  }
  buildSide();
  if (menuBtn) menuBtn.addEventListener("click", () => {
    if (innerWidth > 900) {
      const hide = !root.classList.contains("no-side");
      root.classList.toggle("no-side", hide);
      try { localStorage.setItem("wiki.side", hide ? "0" : "1"); } catch (e) {}
      menuBtn.setAttribute("aria-label", hide ? "Show contents" : "Hide contents");
    } else drawer(!body.classList.contains("drawer"));
  });
  if (scrim) scrim.addEventListener("click", () => drawer(false));
  if (side) side.addEventListener("click", (e) => { if (e.target.closest("a") || e.target.closest(".side-x")) drawer(false); });
  if (menuBtn && innerWidth > 900) menuBtn.setAttribute("aria-label", root.classList.contains("no-side") ? "Show contents" : "Hide contents");
  drawer(false);
  window.addEventListener("resize", () => {
    if (innerWidth > 900 && body.classList.contains("drawer")) drawer(false);
    else if (side) side.inert = innerWidth <= 900 && !body.classList.contains("drawer");
  });

  /* ------------------------------------------------------------------ search */
  const sd = $("#search"), qEl = $("#q"), resEl = $("#results"), scEl = $("#sc");
  let sel = 0, fcourse = "all", lastFocus = null;
  function fuzzy(title, q) {                            // every letter of the query appears in order in the title
    const s = title.toLowerCase(); q = q.replace(/\s+/g, "");
    let j = 0, first = -1, gaps = 0, last = -1;
    for (let i = 0; i < s.length && j < q.length; i++) if (s[i] === q[j]) { if (first < 0) first = i; if (last >= 0) gaps += i - last - 1; last = i; j++; }
    return j === q.length && q.length >= 3 ? 40 - gaps - first : 0;
  }
  function ensureIndex(cb) {
    if (window.WIKI_SEARCH) return cb();
    const s = document.createElement("script"); s.src = ROOT + "assets/search.js"; s.onload = cb; s.onerror = () => { resEl.innerHTML = "<div class='res-hint'>The search index could not be loaded.</div>"; }; document.head.appendChild(s);
  }
  function resultLink(s, title, sub, first) {
    return "<a class='res" + (first ? " sel" : "") + "' href='" + noteUrl(s) + "'><b><span class='dot' style='--c:" + colorOf(W.notes[s][1]) + "'></span>" + esc(title) + "</b><small>" + sub + "</small></a>";
  }
  function recentList() {
    const r = S.recent.filter((s) => W.notes[s]);
    if (!r.length) return "<div class='res-hint'>Type to search titles, headings and text. Try:</div><div class='rels try'>" +
      ["buckling", "Laplace transform", "Bernoulli", "Mohr's circle", "resonance", "rectifier"].map((t) => "<button type='button' class='rel' data-try='" + esc(t) + "'>" + esc(t) + "</button>").join("") + "</div>";
    return "<div class='res-hint'>Recently opened</div>" + r.map((s, i) => resultLink(s, W.notes[s][0], esc(W.titles[W.notes[s][1]] || ""), i === 0)).join("");
  }
  function run() {
    const q = qEl.value.trim().toLowerCase();
    sel = 0;
    if (!q) { resEl.innerHTML = recentList(); return; }
    if (!window.WIKI_SEARCH) return;
    const toks = q.split(/\s+/);
    let hits = [];
    window.WIKI_SEARCH.forEach((d) => {
      if (fcourse !== "all" && d.c !== fcourse) return;
      const t = d.t.toLowerCase(), h = d.h.join(" ").toLowerCase(), x = d.x.toLowerCase();
      let score = 0, ok = true;
      for (const k of toks) {
        let s = 0;
        const ti = t.indexOf(k);
        if (ti >= 0) s += 12 + (ti === 0 ? 4 : 0);
        if (h.indexOf(k) >= 0) s += 5;
        const p = x.indexOf(k); if (p >= 0) { s += 1; if (x.indexOf(k, p + 1) >= 0) s += 1; }
        if (!s) { ok = false; break; } score += s;
      }
      if (ok) hits.push({ d, score });
    });
    let fz = false;
    if (!hits.length) { fz = true; window.WIKI_SEARCH.forEach((d) => { if (fcourse !== "all" && d.c !== fcourse) return; const f = fuzzy(d.t, q); if (f > 0) hits.push({ d, score: f }); }); }
    hits.sort((a, b) => b.score - a.score); hits = hits.slice(0, 30);
    const re = new RegExp("(" + toks.map(rxEsc).join("|") + ")", "ig");
    resEl.innerHTML = (fz && hits.length ? "<div class='res-hint'>No exact match. Closest titles:</div>" : "") + hits.map((h, i) => {
      const d = h.d, p = d.x.toLowerCase().indexOf(toks[0]);
      let snip = "";
      if (p >= 0) { const a = Math.max(0, p - 40); snip = " · …" + esc(d.x.slice(a, a + 130)).replace(re, "<mark>$1</mark>") + "…"; }
      return resultLink(d.s, d.t, esc(W.titles[d.c] || "") + snip, i === 0);
    }).join("") || "<div class='res-hint'>No matches. Try fewer or different words.</div>";
  }
  function openSearch(term) {
    if (!sd) return;
    drawer(false);
    lastFocus = document.activeElement;
    sd.hidden = false; body.classList.add("locked");
    qEl.value = typeof term === "string" ? term : ""; resEl.innerHTML = recentList(); qEl.focus();
    ensureIndex(run);
  }
  function closeSearch() {
    if (!sd || sd.hidden) return;
    sd.hidden = true; body.classList.toggle("locked", body.classList.contains("drawer") || !!$(".lesson"));
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }
  if (scEl) {
    W.courses.filter((c) => c.units.length).forEach((c) => { const o = document.createElement("option"); o.value = c.id; o.textContent = c.title; scEl.appendChild(o); });
    scEl.addEventListener("change", () => { fcourse = scEl.value; run(); qEl.focus(); });
  }
  $$("#openSearch,[data-open-search]").forEach((b) => b.addEventListener("click", () => openSearch()));
  const cs = $("#closeSearch"); if (cs) cs.addEventListener("click", closeSearch);
  if (location.hash.indexOf("#search=") === 0) openSearch(decodeURIComponent(location.hash.slice(8)));
  if (qEl) {
    qEl.placeholder = "Search notes…";
    qEl.addEventListener("input", run);
    resEl.addEventListener("click", (e) => {                       // example searches shown before you have any history
      const b = e.target.closest("[data-try]"); if (!b) return;
      qEl.value = b.dataset.try; qEl.focus(); ensureIndex(run); run();
    });
    qEl.addEventListener("keydown", (e) => {
      const items = $$("a.res", resEl);
      if (e.key === "ArrowDown" || e.key === "ArrowUp") {
        e.preventDefault(); if (!items.length) return;
        sel = Math.max(0, Math.min(items.length - 1, sel + (e.key === "ArrowDown" ? 1 : -1)));
        items.forEach((r, i) => r.classList.toggle("sel", i === sel)); items[sel].scrollIntoView({ block: "nearest" });
      }
      if (e.key === "Enter" && items[sel]) location.href = items[sel].href;
    });
    sd.addEventListener("mousedown", (e) => { if (e.target === sd) closeSearch(); });
  }
  document.addEventListener("keydown", (e) => {
    const tag = (document.activeElement || {}).tagName;
    const typing = tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT" || (document.activeElement || {}).isContentEditable;
    if (e.key === "Escape") { const z = $(".zoom"); if (z) { z.remove(); return; } if (sd && !sd.hidden) closeSearch(); else drawer(false); }
    if ((e.key === "/" && !typing && !e.ctrlKey && !e.metaKey) || ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k")) { e.preventDefault(); openSearch(); }
  });

  /* ------------------------------------------------------------------ reading progress and back to top */
  const thread = $("#thread"), toTop = $("#toTop");
  let ticking = false;
  function onScroll() {
    ticking = false;
    const y = window.pageYOffset, h = root.scrollHeight - innerHeight;
    if (thread && PAGE === "note") thread.style.width = (h > 0 ? Math.min(100, 100 * y / h) : 0) + "%";
    if (toTop) toTop.classList.toggle("on", y > 800);
  }
  window.addEventListener("scroll", () => { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();
  if (toTop) toTop.addEventListener("click", () => window.scrollTo({ top: 0, behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth" }));

  /* ------------------------------------------------------------------ home */
  if (PAGE === "home") {
    const pf = $("#portrait");
    if (pf && portraits.length) {                       // a different face greets you on each visit; purely decorative
      const i = Math.floor(Math.random() * portraits.length);
      pf.innerHTML = portrait(i, 132, false) + "<figcaption>Studying with " + esc(portraits[i][1]) + "</figcaption>"; pf.hidden = false;
    }
    W.courses.forEach((c) => {
      const el = $(".ccard[data-course='" + c.id + "'] .bar i"); if (!el) return;
      const p = progressOf(c); el.style.width = p.total ? (100 * p.done / p.total) + "%" : "0";
    });
    const g = $("#glance");
    if (g) {
      let allN = 0, doneN = 0;
      W.courses.forEach((c) => { const p = progressOf(c); allN += p.total; doneN += p.done; });
      const first = W.courses.find((c) => !c.upcoming && c.units.length) || {};
      const last = S.last && W.notes[S.last] ? S.last : null;
      const cs0 = read(CARDS_KEY), now = Date.now();
      let seen = 0, due = 0;
      (W.cards || []).forEach((cd) => { const st = cs0[cd[0]]; if (st) { seen++; if (st[1] <= now) due++; } });
      const fresh = (W.cards || []).length - seen;
      const weak = Object.keys(S.weak).filter((s) => W.notes[s]).sort((a, b) => S.weak[b] - S.weak[a]);
      let h = last ? "<a href='" + noteUrl(last) + "'><small>Continue</small><b>" + esc(W.notes[last][0]) + "</b></a>"
                   : "<a href='" + ROOT + "course/" + (first.id || "") + ".html'><small>Start here</small><b>" + esc(first.title || "The first course") + "</b></a>";
      h += "<a href='" + ROOT + "review.html'><small>Review</small><b>" + due + " due · " + fresh + " new</b></a>";
      if (weak.length) h += "<a href='" + noteUrl(weak[0]) + "'><small>Flagged to revise</small><b>" + weak.length + " note" + (weak.length === 1 ? "" : "s") + "</b></a>";
      h += "<div><small>Read so far</small><b>" + doneN + " of " + allN + " pages</b></div>";
      g.innerHTML = h;
      const rec = S.recent.filter((s) => W.notes[s] && s !== last).slice(0, 6);       // jump back into what you were reading
      if (rec.length) {
        const r = document.createElement("div"); r.className = "recent";
        r.innerHTML = "<small>Recently opened</small><div class='rels'>" + rec.map((s) => "<a class='rel' href='" + noteUrl(s) + "'><span class='dot' style='--c:" + colorOf(W.notes[s][1]) + "'></span>" + esc(W.notes[s][0]) + "</a>").join("") + "</div>";
        g.parentNode.insertBefore(r, g.nextSibling);
      }
    }
  }

  /* ------------------------------------------------------------------ course page */
  if (PAGE === "course") {
    const c = courseById(COURSE);
    if (c) {
      const p = progressOf(c);
      let cur = null;
      $$(".node[data-slug]").forEach((n) => {
        const done = !!S.done[n.dataset.slug]; n.classList.toggle("done", done);
        if (!done && !cur) { cur = n; n.classList.add("current"); }
      });
      $$(".node[data-prob]").forEach((n) => { if (anySolved(n.dataset.prob)) n.classList.add("done"); });
      const bar = $("#cbar"), txt = $("#cp");
      if (bar) bar.style.width = (p.total ? 100 * p.done / p.total : 0) + "%";
      if (txt) txt.textContent = p.done + " of " + p.total + " read";
      const hd = $(".chead > div");
      if (hd && cur) {                                                           // one obvious next step
        const a = document.createElement("a"); a.className = "btn btn-primary cta"; a.href = cur.getAttribute("href");
        const t = cur.querySelector(".t, .nt") || cur; a.textContent = (p.done ? "Continue: " : "Start with: ") + t.textContent.replace(/^\s*\d+\s*/, "").replace(/\s*✓\s*$/, "").trim();
        hd.appendChild(a);
      }
    }
  }

  /* ------------------------------------------------------------------ note page */
  if (PAGE === "note") {
    pushRecent(SLUG);
    $$(".body h2[id], .body h3[id], .body h4[id]").forEach((h) => {      // a hover link to each heading, so a section can be shared or bookmarked
      const a = document.createElement("a"); a.className = "perma"; a.href = "#" + h.id; a.setAttribute("aria-label", "Link to this section"); a.textContent = "#";
      h.insertBefore(a, h.firstChild);
    });
    document.addEventListener("keydown", (e) => {                       // [ and ] step to the previous and next note
      if (e.ctrlKey || e.metaKey || e.altKey || (e.key !== "[" && e.key !== "]")) return;
      const t = (document.activeElement || {}).tagName;
      if (t === "INPUT" || t === "TEXTAREA" || t === "SELECT" || $(".lesson") || $(".zoom") || !$("#search").hidden) return;
      const a = $(e.key === "]" ? ".pg-next[href]" : ".pager a.pg:not(.pg-next)"); if (a) location.href = a.href;
    });
    const md = $("#markDone"), mw = $("#markWeak");
    const paintDone = () => {
      if (!md) return; const d = !!S.done[SLUG];
      md.textContent = d ? "Read ✓" : "Mark as read"; md.classList.toggle("btn-done", d);
      const t = $("a[aria-current]", side || document); if (t) t.classList.toggle("done", d);
    };
    const paintWeak = () => {
      if (!mw) return; const w = !!S.weak[SLUG];
      mw.textContent = w ? "Flagged to revise ⚑" : "Revise later"; mw.setAttribute("aria-pressed", w ? "true" : "false");
      const t = $("a[aria-current]", side || document); if (t) t.classList.toggle("weak", w);
    };
    if (md) { md.addEventListener("click", () => { if (S.done[SLUG]) { delete S.done[SLUG]; save(); } else markDone(SLUG); paintDone(); }); paintDone(); }
    if (mw) { mw.addEventListener("click", () => { if (S.weak[SLUG]) delete S.weak[SLUG]; else S.weak[SLUG] = Date.now(); save(); paintWeak(); }); paintWeak(); }

    // tap a figure to open it full size; scroll or pinch to look closer
    $$(".body img").forEach((im) => im.addEventListener("click", () => {
      const z = document.createElement("div"); z.className = "zoom"; z.setAttribute("role", "dialog"); z.setAttribute("aria-label", "Figure");
      z.innerHTML = "<button type='button' aria-label='Close figure'>✕</button>";
      const big = document.createElement("img"); big.alt = im.alt || "Figure"; big.src = im.src; z.appendChild(big);
      z.addEventListener("click", (e) => { if (e.target.tagName !== "IMG") z.remove(); });
      document.body.appendChild(z); $("button", z).focus();
    }));

    // inline formulas wider than their line scroll sideways instead of stretching the page
    const fitMath = () => $$(".body .katex").forEach((k) => {
      if (k.closest(".katex-display") || k.closest(".kx-scroll")) return;
      const host = k.closest("p,li,td,th,summary,div") || k.parentNode, hr = host.getBoundingClientRect();
      if (hr.width > 0 && k.getBoundingClientRect().right > hr.right + 1) k.classList.add("kx-scroll");
    });
    fitMath(); window.addEventListener("load", fitMath);
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(fitMath);

    // task checkboxes
    $$("input[data-task]").forEach((i) => {
      const k = i.dataset.task; if (S.tasks[k] !== undefined) i.checked = S.tasks[k];
      i.addEventListener("change", () => { S.tasks[k] = i.checked; save(); });
    });

    // problems: mark solved, or flag the note for revision
    $$(".prob").forEach((p) => {
      const q = p.dataset.q, g = document.createElement("div"); g.className = "grade";
      g.innerHTML = "<span>How did it go?</span><button class='btn' type='button'>I solved it</button><button class='btn' type='button'>Revisit later</button>";
      p.appendChild(g);
      const yes = g.children[1], later = g.children[2];
      const paint = () => { const s = !!S.solved[q]; p.classList.toggle("solved", s); yes.textContent = s ? "Solved ✓" : "I solved it"; yes.classList.toggle("btn-done", s); later.setAttribute("aria-pressed", S.weak[SLUG] ? "true" : "false"); later.textContent = S.weak[SLUG] ? "Flagged to revise ⚑" : "Revisit later"; };
      yes.addEventListener("click", () => { if (S.solved[q]) delete S.solved[q]; else S.solved[q] = Date.now(); save(); paint(); });
      later.addEventListener("click", () => { if (S.weak[SLUG]) delete S.weak[SLUG]; else { S.weak[SLUG] = Date.now(); delete S.solved[q]; } save(); $$(".prob").forEach((x) => x.dispatchEvent(new Event("repaint"))); paintWeak(); });
      p.addEventListener("repaint", paint);
      paint();
    });

    // "on this page": scrollspy beside the text, a collapsible list on narrow screens
    const tocLinks = $$(".toc a");
    if (tocLinks.length) {
      const j = document.createElement("details"); j.className = "jump";
      j.innerHTML = "<summary>On this page</summary>" + tocLinks.map((a) => "<a href='" + a.getAttribute("href") + "'>" + a.innerHTML + "</a>").join("");
      const bodyEl = $(".body"); if (bodyEl) bodyEl.parentNode.insertBefore(j, bodyEl);
      j.addEventListener("click", (e) => { if (e.target.closest("a")) j.open = false; });
      if ("IntersectionObserver" in window) {
        const map = {}; tocLinks.forEach((a) => { map[a.getAttribute("href").slice(1)] = a; });
        const io = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting && map[e.target.id]) { tocLinks.forEach((a) => a.classList.remove("on")); map[e.target.id].classList.add("on"); } }), { rootMargin: "-10% 0px -80% 0px" });
        $$(".body h2[id]").forEach((h) => io.observe(h));
      }
    }

    // mermaid diagrams follow the theme
    if (window.mermaid) {
      const src = $$("pre.mermaid").map((e) => e.textContent);
      window.__remermaid = () => {
        const dark = root.dataset.theme === "dark";
        $$("pre.mermaid").forEach((e, i) => { e.removeAttribute("data-processed"); e.textContent = src[i]; });
        window.mermaid.initialize({ startOnLoad: false, theme: dark ? "dark" : "neutral", securityLevel: "loose", themeVariables: { fontFamily: "system-ui, sans-serif" } });
        window.mermaid.run({ querySelector: "pre.mermaid" }).catch(() => {});
      };
      window.__remermaid();
    }

    // small map of this note's neighbours
    const mg = $("#miniGraph");
    if (mg) {
      const neigh = {}; (W.links[SLUG] || []).concat(W.back[SLUG] || []).forEach((s) => { if (W.notes[s] && s !== SLUG) neigh[s] = 1; });
      const list = Object.keys(neigh).slice(0, 22), ctx = mg.getContext("2d"), dpr = window.devicePixelRatio || 1, Wd = 640, Hd = 320;
      mg.width = Wd * dpr; mg.height = Hd * dpr; ctx.scale(dpr, dpr);
      const pos = [{ s: SLUG, x: Wd / 2, y: Hd / 2, r: 11 }];
      list.forEach((s, i) => { const a = (i / list.length) * Math.PI * 2 - Math.PI / 2; pos.push({ s, x: Wd / 2 + Math.cos(a) * 250, y: Hd / 2 + Math.sin(a) * 118, r: 7 }); });
      const label = (text, x, y) => {
        ctx.font = "600 11.5px system-ui,sans-serif"; const w = ctx.measureText(text).width + 14;
        ctx.fillStyle = css("--surface"); ctx.strokeStyle = css("--line-2"); ctx.lineWidth = 1;
        ctx.beginPath(); ctx.roundRect ? ctx.roundRect(x - w / 2, y - 12, w, 20, 5) : ctx.rect(x - w / 2, y - 12, w, 20); ctx.fill(); ctx.stroke();
        ctx.fillStyle = css("--text"); ctx.textAlign = "center"; ctx.fillText(text, x, y + 2);
      };
      const draw = (hov) => {
        ctx.clearRect(0, 0, Wd, Hd); ctx.lineWidth = 1.2; ctx.strokeStyle = css("--line-2");
        pos.slice(1).forEach((p) => { ctx.beginPath(); ctx.moveTo(pos[0].x, pos[0].y); ctx.lineTo(p.x, p.y); ctx.stroke(); });
        pos.forEach((p, i) => {
          ctx.fillStyle = colorOf(W.notes[p.s][1]); ctx.strokeStyle = css("--surface"); ctx.lineWidth = 2;
          ctx.beginPath(); ctx.arc(p.x, p.y, p.r + (hov === i ? 3 : 0), 0, 7); ctx.fill(); ctx.stroke();
          if (i === 0 || hov === i) { let t = W.notes[p.s][0]; if (t.length > 34) t = t.slice(0, 32) + "…"; label(t, Math.max(80, Math.min(Wd - 80, p.x)), p.y + (p.y > Hd / 2 || i === 0 ? 30 : -22)); }
        });
      };
      const hit = (e) => { const r = mg.getBoundingClientRect(), x = (e.clientX - r.left) * Wd / r.width, y = (e.clientY - r.top) * Hd / r.height; let h = -1; pos.forEach((p, i) => { if (Math.hypot(p.x - x, p.y - y) < p.r + 8) h = i; }); return h; };
      mg.addEventListener("mousemove", (e) => { const h = hit(e); mg.style.cursor = h > 0 ? "pointer" : "default"; draw(h); });
      mg.addEventListener("click", (e) => { const h = hit(e); if (h > 0) { if (e.pointerType === "touch" && mg.dataset.sel !== String(h)) { mg.dataset.sel = h; draw(h); } else location.href = pos[h].s + ".html"; } });
      draw(-1); repaint.push(() => draw(-1));
    }

    // study mode: one section at a time
    const sb = $("#startLesson");
    if (sb) sb.addEventListener("click", startStudy);
    if (sb && location.hash === "#lesson") startStudy();
    function startStudy() {
      const steps = $$(".body > .step"); if (!steps.length || $(".lesson")) return;
      let i = 0;
      const ov = document.createElement("div"); ov.className = "lesson"; ov.setAttribute("role", "dialog"); ov.setAttribute("aria-label", "Study mode");
      ov.innerHTML = "<div class='lesson-top'><button class='lesson-x' type='button' aria-label='Close study mode'>✕</button><div class='lesson-bar'><i></i></div><span class='lesson-count'></span></div><div class='lesson-main'><div class='lesson-card'></div></div><div class='lesson-foot'><div class='in'><button class='btn' id='lBack' type='button'>◂ Back</button><button class='btn btn-primary' id='lNext' type='button'>Next ▸</button></div></div>";
      document.body.appendChild(ov); body.classList.add("locked");
      const card = $(".lesson-card", ov), bar = $(".lesson-bar i", ov), cnt = $(".lesson-count", ov), nextBtn = $("#lNext", ov), backBtn = $("#lBack", ov);
      const show = () => {
        const s = steps[i], label = i === 0 && !$("h2", s) ? "Overview" : "Section " + (i + 1) + " of " + steps.length;
        card.innerHTML = "<div class='step-label'>" + label + "</div><div class='body'>" + s.innerHTML + "</div>";
        $$(".perma", card).forEach((a) => a.remove());
        $$("[id]", card).forEach((e) => e.removeAttribute("id"));          // the note underneath owns these ids
        $$(".widget", card).forEach((w) => { w.innerHTML = ""; w.removeAttribute("data-init"); });
        if (window.initWidgets) window.initWidgets(card);
        $$("details.rv", card).forEach((d) => { d.open = false; });
        bar.style.width = (100 * (i + 1) / steps.length) + "%"; cnt.textContent = (i + 1) + " / " + steps.length;
        nextBtn.textContent = i === steps.length - 1 ? "Finish" : "Next ▸"; backBtn.style.visibility = i ? "visible" : "hidden";
        $(".lesson-main", ov).scrollTop = 0;
      };
      const close = () => { ov.remove(); body.classList.toggle("locked", body.classList.contains("drawer")); document.removeEventListener("keydown", key); if (sb) sb.focus(); };
      const finish = () => {
        markDone(SLUG); paintDone(); bar.style.width = "100%";
        const nx = $(".pg-next"), href = nx ? nx.getAttribute("href") : null;
        card.innerHTML = "<div class='lesson-done'><div class='big'>✓</div><h2>Marked as read</h2><p>You went through all " + steps.length + " sections.</p></div>";
        $(".in", ov).innerHTML = "<button class='btn' id='lExit' type='button'>Back to the note</button>" + (href ? "<a class='btn btn-primary' href='" + href + "'>Next page</a>" : "");
        $("#lExit", ov).addEventListener("click", close); $("#lExit", ov).focus();
      };
      const go = (d) => { if (d > 0 && i === steps.length - 1) return finish(); i = Math.max(0, i + d); show(); };
      function key(e) {
        if (!$(".lesson") || $(".zoom")) return;
        if (e.key === "Escape") { e.stopPropagation(); close(); return; }
        const t = (document.activeElement || {}).tagName;
        if (t === "INPUT" || t === "SELECT" || t === "TEXTAREA" || t === "SUMMARY") return;
        if (e.key === "ArrowRight") go(1);
        if (e.key === "ArrowLeft") go(-1);
      }
      nextBtn.addEventListener("click", () => go(1)); backBtn.addEventListener("click", () => go(-1)); $(".lesson-x", ov).addEventListener("click", close);
      document.addEventListener("keydown", key); show(); nextBtn.focus();
    }
  }

  /* ------------------------------------------------------------------ practice and how-to-solve filters */
  function filters(itemSel) {
    const items = $$(itemSel), box = $("#sf"), sel2 = $("#cf");
    const apply = () => {
      const q = box ? box.value.trim().toLowerCase() : "", cur = sel2 ? sel2.value : "all";
      items.forEach((it) => { it.hidden = !((cur === "all" || it.dataset.course === cur) && (!q || it.textContent.toLowerCase().indexOf(q) >= 0)); });
      $$(".pgroup").forEach((g) => { g.hidden = !$$(itemSel, g).some((x) => !x.hidden); });
    };
    if (box) box.addEventListener("input", apply);
    if (sel2) sel2.addEventListener("change", apply);
    apply();
  }
  if (PAGE === "practice") {
    filters(".pcard");
    $$(".pcard[data-slug]").forEach((n) => { if (anySolved(n.dataset.slug)) n.classList.add("done"); });
    $$(".qs a[data-q]").forEach((a) => { if (S.solved[a.dataset.q]) a.classList.add("done"); });
  }
  if (PAGE === "solve") filters(".scard");

  /* ------------------------------------------------------------------ link map */
  if (PAGE === "graph") {
    const cv = $("#graph"), ctx = cv.getContext("2d"), tip = $("#gtip"), N = W.graph.n, L = W.graph.l;
    const nodes = N.map((n, i) => { const a = Math.random() * 6.283, r = 80 + Math.random() * 220; return { i, s: n[0], t: n[1], c: n[2], d: n[3], x: Math.cos(a) * r, y: Math.sin(a) * r, vx: 0, vy: 0 }; });
    const adj = N.map(() => []); L.forEach((e) => { adj[e[0]].push(e[1]); adj[e[1]].push(e[0]); });
    const view = { x: 0, y: 0, k: innerWidth < 700 ? 0.62 : 0.9 }, dpr = window.devicePixelRatio || 1;
    let alpha = 1, hover = -1, drag = null, dirty = true, cw = 0, ch = 0;
    const size = () => { const r = cv.getBoundingClientRect(); cw = r.width; ch = r.height; cv.width = Math.max(1, r.width * dpr); cv.height = Math.max(1, r.height * dpr); dirty = true; };
    window.addEventListener("resize", size); size(); repaint.push(() => { dirty = true; });
    const tick = () => {
      const n = nodes.length;
      for (let i = 0; i < n; i++) {
        const a = nodes[i];
        for (let j = i + 1; j < n; j++) {
          const b = nodes[j]; let dx = a.x - b.x, dy = a.y - b.y; const d2 = dx * dx + dy * dy + 40;
          if (d2 > 160000) continue;
          const f = 2400 / d2, d = Math.sqrt(d2); dx = dx / d * f; dy = dy / d * f; a.vx += dx; a.vy += dy; b.vx -= dx; b.vy -= dy;
        }
        a.vx -= a.x * 0.0022; a.vy -= a.y * 0.0022;
      }
      L.forEach((e) => {
        const a = nodes[e[0]], b = nodes[e[1]]; let dx = b.x - a.x, dy = b.y - a.y; const d = Math.sqrt(dx * dx + dy * dy) + 0.01, f = (d - 60) * 0.012;
        dx = dx / d * f; dy = dy / d * f; a.vx += dx; a.vy += dy; b.vx -= dx; b.vy -= dy;
      });
      nodes.forEach((a) => { a.vx *= 0.82; a.vy *= 0.82; a.x += a.vx * alpha; a.y += a.vy * alpha; });
      alpha *= 0.992;
    };
    const rad = (n) => 3 + Math.sqrt(n.d) * 1.4;
    const draw = () => {
      const edge = css("--line-2"), accent = css("--accent"), surface = css("--surface"), text = css("--text");
      ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.clearRect(0, 0, cv.width, cv.height);
      ctx.setTransform(dpr * view.k, 0, 0, dpr * view.k, dpr * (cw / 2 + view.x), dpr * (ch / 2 + view.y));
      const hl = hover >= 0 ? adj[hover] : [];
      ctx.lineCap = "round";
      L.forEach((e) => {
        const on = hover >= 0 && (e[0] === hover || e[1] === hover);
        ctx.strokeStyle = on ? accent : edge; ctx.lineWidth = (on ? 1.8 : 1) / view.k; ctx.globalAlpha = hover >= 0 && !on ? 0.2 : 0.9;
        ctx.beginPath(); ctx.moveTo(nodes[e[0]].x, nodes[e[0]].y); ctx.lineTo(nodes[e[1]].x, nodes[e[1]].y); ctx.stroke();
      });
      nodes.forEach((n) => {
        const dim = hover >= 0 && n.i !== hover && hl.indexOf(n.i) < 0, r = rad(n) + (n.i === hover ? 2 : 0);
        ctx.globalAlpha = dim ? 0.3 : 1; ctx.fillStyle = colorOf(n.c); ctx.strokeStyle = surface; ctx.lineWidth = 1.5 / view.k;
        ctx.beginPath(); ctx.arc(n.x, n.y, r, 0, 7); ctx.fill(); ctx.stroke();
      });
      ctx.globalAlpha = 1; const fs = 11 / view.k; ctx.font = "600 " + fs + "px system-ui,sans-serif"; ctx.textAlign = "center";
      const placed = [];                                              // label boxes already drawn, so labels never pile on each other
      const free = (x, y, w, h) => { for (let i = 0; i < placed.length; i++) { const p = placed[i]; if (x < p[0] + p[2] && x + w > p[0] && y < p[1] + p[3] && y + h > p[1]) return false; } return true; };
      const order = nodes.slice().sort((a, b) => (b.i === hover) - (a.i === hover) || (hl.indexOf(b.i) >= 0) - (hl.indexOf(a.i) >= 0) || b.d - a.d);
      order.forEach((n) => {
        const want = n.i === hover || (hover >= 0 && hl.indexOf(n.i) >= 0 && view.k > 0.8) || (hover < 0 && ((n.d >= 28 && view.k > 0.6) || view.k > 2.2));
        if (!want || placed.length > 90) return;
        const t = n.t.length > 30 ? n.t.slice(0, 28) + "…" : n.t, w = ctx.measureText(t).width + 8 / view.k, y = n.y - rad(n) - 6 / view.k, h = fs + 5 / view.k;
        if (n.i !== hover && !free(n.x - w / 2, y - fs, w, h)) return;
        placed.push([n.x - w / 2, y - fs, w, h]);
        ctx.fillStyle = surface; ctx.globalAlpha = 0.92; ctx.fillRect(n.x - w / 2, y - fs, w, h);
        ctx.globalAlpha = 1; ctx.fillStyle = text; ctx.fillText(t, n.x, y);
      });
    };
    const loop = () => { if (alpha > 0.02) { for (let s = 0; s < 3; s++) tick(); dirty = true; } if (dirty) { draw(); dirty = false; } requestAnimationFrame(loop); };
    const toWorld = (e) => { const r = cv.getBoundingClientRect(); return { x: (e.clientX - r.left - r.width / 2 - view.x) / view.k, y: (e.clientY - r.top - r.height / 2 - view.y) / view.k }; };
    const pick = (e) => { const p = toWorld(e); let h = -1, best = 1e9; nodes.forEach((n) => { const d = Math.hypot(n.x - p.x, n.y - p.y); if (d < rad(n) + 6 && d < best) { best = d; h = n.i; } }); return h; };
    const pts = {}; let pinch = null;
    const showTip = (e, i) => { const r = cv.getBoundingClientRect(); tip.textContent = nodes[i].t + " · " + (W.titles[nodes[i].c] || ""); tip.style.left = Math.max(4, Math.min(r.width - 240, e.clientX - r.left + 12)) + "px"; tip.style.top = Math.max(4, e.clientY - r.top + 12) + "px"; tip.style.opacity = 1; };
    const pdist = () => { const k = Object.keys(pts); return Math.hypot(pts[k[0]].x - pts[k[1]].x, pts[k[0]].y - pts[k[1]].y) || 1; };
    cv.addEventListener("pointerdown", (e) => {
      try { cv.setPointerCapture(e.pointerId); } catch (x) {}
      pts[e.pointerId] = { x: e.clientX, y: e.clientY };
      const n = Object.keys(pts).length;
      if (n === 1) drag = { x: e.clientX, y: e.clientY, vx: view.x, vy: view.y, moved: false, touch: e.pointerType !== "mouse" };
      else if (n === 2) { drag = null; pinch = { d: pdist(), k: view.k }; }
    });
    cv.addEventListener("pointermove", (e) => {
      if (pts[e.pointerId]) pts[e.pointerId] = { x: e.clientX, y: e.clientY };
      if (pinch && Object.keys(pts).length === 2) { view.k = Math.max(0.3, Math.min(5, pinch.k * pdist() / pinch.d)); dirty = true; return; }
      if (drag) {
        const dx = e.clientX - drag.x, dy = e.clientY - drag.y;
        if (!drag.moved && Math.hypot(dx, dy) > 5) drag.moved = true;
        if (drag.moved) { view.x = drag.vx + dx; view.y = drag.vy + dy; tip.style.opacity = 0; dirty = true; }
        return;
      }
      if (e.pointerType === "mouse") {
        const h = pick(e); if (h !== hover) { hover = h; dirty = true; }
        cv.style.cursor = hover >= 0 ? "pointer" : "grab";
        if (hover >= 0) showTip(e, hover); else tip.style.opacity = 0;
      }
    });
    const pend = (e) => {
      const d = drag; delete pts[e.pointerId];
      if (Object.keys(pts).length < 2) pinch = null;
      drag = null;
      if (!d || d.moved) return;
      const h = pick(e);
      if (h < 0) { if (d.touch) { hover = -1; tip.style.opacity = 0; dirty = true; } return; }
      if (d.touch && hover !== h) { hover = h; showTip(e, h); dirty = true; }
      else location.href = noteUrl(nodes[h].s);
    };
    cv.addEventListener("pointerup", pend);
    cv.addEventListener("pointercancel", (e) => { delete pts[e.pointerId]; pinch = null; drag = null; });
    cv.addEventListener("wheel", (e) => { e.preventDefault(); view.k = Math.max(0.3, Math.min(5, view.k * (e.deltaY < 0 ? 1.12 : 0.89))); dirty = true; }, { passive: false });
    for (let warm = 0; warm < 320; warm++) tick();
    loop();
  }
})();
