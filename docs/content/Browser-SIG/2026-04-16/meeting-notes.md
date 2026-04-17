## Meeting Notes

### Attendees
- Jared Freeze (Embrace)
- Joaquin Diaz (Embrace)
- Martin Kuba (Grafana Labs)
- Ted Young (Grafana Labs)
- Hugo Levy (Datadog)
- Maxime Quentin (Datadog)

### Agenda
- [martin] Resource timing semantic conventions
  - draft PR to test in the instrumentation [https://github.com/open-telemetry/opentelemetry-browser/pull/232](https://github.com/open-telemetry/opentelemetry-browser/pull/232)
  - do we use unified or browser-specific conventions?
  - do we report fields as they are provided (relative to time origin), or
    - relative to request start
    - absolute timestamps
    - calculated durations
  - proposal - start with browser-specific and time-origin relative values (mirrors the web API and is simplest approach)
- [maxime] event_name format
  - Spotted a difference between browser.resource.timing and browser.navigation_timing
  - Is there a meaning of this formatting diffs
  - If not can we pick a unique format
  - action item: update resource timing to match navigation timing
- [maxime]
  - Semantic convention inputs for the document.url.full VS browser.url.full
  - [https://github.com/open-telemetry/opentelemetry-browser/issues/174#issuecomment-4091336306](https://github.com/open-telemetry/opentelemetry-browser/issues/174#issuecomment-4091336306)
  - Agreed on the `browser.document.url.full` as an entity
  - No instrumentation for entities yet but the sandbox demo could work on a small POC to provide this entity to all spans and events
