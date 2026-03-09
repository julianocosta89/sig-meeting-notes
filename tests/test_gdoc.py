"""Tests for scraper/gdoc.py — Google Docs meeting-notes extraction."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import scraper.gdoc as gdoc
from scraper.gdoc import (
    _collect_list_item,
    _date_variants,
    _extract_leading_attendees,
    _extract_subsection_md,
    _find_date_section,
    _normalize_date_text,
    _to_export_url,
    _unescape_md,
    fetch_meeting_notes,
)

# ---------------------------------------------------------------------------
# Markdown fixtures that mirror a typical Google Docs markdown export
# ---------------------------------------------------------------------------

_SAMPLE_MD = """\
# 2026-01-22

Attendee:

* Alice Smith
* Bob Jones

Agenda:

* Review open PRs
* Discuss v2 spec
  * Breaking changes

Notes:

Some notes here.

# 2026-02-05

Attendee:

* Tyler Benson
* Damien Mathieu
* Sam Xie

Agenda:

* SDK update
* KubeCon planning

# 2026-02-12

Attendee:

* Someone Else
"""

# CC++ SIG style: short month-name headings, trailing soft-break spaces,
# backslash-escaped characters, and deep nesting.
_CC_STYLE_MD = """\
# Feb 9, 2026

Attendee:

* Marc Alff (Oracle)
* Ehsan

Agenda:

* Upstream
  * [Spec](https://github.com/open-telemetry/opentelemetry-specification)
    * Mark declarative config as stable\\#4568
      * Almost there
  * [Semantic conventions](https://github.com/open-telemetry/semantic-conventions)
* Opentelemetry-cpp
  * PR
    * \\[Marc\\] \\- PR cleanup needed
"""

# Simple nested list fixture
_NESTED_MD = """\
# 2026-02-05

Agenda:

* Upstream
  * Spec
  * Semantic conventions
* SDK
"""

# Links in list items (already clean in MD export — no Google redirects)
_LINK_MD = """\
# 2026-02-05

Agenda:

* Review [Issue 123](https://github.com/open-telemetry/opentelemetry-specification/issues/123)
* Visit [example](https://example.com)
"""

# Community Demo SIG style: plain-text date lines (no # heading), labels
# without colons, and * bullets.  The document also has a top-level heading
# before the first meeting that should be ignored.
_PLAIN_DATE_MD = """\
# Resources

* Repository link

2026-02-11

Attendees

* Juliano Costa (Datadog)
* Juande Manjon

Agenda

* \\[Juande\\] Add OpAMP to the Demo
  * Some sub-item
* Docker minimal is broken

2026-01-28

Attendees

* Cyrille Le Clerc

Agenda

* OTel Unplugged Conf
"""

# DevEx SIG style: bold labels (**Attendees:**), dash bullets (- ),
# and trailing soft-break spaces.  This is the format that was previously
# broken because **Attendees:** starts with "*".
_DEVEX_STYLE_MD = """\
# Feb 18, 2026 (EU Meeting)

**Attendees:**

- Juliano Costa (Datadog)
- Johanna Öjeling (Grafana Labs)

**Agenda:**

- \\[Nico\\] MCP updates
  - No TC sponsor
    - Re-scope to focus on the Collector
- Release process
"""


# Arrow-SIG style: plain-text date line with extra content after the date
# (time, meeting type), and * bullets.
_ARROW_STYLE_MD = """\
# OTEL Arrow SIG

Feb 19, 2026 8:00 AM - General meeting
Attendees:

* Brett Mitchell (ElastiFlow)
* Aaron Marten (Microsoft)

Agenda:

* \\[Brett\\]: New member, understanding project trajectory
* \\[Laurent\\] Inter-pipeline topics

Feb 10, 2026 - General meeting
Attendees:

* Joshua MacDonald (Microsoft)
* Laurent Querel (F5)

Agenda:

* Issue triage
"""

# NET SIG style: day-first date format with time and timezone suffix
_NET_STYLE_MD = """\
17 Feb 2026 11:00 AM PST
Attendees:

* Matthew Hensley (Grafana Labs)
* Rajkumar Rangaraj (Microsoft)

Agenda:

* \\[Julius\\] Logs bridge API

10 Feb 2026 11:00 GMT-8
Attendees:

* Matthew Hensley (Grafana Labs)
* Martin Costello (Grafana Labs)

Agenda:

* 1.15.1 soon?
"""

# RPC SIG style: bold paragraph date with weekday prefix and ordinal suffix
_RPC_STYLE_MD = """\
**Wed, Feb 18th, 2026 (Pacific Time) /**
**Thu, Feb 19th, 2026 (China Standard Time)**

Attendees:

* Trask
* Liudmila

Agenda:

* Project board review
* RC PR discussion

**Wed, Feb 11th, 2026 (Pacific Time) /**
**Thu, Feb 12th, 2026 (China Standard Time)**

Attendees:

* Trask
* Steve
"""

# Java-SIG style: level-2 heading with bold + ordinal suffix
_JAVA_STYLE_MD = """\
# OpenTelemetry Java + Instrumentation SIG

## **Feb 19th, 2026 (UTC) - General**

Attendees:

* John Watson (Sublime Security)
* Trask Stalnaker (Microsoft)

Agenda:

* Standing topic: issue triage
* PR review

## **Feb 12th, 2026 (UTC) - General**

Attendees:

* Jay DeLuca (Grafana Labs)
"""

# ja-JA SIG style: dotted month abbreviation in heading ("Feb. 18, 2026")
_DOTTED_MONTH_MD = """\
## Feb. 18, 2026

Attendees:

* Yoshi Yamaguchi (AWS)
* Kohei Sugimoto (MIXI)

Topics

* Drifted Files issue
* prh configuration

## Jan. 21, 2026

Attendees:

* Yoshi Yamaguchi (AWS)
"""

# Prometheus-WG style: "Topics" instead of "Agenda"
_TOPICS_LABEL_MD = """\
## Feb 13, 2026

Attendees: [Arve Knudsen](mailto:arve@example.com)[David Ashpole](mailto:dash@example.com)

Topics:

* \\[arthur\\] Stabilizing Prometheus exporter spec
* Prometheus receiver stabilization

## Jan 30, 2026

Attendees: Krajo, David
"""

# Collector-SIG style: "Notes" as the agenda section
_NOTES_LABEL_MD = """\
## Feb 18, 2026 | 09:00 PT SIG MTG

Attendees

* Evan Bradley (Dynatrace)
* Alex Boten (Honeycomb)

Notes

* Go through high priority issues
* Discuss stabilization

## Feb 11, 2026 | 09:00 PT SIG MTG

Attendees

* Someone Else
"""

# ---------------------------------------------------------------------------
# _to_export_url
# ---------------------------------------------------------------------------


class TestToExportUrl:
    def test_edit_url(self) -> None:
        url = _to_export_url("https://docs.google.com/document/d/ABC123/edit")
        assert url == "https://docs.google.com/document/d/ABC123/export?format=md"

    def test_view_url(self) -> None:
        url = _to_export_url("https://docs.google.com/document/d/XYZ/view")
        assert url == "https://docs.google.com/document/d/XYZ/export?format=md"

    def test_share_url_with_query(self) -> None:
        url = _to_export_url("https://docs.google.com/document/d/DOC_ID/edit?usp=sharing")
        assert url == "https://docs.google.com/document/d/DOC_ID/export?format=md"

    def test_invalid_url_returns_none(self) -> None:
        assert _to_export_url("https://example.com/not-a-doc") is None

    def test_empty_string_returns_none(self) -> None:
        assert _to_export_url("") is None


# ---------------------------------------------------------------------------
# _date_variants
# ---------------------------------------------------------------------------


class TestDateVariants:
    def test_contains_iso(self) -> None:
        assert "2026-02-05" in _date_variants("2026-02-05")

    def test_contains_us_slash_no_leading_zero(self) -> None:
        assert "2/5/2026" in _date_variants("2026-02-05")

    def test_contains_us_slash_leading_zero(self) -> None:
        assert "02/05/2026" in _date_variants("2026-02-05")

    def test_contains_long_month(self) -> None:
        variants = _date_variants("2026-02-05")
        assert any("February" in v for v in variants)

    def test_contains_short_month(self) -> None:
        variants = _date_variants("2026-02-05")
        assert any("Feb" in v for v in variants)

    def test_contains_day_first_short_month(self) -> None:
        variants = _date_variants("2026-02-17")
        assert "17 Feb 2026" in variants

    def test_contains_day_first_with_leading_zero(self) -> None:
        variants = _date_variants("2026-02-05")
        assert "05 Feb 2026" in variants

    def test_contains_dotted_month(self) -> None:
        variants = _date_variants("2026-02-18")
        assert any("Feb." in v for v in variants)

    def test_invalid_date_returns_original(self) -> None:
        assert _date_variants("not-a-date") == ["not-a-date"]


# ---------------------------------------------------------------------------
# _collect_list_item
# ---------------------------------------------------------------------------


class TestCollectListItem:
    def test_bullet_star(self) -> None:
        assert _collect_list_item("* Alice") == "- Alice"

    def test_bullet_dash(self) -> None:
        assert _collect_list_item("- Bob") == "- Bob"

    def test_nested_two_spaces(self) -> None:
        assert _collect_list_item("  * Nested") == "  - Nested"

    def test_nested_four_spaces(self) -> None:
        assert _collect_list_item("    * Deep") == "    - Deep"

    def test_tab_indented(self) -> None:
        assert _collect_list_item("\tItem") == "  - Item"

    def test_tab_indented_two_tabs(self) -> None:
        assert _collect_list_item("\t\tItem") == "    - Item"

    def test_tab_indented_empty_text_returns_none(self) -> None:
        assert _collect_list_item("\t   ") is None

    def test_plain_line_returns_none(self) -> None:
        assert _collect_list_item("Not a list item") is None

    def test_empty_string_returns_none(self) -> None:
        assert _collect_list_item("") is None


# ---------------------------------------------------------------------------
# _normalize_date_text
# ---------------------------------------------------------------------------


class TestNormalizeDateText:
    def test_strips_bold_markers(self) -> None:
        assert _normalize_date_text("**Feb 18, 2026**") == "Feb 18, 2026"

    def test_strips_ordinal_th(self) -> None:
        assert _normalize_date_text("Feb 19th, 2026") == "Feb 19, 2026"

    def test_strips_ordinal_st(self) -> None:
        assert _normalize_date_text("Feb 1st, 2026") == "Feb 1, 2026"

    def test_strips_ordinal_nd(self) -> None:
        assert _normalize_date_text("Feb 2nd, 2026") == "Feb 2, 2026"

    def test_strips_ordinal_rd(self) -> None:
        assert _normalize_date_text("Feb 3rd, 2026") == "Feb 3, 2026"

    def test_strips_bold_and_ordinal_together(self) -> None:
        assert _normalize_date_text("**Wed, Feb 18th, 2026 (PT)**") == "Wed, Feb 18, 2026 (PT)"

    def test_plain_text_unchanged(self) -> None:
        assert _normalize_date_text("Feb 18, 2026") == "Feb 18, 2026"


# ---------------------------------------------------------------------------
# _unescape_md
# ---------------------------------------------------------------------------


class TestUnescapeMd:
    def test_removes_hash_escape(self) -> None:
        assert _unescape_md(r"issue \#4568") == "issue #4568"

    def test_removes_bracket_escapes(self) -> None:
        assert _unescape_md(r"\[Marc\] \- note") == "[Marc] - note"

    def test_removes_asterisk_escape(self) -> None:
        assert _unescape_md(r"\*bold\*") == "*bold*"

    def test_plain_text_unchanged(self) -> None:
        assert _unescape_md("no escapes here") == "no escapes here"

    def test_link_text_unchanged(self) -> None:
        text = "[Spec](https://github.com/open-telemetry/opentelemetry-specification)"
        assert _unescape_md(text) == text


# ---------------------------------------------------------------------------
# _find_date_section
# ---------------------------------------------------------------------------


class TestFindDateSection:
    def test_finds_iso_date(self) -> None:
        section = _find_date_section(_SAMPLE_MD, _date_variants("2026-02-05"))
        assert section is not None
        assert "Tyler Benson" in section

    def test_excludes_content_from_next_section(self) -> None:
        section = _find_date_section(_SAMPLE_MD, _date_variants("2026-02-05"))
        assert section is not None
        assert "Someone Else" not in section

    def test_excludes_content_from_previous_section(self) -> None:
        section = _find_date_section(_SAMPLE_MD, _date_variants("2026-02-05"))
        assert section is not None
        assert "Alice Smith" not in section

    def test_returns_none_for_missing_date(self) -> None:
        assert _find_date_section(_SAMPLE_MD, _date_variants("2099-12-31")) is None

    def test_returns_none_for_empty_document(self) -> None:
        assert _find_date_section("", _date_variants("2026-02-05")) is None

    def test_finds_by_short_month_name(self) -> None:
        section = _find_date_section(_CC_STYLE_MD, _date_variants("2026-02-09"))
        assert section is not None
        assert "Marc Alff" in section

    def test_last_section_has_no_boundary(self) -> None:
        # The last date section extends to end-of-document
        section = _find_date_section(_SAMPLE_MD, _date_variants("2026-02-12"))
        assert section is not None
        assert "Someone Else" in section

    def test_plain_text_date_found(self) -> None:
        section = _find_date_section(_PLAIN_DATE_MD, _date_variants("2026-02-11"))
        assert section is not None
        assert "Juliano Costa" in section

    def test_plain_text_section_excludes_next_date(self) -> None:
        section = _find_date_section(_PLAIN_DATE_MD, _date_variants("2026-02-11"))
        assert section is not None
        assert "Cyrille Le Clerc" not in section

    def test_plain_text_last_section_extends_to_eof(self) -> None:
        section = _find_date_section(_PLAIN_DATE_MD, _date_variants("2026-01-28"))
        assert section is not None
        assert "Cyrille Le Clerc" in section


# ---------------------------------------------------------------------------
# _extract_subsection_md
# ---------------------------------------------------------------------------


class TestExtractSubsectionMd:
    def _section(self, md: str = _SAMPLE_MD, date: str = "2026-02-05") -> str:
        s = _find_date_section(md, _date_variants(date))
        assert s is not None
        return s

    def test_extracts_attendees(self) -> None:
        section = self._section()
        result = _extract_subsection_md(section, "attendee")
        assert result == ["- Tyler Benson", "- Damien Mathieu", "- Sam Xie"]

    def test_extracts_agenda(self) -> None:
        section = self._section()
        result = _extract_subsection_md(section, "agenda")
        assert result == ["- SDK update", "- KubeCon planning"]

    def test_attendees_dont_bleed_into_agenda(self) -> None:
        section = self._section()
        attendees = _extract_subsection_md(section, "attendee")
        assert "- SDK update" not in attendees

    def test_agenda_doesnt_include_attendees(self) -> None:
        section = self._section(date="2026-01-22")
        agenda = _extract_subsection_md(section, "agenda")
        assert "- Alice Smith" not in agenda

    def test_returns_empty_when_subsection_missing(self) -> None:
        section = self._section()
        result = _extract_subsection_md(section, "action items")
        assert result == []

    def test_case_insensitive_keyword(self) -> None:
        section = self._section()
        assert _extract_subsection_md(section, "ATTENDEE") == _extract_subsection_md(
            section, "attendee"
        )

    def test_nested_items_produce_indented_lines(self) -> None:
        section = self._section(_NESTED_MD)
        result = _extract_subsection_md(section, "agenda")
        assert result == ["- Upstream", "  - Spec", "  - Semantic conventions", "- SDK"]

    def test_deep_nesting(self) -> None:
        section = self._section(_CC_STYLE_MD, date="2026-02-09")
        agenda = _extract_subsection_md(section, "agenda")
        assert "- Upstream" in agenda
        assert "  - [Spec](https://github.com/open-telemetry/opentelemetry-specification)" in agenda
        assert "    - Mark declarative config as stable#4568" in agenda
        assert "      - Almost there" in agenda

    def test_links_preserved(self) -> None:
        section = self._section(_LINK_MD)
        result = _extract_subsection_md(section, "agenda")
        spec_issue_url = "https://github.com/open-telemetry/opentelemetry-specification/issues/123"
        assert f"- Review [Issue 123]({spec_issue_url})" in result
        assert "- Visit [example](https://example.com)" in result

    def test_backslash_escapes_removed_in_items(self) -> None:
        section = self._section(_CC_STYLE_MD, date="2026-02-09")
        agenda = _extract_subsection_md(section, "agenda")
        # \[Marc\] \- should become [Marc] -
        assert any("[Marc] - PR cleanup needed" in item for item in agenda)

    def test_trailing_soft_break_spaces_stripped(self) -> None:
        # Lines ending with "  " (soft break) should not produce trailing spaces
        section = self._section(_CC_STYLE_MD, date="2026-02-09")
        attendees = _extract_subsection_md(section, "attendee")
        assert all(not item.endswith("  ") for item in attendees)

    def test_plain_text_date_attendees_no_colon(self) -> None:
        # Labels without colons ("Attendees" not "Attendees:")
        section = self._section(_PLAIN_DATE_MD, "2026-02-11")
        attendees = _extract_subsection_md(section, "attendee")
        assert "- Juliano Costa (Datadog)" in attendees
        assert "- Juande Manjon" in attendees

    def test_plain_text_date_agenda_no_colon(self) -> None:
        section = self._section(_PLAIN_DATE_MD, "2026-02-11")
        agenda = _extract_subsection_md(section, "agenda")
        assert any("Add OpAMP to the Demo" in item for item in agenda)
        assert any("Docker minimal is broken" in item for item in agenda)

    def test_plain_text_date_agenda_nested(self) -> None:
        section = self._section(_PLAIN_DATE_MD, "2026-02-11")
        agenda = _extract_subsection_md(section, "agenda")
        assert any("Some sub-item" in item for item in agenda)

    def test_plain_text_attendees_dont_bleed_into_agenda(self) -> None:
        section = self._section(_PLAIN_DATE_MD, "2026-02-11")
        attendees = _extract_subsection_md(section, "attendee")
        assert not any("OpAMP" in item for item in attendees)

    def test_inline_attendees_on_label_line(self) -> None:
        # "Attendees: Alice, Bob" style — content on the same line as the label.
        section = "Attendees: Alice Smith, Bob Jones\n\nAgenda:\n\n- Item 1\n"
        attendees = _extract_subsection_md(section, "attendee")
        assert "- Alice Smith" in attendees
        assert "- Bob Jones" in attendees

    def test_inline_single_attendee_on_label_line(self) -> None:
        section = "Attendees: Alice Smith\n\n- Bob Jones\n"
        attendees = _extract_subsection_md(section, "attendee")
        assert "- Alice Smith" in attendees
        assert "- Bob Jones" in attendees

    def test_inline_attendees_not_in_agenda(self) -> None:
        section = "Attendees: Alice, Bob\n\nAgenda:\n\n- Plan review\n"
        attendees = _extract_subsection_md(section, "attendee")
        agenda = _extract_subsection_md(section, "agenda")
        assert not any("Plan review" in item for item in attendees)
        assert not any("Alice" in item for item in agenda)


# ---------------------------------------------------------------------------
# DevEx SIG style: bold labels (**Attendees:**) + dash bullets (- )
# ---------------------------------------------------------------------------


class TestDevExStyle:
    """Regression tests for docs that use **Bold:** labels and dash bullets."""

    def _section(self) -> str:
        s = _find_date_section(_DEVEX_STYLE_MD, _date_variants("2026-02-18"))
        assert s is not None
        return s

    def test_finds_date_section(self) -> None:
        assert self._section() is not None

    def test_bold_label_attendees_extracted(self) -> None:
        attendees = _extract_subsection_md(self._section(), "attendee")
        assert "- Juliano Costa (Datadog)" in attendees
        assert "- Johanna Öjeling (Grafana Labs)" in attendees

    def test_bold_label_agenda_extracted(self) -> None:
        agenda = _extract_subsection_md(self._section(), "agenda")
        assert "- Release process" in agenda

    def test_attendees_dont_bleed_into_agenda(self) -> None:
        attendees = _extract_subsection_md(self._section(), "attendee")
        assert not any("MCP" in item for item in attendees)

    def test_agenda_nested_items(self) -> None:
        agenda = _extract_subsection_md(self._section(), "agenda")
        assert "- \\[Nico\\] MCP updates".replace("\\[", "[").replace("\\]", "]") or any(
            "MCP updates" in item for item in agenda
        )
        assert any("No TC sponsor" in item for item in agenda)
        assert any("Re-scope" in item for item in agenda)

    def test_dash_bullets_matched(self) -> None:
        # Ensure dash-bullet items are collected (not just asterisk bullets)
        agenda = _extract_subsection_md(self._section(), "agenda")
        assert len(agenda) > 0


# ---------------------------------------------------------------------------
# Arrow-SIG style: plain-text date with extra content after date variant
# ---------------------------------------------------------------------------


class TestArrowStyle:
    def _section(self, date: str = "2026-02-19") -> str:
        s = _find_date_section(_ARROW_STYLE_MD, _date_variants(date))
        assert s is not None
        return s

    def test_finds_date_with_extra_content(self) -> None:
        assert self._section() is not None

    def test_attendees_extracted(self) -> None:
        attendees = _extract_subsection_md(self._section(), "attendee")
        assert "- Brett Mitchell (ElastiFlow)" in attendees
        assert "- Aaron Marten (Microsoft)" in attendees

    def test_agenda_extracted(self) -> None:
        agenda = _extract_subsection_md(self._section(), "agenda")
        assert any("New member" in item for item in agenda)

    def test_section_boundary_at_next_date(self) -> None:
        section = self._section("2026-02-19")
        assert "Joshua MacDonald" not in section

    def test_second_date_found(self) -> None:
        assert self._section("2026-02-10") is not None


# ---------------------------------------------------------------------------
# NET SIG style: day-first date format ("17 Feb 2026")
# ---------------------------------------------------------------------------


class TestNetStyle:
    def _section(self, date: str = "2026-02-17") -> str:
        s = _find_date_section(_NET_STYLE_MD, _date_variants(date))
        assert s is not None
        return s

    def test_finds_day_first_date(self) -> None:
        assert self._section() is not None

    def test_attendees_extracted(self) -> None:
        attendees = _extract_subsection_md(self._section(), "attendee")
        assert "- Matthew Hensley (Grafana Labs)" in attendees

    def test_agenda_extracted(self) -> None:
        agenda = _extract_subsection_md(self._section(), "agenda")
        assert any("Logs bridge" in item for item in agenda)

    def test_section_boundary_at_next_date(self) -> None:
        assert "Martin Costello" not in self._section("2026-02-17")

    def test_second_date_found(self) -> None:
        assert self._section("2026-02-10") is not None


# ---------------------------------------------------------------------------
# RPC SIG style: bold paragraph with weekday prefix + ordinal suffix
# ---------------------------------------------------------------------------


class TestRpcStyle:
    def _section(self, date: str = "2026-02-18") -> str:
        s = _find_date_section(_RPC_STYLE_MD, _date_variants(date))
        assert s is not None
        return s

    def test_finds_bold_ordinal_date(self) -> None:
        assert self._section() is not None

    def test_attendees_extracted(self) -> None:
        attendees = _extract_subsection_md(self._section(), "attendee")
        assert "- Trask" in attendees
        assert "- Liudmila" in attendees

    def test_agenda_extracted(self) -> None:
        agenda = _extract_subsection_md(self._section(), "agenda")
        assert any("Project board" in item for item in agenda)

    def test_section_boundary_at_next_date(self) -> None:
        assert "Steve" not in self._section("2026-02-18")

    def test_second_date_found(self) -> None:
        assert self._section("2026-02-11") is not None


# ---------------------------------------------------------------------------
# Java SIG style: heading with bold + ordinal suffix
# ---------------------------------------------------------------------------


class TestJavaStyle:
    def _section(self, date: str = "2026-02-19") -> str:
        s = _find_date_section(_JAVA_STYLE_MD, _date_variants(date))
        assert s is not None
        return s

    def test_finds_heading_with_ordinal(self) -> None:
        assert self._section() is not None

    def test_attendees_extracted(self) -> None:
        attendees = _extract_subsection_md(self._section(), "attendee")
        assert "- John Watson (Sublime Security)" in attendees

    def test_agenda_extracted(self) -> None:
        agenda = _extract_subsection_md(self._section(), "agenda")
        assert any("issue triage" in item.lower() for item in agenda)

    def test_section_boundary_at_next_heading(self) -> None:
        assert "Jay DeLuca" not in self._section("2026-02-19")

    def test_second_date_found(self) -> None:
        assert self._section("2026-02-12") is not None


# ---------------------------------------------------------------------------
# Dotted-month style: "Feb. 18, 2026" headings + Topics label
# ---------------------------------------------------------------------------


class TestDottedMonthStyle:
    def _section(self, date: str = "2026-02-18") -> str:
        s = _find_date_section(_DOTTED_MONTH_MD, _date_variants(date))
        assert s is not None
        return s

    def test_finds_dotted_month_heading(self) -> None:
        assert self._section() is not None

    def test_attendees_extracted(self) -> None:
        attendees = _extract_subsection_md(self._section(), "attendee")
        assert "- Yoshi Yamaguchi (AWS)" in attendees

    def test_topics_extracted_as_agenda_fallback(self) -> None:
        section = self._section()
        # Topics extracted via "topic" keyword
        topics = _extract_subsection_md(section, "topic")
        assert any("Drifted" in item for item in topics)

    def test_section_boundary(self) -> None:
        assert "Jan" not in self._section("2026-02-18")


# ---------------------------------------------------------------------------
# Notes-label style: "Notes" section as agenda fallback (Collector-SIG)
# ---------------------------------------------------------------------------


class TestNotesLabelStyle:
    def _section(self, date: str = "2026-02-18") -> str:
        s = _find_date_section(_NOTES_LABEL_MD, _date_variants(date))
        assert s is not None
        return s

    def test_finds_date_with_pipe_suffix(self) -> None:
        assert self._section() is not None

    def test_attendees_extracted(self) -> None:
        attendees = _extract_subsection_md(self._section(), "attendee")
        assert "- Evan Bradley (Dynatrace)" in attendees

    def test_notes_extracted_as_note_keyword(self) -> None:
        notes = _extract_subsection_md(self._section(), "note")
        assert any("high priority" in item.lower() for item in notes)

    def test_section_boundary(self) -> None:
        assert "Someone Else" not in self._section("2026-02-18")


# ---------------------------------------------------------------------------
# fetch_meeting_notes (integration via mocked HTTP)
# ---------------------------------------------------------------------------


class TestFetchMeetingNotes:
    def setup_method(self) -> None:
        # Clear the in-process cache so tests don't influence each other.
        gdoc._DOC_CACHE.clear()

    def _mock_resp(self, md: str = _SAMPLE_MD) -> MagicMock:
        mock = MagicMock()
        mock.text = md
        mock.raise_for_status = MagicMock()
        return mock

    def test_happy_path_attendees(self) -> None:
        with patch("scraper.gdoc.requests.get", return_value=self._mock_resp()):
            result = fetch_meeting_notes(
                "https://docs.google.com/document/d/ABC/edit", "2026-02-05"
            )
        assert result["attendees"] == ["- Tyler Benson", "- Damien Mathieu", "- Sam Xie"]

    def test_happy_path_agenda(self) -> None:
        with patch("scraper.gdoc.requests.get", return_value=self._mock_resp()):
            result = fetch_meeting_notes(
                "https://docs.google.com/document/d/ABC/edit", "2026-02-05"
            )
        assert result["agenda"] == ["- SDK update", "- KubeCon planning"]

    def test_date_not_found_returns_empty(self) -> None:
        with patch("scraper.gdoc.requests.get", return_value=self._mock_resp()):
            result = fetch_meeting_notes(
                "https://docs.google.com/document/d/ABC/edit", "2099-12-31"
            )
        assert result == {"attendees": [], "agenda": []}

    def test_invalid_doc_url_returns_empty(self) -> None:
        result = fetch_meeting_notes("https://example.com/not-a-doc", "2026-02-05")
        assert result == {"attendees": [], "agenda": []}

    def test_network_error_returns_empty(self) -> None:
        with patch(
            "scraper.gdoc.requests.get",
            side_effect=gdoc.requests.RequestException("timeout"),
        ):
            result = fetch_meeting_notes(
                "https://docs.google.com/document/d/ABC/edit", "2026-02-05"
            )
        assert result == {"attendees": [], "agenda": []}

    def test_http_error_returns_empty(self) -> None:
        mock = MagicMock()
        mock.raise_for_status.side_effect = gdoc.requests.HTTPError("403")
        with patch("scraper.gdoc.requests.get", return_value=mock):
            result = fetch_meeting_notes(
                "https://docs.google.com/document/d/ABC/edit", "2026-02-05"
            )
        assert result == {"attendees": [], "agenda": []}

    def test_returns_empty_for_empty_doc(self) -> None:
        with patch(
            "scraper.gdoc.requests.get",
            return_value=self._mock_resp(""),
        ):
            result = fetch_meeting_notes(
                "https://docs.google.com/document/d/ABC/edit", "2026-02-05"
            )
        assert result == {"attendees": [], "agenda": []}

    def test_caches_document(self) -> None:
        mock_get = MagicMock(return_value=self._mock_resp())
        with patch("scraper.gdoc.requests.get", mock_get):
            fetch_meeting_notes("https://docs.google.com/document/d/ABC/edit", "2026-02-05")
            fetch_meeting_notes("https://docs.google.com/document/d/ABC/edit", "2026-02-12")
        # Second call must use cache — only one HTTP request
        assert mock_get.call_count == 1

    def test_empty_md_falls_back_to_txt(self) -> None:
        """When the Markdown export is empty, the plain-text export should be tried."""
        empty_resp = MagicMock()
        empty_resp.text = "   "  # whitespace only → .strip() == ""
        empty_resp.raise_for_status = MagicMock()

        real_resp = MagicMock()
        real_resp.text = _SAMPLE_MD
        real_resp.raise_for_status = MagicMock()

        with patch("scraper.gdoc.requests.get", side_effect=[empty_resp, real_resp]) as mock_get:
            result = fetch_meeting_notes(
                "https://docs.google.com/document/d/ABC/edit", "2026-02-05"
            )
        assert mock_get.call_count == 2
        assert result["attendees"] != []

    def test_previous_day_fallback(self) -> None:
        """If the target date is not found, the day before should be tried."""
        doc = "# 2026-02-04\n\nAttendee:\n\n* Tyler\n\nAgenda:\n\n* Test item\n"
        with patch("scraper.gdoc.requests.get", return_value=self._mock_resp(doc)):
            result = fetch_meeting_notes(
                "https://docs.google.com/document/d/ABC/edit", "2026-02-05"
            )
        assert "- Tyler" in result["attendees"]
        assert any("Test item" in item for item in result["agenda"])

    def test_invalid_date_format_returns_empty(self) -> None:
        """An unparseable date string must not raise; prev-day fallback is skipped."""
        doc = "# 2026-02-04\n\nAttendee:\n\n* Tyler\n\nAgenda:\n\n* Test item\n"
        with patch("scraper.gdoc.requests.get", return_value=self._mock_resp(doc)):
            result = fetch_meeting_notes(
                "https://docs.google.com/document/d/ABC/edit", "not-a-date"
            )
        assert result == {"attendees": [], "agenda": []}


# ---------------------------------------------------------------------------
# _date_variants — localized month abbreviations
# ---------------------------------------------------------------------------


class TestDateVariantsLocalized:
    def test_polish_february_lut(self) -> None:
        variants = _date_variants("2026-02-05")
        assert "5 lut 2026" in variants
        assert "05 lut 2026" in variants

    def test_polish_january_sty(self) -> None:
        variants = _date_variants("2026-01-15")
        assert "15 sty 2026" in variants

    def test_polish_december_gru(self) -> None:
        variants = _date_variants("2026-12-03")
        assert "3 gru 2026" in variants


# ---------------------------------------------------------------------------
# _extract_leading_attendees
# ---------------------------------------------------------------------------


class TestExtractLeadingAttendees:
    def test_collects_leading_bullets(self) -> None:
        section = "* Alice\n* Bob\n\nAgenda\n\n* Item 1\n"
        result = _extract_leading_attendees(section)
        assert result == ["- Alice", "- Bob"]

    def test_stops_at_non_list_line(self) -> None:
        section = "* Alice\n* Bob\nSome label:\n* Charlie\n"
        result = _extract_leading_attendees(section)
        assert result == ["- Alice", "- Bob"]

    def test_empty_section_returns_empty(self) -> None:
        assert _extract_leading_attendees("") == []

    def test_no_leading_bullets_returns_empty(self) -> None:
        section = "Some heading\n* Alice\n"
        assert _extract_leading_attendees(section) == []

    def test_skips_blank_lines(self) -> None:
        section = "\n* Alice\n\n* Bob\n\nSome prose\n"
        result = _extract_leading_attendees(section)
        assert "- Alice" in result
        assert "- Bob" in result

    def test_skips_empty_placeholder_items(self) -> None:
        section = "* Alice\n* \n* Bob\n"
        result = _extract_leading_attendees(section)
        assert "- Alice" in result
        assert "- Bob" in result
        assert len([r for r in result if not r.strip("- ")]) == 0

    def test_dash_bullets_supported(self) -> None:
        section = "- Alice Smith\n- Bob Jones\n\nAgenda\n"
        result = _extract_leading_attendees(section)
        assert "- Alice Smith" in result
        assert "- Bob Jones" in result
