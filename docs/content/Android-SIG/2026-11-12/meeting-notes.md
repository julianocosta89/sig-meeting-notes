## Meeting Notes

### Attendees
- Jason (at kubecon, can’t attend SIG sorry!)
- Vishwan (Grafana)
- Ben (Grafana)
- Jason Morris

### Agenda
- Jason - Contribfest went great! We had at least 10+ folks contribute their first PR to OTel. Unfortunately, none of them were for Android. 😭I’ll do a sweep of those next week, will remove the label and commit small PRs for them.
- Jason - In the DSL, AnrReporterConfiguration and CrashReporterConfiguration both implement WithEventAttributes<T>, which exposes a public addAttributesExtractor(), but the EventAttributesExtractor interface isn’t accessible (lives in common-api). Is there a problem here? If yes, I can open an issue.
