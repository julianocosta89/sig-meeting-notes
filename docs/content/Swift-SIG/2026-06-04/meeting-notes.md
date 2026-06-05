## Meeting Notes

### Attendees
- Bryce Buchanan
- Nacho Bonafonte
- Vinod Vydier

### Agenda
- GRPC 2.0
  - still todo: check the limitations [Bryce]
- cocoapods failed to publish
  - Created PR
- random build failures due to simulator architecture + timing based unit tests
  - we need to update our test makefile to target correct simulator architecture (x86_64 or arm64, not sure which, probably native to runner, which is arm64)
  - inability to rerun failed jobs has resolved.
  - This has been fixed
- do a opentelemetry-swift-core release [Bryce]
  - merged
- [Concurrency issue](https://github.com/open-telemetry/opentelemetry-swift-core/issues/53)
  - Will is working on this
- Issues with API types hiding extensions in SDK
  - no movement on this.
- Bryce out next week (otel-swift cocktail party)
- we need to investigate why we cannot re-run build jobs in open-telemetry-core.
  - It was because the original build was > 1 month old.
- reviewed PRs and Issues in both repos.
