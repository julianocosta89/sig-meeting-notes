## Meeting Notes

### Attendees
- Rafael Roquetto (Grafana)
- Stephen Lang (Grafana)
- Mike Dame (Odigos)
- Robert Pająk (Splunk)
- Nimrod Avni (Coralogix)
- Giuseppe Ognibene (Coralogix)
- Mihir Shah (Culver Max Entertainment Pvt Ltd)
- Tyler Yahn (Splunk)
- Nikola Grcevski(Grafana)
- Ittai Corem (Coralogix)

### Agenda
- [Rafael] [Enhance OTEL_EBPF_BPF_DEBUG to allow printing to trace_pipe only](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/1295)
- [Tyler] [Include build-critical bpf2go generated artifacts in OBI tracked source](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/1322#top)
  - [Mike] [https://github.com/odigos-io/odigos/blob/3ccdbb72460ed532fc16709b244919558821c18f/odiglet/Makefile#L12-L18](https://github.com/odigos-io/odigos/blob/3ccdbb72460ed532fc16709b244919558821c18f/odiglet/Makefile#L12-L18)
  - TODO: Tyler ask the collector-contrib maintainer if they are willing to modify their build process to support OBI
- [Tyler] [Update OBI documentation for the v0.5.0 release](https://github.com/open-telemetry/opentelemetry.io/pull/9151#top)
- [Stephen] CI pains - ask in otel-maintainers channel - [done](https://cloud-native.slack.com/archives/C01NJ7V1KRC/p1771436685739439)
- [Robert] Question: What is k8s-cache? I do not see it documented in [opentelemetry.io](http://opentelemetry.io) and I saw it added to the releases. I thought it was something used only for testing.
  - [Stephen] Answer: When obi runs as a daemonset, each obi instance opens a connection to the k8s API server. If a large k8s cluster has enough nodes, it **will** bring down the API server (even in GKE or other managed control planes). When this happens, the entire cluster becomes unusable. K8s-cache centralises the API server connections to only a few replicas of a deployment (say 1 replica per 50 nodes), so it complements the daemonset deployment. The obi daemonsets then balance all of their connections to the k8s-cache replicas via a k8s-cache service, instead of directly hitting k8s API.
- [Tyler] [Open PRs Review](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pulls)
