## Meeting Notes

### Attendees
- Ted Young (Grafana Labs)
- [Csaba Györgyi](mailto:csaba.gyorgyi@canonical.com) (Canonical)
- Nikola Grcevski (Grafana)
- Jerry Leung (Solarwinds)
- Michele Mancioppi (Dash0)
- Damien Mathieu (Elastic)
- Denys Sedchenko (Grafana Labs)
- Sina P (Canonical)

### Agenda
- [Jerry] Container images infra [https://github.com/open-telemetry/opentelemetry-packaging/issues/87](https://github.com/open-telemetry/opentelemetry-packaging/issues/87)  - This is the current repo of the autoinstrumentation-php [https://github.com/opentelemetry-php/autoinstrumentation-php](https://github.com/opentelemetry-php/autoinstrumentation-php)
  - Jerry and Michele to design the injector contract
- [Damien] Setup homebrew package (with ocb as a start)
  - POC: [https://github.com/dmathieu/homebrew-ocb](https://github.com/dmathieu/homebrew-ocb)
  - Issue: [https://github.com/open-telemetry/community/issues/3344](https://github.com/open-telemetry/community/issues/3344)
  - Damien to work with Michele for the migration of the existing repo under OpenTelemetry
- [Ted] [Netlify for DNS and blob storage?](https://github.com/open-telemetry/community/issues/3641#issuecomment-5671068490)
  - We are already using Netlify to manage [opentelemetry.io](http://opentelemetry.io)
    - Managing DNS for [packages.opentelemetry.io](http://packages.opentelemetry.io) in the same place makes sense
  - Blob storage does not look fit-for-purpose
    - Not S3 compatible
    - Charges for egress
  - Let’s go ahead and set up an account with Cloudflare
    - Maybe we can get some kind of OSS discount
    - Transfer credentials to the right place after we have set the account up as a SIG
- [Csaba] Ubuntu vs Debian
  - Canonical does not want to take over the upstreaming in Debian, so somebody else should do it
- [Denys] Credentials & accounts for OBS, COPR and blob storage.
