## Key Topics
- **Host metrics V1 readiness:** The remaining work is host metrics. Donal is opening a PR to move system metrics to release candidate in Semantic Conventions. The group agreed the work needs more scoping to land by KubeCon Europe.
- **Config and naming:** The group agreed to keep the deprecated host metrics alias (`hostmetrics` alongside `host_metrics`) for 1.0. They also discussed renaming the overly generic `filter` package in core (possibly to `string_match`) and whether to close the open issue.
- **Log muting options:** Filtering error logs by string is brittle, since error strings can change. Braydon raised restructuring the "mute all process errors" config, but no solution was reached before 1.0.
- **PR limits for contributors:** Braydon is at the PR limit and wants to revive filter package PRs for metrics builder config before 1.0. Pablo suggested a process for requesting exceptions, similar to OTel membership vouching.
- **Resource detection:** Igor opened a PR for post-AD default detection. Braydon will review it because it's needed for an upcoming launch. Startup times are acceptable, though the EC2 detector causes a 4–5 second delay on Kubernetes.

## Action Items
- Donal: Open a PR to promote system metrics to release candidate in Semantic Conventions (target: today or tomorrow).
- Donal: Rename the filter package, ping the issue author on GitHub/Slack, and close the issue if there's no reply.
- Braydon: Write the document stating the original host metrics schema will be frozen and new features added only via Semantic Conventions.
- Braydon: Review Igor's post-AD default detection PR (today).
- Braydon: Revive the filter package PRs for metrics builder config before 1.0.
- Christos: Scope the remaining host metrics V1 work so it can be completed by KubeCon Europe.

## Participants
Pablo Baeyens, Donal O'Sullivan, Christos Markou, Braydon Kains, Igor Peschinskii
