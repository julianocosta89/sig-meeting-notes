## Meeting Notes

### Attendees
- Daniel Dyla
- Jared Freeze (Embrace)
- Joaquin Diaz (Embrace)
- David Luna (Elastic)
- Surbhi A (Cisco)

### Agenda
- [Surbhi A] Discuss **standalone event** VS **individual timestamp attributes in original HTTP span** for HTTP network phase breakdown metrics as discussed in this issue, in an attempt to unify the semantic conventions across browser and mobile  - [https://github.com/open-telemetry/semantic-conventions/issues/2827](https://github.com/open-telemetry/semantic-conventions/issues/2827)
  - Drawback with standalone event is that all original HTTP span attributes (like **http.request.method**, **http.response.status_code** etc) which are needed for filtering metrics later (an important use case) are not available on this event and even if they were to be made available, it would mean replicating a lot of the original span data on this event.
  - I want to propose **individual timestamp attributes in original HTTP span**, it does mean that the span has to wait for sometime until all the asynchronous callbacks are done so all those timestamps can be included in the span but this helps in the following ways:
    - Unifying semantics across browser and mobile
    - Having all attributes that are needed for filtering on top of the aggregated metrics.
    - Backends don’t have to correlate between the original HTTP span and this event.
    - Per request level data is available.
  - [Action Item]: start a thread in slack to continue the conversation
    - [Joaquin]: to me it makes sense to be consistent with other client SDKs
- [Jared] Who will be submitting instrumentation to otel-browser?
  - [Joaquin] Start with a simple one so we have a sample to follow up for other instrumentations like user action, first we need this merged https://github.com/open-telemetry/semantic-conventions/pull/1941
