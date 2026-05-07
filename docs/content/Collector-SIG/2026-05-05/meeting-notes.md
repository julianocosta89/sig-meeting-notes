## Meeting Notes

### Attendees
- Antoine Toulme (Splunk)
- Andrew Wilkins (Elastic)
- Blake Rouse (Elastic)
- Josh MacDonald (Microsoft)
- Dmitrii Anoshin (Splunk)
- Sean Marciniak (Splunk)

### Agenda
- [15 min] Go through high priority issues for [stability phase 1](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44130) listed on the [**board**](https://github.com/orgs/open-telemetry/projects/178)
- [Antoine] [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/47162](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/47162) discuss this PR, codeowners role associated, and steps to resolve the issue.
- [Blake] Partial Reload RFC
  - [https://github.com/open-telemetry/opentelemetry-collector/pull/14640](https://github.com/open-telemetry/opentelemetry-collector/pull/14640)
  - Alternative component replacement with gates added between components.
    - This PR just provides the gate module and shows benchmarks of the minimal overhead it adds, that would allow component replacement direct in pipeline.
    - [https://github.com/open-telemetry/opentelemetry-collector/pull/15254](https://github.com/open-telemetry/opentelemetry-collector/pull/15254)
- [Andrew] Status of batch/pipeline/? processor
  - Missing from v1 issue list, should it be there?
  - Josh is working on an RFC – not quite ready yet for review
    - Rough idea:
      - Feature gate in exporterhelper
        - Off: current
        - On: default has batching
      - Context marker: “I have been batched by the batch processor” -> avoids double batching
      - Maybe less magic: if the batch configurations are compatible with each other, the cost of double batching may not be large
      - Consider using the config_converter feature: we can have access to the whole configuration.
