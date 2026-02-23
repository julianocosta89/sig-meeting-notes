"""Playwright tests for the browse UI (Issues #4 and #5)."""

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
                "meetings": [
                    {"date": "2026-02-19", "duration_minutes": 30, "has_summary": False},
                    {"date": "2026-02-05", "duration_minutes": 33, "has_summary": False},
                ],
            },
            {
                "slug": "Java-SIG",
                "name": "Java SIG",
                "meetings": [
                    {"date": "2026-02-10", "duration_minutes": 60, "has_summary": False},
                ],
            },
        ],
    }
    (site / "manifest.json").write_text(json.dumps(manifest))

    # Create transcript files
    go_dir = site / "transcripts" / "Go-SIG"
    go_dir.mkdir(parents=True)
    (go_dir / "2026-02-05.txt").write_text(
        "SIG: Go SIG\n"
        "Date: 2026-02-05\n"
        "Duration: 33 minutes\n"
        "Source URL: https://zoom.us/rec/share/example\n"
        "============================================================\n"
        "\n"
        "Tyler 02:14 Hey, Damien.\n"
        "Damien Mathieu 02:19 Hey!\n"
        "Tyler 02:20 How's it going?\n"
    )
    (go_dir / "2026-02-19.txt").write_text(
        "SIG: Go SIG\n"
        "Date: 2026-02-19\n"
        "Duration: 30 minutes\n"
        "Source URL: https://zoom.us/rec/share/example2\n"
        "============================================================\n"
        "\n"
        "Tyler 02:00 Hello everyone.\n"
        "Damien Mathieu 02:05 Hi Tyler.\n"
    )
    java_dir = site / "transcripts" / "Java-SIG"
    java_dir.mkdir(parents=True)
    (java_dir / "2026-02-10.txt").write_text(
        "SIG: Java SIG\n"
        "Date: 2026-02-10\n"
        "Duration: 60 minutes\n"
        "Source URL: https://zoom.us/rec/share/java-example\n"
        "============================================================\n"
        "\n"
        "Jack 01:00 Welcome to Java SIG.\n"
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
    page.goto(url)
    # Wait until the SIG select has more than 1 option (placeholder + SIGs loaded)
    page.wait_for_function(
        "document.querySelectorAll('#sig-select option').length > 1"
    )


def test_sig_select_populated(browser_ctx):
    """SIG dropdown should contain options from manifest."""
    context, url = browser_ctx
    page = context.new_page()
    _wait_for_app_ready(page, url)
    options = page.evaluate(
        "Array.from(document.querySelectorAll('#sig-select option')).map(o => o.textContent)"
    )
    assert len(options) == 3  # placeholder + 2 SIGs
    assert "Go SIG" in options
    assert "Java SIG" in options
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
    page.goto(url + "?sig=Go-SIG&date=2026-02-05")
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
