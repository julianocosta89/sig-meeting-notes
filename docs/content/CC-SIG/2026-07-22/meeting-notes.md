## Meeting Notes

### Attendees
- Doug Barker
- Tom Tan (absent)

### Agenda
- Upstream
  - [Spec](https://github.com/open-telemetry/opentelemetry-specification)
  - [Semantic conventions](https://github.com/open-telemetry/semantic-conventions)
  - [Configuration](https://github.com/open-telemetry/opentelemetry-configuration)
  - [Proto](https://github.com/open-telemetry/opentelemetry-proto)
  - [Weaver](https://github.com/open-telemetry/weaver)
  - [Bazel-central-registry](https://github.com/bazelbuild/bazel-central-registry)
- Opentelemetry-cpp
  - Issues
    - CI: New regression in the gRPC functional test (observed a handful of failures on multiple branches)
      - This seemed to appear closely with the gRPC upgrade to 1.82.1
      - [https://github.com/open-telemetry/opentelemetry-cpp/issues/4273](https://github.com/open-telemetry/opentelemetry-cpp/issues/4273)
  - PR
    - Spinlock implementation and usage: [https://github.com/open-telemetry/opentelemetry-cpp/pull/4245](https://github.com/open-telemetry/opentelemetry-cpp/pull/4245)
      - change or remove the 1ms sleep in the spinlock?
      - Many sites appear better suited for std::mutex (io, long running methods, methods that allocate).
        - [https://github.com/search?q=repo%3Aopen-telemetry%2Fopentelemetry-cpp%20SpinLockMutex&type=code](https://github.com/search?q=repo%3Aopen-telemetry%2Fopentelemetry-cpp%20SpinLockMutex&type=code)
      - Next steps to review Spinlock implementation and usage.
    - CMake option rename
      - [https://github.com/open-telemetry/opentelemetry-cpp/pull/4268](https://github.com/open-telemetry/opentelemetry-cpp/pull/4268)
  - Misc
- Opentelemetry-cpp-contrib
  - Misc
- Opentelemetry-cpp-buildtools
  - Misc
