## Meeting Notes

### Attendees
- Jason Plumb (Splunk)
- Ben Joseph (Grafana)
- Hanson Ho (Embrace)
- David
- João Oliveira (Datadog)
- Cesar (Elastic)
- Surbhi A (Cisco)

### Agenda
- [jason] what did I miss last week
  - Release happened
  - Small bug - accidentally enabled an auto-instrumentation from core
    - [https://github.com/open-telemetry/opentelemetry-android/issues/1842](https://github.com/open-telemetry/opentelemetry-android/issues/1842)
    - Does this warrant a patch release?
      - Yeah ok
    - AI: Jason to wrangle the release
- [Surbhi A] Discuss semantic convention group guidance on new and experimental client specific telemetry:
  - New repo like [https://github.com/open-telemetry/semantic-conventions-genai](https://github.com/open-telemetry/semantic-conventions-genai) for new experimental client semantic conventions until it is ready to be part of main semantic conventions repo. Some contenders for this:
    - [https://github.com/open-telemetry/semantic-conventions/pull/3727](https://github.com/open-telemetry/semantic-conventions/pull/3727)
      - Reason - Server side apps want these timing attributes to be part of the same HTTP client span but client side app’s use cases do not fit that.
    - Perhaps experimental Interactions semantic conventions.
    - A new repo has a benefit in that you can go see android, ios, browser, common, all in one place.
      - What’s common and what’s different is more obvious
      - New repo should be able to layer on top of the 3 platforms and then common bubbles up to the repo.
  - Federated semconv issue: [https://github.com/open-telemetry/opentelemetry-android/issues/1814](https://github.com/open-telemetry/opentelemetry-android/issues/1814)
  - Who is in charge of making sure things are aligned between client implementations.
    - Client SIG!
    - New repo would need maintainers and approvers
  - Does federation create duplication between implementations?
    - Perhaps, but at least it should help establish usage and is easier to compare between them if/where they differ.
  - Does KMP add complexity here?
    - Maybe some, but ideally the api/sdk don’t even reference semconv
    - Another platform (browser, ios, native, whatever) might have instrumentation that references semconv
  - Should we ever mark these stable then?
    - If we do so, then does it make changing them later impossible or much harder
      - I think the answer is yes
- <your item here>
