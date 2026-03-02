## Meeting Notes

### Attendees
              - Riccardo Magliocchetti (Elastic)
              - Emídio (PicPay)
              - Tammy Baylis (SolarWinds)
              - Leighton Chen (Microsoft)
              - Dan Gomez Blanco (New Relic)
              - Ezzio Moreira (PicPay)

### Agenda
              - Riccardo: Drop instrumentation for boto? No release since 7 years
              - General agreement, create an issue to see if anyone is still using it
              - Issue created https://github.com/open-telemetry/opentelemetry-python-contrib/issues/3588
              - Riccardo: Will contribute a basic OpAMP client implementation in the following weeks:
              - Sketch of integration with some notes https://github.com/open-telemetry/opentelemetry-python/pull/4646
              - OpAMP agent need to get the computed Resource to identify itself to the server
              - No concept of a config and making the sdk dynamic yet
              - Protocol specs https://opentelemetry.io/docs/specs/opamp/
              - Emidio: about Protobuf 6 – https://github.com/open-telemetry/opentelemetry-python/pull/4643
              - Protobuf 6-7 rolling window compatibility
              - Try relax dependency and see if both works with the same proto?
              - Long term: more than one exporter version?
              - Current protobuf downloads https://pepy.tech/projects/protobuf?timeRange=threeMonths&category=version&includeCIDownloads=true&granularity=monthly&viewType=line&versions=6.31.1%2C6.31.0%2C6.31.0rc2%2C5.29.5%2C5.29.4
