"""Shared speaker-boundary detection helpers for transcript parsing and repair."""

from __future__ import annotations

import re
from dataclasses import dataclass

TIMESTAMP_RE = r"\d{1,2}:\d{2}(?::\d{2})?"

# Supported speaker token shapes:
# - regular Unicode name words, including apostrophes/hyphens/dots
# - email-style handles, e.g. lciukaj@splunk.com
# - @handles, e.g. @arielvalentin
_NAME_TOKEN_RE = (
    r"(?:"
    r"@[\w.+-]+"
    r"|[\w.+-]+@[\w.-]+(?:\.[\w.-]+)*"
    r"|[^\W\d_][\w'\u2019]*(?:[.-][\w'\u2019]+)*"
    r")"
)
_NAME_RE = (
    rf"{_NAME_TOKEN_RE}(?:\s+{_NAME_TOKEN_RE})*"
    r"(?:\s+\[[^\]]+\])?"
    r"(?:\s+\|[^|]*?)?"
    r"(?:\s+\([^)]+\))?"
)

SPEAKER_TS_RE = re.compile(rf"(?P<name>{_NAME_RE})\s+(?P<timestamp>{TIMESTAMP_RE})\s+")
SPEAKER_LIKE_RE = re.compile(rf"^(?P<name>{_NAME_RE})\s+(?P<timestamp>{TIMESTAMP_RE})\s+")
EMBEDDED_SPEAKER_RE = re.compile(
    rf"(?P<punct>[.?!…。？！,])\s+(?P<name>{_NAME_RE})\s+(?P<timestamp>{TIMESTAMP_RE})\s"
)

TURN_ENDS = frozenset(".?!…。？！")

SENTENCE_STARTERS = frozenset(
    {
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
        "i",
        "we",
        "he",
        "she",
        "it",
        "they",
        "so",
        "but",
        "and",
        "or",
        "if",
        "as",
        "that",
        "this",
        "a",
        "ok",
        "okay",
        "yes",
        "no",
    }
)


@dataclass(frozen=True)
class SpeakerNameInfo:
    tokens: tuple[str, ...]
    bare_tokens: tuple[str, ...]
    first_token: str
    first_lower: str
    has_org_suffix: bool
    first_has_upper: bool
    first_is_handle_like: bool


def _first_alpha(token: str) -> str:
    for char in token:
        if char.isalpha():
            return char
    return ""


def _is_titleish(token: str) -> bool:
    first_alpha = _first_alpha(token)
    return bool(first_alpha) and not first_alpha.islower()


def speaker_name_info(name_text: str) -> SpeakerNameInfo:
    """Return normalized metadata for a matched speaker-name fragment."""

    tokens = tuple(name_text.split())
    bare_tokens: list[str] = []
    for token in tokens:
        if not token or token[0] in {"[", "|", "("}:
            break
        bare_tokens.append(token)

    first_token = bare_tokens[0] if bare_tokens else ""
    first_alpha = _first_alpha(first_token)
    return SpeakerNameInfo(
        tokens=tokens,
        bare_tokens=tuple(bare_tokens),
        first_token=first_token,
        first_lower=first_token.lower(),
        has_org_suffix=len(bare_tokens) < len(tokens),
        first_has_upper=bool(first_alpha) and first_alpha.isupper(),
        first_is_handle_like=any(char in first_token for char in ".@-"),
    )


def is_new_speaker_start(match: re.Match[str]) -> bool:
    """Return True when a line-start Name+Timestamp match should open a new turn."""

    info = speaker_name_info(match.group("name"))
    if info.first_lower not in SENTENCE_STARTERS:
        return True
    if len(info.bare_tokens) < 2:
        return False
    return not any(not _is_titleish(token) for token in info.bare_tokens[1:])


def should_suppress_embedded_boundary(punct: str, name_text: str) -> bool:
    """Return True when an embedded Name+Timestamp match is sentence text, not a hand-off."""

    info = speaker_name_info(name_text)

    if punct == "…":
        if info.first_lower not in SENTENCE_STARTERS:
            return False
        if len(info.bare_tokens) < 2:
            return True
        return any(not _is_titleish(token) for token in info.bare_tokens[1:])

    if punct == ",":
        if info.first_lower in SENTENCE_STARTERS:
            return True
        if len(info.bare_tokens) > 1:
            return any(not _is_titleish(token) for token in info.bare_tokens[1:])
        return not (info.first_has_upper or info.first_is_handle_like)

    if len(info.bare_tokens) > 1:
        return any(not _is_titleish(token) for token in info.bare_tokens[1:])

    if info.has_org_suffix:
        return info.first_lower in SENTENCE_STARTERS

    if punct in {".", "。"}:
        if info.first_is_handle_like:
            return info.first_lower in SENTENCE_STARTERS
        return len(info.first_lower) < 3 or info.first_lower in SENTENCE_STARTERS

    return info.first_lower in SENTENCE_STARTERS
