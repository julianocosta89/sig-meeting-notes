## Meeting Notes

### Attendees
- Andrew Wilkins (Elastic)
- Liudmila Molkova (Grafana Labs)
- Antoine Toulme (Splunk)
- Josh MacDonald (Microsoft)
- Dmitry Anoshin (Splunk)
- Paulo Janotti (Splunk)
- Blake Rouse (Elastic)

### Agenda
- [Announcement] Amendment to RFC:     [https://github.com/open-telemetry/opentelemetry-collector/pull/14538](https://github.com/open-telemetry/opentelemetry-collector/pull/14538)
- [15 min] Go through high priority issues for [stability phase 1](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44130) listed on the [**board**](https://github.com/orgs/open-telemetry/projects/178)
- [Josh] New storage extension
  - [https://github.com/open-telemxetry/opentelemetry-collector-contrib/issues/4](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/42326#issuecomment-3855158594)[https://github.com/orgs/open-telemetry/projects/178](https://github.com/orgs/open-telemetry/projects/178)[2326](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/42326#issuecomment-3855158594)
  - Josh’s doc on component interfaces: [Component interface guidelines by jmacd · Pull Request #14532 · open-telemetry/opentelemetry-collector](https://github.com/open-telemetry/opentelemetry-collector/pull/14532)
  - We think an _extension_ to the storage interface in the core, meaning an optional storage extension that supports range-queries.
  - Tail sampling processor wants this. Interval processor might want this (elastic has)
  - Josh will follow up
- [Andrew/Blake] Enable partial pipeline reload to reduce downtime
  - [https://github.com/open-telemetry/opentelemetry-collector/issues/14529](https://github.com/open-telemetry/opentelemetry-collector/issues/14529)
  - There is a desire to create new receivers corresponding with new containers spinning up
  - OpAmp is another route towards reconfiguring
  - Evan wants an RFC
  - TODO: find the associated OpAmp issue they’re discussing this
  - The partial-restart prototype restarts a node and all its predecessors
- [Andrew] Proposal for configurable exporterhelper batcher partitioning
  - [https://github.com/open-telemetry/opentelemetry-collector/issues/12795#issuecomment-3658571392](https://github.com/open-telemetry/opentelemetry-collector/issues/12795#issuecomment-3658571392)
  - Josh / Dmitrii will help
- [Andrew] RFC for scraper controller extension interface
  - [https://github.com/open-telemetry/opentelemetry-collector/pull/14469](https://github.com/open-telemetry/opentelemetry-collector/pull/14469)
  - Look into “receivercreator”
  - Please read
- [Liudmila] Using resource attributes to in postgres receiver [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/45347](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/45347)
  - (sometimes) record tables, indexes, database names
  - How to consistently populate `service.*`
  - K8s [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/45736](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/45736)
  - Let’s find those postgres receiver maintainers
  - Would be useful to have semconv somewhere
- [Antoine] Go 1.26 is out! [https://go.dev/doc/go1.26](https://go.dev/doc/go1.26) [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/46000](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/46000)
- [Andrew] confighttp otelhttp instrumentation ordering
  - [https://github.com/open-telemetry/opentelemetry-collector/issues/14508](https://github.com/open-telemetry/opentelemetry-collector/issues/14508)
