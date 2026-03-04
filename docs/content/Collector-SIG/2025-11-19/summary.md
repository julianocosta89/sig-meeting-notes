## Key Topics
- Discussion on improving consistency between `configHTTP` and `configGRPC`, including the potential for breaking API changes.
- Proposal to change the default Windows installer from local system to local service for better security and deployment flexibility.
- Introduction of a new concept for scrapers to allow one-shot scrapes triggered by events, decoupling them from receivers.
- Consideration of using cron jobs for scheduling scrapes in Kubernetes environments.

## Action Items
- Andrew to open a new issue regarding the `configHTTP` and `configGRPC` changes and raise it in Slack for awareness.
- Paulo to create a PR testing the local service configuration for the Windows installer.
- Andrew to share links related to the scraper concept and configuration changes with Paulo via Slack.

## Participants
Andrew Wilkins, Paulo Janotti
