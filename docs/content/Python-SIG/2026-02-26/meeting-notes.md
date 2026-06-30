## Meeting Notes

### Attendees
- Riccardo Magliocchetti (Elastic)
- Tammy Baylis (SolarWinds)
- Keith Decker (Cisco/Splunk)
- Erdenesaikhan Tserendavga (Cisco/Splunk)
- Aaron Abbott (Google)
- Dylan Russell (Google)
- Shuwen Pan (Cisco)
- Liudmila Molkova (Grafana Labs)
- Ridhima Satam (Cisco/Splunk)
- Lukas Hering (Capital One)
- Leighton Chen (Microsoft)

### Agenda
- [Riccardo] declarative-config: sdk or separate package? [https://github.com/open-telemetry/opentelemetry-python/pull/4879](https://github.com/open-telemetry/opentelemetry-python/pull/4879)
  - It’s fine to have it in the sdk
  - Aaron: will instrumentation need to read that?
- [Mike] Are we ready to accept the stale GHA in core and contrib?
  - Let’s merge them
- [Riccardo] LoggingHandler move out of sdk PRs
  - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4210](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4210)
  - [https://github.com/open-telemetry/opentelemetry-python/pull/4919](https://github.com/open-telemetry/opentelemetry-python/pull/4919)
  - Genai people PTAL [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4263](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4263)
- [Riccardo] virtualenv 21 broke hatch that broke tox -e generate [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4265](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4265)
  - Forced virtualenv < 21 until hatch releases a new version
    - Looks like it has been fixed in hatch
- [Riccardo] Next release after LoggingHandler move?
  - Plenty of stuff merged already and it’s like 2.5 months without a release
    - We can do Nextnext in march too
  - Same question about [https://github.com/open-telemetry/opentelemetry-python/pull/4854](https://github.com/open-telemetry/opentelemetry-python/pull/4854)
- [Erden] Add Agent type into GenAI utils
  - Create_agent type [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4217](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4217)
  - Follow up PR for invoke_agent type
- [Keith] - Expand ToolCall type to match Semconvs:
  - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4218/](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4218/)
- [Tammy] PTAL: new and improved psycopg2 AttributeError fix PR [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4257](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4257)
- [Lukas] aiobotocore instrumentation: [http://github.com/open-telemetry/opentelemetry-python-contrib/pull/4049](http://github.com/open-telemetry/opentelemetry-python-contrib/pull/4049)
  - Lukas willing to be codeowner for botocore
  - Riccardo: Will try to do a review
- [Lukas] OTLP Json protoc plugin: [https://github.com/open-telemetry/opentelemetry-python/pull/4910](https://github.com/open-telemetry/opentelemetry-python/pull/4910)
  - Lukas: can cleanup commits to make easier to review
- [Lukas] Contrib header casing bugs: [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4216](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4216)
  - Lukas: also kafka instrumentation may have also casing issues
- [Liudmila] Can I get some green check-mark reviews on OpenAI update? [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3715](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3715) Got several approvals from GenAI crew
- [Shuning] Embedding type PR ready for review [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4219](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4219)
- [Surya] Can I get some reviews on this?
