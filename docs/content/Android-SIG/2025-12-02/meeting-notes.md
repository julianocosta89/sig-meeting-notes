## Meeting Notes

### Attendees
- Jason (Splunk)
- Jairo (Honeycomb)
- Hanson Ho (Embrace)
- Jamie Lynch (Embrace)
- cleverchuk(solarwinds)

### Agenda
- [jason] Any feedback yet on rc.1?
  - Feedback can be added to [https://github.com/open-telemetry/opentelemetry-android/issues/1257](https://github.com/open-telemetry/opentelemetry-android/issues/1257)
- [jason] What do we want to do about [https://github.com/open-telemetry/opentelemetry-android/pull/1406](https://github.com/open-telemetry/opentelemetry-android/pull/1406) ? This one isn’t just the demo app (I think some instrumentation depends on it)
  - Wait until 1.0 is out and then release 2.x right after
    - It’s considerably more work to support 2 release branches
    - Bumping the minSdk version is a breaking change for users
      - Google doesn’t bump the required Play minsdk very often (phew!)
    - Suggest doing major version bumps once a year
  - Also need to consider AGP, kotlin, compose, etc.
  - We’re following Play Services versioning
    - [https://github.com/open-telemetry/opentelemetry-android/blob/79309e01b5ad3baf0b43bf95439201d38e8237c1/VERSIONING.md#android-api-compatibility](https://github.com/open-telemetry/opentelemetry-android/blob/79309e01b5ad3baf0b43bf95439201d38e8237c1/VERSIONING.md#android-api-compatibility)
  - How long should we do releases from a main branch after another main version is released?
    - Dependabot at minimum?
    - As needed. On demand.
  - What we should do is:
    - Pin the versions of the deps for dependabot
- Main is 1.1.0
- We can use a 2.0.0 milestone to put issues in
  - AI: Jason to create milestone
- [jason] Open call for contributors…
  - [https://github.com/open-telemetry/community/blob/main/guides/contributor/membership.md](https://github.com/open-telemetry/community/blob/main/guides/contributor/membership.md)
  - Can we simply copy what’s in core/java?
    - [https://github.com/open-telemetry/opentelemetry-java?tab=readme-ov-file](https://github.com/open-telemetry/opentelemetry-java?tab=readme-ov-file)
- If you haven’t checked out the CLO monitor page for our repo, check it: [https://clomonitor.io/projects/cncf/open-telemetry#opentelemetry-android](https://clomonitor.io/projects/cncf/open-telemetry#opentelemetry-android)
