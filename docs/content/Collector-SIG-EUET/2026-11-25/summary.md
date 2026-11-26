## Key Topics
- **Telemetry resource leaks with partial config reload:** Mikołaj Świątek reported that SDK caches for loggers and meter providers grow per created component when scope attributes are set. Logger fix is simple. Metrics fix needs a complex workaround the auto Collector already uses. Traces are unverified. Jade Guiton wants this resolved before the new pipeline telemetry feature gate reaches beta.
- **PRs needing attention:** Pablo Baeyens noted a PR removing deprecated components and a PR marking the OTLP receiver as beta. Both links are in the meeting notes.
- **PostgreSQL receiver proposal:** Igor Peschinskii proposed a new scraper to emit table schema, index, and primary key metadata from the system catalog without extra permissions. The component has no co-owner present.
- **Stable feature gate removal:** Vibhanshu Singh asked for review of a PR removing stable feature gates, which missed its scheduled 0.166.0 release. Pablo said it looks reasonable and will review after the call.
- **New metric model contribution:** Vibhanshu wants to help maintain the core metric model work with Dimitri and become a code owner. Pablo asked for a PR listing reviewed areas.

## Action Items
- Pablo Baeyens: review the stable feature gate removal PR after the call.
- Pablo Baeyens: keep the PR links open until next week.
- Jade Guiton: review the resource leak issue and assess whether it blocks the feature gate beta.
- Mikołaj Świątek: continue the discussion asynchronously on the resource leak issues, which he has already filed.
- Vibhanshu Singh: open a PR to become a code owner, listing reviewed areas.
- Igor Peschinskii: find a PostgreSQL receiver code owner to review the new scraper proposal.

## Participants
Pablo Baeyens, Mikołaj Świątek, Jade Guiton, Igor Peschinskii, Vibhanshu Singh, Evan Bradley, Jan Korona
