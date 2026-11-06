## Meeting Notes

### Attendees
- Vishwan (Grafana)
- Marius Ciocanel
- Ben (Grafana(
- Nacho Bonafonte
- Vladimir Kukushkin (Apple)
- Billy (ex-aws)

### Agenda
- Ben - Does collecting [device.id](http://device.id)(IDFV) require Privacy disclosure?
  - a PR was created to add this value to [app.installation.id](http://app.install.id) also
- Make optional integrations opt/in with package traits  [https://github.com/open-telemetry/opentelemetry-swift/issues/1258](https://github.com/open-telemetry/opentelemetry-swift/issues/1258)
  - Generally ok with the proposal
- Update README with swift 6 mention and new instrumentations
  - merged
- Try to regenerate automatic semantic conventions creation
  - Draft PR in the works
- High level review of MincoreLaunchInstrumentation and W3C-like schema (draft state), and new direct way to detect warm launch via syscalls - [https://github.com/open-telemetry/opentelemetry-swift/pull/1275](https://github.com/open-telemetry/opentelemetry-swift/pull/1275) (Billy)
- RRWeb (Billy)
- [https://github.com/open-telemetry/opentelemetry-swift/issues/1271](https://github.com/open-telemetry/opentelemetry-swift/issues/1271) - iOS specific docs
