## Meeting Notes

### Attendees
- Jason (Splunk)
- Jamie (Embrace)
- Cesar (Elastic)
- Surbhi A (Cisco)

### Agenda
- [Surbhi] - Discuss the leaking **androidx.*** transitive dependencies:
  - Some potential solutions - [https://github.com/open-telemetry/opentelemetry-android/issues/1663#issuecomment-4145640096](https://github.com/open-telemetry/opentelemetry-android/issues/1663#issuecomment-4145640096)
    - Reflection might be a last resort (we don’t love it)
    - Apps are sensitive to versions of androidx.*
      - The changes from upstream are often breaking/changing
    - Next steps - let’s do the safe thing first
      - Surbhi’s PR removing the reflection
      - Jason’s PR will be stripped to just the one line core removal
    - @RequiresApi could be replaced with our own internal annotation
      - (see the animal sniffer code in conventions)
  - Some fixes - [https://github.com/open-telemetry/opentelemetry-android/pull/1668](https://github.com/open-telemetry/opentelemetry-android/pull/1668)
- [Surbhi] - Discuss open questions on network timing attributes - [https://github.com/open-telemetry/semantic-conventions/issues/3385#issuecomment-4099974525](https://github.com/open-telemetry/semantic-conventions/issues/3385#issuecomment-4099974525)
- [Cesar] Next steps regarding: [https://github.com/open-telemetry/opentelemetry-android/pull/1645](https://github.com/open-telemetry/opentelemetry-android/pull/1645)
  - Let’s try and get this merged
  - Prefer having it in the next release…
  - We think it’s probably OK to stabilize session
- IA: Jason to release java-contrib assuming it’s ok
- Release?
  - - We are due for it, but will probably push back in order to get the milestone work complete
