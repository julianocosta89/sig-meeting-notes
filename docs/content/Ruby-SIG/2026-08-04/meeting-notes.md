## Meeting Notes

### Attendees
- Kayla Reopelle
- Matt Wear
- Xuan Cao
- Daniel Azuma

### Agenda
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - [Kayla] [https://github.com/open-telemetry/opentelemetry-ruby/pull/2164](https://github.com/open-telemetry/opentelemetry-ruby/pull/2164)
    - Stale for a while. Do we want to accept this without further changes?
      - Will check in with them one more time, want the limits in this PR
      - Let stalebot handle it after that
  - [Kayla] [https://github.com/open-telemetry/opentelemetry-ruby/pull/2215](https://github.com/open-telemetry/opentelemetry-ruby/pull/2215)
    - Time to check back in?
  - Declarative config:
    - Goal to get the API to the level we want first
    - Let’s plan to discuss next week
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2443](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2443)
    - As long as it’s compliant with the spec today, we’re good with it
  - TODO: add other PRs
- Auto Instrumentation ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/pulls))
  - [https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/pull/39](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/pull/39)
- Burning questions?
  - [Kayla] Some issues with our release workflows. I’m looking into it.
    - Permissions issue with otelbot token in contrib
    - Github API issue in core
    - May be related to the Zizmor changes
    - MFA requirement for ruby-instrumentation, working with Daniel Azuma on it
      - Had to do this in Google
      - UI and API is the highest level
      - UI and sign-in is the lower level, can still make API calls without MFA
      - The lower level is specifically intended for workflows like this where you have automated scripts publishing gems / implementing MFA into that workflow is challenging
      - Daniel’s recommendation, should just work
      - Kayla will try that out today
- ✨ Happy Reports ✨
