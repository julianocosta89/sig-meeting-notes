## Meeting Notes

### Attendees
- [John Watson](mailto:jkwatson@gmail.com)(Cloudera)
- Jonathan Halliday (IBM)
- Sylvain Juge (Elastic)
- Jack Berg (Grafana Labs)
- Jack Shirazi (Elastic)
- Jay DeLuca (Grafana Labs)
- [Ivo Anjo](mailto:ivo.anjo@datadoghq.com) (Datadog)
- Jason (Splunk)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com)(Grafana Labs)
- Lauri Tulmin (Splunk)

### Agenda
- Standing topic: issue triage
  - [is:open -label:"needs author feedback","needs repro","contribution welcome"](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues?q=is%3Aissue+is%3Aopen+-label%3A%22needs+author+feedback%22%2C%22needs+repro%22%2C%22contribution+welcome%22)
  - [is:open label:"needs triage"](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues?q=is%3Aissue+is%3Aopen+label%3A%22needs+triage%22)
  - ![][image1]
  - ![][image2]
- Standing topic: [stackoverflow questions](https://stackoverflow.com/search?tab=newest&q=%5bopen-telemetry%5d%20java)
- [jack] public sender provider API [https://github.com/open-telemetry/opentelemetry-java/pull/7782](https://github.com/open-telemetry/opentelemetry-java/pull/7782)
  - Big complicated PR, driven by need to minimize API and stop leaking unnecessary details into senders
  - Can break it into pieces, but want all to be merged in one release cycle to minimize churn
- [Jay] [Extension documentation](https://github.com/open-telemetry/opentelemetry.io/pull/8264)
  - Any initial thoughts on the verbosity/content included?
  - Preferences on having code snippets embedded or linking out to external?
  - Jay to look into ENV var stuff
- [Ivo Anjo](mailto:ivo.anjo@datadoghq.com) update on [Sharing Process-Level Resource Attributes with the OpenTelemetry eBPF Profiler](https://docs.google.com/document/d/1-4jo29vWBZZ0nKKAOG13uAQjRcARwmRc4P313LTbPOE/edit?tab=t.0): Demo of publishing process context automatically via OTEL Java SDK extension: [https://github.com/ivoanjo/proc-level-demo/tree/main/otel-java-extension-demo](https://github.com/ivoanjo/proc-level-demo/tree/main/otel-java-extension-demo)
- [Sylvain] opinions on dealing with “minor” breaking change in context of [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/15093](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/15093) ?
- [jason] Stable things must have stable components? Any progress on what we’re going to do about [https://github.com/open-telemetry/opentelemetry.io/pull/8208](https://github.com/open-telemetry/opentelemetry.io/pull/8208) and whatever spec work falls out of that?
  - Now:
    - Foo:
      - Enabled: false # default
  - Later:
    - Foo:
      - Enabled: true # default
  - Default_instrumentation_stability_threshold: stable # default
    - Other options: beta, alpha, etc.
    - The default would be beta
