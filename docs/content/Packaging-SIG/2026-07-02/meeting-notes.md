## Meeting Notes

### Attendees
- Sina P (Canonical)
- Michele Mancioppi (Dash0)
- Diego Hurtado (Dash0)
- Bastian Krol (Dash0)
- Antoine Toulme (Splunk)

### Agenda
- Misalignment between packages, declarative configuration and otel injector:
  - We currently need to have different config files for different languages (as most SDKs do not yet support the Instrumentation overrides for languages), but the Injector cannot inject different env vars for OTEL_CONFIG_FILE based on different languages because it does not really know *what language* it inject (it sets the env vars for all)
  - .NET is the least likely of the launch languages (Node, Java, .NET, Python) to support the declarative config options [we need](https://github.com/open-telemetry/opentelemetry-configuration/blob/main/schema/instrumentation.yaml) in the foreseeable future (Antoine to follow up)
  - We *could* start with the env injection of the Injector to set OTLP endpoints and all, but that would then require some sort of migration to declarative configuration, and ideally that migration would be before the first non-draft release.
- Add an interface to the OTel Collector packages and describe it in [https://github.com/open-telemetry/opentelemetry-packaging/pull/10/](https://github.com/open-telemetry/opentelemetry-packaging/pull/10/)
