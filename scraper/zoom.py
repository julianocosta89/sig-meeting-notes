"""Playwright browser automation to extract transcripts from Zoom recording pages."""

from __future__ import annotations

import logging
import time

from playwright.sync_api import Page
from playwright.sync_api import TimeoutError as PlaywrightTimeout

from scraper.transcript import parse_transcript_html

logger = logging.getLogger(__name__)

# CSS selector for the transcript panel rendered by Zoom's Vue SPA.  Zoom
# serves two variants of the recording player: the newer one tags the panel
# with a data-testid, the ``oldStyle`` one renders a plain <ul>.
TRANSCRIPT_LIST_SELECTOR = "[data-testid='transcript-list'], ul.transcript-list"

# One element per utterance; each carries a stable index, either ``data-row``
# (newer player) or an ``id="transcript-list-item-N"`` suffix (oldStyle player)
TRANSCRIPT_ITEM_SELECTOR = ".transcript-list-item"

# Scroll container for Zoom's virtual-list windowing (newer, then oldStyle player)
SCROLL_CONTAINER_SELECTOR = (
    ".transcript-list .zoom-scrollbar__wrap, .transcript-container .zm-scrollbar__wrap"
)

# Returns [row, outerHTML] for every transcript item currently in the DOM
_COLLECT_ITEMS_JS = (
    "els => els.map(el => ["
    "el.dataset.row ?? el.id.replace('transcript-list-item-', ''), el.outerHTML])"
)

# How long to wait for the page's load event after domcontentloaded (milliseconds)
PAGE_LOAD_TIMEOUT_MS = 20_000

# Fixed grace period (seconds) after page load for Vue SPA to render the transcript
VUE_RENDER_WAIT_S = 5

# Scroll step in pixels for defeating virtual-list windowing
SCROLL_STEP_PX = 400

# Pause between scrolls (seconds) to allow Vue to render newly visible items
SCROLL_PAUSE_S = 0.3

# Known error strings that indicate an unusable recording
_ERROR_STRINGS = [
    "Recording has expired",
    "This recording does not exist",
    "Recording is being processed",
    "This recording has been deleted",
    "Access to this recording is restricted",
]


class ZoomScrapeError(Exception):
    """Raised for recoverable per-recording errors (password, expired, etc.)."""


def scrape_transcript(page: Page, url: str) -> list[str]:  # pragma: no cover
    """
    Navigate to a Zoom recording page and return transcript lines.

    Parameters
    ----------
    page:
        A fresh Playwright page (caller is responsible for context lifecycle).
    url:
        Full Zoom recording URL.

    Returns
    -------
    list[str]
        Lines in "Speaker Name: utterance" format.

    Raises
    ------
    ZoomScrapeError
        For expected failure modes (password, expired, no transcript).
    """
    logger.info("Navigating to %s", url)
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=30_000)
    except PlaywrightTimeout as exc:
        raise ZoomScrapeError("Timed out loading page") from exc

    # Brief pause then check for password prompt
    time.sleep(2)
    if page.query_selector("input[type='password']"):
        raise ZoomScrapeError("Recording is password-protected")

    # Check for error text in page body
    body_text = page.inner_text("body") if page.query_selector("body") else ""
    for err in _ERROR_STRINGS:
        if err.lower() in body_text.lower():
            raise ZoomScrapeError(f"Recording unavailable ({err!r})")

    # Wait for all static resources to finish loading, then give Vue a fixed
    # window to render the transcript. If it's not in the DOM after that, skip.
    logger.info("Waiting for page load …")
    try:
        page.wait_for_load_state("load", timeout=PAGE_LOAD_TIMEOUT_MS)
    except PlaywrightTimeout:
        logger.debug(
            "Page load event did not fire within %dms; proceeding anyway", PAGE_LOAD_TIMEOUT_MS
        )

    logger.info("Waiting %ds for Vue to render transcript …", VUE_RENDER_WAIT_S)
    time.sleep(VUE_RENDER_WAIT_S)

    if page.query_selector(TRANSCRIPT_LIST_SELECTOR) is None:
        raise ZoomScrapeError("No transcript found")
    if page.query_selector(TRANSCRIPT_ITEM_SELECTOR) is None:
        raise ZoomScrapeError("Transcript panel present but no content")

    # The list is windowed: only ~100 items exist in the DOM at once, so items
    # are collected at every scroll step rather than read once at the end.
    items = _collect_transcript_items(page)

    expected = page.get_attribute(TRANSCRIPT_ITEM_SELECTOR, "aria-setsize")
    if expected and expected.isdigit() and len(items) < int(expected):
        logger.warning("Collected %d of %s transcript items", len(items), expected)

    ordered = sorted(items.items(), key=lambda kv: int(kv[0]) if kv[0].isdigit() else -1)
    outer_html = "<div>" + "".join(html for _, html in ordered) + "</div>"
    lines = parse_transcript_html(outer_html)

    if not lines:
        raise ZoomScrapeError("Transcript parsed to empty list")

    logger.info("Extracted %d transcript lines", len(lines))
    return lines


def _collect_transcript_items(page: Page) -> dict[str, str]:  # pragma: no cover
    """
    Scroll the transcript container and return {data-row: outerHTML} for every item.

    Zoom's transcript uses a virtual scroll (zoom-scrollbar) that only keeps a
    window of items in the DOM.  We scroll from top to bottom in steps, pausing
    briefly at each step so Vue can materialise the next batch, and snapshot the
    rendered items each time.
    """
    items: dict[str, str] = {}

    def snapshot() -> None:
        for row, html in page.eval_on_selector_all(TRANSCRIPT_ITEM_SELECTOR, _COLLECT_ITEMS_JS):
            items[row] = html

    container = page.query_selector(SCROLL_CONTAINER_SELECTOR)
    if container is None:
        logger.warning(
            "Scroll container %r not found; collecting rendered items only",
            SCROLL_CONTAINER_SELECTOR,
        )
        snapshot()
        return items

    # Scroll to top first
    container.evaluate("el => { el.scrollTop = 0; }")
    time.sleep(SCROLL_PAUSE_S)
    snapshot()

    # Get total scroll height
    scroll_height: int = container.evaluate("el => el.scrollHeight")
    client_height: int = container.evaluate("el => el.clientHeight")
    max_scroll = max(0, scroll_height - client_height)

    logger.debug(
        "Scrolling transcript container: scrollHeight=%d, clientHeight=%d",
        scroll_height,
        client_height,
    )

    current = 0
    while current < max_scroll:
        current = min(current + SCROLL_STEP_PX, max_scroll)
        container.evaluate("(el, top) => { el.scrollTop = top; }", current)
        time.sleep(SCROLL_PAUSE_S)
        snapshot()

        # Re-check scrollHeight in case new items pushed it down
        new_height: int = container.evaluate("el => el.scrollHeight")
        if new_height > scroll_height:
            scroll_height = new_height
            max_scroll = max(0, scroll_height - client_height)

    logger.debug("Finished scrolling transcript container; collected %d items", len(items))
    return items
