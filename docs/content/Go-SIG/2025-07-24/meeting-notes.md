## Meeting Notes

### Attendees
- Damien Mathieu (Elastic)
- Bryan Boreham (Grafana Labs)
- Tyler Yahn (Splunk)
- Sam Xie (Splunk)

### Agenda
- [Sam]: Host TextAttributes propagator in contrib to support sql commenter
  - Reason: for stable correlation. Mitigate double sampling, as databases usually do not support trace.
  - Context: sql commenter on semconv repo [https://github.com/open-telemetry/semantic-conventions/pull/2495#discussion_r2209133620](https://github.com/open-telemetry/semantic-conventions/pull/2495#discussion_r2209133620)
- [Damien] Will be off from August 1st to 25th
