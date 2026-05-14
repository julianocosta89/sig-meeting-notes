## Meeting Notes

### Attendees
- Antoine Toulme (Splunk)
- Liudmila Molkova (Microsoft)
- Ruediger Schulze (IBM)
- Jim Porell (Rocket)
- Richard Nikula (BMC)
- Greg Shriver (Broadcom)

### Agenda
- [Liudmila] Overview of -genai semconv as a way to separate semantic conventions
  - Plan to execute with a few parallel streams
    - Entities
    - Messaging - mainframe or separate repository?
    - Virtualization - previous discussions on semantic conventions SIG call
      - Best on what was discussed last year, discuss separate repository from mainframe?
    - Discussion of the right scope of work
      - Z HMC too low level
      - Z APM and metrics from subsystems - correlation?
        - Entities definition - TPS PR [https://github.com/open-telemetry/semantic-conventions/pull/1898](https://github.com/open-telemetry/semantic-conventions/pull/1898)
        - Identifiable attributes
- [Antoine] discuss time of meeting again for Ruediger
- [Antoine] quick update on items from last week
  - We are without updates on s390x runners, am trying to push this to GC. I will find other escalation routes.
  - The new repository was a bit bumpy to get going, but I got a request up here: [https://github.com/open-telemetry/community/issues/3432](https://github.com/open-telemetry/community/issues/3432)
- HMC as a collector?
  - Customers may be risk averse to this approach
  - [https://github.com/zhmcclient/golang-zhmcclient](https://github.com/zhmcclient/golang-zhmcclient) - Prometheus
  - Looking at HMC more as an example of how to craft mf otel sem conv?
  - Jim P.  HMC is similar to VM Control Manager -- explaining how a physical machine is broken up into virtual “containers”
- [External? OMP?] Meeting next Monday to discuss OTel Collector on native z/OS USS.
  - Not sure of timelines
  - Stripped down collector was working at one point in the past - albeit sans host metric receiver, and sans some of the processors from the contrib repo
- TPS PR to move to the mainframe SemConv repo: https://github.com/open-telemetry/semantic-conventions/pull/1898
