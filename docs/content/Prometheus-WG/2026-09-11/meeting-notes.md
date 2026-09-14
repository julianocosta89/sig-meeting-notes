## Meeting Notes

### Attendees
- Jonathan
- David Ashpole
- Kyle Eckhart
- Krajo
- Arve Knudsen
- Jack Berg
- Arthur Sens

### Agenda
- Krajo: discuss [https://github.com/open-telemetry/opentelemetry-specification/pull/4956](https://github.com/open-telemetry/opentelemetry-specification/pull/4956)  [https://docs.google.com/document/d/1jHfIOriXvBAFQ9PwRRuEqnmDH8nQ3U1cistdfE7XOIE/edit?tab=t.0](https://docs.google.com/document/d/1jHfIOriXvBAFQ9PwRRuEqnmDH8nQ3U1cistdfE7XOIE/edit?tab=t.0)
  - Arve: The problem I see with Option B is that it proposes a logical inconsistency: I.e. that the OTLP->Prometheus converter has to effectively treat scrape target identity as OTel resource identity. This might currently be how it works in the OTel Collector, but I think it makes the situation worse if this quirk has to be pushed into the Prometheus backend itself. It also has the problem that the scheme can not be applied for scrapers that represent multiple OTel resources.
  - [jack] Are the following statements about option C true?
    - The job/instance of series will change for anyone using the collector prometheus receiver.
      - With utf8, no change. Everyone with default settings will see a change.
    - Therefore, anyone using job/instance directly in queries (i.e. NOT joining on target info), will have their queries break.
    - Answer: Yes. (Or maybe not for C.1? Not clear.)
    - Question: Is it a non-starter to break any prom query leveraging job/instance of any user leveraging the collector prometheus receiver w/ default settings?
- From last meeting: How to do the roundtrip translation between Prometheus<->OTLP when entities are adopted by the industry.
- [Arthur]: [https://github.com/open-telemetry/opentelemetry-collector-releases/pull/1626](https://github.com/open-telemetry/opentelemetry-collector-releases/pull/1626)
  - We're releasing a new Collector distribution soon that includes Prometheus exporters.
  - Prometheus SIG becomes a maintainer for the distribution, and we get a say in what is included.
