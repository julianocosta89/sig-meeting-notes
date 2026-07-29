## Meeting Notes

### Attendees
- Jonathan Halliday (IBM)
- Felix Wong (IBM)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com)(Grafana Labs)
- Jason (Splunk)
- Jay DeLuca (Grafana Labs)
- Pranav Sharma (Google)
- Jack Shirazi (Elastic)
- Peter Findeisen (Cisco)
- Robert Niedziela (Splunk)
- Debashis Mitra (Upblit)
- Yuanfan Peng(Cisco)

### Agenda
- [Felix] Backporting CVE fixes to earlier versions
  - The advisory: [https://github.com/open-telemetry/opentelemetry-java/security/advisories/GHSA-rcgg-9c38-7xpx](https://github.com/open-telemetry/opentelemetry-java/security/advisories/GHSA-rcgg-9c38-7xpx)
  - Microprofile telemetry project with specification for each version (1.0, 1.1, 2.1), each pinned to a specific version of opentelemetry version
    - Oldest version 1.0, didn’t have any logs or metrics or, and so upgrading to patched version of opentelemetry-java
- [Gregor] Contrib relying on class to be removed in 3.0
  - [https://github.com/open-telemetry/opentelemetry-java-contrib/issues/2989](https://github.com/open-telemetry/opentelemetry-java-contrib/issues/2989)
    - [jack s] I will be able to get back to this next week
  - Should we add a milestone or label?
  - Created [https://github.com/open-telemetry/opentelemetry-java-contrib/issues?q=state%3Aopen%20label%3A%22instrumentation%203.0%22](https://github.com/open-telemetry/opentelemetry-java-contrib/issues?q=state%3Aopen%20label%3A%22instrumentation%203.0%22)
- [jack] Solving remaining declarative config pojo problems
  - Experimental properties have public getter / setter API surface area on stable types. This is a blocker for stabilizing.
  - When a property is stabilized and a user continues to use the old `*/development` version, is will be silently dropped from the parsed model.
    - Is something similar needed on instrumentation side?
    - Is something similar needed in DeclarativeConfigProperties?
