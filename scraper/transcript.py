"""Parse Zoom transcript HTML into plain-text speaker utterances."""

from __future__ import annotations

import re

from bs4 import BeautifulSoup, Tag

# Pattern that identifies a continuation line that actually starts a new speaker.
# Zoom's HTML often wraps each <li> in a container div with no "speaker" class,
# so _extract_speaker_and_text cannot detect the speaker and marks the whole line
# as has_speaker=False.  Without this guard, any line following a "…"-terminated
# utterance would be merged regardless of whether it belongs to a different speaker.
#
# Matches display-name variants followed by a timestamp, e.g.:
#   "Name MM:SS "                      — single-word name
#   "First Last MM:SS "                — multi-word name
#   "Donal O'Sullivan MM:SS "          — apostrophe in name token
#   "First Last [Org] MM:SS "          — bracket org tag
#   "First Last | Org MM:SS "          — pipe-separated org
#   "First Last (Org) MM:SS "          — parenthesised org
#   "Q MM:SS "                         — single-character name/initial
# [^\W\d_] matches any Unicode letter (ASCII, accented, CJK, etc.) without
# requiring an ASCII uppercase initial, so names like Élodie or 杉本浩平 are
# recognised.  [\w']* (not +) allows single-character tokens.  The required
# timestamp keeps false positives low.
_SPEAKER_LIKE_RE = re.compile(
    r"^[^\W\d_][\w']*(?:\s+[^\W\d_][\w']*)*"  # name tokens (any Unicode letter, apostrophes ok)
    r"(?:\s+\[[^\]]+\])?"  # optional [Org] bracket tag
    r"(?:\s+\|[^|]*?)?"  # optional | Org pipe suffix
    r"(?:\s+\([^)]+\))?"  # optional (Org) paren suffix
    r"\s+\d{1,2}:\d{2}\s+"  # timestamp
)

# Companion pattern (no ^ anchor) that detects a speaker-start embedded
# inside a continuation line, e.g. "Yeah, so… Andrej 03:22 utterance".
# The preceding sentence-end character keeps false positives low.
_EMBEDDED_SPEAKER_RE = re.compile(
    r"[.?!…。？！]\s*"  # sentence-end punctuation immediately before
    r"[^\W\d_][\w']*(?:\s+[^\W\d_][\w']*)*"  # name tokens
    r"(?:\s+\[[^\]]+\])?"  # optional [Org]
    r"(?:\s+\|[^|]*?)?"  # optional | Org
    r"(?:\s+\([^)]+\))?"  # optional (Org)
    r"\s+\d{1,2}:\d{2}\s"  # timestamp
)


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
        if (
            has_speaker
            or _SPEAKER_LIKE_RE.match(text)
            or _EMBEDDED_SPEAKER_RE.search(text)
            or result[-1][-1] in sentence_ends
        ):
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
