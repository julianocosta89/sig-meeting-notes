"""Tests for scraper/speaker_boundaries.py — shared speaker-boundary helpers."""

from __future__ import annotations

from scraper.speaker_boundaries import (
    EMBEDDED_SPEAKER_RE,
    SPEAKER_LIKE_RE,
    SPEAKER_TS_RE,
    is_new_speaker_start,
    should_suppress_embedded_boundary,
    speaker_name_info,
)

# ---------------------------------------------------------------------------
# speaker_name_info
# ---------------------------------------------------------------------------


class TestSpeakerNameInfo:
    def test_simple_name(self):
        info = speaker_name_info("Alice")
        assert info.tokens == ("Alice",)
        assert info.bare_tokens == ("Alice",)
        assert info.first_token == "Alice"
        assert info.first_lower == "alice"
        assert not info.has_org_suffix
        assert info.first_has_upper
        assert not info.first_is_handle_like

    def test_multi_word_name(self):
        info = speaker_name_info("Alice Smith")
        assert info.bare_tokens == ("Alice", "Smith")
        assert info.first_lower == "alice"
        assert not info.has_org_suffix

    def test_bracket_org_suffix(self):
        info = speaker_name_info("Marc Alff [MySQL]")
        assert info.bare_tokens == ("Marc", "Alff")
        assert info.has_org_suffix

    def test_pipe_org_suffix(self):
        info = speaker_name_info("Giuseppe Ognibene | Coralogix")
        assert info.bare_tokens == ("Giuseppe", "Ognibene")
        assert info.has_org_suffix

    def test_paren_org_suffix(self):
        info = speaker_name_info("Alice Fox (Elastic)")
        assert info.bare_tokens == ("Alice", "Fox")
        assert info.has_org_suffix

    def test_email_handle(self):
        info = speaker_name_info("lciukaj@splunk.com")
        assert info.first_token == "lciukaj@splunk.com"
        assert not info.first_has_upper
        assert info.first_is_handle_like  # contains '@'

    def test_at_handle(self):
        info = speaker_name_info("@arielvalentin")
        assert info.first_token == "@arielvalentin"
        assert info.first_is_handle_like  # contains '@'

    def test_hyphenated_name(self):
        info = speaker_name_info("Chris Lightfoot-Wild")
        assert info.bare_tokens == ("Chris", "Lightfoot-Wild")
        assert info.first_has_upper
        assert not info.first_is_handle_like

    def test_dotted_handle(self):
        info = speaker_name_info("foo.bar")
        assert info.first_token == "foo.bar"
        assert info.first_is_handle_like  # contains '.'

    def test_sentence_starter_first_lower(self):
        info = speaker_name_info("So Koide")
        assert info.first_lower == "so"
        assert info.first_has_upper  # 'S' is uppercase

    def test_empty_string(self):
        info = speaker_name_info("")
        assert info.tokens == ()
        assert info.bare_tokens == ()
        assert info.first_token == ""
        assert not info.first_has_upper
        assert not info.first_is_handle_like


# ---------------------------------------------------------------------------
# SPEAKER_LIKE_RE and SPEAKER_TS_RE
# ---------------------------------------------------------------------------


class TestSpeakerLikeRe:
    def test_simple_name_with_timestamp(self):
        m = SPEAKER_LIKE_RE.match("Alice 10:05 hello")
        assert m is not None
        assert m.group("name") == "Alice"
        assert m.group("timestamp") == "10:05"

    def test_multi_word_name(self):
        m = SPEAKER_LIKE_RE.match("Alice Smith 10:05 hello")
        assert m is not None
        assert m.group("name") == "Alice Smith"

    def test_hyphenated_name(self):
        m = SPEAKER_LIKE_RE.match("Chris Lightfoot-Wild 10:45 hello")
        assert m is not None
        assert m.group("name") == "Chris Lightfoot-Wild"

    def test_email_handle(self):
        m = SPEAKER_LIKE_RE.match("lciukaj@splunk.com 20:59 hello")
        assert m is not None
        assert m.group("name") == "lciukaj@splunk.com"

    def test_hhmmss_timestamp(self):
        m = SPEAKER_LIKE_RE.match("Alice 00:10:05 hello")
        assert m is not None
        assert m.group("timestamp") == "00:10:05"

    def test_no_match_without_timestamp(self):
        assert SPEAKER_LIKE_RE.match("Alice hello") is None

    def test_no_match_digit_start(self):
        # Lines starting with a digit (e.g. a bare timestamp) don't match
        assert SPEAKER_LIKE_RE.match("10:05 hello") is None

    def test_no_match_punctuation_start(self):
        # Lines starting with punctuation don't match
        assert SPEAKER_LIKE_RE.match("(Alice) 10:05 hello") is None

    def test_unicode_apostrophe_in_name(self):
        # Typographic apostrophe (U+2019) in device names like "Austin\u2019s iPhone"
        m = SPEAKER_LIKE_RE.match("Austin\u2019s iPhone 10:05 hello")
        assert m is not None
        assert m.group("name") == "Austin\u2019s iPhone"


class TestSpeakerTsRe:
    def test_finds_match_after_punctuation(self):
        # Non-word character before the name breaks greedy multi-token matching,
        # so only "Alice" is captured as the name.
        m = SPEAKER_TS_RE.search("… Alice 10:05 hello")
        assert m is not None
        assert m.group("name") == "Alice"

    def test_email_handle_mid_string(self):
        m = SPEAKER_TS_RE.search("Alice 10:00 done… lciukaj@splunk.com 20:59 yes")
        assert m is not None  # finds first match


class TestEmbeddedSpeakerRe:
    def test_dot_boundary(self):
        m = EMBEDDED_SPEAKER_RE.search("Alice 10:00 done. Bob 10:05 hello")
        assert m is not None
        assert m.group("punct") == "."
        assert m.group("name") == "Bob"

    def test_ellipsis_boundary(self):
        m = EMBEDDED_SPEAKER_RE.search("Alice 10:00 trailing… Bob 10:05 hello")
        assert m is not None
        assert m.group("punct") == "…"

    def test_comma_boundary(self):
        m = EMBEDDED_SPEAKER_RE.search("Alice 10:00 done, Bob Smith 10:05 hello")
        assert m is not None
        assert m.group("punct") == ","

    def test_no_match_without_preceding_punct(self):
        m = EMBEDDED_SPEAKER_RE.search("Alice 10:00 then Bob 10:05 hello")
        assert m is None


# ---------------------------------------------------------------------------
# is_new_speaker_start
# ---------------------------------------------------------------------------


class TestIsNewSpeakerStart:
    def _match(self, text: str):
        return SPEAKER_LIKE_RE.match(text)

    def test_plain_name_is_new_speaker(self):
        assert is_new_speaker_start(self._match("Alice 10:05 hello"))

    def test_multi_word_name_is_new_speaker(self):
        assert is_new_speaker_start(self._match("Alice Smith 10:05 hello"))

    def test_hyphenated_name_is_new_speaker(self):
        assert is_new_speaker_start(self._match("Chris Lightfoot-Wild 10:45 hi"))

    def test_email_handle_is_new_speaker(self):
        assert is_new_speaker_start(self._match("lciukaj@splunk.com 20:59 yes"))

    def test_sentence_starter_single_token_is_not_new_speaker(self):
        # "So" alone — sentence-starter, no second token → not a speaker
        assert not is_new_speaker_start(self._match("So 10:05 far so good"))

    def test_sentence_starter_titlecase_second_token_is_new_speaker(self):
        # "So Koide" — "So" is a sentence-starter but "Koide" is title-case → real name
        assert is_new_speaker_start(self._match("So Koide 10:05 hello"))

    def test_sentence_starter_lowercase_second_token_is_not_new_speaker(self):
        # "so far" — both tokens present but "far" is lowercase → continuation
        assert not is_new_speaker_start(self._match("So far 10:05 along"))

    def test_article_a_single_token_not_new_speaker(self):
        assert not is_new_speaker_start(self._match("a 10:05 reminder"))


# ---------------------------------------------------------------------------
# should_suppress_embedded_boundary
# ---------------------------------------------------------------------------


class TestShouldSuppressEmbeddedBoundary:
    # -- ellipsis ("…") -------------------------------------------------------

    def test_ellipsis_plain_name_not_suppressed(self):
        assert not should_suppress_embedded_boundary("…", "Alice")

    def test_ellipsis_sentence_starter_single_token_suppressed(self):
        assert should_suppress_embedded_boundary("…", "so")

    def test_ellipsis_sentence_starter_titlecase_second_not_suppressed(self):
        # "So Koide" — second token is title-case → real speaker
        assert not should_suppress_embedded_boundary("…", "So Koide")

    def test_ellipsis_sentence_starter_lowercase_second_suppressed(self):
        assert should_suppress_embedded_boundary("…", "so far")

    def test_ellipsis_email_handle_not_suppressed(self):
        assert not should_suppress_embedded_boundary("…", "lciukaj@splunk.com")

    # -- comma (",") ----------------------------------------------------------

    def test_comma_sentence_starter_suppressed(self):
        assert should_suppress_embedded_boundary(",", "and")

    def test_comma_capitalized_single_token_not_suppressed(self):
        # Capitalized single-token names like "Sergey" are valid hand-offs after ","
        assert not should_suppress_embedded_boundary(",", "Sergey")

    def test_comma_lowercase_single_token_suppressed(self):
        assert should_suppress_embedded_boundary(",", "probably")

    def test_comma_email_handle_not_suppressed(self):
        assert not should_suppress_embedded_boundary(",", "lciukaj@splunk.com")

    def test_comma_multi_word_titlecase_not_suppressed(self):
        assert not should_suppress_embedded_boundary(",", "Kemal Akkoyun")

    def test_comma_multi_word_lowercase_second_suppressed(self):
        assert should_suppress_embedded_boundary(",", "Alice fox")

    # -- period (".") ---------------------------------------------------------

    def test_dot_plain_long_name_not_suppressed(self):
        assert not should_suppress_embedded_boundary(".", "Alice")

    def test_dot_short_name_suppressed(self):
        # Single-token name shorter than 3 chars (not a handle) is suppressed
        assert should_suppress_embedded_boundary(".", "to")

    def test_dot_sentence_starter_suppressed(self):
        assert should_suppress_embedded_boundary(".", "so")

    def test_dot_email_handle_not_suppressed(self):
        # Email handles bypass the length guard
        assert not should_suppress_embedded_boundary(".", "lciukaj@splunk.com")

    def test_dot_multi_word_titlecase_not_suppressed(self):
        assert not should_suppress_embedded_boundary(".", "Alice Smith")

    def test_dot_multi_word_lowercase_second_suppressed(self):
        assert should_suppress_embedded_boundary(".", "Alice fox")

    # -- question/exclamation mark ("?", "!") ---------------------------------

    def test_question_plain_name_not_suppressed(self):
        assert not should_suppress_embedded_boundary("?", "Alice")

    def test_question_sentence_starter_suppressed(self):
        assert should_suppress_embedded_boundary("?", "so")

    def test_exclamation_plain_name_not_suppressed(self):
        assert not should_suppress_embedded_boundary("!", "Bob")

    def test_exclamation_sentence_starter_suppressed(self):
        assert should_suppress_embedded_boundary("!", "and")

    def test_question_multi_word_titlecase_not_suppressed(self):
        assert not should_suppress_embedded_boundary("?", "Alice Smith")

    def test_question_multi_word_lowercase_second_suppressed(self):
        assert should_suppress_embedded_boundary("?", "Alice fox")

    # -- org suffix -----------------------------------------------------------

    def test_single_token_with_org_suffix_not_sentence_starter_not_suppressed(self):
        # "Q | OpenAI" — single bare token "Q" with org suffix, not a sentence-starter
        assert not should_suppress_embedded_boundary(".", "Q | OpenAI")

    def test_single_token_with_org_suffix_sentence_starter_suppressed(self):
        assert should_suppress_embedded_boundary(".", "so | OpenAI")
