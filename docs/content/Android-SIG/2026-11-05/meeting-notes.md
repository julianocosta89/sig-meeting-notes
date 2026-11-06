## Meeting Notes

### Attendees
- Jason (Splunk)
- Ben (Grafana)
- Jamie (Embrace)
- Vishwan (Grafana)
- Hanson Ho (Embrace)
- Cesar (Elastic)

### Agenda
- Jason - Contribfest next week at kubecon, I’ll label some issues or make new ones
- Jamie - Worth shipping a fix for these or not?
  - [https://github.com/open-telemetry/opentelemetry-android/issues/2183](https://github.com/open-telemetry/opentelemetry-android/issues/2183)
    - Why didn’t the build flag this?
    - Do we have build checks for this?
    - AI: Jason to open an issue to figure out why animalsniffer didn’t catch this
      - [https://github.com/open-telemetry/opentelemetry-android/pull/2196](https://github.com/open-telemetry/opentelemetry-android/pull/2196)
      - [https://github.com/open-telemetry/opentelemetry-android/pull/2195](https://github.com/open-telemetry/opentelemetry-android/pull/2195)
    - AI: Jason to make sure there aren’t other obvious Duration violations before doing the patch release
  - [https://github.com/open-telemetry/opentelemetry-android/issues/2186](https://github.com/open-telemetry/opentelemetry-android/issues/2186)
  - We do want a patch release - 1.8.1
- Jason - stale workflows
  - [https://github.com/open-telemetry/opentelemetry-kotlin/pull/1007](https://github.com/open-telemetry/opentelemetry-kotlin/pull/1007)
  - AI: Jason to open a tracking issue and start digging into why this sisn’t working.
    - Adding docs along the way if we don’t have them
    - Goal - both issues and PRs flagged with needs author to get stale after X time
    - Stale issues and PRs get closed after Y time
    - Any activity (comment, commits) keep the stale items open (not closed) and removes the label
    - Any comment from the author on needs-author-feedback removes the label
    - Issues should stay open much longer. We shouldn’t need to treat issues and PRs the same.
