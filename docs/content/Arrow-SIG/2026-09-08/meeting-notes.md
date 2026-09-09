## Meeting Notes

### Attendees
- Josh MacDonald (Microsoft)
- Aaron Marten (Microsoft)
- Albert Lockett (F5)
- Pierre Mariani (contributing privately)
- Laurent Querel (F5)
- Gokhan Uslu (Microsoft)

### Agenda
- [Triage]
  - Issues that need to be discussed: [https://github.com/open-telemetry/otel-arrow/issues?q=is%3Aissue%20state%3Aopen%20sort%3Aupdated-deswc%20label%3Atriage%3Aneeds-discussion](https://github.com/open-telemetry/otel-arrow/issues?q=is%3Aissue%20state%3Aopen%20sort%3Aupdated-desc%20label%3Atriage%3Aneeds-discussion)
  - Issues that have just been marked as stale: [https://github.com/open-telemetry/otel-arrow/issues?q=is%3Aissue%20state%3Aopen%20sort%3Aupdated-desc%20label%3Astale](https://github.com/open-telemetry/otel-arrow/issues?q=is%3Aissue%20state%3Aopen%20sort%3Aupdated-desc%20label%3Astale)
- [feat(context): compile transport header policies by jmacd · Pull Request #4008 · open-telemetry/otel-arrow](https://github.com/open-telemetry/otel-arrow/pull/4008)
- About [https://github.com/open-telemetry/otel-arrow/issues/3992](https://github.com/open-telemetry/otel-arrow/issues/3992)
  - And [https://github.com/open-telemetry/otel-arrow/issues/3848](https://github.com/open-telemetry/otel-arrow/issues/3848)
  - [opentelemetry-collector/confmap/README.md at main · open-telemetry/opentelemetry-collector](https://github.com/open-telemetry/opentelemetry-collector/blob/main/confmap/README.md)
- [Laurent] Diagnostic endpoint and/or dfctl sub-command (First step -> RFC)
  - QA team … providing information to developers w/o sufficient detail
  - Want an easy self-serve diagnostic mechanism, maybe through dfctl CLI
  - Logs, metrics, profiles, etc to assist developers, bundle into a zip file
    - (Is this a flight-recorder?)
  - Ideally a `dfctl replay <flight-recorder-data>` that could attempt to repro
  - Q: Could we use the Quiver to persist a recent window of ITS telemetry?
    - Maybe using a pair of segments, delete after used. Yes, could work. Or, a specialized form. :)
    - Related: [jsuereth/otlp-mmap: Experimental mmap protocol for OTLP](https://github.com/jsuereth/otlp-mmap)
    - Related: [bitdrift - mobile observability](https://bitdrift.io/)
