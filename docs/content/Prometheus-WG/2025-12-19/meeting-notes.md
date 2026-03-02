## Meeting Notes

### Attendees
- arthursens
- owen williams
- adam bernot
- kyle
- [arthursens] Prometheus Receiver progress review.
  - some low-hanging fruit that can be picked up (see board)
  - some harder ones: e.g. test time dependency, service discovery inflating binary size
  - tl;dr lots to do, help needed, etc 🙂
- [kyle] [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/44467](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/44467)
  - CI Errors look unrelated
  - There is a flakiness when running it 1000x locally haven’t focused long enough to figure out why
  - `go test -race ./... -run 'TestExportWithWALEnabled' -count=5000` results in a few errors related to expected payloads not being received
