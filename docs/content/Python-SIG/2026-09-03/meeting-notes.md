## Meeting Notes

### Attendees
- Diego Hurtado (Dash0)
- Tammy Baylis (SolarWinds)
- Lukas Hering (Oracle)
- Riccardo Magliocchetti (Elastic)
- Leighton Chen (Microsoft)
- Aaron Abbott (Google)
- Pablo Collins (Cisco)

### Agenda
- [carlos] Python self observability update in the compliance matrix: [https://github.com/open-telemetry/opentelemetry-specification/pull/5295](https://github.com/open-telemetry/opentelemetry-specification/pull/5295) - please review/confirm.
  - Riccardo: will review
  - Also need to review [https://github.com/open-telemetry/opentelemetry-specification/pull/5190](https://github.com/open-telemetry/opentelemetry-specification/pull/5190)
- [Leighton] Ownership of instrumentations: missing native cannot be a reason for rejection
  - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4154](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4154)
  - Process to also get rid of them
  - Diego: lockstep release is a limitation, better be strict
  - Riccardo:
    - not all instrumentations are created equals
    - Need to fix component owners model
  - Aaron: feedback: if -contrib model was better we woulnd’t end up with so many genai instrumentations
    - Maybe a sponsorship model, be a codeowner for some other package
  - Liudmila:
    - We can learn from java experience
    - Have a plan on how to handle this
  - Diego: don’t count on people without group privileges (approvers, maintainers)  to maintain stuff
  - Lukas: we can take into account PyPi popularity but we should not stop to accept new instrumentations in -contrib altogether
  - Trask:
    - java has instrumentation repo that is maintainer owned (no component owners), more picky
      - For stuff we don’t understand we trust tests
      - Lot of test infrastructure
      - Leverage ai to compare instrumentations of similar kind
      - Sdk components harder to get in
      - We have a java agent knowledge base to get PRs in decent shape before having to review them
      - 100+ instrumentations
      - Support very old versions of libraries, rarely / never drop autoinstrumentation support
      - “As long as it look like the other similar instrumentation” should be fine
      - Pushback on instrumentations for personal projects
      - Test minimum and latest version, nightly job to check latest version (ai nice to fix issues)
        - We may test intermediate versions
        - Tool that checks api shape (muzzle)
      - stable Telemetry guarantee, breaking on major only
    - Contrib has component owner model
      - <50 instrumentations
  - Java [https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/safety-mechanisms.md](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/safety-mechanisms.md)
  - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/VERSIONING.md#dropping-support-for-older-library-versions](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/VERSIONING.md#dropping-support-for-older-library-versions)
