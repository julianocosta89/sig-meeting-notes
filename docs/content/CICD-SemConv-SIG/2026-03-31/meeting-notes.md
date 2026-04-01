## Meeting Notes

### Attendees
- Adriel Perkins (Grainger)
- Christophe Kamphaus
- Dotan Horovits (OpenSearch, AWS)

### Agenda
- (timebox 7 min) Project Status + Triage + Blockers
  - Project Board: [https://github.com/orgs/open-telemetry/projects/171](https://github.com/orgs/open-telemetry/projects/171)
- General
  - Christophe KubeCon feedback
    - We can remove towards release candidate for stabilization of cicd conventions
    - We didn’t have any big changes in the last year
    - We have implementations in the collector so the requirement for implementation that are necessary for stabilization
    - It’s up to us if we want to move forward
      - Potential blockers
        - Unified pipeline semantics - if we stabilized this would become a breaking change
        - On the other hand, this is a huge change and effort to unify these which would push things back
          - There’s no significant driving force behind
          - If this becomes the expanded scope this would necessitate a breaking change
        - We should bring this up in the general semantic conventions meeting
        - The original ask was to start within the CICD scope so as to not block progress
        - Is this biting off something more than we can chew in our current state?
        - There is a broader scope in discussion, but it may not be part of stabilization.
    - We should consciously move towards stabilization.
    - Next step: bring this up in the next semconv meeting Monday April 6th at 11 ET
    - People are starting to implement so we don’t want to leave it in development too much longer (re: deployment.environment vs [deployment.environment.name](http://deployment.environment.name))
    - How do we migrate people for breaking changes if they come up leveraging Weaver/OTel Collector [https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/schemaprocessor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/schemaprocessor)
    - When we create PR to move to RC, we should also create a blog post for advertisement and define when we want to go to release so vendors, etc, can give us feedback in that time.
  - [carlos][3 min] Extending SpanProcessor with span lifecycle operations: [https://github.com/open-telemetry/opentelemetry-specification/issues/5002](https://github.com/open-telemetry/opentelemetry-specification/issues/5002)
