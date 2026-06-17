## Meeting Notes

### Attendees
- Sven Cowart (ElastiFlow)
- Giuseppe Ognibene (Coralogix)
- Rob Cowart (ElastiFlow)
- Antonio Jimenez (ThousandEyes)
- Stephen Lang (Grafana)

### Agenda
- Status
- [Antonio Jimenez]
  - proposal network attributes
    - IP Prefix [https://github.com/open-telemetry/semantic-conventions/issues/3731](https://github.com/open-telemetry/semantic-conventions/issues/3731)
      - Bring up that local/peer are not the right names
    - AS (Autonomous System) Organization Number [https://github.com/open-telemetry/semantic-conventions/issues/3740](https://github.com/open-telemetry/semantic-conventions/issues/3740)
    - Reverse DNS [https://github.com/open-telemetry/semantic-conventions/issues/3741](https://github.com/open-telemetry/semantic-conventions/issues/3741)
      - There is a misalignment with how `.address` is used by source/destination/client/server and how it can represent a domain but not a reverse dns lookup domain. We need to clear up that issue first.
      - There is also friction with the generic meaning behind address
  - Discussing if we really want to keep using `peer` or we prefer to use `local` and `remote`. Open for discussion
- Next Steps:
  - [Sven] Sync with Braydon to setup a new call time.
  - [Sven] Update “Current documents” in the meeting notes
  - [Sven] Network Project document
    - Highlight the overlap to the other SIGs and how to collaborate on an on-going basis
  - [Rob - to do an initial review] Review any network entities in system SIG and engage to avoid fragmenting Network and System SIGs
    - [Stephen] I can keep an eye on k8s sem conv as I’m there regularly, they already overlap with System SIG (for nodes)
