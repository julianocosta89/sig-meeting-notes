## Meeting Notes

### Attendees
- Trask Stalnaker (Microsoft)
- Josh Suereth (Google)
- Sven Cowart (ElastiFlow)
- Rob Cowart (ElastiFlow)
- Dave Cadwallader (Oracle)
- Neil Yashinsky (Force Multiplier Labs / [ContextCore](https://contextcore.me/))
- Armin Ruech (Dynatrace)
- Joao Grassi (Dynatrace)
- Surbhi A (Cisco)
- Ruediger Schulze (IBM)
- Christophe Kamphaus

### Agenda
- Triage
  - [fix: make criticality attribute opt-in #3340 #3348](https://github.com/open-telemetry/semantic-conventions/pull/3348)
    - Josh’s questions:
      - What is the path to add non-stable attributes to stable signals?
        - Implicitly - all of these will always need to be feature-flag guarded, given stable-by-default. Can we denote what this feature-flag is in semconv?
        - Can we remember that these should be recommended once stable? is that allowed on some signals, not others?
      - Entity-Specific - what "baked in" rules policies for other signals still apply to entities? Do we need to change things based on identity / description?
- [trask, 15 min] [https://github.com/open-telemetry/semantic-conventions/pull/3343](https://github.com/open-telemetry/semantic-conventions/pull/3343)
  - Recommending event body to be used as human readable display message (if used at all)
- [trask, 5 min] [https://github.com/open-telemetry/opentelemetry-configuration/pull/520](https://github.com/open-telemetry/opentelemetry-configuration/pull/520)
  - Both options service > peer_mapping and service_peer > mapping both seem ok
- [Surbhi] Discuss unified http client network timing log record proposal here - [https://github.com/open-telemetry/semantic-conventions/issues/2827#issuecomment-3827130424](https://github.com/open-telemetry/semantic-conventions/issues/2827#issuecomment-3827130424)
- [Rob, 5 min] “official” vs “community group” semantic conventions… thinking about the line of demarcation
- [trask, 10 min] beta stability level
  - [https://github.com/open-telemetry/semantic-conventions/pull/3304#issuecomment-3835468855](https://github.com/open-telemetry/semantic-conventions/pull/3304#issuecomment-3835468855)
- [Sudarshan (Oracle)] Can this PR be triaged
  - [https://github.com/open-telemetry/semantic-conventions/pull/2989](https://github.com/open-telemetry/semantic-conventions/pull/2989)
- [suereth, 5-10 min] Updates on Stable-by-Default + Federated Semconv
  - [https://github.com/open-telemetry/opentelemetry-weaver-packages](https://github.com/open-telemetry/opentelemetry-weaver-packages) - New sharable location for policies, codegen, etc.
  - [https://github.com/open-telemetry/opentelemetry-specification/pull/4815](https://github.com/open-telemetry/opentelemetry-specification/pull/4815) - New schema publishing
