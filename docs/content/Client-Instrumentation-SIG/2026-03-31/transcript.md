SIG: Client Instrumentation SIG
Date: 2026-03-31
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Martin Kuba** 00:55 Hi there.
**Jason Plumb** 00:59 What up?
**Martin Kuba** 01:04 How's, how was your time in Amsterdam?
**Jason Plumb** 01:07 It was nice.
Yeah, I was there for, like, 12 days.
I'm still very jet-lagged, though.
**Martin Kuba** 01:16 Damn.
**Jason Plumb** 01:19 Yeah, the weather was great, like, the first few days was, like, really just, like, clear and, like… In the 50s, like, kind of ideal temperature, and then, like, the last few days, it got cold, and like, it was, like, it was, like, at one point, it was snowing and sunny. It was like, what? It was clear, and it was snowing. It was very weird.
Hail a few times.
**Martin Kuba** 01:44 Spring, yeah.
**Jason Plumb** 01:45 Yeah, totally.
**Martin Kuba** 01:48 Yeah.
I've never… the only time I've been in Amsterdam is just at the airport. I've never actually been in the city.
**Jason Plumb** 01:58 Yeah.
Not my favorite airport.
**Martin Kuba** 02:02 Jim.
**Jason Plumb** 02:07 Well, do you want to share screen, Martin?
**Martin Kuba** 02:10 Sure, yeah.
**Jason Plumb** 02:35 I think Hanson might be out. He didn't join the, Android meeting before this one, so we might… Not dwell too long on the crash semantic conventions, although it would be nice to have these… merged… I think I haven't even reviewed this at all.
Cool.
Yeah, having a crash event would be great.
Yeah, I don't think we have to… I don't think we have to dwell on it too much, but yeah, for those interested.
Please review and comment. Let's help get it across the finish line.
**Martin Kuba** 03:30 So you have, you have had, the Android SDK has been capturing crashes now for a while, yeah.
**Jason Plumb** 03:39 Yes.
**Martin Kuba** 03:41 So are you, so obviously you have some semantic conventions in the instrumentation. Are these… are these aligning?
With what you already have, or are you gonna have to go back and change?
Some of it.
**Jason Plumb** 03:56 I don't know the answer to that, because I haven't reviewed this, PR.
**Martin Kuba** 04:00 Okay, okay.
**Jason Plumb** 04:01 But I suspect it's close.
**Martin Kuba** 04:05 Yeah.
**Jason Plumb** 04:07 But also, whatever, it's not stable, right? So, I mean, if we have a semantic invention, we will try and align with that.
Yeah. From there, so if it's wildly different, then I think we would change Android to match.
And deal with the fallout from that. I mean, it's not… it's not ideal, because… Maybe we'd have a way to override or get the old behavior.
Because we don't want to break people's expectations of existing crashes.
But I think we'd probably want to start using the new stuff, and have a way to fall back.
**Martin Kuba** 04:40 Yeah.
Okay.
**Jason Plumb** 04:44 But none of our instrumentations are stable.
**Martin Kuba** 04:47 Yeah.
**Jason Plumb** 04:49 So, we… right now, we have emitDevice.crash, and it has 4 attributes.
exception message, exception stack trace, exception type, and then thread ID, thread name. So, it's not… I don't know why the service name is on there.
Anyway, I need to… I guess I should probably review that PR.
**Martin Kuba** 05:16 Yeah, that's interesting. ServiceName probably should not be here, but… Okay, yeah, sounds good. That's good to know.
I have the next, topic. I… This has been a discussion for a long time, very much related to what we've been talking about, metrics, right?
So… We have been… I don't know if you recall, Ted had this OTEP for entity provider.
You know, we've been talking about modeling sessions as entities.
Which currently we don't do, but it… But I, think that's what we still want to do, yes? Like, are you do… are you in agreement in the Android sake that we should move away from the session ID attribute on… On signals and put it as an attribute, as a resource attribute or entity attribute.
**Jason Plumb** 06:17 we have so much going on right… over there right now that I don't want to even think about this, and I would just love to continue… but it's probably the wrong thing. Like, ideally, conceptually, I think… The future wants us to be using the entity stuff, but, Implementation-wise, it's a pain in the ass.
**Martin Kuba** 06:39 Yeah, so there has been, josh Surath, created this… I think they worked on… they worked on update to spec?
To add… This, for entity method.
Let's see, I don't know if I can find it. I don't know if you've seen this.
**Jason Plumb** 07:03 haven't.
**Martin Kuba** 07:08 Oopsie… Yeah… This is not it, though.
Where is it?
Was it inspect?
Yeah.
Yeah, so this was originally… I think intended, or the end of the SIG thought this would help us.
So instead of this, Instead of… let's see… having an entity provider, like what Ted was, suggesting in the past, They were… they're adding, essentially, to… to meter provider, this four-entity method.
Which allows you to, at a, you know, at a certain point in the SDK's lifetime, you can call this with the updated entity, and it gives you… gives you a new meter. I think, actually.
**Jason Plumb** 08:38 A new meter provider, probably.
**Martin Kuba** 08:39 And it's essentially, like, it's which one is sharing, like, the same configuration as the one that you initialized.
But you can… you can start collecting metrics for… You know, for that entity, like, with the entity's, attributes.
So I worked on… I was looking at this, and trying to see if it would help us with… what we're looking for, but I don't think it does, because…
**Jason Plumb** 09:10 At first glance, I think this has the same problem.
**Martin Kuba** 09:13 Same problem, yeah.
**Jason Plumb** 09:14 Because, like, the record is what matters, right? You're trying to record a value into your meter, and it's, like, you've got this meter set up, and you're counting something, for example. Yeah. You're increasing that count every so often, and then the session changes.
Right? Which means every time that you go to record a value.
You still need to go through this entire chain here if you want to recognize.
**Martin Kuba** 09:37 is…
**Jason Plumb** 09:38 Unless… Unless you store and use the same meter, and you have something that asynchronously, like, knows when or gets notified when the session changes… And then you can replace your meter with this construct.
**Martin Kuba** 09:56 Yeah.
**Jason Plumb** 09:56 And then you're not having to do this entire chain all of the time, it's only when it updates. So that's kind of nice, I guess.
**Martin Kuba** 10:05 But it's all…
**Jason Plumb** 10:06 It still runs the risk, then, of… like, you have to be… I think it forces all of us, both… like, instrumentation and SDK and really browser mobile implementations.
To be super thorough and ensure that you're doing this change everywhere, because otherwise you're gonna be, like, sometime down the future.
You could still be emitting telemetry for the old session.
**Martin Kuba** 10:29 Yes, yes.
**Jason Plumb** 10:30 So it's like, literally every single place that emits telemetry has to be updated when the session changes.
with this approach.
**Martin Kuba** 10:42 Yeah, and… So, like, for the session, like.
For something like the session, like, we're thinking about it as the, like, a global… state, right?
**Jason Plumb** 10:51 post…
**Martin Kuba** 10:52 all the signals that are being emitted, so… Like… I guess, like, if the… If, like, if you had some instrumentation that was… you know, creating its own provider, that can be isolated. That doesn't really solve our problem, yeah.
So anyway, so what I did, I was working on this… Prototype in, in browser.
But what I… Let's see… What I came up with… Essentially, was that, we need to have some kind of… we would need to have some kind of, and I didn't do this for metrics, actually, I did it for logs, because I think we… that's the thing that we care about the most.
**Jason Plumb** 11:50 Sure.
**Martin Kuba** 11:51 to start with, but, like, so let's, like, as an ex… an example, I have this, provider, and that provider… if you have an instrumentation That gets the provider from the global registration.
**Jason Plumb** 12:09 Yeah.
**Martin Kuba** 12:10 Then that provider, right, doesn't change inside the instrumentation, and… but you need to be able to, like, update it then from… from some central place. So, I do have… I did implement a for entity that, like, This is essentially, like, a proxy or, like, a wrapper, and so it does have, like, a provider inside that it delegates to, but from the, like, API perspective, like, I added, like, this set entity.
method.
and… Then it uses the for-entity one, like, to create, like, the underlying provider.
So anyway, like, from, like, an API perspective, I was thinking, like, this for entity doesn't help us, like, what we need to do is, like, have some kind of, like, global API where you can update the entity, right?
Like, something like this.
And the other… the other issue is, like, when you have… when you have instrumentation that… that gets longer.
from the provider, And you update the entity.
Then… and then the logger needs to pick up those new attributes.
So without the instrumentation necessarily having to, like… like, either, like, the instrumentation would have to be notified that that change happened… happened.
Or it would… or the logger would have to do it, like, internally, somehow.
If that makes sense.
**Jason Plumb** 13:43 It does. It's just, yeah, it's really complicated to think about Every single instrumentation, or every single place where you're using… A meter, a logger, a tracer… Having to be changed.
when the session changes. That feels like a big blast radius.
**Martin Kuba** 14:02 Yeah.
**Jason Plumb** 14:03 I wish it… yeah, so to your point, I think I wish it was… Some… just, like, some global thing that you could flip.
But…
**Martin Kuba** 14:11 Yeah.
**Jason Plumb** 14:11 Yeah.
**Martin Kuba** 14:14 So anyway, like, we're… like, this is, like, if you want to take a look at this, and, like, let me know what you think, I mean, if you have some other thoughts.
Essentially, this whole idea is that, like, there's this… we have, like, in our SDK, we would have this, like, entity-aware… Provider and Entity Aware Logger.
Which… Which is basically a wrapper on something that can be changed behind the scenes, so… But, like, from the instrumentation perspective, that's what it interacts with. So, like, when it… when it calls, like, logger emit, like, it will always… Take the latest, and… So that's one thing, like…
**Jason Plumb** 14:58 Say that again. So, anybody who's using this class, right? Yeah. At some point, they call, NCAwareLoggerProvider.getLogger.
**Martin Kuba** 15:08 Correct.
Yeah.
**Jason Plumb** 15:10 And they hold onto that instance for a long time, right? And they're calling it logger.log, but logger.
**Martin Kuba** 15:15 Yes.
**Jason Plumb** 15:15 Logger.log. And then the session changes, and they call logger.log again.
That same logger instance they're holding onto.
It gets changed because it's a proxy.
**Martin Kuba** 15:28 It's a proxy, yeah.
**Jason Plumb** 15:30 Okay… okay.
**Martin Kuba** 15:34 So, yeah, this proxy logger is getting, like, you know.
the instance of the provider, and then, like, when it's emitting, like, it's just calling.
**Jason Plumb** 15:45 Oh, so it's getting the logger every time. Got it. Okay.
**Martin Kuba** 15:49 Yeah.
**Jason Plumb** 15:50 Though it's encapsulating that, okay. Santosh, sorry, how long's your hand been up? I didn't know.
**Santosh** 15:54 No, no, no, yeah, it's fine. I think… I'm trying to understand this, and I'm not fully up-to-date on things.
**Jason Plumb** 16:01 That's fine.
**Santosh** 16:02 So, the session changes in the session, they… it is typically a concern of the SDK, right? Not the instrumentation of this provider.
**Jason Plumb** 16:14 The SDK knows nothing about session. The… I mean, on the client side, that boundary is a little blurred, right, between, like, what's an SDK and what isn't. When you say SDK, I mean the OpenTelemetry SDK?
**Santosh** 16:26 Correct.
**Jason Plumb** 16:26 The OpenTelemetry SDK knows nothing about session.
It's a concern of the resource.
Which I guess is a component of the SDK.
**Santosh** 16:38 Hmm. I was wondering, you know.
Both in the mobile and the browser, whenever the session changes, you know.
it is okay to re-initialize the, you know, all the providers, all the SDK.
It's a one-time change, and these session changes don't have You know, that frequently.
**Martin Kuba** 17:04 Push.
The question is.
**Santosh** 17:06 solve this problem, or… You know, just manage it.
**Martin Kuba** 17:11 Yeah, I mean, this is essentially what hap… what does happen in this prototype, like, when you… when you… But the question is, like, what that would look like from the… from the API, like, from the instrumentation perspective, what… like, how it would interact with it.
So, like, here, like, when somewhere, like, in the SDK, like, where we manage sessions, like, when the session changes, the entity changes, then, like, we call setEntity on the global provider, and it creates a new, new, like.
You know, the delegate provider from… by just calling it for entity.
**Santosh** 17:47 Correct, but the part that I'm, confused is… the logger API, any of the APIs, when they emit messages, whether spans or logs, you know.
only when the control comes to the SDK components, you know, that's when the updated session should get attached, right? And… And so the APIs should… not… be concerned about… Attaching to an entity, or a… human resource.
**Jason Plumb** 18:25 I'm not sure if I followed the question.
**Martin Kuba** 18:27 Yeah.
**Santosh** 18:29 Okay, never mind, I, I'm…
**Jason Plumb** 18:33 The OTEP that was proposed and merged was to do this thing called for entity, so, like.
If an entity changes, you can tell the provider to give you kind of a new view of its current configuration, but with this one thing added or changed.
I think that's what the OTE… from this call today so far, that's what I've gleaned.
**Martin Kuba** 18:54 Is that…
**Jason Plumb** 18:55 Yeah, this OTEP, when you call for entity on your meter provider, you basically get a new meter provider.
And it's true of log… let's call it a logger provider, right?
Like, can you show your implementation again, Martin?
Like, the result type of forEntity… is another logger provider, right? So we're in a logger provider. When you call for entity, you get a new logger provider.
A different logger provider that is backed by a different resource.
**Martin Kuba** 19:25 Yeah.
**Jason Plumb** 19:27 And so it's then the responsibility for all of the places that use The logger provider, or anything that was previously created by that logger provider, to sort of refresh.
to, like, use the new changed instance, and not hold onto their old one. What Martin's done here is always returned a proxy whose internals then can change anytime the entity changes.
**Santosh** 19:52 Yeah.
**Jason Plumb** 19:52 And that lessens the burden on all of the callers, right?
all of the users of this class. That's my understanding of what's happening here.
**Martin Kuba** 20:00 Yeah. Yeah.
**Santosh** 20:02 proxy implemented? Does it, like, have a… Observer that detects.
A change in the entity.
**Martin Kuba** 20:12 Yeah, I mean, so… It, it does… it's a proxy pattern, right? So, like, when you… and I'm basically, like, making an assumption here that all the instrumentations would always get the provider from the global registered provider.
So, like, we would… we would register this… this entity-aware provider to be the global one.
And which is actually just a proxy to the, like, to this, This actual one that provides the, you know, all the implementation.
And then… then, like, when you… on this one, when you call, you know, get a logger, then it actually gets… gives you an instance of this proxy logger.
And the proxy logger… Always kind of delegates to the, To the… to the up-to-date provider that's held in the… Proxy provider, if that makes sense.
I mean, is it… is it a… is it… I… like, I… maybe, like, I don't know, like, if this is a safe assumption.
To make that you would always have One global provider.
Right. Maybe not.
**Jason Plumb** 21:42 I mean, I'm following this approach. I would really love to have cycles to do a prototype in Android to see what it looks like as well, or Kotlin, even, just to see.
I like the fact that I think… I think this allows you to change the session, then, without having to do it in every single place, then, right?
**Martin Kuba** 22:00 Yeah,
**Jason Plumb** 22:01 I like this, I think it's a pretty decent pattern.
I do think about what you were describing, though, is there a way for… Naive usages to get and do the wrong thing.
But if this is hooked into the actual SDK provider, then I think it's fine.
**Martin Kuba** 22:22 Yeah.
I think… and so that's just… I just wanted to, like, get your thoughts on this, like, you know, you don't have… We already talked about this enough, but the other part of this is going back to… Whether we want to support the metrics API SDK in client applications.
at all.
Because, I mean, I think even if we do this, like, we still have… I mean, the… The issue with… with metrics, Doesn't go away, right?
**Jason Plumb** 23:01 Yeah, I think it's a separate concern.
**Martin Kuba** 23:02 several concerns. And when I was talking to Josh, Josh about this, He was basically saying that maybe, maybe, like, if we, as a client group, Do make next… like the… recommendation or… or decision that, like, we don't want to… we don't really care about supporting metric SDK at all, like, in the client, then… then what I have would… would, you know, probably work fine for us, for… for, like, the logger provider and for this trace provider.
**Jason Plumb** 23:41 But why doesn't it work for metrics?
With meter provider, just because of the types.
**Martin Kuba** 23:46 Well, because of the cardinality, and…
**Jason Plumb** 23:48 No, no, I mean that… but you could still build… you could still build a meter provider that does the same thing.
**Martin Kuba** 23:54 Yeah.
**Jason Plumb** 23:55 for entities, it's just whether or not it's worth doing, and it's the most complicated one for maybe little benefit, is that what you're saying?
**Martin Kuba** 24:02 Yeah.
**Jason Plumb** 24:03 Yeah.
We would… so far on Android, we would probably want to have parity between all three, because we haven't yet.
Taken a hardline stance on no metrics.
we're leaning that way, I'm relaxing my opinion on that, I think… I'm kind of okay with people having that foot gun, and then dealing with the cardinality in their back ends, if they want to.
But… I don't know.
Separate topic.
**Martin Kuba** 24:30 Yeah.
**Jason Plumb** 24:33 I like having the parity, and I think if you don't build it for metrics, people will be surprised. You'll have users that are like.
I just want to counter, dude, like, where's my… how come it's getting the old session? You know?
**Santosh** 24:46 So, Jason, quickly, just a couple minutes on that topic.
**Jason Plumb** 24:51 Yeah.
**Santosh** 24:52 You know, couple thoughts.
is, I think, in general, you know.
just based on some brainstorming with, you know, AI systems, I think what I noticed is… that the metrics API may not be… the calls may not be idempotent, so when there are… Networks that are unreliable. If you end up sending the same data point twice, you know, there is no way to know that.
Unlike, unlike, you know, spans and logs, you know, where you can have, an ID, so you, you can't… even if you send the same span twice, you know, you know it's the same span.
And secondly, in the mobile case, it's not uncommon.
For the device to go offline, so you will… end up… You know, sending, data late.
And generally speaking, many metric systems, you know.
Have a limit to what extent they support a late arriving data.
And… And there is a case for reliability. Like, in general, the client environments are unreliable.
**Jason Plumb** 26:08 Open the game.
**Santosh** 26:08 There's difference to the, you know, Back-end, more controlled environments, and… That's one case.
Against.
You know, using metrics.
**Jason Plumb** 26:21 is because some backends will limit the age of… the age for which it will continue to receive or accept metrics. Yeah. Measurements, data points. Yeah.
Yeah, I mean, that's probably true of tracing as well.
Probably less true of vlogging, but… I think even spans of a certain age will get dropped.
**Santosh** 26:42 Correct.
**Jason Plumb** 26:42 Yeah.
But, like, when the thing is up and working just fine.
I don't know. Yeah, I mean, it's worth… it's another data… it's another thing to consider.
**Martin Kuba** 27:02 Yeah.
Yeah, I don't… you know, to be honest with you, I don't really fully understand, like, the implications myself, like, I haven't experienced it, but, like, Josh was saying that, like.
That, that, like, he… he… like, it's been really difficult to figure out, like, how to update the metric, the state of the metric SDK, like, when… when the resource would change, that it creates a lot of problems. I don't know, like.
if… I don't know, like, if it's still the case, like, with this pattern, like, if we had, like, a meter provider that just, like, does use the… the set, you know, the for entity method, you know, under the hood, like, if it's still… like, what the issues are with this, I don't understand.
**Jason Plumb** 27:50 Oh, I do, I think I understand. I think you get a new instrument.
**Martin Kuba** 27:54 Okay.
**Jason Plumb** 27:54 Right, which means that your… whatever aggregations you're doing are then changed.
**Martin Kuba** 27:59 Yeah, okay.
**Jason Plumb** 28:00 Yeah, cause the… I think… I think the instruments are stateful.
**Martin Kuba** 28:06 Okay.
**Jason Plumb** 28:06 You can imagine something that's a cumulative counter, for example. It's gotta know what the current count is.
And if you create a new one, I think you lose that.
**Martin Kuba** 28:18 Okay.
**Jason Plumb** 28:19 Yeah, interesting. I don't want to implement that.
**Martin Kuba** 28:25 Yeah. So, I mean, I… I just… I don't know. Like, I don't know, like, if we… if you should just, like, push people away from it, or… include the, metric SDK and just, like.
A lot of people fail, you know, like, if they want to use it, they can use it, but…
**Jason Plumb** 28:44 That's kind of… that's kind of the stance we've taken on Android, for good or ill, right now. We do expose it. You can create… I mean, we expose everything in the SDK.
And if you want to get a meter provider and get meters, you can do that.
**Martin Kuba** 29:03 Yeah, but the question is, like, how useful it is, like, if there are actual, actual use cases for it.
**Jason Plumb** 29:08 You're right.
Well, I appreciate you showing me this, and I made a note to look at it in all of my free time, which I don't… But I would like to see what a strawman, you know, implementation in Android or Kotlin looks like. And I hadn't seen, or I hadn't been following the entity… Otap, so I'm glad you showed me that, and I appreciate it.
**Martin Kuba** 29:30 Yeah.
Sorry, we're over time. Did you want to talk about this really quick, or…
**Jason Plumb** 29:35 No, I don't. No, it's out there, if you want to look at it, if you care about network timing, go look at it. If not…
**Martin Kuba** 29:41 Actually, so just really quick, like, we actually have just had this discussion in the browser sig, and we are leaning towards implementing our resource timing with these semantic conventions.
**Jason Plumb** 29:51 Cool, we'll give it an approval then.
**Martin Kuba** 29:55 Alright.
**Jason Plumb** 29:55 Alright, cool.
**Martin Kuba** 29:57 Alright, thanks.
**Jason Plumb** 29:58 Thanks, thanks. See ya. Have a good day.
**Martin Kuba** 30:01 True.
