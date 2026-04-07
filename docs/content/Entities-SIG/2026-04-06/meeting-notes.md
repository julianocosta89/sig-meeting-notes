## Meeting Notes

### Attendees
- [krajo Krajcsovits](mailto:gyorgy.krajcsovits@grafana.com)
- Josh Suereth
- Arve

### Agenda
- Lots of noob questions from Krajo
  - General question: what problem are entities solving ? Discovery/grouping and/or separation of identifying resource attributes and descriptive attributes? This is probably written somewhere, but I'm looking at the spec.
    - [https://github.com/open-telemetry/opentelemetry-specification/tree/main/oteps/entities](https://github.com/open-telemetry/opentelemetry-specification/tree/main/oteps/entities)
    - Elevator pitch - Left-hand nav.
    - Meeting Recordings - [https://github.com/open-telemetry/community?tab=readme-ov-file#governing-bodies](https://github.com/open-telemetry/community?tab=readme-ov-file#governing-bodies)
  - General question: when I have a metric with its attributes and identifying resource attributes pointed out by entities, is the expected UX that the metric is the same continuous metric as long as its attributes and identifying attributes remain the same ? I.e. same continuous color line on graph.
    - yes
  - General question: when a metric is associated with more than one entity, what UX do we expect to see when potentially only one entity changes? As in POD moved to a different host ? I would assume this never results in the same metric, so the line on the graph would be a different line for the new POD?
  - The SDK [https://github.com/open-telemetry/opentelemetry-specification/blob/cf7eaed8056917779a1b3581cd81a6695c7b0b52/specification/resource/sdk.md?plain=1#L70](https://github.com/open-telemetry/opentelemetry-specification/blob/cf7eaed8056917779a1b3581cd81a6695c7b0b52/specification/resource/sdk.md?plain=1#L70)  says that the resources merged *later* win.
    - How will we deal with a customer when they inevitably complain about missing some resource data? Or get surprising results when searching by some resource attribute.
    - A: keep it simple and motivation for entities . People that care should put in resources in inverse order so least important to most important so the most important wins.
  - For entities [Placement of Shared Descriptive Attributes](https://github.com/open-telemetry/opentelemetry-specification/blob/cf7eaed8056917779a1b3581cd81a6695c7b0b52/specification/entities/data-model.md?plain=1#L132) says that the "most specific entity" references the conflicting descriptive attribute.
    - First issue: "most specific" is not defined, what are the plans? I heard it's just deferred to later time?
    - Most specific as in for example : generic host detector vs AWS host detector.
    - In general namespace prefix of names helps
  - Does the SDK make sure that when a resource attribute is overwritten with a different value, then the reference from the old entity is cleared ? Otherwise the entity would point to the wrong resource attribute. How do you reconcile the "most specific" reference with the last merged wins algorithm? Will the merge algorithm be changed?
  - Is it too late to amend the specification in a way that either prohibits conflicts (i.e. reject) or makes sure that the missing information is included in the passed OTLP message ?
    - Proposal: count of dropped attributes + collector has error log
    - Proposal: OTLP resolve conflicts + tells database that something was wrong
    - Current non-stable implementation means we cannot know at the database if there was a conflict and
  - Second issue: to restore the missing data, it is suggested to implement a "separate telemetry channel (e.g., entity events)". Unfortunately due to an asynchronous nature of any side channel, this would mean that potentially running the exact same query would return different results over time. From experience we know that if such a thing happens, we get support tickets - so we avoid these situations at all cost.
    - Relax: time sensitive alerting of course cannot depend on this - however other use cases would work fine. Allowable for "non fast alert" analytic use cases.
    - Example: VM name can change over time, but not id. So if VM name is metadata that comes in different path it can be out of sync - but you can educate people about this.
