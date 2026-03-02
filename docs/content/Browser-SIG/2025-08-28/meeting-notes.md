## Meeting Notes

### Attendees
- Martin Kuba (Grafana Labs)
- David Luna (Elastic)
- Maryam Saeidi (Elastic)
- Jared Freeze (Embrace)
- Joaquin Diaz (Embrace)
- Wolfgang Therrien (Honeycomb)
- Abinet Debele (Cisco)
- Carlos Cortez
- Benoit Zugmeyer (Datadog)
- Egor Vorotnikov (Datadog)

### Agenda
- [Jared] [OpenTelemetry Web Repository Separation](https://docs.google.com/document/d/1HFJDE7Fn2qgGL6vd404_hwT1M34b8lxX4zt_LEjPe00/edit?usp=sharing)
  - Objective: Decide on a new repo or not
  - Homework: read and please leave comments or start conversations in Slack
- [martin] [Board review](https://github.com/orgs/open-telemetry/projects/146/views/4)
- Abinet , can we finalize semconv for page view event, [https://github.com/open-telemetry/semantic-conventions/pull/1910](https://github.com/open-telemetry/semantic-conventions/pull/1910), Suggested changes {
- eventName: ‘browser.page_view’,
- attributes: { //moved from body
- url.full // from url,
- refererer,
- type: 0/1 to hard/soft or page_load/route_change
- state_change // from change_state , pushState or replaceState
- title —> remove
- }
- body: {
- }
- }
- action item: please review data model docs
  - [Real User Monitoring (RUM) Use Cases](https://docs.google.com/document/d/1n1TirOsxuQJuToMLwDEQisuuvV_UoDcTiahDPPbJgTc/edit?tab=t.0)
  - telemetry data model proposal - [this doc](https://docs.google.com/document/d/16PbaGoBX66LN3t6DUBTVw8PzsDFT2xvDyFZ3xemhXG8/edit?tab=t.0)
- action review: please review Session manager prototype before it’s merged
  - [https://github.com/open-telemetry/opentelemetry-js/pull/5173](https://github.com/open-telemetry/opentelemetry-js/pull/5173)
