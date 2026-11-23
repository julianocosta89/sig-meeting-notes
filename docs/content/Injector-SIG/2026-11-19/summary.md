## Key Topics
- **Symlink handling in ConfigMap mounts:** A check that accepted only real files broke mounting injector configs via ConfigMap, since symlinks were rejected. The team agreed this was an overcorrection. The packaging issue appears resolved, and a backwards-compatibility PR was opened.
- **Runtime detection:** The team plans to check executable exports to tell whether a binary is Node.js, Deno, or another runtime.
- **Docs and runtime defaults:** An outdated configuration doc needs updating. The default runtime value is an empty string and must be set explicitly to enable injection for a runtime, so the change is likely packaging-only.
- **Markdown style:** The team agreed on one sentence per line, with a 120-character maximum, for Markdown docs. A PR was opened and approved.
- **Stale issues and dependencies:** An old issue about declarative config via OpAMP will likely be closed if the reporter doesn't respond. A dependency update is stalled by a 17.1 release, and the team will open a Renovate PR to fix it.

## Action Items
- Michele: Work on the symlink/ConfigMap fix, possibly with Claude, and check whether any injector code change is needed.
- Michele: Comment on the docs issue to point to the latest configuration docs.
- Bastian: Comment on the declarative config (OpAMP) issue and close it if there is no response.
- Bastian: Follow up with Jack on his spec PR.
- Michele: Open the Renovate PR for the dependency update.
- Michele and Diego: Continue the packaging discussion in Huddle, since it's packaging rather than injector business.

## Participants
Diego Hurtado, Michele Mancioppi, Bastian Krol
