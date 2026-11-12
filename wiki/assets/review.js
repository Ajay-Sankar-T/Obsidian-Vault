/* Review: flashcards and multiple-choice self-test built from the notes' question callouts.
   Spaced repetition in six boxes; the schedule lives in this browser only (localStorage). No dependencies. */
(function () {
  "use strict";
  const W = window.WIKI || { courses: [], colors: {}, titles: {} };
  const DECK = window.WIKI_CARDS || [];
  const root = document.getElementById("rv");
  if (!root) return;
  const KEY = "wiki.cards.v1", PKEY = "wiki.progress.v1", OKEY = "wiki.review.opts";
  const DAY = 864e5, GAPS = [0, 1, 3, 7, 16, 35];                 // days until a card returns, by box
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const load = (k) => { try { return JSON.parse(localStorage.getItem(k)) || {}; } catch (e) { return {}; } };
  const ST = load(KEY);                                           // id -> [box, due, lapses]
  const save = () => { try { localStorage.setItem(KEY, JSON.stringify(ST)); } catch (e) {} };
  const opts = Object.assign({ mode: "cards", deck: "all", queue: "due" }, load(OKEY));
  const keep = () => { try { localStorage.setItem(OKEY, JSON.stringify(opts)); } catch (e) {} };
  let queue = [], pos = 0, shown = false, picked = null, skipped = false, stats = { good: 0, again: 0 };

  const byCourse = {};
  DECK.forEach((d) => { byCourse[d.c] = (byCourse[d.c] || 0) + 1; });
  if (opts.deck !== "all" && !byCourse[opts.deck]) opts.deck = "all";      // a stored deck that no longer exists
  const weakNotes = () => load(PKEY).weak || {};
  const pool = () => DECK.filter((d) => (opts.deck === "all" || d.c === opts.deck) && (opts.mode === "cards" || d.m));

  function counts() {
    const now = Date.now(); let due = 0, fresh = 0, known = 0;
    const p = pool();
    p.forEach((d) => { const s = ST[d.i]; if (!s) fresh++; else { if (s[1] <= now) due++; if (s[0] >= 3) known++; } });
    return { due, fresh, known, total: p.length };
  }
  function shuffle(a) { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }
  function build() {
    const now = Date.now(), p = pool();
    if (opts.queue === "all") queue = shuffle(p.slice());
    else if (opts.queue === "weak") { const w = weakNotes(); queue = shuffle(p.filter((d) => w[d.s])); }
    else {
      const due = p.filter((d) => ST[d.i] && ST[d.i][1] <= now).sort((a, b) => ST[a.i][1] - ST[b.i][1]);
      queue = due.slice(0, 30).concat(shuffle(p.filter((d) => !ST[d.i])).slice(0, 12));
    }
    pos = 0; shown = false; picked = null; skipped = false; stats = { good: 0, again: 0 };
  }
  function grade(d, ok, bonus) {                                   // one place that moves a card between boxes
    const s = ST[d.i] || [0, 0, 0], now = Date.now();
    if (ok) { s[0] = Math.min(GAPS.length - 1, s[0] + (bonus || 1)); s[1] = now + GAPS[s[0]] * DAY; stats.good++; }
    else {
      s[0] = 0; s[1] = now + 10 * 60 * 1000; s[2] = (s[2] || 0) + 1; stats.again++;
      if (queue.indexOf(d, pos + 1) < 0) queue.push(d);            // see it again this session, but only once
    }
    ST[d.i] = s; save();
  }

  function head() {
    const c = counts();
    const decks = '<option value="all">All courses (' + DECK.length + ')</option>' + W.courses.filter((x) => byCourse[x.id]).map((x) => '<option value="' + x.id + '"' + (opts.deck === x.id ? " selected" : "") + '>' + esc(x.title) + ' (' + byCourse[x.id] + ')</option>').join("");
    const seg = (name, items) => '<div class="seg" role="group" aria-label="' + name + '">' + items.map((i) => '<button type="button" data-' + i[0] + '="' + i[1] + '" aria-pressed="' + (opts[i[0]] === i[1]) + '" class="' + (opts[i[0]] === i[1] ? "on" : "") + '">' + i[2] + '</button>').join("") + "</div>";
    return '<div class="rv-stats"><span><b>' + c.due + '</b>due now</span><span><b>' + c.fresh + '</b>not seen yet</span><span><b>' + c.known + '</b>well known</span><span><b>' + c.total + '</b>in this deck</span></div>' +
      '<div class="rv-controls">' + seg("Mode", [["mode", "cards", "Flashcards"], ["mode", "quiz", "Multiple choice <em>" + root.dataset.mcq + "</em>"]]) +
      seg("Queue", [["queue", "due", "Due and new"], ["queue", "weak", "Flagged notes"], ["queue", "all", "Everything"]]) + "</div>" +
      '<div class="rv-decks"><select id="rvDeck" aria-label="Deck">' + decks + "</select></div>";
  }

  const PORT = W.portraits || [];
  function face(d) {                                               // a decorative face, fixed per card so it does not change on redraw
    if (!PORT.length) return "";
    let h = 0; for (let i = 0; i < d.i.length; i++) h = (h * 31 + d.i.charCodeAt(i)) >>> 0;
    const p = PORT[h % PORT.length];
    return '<img class="av" src="assets/waifu/' + p[0] + '.webp" alt="' + esc(p[1]) + '" width="28" height="28" style="--s:28px" loading="lazy">';
  }
  function cardHTML(d) {
    const left = queue.length - pos, pct = queue.length ? Math.round(100 * pos / queue.length) : 0;
    let h = '<div class="rv-progress"><i style="width:' + pct + '%"></i></div><div class="rv-count">' + (pos + 1) + ' of ' + queue.length + ' · ' + left + ' to go</div>';
    h += '<article class="rv-card"><header><span class="rv-course">' + face(d) + esc(W.titles[d.c] || "") + '</span><a class="rv-src" href="n/' + d.s + '.html">' + esc(d.n) + ' ↗</a></header><div class="rv-q">' + d.q + '</div>';
    if (opts.mode === "quiz" && d.m && !skipped) {
      const letters = ["a", "b", "c", "d"].concat(d.q.indexOf("(e)") >= 0 ? ["e"] : []);
      h += '<div class="rv-opts">' + letters.map((l) => {
        const cls = picked ? (l === d.m ? " right" : (l === picked ? " wrong" : "")) : "";
        return '<button type="button" class="rv-opt' + cls + '" data-pick="' + l + '"' + (picked ? " disabled" : "") + '><kbd>' + l.toUpperCase() + '</kbd></button>';
      }).join("") + '</div>';
      if (picked) h += '<div class="rv-verdict ' + (picked === d.m ? "ok" : "no") + '">' + (picked === d.m ? "Correct" : "Not quite. The answer is (" + d.m + ")") + '</div><div class="rv-a">' + d.a + '</div><div class="rv-actions"><button type="button" class="btn btn-primary" data-next="1">Next ▸</button></div>';
      else h += '<div class="rv-hint">Press A to ' + letters[letters.length - 1].toUpperCase() + ', or tap an option. <button type="button" class="linkish" data-skip="1">Show the answer instead</button></div>';
    } else if (shown) {
      h += '<div class="rv-a">' + d.a + '</div><div class="rv-actions"><span>How did it go?</span><button type="button" class="btn" data-rate="0"><kbd>1</kbd> Again</button><button type="button" class="btn btn-primary" data-rate="1"><kbd>2</kbd> Got it</button><button type="button" class="btn" data-rate="2"><kbd>3</kbd> Easy</button></div>';
    } else {
      h += '<div class="rv-actions"><button type="button" class="btn btn-primary" data-show="1">Show answer <kbd>Space</kbd></button></div>';
    }
    return h + "</article>";
  }

  function draw() {
    const hadFocus = root.contains(document.activeElement) && document.activeElement.tagName === "BUTTON";
    let h = head();
    if (!queue.length || pos >= queue.length) {
      const c = counts(), done = queue.length > 0;
      h += '<div class="rv-empty"><h2>' + (done ? "Session complete" : "Nothing waiting") + "</h2>" +
        (done ? "<p>" + stats.good + " remembered, " + stats.again + " to see again soon. Cards you miss return in ten minutes; the rest come back after a day, three days, a week and so on.</p>"
              : "<p>" + (opts.queue === "weak" ? "No cards belong to notes you flagged with “Revise later”. Flag a note while reading and its questions appear here." : opts.mode === "quiz" ? "No multiple-choice questions are due in this deck." : "You are all caught up in this deck.") + "</p>") +
        '<div class="rv-actions">' + (c.fresh || c.due ? '<button type="button" class="btn btn-primary" data-again="1">Start another round</button>' : "") + '<button type="button" class="btn" data-all="1">Practise everything</button></div></div>';
    } else h += cardHTML(queue[pos]);
    root.innerHTML = h;
    if (hadFocus) { const b = root.querySelector("[data-show],[data-next],[data-rate='1'],[data-again]"); if (b) b.focus({ preventScroll: true }); }
  }

  function rate(kind) {                                            // 0 again, 1 good, 2 easy
    const d = queue[pos]; if (!d) return;
    grade(d, kind > 0, kind);
    pos++; shown = false; picked = null; skipped = false; draw();
  }
  function pick(l) {
    const d = queue[pos]; if (!d || picked) return;
    picked = l; grade(d, l === d.m); draw();
  }
  function next() { pos++; shown = false; picked = null; skipped = false; draw(); }

  root.addEventListener("click", (e) => {
    const t = e.target.closest("button"); if (!t) return;
    const ds = t.dataset;
    if (ds.mode) { opts.mode = ds.mode; keep(); build(); draw(); }
    else if (ds.queue) { opts.queue = ds.queue; keep(); build(); draw(); }
    else if (ds.show) { shown = true; draw(); }
    else if (ds.rate) rate(+ds.rate);
    else if (ds.pick) pick(ds.pick);
    else if (ds.next) next();
    else if (ds.skip) { skipped = true; shown = true; draw(); }
    else if (ds.again) { build(); draw(); }
    else if (ds.all) { opts.queue = "all"; keep(); build(); draw(); }
  });
  root.addEventListener("change", (e) => { if (e.target.id === "rvDeck") { opts.deck = e.target.value; keep(); build(); draw(); } });

  document.addEventListener("keydown", (e) => {
    if (e.ctrlKey || e.metaKey || e.altKey) return;
    const a = document.activeElement || {}, tag = a.tagName;
    if (tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT") return;
    const sd = document.getElementById("search"); if (sd && !sd.hidden) return;
    const d = queue[pos]; if (!d || pos >= queue.length) return;
    const enterKey = e.key === " " || e.key === "Enter";
    if (tag === "BUTTON" && enterKey) return;                      // let the focused button handle it
    if (opts.mode === "quiz" && d.m && !skipped) {
      if (!picked && /^[a-e]$/i.test(e.key)) pick(e.key.toLowerCase());
      else if (picked && enterKey) { e.preventDefault(); next(); }
    } else if (!shown && enterKey) { e.preventDefault(); shown = true; draw(); }
    else if (shown && /^[123]$/.test(e.key)) rate(+e.key - 1);
  });

  if (!DECK.length) { root.innerHTML = '<div class="rv-empty"><h2>No questions yet</h2><p>Collapsible “question” callouts in the notes become cards here.</p></div>'; return; }
  build(); draw();
})();
