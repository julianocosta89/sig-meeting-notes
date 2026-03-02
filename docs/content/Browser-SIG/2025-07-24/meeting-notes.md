## Meeting Notes

### Attendees
- Arriana Blais (Honeycomb)
- David Luna (Elastic)
- Dan Gomez Blanco (New Relic)
- Jared Freeze (Embrace)
- Martin Kuba (Grafana Labs)

### Agenda
- [martin] One of the things we discussed last week was to document events that different vendors collect. There was actually significant effort put into this in the Client Instrumentation SIG a while back, and I want to add it as a context as we are revisiting this discussion. I also wonder if we could use this as a starting point and update rather than start from scratch…
  - Here is a link to the document: [https://docs.google.com/document/d/1_5MtDy_8uovK3cQEmwrVmFz0ApLQvQGsYX4ME9Kl3pg/edit?tab=t.0#heading=h.nbj5nuoe6d1n](https://docs.google.com/document/d/1_5MtDy_8uovK3cQEmwrVmFz0ApLQvQGsYX4ME9Kl3pg/edit?tab=t.0#heading=h.nbj5nuoe6d1n)
  - The outcome of this back then was this spreadsheet which we used to agree on the events and attributes we should capture in OTel:
  - [https://docs.google.com/spreadsheets/d/1WEIhp7EX6nOg6eJPg6V5OrIPE8EE-oRD4KoiK_6XBF0/edit?gid=0#gid=0](https://docs.google.com/spreadsheets/d/1WEIhp7EX6nOg6eJPg6V5OrIPE8EE-oRD4KoiK_6XBF0/edit?gid=0#gid=0)
  - This then got distilled into a few semconv PRs:
    - Page view: [https://github.com/open-telemetry/semantic-conventions/pull/1910](https://github.com/open-telemetry/semantic-conventions/pull/1910)
    - Navigation timing: [https://github.com/open-telemetry/semantic-conventions/pull/1919](https://github.com/open-telemetry/semantic-conventions/pull/1919)
    - Resource timing: [https://github.com/open-telemetry/semantic-conventions/pull/1943](https://github.com/open-telemetry/semantic-conventions/pull/1943)
    - User action: [https://github.com/open-telemetry/semantic-conventions/pull/1941](https://github.com/open-telemetry/semantic-conventions/pull/1941)
    - Web vitals (merged): [https://github.com/open-telemetry/semantic-conventions/pull/1940](https://github.com/open-telemetry/semantic-conventions/pull/1940)
- Researching existing implementations
  - Which implementations do we want to look at?
  - What do we want to see?
    - Compare bundle sizes
    - Compare
