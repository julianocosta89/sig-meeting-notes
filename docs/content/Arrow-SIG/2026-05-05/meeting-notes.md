## Meeting Notes

### Attendees
- Laurent Querel (F5)
- Kennedy Bushnell (Microsoft)
- Drew Relmas (Microsoft)
- Tom Tan (Microsoft)
- Jake Dern (F5)
- Max Jacinto
- Will Butler (Microsoft)
- Albert Lockett (F5)
- Josh MacDonald (Microsoft)
- Chanly Ly (F5)
- Aaron Marten (Microsoft)
- Nikhil Manchanda (Microsoft)
- Gokhan Uslu (Microsoft)
- Victor Lu (Microsoft)
- Sameer J (Microsoft)
- Saroj Kumar Patra (Microsoft)

### Agenda
- [Triage]
  - Note! Try to modify triage labels
- [Jake] benchmarks
  - Now covering HTTP/gRPC, DFE, Collector, Rotel, fluentbit and (needs work) Vector
  - Over 200 scenarios, not ready to run automatically
- [Laurent] musl
  - We observed a performance regression on high-scale machines
  - Now using GoogleContainerTools/distroless, problem solved
  - Could have been the memory allocator and/or multithreading behavior
  - TODO: Document that we cannot use just any container image
- [Laurent] filelog receiver
  - [https://github.com/open-telemetry/otel-arrow/issues/2844](https://github.com/open-telemetry/otel-arrow/issues/2844)
  - How will we ensure no data loss in a way consistent with the DFE architecture?
  - Idea about Ack/Nack checkpointing
  - Considering [opentelemetry-collector-contrib/pkg/stanza at main · open-telemetry/opentelemetry-collector-contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/pkg/stanza), a proposal to split the monolithic design found here, ideally to move data processing into processors
