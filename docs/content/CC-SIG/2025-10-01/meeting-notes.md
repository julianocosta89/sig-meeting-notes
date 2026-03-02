## Meeting Notes

### Attendees
- Marc Alff (Oracle)
- Nikhil Bhatia
- Doug Barker
- Pawel (Elastic)

### Agenda
- PHP donation
  - Elastic distribution of OpenTelemetry for PHP
    - https://github.com/open-telemetry/community/issues/2846
    - [https://docs.google.com/document/d/1LCe1g1yzhwu3qcWZOO9979HuJTe9RGHp3q42uqHYJqM/edit?tab=t.0](https://docs.google.com/document/d/1LCe1g1yzhwu3qcWZOO9979HuJTe9RGHp3q42uqHYJqM/edit?tab=t.0)
  - Next steps ?
    - Define how to process the donation
    - Define opentelemetry-cpp future involvement
      - For the repositories (cpp, cpp-contrib, cpp-build-tools)
      - For the maintainers (become maintainers/contributors in other repositories, like opamp-cpp ?)
    - [Marc] Marc to add notes on the public donation proposal (issue # to link)
- Upstream
  - [Spec](https://github.com/open-telemetry/opentelemetry-specification)
  - [Semantic conventions](https://github.com/open-telemetry/semantic-conventions)
  - [Configuration](https://github.com/open-telemetry/opentelemetry-configuration)
  - [Proto](https://github.com/open-telemetry/opentelemetry-proto)
  - [Weaver](https://github.com/open-telemetry/weaver)
- Opentelemetry-cpp
  - Issues
  - PR
  - Misc
    - [Marc] DLL build on windows
      - Needs better CI coverage, we should find issues ourselves and not wait for bug reports
      - Needs to support ABI v1 and ABI v2
      - Clarify how to export : OPENTELEMETRY_EXPORT or file input.src (.def) ?
      - Singletons are still broken on windows.
    - [Marc] Plugable HTTP Authentication
    - [Doug] CI workflow cleanup proposal
    - [Doug] Third party release versions update proposal
- Opentelemetry-cpp-contrib
  - Misc
    - [Marc] Status of cpp-contrib (broken)
- Opentelemetry-cpp-buildtools
  - Misc
