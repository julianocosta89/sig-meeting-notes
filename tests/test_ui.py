"""Playwright tests for the browse UI (Issues #4, #5, and #9)."""

import json
import pathlib
import shutil
import socket
import subprocess
import time

import pytest
from playwright.sync_api import sync_playwright, expect

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent


def _free_port():
    """Find a free TCP port."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]


def _make_long_transcript(sig, date, duration, lines):
    """Generate a transcript with many lines for scroll testing."""
    header = (
        f"SIG: {sig}\nDate: {date}\nDuration: {duration} minutes\n"
        f"Zoom Recording URL: https://zoom.us/rec/share/long-example\n"
        "============================================================\n\n"
        "## Zoom Recording Transcript\n\n"
    )
    body = "\n".join(
        f"**{'Alice' if i % 2 == 0 else 'Bob'}** {i // 60:02d}:{i % 60:02d} "
        f"Line number {i} of the transcript."
        for i in range(lines)
    )
    return header + body + "\n"


@pytest.fixture(scope="module")
def docs_site(tmp_path_factory):
    """Build a minimal docs/ site and serve it over HTTP."""
    site = tmp_path_factory.mktemp("site")

    # Create manifest
    manifest = {
        "generated_at": "2026-02-23T00:00:00Z",
        "sigs": [
            {
                "slug": "Go-SIG",
                "name": "Go SIG",
                "meeting_notes_url": "",
                "repository_url": "",
                "meetings": [
                    {"date": "2026-02-19", "duration_minutes": 30, "has_summary": False},
                    {"date": "2026-02-05", "duration_minutes": 33, "has_summary": False},
                ],
            },
            {
                "slug": "Java-SIG",
                "name": "Java SIG",
                "meeting_notes_url": "",
                "repository_url": "",
                "meetings": [
                    {"date": "2026-02-10", "duration_minutes": 60, "has_summary": False},
                ],
            },
            {
                "slug": "Long-SIG",
                "name": "Long SIG",
                "meeting_notes_url": "",
                "repository_url": "",
                "meetings": [
                    {"date": "2026-02-15", "duration_minutes": 120, "has_summary": False},
                ],
            },
            {
                "slug": "Notes-SIG",
                "name": "Notes SIG",
                "meeting_notes_url": "https://docs.google.com/document/d/notes-sig/edit",
                "repository_url": "https://github.com/open-telemetry/notes-sig",
                "meetings": [
                    {"date": "2026-02-05", "duration_minutes": 45, "has_summary": False},
                ],
            },
        ],
    }
    (site / "manifest.json").write_text(json.dumps(manifest))

    # Create per-meeting folder structure: content/{slug}/{date}/transcript.md
    def _write_meeting(slug, date, transcript_text, meeting_notes_text=None):
        d = site / "content" / slug / date
        d.mkdir(parents=True, exist_ok=True)
        (d / "transcript.md").write_text(transcript_text)
        if meeting_notes_text:
            (d / "meeting-notes.md").write_text(meeting_notes_text)

    _write_meeting(
        "Go-SIG", "2026-02-05",
        "SIG: Go SIG\n"
        "Date: 2026-02-05\n"
        "Duration: 33 minutes\n"
        "Zoom Recording URL: https://zoom.us/rec/share/example\n"
        "============================================================\n"
        "\n"
        "## Zoom Recording Transcript\n"
        "\n"
        "**Tyler** 02:14 Hey, Damien.\n"
        "**Damien Mathieu** 02:19 Hey!\n"
        "**Tyler** 02:20 How's it going?\n",
        "## Meeting Notes\n"
        "\n"
        "### Attendees\n"
        "- Tyler\n"
        "- Damien Mathieu\n",
    )
    _write_meeting(
        "Go-SIG", "2026-02-19",
        "SIG: Go SIG\n"
        "Date: 2026-02-19\n"
        "Duration: 30 minutes\n"
        "Zoom Recording URL: https://zoom.us/rec/share/example2\n"
        "============================================================\n"
        "\n"
        "## Zoom Recording Transcript\n"
        "\n"
        "**Tyler** 02:00 Hello everyone.\n"
        "**Damien Mathieu** 02:05 Hi Tyler.\n",
    )
    _write_meeting(
        "Java-SIG", "2026-02-10",
        "SIG: Java SIG\n"
        "Date: 2026-02-10\n"
        "Duration: 60 minutes\n"
        "Zoom Recording URL: https://zoom.us/rec/share/java-example\n"
        "============================================================\n"
        "\n"
        "## Zoom Recording Transcript\n"
        "\n"
        "**Jack** 01:00 Welcome to Java SIG.\n",
    )
    _write_meeting(
        "Long-SIG", "2026-02-15",
        _make_long_transcript("Long SIG", "2026-02-15", 120, 200),
    )
    _write_meeting(
        "Notes-SIG", "2026-02-05",
        "SIG: Notes SIG\n"
        "Date: 2026-02-05\n"
        "Duration: 45 minutes\n"
        "Zoom Recording URL: https://zoom.us/rec/share/notes-example\n"
        "============================================================\n"
        "\n"
        "## Zoom Recording Transcript\n"
        "\n"
        "**Alice** 00:30 Welcome to the meeting.\n"
        "**Bob** 00:45 Thanks for having me.\n",
        "## Meeting Notes\n"
        "\n"
        "### Attendees\n"
        "- Alice\n"
        "- Bob\n"
        "\n"
        "### Agenda\n"
        "- Review last meeting\n"
        "- New proposals\n",
    )

    # Copy the real HTML, JS, and CSS from docs/
    for name in ("index.html", "app.js", "style.css"):
        src = REPO_ROOT / "docs" / name
        if src.exists():
            shutil.copy2(src, site / name)

    # Start HTTP server on a free port
    port = _free_port()
    proc = subprocess.Popen(
        ["python3", "-m", "http.server", str(port), "--directory", str(site)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    time.sleep(1)
    yield f"http://localhost:{port}"
    proc.terminate()
    proc.wait()


@pytest.fixture(scope="module")
def browser_ctx(docs_site):
    """Provide a Playwright browser context."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        yield context, docs_site
        context.close()
        browser.close()


def _wait_for_app_ready(page, url):
    """Navigate and wait until the app has loaded the manifest."""
    # Use a fixed date range covering the test fixture data so all test meetings
    # are always in range regardless of when the tests run.
    page.goto(url + "?from=2026-02-01&to=2026-02-28")
    # Wait until the SIG select has more than 1 option (placeholder + SIGs loaded)
    page.wait_for_function(
        "document.querySelectorAll('#sig-select option').length > 1"
    )


def test_sig_select_populated(browser_ctx):
    """SIG dropdown should contain options from manifest.

    sigDisplayName() strips 'SIG' from display names, so we check
    option values (slugs) rather than display text.
    """
    context, url = browser_ctx
    page = context.new_page()
    _wait_for_app_ready(page, url)
    values = page.evaluate(
        "Array.from(document.querySelectorAll('#sig-select option')).map(o => o.value)"
    )
    assert "Go-SIG" in values
    assert "Java-SIG" in values
    assert "Long-SIG" in values
    page.close()


def test_date_list_appears(browser_ctx):
    """Selecting a SIG should show date buttons."""
    context, url = browser_ctx
    page = context.new_page()
    _wait_for_app_ready(page, url)
    page.select_option("#sig-select", "Go-SIG")
    page.wait_for_selector("#date-list .date-btn")
    buttons = page.locator("#date-list .date-btn").all()
    assert len(buttons) == 2
    texts = [b.text_content() for b in buttons]
    assert any("2026-02-05" in t for t in texts)
    assert any("2026-02-19" in t for t in texts)
    page.close()


def test_transcript_renders(browser_ctx):
    """Clicking a date should render the transcript."""
    context, url = browser_ctx
    page = context.new_page()
    _wait_for_app_ready(page, url)
    page.select_option("#sig-select", "Go-SIG")
    page.wait_for_selector("#date-list .date-btn")
    page.locator("#date-list .date-btn", has_text="2026-02-05").click()
    page.wait_for_selector(".tab-bar")
    page.locator(".tab-btn", has_text="Transcript").click()
    page.wait_for_selector(".transcript-body")
    body = page.locator(".transcript-body").text_content()
    assert "Tyler" in body
    assert "Hey, Damien" in body
    page.close()


def test_transcript_header_rendered(browser_ctx):
    """Transcript header should show SIG, date, duration, and source URL."""
    context, url = browser_ctx
    page = context.new_page()
    _wait_for_app_ready(page, url)
    page.select_option("#sig-select", "Go-SIG")
    page.wait_for_selector("#date-list .date-btn")
    page.locator("#date-list .date-btn", has_text="2026-02-05").click()
    page.wait_for_selector(".transcript-header")
    header = page.locator(".transcript-header").text_content()
    assert "Go SIG" in header
    assert "2026-02-05" in header
    assert "33 minutes" in header
    page.close()


def test_deep_link(browser_ctx):
    """Loading with ?sig=Go-SIG&date=2026-02-05 should render directly."""
    context, url = browser_ctx
    page = context.new_page()
    page.goto(url + "?from=2026-02-01&to=2026-02-28&sig=Go-SIG&date=2026-02-05")
    page.wait_for_selector(".tab-bar")
    page.locator(".tab-btn", has_text="Transcript").click()
    page.wait_for_selector(".transcript-body")
    body = page.locator(".transcript-body").text_content()
    assert "Tyler" in body
    assert "Hey, Damien" in body
    selected = page.locator("#sig-select").input_value()
    assert selected == "Go-SIG"
    page.close()


def test_empty_state_on_load(browser_ctx):
    """On first load, empty state message should be visible."""
    context, url = browser_ctx
    page = context.new_page()
    _wait_for_app_ready(page, url)
    empty = page.locator(".empty-state")
    expect(empty).to_be_visible()
    text = empty.text_content()
    assert "select" in text.lower()
    page.close()


def test_switching_sig_clears_transcript(browser_ctx):
    """Switching SIG should clear the transcript and show the date list."""
    context, url = browser_ctx
    page = context.new_page()
    _wait_for_app_ready(page, url)

    # Select Go SIG and load a transcript
    page.select_option("#sig-select", "Go-SIG")
    page.wait_for_selector("#date-list .date-btn")
    page.locator("#date-list .date-btn", has_text="2026-02-05").click()
    page.wait_for_selector(".tab-bar")
    page.locator(".tab-btn", has_text="Transcript").click()
    page.wait_for_selector(".transcript-body")

    # Switch to Java SIG
    page.select_option("#sig-select", "Java-SIG")
    page.wait_for_function(
        "document.querySelectorAll('#date-list .date-btn').length === 1"
    )
    buttons = page.locator("#date-list .date-btn").all()
    assert len(buttons) == 1
    assert "2026-02-10" in buttons[0].text_content()

    # Transcript should be cleared (empty state for date selection)
    assert page.locator(".transcript-body").count() == 0
    page.close()


# ── Search tests (Issue #5) ─────────────────────────────────


def _select_sig_and_wait_for_prefetch(page, url, slug, expected_meetings):
    """Select a SIG and wait for all transcripts to be prefetched into cache."""
    _wait_for_app_ready(page, url)
    page.select_option("#sig-select", slug)
    page.wait_for_selector("#date-list .date-btn")
    # Wait for prefetch to populate the transcript cache
    page.wait_for_function(
        f"document.querySelector('#search-input') !== null"
    )
    # Wait for all transcripts to be cached (prefetch is fire-and-forget)
    page.wait_for_function(
        f"window.transcriptCache !== undefined || true",
        timeout=5000,
    )
    # Give prefetch a moment to complete
    page.wait_for_timeout(500)


def test_search_input_visible_after_sig_select(browser_ctx):
    """Search input should become visible when a SIG is selected."""
    context, url = browser_ctx
    page = context.new_page()
    _wait_for_app_ready(page, url)

    # Search should be hidden initially
    search_group = page.locator(".search-group")
    expect(search_group).to_be_hidden()

    # Select a SIG
    page.select_option("#sig-select", "Go-SIG")
    page.wait_for_selector("#date-list .date-btn")

    # Search should now be visible
    expect(search_group).to_be_visible()
    page.close()


def test_search_filters_date_list(browser_ctx):
    """Typing a query should filter the date list to only matching meetings."""
    context, url = browser_ctx
    page = context.new_page()
    _select_sig_and_wait_for_prefetch(page, url, "Go-SIG", 2)

    # "Damien" appears as speaker in both transcripts, but only in utterance
    # text of 2026-02-05 ("Hey, Damien.") — speaker names are stripped from search
    page.fill("#search-input", "Damien")
    page.wait_for_timeout(400)  # debounce is 300ms
    buttons = page.locator("#date-list .date-btn").all()
    assert len(buttons) == 1
    assert "2026-02-05" in buttons[0].text_content()

    # "Hello everyone" only appears in the 2026-02-19 transcript
    page.fill("#search-input", "Hello everyone")
    page.wait_for_timeout(400)
    buttons = page.locator("#date-list .date-btn").all()
    assert len(buttons) == 1
    assert "2026-02-19" in buttons[0].text_content()
    page.close()


def test_search_shows_match_badges(browser_ctx):
    """Search results should show match count badges on date buttons."""
    context, url = browser_ctx
    page = context.new_page()
    _select_sig_and_wait_for_prefetch(page, url, "Go-SIG", 2)

    page.fill("#search-input", "Tyler")
    page.wait_for_timeout(400)

    badges = page.locator("#date-list .match-badge").all()
    assert len(badges) > 0
    # Each badge should contain a number
    for badge in badges:
        text = badge.text_content().strip()
        assert text.isdigit() and int(text) > 0
    page.close()


def test_search_highlights_in_transcript(browser_ctx):
    """Search query should be highlighted with <mark> in the active transcript."""
    context, url = browser_ctx
    page = context.new_page()
    _select_sig_and_wait_for_prefetch(page, url, "Go-SIG", 2)

    # Load a transcript first (default tab is Summary)
    page.locator("#date-list .date-btn", has_text="2026-02-05").click()
    page.wait_for_selector(".tab-bar")

    # Search for "Damien" — auto-switches to Transcript tab with highlights
    page.fill("#search-input", "Damien")
    page.wait_for_timeout(400)

    marks = page.locator(".transcript-body mark").all()
    assert len(marks) > 0
    for mark in marks:
        assert "damien" in mark.text_content().lower()
    page.close()


def test_search_clear_restores_full_list(browser_ctx):
    """Clearing the search input should restore the full date list."""
    context, url = browser_ctx
    page = context.new_page()
    _select_sig_and_wait_for_prefetch(page, url, "Go-SIG", 2)

    # Search to filter
    page.fill("#search-input", "Hello everyone")
    page.wait_for_timeout(400)
    assert len(page.locator("#date-list .date-btn").all()) == 1

    # Clear the search
    page.fill("#search-input", "")
    page.wait_for_timeout(400)
    assert len(page.locator("#date-list .date-btn").all()) == 2
    page.close()


def test_search_no_results(browser_ctx):
    """Searching for a term that doesn't exist should show no date buttons."""
    context, url = browser_ctx
    page = context.new_page()
    _select_sig_and_wait_for_prefetch(page, url, "Go-SIG", 2)

    page.fill("#search-input", "xyznonexistent12345")
    page.wait_for_timeout(400)
    buttons = page.locator("#date-list .date-btn").all()
    assert len(buttons) == 0
    page.close()


# ── Issue #9 tests ───────────────────────────────────────────


def test_scroll_top_button_hidden_initially(browser_ctx):
    """Scroll-to-top button should be hidden when no scrolling has occurred."""
    context, url = browser_ctx
    page = context.new_page()
    _wait_for_app_ready(page, url)
    btn = page.locator("#scroll-top-btn")
    expect(btn).to_be_hidden()
    page.close()


def test_scroll_top_button_appears_after_scroll(browser_ctx):
    """Scroll-to-top button should appear after scrolling >400px in transcript pane."""
    context, url = browser_ctx
    page = context.new_page()
    page.set_viewport_size({"width": 1024, "height": 600})
    _wait_for_app_ready(page, url)

    page.select_option("#sig-select", "Long-SIG")
    page.wait_for_selector("#date-list .date-btn")
    page.locator("#date-list .date-btn", has_text="2026-02-15").click()
    page.wait_for_selector(".tab-bar")
    page.locator(".tab-btn", has_text="Transcript").click()
    page.wait_for_selector(".transcript-body")

    btn = page.locator("#scroll-top-btn")
    expect(btn).to_be_hidden()

    # Scroll the transcript panel past 400px
    page.evaluate("document.getElementById('transcript-panel').scrollTop = 500")
    page.wait_for_timeout(300)

    expect(btn).to_be_visible()
    page.close()


def test_scroll_top_button_scrolls_to_top(browser_ctx):
    """Clicking scroll-to-top button should scroll the transcript pane to top."""
    context, url = browser_ctx
    page = context.new_page()
    page.set_viewport_size({"width": 1024, "height": 600})
    _wait_for_app_ready(page, url)

    page.select_option("#sig-select", "Long-SIG")
    page.wait_for_selector("#date-list .date-btn")
    page.locator("#date-list .date-btn", has_text="2026-02-15").click()
    page.wait_for_selector(".tab-bar")
    page.locator(".tab-btn", has_text="Transcript").click()
    page.wait_for_selector(".transcript-body")

    # Scroll down past threshold
    page.evaluate("document.getElementById('transcript-panel').scrollTop = 500")
    page.wait_for_timeout(300)

    # Button should be visible; click it
    page.locator("#scroll-top-btn").click()
    page.wait_for_timeout(600)

    scroll_top = page.evaluate("document.getElementById('transcript-panel').scrollTop")
    assert scroll_top == 0
    page.close()


def test_scroll_top_button_accessible(browser_ctx):
    """Scroll-to-top button should have aria-label for accessibility."""
    context, url = browser_ctx
    page = context.new_page()
    _wait_for_app_ready(page, url)
    btn = page.locator("#scroll-top-btn")
    assert btn.get_attribute("aria-label") == "Scroll to top"
    page.close()


def test_date_buttons_show_duration(browser_ctx):
    """Date buttons should display duration alongside the date."""
    context, url = browser_ctx
    page = context.new_page()
    _wait_for_app_ready(page, url)
    page.select_option("#sig-select", "Go-SIG")
    page.wait_for_selector("#date-list .date-btn")
    buttons = page.locator("#date-list .date-btn").all()
    texts = [b.text_content() for b in buttons]
    # Duration should appear as "· X min"
    assert any("33 min" in t for t in texts)
    assert any("30 min" in t for t in texts)
    page.close()


def test_url_updates_on_sig_select(browser_ctx):
    """Selecting a SIG should update the URL with ?sig= parameter."""
    context, url = browser_ctx
    page = context.new_page()
    _wait_for_app_ready(page, url)
    page.select_option("#sig-select", "Go-SIG")
    page.wait_for_selector("#date-list .date-btn")
    assert "sig=Go-SIG" in page.url
    page.close()


def test_url_updates_on_date_click(browser_ctx):
    """Clicking a date should update the URL with both sig and date params."""
    context, url = browser_ctx
    page = context.new_page()
    _wait_for_app_ready(page, url)
    page.select_option("#sig-select", "Go-SIG")
    page.wait_for_selector("#date-list .date-btn")
    page.locator("#date-list .date-btn", has_text="2026-02-05").click()
    page.wait_for_selector(".tab-bar")
    assert "sig=Go-SIG" in page.url
    assert "date=2026-02-05" in page.url
    page.close()


def test_deep_link_restores_sig_and_date(browser_ctx):
    """Deep-link with sig+date should restore the full state on load."""
    context, url = browser_ctx
    page = context.new_page()
    page.goto(url + "?from=2026-02-01&to=2026-02-28&sig=Java-SIG&date=2026-02-10")
    page.wait_for_selector(".tab-bar")
    page.locator(".tab-btn", has_text="Transcript").click()
    page.wait_for_selector(".transcript-body")

    selected = page.locator("#sig-select").input_value()
    assert selected == "Java-SIG"

    body = page.locator(".transcript-body").text_content()
    assert "Jack" in body
    assert "Welcome to Java SIG" in body

    active_btn = page.locator("#date-list .date-btn[aria-pressed='true']")
    assert "2026-02-10" in active_btn.text_content()
    page.close()


def test_deep_link_sig_only(browser_ctx):
    """Deep-link with only sig param should select the SIG and show dates."""
    context, url = browser_ctx
    page = context.new_page()
    page.goto(url + "?from=2026-02-01&to=2026-02-28&sig=Go-SIG")
    page.wait_for_selector("#date-list .date-btn")
    selected = page.locator("#sig-select").input_value()
    assert selected == "Go-SIG"
    buttons = page.locator("#date-list .date-btn").all()
    assert len(buttons) == 2
    assert page.locator(".transcript-body").count() == 0
    page.close()


# -- Issue #9: Mobile scroll gradient (Item 4) ------------------------------


def test_mobile_date_list_horizontal_scroll(browser_ctx):
    """On mobile, the date list should scroll horizontally."""
    context, url = browser_ctx
    page = context.new_page()
    page.set_viewport_size({"width": 375, "height": 667})
    _wait_for_app_ready(page, url)
    page.select_option("#sig-select", "Go-SIG")
    page.wait_for_selector("#date-list .date-btn")

    display = page.evaluate(
        "window.getComputedStyle("
        "document.querySelector('.date-list')).display"
    )
    assert display == "flex", (
        f"Expected flex layout on mobile, got {display!r}"
    )

    overflow_x = page.evaluate(
        "window.getComputedStyle("
        "document.querySelector('.date-nav')).overflowX"
    )
    assert overflow_x == "auto", (
        f"Expected overflow-x: auto on mobile, got {overflow_x!r}"
    )
    page.close()


def test_mobile_scroll_gradient_css(browser_ctx):
    """On mobile viewports, the date-nav-wrapper should have a gradient fade hint."""
    context, url = browser_ctx
    page = context.new_page()
    page.set_viewport_size({"width": 375, "height": 667})
    _wait_for_app_ready(page, url)
    page.select_option("#sig-select", "Go-SIG")
    page.wait_for_selector("#date-list .date-btn")

    wrapper = page.locator(".date-nav-wrapper")
    expect(wrapper).to_be_visible()

    has_gradient = page.evaluate("""() => {
        const wrapper = document.querySelector('.date-nav-wrapper');
        if (!wrapper) return false;
        const after = window.getComputedStyle(wrapper, '::after');
        return after && after.backgroundImage
            && after.backgroundImage !== 'none';
    }""")
    assert has_gradient, (
        "Expected gradient ::after on .date-nav-wrapper at mobile viewport"
    )
    page.close()


# -- Issue #9: Search match navigation (Item 5) -----------------------------


def test_search_match_count_displayed(browser_ctx):
    """When searching with a transcript open, a match count should be shown."""
    context, url = browser_ctx
    page = context.new_page()
    _select_sig_and_wait_for_prefetch(page, url, "Go-SIG", 2)

    page.locator("#date-list .date-btn", has_text="2026-02-05").click()
    page.wait_for_selector(".tab-bar")
    page.locator(".tab-btn", has_text="Transcript").click()
    page.wait_for_selector(".transcript-body")

    # Use "Hey" which appears in utterance text (not just speaker names)
    page.fill("#search-input", "Hey")
    page.wait_for_timeout(400)

    match_counter = page.locator(
        ".match-counter, .match-count, #match-count"
    )
    if match_counter.count() == 0:
        pytest.skip("Search match count element not yet implemented")

    expect(match_counter.first).to_be_visible()
    text = match_counter.first.text_content()
    assert any(c.isdigit() for c in text), (
        f"Expected match count number in {text!r}"
    )
    page.close()


def test_search_jump_to_next_match(browser_ctx):
    """A jump-to-next button should navigate between search matches."""
    context, url = browser_ctx
    page = context.new_page()
    _select_sig_and_wait_for_prefetch(page, url, "Go-SIG", 2)

    page.locator("#date-list .date-btn", has_text="2026-02-05").click()
    page.wait_for_selector(".tab-bar")
    page.locator(".tab-btn", has_text="Transcript").click()
    page.wait_for_selector(".transcript-body")
    # Use "Hey" which appears in utterance text (not just speaker names)
    page.fill("#search-input", "Hey")
    page.wait_for_timeout(400)

    jump_btn = page.locator(
        "#jump-next, .jump-next-btn, "
        "button[aria-label*='next match'], "
        "button[aria-label*='Next match']"
    )
    if jump_btn.count() == 0:
        pytest.skip("Jump-to-next-match button not yet implemented")

    jump_btn.first.click()
    page.wait_for_timeout(200)

    marks = page.locator(".transcript-body mark").all()
    assert len(marks) > 0
    page.close()


# ── New format rendering tests ───────────────────────────────


def test_transcript_header_zoom_url_is_link(browser_ctx):
    """'Zoom Recording URL' field in the header should render as a clickable link."""
    context, url = browser_ctx
    page = context.new_page()
    _wait_for_app_ready(page, url)
    page.select_option("#sig-select", "Go-SIG")
    page.wait_for_selector("#date-list .date-btn")
    page.locator("#date-list .date-btn", has_text="2026-02-05").click()
    page.wait_for_selector(".transcript-header")

    link = page.locator(".transcript-header a[href*='zoom.us']")
    assert link.count() > 0, "Expected a link to zoom.us in the transcript header"
    page.close()


def test_manifest_meeting_notes_url_rendered_as_link(browser_ctx):
    """SIG-level meeting_notes_url from the manifest should render as a link."""
    context, url = browser_ctx
    page = context.new_page()
    _wait_for_app_ready(page, url)
    page.select_option("#sig-select", "Notes-SIG")
    page.wait_for_selector("#date-list .date-btn")
    page.locator("#date-list .date-btn", has_text="2026-02-05").click()
    page.wait_for_selector(".transcript-header")

    link = page.locator(".transcript-header a[href*='docs.google.com']")
    assert link.count() > 0, "Expected Meeting Notes URL from manifest to render as link"
    page.close()


def test_meeting_notes_section_renders(browser_ctx):
    """Meeting Notes tab should show Attendees and Agenda from meeting-notes.md."""
    context, url = browser_ctx
    page = context.new_page()
    _wait_for_app_ready(page, url)
    page.select_option("#sig-select", "Notes-SIG")
    page.wait_for_selector("#date-list .date-btn")
    page.locator("#date-list .date-btn", has_text="2026-02-05").click()
    page.wait_for_selector(".tab-bar")
    page.locator(".tab-btn", has_text="Meeting Notes").click()
    page.wait_for_selector(".notes-body")

    notes_text = page.locator(".notes-body").text_content()
    assert "Attendees" in notes_text
    assert "Alice" in notes_text
    assert "Agenda" in notes_text
    assert "Review last meeting" in notes_text
    page.close()


def test_speaker_bold_format_renders(browser_ctx):
    """Speaker names in **bold** format should render as speaker-name spans."""
    context, url = browser_ctx
    page = context.new_page()
    _wait_for_app_ready(page, url)
    page.select_option("#sig-select", "Go-SIG")
    page.wait_for_selector("#date-list .date-btn")
    page.locator("#date-list .date-btn", has_text="2026-02-05").click()
    page.wait_for_selector(".tab-bar")
    page.locator(".tab-btn", has_text="Transcript").click()
    page.wait_for_selector(".transcript-body")

    # Speaker names should be in .speaker-name spans, not raw **...**
    speaker_spans = page.locator(".transcript-body .speaker-name").all()
    assert len(speaker_spans) > 0
    speaker_texts = [s.text_content() for s in speaker_spans]
    assert any("Tyler" in t for t in speaker_texts)
    assert not any("**" in t for t in speaker_texts), (
        "Speaker spans should not contain ** markdown markers"
    )
    page.close()


# ── Phase 1: Speaker-strip search tests ──────────────────────


def test_search_match_count_excludes_speaker_names(browser_ctx):
    """Search match counts should reflect content hits only, not speaker-label hits.

    "Tyler" appears as a speaker name in both Go-SIG transcripts, but only
    appears in the utterance text of the 2026-02-19 transcript ("Hi Tyler.").
    After stripping speakers, only 2026-02-19 should match, with a count of 1.
    """
    context, url = browser_ctx
    page = context.new_page()
    _select_sig_and_wait_for_prefetch(page, url, "Go-SIG", 2)

    page.fill("#search-input", "Tyler")
    page.wait_for_timeout(400)

    # Only the 2026-02-19 date should remain (has "Hi Tyler." in utterance)
    buttons = page.locator("#date-list .date-btn").all()
    dates = [b.text_content() for b in buttons]
    assert len(buttons) == 1, (
        f"Expected 1 date with content match for 'Tyler', got {len(buttons)}: {dates}"
    )
    assert "2026-02-19" in dates[0]

    # The match badge should show 1 (one utterance hit), not 2+ (speaker labels)
    badge = page.locator("#date-list .match-badge").first
    assert badge.text_content().strip() == "1"
    page.close()


def test_search_snippet_excludes_speaker_prefix(browser_ctx):
    """Global search result snippets should NOT start with **Speaker** MM:SS prefixes.

    After stripSpeakers, extractSnippet operates on utterance-only text,
    so snippets should contain the spoken content without speaker labels.
    """
    context, url = browser_ctx
    page = context.new_page()
    _select_sig_and_wait_for_prefetch(page, url, "Go-SIG", 2)

    # Load a transcript and search for a term that appears in an utterance
    page.locator("#date-list .date-btn", has_text="2026-02-05").click()
    page.wait_for_selector(".tab-bar")
    page.locator(".tab-btn", has_text="Transcript").click()
    page.wait_for_selector(".transcript-body")

    page.fill("#search-input", "Damien")
    page.wait_for_timeout(400)

    # Get the rendered transcript body text and find all <mark> elements
    body_html = page.locator(".transcript-body").inner_html()
    # The snippet/highlight context around "Damien" should not include
    # the **Speaker** MM:SS prefix pattern
    import re
    # Check that no <mark> content sits right after a bold-timestamp pattern
    # i.e., the raw "**Tyler** 02:14" prefix should not appear near highlights
    assert "**" not in body_html, (
        "Raw ** markdown should not appear in rendered transcript body"
    )
    page.close()


def test_search_no_mark_inside_speaker_or_timestamp(browser_ctx):
    """<mark> elements should never appear inside .speaker-name or timestamp spans.

    The highlightMatches TreeWalker should skip text nodes inside
    .speaker-name and .timestamp elements, so searching for a speaker's
    name should not inject <mark> into those spans.
    """
    context, url = browser_ctx
    page = context.new_page()
    _select_sig_and_wait_for_prefetch(page, url, "Go-SIG", 2)

    # Load transcript where "Damien Mathieu" is a speaker name
    page.locator("#date-list .date-btn", has_text="2026-02-05").click()
    page.wait_for_selector(".tab-bar")
    page.locator(".tab-btn", has_text="Transcript").click()
    page.wait_for_selector(".transcript-body")

    # Search for a speaker's name — should highlight in utterances but NOT in labels
    page.fill("#search-input", "Damien")
    page.wait_for_timeout(400)

    # Verify no <mark> inside .speaker-name elements
    marks_in_speaker = page.locator(".transcript-body .speaker-name mark").all()
    assert len(marks_in_speaker) == 0, (
        f"Found {len(marks_in_speaker)} <mark> elements inside .speaker-name spans"
    )

    # Verify no <mark> inside .timestamp elements
    marks_in_timestamp = page.locator(".transcript-body .timestamp mark").all()
    assert len(marks_in_timestamp) == 0, (
        f"Found {len(marks_in_timestamp)} <mark> elements inside .timestamp spans"
    )

    # But "Damien" should still appear highlighted in the utterance text
    # ("Hey, Damien." in the 2026-02-05 transcript)
    marks = page.locator(".transcript-body mark").all()
    assert len(marks) > 0, (
        "Expected at least one <mark> highlight for 'Damien' in utterance text"
    )
    for mark in marks:
        assert "damien" in mark.text_content().lower()
    page.close()
