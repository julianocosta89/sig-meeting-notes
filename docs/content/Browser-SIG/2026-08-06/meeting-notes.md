## Meeting Notes

### Attendees
- Cleo Schneider (Google/Firebase)
- Rebecca He (Google/Firebase)
- David Luna (Elastic)
- Martin Kuba (Grafana Labs)
- Trent Mick (Elastic)
- Wolfgang Therrien ([Honeycomb.io](http://Honeycomb.io))
- Hugo Levy (Datadog)

### Agenda
- [david & maxime] allow users to compose SDK with logs and traces
  - `combineSdks` function and generics were made for this. however they are not exported
  - Alternative it to tell users to wrap `start*Sdk` functions to combine with their own SDK
  - discussion [https://github.com/open-telemetry/opentelemetry-browser/pull/357/changes#r3614420596](https://github.com/open-telemetry/opentelemetry-browser/pull/357/changes#r3614420596)
  - David to create an issue/discussion with code samples of both options.
- [martin] Callbacks for adding custom attributes
  - Global vs per-instrumentation
    - [https://github.com/open-telemetry/opentelemetry-browser/issues/359](https://github.com/open-telemetry/opentelemetry-browser/issues/359)
  - Nav instrumentation PR - [https://github.com/open-telemetry/opentelemetry-browser/pull/360](https://github.com/open-telemetry/opentelemetry-browser/pull/360)
  - Alternative could be provide docs on how to pass a processors for all logs regardless of the context.
  - AI: close the global callback issue, document use case with processors, add callback to instrumentations that need the additional context only
- [martin] Roadmap PR
  - last call, planning to merge today
  - [https://github.com/open-telemetry/opentelemetry-browser/pull/361](https://github.com/open-telemetry/opentelemetry-browser/pull/361)
- [david] hopefully last call to review fetch instrumentation [https://github.com/open-telemetry/opentelemetry-browser/pull/281](https://github.com/open-telemetry/opentelemetry-browser/pull/281)
- [martin] Presented the SIG status in Spec SIG
  - [https://docs.google.com/document/d/1hTowNFH6l6VcZlLWTV0VcAyhe3xSuILmPisZZ6gdCRg/edit?tab=t.0#heading=h.pdm4t1uvpx](https://docs.google.com/document/d/1hTowNFH6l6VcZlLWTV0VcAyhe3xSuILmPisZZ6gdCRg/edit?tab=t.0#heading=h.pdm4t1uvpx)
  - fyi only
- [cleo] Onboarding docs PR
  - a couple open questions I could use help on - posted in slack
  - [https://cloud-native.slack.com/archives/C093P0AMP0T/p1786018023086439](https://cloud-native.slack.com/archives/C093P0AMP0T/p1786018023086439)
