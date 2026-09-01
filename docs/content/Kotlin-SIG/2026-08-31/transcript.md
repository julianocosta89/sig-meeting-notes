SIG: Kotlin SIG
Date: 2026-08-31
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Viorel Alexandrescu** 01:33 Blue.
**Jason Plumb** 01:38 Hello.
**Viorel Alexandrescu** 01:46 I think it's, I think it's just us for now.
Might be a quick meeting.
**Jason Plumb** 01:52 Okay, did… did Jamie say something about… Anything?
**Viorel Alexandrescu** 01:58 Mmm… regarding my PR?
**Jason Plumb** 02:02 Hmm, about running this meeting or being here today?
**Viorel Alexandrescu** 02:05 No, no, he's off today. He left Last week,
**Jason Plumb** 02:09 Okay.
**Viorel Alexandrescu** 02:10 He's off due to a public holiday.
**Jason Plumb** 02:15 Okay.
**Viorel Alexandrescu** 02:16 You left a message on Friday.
**Jason Plumb** 02:20 Okay, let me, yeah, let me pull up the meeting notes and I'll run it.
I think Hanson was back, but…
**Viorel Alexandrescu** 02:28 He's off as well. He's… he just left a message saying that, he has a meeting that he can't miss.
**Jason Plumb** 02:35 Okay.
**Viorel Alexandrescu** 02:35 Ilya as well.
Ivan is trying to join.
Just a sec, let me help him.
**Jason Plumb** 02:47 Thank you.
**Viorel Alexandrescu** 03:29 There you go.
**Jason Plumb** 03:31 Pate.
**Ivan “CLOVIS” Canet** 03:34 Hi.
**Jason Plumb** 03:36 Welcome.
So, I'm sharing the doc that I will paste into the chat if anyone has topics that they want to add for today.
**Viorel Alexandrescu** 03:49 Sure thing.
**Jason Plumb** 03:58 Ivan, have you joined us before?
**Ivan “CLOVIS” Canet** 04:01 No, it's the first time. I've discovered the project last week.
**Jason Plumb** 04:05 Cool.
That's awesome. Who are you… who are you with? Are you independent? You work for someone?
**Ivan “CLOVIS” Canet** 04:11 I mean, I have an employer, but I'm here as an independent.
**Jason Plumb** 04:15 Great, okay, cool.
Alright, so I was hoping that Carlos could give us a little bit of an update, because we did, in the spec meeting last week, we did discuss a couple of the open items around… A couple of things that we're trying to get stable, and… I think we're getting… I think we're getting close on those, but I was hoping he could give an update, but he's usually joining late, so we'll just… We'll push that down… And then we'll talk about JSON encoding.
**Viorel Alexandrescu** 04:48 Well, there's not much to add to that. If you want to take a note, the thing is that I'm almost done with my PRs. I just need someone to have a look over my latest comment.
Because… My build is failing due to a… had the dependency for a model, and I can't really get rid of it, because the whole encoding mechanism is based on, Some, some serializable classes.
**Jason Plumb** 05:22 Okay.
Which PR? Can you paste a link to the PR?
**Viorel Alexandrescu** 05:26 Sure, just a sec.
**Jason Plumb** 05:29 Thanks.
**Viorel Alexandrescu** 05:42 Just a sec… okay, I'll just paste it right here in the chat. There you go.
**Jason Plumb** 05:52 Cool.
Thank you, thank you.
**Viorel Alexandrescu** 05:56 They're welcome.
Right, so the whole… the whole thing was that we had a bit of a ping pong a couple of weeks ago.
And if you go a bit up, to Jimmy's latest comment.
**Jason Plumb** 06:20 Yeah.
**Viorel Alexandrescu** 06:21 Yeah, he said that, I may need to… remove a dependency from… with the integration test module. Lower, I explained it… I explained why I can't really do that for now.
**Jason Plumb** 06:38 Let's see what it looks like.
So, is this in here?
**Viorel Alexandrescu** 06:46 Yeah, this is where I'm pulling integration tests, the integration test module. The thing is that I don't really need something specific, like, in terms of testing. All I need is the serializable models. So, if you go into, let's say, JSON log record encoder.
**Jason Plumb** 07:04 Right… oh, not the test, okay?
**Viorel Alexandrescu** 07:07 Yeah, here we pull serializable log record data.
the thing is that that's being exported through the integration test. It's written once there.
And it's been left in that module up until now, and if I remove the integration test dependency, I don't have access to this, and it's the only model that we have which actually caters for, caters, Requirements to be able to serialize things.
In JSON format.
**Jason Plumb** 07:44 Yeah.
**Viorel Alexandrescu** 07:45 So, the quick and dirty solution would be to just copy and paste it. Otherwise, I could move it to a different module.
**Jason Plumb** 07:55 So there's, yeah, so there's… This one and… what's the difference between this first one and the last one?
Conversion. Okay, so this is the class right here.
**Viorel Alexandrescu** 08:06 Yeah, then that one… I think some of them are the extension functions which actually return That given more…
**Jason Plumb** 08:17 The way that I read this, though, is that this is not production code, this is test code.
lives in the integration test package, and so everything that's in integration test should not be part of, like, normal… should… I wouldn't consider it normally part of production code.
So I think Jamie's right to, like, raise this as, like, a concern, but then the answer to what do we do about it, I don't know yet.
So… Yeah, because you do… I see why you want to use this, Maybe there's a place that we can promote this.
Right? If you need it, for production exporter code for JSON… Yeah, I mean, I wish Jamie was here to chime in, but… Copying it… copying it may not be the worst thing, because it's relatively small.
**Viorel Alexandrescu** 09:05 True, but then again, it would be hell to keep it in sync with whatever people would be doing in that, in that module.
**Jason Plumb** 09:13 Well, can we flip this, and can integration test take a dependency on wherever you move this to?
**Viorel Alexandrescu** 09:18 Sure, just tell me where I need to move it.
**Jason Plumb** 09:21 Yeah, I don't have the quick answer for you, cause… I've been slacking off and ignoring this project a lot.
I haven't been slacking off, I've been fighting other fires, is what I've been doing, but, Yeah, I don't have a great answer for you, but let's keep that… let's keep that discussion going, and I apologize.
**Viorel Alexandrescu** 09:41 That's okay, that's fine.
But other than that, if I get this, if I get this out of the way.
it'll be just fine. I can go ahead and finish off with the encoding part, and then once that's done, the file export PR is based on these changes, because I need exactly these classes pulled in. Once this is fixed, that one gets fixed fairly quickly as well.
**Jason Plumb** 10:06 Cool.
**Viorel Alexandrescu** 10:10 But yeah, right now.
I need some input, on this. Yeah. If you… if you… if you wanna… yeah, exactly. Thanks.
**Jason Plumb** 10:19 Yeah, totally.
Yeah, just let me paste to that thing, this thing.
Okay, cool, yeah, and you probably already see, like, just from my purview, there's a ton of PRs that I haven't looked at, you can just tell by the blue… the blue on the sidebar here, so… Carlos… Thanks for joining us. Can we… do you mind providing a little update from the spec meeting?
**Carlos Alberto Cortez** 11:20 Yeah, so basically, this one was on the global propagator's part, basically, the, as you may remember, there's this OpenTelemetry object, which tends to include tracer provider, meter provider, logger provider, and any globals, like, anything that you would need to instrument your code. And… This global facility is a… is a shoot in the specification, which means that And languages can decide whether they expose that or not.
The exception being propagators, which is something that you must provide globally. There are historical reasons, but basically, the long story short, in the… specification call from last Tuesday, it was suggested by a few different maintainers that we relax this condition and the specification. Usually, there are problems when you actually change some of the language in the specification, but one of the Exceptions is when you relax the coffee. If you make something more strict, you are… you can break people, but when you are making something more strict to less strict than you are, actually, you know, and you know that the requirements have changed ever since, you are, you know, you are totally fine with that. So that's the plan, and then, of course, we can move forward, and the plan, because of that, is that I will present a PR, For the specification, to relax this part, and hopefully that will allow this, SIG to not use globals by default.
and add them later, if they are needed, you know? I think that, long story short, then again.
This is more useful for auto-instrumentation, where some agent is actually injecting, you know, like, you know, creating these, all these objects and injecting it somewhere, so you need to consume that. But in your case, we don't do that, so we don't need that, so we can get by without it, for now.
**Jason Plumb** 13:20 Yep.
Cool, yeah, I tried… I was on that call, so I tried to summarize as well. So yeah, the summary on the global propagators was, yes, technically the spec requires it, but it's also fine to go stable without it.
As long as we acknowledge that there could be some case down the road where we might need to add it back. Or add it. Yeah. Right?
**Carlos Alberto Cortez** 13:40 Yeah, I will prepare the… this, relaxed PR for the spec, and we'll discuss that tomorrow.
**Jason Plumb** 13:47 Okay.
**Carlos Alberto Cortez** 13:48 Just to, yeah.
Worst case, even if this has some moratorium on the specification change, we can add a note to the specification that this will change in the future.
And thus allowing us to do what you said, JSON, like, going stable eventually without… Having to do this, yeah.
**Jason Plumb** 14:05 Okay, cool. And there was one other topic, wasn't there? Around… Was it around the global open telemetry?
**Carlos Alberto Cortez** 14:14 No, it's around, about, so the remaining part is the no-op, like, whether we can include that.
**Jason Plumb** 14:24 Oh, yeah, okay.
**Carlos Alberto Cortez** 14:25 Right, and we were… I was just mentioning that last week to Jamie, but we didn't have the chance to actually go deeper.
**Jason Plumb** 14:33 Okay.
**Carlos Alberto Cortez** 14:34 But there's… I can probably summarize that from a comment that there's in the Kotlin, Slack channel, but the problem is that it's kind of… I think it got lost, among other things. But one of the things, like, now that we can get rid of the global objects conversation part.
The knob is that… so basically, there's this separation of API versus SDK. However, there's this thing about that a lot of the components are expected to be implemented de facto at the API level. Or… put it another way, without requiring an actual SDK. Those things are expand context, which is a, like, very basic part, and part of that is also baggage, you know, like, baggage… It's not something that you should need to bring an SDK to implement, you know, to use that. And because of your, like, span context and bugger propagation.
important, and because of that, you also need to add baggage propagator and the W3C trace quantities propagators. So those things are things that need to live somewhere, and the conversation was around whether That's… you know, those should exist somewhere, like in the API, or in some other package. And that overlaps with the… We did not op implementation, because, to some degree.
Because I think there's this concern about making the API too big.
And instead, you define the nob somewhere else, but in the API, you already have to put these other things, like, what's the point?
And a different approach would be to actually have some other package, like, which could be vertically dependent on each other, but in my opinion, it could be kind of weird. Like, you have the API, and then you have this API with backhash propagators.
another one, or the same with no op, and then you have the SDK… no, the, like, the SDK API, and then you have the SDK. So, That's… that's more or less what kind of JavaScript was doing for historical reasons to support nodes on the browser, and now they are trying to simplify that. I don't know how far that will go, but I think they didn't like having so many, you know, packages.
As part of this split.
**Jason Plumb** 16:44 Right, and so what we talked about before was, like, the way the structure is right now is that we have… this NOAP module that we publish, right?
**Carlos Alberto Cortez** 16:53 Yep.
**Jason Plumb** 16:55 And that produces the Noop API and stuff.
For the Noop SDK.
**Carlos Alberto Cortez** 17:02 Yeah, the op is decay, yeah, correct.
Oh, also, by the way, there's a small language in the specification, which I didn't bring up, I want to talk one thing at a time. There's one part of the specification, which is kind of old, like 2021, which mentions, literally, I will read that, the API dependency contains a minimal implementation of the API.
**Jason Plumb** 17:24 That's pretty clear.
**Carlos Alberto Cortez** 17:26 Yeah, but the problem for me is that it's not… even though it says contains, it doesn't must contain. So, if you add I would say, by stating that it's a bug, that it's not using a, you know, normative language.
**Jason Plumb** 17:42 Right.
**Carlos Alberto Cortez** 17:43 People may say, yeah, it's saying that, but it's not normative.
And, yeah, so we can discuss that tomorrow. I think we can do that. This position where I can bring back the summary of that. Jamie's out this week, so we are not in a rush to make progress on that, but we should try and figure out the remaining pieces so we can come to a final conclusion eventually.
**Jason Plumb** 18:07 Cool. Sounds good.
**Carlos Alberto Cortez** 18:11 Jason, what… do you have any opinion on that? Oh, by the way, Jamie has a PR, a draft PR, on how to put, a separate propagators package.
Yeah, it's draft one, there we are.
And the thing is that that could be, like, a separate package, but that would be, like, that would mean, like.
You would have… you need to have, Is that the one? I don't remember.
**Jason Plumb** 18:38 This is not draft, no.
**Carlos Alberto Cortez** 18:40 Probably a different one. Okay. Maybe he made it, I don't know. But anyway, but he got this prototype that at least was prototyped last Thursday, which is that, you are creating another package, so you could have the API.
**Jason Plumb** 18:54 Done.
**Carlos Alberto Cortez** 18:55 the SDK, and then propagators, which is kind of in between that one, yeah, correct?
**Jason Plumb** 19:00 Yeah.
**Carlos Alberto Cortez** 19:01 And for me, it's, yeah, I don't know, I don't… And, of course, there was one important thing I wanted to talk to Jamie about, which is that… and I think Hansel, they also support this idea that an SDK, Like, they find it odd that propagation could exist even without a present.
SDK, you know? Like, you are…
**Jason Plumb** 19:25 I know, it's such a weird concept to me as well, but I understand the desire for it, like… You know, you're not really doing instrumentation, you're not generating metrics or traces or logs or anything, but you can still pass, like, span context, right?
**Carlos Alberto Cortez** 19:39 Yeah, and I'm wondering to what degree that's something that is more naturally needed in the server side, more than the client side, maybe that's a difference.
**Jason Plumb** 19:49 Maybe.
**Carlos Alberto Cortez** 19:50 Oh, maybe.
But I remember, for example, back when I was working at LightStep, we had these, distros.
And then at some point, some people were like, hey, we want to use metrics, but we don't want to use tracing, so we want to disable part of that. So what we could do is that we disable like, we don't set the tracer… the tracing SDK first, and then we just clear the propagators part, you know? And it's part of one step as part of the distro. I wonder if that, yeah, if that would help or not.
Yeah.
But this is one of the other things, because in my mind, if we don't want to actually use If we, like, to have this weird situation, we can just probably do something, like, default thing, or, I don't know, some setup that would say, okay, don't install the SDK. If you're going to disable the SDK, also clear automatically, The propagators, and this is something that the user has to explicitly call.
**Jason Plumb** 20:53 Does the spec address, like, is there a distinction between having the propagators available and actually doing propagation? Like… like, pulling in the headers and then… Creating the headers, like, passing on the headers.
**Carlos Alberto Cortez** 21:08 Yo…
**Jason Plumb** 21:09 Yeah, I know. It doesn't.
**Carlos Alberto Cortez** 21:10 No, no, like, basically, you most… you must make the propagators available. Like, first of all, like, user… like, W3C context, trace context, and baggage, they must be available at the API, let's say. The second thing is that, There can be some propagator's instance.
that may be or not globally. And the last part is that there's never automatic injection. That has to be done from the instrumentation side.
**Jason Plumb** 21:36 Okay, good, good.
**Carlos Alberto Cortez** 21:37 And that's always an opt-in, yeah.
**Jason Plumb** 21:40 Yeah, so what's the use… I don't understand the use case, I guess, for that, to have it available, but then, like, a user still has to write code, or, like, they have to do the propagation still manually in code, or… what's the expectation?
**Carlos Alberto Cortez** 21:52 Yes, correct.
**Jason Plumb** 21:53 Okay, okay.
**Carlos Alberto Cortez** 21:54 Yeah, the idea is that if you have…
**Jason Plumb** 21:55 weird.
**Carlos Alberto Cortez** 21:56 Well, a good idea, more or less, is that if you have different instrumentation, like some native, and some that the user initialized himself.
When they want to extract and inject something, they just go and check whatever is being used by the rest of the system.
**Jason Plumb** 22:12 Okay, okay.
**Carlos Alberto Cortez** 22:14 But yeah, it's very explicit, you know?
Okay.
**Jason Plumb** 22:19 Yeah, I can understand that, that makes sense.
Okay, have you commented on this one yet? I haven't seen this.
**Carlos Alberto Cortez** 22:26 I… no, I only left a comment. I will talk about that with those… the PR I mentioned before.
**Jason Plumb** 22:33 Okay.
**Carlos Alberto Cortez** 22:33 The second with the, the fact about, you know, like, as I mentioned, this statement that's saying that the API dependency contains a minimal implementation, etc.
**Jason Plumb** 22:43 And then…
**Carlos Alberto Cortez** 22:44 Let me make a summary of that, yeah.
And once Jamie's back, we can just, like, gather and… Yeah, but I don't know what's your opinion. My fear, to some degree, is that there will be too many packages, you know? There's already, like.
top, SDK, and then there's a SDK API, and the compact, so…
**Jason Plumb** 23:06 Yeah, definitely a difference of philosophies around that stuff, you know, the Node people, for example, love small packages, like, insane numbers of packages.
This, to me doesn't feel too bad yet, but I definitely hear where you're coming from, like, it's a, you know, it's a lot, but it's not… it's not bananas to me.
**Carlos Alberto Cortez** 23:26 Yeah, and I would say that the SDK API is something, I think it's totally needed, based, you know, on the compatibility layer, for example.
**Jason Plumb** 23:33 Yeah.
**Carlos Alberto Cortez** 23:34 But other ones, probably, we can get by without.
**Jason Plumb** 23:38 Yeah, like, Java doesn't have one of these.
Right. It's just part of… it's just part of the SDK.
**Carlos Alberto Cortez** 23:42 Correct, yes.
**Jason Plumb** 23:43 Yeah.
**Carlos Alberto Cortez** 23:44 Good and bad, also.
**Jason Plumb** 23:45 Yeah, exactly. Trade-offs, yeah.
Because, the trade-off… the main trade-off there being, we kind of don't even know what our SDK API is, it's just, like, whatever's there. I don't even know if we're generating API docs in Java.
**Carlos Alberto Cortez** 23:58 They are, if I remember correctly.
**Jason Plumb** 24:00 Yeah? Okay.
I believe you.
**Carlos Alberto Cortez** 24:03 I remember seeing them.
**Jason Plumb** 24:05 Yeah.
Okay, well, that's cool, that's progress. There's a couple of PRs that are open around that… around stabilization, like… this one.
**Carlos Alberto Cortez** 24:17 Oh, yeah, actually, that's part of that, because, you know, Bagash, like, the API.
**Jason Plumb** 24:23 Yeah.
**Carlos Alberto Cortez** 24:23 Fine.
It's just, like, the last part about that, by default, Bagash exists as, you know, without SDK.
So, do we.
**Jason Plumb** 24:32 Yep.
**Carlos Alberto Cortez** 24:33 Once it's on, we can just put it here or there, but otherwise, it looks correct to me.
**Jason Plumb** 24:39 Okay, cool.
**Carlos Alberto Cortez** 24:43 Now, probably, one disclaimer is that I am doing that as the TC, like, representative, but we can opt in to have a second TC person.
And that person may have to, you know, to make… to ask questions, let's say, you know?
**Jason Plumb** 25:01 Yeah, yeah.
Is there… is that being planned, or are you just talking long-term?
**Carlos Alberto Cortez** 25:07 long-term, and explicitly, like, in case you want to. If not, I can just go a double pass, in case there was some small detail. But yeah, that… that's something that Jamie, you, and Hanson have to decide in the future.
**Jason Plumb** 25:22 Yeah.
Okay.
Your work is appreciated, Carlos. Your expertise is always helpful.
Okay, does anybody have any other topics to discuss? Otherwise, I will spend maybe 5 minutes just looking over issues and see if there's anything new and exciting.
**Ivan “CLOVIS” Canet** 25:46 I mean, not really a topic, but since it's my first time here, I'd like to maybe introduce myself or something, if we have the time.
**Jason Plumb** 25:52 Yeah, please, that'd be great. Yeah, we're always looking for people to help out and join the project, or ask questions, or contribute however they can, so… yeah, welcome.
**Ivan “CLOVIS” Canet** 26:02 Well, here I go then. So, Ivan a… I often go by Clovis online, but you can use either, it's fine.
My specialty is in Kotlin and specifically DSLs, so how to expose different methods and how to make it idiomatic and everything.
I'm in touch with… quite a few people in the Kotlin community, including multiple people on the Kotlin team. Like, I've contributed to multiple keeps and stuff like that, so I've got a good grasp of what's going on there. However, my knowledge of OpenTelemetry is very thin.
So, sorry, in advance if I ask them questions about that. If you want to take a look at what I'm doing at the moment, I'm sending a chat, so these are the two projects that are the most related to what we're doing it. So, Catmongo is… I'm rewriting the MongoDB driver for multiplatform.
And then… so that is kind of similar to, to… what can be done here, and Spine is specifically a DSL for KTOR to make it more convenient to use in a multi-platform way.
So, yeah, my… like, I'm trying to… I am specializing in, like, how do you expose things in Kotlin so that they're idiomatic, that they work in all the platforms, that you have compatibility, etc.
But then, on the OpenTelemetry side itself, like, I've read a bit of the specification, but not that much, and I haven't had the occasion to actually use OpenTelemetry for real.
So… I'd like guidance on, like, what I should learn first, where I should put myself, etc.
**Jason Plumb** 27:42 Cool, yeah, so I can, I can… yeah, thanks for sharing that. As far as OpenTelemetry goes, you know, this project's been around for 6 or 7 years. The main, like, sky-level concepts are to provide, like, a consistent set of APIs and implementations for doing Tracing, distributed tracing, generate metrics, logs, especially logs with context.
and events, and then there's events and profiles and a few other things that have been, you know, developed over the years, but the main things… metrics, traces, and logs being the main APIs. Within each of those, there's maybe smaller sections, like you heard us today talking about baggage and propagation and that kind of stuff.
part of that, like, propagation is part of the W3C spec, but it's also part of OpenTelemetry, because we're like, you must provide a default propagator that adheres to the W3C spec.
as far as where to start looking, I mean, reading the spec is gonna be very exciting, I'm sure, but being familiar with, like, those high-level concepts, and, like, maybe… maybe building a toy or something would be helpful, or, you know, the Kotlin… implement… API and implementation here is coming along pretty quickly. I think metrics right now are maybe the weakest implementation area.
But our focus for the last month or so has been, maybe two months, has been, like, really trying to get the APIs marked as stable, so that users can start Both coding against them, developing against them, and also implementing instrumentations with them.
So, what's the purpose?
**Ivan “CLOVIS” Canet** 29:19 Progress on the overall.
**Jason Plumb** 29:22 On the stability? I think… I think we have a README that addresses that, I think.
**Ivan “CLOVIS” Canet** 29:30 Misstabbing.
**Jason Plumb** 29:32 Yeah, it's kind of buried, so it's in the API module. The README has this matrix, and so the different components… the only thing that we have marked stable so far are the attributes APIs.
But we think that these two are, like, very close.
I don't even know Factory… Factory is the API through which you can create some of these other components, and then logging metrics and tracing are obvious, and propagation we talked a little bit about today.
So I could put this in the dock as well.
And, not entirely unrelated, but, Jamie, Hanson, me, David, we also work on OpenTelemetry Android, which is… primarily Kotlin-based. We want to be able to still continue to support Java, but our main focus, like most Android developers, is Kotlin. And in Android, we also have a DSL that we leverage, like, that we've created for bootstrapping OpenTelemetry into an Android app.
If you haven't seen that, it might be of interest to you, because you also are excited about DSLs.
**Ivan “CLOVIS” Canet** 30:49 I am, however, I don't do Android.
I'm a backend and web guy.
**Jason Plumb** 30:54 Yeah, okay, that's cool.
**Ivan “CLOVIS” Canet** 30:55 Not that I don't like Android, it's just…
**Jason Plumb** 30:59 Fine, yeah. I get it. I get it. I'm just, yeah, I'm just throwing that out there as, like, a piece of information.
**Ivan “CLOVIS” Canet** 31:06 link?
Yeah. And I'll take a look.
**Jason Plumb** 31:12 I think our docs are lacking.
Wow.
**Ivan “CLOVIS” Canet** 31:17 That's every project, isn't it?
**Jason Plumb** 31:19 I know. I think the best… the best example right now is actually probably the demo app.
That's not right. Where am I here?
So in the main application in our demo app, you can kind of see some of this DSL.
So I'll link to this.
And I think Kotlin will trend that way. I think there will be some… there's already some DSL work happening, but I think it'll… I think it'll end up… with something like that as well, so that we do have an idiomatic, like, Kotlin DSL that allows users to configure OpenTelemetry programmatically.
In addition to all of the other ways that we need to be able to support configuring the SDK, specifically through, like, environment variables, and ultimately through declarative configuration, which is like a YAML file.
**Ivan “CLOVIS” Canet** 32:15 So, how is environment variables going to work on a web?
**Jason Plumb** 32:20 They won't. I mean, not that I'm aware. Yeah.
**Ivan “CLOVIS” Canet** 32:24 Yeah, that makes sense.
**Jason Plumb** 32:26 Yeah, I don't think that's gonna be a supported configuration.
**Viorel Alexandrescu** 32:32 And I put so much work into it.
**Jason Plumb** 32:35 You did?
**Viorel Alexandrescu** 32:37 No, I did, yeah, I did the…
**Jason Plumb** 32:38 Just, yeah, to support the environment variables, yeah, yeah, but…
**Viorel Alexandrescu** 32:40 Well, that's not necessarily true. It's gonna work for Node.
**Jason Plumb** 32:45 Exactly, yeah, yeah.
And every other platform that's not the web, except for Android. I don't think you can do environment on Android either.
Doesn't make sense to me.
**Viorel Alexandrescu** 32:57 No, we talked about it back then.
**Jason Plumb** 33:00 Yeah.
Yeah.
I mean, it's useful, it's very… it's definitely helpful on the server side. But all of OpenTelemetry is, like, mostly trending toward declarative configuration being the… the main… like, a YAML file being the main configuration directive for SDKs and instrumentation.
Cool. Well, we, we do this meeting every week. Feel free, as you're scratching around, to, like, add agenda items throughout the week. We really appreciate comments and code reviews, like, as you saw, there's plenty of PRs open right now, and if one strikes your interest and you want to give a review.
we love comments about stuff that may or may not be as idiomatic as we think it is, especially if you're a Kotlin expert, which it sounds like you are. So, reviews are, like, the number one way that you can contribute to this project right now.
And just showing up and asking questions, and if there happens to be an issue that is small enough and bite-sized to maybe do a first contribution, that's great too, but we really need more eyes on the code. It's really, really useful to get reviews on stuff.
**Ivan “CLOVIS” Canet** 34:15 I'm curious, what's the scope of multiplatform? As in, like.
Obviously, there's already a Node.js implementation.
And I don't think you're aiming for Node.js developers to use the Kotlin implementation.
Rights.
So, what's the… the scope, like, do you expect iOS developers to use the Kotlin version? Do you expect… I assume, at term, the goal is for, whatever you already have on Android to be merged with this, and so… It's the same codebase behind it.
**Jason Plumb** 34:54 No. No, we're gonna keep those separate, in fact, but what will happen is that Android will eventually use this implementation of API and SDK.
So, right now, OpenTelemptry Android's based on the OpenTelemptry Java implementation, and so that means we're beholden to a bunch of those Java classes, like those JVM classes, even though most Android developers are just using Kotlin. And there are some rough edges, right, at that boundary, and by switching to a purely Kotlin implementation, we can get away from some of that, and maybe have a more native compilation process, too.
**Ivan “CLOVIS” Canet** 35:32 So, do you expect Java users?
Of the multiplatform library?
**Jason Plumb** 35:38 Well, so it's interesting, right? When you're… when you're saying, do you expect Java users or iOS developers, or whatever, I mean, I think mostly it's Kotlin developers, but, like, what… What, like, who the user is.
is anyone that's, like, writing Kotlin that wants to deploy on these platforms, right?
**Ivan “CLOVIS” Canet** 35:56 Right, but when… when you have a team that does Android or… well, Android less so now, but especially that does iOS, the application is probably going to be 50% Kotlin, 50% Swift.
And so… Right.
it would be a shame to have two different OpenTelemetry SDKs in the same application, right?
**Jason Plumb** 36:16 I see what you're saying. Yeah, It's a good question that I think I don't have an answer for. That's fine. Swift is relatively new as well. I think it's under active development.
And to have those two things come together, I'm not… not entirely sure.
**Ivan “CLOVIS” Canet** 36:38 And other platforms than that. I'm not sure if there's a lot going on for native.
With the project? Is that a target?
**Jason Plumb** 36:47 It is a tar… it is a target, but I don't think we have… That much going on with it yet.
Other than you can, you know, you can target native.
**Ivan “CLOVIS” Canet** 36:58 Yeah, I mean…
**Jason Plumb** 37:01 I don't even think… I don't think we have native tests or anything yet, but I could be wrong. I don't think we do. I haven't seen them.
**Ivan “CLOVIS” Canet** 37:09 To be fair, I don't really see what… OpenTelemetry could be doing that's different there.
Meaning, like, if there's…
**Jason Plumb** 37:19 Yeah, meaning if… one second, please.
No, and just… they're good to go. Thank you. Yeah, sorry about that.
Yeah, I mean, so, like, a test, like a Kotlin app that's using the SDK, using the API, and then the whole thing compiles native, and then running that through its paces, making sure the telemetry is correct. I haven't seen that test yet, but that's certainly, like, what we expect to work.
Right? We have a native target, iOS target, Android target, all those different targets, but I don't think we have integration tests for it yet, because there really isn't… We're working on the API first, I think.
Long term, there'll certainly be an integration tests that need to be built for that stuff.
I was wondering, though, if we, like, you asked, like, what the status of these different platforms is, and… I… I don't know in the code where we actually state… in the repo if we actually state what targets we support, but we have to, right?
**Ivan “CLOVIS” Canet** 38:30 There must be, yeah, in Bill Graddle.
One of them.
**Jason Plumb** 38:35 Yeah, but I mean, actual docs. Yeah.
**Ivan “CLOVIS” Canet** 38:38 Yeah.
And if you do convention plugins, it's going to be hidden somewhere else.
**Jason Plumb** 38:44 Yeah.
**I, I, maybe there's an issue, I wonder… Ivan “CLOVIS” Canet** 38:54 My question was more like, because you can do something that is very idiomatic for Kotlin users, but Java users of the same library will find it inconvenience.
And so, if… if it is important that Java users are able to use it as well, something you can't do in Kotlin, and something you have to shape in a specific way for Java users to be happy with it.
But if we don't care.
**Jason Plumb** 39:20 I would say for this project, for OpenTelemetry Kotlin, no, we don't care, because they have a… like, they have a very mature Java API that they can use.
Right. Right. So there's… I don't think there's a compelling reason for a Java developer to use the Kotlin API, or the Kotlin SDK.
**Ivan “CLOVIS” Canet** 39:38 But that does mean that, forever, OpenTelemetry will need to have both a Java SDK and a Kotlin SDK that are different.
**Jason Plumb** 39:46 Yes, yeah. They're different, they're different implementations, but the API surface is basically the same.
Like, they still adhere to the same specification.
**Ivan “CLOVIS” Canet** 39:55 Right, but basically the same, it's not… like, it's not binary the same, right? If you want to… if you have a mixed Java Kotlin project, you have to design one of them, and you can't… like, using both isn't… Good idea, right?
**Jason Plumb** 40:08 It's true, yeah. So for those hybrid, combined, multi-language projects, it certainly gets complicated, and I don't know off the top of my head what the answer for that is, or what the strategy long-term is for that.
**Ivan “CLOVIS” Canet** 40:22 Okay.
**Jason Plumb** 40:28 Cool.
Well, thanks for joining, Clovis. Nice to meet you, and hopefully we'll see you in the PRs, and hopefully next week.
**Ivan “CLOVIS” Canet** 40:39 I'll take a look, yeah.
**Jason Plumb** 40:40 And Viorel, thanks for all your work as well. Thanks, David. Carlos. Have a good rest of your day.
**Carlos Alberto Cortez** 40:45 Nope.
**Viorel Alexandrescu** 40:45 Good one.
**Jason Plumb** 40:46 Take care.
**Ivan “CLOVIS” Canet** 40:47 Have a good day.
