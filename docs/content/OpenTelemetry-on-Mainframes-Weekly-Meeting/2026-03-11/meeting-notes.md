## Meeting Notes

### Attendees
- Richard Nikula (BMC)
- Jim Porell (Rocket)
- Morgan McLean (Splunk)
- Richard Salac (Broadcom)
- Greg Shriver (Broadcom)

### Agenda
- Ruediger joined the SemConv SIG call on Monday:
  - Reviewed PR [#1898](https://github.com/open-telemetry/semantic-conventions/pull/1898). See the comments [here](https://github.com/open-telemetry/semantic-conventions/pull/1898/changes). Discussed if name space should be tps.* and if other TPS vendors will support. We may write blog to get attention from others, or move to ibm.cics.* and ibm.ims*.
  - Also see the [meeting notes](https://docs.google.com/document/d/10xG7DNKWRhxNmFGt3yYd3980a9uwS8lMl2LvQL3VNK8/edit?tab=t.0#heading=h.ylazl6464n0c) of the SemConv SIG call.
- Discussion around namespace feedback from SemConv SIG.
  - In general, vendor-specific namespaces are not something that currently exists in the OTel Semantic Conventions.  For example, a zos.* namespace would be preferred over a broadcom.* namespace.
  - For tps, a tps.* namespace may make more sense than ibm.* or bmc.* or broadcom.*, etc.
  - Jim to reply to Luidmila in PR [#1898](https://github.com/open-telemetry/semantic-conventions/pull/1898) regarding the existence of other mainframe tps systems that are neither IBM nor Oracle.
  - Agreed that further discussion on this topic is warranted…
