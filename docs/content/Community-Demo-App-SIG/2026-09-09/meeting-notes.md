## Meeting Notes

### Attendees
- Juliano Costa (Datadog)
- Dónal O’Sullivan (Elastic)
- Tobias Oka (Datadog)

### Agenda
- Feedback on instrumentation change to allow operator to perform instrumentation:
- [Dónal] Podman fixes
  - Move CI checkouts out into another PR, only run podman build checks on the specific dockerfile only, when code changes for a specific service. Do not run the entire suite of dockerfiles.
