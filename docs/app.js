// State
let manifest = null;
let currentSig = null;
let currentDate = null;
let currentView = 'transcript'; // 'transcript' | 'summary'
const transcriptCache = new Map();
const summaryCache = new Map();

// DOM refs
const sigSelect = document.getElementById('sig-select');
const dateList = document.getElementById('date-list');
const transcriptPanel = document.getElementById('transcript-panel');
const searchInput = document.getElementById('search-input');
const searchGroup = searchInput ? searchInput.closest('.search-group') : null;
const dateNav = document.querySelector('.date-nav');

// ── Initialization ──────────────────────────────────────────

async function init() {
  const res = await fetch('manifest.json');
  if (!res.ok) {
    showError('Failed to load manifest.');
    return;
  }
  manifest = await res.json();
  populateSigSelect();
  restoreFromURL();
}

function populateSigSelect() {
  for (const sig of manifest.sigs) {
    const opt = document.createElement('option');
    opt.value = sig.slug;
    opt.textContent = sigDisplayName(sig.name);
    sigSelect.appendChild(opt);
  }
}

// ── Helpers ─────────────────────────────────────────────────

function sigDisplayName(name) {
  return name
    .replace(/\s*\(SIG[^)]*\)/g, '')    // "ja-JA Localization (SIG Communications)"
    .replace(/\bSIG:?\s+Meeting\b/g, '') // "Developer Experience SIG Meeting"
    .replace(/\s*\bSIG\b:?/g, '')        // "Entities SIG", "SIG Injector", "End-User SIG: OTel"
    .replace(/\s*\bWG\b/g, '')           // "Agent Management WG"
    .replace(/\s+:/g, ':')              // "End-User : OTel" → "End-User: OTel"
    .replace(/\s+/g, ' ')
    .trim();
}

function getSigMeetings(slug) {
  const sig = manifest.sigs.find(s => s.slug === slug);
  return sig ? sig.meetings : [];
}

function getSigName(slug) {
  const sig = manifest.sigs.find(s => s.slug === slug);
  return sig ? sig.name : slug;
}

function meetingHasSummary(slug, date) {
  const meetings = getSigMeetings(slug);
  const m = meetings.find(m => m.date === date);
  return m ? m.has_summary : false;
}

// ── SIG selection ───────────────────────────────────────────

async function onSIGChange(slug) {
  currentSig = slug;
  currentDate = null;
  currentView = 'transcript';
  searchInput.value = '';

  if (slug) {
    if (searchGroup) searchGroup.hidden = false;
    if (dateNav) dateNav.hidden = false;
    renderDateList(getSigMeetings(slug), null);
    clearTranscript();
    updateURL(slug, null);
    prefetchTranscripts(slug);
  } else {
    if (searchGroup) searchGroup.hidden = true;
    if (dateNav) dateNav.hidden = true;
    dateList.innerHTML = '';
    showEmptyState();
    updateURL(null, null);
  }
}

// ── Date list ───────────────────────────────────────────────

function renderDateList(meetings, activeDate, matchCounts) {
  dateList.innerHTML = '';
  for (const m of meetings) {
    const li = document.createElement('li');
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'date-btn';
    btn.dataset.date = m.date;

    let label = m.date;
    if (m.duration_minutes) {
      label += ' \u00b7 ' + m.duration_minutes + ' min';
    }
    btn.appendChild(document.createTextNode(label));

    if (matchCounts && matchCounts[m.date] != null) {
      const badge = document.createElement('span');
      badge.className = 'match-badge';
      badge.textContent = matchCounts[m.date];
      btn.appendChild(badge);
    }

    btn.setAttribute('aria-pressed', m.date === activeDate ? 'true' : 'false');
    btn.addEventListener('click', () => onDateClick(m.date));
    li.appendChild(btn);
    dateList.appendChild(li);
  }
}

// ── Date click ──────────────────────────────────────────────

async function onDateClick(date) {
  currentDate = date;
  currentView = 'transcript';
  updateURL(currentSig, date);
  renderDateList(getSigMeetings(currentSig), date);
  transcriptPanel.innerHTML = '<div class="loading-state"><div class="loading-spinner"></div><p>Loading\u2026</p></div>';

  try {
    const text = await getTranscript(currentSig, date);
    renderTranscript(text, getCurrentQuery());
    if (meetingHasSummary(currentSig, date)) {
      await switchToView('summary');
    }
  } catch (err) {
    showError('Failed to load transcript: ' + err.message);
  }
}

// ── Transcript fetching ─────────────────────────────────────

async function getTranscript(slug, date) {
  const key = slug + '/' + date;
  if (!transcriptCache.has(key)) {
    const res = await fetch('transcripts/' + slug + '/' + date + '.txt');
    if (!res.ok) throw new Error('HTTP ' + res.status);
    transcriptCache.set(key, await res.text());
  }
  return transcriptCache.get(key);
}

async function prefetchTranscripts(slug) {
  const meetings = getSigMeetings(slug);
  await Promise.all(
    meetings.map(m => getTranscript(slug, m.date).catch(() => {}))
  );
}

// ── Transcript rendering ────────────────────────────────────

function renderTranscript(text, query) {
  const separatorIndex = text.indexOf('\n====');
  if (separatorIndex === -1) {
    transcriptPanel.textContent = text;
    return;
  }

  const headerText = text.substring(0, separatorIndex);
  const bodyText = text.substring(text.indexOf('\n', separatorIndex + 1) + 1).trim();

  transcriptPanel.innerHTML = '';

  // Render header as card with <dl>
  const headerCard = document.createElement('div');
  headerCard.className = 'transcript-header';
  const dl = document.createElement('dl');
  for (const line of headerText.split('\n')) {
    const colonIdx = line.indexOf(':');
    if (colonIdx === -1) continue;
    const key = line.substring(0, colonIdx).trim();
    const val = line.substring(colonIdx + 1).trim();
    const dt = document.createElement('dt');
    dt.textContent = key;
    const dd = document.createElement('dd');
    if (key === 'Source URL') {
      const a = document.createElement('a');
      a.href = val;
      a.textContent = val;
      a.target = '_blank';
      a.rel = 'noopener noreferrer';
      dd.appendChild(a);
    } else {
      dd.textContent = val;
    }
    dl.appendChild(dt);
    dl.appendChild(dd);
  }
  headerCard.appendChild(dl);

  if (currentSig && currentDate && meetingHasSummary(currentSig, currentDate)) {
    const tabBar = document.createElement('div');
    tabBar.className = 'tab-bar';
    tabBar.setAttribute('role', 'tablist');
    for (const [view, label] of [['summary', 'Summary'], ['transcript', 'Transcript']]) {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'tab-btn';
      btn.dataset.view = view;
      btn.setAttribute('role', 'tab');
      btn.setAttribute('aria-selected', 'false');
      btn.textContent = label;
      btn.addEventListener('click', () => switchToView(view));
      tabBar.appendChild(btn);
    }
    headerCard.appendChild(tabBar);
  }

  transcriptPanel.appendChild(headerCard);

  transcriptPanel.appendChild(buildTranscriptBody(bodyText, query));
}

function buildTranscriptBody(bodyText, query) {
  const bodyEl = document.createElement('div');
  bodyEl.className = 'transcript-body';
  for (const line of bodyText.split('\n')) {
    if (!line.trim()) continue;
    const p = document.createElement('p');
    p.className = 'transcript-line';
    const parsed = parseBodyLine(line);
    if (parsed.speaker) {
      const speaker = document.createElement('span');
      speaker.className = 'speaker-name';
      speaker.textContent = parsed.speaker;
      const time = document.createElement('time');
      time.textContent = ' ' + parsed.timestamp + ' ';
      time.className = 'timestamp';
      p.appendChild(speaker);
      p.appendChild(time);
      p.appendChild(document.createTextNode(parsed.utterance));
    } else {
      p.textContent = line;
    }
    bodyEl.appendChild(p);
  }
  if (query) highlightMatches(bodyEl, query);
  return bodyEl;
}

function parseBodyLine(line) {
  const match = line.match(/^(.+?)\s+(\d+:\d+)\s+(.*)$/);
  if (!match) return { speaker: null, timestamp: null, utterance: line };
  return { speaker: match[1], timestamp: match[2], utterance: match[3] };
}

// ── Display helpers ─────────────────────────────────────────

function clearTranscript() {
  transcriptPanel.innerHTML =
    '<div class="empty-state"><p>Select a meeting date to view its transcript.</p></div>';
}

function showEmptyState() {
  transcriptPanel.innerHTML =
    '<div class="empty-state"><p>Select a SIG to browse its meeting transcripts.</p></div>';
}

function showError(msg) {
  const div = document.createElement('div');
  div.className = 'error-state';
  const p = document.createElement('p');
  p.textContent = msg;
  div.appendChild(p);
  transcriptPanel.replaceChildren(div);
}

// ── Summary toggle (Issue #7) ───────────────────────────────

async function getSummary(slug, date) {
  const key = slug + '/' + date;
  if (!summaryCache.has(key)) {
    const res = await fetch('summaries/' + slug + '/' + date + '.md');
    if (!res.ok) throw new Error('HTTP ' + res.status);
    summaryCache.set(key, await res.text());
  }
  return summaryCache.get(key);
}

async function switchToView(view) {
  if (!currentSig || !currentDate) return;
  currentView = view;

  for (const btn of transcriptPanel.querySelectorAll('.tab-btn')) {
    btn.setAttribute('aria-selected', btn.dataset.view === view ? 'true' : 'false');
  }

  const bodyEl = transcriptPanel.querySelector('.transcript-body, .summary-body');
  if (!bodyEl) return;

  if (view === 'summary') {
    try {
      const md = await getSummary(currentSig, currentDate);
      const summaryEl = document.createElement('div');
      summaryEl.className = 'summary-body';
      summaryEl.appendChild(renderMarkdown(md));
      bodyEl.replaceWith(summaryEl);
    } catch (err) {
      showError('Failed to load summary: ' + err.message);
    }
  } else {
    try {
      const text = await getTranscript(currentSig, currentDate);
      const sepIdx = text.indexOf('\n====');
      const bodyText = sepIdx === -1 ? '' :
        text.substring(text.indexOf('\n', sepIdx + 1) + 1).trim();
      bodyEl.replaceWith(buildTranscriptBody(bodyText, getCurrentQuery()));
    } catch (err) {
      showError('Failed to load transcript: ' + err.message);
    }
  }
}

function renderMarkdown(md) {
  const container = document.createDocumentFragment();
  const lines = md.split('\n');
  let currentList = null;

  for (const line of lines) {
    // Headings
    if (line.startsWith('## ')) {
      if (currentList) { container.appendChild(currentList); currentList = null; }
      const h2 = document.createElement('h2');
      h2.appendChild(renderInline(line.substring(3)));
      container.appendChild(h2);
    } else if (line.startsWith('# ')) {
      if (currentList) { container.appendChild(currentList); currentList = null; }
      const h1 = document.createElement('h1');
      h1.appendChild(renderInline(line.substring(2)));
      container.appendChild(h1);
    } else if (line.startsWith('- ')) {
      // List item
      if (!currentList) currentList = document.createElement('ul');
      const li = document.createElement('li');
      li.appendChild(renderInline(line.substring(2)));
      currentList.appendChild(li);
    } else if (line.trim() === '') {
      if (currentList) { container.appendChild(currentList); currentList = null; }
    } else {
      if (currentList) { container.appendChild(currentList); currentList = null; }
      const p = document.createElement('p');
      p.appendChild(renderInline(line));
      container.appendChild(p);
    }
  }
  if (currentList) container.appendChild(currentList);
  return container;
}

function renderInline(text) {
  const frag = document.createDocumentFragment();
  const parts = text.split(/(\*\*[^*]+\*\*)/g);
  for (const part of parts) {
    if (part.startsWith('**') && part.endsWith('**')) {
      const strong = document.createElement('strong');
      strong.textContent = part.slice(2, -2);
      frag.appendChild(strong);
    } else {
      frag.appendChild(document.createTextNode(part));
    }
  }
  return frag;
}

// ── Search (Issue #5) ───────────────────────────────────────

function debounce(fn, ms) {
  let t;
  return function () {
    const args = arguments;
    clearTimeout(t);
    t = setTimeout(() => fn.apply(this, args), ms);
  };
}

async function handleSearch(query) {
  if (!currentSig) return;

  if (!query.trim()) {
    renderDateList(getSigMeetings(currentSig), currentDate);
    if (currentDate) {
      try {
        const text = await getTranscript(currentSig, currentDate);
        renderTranscript(text, '');
        if (meetingHasSummary(currentSig, currentDate)) {
          await switchToView('summary');
        }
      } catch (_) {}
    }
    return;
  }

  const meetings = getSigMeetings(currentSig);
  const matchCounts = {};
  for (const m of meetings) {
    const text = transcriptCache.get(currentSig + '/' + m.date);
    if (text) {
      matchCounts[m.date] = countMatches(text, query);
    }
  }

  const filtered = meetings.filter(m => {
    const count = matchCounts[m.date];
    return count != null && count > 0;
  });

  renderDateList(filtered, currentDate, matchCounts);

  if (currentDate && transcriptCache.has(currentSig + '/' + currentDate)) {
    renderTranscript(transcriptCache.get(currentSig + '/' + currentDate), query);
    currentView = 'transcript';
    for (const btn of transcriptPanel.querySelectorAll('.tab-btn')) {
      btn.setAttribute('aria-selected', btn.dataset.view === 'transcript' ? 'true' : 'false');
    }
  }
}

function countMatches(text, query) {
  if (!query) return 0;
  const lower = text.toLowerCase();
  const q = query.toLowerCase();
  let count = 0;
  let idx = 0;
  while (true) {
    idx = lower.indexOf(q, idx);
    if (idx === -1) break;
    count++;
    idx += q.length;
  }
  return count;
}

function highlightMatches(container, query) {
  if (!query) return;
  const walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT);
  const nodes = [];
  while (walker.nextNode()) nodes.push(walker.currentNode);

  const lowerQuery = query.toLowerCase();
  const qLen = query.length;

  for (const node of nodes) {
    const text = node.textContent;
    const lower = text.toLowerCase();
    if (lower.indexOf(lowerQuery) === -1) continue;

    const frag = document.createDocumentFragment();
    let lastIdx = 0;
    let idx = lower.indexOf(lowerQuery);
    while (idx !== -1) {
      if (idx > lastIdx) {
        frag.appendChild(document.createTextNode(text.substring(lastIdx, idx)));
      }
      const mark = document.createElement('mark');
      mark.textContent = text.substring(idx, idx + qLen);
      frag.appendChild(mark);
      lastIdx = idx + qLen;
      idx = lower.indexOf(lowerQuery, lastIdx);
    }
    if (lastIdx < text.length) {
      frag.appendChild(document.createTextNode(text.substring(lastIdx)));
    }
    node.parentNode.replaceChild(frag, node);
  }
}

// ── URL deep-linking ────────────────────────────────────────

function updateURL(sig, date) {
  const p = new URLSearchParams();
  if (sig) p.set('sig', sig);
  if (date) p.set('date', date);
  const qs = p.toString();
  history.replaceState(null, '', qs ? '?' + qs : location.pathname);
}

function restoreFromURL() {
  const p = new URLSearchParams(location.search);
  const sig = p.get('sig');
  const date = p.get('date');
  if (sig) {
    sigSelect.value = sig;
    onSIGChange(sig).then(() => {
      if (date) onDateClick(date);
    });
  }
}

function getCurrentQuery() {
  return searchInput.value.trim();
}

// ── Event wiring ────────────────────────────────────────────

sigSelect.addEventListener('change', e => onSIGChange(e.target.value));
searchInput.addEventListener('input', debounce(e => handleSearch(e.target.value), 300));

document.addEventListener('DOMContentLoaded', init);
