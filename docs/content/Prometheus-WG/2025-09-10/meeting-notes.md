## Meeting Notes

### Agenda
- [arthursens] There's not a single renovate PR that upgrades Prometheus libraries that passes without manual intervention or that doesn't introduce flakiness. Collector SIG reached out asking if we'd like to remove Prometheus updates from renovate, so we make all upgrades manually.
  - We can automate messages in Slack to remind us when a new release is out.
    - This can be done by subscribing to the RSS page for releases of new prometheus & related repositories versions
- [arthursens] What do we think about running Collector tests in Prometheus CI?
  - Not a PR blocker, just to help us identify which changes will break the collector components early.
  - About the config loading working differently now: [https://github.com/prometheus/prometheus/issues/16756](https://github.com/prometheus/prometheus/issues/16756)
- [Juraj] [PRs](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/42329#issuecomment-3254769552) related to prometheus getting merged without reviews from codeowners.
- [Juraj] Do we recommend using the OTLP ingest endpoint (in Prometheus, Mimir, Cortex) over the remote write exporter?
- [Juraj] Prometheus OTLP endpoint has translation_strategy with options (NoUTF8EscapingWithSuffixes ,UnderscoreEscapingWithSuffixes and NoTranslation) vs RW exporter has add_metric_suffixes which is bool, going forward especially with relation to RW2 what do we want to with configuration around translations for the RW exporter (keeping in mind NoTranslation is only an option for RW2)
- [Juraj] Any chance we could switch which week this meeting happens? I have another biweekly meeting in work at the same time 🤦 and I can’t move that one
  - [krajo] ok by me. I slightly prefer this week as the “other” week is then the same day as OpenMetrics2.0 WG
  - [owen] also ok by me
  - [Juraj] follow up make a pool for voting on time for this meeting
- [krajo] Note: otlp endpoint code changed in Prometheus: [https://github.com/prometheus/prometheus/pull/16951](https://github.com/prometheus/prometheus/pull/16951) . I noticed the pkg/translation/prometheusremotewrite is very similar in otel collector.
  - Juraj interested in moving this out of prometheus/prometheus repo so it’s reusable in promremotewriteexporter.
  - Krajo: touch base with Bartek he’s [thinking about](https://github.com/prometheus/prometheus/pull/17104) making the new interface in Prometheus default and for TSDB itself - but maybe it should now remain OTLPAppender iface - unsure.
- [Sens/Jonathan/David] Needs triage - No Translation Mode for PrometheusRemotewrite Receiver
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/42425#issuecomment-3269941057](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/42425#issuecomment-3269941057)
  - There are workarounds, but that's a fair ask
  - Let's answer with the workaround (use a processor) to quickly unblock the person
  - Let's also say we're happy to enable the work, but needs to be done through the spec to ensure consistency in the ecosystem
  - Arthur will answer the issue
