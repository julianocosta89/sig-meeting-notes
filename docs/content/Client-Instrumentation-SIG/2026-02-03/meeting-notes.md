## Meeting Notes

### Attendees
- Jason (Splunk)
- Maciek Grzybowski (Datadog)
- João Oliveira (Datadog)

### Agenda
- Http network and similar timing:
  - Please review if interested: [https://github.com/open-telemetry/semantic-conventions/issues/2827#issuecomment-3827130424](https://github.com/open-telemetry/semantic-conventions/issues/2827#issuecomment-3827130424)
  - Datadog already gets some of these - should have some input on this.
    - DD common schema “RUM event schema”
- Aggregation on the client side?
  - Example: how to answer this question like “Q: What views have the most number of errors?”
    - Session events handle this today
    - These are very much RUM questions
- We don’t have a great definition of session
  - Session id is [still] an attribute
  - Should we move it to the resource
