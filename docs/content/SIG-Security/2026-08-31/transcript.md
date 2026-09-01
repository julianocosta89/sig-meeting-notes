SIG: SIG Security
Date: 2026-08-31
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Reiley Yang (Microsoft Corporation)** 01:44 Hey, Trask.
Morning.
**Trask Stalnaker (Microsoft Corporation)** 01:47 Morning…
**Reiley Yang (Microsoft Corporation)** 02:02 Ms. Saskway?
**Trask Stalnaker (Microsoft Corporation)** 02:04 Yeah.
**Reiley Yang (Microsoft Corporation)** 02:06 Yeah, so, Thanks for your review on the previous PR. I think the README file looks cleaner. No, I… I'm… I'm working on this, like, SLA level, as we defined, ranging from there's no promise to Some, like, region numbers.
And I'll try to get a PR this week.
So that's the only thing I'm focusing on. And by the way, I saw some folks discussed about the the Rust issue, like, a week ago. It's a supply chain.
attack from North Korea.
Not sure if you heard about that.
**Trask Stalnaker (Microsoft Corporation)** 02:42 Oh, I think I saw you shared… yeah, you shared it.
**Reiley Yang (Microsoft Corporation)** 02:45 Yeah, so in case you haven't seen, just letting you know.
Yeah.
**Trask Stalnaker (Microsoft Corporation)** 02:50 Oof.
**Reiley Yang (Microsoft Corporation)** 02:53 Yeah, so I'm spreading things, trying to make some progress there, but I don't expect myself to have a lot of bandwidth.
**Trask Stalnaker (Microsoft Corporation)** 03:03 Oh, is there stuff that we need to… Deal with related to that attack?
**Reiley Yang (Microsoft Corporation)** 03:08 No, no, so, so I'm, I had a discussion with the TC, because there's a situation, which is not weird to me, but maybe weird for some of the maintainers, and I plan to capture that in the PR, so I can talk to the maintainers in the SPAC maintainer call.
So what happened is, there are folks reading, reaching out to the C++ maintainer, saying, hey, in the contribute repo, you have a library which hasn't been maintained for a while.
And we noticed, like, the… the… the owner who's listed on that component, but we were not able to, get, like, hear back from them. So, what we decided, we're going to open a security advisory there.
So they opened the security advisory, and the maintainer is saying, we have no idea about this contribute library, what should we do? And we're not ready to just go and fix that contribute, because we don't even have very deep knowledge there. So I… I shared my perspective. I'm saying, like, if you're the repo.
owner, maintainer, you should make sure, like, you have the process and rules there. Like, if people want to shove some random components without giving any, like, showing any accountability.
Okay, then that's been to… like, doing that repository's reputation, so you need to define some rule. Either you will absorb it, or you need to kick this out. Then the question is, hey, this component has been existing for a couple years, then should we, like, do we even have the power to… shift deleted.
My point is, you should make sure you do proper communication and get rid of the component if, either way, you don't think you will be able to maintain that.
they need better direct places, so that's my position. But I… I think, like, when the TC… when I share that, it's for understanding.
No objection.
this has… However, being bounced…
**Trask Stalnaker (Microsoft Corporation)** 05:14 Oh, we're losing every other word, or I am,
**Jonathon Klobucar** 05:18 Oh, same year.
**Reiley Yang (Microsoft Corporation)** 05:21 Or communicate broadly. I haven't seen a lot of people. I need to capture, you know, dog and get broader running. Sorry, my network seemed lost to you.
**Trask Stalnaker (Microsoft Corporation)** 05:29 Yeah, we got about every other word there.
**Jonathon Klobucar** 05:35 You might want to just try audio only.
**Reiley Yang (Microsoft Corporation)** 05:41 Is that me, or… I mean, I seem to have…
**Jonathon Klobucar** 05:44 Trask and I both couldn't hear you.
I see.
**Reiley Yang (Microsoft Corporation)** 05:48 I see. Okay, so I'll… I'll turn on my view. Then I'll stop my sharing as well.
**Trask Stalnaker (Microsoft Corporation)** 05:57 Yeah, it's a… I'm glad y'all are having that discussion in the TC, because, I agree that the… I mean, obviously we can't… You know, have… Things that are unmaintained, And have vulnerabilities.
And… I think the key is just, as you said, communi… like, what's the process for communicating that? Because I know there… there was some… pushed back recently, and the Python contrib dropped a component.
And… You know, that caused some downstream issues for people.
**Reiley Yang (Microsoft Corporation)** 06:41 Yup.
**Trask Stalnaker (Microsoft Corporation)** 06:42 and so, you know, I don't know what that… Communication should… needs to look like, but… I think that would at least help, cover our bases as far as, you know.
Hey, here's a time window that the community can Speak up if this is gonna cause problems for them, and come in and, you know, volunteer to take it over.
**Reiley Yang (Microsoft Corporation)** 07:11 Yeah, trust, I feel some of this, like, I do have my opinions and position there, but I also feel that some of this… are not within the security scope. So I'll just briefly talk through what I'm thinking. So first, I think for the users, when they see OpenTelemetry, normally they don't understand the details, they see OpenTelemetry as a whole.
So, they would think, if I'm using this OpenTelemetry Python ICK, I'm picking this plugin, both of them should be handled by the OpenTelemetry community. What they didn't know is there might be an OpenTelemetry Python flask, some, like, XYZ plugin that's owned by some individual.
And if that individual ever decided, I don't want to work on this anymore, and we couldn't figure out who want to work on that for a period of time, let's say, like, 6 months, then the only viable option is we need to communicate that we're dropping this component, because we won't be able to maintain it. Having it there will confuse more folks. But for these customers, they… they will be, like, they might be disappointed because they had the impression before. So, I do feel like for each component we're shaping, we need to define the bar and maybe categorize them. So instead of, like, people trying to figure out individual components, they're trying to say, these are the… the component that OpenTime should officially put its reputation on. These are the contributors.
**Trask Stalnaker (Microsoft Corporation)** 08:32 Yeah.
**Reiley Yang (Microsoft Corporation)** 08:33 OpenTelemetry, like, different tiers, and… and we probably need to be, like, very vocal about the… the tiers, like, contribute. In my opinion, a lot of contribute reports are third-party integration or, like, instrumentation that in open telemetry community, we don't expect like, average maintainers to have that domain-specific knowledge. Let's say if you have, like, a database-specific thing that targets a specific database that nobody else has, expertise, then it would be unfair if we try to put that at the same bar.
salt.
This is number one. I think open telemetry should communicate what's the core set of components that the community would share the responsibility, and what are the additional things, like the like, if you look at the Linux kernel, it's like, there's a kernel and set of tools. Then there's, like, vendor-specific drivers, and vendor-specific drivers, Linus will say.
I don't care about this, like, if… if you don't maintain that, then I'm… I'm not going to include that. So.
We probably need to have that, like, cut out.
And the second thing is for the business continuity, I think we never talk about this, like, I remember in OpenTelemetry.net, the situation is there's a mass transit, like, component, then the owner came, and they're very active. But the problem, now I'm thinking, there's only one owner. If that owner is on vacation, there's a security vulnerability, or… If the owner is on vacation for 3 months, nobody heard about, like, anything from them, then what do you do? So do you think, for each component, we need to require maybe, like, 3 maintainers to be able to start that product. If this is a super passionate individual coming to your SIG saying, I want to handle this, and the perfect fit.
But we're literally saying we'll release a component and let people have this assumption that this will be taken care of, but we rely on a single individual. Do you think that's an issue or not?
**Trask Stalnaker (Microsoft Corporation)** 10:36 Yeah, I mean, I can show what we've done in… in the Java… I mean, obviously, we have the Java Instrumentation repo, which is, all the… most of the instrumentations are there, and that one actually is fully backed by the maintainers.
So we don't have component owners there.
But we do have a contribib rep repo also, which is for random contribib components, and that does have… Owners, and we do require two owners to, Over there.
And if it falls to one, then, you know, we… Put out the call and require another one.
I… I mean, it's hard for me to say from a… from a vulnerability, from a security perspective.
For some repos, like, for the Java like, the… I… I don't… See that as necessarily, like, kicking… they… even in Contrib, like, if it's a… We just haven't gotten security vulnerabilities, in the contribib rep repo other than… transitive CBEs, which are just version bumps.
**Reiley Yang (Microsoft Corporation)** 12:03 Those are easy, like, anyone can do it, even Bob can do it.
**Trask Stalnaker (Microsoft Corporation)** 12:06 I feel like the contrib… the collector contribib is the biggest… problem… Because those components can have… like, they've got auth authentication components over there, and those things can have bugs, vulnerabilities in the… in our code itself.
And so… Yeah, but yeah, I think maybe if we give out, like, tiers of, like, what level of support these components have, and at least label them appropriately, or, you know, if repos choose to say, oh, this… all the components are backed by, you know, the maintainers of this repo versus some repos that Can't, or don't want to do that.
I like it.
**Reiley Yang (Microsoft Corporation)** 13:00 Yeah, then.
I guess that's the only topic I have, so I'm… I'm down here. Wait for my PR.
Anything else?
**Trask Stalnaker (Microsoft Corporation)** 13:11 I'm continuing to babysit the Zizmor and the, scorecard rollout.
The main… the… once the scorecard rollout is done, the next step there is, I think, more interesting for you, Riley, which is, I want to… so the goal of the scorecard rollout is to reduce the false… remove the false positives in the, Code scanning alerts for repos.
So that we can… I wanna then start… Add a workflow that… Basically, it creates issues in repos or escalates in some way if If there are any code scanning alerts.
That are older than X days, or something, just… And I know you've… you've thought about that before, so… Hopefully, once that's done, the… this… this new workflow rollout, then I'll try to put together a proposal, and we can review that.
**Reiley Yang (Microsoft Corporation)** 14:23 Yeah, sounds great.
Okay, I think that's all. Jonathon, do you have something to add?
**Jonathon Klobucar** 14:30 I do not.
I've been out sick this whole week, so…
**Reiley Yang (Microsoft Corporation)** 14:34 Yeah, then cool. I'll rely on you and Trask to review my upcoming PR. Thank you.
Have a good one.
See y'all.
