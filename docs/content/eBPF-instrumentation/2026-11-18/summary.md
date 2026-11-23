## Key Topics
- **Target info metric:** OBI emits `target_info` by default with no way to disable it. The group agreed to add a default-on config toggle, with an issue to revisit removing it in V2.
- **Release 1.1 planning:** Several PRs need review, including disabling Go channels, moving the config, and V1 Route 53 compatibility. Some features can slip past 1.1. Mattia's Redis job-dispatch trace grouping should default to the new behavior with an opt-out toggle.
- **SIG tooling and contributor workflow:** Mattia will request a SIG-specific OTel bot for Renovate post-processing. Tyler described CLA exception branch prefixes and stacked PRs as ways to ease maintainer workflow.
- **2026 roadmap and 2027 goals:** Priorities include packaging OBI in the OTel distribution, dynamic instrumentation, live patching, and expanded W3C trace context propagation. Several 2026 goals (network semconv, .NET support, API/SDK integration) will likely move to 2027, and protocol support may be closed as good enough.
- **Rust vs. Go performance:** Roy raised a benchmark showing Rust collectors using far fewer resources. Tyler argued the gain comes mainly from the Arrow data model rather than the language, and that a Rust rewrite would be costly.

## Action Items
- Nimrod: open an issue for the `target_info` toggle and V2 removal discussion, and sync with Nicola.
- Nimrod: review the Go channels config PR tonight.
- Tyler: add the 1.1 PRs to the shared doc, merge after review, and build CI for API diffs.
- Mattia: switch the Redis trace grouping toggle to default-on with an opt-out, and open the SIG bot request in the community.
- Mattia: research feasibility of the kprobe fast-path trace programs before year end.
- Gregor: create an issue for live patching, and do PR reviews to qualify as an approver.
- Giuseppe: ask about network semantic conventions at the Monday SIG meeting.
- Tyler: close the protocol-support umbrella issue and add 2027 goal labels for contributors.
- All: capture 2027 ideas as issues or sub-issues.

## Participants
Gregor Zeitlinger, Mattia, Giuseppe Ognibene (Coralogix), Roy Reshef (Kubex), Tyler Yahn (Splunk), Nimrod Avni, Marc Tudurí
