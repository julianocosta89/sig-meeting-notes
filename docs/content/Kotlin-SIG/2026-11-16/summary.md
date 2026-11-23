## Key Topics
- **CI caching:** Jamie's PR re-enables CI caching as read-only and removes it from release builds, addressing the earlier cache-poisoning concern. Merges to main still use caching, and releases run the full build. Jason is reviewing it.
- **Context and Propagator API:** Jamie says the changes are mostly done and better match the spec. He is preparing examples and docs for review.
- **gRPC exporter:** Ilia is starting gRPC support for exporting. He will research available gRPC libraries across KMP target platforms and report findings in the issue, then tackle platforms sequentially. He is waiting on membership requests.
- **ContribVEST:** No one picked up the Android or Kotlin issues at KubeCon. Jason will submit PRs for three simple issues, reopen closed PRs, and remove the ContribVEST labels from the rest.
- **KubeCon and upcoming events:** OTel graduated this year. Topics included eBPF instrumentation (Obi) and Arrow as a columnar alternative to OTLP. Discussion covered OTel Unplugged in Brussels (early 2027), KubeCon EU in Barcelona (CFP closed; Maintainer Summit RFC still open), and the Observability Day CFP (closed October 18).

## Action Items
- Jason: Review Jamie's CI caching PR.
- Jason: Submit PRs for the three simple Kotlin issues he created.
- Jason: Reopen the two closed PRs and remove ContribVEST labels from the remaining issues.
- Jamie: Finish context and Propagator API examples and docs, and ping Carlos this week.
- Jamie: Chase membership requests for Ilia and message Jason about the other contributor's request.
- Ilia: Research gRPC libraries for KMP targets and post findings in the issue.
- Ilia: Send the membership request link directly to Jason.

## Participants
Jamie Lynch, Jason Plumb, Hanson Ho, Ilia Liferov, Juan Vega, Carlos Alberto Cortez
