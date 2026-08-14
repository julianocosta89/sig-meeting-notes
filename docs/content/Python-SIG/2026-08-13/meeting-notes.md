## Meeting Notes

### Attendees
- Lukas Hering (Oracle)
- Diego Hurtado (Dash0)
- Riccardo Magliocchetti (Elastic)
- Emídio (Independent)
- Shuwen Pan (Cisco)

### Agenda
- Riccardo: changing default service.name behaviour in sdk [https://github.com/open-telemetry/opentelemetry-python/issues/5544](https://github.com/open-telemetry/opentelemetry-python/issues/5544)
  - Aaron: mind the [schema version](https://opentelemetry.io/docs/specs/otel/resource/sdk/#create) for resource attributes
  - Diego, Carlos: Fair to consider this a bug
  - Also related [https://github.com/open-telemetry/opentelemetry-python/pull/5535#discussion_r3772133412](https://github.com/open-telemetry/opentelemetry-python/pull/5535#discussion_r3772133412)
  - In comparison, Java doesn’t rely on resource detection, and always uses [“unknown_service:java”](https://github.com/open-telemetry/opentelemetry-java/blob/main/sdk/common/src/main/java/io/opentelemetry/sdk/resources/Resource.java#L52); Go [directly consults the OS](https://github.com/open-telemetry/opentelemetry-go/blob/main/sdk/resource/builtin.go#L93) and else fallbacks to “unknown:go”
  - TODO Riccardo: Open an issue in semantic-conventions regardings different implementations and tag language sigs, also mention default
- Carlos: PR Dashboard, e.g. [https://github.com/open-telemetry/opentelemetry-specification/issues/5264](https://github.com/open-telemetry/opentelemetry-specification/issues/5264) for a summary. Java maintainers found this useful.
  - Emidio: how does it work with 1oo+ items?
    - Liudmila: works fine for java [https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/18435](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/18435) , Trask very responsive
  - Carlos: we should do something like [https://github.com/open-telemetry/shared-workflows/pull/238](https://github.com/open-telemetry/shared-workflows/pull/238)
  - Let’s give this a try
    - Emidio: I can volunteer to add it
- Diego: [https://cloud-native.slack.com/archives/C0AD17NMBLZ/p1786632144815569?thread_ts=1785918548.209679&cid=C0AD17NMBLZ](https://cloud-native.slack.com/archives/C0AD17NMBLZ/p1786632144815569?thread_ts=1785918548.209679&cid=C0AD17NMBLZ)
  - [https://github.com/open-telemetry/opentelemetry-packaging/pull/64](https://github.com/open-telemetry/opentelemetry-packaging/pull/64)
- Emidio: messaging instrumentations semconv `OTEL_SEMCONV_STABILITY_OPT_IN` support
  - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4727](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4727)
  - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4920](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4920/changes)
  - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4654](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4654)
  - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4268](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4268)
  - Lukas: we can add helpers in common code
    - Emidio: I can do that
  - Liudmila: 4727 reported may be interested in helping more
- Diego: [https://github.com/open-telemetry/opentelemetry-python/issues/5385](https://github.com/open-telemetry/opentelemetry-python/issues/5385)
  - Riccardo: I would like to try to get more approvers / component owners before adding more process
  - Liudmila: Marylia may have info on setting up the limit of concurrent PRs for first time contributors
    - The dashboard issue and some automation adding automatic reviews will discourage bots
    - Adding friction should not be a mean to get a better community
    - You can turn copilot on
  - Aaron: what should we do next?
    - Riccardo: We can try both automatic review and first-time contributors concurrent pr limit
    - Aaron: Consider simplifying the PR and issue templates?
- [aaron] CI issues during peak hours [https://github.com/open-telemetry/community/issues/3622](https://github.com/open-telemetry/community/issues/3622)
  - Lukas: we can run less test during PRs
    - Maybe just oldest and latest python versions in PR? I think that would reduce by ~3x
    - Also coalescing some tests
