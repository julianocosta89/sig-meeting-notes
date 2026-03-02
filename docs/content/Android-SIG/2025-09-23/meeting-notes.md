## Meeting Notes

### Attendees
- Jason (Splunk)
- Jamie Lynch (Embrace)
- Cesar (Elastic)
- Mustafa Haddara (honeycomb)
- Jairo (honeycomb)
- Francisco Prieto (Embrace)
- cleverchuk(solarwinds)

### Agenda
- [Cesar] What could be causing the codecov error in this PR? [https://github.com/open-telemetry/opentelemetry-android/pull/1242](https://github.com/open-telemetry/opentelemetry-android/pull/1242)
  - Likely caused by being 1 commit behind main branch
  - Only 0.03% change, lolz
  - Jamie offered to take a look, thanks!
- [Cesar] Interesting approach to deal with non stable APIs. [PR by Jamie](https://github.com/open-telemetry/opentelemetry-android/pull/1238) (roadmap to 1.0.0 related).
  - Using methods that are marked as @Incubating causes a compiler warning
  - It is transitive, as shown here: [https://github.com/open-telemetry/opentelemetry-android/actions/runs/17863012755/job/50798314978?pr=1238#step:8:928](https://github.com/open-telemetry/opentelemetry-android/actions/runs/17863012755/job/50798314978?pr=1238#step:8:928) (demo app gets a warning)
  - Classes in this project also get warnings, but it’s just internal (for us devs, not users) for example [https://github.com/open-telemetry/opentelemetry-android/actions/runs/17863012755/job/50798314978?pr=1238#step:8:903](https://github.com/open-telemetry/opentelemetry-android/actions/runs/17863012755/job/50798314978?pr=1238#step:8:903)
  - Android developers are likely familiar with this style of annotation usage
    - AGP has an @Experimental ?
  - Is the new @Incubating annotation itself an api?
    - Can we discourage or prevent its use outside this project?
