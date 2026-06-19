## Meeting Notes

### Attendees
- Pablo Baeyens (Datadog)
- Braydon Kains (Google)
- Roger Coll (Elastic)
- Christos Markou (Elastic)

### Agenda
- Strategy for marking system namespace as stable
  - PR from Braydon explaining the difference between e.g. system.cpu vs cpu namespaces could help here
  - Internal dependencies
    - System.cpu depends on cpu
    - System.disk depends on disk
    - System.filesystem depends on file
    - System.network depends on network
    - Dependency on the host entity
      - We need to decide on the identifying attributes and mark them as stable
        - [host.id](http://host.id) would be the identifying attribute
          - [https://github.com/open-telemetry/semantic-conventions/issues/739](https://github.com/open-telemetry/semantic-conventions/issues/739)
          - The relationship between a host and a cloud VM instance is complicated!
          - What about nested virtualization
  - External dependencies
    - Container metrics depend on a bunch of attributes
    - Network group can help with network namespace
  - How can we split it up?
