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
