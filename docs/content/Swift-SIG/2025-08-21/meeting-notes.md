## Meeting Notes

### Attendees
- Nacho Bonafonte
- Bryce Buchanan
- Vinod Vydier
- Bee Klimt
- Alex Cohen
- Alolita Sharma
- Ariel Demarco

### Agenda
- DataCompression issue: [follow up PR](https://github.com/mw99/DataCompression/pull/38) - Ari
  - Let’s ping this issue again, 2 weeks since last action.
  - He didn’t do the new pod push: https://github.com/CocoaPods/Specs/blob/master/Specs/3/b/e/DataCompression/3.8.0/DataCompression.podspec.json
- Repository Division Follow Up
  - Repo created, but permission issues are hampering progress
- Added tests to uploadTask instrumentation: [https://github.com/open-telemetry/opentelemetry-swift/pull/889](https://github.com/open-telemetry/opentelemetry-swift/pull/889)
- [Issue](https://github.com/open-telemetry/opentelemetry-swift/issues/886) with MeterBuilder in 2.0
  - let’s add some documentation here
- Opamp implementation PR [https://github.com/elastic/apm-agent-ios/pull/290](https://github.com/elastic/apm-agent-ios/pull/290)
  - please take a look
- ‘Contrib’ repo decision:
  - we will rename `opentelemetry-swift-contrib` to `opentelemetry-swift-grpc` to solve the main problem with dependencies: the large size of the GRPC dependency change.
  - we’ll explore additional repos in the future
- Draft an issue with Apple for improvements with SPM/Swift
  - Alolita & Ari to tackle this & we’ll review next week.
- Alex to explore using env-var to enable/disable dependencies
