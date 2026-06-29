## Meeting Notes

### Attendees
- Paulo Vital (IBM)
- Riccardo Magliocchetti (Elastic)
- Keith Decker (Splunk/Cisco)
- Dylan russell (google)
- Aaron Abbott (Google)
- Dan Gomez Blanco (New Relic)
- Pablo Collins (Splunk/Cisco)
- Hector Hernandez (Microsoft)

### Agenda
- [aaron] Logs API/SDK to beta?
  - How do we feel?
  - Where do we update that it’s beta?
  - [https://github.com/open-telemetry/opentelemetry-specification/blob/main/oteps/0232-maturity-of-otel.md#development](https://github.com/open-telemetry/opentelemetry-specification/blob/main/oteps/0232-maturity-of-otel.md#development)
  - [Hector] we can help
  - [Paulo] same
  - [Dan] not convinced about one big release breaking change vs more releases breaking
  - [Riccardo] I won’t stress on doing just one big breaking-change release
  - [Emidio] Wait a bit more for the next release for getting more logging changes together?
  - [Jeremy] Try to do not-breaking changes before the breaking ones
- Paulo: Are the API and SDK (also the contrib packages) FIPS-compliant?
  - [Slack discussion](https://cloud-native.slack.com/archives/C01PD4HUVBL/p1753213294089329)
  - gRPC is main crypto dependency. Maybe check [https://github.com/grpc/grpc/issues/37161](https://github.com/grpc/grpc/issues/37161)
  - [Riccardo] running our tests on a fips-enabled image would be useful
  - [Dan] Do they need just Python or the whole system (so the collector)? Looks like something that can be OTel Project wide, try to propose to community
- Keith’s PR: [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3646](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3646)
  - Name clash with traceloop:
    - [Aaron] Try to speak with Nir and GenAI SIG
- [aaron] [https://github.com/open-telemetry/opentelemetry-python/pull/4676](https://github.com/open-telemetry/opentelemetry-python/pull/4676) from Hector
  - [https://opentelemetry.io/docs/specs/otel/logs/sdk/#additional-logrecord-interfaces](https://opentelemetry.io/docs/specs/otel/logs/sdk/#additional-logrecord-interfaces)
    - [Hector] fine for me to update PR with this
      - Should really make it visible for end users in changelog
      - [emidio] I would use the wording *BREAKING:* in the changelog
