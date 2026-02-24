## Meeting Notes

### Attendees
- Patrice Chalin (CNCF)
- Tiffany Hrabusa (Grafana Labs)
- Vitor Vasconcellos (Mercado Libre)
- Leandro Caracciolo (OllyGarden)
- Severin Neumann (Causely)
- Marylia Gutierrez (Grafana Labs)
- Kasper Nissen (dash0)
- Diana Todea (VictoriaMetrics)

### Agenda
- [Patrice/Fabri] [draft: home page copy changes #9141](https://github.com/open-telemetry/opentelemetry.io/pull/9141)
  - Severin added the tag line topic to the GC agenda and Marylia or Juraci will make sure it’s discussed
  - More discussion is required for some of the parts
  - Might be best to break up the PR into smaller ones - Does Fabri have time to do this?
- [Tiffany] How can we help localization teams who want to organize their work? At OTel Unplugged, a few people requested the ability to edit Issue descriptions. Is that possible? If not, are there other ways we can help them?
  - [Severin] I think we can fix this by giving them “write” permissions on the repo (aka “approvers” in the definition of the admin repo, draft PR: [https://github.com/open-telemetry/admin/pull/567](https://github.com/open-telemetry/admin/pull/567))
  - [Patrice] we could have separate repos for languages so that localization teams can manage their own permissions
    - [Severin] How do we keep those repos in sync? Do we need a Hugo submodule like the spec?
  - [Patrice] meta issues for drifted pages - maybe instead, the language contributors recreate the issues from their own account so they can edit them
  - [Tiffany] can a contributor without a defined role still edit issues?
    - [Severin] the localization teams should be growing their own teams, so if contributors are consistently working on the project, promote them; these teams should be more self-sustaining
    - [Severin] do localization teams have the power to add approvers to their own team?
  - [Patrice] github bot like /assign might be a way to open things up without adding actual permissions
  - [Severin] we want the localization teams to be as independent as possible
    - Proposal: we are open to the localization team taking control of the workflow, but they need to do the heavy lifting - they will need to enable the bot or set up the repo
      - [Patrice] but if they choose a new repo, Comms will have to coordinate
      - [Marylia] a separate repo just creates the same problems and adds complexity
        - [Patrice] one repo per local would create an independent silo
          - Our current set up is not bad and a bot would help to expand our current capabilities
  - [Diana] each local is very different, and the human factor is very important: should we seek out one locale to try out the new workflow?
    - [Severin] issue for language approvers (only) who want to figure out how to work through it
    - [Diana] smaller localization teams will be burdened if they have to experiment
  - [Severin] we don’t want to block the localization teams, but we need drivers from the locales.
  - **Summary**: **Separate repos are too cumbersome for right now, given other priorities of maintainers. The preference is to keep one repo and explore the bot mechanism to help organize workflows.**
    - [Severin] will look into it and create issue for locale approvers
- [Diana] clarifying QQs on triager role- focused on the entire [repo](https://github.com/open-telemetry/opentelemetry.io/issues)?
  - [Severin], yes, across the repo. When you read an issue/PR and you’re not comfortable with the content, don’t comment about the tech, but you can copy edit the text and tag the SME groups for the tech/language
  - [Tiffany] checking issues to see if they are well scoped and if not, asking questions in the issue to get more information for whoever is going to resolve it.
  - [https://opentelemetry.io/docs/contributing/sig-practices/#triage](https://opentelemetry.io/docs/contributing/sig-practices/#triage)
- [Leandro] Social media covers with the same visual identity as the website.
  - [https://cloud-native.slack.com/files/U01V5PFBBAQ/F0ADSFYKGNB/linkedin_cover.png](https://cloud-native.slack.com/files/U01V5PFBBAQ/F0ADSFYKGNB/linkedin_cover.png)
  - [https://cloud-native.slack.com/files/U01V5PFBBAQ/F0AEBHHECQ4/youtube_cover.png](https://cloud-native.slack.com/files/U01V5PFBBAQ/F0AEBHHECQ4/youtube_cover.png)
  - [Leandro] to raise an issue in the Comms repo so we have the images in the repo
    - [Patrice] or someone else who knows Hugo/Docsy can add the images so they are available for different sections
    - [Severin] raising issues is good practice so your contributions get counted in the traditional way
