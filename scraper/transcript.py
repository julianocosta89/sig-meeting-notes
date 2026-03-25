"""Parse Zoom transcript HTML into plain-text speaker utterances."""

from __future__ import annotations

from bs4 import BeautifulSoup, Tag

from scraper.speaker_boundaries import (
    EMBEDDED_SPEAKER_RE as _EMBEDDED_SPEAKER_RE,
)
from scraper.speaker_boundaries import (
    SPEAKER_LIKE_RE as _SPEAKER_LIKE_RE,
)
from scraper.speaker_boundaries import (
    is_new_speaker_start as _is_new_speaker_start,
)
from scraper.speaker_boundaries import (
    should_suppress_embedded_boundary as _embedded_suppress,
)


def _split_embedded_boundaries(text: str) -> list[str]:
    """Split a raw transcript fragment at embedded speaker boundaries."""
    segments: list[str] = []
    remaining = text
    search_pos = 0

    while em := _EMBEDDED_SPEAKER_RE.search(remaining, search_pos):
        split_pos = em.start("punct") + 1
        if _embedded_suppress(em.group("punct"), em.group("name")):
            search_pos = em.end("timestamp")
            continue
        segments.append(remaining[:split_pos].rstrip())
        remaining = remaining[split_pos:].lstrip()
        search_pos = 0

    if remaining:
        segments.append(remaining)
    return segments


def _first_embedded_boundary(text: str):
    """Return the first non-suppressed embedded speaker boundary in text, if any."""
    search_pos = 0
    while em := _EMBEDDED_SPEAKER_RE.search(text, search_pos):
        if not _embedded_suppress(em.group("punct"), em.group("name")):
            return em
        search_pos = em.end("timestamp")
    return None


def parse_transcript_html(outer_html: str) -> list[str]:
    """
    Parse the outerHTML of <ul class="transcript-list"> into lines of:
        Speaker Name: utterance text

    Zoom renders each transcript utterance as an <li> containing:
      - An element with a class containing "speaker" (e.g. <span class="speaker">)
      - One or more text/paragraph elements with the spoken words

    Falls back to treating the first non-empty text node as the speaker label.

    Continuation <li>s (no speaker prefix) are merged into the previous line
    when the break is mid-sentence (previous line does not end with `.`, `?`, or `!`).
    """
    soup = BeautifulSoup(outer_html, "html.parser")
    ul = soup.find("ul")
    if ul is None:
        return []

    raw: list[tuple[bool, str]] = []
    for li in ul.find_all("li", recursive=False):
        speaker, text = _extract_speaker_and_text(li)
        if text:
            if speaker:
                raw.append((True, f"{speaker}: {text}"))
            else:
                raw.append((False, text))
    return _merge_continuation_lines(raw)


def _merge_continuation_lines(raw: list[tuple[bool, str]]) -> list[str]:
    """Merge continuation <li>s into previous line when break is mid-sentence.

    Rule: join when ALL of the following hold:
      - The line has no speaker element (has_speaker is False).
      - The previous line does not end with a sentence terminator.
      - The line does not start with a "Name Timestamp" pattern (i.e. it does
        not look like a new speaker whose speaker element was not detected).

    Speaker lines (has_speaker=True) always start a new entry.
    """
    # ASCII and full-width/CJK sentence-ending punctuation.
    sentence_ends = {".", "?", "!", "。", "？", "！"}
    if not raw:
        return []
    result = [raw[0][1]]
    for has_speaker, text in raw[1:]:
        if has_speaker:
            result.append(text)
        elif (speaker_match := _SPEAKER_LIKE_RE.match(text)) and _is_new_speaker_start(
            speaker_match
        ):
            result.extend(_split_embedded_boundaries(text))
        elif m := _first_embedded_boundary(text):
            # Split at the embedded boundary: the prefix (up to and including the
            # sentence-end punctuation) belongs to the prior turn; the remainder
            # (Name MM:SS utterance) starts a new speaker entry.
            split_pos = m.start("punct") + 1  # one past the sentence-end character
            prefix = text[:split_pos].rstrip()
            remainder = text[split_pos:].lstrip()
            if prefix:
                result[-1] += " " + prefix
            result.extend(_split_embedded_boundaries(remainder))
        elif result[-1][-1] in sentence_ends:
            result.append(text)
        else:
            result[-1] += " " + text
    return result


def _extract_speaker_and_text(li: Tag) -> tuple[str, str]:
    """Return (speaker, utterance) extracted from a single transcript <li>."""
    speaker = ""
    text_parts: list[str] = []

    for child in li.children:
        if not isinstance(child, Tag):
            # Bare text node – skip (usually whitespace)
            continue

        classes = child.get("class") or []

        if any("speaker" in cls.lower() for cls in classes):
            speaker = child.get_text(separator=" ", strip=True)
        else:
            part = child.get_text(separator=" ", strip=True)
            if part:
                text_parts.append(part)

    text = " ".join(text_parts).strip()

    # Fallback: if no speaker was detected, try splitting on newline / first element
    if not speaker and not text:
        full = li.get_text(separator="\n", strip=True)
        if "\n" in full:
            lines = [line.strip() for line in full.split("\n") if line.strip()]
            speaker = lines[0]
            text = " ".join(lines[1:])
        else:
            text = full

    return speaker, text
