## Key Topics
- Harshit Kushwaha accepted the improver role; new approval practice requires two approvers, including one maintainer. Harshit was nominated for OpenTelemetry Community Contributor but did not win.
- Telemetry SDK name for Dart: agreed to use "OpenTelemetry" (not "Dartastic OpenTelemetry") for the telemetry.sdk.name attribute to avoid churn, since the package on pub.dev will eventually point to the official OTel Dart library.
- Ecosystem adoption: Google's Genkit 1.0 uses the Dartastic OpenTelemetry package (0.11.0), and Claude announced OpenTelemetry support. Gen AI semantics are a priority.
- AI-assisted code review: Robert shared his AI PR-review tooling (Claude and Codex running in parallel); the group discussed standardizing AI review skills and adding evals.
- Blockers on moving code into the official repo: credit attribution for contributors, Claude-authored code needing reclassification as assisted-by (requiring a Git reset and sandbox redo), and contributor license/copyright sign-off pending legal review via the governance liaison. Semantics work proceeds meanwhile, with Robert taking credit for generated semantics code.
- Semantic conventions: discussed stable vs. development entry points, federated semantics across repos, and the need for tests verifying values match upstream, since stable attributes cannot change value.

## Action Items
- Michael Bushe: Follow up with the CNCF landscape repo to add maintainers (Michael and Robert) via PR; review Robert's PR review tooling and contribute his agent files.
- Michael Bushe: Finish reviewing the Any value PR over the weekend; post five new SDK issues, including the telemetry SDK name issue.
- Michael Bushe: Coordinate with Severin (governance liaison) on contributor sign-off and the Claude-authored code reclassification.
- Robert Magnusson: Add Harshit to the GitHub team; start semantics PRs on Monday.
- Robert Magnusson: Share PR review skill link with the group.
- Harshit Kushwaha: Push Prometheus environment variables changes by tomorrow.
- Yusuf Rosman: Finish bootstrap PR and address review comments; add stable/development semantics entry points; consider a validation test and automated upstream sync PRs.
- La Pyae Oo: Provide an update on assigned work (unclear from transcript).

## Participants
Michael Bushe, Robert Magnusson, Yusuf Rosman, Harshit Kushwaha, La Pyae Oo
