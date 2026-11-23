## Key Topics
- **Semantic conventions for SNMP/network data:** Participants agreed to model standard SNMP MIBs (interface MIB, MIB-2, entity, host resources, OSPF, BGP) before vendor-specific extensions. OpenConfig and gNMI were discussed as related standards, with the goal of reconciling them.
- **Pull requests for geo and host name conventions:** Antonio presented open PRs adding a GeoNames ID attribute and a proposal for host name lookup via DNS resolution for IP addresses.
- **SNMP receiver profiles:** Antonio and Sven, as code owners of the SNMP receiver in the OTel Collector contrib, proposed profiles that map standard OIDs to semantic conventions while preserving flexibility for vendor-specific metrics.
- **Entities and relationships:** Braydon noted that a major entity contributor is leaving, leaving the entity work under-resourced. The group discussed the need for real-world relationship examples (e.g., LAG membership, VLAN, VRF, tunneling) to define relationship types.
- **Community outreach and KubeCon recap:** Antonio plans to invite contributors from Intel, Ericsson, and Guesswork to help model data center telemetry. Participants also shared KubeCon NA feedback and noted the event felt quiet.

## Action Items
- Antonio Martinez: Create GitHub issues for the SNMP interface MIB semantic convention work and link Rob's draft.
- Rob Cowart: Share his interface MIB draft and existing notes; consider drafting a guide on mapping SNMP concepts to OTel conventions.
- Braydon Kains and Rob Cowart: Serve as points of contact for the entity SIG and bring real-world relationship examples.
- Antonio Martinez: Invite Intel, Ericsson, and other data center contributors to future meetings.
- All: Review the open pull requests for GeoNames ID and host name semantic conventions.

## Participants
Josh Halley, Antonio Martinez, Giuseppe Ognibene, Rob Cowart, Braydon Kains, Matthieu Noirbusson
