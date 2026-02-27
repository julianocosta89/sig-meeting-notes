## Meeting Notes

### Attendees
- Braydon Kains (Google)
- Dónal O’Sullivan (Elastic)
- Christos Markou (Elastic)
- Dmitry Anoshin (Splunk)
- Neil Yashinsky (Force Multiplier Labs / [ContextCore](http://contextcore.me/) )

### Agenda
- [Dónal] Update Process attribute requirement levels [https://github.com/open-telemetry/semantic-conventions/pull/3461](https://github.com/open-telemetry/semantic-conventions/pull/3461)
  - Reply in PR that we want to just update the attribute requirement levels in this PR and we can discuss moving process.executable to its own entity in another issue.
- [Braydon] [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/46207](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/46207)
  - Emitting a unique `service.instance.id` for every process feels incorrect
  - In k8s we explicitly define how service attributes should be populated: [https://github.com/open-telemetry/semantic-conventions/blob/main/docs/non-normative/k8s-attributes.md#service-attributes](https://github.com/open-telemetry/semantic-conventions/blob/main/docs/non-normative/k8s-attributes.md#service-attributes)
