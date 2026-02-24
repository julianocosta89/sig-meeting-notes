## Meeting Notes

### Attendees
- Martin Kuba (Grafana Labs)
- Marco Schaefer (Grafana Labs)
- Joaquin Diaz (Embrace)
- Benoit Zugmeyer (Datadog)
- João Oliveira (Datadog)
- David Luna (Elastic)
- Surbhi A (Cisco)

### Agenda
- [david] Core Web Vitals
  - [https://github.com/open-telemetry/semantic-conventions/blob/main/model/browser/events.yaml](https://github.com/open-telemetry/semantic-conventions/blob/main/model/browser/events.yaml)
  - Is it just an event? Any fields missing?
  - [martin] Semantic conventions need to be updated
    - [https://github.com/open-telemetry/semantic-conventions/issues/3401](https://github.com/open-telemetry/semantic-conventions/issues/3401)
- [martin] Resource timing semantic conventions
  - Proposal for unified conventions [https://github.com/open-telemetry/semantic-conventions/issues/3385](https://github.com/open-telemetry/semantic-conventions/issues/3385)
  - Are we ok with different names than the web API? Does this mapping make sense?
    - [https://github.com/open-telemetry/semantic-conventions/issues/3385#issuecomment-3851132612](https://github.com/open-telemetry/semantic-conventions/issues/3385#issuecomment-3851132612)
  - Alternative - previously proposed dedicated attributes
    - [https://github.com/open-telemetry/semantic-conventions/pull/3069](https://github.com/open-telemetry/semantic-conventions/pull/3069)
  - additional browser attributes
    - [https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming#additional_resource_information](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming#additional_resource_information)
- [martin] Navigation semantic conventions
  - [https://github.com/open-telemetry/semantic-conventions/pull/2806](https://github.com/open-telemetry/semantic-conventions/pull/2806)
  - needs to be finished - request for review / approval
