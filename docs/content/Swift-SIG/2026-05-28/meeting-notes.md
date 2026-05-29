## Meeting Notes

### Attendees
- Bryce Buchanan
- Nacho Bonafonte
- Vinod Vydier

### Agenda
- GRPC 2.0
  - todo: check the limitations [Bryce]
- cocoapods failed to publish
- random build failures due to simulator architecture + timing based unit tests
  - we need to update our test makefile to target correct simulator architecture (x86_64 or arm64, not sure which, probably native to runner, which is arm64)
  - inability to rerun failed jobs has resolved.
- do a opentelemetry-swift-core release [Bryce]
- reviewed PRs and Issues in both repos.
- [Concurrency issue](https://github.com/open-telemetry/opentelemetry-swift-core/issues/53)
- Issues with API types hiding extensions in SDK
