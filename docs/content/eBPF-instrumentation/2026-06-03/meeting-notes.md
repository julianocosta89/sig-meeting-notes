## Meeting Notes

### Attendees
- Roy Reshef (Kubex)
- Antonio Jimenez (ThousandEyes)
- Rob Cowart (ElastiFlow) - Apologies for being late
- Nikola Grcevski (Grafana)
- Tyler Yahn (Splunk)
- [Florian Lehner](mailto:florian.lehner@elastic.co) (Elastic)
- Rafael Roquetto (Grafana)
- Stephen Lang (Grafana)
- Mario Macias (Grafana)
- Marc Tudurí (Grafana)
- Mike Dame (Odigos)

### Agenda
- [Roy] Hello, I’d like to discuss porting the `grafana/beyla` **survey mode** feature into OBI. For various observability purposes, it is extremely valuable to have an identification of the application runtime of the container (regardless of whether further instrumentation of that container is required). I can elaborate on the motivation. Thank you.
- [Mike] Dynamic Selector expansion proposal: [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/2234](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/2234)
- [Antonio] Hey Nikola, what is the status of [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/1659](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/1659) , did you have a chance to start working on the first spike issue [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/1781](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/1781) . Thanks :)
  - [Nikola] Sorry, I’ve been swamped with other work, it will happen, just I need a bit more time.
- I have added a comment to [https://github.com/open-telemetry/semantic-conventions/issues/3682](https://github.com/open-telemetry/semantic-conventions/issues/3682) and would like the opportunity to discuss.
  - [Giuseppe] Hi Rob, thanks so much for the detailed comment! Unfortunately, I can’t join today’s meeting, but I’ll get back asap. We may also have a 1:1 meeting or talk during next week’s sig.
  - Postponing detailed discussion for next week
- [Stephen] RFC for selection by language runtime version: [#2207](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/2207)
- [Mike] Reminder-Go auto sunset sig call tomorrow
- [Antonio] On Monday I was at the OpenTelemetry semantic convention SIG meeting talking about some network attributes proposal. They want to set up a network group.
  - Is anyone interested here that I should invite too.
    - Mario Macias (Grafana)
    - Rob Cowart (ElastiFlow)
    - (?) Giuseppe Ognibene (Coralogix)
    - Stephen Lang (Grafana)
  - Here you can see the attribute that you may be interested too
    - IP Prefix [https://github.com/open-telemetry/semantic-conventions/issues/3731](https://github.com/open-telemetry/semantic-conventions/issues/3731)
    - AS (Autonomous System) Organization Number [https://github.com/open-telemetry/semantic-conventions/issues/3740](https://github.com/open-telemetry/semantic-conventions/issues/3740)
    - Reverse DNS [https://github.com/open-telemetry/semantic-conventions/issues/3741](https://github.com/open-telemetry/semantic-conventions/issues/3741)
- [Mario] Unresolved host renaming in server.address: [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/2035](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/2035)
- [Tyler] [Open PRs](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pulls)
