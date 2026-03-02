## Meeting Notes

### Attendees
- Josh
- [Ted Young](mailto:ted.young@grafana.com)(Grafana Labs)
- [Nathan Smith](mailto:nathan.smith@elastic.co) (Elastic)

### Agenda
- … insert topics here …
  - [josh] Continue Entity + Breaking change discussion
    - Explicitly allowing descriptive attributes on Resource breaks our model
      - (yes, people use them in practice)
      - (yes this only breaks forwards compatibility)
    - How do we want to advertise / communicate this in OTEL?  What is our messaging?
    - Resource immutability examples:
      - OpAMP control signals
    - Problematic case #1
      - Existing receiver assumes immutable Resource
      - Update SDK to one that uses Entity
        - Now mutable attributes impact Resource, breaking receiver.
    - Problematic case #2
      - E.g. [host.ip](http://host.ip) is now a descriptive attribute
      - Existing users that put this on Resource would be *unable to* in the Entity world, if we didn't put descriptive attributes in Resource.
    - Strawman proposal - cancelled
      - By default - only identifying attributes of entities go on Resource
      - Users opt-in to allowing descriptive attributes for Resource
        - [daniel] We should allow descriptive attributes which do not change to be allowed on-by-default
    - We will communicate a breaking change
      - Update routing exporter in collector to have "resource_id" as a routing key
      - Update OpAmp specification to directly interact with Entities
      - Communicate breaking spec change widely.
      - Prometheus Exporter specification
      - Resource + Metric Identity
- Update project tasks + target date
  - [https://github.com/orgs/open-telemetry/projects/85](https://github.com/orgs/open-telemetry/projects/85)
