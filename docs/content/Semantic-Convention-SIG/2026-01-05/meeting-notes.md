## Meeting Notes

### Attendees
- Josh Suereth
- Trask Stalnaker (Microsoft)
- Liudmila Molkova (Grafana Labs)
- [Florian Lehner](mailto:florian.lehner@elastic.co) (Elastic)
- Dave Cadwallader (Oracle)
- Christophe Kamphaus

### Agenda
- (timebox 7 min) Project Status + Triage + Blockers
  - Stability Blockers
  - PR Triage Board: [https://github.com/orgs/open-telemetry/projects/67/views/1](https://github.com/orgs/open-telemetry/projects/67/views/1)
    - [https://github.com/open-telemetry/semantic-conventions/pull/2619](https://github.com/open-telemetry/semantic-conventions/pull/2619)
      - Let's add GCP approver team
  - Issue Triage Board: [https://github.com/orgs/open-telemetry/projects/131/views/1](https://github.com/orgs/open-telemetry/projects/131/views/1)
- (timebox 50 min) General topics
  - [Liudmila, 3 min] How to define spans PR - [https://github.com/open-telemetry/semantic-conventions/pull/3240](https://github.com/open-telemetry/semantic-conventions/pull/3240)
  - [Dave, 3 min] - To use attribute/entity for Oracle Cloud “realm”? Or keep it “flat”? See discussion at end of PR: [https://github.com/open-telemetry/semantic-conventions/pull/3124#](https://github.com/open-telemetry/semantic-conventions/pull/3124#)
    - oracle_cloud.realm
      - Similar to availability zone but different
      - GCP
        - Manager in one AZ, managing resources in another AZ
      - Realm is an entity and its identity is the attribute
      - Entity named “oracle_cloud.realm”
        - Attribute named “oracle_cloud.realm”
    - Considering doing the same for cloud.availability_zone
      - How to report two of them at once, e.g. curr realm, managed by realm…
  - [Liudmila, 15 min] Schema v2 OTEP walkthrough [https://github.com/open-telemetry/opentelemetry-specification/pull/4815](https://github.com/open-telemetry/opentelemetry-specification/pull/4815)
    - Dig into why we needed a list of versions in the old schema url
    - Q: How decentralized publishing would look like
      - otel.io/collector/semconv/1.0.0
        - how would resolved schema would look like
          - Depends on otel
          - Imports otel ones
          - No need to re-declare all otel things
      - Todo for weaver to take res schema
