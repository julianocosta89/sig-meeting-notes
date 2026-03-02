## Meeting Notes

### Attendees
- Reiley Yang
- Jeremy Corley
- Trask Stalnaker

### Agenda
- [reiley] Looking for feedback [https://github.com/open-telemetry/sig-security/pull/156](https://github.com/open-telemetry/sig-security/pull/156)
  - [Trask] for medium/low, consider “SHOULD be released in the upcoming monthly release; MUST be released within 60 days since the initial announcement of the CVE”.
  - [Adriel] we should have separate rules for privately reported issues vs. published vulnerabilities in the dependencies.
  - When/if to publish our own CVE for a dependency
    - If we are exposing the vulnerability to the world, then we’re responsible for disclosing it (high+ after rescoring if needed)
    - In theory we should publish for even lower scores
  - [Reiley to follow up] Examples could help to make it clearer for maintainers
- Google’s osv tools
- [trask] Trivvy / Dependabot security
  - Docker command line for security scan?
  - Docker scout [https://docs.docker.com/scout/](https://docs.docker.com/scout/)
