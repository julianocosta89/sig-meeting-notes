## Meeting Notes

### Attendees
- Ruediger
- Greg
- Anand
- Antoine
- Morgan

### Agenda
- GHA runner for OpenTelemetry Collector repro
  - Ruediger tried to do the install, still had issues.  Suspect that may need to elevate Ruediger’s repo privileges just during the install?  May require assist by Trask or Austin Parker.
- Documentation (see 11/5) to be followed up (Action: Greg)
  - Related topic get the metric discussion continued
- Ruediger: z/OS sub system spans to be added as PR to the Semantic Conventions - to be done
- Current status:
  - OTel Collector:
    - Runs on zLinux, but not z/OS
  - Vendor specific solutions do exist to harvest metrics, logs and traces and emit via OTel.
- Kubecon update
  - Questions from press and analysts at KubeCon wrt Mainframe support for OTel seem to be increasing.  This is telling as KubeCon may be the LAST place one would expect mainframes to be discussed.
