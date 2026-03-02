## Meeting Notes

### Attendees
            - John Scancella
            - Ridhima Satam(Cisco/Splunk)
            - Riccardo Magliocchetti (Elastic)
            - Tammy Baylis (SolarWinds)
            - Dylan Russell (google)
            - Aaron Abbott (Google)
            - Sergey Sergeev (Cisco/Splunk)
            - Jeremy Voss (Microsoft)

### Agenda
            - [Tammy] A new Labeler for custom attributes applied to metrics – thoughts?
            - Prototype: https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3689
            - Inspired by Go net/http instrumentation: https://github.com/open-telemetry/opentelemetry-go-contrib/pull/306
            - For Python, one shared util between several instrumentors (Flask, Django, Falcon, WSGI, ASGI) and up to each to merge custom with base attributes
            - Aaron:
            - Please double check if semantic conventions have an opinion on adding out of spec attributes
            - What about baggage? May not do what we need but can be related
            - Slack thread about baggage https://cloud-native.slack.com/archives/C06KR7ARS3X/p1754512743348209
            - [Riccardo] Refreshed PR for being able to override (but not remove) default headers in OTLP http exporter https://github.com/open-telemetry/opentelemetry-python/pull/4634
            - Some discussion to add it explicitly to documentation here https://github.com/open-telemetry/opentelemetry-specification/pull/4560/
            - [Ridhima 1 min] - Asking maintainers review on,
            - Langchain llm span support: https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3665
            - Aaron:
            - Double tracing for request/response from both langchain and client library
            - E.g. token usage double accounting would be a problem
            - Riccardo:
            - Maybe start slim and then add attributes when the use case requires them?
            - Sergey: We may not have an instrumentation for underlying client library
            - GenAI Utils Structure PR: https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3672
            - [Sergey 10m] Translator/Adaptor approaches for 3rd-party OSS instrumentation libraries to convert other telemetry to OTel semconvs
            - generic callback implementation from zero-code instrumentation
            - https://github.com/open-telemetry/opentelemetry-python/blob/b1cf152324e2a7d475cd9907debc66119eef51f9/opentelemetry-sdk/src/opentelemetry/sdk/trace/__init__.py#L92
            - https://github.com/open-telemetry/opentelemetry-python/blob/b1cf152324e2a7d475cd9907debc66119eef51f9/opentelemetry-sdk/src/opentelemetry/sdk/_configuration/__init__.py
