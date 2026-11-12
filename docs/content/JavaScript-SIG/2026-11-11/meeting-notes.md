## Meeting Notes

### Attendees
- Marc Pichler (Dynatrace)
- Trent Mick (Elastic)
- Jackson Weber (Microsoft)

### Agenda
- Feel free to add your topics below ↙️ 🙂
- [marc] Security Advisories:
  - [https://github.com/open-telemetry/opentelemetry-js/security/advisories/GHSA-qrww-3xmv-qhgm](https://github.com/open-telemetry/opentelemetry-js/security/advisories/GHSA-qrww-3xmv-qhgm)
    - Fixed on v3.x and fix was backported to v2.x
  - [https://github.com/open-telemetry/opentelemetry-js/security/advisories/GHSA-3v2p-hm54-8qcq](https://github.com/open-telemetry/opentelemetry-js/security/advisories/GHSA-3v2p-hm54-8qcq)
    - was fixed a while ago already, advisory is out now.
- [trent] ConfigProvider PR is approved: [https://github.com/open-telemetry/opentelemetry-js/pull/6868](https://github.com/open-telemetry/opentelemetry-js/pull/6868) PTAL. I’d be interested in a sanity check (or just awareness) with other approvers/maintainers. This adds a `api-config` package.
- [trent] ComponentProvider PoC: [https://github.com/open-telemetry/opentelemetry-js/pull/7269](https://github.com/open-telemetry/opentelemetry-js/pull/7269)  PTAL, esp.  Marc if this looks reasonable. This is now defining a ComponentProvider to be a *function*.  The current diff ends up being very small, which is nice.
- [trent] Advisories: Consider handling fixes for any advisory that is lower than "High" in public. Or meh. Mention the curl policy.
