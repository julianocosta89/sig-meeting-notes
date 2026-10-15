## Meeting Notes

### Attendees
- Marc Alff (Oracle)
- Doug Barker
- xxx

### Agenda
- Upstream
  - [Spec](https://github.com/open-telemetry/opentelemetry-specification)
  - [Semantic conventions](https://github.com/open-telemetry/semantic-conventions)
  - [Configuration](https://github.com/open-telemetry/opentelemetry-configuration)
    - upgrade to 1.2.0 is available
  - [Proto](https://github.com/open-telemetry/opentelemetry-proto)
  - [Weaver](https://github.com/open-telemetry/weaver)
  - [Bazel-central-registry](https://github.com/bazelbuild/bazel-central-registry)
- Opentelemetry-cpp
  - Issues
  - PR
    - [Marc] PRs with “Please review” tag
    - [Doug] Need to upgrade 22.04 -> 24.04 and 24.04 -> 26.04 in CI
  - Misc
    - [Marc] Discussion on noexcept
      - Need to log all known exception types caught in the SDK
      - Need an exception safe logging mechanism
      - Look at which SDK methods currently marked noexcept should remove that attribute - Marc will prototype a PR to remove noexcept in the SDK
    - [Marc] Mateen as approver
- Opentelemetry-cpp-contrib
  - Misc
    - [Marc] Progress on CI cleanup / renovate
- Opentelemetry-cpp-buildtools
  - Misc
