## Meeting Notes

### Attendees
- Jared Freeze (Embrace)
- Joaquin Diaz (Embrace)
- Martin Kuba (Grafana Labs)
- Christopher Arredondo (Mercado Libre)
- David Luna (Elastic)
- Hugo Levy (Datadog)
- Maxime Quentin (Datadog)

### Agenda
- [maxime] Entity and browser.document.url.full
  - Should query params be part of the browser.document.url.full
  - If yes => might have too many entities as query params mutate a lot
  - If no => not align with the absolute URL definition from: [https://opentelemetry.io/docs/specs/semconv/registry/attributes/url/#url-full](https://opentelemetry.io/docs/specs/semconv/registry/attributes/url/#url-full)
  - Output:
    - API to pick what page url entity is leveraging all the  [https://opentelemetry.io/docs/specs/semconv/registry/attributes/url](https://opentelemetry.io/docs/specs/semconv/registry/attributes/url/#url-full)
    - Out of the box the browser.document.url.full is the page entity
    - Agree we don’t want the url on all the signals we want it shared as an entity
    - Keep this discussion in the entity github discussion for now but can move to a dedicated issue later
- [david] `user_agent.orginal` semconv comment recommends removal from the entity. Thoughts?
  - [https://github.com/open-telemetry/semantic-conventions/pull/3738#discussion_r3294848876](https://github.com/open-telemetry/semantic-conventions/pull/3738#discussion_r3294848876)
- [Chris] MAX_ATTEMPS (retries) static issue [https://github.com/open-telemetry/opentelemetry-js/issues/6728](https://github.com/open-telemetry/opentelemetry-js/issues/6728)
- Fetch/XHR instrumentations migration
  - two approaches in progress
    - [https://github.com/open-telemetry/opentelemetry-browser/pull/283](https://github.com/open-telemetry/opentelemetry-browser/pull/283)
    - [https://github.com/open-telemetry/opentelemetry-browser/pull/281](https://github.com/open-telemetry/opentelemetry-browser/pull/281)
  - decision: let’s continue discussion in this issue [https://github.com/open-telemetry/opentelemetry-browser/issues/259](https://github.com/open-telemetry/opentelemetry-browser/issues/259)
