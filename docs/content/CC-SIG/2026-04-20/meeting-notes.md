## Meeting Notes

### Attendees
- Marc Alff (Oracle)
- Doug Barker – Can not attend, time conflict
- TomTan

### Agenda
- Upstream
  - [Spec](https://github.com/open-telemetry/opentelemetry-specification)
  - [Semantic conventions](https://github.com/open-telemetry/semantic-conventions)
  - [Configuration](https://github.com/open-telemetry/opentelemetry-configuration)
  - [Proto](https://github.com/open-telemetry/opentelemetry-proto)
  - [Weaver](https://github.com/open-telemetry/weaver)
- Opentelemetry-cpp
  - Issues
    - [Marc] - Need to fix issue #3958
  - PR
  - Misc
    - [Marc] - Plan for the next release ?
    - [Marc] - clang-tidy cleanup, 33 warnings left
    - [Marc] - Discuss, removal of “opentelemetry/plugin”
  - From last week:
    - opentelemetry-proto: Ready to upgrade to v1.10.0?
      - [Marc] - Blocked on bazel central repository, support for 1.10.0 missing
    - Test coverage: Should we expand test coverage reporting for all components/preview flags?
    - Benchmarks: Should we request a bare metal runner for benchmarking?
      - See: [https://github.com/open-telemetry/community/issues/2616](https://github.com/open-telemetry/community/issues/2616)
