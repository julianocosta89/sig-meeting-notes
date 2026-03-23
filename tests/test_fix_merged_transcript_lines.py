"""Tests for scripts/fix_merged_transcript_lines.py — speaker-merge detection and repair."""

from __future__ import annotations

import sys
from pathlib import Path

# Make the scripts/ directory importable.
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from fix_merged_transcript_lines import (  # noqa: E402
    _valid_split_matches,
    fix_line,
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
        # "Bob" appears after a comma — not a valid split point.
        pre = "Alice 10:00 saying something, Bob 10:05 continues"
        matches = _valid_split_matches(pre)
        # Only the first match at position 0 is valid.
        assert all(m.start() == 0 for m in matches)

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

    def test_three_speaker_merge_split(self):
        line = "**Alice Fox** 01:00 first… Bob Smith 02:00 second… Carol Wang 03:00 third."
        result = fix_line(line)
        assert len(result) == 3
        assert "Alice Fox" in result[0]
        assert "Bob Smith" in result[1]
        assert "Carol Wang" in result[2]
