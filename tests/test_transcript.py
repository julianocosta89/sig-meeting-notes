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

    def test_speaker_like_continuation_no_timestamp_still_merged(self):
        """A capitalized word without a timestamp is not a speaker — still merged."""
        raw = [
            _li(False, "Alice: around summertime…"),
            _li(False, "And something more."),
        ]
        assert _merge_continuation_lines(raw) == ["Alice: around summertime… And something more."]


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
