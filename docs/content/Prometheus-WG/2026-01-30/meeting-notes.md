## Meeting Notes

### Attendees
- Krajo
- David
- Arve
- [arthursens] Won't be able to join, traveling to FOSDEM.
  - Would be lovely if you could discuss the impact of appenderv2 in the Prometheus receiver.
  - I did some [initial work](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/45597), and it doesn't seem to be an easy transition; we will need state handling for summaries.
  - Bartek also proposed that [Prometheus Receiver could force ScrapeManager to always transform classic histograms into NHCB](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/45611). I'm seeing some weird test failures after doing this.
  - Finding the time to work on [#44319](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44319) has been difficult for all of us. Could we decide whether to accept the [alternative](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/45335)?
    - Some tests are about how we process the scraped data, we shouldn't have to worry about how it's actually scraped, e.g. [https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/prometheusreceiver/metrics_receiver_protobuf_test.go](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/prometheusreceiver/metrics_receiver_protobuf_test.go) So ideally in the test we can tell scrape manager to take this bytes/file and scrape it without network.
- [krajo] Do we have an expectation when the component stabilization finishes ? [Arthur Silva Sens](mailto:arthur.silvasens@grafana.com)  My team is a little bit in flux, but it would be good to know for planning purposes and planning our involvement.
- [krajo] I'll be more active next quarter. We have a reorg and one of my OKRs will be to become approver/maintainer.
- Triage:
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44360](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44360) for Arve!
