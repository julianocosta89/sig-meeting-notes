## Meeting Notes

### Attendees
- Ziming Liu (Alibaba); **Facilitator**
- [Kemal Akkoyun](mailto:kemal.akkoyun@datadoghq.com) (Datadog)
- Przemek Delewski (Quesma)
- Huxing Zhang (Alibaba)
- Yi Yang (Alibaba)
- [Romain Marcadier](mailto:romain.marcadier@datadoghq.com) (Datadog)
- [Dario Castañé](mailto:dario.castane@datadoghq.com) (Datadog)

### Agenda
- Review Action Items from previous meeting(s)
- Simple demonstration for PR([https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/pull/23](https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/pull/23) ) to connect the instrument framework and the SDK  (Ziming Liu)
  - Do `go mod tidy` when we introducing new dependencies
- Discussion for task splitting ([https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/issues/29](https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/issues/29) )
  - Library instrumentation can be done parallelly
- [Kemal Akkoyun](mailto:kemal.akkoyun@datadoghq.com) Facilitators should follow the [https://github.com/open-telemetry/community/issues/2809](https://github.com/open-telemetry/community/issues/2809) to gain access to [https://docs.google.com/document/d/1gt9ctxKGPrM_XTINqLgkSxYypdrczHkt2znjwgBU4UU/edit#](https://docs.google.com/document/d/1gt9ctxKGPrM_XTINqLgkSxYypdrczHkt2znjwgBU4UU/edit#) for passwords
- [Huxing] [https://github.com/open-telemetry/community/blob/main/RELEASE.md](https://github.com/open-telemetry/community/blob/main/RELEASE.md)
- First MVP
  - Library perspective: http instrumentation net/http server & client @Ziming Liu
  - Compilation framework perspective: Implementation should follow the specification of [https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/tree/main/_docs](https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/tree/main/_docs). And the specification may change.
- [Kemal Akkoyun](mailto:kemal.akkoyun@datadoghq.com) [Observability Day | LF Events](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/co-located-events/observability-day/#registration-details)
  - We will submit the KubeCon talk
