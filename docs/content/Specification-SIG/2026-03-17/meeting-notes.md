## Meeting Notes

### Attendees
- Daniel Dyla
- Dmitry Anoshin
- Josh Suereth
- Martin Kuba
- Arve Knudsen

### Agenda
- [dmitry] Service vs Observed Service (initial discussion)
  - Propose having "observed service" with same attributes as service, but also includes information about who was observing it.
    - make it clear they are separate and have relationship between them
    - How do we make sure we're not merging observed service *and* service? `observed by` would need to be identifying
    - Example
      - Service A runs on Process A
      - Collector C runs on Process C but has service D
      - Collector is observing Process A/Service A.
        - Service instance - Collector *cannot* synthesize a valid service instance id, it has to come from the process, by specification.
        - SDK generates it, collector doesn't have access.
    - [https://github.com/open-telemetry/opentelemetry-specification/pull/4719](https://github.com/open-telemetry/opentelemetry-specification/pull/4719)
    - Strawman -
      - We don't expect `service` on every Resource
      - We can synthesize an UUID for examples where [service.instance.id](http://service.instance.id) does not exist for prometheus compatibility.
  - Related spec PR [https://github.com/open-telemetry/opentelemetry-specification/pull/4905](https://github.com/open-telemetry/opentelemetry-specification/pull/4905)
- Quick recap of browser for Martin
  - Implement browser-specific SDK handling entities? Does this need specification change?
  - Josh's dumb experiment - [https://github.com/jsuereth/otlp-mmap](https://github.com/jsuereth/otlp-mmap)
- [suereth] Follow up active PRs
  - Will raise both PRs in the specification?
