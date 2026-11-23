"""Tests for scripts/upgrade_lockstep.py (pure pin-rewriting helpers)."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

_SPEC = importlib.util.spec_from_file_location(
    "upgrade_lockstep", Path(__file__).parent.parent / "scripts" / "upgrade_lockstep.py"
)
upgrade_lockstep = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(upgrade_lockstep)

PREFIXES = ("opentelemetry-",)

PYPROJECT = """\
[project]
dependencies = [
    "requests==2.34.2",
]

[dependency-groups]
summarize = ["anthropic==2.7.0"]
telemetry = [
    "opentelemetry-distro==0.62b1",
    "opentelemetry-exporter-otlp-proto-http==1.41.1",
]
"""

LOCK = """\
version = 1

[[package]]
name = "opentelemetry-distro"
version = "0.66b2"

[[package]]
name = "opentelemetry-exporter-otlp-proto-http"
version = "1.45.2"

[[package]]
name = "requests"
version = "2.34.2"

[[package]]
name = "otel-recordings"
source = { editable = "." }
"""


class TestFindPins:
    def test_only_matching_prefix(self):
        assert upgrade_lockstep.find_pins(PYPROJECT, PREFIXES) == {
            "opentelemetry-distro": "0.62b1",
            "opentelemetry-exporter-otlp-proto-http": "1.41.1",
        }

    def test_prefix_match_is_normalized(self):
        text = '"OpenTelemetry_Distro==0.62b1"'
        assert upgrade_lockstep.find_pins(text, PREFIXES) == {"OpenTelemetry_Distro": "0.62b1"}


class TestRelaxPins:
    def test_relaxes_matching_and_keeps_others(self):
        relaxed = upgrade_lockstep.relax_pins(PYPROJECT, PREFIXES)
        assert '"opentelemetry-distro>=0.62b1"' in relaxed
        assert '"opentelemetry-exporter-otlp-proto-http>=1.41.1"' in relaxed
        assert '"requests==2.34.2"' in relaxed
        assert '"anthropic==2.7.0"' in relaxed


class TestRepin:
    def test_round_trip_to_locked_versions(self):
        relaxed = upgrade_lockstep.relax_pins(PYPROJECT, PREFIXES)
        versions = upgrade_lockstep.locked_versions(LOCK)
        repinned = upgrade_lockstep.repin(relaxed, versions, PREFIXES)
        assert upgrade_lockstep.find_pins(repinned, PREFIXES) == {
            "opentelemetry-distro": "0.66b2",
            "opentelemetry-exporter-otlp-proto-http": "1.45.2",
        }
        assert '"requests==2.34.2"' in repinned

    def test_missing_from_lock_raises(self):
        relaxed = upgrade_lockstep.relax_pins(PYPROJECT, PREFIXES)
        with pytest.raises(KeyError, match="opentelemetry-distro"):
            upgrade_lockstep.repin(relaxed, {}, PREFIXES)


class TestLockedVersions:
    def test_skips_packages_without_version(self):
        versions = upgrade_lockstep.locked_versions(LOCK)
        assert versions["opentelemetry-distro"] == "0.66b2"
        assert "otel-recordings" not in versions
