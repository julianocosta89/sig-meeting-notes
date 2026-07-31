SIG: Swift SIG
Date: 2026-07-30
Duration: 36 minutes
============================================================

## Zoom Recording Transcript

**nacho** 03:47 Chiro, good morning.
**Vishwan aranha** 04:33 Hey, guys.
**Ben Joseph** 04:40 Thank you.
**nacho** 04:45 So… Sorry, admissary Justin.
Cool.
Yeah, that's better.
Yeah, yeah, it looked like… Not, not more people, coming today. So, let's go… Previewing the last… oh, you know, this journey also.
I do not…
**Vinod Vydier** 05:30 Hey, hey, hey.
Sorry, getting delayed.
**nacho** 05:34 Okay.
Yeah, you… so, great, because you were last week.
Yeah, there are… I have seen there are some new topics.
probably… This one, added them.
So, let's review last week's topics, and let's go with the new one.
As soon as possible.
So… in… In case you don't know about that, it has been made public. There is a deprecation plant for cocoa pots.
The plan is that we are removing, support for cocoa pots.
And the last release that we will release.
will be September, and the deprecation plan explains clearly.
By the last version, we will release that.
we can support will be in September, and in December, CocoaPots gets frozen forever, so that's our latest release.
There is the application plan there in the document. I don't know if you have access to the document.
So, yes.
Yeah, just to be aware.
From… From last week.
There is also, this is something that has been coming for several weeks, is merging… merging back SwiftCore.
Into Swiss main. That… that was a change what we did in the past… Because there were some people that didn't want to download the full repository, just for having the SDKey and a API. And what… Any advance last week, apart from creating the issue, Vinod?
**Vinod Vydier** 07:25 No, not… no, I think we still need more discussion on that.
And, yeah, even Ari has not been actually joining. He's been busy, so yeah, we need some additional… My internals also.
Yeah, that's not a small effort, right? We need some extra…
**nacho** 07:45 Yeah, there are many of the ice.
just keeping SwiftCore as a copy of the files.
And when we release a version in Swift Main, we will Create that read-only repository without the new files, so people can still download them from the same folders that they are now.
But, we will… the live code will be leaving again in the OpenTelemetry Swift.
project, and not in the Swift Core, so we can continue building, testing, And updating the core… Or, or the core libraries in a, in a… comfortable way to keep compatibility in the rest of the libraries, because, yeah, it was changed because there were some Users of the library that wanted that, but… We, we have seen the, the, the limitations and, and the… Extra work that's needed, and the quality of the library has decreased a lot.
And we have had some bills that were not building correctly, without notifying correctly, and with some changes that were needed for the main library that needed to be in core, and that We needed two versions for that to happen, and that has been… a really bad experience for, I think, for everyone, not only the maintainers.
So we… the plan is moving into that, more or less soon.
So, yeah, we can add plants more.
So that… those are the topics from last week. New topics, gRPC, To operate, that's what… Added by you, Vishwan?
You are probably on mute.
We cannot hear you Noah, we are… be swamped.
**Vinod Vydier** 09:59 Vishwan is… I think he's probably not there.
**nacho** 10:05 He was on mute, and he…
**Vishwan aranha** 10:07 Can you guys…
**nacho** 10:08 mute? Yeah. Yes.
**Vishwan aranha** 10:10 So, that… that issue, I did not add that. I added the second PR request thing.
**nacho** 10:16 Okay, okay, sorry. So the ZRPC2, who, who was the author?
The… who added it?
**Vinod Vydier** 10:26 Paul is the one. Yeah, Paul is not here.
So there's a bruised dead.
**nacho** 10:33 Okay.
**Vinod Vydier** 10:33 Yep.
**nacho** 10:35 So, regarding this one, Yeah, I think that Swift 6 was one of the limitations that we were not updating to gRPC2.
But I'm not sure the… We can still update without growing the version of iOS.
I looked.
I'm changing that limitation.
But I will… I, I think we could add that.
Probably, probably soon after the… Probably after the new… released from Apple, from the 27 version, maybe we can… we can think about Changing that, so we, we are still… keep the number of compatibilities. But if the author is not here, who probably knows where about these limitations?
Because the… Yeah Okay.
It has been… Okay… Yeah, this has been handled.
You know, they… offer support.
Yeah, I don't… Yeah, if the person who comes… is interested in adding that and changing, we can accept PR, so… Yeah, that's the only doubt I have, but probably after the 27 release of iOS and Macours, we can.
Probably keep a lot of… There seems there.
I don't know if there's a limitation there. Okay, so the OTLP trace for failures, that was yours, right? This one?
**Vishwan aranha** 12:58 Yes, that was mine. I just wanted reviews on that.
**nacho** 13:03 Okay, yeah, if you… Want to explain a bit what… You have done here, or what's… Probably can't help in reviewing. Sure.
**Vishwan aranha** 13:15 Sure, it was, like, a good first issue listed. I was, like, trying out, iOS issues, and it basically exports failures, and, like, partial failures were, like, mostly silent.
And this makes, like, missing, like, spans difficult to debug. So, I changed, like, the exporter now, so it uses, like, its existing logger to explain what failed.
And it's, like, pretty straightforward, small fix, and Yeah, it's… let me know if you need any… if you have any specific questions on this as you go through it.
**nacho** 13:48 Okay, yeah, this uses the existing logo, right?
**Vishwan aranha** 13:51 Yes.
**nacho** 13:52 And it has some jalapid.
It looks… quite focused, and…
**Vishwan aranha** 14:00 And I also tested it, like, logging fix works with the current GPRC version… gRPC version, but, the update, like, for, GRPC2, I… I haven't tested it, but I can test with that, too.
**nacho** 14:14 Okay, yeah, We are still not moving to gRPC2, so currently we are still not supporting that because of the Swift 6 limitations. I think that Yeah, as we have commented before.
Okay.
Yeah, it looks… Yeah, it looks quite… It's good from a quick preview.
But yeah, let's… We, we will, we will try to address, reviewing,
**Vishwan aranha** 14:55 And since I'm not a maintainer, I don't have merge access either, so if you guys review and approve it, feel free to merge if you get the chance.
**nacho** 15:03 Yeah, okay. Do you have any need for this to… any version for this? I mean, sometimes people just have peers.
Because they… Of some need for… Quick or soon release of something.
**Vishwan aranha** 15:18 No, no, I don't have any. Like, this was, like, the first… it was listed as a good first issue, so I just wanted to try it out.
**nacho** 15:24 Yeah, perfect, perfect, so… Yeah, thanks, thanks for that.
**Vishwan aranha** 15:28 Thanks.
**nacho** 15:30 Okay, so we can continue reviewing the… If there are any, other issues in the project?
So let's go with… Okay, core… Yeah, I… Issues are… quite dark, I think?
Yes, I think so.
issues, anything beyond pull request?
This was… There's… yeah.
Okay, there are some changes here, some PRs also… For validating instrument names… Okay.
Yeah, this is, Oh, we have now a ChatGPT codex, really automatic.
Okay, okay, Visa S.
Ice.
Big change… Yeah, I don't know if… Having the validator as a different class.
For a different file.
Is what we really want.
Not to create so many classes.
Because instruments will be there.
Isn't it so big, like… Yeah, this is a small file.
So I think we should… Add the validator inside the builder.
What do you think, Vinod?
**Vinod Vydier** 17:44 Yeah, so, let me actually… so the instrument builder has…
**nacho** 17:50 The instrumentation has 80… 80 lines.
Which is quite limited, so we… we could… the validation, I think, should be done, probably, in the own builder as a method.
**Vinod Vydier** 18:02 Who knows?
**nacho** 18:03 bit of Kavinavata.
**Vinod Vydier** 18:04 Another file, okay.
**nacho** 18:06 Yeah, because it's just a validator for the instrument.
**Vinod Vydier** 18:08 Yeah, yeah. Yep, yep,
**nacho** 18:12 Okay.
**Vinod Vydier** 18:12 Keep it simple, yeah.
**nacho** 18:19 Boy, I'm not… Saying.
**Vinod Vydier** 18:21 I didn't…
**nacho** 18:28 Okay… Enter, enter to batch, log record processor, exportinode timer.
Okay… Hmm.
Okay… Yeah, that's… that could be a part.
Why are we meeting back.
I'm not so sure about this.
Any, any… Do you want to?
**Vinod Vydier** 20:32 It seems like… it seems like it's also, there's some… Documentation from Claude.
But, I mean, he might have found this, from his personal testing.
I don't know.
**nacho** 20:45 I have never had any… I have never had any issue with make timer source not having a set cancel handler.
Personally.
So… Pete.
It's a bit too suspicious for me.
**Vinod Vydier** 21:05 And ask if there is a… Specific scenario that you hit that issue.
**nacho** 21:13 Yeah, any of you have had an issue?
with… dinosaurs not having a cancer family?
**Vinod Vydier** 21:23 Nope.
**nacho** 21:27 This looks like fluid hallucination to me.
A bit.
There you go.
Hmm.
**Vinod Vydier** 22:32 Hmm.
**nacho** 22:59 Do you think that… Yeah, it's a bit too spacious.
**Vinod Vydier** 23:04 Yep, yep, yep.
But the explanation does make sense, but I think… Indeed.
**nacho** 23:13 I mean, yeah, Cloth may… Cloth, or whatever AI you use, always You know, explains it as if it were true.
I have never had this.
**Vinod Vydier** 23:29 It's also from a Kotlin multiplatform app, so it could be some sort of a… React or some hybrid.
that uses… Yes.
**nacho** 23:41 Canceling a timer without an event canceled handler?
I have never had an issue with that.
So, it… I think it must be another thing, and… and this AI has just… added something.
Or thought it's the only possibility, and… Yes, yeah, that's my… my opinion, yeah.
Yeah, let's… we can continue with this, yeah, in next meetings. If he adds something, or we… or any other… person in the next meeting has any experience with that, so yeah.
Okay, yeah, this is what we have now. These were all requests and issues, and for the… main library… Yeah, we should try to just approve as much requests on the call before moving back.
So yeah, let's see, any issues?
Okay, these days, we plan to merge back.
No one has added anything in this.
PR, so no comments.
From anyone, Okay… Yeah, well, this… this world.
I'm targeting pull requests… These are updating.
the… Yeah, this is the PR we have been talking now.
**Vinod Vydier** 25:26 Costa.
**nacho** 25:27 So yeah, we should take a look and try to… Provide feedback or a proof as soon as possible.
And the release… Oh.
Okay.
Within Apo.
Yeah, who wanted to merge it.
Finally.
**Vinod Vydier** 25:56 So that's a bot is creating the new world?
**nacho** 25:59 Bryce Credit created it last week, and we have not released it.
**Vinod Vydier** 26:03 Oh, okay.
**nacho** 26:05 Right.
Yeah, no, we are still happening, okay.
So, yeah, good.
Okay, and the rest are updates.
This one… Same on… Maybe Dave has not added anything right here.
Okay, yeah.
So we're still waiting for feedback there. Yeah, and that's… that… that makes all the reviews on the PS.
Any other topic from anyone?
**Vinod Vydier** 26:46 Nope.
**Ben Joseph** 26:47 Hey, I just wanted to introduce myself. I'm a colleague of Vishwan, and it's Ben.
We both work at Grafana. I don't, I don't have a, much experience with iOS, but, like, I'm hoping to, contribute in some form. I'm working on the collector side, For hotel, also contributing to the Android, hotel, project.
**nacho** 27:15 Congrat.
**Ben Joseph** 27:16 So I hope, like, I can do some contributions here. I'm hoping to pick up, first-time, good, good first-time issue, and, like, have a PR ready. If there is anything, you know, that needs to be prioritized among that, you can let me know, and I can pick that up, also, I, I just want to, get a sense of, like, like, do we have any, any, roadmaps or, like, any features, If something needs to be built, if there's any gap that we are looking to… bridge, how do we bring that up? Like, is the SIG meeting the venue for that discussion, and then… then we go about, building that, or do we have any, any documents planned with that kind of roadmaps or anything?
**nacho** 28:08 Yeah, okay, yeah, the truth is that We are currently in a… in a… just… Trying to… how to say.
Put down fires.
**Ben Joseph** 28:23 Okay.
**nacho** 28:23 I'm liberating the project, because, yeah, the… the time that maintainers currently have it's very limited.
And yeah, we… Try to keep up, and fix things, Update the library, but we are currently mostly reviewing PRs from third, third-party developers, mainly.
And not much work is being done inside by the maintainers.
Currently because of, yeah, work, changes and things like that.
So, So, yeah, we try to keep up with the issues, we try to label them, and we try to review the PRs from People and try to keep a direction on the project, like, yeah, like, keeping good compatibility, updating when we need it.
But, yeah. Currently, it's moving like that. There is no, clear plan.
For anything, except the plan that we plan to recover the core into the main library.
That's fine. Okay.
That's, something in the big plan. We also plan the deprecation for cocoa pots, and we are trying, basically, to reduce as much maintenance Time as possible in order to be able to spend more time.
In really important tasks.
I'm trying to, yeah, to update when needed.
So, yeah.
Totally free to take on the task that, Open, if you want with first one, or first-time topics, or first-time issues.
That… those are probably easier, but if you are interested in any other, or… adding new features, or reviewing the semantic conventions, or something like that. Yeah, totally, totally open and free for that.
**Ben Joseph** 30:27 Okay, sounds good. And, like, for feedback, I know, like, how, how, how is that done? Like, should we, are the discussions usually on the, on the issue, or the PR, or, like, any Slack discussions are happening? What is the preferred group for this SIG?
**nacho** 30:48 Yeah, currently, we try to keep that in the PRs themselves.
**Ben Joseph** 30:53 Okay.
**nacho** 30:54 But some… sometimes… If… if there are some issues.
Sometimes serving them by, you know, in a meeting like this is great.
So, if there are gaps in how developing something, or how to approach some problems, and someone needs feedback, yeah, can come here, and we can try to guide.
In the best possible solution, but yeah, usually here. The Slack channel, I don't think it's much used.
By me.
by anyone.
Because it had many… it has… it has had many noise in the past.
And…
**Vinod Vydier** 31:39 It's mostly reminders and things like that, there's a lot of noise. Yeah.
**Ben Joseph** 31:43 Canada.
**nacho** 31:44 Yeah, the noise moved to the notification as well.
So, yeah, I think we could get back to just that.
And it's, that's… as a forum for talking about, yeah, I… Yeah, I've done this, but… Quick answers there.
Probably coming to the SIG meeting, For direct answers is the best solution if you want something more or less quickly.
Or the PR themselves. But yeah, the meeting is where… Every week, every week.
There will be some… We expect to always be something.
Oh, someone from the maintainer team.
For, for, yeah, for addressing issues, or directions, or, or with that.
**Ben Joseph** 32:34 Yeah, okay, yeah, sounds good, like… That helps.
One, one question I had, like, is there any desire to, have any other tool for crash reporting other than MetricKit, like,
**nacho** 32:53 Yeah.
**Ben Joseph** 32:53 Clark.
**nacho** 32:54 Yeah, there is a… there is a PR, with KS CRAS Support,
**Ben Joseph** 33:00 Oh, okay.
**nacho** 33:00 still in draft. You can check that in the main library.
Yeah, in the, but it's still… Draft, for a week. Okay.
**Ben Joseph** 33:14 Okay.
Is that actively somebody working on it, or…
**nacho** 33:19 It was funny.
**Vinod Vydier** 33:22 I can, I can…
**nacho** 33:23 But…
**Vinod Vydier** 33:23 Sure.
**nacho** 33:25 Yeah, this is… yeah, here, there is a draft from Wheeling.
Okay, started on December.
**Ben Joseph** 33:33 Okay.
**nacho** 33:35 It's more or less… I mean, it's working.
In a limited way.
But it reports.
It has been reviewed, but still has some issues.
The author… Has said he planned.
to address… Some… some of the issues?
But, yeah, I still have some conflicts, but it's… probably… I don't know. I have not seen… I have not seen William.
**Vinod Vydier** 34:07 He's working on… Yeah, he's working on adding it into the ADOT distribution, I think, so…
**nacho** 34:13 Okay, yeah. So I don't… I have not seen him collapse.
**Ben Joseph** 34:18 Are you noticing Amazon distribution?
**nacho** 34:22 So, probably, Indeed.
Yeah, I would expect it to land probably around September.
Probably, if he joins… I mean, this is summertime, so it's a bit more difficult, people have more things and have…
**Ben Joseph** 34:38 Gotcha.
**nacho** 34:39 Not only holidays, but also to cover, some colleagues from holidays sometimes, so it…
**Ben Joseph** 34:45 Right.
**nacho** 34:46 But yeah, this is more or less working. You can take a… I mean, you can… maybe use the, the, the PR right now?
It works, maybe a bit limited, and you can also address some… I mean, or add any comments, or just test if you work here. This is for KS Cross.
**Ben Joseph** 35:07 Got it. Yeah. Obviously, I just wanted to understand, like, somebody was already looking into it, and if it's coming in a… I mean, if there is… somebody is gonna work on it, I think… I think we are good, but I'll definitely take a look at, yeah, so this is a gap that we saw and, like, would have been nice to have. We also don't have a timeline or, like, a specific desire to get this in… within this timeline, so if it's coming September or later this year.
**nacho** 35:33 Yeah.
**Ben Joseph** 35:34 That sounds good.
**nacho** 35:35 I don't know, right? But I would expect that around that time, because currently, he addressed most of the feedback. Right.
So, yeah.
I don't know if it will be beta quality or final quality, probably a bit on the beta early, because… Okay. Yeah.
now has some conflicts that… We should address.
But you can take a look, if you want to maybe address some of that.
feedback, or… Or just expect what, what, how it's gonna, gonna work.
about ya.
**Ben Joseph** 36:18 Sounds good.
Yeah, I'll probably start with some smaller perspectives.
**nacho** 36:26 Okay, if there are no more topics.
We, we can… we can leave it here today.
**Ben Joseph** 36:36 Alright.
Thank you.
**Vinod Vydier** 36:38 Sounds good. See ya.
**nacho** 36:40 See you, bye.
**Vinod Vydier** 36:41 Bye.
