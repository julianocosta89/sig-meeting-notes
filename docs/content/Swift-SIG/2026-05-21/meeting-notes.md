## Meeting Notes

### Attendees
- Bryce Buchanan
- Nacho Bonafonte
- Vinod Vydier
- Billy Zhou

### Agenda
- [Ari] SPM Traits investigation
- 2.4.1 in pre-release
- Swift6 release
- GRPC 2.0
  - dependency concerns
- cocoapods failed to publish
- random build failures due to simulator architecture + timing based unit tests
  - we need to update our test makefile to target correct simulator architecture (x86_64 or arm64, not sure which, probably native to runner, which is arm64)
