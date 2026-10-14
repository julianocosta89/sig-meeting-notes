SIG: Client SIG
Date: 2026-10-13
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 03:08 Hey, David.
**Jared Freeze (Palo Alto Networks)** 03:49 Lucas.
**Jason Plumb** 03:52 Hey, Jared.
Are you also with Embrace?
**Jared Freeze (Palo Alto Networks)** 04:03 Not anymore.
**Jason Plumb** 04:04 Anymore.
**Jared Freeze (Palo Alto Networks)** 04:06 Yeah. No. Yes. But we got bought by Palo Alto.
**Jason Plumb** 04:09 Right. Right. But they're keeping the brand. Right?
**Jared Freeze (Palo Alto Networks)** 04:12 No, it's gone as of last week.
**Jason Plumb** 04:15 Oh.
**Hanson Ho** 04:15 Well, I mean, we're the word embrace is still there, and product names and things are.
**Jason Plumb** 04:22 Yeah.
**Hanson Ho** 04:23 Who knows?
Being embraced by Xcore.
**Jared Freeze (Palo Alto Networks)** 04:29 Well, we do know. They said it's gonna be gone, but our library is called Embrace Web SDK. I mean, that is a mess.
**Jason Plumb** 04:36 I'm not gonna rename that, yeah.
**Jared Freeze (Palo Alto Networks)** 04:38 I mean, it's like… Hello slash browser? No, no, literally no one knows, I've asked.
You know, with no real response. So Hanson and I will probably just run with whatever we find best.
**Hanson Ho** 04:51 It's gonna be embraced until they change, you know, yeah.
The internals don't have to match the marketing.
There's so many things we've used that the internals don't match the marketing, because marketing always changes, and you can't really tag it to that, anyway.
**Jared Freeze (Palo Alto Networks)** 05:09 they don't use GitHub, which is interesting because they're security companies. So There's gotta be some pipeline between whatever they use and whatever the public sees. So.
**Jason Plumb** 05:20 Yeah.
**Hanson Ho** 05:21 They don't have SDK anything, so it's… it's, you know… Anyway.
**Jared Freeze (Palo Alto Networks)** 05:30 Interesting times.
**Jason Plumb** 05:36 I can't relate to any of that now that I'm a Cisco employee.
**Hanson Ho** 05:40 A company… a Splunk, a Cisco company.
**Jason Plumb** 05:44 Yeah, I mean, basically, basically.
SignalFX was, like, bought by Splunk, and so that story is basically, like, the group I work for is basically former SignalFX and Omniscient doing tracing and metrics, and those two companies came to Splunk, and… Splunk came into Cisco, as it happens.
**Hanson Ho** 06:06 Worked for a company where the products be the comp the bot company became remained as part of the brand, but as a product. And then another company came in and bought that, and then they turned the version number into the product name, because the version number had a lot of cachet. So, it's XI, XIR2, XIR3.
Anyway.
That's why I don't care about market names.
Cool. Okay, Martin's got a couple of topics on the, agenda… Who wants to share? I can share, someone else types.
Y'all can see this.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 06:59 Yeah.
I have, yeah, a couple of small, topics here.
of one… The first one is about the approval policy. We talked about this, I think, a couple of weeks ago, to mirror… and we… I think we agreed, to mirror the Gen AI one, which is basically… One approval is fine for just, like, chore stuff, and… For actually making changes to the conventions, like, we need two approvals, and they should be from, ideally from two different companies.
So I opened a PR to document this.
There is, one issue, though, because we currently, if I open a PR, like, the other two maintainers are in the same company, so we would need somebody else to be able to approve.
So I wanted to kind of bring that up as a… as a topic to see, like, if you want to add more maintainers or more, or some… some approve… approvers.
And if anyone was interested in… in… Be part of that, so…
**Jason Plumb** 08:14 I offered to be an approver, so if there's interest, and if that helps with that, I'm happy to be an approver.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 08:21 That would be great. Thanks, Jason.
**Jason Plumb** 08:24 I mean, this is not… definitely not… I'm not giving this the attention it deserves right now, because of a gazillion distractions and other priorities, but I'm happy to… at least I'm here, I can try and help.
**Hanson Ho** 08:37 Sure.
**Jason Plumb** 08:40 I'll put a comment on the PR, too.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 08:48 Okay.
I'll add you to the group.
**Jason Plumb** 08:52 Cool.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 08:55 Alright, and the other one… is, so I think the work that we have in progress.
Is to migrate, or to add some actual, namespaces.
I do have the browser one open.
It got some reviews. I have, I'm just waiting for.
Those are used to be done again.
After making some changes, But I think that one would make sense to go first, because it doesn't need any migration. Those… those are… don't exist in any registry right now. So, yeah, I think once it has approvals, I think I would merge this, and maybe we can test our process Hanson on it.
**Hanson Ho** 09:43 Perfect.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 09:45 And then the other ones, I've been kinda looking at what the sequence of steps would be to… To migrate those. There's actually… I saw that… I think a mainframe.
The mainframe registry recently did one.
So I was looking how they did it. If you open the… the second link.
**Hanson Ho** 10:10 you.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 10:11 Yeah, so I created this, this kind of overall issue with… that has sub-issues for the other… for the specific namespaces.
And in the description, I listed, like, the sequence of steps that would need to happen.
So I think what needs to happen is, like, so we would open… we would add them here, but we would not actually merge that PR until there is a release in Core that has those removed. So we would hold that PR.
We would also, at the same time, we would open a PR to add exclusions in the core registry that would get merged, and then once it's released, we would merge our PR and do our own release.
And then, for… if if we know of any consumers of those of those of those attributes that were migrated, we should. We should tell them. This. This applies only for for anyone like who runs weaver.
But I think, like, for… for example, like, if you moved the app or session, I think that affects Android.
So you would. We would probably need to make updates in in that Sdk.
Repo. And then, I think a follow-up step would be to do a cleanup in the core registry, like, move those attributes to deprecated.
**Hanson Ho** 11:40 Yeah, deprecated attributes are usable anyway, so it wouldn't be, you might get a warning or something like that, but they're not gonna be, you know, there aren't gonna be build breaks unless they have warnings and the warnings will trigger a build break or something like that.
So once the deprecation happens, we should soon have at least a registry out. And then in terms of artifacts, this is when we can get to… then I talk, like, about artifacts, a little later on, but yeah, seems like a reasonable process.
I would assume the… folks who are… Approve… or maintainers will have to approve the.
the specific namespace migration. So we say, hey, hey, we want to own app, and they'll say, yes, you can do that, and then we'll go ahead and do that.
Like a step zero, or something like that.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 12:33 Yeah, yeah, yeah.
Yeah. And I don't think I was looking. I don't think that the decor registry does releases very often. I think the last one was in August.
So, just something to keep in mind as well.
I don't know if you want to do them, like, one at a time, or, like, you might want to just do a bunch of them together.
**Hanson Ho** 12:59 Yeah, once we get one in, it'll be mechanical, hopefully, for the other ones, if it's just saying literally everything from the old one to the new one. Unless there are violations, because I think the old one is still in V1, so if we have to move it over, the deprecation won't necessarily just be an exact copy over of the YAML, be like… a spiritual migration, but to generate artifacts and things like that should be exactly the same, so we can at least test that.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 13:24 Okay.
**Hanson Ho** 13:27 Cool, thanks, Martin.
Cool. Okay.
My topic is artifact releases, so last week we talked about, generating artifacts and pinning it to specific versions that we release. Every time we release, we generate some artifacts. Talk to folks over on the Semantic Conventions.
Slack. And there's apparently an effort going on to standardize this type of generation. I haven't looked at the repo in the detail, but the idea is that there'll be shared templates that could be used, shared infra to actually say, hey.
for this language, you can generate these things and done in a common way. So if that's the case, I haven't looked at the details and what the artifacts are, how you do it. It's either running it from our repo or running it from a core repo, but… there is going to be a standardized way of doing this, without us having to, like, give it a new process, which is good. Or templates, in the case of the Markdown stuff.
So, I was gonna take some time last week to look at this. I didn't have time, so I'll look at it this week. But the idea is that we can do our releases, but just skip the artifact generation part. So just when we release 0.10 dev, containing the four browser, attributes.
That will live as a release for the registry. So you can consume it, that'll live on forever, but there will be no associated artifacts with it.
Until that stuff is settled. So, is that cool with folks? So for now, you want to consume this… consume it via the Weaver. Eventually, there'll be a lower friction way of doing this, and we could.
See what infra is needed to do that.
I think they'll also accept, language templates, so if we want to have Kotlin or JavaScript or TypeScript templates, uploaded to the core place, we can do that.
And that's not to say repos individually can't have their own custom templates that do more. It's just that there will be, like, you know, a canonical you know, place where people can just reference artifacts rather than registries, and have to generate them.
Cool.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 15:51 Sounds good.
**Hanson Ho** 15:57 I will… Add Jason.
to the approvers list.
**Jason Plumb** 16:04 Cool, I just submitted a PR with the README update.
**Hanson Ho** 16:08 Oh, perfect. There you go.
Just have to approve it and merge it.
Any other topics?
**Jared Freeze (Palo Alto Networks)** 16:24 I was just gonna say, it's nice to hear that there's some standardization going on, because I feel like the… PR that we saw in our vendor SDK was, like, very complicated.
Like, very, very many files. So it'd be nice to have generation be a little bit more streamlined. I don't know if it's gonna be a library or something, but…
**Hanson Ho** 16:46 Well, library is Weaver. I think the PRs, having to set up the templates, is one. If we want to add validation and tests, that's another. So it's almost like the Hello World looks very similar in terms of size as, like, one that adds 10 different attributes, so yeah.
The setup… the initial setup one is going to be a little bit of something, but… Eventually, hopefully, it will be easier.
If you don't need custom templates, I should say.
**Jason Plumb** 17:18 Since the agenda is a little bit light, I will bring up a topic.
So is anyone on the call or do you think is anyone going to KubeCon in Salt Lake City in November?
The reason I ask is because what we've done in other SIGs in the past, is to try and hold an in-person, like, SIG meeting if there's enough interest that usually pulls in a few people from the community that are, like, interested in open telemetry, that are like, oh, I didn't know, like, I care about client stuff, you know, that might be… interesting topics that fall out of that. We did one a few years ago, thinking we might do one again, but it sounds like no one's gonna be there except for me. I mean, no one on this call, anyway.
All right.
**Jared Freeze (Palo Alto Networks)** 18:11 Yeah. We wanted to go. It it's actually our very first in person.
Like, non-remote week.
With the new company, so…
**Jason Plumb** 18:19 Oh, yeah, okay.
**Jared Freeze (Palo Alto Networks)** 18:21 It's exactly the same days.
**Hanson Ho** 18:24 It's also Remembrance Day, so.
**Jason Plumb** 18:30 Yeah, I think we have Veterans Day in the US on one of the days of KubeCon.
Okay, cool. Well, we don't have to drag it out anymore. I just thought I'd ask in case there was momentum and there isn't, which is fine.
**Hanson Ho** 18:43 Were there a lot of other SIGs that had people who usually go, but no one's going this time?
**Jason Plumb** 18:51 I mean, the collector is always super busy, and I think the eBPF and GO thing last time was, like, pretty jumpin'.
Yeah.
But no worries, and no FOMO, it's fine.
**Hanson Ho** 19:07 Yeah.
Then take my talk, so I can go.
Or is that the one I forgot to submit? I forgot which one.
**Jason Plumb** 19:16 It is what it is.
**Hanson Ho** 19:17 this.
**Jason Plumb** 19:18 And they didn't accept the talk you didn't submit?
**Hanson Ho** 19:21 Yeah. No, no, well, it's one of the others.
**Jason Plumb** 19:25 Well, yeah, the, the EU1 RFC closed Sunday, and then they'll have Observability Day open soon, if it's not already?
Which is in Barcelona.
**Hanson Ho** 19:43 Cool.
Any other topics? We'll get to the reviews.
soon. Looking forward to releasing 0.1. No one has done a, release yet, and I said we'd be guinea pigs, so, let's do it.
**Jared Freeze (Palo Alto Networks)** 20:03 I do have one question. That URL that goes to opentelemetry.io.
Has no actual target? What is the reasoning for that?
Like there's a registry URL that's like part of like the schema URL or I think, but it doesn't like there's no actual like landing page for it. Is that it's just representative? Is that the idea?
**Hanson Ho** 20:28 Yeah, so the schema URL is actually just a key that they use URL. In fact, the scheme is not even part of the URL, or part of the key. It's just that you could have that domain registry, so that you can claim ownership of that.
And then everything else is arbitrary. What's important is the, version and the, suffix, whether it's dev or not, and then, you know, who owns it. Everything in the middle is like, yeah, whatever, just make it… make it consistent.
So yeah, it doesn't have to necessarily be a web page.
**Jared Freeze (Palo Alto Networks)** 21:04 Well, if… I mean, if we follow the standard, it might be nice, actually, to have that be part of generation.
**Hanson Ho** 21:09 Yeah.
**Jared Freeze (Palo Alto Networks)** 21:09 To, like, have docs, I mean… I don't know if that's too much work, but… It looks like a URL, so, you know, when you open it and it doesn't go anywhere, you're like… Where are the keys? What kind of schema is this?
**Hanson Ho** 21:24 We're.
**Jared Freeze (Palo Alto Networks)** 21:24 these guys, you know.
**Hanson Ho** 21:26 That's a good point.
**Jared Freeze (Palo Alto Networks)** 21:30 Cool. I was just confused.
**Hanson Ho** 21:33 Alrighty.
Any other topics?
Get a little bit of time back.
**Jared Freeze (Palo Alto Networks)** 21:45 Cool. Thanks all.
**Jason Plumb** 21:47 Bye, everyone.
