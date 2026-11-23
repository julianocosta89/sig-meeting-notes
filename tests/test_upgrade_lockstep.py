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


UPGRADED_LOCK = LOCK
OLD_LOCK = LOCK.replace('"0.66b2"', '"0.62b1"').replace('"1.45.2"', '"1.41.1"')


def _project(tmp_path: Path) -> Path:
    (tmp_path / "pyproject.toml").write_text(PYPROJECT)
    (tmp_path / "uv.lock").write_text(OLD_LOCK)
    return tmp_path


class TestUpgrade:
    def test_upgrades_family_and_repins(self, tmp_path, monkeypatch):
        root = _project(tmp_path)
        calls: list[tuple[str, ...]] = []

        def fake_uv(*args: str) -> None:
            calls.append(args)
            if "--upgrade-package" in args:
                (root / "uv.lock").write_text(UPGRADED_LOCK)

        monkeypatch.setattr(upgrade_lockstep, "_uv", fake_uv)
        changes = upgrade_lockstep.upgrade(root, PREFIXES)

        assert changes == {
            "opentelemetry-distro": ("0.62b1", "0.66b2"),
            "opentelemetry-exporter-otlp-proto-http": ("1.41.1", "1.45.2"),
        }
        text = (root / "pyproject.toml").read_text()
        assert '"opentelemetry-distro==0.66b2"' in text
        assert '"requests==2.34.2"' in text
        # Only the opentelemetry-* family is upgraded; requests stays locked
        assert calls[0] == (
            "lock",
            "--directory",
            str(root),
            "--upgrade-package",
            "opentelemetry-distro",
            "--upgrade-package",
            "opentelemetry-exporter-otlp-proto-http",
        )
        assert calls[1] == ("lock", "--directory", str(root))

    def test_no_matching_pins_is_noop(self, tmp_path, monkeypatch):
        root = _project(tmp_path)
        monkeypatch.setattr(upgrade_lockstep, "_uv", lambda *a: pytest.fail("uv called"))
        assert upgrade_lockstep.upgrade(root, ("nothing-",)) == {}

    def test_failure_restores_files(self, tmp_path, monkeypatch):
        root = _project(tmp_path)

        def failing_uv(*args: str) -> None:
            (root / "uv.lock").write_text("broken")
            raise RuntimeError("resolution failed")

        monkeypatch.setattr(upgrade_lockstep, "_uv", failing_uv)
        with pytest.raises(RuntimeError, match="resolution failed"):
            upgrade_lockstep.upgrade(root, PREFIXES)
        assert (root / "pyproject.toml").read_text() == PYPROJECT
        assert (root / "uv.lock").read_text() == OLD_LOCK


class TestUvRunner:
    def test_missing_uv_raises(self, monkeypatch):
        monkeypatch.setattr(upgrade_lockstep.shutil, "which", lambda _: None)
        with pytest.raises(RuntimeError, match="uv not found"):
            upgrade_lockstep._uv("lock")

    def test_runs_uv_with_check(self, monkeypatch):
        seen = {}
        monkeypatch.setattr(upgrade_lockstep.shutil, "which", lambda _: "/bin/uv")
        monkeypatch.setattr(
            upgrade_lockstep.subprocess, "run", lambda cmd, check: seen.update(cmd=cmd, check=check)
        )
        upgrade_lockstep._uv("lock", "--directory", "x")
        assert seen == {"cmd": ["/bin/uv", "lock", "--directory", "x"], "check": True}
