SIG: Kotlin SIG
Date: 2026-04-13
Duration: 36 minutes
============================================================

## Zoom Recording Transcript

**Hanson** 01:29 Hello?
I think Jason is out until the 20th, So, I don't think he's coming to date.
**Jamie Lynch** 01:41 Yeah, I think EE mentioned that last time.
Oh, I guess we can give it a couple of minutes and… See if anyone else shows up.
**Hanson** 01:50 Sure.
Carlos, came last time, so he might come today as well.
I finally did the action item I had, from last week about posting about the, No-op implementation, inclusion, We can discuss that further.
I'll add to the agenda.
I think Carlos was supposed to ask, the TC as well.
**Jamie Lynch** 02:51 Cool. I guess we can just make a start and see if anyone else does show up, but this might be a quick one.
**Hanson** 02:58 Sounds good.
**Jamie Lynch** 02:58 Cool. So, first item, the release workflow is failing due to some new branch permissions that were added.
So basically… Let me see if I can bring it up.
**Hanson** 03:15 Is it the ones that Jason added for read permission stuff?
**Jamie Lynch** 03:19 Let me see if I can find the workflow.
What's in here? No one's… As in preparing release French.
Yeah. So, two of the workflows passed, basically, and… After… Some, amendments to the boundary protection, basically.
But OpenSelemetry Bot is no longer authorized to push to a branch.
Yeah, so… I guess.
first thing to check would probably be whether OpenTelemetry Android is actually doing this as well.
Because I've basically just taking the workflow from there.
So yeah, I think the options were… Remove the branch protection for release branches.
Or… have a look at what OpenTelemetry Android is doing.
**Hanson** 04:39 I want to say explicitly this was added, we discussed this last week, or maybe it's on Slack or something like that.
But, it was desirable to protect, release branches. So I would imagine either, there's some other way for Android to get around this.
or, there is, where they're not using the same level of automation.
Either way, if this was taken directly from Android, that should be the case. So there must be special permissions, granted, or some sort of override.
Because, yeah, Jason, detected this, and figured, oh yeah, we should protect it, and it's like, yeah, that makes sense, because… In fact, that is probably the vector to get bad stuff out, is through the release branches. So, it does make sense to protect it. So, we can take a look at what could be going on there.
**Jamie Lynch** 05:52 So I guess another possibility is that this is also an issue on OpenTelemetry Android, but we're just not running into it yet.
**Hanson** 06:01 Possible.
**Jamie Lynch** 06:03 Since we've released there.
Yeah, I guess we could… like, that's an action item, I'd be happy to go check out what OpenSlundry Android is doing, first off, and…
**Hanson** 06:17 Yes, sounds good.
**Jamie Lynch** 06:19 Ben can discuss async.
**Hanson** 06:23 Hey, Carlos.
**Carlos Alberto Cortez** 06:24 Hey, hey!
**Hanson** 06:32 Cool. While you're here, curious to know if you know about, any of the branch protection stuff or release branches for the other repositories, because we're running into some, workflow issues, with… with permissions and branch protections on the release branches. And we… we're taking stuff away… we're taking workflows from OpenSelf to your Android, and they don't seem to be having that problem. Do you know if there's any special bypass or permissions that are necessary for the bot account, in order to merge directly into the release branches?
**Carlos Alberto Cortez** 07:02 No idea myself, yeah. I can do a follow-up, or try to ask to other maintainers in case they have seen similar situations, but yeah.
**Hanson** 07:12 That's alright, I think one of us will go and look at the Android repo and see what's going on.
**Carlos Alberto Cortez** 07:17 Yeah.
Make sense?
Otherwise, happy to help, yeah, but yeah, no idea.
**Jamie Lynch** 07:27 Cool. Next item, basically, I wanted to carry on with the logging API stabilization discussion. So, I wasn't here last week, and I think there were some… There was, like, some discussion on that, so… Yeah, it'd be just cool to… Pick that up, basically.
**Hanson** 07:50 Yeah, so the summary is that basically the logging API, depends on a bunch of other APIs that, like context and things like that, that themselves need to be stable for the logging API to be stable. And, And if we wanna… Excuse me.
declare logging API, stable without, say, declaring tracing API stable, they need to be in two separate repos, because the repos tend to be, you know.
declared stable on its own. And looking at what the dependencies are, what the unique things about Logger API actually is, that in and of itself is not controversial. It's things like the attributes, it's things like context. So, by the time we get all of that, The difference between… doing tracing and logging, and doing logging separately, is… is… is some non-controversial tracing stuff.
So, the idea is that if we want to do it separately, we can, but we'd have to, like, put it into two repos, and then do it that way. I think what I was maintaining in the last meeting is If the difference is… like, if we have to do… jump through all these hoops just to get one stable and the other stable, like, in a week or whatever, we might as well do these two together, because the hard work, the blocking work, really, is the common stuff.
Like, attributes and, and, and, and, and context and stuff like that, so…
**Jamie Lynch** 09:22 Got it. That's… that's helpful.
Sorry, gone.
**Carlos Alberto Cortez** 09:27 Yeah, also I could say that, there are many things of even if you have logging API by itself, things that have to be implemented in all cases, that may affect all signals, and context is one of them, the second one is baggage, which you started working on.
And basically those two things, for example, you know? So yeah, I would say that that's also, like, the explanation, and just to be clear, it wouldn't have to be two different repos, but at least two different artifacts. But still, it's a lot of work, you know, to be able to release Those things separatedly, yeah.
**Hanson** 10:05 Yeah, sorry, I meant two artifacts, because we only have one repo for everything, but we have, you know, a handful of artifacts, so…
**Jamie Lynch** 10:13 Cool.
Yeah, I guess from my perspective, my reference would be… just addressing… what is needed to get, like, the shared things, like contest, attributes and baggage, kind of, like, agreed upon, and then we can just all declare it stable.
When it makes sense. Yeah, I've just raised a question, because… I noticed there wasn't too much to do on the blogging interface itself, but if there's more to do, that's fine.
**Hanson** 10:49 Yeah, basically, it's when we can check a checkbox on the thing, and if it requires creating new artifacts just to check a checkbox a little bit earlier, we might as well just, you know, go through the tracing stuff and see what, in addition there is, just check all checkboxes kept.
**Jamie Lynch** 11:07 together.
**Hanson** 11:09 Because ultimately, we want to keep, like, one API artifact for everything.
Or at least everything that we have right now. If the idea is to separate them going forward, then doing separation makes sense right now. But if the idea is to not do that, then it'd be weird to just have them separated and eventually merge them back together, or something like that.
**Jamie Lynch** 11:30 Yeah, go down.
And… just so I have an exhaustive list, was it… context, attributes, baggage, was that it, or was there… What about further things?
**Hanson** 11:48 there's, like, the OpenTelemetry object itself, but I think we've already said that, we could mark certain things, using experimental API or something like that. Like, if we have metrics that are not fully, well, it's not even there right now, but, like, if we have it like, then we could… there are ones that we could probably, on the higher level, that we could probably opt out, aspects of, but.
I think those… those three are the bigger ones. Carlos, are there… are there other ones?
**Carlos Alberto Cortez** 12:20 There's the no-op discussion, which is on a separate point, like, yeah.
**Hanson** 12:27 Right. We can talk about the NOAP, after the API.
**Carlos Alberto Cortez** 12:32 Yeah, I would say that, yeah, basically, Jamie, that's the state of things. For me, personally, I would say context is the big thing, because we have to provide an implementation out of the box.
Or at least, you know, yeah, work… yeah, because, you know, like, currently, if I remember correctly, when you use Java, you rely on that context implementation.
But yeah, when you use Android, use a different one, and that kind of stuff has to be solved, or clarified, or documented, discussed, at least, you know?
I would say the rest, the rest is relatively simple. It's not, like, still has to be done, like.
Provide baggage propagation, for example, or trace context propagation out of the box, but it's relatively simple, already straightforward at least, compared to the context part.
**Jamie Lynch** 13:21 Makes sense.
**Hanson** 13:23 So is propagation a separate API, then, that we also need to stabilize before?
**Carlos Alberto Cortez** 13:31 Push it out here.
**Hanson** 13:32 Okay.
**Carlos Alberto Cortez** 13:34 Yeah, for example, Python, just to be super clear, Python includes the context implementation, which relies on some other library that Python provides out of the box as part of the API. That's what they do, but Java separates a context.
artifact, and then you have the API artifact.
Either way works, as long as, as part of the API, let's say, the API side.
Context is implemented, yeah, like an actual… you provide an actual implementation.
**Hanson** 14:06 Are we talking about the API or the implementation?
Yeah.
**Carlos Alberto Cortez** 14:09 Yeah, actually, that's something I need to, yeah, and yeah, we can discuss that, because I was checking that. You may remember, there was some conversation, and this was also part Briefly, about what we talked, speculed last week regarding the no-op, and it's that… APIs provide a full context implementation, which for our case is different, you know?
Because the context.
relies on… on the actual implementation, you know? It's different, and… yeah, so, I'm doing some follow-up on that one.
**Hanson** 14:50 So the… so the API implementation of context is actually not a no-op, is that what you're saying?
**Carlos Alberto Cortez** 14:57 That's correct, yes.
**Hanson** 14:58 Okay, interesting.
**Carlos Alberto Cortez** 15:00 But, yeah, however, for our own case, it's widely different, because, you know, Yeah, so I'm trying to read, again, that part of the spec and come up with something. That's independently of the fact that this has to be implemented also for the mobile space for Android.
But, yeah, like, whether… yeah.
whether that's something that can be done or not. Well, one of… I don't know, so I guess that I have a question for both of you.
And I guess that the question is whether you actually imagine having the Kotlin, seek actually be widely used against the Java implementation.
Because I was talking to some people, like, that I know, that are in this space, and they were saying that we, like, we don't imagine ourselves using that.
like, against the server side, but mobile, we… we are loving the idea of using that, you know, instead of Java, you know?
So I don't know if you have, like… because what I'm saying is that from the spec perspective, if you have to provide an actual full context implementation.
Then we could probably discard the Java layer, probably. I mean, just an idea, still to be discussed.
And then just rely on the… on the Android one, yeah.
**Hanson** 16:33 So, I think, and correct me if I'm wrong, Jamie, the implementation, the Kotlin implementation has a context implementation. And the API doesn't have, a context implementation. I think it has the API for a context object.
But there's no propagation or anything like that. If it's no op, it's no op.
So, does the API implementation of context do more than just effectively provide, like, an empty context? Does it actually do propagation and other things?
Is that why there's a bit of additional trickiness to it?
The last one's for Carlos, sorry.
I'll tell you, so…
**Carlos Alberto Cortez** 17:29 Okay, so could you… could you elaborate? Because I thought, for some reason, it's for Jamie, so could you elaborate on the details?
**Hanson** 17:37 Right, so we're right now talking about the, the API stabilization and making sure that we have an API for context. But then you brought up the fact that the no-op implementation, in the API for context is more than just NOP. There's a bit of… you know, logic in there.
So, the context implementation for the Kotlin SDK exists, fully exists, but the API, I believe, is just, just returns, like, a pretty… something, it's something that's, like, you know, a context object without, without, like.
anything, because it's… it's a no-op everything, right? So why would you need anything, beyond that? So my question was that, what additional functionality is the… API slash no-op implementation of context doing, that…
**Carlos Alberto Cortez** 18:31 Oh, yeah, okay, yeah, yeah, I think, I think I got it this time. So… I think that for other Sikh contexts.
at the API side, provides the full implementation.
So basically, if you are, like, a user, you may be doing no op behind the scenes, but context is always propagated, even if you're using the API only.
against a no-op implementation. No op, in this case, would mean no op for the tracing, metrics, logging, profiles, etc. thing. But context is an actual implementation. You will be actually propagating trace context and baggage and everything else.
Yeah.
So I guess that's the thing here, because if I remember correctly, it's for Kotlin, for the API, Pacers?
You have the no op parts.
And it's kind of… now I'm realizing it's confusing, because it's like you are mixing kind of concerns, because on the API, you expect traces, metrics, logging to be no op, but you expect context to be fully implemented there, yeah.
**Hanson** 19:41 So, right now, I mean, this is something we're still talking about, but, there's no automatic context propagation through threads, in the Kotlin, implement… Kotlin API. And I think if you bring in the Java SDK implementation.
Then, which context implementation did we get?
**Carlos Alberto Cortez** 20:06 Yeah. It could be some dynamic loading.
to work around that, or I was saying before that in the worst case, we just discard that there's no interoperability. I don't know, there are options, but, We need to provide something. I don't know. The other… yeah.
That's an interesting one, and that's why I'm still thinking about that. I was talking to some people, just in case, asking general stuff, that's still on me, so you can probably assign that to me for now, to get an initial feedback, in the same way how I did things for the no-op part against the spec.
**Hanson** 20:42 So specifically… oh, go ahead.
**Carlos Alberto Cortez** 20:44 Yeah, because, for example, let's say there's already a context propagation that works great for Android.
And if that already existed, still, there's the problem, like, what did you do, like… If you want, because that's only available for Android, right?
So, that's, yeah, the question.
So, I would say that if you have the need to start working on context for the Android part, that's absolutely great.
Because this is an independent thing from how the packages, context-wise, are organized.
And definitely, yes. I will do the follow-up on that one.
**Hanson** 21:25 So, let me try to restate the problem, just so that we can answer the question very specifically.
If you use the Kotlin API, there is no automatic context propagation. And whether or not the SIG is okay with that, because at least by default right now, the Android SDK implementation of context doesn't have automatic thread-based propagation anyway.
And the one area where I don't know how we currently behave is, can you use the Kotlin API, but then the Java context implementation, to get automatic context propagation. Through the Kotlin API, using underneath Java implementation.
So, I think we gotta figure out whether, A, that's even a scenario you want to support, and B, what it currently does right now.
And if the SIG is okay with, with that kind of corner case not being supported, then we can, you know, amongst ourselves decide, whether we're okay with that as well.
**Carlos Alberto Cortez** 22:36 Yep, yep.
**Jamie Lynch** 22:39 Cool. I feel like, all of these are probably a good starting point for, like, maybe, like, creating some milestones and… then we can kind of, like, split it into issues and get into the finer detail. Yeah.
**Hanson** 22:56 Sounds good.
**Jamie Lynch** 22:57 Did we mostly, kind of, cover this point about the NOAP implementation, or is there more to discuss there?
**Carlos Alberto Cortez** 23:05 Something to…
**Hanson** 23:06 Go ahead.
**Carlos Alberto Cortez** 23:06 closing.
Yeah, sorry, my internet is wonky again. I think it happens every Monday, sorry for that. Let me know if you need me to repeat something. But yeah, basically, the thing is that currently, the Culture API doesn't provide an OAP, For having a no-op, you actually have to call a package that does the no-op.
And we were discussing whether that's something that we can keep, or we actually move the op functionality into the API.
And, the spec… is… Stay something, but it's kind of general at the same time.
So, I brought up, this point to the spec call last week.
And there are two important parts on that, side. One of them is that if you are offering native instrumentation for your library.
You need an op to come by default, but you don't want it to mess up in case the They, you know, like, create some confusion in case the user has to bring the actual SDK.
And because of this, it's much simpler if you have the no-op in the API part. Oh, actually, give me a second.
I need 10 seconds, sorry.
**Jamie Lynch** 24:22 Boom.
I'm going to… Let's see if I can find, PR on the docs repo.
But it kind of shows… the strategy I was hoping to take all of us.
**Hanson** 24:38 Yeah.
like… I was under the assumption the instrumentation… instrumentations don't need to actually pull in the implementation, no op or otherwise, because it's just… Deferred.
To whoever provides it.
**Jamie Lynch** 25:13 I think… from… from reading the spec, I think it does say that the API should default to NOAP.
P… approach that I've tried to take for it so far is, say you've got a function that takes an be OpenTelemetry AI as a parameter.
If you're writing… like, if you're developing your own SDK, if you wanted to instrument with OpenTelemetry.
then the idea is you would just add the API package and the no-op package.
And then you can effectively default it to the NOAP implementation.
then… if… if you have some other code that wants to pass in an actual implementation of, like, a Java SDK or forgotten implementation.
You'd be able to basically override the no-op value.
**Hanson** 26:16 So, example, would that be considered… so, so, I would say, like, at this point, the… Having a default parameter would just be… you know, syntactic sugar. So, you know, you could do it without having to directly import the package. Like, if you're just writing instrumentation, and you're… your package doesn't take an OAP, you'll still compile, and it'll still run. It's just that the caller will have to provide it. So this is nice, in terms of, like, not having to do that, but it's not a requirement.
Like, it's not like if you don't include this, it will fail to compile, or it'll run to errors.
It'll always work. And I think that was the concern, is… is at least the core of the concern, at least when I… the way I understood it. We'll wait for Carlos to come back first. But I would say that the context stuff adds an additional wrinkle.
which I hadn't… previously known.
But I think… I think as an example, that's… that's fine, but we might also want to have an example where Excuse me, we don't pull in the, the no-op, just to… just to show that instrumentation don't necessarily need it.
**Carlos Alberto Cortez** 27:44 Yeah, I think she… Yeah, I would say that the typical use case is that you have a global open telemetry object. Like, for example, global open telemetry with a GET method that returns any register, global open telemetry object.
And then once you have that, that can be called by instrumentation, and it will get either an OAP or an actual implementation. So, we have to provide at least that part, you know?
instead of actually, like, because in the example that you were pointing to, Jamie, you are actually creating and importing the no-op implementation.
And we… so I would say that for testing, that's fine.
But when it comes to actually using DAV in instrumentation, that's not something we want to do. Like, you should be get… yeah.
**Hanson** 28:34 So I think that's… what I was saying is that that's actually not necessary. Like, we could remove the import of the no-op, and it's still fine. It's the user of the instrumentation that will have to provide it at that point.
Adding that is… is syntactic sugar, which does… it's not actually necessary. Somebody has to provide an implementation, when that functionality is invoked.
But the instrumentation itself does not need to know what it is. It just needs to know the OpenTelemetry, Higher level object interface.
**Carlos Alberto Cortez** 29:05 Yeah, as long as there's a global object that you can call and get, yeah, that's fine.
**Hanson** 29:11 I remember reading the Java code, and the global object is actually discouraged.
And that you should always, have an instance explicitly provided.
And I think that's the approach that we took here, in the SDK. I don't think there was a global object.
**Carlos Alberto Cortez** 29:32 There is. Actually, it's used if you use an agent, and that's supported for that scenario.
Specifically, yeah.
**Hanson** 29:40 Oh, no, the Java definitely has it, but I remember reading something in the Java code or documentation to say that's not recommended, and in fact, Some people wish that didn't exist.
**Carlos Alberto Cortez** 29:53 Yeah, I mean, yeah, so to be fair, that brings me to the second point in the spec discussion, that there's not a single Seek that doesn't implement an OAOP as part of the API.
Java, I think, if I remember correctly, has those, pieces of documentation about, please consider not using the global OpenTelemetry object, because of, initialization problems, and ordering, and… Sort of, You know, situations, like, that create a problem, like, you're too many… Threads are trying to create that.
And then you don't get the one you wanted. You don't create the one you wanted.
But in general, and that was the second thing, that most people, most of the maintainers think that there's value in keeping this globally, in the knob.
at the API side.
Yeah, so that's one… and actually, one of the people supporting this was Java maintainer, Jack Burke.
So probably need to do a follow-up with him on that part.
But the general feeling is that there's value if we can keep them up.
knob part in the API.
Otherwise, we would be the first league that doesn't do that, you know?
And as I said before, for Java, this is the way it is, but for Python, for example, it's totally fine having this global object.
Like, there's no, like… yeah, go ahead.
**Hanson** 31:32 So I guess the global implementation is really the reason why the no-op implementation is bundled with the API, so that the API can, by default, initialize some implementation.
**Carlos Alberto Cortez** 31:48 Yep.
**Hanson** 31:50 So if we don't have a global object, then… the, the other thing doesn't… isn't necessary, and if we have it, Or rather.
Having things bundled and the existence of a global implementation seems… you know, part and parcel of the same requirement. And we either do both, or we… Dune… we don't do that.
**Carlos Alberto Cortez** 32:14 Right.
Yeah, and as part of the follow-up, I would say, first, I would like to, that's on me as well, talk to Jack Baer, discuss some details about their… the situations that… the JavaSea has faced, like, historical context, on these… global object, and then come back to you. If that's okay, like, unless there's a rush to do this.
**Hanson** 32:38 I think a global object is useful if you have instrumentation that is initialized by itself without having, like, a programmatic call to provide an implementation. So if you can basically discover an implementation, to use. But… So far, I don't… I… I don't know if… if that's… something that… we require. So maybe this is on us to discuss whether that… like, the scenario where the global object is a must-have is something that applies to us.
Because I think now I understand more about why these, there's desire to bundle them, but whether that desire or the requirements for that desire is necessarily supported in what we're trying to do, so…
**Carlos Alberto Cortez** 33:36 Yeah, unless there's some rush, I would like to follow up on that point before I come back to you. But I guess that… that brings me also to my second question on this front.
Is there some technical reason? I mean, just, like, let's say that, we leave the organization part, discussion part outside. Is there any technical reason that could prevent an op to leave in the API?
Or if, in the worst case, if that's needed, that can be done easily. And we discussed that hands on Jason and I, Jamie, but yeah, I would like to get your opinion on that one.
**Jamie Lynch** 34:13 Yeah, there's, there's not any technical reason… I guess why it's not feasible. There's more… the design decision of whether we want to do that.
And what the consequences are of… bundling a no-op into the API would be.
I even think that right now, the API package might include the no-op package by default, so it's effectively… You're getting those symbols anyway, but… We can go check that, and Yeah, I don't think any of, like, the discussion we've had today is urgent, it's more just… Moving stuff along, so it'd be cool to get other people's opinions on this, if you have time.
**Carlos Alberto Cortez** 35:00 Okay, yeah, so let me follow up on that one that interacts with what Hansel mentioned. Okay, so there's no rush, you can do that this week, along with the.
**Jamie Lynch** 35:08 what's called.
**Carlos Alberto Cortez** 35:09 art, yeah.
**Hanson** 35:11 Yeah, I think, as discussed last week, It… technically, we could do that, no problem. Like, you know, in the same way that Jamie was talking about, I didn't even know it might be that way already, that it effectively… the module, you know, pulls in, you know, the no-op implementation. But, you know.
I think this is something that's so fundamental that it may… it's probably good to, like, look at it To make sure we absolutely need it. Because, we could always add it in later. Taking it out is probably a little harder, in terms of, you know, breaking stuff, so…
**Carlos Alberto Cortez** 35:49 Yeah, correct.
Yeah, so it's better to discuss that fully before we introduce that. If we introduce that, it should be on when everything is super aligned, super clear, we are confident, yeah.
**Jamie Lynch** 36:02 Yeah.
Cool.
Anything else to discuss?
**Hanson** 36:14 So for the, the sub, I guess, dependent APIs will create milestones, and knock them off one by one. And when those are knocked off, we'll know that, hey, you know, all… we could stabilize, log and tracer, just because everything else below it is good.
**Jamie Lynch** 36:34 Yep.
**Hanson** 36:39 Cool.
**Jamie Lynch** 36:40 Cool. Thanks for coming, everyone.
**Carlos Alberto Cortez** 36:44 Yeah, well, we'll come back.
**Hanson** 36:46 Carlos.
**Carlos Alberto Cortez** 36:47 Thank you. Ciao.
