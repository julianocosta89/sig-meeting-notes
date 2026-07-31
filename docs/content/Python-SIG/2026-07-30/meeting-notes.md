## Meeting Notes

### Attendees
- Aaron Abbott (Google)
- Tammy Baylis (SolarWinds)
- Diego Hurtado [ocelotl](Dash0)
- Liudmila Molkova (Google)
- Dylan russell (google)
- Lukas Hering (Oracle)
- Keith Decker (Cisco/Splunk)
- Pablo Collins (Cisco)
- Josh Winerman (Cisco/Splunk)

### Agenda
- [aaron] complex attributes [https://github.com/open-telemetry/opentelemetry-python/pull/5266/](https://github.com/open-telemetry/opentelemetry-python/pull/5266/)
  - [Mike's comment](https://github.com/open-telemetry/opentelemetry-python/pull/5266#discussion_r3376099968) about if it’s a breaking change
  - Follow up to see what other languages did
  - Note instrumentations don’t set complex attributes yet so should be a noop at first
- [liudmila] Ok to remove and deprecate genai packages in contrib?
  - 4 of them were never release from contrib, just delete them and leave README tombstone
  - 4 that have releases (OpenAI, google-genai, vertex)
    - Vertex didn’t move but original package is deprecated. Let’s deprecate instrumentation?
    - Google-genai we moved to new repo and didn’t change package name. Changed version.
    - OpenAI and OpenAI agents, add `@deprecated` , update readmes and do release?
- [dylan] [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4896#discussion_r3675716277](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4896#discussion_r3675716277) –
  - I think we can use a unpinned version specifier for the google-genai packages if we want them available to bootstrap (similar to what the PR did). Wouldn’t require manual maintenance every time.
  - There’s also [https://github.com/open-telemetry/opentelemetry-python-contrib/blob/main/opentelemetry-contrib-instrumentations/pyproject.toml](https://github.com/open-telemetry/opentelemetry-python-contrib/blob/main/opentelemetry-contrib-instrumentations/pyproject.toml)
