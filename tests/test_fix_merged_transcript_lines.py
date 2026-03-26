"""Tests for scripts/fix_merged_transcript_lines.py — speaker-merge detection and repair."""

from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import patch

# Make the scripts/ directory importable.
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from fix_merged_transcript_lines import (  # noqa: E402
    _format_segment,
    _parse_args,
    _split_header_body,
    _valid_split_matches,
    fix_line,
    fix_transcript_file,
    main,
)

# ---------------------------------------------------------------------------
# _valid_split_matches — pattern detection
# ---------------------------------------------------------------------------


class TestValidSplitMatches:
    def test_no_match_plain_text(self):
        assert _valid_split_matches("just some text without a timestamp") == []

    def test_single_speaker_at_start(self):
        matches = _valid_split_matches("Marc Pichler 13:40 Hello there.")
        assert len(matches) == 1
        assert matches[0].start() == 0

    def test_sentence_starter_at_start_suppressed_on_non_bold_line(self):
        # By default (non-bold / orphan line), sentence-starter names at
        # position 0 are suppressed to avoid fabricating clock phrases as speakers.
        matches = _valid_split_matches("At 10:05 we begin. Bob 10:06 Hi.")
        assert len(matches) == 1
        assert matches[0].group("name") == "Bob"

    def test_sentence_starter_at_start_accepted_when_known_bold(self):
        # When the caller signals the position-0 token is a known speaker
        # (e.g. the line was originally bold-formatted), starters are accepted.
        matches = _valid_split_matches(
            "Okay 10:00 Intro. Bob 10:01 Hi.", known_speaker_at_start=True
        )
        assert len(matches) == 2
        assert matches[0].group("name") == "Okay"
        assert matches[1].group("name") == "Bob"

    def test_merged_two_speakers(self):
        pre = "Marc Pichler 13:40 asking… Marylia Gutierrez 13:43 I'll just ask"
        matches = _valid_split_matches(pre)
        assert len(matches) == 2
        assert matches[0].start() == 0
        assert matches[1].group(1) == "Marylia Gutierrez"

    def test_apostrophe_name_detected(self):
        pre = "Alice Fox 10:00 Over to Donal… Donal O'Sullivan 10:05 Thanks."
        matches = _valid_split_matches(pre)
        assert len(matches) == 2
        assert matches[1].group(1) == "Donal O'Sullivan"

    def test_hyphenated_name_detected(self):
        pre = "Sergey 10:27 It can drift… Chris Lightfoot-Wild 10:45 It reads like if…"
        matches = _valid_split_matches(pre)
        assert len(matches) == 2
        assert matches[1].group(1) == "Chris Lightfoot-Wild"

    def test_bracket_org_name_detected(self):
        pre = "Alice Fox 10:00 Over to Marc… Marc Alff [MySQL] 10:03 Happy."
        matches = _valid_split_matches(pre)
        assert len(matches) == 2
        assert matches[1].group(1) == "Marc Alff [MySQL]"

    def test_pipe_org_name_detected(self):
        pre = "Alice Fox 10:00 Over to Giuseppe… Giuseppe Ognibene | Coralogix 10:07 Sure."
        matches = _valid_split_matches(pre)
        assert len(matches) == 2
        assert matches[1].group(1) == "Giuseppe Ognibene | Coralogix"

    def test_no_match_when_not_preceded_by_sentence_end(self):
        # A non-speaker clock phrase without sentence-ending punctuation is not a split point.
        pre = "Alice 10:00 saying something, probably 10:05 continues"
        matches = _valid_split_matches(pre)
        # Only the first match at position 0 is valid.
        assert all(m.start() == 0 for m in matches)

    def test_email_domain_suffix_not_a_split_point(self):
        # "com" after "splunk." must not be treated as a speaker name.
        pre = "Alice 10:00 email me at lciukaj@splunk.com 20:59 and I'll follow up."
        matches = _valid_split_matches(pre)
        assert len(matches) == 1
        assert matches[0].start() == 0

    def test_dotted_hostname_suffix_not_a_split_point(self):
        # "com" after "sub.domain." must not be treated as a speaker name.
        pre = "Alice 10:00 see sub.domain.com 20:59 for details."
        matches = _valid_split_matches(pre)
        assert len(matches) == 1
        assert matches[0].start() == 0

    def test_short_name_after_period_not_a_split_point(self):
        # "At" (2 chars) after '.' must not be treated as a speaker (preposition guard).
        pre = "Alice 10:00 We can restart. At 10:05 we begin."
        matches = _valid_split_matches(pre)
        assert len(matches) == 1
        assert matches[0].start() == 0

    def test_short_name_after_ellipsis_is_a_split_point(self):
        # "Q" (1 char) after '…' IS a valid split (single-char speaker handle).
        pre = "Alice Fox 10:00 over… Q 10:05 Thanks."
        matches = _valid_split_matches(pre)
        assert len(matches) == 2
        assert matches[1].group(1) == "Q"

    def test_email_stem_after_period_not_a_split_point(self):
        # 'alice@example.' ends with '.'; stem contains '@' → skip (line 153).
        pre = "Alice 10:00 email alice@example. Bob 10:05 Hello."
        matches = _valid_split_matches(pre)
        assert len(matches) == 1
        assert matches[0].start() == 0

    def test_dotted_stem_after_period_not_a_split_point(self):
        # 'config.example.' ends with '.'; stem contains '.' → skip (line 153).
        pre = "Alice 10:00 see config.example. Bob 10:05 Hello."
        matches = _valid_split_matches(pre)
        assert len(matches) == 1
        assert matches[0].start() == 0

    def test_bracket_org_name_after_period_is_split_point(self):
        # '[MySQL]' causes break in name_tokens loop (line 162).
        pre = "Alice 10:00 Done. Marc Alff [MySQL] 10:03 Happy."
        matches = _valid_split_matches(pre)
        assert len(matches) == 2
        assert "[MySQL]" in matches[1].group(1)

    def test_multi_token_lowercase_second_word_after_period_not_a_split_point(self):
        # 'far' is lowercase → suppressed (lines 166-167).
        pre = "Alice 10:00 Done. So far 10:05 along."
        matches = _valid_split_matches(pre)
        assert len(matches) == 1
        assert matches[0].start() == 0

    def test_sentence_starter_with_org_suffix_after_period_not_a_split_point(self):
        # 'So' is a sentence-starter; single-token + org suffix (lines 171-172).
        pre = "Alice 10:00 Done. So | Org 10:05 Hello."
        matches = _valid_split_matches(pre)
        assert len(matches) == 1
        assert matches[0].start() == 0

    def test_sentence_starter_after_ellipsis_not_a_split_point(self):
        # 'at' is in _SENTENCE_STARTERS → suppressed after '…' (line 181).
        pre = "Alice 10:00 passing… at 10:05 we begin."
        matches = _valid_split_matches(pre)
        assert len(matches) == 1
        assert matches[0].start() == 0

    def test_last_first_comma_name_with_known_speaker_not_a_split_point(self):
        # "Last, First" format at the start of a known-speaker bold line: the comma
        # is part of the speaker label, not a split boundary.
        pre = "Yazdankhah, Mani 01:03:09 Hello everyone."
        matches = _valid_split_matches(pre, known_speaker_at_start=True)
        assert len(matches) == 0

    def test_last_first_comma_name_unknown_speaker_is_split_point(self):
        # Without known_speaker_at_start, the comma-preceded "Mani" is still
        # treated as a potential split (behaviour unchanged for unknown context).
        pre = "Yazdankhah, Mani 01:03:09 Hello everyone."
        matches = _valid_split_matches(pre, known_speaker_at_start=False)
        assert len(matches) == 1
        assert matches[0].group(1) == "Mani"

    def test_comma_before_multi_token_speaker_is_split_point(self):
        # Multi-word name after ',' → valid split.
        pre = "Alice 10:00 started, Kemal Akkoyun 31:30 Happy to be here."
        matches = _valid_split_matches(pre)
        assert len(matches) == 2
        assert matches[1].group(1) == "Kemal Akkoyun"

    def test_comma_before_capitalized_single_token_speaker_is_split_point(self):
        pre = "Bob Strecansky 19:36 Yeah, Sergey 19:38 I mean, it sounds right."
        matches = _valid_split_matches(pre)
        assert len(matches) == 2
        assert matches[1].group(1) == "Sergey"

    def test_comma_before_single_token_not_a_split_point(self):
        # Single-word name after ',' → not split to avoid false positives.
        pre = "Alice 10:00 Let me check, probably 30:00 we can start."
        matches = _valid_split_matches(pre)
        assert len(matches) == 1
        assert matches[0].start() == 0

    def test_comma_before_sentence_starter_not_a_split_point(self):
        # Sentence-starter word after ',' → not split even in multi-token form.
        pre = "Alice 10:00 hand over, and Bob Smith 10:05 Thanks."
        matches = _valid_split_matches(pre)
        assert len(matches) == 1
        assert matches[0].start() == 0

    def test_title_cased_multi_token_after_ellipsis_is_split_point(self):
        # "So Koide" — "So" is a starter but "Koide" is title-cased → valid split.
        pre = "Alice 10:00 passing… So Koide 10:05 Thanks."
        matches = _valid_split_matches(pre)
        assert len(matches) == 2
        assert matches[1].group(1) == "So Koide"

    def test_email_handle_after_ellipsis_is_split_point(self):
        pre = "Tiffany Hrabusa 20:55 I haven't looked at it yet… lciukaj@splunk.com 20:59 Yeah."
        matches = _valid_split_matches(pre)
        assert len(matches) == 2
        assert matches[1].group(1) == "lciukaj@splunk.com"

    def test_suppressed_match_does_not_block_later_valid_match(self):
        pre = "Bob 10:00 ... At 10:05 we begin. Carol 10:06 Thanks."
        matches = _valid_split_matches(pre)
        assert len(matches) == 2
        assert matches[0].group(1) == "Bob"
        assert matches[1].group(1) == "Carol"

    def test_article_a_after_ellipsis_not_a_split_point(self):
        # 'a' (English article) is in _SENTENCE_STARTERS → suppressed after '…'.
        pre = "Alice 10:00 passing… a 10:05 reminder was sent."
        matches = _valid_split_matches(pre)
        assert len(matches) == 1
        assert matches[0].start() == 0

    def test_speaker_after_question_mark_is_split_point(self):
        # Single token, not a sentence-starter, after '?' → valid (lines 186-204).
        pre = "Alice 10:00 Really? Bob 10:05 Thanks."
        matches = _valid_split_matches(pre)
        assert len(matches) == 2
        assert matches[1].group(1) == "Bob"

    def test_multi_token_title_case_after_question_mark_is_split_point(self):
        # Multi-token, all title-case after '?' → valid (lines 194-195, no suppress).
        pre = "Alice 10:00 Really? Bob Smith 10:05 Thanks."
        matches = _valid_split_matches(pre)
        assert len(matches) == 2
        assert matches[1].group(1) == "Bob Smith"

    def test_multi_token_lowercase_after_question_mark_not_a_split_point(self):
        # 'far' is lowercase after '?' → suppressed (lines 195-196).
        pre = "Alice 10:00 Really? So far 10:05 along."
        matches = _valid_split_matches(pre)
        assert len(matches) == 1

    def test_bracket_org_name_after_question_mark_is_split_point(self):
        # '[MySQL]' breaks the loop (line 191); single bare token + org, not a starter.
        pre = "Alice 10:00 Really? Marc [MySQL] 10:05 Thanks."
        matches = _valid_split_matches(pre)
        assert len(matches) == 2
        assert "[MySQL]" in matches[1].group(1)

    def test_sentence_starter_with_org_after_question_mark_not_a_split_point(self):
        # 'So' is a starter; single bare token + org suffix (lines 197-199).
        pre = "Alice 10:00 Really? So | Org 10:05 Hello."
        matches = _valid_split_matches(pre)
        assert len(matches) == 1

    def test_sentence_starter_after_exclamation_not_a_split_point(self):
        # 'So' is in _SENTENCE_STARTERS; single token, no org (lines 200-203).
        pre = "Alice 10:00 Done! So 10:05 we continue."
        matches = _valid_split_matches(pre)
        assert len(matches) == 1

    def test_dotted_handle_not_a_split_point(self):
        # The dotted handle itself is a valid start-of-line speaker, but the inner
        # ".jomard 44:07" fragment must not become an extra split point.
        pre = "mackenzie.jomard 44:07 Just checking in."
        matches = _valid_split_matches(pre)
        assert len(matches) == 1
        assert matches[0].start() == 0

    def test_dot_prefixed_fragment_after_sentence_end_is_not_treated_as_speaker(self):
        pre = "Alice 10:00 Done. .jomard 44:07 Hi. Bob 44:10 Hi."
        matches = _valid_split_matches(pre)
        assert len(matches) == 2
        assert matches[0].group(1) == "Alice"
        assert matches[1].group(1) == "Bob"

    def test_sentence_ending_dot_still_valid(self):
        # A genuine sentence end with '.' must still trigger a split.
        pre = "Dan Gomez 10:28 so… Andrej 10:32 Oh. Bob 10:40 Thanks."
        matches = _valid_split_matches(pre)
        assert len(matches) == 3

    def test_unicode_name_detected(self):
        pre = "Alice 08:07 Let me just… Juraci Paixão Kröhling 08:13 I mean…"
        matches = _valid_split_matches(pre)
        assert len(matches) == 2
        assert "Juraci" in matches[1].group(1)

    def test_single_word_name_detected(self):
        pre = "Dan Gomez 10:28 so… Andrej 10:32 Oh, okay."
        matches = _valid_split_matches(pre)
        assert len(matches) == 2
        assert matches[1].group(1) == "Andrej"

    def test_cjk_name_detected(self):
        pre = "Alice Fox 10:00 Over to our next speaker… 杉本浩平 10:05 よろしく。"
        matches = _valid_split_matches(pre)
        assert len(matches) == 2
        assert "杉本浩平" in matches[1].group(1)

    def test_cjk_full_width_punctuation_is_valid_turn_end(self):
        # 。？！ must trigger a split just like their ASCII equivalents
        pre = "Alice 10:00 こんにちは。 Bob 10:05 Thanks."
        matches = _valid_split_matches(pre)
        assert len(matches) == 2
        assert matches[1].group(1) == "Bob"

    def test_accented_uppercase_name_detected(self):
        pre = "Alice Fox 10:00 Thanks, over to Élodie… Élodie Dupont 10:05 Merci."
        matches = _valid_split_matches(pre)
        assert len(matches) == 2
        assert "Élodie" in matches[1].group(1)

    def test_single_char_name_detected(self):
        pre = "Alice Fox 10:00 Passing to Q… Q 10:05 Thanks."
        matches = _valid_split_matches(pre)
        assert len(matches) == 2
        assert matches[1].group(1) == "Q"

    def test_single_char_unicode_name_detected(self):
        pre = "Alice Fox 10:00 Over to É… É 10:05 Merci."
        matches = _valid_split_matches(pre)
        assert len(matches) == 2
        assert matches[1].group(1) == "É"


# ---------------------------------------------------------------------------
# fix_line — no-op on clean lines
# ---------------------------------------------------------------------------


class TestFixLineNoOp:
    def test_clean_line_unchanged(self):
        line = "**Marc Pichler** 13:40 Hello there."
        assert fix_line(line) == [line]

    def test_plain_text_unchanged(self):
        line = "just some continuation text"
        assert fix_line(line) == [line]

    def test_empty_line_unchanged(self):
        assert fix_line("") == [""]


# ---------------------------------------------------------------------------
# fix_line — merges detected and split
# ---------------------------------------------------------------------------


class TestFixLineSplit:
    def test_two_speaker_merge_split(self):
        line = "**Marc Pichler** 13:40 asking… Marylia Gutierrez 13:43 I'll ask."
        result = fix_line(line)
        assert len(result) == 2
        assert result[0] == "**Marc Pichler** 13:40 asking…"
        assert result[1] == "**Marylia Gutierrez** 13:43 I'll ask."

    def test_apostrophe_speaker_split(self):
        line = "**Alice Fox** 10:00 Over to Donal… Donal O'Sullivan 10:05 Thanks."
        result = fix_line(line)
        assert len(result) == 2
        assert "O'Sullivan" in result[1]

    def test_bracket_org_speaker_split(self):
        line = "**Alice Fox** 10:00 Over to Marc… Marc Alff [MySQL] 10:03 Happy."
        result = fix_line(line)
        assert len(result) == 2
        assert "[MySQL]" in result[1]

    def test_pipe_org_speaker_split(self):
        line = "**Alice Fox** 10:00 Over… Giuseppe Ognibene | Coralogix 10:07 Sure."
        result = fix_line(line)
        assert len(result) == 2
        assert "Coralogix" in result[1]

    def test_hyphenated_speaker_split(self):
        line = (
            "**Sergey** 10:27 It can drift over time… Chris Lightfoot-Wild 10:45 It reads like if…"
        )
        result = fix_line(line)
        assert len(result) == 2
        assert result[1] == "**Chris Lightfoot-Wild** 10:45 It reads like if…"

    def test_email_handle_speaker_split(self):
        line = "**Tiffany Hrabusa** 20:55 I haven't looked at it yet, so… lciukaj@splunk.com 20:59 Yeah."  # noqa: E501
        result = fix_line(line)
        assert len(result) == 2
        assert result[1] == "**lciukaj@splunk.com** 20:59 Yeah."

    def test_three_speaker_merge_split(self):
        line = "**Alice Fox** 01:00 first… Bob Smith 02:00 second… Carol Wang 03:00 third."
        result = fix_line(line)
        assert len(result) == 3
        assert "Alice Fox" in result[0]
        assert "Bob Smith" in result[1]
        assert "Carol Wang" in result[2]

    def test_prefix_text_before_first_speaker(self):
        """Text before the first speaker-like match is split into a separate line."""
        line = "continuation text. Alice 10:00 Hello world."
        result = fix_line(line)
        assert len(result) == 2
        assert result[0] == "continuation text."
        assert result[1] == "**Alice** 10:00 Hello world."

    def test_sentence_starter_display_name_bold_preserved(self):
        # Speakers like "Okay", "No", "Yes" are in _SENTENCE_STARTERS but are
        # valid display names — they must keep their bold formatting after repair.
        line = "**Okay** 10:00 Intro. Bob 10:01 Hi."
        assert fix_line(line) == [
            "**Okay** 10:00 Intro.",
            "**Bob** 10:01 Hi.",
        ]

    def test_dotted_handle_line_not_corrupted(self):
        """A single-speaker line with a dotted handle is returned unchanged."""
        line = "**mackenzie.jomard** 44:07 Just checking in."
        assert fix_line(line) == [line]

    def test_hh_mm_ss_timestamp_detected(self):
        """A merged line with HH:MM:SS timestamps is split correctly."""
        line = "**Alice Fox** 00:12:55 first… Bob Smith 00:13:34 second."
        result = fix_line(line)
        assert len(result) == 2
        assert "Alice Fox" in result[0]
        assert "Bob Smith" in result[1]
        assert "00:13:34" in result[1]

    def test_suppressed_mid_line_match_does_not_block_later_split(self):
        line = "**Bob** 10:00 ... At 10:05 we begin. Carol 10:06 Thanks."
        assert fix_line(line) == [
            "**Bob** 10:00 ... At 10:05 we begin.",
            "**Carol** 10:06 Thanks.",
        ]

    def test_last_first_comma_name_not_corrupted(self):
        # "Last, First" bold-formatted speaker line must not be split at the comma.
        line = "**Yazdankhah, Mani** 01:03:09 Hello everyone."
        assert fix_line(line) == [line]

    def test_last_first_comma_name_split_at_later_boundary(self):
        # "Last, First" speaker followed by a merged second speaker is split correctly.
        line = "**Yazdankhah, Mani** 01:03:09 Intro. Alice 02:00:00 Thanks."
        result = fix_line(line)
        assert result == [
            "**Yazdankhah, Mani** 01:03:09 Intro.",
            "**Alice** 02:00:00 Thanks.",
        ]

    def test_comma_before_capitalized_single_token_speaker_split(self):
        line = "**Bob Strecansky** 19:36 Yeah, Sergey 19:38 I mean, it sounds right."
        result = fix_line(line)
        assert result == [
            "**Bob Strecansky** 19:36 Yeah,",
            "**Sergey** 19:38 I mean, it sounds right.",
        ]

    def test_comma_before_email_handle_speaker_split(self):
        line = (
            "**Tiffany Hrabusa** 20:55 copy edit is done, "
            "lciukaj@splunk.com 20:59 Yeah, did you have plans to discuss next steps?"
        )
        result = fix_line(line)
        assert result == [
            "**Tiffany Hrabusa** 20:55 copy edit is done,",
            "**lciukaj@splunk.com** 20:59 Yeah, did you have plans to discuss next steps?",
        ]


# ---------------------------------------------------------------------------
# _format_segment — fallback branch
# ---------------------------------------------------------------------------


class TestFormatSegment:
    def test_valid_speaker_format(self):
        assert _format_segment("Alice 10:00 Hello world.") == "**Alice** 10:00 Hello world."

    def test_no_timestamp_returns_as_is(self):
        """When segment has no Name+Timestamp, return it unchanged (line 78 branch)."""
        assert _format_segment("just some continuation text.") == "just some continuation text."


# ---------------------------------------------------------------------------
# _split_header_body
# ---------------------------------------------------------------------------

_SEP = "=" * 60


class TestSplitHeaderBody:
    def test_with_separator(self):
        text = f"SIG: Test\nDate: 2026-01-01\n{_SEP}\nbody line 1\nbody line 2"
        header, body = _split_header_body(text)
        assert header == f"SIG: Test\nDate: 2026-01-01\n{_SEP}"
        assert body == ["", "body line 1", "body line 2"]

    def test_without_separator(self):
        text = "no separator here\njust lines"
        header, body = _split_header_body(text)
        assert header == ""
        assert body == ["no separator here", "just lines"]


# ---------------------------------------------------------------------------
# fix_transcript_file
# ---------------------------------------------------------------------------


class TestFixTranscriptFile:
    def test_clean_file_no_changes(self, tmp_path):
        content = f"SIG: Test\n{_SEP}\n**Alice** 10:00 Hello.\n"
        f = tmp_path / "transcript.md"
        f.write_text(content, encoding="utf-8")
        changes, new_text = fix_transcript_file(f)
        assert changes == []
        assert new_text == content

    def test_merged_lines_detected(self, tmp_path):
        content = f"SIG: Test\n{_SEP}\n**Alice Fox** 10:00 Over… Bob Smith 10:05 Thanks.\n"
        f = tmp_path / "transcript.md"
        f.write_text(content, encoding="utf-8")
        changes, new_text = fix_transcript_file(f)
        assert len(changes) == 1
        lineno, orig, replacement = changes[0]
        assert "Alice Fox" in orig
        assert len(replacement) == 2
        assert "**Bob Smith**" in new_text

    def test_no_separator_still_processes(self, tmp_path):
        content = "**Alice Fox** 10:00 Over… Bob Smith 10:05 Thanks.\n"
        f = tmp_path / "transcript.md"
        f.write_text(content, encoding="utf-8")
        changes, new_text = fix_transcript_file(f)
        assert len(changes) == 1

    def test_prefix_not_appended_to_separator_when_first_body_line_splits(self, tmp_path):
        """Prefix must not be merged into the empty sentinel line after the separator."""
        content = f"SIG: Test\n{_SEP}\n**So, I'm on… Victoria Nduka** 04:45 Hello there.\n"
        f = tmp_path / "transcript.md"
        f.write_text(content, encoding="utf-8")
        changes, new_text = fix_transcript_file(f)
        assert len(changes) == 1
        lines = new_text.splitlines()
        # Separator must be intact — not "====...So, I'm on…"
        assert _SEP in lines
        sep_idx = lines.index(_SEP)
        assert lines[sep_idx] == _SEP
        assert any("**Victoria Nduka**" in ln for ln in lines)

    def test_prefix_fragment_appended_to_prior_line(self, tmp_path):
        """Leading plain-text fragment is appended to the previous speaker line."""
        content = (
            f"SIG: Test\n{_SEP}\n"
            "**Alice Fox** 10:00 Let me just…\n"
            "**So, I'm on… Victoria Nduka** 04:45 Hello there.\n"
        )
        f = tmp_path / "transcript.md"
        f.write_text(content, encoding="utf-8")
        changes, new_text = fix_transcript_file(f)
        assert len(changes) == 1
        lines = new_text.splitlines()
        # "So, I'm on…" must be appended to Alice's line, not standalone
        assert any("So, I'm on…" in ln and "Alice Fox" in ln for ln in lines)
        assert any("**Victoria Nduka**" in ln for ln in lines)
        assert not any(ln.strip() == "So, I'm on…" for ln in lines)


# ---------------------------------------------------------------------------
# _parse_args
# ---------------------------------------------------------------------------


class TestParseArgs:
    def test_defaults(self):
        with patch("sys.argv", ["prog"]):
            args = _parse_args()
        assert args.execute is False
        assert args.sig is None

    def test_execute_flag(self):
        with patch("sys.argv", ["prog", "--execute"]):
            args = _parse_args()
        assert args.execute is True

    def test_sig_option(self):
        with patch("sys.argv", ["prog", "--sig", "go"]):
            args = _parse_args()
        assert args.sig == "go"


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------


class TestMain:
    def _make_transcript(self, path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def test_no_merged_lines_found(self, tmp_path, capsys):
        self._make_transcript(
            tmp_path / "Go-SIG" / "2026-01-01" / "transcript.md",
            f"SIG: Go\n{_SEP}\n**Alice** 10:00 Hello.\n",
        )
        with patch("sys.argv", ["prog"]):
            rc = main(tmp_path)
        assert rc == 0
        assert "No merged lines found." in capsys.readouterr().out

    def test_dry_run_shows_would_fix(self, tmp_path, capsys):
        self._make_transcript(
            tmp_path / "Go-SIG" / "2026-01-01" / "transcript.md",
            f"SIG: Go\n{_SEP}\n**Alice Fox** 10:00 Over… Bob Smith 10:05 Thanks.\n",
        )
        with patch("sys.argv", ["prog"]):
            rc = main(tmp_path)
        assert rc == 0
        out = capsys.readouterr().out
        assert "Would fix" in out
        assert "Re-run with --execute" in out

    def test_execute_applies_fix(self, tmp_path, capsys):
        f = tmp_path / "Go-SIG" / "2026-01-01" / "transcript.md"
        self._make_transcript(
            f,
            f"SIG: Go\n{_SEP}\n**Alice Fox** 10:00 Over… Bob Smith 10:05 Thanks.\n",
        )
        with patch("sys.argv", ["prog", "--execute"]):
            rc = main(tmp_path)
        assert rc == 0
        assert "Fixed" in capsys.readouterr().out
        assert "**Bob Smith**" in f.read_text(encoding="utf-8")

    def test_sig_filter_excludes_non_matching(self, tmp_path, capsys):
        self._make_transcript(
            tmp_path / "Go-SIG" / "2026-01-01" / "transcript.md",
            f"SIG: Go\n{_SEP}\n**Alice Fox** 10:00 Over… Bob Smith 10:05 Thanks.\n",
        )
        with patch("sys.argv", ["prog", "--sig", "python"]):
            rc = main(tmp_path)
        assert rc == 0
        assert "No merged lines found." in capsys.readouterr().out

    def test_sig_filter_includes_matching(self, tmp_path, capsys):
        self._make_transcript(
            tmp_path / "Go-SIG" / "2026-01-01" / "transcript.md",
            f"SIG: Go\n{_SEP}\n**Alice Fox** 10:00 Over… Bob Smith 10:05 Thanks.\n",
        )
        with patch("sys.argv", ["prog", "--sig", "go"]):
            rc = main(tmp_path)
        assert rc == 0
        assert "Would fix" in capsys.readouterr().out

    def test_default_content_dir_used_when_none(self, capsys):
        """When content_dir=None, main resolves the default docs/content path."""
        with patch("sys.argv", ["prog", "--sig", "__nonexistent_sig_xyz__"]):
            rc = main(None)
        assert rc == 0
        assert "No merged lines found." in capsys.readouterr().out
