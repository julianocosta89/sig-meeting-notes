## Meeting Notes

### Attendees
- Martin Kuba (Grafana Labs)
- [Daniel Dyla](mailto:dyladan@gmail.com)
- Jared Freeze (Embrace)
- Joaquin Diaz (Embrace)
- Marco Schaefer (Grafana Labs)
- Wolfgang Therrien ([Honeycomb.io](http://Honeycomb.io))
- David Luna (Elastic)
- Benoit Zugmeyer (Datadog)
- Trent Mick (Elastic)

### Agenda
- [Trask] Invitation to join Semantic Convention SIG meeting Monday, Nov 17 to discuss confusion between app.* namespace and Kubernetes app.* [https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/#labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/#labels)
- [Marc] I talked to other JS Maintainers about how we could unblock some work that the Browser SIG is doing/avoid bottlenecks
  - idea: we can make Browser SIG Maintainers approver-equivalent in the JS repos for browser-targeted packages in JS core/contrib - limited by CODEOWNERS file similar to how it works on the SemConv repo.
  - Q: Is anyone opposed to doing this? :)
  - We identified these packages: [https://github.com/open-telemetry/opentelemetry-browser](https://github.com/open-telemetry/opentelemetry-browser)
- [Joaquin] Move forward with [https://github.com/open-telemetry/opentelemetry-browser/pull/35](https://github.com/open-telemetry/opentelemetry-browser/pull/35) or wait for semconv?
- [Wolfgang]
  - Needs an clear ‘req changes’ from Martin
  - [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2751](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2751)
- [Jared] First pass at Turbo scaffold [https://github.com/open-telemetry/opentelemetry-browser/pull/44](https://github.com/open-telemetry/opentelemetry-browser/pull/44)
