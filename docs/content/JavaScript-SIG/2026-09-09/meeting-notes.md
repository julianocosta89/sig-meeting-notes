## Meeting Notes

### Attendees
- Amir Sadeghi (Intelika)
- Matt Wear (Dash0)
- David Luna (Elastic)
- Pranav Sharma (Google)
- Jared Freeze (Palo Alto Networks)
- Hector Hernandez (Microsoft)
- Jackson Weber (Microsoft)
- Marylia (Grafana)
- Trent Mick (Elastic)

### Agenda
- **Feel free to add your topics below ↙️ 🙂**
- [Amir] NestJS 12 instrumentation support: [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3733](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3733)
  - Clarify the unmaintained/autoclose status and unblock first-contributor CI/review.
- [marc][SDK 3.x] Plans for instrumentation-restify?
  - [https://github.com/open-telemetry/opentelemetry-js/issues/6875](https://github.com/open-telemetry/opentelemetry-js/issues/6875)
  - New release was published recently
- [pranav] (Review request): OpenTelemetry GenAI utils - split PRs
  - [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3709](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3709)
  - [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3712](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3712)
- [trent] Discuss some open questions on widening Attributes: [https://gist.github.com/trentm/8068b1ded798329cadf9838be1a63b21](https://gist.github.com/trentm/8068b1ded798329cadf9838be1a63b21)
  - [trent] From discussion:
    - Carlos suggested a possible OTel blog post in advance of the changes if we are concerned there might be user breakage. We don’t think there will be breakage.  However, a blog post on this seems good. Trent & Marylia might work together on one.
    - Use simple attributes for span event attributes and instrumentationScope attributes, because starting simple (as allowed by the spec) is easier. We can support complex attributes for these later if justified.
    - Use full guard (`core.cleanAttributes()` or equivalent) for resource attributes, because this isn’t a hot path there is no perf concern.
    - For metric attributes: the impression from the Node Collab Summit was that OTel metrics is *already* slower than wanted, so adding a perf hit doing validation of metric attributes is unwanted. The plan then is to not change current sdk-metric behaviour: given attributes will not be guarded. We’ll doc that metric attributes should only be simple attribute types, and it is users’ responsibility.  (We can separately discuss/decide if we want to export a `type SimpleAttributes` from `core` that users could use for TypeScript guidance on their attributes.  We should (could be separate) add a try/catch on `JSON.stringify(attributes)` in PrometheusExporter that can crash.
    - Marc suggested I follow up with Dan on the proposal to have `undefined` **not** be part of AnyValue. I’m proposing `null` is the “empty value” for JS referred to in the spec.
- [trent] As ever, would appreciate other opinions on [https://github.com/open-telemetry/opentelemetry-js/pull/6999](https://github.com/open-telemetry/opentelemetry-js/pull/6999)
- [jared] should we `deprecate` browser packages that don’t have a replacement?
  - [trent] I think we decided to mark them `@deprecated` early, pointing to the opentelemetry-browser issue with the *plan*.
  - [trent] Still an open Q whether we are comfortable dropping sdk-trace-web given its usage in [opentelemetry.io](http://opentelemetry.io) docs.
- [marylia] FYI, be careful if you use agents to read issues, there were a few “prompt injections” as a hidden comments on other otel repos
- [Bhaskar Banerjee] from Capital One - wanted to check on the JSON file exporter options like in Java and Python
  - [trent] E.g. Python impl: [https://github.com/open-telemetry/opentelemetry-python/tree/main/exporter/opentelemetry-exporter-otlp-json-file](https://github.com/open-telemetry/opentelemetry-python/tree/main/exporter/opentelemetry-exporter-otlp-json-file)
