## Meeting Notes

### Attendees
- [Jonathan Santos](mailto:perebaj@gmail.com)
- Kyle
- Arthur
- David
- Naman

### Agenda
- [krajo Krajcsovits](mailto:gyorgy.krajcsovits@grafana.com) : I've seen [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/46426](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/46426) and am trying to get to it by next Wednesday. To be fair it isn't new, "just" refactored functionality so don't block on me.  I have a private appointment today (10th April), and won't make it to the meeting.
- [arthur] [Kyle Eckhart](mailto:kyle.eckhart@grafana.com) and I made the [first Prometheus exporter](https://github.com/prometheus-community/stackdriver_exporter/pull/477) embeddable into a custom Collector distribution, and we're working on the [second one](https://github.com/prometheus-community/yet-another-cloudwatch-exporter/pull/1837). There is a [playground repository](https://github.com/prometheus/prometheus-opentelemetry-collector), if people want to test this out.
- [arthur/andrej] [Andrej Kiripolsky](mailto:andrej.kiripolsky@grafana.com) did an [in-person survey](https://docs.google.com/document/d/1gfE8UmeHaAmFG6ZjRiVDO2Phi-5Vk3mLpMU3YJQ58PU/edit?tab=t.0#heading=h.zbk80121fq6r) during KubeCon EU and realized there were several small adjustments to make after interviewing 5-10 people. Adjustments were made, and we'll promote the survey more aggressively on the Prometheus and OTel websites using Google Forms.
- [arthur/pablo] Arthur and Pablo did a summary of Prometheus<->OTel related activities at KubeCon: [Prometheus<->OTel interoperability at KubeCon EU 2026](https://docs.google.com/document/d/1RKy2THrgYBSW4RHywhW-zEK6Vsn5nrdCrUIfYpej69o/edit?userstoinvite=pablo.baeyens@datadoghq.com&sharingaction=manageaccess&role=writer&tab=t.0#heading=h.3oes36i45k2)
- [dashpole] Spec PRs
  - Metadata: [https://github.com/open-telemetry/opentelemetry-specification/pull/4966](https://github.com/open-telemetry/opentelemetry-specification/pull/4966)
  - Exemplar: [https://github.com/open-telemetry/opentelemetry-specification/pull/4964](https://github.com/open-telemetry/opentelemetry-specification/pull/4964)
  - Timestamp: [https://github.com/open-telemetry/opentelemetry-specification/pull/4953](https://github.com/open-telemetry/opentelemetry-specification/pull/4953)
  - Resource: [https://github.com/open-telemetry/opentelemetry-specification/pull/4956](https://github.com/open-telemetry/opentelemetry-specification/pull/4956)
  - Scope: [https://github.com/open-telemetry/opentelemetry-specification/pull/5004/](https://github.com/open-telemetry/opentelemetry-specification/pull/5004/)
  - Check-in:
    - Prom-> OTLP: [https://github.com/open-telemetry/opentelemetry-specification/issues/4742](https://github.com/open-telemetry/opentelemetry-specification/issues/4742)
    - OTLP -> Prom: [https://github.com/open-telemetry/opentelemetry-specification/issues/4803](https://github.com/open-telemetry/opentelemetry-specification/issues/4803)
- Stabilization efforts review!
- [Naman] Okay to work on - [Ticket](https://github.com/orgs/open-telemetry/projects/178/views/3?pane=issue&itemId=138858576&issue=open-telemetry%7Copentelemetry-collector-contrib%7C44196)??? Since [pr](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/45233) already exists but requires changes
  - Any open ticket that can be worked on
- [https://github.com/prometheus/otlptranslator/issues/65](https://github.com/prometheus/otlptranslator/issues/65) - Naman-B-Parlecha
- Memory Limiter in Prometheus:
  - [https://github.com/prometheus/proposals/pull/76](https://github.com/prometheus/proposals/pull/76)
- OpenMetrics 2.0:
  - Initial SDK support PR: [https://github.com/prometheus/common/pull/894](https://github.com/prometheus/common/pull/894)
  - [https://prometheus.io/docs/specs/om/open_metrics_spec_2_0/](https://prometheus.io/docs/specs/om/open_metrics_spec_2_0/)
  - [https://github.com/prometheus/OpenMetrics](https://github.com/prometheus/OpenMetrics)
