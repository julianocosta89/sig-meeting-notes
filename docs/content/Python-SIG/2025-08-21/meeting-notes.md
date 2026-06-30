## Meeting Notes

### Attendees
- John Scancella
- Shuwen Pan(Cisco)
- Dylan russell (google)
- Leighton Chen (Microsoft)
- Riccardo Magliocchetti (Elastic)
- Tammy Baylis (SolarWinds)
- Pablo Collins (Cisco/Splunk)
- Keith Decker (Cisco/Splunk)

### Agenda
- [Riccardo] Auto-instrumentation hack for gevent apps (e.g. locust) also opentelemetry-operator friendly [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3699](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3699)
- [Riccardo] Revise CODEOWNERS / components_owner [https://github.com/open-telemetry/admin/pull/185](https://github.com/open-telemetry/admin/pull/185)
  - Some component owners are not members of opentelemetry
  - Leighton: Need to update CODEOWNERS but component_owners can be a separate change
- [John Scancella] anything additional needed for MR: [https://github.com/open-telemetry/opentelemetry-python/pull/4728](https://github.com/open-telemetry/opentelemetry-python/pull/4728) ?
  - Tammy: try locally tox -e docs
- [Sergey Sergeev] sampling telemetry and delaying it for evaluations
  - Riccardo: discuss on slack or next week since Sergey was not there
    - Sergey: sorry, got dragged into another meeting :( will post a question in slack
- [dylan] Can this be merged: [https://github.com/open-telemetry/opentelemetry-python/pull/4695](https://github.com/open-telemetry/opentelemetry-python/pull/4695)  or any concerns ?
  - Riccardo: I’ll take another look
