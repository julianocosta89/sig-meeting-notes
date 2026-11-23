## Key Topics
- **Exponential histograms as SDK default:** Trask raised whether SDKs could switch to exponential histograms by default. Maintainers agreed this would be a breaking change requiring major SDK version bumps. Concerns include bucket counts and exemplar cost, and the group suggested tuning defaults before enabling them.
- **Security bar for authenticated DDoS and resource exhaustion:** Reiley proposed a threshold for which issues count as security vulnerabilities. Braydon and David raised concerns about the CVE workload, while Josh stressed tenant isolation and updating the threat model to cover authenticated traffic.
- **Span lifecycle events proposal:** Christophe proposed events for long-running spans (CI/CD, agent workflows) and a prototype in OTel semantic conventions. Discussion covered two span models, parent-child relationships, whether the SDK or instrumentation should emit events, and the risk of user confusion. The group agreed to prototype in CI/CD first and continue offline.
- **Helm charts heartbeat:** Tyler reported seven charts, active drive-by contributions, and a collector component renaming feature. He plans a testing framework for rendered config and noted overlap questions with the packaging SIG. Trask flagged that the related eBPF network repo is archived.
- **Entities ID PR:** Josh asked for reviews on a PR that he said is needed to reach alpha for entities. It has SIG approval, and a presentation may follow if review is thin.

## Action Items
- Christophe: Continue the span lifecycle events prototype in CI/CD, review the client-side session events and profiling approaches, and continue discussion offline or next week.
- Josh Suereth and Joshua MacDonald: Explore reducing exemplar and bucket defaults for exponential histograms, and create a tracking issue (Carlos suggested this).
- Reiley Yang: Gather maintainer feedback on the security vulnerability bar.
- Tyler Helmuth: Remove the archived eBPF network chart, and recruit contributors for the Helm testing framework.
- Reviewers: Review the entities ID PR this week. Josh or Dimitri may present next week if feedback is limited.
- David Ashpole: Gather reviews on the instrumentation stability OTEP.
- Michele Mancioppi: Collect last-minute feedback on the automatic injection criteria PR before its planned merge.
- Carlos Alberto Cortez: Add Josh or Dimitri to the next agenda if needed.

## Participants
Carlos Alberto Cortez, Michele Mancioppi, David Ashpole, Trask Stalnaker, Josh Suereth, Reiley Yang, Joshua MacDonald, Braydon Kains, Christophe Kamphaus, Liudmila Molkova, Jason Plumb, Tyler Helmuth, Aleksandar Hadzibabic
