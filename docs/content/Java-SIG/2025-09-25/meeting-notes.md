## Meeting Notes

### Attendees
- Jonathan Halliday (IBM)
- [John Watson](mailto:jkwatson@gmail.com)(Cloudera)
- Jason (Splunk)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com) (Grafana)
- Jay DeLuca (Grafana)
- Trask Stalnaker (Microsoft)
- Peter Findeisen (Cisco)
- Surbhi A (Cisco)
- Robert Niedziela (Splunk)
- Jack Shirazi (Elastic)

### Agenda
- Old / backlog issue and PR triage
  - Some need a decision
  - A good way to help is to jump in and review/guide authors
  - Additional automation for things **with** **no activity**
    - Could mark stale first to give people a grace period
    - **Could automate adding the “needs author feedback” label and a comment asking them to respond**
    - Auto close Issues after 1 year for new feature requests
      - Include comment about re-opening if they want
      - Ensure comment includes how to re-open (might not be available for non-members)
    - Auto close if “needs repro” for 1 month (?)
    - Auto close PRs after 1 year regardless of tags
      - Could do this manually instead of automating
        - Less personal to use a bot
  - Jay to look into implementing this
  - Collector contrib has 14 days to mark as stale: [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/37114#issuecomment-2664635396](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/37114#issuecomment-2664635396)
    - This PR was marked stale due to lack of activity. It will be closed in 14 days.
- [trask] Overview of a few core repo PRs, can answer any questions
  - [https://github.com/open-telemetry/opentelemetry-java/pull/7683](https://github.com/open-telemetry/opentelemetry-java/pull/7683)
  - [https://github.com/open-telemetry/opentelemetry-java/pull/7691](https://github.com/open-telemetry/opentelemetry-java/pull/7691)
  - [https://github.com/open-telemetry/opentelemetry-java/pull/7696](https://github.com/open-telemetry/opentelemetry-java/pull/7696)
  - [https://github.com/open-telemetry/opentelemetry-java/pull/7700](https://github.com/open-telemetry/opentelemetry-java/pull/7700)
  - [https://github.com/open-telemetry/opentelemetry-java/pull/7706](https://github.com/open-telemetry/opentelemetry-java/pull/7706)
  - [https://github.com/open-telemetry/opentelemetry-java/pull/7701](https://github.com/open-telemetry/opentelemetry-java/pull/7701)
- [Patrick] [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/14757](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/14757)
  - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/RELEASING.md#release-cadence](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/RELEASING.md#release-cadence)
- [Gregor] What to do about lychee failing to validate GH anchors? [https://github.com/lycheeverse/lychee/issues/1729#issuecomment-3214228199](https://github.com/lycheeverse/lychee/issues/1729#issuecomment-3214228199)
  - Try to run lychee twice - without anchors when gh is included
- [Surbhi A] Adding dns/tls/tcp events with timestamps to HTTP span.event to gather duration metrics in backends. For example:
- [https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/instrumentation/netty/README.md#settings-for-the-netty-instrumentation](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/instrumentation/netty/README.md#settings-for-the-netty-instrumentation)
- [https://github.com/open-telemetry/semantic-conventions/blob/main/docs/general/events.md](https://github.com/open-telemetry/semantic-conventions/blob/main/docs/general/events.md)
- [Jonathan] people with an interest in the profiling signal type may wish to read [https://docs.google.com/document/d/1hrfElwEdoUQbj-fY0vVVN7kmWmlmn9F_eZzxMuVnVwo/edit?usp=sharing](https://docs.google.com/document/d/1hrfElwEdoUQbj-fY0vVVN7kmWmlmn9F_eZzxMuVnVwo/edit?usp=sharing) in preparation for discussion. (we probably want JackBerg back from leave before discussing?)
- [Gregor] if time, discuss declarative configuration, as there’s no call today
