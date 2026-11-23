## Key Topics
- **AI tooling for the repo:** Pavol uses CodeRabbit internally and wants an automatic first-pass PR review. Mikołaj prefers narrowly scoped AI checks and suggests AI initial triage on issues, with clear messaging that maintainers still respond.
- **Dependency auto-merge:** The group discussed auto-merging Renovate PRs that pass CI. Mikołaj proposed grouping updates and limiting auto-merge to patch versions or test dependencies. He wants manual review for high-impact dependencies like the Prometheus Operator, the Go version, and base images.
- **Feature gate cleanup and feature requests:** The group agreed to remove two stable feature gates. They agreed to allow an instrumentation image tag override via annotation only when the Instrumentation CR enables it with a boolean. A base collector config merge proposal was parked pending a stronger use case. A label-selector filter for watched CRs was accepted.
- **CRD and release maintenance:** Pavol will set the v1alpha1 CRD to `served: false` instead of using a feature gate, with release notes explaining how to re-enable it. Signed images are waiting on a Red Hat build, and the minimum supported Kubernetes version may be raised around February after OpenShift 4.20 leaves extended support.

## Action Items
- Pavol: Investigate AI PR review and AI issue triage options for the repo.
- Pavol: Look into enabling Renovate auto-merge, scoped to safe dependency types.
- Mikołaj: Remove the two stable feature gates.
- Mikołaj: Close the base collector config PR and comment on the issue that it is parked pending a specific use case.
- Mikołaj: Remove the "discussed" label from the label-selector PR so it can proceed.
- Pavol: Open the v1alpha1 `served: false` PR and post on the related issue with patch instructions to restore it.
- Pavol: Bump to signed images once the Red Hat build is available.
- Mikołaj: Raise the minimum supported Kubernetes version around February.
- Benedikt: Implement the tag-override boolean on the Instrumentation CR (not yet assigned explicitly).
- Andy Keller: Review the instance UID PR for the OpAMP-related work.

## Participants
Pavol Loffay, Mikołaj Świątek, Benedikt Bongartz, Mujib Ahasan, Andy Keller
