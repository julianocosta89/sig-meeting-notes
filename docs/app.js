// ── Theme management ─────────────────────────────────────────

const THEME_KEY = 'otel-notes-theme';
const THEME_MODES = ['auto', 'light', 'dark'];

const THEME_ICONS = {
  auto:  '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><defs><clipPath id="half-clip"><rect x="12" y="3" width="9" height="18" /></clipPath></defs><circle cx="12" cy="12" r="9" fill="currentColor" stroke="none" clip-path="url(#half-clip)" /><circle cx="12" cy="12" r="9"></circle>',
  light: '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/></svg>',
  dark: '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>',
};

const THEME_LABELS = {
  auto: 'Switch to light mode',
  light: 'Switch to dark mode',
  dark: 'Switch to auto mode',
};

function getStoredTheme() {
  try { return localStorage.getItem(THEME_KEY) || 'auto'; } catch { return 'auto'; }
}

function applyTheme(mode) {
  if (mode === 'auto') {
    document.documentElement.removeAttribute('data-theme');
  } else {
    document.documentElement.setAttribute('data-theme', mode);
  }
}

function initThemeToggle() {
  const btn = document.getElementById('theme-toggle');
  if (!btn) return;

  function updateBtn(mode) {
    btn.innerHTML = THEME_ICONS[mode];
    btn.setAttribute('aria-label', THEME_LABELS[mode]);
    btn.title = THEME_LABELS[mode];
  }

  btn.addEventListener('click', () => {
    const current = getStoredTheme();
    const next = THEME_MODES[(THEME_MODES.indexOf(current) + 1) % THEME_MODES.length];
    try { localStorage.setItem(THEME_KEY, next); } catch {}
    applyTheme(next);
    updateBtn(next);
  });

  updateBtn(getStoredTheme());
}

// State
let manifest = null;
let currentSig = null;
let currentDate = null;
let currentView = 'summary'; // 'transcript' | 'summary' | 'meeting-notes'
const transcriptCache = new Map();
const meetingNotesCache = new Map();
const summaryCache = new Map();

// Date range filter state
let filterFrom = null;       // YYYY-MM-DD
let filterTo   = null;       // YYYY-MM-DD
let calYear    = null;       // currently displayed calendar month
let calMonth   = null;
let pendingFrom = null;      // first click during "selecting to" mode
let hoverDate  = null;       // mouseover preview date

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
const globalSearchInput = document.getElementById('global-search-input');

// ── Date range helpers ────────────────────────────────────────

function isoDate(d) {
  const y = d.getFullYear();
  const m = String(d.getMonth() + 1).padStart(2, '0');
  const day = String(d.getDate()).padStart(2, '0');
  return `${y}-${m}-${day}`;
}

function inRange(dateStr) {
  return dateStr >= filterFrom && dateStr <= filterTo;
}

function isValidDateParam(s) {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(s)) return false;
  const d = new Date(s + 'T00:00:00');
  if (isNaN(d.getTime())) return false;
  // Reject rolled-over dates (e.g. "2026-02-31" normalises to "2026-03-03")
  const y = String(d.getFullYear()).padStart(4, '0');
  const mo = String(d.getMonth() + 1).padStart(2, '0');
  const day = String(d.getDate()).padStart(2, '0');
  return `${y}-${mo}-${day}` === s;
}

let manifestMinDate = null;
function computeManifestMinDate() {
  let min = '9999-99-99';
  for (const sig of manifest.sigs)
    for (const m of sig.meetings)
      if (m.date < min) min = m.date;
  manifestMinDate = min;
}

function defaultRangeStart() {
  const d = new Date();
  d.setDate(d.getDate() - 14);
  return d;
}

function initDateRange() {
  const today = new Date();
  const from  = defaultRangeStart();
  filterFrom = isoDate(from);
  filterTo   = isoDate(today);
  calYear  = today.getFullYear();
  calMonth = today.getMonth();
  updateDateRangeLabel();
}

function updateDateRangeLabel() {
  const today = isoDate(new Date());
  const twoWeeksAgo = isoDate(defaultRangeStart());
  const label = document.getElementById('date-range-label');
  label.textContent =
    filterFrom === twoWeeksAgo && filterTo === today
      ? 'last two weeks'
      : filterFrom + ' \u2192 ' + filterTo;
}

function renderCalendar() {
  const grid = document.getElementById('cal-grid');
  const monthLabel = document.getElementById('cal-month-label');
  grid.innerHTML = '';

  const monthNames = ['January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'];
  monthLabel.textContent = monthNames[calMonth] + ' ' + calYear;

  const today = isoDate(new Date());

  // Determine effective range for highlighting
  let rangeStart = filterFrom;
  let rangeEnd = filterTo;
  if (pendingFrom) {
    rangeStart = pendingFrom;
    rangeEnd = hoverDate || pendingFrom;
    if (rangeEnd < rangeStart) {
      const tmp = rangeStart;
      rangeStart = rangeEnd;
      rangeEnd = tmp;
    }
  }

  // Weekday headers
  for (const day of ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']) {
    const span = document.createElement('span');
    span.className = 'cal-weekday';
    span.textContent = day;
    grid.appendChild(span);
  }

  // First day of month and number of days
  const firstDay = new Date(calYear, calMonth, 1).getDay();
  const daysInMonth = new Date(calYear, calMonth + 1, 0).getDate();

  // Padding cells
  for (let i = 0; i < firstDay; i++) {
    const span = document.createElement('span');
    span.className = 'cal-day cal-day--empty';
    grid.appendChild(span);
  }

  // Day buttons
  for (let d = 1; d <= daysInMonth; d++) {
    const dateStr = calYear + '-' + String(calMonth + 1).padStart(2, '0') + '-' + String(d).padStart(2, '0');
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'cal-day';
    btn.dataset.date = dateStr;
    btn.textContent = d;
    btn.setAttribute('aria-label', monthNames[calMonth] + ' ' + d + ', ' + calYear);

    const isDisabled = dateStr < manifestMinDate || dateStr > today;
    if (isDisabled) {
      btn.classList.add('cal-day--disabled');
      btn.disabled = true;
    }

    if (dateStr === rangeStart) btn.classList.add('cal-day--from');
    if (dateStr === rangeEnd) btn.classList.add('cal-day--to');
    if (dateStr > rangeStart && dateStr < rangeEnd) btn.classList.add('cal-day--in-range');
    if (dateStr === today) btn.classList.add('cal-day--today');
    if (pendingFrom && dateStr === pendingFrom) btn.classList.add('cal-day--pending');

    grid.appendChild(btn);
  }

  // Update prev/next button disabled state
  const calPrev = document.getElementById('cal-prev');
  const calNext = document.getElementById('cal-next');
  if (manifestMinDate) {
    const minYear = parseInt(manifestMinDate.slice(0, 4), 10);
    const minMonth = parseInt(manifestMinDate.slice(5, 7), 10) - 1;
    calPrev.disabled = calYear < minYear || (calYear === minYear && calMonth <= minMonth);
  }
  const todayDate = new Date();
  calNext.disabled = calYear > todayDate.getFullYear() || (calYear === todayDate.getFullYear() && calMonth >= todayDate.getMonth());
}

function openCalendar() {
  pendingFrom = null;
  hoverDate = null;
  renderCalendar();
  const popup = document.getElementById('calendar-popup');
  popup.removeAttribute('hidden');
  document.getElementById('date-range-row').setAttribute('aria-expanded', 'true');
  // Move focus to the previous-month button inside the popup
  const firstFocusable = popup.querySelector('button:not(:disabled)');
  if (firstFocusable) firstFocusable.focus();
}

function closeCalendar() {
  const popup = document.getElementById('calendar-popup');
  popup.setAttribute('hidden', '');
  const row = document.getElementById('date-range-row');
  row.setAttribute('aria-expanded', 'false');
  row.focus();
  pendingFrom = null;
  hoverDate = null;
}

function onDateRangeChange() {
  updateDateRangeLabel();
  updateURL(currentSig, currentDate, false);

  // Repopulate SIG dropdown
  sigSelect.innerHTML = '<option value="">Choose a SIG...</option>';
  populateSigSelect();

  // Clear SIG selection if it no longer has meetings in range
  if (currentSig) {
    const sig = manifest.sigs.find(s => s.slug === currentSig);
    if (!sig || !sig.meetings.some(m => inRange(m.date))) {
      currentSig = null;
      currentDate = null;
      dateList.innerHTML = '';
      transcriptPanel.innerHTML = '';
      if (searchGroup) searchGroup.hidden = true;
      if (dateNavWrapper) dateNavWrapper.hidden = true;
      showEmptyState();
      updateURL(null, null, true);
      if (globalSearchInput.value.trim()) handleGlobalSearch(globalSearchInput.value.trim());
      return;
    }
    sigSelect.value = currentSig;
    renderDateList(getSigMeetings(currentSig).filter(m => inRange(m.date)), currentDate);

    // If current date is out of range, clear it
    if (currentDate && !inRange(currentDate)) {
      currentDate = null;
      clearTranscript();
      updateURL(currentSig, null, true);
    }
  }

  // Re-run active search
  if (globalSearchInput.value.trim()) handleGlobalSearch(globalSearchInput.value.trim());
  else if (searchInput.value.trim()) handleSearch(searchInput.value.trim());
}

function wireCalendarListeners() {
  const dateRangeRow = document.getElementById('date-range-row');
  const calGrid = document.getElementById('cal-grid');
  const calPrev = document.getElementById('cal-prev');
  const calNext = document.getElementById('cal-next');
  const calReset = document.getElementById('cal-reset');

  dateRangeRow.addEventListener('click', openCalendar);
  dateRangeRow.addEventListener('keydown', e => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      openCalendar();
    }
  });

  calGrid.addEventListener('click', e => {
    const btn = e.target.closest('.cal-day');
    if (!btn || btn.disabled) return;
    e.stopPropagation();
    const d = btn.dataset.date;
    if (!d) return;
    if (!pendingFrom) {
      pendingFrom = d;
      renderCalendar();
    } else {
      if (d >= pendingFrom) {
        filterFrom = pendingFrom;
        filterTo   = d;
      } else {
        pendingFrom = d;
        renderCalendar();
        return;
      }
      closeCalendar();
      onDateRangeChange();
    }
  });

  calGrid.addEventListener('mouseover', e => {
    if (!pendingFrom) return;
    const btn = e.target.closest('.cal-day');
    if (!btn || btn.disabled || !btn.dataset.date) return;
    if (hoverDate === btn.dataset.date) return; // skip redundant re-render
    hoverDate = btn.dataset.date;
    renderCalendar();
  });

  calPrev.addEventListener('click', e => {
    e.stopPropagation();
    calMonth--;
    if (calMonth < 0) { calMonth = 11; calYear--; }
    renderCalendar();
  });

  calNext.addEventListener('click', e => {
    e.stopPropagation();
    calMonth++;
    if (calMonth > 11) { calMonth = 0; calYear++; }
    renderCalendar();
  });

  calReset.addEventListener('click', e => {
    e.stopPropagation();
    initDateRange();
    closeCalendar();
    onDateRangeChange();
  });

  // Focus trap: keep Tab cycling inside the open popup
  const popup = document.getElementById('calendar-popup');
  popup.addEventListener('keydown', e => {
    if (e.key === 'Tab') {
      const focusable = popup.querySelectorAll('button:not(:disabled)');
      if (focusable.length === 0) return;
      const first = focusable[0];
      const last = focusable[focusable.length - 1];
      if (e.shiftKey) {
        if (document.activeElement === first) { e.preventDefault(); last.focus(); }
      } else {
        if (document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    }
  });

  // Close on click outside
  document.addEventListener('click', e => {
    const calPopup = document.getElementById('calendar-popup');
    if (!calPopup.hidden && !calPopup.contains(e.target) &&
        !dateRangeRow.contains(e.target))
      closeCalendar();
  });
}

// Match navigation state
let currentMatchIndex = -1;
let totalMatches = 0;

// Global search state
let globalSearchActive = false;
let globalSearchAbort = null;

// ── Initialization ──────────────────────────────────────────

let initInProgress = false;

async function init() {
  if (initInProgress) return;
  initInProgress = true;
  try {
    const res = await fetch('manifest.json');
    if (!res.ok) {
      showError('Failed to load manifest.', init);
      return;
    }
    manifest = await res.json();
    computeManifestMinDate();
    initDateRange();
    populateSigSelect();
    restoreFromURL();
    wireCalendarListeners();
    const pendingGlobal = globalSearchInput.value.trim();
    if (pendingGlobal) handleGlobalSearch(pendingGlobal);
  } catch (err) {
    showError('Failed to load manifest.', init);
  } finally {
    initInProgress = false;
  }
}

function populateSigSelect() {
  // Remove previous empty-range hint if present
  const oldHint = document.getElementById('no-meetings-hint');
  if (oldHint) oldHint.remove();

  let count = 0;
  for (const sig of manifest.sigs) {
    if (!sig.meetings.some(m => inRange(m.date))) continue;
    const opt = document.createElement('option');
    opt.value = sig.slug;
    opt.textContent = sigDisplayName(sig.name);
    sigSelect.appendChild(opt);
    count++;
  }

  // Show a hint when the date range contains no meetings
  if (count === 0) {
    const hint = document.createElement('p');
    hint.id = 'no-meetings-hint';
    hint.style.cssText = 'font-size:0.8rem;color:var(--fg-muted);margin:0.25rem 0 0;';
    hint.textContent = 'No meetings in this date range.';
    sigSelect.parentNode.appendChild(hint);
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

async function onSIGChange(slug, options) {
  globalSearchInput.value = '';
  if (globalSearchActive) {
    globalSearchActive = false;
    if (globalSearchAbort) { globalSearchAbort.abort(); globalSearchAbort = null; }
  }
  const replace = options && options.replace;
  currentSig = slug;
  currentDate = null;
  currentView = 'summary';
  searchInput.value = '';
  resetMatchNav();

  if (slug) {
    if (searchGroup) searchGroup.hidden = false;
    if (dateNavWrapper) dateNavWrapper.hidden = false;
    if (searchNav) searchNav.hidden = true;
    renderDateList(getSigMeetings(slug).filter(m => inRange(m.date)), null);
    clearTranscript();
    updateURL(slug, null, replace);
    prefetchTranscripts(slug);
  } else {
    if (searchGroup) searchGroup.hidden = true;
    if (dateNavWrapper) dateNavWrapper.hidden = true;
    if (searchNav) searchNav.hidden = true;
    dateList.innerHTML = '';
    showEmptyState();
    updateURL(null, null, replace);
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

  // Show "no results" message when search yields nothing
  if (matchCounts && meetings.length === 0) {
    const noResults = document.createElement('li');
    noResults.className = 'no-results-message';
    noResults.setAttribute('role', 'status');
    const strong = document.createElement('strong');
    strong.textContent = 'No matches found';
    const hint = document.createElement('p');
    hint.textContent = 'Try a different search term or check spelling.';
    noResults.appendChild(strong);
    noResults.appendChild(hint);
    dateList.appendChild(noResults);
  }
}

// Keyboard navigation for date list (arrow keys, Home, End)
dateList.addEventListener('keydown', function (e) {
  const btns = Array.from(dateList.querySelectorAll('.date-btn'));
  const idx = btns.indexOf(e.target);
  if (idx === -1) return;
  let next = -1;
  if (e.key === 'ArrowDown' || e.key === 'ArrowRight') next = Math.min(idx + 1, btns.length - 1);
  else if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') next = Math.max(idx - 1, 0);
  else if (e.key === 'Home') next = 0;
  else if (e.key === 'End') next = btns.length - 1;
  if (next !== -1 && next !== idx) {
    e.preventDefault();
    btns[next].focus();
  }
});

// ── Date click ──────────────────────────────────────────────

async function onDateClick(date, options) {
  const replace = options && options.replace;
  currentDate = date;
  updateURL(currentSig, date, replace);
  renderDateList(getSigMeetings(currentSig).filter(m => inRange(m.date)), date);
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
    showError('Failed to load transcript: ' + err.message, () => onDateClick(requestedDate, { replace: true }));
  }
}

// ── Transcript fetching ─────────────────────────────────────

async function getTranscript(slug, date, signal) {
  const key = slug + '/' + date;
  if (!transcriptCache.has(key)) {
    const res = await fetch('content/' + slug + '/' + date + '/transcript.md', signal ? { signal } : undefined);
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
  const meetings = getSigMeetings(slug).filter(m => inRange(m.date));
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

  // Render breadcrumb for orientation
  if (currentSig && currentDate) {
    const breadcrumb = document.createElement('nav');
    breadcrumb.className = 'breadcrumb';
    breadcrumb.setAttribute('aria-label', 'Current location');
    const sigBtn = document.createElement('button');
    sigBtn.className = 'breadcrumb-sig';
    sigBtn.textContent = sigDisplayName(getSigName(currentSig));
    sigBtn.addEventListener('click', () => {
      currentDate = null;
      searchInput.value = '';
      resetMatchNav();
      renderDateList(getSigMeetings(currentSig).filter(m => inRange(m.date)), null);
      clearTranscript();
      updateURL(currentSig, null);
    });
    const sep = document.createElement('span');
    sep.className = 'breadcrumb-sep';
    sep.textContent = '/';
    sep.setAttribute('aria-hidden', 'true');
    const dateSpan = document.createElement('span');
    dateSpan.className = 'breadcrumb-date';
    dateSpan.textContent = currentDate;
    breadcrumb.appendChild(sigBtn);
    breadcrumb.appendChild(sep);
    breadcrumb.appendChild(dateSpan);
    transcriptPanel.appendChild(breadcrumb);
  }

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
  const views = [['summary', 'Summary'], ['meeting-notes', 'Meeting Notes'], ['transcript', 'Transcript']];
  for (const [view, label] of views) {
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'tab-btn';
    btn.dataset.view = view;
    btn.id = 'tab-' + view;
    btn.setAttribute('role', 'tab');
    btn.setAttribute('aria-selected', 'false');
    btn.setAttribute('aria-controls', 'tabpanel');
    btn.setAttribute('tabindex', '-1');
    btn.textContent = label;
    btn.addEventListener('click', () => switchToView(view));
    tabBar.appendChild(btn);
  }
  // Keyboard navigation for tabs (WAI-ARIA Tabs pattern)
  tabBar.addEventListener('keydown', function (e) {
    const tabs = Array.from(tabBar.querySelectorAll('[role="tab"]'));
    const idx = tabs.indexOf(e.target);
    if (idx === -1) return;
    let next = -1;
    if (e.key === 'ArrowRight') next = (idx + 1) % tabs.length;
    else if (e.key === 'ArrowLeft') next = (idx - 1 + tabs.length) % tabs.length;
    else if (e.key === 'Home') next = 0;
    else if (e.key === 'End') next = tabs.length - 1;
    if (next !== -1) {
      e.preventDefault();
      tabs[next].focus();
      switchToView(tabs[next].dataset.view);
    }
  });
  headerCard.appendChild(tabBar);

  transcriptPanel.appendChild(headerCard);

  // Append a summary-body placeholder; caller will call switchToView to fill it
  const placeholder = document.createElement('div');
  placeholder.className = 'summary-body';
  placeholder.id = 'tabpanel';
  placeholder.setAttribute('role', 'tabpanel');
  placeholder.setAttribute('tabindex', '0');
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
  // New format: **Speaker** MM:SS or HH:MM:SS utterance
  const boldMatch = line.match(/^\*\*(.+?)\*\*\s+(\d+:\d+(?::\d+)?)\s+(.*)$/);
  if (boldMatch) return { speaker: boldMatch[1], timestamp: boldMatch[2], utterance: boldMatch[3] };
  // Legacy format: Speaker MM:SS or HH:MM:SS utterance
  const match = line.match(/^(.+?)\s+(\d+:\d+(?::\d+)?)\s+(.*)$/);
  if (!match) return { speaker: null, timestamp: null, utterance: line };
  return { speaker: match[1], timestamp: match[2], utterance: match[3] };
}

function stripSpeakers(text) {
  return text.split('\n').map(line => {
    const parsed = parseBodyLine(line);
    if (!parsed || !parsed.utterance) return line;
    if (parsed.speaker === null && parsed.timestamp === null) return line;
    return parsed.utterance;
  }).join('\n');
}

// ── SVG Icons for empty/error states ─────────────────────────

function createSVGIcon(type) {
  const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  svg.setAttribute('width', '48');
  svg.setAttribute('height', '48');
  svg.setAttribute('viewBox', '0 0 24 24');
  svg.setAttribute('fill', 'none');
  svg.setAttribute('stroke', 'currentColor');
  svg.setAttribute('stroke-width', '1.5');
  svg.setAttribute('stroke-linecap', 'round');
  svg.setAttribute('stroke-linejoin', 'round');
  svg.setAttribute('aria-hidden', 'true');
  svg.classList.add('state-icon');

  if (type === 'folder') {
    const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    path.setAttribute('d', 'M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z');
    svg.appendChild(path);
  } else if (type === 'calendar') {
    const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
    rect.setAttribute('x', '3'); rect.setAttribute('y', '4');
    rect.setAttribute('width', '18'); rect.setAttribute('height', '18');
    rect.setAttribute('rx', '2'); rect.setAttribute('ry', '2');
    const line1 = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    line1.setAttribute('x1', '16'); line1.setAttribute('y1', '2');
    line1.setAttribute('x2', '16'); line1.setAttribute('y2', '6');
    const line2 = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    line2.setAttribute('x1', '8'); line2.setAttribute('y1', '2');
    line2.setAttribute('x2', '8'); line2.setAttribute('y2', '6');
    const line3 = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    line3.setAttribute('x1', '3'); line3.setAttribute('y1', '10');
    line3.setAttribute('x2', '21'); line3.setAttribute('y2', '10');
    svg.appendChild(rect); svg.appendChild(line1); svg.appendChild(line2); svg.appendChild(line3);
  } else if (type === 'alert') {
    const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    path.setAttribute('d', 'M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z');
    const line1 = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    line1.setAttribute('x1', '12'); line1.setAttribute('y1', '9');
    line1.setAttribute('x2', '12'); line1.setAttribute('y2', '13');
    const line2 = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    line2.setAttribute('x1', '12'); line2.setAttribute('y1', '17');
    line2.setAttribute('x2', '12.01'); line2.setAttribute('y2', '17');
    svg.appendChild(path); svg.appendChild(line1); svg.appendChild(line2);
  }
  return svg;
}

// ── Display helpers ─────────────────────────────────────────

function clearTranscript() {
  const div = document.createElement('div');
  div.className = 'empty-state';
  div.appendChild(createSVGIcon('calendar'));
  const heading = document.createElement('p');
  heading.className = 'state-heading';
  heading.textContent = 'Choose a meeting date';
  div.appendChild(heading);
  const p = document.createElement('p');
  p.textContent = 'Select a date from the sidebar to view the transcript, summary, and meeting notes.';
  div.appendChild(p);
  transcriptPanel.replaceChildren(div);
}

function showEmptyState() {
  const div = document.createElement('div');
  div.className = 'empty-state';
  div.appendChild(createSVGIcon('folder'));
  const heading = document.createElement('p');
  heading.className = 'state-heading';
  heading.textContent = 'Browse SIG meeting transcripts';
  div.appendChild(heading);
  const p = document.createElement('p');
  p.textContent = 'Choose a Special Interest Group from the dropdown to see its recorded meetings.';
  div.appendChild(p);
  const hint = document.createElement('p');
  hint.className = 'state-hint';
  hint.innerHTML = 'Or press <kbd>/</kbd> to search across all SIGs.';
  div.appendChild(hint);
  transcriptPanel.replaceChildren(div);
}

function showError(msg, retryFn) {
  const div = document.createElement('div');
  div.className = 'error-state';
  div.appendChild(createSVGIcon('alert'));
  const p = document.createElement('p');
  p.textContent = msg;
  div.appendChild(p);
  if (retryFn) {
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'retry-btn';
    btn.textContent = 'Retry';
    btn.addEventListener('click', retryFn);
    div.appendChild(btn);
  }
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
  const requestedSig = currentSig;
  const requestedDate = currentDate;
  currentView = view;

  history.replaceState(null, '', location.search + '#' + view);

  for (const btn of transcriptPanel.querySelectorAll('.tab-btn')) {
    const isSelected = btn.dataset.view === view;
    btn.setAttribute('aria-selected', isSelected ? 'true' : 'false');
    btn.setAttribute('tabindex', isSelected ? '0' : '-1');
  }
  const panel = transcriptPanel.querySelector('#tabpanel');
  if (panel) panel.setAttribute('aria-labelledby', 'tab-' + view);

  const bodyEl = transcriptPanel.querySelector('.transcript-body, .summary-body, .notes-body');
  if (!bodyEl) return;

  function makePanel(className) {
    const el = document.createElement('div');
    el.className = className;
    el.id = 'tabpanel';
    el.setAttribute('role', 'tabpanel');
    el.setAttribute('aria-labelledby', 'tab-' + view);
    el.setAttribute('tabindex', '0');
    return el;
  }

  if (view === 'summary') {
    if (!meetingHasSummary(requestedSig, requestedDate)) {
      const summaryEl = makePanel('summary-body');
      const p = document.createElement('p');
      p.textContent = 'No summary available.';
      summaryEl.appendChild(p);
      bodyEl.replaceWith(summaryEl);
    } else {
      try {
        const md = await getSummary(requestedSig, requestedDate);
        if (currentSig !== requestedSig || currentDate !== requestedDate) return;
        const summaryEl = makePanel('summary-body');
        summaryEl.appendChild(renderMarkdown(md));
        bodyEl.replaceWith(summaryEl);
      } catch (err) {
        if (currentSig !== requestedSig || currentDate !== requestedDate) return;
        showError('Failed to load summary: ' + err.message, () => {
          summaryCache.delete(currentSig + '/' + currentDate);
          onDateClick(currentDate, { replace: true }).then(() => switchToView('summary'));
        });
      }
    }
  } else if (view === 'meeting-notes') {
    try {
      const notesText = await getMeetingNotes(requestedSig, requestedDate);
      if (currentSig !== requestedSig || currentDate !== requestedDate) return;
      const notesEl = makePanel('notes-body');
      if (notesText) {
        notesEl.appendChild(renderMarkdown(notesText));
      } else {
        const p = document.createElement('p');
        p.textContent = 'No meeting notes available.';
        notesEl.appendChild(p);
      }
      bodyEl.replaceWith(notesEl);
    } catch (err) {
      if (currentSig !== requestedSig || currentDate !== requestedDate) return;
      showError('Failed to load meeting notes: ' + err.message, () => {
        meetingNotesCache.delete(currentSig + '/' + currentDate);
        onDateClick(currentDate, { replace: true }).then(() => switchToView('meeting-notes'));
      });
    }
  } else {
    try {
      const text = await getTranscript(requestedSig, requestedDate);
      if (currentSig !== requestedSig || currentDate !== requestedDate) return;
      const sepIdx = text.indexOf('\n====');
      const bodyText = sepIdx === -1 ? '' :
        text.substring(text.indexOf('\n', sepIdx + 1) + 1).trim();
      const transcriptEl = buildTranscriptBody(bodyText, getCurrentQuery());
      transcriptEl.id = 'tabpanel';
      transcriptEl.setAttribute('role', 'tabpanel');
      transcriptEl.setAttribute('aria-labelledby', 'tab-' + view);
      transcriptEl.setAttribute('tabindex', '0');
      bodyEl.replaceWith(transcriptEl);
    } catch (err) {
      if (currentSig !== requestedSig || currentDate !== requestedDate) return;
      showError('Failed to load transcript: ' + err.message, () => {
        transcriptCache.delete(currentSig + '/' + currentDate);
        onDateClick(currentDate, { replace: true }).then(() => switchToView('transcript'));
      });
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
  function debounced() {
    const args = arguments;
    clearTimeout(t);
    t = setTimeout(() => fn.apply(this, args), ms);
  }
  debounced.cancel = () => clearTimeout(t);
  return debounced;
}

async function handleSearch(query) {
  if (!currentSig || globalSearchActive) return;

  if (!query.trim()) {
    if (searchNav) searchNav.hidden = true;
    resetMatchNav();
    renderDateList(getSigMeetings(currentSig).filter(m => inRange(m.date)), currentDate);
    if (currentDate) {
      const sig = currentSig, date = currentDate;
      try {
        const text = await getTranscript(sig, date);
        if (currentSig !== sig || currentDate !== date) return;
        renderTranscript(text, '');
        await switchToView('summary');
      } catch (_) {}
    }
    return;
  }

  const meetings = getSigMeetings(currentSig).filter(m => inRange(m.date));
  const matchCounts = {};
  for (const m of meetings) {
    const key = currentSig + '/' + m.date;
    if (transcriptCache.has(key)) {
      matchCounts[m.date] = countMatches(transcriptCache.get(key) || '', query);
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
  const lower = stripSpeakers(text).toLowerCase();
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
  const walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT, {
    acceptNode(node) {
      if (node.parentElement && node.parentElement.closest('.speaker-name, .timestamp')) {
        return NodeFilter.FILTER_REJECT;
      }
      return NodeFilter.FILTER_ACCEPT;
    }
  });
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

function updateURL(sig, date, replace) {
  const p = new URLSearchParams();
  if (sig) p.set('sig', sig);
  if (date) p.set('date', date);
  // Add from/to only when they differ from the default two-week window
  const today = isoDate(new Date());
  const twoWeeksAgo = isoDate(defaultRangeStart());
  if (filterFrom && filterTo && (filterFrom !== twoWeeksAgo || filterTo !== today)) {
    p.set('from', filterFrom);
    p.set('to', filterTo);
  }
  const qs = p.toString();
  const url = qs ? '?' + qs : location.pathname;
  if (replace) {
    history.replaceState({ sig: sig || null, date: date || null }, '', url);
  } else {
    history.pushState({ sig: sig || null, date: date || null }, '', url);
  }
}

function restoreFromURL() {
  const p = new URLSearchParams(location.search);
  const sig = p.get('sig');
  const date = p.get('date');
  const fromParam = p.get('from');
  const toParam = p.get('to');
  const validViews = new Set(['summary', 'meeting-notes', 'transcript']);
  const targetView = validViews.has(location.hash.slice(1)) ? location.hash.slice(1) : null;

  // Restore date range from URL params
  if (fromParam && toParam && isValidDateParam(fromParam) && isValidDateParam(toParam) && fromParam <= toParam) {
    const toDate = new Date(toParam + 'T00:00:00');
    filterFrom = fromParam;
    filterTo = toParam;
    calYear = toDate.getFullYear();
    calMonth = toDate.getMonth();
    updateDateRangeLabel();
    // Re-populate SIG dropdown with new range
    sigSelect.innerHTML = '<option value="">Choose a SIG...</option>';
    populateSigSelect();
  }

  const sigInRange = sig && manifest.sigs.some(
    s => s.slug === sig && s.meetings.some(m => inRange(m.date))
  );
  if (sigInRange) {
    sigSelect.value = sig;
    onSIGChange(sig, { replace: true }).then(() => {
      if (date && inRange(date)) {
        onDateClick(date, { replace: true }).then(() => {
          if (targetView && targetView !== currentView) switchToView(targetView);
        });
      }
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

// ── Global Search ───────────────────────────────────────────

function getAllMeetings() {
  if (!manifest) return [];
  const all = [];
  for (const sig of manifest.sigs) {
    for (const m of sig.meetings) {
      if (!inRange(m.date)) continue;
      all.push({ sig: sig.slug, sigName: sig.name, date: m.date, duration: m.duration_minutes });
    }
  }
  return all;
}

function extractSnippet(text, query, contextLength = 120) {
  text = stripSpeakers(text);
  const lower = text.toLowerCase();
  const q = query.toLowerCase();
  const idx = lower.indexOf(q);
  if (idx === -1) return '';
  const start = Math.max(0, idx - contextLength);
  const end = Math.min(text.length, idx + q.length + contextLength);
  let snippet = text.substring(start, end).replace(/\n/g, ' ').replace(/\s+/g, ' ').trim();
  if (start > 0) snippet = '\u2026' + snippet;
  if (end < text.length) snippet += '\u2026';
  return snippet;
}

function buildSnippetWithHighlight(text, query) {
  const frag = document.createDocumentFragment();
  if (!query || !text) {
    frag.appendChild(document.createTextNode(text || ''));
    return frag;
  }
  const lower = text.toLowerCase();
  const q = query.toLowerCase();
  const qLen = query.length;
  let lastIdx = 0;
  let idx = lower.indexOf(q);
  while (idx !== -1) {
    if (idx > lastIdx) frag.appendChild(document.createTextNode(text.substring(lastIdx, idx)));
    const mark = document.createElement('mark');
    mark.textContent = text.substring(idx, idx + qLen);
    frag.appendChild(mark);
    lastIdx = idx + qLen;
    idx = lower.indexOf(q, lastIdx);
  }
  if (lastIdx < text.length) frag.appendChild(document.createTextNode(text.substring(lastIdx)));
  return frag;
}

function gatherCachedGlobalResults(query) {
  const results = [];
  for (const { sig, sigName, date, duration } of getAllMeetings()) {
    const key = sig + '/' + date;
    if (transcriptCache.has(key)) {
      const text = transcriptCache.get(key);
      const count = countMatches(text, query);
      if (count > 0) {
        results.push({ sig, sigName, date, duration, count, snippet: extractSnippet(text, query) });
      }
    }
  }
  results.sort((a, b) => b.count !== a.count ? b.count - a.count : b.date.localeCompare(a.date));
  return results;
}

function renderGlobalResults(results, isLoading, cachedCount, totalCount, query) {
  transcriptPanel.innerHTML = '';
  const container = document.createElement('div');
  container.className = 'global-results';

  // Summary bar
  const summary = document.createElement('div');
  summary.className = 'global-results-summary';
  const totalMatchCount = results.reduce((sum, r) => sum + r.count, 0);
  if (isLoading) {
    const found = document.createElement('span');
    found.textContent = totalMatchCount
      ? totalMatchCount + ' match' + (totalMatchCount !== 1 ? 'es' : '') + ' in ' + results.length + ' meeting' + (results.length !== 1 ? 's' : '')
      : 'Searching\u2026';
    const progress = document.createElement('span');
    progress.className = 'global-results-progress';
    progress.textContent = cachedCount + ' / ' + totalCount + ' transcripts searched';
    summary.appendChild(found);
    summary.appendChild(progress);
  } else if (results.length === 0) {
    summary.textContent = 'No matches found across ' + totalCount + ' meetings.';
  } else {
    summary.textContent = totalMatchCount + ' match' + (totalMatchCount !== 1 ? 'es' : '') + ' across ' + results.length + ' meeting' + (results.length !== 1 ? 's' : '');
  }
  container.appendChild(summary);

  if (results.length > 0) {
    const ul = document.createElement('ul');
    ul.className = 'global-results-list';
    for (const result of results) {
      const li = document.createElement('li');
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'global-result-btn';

      const header = document.createElement('div');
      header.className = 'result-header';

      const sigName = document.createElement('span');
      sigName.className = 'result-sig-name';
      sigName.textContent = sigDisplayName(result.sigName);

      const meta = document.createElement('span');
      meta.className = 'result-meta';
      meta.textContent = result.date + (result.duration ? ' \u00b7 ' + result.duration + ' min' : '');

      const badge = document.createElement('span');
      badge.className = 'match-badge';
      badge.textContent = result.count;

      header.appendChild(sigName);
      header.appendChild(meta);
      header.appendChild(badge);

      const snippet = document.createElement('p');
      snippet.className = 'result-snippet';
      snippet.appendChild(buildSnippetWithHighlight(result.snippet, query));

      btn.appendChild(header);
      btn.appendChild(snippet);
      btn.addEventListener('click', () => onGlobalResultClick(result.sig, result.date, query));
      li.appendChild(btn);
      ul.appendChild(li);
    }
    container.appendChild(ul);
  }

  transcriptPanel.appendChild(container);
}

async function fetchUncachedForGlobalSearch(query, signal, totalCount) {
  const allMeetings = getAllMeetings();
  const uncached = allMeetings.filter(({ sig, date }) => !transcriptCache.has(sig + '/' + date));
  let succeeded = 0;
  let failed = 0;
  let rafPending = false;

  const scheduleUpdate = () => {
    if (rafPending || signal.aborted) return;
    rafPending = true;
    requestAnimationFrame(() => {
      rafPending = false;
      if (!signal.aborted) {
        const results = gatherCachedGlobalResults(query);
        const cachedCount = allMeetings.length - uncached.length + succeeded;
        renderGlobalResults(results, succeeded + failed < uncached.length, cachedCount, totalCount, query);
      }
    });
  };

  // Limit concurrent fetches to avoid overwhelming the server
  const CONCURRENCY = 6;
  let cursor = 0;
  async function worker() {
    while (cursor < uncached.length && !signal.aborted) {
      const idx = cursor++;
      const { sig, date } = uncached[idx];
      try { await getTranscript(sig, date, signal); succeeded++; } catch (_) { failed++; }
      scheduleUpdate();
    }
  }
  await Promise.all(Array.from({ length: Math.min(CONCURRENCY, uncached.length) }, worker));

  if (!signal.aborted) {
    const results = gatherCachedGlobalResults(query);
    const cachedCount = allMeetings.length - uncached.length + succeeded;
    // Keep isLoading=true when some fetches failed so the summary
    // shows "X / Y transcripts searched" rather than claiming all were searched.
    renderGlobalResults(results, failed > 0, cachedCount, totalCount, query);
  }
}

async function handleGlobalSearch(query) {
  const q = query.trim();

  if (!q) {
    exitGlobalSearch();
    return;
  }

  if (!manifest) return;

  // Cancel any previous search
  if (globalSearchAbort) globalSearchAbort.abort();
  globalSearchAbort = new AbortController();
  const signal = globalSearchAbort.signal;

  globalSearchActive = true;
  if (searchGroup) searchGroup.hidden = true;
  if (dateNavWrapper) dateNavWrapper.hidden = true;
  if (searchNav) searchNav.hidden = true;
  resetMatchNav();

  const allMeetings = getAllMeetings();
  const totalCount = allMeetings.length;
  const cachedCount = allMeetings.filter(({ sig, date }) => transcriptCache.has(sig + '/' + date)).length;
  const hasUncached = cachedCount < totalCount;

  // Show cached results immediately
  const initial = gatherCachedGlobalResults(q);
  renderGlobalResults(initial, hasUncached, cachedCount, totalCount, q);

  if (hasUncached) {
    await fetchUncachedForGlobalSearch(q, signal, totalCount);
  }
}

function exitGlobalSearch() {
  if (!globalSearchActive) return;
  globalSearchActive = false;
  if (globalSearchAbort) {
    globalSearchAbort.abort();
    globalSearchAbort = null;
  }
  // Restore SIG-specific UI
  if (currentSig) {
    if (searchGroup) searchGroup.hidden = false;
    if (dateNavWrapper) dateNavWrapper.hidden = false;
    const localQuery = getCurrentQuery();
    if (localQuery) {
      if (!currentDate) clearTranscript();
      handleSearch(localQuery).catch(() => {});
    } else {
      renderDateList(getSigMeetings(currentSig).filter(m => inRange(m.date)), currentDate, null);
      if (currentDate) {
        onDateClick(currentDate, { replace: true }).catch(() => {});
      } else {
        clearTranscript();
      }
    }
  } else {
    if (searchGroup) searchGroup.hidden = true;
    if (dateNavWrapper) dateNavWrapper.hidden = true;
    showEmptyState();
  }
}

async function onGlobalResultClick(slug, date, query) {
  globalSearchInput.value = '';
  exitGlobalSearch();

  sigSelect.value = slug;
  await onSIGChange(slug, { replace: true }); // resets searchInput.value to ''
  searchInput.value = query;
  await onDateClick(date);
  if (query) await handleSearch(query);
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
const debouncedHandleSearch = debounce(e => handleSearch(e.target.value), 300);
const debouncedHandleGlobalSearch = debounce(e => handleGlobalSearch(e.target.value), 300);
searchInput.addEventListener('input', debouncedHandleSearch);
globalSearchInput.addEventListener('input', debouncedHandleGlobalSearch);
transcriptPanel.addEventListener('scroll', updateScrollTopVisibility);
if (scrollTopBtn) scrollTopBtn.addEventListener('click', scrollToTop);

if (prevMatchBtn) prevMatchBtn.addEventListener('click', jumpToPrevMatch);
if (nextMatchBtn) nextMatchBtn.addEventListener('click', jumpToNextMatch);

document.addEventListener('keydown', function (e) {
  const target = e.target;
  const inInput = target.tagName === 'INPUT' || target.tagName === 'TEXTAREA' || target.tagName === 'SELECT';

  // Ctrl/Cmd+G — next/prev search match
  if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'g') {
    e.preventDefault();
    if (e.shiftKey) {
      jumpToPrevMatch();
    } else {
      jumpToNextMatch();
    }
    return;
  }

  // Escape — close calendar popup first, then clear search inputs
  if (e.key === 'Escape') {
    const calPopup = document.getElementById('calendar-popup');
    if (calPopup && !calPopup.hidden) {
      closeCalendar();
      return;
    }
    if (target === globalSearchInput && globalSearchInput.value) {
      debouncedHandleGlobalSearch.cancel();
      globalSearchInput.value = '';
      handleGlobalSearch('');
      globalSearchInput.blur();
      return;
    }
    if (target === searchInput && searchInput.value) {
      debouncedHandleSearch.cancel();
      searchInput.value = '';
      handleSearch('');
      searchInput.blur();
      return;
    }
    if (inInput) {
      target.blur();
      return;
    }
  }

  // "/" — focus global search (when not typing in an input)
  if (e.key === '/' && !inInput && !e.ctrlKey && !e.metaKey) {
    e.preventDefault();
    globalSearchInput.focus();
    return;
  }
});

// ── Browser back/forward navigation ─────────────────────────

window.addEventListener('popstate', function () {
  if (!manifest) return;
  const p = new URLSearchParams(location.search);
  const sig = p.get('sig') || '';
  const date = p.get('date') || '';
  const fromParam = p.get('from');
  const toParam = p.get('to');
  const validViews = new Set(['summary', 'meeting-notes', 'transcript']);
  const targetView = validViews.has(location.hash.slice(1)) ? location.hash.slice(1) : null;

  // Restore date range from URL
  if (fromParam && toParam && isValidDateParam(fromParam) && isValidDateParam(toParam) && fromParam <= toParam) {
    filterFrom = fromParam;
    filterTo = toParam;
    updateDateRangeLabel();
  } else if (filterFrom !== isoDate(defaultRangeStart()) || filterTo !== isoDate(new Date())) {
    initDateRange();
  }
  sigSelect.innerHTML = '<option value="">Choose a SIG...</option>';
  populateSigSelect();

  const popSigInRange = sig && manifest.sigs.some(
    s => s.slug === sig && s.meetings.some(m => inRange(m.date))
  );
  if (sig !== (currentSig || '') && (popSigInRange || !sig)) {
    sigSelect.value = sig || '';
    onSIGChange(sig, { replace: true }).then(() => {
      if (date && inRange(date)) {
        onDateClick(date, { replace: true }).then(() => {
          if (targetView && targetView !== currentView) switchToView(targetView);
        });
      }
    });
  } else if (date !== (currentDate || '') && (sig === (currentSig || '') || !sig)) {
    if (globalSearchActive) {
      globalSearchActive = false;
      if (globalSearchAbort) { globalSearchAbort.abort(); globalSearchAbort = null; }
      globalSearchInput.value = '';
      if (searchGroup) searchGroup.hidden = false;
      if (dateNavWrapper) dateNavWrapper.hidden = false;
    }
    if (date && inRange(date)) {
      onDateClick(date, { replace: true }).then(() => {
        if (targetView && targetView !== currentView) switchToView(targetView);
      });
    } else {
      currentDate = null;
      renderDateList(getSigMeetings(currentSig).filter(m => inRange(m.date)), null);
      clearTranscript();
      searchInput.value = '';
      resetMatchNav();
    }
  } else {
    // Range may have changed with the same sig/date — reconcile the view.
    if (currentSig) {
      const inRangeMeetings = getSigMeetings(currentSig).filter(m => inRange(m.date));
      if (inRangeMeetings.length === 0) {
        currentSig = null;
        currentDate = null;
        dateList.innerHTML = '';
        transcriptPanel.innerHTML = '';
        if (searchGroup) searchGroup.hidden = true;
        if (dateNavWrapper) dateNavWrapper.hidden = true;
        showEmptyState();
        updateURL(null, null, true);
        if (globalSearchInput.value.trim()) handleGlobalSearch(globalSearchInput.value.trim());
      } else {
        const activeDate = currentDate && inRange(currentDate) ? currentDate : null;
        renderDateList(inRangeMeetings, activeDate);
        if (currentDate && !inRange(currentDate)) {
          currentDate = null;
          clearTranscript();
        }
        if (targetView && targetView !== currentView) switchToView(targetView);
      }
    } else if (targetView && targetView !== currentView) {
      switchToView(targetView);
    }
  }
});

// ── Mobile sidebar toggle ────────────────────────────────────

const sidebarToggle = document.getElementById('sidebar-toggle');
const sidebar = document.querySelector('.sidebar');

function initSidebarToggle() {
  if (!sidebarToggle || !sidebar) return;
  const mq = window.matchMedia('(max-width: 640px)');

  function updateToggleVisibility() {
    if (mq.matches) {
      sidebarToggle.hidden = false;
    } else {
      sidebarToggle.hidden = true;
      sidebar.classList.remove('collapsed');
    }
  }

  sidebarToggle.addEventListener('click', () => {
    const isCollapsed = sidebar.classList.toggle('collapsed');
    sidebarToggle.setAttribute('aria-expanded', isCollapsed ? 'false' : 'true');
  });

  mq.addEventListener('change', updateToggleVisibility);
  updateToggleVisibility();
}

initSidebarToggle();
initThemeToggle();

document.addEventListener('DOMContentLoaded', init);
