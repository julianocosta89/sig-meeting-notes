## Meeting Notes

### Attendees
- Wolfgang Therrien ([Honeycomb.io](http://Honeycomb.io))
- Jared Freeze (Embrace)
- Joaquin Diaz (Embrace)
- Martin Kuba (Grafana Labs)
- Benoit Zugmeyer (Datadog)
- Abinet Debele (Cisco)

### Agenda
- 🎉Our first event-based instrumentation has been merged!
  - [https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main/packages/instrumentation-web-exception](https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main/packages/instrumentation-web-exception)
  - Big thanks to Wolfgang!
- [Jared] Link to url proposal [https://cloud-native.slack.com/archives/C093P0AMP0T/p1762968686640619?thread_ts=1762905449.223569&cid=C093P0AMP0T](https://cloud-native.slack.com/archives/C093P0AMP0T/p1762968686640619?thread_ts=1762905449.223569&cid=C093P0AMP0T)
  - [https://github.com/open-telemetry/semantic-conventions/blob/main/docs/registry/attributes/url.md](https://github.com/open-telemetry/semantic-conventions/blob/main/docs/registry/attributes/url.md)
- page / document ID
  - Benoit to open issue with use cases
- Request for review of
  - Navigation instrumentation, [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3148](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3148)
  - User Actions instrumentation
- Navigation Instrumentation
  - action item: Abinet to do a demo of the instrumentation next week
- Other action items
  - create issue for our approach to migrating instrumentations to the browser repository
- Stabilizing instrumentations
  - stabilize semantic conventions first?
  - what is preventing instrumentations that have been around for a long time to become stable?
  - define process / support for stable instrumentations vs experimental
  - should we formalize maintainers for the browser SDK?
