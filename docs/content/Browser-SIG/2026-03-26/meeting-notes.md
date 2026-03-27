## Meeting Notes

### Attendees
- Martin Kuba (Grafana Labs)
- Jared Freeze (Embrace)
- Joaquin Diaz (Embrace)
- Maxime Quentin (Datadog)
- Hugo Levy (Datadog)
- Marco Schaefer (Grafana Labs)

### Agenda
- [maxime] Prototype for the Browser SDK Demo
  - [https://mquentin.github.io/otel-browser-sdk-demo](https://mquentin.github.io/otel-browser-sdk-demo)
  - [martin] [Discussion on demo/prototype](https://github.com/open-telemetry/opentelemetry-browser/discussions/208)
  - Add an index in front of it and add it in the repo
- [maxime] page URL attribute
  - [Updated issue out of the last SIG discussion](https://github.com/open-telemetry/opentelemetry-browser/issues/174#issuecomment-4091336306)
  - what about matching Web API semantic browser.document.url.full
  - [https://developer.mozilla.org/en-US/docs/Web/API/Document/URL](https://developer.mozilla.org/en-US/docs/Web/API/Document/URL)
  - [martin] we already have some precedent for this [here](https://github.com/open-telemetry/opentelemetry-js-contrib/blob/main/packages/instrumentation-browser-navigation/src/instrumentation.ts#L34-L35)
- [david] instrumentation scope
  - Instr use to set scope with the package name
  - Browser instrumentations live in the same package so this approach won’t work. All will have the same scope
  - Example [Web Vitals](https://github.com/open-telemetry/opentelemetry-browser/blob/d6453f2b81b49bdcb394a35b269e85a5135afffb/packages/instrumentation/src/web-vitals/instrumentation.ts#L49)
  - Use the package with subpaths? “@opentelemetry/browser-instrumentation/experimental/web-vitals”
    - Yes, already doing it
    - Instrumentations migrated to browser should follow the same rule
  - If so, is it a good idea to have the “experimental” part which eventually will disappear?
    - Decided to not include experimental
- [martin] Sync on roadmap
  - [https://docs.google.com/document/d/18QggfTXwUgxPaqmW6f-Q-PzUK0i_lq3wh7R8BUq7TPI/edit?tab=t.0](https://docs.google.com/document/d/18QggfTXwUgxPaqmW6f-Q-PzUK0i_lq3wh7R8BUq7TPI/edit?tab=t.0)
