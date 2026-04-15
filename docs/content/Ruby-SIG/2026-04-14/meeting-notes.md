## Meeting Notes

### Attendees
- Kayla Reopelle (New Relic)
- Hannah Ramadan (New Relic)
- Robb Kidd (Honeycomb)
- Xuan Cao
- Argun Rajappa
- Bart de Water

### Agenda
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
  - Policies otep
  - Stabilization discussion
  - [Log Processor for Span Events proposal](https://github.com/open-telemetry/opentelemetry-specification/pull/5006)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - [kayla] Reviews requested:
    - [fix: Limit length of response body read to 4mb](https://github.com/open-telemetry/opentelemetry-ruby/pull/2080)
      - Security issue with reading the whole response body.
    - [feat: Add event_name field to Logs](https://github.com/open-telemetry/opentelemetry-ruby/pull/2077)
    - [feat: bump semantic conventions to 1.38.0](https://github.com/open-telemetry/opentelemetry-ruby/pull/2058)
      - Robb proposes that we merge [the PR configuring Renovate to perform the semconv updates](https://github.com/open-telemetry/opentelemetry-ruby/pull/2056) and compare the PR it opens for 1.38.0 to this one as a bake-off for automating this work.
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - [bart] state of metrics in contrib? [feat(active-job): Add performance metrics to process span #2198](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2198)
    - Add option to opt-in
- Burning questions?
  - [xuan] [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls?q=is%3Apr+is%3Aopen+coverage](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls?q=is%3Apr+is%3Aopen+coverage)
    - One Major Theme for HTTP semconv stability code paths: Old code paths should be easy to remove when we’re ready to go Stable Only
  - [xuan] noisy labels + simplify reviewers
- **Question**: Do we want to remove the option to send raw SQL? It’ll either be obfuscated or not sent. - [PR comment](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2095#discussion_r2998738206)
- According to [spec](https://github.com/open-telemetry/semantic-conventions/blo), non-parameterized query text SHOULD NOT be collected unless sanitized. Since Trilogy's query(sql) method doesn't support parameterized queries, all queries are non-parameterized.
- **[Strict Spec] db_statement config**: :omit, :obfuscate (default: :obfuscate)
  - Spec compliant & security-by-default
- **[Current] db_statement config**: :omit, :include, :obfuscate (default: :obfuscate)
  - Flexibility for users who want raw SQL (e.g., debugging, known-safe queries)
- **Question**: How do we want to handle span names
  - According to spec, the operation name "SHOULD NOT be extracted from db.query.text" but "SHOULD NOT" allows discretion.
- ✨ Happy Reports ✨
