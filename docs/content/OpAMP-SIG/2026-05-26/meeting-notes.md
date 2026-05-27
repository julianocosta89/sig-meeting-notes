## Meeting Notes

### Attendees
- Dakota Paasman (Dynatrace)
- Andy Keller (Dynatrace)
- Tigran Najaryan
- Juande Manjon
- Stanley Liu (Datadog)
- Evan Bradley (Dynatrace)
- Bejal Lewis
- Israel Blancas (Coralogix)
- Kelsey Ma (Splunk)

### Agenda
- [Juande] [Restructure proto folders to align with versioned packages #338](https://github.com/open-telemetry/opamp-spec/issues/338)
  - It is a possible action item after *opamp.proto**.v1*** [Include version in package name #251](https://github.com/open-telemetry/opamp-spec/commit/a642d8b8e88e828ef6c70054d361c6e9dbd80fd0)
  - Allows [Add CI workflow for detecting breaking changes #213](https://github.com/open-telemetry/opamp-spec/issues/213)
- proto/ folder with package opamp.proto.v1
- proto/opamp/proto/v1/ → package opamp.proto.v1 (current, no change)
- proto/opamp/proto/v2/ → package opamp.proto.v2 (future, consistent package naming)
- [Jade] Let’s discuss [[extension/opamp] Reported identifying attributes not matching Collector internal telemetry #46649](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/46649)
- [Stanley] Next steps for OpAMP Message Attestation [https://github.com/open-telemetry/opamp-spec/pull/333](https://github.com/open-telemetry/opamp-spec/pull/333)
  - [Proposal doc](https://docs.google.com/document/d/10IwvaEMs-CqE6OmTcGJHMf7TwJJPqvAabCjMQ5OTcP4/edit?tab=t.8gtjif5uhm5o#heading=h.ixgh839gvcz2)
- [Andy] Max message size for OpAMP messages [https://github.com/open-telemetry/opentelemetry-dotnet-contrib/pull/4116](https://github.com/open-telemetry/opentelemetry-dotnet-contrib/pull/4116)
