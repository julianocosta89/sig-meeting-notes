## Key Topics
- **Release automation:** Brett has tagged new versions and is nearly finished automating releases in DevTools. He plans a manual release today, which needs a release-prep PR approved first.
- **SemConv incubating attribute removals:** Incubating attributes were removed in a SemConv update, breaking dependent code. Options discussed include keeping removed attributes as deprecated, failing CI on removals, namespacing incubating attributes by version, and using AI agents to track changes.
- **Docker distro image:** Brett has a PR to publish an OTel distro Docker image for `COPY --from` use, which Paweł supports. They discussed the OTel Operator's PHP work and Paweł's plan to integrate the distro on his Elastic task. Auto-injection via the LD_PRELOAD injector only works on hosts, not in containers.
- **Declarative config and HTTP sanitization:** The contrib HTTP config and URI sanitizer have drifted from core. Typed access is still pending in the spec, and the team discussed whether contrib should align with core's config shape.
- **Security advisory and maintainers:** A reported issue involves Symfony HTTP Foundation instrumentation changing userland request behaviour. The advisory still needs to be accepted by the assigned roster member. Brett made Paweł and Chris maintainers across the PHP repos during the meeting.

## Action Items
- Brett: Research how other SIGs handle SemConv attribute removal and propose a policy or CI check.
- Brett: Prepare and run the manual release, starting with the release-prep PR for approval.
- Brett: Ping Carlos to accept the security advisory, then coordinate the patch release.
- Brett: Follow up on the declarative config path forward, possibly by setting up a call with Tobias.
- Chris: Add a second maintainer to the Packages entries using the new API.
- Chris: Update the contrib URI sanitizer PR to build against the spec attributes.
- Chris: Investigate whether instrumentation can safely access the request object without side effects.
- Paweł: Review and merge the Docker distro PR after fixing the noted script issues.
- Paweł: Explore integrating the distro with the OTel Operator as part of his Elastic task.

## Participants
Brett McBride, Paweł, Chris Lightfoot-Wild
