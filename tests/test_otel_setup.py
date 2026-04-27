"""Tests for scraper/otel_setup.py."""

from __future__ import annotations

import sys
import unittest.mock

import pytest

from scraper.otel_setup import StatusCode, _NoOpSpan, _NoOpTracer, configure_tracer


def test_configure_tracer_no_endpoint_returns_noop(monkeypatch):
    monkeypatch.delenv("OTEL_EXPORTER_OTLP_ENDPOINT", raising=False)
    tracer = configure_tracer("test-service")
    assert isinstance(tracer, _NoOpTracer)


def test_configure_tracer_empty_endpoint_returns_noop(monkeypatch):
    monkeypatch.setenv("OTEL_EXPORTER_OTLP_ENDPOINT", "   ")
    tracer = configure_tracer("test-service")
    assert isinstance(tracer, _NoOpTracer)


def test_configure_tracer_endpoint_set_but_package_missing_returns_noop(monkeypatch):
    """When OTLP endpoint is set but opentelemetry is not installed, fall back to no-op."""
    monkeypatch.setenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:4318")
    # Simulate the packages being absent by masking all opentelemetry entries in
    # sys.modules — Python raises ImportError on any deferred import that hits None.
    # Explicitly include "opentelemetry" so the import is blocked even when the
    # package is installed but hasn't been imported yet (so sys.modules is empty).
    masked = {k: None for k in sys.modules if k.startswith("opentelemetry")}
    masked["opentelemetry"] = None
    with unittest.mock.patch.dict("sys.modules", masked):
        tracer = configure_tracer("test-service")
    assert isinstance(tracer, _NoOpTracer)


def test_noop_tracer_is_context_manager():
    tracer = _NoOpTracer()
    with tracer.start_as_current_span("my-span") as span:
        assert isinstance(span, _NoOpSpan)


def test_noop_span_set_attribute_is_safe():
    span = _NoOpSpan()
    span.set_attribute("key", "value")
    span.set_attribute("count", 42)


def test_noop_span_set_status_is_safe():
    span = _NoOpSpan()
    span.set_status(StatusCode.ERROR, "something failed")
    span.set_status(StatusCode.OK)


def test_noop_span_record_exception_is_safe():
    span = _NoOpSpan()
    span.record_exception(ValueError("boom"))


def test_noop_tracer_ignores_span_kwargs():
    tracer = _NoOpTracer()
    with tracer.start_as_current_span("span", attributes={"a": 1}, kind="INTERNAL") as span:
        assert isinstance(span, _NoOpSpan)


@pytest.mark.parametrize("service_name", ["refresh", "summarize", "digest", "build-site"])
def test_configure_tracer_returns_noop_for_any_service_name(service_name, monkeypatch):
    monkeypatch.delenv("OTEL_EXPORTER_OTLP_ENDPOINT", raising=False)
    tracer = configure_tracer(service_name)
    assert isinstance(tracer, _NoOpTracer)
