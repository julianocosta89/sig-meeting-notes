SIG: Semantic Conventions SIG
Date: 2026-09-21
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Michele Mancioppi (Dash0 Inc.)** 02:02 Hey, Trask.
**Trask Stalnaker (Microsoft Corporation)** 04:28 Can you hear me now?
Fantastic.
**Daniel Dyla (Dynatrace)** 04:33 Yes, we can hear you.
**Trask Stalnaker (Microsoft Corporation)** 04:38 Love this microphone. Love, love this headset.
Alright, we are… I know that, Both Lyudmila and Josh are… out today.
So probably we can get started.
Michele… Let's start with you.
**Michele Mancioppi (Dash0 Inc.)** 05:10 FAPR.
The PR is the one… so we had a discussion a couple of weeks ago in the maintainer call.
For, putting a requirement about, requiring SDKs that cannot honor the, The conversion from spam events to log records.
To actually, emit a log with the internal logger.
Trask locker. Robert asked for a, proof of concept. I delivered the proof of concept to the Java agent.
Robert says, yeah, but the concept is not valid because the logger could be disabled at runtime.
And, to which I ask, since when can we do that?
So I think this is more, like, for UT Trask, as a, Java agent maintainer, and as the maintainer for the sand cones, because it touches, both of your SIGs.
**Trask Stalnaker (Microsoft Corporation)** 06:19 So… There is, I mean, there's… There is the capability, we haven't exposed it generically through the Java… through the, vanilla Java agent, to change loggers, enable disable loggers at runtime.
But that has been one of the motivations behind the op-amp, Work.
I'm not really sure… That's… Is that rela- how is that relevant?
Yeah, and apologies, I think there's another Java PR listed here, on the agenda I saw, and, we are, with the 3.0 stuff upcoming in the Java repo, we are kind of… Not having any time to look at other stuff at the moment.
**Michele Mancioppi (Dash0 Inc.)** 07:36 I'll leave it at that, Dyla. If you tell me that there is a way.
in the Java agent to, listen to the logging… to the logger… the logger provider being turned on and off.
love to do it. I do not believe we have the capability of listening to it, and your original code suffers from the same bug.
We're, turning on the logger provider afterwards.
results in the, in the, span events not being converted to logger provider.
I do not believe we have facilities, like a hook, that can be listened to recite.
That?
**Trask Stalnaker (Microsoft Corporation)** 08:20 Yeah, I think the way that it works is, there's a hook that you can use to, like, via the op-amp, to enable and disable loggers.
At runtime, but I don't think there's a listening mechanism specifically for loggers enabling and disabling Right, it's more of a… PopAmp gets the signal from The remote configuration, and it can update the loggers.
**Michele Mancioppi (Dash0 Inc.)** 08:59 Would that result in a reset of the SDK?
**Trask Stalnaker (Microsoft Corporation)** 09:04 No.
**Michele Mancioppi (Dash0 Inc.)** 09:06 then, both your committed code and mine have a problem with OpAMP.
**Trask Stalnaker (Microsoft Corporation)** 09:12 Yeah, I mean, the… I would not say that this is something we support today in this repo.
It's… the… I believe the Elastic folks have… some support.
for… this… In their distro already, and they're… they've been the ones kind of driving this.
Work, so it… it's future… But, yeah, I am not sure it's…
**Michele Mancioppi (Dash0 Inc.)** 09:44 My expectation is if a maintainer of the Java agent goes and says, this is the best we can do because we have X, then Robert is satisfied, and the PR for Semantic Conventions can go ahead.
**Trask Stalnaker (Microsoft Corporation)** 09:57 Okay.
**Michele Mancioppi (Dash0 Inc.)** 10:00 I mean, I hope so, because a POC that asked for something that cannot be done.
I don't think it's a valid request.
**Trask Stalnaker (Microsoft Corporation)** 10:09 Yeah, unless it points out some problem with the spec that, I mean.
We can't… yeah, I don't know.
Sorry, I don't really… Oh, we can look at…
**Michele Mancioppi (Dash0 Inc.)** 10:24 I'm fine taking this one offline, just not to… To burn more, diamond is sick.
**Trask Stalnaker (Microsoft Corporation)** 10:33 Okay.
Yeah, yeah.
J.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 10:49 This one's just quick, just more of an inform, and because Ludmilla is in here, I'll also share it kind of in the internal chat, but I've been putting… I've been working on this for a little bit, just kind of… explaining the kind of future vision of the Ecosystem Explorer, and kind of how I expect to tie it into some of the Semantic Convention Conformance data, that we're now collecting.
And it came up in the specifications SIG last week, also in the context of Like, how do we, decide what kind of third-party, instrumentations and other components we kind of label as compliant.
And so, kind of just setting the stage as, like, this is kind of one area, the Semantic Conventions conformance is one area that we can use in the future, and just how that all ties together. So there's a lot of mention of Weaver and the Semantic Conformance, Semantic Conventions conformance stuff.
So just if anybody has time to, take a look, and if you have any feedback or thoughts on it, I'd appreciate it, but… Yeah.
**Trask Stalnaker (Microsoft Corporation)** 12:04 This is great. The timeline there.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 12:08 Yeah, actually, I'm building an interactive timeline into the Explorer, too. I have a POC of it up that that's a screenshot from, but… That was kind of helpful.
**Trask Stalnaker (Microsoft Corporation)** 12:22 Might be interesting to put the de facto The de facto stable.
Version.
in here…
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 12:35 How would I know…
**Trask Stalnaker (Microsoft Corporation)** 12:38 That was the version that, we said don't update.
So, if we look at HCP… For HTTP, it's 1.20.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 12:59 Okay.
Yeah, I could definitely put those in there.
**Trask Stalnaker (Microsoft Corporation)** 13:04 Yeah, just because, I mean, that's kinda what happened.
Given that it was open for so long, We said, okay, like.
There's so many people using it, and using it in production, that we decided that Even though it wasn't… officially declared stable, we used the term de facto stable.
Right. Right.
And… Said, okay, that is… An important version there.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 13:40 Cool, yeah, I can add those.
Yeah, and basically the TLDR is, yeah, as Semantic Conventions stabilize, we don't really have a great way to see, kind of, from a macro view, about how quickly all of the instrumentation is keeping up with it.
And we think that using Weaver and structured metadata and this conformance project idea, will allow us to kind of put together, like, a global registry that provides the individual roadmaps, for different projects to get to like, you know, full compliance. And I put a little mention in here about the Java Agent 3.0, and how, as we move towards stabilizing databases, and messaging, and how we've already stabilized the HTTP conventions that have allowed us to see, you know, if there were any gaps, and kind of provide a focus So yeah, and in Trask, too, if you have any… you know, if I'm characterizing it incorrectly, or if you have other ways that this, you know… I'm assuming I saw you doing the work in both projects, and it seemed like you were using one to guide the other.
If I got that wrong, let me know, but… I just think that that kind of proves out the value of doing this type of work, just to make everything more visible.
**Trask Stalnaker (Microsoft Corporation)** 15:08 Yeah, definitely the… the HTTP… Conformed, because we did add all of the… Hcd.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 15:21 Yeah, the HTTP. Yeah, I know there was, like, some network attributes that it looked like you were… you were finding small gaps and fixing.
**Trask Stalnaker (Microsoft Corporation)** 15:29 Oh, yeah, so in the ACDP, there were four… yeah, there were four cases where we were not emitting something.
In database, we haven't really built out enough…
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 15:43 Right.
**Trask Stalnaker (Microsoft Corporation)** 15:44 To… Get that level of… detail.
But yeah, yeah, I hope to.
I mean, we will.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 15:56 Yep.
**Trask Stalnaker (Microsoft Corporation)** 16:00 Nice.
And so, yeah, your ask is just anyone to review the blog post.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 16:13 Yeah, if anything sticks out, you know, as something that you think is inaccurate, or if you have other ideas of how, like, this information will be useful in the future, I'd just love to hear other people's thoughts, so…
**Trask Stalnaker (Microsoft Corporation)** 16:29 Cool.
Alright, Aryan…
**Aryan (NewRelic)** 16:38 Yeah, hi, hi everyone, hello. I just came here to remind, about, last week, when I was here, we had a discussion about, the Semantic Convention PR for messages and queues getting auto-closed, and, like, somebody would review my PR and open it, so I'm just here if, like.
Somebody could take it forward just a bit.
**Trask Stalnaker (Microsoft Corporation)** 17:04 Yeah, so, as I mentioned earlier in the call, in the Java repo.
we're pretty, we're backlogged right now with the upcoming Trio release.
But we can… I think we can at least get this reopened with, Oh, first, if I reopen it, it will just get auto-closed again.
We gotta do this, Consider re… Opening with POC…
**Aryan (NewRelic)** 17:49 Perfect.
**Trask Stalnaker (Microsoft Corporation)** 17:50 Alright.
We made, like, this much progress.
**Aryan (NewRelic)** 17:53 Yeah, that's actually some progress.
**Trask Stalnaker (Microsoft Corporation)** 17:56 Oh wait, I didn't hit reopen, though. There we go.
Yes.
**Aryan (NewRelic)** 18:03 Okay. Yeah, that's pretty much it from my side. Thank you.
**Trask Stalnaker (Microsoft Corporation)** 18:11 Alright, moving on, Igor.
**Igor Peschinskii** 18:14 Yeah, thanks.
There is a PR of extending the hostility definition we came up with in the system, Semantic Convention SIG.
With improved definition of the host ID, and this PR is open for 2 months, And, We got all the approvals needed, including the maintainers, so I think we're ready to merge.
But I will wait a couple of days.
any comments, if somebody has. And after that.
I think I will reach out to Ludmu, so she can help to merge this PR.
But if anybody… can add something to the discussion. You're welcome.
**Trask Stalnaker (Microsoft Corporation)** 19:02 Yeah, I think this looks plenty well approved from the system. We've got.
Folks from multiple… like, 4 people from the system Semantic Convention SIG, and 1 maintainer here.
Yeah.
**Igor Peschinskii** 19:29 Oh, okay, thank you.
**Trask Stalnaker (Microsoft Corporation)** 19:31 Yeah.
Okay, we've hit the end of the agenda. Anything else anybody wanted to raise today?
**Christophe Kamphaus** 19:46 Yeah, seems like I joined just in time.
And it was specifically a question to you.
In the Semantic Conventions conformance Repo.
I notice that we have a lot of renovate PRs there.
And, they often touch… the data JSON, or… Transitive dependencies of the scenarios that need to be… that need to update their logs.
So, there's some manual steps involved there, and I was wondering if there's a possibility to automate it.
**Trask Stalnaker (Microsoft Corporation)** 20:28 Did I not… Do that already… Looks like I didn't… Yeah, definitely we… I think I did, in my prototype, even, let's see, renovate autofix here.
Yeah, what this did was, on Renovate PR's Generate committed… On renovate PRs and pushback.
My workflow call, fix… I don't remember why I… Da… this… particular way… Yeah, there's also some examples, like, I think the collector… several, repos have that post-renovate kind of step.
And since the Renovate PRs are not forked PRs, since they're in the upstream repo branches themselves, we… we can have access to secrets. We don't have to do anything, security.
Unwise, like, pull request target.
**Christophe Kamphaus** 22:01 Okay, great.
Will you take care of Seth?
I think you know best how it works.
**Trask Stalnaker (Microsoft Corporation)** 22:10 I… Let's see, did I really not… Send… Yeah, also, it probably sh… Should do some grouping if we're not already… Yeah, yeah, I'll do that.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 22:55 I had a question, too, about this. So, is this something that we always want to be on, like, the… The bleeding edge of pretty much every library and dependency that we're running, or… Will we potentially have cases where we want to freeze.
**Christophe Kamphaus** 23:14 I've seen one dependency, at least, where the instrumentation library wasn't ready yet, so it didn't support the very latest version.
**Trask Stalnaker (Microsoft Corporation)** 23:29 Yeah, what would be, jay, did you have any, examples in mind of why we wouldn't want to be on the latest?
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 23:38 No, I just wasn't sure what our, kind of, goal is, I mean, I could think of situations like… like, maybe, like, major versions of, like, Spring Boot or something, like, where we might want to continue running you know, multiple variations, but, I don't know that we have many of those types of things. But I was just curious, like, because I've seen the renovate PRs come up too, and I just wasn't sure, like, how I should be thinking about them.
**Michele Mancioppi (Dash0 Inc.)** 24:09 Spring Boot is a bit special, now that you mention it. They are… I don't think they support yet the HTTP stable Semantic Conventions.
I'm not sure.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 24:25 I guess I mean, more of our Java agent instrumentation for these libraries, like, would we want to run the scenarios for each major version?
**Michele Mancioppi (Dash0 Inc.)** 24:34 No, there is definitely a, for example, a node. The, the Semantic Conventions, the new version of ZCC Semantic Conventions, I think they're still up 10.
And, I don't remember if the plan was to turn it on with the next major version.
Or, that there was a date.
But it, in general, There are still instrumentations, there are on non-stable Semantic Convention versions.
with either an opt-in or a timeline for migration. It's not something that happens very fast.
**Trask Stalnaker (Microsoft Corporation)** 25:13 Yeah, so I was thinking, at least for now, like, when I did the HTTP libraries for Java, I… Did intentionally only pick the latest.
even, like, say, Apache HTTP… You know, we have multiple instrumentations in Java for different major versions.
But I've… So, I intentionally kept it… I guess, simple in this repo for now.
Simple decision matrix, just always and only take the latest.
And I could see definitely expanding that at some point.
But… Since we're… we've got a lot of… a lot of ways to go to build this out initially, keep it simple.
**Christophe Kamphaus** 26:14 Yeah, I think also the CI time would otherwise increase.
**Trask Stalnaker (Microsoft Corporation)** 26:20 Yeah, yeah, CI time, we've gotta probably… do some more, I think… We've split it out by language… so far.
Oh, by language and domain.
Okay, so 19 minutes is not so bad.
As probably our max.
We'll see. Once we get… I bet the Java database will be longer.
Because there's a lot of them, plus they spin up Docker containers.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 26:57 Yup.
**Trask Stalnaker (Microsoft Corporation)** 27:10 Cool, anything else about conformance? Anything else?
**Christophe Kamphaus** 27:18 Nope.
Thank you very much.
**Trask Stalnaker (Microsoft Corporation)** 27:23 Alright, thank you all.
Enjoy your half hour.
**Christophe Kamphaus** 27:28 See you.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 27:29 Yeah.
