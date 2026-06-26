## Meeting Notes

### Attendees
- [Nayef Ghattas](mailto:nayef.ghattas@datadoghq.com) (Datadog)
- [Florian Lehner](mailto:florian.lehner@elastic.co) (Elastic)
- [Christos Kalkanis](mailto:christos.kalkanis@elastic.co) (Elastic)
- Jonathan Halliday (IBM)
- [Scott Gerring](mailto:scott@datadoghq.com)(Datadog)
- [Alexey Alexandrov](mailto:aalexand@google.com) (Google)

### Agenda
- Review action items:
  - [Felix Geisendörfer](mailto:felix.geisendoerfer@datadoghq.com) / [florian.lehner@elastic.co](mailto:florian.lehner@elastic.co) / [Ivo Anjo](mailto:ivo.anjo@datadoghq.com): Figure out KeyValueUnit proposal, see Apr 2 discussion. Next step: [Ivo Anjo](mailto:ivo.anjo@datadoghq.com) will ping TC to get their thoughts on the options:
  - [Alexey Alexandrov](mailto:aalexand@google.com) Add duplicate and orphan checks to the conformance checker.
    - Move duplicates check to [Florian Lehner](mailto:florian.lehner@elastic.co)
  - [Alexey Alexandrov](mailto:aalexand@google.com) Clarify Profile.period_type and Profile.period semantics). See [this discussion](#bookmark=id.9nkv5styhrxf) below. And later discussion [here](#bookmark=id.j6n3lln9n34g).
    - Sent [#791](https://github.com/open-telemetry/opentelemetry-proto/pull/791)
    - Alexey to take another look at the PR, address the comment and see if it can be merged anyway and the discussion we are having about the sample type vs period type interoperability can be handled separately.
  - [Nayef Ghattas](mailto:nayef.ghattas@datadoghq.com) Open GH issue on including OTLP version in payloads.
    - [https://github.com/open-telemetry/sig-profiling/issues/82](https://github.com/open-telemetry/sig-profiling/issues/82)
  - [Christos Kalkanis](mailto:christos.kalkanis@elastic.co) Data Format PR
    - Will fix merge conflicts and ping TC for a 2nd approval
  - [Alexey Alexandrov](mailto:aalexand@google.com) Figure out what to do with this [older Profiles OTEP](https://github.com/open-telemetry/opentelemetry-specification/blob/main/oteps/profiles/0239-profiles-data-model.md). See [this discussion below](#bookmark=id.mjn7dj4yyazk).
    - Depends on [https://github.com/open-telemetry/opentelemetry-specification/pull/4965](https://github.com/open-telemetry/opentelemetry-specification/pull/4965)
    - This is blocked by christos PRs above. When they land, we can update the OTEP and point to these newer docs.
  - [Ivo Anjo](mailto:ivo.anjo@datadoghq.com) & [Scott Gerring](mailto:scott@datadoghq.com) Update thread context OTEP with appendix about go support
    - Look at it an show you support
- [Florian Lehner](mailto:florian.lehner@elastic.co) I will request a new release of OTel/Proto - do we want to land something?
  - [https://github.com/open-telemetry/opentelemetry-proto/pull/786](https://github.com/open-telemetry/opentelemetry-proto/pull/786) keep unmerged
  - [https://github.com/open-telemetry/opentelemetry-proto/pull/791](https://github.com/open-telemetry/opentelemetry-proto/pull/791) - merge it
- [Florian Lehner](mailto:florian.lehner@elastic.co)profcheck: can we get some feedback/approvals?
  - [https://github.com/open-telemetry/sig-profiling/pull/142](https://github.com/open-telemetry/sig-profiling/pull/142) - do values/timestamp check on samples only if configured
    - [Florian Lehner](mailto:florian.lehner@elastic.co) IgnoreSampleTimestampShape as follow up
  - [https://github.com/open-telemetry/sig-profiling/pull/143](https://github.com/open-telemetry/sig-profiling/pull/143) - add reference check
- [Scott Gerring](mailto:scott@datadoghq.com)FYI we are starting to look at heap profiling. Hope to have something to show everyone to kick off discussions (and a design proposal) in not too long
  - We’re focusing on native memory usage
  - Discussion of the design happen in <TBD> Scott Gerring
  - Chris: Elastic experimented with USDT/trampolines in the past, maybe we can
  - Alexey: google tcmalloc has a heap profiler FWIW ([link](https://github.com/google/tcmalloc/blob/master/tcmalloc/sampler.cc))
  - Florian: current status of custom probes [https://github.com/open-telemetry/opentelemetry-ebpf-profiler/pull/1326#issuecomment-4552534029](https://github.com/open-telemetry/opentelemetry-ebpf-profiler/pull/1326#issuecomment-4552534029) that enables this new kinds of profiling
