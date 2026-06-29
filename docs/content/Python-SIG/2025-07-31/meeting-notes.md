## Meeting Notes

### Attendees
- Hector Hernandez (Microsoft)
- Aaron Abbott (Google)
- Keith Decker (Cisco/Splunk)
- Pablo Collins (Cisco/Splunk)
- Riccardo Magliocchetti (Elastic)

### Agenda
- [Keith] Weaviate Instrumentation Skeleton - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3646](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3646)
  - [aaron] will take a look
- [Aaron] [Runtime context fails to detach token · Issue #2606 · open-telemetry/opentelemetry-python · GitHub](https://github.com/open-telemetry/opentelemetry-python/issues/2606)
  - Improve docs about this
- [Aaron] [Infinite loop through exporter, when using OTLPLogExporter · Issue #4688 · open-telemetry/opentelemetry-python](https://github.com/open-telemetry/opentelemetry-python/issues/4688)
  - If there’s not otlp receiver running do you expect to see errors?
  - Pablo: played a bit with this, I think when we detect network issues we should be using a separate queue until it is resolved
    - Aaron: please leave a comment
    - Should take at what other languages are doing ➕
- [John] Any good first issues?
  - Yes we have! Also docs!
