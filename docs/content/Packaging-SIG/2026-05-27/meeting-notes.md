## Meeting Notes

### Attendees
- Ted Young (Grafana Labs)
- Michele Mancioppi (Dash0)
- Denys Sedchenko (Grafana Labs)
- Antoine Toulme (Splunk)
- Sina (Canonical)

### Agenda
- Denys: update the research for hosting
  - We had agreed to contact the Kubernetes people with their setup and Alex Boten from the collector SIG. The collector is using a tool called [cosign](https://github.com/sigstore/cosign), which allows you to submit packages and it will sign it for you. It needs an external certificate of authority, and [fulcio](https://docs.sigstore.dev/certificate_authority/overview/) is the recommended option.
  - Regarding Kubernetes they have two proposals for the release process, not checked in detail yet. Asked feedback in the sig-release, no feedback yet.
  - No success yet into signing into OBS
- Michele: update on the metapackage PR
