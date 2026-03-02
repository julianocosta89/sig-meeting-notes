## Meeting Notes

### Attendees
- Jared Freeze (Embrace)
- Joaquin Diaz (Embrace)
- Arriana Blais (Honeycomb)
- Ted Young (Grafana Labs)
- Maryam Saeidi (Elastic)
- [Daniel Dyla](mailto:dyladan@gmail.com)
- Carlos Cortez
- Benoit Zugmeyer (Datadog)
- Trent Mick (Elastic)
- Karlie L (Microsoft)

### Agenda
- [Joaquin] [Browser Observability Model](https://docs.google.com/document/d/1UrtbLyzd92YFYsuS6NkCeNVqjpcV89DtoSGqgVlZclc/edit?usp=sharing)
  - [martin] I also shared [this doc](https://docs.google.com/document/d/16PbaGoBX66LN3t6DUBTVw8PzsDFT2xvDyFZ3xemhXG8/edit?tab=t.0) a few weeks ago
  - [martin] I want to highlight the following
    - we should not generate metrics in client SDKs directly, ok in the backend from events
      - the Client Instrumentation SIG has discussed this and is planning to document this in the web site documentation (see [this PR](https://github.com/open-telemetry/opentelemetry.io/pull/7478))
    - does it make sense to generate spans from resource timing data?
- [Jared] Intended browser support
  - I propose providing code that is Baseline Widely available [https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility#baseline_badges](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility#baseline_badges)
- [dan] (related to above) [https://github.com/open-telemetry/opentelemetry-js/pull/5807](https://github.com/open-telemetry/opentelemetry-js/pull/5807)
  - PR adds support for fetch
  - OK to drop XHR support in http exporters in order to avoid ever-growing modules?
  - Fetch included in baseline widely available
  - Service workers, node 18+ have fetch support but no XHR or beacon
- [benoit] Associate Browser telemetry with a “page_view.id” similar to [“session.id”](https://docs.google.com/document/d/16PbaGoBX66LN3t6DUBTVw8PzsDFT2xvDyFZ3xemhXG8/edit?tab=t.0#bookmark=id.50qniap3tff4)?
- [Jared] should this meeting be longer? More chat on slack instead?
