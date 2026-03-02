## Meeting Notes

### Attendees
- [John Watson](mailto:jkwatson@gmail.com)(Cloudera)
- Jack Shirazi (Elastic)
- Jay DeLuca (Grafana Labs)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com) (Grafana Labs)
- Trask Stalnaker (Microsoft)
- Robert Niedziela (Splunk)
- Jonathan Halliday (IBM)
- Jason (Splunk)
- cleverchuk(solarwinds)
- Anvesh (Redpin)

### Agenda
- Standing topic: issue triage
  - [is:open -label:"needs author feedback","needs repro","contribution welcome"](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues?q=is%3Aissue+is%3Aopen+-label%3A%22needs+author+feedback%22%2C%22needs+repro%22%2C%22contribution+welcome%22)
  - [is:open label:"needs triage"](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues?q=is%3Aissue+is%3Aopen+label%3A%22needs+triage%22)
- Standing topic: [stackoverflow questions](https://stackoverflow.com/search?tab=newest&q=%5bopen-telemetry%5d%20java)
- [Jack s] “sampler already supports eg 20% samples but 100% errors” - from fly-by comment in APAC meeting, how does it do that? (or is this a custom sampler that you could implement and add?)
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/probabilisticsamplerprocessor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/probabilisticsamplerprocessor)
- FYI: Sampling rate can now be propagated: consistent sampler in contrib
  - PR to move to SDK incubator (will have some renaming)
  - Ask about .NET developers (Gregor)
- [Gregor] [init logic question](https://github.com/open-telemetry/opentelemetry-java/pull/7475)
- [Jay] Update on instrumentation explorer
  - [https://jaydeluca.github.io/instrumentation-explorer/](https://jaydeluca.github.io/instrumentation-explorer/)
- [antoine] - packaging [https://github.com/open-telemetry/opentelemetry-java/pull/7634](https://github.com/open-telemetry/opentelemetry-java/pull/7634)
  - Discussed in APAC meeting
- HTTP Client span naming
  - OpenFeign -> OkHTTP (HttpUrlConnection?)
  - OpenFeign has support for `url.template`
  - (Similar for Retrofit)
  - UrlTemplate similar to HttpRoute
- [jason] more of a spec question, but does anybody know if there is language about sync gauges? [https://github.com/open-telemetry/opentelemetry-java/pull/7634](https://github.com/open-telemetry/opentelemetry-java/pull/7634)
