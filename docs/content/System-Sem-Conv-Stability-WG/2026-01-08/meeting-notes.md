## Meeting Notes

### Attendees
- Braydon Kains (Google)
- Dmitry Anoshin (Splunk)
- Donal O’Sullivan (Elastic)
- Pablo Baeyens (Datadog)
- Roger Coll (Elastic)

### Agenda
- [Braydon] Update to OS-exclusive metric naming guidance [https://github.com/open-telemetry/semantic-conventions/pull/3261](https://github.com/open-telemetry/semantic-conventions/pull/3261)
- [Roger] Pressure metrics: [https://github.com/open-telemetry/semantic-conventions/pull/3068](https://github.com/open-telemetry/semantic-conventions/pull/3068)
  - Suffix -> time window -> guidelines
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/42779](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/42779)
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/45154](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/45154)
    - system.cpu.linux.pressure_average.10s tasks={some/total}
    - system.cpu.linux.pressure_average.total
- [Donal] Rename system.memory.shared to system.memory.linux.shared
  - [https://github.com/open-telemetry/semantic-conventions/issues/3260](https://github.com/open-telemetry/semantic-conventions/issues/3260)
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/45194](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/45194)
  - Go ahead and open the PR in semconv to change the name, no need to deprecate.
