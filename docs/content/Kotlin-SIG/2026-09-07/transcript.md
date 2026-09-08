SIG: Kotlin SIG
Date: 2026-09-07
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Ilia Liferov** 00:38 Hi, Dreamy.
**Jamie Lynch** 00:42 How you doing?
**Ilia Liferov** 00:44 I'm fine.
What about you?
**Jamie Lynch** 00:48 Yeah, pretty good.
I got a feeling this might be a quiet one, because it's a US holiday.
**Ilia Liferov** 00:55 Yeah.
Could probably be wrong here.
**Jamie Lynch** 01:02 Whereabouts are you based, by the way?
**Ilia Liferov** 01:05 Sorry, about what?
**Jamie Lynch** 01:06 Where are you based? Like, what city are you in?
**Ilia Liferov** 01:12 Sorry, I can't understand you.
**Jamie Lynch** 01:15 Where do you live?
**Ilia Liferov** 01:17 Yeah, I live in Prague.
**Jamie Lynch** 01:19 Czech Republic.
**Ilia Liferov** 01:20 Yeah, yeah, yeah.
**Jamie Lynch** 01:21 Yeah, I'm in Manchester.
**Ilia Liferov** 01:24 Okay, yeah, that's great.
And you've been born, yeah, in Manchester, or…
**Jamie Lynch** 01:30 Not born in Manchester, but yeah, I've been here for a while now, for a few years.
**Ilia Liferov** 01:36 Yeah.
**Jamie Lynch** 01:37 Yeah, I really like Park. Yeah, it was a nice.
**Ilia Liferov** 01:40 I've been to Prague, yeah.
**Jamie Lynch** 01:42 Just… just for a few days, yeah.
**Ilia Liferov** 01:43 Okay, okay, yeah, Prague is nice. I'm from Russia originally. I'm… I've moved to Prague… 12 years ago, to study computer science.
And I'm working here with Mike.
With my guys, we have started the, like, company here.
I've mentioned in my, in my welcome message.
Yeah, and, like, the city is really, really good. It's convenient, and not, So pricey in terms of, like, living… living costs.
So, yeah, that's… that's fine.
**Jamie Lynch** 02:25 Oh, awesome.
Well, it's a pretty light agenda so far, so… I'll just paste the link into the meeting, we can see if anyone turns up.
**Ilia Liferov** 02:42 Yeah.
**Jamie Lynch** 02:43 I got one PR I had.
**Ilia Liferov** 02:46 Yeah, I've joined to mention my progress. I can also paste, oh, my PR here… I have opened a draft PR for… the latest issue… You have assigned to me.
It's about back pressure.
And concurrency control.
And I just… wanted to let you know that I have an idea drafted in the pull request, and I've also left a comment.
There in the issue, just to let you know, yeah, and, like, any feedback, appreciated, like, basically.
Oh… I have, limited the number of concurrent, coroutines, kicked off, and also, made the, expert, Function to suspend to make some kind of back pressure on the flashing coroutine, Or… to make it, so… Waiting for, people are for concurrent, or… Coroutines.
If all of them are busy. So that's, like, the, simple, simple idea.
And I'm not sure if it's… if this is the right direction, or… Speaking of the architecture, like, between the processor and the exporter.
So that's basically my question here.
**Jamie Lynch** 04:41 Got it. Okay. So… I think… Memory, the problem was we were basically not waiting when creating.
routines, and it was just creating all of them at once, and then… kind of retrying. So, So, you basically added a limit, so that says you can only have, like, a maximum of 5 semaphores, 5 coroutines at a time.
Okay.
And…
**Ilia Liferov** 05:19 Yeah, that's right, like, when the, I don't know, like, the collector is down, and all of the, in this case, like, 5 is just a number, in the draft, we can, we can discuss it.
**Jamie Lynch** 05:32 I think.
**Ilia Liferov** 05:32 if we stick to this solution, we need to make it configurable, I guess, in the configuration. So, when the… all of the coroutines are busy, processor, like, just waiting for, any… On them, to finish and, like, suspend it, in its, like, flashing, flashing, flashing loop.
**Jamie Lynch** 05:59 Yeah, this feels like a… the right sort of approach to me.
Do you know what would happen while it's waiting? So, the process would just be suspending, That cause, like, back pressure at all?
**Ilia Liferov** 06:19 Like, my, thinking here is that, like, we can, we don't want to drop, when, when the, when the bull is full, I mean, like, pull off, Exporting coroutines. We don't want to drop, the patches.
Although, like, the specification tells that we… when we are under pressure, we can drop telemetry, as far as I understand. But, like, on the other side, we have a queue in the processor.
So, it would be great to, like, leave this queue, filling… filling up, when the exporters are… all of the exporters are busy, and just, like, Make some time for the exporter coroutines to, like, free up and, catch, on the next, yeah.
On the next, exporting attempts from the, flashing coroutine.
Oh.
**Jamie Lynch** 07:22 Okay.
**Ilia Liferov** 07:23 That's, that's the idea.
**Jamie Lynch** 07:26 Yeah, I think I probably need to have a bit more of a read do this, like, offline, but yeah, it seems like a pretty sensible idea to me, and…
**Ilia Liferov** 07:37 Keith?
**Jamie Lynch** 07:37 So, taking a look at this, I will… At myself, as a reviewer.
**Ilia Liferov** 07:43 Yeah, thank you.
**Jamie Lynch** 07:44 Try and look up that tomorrow.
**Ilia Liferov** 07:47 Would be great.
**Jamie Lynch** 07:52 Did you have anything else you wanted to discuss around that?
**Ilia Liferov** 07:56 Not from my side, that's the only issue I'm working on. So, if you have any other, like, ideas, I'm happy to implement it the other way, so, like, just let me know, and… Yeah, so…
**Jamie Lynch** 08:10 Yeah, I appreciate that.
**Ilia Liferov** 08:12 Thank you.
**Jamie Lynch** 08:13 Yeah, Ben, I was just gonna back this up, mainly so that Carlos could have a look, if he's gonna look at my notes. But yeah, I think what we've been discussing the previous view SIGS is basically the need to have the propagator API when… when the SDK is disabled, I think the OpenTelemetry specification says there should be, like, a working propagator implementation. So this just kind of starts moving out some of the internals, towards doing that. So, like, it moves, things like fur.
Baggage, model classes.
But yeah, nothing really too much to say beyond… I'm gonna keep, kind of, moving on with that.
Cool.
**Ilia Liferov** 09:11 Fair.
**Jamie Lynch** 09:12 Anything else from anyone else?
**Ilia Liferov** 09:16 Not from my slides.
**Jamie Lynch** 09:18 Then I think we're probably gonna wrap up. Pretty quickly today.
**Carlos Alberto Cortez** 09:24 Oh, hello, hello.
**Ilia Liferov** 09:25 Hi, Cole.
**Carlos Alberto Cortez** 09:27 Hello, yeah, I don't know if you guys covered that, didn't see the agenda, but basically, Oh, okay, that's your first PR, propagator Module PR, I think that's the one.
But some, update from the specification side is that… We are going to make the global propagators optional.
Things that we can definitely, at this moment, escape.
All the global instances, till we deem them.
Really needed, so in the meantime, that's looking good!
I have a PR for that specification, that will simplify things. We briefly discussed a little bit more again the… now that global instances are not needed, at least for now.
the separation between the no-op and the API layer.
And all the consequences, and… So, in general, people think that even though there's a specific section.
in the specification that mentions that the API contains a minimal implementation that does nothing.
It's very flexible to allow languages To do what they think is the best for them.
Up to us if you… like, so that's a good thing to know. At the same time.
They think that the general, at least for the rest of the languages.
the pros of having the no-op and the API together simplifies things, especially when it comes to the coupling, managing different versions, and all that.
And basically, yeah, people say that only if there are, like, actual, practical, very specific reasons, they could… of course, suggests we keep the API within all players.
**Jamie Lynch** 11:20 God.
**Carlos Alberto Cortez** 11:21 That's it. But anyway, so we can discuss the details, other day, offline or something, but basically we are allowed to do that, if we think that's the case, you know.
**Jamie Lynch** 11:31 Okay, awesome. Yeah, that was really good to hear all those details. Yeah, I think, the bit that you probably missed is I've just started, kind of, trying to break out the propagator and context implementation into a separate module so that it would be possible to Basically, use it from a no-op, version if we wanted to.
So, yeah, it was basically just breaking up that proof-of-concept PR we put up a couple of weeks ago.
**Carlos Alberto Cortez** 12:02 Yeah, the interesting thing is that I don't know what's… how do you see that, because, like, are you planning to put baggage… Dirt, as well.
because remember that Bagas, the propagators and spam context have to be implemented. They have to be, like, you need to expose them without an SDK, so would be the plan to put all the other parts there? Or do you… or you are still exploring that part?
**Jamie Lynch** 12:34 I think still exploring. I was gonna start off with, like, one of the… propagators, either baggage or trace context, because I think At least one of those doesn't need too many, like, parameters.
From what I remember. So, I was just gonna start off with that, and then see what… Curries over.
**Carlos Alberto Cortez** 12:56 Okay. Okay, yeah, thank you so much for that. Okay, I will keep an eye on the, on the experimentation, see how that goes. I will try to provide my feedback.
Yeah, good.
**Jamie Lynch** 13:05 Awesome. Thank you.
**Carlos Alberto Cortez** 13:07 That's all from the side.
**Jamie Lynch** 13:09 Any other updates?
I think it's quite a week as a US holiday, so everyone gets a bit of time back.
Cool. Thanks for coming, everyone.
**Ilia Liferov** 13:23 Anchor. Have a nice day. Bye.
**Carlos Alberto Cortez** 13:26 Toe.
