## Meeting Notes

### Attendees
- **Bob Strecansky**
- **Chris Lightfoot-Wild**
- **Pawel Filipczak**

### Agenda
- Suppressing instrumentation [CLW]
  - Follow up with a slack thread in #otel-php or #otel-instrumentation
  - Laravel instrumentation - I’d like to be able to turn off all instrumentation and turn it back on again
    - Capture a unit of work
    - Very long running traces (job processing, et. al) - distant parent
- Update [PF]
  - Small bugfixes and documentation ([README.md](http://README.md) / docs / dev guide)
  - Working on the release workflow
  - Release imminent!
    - Try it out: [https://github.com/open-telemetry/opentelemetry-php-distro/actions/runs/22494009391](https://github.com/open-telemetry/opentelemetry-php-distro/actions/runs/22494009391)
    - Grab the artifacts from the build to try it out!
      - [packages-linux-x86-64](https://github.com/open-telemetry/opentelemetry-php-distro/actions/runs/22494009391/artifacts/5693482151)
