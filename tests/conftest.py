"""Shared pytest fixtures for the OTel recordings test suite."""

import pathlib
import textwrap

import pytest

SAMPLE_TRANSCRIPT = textwrap.dedent("""\
    SIG: Go SIG
    Date: 2026-02-05
    Duration: 33 minutes
    Source URL: https://zoom.us/rec/share/example
    ============================================================

    Tyler 02:14 Hey, Damien.
    Damien Mathieu 02:19 Hey!
    Tyler 02:20 How's it going?
""")


@pytest.fixture()
def transcript_tree(tmp_path: pathlib.Path) -> pathlib.Path:
    """Create a minimal transcripts/ tree with one SIG and one meeting."""
    sig_dir = tmp_path / "transcripts" / "Go-SIG"
    sig_dir.mkdir(parents=True)
    (sig_dir / "2026-02-05.txt").write_text(SAMPLE_TRANSCRIPT)
    return tmp_path
