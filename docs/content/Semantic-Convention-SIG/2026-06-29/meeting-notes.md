## Meeting Notes

### Attendees
- Armin Ruech (Dynatrace)
- Rob Cowart (ElastiFlow)
- Christophe Kamphaus
- Ruediger Schulze (IBM)
- Surbhi A (Cisco)

### Agenda
- (timebox 7 min) Project Status + Triage + Blockers
  - Stability Blockers
  - PR Triage Board: [https://github.com/orgs/open-telemetry/proje](https://github.com/orgs/open-telemetry/projects/67/views/1)
  - [cts/67/views/1](https://github.com/orgs/open-telemetry/projects/67/views/1)
  - Issue Triage Board: [https://github.com/orgs/open-telemetry/projects/131/views/1](https://github.com/orgs/open-telemetry/projects/131/views/1)
- [Surbhi A, 15-20 mins] Discuss HTTP Network Timing semantic conventions further - [https://github.com/open-telemetry/semantic-conventions/pull/3727](https://github.com/open-telemetry/semantic-conventions/pull/3727)
  - Client side MAY look a little bit different
    - This can live in federated repo for clients
    - Can evolve and go through iterations independently from core semconv
    - Users may expect some things to be the same across HTTP request from mobile/browser and HTTP requests between servers
    - What else could be in the federated repo?
      - RUM events
  - There are things common with general HTTP
    - Phase timings (attributes / metrics names)
- Federation
  - Repo
  - SemConv can now be used as a dependency, need to release
    - Ruediger will send PR to mark mainframes things as excluded
      - annotations:
      - dependency_resolution:
      - exclude: true
    - Liudmila will release semconv after it's in
    - Annotation to disable moved things in semconv
    - Reusable templates [https://github.com/open-telemetry/opentelemetry-weaver-packages/pull/38](https://github.com/open-telemetry/opentelemetry-weaver-packages/pull/38)
    - Release
      - Weaver registry package -> GH release artifacts
      - otel.io publishing  - not figured out yet
