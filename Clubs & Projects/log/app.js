/* Saathi Log — AcadBuddy maintenance desk. No build step, no server: data lives in this browser (localStorage). */
(() => {
'use strict';

/* ---------- helpers ---------- */
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const uid = () => Math.random().toString(36).slice(2, 9);
const DAY = 864e5;
const pad = n => String(n).padStart(2, '0');
const iso = d => { const x = new Date(d); return `${x.getFullYear()}-${pad(x.getMonth() + 1)}-${pad(x.getDate())}`; };
const today = () => iso(new Date());
const parse = s => new Date(s + 'T00:00:00');
const daysBetween = (a, b) => Math.round((parse(b) - parse(a)) / DAY);
const ago = n => iso(new Date(Date.now() - n * DAY));
const fmtDate = s => parse(s).toLocaleDateString('en-IN', { day: 'numeric', month: 'short' });
const monthKey = d => iso(d).slice(0, 7);
const monthLabel = k => new Date(k + '-01T00:00:00').toLocaleDateString('en-IN', { month: 'long', year: 'numeric' });
const inr = n => '₹' + Number(n).toLocaleString('en-IN');
const IMG = n => `assets/${n}.png`;

/* ---------- state ---------- */
const KEY = 'saathi-log-v1';
const memory = {};
const store = {
  get() { try { return localStorage.getItem(KEY); } catch { return memory[KEY] ?? null; } },
  set(v) { try { localStorage.setItem(KEY, v); } catch { memory[KEY] = v; } }
};

function seed() {
  const s = true;
  return {
    v: 1,
    settings: { stipend: 350, cadence: 14, theme: 'light' },
    people: [
      { id: 'p1', role: 'mentor', name: 'Mira', course: 'Calculus', grade: 'S', cgpa: 9.1, disc: false, ui: false, sample: s },
      { id: 'p2', role: 'mentor', name: 'Rohan', course: 'Physics', grade: 'A', cgpa: 8.2, disc: false, ui: false, sample: s },
      { id: 'p3', role: 'mentor', name: 'Tara', course: 'Programming', grade: 'A', cgpa: 6.2, disc: false, ui: false, sample: s },
      { id: 'p4', role: 'mentee', name: 'Aarav', year: '1st', sample: s },
      { id: 'p5', role: 'mentee', name: 'Ishita', year: '1st', sample: s },
      { id: 'p6', role: 'mentee', name: 'Kabir', year: '2nd', sample: s }
    ],
    pairs: [
      { id: 'q1', mentorId: 'p1', menteeId: 'p4', course: 'Calculus', started: ago(60), status: 'active', sample: s },
      { id: 'q2', mentorId: 'p2', menteeId: 'p5', course: 'Physics', started: ago(45), status: 'active', sample: s },
      { id: 'q3', mentorId: 'p2', menteeId: 'p6', course: 'Physics', started: ago(40), status: 'active', sample: s }
    ],
    logs: [
      { id: uid(), date: ago(2), type: 'meetup', pairId: 'q1', title: 'Limits & continuity walkthrough', body: 'Went through tutorial 3 together. Aarav now knows where to start on epsilon-delta.', mood: 4, sample: s },
      { id: uid(), date: ago(5), type: 'check-in', pairId: 'q2', title: 'Quick call before quiz', body: 'Ishita nervous about the quiz; shared a revision order.', mood: 3, sample: s },
      { id: uid(), date: ago(9), type: 'win', pairId: 'q1', title: 'First S-grade tutorial', body: 'Aarav finished a tutorial unaided.', mood: 5, sample: s },
      { id: uid(), date: ago(12), type: 'concern', pairId: 'q3', title: 'Kabir missing meetups', body: 'Third reschedule in a row. Check if it is workload or something bigger; loop in a coordinator if needed.', mood: 2, resolved: false, sample: s },
      { id: uid(), date: ago(17), type: 'meetup', pairId: 'q2', title: 'Mechanics basics', body: 'Free-body diagrams. Used the "who pushes whom" trick.', mood: 4, sample: s },
      { id: uid(), date: ago(24), type: 'note', title: 'Orientation round-up', body: 'Collected FAQs from freshies: endsem format, where tutorials live, why everyone says CG.', mood: 3, sample: s },
      { id: uid(), date: ago(33), type: 'meetup', pairId: 'q3', title: 'Intro session', body: 'Set expectations: guide, support, empower; not a personal professor.', mood: 4, sample: s },
      { id: uid(), date: ago(41), type: 'meetup', pairId: 'q1', title: 'Course plan', body: 'Mapped the semester into weekly targets.', mood: 4, sample: s },
      { id: uid(), date: ago(58), type: 'note', title: 'Matching done', body: 'Paired by course and slot availability.', mood: 3, sample: s },
      { id: uid(), date: ago(70), type: 'note', title: 'Kick-off', body: 'Mentor interviews done. Pairs go live.', mood: 5, sample: s }
    ],
    tasks: [
      { id: uid(), title: 'Collect mentor feedback forms', col: 'todo', due: ago(-4), tag: 'feedback', notes: '', sample: true },
      { id: uid(), title: 'Send stipend sheet to coordinators', col: 'doing', due: ago(-1), tag: 'stipend', notes: 'Needs this month\'s paid ticks first.', sample: true },
      { id: uid(), title: 'Recruit mentors for Programming', col: 'todo', due: ago(-10), tag: 'recruit', notes: 'Check S/A grade and CGPA ≥ 6.5.', sample: true },
      { id: uid(), title: 'Update the FAQ for freshies', col: 'done', due: ago(3), tag: 'docs', notes: '', sample: true }
    ],
    pay: {},
    team: ['Jagadeep Reddy', 'Akshara', 'Adithy Ashok', 'Nilmani Kumar', 'Anshal Kasliwal', 'Varad']
  };
}

let S;
function load() {
  try { S = JSON.parse(store.get()); } catch { S = null; }
  if (!S || !S.people) { S = seed(); if (matchMedia('(prefers-color-scheme: dark)').matches) S.settings.theme = 'dark'; }
  S.settings ||= { stipend: 350, cadence: 14, theme: 'light' };
  S.pay ||= {};
}
const save = () => store.set(JSON.stringify(S));

/* ---------- selectors / derived data ---------- */
const person = id => S.people.find(p => p.id === id);
const pairOf = id => S.pairs.find(p => p.id === id);
const pairLabel = p => `${person(p.mentorId)?.name ?? '?'} → ${person(p.menteeId)?.name ?? '?'}`;

function eligibility(m) {
  return [
    ['S/A in the course', ['S', 'A'].includes(String(m.grade).toUpperCase())],
    ['CGPA ≥ 6.5', Number(m.cgpa) >= 6.5],
    ['No disciplinary record', !m.disc],
    ['No U/I grade', !m.ui]
  ];
}
function lastContact(p) {
  const ds = S.logs.filter(l => l.pairId === p.id && ['meetup', 'check-in'].includes(l.type)).map(l => l.date);
  ds.push(p.started);
  return ds.sort().pop();
}
function dueState(p) {
  if (p.status !== 'active') return { k: 'off', days: 0, label: p.status };
  const days = daysBetween(lastContact(p), today());
  const c = Number(S.settings.cadence);
  if (days <= c) return { k: 'ok', days, label: days === 0 ? 'met today' : `${days}d ago` };
  if (days <= c + 7) return { k: 'due', days, label: `${days}d · due` };
  return { k: 'late', days, label: `${days}d · overdue` };
}
const activePairs = () => S.pairs.filter(p => p.status === 'active');
const openConcerns = () => S.logs.filter(l => l.type === 'concern' && !l.resolved);
const openTasks = () => S.tasks.filter(t => t.col !== 'done');
const hasSample = () => [S.people, S.pairs, S.logs, S.tasks].some(a => a.some(x => x.sample));

function stipendRows(mk) {
  const end = new Date(+mk.slice(0, 4), +mk.slice(5, 7), 0);
  return S.pairs.filter(p => p.status !== 'paused' && parse(p.started) <= end);
}
const isPaid = (mk, id) => !!(S.pay[mk] && S.pay[mk][id]);

/* ---------- ui primitives ---------- */
let toastT;
function toast(msg) {
  const t = $('#toast'); t.textContent = msg; t.classList.add('show');
  clearTimeout(toastT); toastT = setTimeout(() => t.classList.remove('show'), 2400);
}

function confetti(n = 90) {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const c = $('#confetti'), x = c.getContext('2d');
  c.width = innerWidth; c.height = innerHeight;
  const cols = ['#918bd0', '#f28a3a', '#a6d6a0', '#f8c9d4', '#ebdbff', '#ffe08a'];
  const ps = Array.from({ length: n }, () => ({
    x: innerWidth / 2 + (Math.random() - .5) * 200, y: innerHeight * .7,
    vx: (Math.random() - .5) * 14, vy: -Math.random() * 16 - 6, r: Math.random() * 6 + 4,
    c: cols[Math.random() * cols.length | 0], a: Math.random() * 6, va: (Math.random() - .5) * .4, paw: Math.random() < .2
  }));
  let f = 0;
  (function tick() {
    x.clearRect(0, 0, c.width, c.height);
    ps.forEach(p => {
      p.vy += .45; p.x += p.vx; p.y += p.vy; p.a += p.va;
      x.save(); x.translate(p.x, p.y); x.rotate(p.a); x.fillStyle = p.c;
      if (p.paw) { x.font = '18px serif'; x.fillText('🐾', -9, 9); } else x.fillRect(-p.r / 2, -p.r / 2, p.r, p.r * 1.4);
      x.restore();
    });
    if (++f < 110) requestAnimationFrame(tick); else x.clearRect(0, 0, c.width, c.height);
  })();
}

function closeOverlay() { const o = $('#overlay'); o.hidden = true; o.innerHTML = ''; document.body.style.overflow = ''; }
function openOverlay(html) {
  const o = $('#overlay'); o.innerHTML = html; o.hidden = false; document.body.style.overflow = 'hidden';
  return o;
}

/* generic form dialog */
function form(title, fields, onSubmit, submitLabel = 'Save') {
  const f = x => {
    const v = x.value ?? '';
    if (x.type === 'select') return `<div class="field"><label for="f-${x.name}">${esc(x.label)}</label><select id="f-${x.name}" name="${x.name}">${x.options.map(o => { const [val, lab] = Array.isArray(o) ? o : [o, o]; return `<option value="${esc(val)}" ${String(val) === String(v) ? 'selected' : ''}>${esc(lab)}</option>`; }).join('')}</select></div>`;
    if (x.type === 'textarea') return `<div class="field"><label for="f-${x.name}">${esc(x.label)}</label><textarea id="f-${x.name}" name="${x.name}" placeholder="${esc(x.ph || '')}">${esc(v)}</textarea></div>`;
    if (x.type === 'checkbox') return `<div class="field check"><input type="checkbox" id="f-${x.name}" name="${x.name}" ${v ? 'checked' : ''}><label for="f-${x.name}">${esc(x.label)}</label></div>`;
    return `<div class="field"><label for="f-${x.name}">${esc(x.label)}</label><input id="f-${x.name}" name="${x.name}" type="${x.type || 'text'}" value="${esc(v)}" ${x.step ? `step="${x.step}"` : ''} ${x.required ? 'required' : ''} placeholder="${esc(x.ph || '')}"></div>`;
  };
  const o = openOverlay(`<form class="card modal tape"><h2>${esc(title)}</h2>${fields.map(f).join('')}<div class="row"><span class="sp"></span><button type="button" class="btn ghost" data-close>Cancel</button><button class="btn" type="submit">${esc(submitLabel)}</button></div></form>`);
  const fm = $('form', o);
  const first = $('input,select,textarea', fm); first && first.focus();
  fm.addEventListener('submit', e => {
    e.preventDefault();
    const out = {};
    fields.forEach(x => { const el = fm.elements[x.name]; out[x.name] = x.type === 'checkbox' ? el.checked : el.value.trim(); });
    onSubmit(out); closeOverlay();
  });
}

/* ---------- views ---------- */
const views = {};
const wrapHead = (title, sub, actions = '') => `<div class="head"><div><span class="hand">${sub[0]}</span><h1>${title}</h1><p>${sub[1]}</p></div><div class="actions">${actions}</div></div>`;

views.today = () => {
  const ap = activePairs(), states = ap.map(p => ({ p, d: dueState(p) }));
  const late = states.filter(s => s.d.k === 'late'), due = states.filter(s => s.d.k === 'due');
  const concerns = openConcerns(), tasks = openTasks();
  const mk = monthKey(new Date()), rows = stipendRows(mk), paid = rows.filter(p => isPaid(mk, p.id)).length;
  const mood = (late.length + concerns.length === 0) ? 'duo-desk' : (late.length + concerns.length <= 2 ? 'lila-wave' : 'lila-desk');
  const forecast = late.length ? ['⛈️', `Stormy: ${late.length} overdue check-in${late.length > 1 ? 's' : ''}`]
    : due.length ? ['⛅', `Cloudy: ${due.length} check-in${due.length > 1 ? 's' : ''} coming due`] : ['☀️', 'Clear skies: everyone is on track'];
  const h = new Date().getHours();
  const greet = h < 5 ? 'Still up' : h < 12 ? 'Good morning' : h < 17 ? 'Good afternoon' : h < 21 ? 'Good evening' : 'Late-night shift';
  const next = [
    ...late.map(s => `<li>🐾 <b>${esc(pairLabel(s.p))}</b> hasn't met in ${s.d.days} days <button class="btn small" data-action="logmeet" data-id="${s.p.id}">Log meetup</button></li>`),
    ...concerns.map(l => `<li>🧡 Open concern: <b>${esc(l.title)}</b> <a class="chip late" href="#/journal">see</a></li>`),
    ...tasks.filter(t => t.due && daysBetween(today(), t.due) <= 2).map(t => `<li>🧺 <b>${esc(t.title)}</b> <span class="chip ${daysBetween(today(), t.due) < 0 ? 'late' : 'due'}">${daysBetween(today(), t.due) < 0 ? 'overdue' : 'due ' + fmtDate(t.due)}</span></li>`)
  ];
  // heatmap: last 20 weeks, Sunday-aligned
  const counts = {}; S.logs.forEach(l => counts[l.date] = (counts[l.date] || 0) + 1);
  const end = new Date(); const start = new Date(end.getTime() - (19 * 7 + end.getDay()) * DAY);
  let cells = ''; let total = 0;
  for (let d = new Date(start); d <= end; d = new Date(d.getTime() + DAY)) {
    const k = iso(d), c = counts[k] || 0; total += c;
    cells += `<i data-l="${Math.min(c, 4)}" ${k === today() ? 'class="today"' : ''} title="${fmtDate(k)}: ${c} entr${c === 1 ? 'y' : 'ies'}"></i>`;
  }
  const recent = [...S.logs].sort((a, b) => b.date.localeCompare(a.date)).slice(0, 4);
  return `
  ${hasSample() ? `<div class="banner"><img src="${IMG('sparky-wave')}" width="46" alt=""><span><b>You're looking at sample data.</b> Poke around, then wipe it and add your real mentors and mentees.</span><span class="sp"></span><button class="btn small" data-action="clearsample">Clear sample data</button></div>` : ''}
  <div class="card hero tape lift">
    <img class="mascot" src="${IMG(mood)}" alt="">
    <div>
      <span class="hand">${greet}, Ajay</span>
      <h1>Here's how the AcadBuddy garden is growing 🌱</h1>
      <div class="forecast"><span>${forecast[0]}</span>${forecast[1]}</div>
      ${next.length ? `<ul class="next">${next.slice(0, 5).join('')}</ul>` : `<p class="muted">Nothing needs you right now. Maybe log a win? 🎉</p>`}
      <div class="actions" style="margin-top:12px">
        <button class="btn" data-action="logmeet">＋ Log a meetup</button>
        <button class="btn ghost" data-action="newentry">＋ Journal entry</button>
        <button class="btn ghost" data-action="theme">🌙 / ☀️ Theme</button>
      </div>
    </div>
  </div>
  <div class="grid g4" style="margin-top:22px">
    <div class="card stat lift"><span>Active buddy pairs</span><b>${ap.length}</b><span class="small">${S.people.filter(p => p.role === 'mentor').length} mentors · ${S.people.filter(p => p.role === 'mentee').length} mentees</span></div>
    <div class="card stat lift"><span>Check-ins due or late</span><b>${due.length + late.length}</b><span class="small">cadence: every ${S.settings.cadence} days</span></div>
    <div class="card stat lift"><span>Chores open</span><b>${tasks.length}</b><span class="small">${S.tasks.filter(t => t.col === 'doing').length} in progress</span></div>
    <div class="card stat lift"><span>${monthLabel(mk).split(' ')[0]} stipend paid</span><b>${paid}/${rows.length}</b><div class="bar" title="${paid} of ${rows.length}"><i style="width:${rows.length ? paid / rows.length * 100 : 0}%"></i></div></div>
  </div>
  <div class="grid g2" style="margin-top:22px">
    <div class="card"><h2>Paw-print calendar</h2><p class="muted small" style="margin:-6px 0 6px">${total} journal entr${total === 1 ? 'y' : 'ies'} in the last 20 weeks. The brighter the paw, the busier the day.</p>
      <div class="heat" role="img" aria-label="Activity heatmap">${cells}</div>
      <div class="legend">less <i style="background:var(--lav)"></i><i style="background:var(--lav2)"></i><i style="background:var(--peri)"></i><i style="background:var(--orange)"></i> more</div></div>
    <div class="card"><h2>Fresh from the journal</h2>
      ${recent.length ? recent.map(l => `<div class="row" style="margin-bottom:10px"><span class="chip">${esc(l.type)}</span><b>${esc(l.title)}</b><span class="sp"></span><span class="muted small">${fmtDate(l.date)}</span></div>`).join('') : '<div class="empty">no entries yet</div>'}
      <a class="btn small ghost" href="#/journal">Open journal →</a></div>
  </div>`;
};

views.pairs = () => {
  const mentors = S.people.filter(p => p.role === 'mentor'), mentees = S.people.filter(p => p.role === 'mentee');
  const pairCard = p => {
    const d = dueState(p), m = person(p.mentorId), e = person(p.menteeId);
    return `<div class="card pair lift">
      <div class="duo"><span class="av"><img src="${IMG('sparky-wave')}" alt=""></span><span class="arrow">→</span><span class="av"><img src="${IMG('lila-wave')}" alt=""></span>
        <span class="sp"></span><span class="chip ${d.k}">${esc(d.label)}</span></div>
      <div class="who"><b>${esc(m?.name)}</b> <span class="muted">mentors</span> <b>${esc(e?.name)}</b>${e?.year ? ` <span class="chip">${esc(e.year)} yr</span>` : ''}${p.sample ? ' <span class="chip sample">sample</span>' : ''}</div>
      <div class="muted small">${esc(p.course || '—')} · since ${fmtDate(p.started)} · last contact ${fmtDate(lastContact(p))}</div>
      <div class="row">
        ${p.status === 'active' ? `<button class="btn small" data-action="logmeet" data-id="${p.id}">Log meetup</button>` : ''}
        <button class="btn small ghost" data-action="pairstatus" data-id="${p.id}">${p.status === 'active' ? 'Pause' : 'Reactivate'}</button>
        <button class="btn small danger" data-action="delpair" data-id="${p.id}">Remove</button>
      </div></div>`;
  };
  const mentorRow = m => {
    const checks = eligibility(m), ok = checks.every(c => c[1]);
    const n = S.pairs.filter(p => p.mentorId === m.id && p.status === 'active').length;
    return `<tr><td><b>${esc(m.name)}</b>${m.sample ? ' <span class="chip sample">sample</span>' : ''}<div class="muted small">${esc(m.course || '')} · grade ${esc(m.grade || '?')} · CGPA ${esc(m.cgpa ?? '?')}</div></td>
      <td><div class="checks">${checks.map(c => `<span class="chip ${c[1] ? 'ok' : 'late'}">${c[1] ? '✓' : '✕'} ${c[0]}</span>`).join('')}</div></td>
      <td>${ok ? '<span class="chip ok">eligible</span>' : '<span class="chip late">check criteria</span>'}<div class="muted small">${n} active mentee${n === 1 ? '' : 's'}</div></td>
      <td><button class="btn small ghost" data-action="editperson" data-id="${m.id}">Edit</button> <button class="btn small danger" data-action="delperson" data-id="${m.id}">✕</button></td></tr>`;
  };
  return wrapHead('Buddies', ['pairs & people', 'Every mentor, every mentee, and who is looking after whom.'],
    `<button class="btn" data-action="newpair">＋ New pair</button><button class="btn ghost" data-action="newperson" data-role="mentor">＋ Mentor</button><button class="btn ghost" data-action="newperson" data-role="mentee">＋ Mentee</button>`) + `
  ${S.pairs.length ? `<div class="grid g3">${S.pairs.map(pairCard).join('')}</div>` : `<div class="card"><div class="empty">No pairs yet. Add a mentor and a mentee, then pair them up.</div></div>`}
  <div class="card" style="margin-top:24px"><h2>Mentors <span class="muted small">· eligibility is checked against the deck's criteria</span></h2>
    ${mentors.length ? `<div class="tablewrap"><table><thead><tr><th>Mentor</th><th>Criteria</th><th>Status</th><th></th></tr></thead><tbody>${mentors.map(mentorRow).join('')}</tbody></table></div>` : '<div class="empty">no mentors yet</div>'}</div>
  <div class="card" style="margin-top:24px"><h2>Mentees</h2>
    ${mentees.length ? `<div class="row">${mentees.map(e => `<span class="chip" style="font-size:.9rem;padding:4px 12px">${esc(e.name)}${e.year ? ' · ' + esc(e.year) : ''} <a href="#/pairs" data-action="editperson" data-id="${e.id}" title="Edit">✎</a> <a href="#/pairs" data-action="delperson" data-id="${e.id}" title="Remove">✕</a></span>`).join('')}</div>` : '<div class="empty">no mentees yet</div>'}
    <p class="muted small">Tip: use first names or initials only. This page is saved in your browser, but a wellness log should stay lean on personal details.</p></div>`;
};

let jFilter = 'all';
views.journal = () => {
  const types = ['all', 'meetup', 'check-in', 'concern', 'win', 'note'];
  const list = [...S.logs].filter(l => jFilter === 'all' || l.type === jFilter).sort((a, b) => b.date.localeCompare(a.date) || 0);
  let last = '', html = '';
  list.forEach(l => {
    const mk = l.date.slice(0, 7);
    if (mk !== last) { html += `<div class="month">${monthLabel(mk)}</div>`; last = mk; }
    const p = l.pairId && pairOf(l.pairId);
    html += `<div class="entry card concern-${!!l.resolved} ${l.type}">
      <div class="row"><span class="chip">${esc(l.type)}</span>${p ? `<span class="chip">${esc(pairLabel(p))}</span>` : ''}${l.type === 'concern' ? `<span class="chip ${l.resolved ? 'ok' : 'late'}">${l.resolved ? 'resolved' : 'open'}</span>` : ''}${l.sample ? '<span class="chip sample">sample</span>' : ''}
        <span class="sp"></span><span class="mood" title="mood ${l.mood}/5">${'●'.repeat(l.mood || 0)}${'○'.repeat(5 - (l.mood || 0))}</span><span class="muted small">${fmtDate(l.date)}</span></div>
      <h3 style="margin-top:8px">${esc(l.title)}</h3>${l.body ? `<p>${esc(l.body)}</p>` : ''}
      <div class="row" style="margin-top:10px">
        ${l.type === 'concern' ? `<button class="btn small green" data-action="resolve" data-id="${l.id}">${l.resolved ? 'Reopen' : 'Mark resolved'}</button>` : ''}
        <button class="btn small ghost" data-action="editentry" data-id="${l.id}">Edit</button><button class="btn small danger" data-action="delentry" data-id="${l.id}">Delete</button></div></div>`;
  });
  return wrapHead('Journal', ['what happened', 'Meetups, check-ins, worries and wins. Future-you says thanks.'],
    `<button class="btn" data-action="newentry">＋ New entry</button><button class="btn ghost" data-action="exportmd">⬇ Markdown</button>`) + `
  <div class="seg" style="margin-bottom:8px">${types.map(t => `<button class="${t === jFilter ? 'on' : ''}" data-action="jfilter" data-t="${t}">${t === 'all' ? 'everything' : t}</button>`).join('')}</div>
  <div class="timeline">${html || '<div class="card"><div class="empty">Nothing here yet 🍃</div></div>'}</div>`;
};

const COLS = [['todo', 'To do 🌰'], ['doing', 'Doing 🔥'], ['done', 'Done 🌸']];
views.board = () => `
  ${wrapHead('Chores', ['maintenance board', 'Recruiting, forms, sheets: everything that keeps the programme running. Drag cards between columns.'],
    `<button class="btn" data-action="newtask">＋ New chore</button>`)}
  <div class="board">${COLS.map(([k, label]) => {
    const ts = S.tasks.filter(t => t.col === k);
    return `<div class="col" data-col="${k}"><h3>${label} <span class="chip">${ts.length}</span></h3>${ts.length ? ts.map(t => {
      const dd = t.due ? daysBetween(today(), t.due) : null;
      return `<div class="task" draggable="true" data-id="${t.id}"><b>${esc(t.title)}</b>${t.notes ? `<p>${esc(t.notes)}</p>` : ''}
        <div class="row">${t.tag ? `<span class="chip">${esc(t.tag)}</span>` : ''}${t.due ? `<span class="chip ${k === 'done' ? 'ok' : dd < 0 ? 'late' : dd <= 2 ? 'due' : ''}">${k === 'done' ? 'done' : dd < 0 ? 'overdue' : fmtDate(t.due)}</span>` : ''}${t.sample ? '<span class="chip sample">sample</span>' : ''}<span class="sp"></span>
          ${k !== 'todo' ? `<button class="btn small ghost" data-action="movetask" data-id="${t.id}" data-d="-1" aria-label="Move left">◀</button>` : ''}${k !== 'done' ? `<button class="btn small ghost" data-action="movetask" data-id="${t.id}" data-d="1" aria-label="Move right">▶</button>` : ''}
          <button class="btn small ghost" data-action="edittask" data-id="${t.id}" aria-label="Edit">✎</button><button class="btn small danger" data-action="deltask" data-id="${t.id}" aria-label="Delete">✕</button></div></div>`;
    }).join('') : '<div class="empty">drop a card here</div>'}</div>`;
  }).join('')}</div>`;

let stipMonth = monthKey(new Date());
views.stipend = () => {
  const rows = stipendRows(stipMonth), per = Number(S.settings.stipend);
  const paid = rows.filter(p => isPaid(stipMonth, p.id));
  const byMentor = {};
  rows.forEach(p => { (byMentor[p.mentorId] ||= []).push(p); });
  return wrapHead('Stipend', ['the "yes we pay you" page', `${inr(per)} per mentee per month, tracked pair by pair.`],
    `<button class="btn ghost" data-action="setstipend">⚙ Rate &amp; cadence</button>`) + `
  <div class="card row" style="justify-content:space-between;margin-bottom:22px">
    <div class="months"><button class="btn small ghost" data-action="month" data-d="-1" aria-label="Previous month">◀</button><b>${monthLabel(stipMonth)}</b><button class="btn small ghost" data-action="month" data-d="1" aria-label="Next month">▶</button></div>
    <div><div class="money">${inr(paid.length * per)} <span class="muted small">of ${inr(rows.length * per)}</span></div>
    <div class="bar" style="min-width:200px"><i style="width:${rows.length ? paid.length / rows.length * 100 : 0}%"></i></div></div>
  </div>
  <div class="grid g2">
    <div class="card"><h2>Pair by pair</h2>${rows.length ? rows.map(p => {
      const ok = isPaid(stipMonth, p.id);
      return `<label class="paid-row ${ok ? 'done' : ''}"><input type="checkbox" data-action="pay" data-id="${p.id}" ${ok ? 'checked' : ''}><span><b>${esc(pairLabel(p))}</b><br><span class="small muted">${esc(p.course || '')}${p.status === 'ended' ? ' · ended' : ''}</span></span><span class="sp"></span><b>${inr(per)}</b></label>`;
    }).join('') : '<div class="empty">no pairs this month</div>'}</div>
    <div class="card"><h2>Per mentor</h2>${Object.keys(byMentor).length ? Object.entries(byMentor).map(([mid, ps]) => {
      const pd = ps.filter(p => isPaid(stipMonth, p.id)).length;
      return `<div class="paid-row"><span class="av"><img src="${IMG('sparky-wave')}" alt=""></span><span><b>${esc(person(mid)?.name)}</b><br><span class="small muted">${ps.length} mentee${ps.length > 1 ? 's' : ''} · ${pd} paid</span></span><span class="sp"></span><b>${inr(ps.length * per)}</b></div>`;
    }).join('') : '<div class="empty">nothing to pay yet</div>'}
      <p class="muted small">Total if every pair is paid: <b>${inr(rows.length * per)}</b>. Paused pairs are left out.</p></div>
  </div>`;
};

views.handbook = () => `
  ${wrapHead('Handbook', ['the why behind it', 'Straight from the Acad Buddy deck, so nobody has to dig for the PDF.'])}
  <div class="card tape" style="background:var(--lav)"><div class="row"><img src="${IMG('lila-lost')}" width="190" alt=""><div style="flex:1;min-width:240px">
    <h2>What is AcadBuddy?</h2><p>A peer academic support system where senior students help freshies navigate academics through guidance, doubt-clearing and shared experience. An AcadBuddy is <b>not a personal professor</b>: they're the senior you wish you had in your first semester.</p>
    <div class="row"><span class="chip">🧭 Guide</span><span class="chip">🤝 Support</span><span class="chip">🌱 Empower</span></div></div></div></div>
  <h2 style="margin:26px 0 12px">What makes a good AcadBuddy?</h2>
  <div class="six">
    ${[['🧠', 'Knows the subject'], ['💬', 'Explains clearly'], ['🤝', 'Approachable'], ['⏰', 'Reliable'], ['❤️', 'Patient']].map(([e, t]) => `<div class="card"><span class="em">${e}</span><b>${t}</b></div>`).join('')}
    <div class="card star"><span class="em">🃏</span><b>Knows when NOT to give the answer</b></div>
  </div>
  <div class="grid g2" style="margin-top:26px">
    <div class="card"><h2>Becoming a Sparky</h2><ul>
      <li>Compulsory S or A in the course they wish to teach</li><li>CGPA cut-off: 6.5</li><li>No record of disciplinary action</li><li>No U/I grade in any course (subject to the department)</li></ul>
      <p class="muted small">The Buddies page checks these automatically for every mentor.</p>
      <p><b>Stipend:</b> ${inr(S.settings.stipend)} per mentee per month. SMC mentors can become AMC mentors (lighter interview, but constant updates to the people responsible about work and meetups). Mentees can be 1st or 2nd years.</p></div>
    <div class="card"><h2>Why a wellness team?</h2><p>Because academic wellbeing is wellbeing.</p><ul>
      <li>🤝 <b>Peer support</b>: someone has been through this before</li><li>🧭 <b>Academic navigation</b>: how to approach IITM courses</li><li>🧠 <b>Confidence</b>: from "I can't do this" to "I know where I'm stuck"</li><li>🌱 <b>Early intervention</b>: before it gets overwhelming</li><li>🔗 <b>Connection</b>: reach the right support when it goes beyond academics</li></ul></div>
  </div>
  <div class="card" style="margin-top:22px"><h2>Coordinators <span class="muted small">· your second point of contact</span></h2>
    <div class="row"><img src="${IMG('sparky-arms')}" width="130" alt="">
    <div class="coord">${S.team.map(n => `<span>${esc(n)}</span>`).join('')}</div></div>
    <div class="actions" style="margin-top:10px"><button class="btn small ghost" data-action="editteam">Edit coordinators</button></div></div>
  <div class="card faq" style="margin-top:22px"><h2>Quick answers</h2>
    <details><summary>When should a concern be escalated?</summary><p class="muted">When the issue is more than academics (stress, missing sessions without reason, anything that worries you). Log it as a <b>concern</b> in the Journal and tell a coordinator. A buddy connects the student to the right support, they don't carry it alone.</p></details>
    <details><summary>How often should pairs meet?</summary><p class="muted">The desk assumes every ${S.settings.cadence} days (change it under Stipend → Rate &amp; cadence). A check-in turns <b>due</b> after that and <b>overdue</b> a week later.</p></details>
    <details><summary>Where is my data?</summary><p class="muted">Only in this browser. Use ⌘K → "Export backup" to save a JSON file, and "Import backup" to restore it somewhere else.</p></details></div>`;

/* ---------- render / routing ---------- */
function route() { return (location.hash.replace(/^#\//, '') || 'today').split('?')[0]; }
function render(keepScroll) {
  const r = views[route()] ? route() : 'today';
  const y = scrollY;
  const v = $('#view'); v.innerHTML = views[r](); v.classList.remove('view-in'); void v.offsetWidth; if (!keepScroll) v.classList.add('view-in');
  $$('#nav a').forEach(a => a.classList.toggle('on', a.dataset.route === r));
  document.title = `${r[0].toUpperCase() + r.slice(1)} · Saathi Log`;
  wireBoard();
  if (keepScroll) scrollTo(0, y);
}
function commit(msg, keepScroll = true) { save(); render(keepScroll); if (msg) toast(msg); }

function applyTheme() {
  document.documentElement.dataset.theme = S.settings.theme;
  $('#themeBtn').textContent = S.settings.theme === 'dark' ? '☀️ Daylight' : '🌙 Night study';
}

/* ---------- drag & drop for the board ---------- */
function wireBoard() {
  $$('.task').forEach(t => {
    t.addEventListener('dragstart', e => { e.dataTransfer.setData('text/plain', t.dataset.id); t.classList.add('drag'); });
    t.addEventListener('dragend', () => t.classList.remove('drag'));
  });
  $$('.col').forEach(c => {
    c.addEventListener('dragover', e => { e.preventDefault(); c.classList.add('over'); });
    c.addEventListener('dragleave', () => c.classList.remove('over'));
    c.addEventListener('drop', e => {
      e.preventDefault(); c.classList.remove('over');
      const t = S.tasks.find(x => x.id === e.dataTransfer.getData('text/plain'));
      if (t && t.col !== c.dataset.col) { const was = t.col; t.col = c.dataset.col; if (t.col === 'done' && was !== 'done') confetti(); commit(); }
    });
  });
}

/* ---------- actions ---------- */
const pairOptions = () => activePairs().map(p => [p.id, pairLabel(p)]);
const personForm = (role, p = {}) => {
  const fields = [{ name: 'name', label: 'Name (first name is plenty)', value: p.name, required: true }];
  if (role === 'mentor') fields.push(
    { name: 'course', label: 'Course they teach', value: p.course },
    { name: 'grade', label: 'Grade in that course', type: 'select', options: ['S', 'A', 'B', 'C', 'D', 'E'], value: p.grade || 'A' },
    { name: 'cgpa', label: 'CGPA', type: 'number', step: '0.01', value: p.cgpa ?? '' },
    { name: 'disc', label: 'Has a disciplinary record', type: 'checkbox', value: p.disc },
    { name: 'ui', label: 'Has a U or I grade in any course', type: 'checkbox', value: p.ui });
  else fields.push({ name: 'year', label: 'Year', type: 'select', options: ['1st', '2nd', '3rd'], value: p.year || '1st' });
  form(p.id ? `Edit ${role}` : `New ${role}`, fields, v => {
    if (p.id) Object.assign(p, v); else S.people.push({ id: uid(), role, ...v });
    commit(p.id ? 'Saved ✨' : `${role[0].toUpperCase() + role.slice(1)} added 🐾`);
  });
};
const entryForm = (l = {}, pre = {}) => form(l.id ? 'Edit entry' : 'New journal entry', [
  { name: 'type', label: 'Type', type: 'select', options: ['meetup', 'check-in', 'concern', 'win', 'note'], value: l.type || pre.type || 'note' },
  { name: 'pairId', label: 'Pair (optional)', type: 'select', options: [['', '— none —'], ...S.pairs.map(p => [p.id, pairLabel(p)])], value: l.pairId || pre.pairId || '' },
  { name: 'date', label: 'Date', type: 'date', value: l.date || today(), required: true },
  { name: 'title', label: 'Title', value: l.title || pre.title, required: true, ph: 'What happened?' },
  { name: 'body', label: 'Notes', type: 'textarea', value: l.body, ph: 'Keep personal details light.' },
  { name: 'mood', label: 'How did it feel? (1 rough – 5 great)', type: 'select', options: ['1', '2', '3', '4', '5'], value: String(l.mood || 3) }
], v => {
  v.mood = +v.mood; v.pairId = v.pairId || undefined;
  if (l.id) Object.assign(l, v); else S.logs.push({ id: uid(), ...v, resolved: v.type === 'concern' ? false : undefined });
  if (v.type === 'win') confetti(60);
  commit(l.id ? 'Saved ✨' : 'Logged 📒');
});
const taskForm = (t = {}, col = 'todo') => form(t.id ? 'Edit chore' : 'New chore', [
  { name: 'title', label: 'Chore', value: t.title, required: true },
  { name: 'notes', label: 'Notes', type: 'textarea', value: t.notes },
  { name: 'tag', label: 'Tag', value: t.tag, ph: 'recruit, stipend, docs…' },
  { name: 'due', label: 'Due', type: 'date', value: t.due || '' },
  { name: 'col', label: 'Column', type: 'select', options: COLS, value: t.col || col }
], v => { if (t.id) Object.assign(t, v); else S.tasks.push({ id: uid(), ...v }); commit('Saved ✨'); });

function logMeetup(pairId) {
  if (!S.pairs.length) return toast('Create a pair first 🐾');
  const p = pairId && pairOf(pairId);
  form('Log a meetup', [
    { name: 'pairId', label: 'Pair', type: 'select', options: S.pairs.map(q => [q.id, pairLabel(q)]), value: pairId || S.pairs[0].id },
    { name: 'date', label: 'Date', type: 'date', value: today(), required: true },
    { name: 'title', label: 'What did you cover?', required: true, value: p ? '' : '' },
    { name: 'body', label: 'Notes', type: 'textarea' },
    { name: 'mood', label: 'How did it feel? (1–5)', type: 'select', options: ['1', '2', '3', '4', '5'], value: '4' }
  ], v => { S.logs.push({ id: uid(), type: 'meetup', ...v, mood: +v.mood }); confetti(50); commit('Meetup logged, nice 🐾'); }, 'Log it');
}

function exportBackup() {
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([JSON.stringify(S, null, 2)], { type: 'application/json' }));
  a.download = `saathi-log-backup-${today()}.json`; a.click(); setTimeout(() => URL.revokeObjectURL(a.href), 1000);
  toast('Backup downloaded');
}
function importBackup() {
  const i = document.createElement('input'); i.type = 'file'; i.accept = 'application/json';
  i.onchange = async () => {
    try {
      const d = JSON.parse(await i.files[0].text());
      if (!d.people || !d.pairs || !d.logs) throw 0;
      S = d; S.settings ||= { stipend: 350, cadence: 14, theme: 'light' }; S.pay ||= {}; S.tasks ||= []; S.team ||= [];
      applyTheme(); commit('Backup restored 🌸', false);
    } catch { toast('That file does not look like a Saathi Log backup'); }
  };
  i.click();
}
function exportMarkdown() {
  const lines = ['# Saathi Log — AcadBuddy journal', '', `_Exported ${today()}_`, ''];
  [...S.logs].sort((a, b) => b.date.localeCompare(a.date)).forEach(l => {
    const p = l.pairId && pairOf(l.pairId);
    lines.push(`## ${l.date} · ${l.title}`, `*${l.type}${p ? ' · ' + pairLabel(p) : ''}${l.type === 'concern' ? (l.resolved ? ' · resolved' : ' · open') : ''}*`, '', l.body || '', '');
  });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([lines.join('\n')], { type: 'text/markdown' }));
  a.download = `saathi-journal-${today()}.md`; a.click(); setTimeout(() => URL.revokeObjectURL(a.href), 1000);
}

const A = {
  theme() { S.settings.theme = S.settings.theme === 'dark' ? 'light' : 'dark'; applyTheme(); save(); },
  palette: openPalette,
  clearsample() {
    if (!confirm('Remove all sample mentors, mentees, pairs, entries and chores? Anything you added yourself stays.')) return;
    ['people', 'pairs', 'logs', 'tasks'].forEach(k => S[k] = S[k].filter(x => !x.sample));
    const pid = new Set(S.pairs.map(p => p.id));
    Object.keys(S.pay).forEach(m => Object.keys(S.pay[m]).forEach(id => { if (!pid.has(id)) delete S.pay[m][id]; }));
    commit('Fresh desk ✨', false);
  },
  logmeet(el) { logMeetup(el && el.dataset.id); },
  newpair() {
    const mentors = S.people.filter(p => p.role === 'mentor'), mentees = S.people.filter(p => p.role === 'mentee');
    if (!mentors.length || !mentees.length) return toast('Add at least one mentor and one mentee first');
    form('New buddy pair', [
      { name: 'mentorId', label: 'Mentor', type: 'select', options: mentors.map(m => [m.id, m.name + (eligibility(m).every(c => c[1]) ? '' : ' (check criteria)')]) },
      { name: 'menteeId', label: 'Mentee', type: 'select', options: mentees.map(m => [m.id, m.name]) },
      { name: 'course', label: 'Course', value: mentors[0].course },
      { name: 'started', label: 'Started', type: 'date', value: today() }
    ], v => { S.pairs.push({ id: uid(), status: 'active', ...v }); confetti(70); commit('Pair created 🐾'); }, 'Pair them');
  },
  newperson(el) { personForm(el.dataset.role); },
  editperson(el, e) { e.preventDefault(); personForm(person(el.dataset.id).role, person(el.dataset.id)); },
  delperson(el, e) {
    e.preventDefault(); const p = person(el.dataset.id);
    if (!confirm(`Remove ${p.name}? Their pairs go too (journal entries stay).`)) return;
    S.pairs = S.pairs.filter(q => q.mentorId !== p.id && q.menteeId !== p.id);
    S.people = S.people.filter(q => q.id !== p.id); commit('Removed');
  },
  pairstatus(el) { const p = pairOf(el.dataset.id); p.status = p.status === 'active' ? 'paused' : 'active'; commit(p.status === 'active' ? 'Back on 🐾' : 'Paused'); },
  delpair(el) { if (confirm('Remove this pair? Journal entries stay.')) { S.pairs = S.pairs.filter(p => p.id !== el.dataset.id); commit('Removed'); } },
  newentry() { entryForm(); },
  editentry(el) { entryForm(S.logs.find(l => l.id === el.dataset.id)); },
  delentry(el) { if (confirm('Delete this entry?')) { S.logs = S.logs.filter(l => l.id !== el.dataset.id); commit('Deleted'); } },
  resolve(el) { const l = S.logs.find(x => x.id === el.dataset.id); l.resolved = !l.resolved; if (l.resolved) confetti(40); commit(l.resolved ? 'Resolved 💚' : 'Reopened'); },
  jfilter(el) { jFilter = el.dataset.t; render(true); },
  exportmd: exportMarkdown,
  newtask() { taskForm(); },
  edittask(el) { taskForm(S.tasks.find(t => t.id === el.dataset.id)); },
  deltask(el) { S.tasks = S.tasks.filter(t => t.id !== el.dataset.id); commit('Removed'); },
  movetask(el) {
    const t = S.tasks.find(x => x.id === el.dataset.id), order = COLS.map(c => c[0]);
    const was = t.col; t.col = order[Math.max(0, Math.min(2, order.indexOf(t.col) + +el.dataset.d))];
    if (t.col === 'done' && was !== 'done') confetti(); commit();
  },
  month(el) { const [y, m] = stipMonth.split('-').map(Number); stipMonth = monthKey(new Date(y, m - 1 + +el.dataset.d, 1)); render(true); },
  pay(el) {
    (S.pay[stipMonth] ||= {})[el.dataset.id] = el.checked;
    if (el.checked && stipendRows(stipMonth).every(p => isPaid(stipMonth, p.id))) confetti(120);
    commit();
  },
  setstipend() {
    form('Rate & cadence', [
      { name: 'stipend', label: 'Stipend per mentee per month (₹)', type: 'number', value: S.settings.stipend },
      { name: 'cadence', label: 'Expected days between meetups', type: 'number', value: S.settings.cadence }
    ], v => { S.settings.stipend = +v.stipend || 350; S.settings.cadence = +v.cadence || 14; commit('Updated'); });
  },
  editteam() {
    form('Coordinators', [{ name: 'team', label: 'One name per line', type: 'textarea', value: S.team.join('\n') }],
      v => { S.team = v.team.split('\n').map(s => s.trim()).filter(Boolean); commit('Saved ✨'); });
  },
  export: exportBackup, import: importBackup
};

/* ---------- command palette ---------- */
function openPalette() {
  const cmds = [
    ['Go to Today', 'g t', () => location.hash = '#/today'], ['Go to Buddies', 'g b', () => location.hash = '#/pairs'],
    ['Go to Journal', 'g j', () => location.hash = '#/journal'], ['Go to Chores', 'g c', () => location.hash = '#/board'],
    ['Go to Stipend', 'g s', () => location.hash = '#/stipend'], ['Go to Handbook', 'g h', () => location.hash = '#/handbook'],
    ['Log a meetup', '+', () => logMeetup()], ['New journal entry', '+', () => entryForm()], ['New chore', '+', () => taskForm()],
    ['New buddy pair', '+', () => A.newpair()], ['Add mentor', '+', () => personForm('mentor')], ['Add mentee', '+', () => personForm('mentee')],
    ['Toggle night study', '☾', () => A.theme()], ['Export backup (JSON)', '⬇', exportBackup], ['Import backup', '⬆', importBackup],
    ['Export journal as Markdown', '⬇', exportMarkdown], ['Celebrate 🎉', '✨', () => confetti(140)]
  ];
  const o = openOverlay(`<div class="card pal tape"><input id="pq" placeholder="Type a command…" autocomplete="off" aria-label="Command"><ul id="pl"></ul></div>`);
  let sel = 0, shown = cmds;
  const paint = () => { $('#pl').innerHTML = shown.map((c, i) => `<li class="${i === sel ? 'on' : ''}" data-i="${i}"><span>${esc(c[0])}</span><kbd>${esc(c[1])}</kbd></li>`).join('') || '<li class="muted">No match</li>'; };
  const run = i => { const c = shown[i]; if (!c) return; closeOverlay(); setTimeout(c[2], 30); };
  $('#pq').addEventListener('input', e => { const q = e.target.value.toLowerCase(); shown = cmds.filter(c => c[0].toLowerCase().includes(q)); sel = 0; paint(); });
  $('#pq').addEventListener('keydown', e => {
    if (e.key === 'ArrowDown') { sel = Math.min(sel + 1, shown.length - 1); paint(); e.preventDefault(); }
    else if (e.key === 'ArrowUp') { sel = Math.max(sel - 1, 0); paint(); e.preventDefault(); }
    else if (e.key === 'Enter') run(sel);
  });
  $('#pl').addEventListener('click', e => { const li = e.target.closest('li[data-i]'); if (li) run(+li.dataset.i); });
  paint(); $('#pq').focus();
}

/* ---------- events ---------- */
document.addEventListener('click', e => {
  if (e.target.closest('[data-close]') || e.target.id === 'overlay') return closeOverlay();
  const el = e.target.closest('[data-action]');
  if (el && el.dataset.action !== 'pay' && A[el.dataset.action]) A[el.dataset.action](el, e);
});
document.addEventListener('change', e => {
  const el = e.target.closest('[data-action="pay"]'); if (el) A.pay(el);
});
document.addEventListener('keydown', e => {
  if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); $('#overlay').hidden ? openPalette() : closeOverlay(); }
  else if (e.key === 'Escape' && !$('#overlay').hidden) closeOverlay();
});
window.addEventListener('hashchange', () => { closeOverlay(); render(); scrollTo(0, 0); });

load(); applyTheme(); render();
})();
