## Meeting Notes

### Attendees
- Josh Suereth
- Dónal O’Sullivan (Elastic)
- Liudmila Molkova

### Agenda
- [rrschulze] [Initial definition of a Transaction Processing System](https://github.com/open-telemetry/semantic-conventions/pull/1898) (TPS) #1898
- [rrschulze] [Mainframe SIG plans](https://github.com/open-telemetry/semantic-conventions/issues/3330#issuecomment-3833467802) for 2026
  - Messaging and Database spans - how to address  them?
    - Database: interested in the server conventions
      - [https://github.com/open-telemetry/community/issues/1678](https://github.com/open-telemetry/community/issues/1678)
      - Write ibm-specific conventions, write and hype it and attract community this way
    - Messaging: also client and server
      - Server - same as db
      - Client - can we resurrect messaging SIG?
        - Let's try to start it this year, but it won't end this year
    - Job processing
      - Some generic concepts
      - Batch processing
      - At least 5 background jobs / scheduled in Java instr repo
        - Batch: spring batch
        - Span kind: internal ?
      - What's the intersection with messaging
        - Links + context propagation
        - Parent for just one
  - Status of entities and relationships?
    - Important in the context of metrics
    - [https://github.com/open-telemetry/opentelemetry-specification/pull/4836](https://github.com/open-telemetry/opentelemetry-specification/pull/4836)
  - Status of virtualization?
    - E.g. hosting on virtual machine and corresponding entities/resource detection
    - Check with container approvers
    - Needs some work, focused on k8s - need a semconv SIG for this
- [Dónal] [https://github.com/open-telemetry/semantic-conventions/pull/3461](https://github.com/open-telemetry/semantic-conventions/pull/3461)
  - process attribute requirement levels PR.
  - Liudmila will review.
- [Hilmar] Log.type [https://github.com/open-telemetry/semantic-conventions/pull/3469](https://github.com/open-telemetry/semantic-conventions/pull/3469)
  - This is a design doc more than a convention
  - Let's do prototyping and potentially OTEP where we can talk about problem and high-level solution
  - Semconv is the last step
  - What would be an example of prototype and otep
    - Service criticality is an  example
      - [https://github.com/open-telemetry/semantic-conventions/pull/3088](https://github.com/open-telemetry/semantic-conventions/pull/3088)
      - Prototype:
        - [https://github.com/open-telemetry/opentelemetry-demo/pull/2770](https://github.com/open-telemetry/opentelemetry-demo/pull/2770)
    - Oteps - [https://github.com/open-telemetry/opentelemetry-specification/tree/main/oteps](https://github.com/open-telemetry/opentelemetry-specification/tree/main/oteps)
  - Always is an explicit API call
    - Analyze existing audit log formats and see how to represent them in semconv / what's common across them
