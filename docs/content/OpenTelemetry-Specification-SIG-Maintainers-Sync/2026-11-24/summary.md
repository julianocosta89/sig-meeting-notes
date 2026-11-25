## Key Topics
- **Profiler identification:** The Profiling SIG proposed reusing `telemetry.distro.name` to identify the eBPF profiler producer. Participants agreed it fits a separate eBPF distro, but it doesn't fit in-process profilers embedded in existing distros (e.g., the Java agent). An instrumentation-scope or new attribute may be needed.
- **Entity data model (ID scope):** Josh Suereth presented a spec change that marks whether an entity's identity is globally unique or local to a parent. Liudmila Molkova raised wording and protocol-efficiency concerns, such as dropping the ternary scope type. Josh agreed the wording is confusing and needs more review.
- **Span requirements consolidation:** Liudmila proposed moving cardinality and other requirements for span name and span type into the semantic conventions repo, keeping the API doc as a general reference. Discussion covered whether the API can enforce these rules and how to avoid duplicated text. Stable-attribute changes are set to merge by end of week absent objections.
- **Maintainer security advisory access:** GitHub now gives maintainers access to security advisories, which Trask Stalnaker tested on the Java instrumentation repo. Limits remain around temporary private forks, and a broader process is being discussed in the SIG Security group.
- **Meeting cancellations:** Thursday and Friday meetings during the shutdown week are being canceled.

## Action Items
- Florian Lehner: Follow up with other profiling contributors on a profiler-identification attribute that covers in-process profilers.
- Josh Suereth: Revise the entity ID scope wording, evaluate Liudmila's protocol simplification, and seek broader review.
- Liudmila Molkova: Raise the dot-vs-underscore semantic conventions comment; merge the stable-attributes change by end of week if no objections.
- Trask Stalnaker: Post in the Maintainer channel about canceling Thursday and Friday meetings.
- All: Review and comment on the GitHub security advisory process discussion (Robert's PR).

## Participants
Reiley Yang, Alex Boten, Florian Lehner, Jason Plumb, Michele Mancioppi, Trask Stalnaker, Josh Suereth, Liudmila Molkova, Robert Pająk, David Ashpole, Carlos Alberto Cortez, Jack Berg
