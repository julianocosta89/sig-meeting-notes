## Meeting Notes

### Attendees
- Anand
- Jim Porell
- Ruediger
- Greg

### Agenda
- Sent details to Greg how to request Organisation Membership (to allow to add him as Project Lead later on)
- Updated [PR#1898](https://github.com/open-telemetry/semantic-conventions/pull/1898):
  - Introduce a TPS entity (identifying attribute [tps.region.id](http://tps.region.id))
  - Defined ibm.ims.commit_mode as enum
  - Resolved ambiguity of [tps.transaction.owner.id](http://tps.transaction.owner.id)
- Follow ups once PR#1898 is approved
  - Add and align with additional attribute used in product implementations (CICS, IMS)
  - [z/OS Software](https://opentelemetry.io/docs/specs/semconv/registry/entities/zos/#zos-software) is currently a z/OS system following its attributes
- Additional PRs for MQ, Db2 and CICS, IMS specific attributes will be open later in September
- Survey blog draft sent to Mae for OMP blog release, will open PR for [opentelemetry.io](http://opentelemetry.io) blog in the next days
- Continue discussion for [Metric Semantic Conventions](https://docs.google.com/spreadsheets/d/1CNn5AW8px_98vzrUCEbtWxXB5MVY5Fn8/edit?gid=183501072#gid=183501072)
  - Consideration of histogram as metric type for metrics like system.cpu.utilization (example: latency of transaction, and throughput per second)
  - Sampling of metrics depending on aggregation intervals
