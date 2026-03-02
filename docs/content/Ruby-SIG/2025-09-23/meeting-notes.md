## Meeting Notes

### Attendees
- Ariel Valentin (GitHub)
- Wendy Smoak
- Arjun Rajappa
- Eric Mustin (Elastic)
- Hannah Ramadan

### Agenda
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - (arielvalentin) ​​Ruby 3.1 && 3.2 EoL
    - Make an Issue to document work to be done (bump min rubies version in gemspecs, bump rubocop to match ruby version compatibility)
    - Update Changlog or give notice in some way
  - (the whole gang) Metrics+Trace+log sdks all are spinning up background threads, is that problematic, are there configuration options that ought to be available to allow end-users to choose limits/options around this behavior?
    - Next steps: look into what other language sigs are doing that are similar to ruby (python, etc)
  - (arielvalentin) Can we introduce automation to keep protos up to date?
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - (arielvalentin) Rails 8 Events, Job Continuations Etc… [https://rubyonrails.org/2025/9/4/rails-8-1-beta-1](https://rubyonrails.org/2025/9/4/rails-8-1-beta-1)
    - Open questions on impact on our log bridges and instrumentations
- Burning questions?
- ✨ Happy Reports ✨
