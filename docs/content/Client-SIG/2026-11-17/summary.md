## Key Topics
- **Deprecating client-side semantic conventions in the core registry:** Martin has approved PRs to deprecate client-side conventions in core, which must merge before matching PRs can follow in the client-side registry. Deprecated attributes stay available, and Hanson will handle the Android equivalents.
- **Android namespace cleanup:** Hanson proposes deleting unpublished, internal Android instrumentation conventions rather than deprecating them, since they were never versioned or published as a stable registry. Jason is unsure whether anything depends on them, and the group agreed to keep stability guarantees for published conventions.
- **Schema URLs and multiple registries:** Instrumentation can depend on more than one registry (for example, client-side and core), and dependencies are not transitive. This raises an open question about which schema URL an SDK should report, and the group agreed the design needs clarification.
- **Dev vs. stable schemas:** The relationship between dev and stable schemas is unclear. Dev is likely a superset of stable, but the group thinks this needs confirmation.

## Action Items
- Martin: Review and approve the core registry deprecation PRs (Hanson to stamp them).
- Hanson: Deprecate the Android-namespace conventions this week, following the same process Martin used.
- Hanson: Ask in Slack how instrumentation should set schema URLs when it depends on multiple registries, and look into the Weaver change he plans to push.
- Jason: Review the SemConv PRs this morning.
- Group: Clarify the federated schema design, including the dev/stable relationship.

## Participants
Martin Kuba, Jason Plumb, Hanson Ho, Michael Bushe
