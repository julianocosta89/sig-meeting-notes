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

    def test_cjk_name_detected(self):
        pre = "Alice Fox 10:00 Over to our next speaker… 杉本浩平 10:05 よろしく。"
        matches = _valid_split_matches(pre)
        assert len(matches) == 2
        assert "杉本浩平" in matches[1].group(1)

    def test_accented_uppercase_name_detected(self):
        pre = "Alice Fox 10:00 Thanks, over to Élodie… Élodie Dupont 10:05 Merci."
        matches = _valid_split_matches(pre)
        assert len(matches) == 2
        assert "Élodie" in matches[1].group(1)


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

    def test_prefix_text_before_first_speaker(self):
        """Text before the first speaker-like match is split into a separate line."""
        line = "continuation text. Alice 10:00 Hello world."
        result = fix_line(line)
        assert len(result) == 2
        assert result[0] == "continuation text."
        assert result[1] == "**Alice** 10:00 Hello world."


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
