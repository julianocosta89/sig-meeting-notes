## Meeting Notes

### Attendees
- Jay DeLuca (Grafana Labs)
- [John Watson](mailto:jkwatson@gmail.com)(Sublime Security)
- Trask Stalnaker (Microsoft)
- Jason (Splunk)
- [John Watson](mailto:jkwatson@gmail.com)(Sublime Security)
- Jonathan Halliday (IBM)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com) (Grafana Labs)
- Pranav Sharma (Google)
- Peter Findeisen (Cisco)
- Jack Shirazi (Elastic)
- Lauri Tulmin (Splunk)

### Agenda
- Java Instrumentation v3 review
  - Database semconv stability
    - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/12608](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/12608)
    - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/19019](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/19019)
    - [**https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/19036**](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/19036)
    - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/18903](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/18903)
  - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues?q=is%3Aissue%20state%3Aopen%20milestone%3Av3.0.0](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues?q=is%3Aissue%20state%3Aopen%20milestone%3Av3.0.0)
  - Can we improve our integration with Micrometer?
    - Currently disabling micrometer and spring actuator by default
      - Sometimes they emit metrics with same name, which causes SDK warnings
      - Sometimes they emit same metric with different names, which is also confusing
    - Can we make enabling it less painful?
      - Can we default exclude specific known problematic metrics?
    - Are there metrics that would be useful for us to add natively?
- [Jay] I am writing a blog about the 3.0 release
  - [Java Agent 3.0 Blog Post](https://docs.google.com/document/d/160OROdFGqkAoSf1dOA39XiuS3fHNJ9w9aVAGzEcAVL0/edit?usp=sharing)
  - Highlighting: database and code semconv, things that could impact queries, how to run the duplicate mode to test things out before upgrading, a nudge to use declarative config
  - Anything else we should add?
    - Indy - if it lands
  - Extra blog for spring boot DC (Gregor)?
    - Better dedicated post
