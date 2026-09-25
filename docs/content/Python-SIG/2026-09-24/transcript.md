SIG: Python SIG
Date: 2026-09-24
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Diego Hurtado (Dash0)** 00:31 Hello, everybody.
**Tammy Baylis** 00:36 Hey, Diego. Hey, everyone.
**Riccardo Magliocchetti** 00:39 Hey, everyone.
**Tammy Baylis** 02:19 Hey, everyone. Welcome to the Hotel Python SIG once again.
the, notes are in the chat.
And as people trickle in, I'll just start with some triage. We'll go till 9-10!
So… Always a lot of PRs we can look… just a quick refresh. We can look at the Contrib list first.
Go past the maintainers… Go past the really old waiting on reviewers, and… Look at the recent… Waiting on reviewer's PR, so quite a few new ones today.
From StrawGateOpAmp Client… 2 hours ago.
Oh, I do not know much at all about the op amp.
I know.
**Riccardo Magliocchetti** 03:22 Yeah, you'll be an issue in the… I said to OpenPR, so I'll take a look.
**Tammy Baylis** 03:28 Awesome, thank you, Riccardo.
GRPC… Four hours ago, JSTAR fixes.
Relatively new issue. Also… Reattaches and ended parent… oh, hmm.
So, I know that the SEM call for gRPC is still very much in flux, but this doesn't have anything to do with that, so that kinda… Stops the yellow light in my head.
Yeah, steps to reproduce… great. Budget issue, I think.
Oh, I should have marked the other one as… Hmm.
Ready for review.
And I should have marked this as ready for review.
Go.
Flask fix. A different Riccardo.
Older bug… Oh, reported by the last same person.
S-S-E spa… Okay, great.
Hmm.
Do one more. IBM MQ instrument… -Oh. New instrumentation package.
Hmm.
Yeah, with any… with any new, suggestion for a community instrument, or… We're always gonna ask if they're gonna support native instrumentation, yeah.
Adding the instrumentation inside IBM's IBM MQ client itself already ships a small OTEL module for trace context propagation.
Hmm…
**Riccardo Magliocchetti** 06:18 the second problem is not really a problem, I guess.
**Tammy Baylis** 06:22 Yeah.
**Emídio Neto** 06:23 Yeah. I'd say the same.
**Tammy Baylis** 06:30 But yeah, this…
**Riccardo Magliocchetti** 06:31 Yeah, probably the stream material should go into PyMQI more than… IBM MAQ, I guess.
**Tammy Baylis** 06:42 So… Hi, CISOP's name? Yeah.
Oh, Mike's here, hello.
cut this… B… implemented as Native Hotel Support, and I… MQI… Senator… Have you looked into?
Okay, I think that was what we wanted to say.
I think that's good enough. Cool.
Okay, 2 more minutes. Let's look at the core PRs.
For a second.
Oh, yeah, I… this is a topic I've added to the list, we can get to that later.
Detect… so Lukas has looked at this one already. Detect character pattern wall card.
This is ongoing, great, thank you.
Hmm… I looked at some of these last time.
Just be ready for a few.
We'll look at this later.
Hmm… Let me look at this… Yeah, I think we talked about this.
Right, docs update, shouldn't review this.
Okay, 9-10, we'll stop triage there for today. Thanks, everyone, for contributing and reviewing.
I'm sharing already, we can go into a few topics. I put in a couple first.
This one is, I think, part of what I brought up last week about, Ahmed, a newish contributor, wanting to, implement a lot of the missing DB instrumenter metrics. So, we re-scoped this PR to not have an opt-in, and all it does is, just modernize the metrics for connection, db client connection count, and it is a small breaking change.
But it'll… name it properly, I've approved it. Just, please have a look, and then I'm gonna keep, working with them to… do more PRs.
That's just an advertisement. My second topic is… This PR, I didn't have anything to do with, with this implementation, but it came… Into my feed, so I just wanted to see what others think.
Dotify reported it and did the PR, and there's no… Safeguard… wrong word. But, if… user sets export time up millis in the Batchman processor to a negative value, then it just, doesn't trace back, which isn't great.
The… Yeah, from my point of view, I think if we did want to introduce the catch of that value error.
specifically for OTELPython, then I think it makes sense, because the way we have things inter… implemented is that If users wanted to not have, an interval, i.e. just do it kind of synchronously, then we ask them to do infinity.
It's a deviation from what Java and .NET do, because if they set zero.
Then that's their way of doing… No batching, or, like, continuous?
So yeah, I just wanted to see what people think if this change is okay, or if we should… do something else.
**Carlos Alberto Cortez (Dash0)** 12:02 I have a question. Our… Are the rest of the, components using this, like infinity? Is that a common thing for the rest?
**Tammy Baylis** 12:16 I think it is also in place for the JSON exporter.
**Carlos Alberto Cortez (Dash0)** 12:23 Okay.
I'm asking because, according to the specification, 0 should be the value for infinity. However, this was added, kind of late in the game.
So it's a shoot.
So, in theory, it would be nicer to have zero, but if the rest of the components are using infinity already, it's probably late. Yeah, correct.
Okay.
**Aaron Abbott (Google LLC)** 12:52 Can we… can we… well, I guess two points. One, can we support both? And then… To, it seems like if you did pass infinity, even if we didn't check it, it would just effectively have the same result, because the timeout would never be reached, right?
**Tammy Baylis** 13:10 Yeah.
Diego.
**Diego Hurtado (Dash0)** 13:15 Yeah, just, maybe a question for Carlos. Actually, just curious why… Why other languages are not doing the same thing.
Using Affinity as well.
**Carlos Alberto Cortez (Dash0)** 13:29 I think that everybody had different understanding, and there was some prior art.
In some, libraries, like Java, I think there are a few different HTTP libraries that use zero.
As not, you know, as infinity, no timeout, and that's why it came from there.
And it seems it's like an extended use, at least in other languages as well.
But then, of course, there was a confusion on that specific case.
Yeah, so that's why it was added late.
**Diego Hurtado (Dash0)** 14:04 Alright, thank you.
**Aaron Abbott (Google LLC)** 14:06 Yeah, I mean, if it's in the… the semantics are a bit confusing with that, but if it's in the spec already, I suppose that's just the way it is. Maybe we should pay closer attention from our SIG, but I was gonna mention, I'm pretty sure we support infinity in one other place, or some other magic value for the export interval.
If you set it, I believe it's to infinity, it will just not create the background thread.
At all.
And then it lets people just do… Force, like, call force flush instead, so…
**Lukas Hering** 14:42 Yeah, that's for the periodic exporting metric reader.
**Aaron Abbott (Google LLC)** 14:45 Yeah, exactly, yeah.
**Tammy Baylis** 14:54 Yeah, thank you.
Yeah, sorry, Dylan, go ahead.
**Dylan Russell** 14:57 Yeah, so separately, I don't think we actually passed this in.
We don't ever pass this into the export call.
So we could also… Update the code to do that.
And I think… I'd have to look at, like, the… Exporter interfaces to see if they… Except millis or, like, floats.
Because I think, the OTLP exporters accept floats.
And that was, like, a somewhat recent change, because I think when I was… Like, looking at this before, we didn't accept floats into the export function, but we do now.
**Tammy Baylis** 15:51 That's… that's even better, that's even more complicated.
**Dylan Russell** 15:56 Yeah.
And there's also, on the OTLP exporters, we… you can set the timeouts for those through NVARS, and I think… Those will get overridden.
By what gets passed through to… export explicitly.
I don't know if that's, like, what the spec… Wants us to do or not, but that's another thing to, like, look into.
**Tammy Baylis** 16:28 Okay…
**Dylan Russell** 16:32 Yeah, I can add a comment with those things.
**Tammy Baylis** 16:35 Okay. Yeah, thank you, Dylan. Right, so this is, To catch the value error, I guess, wouldn't do much harm, like, very short-term, but turns out it's, Bit of a… a big… big mess in terms of consistency, even within our own implementation, so… Yeah, thank you. If you could add your… your thoughts, Dylan, that'd be great, and I'll… I'll add my own later, and… We can see how we proceed.
Right.
Oh, and thank you, thank you for… Person taking notes.
Okay, Lucas, log stability…
**Lukas Hering** 17:25 Yeah, I guess… it looks like, I guess, yeah, just to point out, I think we merged the last, or one of the last PRs for, that were… that's for log stabilization. There might be one more in contribib, Actually, I think that I might have linked the wrong issue, sorry. But the question I wanted to discuss is, I think that for, That we should probably try to target, the… not this coming release, but the next release to stabilize logs, if possible.
And the one question that we kind of need to address is how do we want to go about adding or removing the… the import paths for logging. Do you actually mind if I take over screen share briefly?
Motorship.
**Tammy Baylis** 18:29 Yeah, one second, stop… Stop share.
There we go.
**Lukas Hering** 18:40 Okay, let me see here… okay.
Yeah, so… B.
I'll close these out.
So, yeah, so currently we have, logs are under this underscore prefixed namespace within the SDK, but, the… I guess where we, where this… if we just remove this namespace when we stabilize, or change it to just regular logs, the concern is that this would then break, exporters. So, like, for example, the log exporter HTTP log exporter, imports directly from… From this… this private namespace?
And, so, yeah, so when we do stabilize, I guess the idea that I had is that we can add the public The public import path, and then keep this around for at least a few releases, so that, existing exporters don't break.
This is, like, particularly an issue because… The, like, the constraint here is, Unless we do a major version release, this would mean that… technically, current and all previous versions of the exporters are compatible with all new versions of the SDK, so we technically can't So if we remove this, it would kind of break prior versions of SDKs. So I guess, just kind of curious what others' thoughts are here. Like, should we just, keep this around for a bit, add the new path, and then eventually remove it, or are we okay with just removing it right away? Like, again, it's technically… I mean, this is still private, this log exporter, but, you know, with auto instrumentation, it does automatically pull it in.
Yeah, Aaron?
**Aaron Abbott (Google LLC)** 20:44 Was I before you, Leighton?
Not sure.
**Lukas Hering** 20:47 I think…
**Leighton** 20:48 Yeah, yeah, go for it.
**Lukas Hering** 20:50 Okay.
**Aaron Abbott (Google LLC)** 20:52 Yeah, I was just gonna say, I think for metrics, we might not have done that, but we also didn't have it in this… Indeterminate state for almost, like, 3 years or whatever, so, I think it makes sense to leave.
you know, try to keep backward compatibility with these import paths for some time.
And maybe we can… I think we have this, like, internal pattern where we just expose an init file, so it should be pretty easy to… Hopefully do it cleanly, and I guess we might need to leave it around forever because of this exporter issue, like you mentioned, Lucas, but… That makes sense to me, Leighton?
**Leighton** 21:34 Hey, are you guys doing your streaming properly?
**Lukas Hering** 21:37 Yep.
**Aaron Abbott (Google LLC)** 21:38 Yep.
**Leighton** 21:39 Oh, cool.
Is it an option to… bumped the minimum… version of the SDK.
As a dependency.
**Lukas Hering** 21:49 Well, we do that every release. This year is, like.
1.40, for example, is compatible with all future 1.X versions, or 1.50, right? With this, this version specifier here.
**Leighton** 22:07 Oh, you mean, like, without a major version bump, right?
**Lukas Hering** 22:10 Yeah, we'd have to do it…
**Leighton** 22:11 That would entail.
**Lukas Hering** 22:12 doctor would just do a major version bump, but I… I don't know, like… Technically, like… We… we…
**Leighton** 22:19 Yeah.
**Lukas Hering** 22:20 Yeah, so…
**Leighton** 22:22 Yeah, I think that the hurdle for that is actually much larger than just supporting this for a couple versions, so… I'm… I'm for it as well.
**Lukas Hering** 22:30 Yeah, it's a little ugly to keep around this old name, but I think it's probably the preferable option. Just, yeah, I just wanted to make sure we're kind of all in line with this.
Okay, yeah.
**Leighton** 22:43 Yeah, especially because I think we were also discussing, like, perhaps just removing it.
Making sure the, API stability is… is there.
And then we'll have the… 1.0s in the future.
major version problems with the SDK.
Sorry, that's more like… implementation, so… Yeah, yeah, I'm good for this.
**Lukas Hering** 23:13 Okay.
Riccardo?
**Riccardo Magliocchetti** 23:15 Yeah, like, do we want to keep the logging handler around?
Because, like, it should be, like.
Already writing a message that is deprecated, and we're going to remove it.
**Lukas Hering** 23:31 I… you're talking about… I know there's a… a legacy… this is the… for the… I'm in the… this is for the log exporters, but are you talking more about the…
**Riccardo Magliocchetti** 23:43 SDK, if…
**Lukas Hering** 23:46 This guy, this, deprecated, Yeah, well, I mean, we could probably remove this. I was more concerned about the actual Keeping around the… this, like, these import paths here, this, especially this underscore logs one.
Are you… you're, you're just suggesting we remove, this handler.
**Riccardo Magliocchetti** 24:19 It was more of a question than a suggestion, but… Like, do you see it a problem to keep the underscore logs around, but remove something that is inside it?
**Lukas Hering** 24:31 Yeah, I… I think I would be more comfortable, like, still keeping this, but yeah, like, we could remove this, maybe, because I don't think… I think most people at this point have switched to the blogging instrumenter.
Yeah, yeah, I'm open… I don't really have a preference, so if we think that this can go, then that's fine.
I mean, either way, like, once we… once we do do a 2.X release, and whenever that is, like, then eventually we can just get rid of all this extra baggage, but…
**Leighton** 25:13 I'm okay with doing it as part of the, next major version release, the 2.X.
**Aaron Abbott (Google LLC)** 25:20 Yeah, I mean, the maintenance burden is very low for this.
**Leighton** 25:24 Yeah.
**Lukas Hering** 25:26 Okay, yeah, so we can keep this, I guess.
We can keep it around. I can see if we can add more. Looks like there's already deprecation warnings here, But… yeah, okay.
Yep, that's all I had for this.
**Aaron Abbott (Google LLC)** 25:45 Cool.
**Leighton** 25:45 Hey, Lukas, I have a question. So if… If we wanted to make a, kind of a… of… like, all-around push for this.
I think there's a current open issue tracking all the stability items, but it's a little bit outdated.
So that might be the best place to start, but I think there are a couple others who are interested in contributing, but… not… not… I don't think they know where to start, so…
**Lukas Hering** 26:17 Yeah, I…
**Leighton** 26:18 I can work together with you to help with that.
**Lukas Hering** 26:25 Yeah, sorry, there… yeah, there was a… I'm trying to, I'll, I can… I can find offline, but from what I was looking, I think, almost we're… if… if not already there, there's, like, there's very few remaining features we need, to be considered log stable, so I think, like, targeting the… The next release after this most recent one is pretty, pretty realistic.
**Leighton** 26:54 Yeah.
**Tammy Baylis** 27:15 Okay… Right, I'm sharing again, if nothing else. Next topic, Carlos, about the… GRPC Proto Exporter…
**Carlos Alberto Cortez (Dash0)** 27:27 Yeah, this is just, one more PR that, needs probably some final review. Diego already reviewed that, And there's one more review, but, That was done in the past, but it needs a final, you know, pass.
And, AIC has been waiting there for a little while, it would be nice to get some eyes on that. And, likewise, I was thinking about the Zero case.
But I didn't comment on the PR, like, trying to figure out what could be the answer, you know, from the previous conversation regarding the Ciro case.
**Tammy Baylis** 28:04 Right.
**Carlos Alberto Cortez (Dash0)** 28:08 Yeah, other than that, it seems that the PR was simplified from some other stuff that it included, but some other PR… actually was merged, so it's a very small PR. I suggest people take a look.
**Tammy Baylis** 28:28 Yeah, awesome.
Okay.
We'll take a look, thank you.
Last topic from Aaron, another please take a look.
**Aaron Abbott (Google LLC)** 28:43 Yes.
So this one has come up in the spec call a couple times, and, if you scroll down a… well, okay, first of all, it's, Kind of just, codifying And trying to standardize some of the stuff that we've probably already discussed, which is good principles for having an SDK or auto-instrumentation be easy to, like, inject, meaning auto-instrumentation in a broad sense, like across a host or in a Kubernetes cluster or something like that.
So… Yeah, if you can scroll down a bit… There's a comment from Jack, and he did… Some good research into, that one right there, with all the… where they tagged everyone.
He did some good research into… you know.
Which… which languages might not be complying with this statement right here, and… I guess I'll just read it. It's RTMS and runtime, shouldn't crash when the runtime or runtime version is not compatible with the auto-instrumentation or with the SDK.
So I think we have some kind of very basic checks for some of this stuff.
But, for example, we don't support, like, Python 2.7, so if you try to run the auto-instrumentation with Python 2.7, it might throw a syntax error really early on.
And, yeah, so… I see your hand, Riccardo. I'll just say, like, we have… we're really good about dropping versions, and I think, generally, as Otel, we've been more focused on, like, cloud-native sort of deployments, or, like.
You know, somebody manages their container.
And this is more focused on traditional observability or, like.
I'm gonna install the injector on my VM, which is running Debian from, like, 10 years ago, or something like that. So, I think… I'll let you go, Riccardo, but some of the things we could probably support pretty easily, I think.
**Riccardo Magliocchetti** 30:45 Yeah, like, I was asking if… So, like, is there the rational of his request? Because remember that the injector already checks The interpreter version before injecting.
And so, like, why we should move this, to the SDKs?
**Aaron Abbott (Google LLC)** 31:05 Yeah.
No, it's a good question. I think… I think in a lot of cases, as long as we have, like.
the interface between us and the injector, or us and the Kubernetes operator, really clear.
So, for example, we say, hey, you should implement your own site customize, and we make it easy to do that kind of thing, and it should import our site customize afterward.
it's probably fine. I do think there's, like, some duplication between, I assume, the injector and the CADS operator. I think the CADS operator, we've had, like, a lot of back and forth with them, and they tried to have not a lot of code upstream that wraps our stuff.
But yeah, the… if you read through this, If you read through this one, I think it's more… More about what should be possible, and not, like, specific requirements for, Stuff that we would have to do, but I do hear you, Riccardo, it makes sense.
**Riccardo Magliocchetti** 32:02 Yeah, it's like… it's… I know it's a should, but it's a big ask, like, it's like… keep everything working for forever. Like, for us, the syntax errors… Like, we should keep the syntax compatible with… something that is not maintained anymore since 10 years? I don't know.
**Aaron Abbott (Google LLC)** 32:22 Yeah, I mean, I think… having, like, a shim that works on Python 2.7 is probably a pretty small ask.
And to be clear, the ask here is that it should just fail gracefully if that situation is detected. It's not like we need to support Python 2.7 or.
**Riccardo Magliocchetti** 32:39 Yeah.
**Aaron Abbott (Google LLC)** 32:40 Python 3.1 or stuff like that, so… Yeah, I'm hoping some of these… like, some of them are probably just good to have, like, you know, somebody tries out OpenTelemetry Auto Instrumentation, or… you know, they run it on some old script they have, and it just crashes the program. Like, if it's a relatively a simple ask, I think.
we could probably do our best to support it, but honestly, I mostly just wanted to raise this to everybody, and… like, I'm glad we have thoughts, just, you know, please take a look at the… The PR.
**Riccardo Magliocchetti** 33:13 By the way, like, I agree that we should probably improve in this regard, and they're also sympathetic to the old dbian running on a VM, but yeah.
I was just, like… surprised by… The specific requests.
Grace?
**Aaron Abbott (Google LLC)** 33:36 Yep.
Cool. The other thing that was kind of mentioned in here, not specifically this comment, was around, like, vendoring, and that's something that was discussed in the spec.
So, I think… I don't think the tooling is really great in Python for vending, or at least I haven't played around with it a lot. I think in some cases, like gRPC, the tooling that exists probably just won't work, because there's native code.
And, it's not going to be able to copy all that, because it's, you know.
It has a whole toolchain and all that stuff, so… You know, we've… I think we've discussed the protobuf thing a couple times back and forth.
We had, we had, like, you know, these importlib discussions, import lib metadata discussions, and potentially vending them, We have dependency, I think, on URLib3.
For the exporters, so… Yeah, like, there's There's some recommendations regarding vendoring, and… Yeah, we should just consider, like.
the boundary we have between ourselves and the injector, and please take a look at this PR.
**Tammy Baylis** 34:53 Yeah, thank you, Erin, for being the… Point of contact and interface on this with everyone else.
**Aaron Abbott (Google LLC)** 35:02 No problem.
**Tammy Baylis** 35:05 Looks like…
**Aaron Abbott (Google LLC)** 35:05 We're at the end.
**Tammy Baylis** 35:07 Yeah…
**Dylan Russell** 35:09 I have one thing.
**Tammy Baylis** 35:10 Yeah, sure.
**Dylan Russell** 35:12 Just going back to the export timeout millis… Apparently, that's the amount of time The batch processor is supposed to wait.
Before canceling the call.
But in Python, I don't think there's any good way to, like, cancel.
and export.
**Tammy Baylis** 35:34 Yeah, I think…
**Aaron Abbott (Google LLC)** 35:36 I think we do… we made it work for metrics, but… the current… the current, trace SDK, and I'm not sure about logs. I don't know if they let you propagate the timeout into the, exporter or not.
**Dylan Russell** 35:54 Yeah, I don't think there's any export, or any timeout.
Hmm, like…
**Aaron Abbott (Google LLC)** 36:00 I… I could have sworn for, for metrics we have… we might not do anything with it, but I think we'd pass it through.
**Dylan Russell** 36:10 Hmm.
**Aaron Abbott (Google LLC)** 36:11 I can double check that one.
Or at least the API should allow us to do that kind of thing.
**Dylan Russell** 36:19 Okay.
Well, maybe there's nothing to do for logs and spans.
It's not like Go, where you have, like, the context thing you can, like, set a timeout on and, like, pass it through to the export call.
**Aaron Abbott (Google LLC)** 36:43 Yep.
**Dylan Russell** 36:47 Anyway, yeah, if anyone has more thoughts on that, I guess just… you can discuss on the issue.
Yeah, that was all.
**Aaron Abbott (Google LLC)** 37:00 Alright, see y'all next week, then. KBG.
**Tammy Baylis** 37:03 Thanks, everyone.
**Dylan Russell** 37:05 Yes.
**Riccardo Magliocchetti** 37:06 Yep.
