## Meeting Notes

### Attendees
- Joaquin Diaz (Embrace)
- Jared Freeze (Embrace)
- Martin Kuba (Grafana Labs)
- Wolfgang Therrien (Honeycomb)
- David Luna (Elastic)
- Abinet Debele(Cisco)
- Ted Young (Grafana Labs)
- Hector Hernandez (Microsoft)
- Karlie L (Microsoft)

### Agenda
- [martin] Navigation event semantic conventions
  - [https://github.com/open-telemetry/semantic-conventions/pull/2806](https://github.com/open-telemetry/semantic-conventions/pull/2806)
  - alternative proposal to the [page view event](https://github.com/open-telemetry/semantic-conventions/pull/1910)
  - reasoning
    - navigation is a low-level “objective” event, while page view is up for interpretation (derived event)
    - use cases: hard navigation, same-document navigation (any URL change), soft navigation (SPA route change), logical view of content (may not have URL change)
    - We need an event that represents hard page load, captured before any content is displayed to the user. Page view implies user seeing content, especially if we expand the definition of page view to be a logical page view (e.g. user was presented with some content without navigation).
    - We can still introduce a page view event, but it may have a different meaning.
    - more details in this issue [https://github.com/open-telemetry/opentelemetry-browser/issues/3](https://github.com/open-telemetry/opentelemetry-browser/issues/3)
  - Action item: update the page view PR [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2386](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2386)
- [karlie] User action semantic conventions
  - [https://github.com/open-telemetry/semantic-conventions/pull/1941](https://github.com/open-telemetry/semantic-conventions/pull/1941)
  - The comment [https://github.com/open-telemetry/semantic-conventions/pull/1941#discussion_r2163793425](https://github.com/open-telemetry/semantic-conventions/pull/1941#discussion_r2163793425)  and [https://github.com/open-telemetry/semantic-conventions/pull/1941/files#r2163786665](https://github.com/open-telemetry/semantic-conventions/pull/1941/files#r2163786665) mentioned that type/tag_name might be attributes, do we want to change it to attributes or keep it as it is? (since they are under development and we can always change it later)
- [Ted] New entities proposal
  - [https://github.com/open-telemetry/opentelemetry-specification/pull/4665](https://github.com/open-telemetry/opentelemetry-specification/pull/4665)
  - I hate it
  - But mutable resources are concerning to sdk implementors
