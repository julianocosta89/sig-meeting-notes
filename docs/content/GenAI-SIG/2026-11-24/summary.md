## Key Topics
- **Agent identity definitions:** Victor Lu's draft taxonomy (developed with OCSF and the OpenID Foundation AIM group) prompted debate. Pam Dixon argued that telemetry's agent identifier is a grouping label, while credential-based identity is different and should stay separate. Liudmila Molkova noted that OTel's existing GenAI Agent ID already fits the "identifier" concept. Agent skill is being replaced with agent identifier in the draft.
- **COSI/OCSF collaboration:** Jeff Leva shared a COSI issue outlining objectives and attribute definitions. Trask Stalnaker stressed that OTel's scope is mapping attributes that libraries can already capture, backed by real instrumentation or reference scenarios. The group discussed whether a GenAI security group should start under COSI/OCSF before forming an OTel group.
- **Message parts stability:** Liudmila raised concerns that provider-specific message parts have no stability guarantees. Options discussed included capturing them by default, using an opt-in flag, and using an "unknown" prefix instead of vendor prefixes. The topic was deferred to the stabilization call.
- **Upcoming presentation:** A Google contributor will present a trajectory format at the December 1 meeting, covering how trajectories relate to OTel.

## Action Items
- Victor Lu: share feedback with the OCSF team, update the taxonomy draft (replace agent skill with agent identifier), and work out how to show document comments to reviewers.
- Pam Dixon: send Victor the ITU SG17 contact information.
- Victor Lu: reach out to ITU SG17 after receiving the contact.
- Liudmila Molkova: revise message-parts options and bring them to the stabilization call.
- Jeff Leva: take feedback on the COSI issue and build real-evidence examples (via the OCSF emitter/Red Hat Praxis work) to support OCSF proposals.
- Victor Lu / Jeff Leva: decide whether a GenAI security group should be proposed in COSI/OCSF or as a new OTel SIG via a community issue.

## Participants
Liudmila Molkova, Surya Teja, Jeff Leva, Victor Lu, Pam Dixon, Trask Stalnaker, Aaron Abbott
