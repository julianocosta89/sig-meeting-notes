## Key Topics
- **Long-running spans modeled as events:** Christophe proposed generic lifecycle events versus per-span-type events. Debate covered span model consistency, backend reconstruction, sampling/collector routing, and whether this belongs in the spec rather than Semantic Conventions. Agreed to take it to spec work.
- **Federated registries and namespaces:** Discussed reserving namespaces in core Semantic Conventions for external groups (Focus, OCSF, Green Software Foundation). Agreed on a litmus test for inclusion and a separate PR defining the policy.
- **OCSF collaboration:** Stephanie B proposed a dedicated working group. Josh suggested drafting a project proposal first, with a recurring Tuesday 1:15 ET slot as a starting point.
- **Database response status codes in duration metrics:** Debated whether to require status codes on failed-operation duration metrics. Concern about breaking alerts and histogram grouping. Liudmila to check existing wording; topic continued offline.
- **Schema V2 transition:** Liudmila proposed publishing a dev V2 schema artifact and maintaining a stable folder structure. Weaver's "latest" selection logic was flagged as fragile.

## Action Items
- Christophe: Take the long-running span event discussion to the spec/meeting, and open a separate PR for the federated registry policy.
- Josh: Raise the namespace/registry governance question with the GC; add criteria for inclusion; follow up on the OCSF collaboration.
- Josh and Michele: Continue the database status code/metric discussion on the issue.
- Liudmila: Check existing database duration metric wording on status codes; draft Semantic Conventions 3.0 V2 schema PR; notify OTel.io maintainers.
- Stephanie B: Post draft agenda and Slack channel info for the OCSF collaboration meeting; share links to prior documentation.
- Liudmila: Post Weaver resolution issues in the Weaver call.

## Participants
Josh Suereth, Christophe Kamphaus, Michele Mancioppi, Liudmila Molkova, Stephanie B, Armin (Dynatrace)
