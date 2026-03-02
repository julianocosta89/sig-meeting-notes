## Meeting Notes

### Attendees
- Pierre Tessier (Honeycomb)
- [Juliano Costa](mailto:juliano.costa@datadoghq.com)(Datadog)
- Ani (OpenSearch)
- Alessio (Suse)
- Shenoy Pratik (OpenSearch)
- Roger Coll (Elastic)
- Jonathan Munz (Embrace)

### Agenda
- [Alessio] Adding an Elixir based service to the demo
  - Decided to rewrite the flagd-ui with Elixir instead of adding a new service
- [Pierre] [Next.js](http://Next.js) auto instrumentation continues to cause some issues with adding a span.kind = server.
  - Instead of fixing this in the demo, we will ask the JS SIG to work with the auto-instrumentation library to clean up span.kind and [span.name](http://span.name)
