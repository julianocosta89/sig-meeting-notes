## Meeting Notes

### Attendees
- [João Duarte](mailto:joao@elastic.co) (Elastic)
- Kalman Meth (IBM)
- Pablo Baeyens (Datadog)
- Christos Markou (Elastic)
- Moritz Wiesinger (Dynatrace)
- [Jade Guiton](mailto:jade.guiton@datadoghq.com) (Datadog)
- [Evan Bradley](mailto:google@evanbradley.org) (Dynatrace)
- Dhanya R Mathews (IBM)
- Roger Coll (Elastic)
- Edmo Vamerlatti (Elastic)
- Damien Mathieu (Elastic)
- Marylia Gutierrez (Grafana Labs)
- Mikołaj Świątek (Elastic)
- Paulo Dias (Five9)
- Michalis Katsoulis (Elastic)

### Agenda
- [Marylia]: Feedback from contributor experience PR survey for non-members:
  - Avg 13 answers: 4.6/5
  - General people are happy with the process
  - Suggestion: Add documentation on running the local testing across multiple platforms
  - Common complaint: PRs can be quick to get reviews and approval, but after approval is taking a long time to actually get merged, with contributors having to ping or go after people to get their PRs merged, and it's not clear who should be doing what
  - Complaints about broken pipeline
  - Live discussion
    - Issues that we could open
      - Automatically add label if codeowners have approved and approvers have done so as well
        - E.g. in the JS repo [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2798/files](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2798/files)
      - Move approval process description to [CONTRIBUTING.md](http://CONTRIBUTING.md)
      - Create process (maybe within meetings) to go through PR backlog
- [Dhanya]: Requesting review for the PR [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/41877](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/41877)
  - The Sampling SIG is a good place to get traction on this, details are available on [https://github.com/open-telemetry/community?tab=readme-ov-file#sig-sampling](https://github.com/open-telemetry/community?tab=readme-ov-file#sig-sampling)
- [Michalis] Sponsorship for new component aws lambda receiver
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/43504](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/43504)
- [Pablo] Addressing TOC recommendations from adopter interviews
  - See TOC recommendations doc: [Recommendations for OpenTelemetry](https://docs.google.com/document/d/1SQMdfYpCiBfpxtWDwASXVIl-PIzD9X4vdDPXYUphAF0/edit?tab=t.0#heading=h.fn06amgn4poq) and TOC issue [https://github.com/cncf/toc/issues/1739#issuecomment-3386269224](https://github.com/cncf/toc/issues/1739#issuecomment-3386269224)
  - See [Specification SIG recording from yesterday](https://zoom.us/rec/play/39lDX-zX5wSyxo9UiLNKpWaAcKwUJsg22_BPfXmnt4Xv8cvPWp814aAKpJKqtR-6gA6kGJD6DbUENkxb.8eeh_1hnIBveqvbx?eagerLoadZvaPages=&isReferralProgramEnabled=false&isReferralProgramAvailable=false&accessLevel=meeting&canPlayFromShare=true&from=share_recording_detail&continueMode=true&componentName=rec-play&originRequestUrl=https%3A%2F%2Fzoom.us%2Frec%2Fshare%2FgrTgw03OZSoUWkVbv5rQkhY_V9YN40IvsUrM-nwpE3gDYOvl6vY32K4SMkBkO68I.mIJ9CbqGccekyBjm)
  - Not a critique on our work, mostly a question of framing of stability and documentation
  - Pablo is going to make the Collector-specific discussion into issues for further discussion
- [Roger] Any plans/discussion to change zap.Logger with Golang’s standard [slog](https://pkg.go.dev/log/slog)? [https://github.com/open-telemetry/opentelemetry-ebpf-profiler/issues/417#issuecomment-2976701664](https://github.com/open-telemetry/opentelemetry-ebpf-profiler/issues/417#issuecomment-2976701664)
  - component.TelemetrySettings is v1 now, we would have to maintain support for zap as long as we maintain component v1 (v2 would be a long term thing)
  - Pablo thinks using [https://pkg.go.dev/go.uber.org/zap/exp/zapslog](https://pkg.go.dev/go.uber.org/zap/exp/zapslog) is a good first step
- [Mikołaj] PSA: opentelemetry-operator now runs its E2E tests against contrib [nightly](https://github.com/open-telemetry/opentelemetry-operator/actions/workflows/e2e-nightly.yaml). These tests caught some serious bugs recently, and it would’ve been much simpler for everyone if it happened earlier rather than later.
