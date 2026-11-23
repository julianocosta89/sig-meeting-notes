## Key Topics
- **Python 3.9 support:** Denys asked whether OTel Python instrumentation will support Python 3.9, since RHEL 9's system Python is 3.9. Diego noted the Python SIG's policy of dropping old versions, and Michele argued the policy optimizes for maintainers rather than end users. Diego will raise it with the Python SIG.
- **Injector and agent packaging tension:** Diego argued that packaging's needs (vendored dependencies, support for all Python versions) conflict with the rest of the project and may push users toward the older OTel Python agent. Michele said a recently merged specification PR defining requirements for injectable libraries can help these discussions.
- **Packaging repo cleanup:** With OBS becoming the source of truth for builds, Denys asked whether the repo's own packaging infrastructure (DEB/RPM build code) is still needed. Michele suggested opening a PR to delete unneeded pieces and asking the channel whether anyone wants to maintain them. Several open PRs were triaged, and one was sent back for rework.
- **Collector packaging:** Denys asked whether there is a plan to package the Collector. Michele said there is interest, a tracking issue was opened, but nobody is working on it. They agreed to defer until a package hosting location exists.
- **SBOM generation:** The group discussed whether packaging should generate SBOMs or whether upstream should provide them, since the Collector maintainers would normally own this. No decision was made; the group agreed to wait until customers request SBOMs.

## Action Items
- Diego: Raise the Python 3.9 support question with the Python SIG (revive issue 309).
- Michele: Send the rework PR back to its author with feedback.
- Michele: Post in the channel asking maintainers whether they want to keep any packaging infrastructure that OBS replaces.
- Denys: Open a PR removing unneeded package-building infrastructure from the repo.
- Diego: Review the outstanding PR that needs rebasing and conflict resolution.
- Diego: Look into the packaging PR states and report back (as discussed).

## Participants
Diego Hurtado, Denys Sedchenko, Michele Mancioppi
