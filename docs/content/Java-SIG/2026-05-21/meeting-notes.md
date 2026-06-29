## Meeting Notes

### Attendees
- Jason (Splunk)
- Jay DeLuca (Grafana Labs)
- Jack Berg (Grafana Labs)
- Jonathan Halliday (IBM)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com) (Grafana Labs)
- Peter Findeisen (Cisco)
- Pranav Sharma (Google)
- Lauri Tulmin (Splunk)

### Agenda
- [Gregor] Pinned versions for muzzle for distros - what to do to fix it?
  - Currently broken
  - Fall back gracefully if file not present
- [jack] Removing all internal code from zipkin: [https://github.com/open-telemetry/opentelemetry-java/pull/8413](https://github.com/open-telemetry/opentelemetry-java/pull/8413)
  - Heads up to instrumentation. Moving instrumentation suppression: [https://github.com/open-telemetry/opentelemetry-java/pull/8413#discussion_r3274553524](https://github.com/open-telemetry/opentelemetry-java/pull/8413#discussion_r3274553524)
- [jason] wtaf? [https://github.com/open-telemetry/opentelemetry-java-contrib/pull/2837](https://github.com/open-telemetry/opentelemetry-java-contrib/pull/2837)
- [Gregor] Since we just do a bunch of security work in Grafana Labs - what’s the state of affairs of OTel
  - GitHub action linters
  - …
  - [Trask] Put secrets into explicit environments, which have protected access
  - [jack] sig-security recommendations: [https://github.com/open-telemetry/sig-security/blob/main/docs/recommendations.md](https://github.com/open-telemetry/sig-security/blob/main/docs/recommendations.md)
  - [jack] Related slack convo on zizmor [https://cloud-native.slack.com/archives/C01NJ7V1KRC/p1779297831806729?thread_ts=1779295209.483399&cid=C01NJ7V1KRC](https://cloud-native.slack.com/archives/C01NJ7V1KRC/p1779297831806729?thread_ts=1779295209.483399&cid=C01NJ7V1KRC)
  - [https://github.com/step-security/harden-runner](https://github.com/step-security/harden-runner)
  - [Trask] Create protected environment, move secrets to it
  - [Trask] applied to claude / openai OSS security programs
  - [jack] Key rotation on some schedule?
  - [jack] Delay updating dependencies?
    - But what happens if everyone waits?
    - Should github actions updates be less frequent since those represent supply chain attacks?
      - [trask] monthly github actions updates, but configure to update early if CVE
  - [Trask] Dependabot and GH have ways to publish your transitive deps and GH will use that for scanning
