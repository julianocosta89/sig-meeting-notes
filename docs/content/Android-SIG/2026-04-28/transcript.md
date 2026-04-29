SIG: Android SIG
Date: 2026-04-28
Duration: 57 minutes
Zoom Recording URL: https://zoom.us/rec/share/hEovOXMoUy5CiJgflwk3l0ORpH2rFbPmIbYguI8S1hBgJTUvdEa7iwPiJ6fdRqc7.zGVezlL5sOFLIcKy
============================================================

## Zoom Recording Transcript

**Cesar Munoz** 07:10 Hello. Good morning.
And good afternoon.
**Jason Plumb** 07:20 Ann, good afternoon.
Just getting set up here, a little late to the meeting today.
Let's give it one more minute.
This one.
So, I guess we can jump in while people are joining. So, David, I looked at your PR, and I think it mostly looks good. I was wondering if there's anything else. I think, from the other reviewers, there might have been something, but I've… let's see.
I haven't approved it yet, but I gave you some feedback, it's looking good overall.
Yeah, so this is… this… this is non-blocking, right?
We can always come back and change the semantic conventions, so I'm inclined to merge this.
I think it looks pretty good.
The one thing that did occur to me is, can we get… and I can open an issue for this… So I'll create an issue after we get this one merged that is to add some sort of functionality into the demo app so we can detect this double tap.
And take a look at the telemetry and what it looks like.
That sounds good.
**Cesar Munoz** 10:10 Sounds good to me.
I'm just back from… PTO, haven't taken a look, but… as a first glance, and based on the comments, I don't think there's… I shouldn't… you shouldn't hold it.
For my review, because it's… I mean, it seems straightforward enough.
Yeah, so we can always, you know… this is an instrumentation, we can always, you know, update it, or something is needed, if needed.
**Jason Plumb** 10:40 Exactly.
Okay, that sounds good to me.
And… let's see… Cool, so, we also got the release out last week, it was pretty beefy, there was a bunch of stuff in it. I don't think we've had anyone… Raise any new issues, or any… Problems with the new one?
So that's a good sign.
And… Not too many new PRs.
would… be nice to get this one in. Are we still waiting on the semantic… yeah, we're probably still waiting on this one.
**Cesar Munoz** 11:27 Yeah.
I just saw earlier that… I think that Mila… Yeah, it's waiting for more approval.
So…
**Jason Plumb** 11:38 Okay… I didn't realize they have that.
Status, but okay.
**Cesar Munoz** 11:49 I'm guessing it's because of… Probably they want other platforms to look at it, maybe?
So far, only Andre has approved it.
I'm asking because I'm a bit… Confused.
What other people should take a look at it?
**Jason Plumb** 12:09 Yeah, so we have the client SIG after this, I'll ask people over there if they can do that.
**Cesar Munoz** 12:14 Thank you.
**Jason Plumb** 12:15 Yeah, and maybe we'll get some traction.
Because it's been out there for a while now, and it would be cool to move that forward.
Since February.
**Cesar Munoz** 12:26 Yeah.
**Jason Plumb** 12:30 Alright, well, what other PRs or issues are people thinking about?
Do we want to leave these ones out there for a little while still, Cesar?
**Cesar Munoz** 12:51 Nope.
Thanks for letting me know. I actually forgot about those.
**Jason Plumb** 12:56 Okay.
**Cesar Munoz** 12:57 I'll close them.
**Jason Plumb** 12:59 And then, what about this one? Might be in the same boat.
Where it was just implementation API.
**Cesar Munoz** 13:08 No, I think it's the same… threaten to the same thing. We were all proposing changes.
**Jason Plumb** 13:13 Yeah.
Okay… Yeah, this person has kind of disappeared, I think. They dropped some PRs, and a couple of them got merged, and these are kind of stuck, and they've… Not yet circled back. It looks like maybe this one did. Let's see…
**Cesar Munoz** 14:12 Yeah, there's a lot of comments, and…
**Jason Plumb** 14:15 for two weeks, but, like, is there anyone to review it? But I think he hasn't addressed… the stuff that's still open from Copilot, so… I don't know, hopefully they come back to this, but there's also merge conflicts now.
**Cesar Munoz** 14:36 Seems like they are… Probably, they're ignoring Copilot.
**Jason Plumb** 14:43 Maybe.
Yeah.
**Cesar Munoz** 14:47 But if that's the case, I mean, they can just resolve the conversations, or maybe add a comment. Which is something that we've all done, you know, the repos.
Kind of like saying, well, this is not… It does not apply for this and this, and… Yeah.
**Jason Plumb** 15:04 Yeah, this was also a large PR, so I think it does need more attention.
**Cesar Munoz** 15:13 Got it.
**Jason Plumb** 15:15 I think Contrib was going out yesterday. If it didn't happen, it'll probably ha- yeah, so it happened just 2 hours ago.
And then we should pick that up, cause… Oh, I don't know that there were any disk buffering changes, actually, in that. I think there weren't.
No, okay.
Well, it's unrelated to Android, but I… hopefully you saw this one, Cesar.
**Cesar Munoz** 15:40 I saw it, thanks for creating it.
**Jason Plumb** 15:43 Cool, cool.
Alright.
Clever Chuck, do you have anything that you're looking at that you want to bring up for Android today?
**Cleverchuk** 15:56 No.
**Jason Plumb** 15:58 Okay.
Well, hopefully for the next release, I mean, as far as, like, stabilization goes, I guess we should spend a few minutes talking about that.
And really, I hope it's the instrumentation API, I think is what our next target is.
Nope.
**Cesar Munoz** 16:28 Yeah, I think it makes sense. Yeah.
**Jason Plumb** 16:32 Which is really just this, right?
**Cesar Munoz** 16:36 Yeah.
**Jason Plumb** 16:37 And so, context is from Android, OpenTelemetry ROM is already stable.
And so there's nothing in this interface that would prevent us from doing that.
Okay.
**Cesar Munoz** 16:52 It's been a while since I took a look at it, but it seems like… It's just a matter of changing the, setting the Gradle property.
**Jason Plumb** 17:02 Yep, that's all it is.
**Cesar Munoz** 17:03 There's… there's nothing else to change, yeah.
**Jason Plumb** 17:06 Yeah, like, we have it for this one. It's one of these.
**Cesar Munoz** 17:10 Yeah.
**Jason Plumb** 17:11 Yeah.
But that'd be good to have in the next release. And then, we also have declared… In the last release.
the session API stable.
**Cesar Munoz** 17:24 Yeah.
which is already deployed the release.
**Jason Plumb** 17:29 Yeah, yeah. Yeah. So that's progress.
**Cesar Munoz** 17:32 That's great.
**Jason Plumb** 17:34 Yeah.
**Cesar Munoz** 17:40 I mean, after we… Oh, yeah, go ahead, clever show.
**Cleverchuk** 17:45 Yeah, I was gonna ask, about declarative config.
Is Android gonna consider that?
**Jason Plumb** 17:52 So I have… it's funny you should ask that, I have had, on my little personal to-do list for, like, 3 weeks, I've had 2 items on there. One is to create an issue for declarative config on Android, and the other one is to create an issue for declarative config on Kotlin. So, yeah, I think we will. I think we need to. I don't think we're there yet.
I think it will… I think it'll be some time before we can really dive in on that, but… We definitely need to consider it, I think people want it.
**Cleverchuk** 18:23 Okay.
**Cesar Munoz** 18:24 I think it was Julia.
**Cleverchuk** 18:33 And about the Kotlin SDK, how's that effort going?
You guys know.
**Cesar Munoz** 18:46 I haven't been involved, but I think Jason… She'll have some… some insights.
**Jason Plumb** 18:54 Yeah, so it's coming along, we're working towards stabilizing the first API.
So just to sort of recap, right, this is the, Kotlin language-only… API implementation with an SDK that can both be used on Kotlin Multiplatform.
Which means that you cannot normally have any JVM or Java code in the project if you want to target multi-platform.
there is currently an API, and an SDK in Kotlin, but the API in Kotlin can be backed by one of two implementations, SDKs, the existing upstream Java SDK, or the one that's being fleshed out.
And currently built and is not complete yet in Kotlin.
So the first thing we're working towards stabilizing, and I think… Jamie has done a pretty good job of putting milestones on these things.
So we have… some… these really are, like, stabilization milestones, but if you look, I think logging is pretty close.
I think logging API will be the first one that gets marked stable, and then we'll probably work toward tracing next.
So it's coming along. We could use some help if anybody's interested in joining that. There's a lot of issues, as you can see. They're all relatively small, and there are a lot of, like, kind of edge Casey-type areas around, spec compliance.
So making sure that it's both still idiomatic Kotlin and adheres to the specification.
And it's moving forward, and we have… we have SIG meetings on Mondays, if you want to join that.
Even just to listen in, or watch the recordings, or whatever.
**Cleverchuk** 20:48 Cool. Thanks.
**Jason Plumb** 20:50 Yeah, and you know, somewhere down the road, we'll switch over Android to… using that. There was a prototype, I think, that Jamie submitted, like, a few months ago that just shows, like.
what using the API would look like, even if it's still backed by the JVM version of the SDK.
**Cesar Munoz** 21:12 Everything's moving pretty, pretty quickly, so…
**Jason Plumb** 21:15 Yep.
**Cesar Munoz** 21:16 It's good stuff.
**Jason Plumb** 21:17 Yeah, we're pretty… we're pretty bullish over there about trying to get stuff stable pretty quickly. And we have someone from… we have Carlos, helping out with, spec review, because he knows the specification very well.
Yeah, do you all have users that are asking for stuff in Android that's not there yet now? Or are people pretty happy with it? Do we have a sense of this?
Not sure.
**Cesar Munoz** 21:58 I think most of the… No, most of the time, they just want… You know, cross-reporting and… an HTTP spans.
**Jason Plumb** 22:10 Yup.
**Cesar Munoz** 22:10 Those are the two favorites.
there's something that somebody asked in the OTL Android Chat, group chat.
about… Crashes that are obfuscated.
Which is normal in Android.
But, it's… it's… Like, sometimes I try to… like… I'm not sure if it's inside the scope of what OTEL can… address, you know? Because it's like… It's a way to see the data.
Later.
**Jason Plumb** 23:00 Right.
**Cesar Munoz** 23:01 That it's readable for you.
Right. It's got nothing to do with how you collect the data, and, you know, what are the, attribute names, or stuff like that, so… I'm not sure it's something we could do anything about on the Asian side, but that's also something that I know people Are very interested in.
**Jason Plumb** 23:29 Yeah, I think, I think we, Splunk, have a thing that allows people to upload the de-obfuscation file, right, which is like a build time artifact. I think that's a pretty common approach.
And I agree, I think I agree that it's not really in scope of this project to do that, unless there's something we could do that Helps to make generating those files easier, or packaging them easier, or uploading them easier, but it's not really… There's no real OpenTelemetry solution for that, so… It does seem like it's outside the scope of this project.
To me.
**Cesar Munoz** 24:09 Yeah. Yeah, no, I understand.
**Jason Plumb** 24:13 And whatever that file looks like, it's not gonna look the same as on the web or on… iOS or any other platform, it's gonna be very Android-specific, I would imagine.
**Cesar Munoz** 24:23 Yeah.
Yeah, what I understand, oh, for iOS, it's not even… It's not readable, it's just a binary plot, so…
**Jason Plumb** 24:33 Yeah.
Yup.
Well, I think that, you know, the agenda's pretty light, so I will hang out and just… we can just chat for a little bit. I certainly understand if people want to drop. We don't have to take the full hour, but maybe I would just cruise through open issues and do a little triaging, sort of on the fly, and if something looks interesting, we can talk about it, and if people want to drop.
No hard feelings. So… How does that sound? Sound good? Looking at this one, this seems a little old now, so… They were using the RUM builder directly and calling Build, and they… seem to not be getting the session provider. Is this… this cannot still be true, can it?
So this person… seems to be having the same problem.
And they are bypassing the agent because they want the tracer provider customizer To add a span processor.
**Cesar Munoz** 25:45 Oh, but look at that, it's for… seems to be for global attributes.
**Jason Plumb** 25:49 Yeah, but maybe that's their own thing?
I know, yeah.
**Cesar Munoz** 25:53 I mean, if it's a thing about… if it's about attributes, they can also… Pass something to the agent.
I think a supplier or something for attributes, right?
**Jason Plumb** 26:05 I think so.
But this is… this should still be a valid use case, like, using the Room Builder directly, for whatever reason.
And then… We should… we should still be generating sessions, so…
**Cesar Munoz** 26:21 The thing is that the sessions I mean, they, they, they need, like, a life cycle and a, you know, a decision-making and stuff, so we put all of that code in the agent, because it's all opinionated.
**Jason Plumb** 26:41 Yes. Yeah.
So they would have to recreate that, basically. Like, they would need to… Like, where is that code? So that's in… the initializer…
**Cesar Munoz** 26:58 Yeah.
**Jason Plumb** 27:02 Right, so they can call this, but they probably can't create one, huh?
Like, this is on the OpenTelemetry Realm Builder.
No, sorry, this is on the Rum Builder.
**Cesar Munoz** 27:16 Yeah, and their passing decision provider. Well, we are.
But we're passing our… Implementation of it.
**Jason Plumb** 27:25 Yeah, and they're saying there's no implementation available, and that's… That's true, right? Because it's internal? Is that… is that internal?
**Cesar Munoz** 27:33 I think so.
But it's in the agent.
**Jason Plumb** 27:37 Oh, it is. Okay, so this is the API, but the only implementation is in the agent.
**Cesar Munoz** 27:43 That's my understanding, yeah.
**Jason Plumb** 27:46 No, not there.
**Cesar Munoz** 27:48 This is the API.
**Jason Plumb** 27:50 Sorry.
the… agent.
Here, you know.
**Cesar Munoz** 28:02 There it is, the manager.
**Jason Plumb** 28:07 We could make this its own module.
**Cesar Munoz** 28:12 You mean, like, our opinionated session provider implementation?
**Jason Plumb** 28:18 Yeah…
**Cesar Munoz** 28:19 For when people don't want to use the agent.
Sounds a bit…
**Jason Plumb** 28:25 It would be the same… it would be the same one that the agent uses, but it would be made available for other people to use if they were using the builder.
**Cesar Munoz** 28:33 Yeah.
**Jason Plumb** 28:34 I think it's important for us to be opinionated about this, but it would help if we had some consensus in… The semantic conventions or the spec.
About session.
**Cesar Munoz** 28:47 True.
Which is probably why we… Kept it internal.
**Jason Plumb** 28:53 Yep, I think… Hoping, yeah.
Yeah, but if we made this its own module, we could still mark it experimental, and then people could use it, it just would not be stable yet.
**Cesar Munoz** 29:07 True.
I mean, it will definitely be helpful, I'm just not.
**Jason Plumb** 29:13 Yeah.
**Cesar Munoz** 29:14 how… how much?
You know, because it's… like… seems to be a bit of an edge case. If that use case that the user was mentioning of them having to use the builder because they had to use the trace customizer just to add global attributes, then they don't need to use the builder for that, because the.
**Jason Plumb** 29:39 Yeah, that's true.
**Cesar Munoz** 29:39 She'll allow them to do the same.
So…
**Jason Plumb** 29:43 There's another person that has the same scenario, that they said they want span processors.
Which, this is custom.
Inc.
**Cesar Munoz** 29:51 Yeah.
**Jason Plumb** 29:52 And is… there's probably no way to add a span processor in the agent? I can't remember.
**Cesar Munoz** 30:01 I don't remember, but I don't think there is. But probably… Hmm…
**Jason Plumb** 30:10 Not here, in the initializer.
In the DSL, maybe.
**Cesar Munoz** 30:31 You're more familiarized with the Kotlin SDK than I am, so maybe… You know, I would like to… Hear about you for this case.
I think a while ago, we were discussing about, you know, when we were talking about the Kotlin SDK and migrating Autelandroid to it in the future.
That probably whatever is in core right now.
You know, the builder, which is all super generic.
might be all replaced by the Kotlin, SDK… You know, tools and constructors and stuff.
So, if that's the case, then… Maybe the… our focus should be to try and, Make the agent as flexible as possible.
And then probably avoid people from using Core directly in the builder.
**Jason Plumb** 31:38 That… I like that idea quite a bit, is to have a rich feature set in the DSL and the agent.
And then be able to swap core out at some point.
Because hopefully the agent is accounting for most common use cases. Like, we kept… we kept Core exposed as, like, a fallback for people that didn't want to or couldn't use the agent for these weird edge cases.
To me, a span processor does not feel like an edge case. That feels like a pretty common thing.
And so, if we don't have that, we should probably consider… adding it. I thought it would be in here, but I don't see it.
So there's the OTel Rum config, but I believe that that's not exposed, right?
That's from CORE.
**Cesar Munoz** 32:30 Yes, that's… It's from core, that's… yeah, as far as I remember, it is. If we haven't moved it.
I mean, I agree, I mean, if it's needed to have the processors To be able to add processors, then we should add it.
So, now, I'm just not sure if that's… actually needed. I mean, if all people want to do is to add attributes.
Then they don't need to pass a processor.
**Jason Plumb** 33:04 Yeah, I don't know what these other use cases. There's some Datadog one, and there's a logging one, and there is… I mean, you could log it… like, you don't need a spam processor to log it, you can do that with an exporter. That's what… that's the intention, is to be able to log… With a logging exporter, so you would compose and have a multi-exporter, one that logs and one that does whatever we do today.
And then… User context is probably, like, application-level stuff, where, like, a user has logged in, and then they want to carry that forward.
**Cesar Munoz** 33:36 Yeah, I mean, I think… But again, these only… More info from these people.
**Jason Plumb** 33:43 Yeah, and it's been a few months now, so it's probably good to circle back on this. I don't want to close it yet, because I think there's some interesting things floating around here.
**Cesar Munoz** 33:52 I agree.
**Jason Plumb** 33:53 The risk, or one of the challenges with just using span processors for all this stuff.
Is that not all of the telemetry is spans.
Right? It's like a… it's a smaller portion now. The stuff that is spans is, like.
some lifecycle stuff and HTTP, but, like, there's a lot of events that wouldn't… these wouldn't apply to at all.
You know?
**Cesar Munoz** 34:17 Yeah, unlike our… current supplier of attributes, which Goes to both logs and spans.
**Jason Plumb** 34:25 Yeah.
**Cesar Munoz** 34:27 the, also, my… a concern, another concern of mine.
will be… well, I guess depends on how we wire… wire it up later.
Is that maybe people add, Something that they want to get exported, but then it probably does… it doesn't, because the exporter is attached to Our processor, not the one that they provide.
But I guess that's just a matter of… adding our processor last.
And, maybe it'll work.
I guess to, you know, to make things… simpler, or to keep things short, I'm all up for adding more stuff.
To make it as flexible as possible.
Cool. You know, but if… but if it's needed, because it's, like, if it's, like, just people not knowing that they already can do that.
Without that big of a hammer.
then… you know, If it's not needed, then… It shouldn't be added.
**Jason Plumb** 35:47 Like, the global attributes being one example of that, yeah. I agree, and, like, the logging thing, like, this is not necessary, you can deal with an exporter.
**Cesar Munoz** 35:56 Yeah.
**Jason Plumb** 35:58 I wonder, too, if, you know, we're at a stage now that we're starting to stabilize these components, and we have the DSL, if it makes sense to… Start documenting some common patterns, like, like… hey, I want to do X, like, here's how you do it using the agent. Like, having some… prescriptive recipes, or something might be nice in docs.
**Cesar Munoz** 36:24 Yeah, that sounds good. I mean, if we don't have it there yet… Yeah.
Broadly, something we can add into the, into the demo app.
If it's not there yet.
**Jason Plumb** 36:43 Yeah, and I don't want the… I don't want the, the… I love the demo app, and I think it's really demonstrative, and I think it's super helpful, and we should keep it around, and maybe one day we should migrate it to the OpenTelemetry demo project? I think that's… we said, like, 2 years ago, almost, that that's where it would live.
And we haven't made more progress on that, it would be nice to… it's nice to have it here as well, so we can just add features and just test it, like, alongside of our code.
But really, this does want to live in the OpenTelemetry demo project.
Which is this one.
I don't know if they saw that diagram. There used to be a massive diagram in here about… The way this thing looked.
Maybe it's on this, this site.
Not anymore. But, I mean, just look at the number of services in this thing, it's like, there's so many. And it covers a bunch of different… Parts of the ecosystem.
and a ton of different languages, and having Android in here, too, would be great, like, as an alternate front end, right? Front end's a web.
**Cesar Munoz** 37:59 I mean, they're… they start… they start reacting negative. So, yeah, I think it makes.
**Jason Plumb** 38:03 Yeah, exactly.
**Cesar Munoz** 38:04 Brown, good to be here.
**Jason Plumb** 38:06 Yep. Anyway, what I was getting at is, like, I don't think our docs… our docs are great, but it's just, like, they're pretty fresh, and… You know, it gives Anne example.
Right? Of how to use the initializer.
But it doesn't really talk about specific use cases or how to do things.
So I think it… I think it would be probably a pretty welcome addition to have some better docs around that stuff.
**Cesar Munoz** 38:39 You mean, like, another repo with recipes, or… or maybe just a how-to section of the…
**Jason Plumb** 38:47 I think just… I can think it can fit under here, under Android, and just be like, how do I, or common use cases, you know, something like that.
**Cesar Munoz** 38:56 I see him.
Yeah, sounds good.
**Jason Plumb** 39:05 Well, that's cool. So we got all of that by looking at this issue, but we should probably respond to them and be like, hey, now that we've got.
**Cesar Munoz** 39:12 I'll be honest.
**Jason Plumb** 39:12 kind of stabilize? What use cases remain?
But also, span processor seems pretty reasonable to me. Anyway… Let's look at other areas.
**Cesar Munoz** 39:22 I mean, we… we can add it, it's just that if it's just for the attributes, it's like… I mean… I don't see…
**Jason Plumb** 39:32 Yeah, and I… I added bug to this, but now that we've read through it and talked about it more, I don't know that it's a bug, it's just, like, a gap, maybe. It's like, they had an expectation that the session manager would be wired up automatically, or that they could wire it up, and it's just not… The case today.
**Cesar Munoz** 39:47 More like an enhancement, then.
**Jason Plumb** 39:49 Yeah.
I'm gonna change that.
**Cesar Munoz** 39:53 I'll… follow up.
In the comments there.
**Jason Plumb** 39:58 Cool.
So those… as far as bugs go, those are the only two.
This one is just, you know, coroutines.
Yup.
Someone would need to really dig in and look at what it would take to handle this, because it's super complicated.
So I don't want to talk about it. I don't want to think about it. The… so the other labels that we have, I think, are… DSL enhancements.
Nothing there today.
If we look at enhancements, there should be a ton.
Let's start at the bottom, let's look at the old stuff.
23! Oh my gosh, time flies.
Oh, I don't even understand this one.
So, this person's been around for a while, I think.
I think they've helped out, so it'd be cool to get their feedback on this, like… Can you come up with a demo that shows this? Like, can you…
**Cesar Munoz** 41:38 Okay, so I think it's talking about, He doesn't want to see traces… or records errors.
Which I'm not even sure that's still a thing.
Give it that those were events.
**Jason Plumb** 41:53 Right.
**Cesar Munoz** 41:54 To ignore those, in some cases, Specifically, he's talking about coroutine.
Issues.
Coroutine-related errors.
It sounds quite, edge Casey.
Yeah.
**Jason Plumb** 42:20 But given the age of this, I think I'm just gonna reach out and say, hey, is it still relevant?
We'll put the, needs author feedback on it.
And then we'll go from there.
But yeah, if this is still relevant, hopefully they come back around.
**Cesar Munoz** 42:37 Yeah.
**Jason Plumb** 42:39 More coroutine stuff.
This is from you, Cesar.
**Cesar Munoz** 42:50 Right. Alex, this is just so old.
**Jason Plumb** 42:56 Yeah.
**Cesar Munoz** 42:57 So… I guess, long story short, the… context… When you create a span outside of a quarantine, doesn't… leak into the coroutine. And so… Like, in the code, did you see that the quarantine It seems to be something that you launch from, like, regular code.
But then, it's kind of strange that maybe you create a span within the coroutine.
And you had a span outside of the quarantine, and then they are not, like, linked together as a, you know, parent-child kind of.
**Jason Plumb** 43:39 That's right, because the propagation… the local context propagation is broken across coroutines.
**Cesar Munoz** 43:45 Yeah, so…
**Jason Plumb** 43:46 packed across coroutines.
**Cesar Munoz** 43:49 And the Java SDK has a way to address this. It's just that it's in a… No, well, I mean, they… no, they do… they… they have a, an artifact only for coupling coroutines.
That allows you to… inject a… Context into a coroutine.
an open telemetry context into a curriculum.
**Jason Plumb** 44:14 Okay. Okay.
**Cesar Munoz** 44:17 And, it works, but it needs you to… it needs users to do this manually, so that issue that I created was to do this automatically.
**Jason Plumb** 44:33 Got it. Okay, so here's the extension that does that.
**Cesar Munoz** 44:38 Yeah.
**Jason Plumb** 44:40 Got it.
**Cesar Munoz** 44:49 So this is an idea for an instrumentation.
**Jason Plumb** 44:52 Yep, enhancement. That's cool.
**Cesar Munoz** 44:55 Which, to be honest, I just forgot about, and… Never…
**Jason Plumb** 44:59 well.
**Cesar Munoz** 45:00 choke that aid in anymore.
**Jason Plumb** 45:01 There's plenty… there's plenty… there's plenty of stuff out here.
Low memory events, that's help wanted enhancement, you know, it'd be good new instrumentation.
**Cesar Munoz** 45:19 I mean, now that the API is basically stable, it's a nice moment to start creating those.
**Jason Plumb** 45:27 Yeah, if people have cycles to start building stuff, that would be great, yeah. New instrumentation.
So when session expires, they want to get called back.
Well, we have an interface for that. It's called the Session Observer.
**Cesar Munoz** 45:47 Observer. Yeah.
**Jason Plumb** 45:50 Okay… And they're saying…
**Cesar Munoz** 45:53 Yeah.
**Jason Plumb** 45:54 To be able to do cleanup of something, okay.
**Cesar Munoz** 45:57 That should be possible now.
Actually, with the latest release.
**Jason Plumb** 46:01 I agree.
So I said this back in 2024, we do have this observer in place.
**Cesar Munoz** 46:13 Yeah, but it was not accessible to… Outside of our code.
**Jason Plumb** 46:17 But it is old. But now it is.
**Cesar Munoz** 46:19 Yeah?
**Jason Plumb** 46:23 So…
**Cesar Munoz** 46:23 It is now, but as in, like, The latest release.
Oh, it's brand new.
**Jason Plumb** 46:29 Oh, was it part of that release?
Yeah?
Let's see…
**Cesar Munoz** 46:38 Well, when we stabilized sessions.
**Jason Plumb** 46:42 Yeah.
**Cesar Munoz** 46:44 we stabilize that observer, and also, I think we now provide the provider, session provider.
**Jason Plumb** 46:52 But it's also probably in a DSL now.
**Cesar Munoz** 46:57 Hmm… I'm not sure.
**Jason Plumb** 47:00 Or maybe it's in here.
No, that's the implementation. The DSL… This one, right?
There's no callback on this one.
Is it session?
I don't know, maybe there's no way to do it.
**Cesar Munoz** 47:28 Let me check.
I mean, we can… we can add a DSL option now.
**Jason Plumb** 47:34 I mean, if we.
**Cesar Munoz** 47:34 be pretty trivial.
**Jason Plumb** 47:36 Yeah, people want this, though.
**Cesar Munoz** 47:39 The thing is that, you know, it's been a long time, and there's been a lot of changes.
And back in the day, I think it was not as easy as it is today. So…
**Jason Plumb** 47:50 Yeah, I agree. It'd be cool to, again, have an example, like, if we had this documentation area.
One of the things could be, how do I monitor for session ID changes? Like, I want to get notified, how do I do that? And showing that wired up to the agent might be nice.
But I don't know if you can do it today.
**Cesar Munoz** 48:15 Well, you can… But it's, it's, so… So, here… Well, it's not straightforward. It's probably better… it's probably best to add an option to the DSL. If you open the link that I sent.
So essentially, people could, cast that type.
from the ROM instance to an observer.
And then… Use it as an observer, observable… I forgot.
Codish, or something.
**Jason Plumb** 49:00 Yeah, there's kind of 3 interfaces, right? The provider.
And the publish… no, the publisher and the manager, is that right?
Can't keep this straight. Nope.
**Cesar Munoz** 49:13 No, the manager, it's the implementation of both.
**Jason Plumb** 49:16 Okay, so there's the… there's the provider and the publisher.
So the publisher is what notifies the observers, like, you register your observers with it, and the provider is the one that provides the actual session ID.
**Cesar Munoz** 49:30 And our manager is both.
**Jason Plumb** 49:33 And our manager is both.
So, they would need to cast that thing that you sent, they would need to cast this provider as a manager, and then call adobserver.
**Cesar Munoz** 49:43 Or as a… or as a publisher. But yeah.
**Jason Plumb** 49:46 Which is super clunky.
**Cesar Munoz** 49:48 Yeah, it's… yeah.
Yeah, it's probably better to add it to the DSL.
**Jason Plumb** 49:58 I'm gonna make a note of this one in the meeting notes as well.
**Cesar Munoz** 50:05 Yeah.
Thank you.
**Jason Plumb** 50:29 Okay… It is kind of fun to go back and see these old issues. I haven't done this in a little while, so… Compose navigation, we have some of this, don't we? Or, no, we just have Compose Click, right?
Yeah, this is… this…
**Cesar Munoz** 50:53 Right.
**Jason Plumb** 50:54 This is super complicated.
**Cesar Munoz** 50:57 The thing is that composites… It's… it changes a lot, so I'm not sure…
**Jason Plumb** 51:03 Yup.
**Cesar Munoz** 51:05 And I think we actually have what you said, we had Compose Click, But then it only worked.
with a specific version of Compose, and then it broke.
But then it got fixed again, like, out of the blue.
In a newer version, so…
**Jason Plumb** 51:25 Yeah, and I mean, the very concept of navigation doesn't fit nicely into the Compose model anyway, right? Like, within Compose, you can swap out entire parts of the screen, but it's not necessarily a navigation. Like, you're not going from one page to another. You're just making changes within the current page, so… Like, conceptually, navigation is a weird concept.
I remember.
**Cesar Munoz** 51:50 Yeah, unless we all agree on what we want to define as navigation, and then we're from that.
**Jason Plumb** 51:59 Yeah, look at this milestone. Oh man, stabilizing… I forgot we had this milestone.
Instrumentation and API stabilization, which is what we think we're gonna do in the next release, right?
**Cesar Munoz** 52:15 Well, yeah?
I think the second one, it's… It's done already.
**Jason Plumb** 52:22 Yeah…
**Cesar Munoz** 52:24 Yep.
I forgot to close it… close it.
**Jason Plumb** 52:27 I will let you close that one.
**Cesar Munoz** 52:30 Yeah.
**Jason Plumb** 52:32 And then… document the config process. That seems like a good idea.
Yeah, that's cool. And then… You know, this is a nice-to-have… I don't think we have this yet, do we?
Once again, I'm referring back to the DSL to remember if there's a way to do it, because it's not fresh in my brain.
**Cesar Munoz** 53:14 I don't remember.
**Jason Plumb** 53:34 Let's just assume there's some random third-party instrumentation on the class path, and the loader would find it, and by default it tries to load it, right?
But there's a… there's a flag to tell it not to automatically find stuff, right?
**Cesar Munoz** 53:49 Yeah, but I think that's only in core.
I'm not sure if it's in the DSL yet.
**Jason Plumb** 54:00 Okay, I'm just gonna make a note of that to visit that as well, because I think that's a pretty good… Thing to investigate.
**Cesar Munoz** 54:09 Yeah.
**Jason Plumb** 54:22 Which is part of this. Which is part of this milestone.
Alright.
Yeah, migrating… migrating more stuff to build time is also pretty interesting to me. I think having… I know, Cesar, you've done a lot of work in the past with, like, some Gradle plugins that do some of this.
I think… I think this is pretty cool.
with span comes from the Java world, you know, but we could build an equivalent that if a user in their application code wants to wrap certain parts of their business logic with a span, this is a really convenient way of doing it, but we don't have bytecode weaving, so it'd have to be kind of… Build time.
And… not everything would necessarily want to be a span. Some people probably want events around things, too. So it's just interesting to think about building these kinds of things.
**Cesar Munoz** 55:45 Which will be an instrumentation.
It would.
**Jason Plumb** 55:48 Yep.
**Cesar Munoz** 55:50 I think we thought about it for a second, and then somebody came up with the question, what… what do I do? What should we do when the width span… Annotation is applied to a method that launches a coroutine.
**Jason Plumb** 56:06 Yeah, I'm sure, yeah.
**Cesar Munoz** 56:08 shield this bank cover. And I think… It's, Yeah, and we're talking about… we're talking about Kotlin plugins.
**Jason Plumb** 56:21 Yes.
**Cesar Munoz** 56:21 To, to do the implementation.
**Jason Plumb** 56:24 Yep.
**Cesar Munoz** 56:25 I think this person… was… volunteering to create a POC, but I think they never came back.
**Jason Plumb** 56:35 Yeah, okay.
**Cesar Munoz** 56:37 But, I mean, we can start simple and just ignore coroutines and presentation.
**Jason Plumb** 56:44 Yeah.
Yeah, it'd be cool to see what that looks like, and if people want to use it or they like it.
**Cesar Munoz** 56:51 Yeah.
Yeah, that would be a cool one to have.
**Jason Plumb** 56:58 Well, I might get some more coffee before the client SIG meeting.
**Cesar Munoz** 57:05 But it was, it's a good idea to revisit these old issues.
**Jason Plumb** 57:11 Yeah, I think it was kind of fun just to, like, have an open agenda and just kind of do this ad hoc.
Yeah, and also free stuff, too.
**Cesar Munoz** 57:19 It's also because some of them are already solved, or now have ways to get solved, so… Yeah.
**Jason Plumb** 57:26 Yeah, totally.
Well, cool, there's always lots to do, and I appreciate everyone who's here to help out with it.
**Cesar Munoz** 57:37 Yeah, me too.
**Jason Plumb** 57:38 Alright.
**Cesar Munoz** 57:39 I'll talk to you later.
**Jason Plumb** 57:40 Yeah, have a good rest of your day, y'all, thanks, appreciate you.
**Cesar Munoz** 57:43 You too.
**Jason Plumb** 57:44 Alright, bye.
