## Meeting Notes

### Attendees
- [Arve Knudsen](mailto:arve.knudsen@grafana.com)
- Jonathan
- Arthur
- [Kyle Eckhart](mailto:kyle.eckhart@grafana.com)

### Agenda
- [jonathan]
  - Should we migrate all tests that fit the AppenderV1 to AppenderV2?
    - David's comment on Slack -> [https://cloud-native.slack.com/archives/C01LSCJBXDZ/p1772131956082209?thread_ts=1770740347.176179&cid=C01LSCJBXDZ](https://cloud-native.slack.com/archives/C01LSCJBXDZ/p1772131956082209?thread_ts=1770740347.176179&cid=C01LSCJBXDZ)
    - Can I do that on this PR -> [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/46426](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/46426)?
    - Can we switch from v2 to v1 without a benchmark?
    - We need to work on the testbed PR that is mentioned below.
    - PR that can be used as inspiration: [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/45597](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/45597)
    - We need a macro benchmark. Figure out how to provide some data to the receiver and benchmark it. Very similar to prombench.
- [Kyle] Is there anyone who might be able to help with questions regarding the receiver with series ref handling + staleness: [https://cloud-native.slack.com/archives/C01LSCJBXDZ/p1772044336575139?thread_ts=1772015741.272249&cid=C01LSCJBXDZ](https://cloud-native.slack.com/archives/C01LSCJBXDZ/p1772044336575139?thread_ts=1772015741.272249&cid=C01LSCJBXDZ)?
  - [Kyle] Will keep digging focusing on repro tests for possible issues with the way refs are currently handled
- [Arthur] OTel End User SIG reached out, asking if we want to do a follow-up survey to [this one](https://opentelemetry.io/blog/2024/prometheus-compatibility-survey/). What do we think?
  - The previous survey was focused on dots vs underscores, suffixes vs no suffixes, not sure if there's anything to follow up from that. We could think of other things we want answers for.
  - Some ideas:
    - It would be helpful to understand their current experience with Prometheus exporter vs Collector receivers.
    - We know Prometheus receiver is the most used component in the collector. Why is that? What's so important about it?
    - Which SDK do people use for their instrumentation, Prometheus or OTel. Why do they choose one over the other?
- [arthur] Prometheus 3.10.0 is out, anyone volunteering to do the bump? 🙂
- [arthur] Prometheus Receiver progress review
  - I re-opened [opentelemetry-collector-contrib#44195](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44195), we need to add a benchmark to testbed and the results will automatically be posted on the OTel Website.
    - I would like to work on it, @perebaj.
  - [opentelemetry-collector-contrib#41502](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/41502) is a long standing issue that will conflict with the appenderv2 adoption. Any takers for this?
  - Regarding the spec work, I've created two new project boards[[1](https://github.com/orgs/open-telemetry/projects/142/views/8)][[2](https://github.com/orgs/open-telemetry/projects/142/views/9)]. I had to go beg for some extra permissions in the spec repo, but it's solved now. I'm still working on clarifying the work to be done. I'll let you all know in our channel once they are ready 🙏
