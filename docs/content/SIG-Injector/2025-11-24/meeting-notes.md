## Meeting Notes

### Attendees
- Antoine Toulme (Splunk)
- Jack Berg (Grafana Labs)

### Agenda
- Package organization
  - Opentelemetry package is overarching
  - Opentelemetry depends on
    - Injector
      - Depends on <language_auto_instrumentation> package
    - OBI package
    - Collector
