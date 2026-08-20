## Meeting Notes

### Attendees
- Marc Alff (Oracle) – online now
- Doug Barker
- xxx

### Agenda
- Upstream
  - [Spec](https://github.com/open-telemetry/opentelemetry-specification)
  - [Semantic conventions](https://github.com/open-telemetry/semantic-conventions)
    - Release 1.44 last week, need to upgrade.
  - [Configuration](https://github.com/open-telemetry/opentelemetry-configuration)
  - [Proto](https://github.com/open-telemetry/opentelemetry-proto)
    - Release 1.11 3 weeks ago, need to upgrade.
    - Need bazel central repository to upgrade from 1.8
  - [Weaver](https://github.com/open-telemetry/weaver)
    - Release 0.25.1 2 weeks ago, need to upgrade.
  - [Bazel-central-registry](https://github.com/bazelbuild/bazel-central-registry)
    - Contribution for opentelemetry-cpp 1.28
- Opentelemetry-cpp
  - Issues
    - CI: New regression in the gRPC functional test (observed a handful of failures on multiple branches)
      - This seemed to appear closely with the gRPC upgrade to 1.82.1
      - [https://github.com/open-telemetry/opentelemetry-cpp/issues/4273](https://github.com/open-telemetry/opentelemetry-cpp/issues/4273)
    - Spinlock replacement with std::mutex in the Metrics SDK
      - [https://github.com/open-telemetry/opentelemetry-cpp/issues/4317](https://github.com/open-telemetry/opentelemetry-cpp/issues/4317)
      - Next step:
        - complete the swap in storage and aggregation classes.
    - Exception handling in the SDK
      - [https://github.com/open-telemetry/opentelemetry-cpp/issues/4361](https://github.com/open-telemetry/opentelemetry-cpp/issues/4361)
      - Review Marc’s proposal to add `GetTracerImpl`
      - Review Doug’s proposal to remove noexcept from provider and instrumentation scoped object constructors.
      - Next step:
        - remove noexcept from Providers and Tracer/Meter/Logger
  - PR
    - Drop stale async attribute sets from cumulative exports
      - [https://github.com/open-telemetry/opentelemetry-cpp/pull/4140](https://github.com/open-telemetry/opentelemetry-cpp/pull/4140)
      - [https://github.com/open-telemetry/opentelemetry-cpp/issues/4108](https://github.com/open-telemetry/opentelemetry-cpp/issues/4108)
      - [https://github.com/open-telemetry/opentelemetry-cpp/pull/4268](https://github.com/open-telemetry/opentelemetry-cpp/pull/4268)
      - Anything blocking?
    - Publishing doxygen documentation
      - [https://github.com/open-telemetry/opentelemetry-cpp/pull/4308](https://github.com/open-telemetry/opentelemetry-cpp/pull/4308)
  - Misc
- Opentelemetry-cpp-contrib
  - Misc
- Opentelemetry-cpp-buildtools
  - Misc
