SIG: Android SIG
Date: 2026-06-09
Duration: 45 minutes
============================================================

## Zoom Recording Transcript

**Jason Morris** 02:20 Oh, yeah.
**Hanson Ho** 03:46 Okay.
Lowe.
**Jason Plumb** 03:53 Good morning.
How do computers work, anyway?
**Hanson Ho** 04:07 There's a little gremlin inside, and they crawl around.
**Jason Morris** 04:12 If you overheat him, you let the smoke out.
**Jason Plumb** 04:16 The magic smoke, yes.
Let's give it one more minute.
I would love for this meeting to be 5 hours later.
**Hanson Ho** 04:52 Which make it really difficult for the Europeans.
**Jason Plumb** 04:55 Nearly impossible.
But that's not why I'd like it later.
I love our Europeans.
And our Africans!
Now that we're, like, really, truly global.
**Hanson Ho** 05:15 the outside of North American, or actually, the Americas time zones, I guess.
**Jason Plumb** 05:22 Yeah.
Okay, well, agenda's looking pretty light. Let's look at some of these issues that David's bringing up that look to be pretty… Low impact. Was there anything special to note about these, David?
**DavidGrath** 05:45 No, nothing of note in particular, no.
**Jason Plumb** 05:50 Okay, cool. We can just… we can go through them, because we've got the time.
So, this was from last year.
Yeah… yeah, we should limit this.
I think this is still worth doing. Yeah.
**Hanson Ho** 06:08 It should be simple, it should be simple too, right?
**Jason Plumb** 06:11 Exactly. So, when David and others, if you're looking or going through issues and you see these, This is one that you can tag, or you can label it with, good first issue.
And then another one is, like, Help Wanted.
And I'm pretty sure as an approver, you can do that now, so please, you know, feel free to… Add labels, because it does help, you know, people are sometimes hunting for things to work on, and so just having a little bit of… A hint there can help.
Yeah, definitely worth doing.
Oh, maybe Hanson has an update on this.
**Hanson Ho** 06:48 Yeah, this is done.
Yeah. We're just waiting for it. I hadn't checked for a couple days, let me…
**Jason Plumb** 06:58 I don't…
**Hanson Ho** 06:58 No.
**Jason Plumb** 06:59 I never checked for an invite, should I check my personal email for an invite?
**Hanson Ho** 07:02 No, I haven't done that yet, because I did with my personal, Google account, so I have to go to the other computer. Yeah.
**Jason Plumb** 07:12 Will you ping me when that's done? Just so I don't also sleep on it? Because I could.
**Hanson Ho** 07:18 I was trying to, like… I was waiting for it to actually, show up in the listings first, and it hasn't done so. So, yeah. Right now, it's still not there. I'm looking at… so this is where I'm looking.
Share it for y'all. Oh, where is it?
**Jason Plumb** 07:38 Do you want to share?
**Hanson Ho** 07:40 Well, I'm just gonna… I'll send it to… I'll send the URL, okay.
So it should be listed, here, when it's all said and done, under OpenTelemetry Android, and it's not right now, so… I'm gonna see if it's elsewhere.
I did a search, not there yet. So, what it… it took forever, because Google took forever to get back to us, and they finally did after months, so, we submitted the second list of things, to do. They've… they've… we've released the APK with the metadata a long time ago, and and now we're waiting it for it to be listed. And I'm listed as the only manager right now, Because we have to find the Google accounts, and at that point, it was difficult to find Google accounts, even email addresses, frankly. So, several added me, and I'm gonna add, the rest of the maintainers, to, to be the managers, whatever that means.
we're not expecting a ton of data from this, we're… we just want to kind of just have it listed, so it's just there under the SDK, console, registration, approved SDKs or whatever, so…
**Jason Plumb** 09:06 And then we get some very broad, obtuse usage numbers or something, right?
**Hanson Ho** 09:13 Yeah, yeah. Yeah, I don't know if I have access to the Embrace stuff, but it's… I would say it's not, It's not complete, and the… the… whatever crashes that they tell us happens is, not vetted. So a lot of data is actionable.
But it's… it's there, so we should take advantage of it, kind of thing. Better than nothing.
**Jason Plumb** 09:37 book.
**Jason Morris** 09:38 There are also the nice features about being able to say when a crash is SDK attributable and things like that, which can.
**Jason Plumb** 09:47 Okay.
**Jason Morris** 09:47 which can affect people who are using those versions. If they see that crash, they get a marking in the Play Store for it, and stuff like that.
**Jason Plumb** 09:56 That's cool. I didn't… yeah, and then we could… we would be able to see some stack traces, probably, and figure out where… okay. Really helpful, yeah. Okay, let's close this one for now, because I think I agree, it's done.
We did get it into the console. Awesome.
Thanks for…
**Hanson Ho** 10:15 It's been submitted, it hasn't been listed yet, so there's the final step of, hey, there it is. We'll wait for that to happen, but there's nothing.
**Jason Plumb** 10:26 Well, I closed it, yeah. I figure that's no longer actionable.
**Hanson Ho** 10:30 Yeah.
**Jason Plumb** 10:32 Oh yeah, there was some new discussion on this recently, I think, so… Yeah, so this was, I think… Right, we… Where do we report this? We report this in telemetry somewhere.
Don't we?
I don't remember, but let's see.
**Hanson Ho** 11:00 I doubt it.
It's something that's difficult to accurately get, and it doesn't actually do very much, because it doesn't list the powers of the cores, and especially these days, having 4, 6, 8 cores It doesn't say very much.
**Jason Plumb** 11:24 It's true.
But, I think the original… I think the original conversation was around… augmenting other telemetry. Like, if you know that something is taking a long time and you think it's CPU-intensive, like, knowing the core count or the number of allocated cores might be useful to have alongside of your other telemetry.
But it seems like it's not… it seems like it's not, you know, we would just maybe be emitting an event every time it changed, right? Which is, like… You know, it's not that much data.
**Hanson Ho** 11:59 I don't even know if this API uniformly returns different values or correct values. Like, I… I, I, I, I… I've never thought about allocated cores changing.
**Jason Plumb** 12:18 I know.
**Hanson Ho** 12:19 Especially, like.
**Jason Plumb** 12:20 Damn.
**Hanson Ho** 12:21 And, in, in, like… After a process has started.
**Jason Plumb** 12:27 But I think that's also one of the reasons we considered doing this, is because I think none of us understand… the rhyme or reason of when your app might have more or fewer cores. And what a crazy thing, like, if this ends up generating, like, you know, hundreds of events per minute, like, I didn't know that my app was getting its core count switched all the time by the platform, like… I don't know.
**Hanson Ho** 12:51 I don't even think apps have access to cores. Like, I think that's something that's fairly opaque to them. I certainly know you can't… you can't assign, jobs to cores. Like, that's… that's… that's the domain, the schedule.
**Jason Plumb** 13:07 Right.
**Hanson Ho** 13:07 So…
**Jason Plumb** 13:12 But it's just like, how many are… how many are currently allocated to the JVM? The JVM not even being a real thing anymore, right, yeah?
**Hanson Ho** 13:20 Yeah.
**Jason Plumb** 13:21 And this goes all the way back to 1, so maybe it's just, like… baggage, like, it's crusty? I don't know. But I think it'd still be interesting. Even if it's experimental, even if it's opt-in, I don't know, I'm curious about what it reports.
And, you know, there's other options, too. I would love to, you know, even have issues for these.
**Hanson Ho** 13:42 I would say that's probably a lot more, useful.
**Jason Plumb** 13:48 Yeah, I would love to see some follow-up issues for these. I don't mind letting this kind of age out and stagnate, like, in… 6 months if no one picks it up, and we can close it then, but let it… I think we let this simmer for a little while longer, and then let's open issues for these.
**Hanson Ho** 14:10 So this is something that we're actually working on at Embrace.
How to properly model this in a way that is not just add an attribute to every piece of telemetry, with this. This would be the naive kind of hotel way of doing it, which is kind of like a global attributes appender type thing.
But that can get super noisy, especially if there's thrashing. And how do you represent that on spans, for instance, if it's just an attribute?
So, it really depends on whether we want to be a bit smarter.
Or we just want to do it, like.
what hotel would do it, which I think is massively inefficient, and… and potentially, Difficult to, associate with spans, which have multiple points in time.
**Jason Plumb** 15:11 Yeah, so, like, the CPU count, clearly an event, right? In hopes that it's not changing so frequently, right? Like, literally, if the count is changing Hundreds of times per minute, then it's probably better modeled as a metric, I know, And you probably don't want to generate hundreds of events per minute, but, and we also know all the complications around metrics.
But, I'm curious about what these provide, because I don't know these APIs. So, thermal status… So this one, so thermal status… What do you get?
You get a changed event. What does that look like?
You get a status with no description of what that is.
It's probably an enum or something, right?
Which means a, you know, fixed set of values seems reasonable to make an event out of that.
**Hanson Ho** 16:12 Yep. If we want change events, We can always do that for thermal state, for a network state.
**Jason Plumb** 16:24 And power save mode changed, does it tell you what it… Changed to… This is within the Power Manager, so it's, like, one of the events you can get from the Power Manager. And then do you have to come back and read it?
Get location… is power save mode.
Yeah… So, it's even saying here, like.
You can monitor for changes to it with this.
So maybe it's Boolean? That's all this is, is Boolean, it sounds like.
**Hanson Ho** 17:12 Yep.
**Jason Plumb** 17:13 But when you get this event, you don't necessarily know what the current state is unless you're holding it. So you probably want to just pull this anyway, right?
**Hanson Ho** 17:21 Yeah.
**Jason Plumb** 17:22 And hope that it didn't change back by the time you pulled.
Anyway, those seem like good things to maybe have follow-up issues for, and we can scrutinize them individually. I mean, I'm… I'm… I err, especially right now, in this stage of the project's life.
I err on adding more features and getting stuff in there for people to tinker with and play with and try and find value.
I'm willing to take on… I want us to be willing to take on more of that collective, kind of, maintenance burden for features like this, and exposing platform features, especially through telemetry. And maybe some of them, you know.
don't stick around, because no one uses them, but I think it's interesting to surface this stuff.
**Hanson Ho** 18:07 But we could also put a cap on, the number that we do per process or something like that, if we were worried about thrashing.
Specifically, you're basically saying anything that the platform is surfacing through listeners as events, it may be interesting to just create events for them.
**Jason Plumb** 18:38 I think so. Yeah, I think there's nothing wrong with that. I think… you know, we want to eventually align with semantic conventions and have some of that stuff be more, kind of, OTEL-native, but in the short term, I think it's really pretty cool to be able to surface some of that stuff.
**Hanson Ho** 18:57 The problem with events is that they don't… it's not as… as nice. For correlation.
Because you're not saying spans and things are related.
maybe you could associate certain things with sessions, but there's no… yeah, unless you're, like, aligned temporally, or look at everything, like, within a session, like, in a timeline, it's… it's difficult to do that type of aggregation and say, hey, you know, you know, when performance is slow, this event tends to crop up. And I think that's what would make it useful.
**Jason Plumb** 19:33 Yeah, I mean, I think most rum products display stuff on a timeline.
I think that's where the value is.
And yeah, if people start seeing patterns, like, oh, I've noticed, like, more than one session where after they went to screen 3, like, a second later, they're getting this CPU spike, or they're getting this power… like, this power draw change, or, you know, thermal status change. I don't know, just… I think without the telemetry, you just don't know.
And at least having the telemetry allows you to decide if there's something, if there's signal, if there's meaningful signal within those signals.
**Hanson Ho** 20:06 Yeah, it may not be a bad first step, I guess.
**Jason Plumb** 20:21 So, David, if you were mentioning these because you were thinking about finding, kind of, low-hanging fruit to pick up, I think all of these… well, we closed one of them, but I think those other two are completely valid.
For anyone to pick up, so, like… I'm just gonna put a comment to, create… I'll create… I'll just… I'll create new issues on these two ideas, and then we can follow up with those two, but these are… These are good. And I did pose this as a question, because I was like, I don't know, we talked about it, should we do it? It sounds like we still don't know, so I'm just gonna leave this as is.
And I think it is new… do we have new instrumentation? Yeah, that's also a label.
Right? This is, like, a question that would end up being an enhancement, and it concerns new instrumentation. I think there was al- was this one also new instrumentation?
No. Okay.
Alright, let's check out this one.
Oh, yes.
**Hanson Ho** 21:25 Yeah, if I remember, we looked at the implementation last week for this, right? I think… Yeah.
**Jason Plumb** 21:33 So this is the oldest PR, No, this is the issue. This is the oldest PR.
So the issue that it was resolving is… Carrier information missing for Wi-Fi connections.
Yeah, and what does this do?
Oh, did this just get… Dropped on the floor? Why?
Is this just sitting here?
Terrible.
That… It is wild. I feel really bad about this. I don't… I don't… hmm.
This makes me sad, but I appreciate you bringing this up.
This should not happen. This is really the oldest I'll open one.
Man, okay, well… That's bad contributor experience. It looks like we just ignored it. I don't understand why.
**Hanson Ho** 22:46 Oh.
**Jason Plumb** 22:48 And not… we didn't completely ignore it. I mean, to be fair, Jamie's like, yeah, maintainers, you should probably look at this.
And then… We didn't, so I… this is not great, yeah.
So, how do they change it? They say…
**Hanson Ho** 23:09 They added the carrier information.
If it existed.
**Jason Plumb** 23:13 Yeah… Yeah, so even on Wi-Fi.
**Hanson Ho** 23:25 Interesting. But that actually… say anything.
**Jason Plumb** 23:30 Yeah, this is great. I mean, I don't know why we wouldn't just take this.
Okay, let me respond and apologize and see if we can get these resolved.
Because its age means it probably needs some help.
But maybe I will just PR fixes, whatever those look like, into this branch.
And apologize. Okay, that's what I'll do. Oh, man.
Thanks for bringing that up, David. I don't know why that was ignored.
I mean, I wanna… I wanna give a little additional thought to whether the… existence of carrier information on a Wi-Fi object is confusing, but I… I don't… I don't know, I don't think so.
What is network state? Is that one of ours, or is that a built-in?
I don't know.
**Jason Morris** 25:02 Yeah, in this case, it's… yeah.
**Jason Plumb** 25:06 Yeah, so in this case, we'd be reporting Wi-Fi.
**Jason Morris** 25:09 Yeah.
**Hanson Ho** 25:11 I think this was what we were looking at last time, where, we're looking at, current network, and you may not be connecting to the one that is… or the current one doesn't have internet access, and you're actually going through some other one. We're saying, is that even possible?
**Jason Plumb** 25:31 Yeah.
Let me just look at this again.
Yeah, this seems… this seems fine. So, current network has that completely as an optional.
I think… Yeah, so carrier nullable. I think that's completely fine.
Because carrier is very much specifically not, like, about Wi-Fi provider or anything, it's about your SIM… your cellular carrier.
Yeah, this seems like a good change. I feel… yeah, that's… okay, I'll take that on.
Cool, thanks for bringing that up.
It makes me sad when stuff falls through the cracks, but… Doesn't happen all the time.
Okay, new issues.
Nothing new in the last week or so. How about PRs?
**Hanson Ho** 27:11 Oh, if we have time, we can maybe talk about whether we wanted actually to do this.
**Jason Plumb** 27:23 Yes, I have not reviewed this yet. Oh, yes, I have.
**Hanson Ho** 27:31 So I had a bit of time last week, and instead of finding the perfect thing to do, I just picked a thing.
This is… we talked about having an API that disables the signal, to get… provide no op implementations.
Rather than having no.
processors, which still goes through the whole SDK and incur the instrumentation.
looking at the code, there would have been an obvious way, which is to provide a no-op, tracer, when we actually create the SDK instance, but the SDK instance expects, an SDK tracer provider, things like that, and, those are not… accessible. The no-op provided is just a tracer provider and a logger provider, so to do this, you'd have to wrap it, and basically provide it at a different level.
So, the code is… is just a simple wrapper.
tried to not have it, but it kind of has to have that if we want to do this, unless… the SDK exposes an SDK implementation of NOP that we can then use.
So… Most of the changes is really, plumbing, and tests, so… But we do incur.
a… Slight bit of complexity by having to wrap it.
**Jason Plumb** 29:01 Yeah, so, I mean, this is interesting, though. I think that this is pretty low weight. I mean, I understand, I think, now that I'm waking up a little bit, maybe I don't understand where Scissor was coming from, but… This also seems… fine, right? A delegate where you can disable each individual one. In the event that it is disabled, you, when you get a tracer provider, you get the no-op version. I mean, I think that's… really what we had talked about, and I think metrics doesn't… Have one?
Is that… did you find this? Like, there is a NOAP meter provider?
**Hanson Ho** 29:37 Yes.
**Jason Plumb** 29:39 Cool.
**Hanson Ho** 29:40 I don't know what the implementation is, but it looks parallel to all the other ones.
**Jason Plumb** 29:46 Yeah.
**Hanson Ho** 29:46 I assume it's actual, truly an OAP, and not just a, A default that does a pass-through and just… Dev knows it.
**Jason Plumb** 29:57 I think that's a good idea. I think we should do this. Because I think… I think that's a better approach than we had talked about disabling the exporters.
**Hanson Ho** 30:07 I mean, it effectively… Yeah, if you disable the ex… if you can… if we don't set it in the default one, and they set one, it will go through the exporters, because there is a provider. This will stop it at the source, it doesn't basically pass it downstream.
**Jason Plumb** 30:24 And you're wasting… you're not wasting CPU, you're not wasting disk buffering, and all of that, so… Yeah, so I think the question was, does this already exist? Can… like, can we…
**Hanson Ho** 30:43 Unfortunately, no, there's a spot that makes it seem like you could, but what they're asking for is… is not in the shape that we need it to be. It's asking.
**Jason Plumb** 30:52 Really?
**Hanson Ho** 30:53 Yeah, it… said tracer provider requires an SDK tracer provider, and the… tracer provider no-op, returns a tracer provider. So… I don't know why it asks for an SDK tracer provider. That would be up to the SDK.
It almost feels like asking for a tuition provider ought to be enough, but obviously there's something in that interface that it requires.
**Jason Plumb** 31:22 Yeah, wait, where is this live? Yeah, so maybe that was just a mistake, though.
Again, this is not stable, we could change this, but you're.
**Hanson Ho** 31:29 Oh.
**Jason Plumb** 31:29 this…
**Hanson Ho** 31:31 Yeah, exactly, it's the OpenTelemetry SDK that's asking for it.
Like, the obvious thing here would be to replace Builder Provider with the no-op, but it doesn't… Interfaces don't mesh.
**Jason Plumb** 31:50 But there's a… there's still customizers, right? And the relationship… I don't know what the relationship is between… setting the tracer provider on the SDK builder versus having customizers.
Right, because there are… How do you searching this thing?
**Hanson Ho** 32:08 I think the customizers are, applied before, because the customizers are something that we provide, right?
**Jason Plumb** 32:18 We have a list of them, but then we provide them to the auto-configure.
Oh, no, we?
**Hanson Ho** 32:27 How can we apply them?
**Jason Plumb** 32:29 Yeah, no, yeah, you're right, yeah, interesting. We apply them before building the tracer provider. That really sucks. Oh, man, so… Huh. And there's probably no-op SDK, and, like, it wouldn't make sense for the SDK to have a no-op.
Like, that really is an API level…
**Hanson Ho** 32:50 No, no, the tracer… the tracer interface is part of the SDK package. This is something we talked about before, where, in the Kotlin, we wanted the tracer stuff, or the provider stuff. Okay. Actually, no, no, no, no, no, maybe that's not… maybe that's not right. Maybe I'm thinking about something else.
No, no, the, the, the exp… no, yeah, no, no, I was thinking about something else. Exporters and, and, and, and, and, processors is part of the SDK, surface, and not part of the API surface. So perhaps why the, SDK requires an SDK, tracer provider, not just a tracer provider, is that it needs something on… That has to do with exporters and processors in order to hook this up.
To do the… to do the, application of, of, of the customizers.
Because those tend to be related to that.
**Jason Plumb** 33:52 Okay.
**Hanson Ho** 33:54 Yeah, ad span process, so that would not…
**Jason Plumb** 33:57 Yeah, I think this is a good answer then, like, yeah, we wish we could do it that way.
But it's not really set up to… I'm with you on this one, Cesar, that is odd.
**Hanson Ho** 34:13 Yeah, I think when I first looked at this, I was like, I can do this pretty easily. And then… and then I looked at that, it's like, oh, it's not there, and then… As things go.
**Jason Plumb** 34:24 I think we should get this in the next release, I think this is good. In fact, let's do, since we have time… And I was gonna open it up to see if that person who was rejoining a few times wanted to say anything, but they've dropped off again.
I think we had somebody who I didn't recognize, who I had… I didn't see them on the agenda, and I didn't really… They were popping on and off, but let's… while we're at it, let's go and create… a milestone.
For whatever version we're on.
Just 1.5? Yeah, 1.5… Let's put this… because I think we're going to release next week.
And… let's put this in 1.5.
**Hanson Ho** 35:27 If we want to release next week, do we want to release Andrew or Kotlin as well, so we can get the set semantic convention? Oh, actually, never mind, because we need semantic conventions to update first before… We could update.
**Jason Plumb** 35:40 Yeah, were there any specific ones that you were thinking of?
**Hanson Ho** 35:42 Oh, the crash one, I wanted to… like, we've been trying to do that for so long.
**Jason Plumb** 35:47 Oh, yeah.
I don't think we'll be able to pick that up this time. I'm guessing it's gonna be another month.
**Hanson Ho** 35:53 That's fine, it's… the fact that the string itself has changed is the important part, so…
**Jason Plumb** 35:58 Yeah, in fact, where was that… Only because it was sitting out here for so long, I want to also just throw this in the milestone, but it looks like you cannot, once you've… yeah, you can.
Even though it's closed, I want to make sure we cut… Can include that as a thing.
And then, are there any other pull requests that we should get into this milestone?
Yes.
So there's… there's some timing that's gonna happen here. This is one of the, fortunately, rare cases where a change in core Has broken our usage of instrumentation.
So we need to wait for the instrumentation repo to release.
But this needs to be in the… this needs to also be part of the milestone.
And that'll depend on the… this… this can't merge until we get instrumentation released.
Which will happen at the end of the week.
**Hanson Ho** 37:03 What do we use for the instrumentation repo, the OKHTP?
**Jason Plumb** 37:07 Yeah, the API. We use the API for some… a couple of the…
**Hanson Ho** 37:10 Oh, okay.
**Jason Plumb** 37:10 HDP.
**Hanson Ho** 37:11 Okay.
**Jason Plumb** 37:15 We should just merge this.
How are we doing on this one? This would be nice to get in there.
But we talked about it last week, and then we proceeded to ignore it. Okay, I think… This would be nice to have as well.
Let's do it.
Cool, I think that's a good… I think it's a good start.
And maybe this one.
**Hanson Ho** 38:12 Yeah, all the, all the open, all the open… There's, like, the one above… also has been open since January.
**Jason Plumb** 38:27 Yeah, this one was contentious.
**Hanson Ho** 38:29 Okay, I haven't seen it.
**Jason Plumb** 38:34 Yeah, so they were… I think they were moving…
**Hanson Ho** 38:38 Oh, ew, yeah, that's problematic, actually.
**Jason Plumb** 38:42 I know, it's why it's tough.
**Hanson Ho** 38:44 Okay, nevermind.
We should respond, because he responded last, and…
**Jason Plumb** 38:51 Yeah, I'm curious now if this person is still active on GitHub.
Kind of.
Okay, yeah, hopefully they come back.
Cool. So that's looking okay, and then, yeah, again, I think instrumentation… will be… probably… it ends up usually being Friday and not Wednesday, so we can expect to release next week, which gives us a little bit of a buffer.
And then, I think… Yeah, so we should release… Next week.
Cool.
If there's anything else that comes up that you think should be… In that milestone, feel free to add it, and we can… hash out the rest of it next week. But I think that's a good start.
Oh, oh, oh, oh, there's also… This has been on my list for a while, and it's nagging in the back of my brain.
We want to stabilize this module.
Right?
**Hanson Ho** 40:11 Oh, yeah!
**Jason Plumb** 40:12 And we haven't done that yet, so do we have an issue for that?
**Hanson Ho** 40:15 Didn't we resolve?
the discussion.
This is… this is a while ago, wasn't it?
**Jason Plumb** 40:22 Yeah.
But if we scroll down, I think, Yeah, so I think we want to do this. So, he's got this milestone… called Stabilize Instrumentation API.
**Hanson Ho** 40:44 Document is the only one that's left over.
**Jason Plumb** 40:54 Yeah, we should do this, though.
**Hanson Ho** 41:00 Can we add a milestone to the milestone?
**Jason Plumb** 41:04 No, I don't think you can do that.
**Hanson Ho** 41:06 Okay.
**Jason Plumb** 41:09 I don't know how to do it.
But I'm gonna create another issue, which is to actually add the Gradle properties to make that stable.
And I'm gonna do it right now on this call, since our agenda's late.
And we can mimic what's done in the agent.
this thing.
**Hanson Ho** 41:59 Right. And this takes the alpha out of the version, but we keep the, the name of the artifact.
**Jason Plumb** 42:09 Exactly, it just drops the alpha.
**Hanson Ho** 42:14 And the bomb should change accordingly, so no one… if they're using the BOM, no one should… They shouldn't have to change anything.
**Jason Plumb** 42:23 You can only have one milestone.
**Hanson Ho** 42:30 Create a tracking issue that points to that.
**Jason Plumb** 42:33 Yup.
Alright, so then… Let's see… Nope, have to go into issue list, and then filter by milestones.
Then do… this… And then… We really want this. Yeah.
Okay.
That's kind of all I have. Has anything else hit the agenda?
It looks like no.
let's get reviews on some of these, and I will take my action items, and… We'll see you next week.
**Hanson Ho** 43:48 Cool.
I think this week is the, client.
Sig1 as well, so maybe I'll see some of you at 9.
**Jason Plumb** 43:56 Yeah, yeah. I think I can make it this week, so cool.
**Hanson Ho** 43:59 Alright.
**Jason Plumb** 44:00 Alright, take care.
**DavidGrath** 44:01 Sorry, quick one.
**Jason Plumb** 44:03 Yeah, yeah.
**DavidGrath** 44:03 June 2nd, sorry. You made it June 2nd, you've got to change it.
**Jason Plumb** 44:08 Say it one more time, sorry.
**DavidGrath** 44:10 If I go to modify the June 2nd copy, There's the detail copied.
**Jason Plumb** 44:17 I missed what you were trying to modify, again.
**DavidGrath** 44:20 You copied June 2nd over to today, and you forgot to change it to June 9th.
**Jason Plumb** 44:25 Oh, I did.
**Hanson Ho** 44:27 Oh, okay, right.
**Jason Plumb** 44:28 Yeah, thank you. No, that… I… Again, so early here, I'm barely awake.
Thank you for calling that out.
**DavidGrath** 44:37 Right.
**Hanson Ho** 44:37 Jason and… or the other Jason, the non-Splunk Jason, and David, maybe you want to… you can put your names in the, the SIG doc, as attendees as well, if you feel like.
**Jason Plumb** 44:51 Yeah, that's helpful. I mean… Just to also have the doc up in case something… while we're talking about something else, if something… stimulates, but also just to have a record of, like, who's been helping out and joining. It is… it's helpful to the organization… the larger organization, because, it shows that it's not just me and Hanson every time. And also, if we need to… like, jar the memory. Like, knowing who was on a given call is also really helpful.
Cool.
Thanks, everyone!
**Hanson Ho** 45:25 Okay, bye!
**Jason Plumb** 45:26 I…
