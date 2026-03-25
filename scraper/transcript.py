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
    r"\s+\d{1,2}:\d{2}(?::\d{2})?\s+"  # timestamp (MM:SS or HH:MM:SS)
)

# Companion pattern (no ^ anchor) that detects a speaker-start embedded
# inside a continuation line, e.g. "Yeah, so… Andrej 03:22 utterance".
# The preceding sentence-end character keeps false positives low.
# Common English words that can appear at the start of a sentence and superficially
# match the Name+Timestamp pattern but are NOT speaker names.  When a continuation
# line starts with one of these words (case-insensitive), _SPEAKER_LIKE_RE's match
# is treated as a regular continuation rather than a new-speaker boundary.
_SENTENCE_STARTERS = frozenset(
    {
        # Temporal prepositions / adverbs
        "at",
        "by",
        "on",
        "in",
        "for",
        "from",
        "to",
        "since",
        "until",
        "today",
        "tomorrow",
        "now",
        "then",
        "after",
        "before",
        # Pronouns
        "i",
        "we",
        "he",
        "she",
        "it",
        "they",
        # Conjunctions / discourse markers
        "so",
        "but",
        "and",
        "or",
        "if",
        "as",
        "that",
        "this",
        # Articles
        "a",
        # Acknowledgements
        "ok",
        "okay",
        "yes",
        "no",
    }
)


def _is_new_speaker_start(text: str) -> bool:
    """Return True when text (already matching _SPEAKER_LIKE_RE) starts a new-speaker turn.

    Rejects common sentence-starter words unless the name is multi-token and
    all non-first bare name tokens are title-cased.  This distinguishes real
    multi-word display names like "So Koide 10:05" (first token "So" is a
    sentence-starter, but "Koide" starts uppercase → new speaker) from
    sentence continuations like "So far 10:05" ("far" starts lowercase →
    continuation).
    """
    tokens = text.split()
    first_lower = tokens[0].lower() if tokens else ""
    if first_lower not in _SENTENCE_STARTERS:
        return True
    # First token is a sentence-starter word; collect bare name tokens up to
    # the timestamp, stopping at org-suffix markers ('[', '|', '(') and the
    # timestamp itself.
    name_only: list[str] = []
    for t in tokens:
        if not t or t[0] in {"[", "|", "("}:
            break
        if re.match(r"\d{1,2}:\d{2}(?::\d{2})?$", t):
            break
        name_only.append(t)
    if len(name_only) < 2:
        return False
    # Multi-token: accept only when every non-first bare token begins with a
    # non-lowercase letter (title-case), e.g. "So Koide" → True; "so far" → False.
    return not any(t[0].islower() for t in name_only[1:] if t and t[0].isalpha())


def _embedded_suppress(punct: str, first_lower: str, full_name_tokens: list[str]) -> bool:
    """Return True when an _EMBEDDED_SPEAKER_RE match should be suppressed.

    Prevents clock phrases, sentence-starter words, and sentence fragments
    from being mistaken for new-speaker boundaries.

    punct            — boundary character immediately before the match
    first_lower      — lowercase first word of the text after the boundary
    full_name_tokens — name tokens from _EMBEDDED_SPEAKER_RE group 1
    """
    if punct == "…":
        return first_lower in _SENTENCE_STARTERS
    if punct == ",":
        name_only: list[str] = []
        for t in full_name_tokens:
            if not t or t[0] in {"[", "|", "("}:
                break
            name_only.append(t)
        return (
            len(name_only) < 2
            or first_lower in _SENTENCE_STARTERS
            or any(t[0].islower() for t in name_only[1:] if t and t[0].isalpha())
        )
    # ".", "?", "!", "。", "？", "！"
    name_only = []
    for t in full_name_tokens:
        if not t or t[0] in {"[", "|", "("}:
            break
        name_only.append(t)
    has_org_suffix = len(name_only) < len(full_name_tokens)
    if len(name_only) > 1:
        return any(t[0].islower() for t in name_only[1:] if t[0].isalpha())
    if has_org_suffix:
        return first_lower in _SENTENCE_STARTERS
    # Pure single-token name — apply length guard after "." / "。".
    if punct in {".", "。"}:
        return len(first_lower) < 3 or first_lower in _SENTENCE_STARTERS
    return first_lower in _SENTENCE_STARTERS


_EMBEDDED_SPEAKER_RE = re.compile(
    r"[.?!…。？！,]\s+"  # sentence-end punctuation or comma followed by whitespace
    r"([^\W\d_][\w']*(?:\s+[^\W\d_][\w']*)*"  # group 1: name tokens
    r"(?:\s+\[[^\]]+\])?"  # optional [Org]
    r"(?:\s+\|[^|]*?)?"  # optional | Org
    r"(?:\s+\([^)]+\))?)"  # optional (Org) — closes group 1
    r"\s+\d{1,2}:\d{2}(?::\d{2})?\s"  # timestamp (MM:SS or HH:MM:SS)
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
        if has_speaker:
            result.append(text)
        elif _SPEAKER_LIKE_RE.match(text) and _is_new_speaker_start(text):
            remaining = text
            while em := _EMBEDDED_SPEAKER_RE.search(remaining):
                split_pos = em.start() + 1
                after = remaining[split_pos:].lstrip()
                punct = remaining[em.start()]
                first_lower = (after.split(None, 1)[0] if after else "").lower()
                full_name_tokens = em.group(1).split() if em.group(1) else []
                if not _embedded_suppress(punct, first_lower, full_name_tokens):
                    result.append(remaining[:split_pos].rstrip())
                    remaining = after
                else:
                    break
            result.append(remaining)
        elif m := _EMBEDDED_SPEAKER_RE.search(text):
            # Split at the embedded boundary: the prefix (up to and including the
            # sentence-end punctuation) belongs to the prior turn; the remainder
            # (Name MM:SS utterance) starts a new speaker entry.
            split_pos = m.start() + 1  # one past the sentence-end character
            prefix = text[:split_pos].rstrip()
            remainder = text[split_pos:].lstrip()
            first_token = remainder.split(None, 1)[0] if remainder else ""
            punct = text[m.start()]
            first_lower = first_token.lower()
            full_name_tokens = m.group(1).split() if m.group(1) else []
            suppress = _embedded_suppress(punct, first_lower, full_name_tokens)
            if suppress:
                if result[-1][-1] in sentence_ends:
                    result.append(text)
                else:
                    result[-1] += " " + text
            else:
                if prefix:
                    result[-1] += " " + prefix
                # Walk the remainder for further embedded boundaries.
                remaining = remainder
                while em2 := _EMBEDDED_SPEAKER_RE.search(remaining):
                    sp2 = em2.start() + 1
                    after2 = remaining[sp2:].lstrip()
                    p2 = remaining[em2.start()]
                    fl2 = (after2.split(None, 1)[0] if after2 else "").lower()
                    fnt2 = em2.group(1).split() if em2.group(1) else []
                    if not _embedded_suppress(p2, fl2, fnt2):
                        result.append(remaining[:sp2].rstrip())
                        remaining = after2
                    else:
                        break
                if remaining:
                    result.append(remaining)
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
