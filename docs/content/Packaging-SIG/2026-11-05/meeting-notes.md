## Meeting Notes

### Attendees
- Denys Sedchenko (Grafana Labs)
- Antoine Toulme (Splunk)

### Agenda
- [Denys] OpenBuildService project for DEB (and eventually for RPM).
  - OBS project is created [here](https://build.opensuse.org/project/show/home:opentelemetry).
  - I’m working on a stacked PR for the build process, CI/CD and etc.
  - Kubernetes was a main source of inspiration for the repo structure and build process.
  - Questions:
    - ~~Our integration test jobs are failing as Apache’s host is down or having TLS handshake issues.~~ Host is up again, but maybe we should consider cashing Tomcat?
    - I would really like to reuse Jack’s approach to bump and rebuild packages on Renovate PR.
    - We store a version of each component in `release.txt`. What’s the source of truth for the `opentelemetry` meta package?
