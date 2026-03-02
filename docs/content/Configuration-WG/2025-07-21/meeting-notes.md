## Meeting Notes

### Attendees
- Tyler Yahn (Splunk)
- Dan Gomez Blanco (New Relic)

### Agenda
- [Triage project board](https://github.com/orgs/open-telemetry/projects/38)
- [dan] Related to [Controlling context propagation boundary · Issue #1633 · open-telemetry/opentelemetry-specification · GitHub](https://github.com/open-telemetry/opentelemetry-specification/issues/1633)
  - Aiming to raise an OTEP for this in the coming weeks and looking for prior art regarding common areas in instrumentation config (e.g. HTTP, messaging)
  - Reason for proposing common config and not Propagators API/SDK changes includes the fact that makes sense that responsibility of Propagators API ends at injecting/extracting into/from carrier, and same propagator (e.g. W3C Baggage) may need different config to control boundaries for HTTP vs messaging or other instrumentations.
  - As part of OTEP, prototype in Java (where other prior art for common config is already in place) would help
