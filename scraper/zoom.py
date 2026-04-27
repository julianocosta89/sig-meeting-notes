"""Playwright browser automation to extract transcripts from Zoom recording pages."""

from __future__ import annotations

import logging
import time

from playwright.sync_api import Page
from playwright.sync_api import TimeoutError as PlaywrightTimeout

from scraper.transcript import parse_transcript_html

logger = logging.getLogger(__name__)

# CSS selector for the transcript list rendered by Zoom's Vue SPA
TRANSCRIPT_LIST_SELECTOR = "ul.transcript-list"

# Fallback broader selector if the precise one misses
TRANSCRIPT_WRAPPER_SELECTOR = ".transcript-wrapper"

# Scroll container for Zoom's virtual-list windowing
SCROLL_CONTAINER_SELECTOR = ".zm-scrollbar__wrap"

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


def scrape_transcript(page: Page, url: str) -> list[str]:
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
        if page.query_selector(TRANSCRIPT_WRAPPER_SELECTOR):
            raise ZoomScrapeError("Transcript panel present but no content")
        raise ZoomScrapeError("No transcript found")

    # Defeat virtual-list windowing by scrolling the container top-to-bottom
    _scroll_transcript_into_view(page)

    # Extract outerHTML of the transcript list
    ul_element = page.query_selector(TRANSCRIPT_LIST_SELECTOR)
    if ul_element is None:
        raise ZoomScrapeError("Transcript list disappeared after scroll")

    outer_html = ul_element.evaluate("el => el.outerHTML")
    lines = parse_transcript_html(outer_html)

    if not lines:
        raise ZoomScrapeError("Transcript parsed to empty list")

    logger.info("Extracted %d transcript lines", len(lines))
    return lines


def _scroll_transcript_into_view(page: Page) -> None:
    """
    Scroll the zm-scrollbar container to force all virtual-list items to render.

    Zoom's transcript uses a virtual scroll (zm-scrollbar) that only keeps
    visible <li> elements in the DOM.  We scroll from top to bottom in steps,
    pausing briefly at each step so Vue can materialise the next batch of items.
    """
    container = page.query_selector(SCROLL_CONTAINER_SELECTOR)
    if container is None:
        logger.warning(
            "Scroll container %r not found; skipping scroll",
            SCROLL_CONTAINER_SELECTOR,
        )
        return

    # Scroll to top first
    container.evaluate("el => { el.scrollTop = 0; }")
    time.sleep(SCROLL_PAUSE_S)

    # Get total scroll height
    scroll_height: int = container.evaluate("el => el.scrollHeight")
    client_height: int = container.evaluate("el => el.clientHeight")
    max_scroll = max(0, scroll_height - client_height)

    if max_scroll == 0:
        # Content fits without scrolling – nothing to do
        return

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

        # Re-check scrollHeight in case new items pushed it down
        new_height: int = container.evaluate("el => el.scrollHeight")
        if new_height > scroll_height:
            scroll_height = new_height
            max_scroll = max(0, scroll_height - client_height)

    # Scroll back to top so any final render pass picks up early items
    container.evaluate("el => { el.scrollTop = 0; }")
    time.sleep(SCROLL_PAUSE_S)

    logger.debug("Finished scrolling transcript container")
