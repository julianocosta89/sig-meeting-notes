## Meeting Notes

### Attendees
- Vitor Vasconcellos
- Tiffany Hrabusa (Grafana Labs)
- Jay Deluca (Grafana Labs)
- Sophie (Elastic)

### Agenda
- [Tiffany] dependabot PRs - could someone more knowledgeable than me take a look and merge? After the latest supply chain attack, I’m afraid to touch them.
  - Maybe we should add a gate based on how old the release is - like the bot PR can’t be opened until the release is at least 7 days old
    - If we move to using renovate, [here is how it can be done](https://github.com/open-telemetry/opentelemetry-ecosystem-explorer/blob/main/.github/renovate.json5#L4)
  - Tiffany will create an issue
- [Jay] Inform - For anyone interested in keeping  up with the explorer proj, going to be posting regular updates in [slack](https://cloud-native.slack.com/archives/C09N6DDGSPQ/p1778332229914279)
- [Tiffany] We should ask Tyler Helmuth if we can use or repurpose his AI open source etiquette talk
  - [Lightning Talk: How To Responsibly and Effectively Contribute To Open Source Using... Tyler Helmuth](https://www.youtube.com/watch?v=hBiJ5ZQDVds)
  - Sophie will ask Tyler and get the ball rolling.
- [Vitor] Take a look at Explorer front end redesign: [https://github.com/open-telemetry/opentelemetry-ecosystem-explorer/issues/84#issuecomment-4373694983](https://github.com/open-telemetry/opentelemetry-ecosystem-explorer/issues/84#issuecomment-4373694983)
  - [Jay] Making these changes while the site is actively being built might be difficult, but the design choices are great and it’s definitely the right direction
