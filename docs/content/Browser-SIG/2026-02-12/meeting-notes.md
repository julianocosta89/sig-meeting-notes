## Meeting Notes

### Attendees
- Martin Kuba (Grafana)
- Jared Freeze (Embrace)
- João Oliveira (Datadog)

### Agenda
- [david] TODO: context manager thoughts
  - Current state: zone and stack (inside web-trace-sdk)
  - Some issues/requests regarding CM
    - Move stack somewhere else ([issue](https://github.com/open-telemetry/opentelemetry-js/issues/1386))
    - Zoneless CM ([issue](https://github.com/open-telemetry/opentelemetry-js/issues/6211))
  - Web standard progress
    - [Async context proposal](https://github.com/tc39/proposal-async-context/) waiting on web APIs integration
    - Recent progress in webidl
      - [https://github.com/whatwg/html/pull/12152](https://github.com/whatwg/html/pull/12152)
      - [https://github.com/whatwg/webidl/pull/1568](https://github.com/whatwg/webidl/pull/1568)
  - Qs
    - Could stack be moved to the API (and replace Noop)?
    - Knowing we cannot workaround the async/await. Anyone interested in providing a “best effort” CM?
- [jared] fetch/sendBeacon bug is approved but a sanity check from Browser would be great
  - ​​[https://github.com/open-telemetry/opentelemetry-js/pull/6391](https://github.com/open-telemetry/opentelemetry-js/pull/6391)
- [martin,jared] versioning proposals
  - issue with options [https://github.com/open-telemetry/opentelemetry-browser/issues/131#issuecomment-3888872559](https://github.com/open-telemetry/opentelemetry-browser/issues/131#issuecomment-3888872559)
- [martin] Release / publish process
  - looking for help
  - same issue as versioning, but can create a separate issue
