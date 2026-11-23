## Key Topics
- **Long-running spans:** Christophe followed up on SemConv feedback that long-running span lifecycle events should go through the spec process first. He drafted a proposal for OTel span events and will join the spec (SPAC) meeting. Open questions include delta vs. full-snapshot heartbeats, how to merge attributes, and how to reconstruct spans from events. Prior art includes Dagger's approach of emitting full span snapshots.
- **Span and metric naming:** A proposal to rename CI/CD metrics to align with span names was discussed. Participants, including Carlos, Dotan, and Adriel, argued against renaming a widely used, near-stable metric. Span duration should always match the metric duration, so no distinct use case exists.
- **OTel Unplugged Europe 2027:** Dotan announced the unconference will be held in early February 2027 as a fringe event of FOSDEM, in the same location. He also asked for community sponsors.

## Action Items
- Christophe to comment on the metric rename proposal, recommending against renaming.
- Christophe to bring the long-running span proposal to the spec (SPAC) meeting.
- Christophe to sync on work codifying span metrics in the spec.
- Dotan to add the OTel Unplugged Europe registration link to the meeting notes.
- Adriel to attend the next session if schedule allows.

## Participants
Adriel Quinn Perkins, Christophe Kamphaus, Carlos Alberto Cortez, Dotan Horovits
