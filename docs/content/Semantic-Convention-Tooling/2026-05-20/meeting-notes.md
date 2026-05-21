## Meeting Notes

### Attendees
- Jeremy
- Cijo Thomas
- Josh Suereth
- Liudmila Molkova
- Arianna Vespri (2nd half)

### Agenda
- [Cijo] Discuss shipping Github actions to help Weaver Live-Check across OTel repos and possibly elsewhere
  - [https://github.com/open-telemetry/weaver/pull/1448](https://github.com/open-telemetry/weaver/pull/1448)
- [Arianna] I have this PR open [https://github.com/open-telemetry/opentelemetry-weaver-packages/pull/29](https://github.com/open-telemetry/opentelemetry-weaver-packages/pull/29)
- [Jeremy] Scorecard PRs and Badge
  - TODO - figure out why branch protection is being flagged as missing.
- [Liudmila] Exclude definitions [https://github.com/open-telemetry/weaver/pull/1458](https://github.com/open-telemetry/weaver/pull/1458)
  - Looks good
  - Include_unreferenced + live_check
    - We need to support multiple schema_urls
    - [https://github.com/open-telemetry/weaver/issues/1456](https://github.com/open-telemetry/weaver/issues/1456)
- [Jeremy] Shall we do this?
  - entity_associations:
  - - all_of:
  - - market_switcher
  - - tenant
  - - cloud
  - - one_of:
  - - host
  - - container
  - - one_of: <-- multiple one_ofs
  - - all_of: <-- nesting all_ofs and one_ofs
  - - x
  - - y
  - - z
