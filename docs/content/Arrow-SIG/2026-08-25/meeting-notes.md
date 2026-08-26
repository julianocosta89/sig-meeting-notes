## Meeting Notes

### Attendees
- Josh MacDonald (Microsoft)
- Laurent Querel (F5)
- Jake Dern (F5)
- Brian Sapozhnikov (Microsoft)
- Utkarsh Umesan Pillai (Microsoft)
- Drew Relmas (Microsoft)
- Aaron Marten (Microsoft)
- Nikhil Manchanda (Microsoft)
- Albert Lockett (F5)
- Gokhan Uslu (Microsoft)
- Swapnil Ashtekar (Microsoft)

### Agenda
- [Triage]
  - Issues that need to be discussed: [https://github.com/open-telemetry/otel-arrow/issues?q=is%3Aissue%20state%3Aopen%20sort%3Aupdated-desc%20label%3Atriage%3Aneeds-discussion](https://github.com/open-telemetry/otel-arrow/issues?q=is%3Aissue%20state%3Aopen%20sort%3Aupdated-desc%20label%3Atriage%3Aneeds-discussion)
    - About [https://github.com/open-telemetry/otel-arrow/issues/3452](https://github.com/open-telemetry/otel-arrow/issues/3452)
      - Relation to [https://github.com/open-telemetry/otel-arrow/issues/3837](https://github.com/open-telemetry/otel-arrow/issues/3837), [https://github.com/open-telemetry/otel-arrow/issues/3875](https://github.com/open-telemetry/otel-arrow/issues/3875)
      - Stanza ref: [https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/pkg/stanza](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/pkg/stanza)
    - About metrics, duration metrics and booleans vs levels
    - About [https://github.com/open-telemetry/otel-arrow/issues/3848](https://github.com/open-telemetry/otel-arrow/issues/3848) the configuration quagmire
    - About mixed-signal OTAP: long-term vision!
    - About Kafka receiver metrics [https://github.com/open-telemetry/otel-arrow/issues/3860](https://github.com/open-telemetry/otel-arrow/issues/3860)
  - Issues that have just been marked as stale: [https://github.com/open-telemetry/otel-arrow/issues?q=is%3Aissue%20state%3Aopen%20sort%3Aupdated-desc%20label%3Astale](https://github.com/open-telemetry/otel-arrow/issues?q=is%3Aissue%20state%3Aopen%20sort%3Aupdated-desc%20label%3Astale)
- [jmacd] Multiple topics of future direction roughly mapped:
  - [Introduce pluggable PData Arrow batch representations · Issue #3875 · open-telemetry/otel-arrow](https://github.com/open-telemetry/otel-arrow/issues/3875)
  - [Support mixed-signal Pdata · Issue #3876 · open-telemetry/otel-arrow](https://github.com/open-telemetry/otel-arrow/issues/3876)
  - [RFC: Flight Recorder and mixed-signal PData representations by jmacd · Pull Request #3877 · open-telemetry/otel-arrow](https://github.com/open-telemetry/otel-arrow/pull/3877)
  - [Prototype pluggable Arrow internal-log stacktraces by jmacd · Pull Request #3882 · open-telemetry/otel-arrow](https://github.com/open-telemetry/otel-arrow/pull/3882)
