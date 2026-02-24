## Meeting Notes

### Attendees
- Neil Yashinsky (Force Multiplier Labs / [ContextCore](http://contextcore.me/) )
- Carlos Cortez
- Alan Clucas (Pipekit)
- Dotan Horovits

### Agenda
- (timebox 7 min) Project Status + Triage + Blockers
- Calos - Long Running Spans
  - Reference to this issue a few week back ( [carlos] Long running spans: [https://github.com/open-telemetry/opentelemetry-specification/issues/373](https://github.com/open-telemetry/opentelemetry-specification/issues/373)
  - Discussion of how you send all of the attributes for spans
    - Long running traces have volume challenges
    - Span Events being deprecated doesn’t exactly complicate things, but its worth keeping in mind
    - Heartbeats - how required is it to get all the info in the variables
    - Neil suggested maybe deriving metrics from logs to reduce the need for lots of data being sent
    - Alan’s challenge _____
    - Carlos creating PR for the request, still have time to iterate’
      - Need an actual back end prior to going stable
    - Is it about the attributes changing more than the quantity?  Is the worry about updating attributes
      - If you have a few dozen long running processes
    - How often do long running spans get long running attributes
    - Alan - SIG has documented attributes
      - Alan supports some migration of CI/CD attributes to also cover Workflows.  He would be OK with them being fixed in time.  Jenkins and Github have the static info at a single point in time
      - If we need to log start, heartbeat and end - then bind attributes to that span
      - Ideally Alan would like the point to be flexible
    - For some attributes will have high cardinality - 1 per workflow run
      - Sounds high, but any CI/CD will want this level of cardinality
      - Example to bind back to the originating SHA1 in Git we end up at 1:1 mapping
