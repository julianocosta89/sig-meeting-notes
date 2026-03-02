## Meeting Notes

### Attendees
  - Dylan russell (google)
  - Hector Hernandez (Microsoft)
  - Tammy Baylis (SolarWinds)
  - Riccardo Magliocchetti (Elastic)
  - Alex Boten (Honeycomb)
  - Leighton Chen (Microsoft)
  - Shuwen Pan (Cisco)
  - Keith Decker (Cisco/Splunk)

### Agenda
  - [Riccardo] 1.39.1 is out with a couple of backports:
  - https://github.com/open-telemetry/opentelemetry-python/pull/4850
  - https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4020
  - One issue during release process:
  - https://github.com/open-telemetry/opentelemetry-python/issues/4853
  - [Riccardo] We have -contrib PRs to review if you have time, thanks in advance!
  - [Riccardo] PSA: pipenv made pre-releases not installed by default https://github.com/pypa/pipenv/issues/6485 and users got confused https://github.com/open-telemetry/opentelemetry-python/issues/4849
  - Then they changed to install pre-releases if there are no releases https://github.com/pypa/pipenv/pull/6486
  - Time to drop the bX from release versions? Maybe version < 1 and Trove classifiers are enough for signaling beta status
  - Leighton: lgtm
  - [Dylan] Ways to suppress auto-instrumentation from instrumenting a particular package ? Context: https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4009
  - Leighton: haven’t looked at your code but suppress_instrumentation looks like what you want
  - [alex] Declarative configuration implementation
  - https://github.com/open-telemetry/opentelemetry-python/issues/3631
  - https://github.com/open-telemetry/opentelemetry-configuration/pull/456
