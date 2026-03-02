## Meeting Notes

### Attendees
- Drew Relmas (Microsoft)
- Jake Dern (Microsoft)

### Agenda
- [Jake] Question about otelarrowexporter - Why does it spawn 11 separate gRPC streams/connections and also time out the streams after 30 seconds by default?
  - Possible answer for the 11 separate connections is that the exporter uses half the number of reported available cores, in this case 22.
- [Jake] Question about delta dictionary support in otel-arrow-rust - Looks like support is not implemented yet. Is this something being worked on and/or open to contribution?
