## Meeting Notes

### Attendees
- Sven Cowart (ElastiFlow)
- Mario Macias (Grafana)

### Agenda
- [Sven] - Project [PR](https://github.com/open-telemetry/community/pull/3560) is updated.
- [Sven] - Begin addressing the [near-term goals](https://github.com/open-telemetry/community/pull/3560/changes#diff-47439c727556ca2663e76313b3582e3849bca8b7f5bb07484c3acff153d835c1R36-R41).
- [Braydon] - Sanity check on a new system network metric [https://github.com/open-telemetry/semantic-conventions/pull/3848](https://github.com/open-telemetry/semantic-conventions/pull/3848)
  - We need to follow up about the HW semantic convention [https://opentelemetry.io/docs/specs/semconv/hardware/network/](https://opentelemetry.io/docs/specs/semconv/hardware/network/)
  - Mario: “to the direction naming, in the network flows proposal, we faced a similar issue: we need to classify ingress/egress traffic at the interface level (not at the physical host level”
- [Antonio] discuss the possibility to have network.remote.address_ipv4 network.remote.address_ipv6 apart from network.remote.address
  - That cover the use case that an entity has ipv4 and ipv6 for the same time series.
- [Sven] - Open issues/PRs for the items in our near-term goals.
- [Sven] - Stephen OBI / Braydon collectors / Henrik dev-rel dynatrace
