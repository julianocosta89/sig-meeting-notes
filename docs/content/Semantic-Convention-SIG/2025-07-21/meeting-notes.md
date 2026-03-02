## Meeting Notes

### Attendees
- [Daniel Dyla](mailto:dyladan@gmail.com)
- Liudmila Molkova (Microsoft)
- Trask Stalnaker (Microsoft)
- Carlos Crespo (Elastic)
- Sam Xie (Splunk)
- Josh Suereth (google) [first 30 min only]
- Joao Grassi (Dynatrace)
- Alexandra Konrad (Elastic)
- Armin Ruech (Dynatrace)
- Christophe Kamphaus
- Nick Moore (Grafana)
- James Thompson
- Bertrand Martin (MetricsHub)
- Matthew Hensley (Grafana Labs)

### Agenda
- (timebox 7 min) Project Status + Triage + Blockers
  - Stability Blockers
  - PR Triage Board: [https://github.com/orgs/open-telemetry/projects/67/views/1](https://github.com/orgs/open-telemetry/projects/67/views/1)
  - Issue Triage Board: [https://github.com/orgs/open-telemetry/projects/131/views/1](https://github.com/orgs/open-telemetry/projects/131/views/1)
- (timebox 50 min) General topics
  - [sam, 5 min] Add SQL commenter as context propagation for databases [https://github.com/open-telemetry/semantic-conventions/pull/2495#discussion_r2199242475](https://github.com/open-telemetry/semantic-conventions/pull/2495#discussion_r2199242475)
    - service.* is not available for instrumentation
    - DB instrumentation can take propagator and it does not need to know what propagator propagates
    - Service* propagator should be discussed in the spec call - need a way to access service*
      - Spec is not specific enough to implement across languages
    - Do we have a prototype for service.name propagator?
      - Prototype: https://github.com/XSAM/otelsql/pull/512
    - Let's take service.name part from the PR and tackle it separately
      - Need to have a spec discussion on the API-level access to resource/entity API
      - Need to have a couple of prototypes
  - [nick, 5 min] Vulnerability component and CVSS 4 [https://github.com/open-telemetry/semantic-conventions/pull/1295#discussion_r2190282193](https://github.com/open-telemetry/semantic-conventions/pull/1295#discussion_r2190282193)
    - Not much progress in security semconv
    - Could we follow OCSF more closely?
    - General semconv leans on security semconv SIG
    - We can try to model OCSF domain
  - [liudmila, 5 min] Hugo (otel.io) issues with html links [https://github.com/open-telemetry/semantic-conventions/issues/2536](https://github.com/open-telemetry/semantic-conventions/issues/2536)
  - [james, 10 min] namespace registry as central point to go for definitions [https://github.com/open-telemetry/semantic-conventions/pull/2548](https://github.com/open-telemetry/semantic-conventions/pull/2548)
    - Namespace page is where all definition from one conventions are defined
    - AI: let's try to materialize it for HTTP
  - [alexandra, 1 min] Request for reviews for hardware PR [https://github.com/open-telemetry/semantic-conventions/pull/2380](https://github.com/open-telemetry/semantic-conventions/pull/2380)
    - the same as md, naming has not changed
  - [braydon, 5 min] Using common attribute with a specific defined value in certain contexts
    - [https://github.com/open-telemetry/semantic-conventions/pull/2287#discussion_r2207181141](https://github.com/open-telemetry/semantic-conventions/pull/2287#discussion_r2207181141)
    - Metric references with refinement would work, being discussed in weaver
    - Currently doing it manually with [https://github.com/open-telemetry/semantic-conventions/blob/main/docs/dotnet/dotnet-http-metrics.md#metric-httpserverrequestduration](https://github.com/open-telemetry/semantic-conventions/blob/main/docs/dotnet/dotnet-http-metrics.md#metric-httpserverrequestduration)
