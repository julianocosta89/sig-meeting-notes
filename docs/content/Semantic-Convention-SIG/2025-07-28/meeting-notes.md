## Meeting Notes

### Attendees
- Joao Grassi (Dynatrace)
- [Daniel Dyla](mailto:dyladan@gmail.com)
- James Thompson
- Armin Ruech (Dynatrace)
- Christophe Kamphaus
- Thomas Hunter II (DataDog)
- Valentin Zakharov (DataDog)
- Josh Suereth
- Marylia Gutierrez (Grafana)
- Trask Stalnaker (Microsoft)
- Alexandra Konrad (Elastic)
- Liudmila Molkova (Microsoft)
- Braydon Kains (Google) (arrived late)

### Agenda
- (timebox 7 min) Project Status + Triage + Blockers
  - Stability Blockers
  - PR Triage Board: [https://github.com/orgs/open-telemetry/projects/67/views/1](https://github.com/orgs/open-telemetry/projects/67/views/1)
  - Issue Triage Board: [https://github.com/orgs/open-telemetry/projects/131/views/1](https://github.com/orgs/open-telemetry/projects/131/views/1)
- (timebox 50 min) General topics
  - [liudmila, 5 min] GenAI SIG would like to start allowing complex attributes on spans in the scope of [https://github.com/open-telemetry/semantic-conventions/pull/2179](https://github.com/open-telemetry/semantic-conventions/pull/2179) to continue the experimentation (no stability in sight). Asking to relax policy to allow complex attributes on spans in general or for exception for these specific attributes (until spec is updated based on [https://github.com/open-telemetry/opentelemetry-specification/pull/4485](https://github.com/open-telemetry/opentelemetry-specification/pull/4485))
  - [james, 5 min] [https://github.com/open-telemetry/semantic-conventions/pull/2370](https://github.com/open-telemetry/semantic-conventions/pull/2370)
  - [trask, 2 min] [https://github.com/open-telemetry/semantic-conventions/pull/2549](https://github.com/open-telemetry/semantic-conventions/pull/2549)
  - [trask, 5 min] What’s our recommendation for when to capture `thread.name` and `thread.id`?
    - E.g. the Java agent captures these on all spans
    - But HTTP semconv doesn’t specify them
    - I’m thinking they should be opt-in in Java agent 3.0
  - [james, 5-10 min] [https://github.com/open-telemetry/semantic-conventions/pull/2548](https://github.com/open-telemetry/semantic-conventions/pull/2548)
  - [James 5min] how best to get documentation PR progressed
  - [tlhunter, 5 min] Websocket traces ([Slack thread](https://cloud-native.slack.com/archives/C041APFBYQP/p1753129583909499))
