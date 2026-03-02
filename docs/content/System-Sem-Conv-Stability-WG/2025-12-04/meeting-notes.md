## Meeting Notes

### Attendees
- Braydon Kains (Google)
- Pablo Baeyens (Datadog)
- Christos Markou (Elastic)
- Dmitry Anoshin (Splunk)

### Agenda
- Migration from old to new conventions in the Collector
  - Options we have
    - Environment variable
    - Feature gate pairs
      - We could do it per namespace/entity
      - We could it per component
    - Meta feature gate (meta feature gate pair?)
  - Criteria
    - It should be easy to 'double publish': use the old ones and the new ones at the same time
    - We need to keep it simple: per namespace may be too much
    - Typically feature gates only affect a single component (though there have been exceptions)
    - Per component means we are committing to the whole list of metrics/attributes to be stable before we mark the feature gate as stable
      - There are some metrics that are unclear if we want them now or not (e.g. openshift metrics?). This could be discussed on a case-by-case basis
