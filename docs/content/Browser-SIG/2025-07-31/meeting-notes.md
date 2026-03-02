## Meeting Notes

### Attendees
- Martin Kuba (Grafana Labs)
- Arriana Blais (Honeycomb)
- Benoit Zugmeyer (Datadog)
- Santosh Cheler (Cisco Splunk)
- Antoine Toulme (Cisco Splunk)
- Dan Gomez Blanco (New Relic)
- Jordan Porter (New Relic)
- Ted Young (Grafana Labs)
- [Daniel Dyla](mailto:dyladan@gmail.com)
- Jared Freeze (Embrace)
- Hector Hernandez (Microsoft)
- Karlie L (Microsoft)
- Purvi Kanal (Honeycomb)

### Agenda
- [martin] Page view event semantic conventions
  - [https://github.com/open-telemetry/semantic-conventions/pull/1910](https://github.com/open-telemetry/semantic-conventions/pull/1910)
  - Looking for consensus about the proposed approach
    - Two events - page view to track number of views, and navigation timing for timing data
  - Should the page view event be used for soft navigation?
    - Soft navigation are currently not well defined
    - Can be captured by instrumenting framework routers
    - There is a [W3C draft](https://wicg.github.io/soft-navigations/) and Chrome has experimental implementation
- [martin] Session manager PR
  - [https://github.com/open-telemetry/opentelemetry-js/pull/5173](https://github.com/open-telemetry/opentelemetry-js/pull/5173)
  - Up-to-date with previous reviews/comments
  - Since it is new to this group, should we take a step back or push this forward?
- [Ted] What’s the best way to model our telemetry goals? AKA a combination of what data we plan to emit with our expectations of how it will be used.
- [Ted] [Backlog management](https://github.com/orgs/open-telemetry/projects/146/)
  - Seems like we want to change the order of attack
    - Phase 1:
      - Semantic Conventions
      - Sessions & Entities
      - Instrumentation
    - Phase 2:
      - Benchmarking and Analysis
      - API v2.0
    - Unclear:
      - Navigation
      - Anonymous user ids
