## Meeting Notes

### Attendees
- [John Watson](mailto:jkwatson@gmail.com)(Sublime Security)
- Jay DeLuca (Grafana Labs)
- Trask Stalnaker (Microsoft)
- Pranav Sharma (Google)
- Jonathan Halliday (IBM)
- Prasad Sawool (Pixeltee)
- Cleverchuk (Solarwinds)
- Bruno Baptista (IBM)

### Agenda
- Standing topic: issue triage
  - [is:open -label:"needs u feedback","needs repro","contribution welcome"](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues?q=is%3Aissue+is%3Aopen+-label%3A%22needs+author+feedback%22%2C%22needs+repro%22%2C%22contribution+welcome%22)
  - [is:open label:"needs triage"](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues?q=is%3Aissue+is%3Aopen+label%3A%22needs+triage%22)
- Standing topic: [stackoverflow questions](https://stackoverflow.com/search?tab=newest&q=%5bopen-telemetry%5d%20java)
- [Jay] How should we think about new configuration options in [contrib](https://github.com/open-telemetry/opentelemetry-java-contrib/pull/2753/files#diff-8d6a594f6f8b18cf94ed9d7c81427d65a79796292b53f20e0c4260d758dbb9ecR25-R28)?
  - Do they need to follow any particular conventions?
  - [Jack] The way I think about it, the contrib components are independent things, just using the same infrastructure in the repo.
    - To what extent do we need to conform to conventions of the core or instrumentation repo?
    - There are components that have been converted because they are used in the agent
      - Resource detectors
      - Samplers
    - Core repo is very strict now. Ensure there’s equivalent in both standard system properties and declarative config.
      - [jack] Issue to document policy: [https://github.com/open-telemetry/opentelemetry-java/issues/8300](https://github.com/open-telemetry/opentelemetry-java/issues/8300)
  - Theres a bridge installed in the agent, could take the same approach in contrib
- [Jay] Thoughts on a [kitchen sink for instrumentation configs](https://github.com/jaydeluca/opentelemetry-java-instrumentation/blob/example-config-doc/docs%2Fdeclarative-configuration-example.yaml)? - (work in progress)
  - Related: Gregor is adding some [basic examples to opentelemetry.io](https://deploy-preview-9448--opentelemetry.netlify.app/docs/zero-code/java/agent/declarative-configuration/)
  - Should it also include the [SDK configs](https://github.com/open-telemetry/opentelemetry-configuration/blob/main/examples/otel-getting-started.yaml)? Or just link to it in the heading
- [jack] core PRs worth discussing (time permitting)
  - [https://github.com/open-telemetry/opentelemetry-java/pull/8255](https://github.com/open-telemetry/opentelemetry-java/pull/8255) yes or no?
  - [https://github.com/open-telemetry/opentelemetry-java/pull/8086](https://github.com/open-telemetry/opentelemetry-java/pull/8086) haven’t heard back about the original issue. Should we wait for more interest? Wait for okhttp v6?
  - [https://github.com/open-telemetry/opentelemetry-java/pull/8077](https://github.com/open-telemetry/opentelemetry-java/pull/8077) Tradeoff between single threaded and concurrent performance.
- [Pranav] API change PR: [https://github.com/open-telemetry/opentelemetry-java/pull/8296](https://github.com/open-telemetry/opentelemetry-java/pull/8296)
