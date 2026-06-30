## Meeting Notes

### Attendees
- Hector Hernandez (Microsoft)
- Diego Hurtado
- Dylan Russell (google)
- Tammy Baylis (SolarWinds)
- Radhika Gupta (microsoft)
- Jackson Weber (Microsoft)
- Aaron Abbott (Google)
- Josh Winerman (Cisco/Splunk)
- Carlos Cortez
- Emídio
- Keith Decker (Cisco/Splunk)
- Erdenesaikhan Tserendavga (Cisco/Splunk)
- Shuwen Pan (Cisco)
- Leighton Chen (Microsoft)
- Pablo Collins (Cisco)
- Lukas Hering (Oracle)
- Liudmila Molkova (Google)
- Marcelo Trylesinski (Pydantic)

### Agenda
- [Hector] Log Stabilization status
  - Riccardo was tracking here [https://github.com/open-telemetry/opentelemetry-python/issues/4750](https://github.com/open-telemetry/opentelemetry-python/issues/4750)
  - There’s also GC review [https://github.com/open-telemetry/community/issues/1751](https://github.com/open-telemetry/community/issues/1751)
    - Liudmila to take another pass at the review
  - [aaron] there’s some outstanding tech debt we wanted to clean up
    - [Deprecate events API/SDK · Issue #4655 · open-telemetry/opentelemetry-python](https://github.com/open-telemetry/opentelemetry-python/issues/4655)
    - Let’s remove deprecated stuff
- [aaron] service instance id, forking
  - [https://github.com/open-telemetry/opentelemetry-python/pull/5259](https://github.com/open-telemetry/opentelemetry-python/pull/5259)
  - [https://github.com/open-telemetry/opentelemetry-python/pull/5280](https://github.com/open-telemetry/opentelemetry-python/pull/5280)
- [Leighton] HTTP/DB instrumentation stabilize
  - [https://github.com/open-telemetry/opentelemetry-python-contrib/issues/2453#issuecomment-4634703394](https://github.com/open-telemetry/opentelemetry-python-contrib/issues/2453#issuecomment-4634703394)
- [Liudmila] Looking for volunteers interested in prototyping exception events for HTTP and DB instead of span events  [https://github.com/open-telemetry/semantic-conventions/issues/3554](https://github.com/open-telemetry/semantic-conventions/issues/3554)
- [Marcelo] httpx2 last week stuff
  - Update instrumentor to support httpx2 [https://github.com/open-telemetry/opentelemetry-python-contrib/issues/4635](https://github.com/open-telemetry/opentelemetry-python-contrib/issues/4635)
  - [Marcelo] it’s hard for us to consume the instrumentation in the httpx2 repo
- [Marcelo] MCP instrumentation
  - Native instr in the python SDK. just one or two spans
  - I probably won’t do more myself, but if you want to please come contribute upstream
    - [Lukas] I have some additional capacity and am willing to contribute here
  - End of July release date
  - Interop with fastmcp, fyi [https://github.com/PrefectHQ/fastmcp/issues/3451](https://github.com/PrefectHQ/fastmcp/issues/3451)
  - Stabilizing semconv for MCP?
    - Let’s do it! (sarcasm?) Just need time to do it and might be lower priority than the inference. Someone needs to drive
    - MCP new stateless transport should work without _meta hacks. I think it’s a
