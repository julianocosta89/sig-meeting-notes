## Meeting Notes

### Attendees
- Przemek Delewski (Quesma); **Facilitator**
- Kemal Akkoyun (Datadog)
- Huxing Zhang(Alibaba)
- Yi Yang(Alibaba)
- Ziming Liu(Alibaba)
- Haibin Zhang(Alibaba)

### Agenda
- [Przemek] CI workflow and unit test coverage
- [Kemal Akkoyun](mailto:kemal.akkoyun@datadoghq.com) Let’s decide on timeline of MVP/Initial release and the scope of it (v0.1.0 release)
  - Proposal:
    - Instrumenting http and grpc
    - Beginning of October
  - Start from something very minimal just to show how it works in practice, then extend it
  - We can describe what we would like to inject and where in current version of configuration and it that will be not be enough we can hardcode stuff
- [Kemal Akkoyun](mailto:kemal.akkoyun@datadoghq.com) Thoughts on [https://github.com/open-telemetry/weaver](https://github.com/open-telemetry/weaver)
  - Support automatically injecting generated code using our tool
  - Defining semantic conventions for our instrumentation and using [https://github.com/open-telemetry/weaver/blob/main/docs/usage.md#registry-diff](https://github.com/open-telemetry/weaver/blob/main/docs/usage.md#registry-diff) to check it
    - It could be part of the CI
- [Huxing] CFP for KCD Hangzhou: Sep 21, 2025 [https://community.cncf.io/events/details/cncf-kcd-hangzhou-presents-kcd-hangzhou-openinfra-china-day-2025/](https://community.cncf.io/events/details/cncf-kcd-hangzhou-presents-kcd-hangzhou-openinfra-china-day-2025/)
- [Kemal Akkoyun](mailto:kemal.akkoyun@datadoghq.com) CFP for KubeCon EU [https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/program/cfp/](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/program/cfp/) Oct 12, 2025
  - Three parties will submit together
  - Add examples on instrumenting the agents
  - Submit several proposals
  - Submit for the observability day
  - Also check whether we can have a maintainers’ day access/meeting
- [Yi Yang] hello world showcase for new compile instrumentation
  - Subtasks of instrumentation tool: enable test, instrument struct, make net/http work
- [Huxing] Introduction of using AI(like Github Copilot) to do code review or other stuff
