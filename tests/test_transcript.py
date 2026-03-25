"""Tests for scraper/transcript.py — HTML parsing and continuation-line merging."""

from __future__ import annotations

from scraper.transcript import _merge_continuation_lines, parse_transcript_html

# ---------------------------------------------------------------------------
# _merge_continuation_lines unit tests
# ---------------------------------------------------------------------------


def _li(has_speaker: bool, text: str) -> tuple[bool, str]:
    return (has_speaker, text)


class TestMergeContinuationLines:
    def test_empty_input(self):
        assert _merge_continuation_lines([]) == []

    def test_single_item(self):
        assert _merge_continuation_lines([_li(True, "Alice: hello")]) == ["Alice: hello"]

    def test_mid_sentence_break_joined(self):
        raw = [
            _li(True, "Alice: some of the,"),
            _li(False, "image dependencies"),
        ]
        assert _merge_continuation_lines(raw) == ["Alice: some of the, image dependencies"]

    def test_sentence_ending_period_preserved(self):
        raw = [
            _li(True, "Alice: done."),
            _li(False, "Next thought."),
        ]
        assert _merge_continuation_lines(raw) == ["Alice: done.", "Next thought."]

    def test_sentence_ending_question_mark_preserved(self):
        raw = [
            _li(True, "Alice: is this right?"),
            _li(False, "Yes."),
        ]
        assert _merge_continuation_lines(raw) == ["Alice: is this right?", "Yes."]

    def test_sentence_ending_exclamation_preserved(self):
        raw = [
            _li(True, "Alice: great!"),
            _li(False, "And more."),
        ]
        assert _merge_continuation_lines(raw) == ["Alice: great!", "And more."]

    def test_ellipsis_ending_joined(self):
        raw = [
            _li(True, "Alice: around summertime…"),
            _li(False, "And, yeah."),
        ]
        assert _merge_continuation_lines(raw) == ["Alice: around summertime… And, yeah."]

    def test_speaker_line_starts_new_entry(self):
        raw = [
            _li(True, "Alice: first,"),
            _li(True, "Bob: second"),
        ]
        assert _merge_continuation_lines(raw) == ["Alice: first,", "Bob: second"]

    def test_multiple_continuations_joined(self):
        raw = [
            _li(True, "Alice: one,"),
            _li(False, "two,"),
            _li(False, "three."),
        ]
        assert _merge_continuation_lines(raw) == ["Alice: one, two, three."]

    def test_continuation_after_sentence_end_not_joined(self):
        raw = [
            _li(True, "Alice: done."),
            _li(False, "continued here"),
        ]
        assert _merge_continuation_lines(raw) == ["Alice: done.", "continued here"]

    def test_cjk_sentence_end_preserved(self):
        raw = [
            _li(True, "Yoshi: またオーディオが聞こえない。"),
            _li(False, "なんだろう。"),
        ]
        assert _merge_continuation_lines(raw) == [
            "Yoshi: またオーディオが聞こえない。",
            "なんだろう。",
        ]

    def test_cjk_mid_sentence_joined(self):
        raw = [
            _li(True, "Yoshi: なんだろう"),
            _li(False, "あ、これだ。"),
        ]
        assert _merge_continuation_lines(raw) == ["Yoshi: なんだろう あ、これだ。"]

    def test_em_dash_ending_joined(self):
        raw = [
            _li(True, "Alice: it was—"),
            _li(False, "unexpected."),
        ]
        assert _merge_continuation_lines(raw) == ["Alice: it was— unexpected."]

    def test_speaker_like_continuation_not_merged(self):
        """A no-speaker line that looks like 'Name Timestamp text' starts a new entry.

        Zoom often wraps each <li> in a container div with no 'speaker' class, so
        all lines arrive with has_speaker=False.  Without _SPEAKER_LIKE_RE the next
        speaker's line would be merged into the previous one when it ends with '…'.
        """
        raw = [
            _li(False, "Marc Pichler 13:40 If there's no more comments, which is asking…"),
            _li(False, "Marylia Gutierrez 13:43 I'll just ask you for a review on the…"),
            _li(False, "Marc Pichler (Dynatrace) 13:45 Oh."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Marc Pichler 13:40 If there's no more comments, which is asking…",
            "Marylia Gutierrez 13:43 I'll just ask you for a review on the…",
            "Marc Pichler (Dynatrace) 13:45 Oh.",
        ]

    def test_single_word_speaker_not_merged(self):
        """A single-word name followed by a timestamp starts a new entry (e.g. 'Andrej 10:32 …')."""
        raw = [
            _li(False, "Dan Gomez Blanco 10:28 I know… was just another meeting, so…"),
            _li(False, "Andrej 10:32 Oh, okay, so maybe she will join as well."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Dan Gomez Blanco 10:28 I know… was just another meeting, so…",
            "Andrej 10:32 Oh, okay, so maybe she will join as well.",
        ]

    def test_unicode_speaker_not_merged(self):
        """A name containing Unicode diacritics followed by a timestamp starts a new entry."""
        raw = [
            _li(False, "Marylia Gutierrez 08:07 Yeah, I have it easily here. Let me just…"),
            _li(False, "Juraci Paixão Kröhling 08:13 I mean…"),
        ]
        assert _merge_continuation_lines(raw) == [
            "Marylia Gutierrez 08:07 Yeah, I have it easily here. Let me just…",
            "Juraci Paixão Kröhling 08:13 I mean…",
        ]

    def test_apostrophe_speaker_not_merged(self):
        """A name token containing an apostrophe (e.g. O'Sullivan) starts a new entry."""
        raw = [
            _li(False, "Alice Fox 10:00 Let me hand over to Donal…"),
            _li(False, "Donal O'Sullivan 10:05 Thanks, yes."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 10:00 Let me hand over to Donal…",
            "Donal O'Sullivan 10:05 Thanks, yes.",
        ]

    def test_hyphenated_speaker_not_merged(self):
        """A hyphenated display name starts a new entry."""
        raw = [
            _li(False, "Sergey 10:27 It can drift over time…"),
            _li(False, "Chris Lightfoot-Wild 10:45 It reads like if…"),
        ]
        assert _merge_continuation_lines(raw) == [
            "Sergey 10:27 It can drift over time…",
            "Chris Lightfoot-Wild 10:45 It reads like if…",
        ]

    def test_bracket_org_speaker_not_merged(self):
        """A display name with a bracket org tag (e.g. 'Marc Alff [MySQL]') starts a new entry."""
        raw = [
            _li(False, "Alice Fox 10:00 Great, over to Marc…"),
            _li(False, "Marc Alff [MySQL] 10:03 Happy to share."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 10:00 Great, over to Marc…",
            "Marc Alff [MySQL] 10:03 Happy to share.",
        ]

    def test_pipe_org_speaker_not_merged(self):
        """A display name with a pipe-separated org (e.g. 'Name | Org') starts a new entry."""
        raw = [
            _li(False, "Alice Fox 10:00 Over to Giuseppe…"),
            _li(False, "Giuseppe Ognibene | Coralogix 10:07 Sure."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 10:00 Over to Giuseppe…",
            "Giuseppe Ognibene | Coralogix 10:07 Sure.",
        ]

    def test_email_handle_speaker_not_merged(self):
        """An email-style display name starts a new entry."""
        raw = [
            _li(False, "Tiffany Hrabusa 20:55 I haven't looked at it yet, so…"),
            _li(False, "lciukaj@splunk.com 20:59 Yeah, did you have plans to discuss next steps?"),
        ]
        assert _merge_continuation_lines(raw) == [
            "Tiffany Hrabusa 20:55 I haven't looked at it yet, so…",
            "lciukaj@splunk.com 20:59 Yeah, did you have plans to discuss next steps?",
        ]

    def test_speaker_like_continuation_no_timestamp_still_merged(self):
        """A capitalized word without a timestamp is not a speaker — still merged."""
        raw = [
            _li(False, "Alice: around summertime…"),
            _li(False, "And something more."),
        ]
        assert _merge_continuation_lines(raw) == ["Alice: around summertime… And something more."]

    def test_cjk_speaker_not_merged(self):
        """A CJK name followed by a timestamp is recognised as a new speaker."""
        raw = [
            _li(False, "Alice Fox 10:00 Over to our next speaker…"),
            _li(False, "杉本浩平 10:05 よろしくお願いします。"),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 10:00 Over to our next speaker…",
            "杉本浩平 10:05 よろしくお願いします。",
        ]

    def test_accented_uppercase_speaker_not_merged(self):
        """A name starting with a non-ASCII uppercase letter is recognised as a new speaker."""
        raw = [
            _li(False, "Alice Fox 10:00 Thanks, over to Élodie…"),
            _li(False, "Élodie Dupont 10:05 Merci."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 10:00 Thanks, over to Élodie…",
            "Élodie Dupont 10:05 Merci.",
        ]

    def test_single_char_speaker_not_merged(self):
        """A single-character display name/initial is recognised as a new speaker."""
        raw = [
            _li(False, "Alice Fox 10:00 Passing to Q…"),
            _li(False, "Q 10:05 Thanks."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 10:00 Passing to Q…",
            "Q 10:05 Thanks.",
        ]

    def test_single_char_unicode_speaker_not_merged(self):
        """A single-character Unicode initial is recognised as a new speaker."""
        raw = [
            _li(False, "Alice Fox 10:00 Over to Élodie…"),
            _li(False, "É 10:05 Merci."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 10:00 Over to Élodie…",
            "É 10:05 Merci.",
        ]

    def test_embedded_speaker_splits_prefix_and_remainder(self):
        """prefix before embedded Name MM:SS is appended to prior turn; remainder is a new entry."""
        raw = [
            _li(False, "Alice Fox 10:00 passing over…"),
            _li(False, "Yeah, so… Andrej 03:22 Thanks."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 10:00 passing over… Yeah, so…",
            "Andrej 03:22 Thanks.",
        ]

    def test_embedded_speaker_no_prefix_starts_new_entry(self):
        """When text starts at the sentence-end char, only a new entry is created."""
        raw = [
            _li(False, "Alice Fox 10:00 passing over…"),
            _li(False, "… Andrej 03:22 Thanks."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 10:00 passing over… …",
            "Andrej 03:22 Thanks.",
        ]

    def test_embedded_clock_phrase_does_not_block_later_real_speaker_split(self):
        """Suppressed clock phrases should not prevent scanning to a later real hand-off."""
        raw = [
            _li(True, "Alice: previous turn."),
            _li(False, "Bob 10:00 ... At 10:05 we begin. Carol 10:06 Thanks."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice: previous turn.",
            "Bob 10:00 ... At 10:05 we begin.",
            "Carol 10:06 Thanks.",
        ]

    def test_hh_mm_ss_speaker_not_merged(self):
        """A name followed by an HH:MM:SS timestamp starts a new entry."""
        raw = [
            _li(False, "Alice Fox 00:12:55 over to Bob…"),
            _li(False, "Bob 00:13:34 Thanks."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 00:12:55 over to Bob…",
            "Bob 00:13:34 Thanks.",
        ]

    def test_embedded_hh_mm_ss_speaker_splits_prefix_and_remainder(self):
        """An embedded HH:MM:SS boundary is also split correctly."""
        raw = [
            _li(False, "Alice Fox 00:12:55 let me hand over…"),
            _li(False, "Yeah, so… Bob 00:13:34 Thanks."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 00:12:55 let me hand over… Yeah, so…",
            "Bob 00:13:34 Thanks.",
        ]

    def test_article_a_after_ellipsis_not_treated_as_speaker(self):
        """'a' (English article) after '…' is not a speaker name."""
        raw = [
            _li(False, "Alice Fox 10:00 passing over…"),
            _li(False, "a 10:05 reminder was sent."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 10:00 passing over… a 10:05 reminder was sent.",
        ]

    def test_sentence_starter_not_treated_as_speaker(self):
        """Common sentence-starting words (e.g. 'At', 'Today') are not speaker names."""
        raw = [
            _li(False, "Alice Fox 10:00 passing over…"),
            _li(False, "At 10:05 we begin."),
        ]
        # 'At' is in _SENTENCE_STARTERS, so it should merge rather than start a new entry.
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 10:00 passing over… At 10:05 we begin.",
        ]

    def test_sentence_starter_first_token_title_cased_second_is_new_speaker(self):
        """'So Koide 10:05' starts a new turn despite 'So' being a sentence-starter.

        When the first token is in _SENTENCE_STARTERS but subsequent bare tokens
        are title-cased, the line is treated as a new-speaker start rather than
        merged into the previous utterance.
        """
        raw = [
            _li(False, "Alice Fox 10:00 Good point…"),
            _li(False, "So Koide 10:05 Thanks."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 10:00 Good point…",
            "So Koide 10:05 Thanks.",
        ]

    def test_short_name_after_period_not_split_as_embedded_speaker(self):
        """A 2-char word after '.' (e.g. 'At 10:01') is not treated as a speaker."""
        raw = [
            _li(False, "Alice Fox 10:00 Let's restart."),
            _li(False, "Okay. At 10:01 we begin."),
        ]
        # 'At' is 2 chars after '.', so it is NOT split as a new speaker.
        # The previous line ends with '.', so the continuation starts a new entry.
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 10:00 Let's restart.",
            "Okay. At 10:01 we begin.",
        ]

    def test_short_name_after_ellipsis_still_split(self):
        """A single-char name after '…' IS treated as a new speaker (not suppressed)."""
        raw = [
            _li(False, "Alice Fox 10:00 passing over…"),
            _li(False, "yeah… Q 10:05 Right."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 10:00 passing over… yeah…",
            "Q 10:05 Right.",
        ]

    def test_dotted_handle_speaker_not_merged(self):
        """A dotted handle at the start of the continuation is treated as a speaker."""
        raw = [
            _li(False, "Alice Fox 10:00 passing over…"),
            _li(False, "foo.bar 10:01 Sure."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 10:00 passing over…",
            "foo.bar 10:01 Sure.",
        ]

    def test_comma_before_multi_token_speaker_splits_embedded(self):
        """A multi-word speaker name after ',' is split as an embedded boundary.

        Zoom sometimes renders two consecutive speaker turns in a single <li>
        where the boundary is a comma rather than sentence-ending punctuation.
        """
        raw = [
            _li(False, "Alice Fox 10:00 let me pass the mic"),
            _li(False, "sure, thanks, Kemal Akkoyun 31:30 I'm super happy to be here."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 10:00 let me pass the mic sure, thanks,",
            "Kemal Akkoyun 31:30 I'm super happy to be here.",
        ]

    def test_comma_before_single_token_speaker_splits_embedded(self):
        """A capitalized single-token speaker after ',' is split as a real hand-off."""
        raw = [
            _li(False, "Bob Strecansky 19:36 Yeah"),
            _li(False, "Yeah, Sergey 19:38 I mean, it sounds like they're placed correctly."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Bob Strecansky 19:36 Yeah Yeah,",
            "Sergey 19:38 I mean, it sounds like they're placed correctly.",
        ]

    def test_comma_before_single_token_not_split_as_embedded_speaker(self):
        """A single-word token after ',' is NOT split to avoid false positives."""
        raw = [
            _li(False, "Alice Fox 10:00 Let me check"),
            _li(False, "probably, probably 30:00 we can start."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 10:00 Let me check probably, probably 30:00 we can start.",
        ]

    def test_comma_before_sentence_starter_not_split_as_embedded_speaker(self):
        """A sentence-starter word after ',' is NOT split even as a multi-token."""
        raw = [
            _li(False, "Alice Fox 10:00 let me hand over"),
            _li(False, "yes, and Alice Smith 10:05 Thanks."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 10:00 let me hand over yes, and Alice Smith 10:05 Thanks.",
        ]

    def test_comma_before_email_handle_speaker_splits_embedded(self):
        """An email-style speaker after ',' is split even when the handle is lowercase."""
        raw = [
            _li(False, "Tiffany Hrabusa 20:55 I haven't looked at it yet"),
            _li(
                False,
                "copy edit is done, lciukaj@splunk.com 20:59 Yeah, did you have plans to discuss next steps?",  # noqa: E501
            ),
        ]
        assert _merge_continuation_lines(raw) == [
            "Tiffany Hrabusa 20:55 I haven't looked at it yet copy edit is done,",
            "lciukaj@splunk.com 20:59 Yeah, did you have plans to discuss next steps?",
        ]

    def test_suppressed_period_match_in_remainder_does_not_block_later_split(self):
        """Continuation remainders should keep scanning after a suppressed sentence-starter."""
        raw = [
            _li(True, "Alice: previous turn"),
            _li(False, "noted. At 10:05 we begin. Bob 10:06 Hi."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice: previous turn noted. At 10:05 we begin.",
            "Bob 10:06 Hi.",
        ]

    def test_suppressed_embedded_match_after_sentence_end_stays_new_entry(self):
        """A suppressed embedded clock phrase stays as a new entry when the previous turn ended."""
        raw = [
            _li(True, "Alice: done."),
            _li(False, "Okay. At 10:05 we begin."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice: done.",
            "Okay. At 10:05 we begin.",
        ]

    def test_suppressed_embedded_match_mid_sentence_merges_whole_line(self):
        """A suppressed embedded clock phrase merges when the previous turn is mid-sentence."""
        raw = [
            _li(True, "Alice: still going"),
            _li(False, "Okay. At 10:05 we begin."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice: still going Okay. At 10:05 we begin.",
        ]

    def test_extract_speaker_skips_bare_text_nodes(self):
        """Bare text children should not interfere with speaker/text extraction."""
        html = (
            '<ul class="transcript-list">'
            '<li>  <span class="speaker">Alice</span> hello <p>world.</p> </li>'
            "</ul>"
        )
        assert parse_transcript_html(html) == ["Alice: world."]

    def test_extract_speaker_fallback_from_newline_text(self):
        """When no child tags are present, newline-separated text falls back to speaker + body."""
        html = "<ul><li>Alice\nhello world.</li></ul>"
        assert parse_transcript_html(html) == ["Alice: hello world."]

    def test_extract_text_fallback_without_newline(self):
        """When no speaker is detectable and there is no newline, keep the full text as body."""
        html = "<ul><li>just continuation text</li></ul>"
        assert parse_transcript_html(html) == ["just continuation text"]

    def test_extract_text_fallback_with_single_text_line(self):
        """Single-line fallback text should not create a synthetic speaker."""
        html = "<ul><li>plain fallback body</li></ul>"
        assert parse_transcript_html(html) == ["plain fallback body"]

    def test_extract_speaker_fallback_with_multiple_lines(self):
        """Fallback newline parsing should join the remaining body lines."""
        html = "<ul><li>Alice\nhello\nworld.</li></ul>"
        assert parse_transcript_html(html) == ["Alice: hello world."]

    def test_continuation_without_embedded_speaker_still_merged(self):
        """A plain continuation line with no embedded speaker is still merged."""
        raw = [
            _li(False, "Alice Fox 10:00 passing over…"),
            _li(False, "Yeah, so I think we can start."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 10:00 passing over… Yeah, so I think we can start.",
        ]

    def test_multi_token_title_cased_name_after_period_splits(self):
        """A title-cased multi-token name ('So Koide') after '.' is a new speaker.

        The prefix before the embedded speaker ('I agree.') is appended to the
        previous turn; the remainder starts a new speaker entry.
        """
        raw = [
            _li(False, "Alice Fox 10:00 Good point."),
            _li(False, "I agree. So Koide 10:05 Thanks."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 10:00 Good point. I agree.",
            "So Koide 10:05 Thanks.",
        ]

    def test_multi_token_lowercase_second_word_after_period_not_split(self):
        """A phrase with lowercase second word ('So far 10:05') is NOT a new speaker.

        The whole line is kept as a new entry (previous turn ended with '.').
        """
        raw = [
            _li(False, "Alice Fox 10:00 Good point."),
            _li(False, "I agree. So far 10:05 into the meeting."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 10:00 Good point.",
            "I agree. So far 10:05 into the meeting.",
        ]

    def test_multi_token_name_with_lowercase_org_suffix_splits(self):
        """A name with a lowercase org suffix ('So Koide | openTelemetry') still splits.

        Org suffix tokens (after '|', '[', '(') are excluded from the
        title-case check so that lowercase org words don't suppress the split.
        """
        raw = [
            _li(False, "Alice Fox 10:00 Good point."),
            _li(False, "I agree. So Koide | openTelemetry 10:05 Thanks."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 10:00 Good point. I agree.",
            "So Koide | openTelemetry 10:05 Thanks.",
        ]

    def test_sentence_starter_with_pipe_suffix_not_split(self):
        """A sentence-starter word followed immediately by a pipe org ('So | far') is not a speaker.

        When only one bare name token exists before the org marker, single-token
        rules apply and suppress the false split.
        """
        raw = [
            _li(False, "Alice Fox 10:00 Good point."),
            _li(False, "I agree. So | far 10:05 into the meeting."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 10:00 Good point.",
            "I agree. So | far 10:05 into the meeting.",
        ]

    def test_embedded_speaker_after_question_mark_splits(self):
        """An embedded speaker after '?' is split as a new speaker turn (line 209)."""
        raw = [
            _li(False, "Alice Fox 10:00 Is that right…"),
            _li(False, "Yeah? Bob 10:05 Thanks."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 10:00 Is that right… Yeah?",
            "Bob 10:05 Thanks.",
        ]

    def test_sentence_starter_after_exclamation_suppressed_merges_when_prev_no_sentence_end(self):
        """suppress=True + prev line no sentence-end → merge whole line (line 216)."""
        raw = [
            _li(False, "Alice Fox 10:00 let me pass"),
            _li(False, "yeah… at 10:05 we begin."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 10:00 let me pass yeah… at 10:05 we begin.",
        ]

    def test_short_initial_with_org_suffix_after_period_splits(self):
        """A short initial with an org suffix ('Q | OpenAI') after '.' is a new speaker.

        The org suffix is evidence of a real display name; the length guard is
        skipped so that single-character initials are not suppressed.
        """
        raw = [
            _li(False, "Alice Fox 10:00 Good point."),
            _li(False, "I agree. Q | OpenAI 10:05 Thanks."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice Fox 10:00 Good point. I agree.",
            "Q | OpenAI 10:05 Thanks.",
        ]

    def test_speaker_start_line_with_inner_embedded_boundary_is_split(self):
        """A line that starts with Name+Timestamp AND contains a later embedded
        boundary should be split at the inner boundary too.

        This covers the case where Zoom emits a raw line like:
          "Ernest Owojori 31:14 Great idea… Andrej 31:16 Agreed."
        The outer _is_new_speaker_start branch must not swallow the whole
        thing — it should split into two speaker entries.
        """
        raw = [
            _li(True, "Alice: previous turn."),
            _li(False, "Ernest Owojori 31:14 Great idea… Andrej 31:16 Agreed."),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice: previous turn.",
            "Ernest Owojori 31:14 Great idea…",
            "Andrej 31:16 Agreed.",
        ]

    def test_speaker_start_line_with_multiple_inner_boundaries_split_all(self):
        """Three speakers packed into one raw line are all separated."""
        raw = [
            _li(True, "Alice: done."),
            _li(False, "Bob Smith 10:00 First. Carol Jones 10:01 Second. Dave 10:02 Third."),
        ]
        result = _merge_continuation_lines(raw)
        assert result == [
            "Alice: done.",
            "Bob Smith 10:00 First.",
            "Carol Jones 10:01 Second.",
            "Dave 10:02 Third.",
        ]

    def test_embedded_speaker_in_continuation_line_followed_by_further_boundary(self):
        """A continuation line (no speaker start) with two embedded boundaries
        is split at both points."""
        raw = [
            _li(True, "Alice: hmm"),
            _li(False, "not sure. Bob Smith 10:00 I agree. Carol 10:01 Me too."),
        ]
        result = _merge_continuation_lines(raw)
        assert result == [
            "Alice: hmm not sure.",
            "Bob Smith 10:00 I agree.",
            "Carol 10:01 Me too.",
        ]

    def test_speaker_start_line_with_hyphenated_and_email_boundaries_split_all(self):
        """A speaker-start continuation should also split later hyphenated/email speaker turns."""
        raw = [
            _li(True, "Alice: done."),
            _li(
                False,
                "Sergey 10:27 It can drift over time… Chris Lightfoot-Wild 10:45 It reads like if… lciukaj@splunk.com 10:59 Yep.",  # noqa: E501
            ),
        ]
        assert _merge_continuation_lines(raw) == [
            "Alice: done.",
            "Sergey 10:27 It can drift over time…",
            "Chris Lightfoot-Wild 10:45 It reads like if…",
            "lciukaj@splunk.com 10:59 Yep.",
        ]


# ---------------------------------------------------------------------------
# parse_transcript_html integration tests (HTML → merged lines)
# ---------------------------------------------------------------------------

_SPEAKER_CLASS = "speaker"


def _make_ul(*items: tuple[str, str]) -> str:
    """Build a minimal transcript HTML from (speaker, text) pairs.

    Pass speaker="" to produce a continuation <li> (no speaker element).
    """
    lis = []
    for speaker, text in items:
        if speaker:
            lis.append(f'<li><span class="{_SPEAKER_CLASS}">{speaker}</span><p>{text}</p></li>')
        else:
            lis.append(f"<li><p>{text}</p></li>")
    return f'<ul class="transcript-list">{"".join(lis)}</ul>'


class TestParseTranscriptHtml:
    def test_empty_ul(self):
        assert parse_transcript_html("<ul></ul>") == []

    def test_no_ul(self):
        assert parse_transcript_html("<div></div>") == []

    def test_single_utterance(self):
        html = _make_ul(("Alice", "hello world."))
        assert parse_transcript_html(html) == ["Alice: hello world."]

    def test_mid_sentence_continuation_merged(self):
        html = _make_ul(
            ("Gerard Vanloo", "some of the,"),
            ("", "the image dependencies, I think sometime last year,"),
            ("", "in the… around summertime."),
            ("", "And, yeah."),
        )
        lines = parse_transcript_html(html)
        assert len(lines) == 2
        assert lines[0] == (
            "Gerard Vanloo: some of the, "
            "the image dependencies, I think sometime last year, "
            "in the… around summertime."
        )
        assert lines[1] == "And, yeah."

    def test_sentence_boundary_preserved(self):
        html = _make_ul(
            ("Alice", "done."),
            ("", "New sentence."),
        )
        assert parse_transcript_html(html) == ["Alice: done.", "New sentence."]

    def test_multiple_speakers_not_merged(self):
        html = _make_ul(
            ("Alice", "first,"),
            ("Bob", "second."),
        )
        assert parse_transcript_html(html) == ["Alice: first,", "Bob: second."]
