## Meeting Notes

### Attendees
- Rob Cowart (ElastiFlow)
- Josh Suereth
- Daniel Dyla
- Dmitry Anoshin
- Michele Mancioppi (Dash0)
- Pablo Baeyens (Datadog)

### Agenda
- SDK changes
  - Loose / Raw are too colloquial
  - "Unassociated"
  - AI - jsuereth - Create PR to spec with changes to get Java prototype submitted upstream.
- [Rob] Network entities
- [michele] we have entity type and id, why not name?
  - Name would be non-unique human readable identifier
  - [josh] ideally name would be derivable from the type and attributes
  - Could add semi-normative (e.g. SHOULD) `name` derivation for an entity by type in semantic conventions.
    - e.g. would rely on recommended attributes
    - Could be in an annotation so it's machine-consumable
  - Today we have entity id + entity-type
    - Do we need to send a type all the time?
    - The ID currently defines the type
- [pablo] host resource attributes when you cannot identify a host
  - In order to talk about host entity, you need all identifying attributes populated?
  - Not on cloud VM - don't have /etc/machine/id
