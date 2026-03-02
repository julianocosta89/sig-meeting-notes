## Meeting Notes

### Attendees
- Cijo Thomas (Microsoft)
- [Scott Gerring](mailto:scott.gerring@gmail.com)(Datadog)
- Lalit Kumar Bhasin (Microsoft)

### Agenda
  - Looks like we have some breaking changes, so better to do 0.31
  - And delay until we get majority of Tracing API breaking changes in
  - Tracer.in_span
  - Tracer.SpanBuilder()...builder()
  - Both has usability issue and likely performance issues.
  - [cijo] to add benchmarks to see if the perf issues are measurable/impactful
