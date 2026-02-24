// State
let manifest = null;
let currentSig = null;
let currentDate = null;
let currentView = 'summary'; // 'transcript' | 'summary' | 'meeting-notes'
const transcriptCache = new Map();
const meetingNotesCache = new Map();
const summaryCache = new Map();

// DOM refs
const sigSelect = document.getElementById('sig-select');
const dateList = document.getElementById('date-list');
const transcriptPanel = document.getElementById('transcript-panel');
const searchInput = document.getElementById('search-input');
const searchGroup = searchInput ? searchInput.closest('.search-group') : null;
const dateNavWrapper = document.querySelector('.date-nav-wrapper');
const searchNav = document.querySelector('.search-nav');
const matchCounter = document.querySelector('.match-counter');
const prevMatchBtn = document.getElementById('prev-match-btn');
const nextMatchBtn = document.getElementById('next-match-btn');

// Match navigation state
let currentMatchIndex = -1;
let totalMatches = 0;

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
  currentView = 'summary';
  searchInput.value = '';
  resetMatchNav();

  if (slug) {
    if (searchGroup) searchGroup.hidden = false;
    if (dateNavWrapper) dateNavWrapper.hidden = false;
    if (searchNav) searchNav.hidden = true;
    renderDateList(getSigMeetings(slug), null);
    clearTranscript();
    updateURL(slug, null);
    prefetchTranscripts(slug);
  } else {
    if (searchGroup) searchGroup.hidden = true;
    if (dateNavWrapper) dateNavWrapper.hidden = true;
    if (searchNav) searchNav.hidden = true;
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
    } else if (matchCounts && matchCounts[m.date] == null) {
      // Uncached transcript — show loading spinner (Issue #34)
      btn.classList.add('date-btn-loading');
      const spinner = document.createElement('span');
      spinner.className = 'btn-spinner';
      spinner.setAttribute('aria-label', 'Loading');
      btn.appendChild(spinner);
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
  updateURL(currentSig, date);
  renderDateList(getSigMeetings(currentSig), date);
  transcriptPanel.innerHTML = '<div class="loading-state"><div class="loading-spinner"></div><p>Loading\u2026</p></div>';

  // Snapshot for staleness guard (Issue #33)
  const requestedSig = currentSig;
  const requestedDate = date;

  try {
    const [text] = await Promise.all([
      getTranscript(currentSig, date),
      getMeetingNotes(currentSig, date).catch(() => ''),
    ]);

    // Staleness guard: discard if user navigated away during fetch
    if (currentSig !== requestedSig || currentDate !== requestedDate) return;

    renderTranscript(text, getCurrentQuery());
    if (getCurrentQuery()) {
      await switchToView('transcript');
      updateMatchNav();
    } else {
      await switchToView('summary');
    }
  } catch (err) {
    if (currentSig !== requestedSig || currentDate !== requestedDate) return;
    showError('Failed to load transcript: ' + err.message);
  }
}

// ── Transcript fetching ─────────────────────────────────────

async function getTranscript(slug, date) {
  const key = slug + '/' + date;
  if (!transcriptCache.has(key)) {
    const res = await fetch('content/' + slug + '/' + date + '/transcript.md');
    if (!res.ok) throw new Error('HTTP ' + res.status);
    transcriptCache.set(key, await res.text());
  }
  return transcriptCache.get(key);
}

async function getMeetingNotes(slug, date) {
  const key = slug + '/' + date;
  if (!meetingNotesCache.has(key)) {
    const res = await fetch('content/' + slug + '/' + date + '/meeting-notes.md');
    meetingNotesCache.set(key, res.ok ? await res.text() : '');
  }
  return meetingNotesCache.get(key);
}

async function prefetchTranscripts(slug) {
  const meetings = getSigMeetings(slug);
  await Promise.all(
    meetings.map(m => Promise.all([
      getTranscript(slug, m.date).catch(() => {}),
      getMeetingNotes(slug, m.date).catch(() => {}),
    ]))
  );
  // Re-run active search now that cache is warm (Issue #34)
  const query = getCurrentQuery();
  if (query && currentSig === slug) {
    handleSearch(query);
  }
}

// ── Transcript rendering ────────────────────────────────────

function getSigData(slug) {
  return manifest ? manifest.sigs.find(s => s.slug === slug) || null : null;
}

function renderTranscript(text, query) {
  const separatorIndex = text.indexOf('\n====');
  if (separatorIndex === -1) {
    transcriptPanel.textContent = text;
    return;
  }

  const headerText = text.substring(0, separatorIndex);

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
    if (key === 'Source URL' || key === 'Zoom Recording URL') {
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

  // Append SIG-level links from manifest (Meeting Notes, Repository)
  const sig = getSigData(currentSig);
  if (sig) {
    for (const [label, url] of [['Meeting Notes', sig.meeting_notes_url], ['Repository', sig.repository_url]]) {
      if (!url) continue;
      const dt = document.createElement('dt');
      dt.textContent = label;
      const dd = document.createElement('dd');
      const a = document.createElement('a');
      a.href = url;
      a.textContent = url;
      a.target = '_blank';
      a.rel = 'noopener noreferrer';
      dd.appendChild(a);
      dl.appendChild(dt);
      dl.appendChild(dd);
    }
  }

  headerCard.appendChild(dl);

  // Always render 3-tab bar
  const tabBar = document.createElement('div');
  tabBar.className = 'tab-bar';
  tabBar.setAttribute('role', 'tablist');
  for (const [view, label] of [['summary', 'Summary'], ['meeting-notes', 'Meeting Notes'], ['transcript', 'Transcript']]) {
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

  transcriptPanel.appendChild(headerCard);

  // Append a summary-body placeholder; caller will call switchToView to fill it
  const placeholder = document.createElement('div');
  placeholder.className = 'summary-body';
  transcriptPanel.appendChild(placeholder);
}

function buildTranscriptBody(bodyText, query) {
  const bodyEl = document.createElement('div');
  bodyEl.className = 'transcript-body';

  // Strip the '## Zoom Recording Transcript' heading if present
  const TRANSCRIPT_SECTION = '## Zoom Recording Transcript';
  let transcriptText = bodyText;
  if (bodyText.startsWith(TRANSCRIPT_SECTION)) {
    transcriptText = bodyText.substring(TRANSCRIPT_SECTION.length).trim();
  } else {
    const nlMarkerIdx = bodyText.indexOf('\n' + TRANSCRIPT_SECTION);
    if (nlMarkerIdx !== -1) {
      transcriptText = bodyText.substring(nlMarkerIdx + 1 + TRANSCRIPT_SECTION.length).trim();
    }
  }

  // Render transcript lines
  for (const line of transcriptText.split('\n')) {
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
  // New format: **Speaker** MM:SS utterance
  const boldMatch = line.match(/^\*\*(.+?)\*\*\s+(\d+:\d+)\s+(.*)$/);
  if (boldMatch) return { speaker: boldMatch[1], timestamp: boldMatch[2], utterance: boldMatch[3] };
  // Legacy format: Speaker MM:SS utterance
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
    const res = await fetch('content/' + slug + '/' + date + '/summary.md');
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

  const bodyEl = transcriptPanel.querySelector('.transcript-body, .summary-body, .notes-body');
  if (!bodyEl) return;

  if (view === 'summary') {
    if (!meetingHasSummary(currentSig, currentDate)) {
      const summaryEl = document.createElement('div');
      summaryEl.className = 'summary-body';
      const p = document.createElement('p');
      p.textContent = 'No summary available.';
      summaryEl.appendChild(p);
      bodyEl.replaceWith(summaryEl);
    } else {
      try {
        const md = await getSummary(currentSig, currentDate);
        const summaryEl = document.createElement('div');
        summaryEl.className = 'summary-body';
        summaryEl.appendChild(renderMarkdown(md));
        bodyEl.replaceWith(summaryEl);
      } catch (err) {
        showError('Failed to load summary: ' + err.message);
      }
    }
  } else if (view === 'meeting-notes') {
    try {
      const notesText = await getMeetingNotes(currentSig, currentDate);
      const notesEl = document.createElement('div');
      notesEl.className = 'notes-body';
      if (notesText) {
        notesEl.appendChild(renderMarkdown(notesText));
      } else {
        const p = document.createElement('p');
        p.textContent = 'No meeting notes available.';
        notesEl.appendChild(p);
      }
      bodyEl.replaceWith(notesEl);
    } catch (err) {
      showError('Failed to load meeting notes: ' + err.message);
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
  let listStack = []; // array of <ul> elements indexed by depth

  function flushList() {
    if (listStack.length > 0) {
      container.appendChild(listStack[0]);
      listStack = [];
    }
  }

  for (const line of lines) {
    const listMatch = line.match(/^( *)- (.*)$/);
    if (line.startsWith('### ')) {
      flushList();
      const h3 = document.createElement('h3');
      h3.appendChild(renderInline(line.substring(4)));
      container.appendChild(h3);
    } else if (line.startsWith('## ')) {
      flushList();
      const h2 = document.createElement('h2');
      h2.appendChild(renderInline(line.substring(3)));
      container.appendChild(h2);
    } else if (line.startsWith('# ')) {
      flushList();
      const h1 = document.createElement('h1');
      h1.appendChild(renderInline(line.substring(2)));
      container.appendChild(h1);
    } else if (listMatch) {
      const depth = Math.floor(listMatch[1].length / 2);
      const text = listMatch[2];
      // Pop stack if going back to shallower depth
      while (listStack.length > depth + 1) listStack.pop();
      // Grow stack to required depth
      while (listStack.length < depth + 1) {
        const ul = document.createElement('ul');
        if (listStack.length > 0) {
          const parentUl = listStack[listStack.length - 1];
          const lastLi = parentUl.lastElementChild;
          if (lastLi) lastLi.appendChild(ul);
          else parentUl.appendChild(ul);
        }
        listStack.push(ul);
      }
      const li = document.createElement('li');
      li.appendChild(renderInline(text));
      listStack[listStack.length - 1].appendChild(li);
    } else if (line.trim() === '') {
      flushList();
    } else {
      flushList();
      const p = document.createElement('p');
      p.appendChild(renderInline(line));
      container.appendChild(p);
    }
  }
  flushList();
  return container;
}

function renderInline(text) {
  const frag = document.createDocumentFragment();
  const parts = text.split(/(\*\*[^*]+\*\*|\[[^\]]+\]\([^)]+\))/g);
  for (const part of parts) {
    if (part.startsWith('**') && part.endsWith('**')) {
      const strong = document.createElement('strong');
      strong.textContent = part.slice(2, -2);
      frag.appendChild(strong);
    } else if (/^\[[^\]]+\]\([^)]+\)$/.test(part)) {
      const m = part.match(/^\[([^\]]+)\]\(([^)]+)\)$/);
      const a = document.createElement('a');
      a.href = m[2];
      a.textContent = m[1];
      a.target = '_blank';
      a.rel = 'noopener noreferrer';
      frag.appendChild(a);
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
    if (searchNav) searchNav.hidden = true;
    resetMatchNav();
    renderDateList(getSigMeetings(currentSig), currentDate);
    if (currentDate) {
      try {
        const text = await getTranscript(currentSig, currentDate);
        renderTranscript(text, '');
        await switchToView('summary');
      } catch (_) {}
    }
    return;
  }

  const meetings = getSigMeetings(currentSig);
  const matchCounts = {};
  for (const m of meetings) {
    const key = currentSig + '/' + m.date;
    if (transcriptCache.has(key)) {
      const combined = (transcriptCache.get(key) || '') + '\n' + (meetingNotesCache.get(key) || '');
      matchCounts[m.date] = countMatches(combined, query);
    }
  }

  const filtered = meetings.filter(m => {
    const key = currentSig + '/' + m.date;
    if (!transcriptCache.has(key)) return true; // uncached = show as pending
    const count = matchCounts[m.date];
    return count != null && count > 0;
  });

  renderDateList(filtered, currentDate, matchCounts);

  if (currentDate && transcriptCache.has(currentSig + '/' + currentDate)) {
    const key = currentSig + '/' + currentDate;
    renderTranscript(transcriptCache.get(key), query);
    await switchToView('transcript');
    updateMatchNav();
  } else {
    resetMatchNav();
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

// ── Search match navigation (Issue #9 item 5) ──────────────

function updateMatchNav() {
  const marks = transcriptPanel.querySelectorAll('.transcript-body mark');
  totalMatches = marks.length;
  currentMatchIndex = totalMatches > 0 ? 0 : -1;

  if (totalMatches > 0 && searchNav) {
    searchNav.hidden = false;
    updateMatchCounter();
    highlightCurrentMatch();
  } else if (searchNav) {
    searchNav.hidden = true;
  }
  updateNavButtons();
}

function resetMatchNav() {
  currentMatchIndex = -1;
  totalMatches = 0;
  if (searchNav) searchNav.hidden = true;
  if (matchCounter) matchCounter.textContent = '0 / 0 matches';
  updateNavButtons();
}

function updateMatchCounter() {
  if (!matchCounter) return;
  if (totalMatches === 0) {
    matchCounter.textContent = '0 / 0 matches';
  } else {
    matchCounter.textContent = (currentMatchIndex + 1) + ' / ' + totalMatches + ' matches';
  }
}

function updateNavButtons() {
  if (prevMatchBtn) prevMatchBtn.disabled = totalMatches === 0;
  if (nextMatchBtn) nextMatchBtn.disabled = totalMatches === 0;
}

function highlightCurrentMatch() {
  const marks = transcriptPanel.querySelectorAll('.transcript-body mark');
  for (const m of marks) m.classList.remove('current-match');

  if (currentMatchIndex >= 0 && currentMatchIndex < marks.length) {
    const current = marks[currentMatchIndex];
    current.classList.add('current-match');
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    current.scrollIntoView({
      behavior: prefersReducedMotion ? 'auto' : 'smooth',
      block: 'center'
    });
  }
}

function jumpToNextMatch() {
  if (totalMatches === 0) return;
  currentMatchIndex = (currentMatchIndex + 1) % totalMatches;
  updateMatchCounter();
  highlightCurrentMatch();
}

function jumpToPrevMatch() {
  if (totalMatches === 0) return;
  currentMatchIndex = (currentMatchIndex - 1 + totalMatches) % totalMatches;
  updateMatchCounter();
  highlightCurrentMatch();
}

// ── Scroll-to-top button ────────────────────────────────────

const scrollTopBtn = document.getElementById('scroll-top-btn');

function updateScrollTopVisibility() {
  if (!scrollTopBtn) return;
  scrollTopBtn.hidden = transcriptPanel.scrollTop <= 400;
}

function scrollToTop() {
  transcriptPanel.scrollTo({ top: 0, behavior: 'smooth' });
}

// ── Event wiring ────────────────────────────────────────────

sigSelect.addEventListener('change', e => onSIGChange(e.target.value));
searchInput.addEventListener('input', debounce(e => handleSearch(e.target.value), 300));
transcriptPanel.addEventListener('scroll', updateScrollTopVisibility);
if (scrollTopBtn) scrollTopBtn.addEventListener('click', scrollToTop);

if (prevMatchBtn) prevMatchBtn.addEventListener('click', jumpToPrevMatch);
if (nextMatchBtn) nextMatchBtn.addEventListener('click', jumpToNextMatch);

document.addEventListener('keydown', function (e) {
  if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'g') {
    e.preventDefault();
    if (e.shiftKey) {
      jumpToPrevMatch();
    } else {
      jumpToNextMatch();
    }
  }
});

document.addEventListener('DOMContentLoaded', init);
