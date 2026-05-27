## Meeting Notes

### Attendees
- Antoine Toulme (Splunk)
- Andrew Wilkins (Elastic)
- Blake Rouse (Elastic)
- Josh MacDonald (Microsoft)

### Agenda
- Discuss
- Gate processor (Blake) discussion with Josh about exporterhelper and blocking
  - Recommend not adding complexity in gate, users can configure block_on_overflow and wait_for_result to inherit blocking timeout management from the exporterhelper w/o new cost.
- PSA: June 2, 2026 Tuesday 8am PT at the specification SIG will be a presentation on Collector v1 stability led by Pablo (?); June 9, 2026 at the same time will present OTel-Arrow Phase-2 by Laurent
- Inform sd_notify support [https://github.com/open-telemetry/opentelemetry-collector/issues/15128](https://github.com/open-telemetry/opentelemetry-collector/issues/15128)
