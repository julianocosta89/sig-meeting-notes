"""Shared OpenTelemetry tracer setup for CLI scripts.

Returns a real tracer when ``OTEL_EXPORTER_OTLP_ENDPOINT`` is set and the
``opentelemetry-distro`` package is installed.  Falls back silently to a
no-op tracer so scripts work unchanged when telemetry is not configured.
"""

from __future__ import annotations

import atexit
import contextlib
import os
from collections.abc import Generator
from typing import Protocol

try:
    from opentelemetry.trace import StatusCode
except ImportError:
    from enum import Enum

    class StatusCode(Enum):  # type: ignore[no-redef]
        UNSET = 0
        OK = 1
        ERROR = 2


class _Tracer(Protocol):
    def start_as_current_span(
        self, name: str, **kwargs: object
    ) -> contextlib.AbstractContextManager[object]: ...


class _NoOpSpan:
    def set_attribute(self, key: str, value: object) -> None:  # noqa: ARG002
        pass

    def set_status(self, status: object, description: str = "") -> None:  # noqa: ARG002
        pass

    def record_exception(self, exception: Exception, **kwargs: object) -> None:  # noqa: ARG002
        pass


@contextlib.contextmanager
def _noop_ctx() -> Generator[_NoOpSpan]:
    yield _NoOpSpan()


class _NoOpTracer:
    def start_as_current_span(  # noqa: ARG002
        self, name: str, **kwargs: object
    ) -> contextlib.AbstractContextManager[_NoOpSpan]:
        return _noop_ctx()


def configure_tracer(service_name: str) -> _Tracer:
    """Return a tracer for *service_name*.

    Reads ``OTEL_EXPORTER_OTLP_ENDPOINT`` and ``OTEL_EXPORTER_OTLP_HEADERS``
    from the environment (standard OTel SDK env vars).  Set
    ``OTEL_SERVICE_NAME`` to override the service name reported to the backend.

    Returns a ``_NoOpTracer`` when the endpoint is not configured or when the
    ``opentelemetry`` packages are not installed.
    """
    endpoint = os.environ.get("OTEL_EXPORTER_OTLP_ENDPOINT", "").strip()
    if not endpoint:
        return _NoOpTracer()

    try:
        from opentelemetry import trace  # noqa: PLC0415
        from opentelemetry._logs import set_logger_provider  # noqa: PLC0415
        from opentelemetry.exporter.otlp.proto.http._log_exporter import (  # noqa: PLC0415
            OTLPLogExporter,
        )
        from opentelemetry.exporter.otlp.proto.http.trace_exporter import (  # noqa: PLC0415
            OTLPSpanExporter,
        )
        from opentelemetry.sdk._logs import LoggerProvider  # noqa: PLC0415
        from opentelemetry.sdk._logs.export import BatchLogRecordProcessor  # noqa: PLC0415
        from opentelemetry.sdk.resources import Resource  # noqa: PLC0415
        from opentelemetry.sdk.trace import TracerProvider  # noqa: PLC0415
        from opentelemetry.sdk.trace.export import SimpleSpanProcessor  # noqa: PLC0415
    except ImportError:
        return _NoOpTracer()

    svc_name = os.environ.get("OTEL_SERVICE_NAME", service_name)  # pragma: no cover
    resource = Resource.create({"service.name": svc_name})  # pragma: no cover

    provider = TracerProvider(resource=resource)  # pragma: no cover
    provider.add_span_processor(SimpleSpanProcessor(OTLPSpanExporter()))  # pragma: no cover
    trace.set_tracer_provider(provider)  # pragma: no cover

    log_provider = LoggerProvider(resource=resource)  # pragma: no cover
    log_provider.add_log_record_processor(
        BatchLogRecordProcessor(OTLPLogExporter())
    )  # pragma: no cover
    set_logger_provider(log_provider)  # pragma: no cover

    try:  # pragma: no cover
        from opentelemetry.instrumentation.logging import LoggingInstrumentor  # noqa: PLC0415

        # set_logger_provider() must be called before instrument() so the handler
        # it installs picks up our configured LoggerProvider instead of the no-op default.
        # set_logging_format=False (default): inject OTel attributes into LogRecords for
        # backend correlation without overriding the script's own log format string.
        # Overriding the format string would break uninstrument() on shutdown because
        # the format is not restored, causing KeyError on %(otelTraceID)s in log records.
        LoggingInstrumentor().instrument(set_logging_format=False)
    except Exception:  # noqa: BLE001, S110  # pragma: no cover
        pass

    try:  # pragma: no cover
        from opentelemetry.instrumentation.requests import RequestsInstrumentor  # noqa: PLC0415

        RequestsInstrumentor().instrument()
    except Exception:  # noqa: BLE001, S110  # pragma: no cover
        pass

    try:  # pragma: no cover
        from opentelemetry.instrumentation.openai_v2 import OpenAIInstrumentor  # noqa: PLC0415

        OpenAIInstrumentor().instrument()
    except Exception as exc:  # noqa: BLE001  # pragma: no cover
        import logging  # noqa: PLC0415

        logging.getLogger(__name__).warning("OpenAI instrumentation failed: %s", exc)

    def _shutdown() -> None:  # pragma: no cover
        # TracerProvider and LoggerProvider each register their own atexit handlers
        # when constructed (before this closure is registered). Because atexit runs
        # LIFO, this closure runs first — we only need to uninstrument so that the
        # SDK's subsequent atexit calls can shut down the providers cleanly:
        #   - RequestsInstrumentor: prevents OTLP log-export HTTP calls from creating
        #     new spans after the trace provider has been torn down.
        #   - LoggingInstrumentor: prevents SDK shutdown warnings from being forwarded
        #     to the log provider after it has been torn down.
        # Calling provider.shutdown() / log_provider.shutdown() here would cause the
        # SDK's own atexit to see an already-closed exporter and log a warning.
        try:
            from opentelemetry.instrumentation.requests import RequestsInstrumentor  # noqa: PLC0415

            RequestsInstrumentor().uninstrument()
        except Exception:  # noqa: BLE001, S110
            pass
        try:
            from opentelemetry.instrumentation.logging import LoggingInstrumentor  # noqa: PLC0415

            LoggingInstrumentor().uninstrument()
        except Exception:  # noqa: BLE001, S110
            pass

    atexit.register(_shutdown)  # pragma: no cover
    return trace.get_tracer(service_name)  # pragma: no cover
