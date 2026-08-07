## Meeting Notes

### Attendees
- Aaron Abbott (Google)
- Diego Hurtado (Dash0)
- Dylan russell (Google)
- Michele Mancioppi (Dash0)
- Josh Winerman (Cisco/Splunk)
- Emídio (Independent)
- Lukas Hering (Oracle)
- Carlos Cortez (Dash0)
- Liudmila Molkova (Google)

### Agenda
- Diego PTAL [https://github.com/open-telemetry/opentelemetry-python/pull/5337](https://github.com/open-telemetry/opentelemetry-python/pull/5337)
  - [Lukas] lets wait a little more, it’s not urgent. Get more thoughts from others
  - Possibility of putting it in contrib
  - Possibility of using C++ component
  - Testing it with eBPF profiler, is a relatively new feature. Would be good to validate it.
  - Lets verify end to end before merging
- Diego please reopen [https://github.com/open-telemetry/opentelemetry-python/pull/5381](https://github.com/open-telemetry/opentelemetry-python/pull/5381)
  - Will reopen a new PR, github wont let us
- Diego [https://github.com/open-telemetry/opentelemetry-python/issues/5385](https://github.com/open-telemetry/opentelemetry-python/issues/5385)
  - Let’s chat next week when Riccardo is around
- Diego [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4883](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4883)
  - Context
    - MLFlow in an older version, it was running pip install
  - Is the point that we don’t want any dependencies in instrumentations?
  - [lukas] Can we vendor?
    - I.e. copy in the code
    - Change imports
    - More maintainable
    - [vendoring](https://github.com/pradyunsg/vendoring) package which [pypi uses](https://pip.pypa.io/en/latest/development/vendoring-policy/#automatic-vendoring)
    - Can we try [copybara](https://github.com/google/copybara) if there is no good general tool?
    - Pip uses vendoring: [https://github.com/pypa/pip/tree/main/tools](https://github.com/pypa/pip/tree/main/tools)
      - See: [https://pip.pypa.io/en/latest/development/vendoring-policy/](https://pip.pypa.io/en/latest/development/vendoring-policy/)
      - [https://pypi.org/project/vendoring/](https://pypi.org/project/vendoring/)
    - Ray uses vendoring: [https://github.com/ray-project/ray](https://github.com/ray-project/ray)
- Diego [https://cloud-native.slack.com/archives/C01PD4HUVBL/p1784533480125439](https://cloud-native.slack.com/archives/C01PD4HUVBL/p1784533480125439)
  - Can loosen the `opentelemetry-instrumentation == 0.66b0.dev`
  - For example [here](https://github.com/open-telemetry/opentelemetry-python-contrib/blob/ac3673d2c3550a52faa6d08c0ec7de66744300d6/instrumentation/opentelemetry-instrumentation-pika/pyproject.toml#L28-L29)
  - [aaron] can we just mark opentelemetry-instrumentation as 1.x and not just leave bare unconstrained dep?
    - We will need to do this for stability at some point anyway.
    - [lukas] +1 bare dep would cause problems since we import some internal versions
  - Let’s just revert the deletion of elastic for now until we have a stable instrumentation package.
- Aaron/Dylan [https://github.com/open-telemetry/opentelemetry-python/pull/5491](https://github.com/open-telemetry/opentelemetry-python/pull/5491) Ruff
- Emidio [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4842](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4842) discord.py instrumentation
  - the context here is discord.py lib maintainers are not open to instrument the code natively using opentelemetry. Contributor opened this PR to have discord.py auto-instrumentation in -contrib. What’s the guidance for new instrumentations – need at least component owner?
