## Meeting Notes

### Attendees
- Pablo Baeyens (Datadog)
- Dmitry Anoshin (Splunk)
- Braydon Kains (Google)

### Agenda
- [Pablo] Failing checks on [https://github.com/open-telemetry/semantic-conventions/pull/3758](https://github.com/open-telemetry/semantic-conventions/pull/3758)
  - Affected attributes
    - [disk.io](http://disk.io).direction
      - Used by container metrics [https://github.com/open-telemetry/semantic-conventions/blob/942f03f7da57f3f7d7a14607aaee8183f0c71326/docs/system/container-metrics.md?plain=1#L222](https://github.com/open-telemetry/semantic-conventions/blob/942f03f7da57f3f7d7a14607aaee8183f0c71326/docs/system/container-metrics.md?plain=1#L222) (metric inspired by system metric)
    - network.io.direction
      - Used in k8s metrics: [https://github.com/open-telemetry/semantic-conventions/blob/942f03f7da57f3f7d7a14607aaee8183f0c71326/docs/non-normative/k8s-migration.md?plain=1#L95](https://github.com/open-telemetry/semantic-conventions/blob/942f03f7da57f3f7d7a14607aaee8183f0c71326/docs/non-normative/k8s-migration.md?plain=1#L95)
      - And hardware GPU [https://github.com/open-telemetry/semantic-conventions/blob/942f03f7da57f3f7d7a14607aaee8183f0c71326/docs/hardware/gpu.md?plain=1#L52](https://github.com/open-telemetry/semantic-conventions/blob/942f03f7da57f3f7d7a14607aaee8183f0c71326/docs/hardware/gpu.md?plain=1#L52)
    - System.paging.fault.type
      - Use by container metrics [https://github.com/open-telemetry/semantic-conventions/blob/942f03f7da57f3f7d7a14607aaee8183f0c71326/docs/system/container-metrics.md?plain=1#L222](https://github.com/open-telemetry/semantic-conventions/blob/942f03f7da57f3f7d7a14607aaee8183f0c71326/docs/system/container-metrics.md?plain=1#L222) (metric inspired by system metric)
  - What to do
    - Talk next week to confirm if [network.io](http://network.io).direction was
