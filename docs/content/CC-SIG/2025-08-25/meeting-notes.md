## Meeting Notes

### Attendees
- Marc Alff (Oracle)
- Doug Barker
- Tom Tan (Microsoft)
- Lalit Kumar Bhasin (Microsoft)

### Agenda
- Upstream
  - [Spec](https://github.com/open-telemetry/opentelemetry-specification)
    - Spec configuration matrix moving to yaml
      - https://github.com/open-telemetry/opentelemetry-specification/pull/4631
  - [Semantic conventions](https://github.com/open-telemetry/semantic-conventions)
    - Release 1.37.0 in preparation
      - https://github.com/open-telemetry/semantic-conventions/pull/2681
  - [Configuration](https://github.com/open-telemetry/opentelemetry-configuration)
    - Still on version 1.0.0-rc.1
    - No ETA for release 1.0.0
  - [Proto](https://github.com/open-telemetry/opentelemetry-proto)
  - [Weaver](https://github.com/open-telemetry/weaver)
    - Release 0.17.1
- Opentelemetry-cpp
  - Issues
  - PR
    - File configuration (#2518)
      - Getting very close
      - Need:
        - Bazel support for dependencies (c4core, rapidyaml)
        - Bazel support
        - CMake support
  - Misc
    - [Marc] CI
      - How to organize CI to latest packages, yet test C++14 / C++17 / etc (related to Doug work on CMake)
    - [Marc] Next release
      - Date, content ?
    - [Doug] Plan to move to C++17 and drop C++14? This will block upgrading to the latest third-party releases for googletest, benchmark, protobuf, grpc.
- Opentelemetry-cpp-contrib
  - Misc
- Opentelemetry-cpp-buildtools
  - Misc
