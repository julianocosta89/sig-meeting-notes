## Meeting Notes

### Attendees
- Josh MacDonald (Microsoft)
- Laurent Querel (F5)
- Albert Lockett (F5)
- Jake Dern (F5)
- Aaron Marten (Microsoft)
- Utkarsh Umesan Pillai (Microsoft)
- Tom Tan (Microsoft)

### Agenda
- [Albert]: propose renaming otlp_exporter to otlp_grpc_exporter
  - Change URN accordingly urn:otel:otlp:exporter -> urn:otel:otlp_grpc:exporter
  - Consensus: makes sense!
- [Laurent]: Topic rounds 2 and 3
  - Topics are a mechanism to bind producers and consumers across pipelines, whether in a single group (core) or across cores. (Round 1 was last week, configuration model)
  - Current work on in-memory topic broker. Plan to support durable queue from topics in the future.
  - Round 2: the channel implementation by itself, topic exporter can write to channel, topic receiver can read from channel. Receiver has metadata about the kind of subscription: broadcast is one thing, load balance is a different thing.
  - Round 3: connect the new channel and topic receiver/exporter with the rest of the engine. Use the parsed/validated configuration to create the necessary topic exporter/receiver components and connect with pipelines. Includes a configuration model sufficient for the example below.
  - Description of a pipeline: Receiver -> Content processor -> Topic exporters; Topic receiver -> Per-tenant pipeline. This can be working by next week.
  - Description of a pipeline: Receiver -> Topic exporter; Topic receiver -> … This is to enable live reconfiguration of the second part, after the topic.
  - Notes: Ack/Nack is propagated backwards through topics. A MPSC channel is used to send messages to the pipeline controller (same core, today); idea is to link Ack/Nack delivery in a topic receiver to the next receiver _on a different core_.
  - Note that pipeline placement could take inter-group and inter-core communication as defined by the configuration into account, for example to place pipelines that communicate on the same NUMA node.
  - Note we can move transforms across topic boundaries, …
  - About limits for tenants: CPU limits are available on a per-thread basis; we can also monitor memory allocation per thread (tenant), we should be able to control CPU or memory limits at this level of granularity.
- [Josh] Thought experiment: how does an “embedded pipeline” differ from a “telemetry SDK”?
  - [LQ]: there are signs of community interest, look at NYC Rust meetup
- [Jake] New OTAP Spec draft today: [Pull requests · open-telemetry/otel-arrow](https://github.com/open-telemetry/otel-arrow/pull/2040)
- [Drew from Slack]: ask for additional eyes on [https://github.com/open-telemetry/otel-arrow/pull/2033](https://github.com/open-telemetry/otel-arrow/pull/2033)
  - The context is [https://github.com/open-telemetry/otel-arrow/issues/1964](https://github.com/open-telemetry/otel-arrow/issues/1964)
- [Utkarsh] [Refactor URN format: Flip component name and type ordering · Issue #2108 · open-telemetry/otel-arrow](https://github.com/open-telemetry/otel-arrow/issues/2108)
