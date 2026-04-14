SIG: Semantic Convention SIG
Date: 2026-04-13
Duration: 45 minutes
============================================================

## Zoom Recording Transcript

**Christophe Kamphaus** 00:18 Hello.
**Trask Stalnaker** 00:21 Hey!
My headset isn't working, can you hear me?
**Armin (Dynatrace)** 02:44 Yep.
**Christophe Kamphaus** 02:44 Yes, now I could hear you.
**Trask Stalnaker** 02:47 Great.
So, let's do just a bit of triage to start.
But nothing blocked is good, ready to be merged.
I think, I'll leave this open if the… maybe by next week if they don't, see this suggestion, I may just apply it.
So I guess I should… Mmm, it's kind of ready to be merged.
Move process executable to its own… Entity.
Alright, this has lots of approvals.
And… One open… a couple of open… Discussions… Mostly…
**Christophe Kamphaus** 05:22 It also looks like no one from security approvers has taken a look yet.
Well, at least approved yet.
**Trask Stalnaker** 05:31 No one from where?
**Christophe Kamphaus** 05:33 From the security approvers.
**Trask Stalnaker** 05:37 Or does it, affect secur… yeah… This SIG hasn't really been active, though, so I'm not sure if it's fair to hold anything up on that. I think it's maybe more just a notification at this point.
**Liudmila Molkova** 06:03 Is, is Braden here?
I wanted to chat with him about the… The entity naming it, it doesn't seem so.
Okay, I'll take offline.
**Trask Stalnaker** 06:15 Oh, okay, the… Got it.
Let's maybe look at, let's see, we had discussed this last week, I didn't notice… let's see… Oh, is this just a simple…
**Christophe Kamphaus** 06:59 It was a discussion we had last week about whether it should be… a decentralized SunConf.
**Trask Stalnaker** 07:15 Okay, this one is… Simple. Did they have a bigger PR, a bigger graph?
URL, PR… Oh yeah, this one. Okay.
This is the big one.
**Liudmila Molkova** 07:32 Yeah, we just, yeah, we discussed, sorry, I, I was out for a sec. I'm still making progress on this, so I'll reach out to you, Trask to, share the federated SAMConf.
**Trask Stalnaker** 07:50 Who got this one?
I noticed, Ludmila, you just approved that, What do you think, should we… Go ahead and… Move this in, merge this, separate.
**Liudmila Molkova** 08:14 Yeah I think this is a trivial change, and I… Like, like… I wouldn't mind even getting the other one in, it's just because we have a chance to… move it to the right home, and it's big enough that I'm proposing to, try it.
For this one, no concerns.
**Trask Stalnaker** 08:35 Okay.
Let's see, we've got Gen AI stuff… Promote process attributes to RC… Looks like it has, most of the… System SoundCon Conv… Okay… Okay, so that one's still not almost… that one's almost ready, but not quite.
I had a question for that.
Okay, cool.
**Liudmila Molkova** 09:38 Do we have any people, by the way, from the Prata Sense System Semantic Conventions group here?
Doesn't seem so.
Okay.
**Trask Stalnaker** 10:01 This one, right, this one is… did we merge the other? Or is this one still blocked on… the enum value…
**Liudmila Molkova** 10:16 I think we blocked… sorry, we merged in them.
**Christophe Kamphaus** 10:20 Yes, Inium values was, merged.
**Trask Stalnaker** 10:23 It was merged. Oh, okay. Great. I missed that. Awesome.
We run a development protection staging test.
entity.
Good question.
Let's see, what's our… Our agenda's looking pretty light, Look at another… PR, maybe.
I saw a lot of discussion on this… Dash flow, okay… What do we end up with? Current?
And desire, and… oh, interesting, okay.
Does anybody know how this relates to… Do we have a process CPU?
Our process CPU count, I think?
Maybe I'm just thinking of Java, we have JBM CPU limit.
**Liudmila Molkova** 12:57 You want to find some, something similar to limits?
**Trask Stalnaker** 13:05 Sorry, say that again?
**Liudmila Molkova** 13:07 You want to find something similar to the snapping pattern?
**Trask Stalnaker** 13:13 Not just a pattern, I thought we had… actual CPU limit somewhere. I think we have it in JVM, is maybe where I'm getting mixed up here.
We have CPU count.
**Liudmila Molkova** 13:30 And there's GVM memory limit.
**Trask Stalnaker** 13:33 Yeah, but specifically for CPU, I was wondering how this relates… If we had, overlap with general process CPU limits.
or CPU count. I mean, it's not really a limit in the sense of, like, Kubernetes or some virtualization where you set a limit, but you… the number of CPUs you have allocated Is still an effective limit.
**Liudmila Molkova** 14:12 Oh, what?
Well, given that the limit is dynamic.
would we change how we report GVM metrics, and if it even leaks into the GVM API that we can… Find it out.
**Trask Stalnaker** 14:35 Yeah, I mean, it's a metric value, not a… Resource attribute.
So it… Intentionally can change over time.
And it's just meant to be a… A limit, effectively, to divide your time by to get, like, percentage of CPU utilization.
**Liudmila Molkova** 15:07 Okay, so the dynamic was another trace. There are multiple characteristics of the limit for Kubernetes.
The desire… like, the desired, right?
And what you actually got.
**Trask Stalnaker** 15:23 Yeah, yeah.
So the real limit, and the… the real limit, and your… your target… your requested limit.
desired… Okay, so we've got this pattern of… Okay, yes, request, requested. Request. What is request?
CPU request.
**Liudmila Molkova** 16:00 So, I think in Kubernetes, you can specify a limit, the hard limit, and the request is what you… One within this limit, so these are the Kubernetes properties.
**Christophe Kamphaus** 16:15 The request is used by the scheduler.
So it will only schedule your workload on nodes where This is available.
**Trask Stalnaker** 16:27 Okay, thank you.
Let's see, has our agenda grown? Our agenda's still blank.
Let's see, any other… Let's see… We're at Kubernetes, assuming… let's see… Christoph, do you think we should merge this?
Or, let's see, Chris Mark Dash Clow, who's been in the bot, Chris Mark Dash, everybody who's… I guess I can just ask.
Thanks, Christoph, for reviewing that.
I think your… General approval should… Yeah, I mean, yeah, I have a green version.
**Christophe Kamphaus** 18:05 There were several from Kubernetes that reviewed it.
And I checked if it looked good, and… yeah.
**Trask Stalnaker** 18:21 Jennya, Jennya, okay.
Any… open the floor to any… Anything anybody wants to chat about today?
Otherwise, we'll come…
**Victor Lu** 18:37 Just about the… Ocsf.
**Trask Stalnaker** 18:42 Oh, yeah. Yeah, sorry, I was… I forgot last week that I was out of office on Thursday and Friday, so I wasn't able to meet.
**Victor Lu** 18:50 Oh, no problem. Josh was also not able to join, but I… there… it just happened, Anponian from, Splunk, now, I guess, part of Cisco, has presented about AI, matrix, for, actually, no, I'm sorry, not OI Matrix. OpenTelemetry, that's mapped to OCSF. So they are already working on that. My understanding, at this point, there's no meeting within OpenTelemetry that's focused on security, so I guess the question is.
going forward, do you think that discussion should stay within OCSF and then only come to OpenTelemetry to be in sync, or it should be, set up a meeting in OpenTelemetry as well to discuss about security-related matrix?
**Trask Stalnaker** 19:47 So my previous thought, and when we met with them last year, like a year ago, was that sense was exactly what you said, which is since we don't have an active security group here, and the security experts, domain expertise reside… resides in the OCSF, that… It would be… it could be nice to just delegate, like, let them… run it from there, and we can, you know, join… we can direct people who are interested over there. I am curious about… the, I think the only thing that's changed since then is sort of the, Gen AI, the interest in security from a GenAI perspective.
And I could… I think there are people in the Gen AI SIG who are interested in security.
So maybe, so there might be a little bit more… we might need a little bit more coordination in the Gen AI security world with them, and I'm not sure what that… Looks like…
**Victor Lu** 21:01 Yeah, actually, as a matter of fact, the… I just discussed with the Gen AI team.
And there's another community called COSI Coalition of Secure AI, where is interest to create, open telemetry-focused, matrix for AI security. But actually, the non-AI security and AI security really cannot be separated, in a way, because they are really correlated, tightly coupled.
So… I guess it's up to the OpenTelemetry community to decide, whether, there should be, maybe, as you said, the OpenTelemetry Gen AI community plus COSI collaboration.
In addition to communicating with OCSF, or maybe OCSF-focused discussion, where everybody goes to OCSF and discuss there.
I guess, yeah, that's something that probably needs to be discussed, decided here.
**Liudmila Molkova** 22:10 Do you have any links for the second one? I didn't catch the name.
**Victor Lu** 22:16 It's called, COSI, Croatian for Secure AI, C-O-S-A-I.
Smart.
Yeah, if you're, interested in joining that, I can, send you the link, but it requires membership, but the first time, I think, inviting, there's no problem. They're pretty open.
**Liudmila Molkova** 22:38 Yeah, that's… that's the tough part, that… If it's not helping, if there is… the notes and everything is not helping, it's…
**Victor Lu** 22:46 Kinda hot.
**Liudmila Molkova** 22:47 Part 2.
purchasing.
**Victor Lu** 22:50 Yeah, but there's… if it's decided this should be part of a telemetry discussion here, I see no problem for them to come to OpenTelemetry meetings to discuss.
It's not bad.
**Liudmila Molkova** 23:03 It would be interesting, I could be interested to come once and talk about open telemetry, and what we have, and how we see it. I cannot commit to joining the effort.
Because… I don't want to push OpenTelemetry as a standard into other communities, unless they really are interested in And they want us to find something in common.
**Victor Lu** 23:29 They… this is the part I don't quite understand. My understanding, talking to the main person who… my personal opinion, it needs to be a collaboration of all communities.
Including OCSS, but there are some, proposal VZ and COSI to create, open telemetry, for AI security there, as kind of separate effort extension.
That's how it usually works, so it's better to come here to discuss?
University.
Talk to me.
**Trask Stalnaker** 24:02 In this case, it's gonna be better to come here, I think, at least initially, to make sure that we're not, you know, creating multiple standards.
**Victor Lu** 24:14 et cetera.
**Trask Stalnaker** 24:15 Because it's definitely, while we haven't had general security interest, there is… There is active work in Gen AI security, and there are active PRs open in the Symante Convention repo covering, some AI security areas.
So I do think we need to collaborate.
**Victor Lu** 24:41 On Instagram.
**Trask Stalnaker** 24:42 closely on that particular intersection of security and AI.
**Victor Lu** 24:50 Yeah, that's my impression. Otherwise, it will be…
**Trask Stalnaker** 24:54 Multiple standards.
**Victor Lu** 24:55 it won't… even if you call open telemetry, it will not be open telemetry. Yep. So, in that case, I guess, so, so, anyone want to, I can, I can ping you on, on Slack to, invite you, just, like, invited, Ed, Nankumar, to, to make the meeting. He didn't join the last.
two weeks, I'm not sure he's that busy, probably. Yeah, that team already know about OpenTelemetry, so probably there's no need for presentation about OpenTelemetry. They are ready to create their own, basically.
Issues like bears.
**Trask Stalnaker** 25:39 Yeah… I mean, the OCSF one is easier, like, that's under Linux Foundation. What is… where… what is Oasis Open Project?
**Victor Lu** 26:01 Yeah, that, that, that, that, is, also, actually, I'm not sure, because the, the, OCSF seems to be a… there are not many people attending, but it looks like there, it is, However, have a lot of people in the, in Slack, at least. But the, the COSI is membership-based, community, but it's quite open, actually. I guess, Yeah, how should.
**Trask Stalnaker** 26:31 Yeah, maybe you do, so they have a… maybe, can I get, can you invite me to the Slack, or post…
**Victor Lu** 26:39 Sure. I'll ping you the meeting, which is, if you can join on Tuesday, afternoon, 2 p.m. Eastern. I think that's the best place to discuss about where this discussion should happen, at this point.
**Trask Stalnaker** 26:54 Okay.
**Victor Lu** 26:55 Correct.
**Trask Stalnaker** 26:56 Sounds good. Yeah, I can, I can do that.
**Victor Lu** 26:58 But… Let's find you first. Yeah, I find you on Slack.
And who else should want to join the, the, the, cosign meeting to discuss?
Goodbye.
What's that?
**Liudmila Molkova** 27:14 Since just volunteer tile, I'll just pass on this, thank you.
**Trask Stalnaker** 27:18 Yeah, I think it's fine just for one, like, wood.
I don't think our goal… our… yeah, I'll just join from a, you know, let them know what we're doing, and hopefully, pull them in, sort of, to our community, have them join to discuss within the OpenTelemetry meetings,
**Victor Lu** 27:41 Yeah, I think that would be great. I just said, otherwise, it will be created as a totally separate matrix.
**Trask Stalnaker** 27:48 Yep.
Yeah, and I probably, probably won't join tomorrow, probably, is it every week?
**Victor Lu** 28:00 Yeah, yeah, that's… that's where… every… every Thursday at, 2 p.m. Eastern.
**Trask Stalnaker** 28:05 Tuesday or Thursday?
**Victor Lu** 28:07 Thursday.
**Trask Stalnaker** 28:08 Thursday. Oh, okay, okay. Maybe, When is… isn't that when the OCSF…
**Victor Lu** 28:20 Oh, I see.
**Trask Stalnaker** 28:20 Justin.
**Victor Lu** 28:21 Oh, I, actually, I apologize, I, I, I messed up. OCSF is Thursday at 2PM. I think it's 1 p.m. Thursday, Eastern.
Confidently.
Yeah, they're the cool thing.
**Trask Stalnaker** 28:37 Oh, okay, right beforehand?
**Victor Lu** 28:39 Yep.
**Trask Stalnaker** 28:41 Okay. Yeah, I'll probably wait and join that the week after, because I'd like to discuss with the OCSF folks first, because I think that's… that we've had previous discussions with them, and, they're sort of, you know, within our Linux umbrella, Linux Foundation umbrella, and… I'd like to sort of line up what, our story with them first, and then, you know, we can reach out to the Cosi books.
**Victor Lu** 29:11 Yeah, sounds good. Thanks.
**Liudmila Molkova** 29:16 I'm thinking, should we, maybe… well, we have so many things going on in the AI group, but should we maybe have some… blog saying how we see this, because… To me.
Okay, let's say there are 3 different standards for AI telemetry, observability, AI, security, AI… Something else? Anyway, so there are, let's say, two standards, or three standards, who is going to capture what. So, in OpenTelemetry, we first focus on the client and the application observability, and second on maybe the self-hosting.
insert maybe on the cloud providers, but we… our goal is to provide instrumentation libraries, right? We are not… Super excited about conventions without Something that users can… Just get by installing some instrumentation library, so enabling something.
And… if… It would be interesting to understand what the security groups target. Does it target cloud providers, model providers, people who host things? Do… what kind of… who is supposed to follow them? Who is supposed to implement them?
And maybe if we can document, just as a blog, of what… how we see it.
in our tel community, and then it would be useful to compare what is the intersection, actually.
If we all target writing instrumentation libraries, then we are in the bad state with multiple standards.
**Trask Stalnaker** 31:11 That's a good point, that there may be, yeah, some… logical… Boundaries that we can… define.
**Liudmila Molkova** 31:27 Yeah.
**Trask Stalnaker** 31:34 Cool. Anything else anyone wants to chat about?
Gen AI, security, or other?
**Christophe Kamphaus** 31:44 I think the Kubernetes PR is now ready to be matched.
**Trask Stalnaker** 31:52 Alright, thank you.
**Liudmila Molkova** 32:08 I'm adding the topic. It's been… two quiet weeks in this meeting, and I want to check the temperature, like, what… of course, people who didn't join cannot share, but I'm thinking, like.
Is it quiet because we don't drive any big projects here? Is it quite because sub-seqs are doing fine and they don't need anything?
Like, do people have any thoughts? I can talk about some ideas, but I'm curious what people think.
**Trask Stalnaker** 32:53 Yeah, that would be my… Guess is that, you know, we… As, like, system… metrics, database, as all of RPC, as all of these were going through stabilization, there were a lot of, kind of.
global SEMConf conventions that we had to work out that would keep getting punted… pushed into this meeting, I mean, brought to this meeting and discussed.
But the… stabilization, Effort seemed to be… pretty solid right now. Rpc is RC… System SEMCOM, I think, is RC, or almost RC.
Kubernetes is getting there. There haven't been a lot of… Those kinds of questions.
Which is good.
**Liudmila Molkova** 34:01 Yeah.
**Trask Stalnaker** 34:05 And we've also been, sort of, pushing out… we've been drawing, kind of, Harder boundaries as far as taking in new Semantic conventions, that don't have a… Group to really drive them.
So less… sort of… PR's work that… falls outside of existing SIGs.
Which I think is also good. I mean, is… Very intentional.
We also put messaging on hold.
Which, will probably… have still more… Worms to work out.
**Liudmila Molkova** 35:01 Right.
You want it in writing.
I think there are some… infrastructural changes that will be coming with V2 work and tooling, but they are more mechanical.
So, let's see… So we are actively working on the V2 schema. It's now polishing, mostly, and the last… issues that we find, but at some point soon, we will pull the trigger, and we will say that V2 of the schema is ready.
And this will come with the two changes.
So, first we care, we will… We will not be forced to rewrite every convention in V2.
But we'll probably have some skill to rewrite it.
And we will gradually move them from V1 to V2.
It's not… it's not like… I think we can do this one-to-one, but I think we should leverage this opportunity to clean up some of the most complicated conventions in terms of hierarchy, like the group hierarchy. Should probably flatten it down, clean it up, and V2 will force us to do some of it, but we can, Just some human judgment and some nice decisions there to make it nice.
Then, there will be some work there. The other part will be the publishing part.
And… this is probably just one infrastructural change, or a set of small infrastructural change. They don't affect any particular convention, but it's like, okay, instead of Publishing.
The schema file we would publish.
more.
The resolved schema file, with all the conventions.
It will affect semantic conventions consumers more than semantic conventions producers, so that… more outside people.
But, after V2, like, the, the… we do feature parity with one lens, I think we will have capacity to and… and reasons to… improve the schemas that we have. Like, for example, we don't have histograms.
in YAML, the histogram boundaries, or we don't have, I don't know, metric requirement levels, and we don't have means to describe specific types, so there could be Finally, we are not making any progress on the schema improvements, because we are spending all the effort on moving to V2 and, like, designing V2, but then we can invest more into YAML, and we can invest in into… Just better coverage.
And again, it does not affect changing semantic conventions, but taking existing YAML.
And… sorry, taking existing Markdown and making it YAML.
And there was something we… Been discussing Last week, in the GCTC channel related to… Thinking more about instrumentations?
In semantic conventions, and maybe, having this group drive… Consistency in instrumentations across hotel repos.
Through river life checks and other enforcement mechanisms.
**Trask Stalnaker** 39:42 Yeah, I think that's a nice, Kind of follow-on for… this… SIG or focus area for this SIG, In the future is conformance of… the existing… Semantic conventions that have been published.
like, I guess, ideally it would be the groups… I mean, maybe ideally it would be the semconfigs, like the, the HTTP, CENCOMSIG itself, like, that would Follow through that whole arc.
But I think… We've kind of effectively disbanded Most of… or, well, I guess we've only stabilized a couple of things, So far, but those groups don't really exist, anymore, except for in the folks here.
**Michele Mancioppi** 40:42 And besides, as far as I can tell, 26… Did not have the cross… really, the cross-language.
Representation to actually go and ensure that The language seeks to actually do this.
**Trask Stalnaker** 40:58 Yeah, and that's a good question, whether this SIG would, Just do, like, conformance report and maybe open issues with, or, you know, essentially document what's out of compliance… out of conformance.
Or if we also, you know, can have the language expertise to go and fix those Fix them as well.
**Michele Mancioppi** 41:33 I think maybe it's in phases, right? So first, we need to understand The extent of the noncompliance.
then, I suppose some languages will be first-class citizens, and… We may go and fix stuff.
And others that do not gather nearly as much interest, then maybe it's gonna be a bit different.
**Trask Stalnaker** 42:00 Yep.
**Liudmila Molkova** 42:04 Yeah, so I think we are… targeting, just make it transparent, making it easy for SIGs to consume the tooling and build a conformance report, have an infrastructure to publish conformance reports, pages, and whatnot.
we can work on this. Like, it's interesting that the line between this SIG and tooling sig gets blurry. It used to be that the tooling sig was a small part of this one, now it seems that this one is becoming kind of small part of the tooling.
**Trask Stalnaker** 42:37 Oh, no, tooling, yeah.
Maybe we merge them back together.
**Michele Mancioppi** 42:44 I mean, for the record, he's not a bad state of affairs.
**Liudmila Molkova** 42:51 Interesting.
**Michele Mancioppi** 42:51 absorbed it.
**Liudmila Molkova** 42:54 Maybe we should… one thing that Weaver calls are very active, and they're very technical, but they are Rust technical.
So, it's maybe interesting to merge, but I think we should still keep maybe two different calls for people who are interested in different things.
**Michele Mancioppi** 43:13 I also imagine that the moment the SIF starts publishing non-compliance reports, the activity is going to go up of people saying, hey, what do you mean I'm not compliant?
**Trask Stalnaker** 43:24 Yeah.
**Michele Mancioppi** 43:24 The discussions are going to be very much in the direction of, do we have to? Say, yeah, you do.
**Liudmila Molkova** 43:29 Yeah, great point.
Cool.
I pasted the link to the collector PR, where… The beaver life check, or some form of it, is introduced.
maybe even as a VASM component, or maybe as a test component, not sure, but this… this… Tests, collector, receivers, compliance with something, I'm not sure what.
Maybe metadata YAML.
**Trask Stalnaker** 44:13 Cool.
Anything else you want to talk about next?
**Liudmila Molkova** 44:34 Nothing from me.
**Trask Stalnaker** 44:37 Alright then.
Cross. West call? Yeah.
**Christophe Kamphaus** 44:43 you were asked for on Slack in the Hotel Maintainer's channel.
**Trask Stalnaker** 44:47 -Oh, did GitHub, did something happen in GitHub?
**Christophe Kamphaus** 44:52 Perfectly, yes.
**Trask Stalnaker** 44:54 Deleted the meeting notes for the specification.
That one?
**Christophe Kamphaus** 44:59 The one before, about the merge queues.
**Trask Stalnaker** 45:02 Merge queues… Okay, Yeah.
**Liudmila Molkova** 45:15 Okay.
We'll let you fight it for your Trisk.
**Trask Stalnaker** 45:20 Alright, thanks a lot.
Bye.
**Liudmila Molkova** 45:23 Thank you.
**Michele Mancioppi** 45:24 Bye.
