## Meeting Notes

### Attendees
- [Jay DeLuca](mailto:jay.deluca@grafana.com) (Grafana Labs)
- Tiffany Hrabusa (Grafana Labs)
- Patrice Chalin (CNCF)
- Severin Neumann (Causely)
- Vitor Vasconcellos (Mercado Libre)
- Sophia Solomon (Elastic)

### Agenda
- [Patrice] [https://agents.md](https://agents.md) - is it time to add this and try it out? ([Maintainers Slack thread context](https://cloud-native.slack.com/archives/C06EDFPQ5EH/p1756290368722199))
  - Let’s have it
- [Jay] I want to explore ways we can improve instrumentation documentation. I have been implementing [metadata](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/instrumentation-list.yaml) for java to try and automate some of this. I am thinking the outcome of this discussion will be a github issue where we can continue hashing out details.
  - Problem:
    - Instrumentation is complex (javaagent vs library, configs, variable telemetry, target versions etc)
    - The existing github READMEs are not indexed by google.
      - Current (java) docs:
        - [Supported libraries list](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/supported-libraries.md)
        - [Individual library doc](https://github.com/open-telemetry/opentelemetry-java-instrumentation/tree/main/instrumentation/kafka/kafka-clients/kafka-clients-2.6/library)
  - Goal is to be able to answer questions like:
    - *Will the version of library x that I use be instrumented automatically?*
    - *The library I use is listed in “supported libraries”, what telemetry will I get?*
    - *Are there any configurations I can enable to get additional attributes on my metrics or spans?*
    - *Are there any configurations I can enable to get more/less metrics or spans for the libraries I use?*
    - *I’m about to upgrade my auto-instrumentation from version x to version y, what telemetry or attributes changed?*
  - Experimenting with automating instrumentation documentation based on metadata. Created a UI tool called the [Instrumentation Explorer](https://jaydeluca.github.io/instrumentation-explorer/). What do you think about incorporating this in [opentelemetry.io](http://opentelemetry.io) and/or the registry?
    - Blog posts about the creation process: [first](https://sensorsandsignals.io/posts/2025/otel-instrumentation-metadata-project/), [second](https://sensorsandsignals.io/posts/2025/otel-instrumentation-metadata-telemetry-variations/), [third](https://sensorsandsignals.io/posts/2025/leveraging-instrumentation-metadata/)
    - Examples:
      - [Couchbase-2.6](https://jaydeluca.github.io/instrumentation-explorer/library/2.19/couchbase-2.6)
      - [Cassandra-4.0](https://jaydeluca.github.io/instrumentation-explorer/library/2.19/cassandra-4.0)
      - [Application analyzer](https://jaydeluca.github.io/instrumentation-explorer/analyze?instrumentations=YXBhY2hlLWh0dHBjbGllbnQtNS4wLGV4ZWN1dG9ycyxoaWthcmljcC0zLjAsaHR0cC11cmwtY29ubmVjdGlvbixqYXZhLWh0dHAtY2xpZW50LGphdmEtaHR0cC1zZXJ2ZXIsamRiYyxrYWZrYS1jbGllbnRzLTAuMTEsbG9nYmFjay1hcHBlbmRlci0xLjAsbWljcm9tZXRlci0xLjUscm1pLHNwcmluZy1ib290LWFjdHVhdG9yLWF1dG9jb25maWd1cmUtMi4wLHNwcmluZy1jb3JlLTIuMCxzcHJpbmctZGF0YS0xLjgsc3ByaW5nLXNjaGVkdWxpbmctMy4xLHNwcmluZy13ZWItNi4wLHNwcmluZy13ZWJtdmMtNi4wLHRvbWNhdC0xMC4w&version=2.19) (generated from a new WIP feature of [otel-checker](https://github.com/grafana/otel-checker))
- [Tiffany] Any thoughts on how best to address the [Collector patch release issue](https://github.com/open-telemetry/opentelemetry.io/issues/7546)?
  - I attended the Collector SIG meeting today to learn a little more about the problem. See the explanation I received from one of the Collector Approvers below.
- [localization] Kicking off [Romanian localization](https://cloud-native.slack.com/archives/C076RUAGP37/p1756887767746729).
- [Tiffany] Update on Collector docs refactoring. [Proposed rearchitecture](https://www.mindomo.com/mindmap/c6ececd0512d46edb8f5048d19f18de1) was presented to Collector SIG today. Feedback was very positive. Slack thread for asynchronous feedback: [https://cloud-native.slack.com/archives/C01N6P7KR6W/p1756843654525619](https://cloud-native.slack.com/archives/C01N6P7KR6W/p1756843654525619)
