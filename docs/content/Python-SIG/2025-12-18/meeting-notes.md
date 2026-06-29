## Meeting Notes

### Attendees
- Alex Boten (Honeycomb)
- Aaron Abbott (Google)
- Joshua Winerman (Cisco/Splunk)
- Keith Decker (Cisco/Splunk)
- Riccardo Magliocchetti (Elastic)

### Agenda
- PSA: next meeting is January 8th
  - OpenTelemetry will observe an end-of-year break between Monday, Dec 22 and Fri, Jan 2. All SIG meetings are cancelled during this time. Responses may be delayed to non-security-related issues or pull requests.
- [Riccardo]: PTAL WIP PR for adding Tracer Config and Configurator [https://github.com/open-telemetry/opentelemetry-python/pull/4861](https://github.com/open-telemetry/opentelemetry-python/pull/4861)
  - This adds a way to enable / disable tracers
  - Specs still in development
  - There’s also for metrics and logs
  - Aaron: I can take a look
    - Given the experience with _logs that even if private has become the de-facto standard we can do something with @overload to separate the development part
      - Riccardo: I can look into that but in this specific case this is sdk only and not expect a lot of people to look into this
