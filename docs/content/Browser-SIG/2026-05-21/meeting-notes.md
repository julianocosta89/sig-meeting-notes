## Meeting Notes

### Attendees
- Jared Freeze (Embrace)
- Joaquin Diaz (Embrace)
- David Luna (Elastic)
- Hugo Levy (Datadog)
- Maxime Quentin (Datadog)

### Agenda
- [martin] Event display message
  - proposed here [https://github.com/open-telemetry/opentelemetry-browser/pull/282](https://github.com/open-telemetry/opentelemetry-browser/pull/282)
  - added this issue in sem conv [https://github.com/open-telemetry/semantic-conventions/issues/3724](https://github.com/open-telemetry/semantic-conventions/issues/3724)
- [david] [https://github.com/open-telemetry/opentelemetry-js/pull/6729](https://github.com/open-telemetry/opentelemetry-js/pull/6729)
  - Noticed user agent is not set always
    - Semantic conventions [note](https://github.com/open-telemetry/semantic-conventions/blob/8faf5c44488667d2a819fc349c5997be7070caac/model/browser/entities.yaml#L18)
  - But userAgentData is not baseline. Possible segmentation
    - Most of desktops are chromium (API available) but most mobile are Safari (API unavailable)
  - **Conclusion:** Include UA always so
    - Update semvconv note to reflect that
    - Update browser detector accordingly
- Document URL / Session ID as entities
  - prototype PR ​​[https://github.com/open-telemetry/opentelemetry-browser/pull/269](https://github.com/open-telemetry/opentelemetry-browser/pull/269)
  - discussion topic [https://github.com/open-telemetry/opentelemetry-browser/discussions/265](https://github.com/open-telemetry/opentelemetry-browser/discussions/265)
