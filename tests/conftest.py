"""Shared pytest fixtures for the test suite."""

from __future__ import annotations

import pytest


@pytest.fixture(autouse=True)
def _no_otel_endpoint(monkeypatch: pytest.MonkeyPatch) -> None:
    """Clear OTEL_EXPORTER_OTLP_ENDPOINT so configure_tracer returns a no-op tracer.

    Without this, any test that calls main() could cause configure_tracer to
    configure the real OTel SDK and instrument the re module via ReInstrumentor.
    That patched re.search breaks pytest's own match= checks in pytest.raises.
    Tests that need a real endpoint set it explicitly via monkeypatch.setenv.
    """
    monkeypatch.delenv("OTEL_EXPORTER_OTLP_ENDPOINT", raising=False)
