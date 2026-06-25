## Meeting Notes

### Attendees
- Marc Pichler (Dynatrace)
- Trent Mick (Elastic)
- Jared Lewis
- Marylia Gutierrez (Grafana Labs)
- Jamie Danielson (Honeycomb)

### Agenda
- **Feel free to add your topics below ↙️ 🙂**
- [marc] to factory function or not to factory function, that is the question:
  - [https://github.com/open-telemetry/opentelemetry-js/pull/6168](https://github.com/open-telemetry/opentelemetry-js/pull/6168)
  - Personally I have a slight preference to using a factory function for this new sampler, but can go either way. All others are exported as classes right now.
- [marc] context.attach()/context.detach() PR is now ready for review
  - [https://github.com/open-telemetry/opentelemetry-js/pull/6845](https://github.com/open-telemetry/opentelemetry-js/pull/6845)
  - I added some notes on some of the decisions I made when working on this. None of these are set in stone - happy to change things if needed :)
  - Will follow up with PRs for other context managers (best-effort impl) and tracing channel instrumentation util in the coming days
- [marc] we have a somewhat unique window to do the same to the new sdk-trace package, and rename Span to ReadWriteSpan WDYT?
  - [https://github.com/open-telemetry/opentelemetry-js/issues/6821](https://github.com/open-telemetry/opentelemetry-js/issues/6821)
- [trent] remove shim-opencensus ([https://github.com/open-telemetry/opentelemetry-js/pull/6843](https://github.com/open-telemetry/opentelemetry-js/pull/6843)) and shim-opentracing (no PR yet)?
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
