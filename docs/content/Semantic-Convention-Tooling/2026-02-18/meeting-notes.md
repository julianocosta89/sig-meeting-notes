## Meeting Notes

### Attendees
- Jeremy Blythe
- Liudmila Molkova
- Arianna Vespri
- Neil Yashinsky

### Agenda
- [josh/liudmila] Backwards compatibility story - [https://github.com/open-telemetry/weaver/pull/1202](https://github.com/open-telemetry/weaver/pull/1202)
  - Start looking at weaver 1.0 when v2 schema stabilizes
  - Keep compatibility with schema v1 for now, use –future to turn warnings into errors.
- Minor Tangent - Look at using a copilot script/playbook for fixing renovate PRs.
- [josh] Weaver Packages -
  - Any remaining blockers on [https://github.com/open-telemetry/weaver/pull/1166](https://github.com/open-telemetry/weaver/pull/1166)?
  - Next steps - How to have special treatment for [https://github.com/open-telemetry/opentelemetry-weaver-packages](https://github.com/open-telemetry/opentelemetry-weaver-packages)
    - hardcode in `VirtualDirectoryRef` ?
    - Something like `weaver check -p pkg:check/stability` or `weaver check -p pkg://policies/check/stability`
    - Should we just defer this for now.
- Minor Tangent - Look into bundling renovate PRs.
- [josh] Build Change discussions
  - We're in ok shape for now
  - Let's merge the PR to migrate to [React.js](http://React.js), then sort out next steps.
- [josh] Git Ref PR - [https://github.com/open-telemetry/weaver/pull/1201](https://github.com/open-telemetry/weaver/pull/1201)
  - Renovate support?
  - (Can we have by-hash, but also have tags, similar to docker-hash-tagging?)
  - Using git ref is more elegant, but achieves same thing.
  - Move xtask to refspec.
- [liudmila] call for review - [https://github.com/open-telemetry/weaver/pull/1154](https://github.com/open-telemetry/weaver/pull/1154)
- [josh] Comments on `weaver registry json-schema` and default output for `weaver registry resolve`
  - `weaver registry package` - will package the directory that will be published.
  - Will we need `resolve`?
    - Deprecate resolve?
    - Add a flag (for now) to output resolved schema (not forge)
