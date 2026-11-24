## Key Topics
- **OB SIG flow issues and flow semantic conventions:** Giuseppe relayed a question from the OB SIG about whether two open flow issues belong in the 2026 goals or 2027. Antonio judged 2026 is too close given the holidays. Sven is holding off on PRs until a formal flow semantic convention proposal exists. The CIDR attributes now exist, and flow.direction will map to network.direction (ingress/egress).
- **Entity relationships:** Braydon explained that entity relationships will be emitted as entity events, separate from signal payloads, so backends can track them over time. This approach is still theoretical and not yet implemented in backends. Sven will apply it to his entity work.
- **system.network and hardware.network consolidation:** Antonio proposed moving interface and packet metrics into the existing network namespace and deprecating the hardware and system.network conventions. Braydon noted these are close to ProcFS data and are heading to release candidate, so a replacement is needed first. Rob argued interfaces belong under system, and Sven leaned toward modeling via entities. No decision was reached.
- **Test environments for network telemetry:** Antonio proposed using Oracle/OCI credits (via John Ashley) for a virtual network lab for SNMP receiver testing. Alec suggested DevNet always-on sandboxes as an alternative, and Sven noted Rob's lab and possible Boston rack space for real hardware.

## Action Items
- Giuseppe: Check the status of the two OB SIG flow issues and open a Slack thread in the OTel network channel.
- Sven: Finish a formal flow semantic convention proposal and a PR for the CIDR and network.direction changes within a few days.
- Antonio: Finish the interface/packet PR and share it in Slack. Collect emails for Oracle credit access and send them to John Ashley.
- Rob: Investigate sys/class/net metrics and map them to Antonio's PR to inform the system vs. network decision.
- All: Suggest which metrics should move under the network namespace.
- Antonio: Follow up on remaining agenda items at the next meeting.

## Participants
Rob Cowart, Antonio Martinez, Giuseppe Ognibene, Sven Cowart, Braydon Kains, Alec
