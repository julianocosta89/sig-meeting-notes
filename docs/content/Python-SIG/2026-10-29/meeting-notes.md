## Meeting Notes

### Attendees
- Diego Hurtado (Dash0)
- Dylan russell (google)
- Lukas Hering (Oracle)
- Mekan Baymyradov (Ojak)
- Walace Maia ( W Trsut)
- Pablo Collins (Cisco)

### Agenda
- Diego: packaging dependency
- Diego: Lots of vulnerability and quality alerts
- Diego: new instrumentation policy [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5045](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5045)
- [Lukas] [opentelemetry-sdk: add support for advisory attributes on metric instruments](https://github.com/open-telemetry/opentelemetry-python/pull/5444)
- [Liudmila] Span type API + SDK, no exporters [https://github.com/open-telemetry/opentelemetry-python/pull/5819](https://github.com/open-telemetry/opentelemetry-python/pull/5819)
- [dylan] Add PyPi / Github attestation to build / release workflows ([recommended in sig security](https://github.com/open-telemetry/sig-security/blob/48015b753f766f4b3616e5d2d78f22d12c8afa72/docs/recommendations.md#attest-release-artifacts-with-github-artifact-attestations)). Requires opting in to [trusted publishing on PyPi](https://docs.pypi.org/trusted-publishers/adding-a-publisher/) . ([Github example of attestation](https://github.com/open-telemetry/weaver/attestations), [PyPi example](https://pypi.org/project/opentelemetry-instrumentation-google-genai/#security))
- [Leighton] Patch release: [[release/v1.45.x-0.66bx] Backport metric cardinality limits and traceparent parsing by lzchen · Pull Request #5856 · open-telemetry/opentelemetry-python](https://github.com/open-telemetry/opentelemetry-python/pull/5856)
- [mekanbaymyradov]: sqlalchemy don’t suppress pool connection metrics: [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5246](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5246)
