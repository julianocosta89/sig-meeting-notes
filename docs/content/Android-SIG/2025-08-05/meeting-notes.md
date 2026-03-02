## Meeting Notes

### Attendees
- Jason (Splunk)
- Hanson Ho (Embrace)
- Jairo (honeycomb)
- Jamie Lynch (Embrace)
- Mustafa Haddara (honeycomb)
- cleverchuk(solarwinds)

### Agenda
- KSP work is ongoing
  - Likely going to need a change to the build-time steps that take @AutoService -> meta-inf service loader files.
  - Kapt is in maintenance mode, so switching seems smart
- Jason: Always looking for help reviewing PRs. Thanks!
- Hanson: Kotlin API update
  - Embrace shipped an SDK version that uses (internally) the API and Java-API adapters to prove it out in production
  - [https://github.com/embrace-io/opentelemetry-kotlin](https://github.com/embrace-io/opentelemetry-kotlin)
  - Long term goal is to support KMP (kotlin multi-platform)
- uninstall/shutdown
  - Still need services
  - Still need a
- AI: Jason to create tracking issue for all the instrumentation uninstall() [https://github.com/open-telemetry/opentelemetry-android/pull/1109](https://github.com/open-telemetry/opentelemetry-android/pull/1109)
- AI: Hanson to create issue in java-contrib to take disk buffering to beta
- AI: Jason to file issue on contrib because the published artifacts all have -alpha even when it’s listed as beta/stable in the main [README.md](http://README.md)
  - [https://github.com/open-telemetry/opentelemetry-java-contrib/issues/2078](https://github.com/open-telemetry/opentelemetry-java-contrib/issues/2078)
