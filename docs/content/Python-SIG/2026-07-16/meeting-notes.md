## Meeting Notes

### Attendees
- Diego Hurtado (Dash0)
- Lukas Hering (Oracle)
- Shuwen Pan (Cisco)
- Dylan russell (google)
- Riccardo Magliocchetti (Elastic)
- Erdenesaikhan Tserendavga (Cisco/Splunk)
- Pablo Collins (Cisco)
- Keith Decker (Cisco/Splunk)
- Josh Winerman (Cisco/Splunk)
- Tammy Baylis (SolarWinds)
- Hector Hernandez (Microsoft)

### Agenda
- Riccardo: PSA Declarative config package not published for latest release
  - UPDATE: published
- Diego [**https://github.com/open-telemetry/opentelemetry-python/issues/5385**](https://github.com/open-telemetry/opentelemetry-python/issues/5385)
  - Diego: 3X rate of PR opened in 2026
  - Lukas: +1 from me
- **Diego [https://github.com/open-telemetry/opentelemetry-python/pull/5374](https://github.com/open-telemetry/opentelemetry-python/pull/5374)**
- Carlos: Close old env propagator PR? [https://github.com/open-telemetry/opentelemetry-python/pull/2110](https://github.com/open-telemetry/opentelemetry-python/pull/2110)
- Diego noprotobuf [https://github.com/ocelotl/opentelemetry-python/tree/pyproto](https://github.com/ocelotl/opentelemetry-python/tree/pyproto)
  - Diego: also remove requests, grpcio is next
  - Lukas: I have PR that abstracts the http library
  - Lukas: Probably a rust exporter that avoids protobuf and grpcio
  - Lukas: vendoring an alternative
    - Riccardo: I’m against vendoring, worried of security issues
- Lukas: discuss ways to better expose developmental features in SDK (context [https://github.com/open-telemetry/opentelemetry-specification/pull/5190](https://github.com/open-telemetry/opentelemetry-specification/pull/5190) )
  - Visibility issue for users
  - Riccardo: maybe a different mark for compliance matrix is enough?
  - Carlos: it’s vital that stuff that is experimental is marked as such
- Carlos: AlwaysRecord sampler: [https://github.com/open-telemetry/opentelemetry-python/pull/5354](https://github.com/open-telemetry/opentelemetry-python/pull/5354)
  - Trivial but needs some more reviews - namely, that envVars/declarative config doesn’t support this yet (accidental missing, I can drive the addition of this separately)
  - Lukas: can’t we add an entrypoint?
    - Riccardo: It requires another sampler as argument
