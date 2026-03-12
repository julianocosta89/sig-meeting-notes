"""Parse Zoom transcript HTML into plain-text speaker utterances."""

from __future__ import annotations

from bs4 import BeautifulSoup, Tag


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

    Rule: join when previous line does NOT end with '.', '?', or '!'.
    Speaker lines always start a new entry.
    """
    # ASCII and full-width/CJK sentence-ending punctuation.
    sentence_ends = {".", "?", "!", "。", "？", "！"}
    if not raw:
        return []
    result = [raw[0][1]]
    for has_speaker, text in raw[1:]:
        if has_speaker or result[-1][-1] in sentence_ends:
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
