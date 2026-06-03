## Meeting Notes

### Attendees
- Joshua MacDonald (Microsoft)
- Cijo Thomas (Microsoft)
- Drew Relmas (Microsoft)
- Kennedy Bushnell (Microsoft)
- Utkarsh Umesan Pillai (Microsoft)
- Aaron Marten (Microsoft)
- Nikhil Manchanda (Microsoft)
- Jake Dern (F5)
- Laurent Querel (F5)
- Max Jacinto

### Agenda
- [Triage]
  - Note! Try to modify triage labels
  - Through issue #3183
- [Drew] Metric Resource/Scope Attributes
  - [Self-telemetry attributes emitted as metric data-point attributes instead of Resource/Scope layers #3161](https://github.com/open-telemetry/otel-arrow/issues/3161)
  - [fix(observability): Emit resource/entity metric attributes at proper OpenTelemetry layer by drewrelmas · Pull Request #3168 · open-telemetry/otel-arrow](https://github.com/open-telemetry/otel-arrow/pull/3168)
  - About flow metrics, wanting to filter flow_metrics by scope attribute name: see issue #2742, noting that (#3161) we are not sending scope attributes correctly (nor resource level).
  - Discussion about [host.id](http://host.id) being incorrect, would now be detected by the new weaver live-check
- [Kennedy] FileLogReceiver - Aishwariya looking to contribute (GH Handle: IceRam)
  - Laurent proposes 3 ways to split this work
  - 1. Discovery of files and the extension interface
  - 2. Distributing files to multiple cores to actually read
  - 3. Format extensions for e.g., various formats
  - Shutdown & live reconfig
- [Cijo] Self-observability + Weaver enforcement,  ​​[https://github.com/open-telemetry/otel-arrow/pull/3175](https://github.com/open-telemetry/otel-arrow/pull/3175)
  - Already covered during Drew’s topic, when we touched on incorrect semantic convention!
- About all of the open PRs!
  - Ideas:
  - Drew: like Collector/Contrib use CODEOWNERS and auto-assign.
  - Everyone! Please review more PRs.
  - [ci: add PR size labeler workflow by cijothomas · Pull Request #2989 · open-telemetry/otel-arrow](https://github.com/open-telemetry/otel-arrow/pull/2989)  is to label PR size as a gentle reminder
  - Maybe reduce stale threshold to 2 weeks, let people re-open
- [Cijo]: How to move metrics macros to use weaver.
  - [laurent] OTel(and weaver) have no concept of metric_set in the metric semantic convention format
  - [jmacd] wants to talk about [Internal metrics telemetry pipeline and SDK design by jmacd · Pull Request #2623 · open-telemetry/otel-arrow](https://github.com/open-telemetry/otel-arrow/pull/2623)
    - Proposes to use a .yaml file for metric_set schema
    - Proposes to use metric-level dependent attributes (e.g., outcome, signal)
  - For the weaver group and metric_set, wanted a full specification
  - We should be able to define a metric_set yaml syntax, generate the code we need w/ minijinja templates. Recommend: use the semantic convention format, use the extension mechanism on top.
  - Relates with Drew’s PR on data point attributes. (in 2623 the diagrams cover this topic)
  - Ideally, we should use the new OTel Entities signal, entities define which attributes are in scope. (These can also be the correlation ID with otel_scope_info).
