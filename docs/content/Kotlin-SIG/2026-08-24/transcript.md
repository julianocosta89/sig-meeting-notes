SIG: Kotlin SIG
Date: 2026-08-24
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Viorel Alexandrescu** 00:38 Hey, David.
Hey, Jamie.
Blue.
**Jamie Lynch** 00:50 How are you doing?
**Viorel Alexandrescu** 00:52 So, still.
**DavidGrath** 00:53 with stress.
**Jamie Lynch** 00:56 Oh, that's fine.
**Viorel Alexandrescu** 00:59 I mean, it's not because of something bad, it's, A couple of months ago, I was looking for user groups in Bucharest for Kotlin-related events, and… nothing came up, like, literally nothing came up.
So I decided to do my own thing, and I started a new user group, which got acknowledged by JetBrains, and I don't know if you saw, but because there's the 15-year event this year for Kotlin.
Yeah? Right. Yeah, exactly. I found the opportunity to organize a debut event for the community.
And it's not so easy tackling all of this stuff, like… talking to JetBrains as they said they want to send some, like, plush toys and, you know, merchandise and stuff, and getting people around, and finding people who want to be speakers, because at the moment, I'm the only one who actually has a topic to talk about.
And, yeah, that's… that's been taking up some time.
**Jamie Lynch** 02:03 Yeah, well, I hope that goes well for you. Yeah, it takes a lot.
Kind of organizing a community like that.
**Viorel Alexandrescu** 02:22 I'm waiting on Jason and,
**Jamie Lynch** 02:26 Yeah, I'll give him a few more minutes.
You know, in the meantime, Drop this in the chat.
And if anyone has… Anything we want to discuss, please add it to the agenda. Otherwise, I guess we'll go through these.
Well, I'll just give it another minute or so, and then we can… make a star. I know that Hansen's out this week, but…
**Viorel Alexandrescu** 03:52 Yeah, he might have said something.
**Jamie Lynch** 04:22 Okay, cool. I think we'll just make a start, and as folks join, The meeting link should be on the invite and also in the chat, so if you do have Anything you want to add onto the agenda, just feel free to edit the doc with a new bullet point down here.
**Viorel Alexandrescu** 04:40 Yep.
**Jamie Lynch** 04:41 And, yeah, we'll just start on the first, item, so… I think it's been about 4 weeks since we released, so I figure we'll probably do another release this week.
Oh, hey Jason.
**Jason Plumb** 04:57 Hey, sorry I was late.
**Viorel Alexandrescu** 04:59 That's okay, hello.
**Jamie Lynch** 05:02 So, is there anything that specifically needs to go in that one, or should we just kind of aim for kind of, like, midweek?
**Jason Plumb** 05:14 I'm not aware of anything specific that we should try and force or rush in there, I think it's… I think we're good.
I think last… I think last week we were talking about a couple of the stabilization ones, but…
**Jamie Lynch** 05:25 Hmm.
**Jason Plumb** 05:28 I don't think we should gate. I mean, we're gonna release again.
**Jamie Lynch** 05:30 Okay.
**Jason Plumb** 05:31 Yeah.
**Jamie Lynch** 05:47 Cool. So, I'm happy to take that on, unless anyone wants to volunteer for that.
**Viorel Alexandrescu** 05:58 Oh, that looks good.
**Jamie Lynch** 06:01 Okay, cool. I want to skip to this item first, because I figure it's going to be quicker than API stabilization discussions, so VOL, I think this was yours, right?
**Viorel Alexandrescu** 06:15 Yeah, yeah, yeah. Well, I am tackling the comments you left. I'll roll back some of the changes I did so that these, concerns are separated, because I wanted in the encoding PR only to tackle what it meant to encode.
to a specific format, and then in a different PR to actually tackle how do they get encoded to… how do they get written to a file, how do they get exported, because I saw that there's a standard way of doing it in the library, at least in OTLP exporters, or for, Protobuff.
And I thought maybe I should go by the same way, but you do have a fair point using the encode to stream function. From what I saw, there's nothing official at the moment.
in Kotlin multiplatform that… Would enable us to use any kind of stream.
only whatever OQ gives us through syncs and buffers, that's… that's about it.
I mean, yeah, sure, if you create a, an abstraction over it, and implement streams in the JVM implementation, yeah, that's gonna work, but otherwise… or maybe even for the Android target?
But the other ones, I'm not… I'm fairly sure that they won't work. So, I'll separate these, and once that's done, I'll hit you up for an approval.
**Jamie Lynch** 07:48 Cool. And, yeah, on the stream versus, like, string issue, I don't think that necessarily needs to be blocking for this BR.
But, yeah, I think the thing… I initially wanted to avoid was… If we're serializing an entire, like, piece of telemetry.
into JSON, and then holding it as a string.
That's potentially less efficient in the amount of memory we're holding on the heap versus just stabilizing it to, like, an output stream or something like that.
So, I think with OKIO, you can get a sync and then convert it to a… stream, Move out.
Yeah, I know that… for Kotlin Civilization… JSON library still has it as an experimental API, so I'm happy to skip that for now.
**Viorel Alexandrescu** 08:53 Yeah, I don't think we have a bridge to do it directly, because Okio at least needs an input. I think the only way we might be able to short… to use a short circuit on this is… maybe to write using byte buffers or something, because I saw Okio supports that instead of strings, but regardless which way we tackle it, it's still gonna be in memory.
So, unless we use that experimental function, I'm fairly sure we can't really avoid this, at the moment, at least.
So I'd rather we just keep it standard, like it's in the other places, and then see what we can do specifically there.
**Jamie Lynch** 09:37 Yeah.
I'd be happy with that.
**Viorel Alexandrescu** 09:41 Okay.
**Jason Plumb** 10:00 There's a third-party library that does it.
I'm not suggesting that we use that. I don't want to take a dependency, like, in the exporters especially, but I just was like, what's out there? There is one.
**Jamie Lynch** 10:13 What is it called, out of interest?
**Jason Plumb** 10:15 I'll paste it in the notes.
**Jamie Lynch** 10:17 Yeah.
**Jason Plumb** 10:17 Man.
**Jamie Lynch** 10:26 Kotlin Jason Stream.
**Jason Plumb** 10:28 And it targets KMP, apparently.
**Viorel Alexandrescu** 10:32 Yeah, I saw this.
**Jason Plumb** 10:34 Yeah, I don't know that we ought to use it, I'm just… it's just a reference.
**Jamie Lynch** 10:45 That's good to know that something exists.
But yeah, I feel like we can probably stick with, original one map.
**Jason Plumb** 10:58 Yep.
**Jamie Lynch** 11:01 Okay, cool. Ilia, did you want to talk about, OTLP civilization attempts? Yeah.
**Ilia Liferov** 11:09 Yeah, the lower ground.
Thank you, Jamie, for sending me the issue. I would just let you know that, I saw your comments, and, like, I see some, chance to improve. We need to deal with, Oh… memory, or retained memory, because you, you, you asked me about the baseline, and I've just commented that, Yeah, sorry for not being transparent. I forgot to mention the baseline board was, 37, so I think, like, the brute force optimization, doubled the retained memory, and this… Looks like the best performance impact from my point of view, and you as well.
Soul.
We need to deal with the references holding the telemetry list before the serialization, so I will take a look at this and, like, research the options to improve here.
And also, I noticed that GZP is configured, but is not enabled, apparently, so I will open the issue and… Take a look at this as well.
**Jamie Lynch** 12:30 Cool. Yeah, for Jisa, that'd be great if you could open up an issue, and then we can kind of, like…
**Ilia Liferov** 12:36 Nope, nope, we'll do it.
**Jamie Lynch** 12:37 Kind of, like, investigate.
That and, see what's going on there.
I think, just to give context to anyone who might be not familiar… might not be familiar with this issue.
is, I just opened this up, noticing that we re-serialize the payload every time we attempt to make a HTTP request.
So… yeah, I guess I thought naively we might be able to civilize once before… like, retrying.
But, there's basically some discussion here about Well, the trade-off there is you lose the… serialization cost and CPU, but you'll have to hold on to the payload in memory, so… The discussion here is basically around how much memory that's adding versus what sort of cost we're… not incurring anymore on CPU.
And allocations.
**Jason Plumb** 13:46 Yeah, that's a hard… that's a hard, equation.
**Jamie Lynch** 13:49 Hmm.
**Jason Plumb** 13:52 And determining, like, what the right balance is, is often hard.
I just would like to, like, encourage us a little bit to be careful of optimizing too early. You know, let's get some exporters in really, like, used code, and have them be put under load for a while, and see where things kind of play out before we try and be too smart with it.
It's kind of my instinct.
**Jamie Lynch** 14:21 Yeah, that's fair.
So… I guess… Kind of, like, following… that one thing we could do as an action is open up an issue about gzip encoding.
And… Yeah, I think… Having had someone look into this a bit more, my instinct is probably to leave the civilization Side of things alone for now, until we can… have… yeah, until, like, I guess the OTLV export is a bit… More stable, and…
**Jason Plumb** 15:07 Yeah, I like that. I mean, and GZIP also will be optional, right? Because there's a trade-off there, too, for… computation versus wire size. But yeah, I think having a separate issue for that would be great.
And I think that approach that you described is solid. Ilia, what do you think?
**Ilia Liferov** 15:25 Yeah, yeah, I agree, because, like, the trade-off is not, clear for me, and, like, from my point of view, like, GZ, let's start with, with this one. We'll see. I'm not really sure about the best practice, where do you store, or do you want to store any, I don't know, like, experimental performance, like, benchmarks or something like this, because, like, I have set up, my main methods and classes for… To, to do those, like, performance, Profiling and so on. And, like, I don't really know if you want me to… Aww.
Push those, or, like, Store it, somewhere in the library source code, or, like, leave it to myself.
Oh… That's… some kind of, like, organizational question, and, like, speaking of the performance, I think we would start with, GZ fix, and, like, do the profiling once again, and we'll see.
**Jamie Lynch** 16:44 Yeah, I think GZEP definitely feels like a good place to start.
From my perspective, yeah.
I guess… As far as, like, the benchmarks go, And this is just my personal take. I feel like if it's something we're gonna use quite frequently to… like, benchmark a specific piece of code, then it would be… potentially useful to add to the repo.
But if it's just kind of like a… one-off, or something we're gonna use a couple of times, then I'd be fine with kind of, like, leaving it, for now.
**Ilia Liferov** 17:23 And also, like, from my point of view, JZ would be the great first issue for me, since, it's like I'm new by here.
So I will open it and, propose a pull request.
And hopefully you'll understand me, because, like, I haven't used… I haven't speak English for a pretty long time, so, sorry, kind of nervous here.
**Jason Plumb** 17:44 It's good. No, you're fine. Yeah.
**Ilia Liferov** 17:47 I agree.
**Jason Plumb** 17:47 Great.
Yeah.
**Ilia Liferov** 17:49 Okay, thank you.
**Jason Plumb** 17:53 Jamie's the only one that speaks proper English anyway.
**Jamie Lynch** 17:58 Well, don't know about that.
Okay, cool.
Feel free to add more issues to the agenda as we discuss, but I think the next item was API stabilization discussions.
So I guess we can… Have a look at where we left off, which was with the… default behavior for the Propagator API.
So after the SIG meeting, I went away and kind of… Wrote up what the current state is, what the spec requirements state for the… API, and, Then I just tried to write out in my head, What?
the reasoning is, for the spec, doing this.
And… Any concerns?
That I had from a mobile perspective.
**Carlos Alberto Cortez** 19:03 I put some comments, by the way, on the Slack channel, probably people didn't see that fully.
But I was mentioning basically two things that we can separate the topic into.
**Jamie Lynch** 19:17 Yeah.
**Carlos Alberto Cortez** 19:17 The first one is, the no-op, the second is the global part.
Yeah, I would say that, On the global part, even though it's not recommended, as Jack mentioned, for a few reasons.
This pack is actually… At least for proprietors, maybe not for the other stuff, because it's, like.
recommended with propagators, like, get global propagator is a must-have operation.
Which is kind of an interesting thing.
And probably I will bring that up tomorrow in the specification call.
Like, do we really need that or not?
because you may, I was making the case of Golang, which… you know, specifies context, you are passing context everywhere, and even with this, they were forced to add a global GET propagator, you know?
**Jamie Lynch** 20:15 Hmm.
**Carlos Alberto Cortez** 20:20 That's on one side. Under op, I was listing all the things that have to be available. Not necessarily in the API, but let's say without an SDK.
Which is, you have to fully implement span context, baggage, baggage propagator, W3C propagator, composite, or composite text map propagators.
And I was mentioning that the way JavaScript kind of does this is that they have an API package, which does nothing, then they have a core package, which depends on the API and the API, which defines a lot of these components that I was talking about. And then they have two more packages below, which are the packages, one for the browser, one for Node.
So that's kind of interesting, that's a good alternative, yeah.
**Jamie Lynch** 21:12 Yeah, that'd be an interesting… Way of doing it, so it's something that depends on the… API.
Package, but… It's kind of separated from the rest of the implementation, right?
**Carlos Alberto Cortez** 21:26 Yeah, there's also one section in the specification, which is called, Client Guidelines… Library Guidelines, sorry. And it has a specific line saying the API dependency contains a minimal implementation of the API… of the API. When other implementation is explicitly included in the application, no telemetry will be collected, etc. And the thing is that, this is what it's saying. Basically, you need… you have… you must include the no-op in the API… the API, sorry, lack of caffeine. So it's, yeah.
The thing is that… It's… it's an interesting thing, because it's not using… actually, you know, a MOST clause there, but I think that was kind of the intention, yeah. Yeah, it's open to interpretation, but I would say, either way.
you need to put some of the basic components, even without the main SDK, somewhere.
And the most natural place feels like the API. Of course, unless you want to have one more package besides which could be doing, you know, op plus, as I said before.
Implementing span context, baggage, baggage propagator, etc.
Yeah, so that's kind of the stuff.
And the kind of final… my final conclusion on that front is that even if we don't have to support global instances, like Global OpenTelemetry, If, in the future.
This has to be Aviv.
I mean, I hope we don't have to, ever, but if we have to.
for whatever reason, then at that moment, the API needs to include the NOP implementation.
So that's something to… Keep in mind.
**Jamie Lynch** 23:20 Okay.
Just to clarify again, because a week has passed and I've forgotten some of the context, The reason for needing, like, a baggage propagator and trace context propagator is… for the instrumentation to basically pass on the information when the SDK is disabled, is that correct?
**Carlos Alberto Cortez** 23:48 Yeah, correct. It's… and it's not like the SDK is disabled, it's more like… For example, you are, like, doing some local instrumentation, like, custom instrumentation.
And you are not the operator?
Necessarily, so you are just writing instrumentation, and you are doing propagate… propagation by default.
And the SDK may or may not be even stalled, like, the operator will decide that.
But you are still doing propagation. So in this case, it would be instrumentation, but kind of the custom side.
Also, of course, very often, like, instrumentation, like HTTP will do propagation out of the box, and they have to access this.
**Jamie Lynch** 24:30 Hmm, Okay.
Yeah, I should also mention, I did one small tweak, which I hoped would be non-controversial, is… the spec, I think, says the default propagator should be WVC baggage and trace context. Currently, the implementation of OpenTelemetry Kotlin was Basically setting it to a no-op propagator.
So, I've opened up this PR, which switches it to… use those by default, so I think that's getting us some of the way better.
**Carlos Alberto Cortez** 25:17 Yes and no. I would say that one thing is the fact that these propagators are defined and available.
**Jamie Lynch** 25:26 Hmm.
**Carlos Alberto Cortez** 25:26 And the other thing is, what's the default? And actually, if I remember correctly, I may need to double-check, but… If the user doesn't configure anything.
You get no propagation at all.
Yeah, so that's the default. I don't know if, like… My impression is probably that has to change for Kotlin.
Like, which for default, you have to override that, I don't know.
But usually, like, the user… I mean, at least this is how it has been for other SIGs, that as part of the required, let's say required configuration, the user must specify explicitly what propagators… And… probably the language and the specification is not clear enough, but basically the idea about baggage and trace context is more like they are available at the API, always, by default.
They are available, but they are not enabled. The user must opt-in.
**Jamie Lynch** 26:27 Got it. Okay.
Cool. I think… I'll go away and… Have a bit of a think.
On this, and… maybe try and, like, sketch out some designs, I think, as a next step.
**Carlos Alberto Cortez** 26:49 Yeah, happy to take another call. I know this has been coming back and forth, but yeah, let's… let's do that. I will be, very, like, in the loop. And as I said before, there's a message I put in the Slack, so we can keep discussing that there. Tomorrow, I will bring the global GET propagator thing to the specification to discuss that there. I'm very curious, because that will impact… you know whether we can actually, like, get rid of this or not. Long story short, by the way, I was talking to Jack, who is a Java maintainer.
And he mentioned that They are doing, just confirming what we were talking about last week, I think.
that they have this global OpenTelemetry object, and it's mostly useful if you use auto-instrumentation, which we won't need.
At least for the time being.
So we wouldn't need that, you know?
So we are good on that side. I just have to confirm the… or see what people think about this, get global propagator.
**Jamie Lynch** 27:50 Okay. Yeah. Cool.
**Carlos Alberto Cortez** 27:52 And yeah, I suggest you do some thinking, and everybody in this group, go read that if you're interested.
And, yeah, tomorrow the call is, more or less this time, one hour earlier.
And then after that, we can come to conclusions, and yeah.
**Jamie Lynch** 28:08 Okay, awesome. Yeah, thanks for, thanks for taking that on and, asking about it.
**Carlos Alberto Cortez** 28:14 Yeah, Alex, you cannot go, sorry for that. It was… yeah, it's like… There's a lot of moving pieces here.
**Jamie Lynch** 28:22 Oh yeah, for sure.
**Carlos Alberto Cortez** 28:23 are not obvious, you know? I mean, there's a reason why even Java, even though they… anyway, there are so many technical details, we have learned ever since.
**Jamie Lynch** 28:31 Yeah.
**Carlos Alberto Cortez** 28:32 was written, so now probably it's a good time to ask some questions, yeah.
**Jamie Lynch** 28:37 Yeah, and ultimately, I want to get it right, and Yeah, I'm not super familiar with how it works already in OpenTelemetry, so I'll probably… Got a lot of questions about stuff.
**Carlos Alberto Cortez** 28:51 Yep.
**Jamie Lynch** 28:57 Okay, cool.
I think… That kind of sums up the… Baggage stuff.
Did we have any other items that folks wanted to discuss?
**Viorel Alexandrescu** 29:17 No, but I'm curious about something. Do we have a time frame For which we need to tackle these things.
I mean, to be honest, I did feel bad at some point that I didn't manage to get my head around finishing up on the exporters thing, but… You said about releasing, releasing this week, or in the… or previously we had a release. I mean, is there a calendar for these things, or whenever we get the time to work around this?
**Jamie Lynch** 29:51 So, let me double check what we've written down.
releasing. I'm pretty sure we had something.
Yeah, so the cadence is just approximately once a month. Sometimes we do it More frequently, sometimes less frequently.
I don't think there's any specific… timeline, for… Like, completing, like, a particular milestone or anything like that. Yeah, I think… We're just trying to get…
**Viorel Alexandrescu** 30:39 Get things done.
**Jamie Lynch** 30:40 Yeah, trying to get stuff done. And in terms of priorities right now, I would say… the logging API and tracing API, getting agreement on what those should look like, and stabilizing them, probably the… top priorities.
**Viorel Alexandrescu** 31:02 Okay.
**Jamie Lynch** 31:06 I think we even have this document, actually.
So yeah, this kind of goes over, like, the very… broad, high-level goals, which we've kind of been implicitly assuming everyone knows. So yeah, work is in the issue tracker, and if it's not there, we can create issues.
But basically, any APIs marked with experimental API, we could… change and break, which reduces confidence for people using it. So yeah.
Contacts, blogging, tracing of our top priority ones to… Yeah, I do.
**Viorel Alexandrescu** 31:53 Okay.
**Jamie Lynch** 32:00 Cool. We can get a bit of time back, unless anyone has final thoughts.
**Viorel Alexandrescu** 32:07 No, that was enough for me.
**Jamie Lynch** 32:10 Awesome.
Thanks, everyone.
**Ilia Liferov** 32:11 Thank you.
Bye.
**Carlos Alberto Cortez** 32:14 Nope.
