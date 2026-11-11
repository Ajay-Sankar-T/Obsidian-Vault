/* Review: flashcards and multiple-choice self-test built from the notes' question callouts.
   Spaced repetition in five boxes; the schedule lives in this browser only (localStorage). No dependencies. */
(function () {
  "use strict";
  const W = window.WIKI || { courses: [], colors: {}, titles: {} };
  const DECK = window.WIKI_CARDS || [];
  const root = document.getElementById("rv");
  if (!root) return;
  const KEY = "wiki.cards.v1", PKEY = "wiki.progress.v1";
  const DAY = 864e5, GAPS = [0, 1, 3, 7, 16, 35];              // days until a card returns, by box
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const load = (k) => { try { return JSON.parse(localStorage.getItem(k)) || {}; } catch (e) { return {}; } };
  let ST = load(KEY);                                          // id -> [box, due, lapses]
  const save = () => { try { localStorage.setItem(KEY, JSON.stringify(ST)); } catch (e) {} };
  const colour = (cid) => (W.colors[cid] || ["#a9812f"])[0];
  const opts = { mode: "cards", deck: "all", queue: "due" };
  try { Object.assign(opts, JSON.parse(localStorage.getItem("wiki.review.opts") || "{}")); } catch (e) {}
  let queue = [], pos = 0, shown = false, picked = null, skipped = false, stats = { good: 0, again: 0 };

  const byCourse = {};
  DECK.forEach((d) => { byCourse[d.c] = (byCourse[d.c] || 0) + 1; });
  const weakNotes = () => load(PKEY).weak || {};

  function counts() {
    const now = Date.now();
    let due = 0, fresh = 0, known = 0;
    DECK.forEach((d) => { const s = ST[d.i]; if (!s) fresh++; else { if (s[1] <= now) due++; if (s[0] >= 3) known++; } });
    return { due, fresh, known, total: DECK.length };
  }
  function pool() {
    return DECK.filter((d) => (opts.deck === "all" || d.c === opts.deck) && (opts.mode === "cards" || d.m));
  }
  function shuffle(a) { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); const t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function build() {
    const now = Date.now(), p = pool();
    let q;
    if (opts.queue === "all") q = shuffle(p.slice());
    else if (opts.queue === "weak") { const w = weakNotes(); q = shuffle(p.filter((d) => w[d.s])); }
    else {
      const due = p.filter((d) => ST[d.i] && ST[d.i][1] <= now).sort((a, b) => ST[a.i][1] - ST[b.i][1]);
      const fresh = shuffle(p.filter((d) => !ST[d.i])).slice(0, 12);
      q = due.slice(0, 30).concat(fresh);
    }
    queue = q; pos = 0; shown = false; picked = null; skipped = false; stats = { good: 0, again: 0 };
  }

  function rate(kind) {                                        // kind: 0 again, 1 good, 2 easy
    const d = queue[pos], s = ST[d.i] || [0, 0, 0], now = Date.now();
    if (kind === 0) { s[0] = 0; s[1] = now + 10 * 60 * 1000; s[2] = (s[2] || 0) + 1; stats.again++; queue.push(d); }
    else { s[0] = Math.min(GAPS.length - 1, s[0] + kind); s[1] = now + GAPS[s[0]] * DAY; stats.good++; }
    ST[d.i] = s; save();
    pos++; shown = false; picked = null; skipped = false; draw();
  }

  function head() {
    const c = counts();
    const chips = '<button type="button" class="fchip' + (opts.deck === "all" ? " on" : "") + '" data-deck="all">All <em>' + DECK.length + '</em></button>' +
      W.courses.filter((x) => byCourse[x.id]).map((x) => '<button type="button" class="fchip' + (opts.deck === x.id ? " on" : "") + '" data-deck="' + x.id + '" style="--c:' + x.color + '">' + esc(x.title) + ' <em>' + byCourse[x.id] + '</em></button>').join("");
    return '<div class="rv-stats"><span><b>' + c.due + '</b> due now</span><span><b>' + c.fresh + '</b> not seen yet</span><span><b>' + c.known + '</b> well known</span><span><b>' + c.total + '</b> cards</span></div>' +
      '<div class="rv-controls"><div class="seg" role="group" aria-label="Mode"><button type="button" data-mode="cards" class="' + (opts.mode === "cards" ? "on" : "") + '">Flashcards</button><button type="button" data-mode="quiz" class="' + (opts.mode === "quiz" ? "on" : "") + '">Multiple choice <em>' + root.dataset.mcq + '</em></button></div>' +
      '<div class="seg" role="group" aria-label="Queue"><button type="button" data-queue="due" class="' + (opts.queue === "due" ? "on" : "") + '">Due and new</button><button type="button" data-queue="weak" class="' + (opts.queue === "weak" ? "on" : "") + '">Flagged notes</button><button type="button" data-queue="all" class="' + (opts.queue === "all" ? "on" : "") + '">Everything</button></div></div>' +
      '<div class="filters">' + chips + '</div>';
  }

  function cardHTML(d) {
    const left = queue.length - pos, pct = queue.length ? Math.round(100 * pos / queue.length) : 0;
    let h = '<div class="rv-progress"><i style="width:' + pct + '%"></i></div><div class="rv-count">' + (pos + 1) + ' of ' + queue.length + ' · ' + left + ' to go</div>';
    h += '<article class="rv-card" style="--c:' + colour(d.c) + '"><header><span class="rv-course">' + esc(W.titles[d.c] || "") + '</span><a class="rv-src" href="n/' + d.s + '.html">' + esc(d.n) + ' ↗</a></header><div class="rv-q">' + d.q + '</div>';
    if (opts.mode === "quiz" && d.m && !skipped) {
      const letters = ["a", "b", "c", "d"].concat(d.q.indexOf("(e)") >= 0 ? ["e"] : []);
      h += '<div class="rv-opts">' + letters.map((l) => {
        let cls = "";
        if (picked) cls = l === d.m ? " right" : (l === picked ? " wrong" : "");
        return '<button type="button" class="rv-opt' + cls + '" data-pick="' + l + '"' + (picked ? " disabled" : "") + '><kbd>' + l.toUpperCase() + '</kbd></button>';
      }).join("") + '</div>';
      if (picked) h += '<div class="rv-verdict ' + (picked === d.m ? "ok" : "no") + '">' + (picked === d.m ? "Correct" : "Not quite: the answer is (" + d.m + ")") + '</div><div class="rv-a">' + d.a + '</div><div class="rv-actions"><button type="button" class="btn" data-next="1">Next ▸</button></div>';
      else h += '<div class="rv-hint">Press A to D, or tap an option. <button type="button" class="linkish" data-skip="1">Show the answer instead</button></div>';
    } else if (shown) {
      h += '<div class="rv-a">' + d.a + '</div><div class="rv-actions"><span>How did it go?</span><button type="button" class="btn btn-ghost" data-rate="0"><kbd>1</kbd> Again</button><button type="button" class="btn" data-rate="1"><kbd>2</kbd> Got it</button><button type="button" class="btn btn-ghost" data-rate="2"><kbd>3</kbd> Easy</button></div>';
    } else {
      h += '<div class="rv-actions"><button type="button" class="btn" data-show="1">Show answer <kbd>Space</kbd></button></div>';
    }
    return h + '</article>';
  }

  function draw() {
    let h = head();
    if (!queue.length || pos >= queue.length) {
      const c = counts(), done = queue.length > 0;
      h += '<div class="rv-empty"><h2>' + (done ? "Session complete" : "Nothing waiting") + '</h2>' +
        (done ? '<p>' + stats.good + ' remembered, ' + stats.again + ' to see again soon. Cards you missed return in ten minutes; the rest come back after a day, three days, a week and so on.</p>'
              : '<p>' + (opts.queue === "weak" ? "No cards belong to notes you flagged with “Revise later”. Flag a note while reading and its questions appear here." : opts.mode === "quiz" ? "No multiple-choice questions are due in this deck." : "You are all caught up in this deck.") + '</p>') +
        '<div class="rv-actions">' + (c.fresh || c.due ? '<button type="button" class="btn" data-again="1">Start another round</button>' : "") + '<button type="button" class="btn btn-ghost" data-all="1">Practise everything</button></div></div>';
    } else h += cardHTML(queue[pos]);
    root.innerHTML = h;
    if (window.renderMathInElement) { /* math is pre-rendered by the build */ }
  }

  root.addEventListener("click", (e) => {
    const t = e.target.closest("button"); if (!t) return;
    const d = queue[pos];
    if (t.dataset.deck) { opts.deck = t.dataset.deck; keep(); build(); draw(); }
    else if (t.dataset.mode) { opts.mode = t.dataset.mode; keep(); build(); draw(); }
    else if (t.dataset.queue) { opts.queue = t.dataset.queue; keep(); build(); draw(); }
    else if (t.dataset.show) { shown = true; draw(); }
    else if (t.dataset.rate) rate(+t.dataset.rate);
    else if (t.dataset.pick && d && !picked) pick(t.dataset.pick);
    else if (t.dataset.next) next();
    else if (t.dataset.skip) { skipped = true; shown = true; draw(); }
    else if (t.dataset.again) { build(); draw(); }
    else if (t.dataset.all) { opts.queue = "all"; keep(); build(); draw(); }
  });
  function keep() { try { localStorage.setItem("wiki.review.opts", JSON.stringify(opts)); } catch (e) {} }
  function pick(l) {
    const d = queue[pos]; picked = l;
    const ok = l === d.m, s = ST[d.i] || [0, 0, 0], now = Date.now();
    if (ok) { s[0] = Math.min(GAPS.length - 1, s[0] + 1); s[1] = now + GAPS[s[0]] * DAY; stats.good++; }
    else { s[0] = 0; s[1] = now + 10 * 60 * 1000; s[2] = (s[2] || 0) + 1; stats.again++; queue.push(d); }
    ST[d.i] = s; save(); draw();
  }
  function next() { pos++; shown = false; picked = null; skipped = false; draw(); }

  document.addEventListener("keydown", (e) => {
    if (e.ctrlKey || e.metaKey || e.altKey) return;
    const tag = (document.activeElement || {}).tagName;
    if (tag === "INPUT" || tag === "TEXTAREA" || !queue[pos] || pos >= queue.length) return;
    const d = queue[pos];
    if (opts.mode === "quiz" && d.m && !skipped) {
      if (!picked && /^[a-e]$/i.test(e.key)) { pick(e.key.toLowerCase()); }
      else if (picked && (e.key === " " || e.key === "Enter")) { e.preventDefault(); next(); }
    } else if (!shown && (e.key === " " || e.key === "Enter")) { e.preventDefault(); shown = true; draw(); }
    else if (shown && /^[123]$/.test(e.key)) rate(+e.key - 1);
  });

  if (!DECK.length) { root.innerHTML = '<div class="rv-empty"><h2>No questions yet</h2><p>Collapsible “question” callouts in the notes become cards here.</p></div>'; return; }
  build(); draw();
})();
