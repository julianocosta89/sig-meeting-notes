SIG: Kotlin SIG
Date: 2026-09-21
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 01:15 Hello.
**Hanson Ho** 01:29 Hello.
Bolks hear me?
**Jason Plumb** 01:57 Yes. Yeah.
**Hanson Ho** 02:00 unusually quiet.
**Jason Plumb** 02:06 Monday morning.
**Hanson Ho** 02:09 You have to switch laptops between different meetings.
still figuring out post-acquisition IT.
Stuff.
**Jason Plumb** 02:19 fun. Yeah.
**Jamie Lynch** 02:23 Some are fervor longer than others.
**Hanson Ho** 02:25 Some have two laptops, and some don't have two laptops.
**Jamie Lynch** 02:40 Cool, I'll just give it another minute for folks to add items to the agenda, and… Then we can just make a stop.
**Jason Plumb** 02:55 Well, in case it's not glaringly obvious, my attention is still elsewhere.
**Hanson Ho** 03:02 Not glaringly.
**Jason Plumb** 03:06 Well, doing what we can.
**Jamie Lynch** 03:18 Cool. I will just make a start, but if anyone does have Like, any items that we want to discuss, please just add them to the agenda as we go.
Cool, I thought we'd start with yours, Ilia. So, you're working on telemetry, exporter, back pressure.
**Ilia Liferov** 03:38 Yeah, that's right, and just to give an update that I'm in progress, and… I will lend an update soon, in my draft PR, with the designed approach, so, just to let you know that it's not, like, I'm not stuck, just working on this.
It's in progress.
**Jamie Lynch** 04:00 Awesome. Yeah, just for context for everyone else, I think currently the telemetry export basically just Fires off, what initiates a coroutine for everything, or for every single item that's in the batch of telemetry. So we probably want some sort of… Backpressure to avoid.
Yeah, bad things.
But yeah, I think… Just, ping one of us if… Do you have any questions about that one?
**Jason Plumb** 04:44 Well, does the spec say anything about this? Do we know?
**Jamie Lynch** 04:50 That's a good question. Have a look.
**Jason Plumb** 04:54 I don't remember anything specifically about back pressure in the batch span processor.
**Carlos Alberto Cortez** 05:00 Yeah, it's really general, the front.
**Jason Plumb** 05:02 Yeah.
**Hanson Ho** 05:04 Feels very implementation-y specific.
**Jason Plumb** 05:07 Sport is straight.
**Hanson Ho** 05:08 different things.
**Jason Plumb** 05:09 Totally.
**Ilia Liferov** 05:10 Yeah, as far as I understand, the only thing, the specification tells that the collector can He's able to return, retry after header.
Forcing the clients to, like, slow down, so that's… Something, we want to respect, and the… point is that, we need to treat this retry after for the entire endpoint, not for a particular batch, as far as I understand.
So… That's basically the cornerstone… cornerstone of my, of my approach, and, like, we need to… Cover this, properly.
Yup.
That's.
**Jason Plumb** 05:58 Sounds good. Yep.
**Jamie Lynch** 06:00 Makes sense.
Cool. Yeah, I think the next thing I wanted to discuss, if… no one had anything else, was, this PR. So… I think this is the first… Well, it was the first major PR, I guess, but it's not, like.
a small refactor, and it's intending to separate out the propagation and context interfaces to a different module from the API module.
So there's a bit more detail on the discussion, but effectively what I've done is I've just taken all the existing interfaces, like.
context, and, like, for factories to, like, create expand context, baggage, etc, and I've put them in a different module.
I've… added a… propagator's interface that kind of allows you to access them. So, functionally, it would be the same As having… the old way of doing things, where you access everything from telemetry.
So it was kind of an example here, where you can create a propagator, then obtain A text map replicator from that.
And… that allows you to… access, propagation APIs without having an SDK instance.
And then… There's also the ability to, kind of.
pass that in when you're creating an SDK instance.
So… I had a couple of items that I'd like to discuss around this, but before I'd open the floor up for any thoughts on this, or the change set, first.
**Hanson Ho** 08:03 So how does Java and other places get around having this, like, zeroth layer, basically, like, beneath the API layer?
**Jason Plumb** 08:13 You mean specifically for propagators?
**Hanson Ho** 08:15 Yeah, because propagators are, like… We can exist any way, so… but that needs.
**Jason Plumb** 08:22 Yeah.
**Hanson Ho** 08:23 things.
**Jason Plumb** 08:25 Java has it baked into the API.
The propagators are part of the API in Java.
**Hanson Ho** 08:34 And for us, that's not possible, because… Just better… or not possible, but we prefer this because of just better organization.
**Jason Plumb** 08:45 I think so.
**Hanson Ho** 08:48 Cool.
**Jamie Lynch** 08:49 Yeah.
That'd be… My preference, at least.
**Hanson Ho** 08:58 Sounds good, though, like… We can rip things off, I like that.
**Jamie Lynch** 09:04 Okay, then if we've got time, I'd quite like to go through these, discussion items, because I think starting with the easy one first, like, is propagators and create propagators a good name? I couldn't really think of a… better one, but I feel like there might be a better one.
**Jason Plumb** 09:29 Can you show the usage again?
**Jamie Lynch** 09:31 Yeah, sure.
**Jason Plumb** 09:32 Yeah, just right there, okay.
Seems pretty good.
I got no beef with that, I think. I think that's… I think that's great.
**Jamie Lynch** 09:51 Okay, well, I guess when folks are able to review this, we can… Yeah, I guess, if anyone thinks of a better name.
It's always good to know.
And then… The next point is… Currently, I've implemented this so that the existing OpenTelemetry interface basically extends propagators.
So… That allows us to… Basically, maintain backwards compatibility with what existed before.
But I'd be open to, like, a different… Like, making a baking change there, if we can think of a better syntax.
So I'll see if I can find V.
Actual interface to it.
Show what that looks like.
So, yeah, basically there's this propagator's interface, but now has, like, all the factories that basically allow you to create objects like a trace flags or trace state.
and… Yeah, they've just been moved over, essentially, and the OpenTelemetry interface now extends, propagators.
**Jason Plumb** 11:29 Because these are interfaces, I think that that's probably okay.
**Hanson Ho** 11:37 And if we're gonna make the move, this… this makes sense. Otherwise… I mean, yeah, this is the relationship, so… I'm okay with that.
**Jamie Lynch** 11:48 Okay.
**Jason Plumb** 11:49 You could, like, conceptually, you could still keep them separate and have yet a third interface that combines them, like a propagating open telemetry or something, but I don't know that we need that.
**Jamie Lynch** 12:01 Okay.
Boom.
I guess we can… Chot spell. Number 3, which will be the… Interesting one. So… Yeah, basically, my understanding of what we want to do with this is we want To provide a working implementation So that if you're… Like, going to the… Like, baggage factory, for instance, to create baggage, you want to get a working object back.
So… I think that's fine for the, like, implementation mode, so where we're using Kotlin multiplatform behind the scenes. I just wanted us to agree on what that should look like for the compatibility layer.
So, the way I see it, we've got two options, one of which is we try and wrap The existing OpenTelemetry Java propagation layer.
Which… A consequence of that is probably we would need to, like, have separate modules, Like, depending on API propagators. Or alternatively, we could… effectively use our own propagation layer within OpenTelemetry Java.
Which… should work. It's just, It feels less of a compatibility layer at that point.
**Jason Plumb** 13:52 Yeah, I'm not entirely following, so is that suggesting that we would have, like, API propagators Java?
As, like, a new module, or…
**Jamie Lynch** 14:03 Yeah, so basically… Bye.
go back to this. So, we're gonna be, like, this is gonna be ultimately supplied by… a Kotlin multiplatform implementation right now.
**Jason Plumb** 14:20 Yep.
**Jamie Lynch** 14:21 if we want to support the… Yeah, basically, if we want to add this support.
to the compatibility mode, we face a choice between using that Kotlin multiplatform implementation, or decorating, the existing Java implementation.
**Jason Plumb** 14:55 Got it. So it's… it's… the choice is, do we just use the native, pure Kotlin implementation, or do we use Java? Is that the… kind of the choice?
**Jamie Lynch** 15:05 Yeah, basically. Yeah, because… We… currently, we have… the same API that's… that allows you to kind of… you can use the same API against the, like, KMP implementation or the Java implementation. So if we're tying a specific implementation to this API, that means we have to use the KMP implementation of, like, span context within OpenSelemetry Java.
And that's responsible.
**Jason Plumb** 15:38 Within the… sorry, yeah. Within the OpenTelemetry Java compat layer that already exists. Yes. Yes, okay. And… That's not what we're doing today.
**Jamie Lynch** 15:52 No. So currently, we're basically just… Adding loads of decorators around that.
**Jason Plumb** 15:57 Yeah. Isn't it… I mean, it seems to me to be better to be… like, if we have… when… in the cases where we do have… a pure native Kotlin implementation, we should use it, it seems to me.
Rather than… Using the compat… like, long-term, minimizing compat seems like the move.
Seems like the good idea.
When… if and when we have places in our implementation that are native.
If that makes sense.
So if we have a fully baked spam context, Why not use it?
Like, why should we even have a compat layer at all for that?
**Hanson Ho** 16:42 So I think the compat layer was… was the idea that, oh, this is actually super safe, because everything is going to go through the Java layer. So you're just basically talking to a pass-through with… that's shaped differently. So everything is going to go through Java.
And everything has thus far been like that. Except now we've pulled, kind of, this part outside of this, so if we have a, compat version of API propagators.
it's kind of weird, because in Java, everything's tied together, so you kind of have a bit of that already, and in Kotlin, it's not.
so what it's doing is, I think, similar, so there's more of an argument to, like, just use one implementation. But… Are there people who want purely Java?
implementation, even at this layer.
I mean, long-term, I think the idea is no. And in short term, are there any migration cases where they're like, no, no, this part has to be… Job.
**Jason Plumb** 17:53 I can't think of any, but it's still early in the morning, but, like, I… I don't anticipate that.
**Hanson Ho** 18:00 I… I agree. Do you? Yeah, okay. No, I don't, I don't, I don't.
**Jason Plumb** 18:04 Yeah.
**Hanson Ho** 18:04 I think… I think using this part and having it… so I think it… I think… I think… I think having Compat is a risk mitigation layer, and… I think this is a lot less risky than, like, the entire tracing system, or, you know, like, that kind of stuff. So… In theory, to be 100% compat.
yeah, maybe, you know, something going through Java would be great, but… It feels like it just adds a lot more gunk, and if nobody's really asking for it, like, not even ourselves right now, it feels like… It feels like someone should document and say, hey, this is not compat, per se. But… Who would care?
And if someone does, maybe…
**Jason Plumb** 18:54 That's what I'm getting at. In fact, we know for sure the opposite's true. Like, someone who's targeting iOS very much cares, and they don't want the Java one, right? Like…
**Hanson Ho** 19:03 Yeah, exactly. It's, it's… yeah, in fact, it's… it's… Yeah, the compat feels like a… someone who's using Java on Android.
who's afraid and wants a safer path.
**Jason Plumb** 19:19 I say we build that when it's asked for. Like, I think we do the native thing where we can.
**Hanson Ho** 19:24 Agreed. Document it, but… but let's not… let's not… Shoot ourselves in the foot until someone asks us to.
**Jason Plumb** 19:32 I like that.
**Jamie Lynch** 19:34 So… Yeah, I think, given it's an interface, it probably would be possible to Retrofits.
like, a compatibility to the decorator at a later date. The only… use case I can think of where it might possibly… change stuff, as if, like, if you've, like, created a Java SDK, and then you want to decorate the OpenTelemetry Kotlin API, Oh, sorry, so you've created a Java SDK, and then you want to wrap it in a Kotlin API, But I guess it depends on what API we're using. Like, really, it's only stuff that has Shared state, like, context that might be… programmatic.
**Jason Plumb** 20:32 Yeah, I'm not sure, I can't… I'm not thinking fully through it yet.
But it, I mean, it feels… feels like it should be safe.
**Hanson Ho** 20:42 Does it affect default contexts?
**Jamie Lynch** 20:47 I think this is kind of, like, moving on to our next point, which we should… discuss. But yeah, basically, we… Should kind of figure out how default contexts works in this scenario. So, if you've got one API… Which we would do in the API propagators module, but then we've got this compact implementation and a… KMP implementation.
They're both using different mechanisms for storing context.
And because API propagators would be created before either of those modules, Do you… Even need some global states.
Or… you need… to accept some divergence, unless there's a third option I'm not seeing.
So…
**Jason Plumb** 21:52 Yeah, yeah, so I'm… yeah, sorry, let me think out loud for one second. So, if you… if you are a user, and you chose to use the KMP implementation of propagators, but elsewhere, you're also using the Java SDK, via Compat, right?
those are two different implementations. They are at odds with each other, potentially, on how they do storage.
What you can do, though, is you can… customize the storage for the Java SDK. Like, you can provide your own storage.
So a user could… one could build a Java-compatible storage that's backed by the same KMP implementation. So it's like… it's like a reverse facade, if that makes sense. Like, normally we're putting, like.
Kotlin APIs layers on top of Java implementation, this would be, like, the other way around. You'd have to have a Java implementation that is somehow backed by the KMP one.
I don't know how to do that.
**Jamie Lynch** 22:54 Yeah.
I think that use case makes sense to me.
like, it's… if the SDK has not been constructed, and you're an instrumentation author, and you're just looking to… Like, potentially set something on the context.
That's the use case I'm less clear about. But maybe that's not even a valid use case in respect, I don't know.
**Jason Plumb** 23:18 Yeah.
**Hanson Ho** 23:21 Yeah, because in Java, everything's tied together, so… I don't know how you would even create propagators.
Java propagators without an SDK, because that's not possible.
**Jamie Lynch** 23:37 Okay.
**Hanson Ho** 23:39 And, you know, functionally, the biggest difference for… the reason I brought up default is… is, the expectation that thread local, is used. So, as long as Java implementation, or using the compat implementation, the behavior is that way, while under the hood it's being powered by the KMP implementation, as long as that contract is kind of kept in place.
I hope that's okay.
Otherwise, we would need, you know, everything threaded through Java.
**Jason Plumb** 24:24 Yeah.
Yeah, I'm not… I'm not sure.
**Jamie Lynch** 24:37 I guess… It's just context, really, that's… the only thing that's potentially holding state, so… what I could… do is I can go and look at the OpenSelemetry Java SDK and figure out if there is a way to Easily set, like, a different mechanism that we could use.
If we needed to.
**Carlos Alberto Cortez** 25:04 There is a way to, to manage the actual storage.
Not the logic around context, but the storage itself.
Yes. I don't know whether that would be no, but you can look at that.
**Hanson Ho** 25:18 Yeah, feel that?
**Jason Plumb** 25:19 It feels like there should be a way to provide an implementation there that's backed by Kotlin.
**Hanson Ho** 25:24 it'd be a… it'd be an implementation that's backed by Kotlin that implates what Java does, so…
**Jason Plumb** 25:31 It would be.
**Hanson Ho** 25:35 But this stuff is so light, and it's, it's one of those things where… yeah, theoretically, we're going through two extra layers, but it's… it's doing effectively the same thing. So, if we require a… Java implementation of a Kotlin interface of a Java implementation.
So be it, or… or… Or not even that, it's a Kotlin implementation that emulates the Java implementation, so it is… Anyway, you know what I'm talking about.
**Jamie Lynch** 26:06 No.
**Jason Plumb** 26:08 This is a pain point, though, right? Because when those two things don't match, all hell is gonna break loose. Like, if so… yeah. And it would… It would be an easy thing for a user to overlook, I think, as well.
Right.
**Hanson Ho** 26:22 I… I think you'll feel loudly.
at least, that's… that's what I'm thinking. If something doesn't work. Like, I don't think this.
**Jason Plumb** 26:30 I think you would just have different contexts bouncing around in different cases.
**Hanson Ho** 26:34 Oh, yeah.
**Jason Plumb** 26:35 Just, like, completely… I don't know, like, misaligned spans or something. I don't know, like, you'd have different… spans.
**Hanson Ho** 26:45 they won't work, because I don't think you can have a Java context play nice with a Kotlin context. So if you initiate… instantiate, like, the entire thing, it's only one type of context. So, whatever weird implementation we have here with the hybrid, it's gonna be, like, all shaped like that. So, things connected to it will all be weird.
I don't know if… I don't think we support… contacts created in one implementation to be then used by another.
**Jason Plumb** 27:20 Does seem problematic.
**Hanson Ho** 27:22 I think it… there's a conversion to where they kind of normalize.
**Jason Plumb** 27:32 Yeah, I just don't know.
**Jamie Lynch** 27:37 Yeah.
I guess.
Yeah, I think… rather than spending ages talking about this, I can just go look at what the actual APIs are, maybe, like, try and draft, some VR up that would show How do we deal with this use case, and then we can discuss it further next week.
**Jason Plumb** 27:59 I think that would be helpful.
**Jamie Lynch** 28:07 Hey. And Ben, there's one extra point, just… yeah, talking about naming again, so I don't think we necessarily need… to discuss that now.
But, yeah, if folks get the time to review this, That would be really appreciated. And we can probably, like, pick it up next week.
**Carlos Alberto Cortez** 28:34 Yeah, actually, I would like to do a full review of this, yeah. So, I will try to do that by Wednesday, so there's no, like… There's enough time for other people to provide their feedback.
**Jason Plumb** 28:48 Thank you, Carlos.
**Jamie Lynch** 28:50 Thank you.
Okay, cool. So… I had one other topic, if folks have other items, please add them to the agenda. But yeah, I just… noticed that this issue got a few comments. So basically the… we have a batch telemetry processor that basically isn't working in a Fed-safe way.
I… Yeah, just so… We had to…
**Jason Plumb** 29:26 -
**Jamie Lynch** 29:26 Some folks actually hanging on this in production.
**Jason Plumb** 29:30 That's cool.
**Jamie Lynch** 29:39 So…
**Jason Plumb** 29:40 Yeah, we should probably fix that.
**Jamie Lynch** 29:42 Yeah, we should probably… Take a look at that.
**Jason Plumb** 29:51 I'm gonna see what Java does.
**Hanson Ho** 29:59 Hmm.
**Jamie Lynch** 30:07 We'll see if I can, Find the natural code as well, so we can see what it's doing.
Yeah, so we've got a queue, which is an array deck.
What do you have?
Mutex… Schooling… mute text with lock.
**Jason Plumb** 30:40 Workers queue the workers.
**Jamie Lynch** 30:46 Yeah, so I think that's where it's probably… I wink.
So I assume this isn't actually… Like, I took… Like, it's not like a traditional Java mutex, I think that's a coroutines API.
**Jason Plumb** 31:04 Oh.
**Hanson Ho** 31:07 So with lock is not actually locking.
**Jason Plumb** 31:11 Yeah.
**Jamie Lynch** 31:11 Not in the way I think we'd traditionally assume it to be.
I think.
Yeah, I'm not super familiar with Coreoutine's API.
But, yes, it feels like… I could probably take a look at.
Exactly what that API is doing, and figure out whether we need, like.
To synchronize on some other lock, or whether there's a better solution with coroutines.
**Jason Plumb** 32:00 Yeah, I'm just scratching around Java for a little bit, It's not immediately obvious that it's thread-safe.
But I'd be very surprised if it wasn't, somehow.
**Hanson Ho** 32:19 It's the processor… Yeah, let's take a look at some…
**Jason Plumb** 32:41 Yeah, the batch span processor is weird, because it, it has this worker class that's, like, kind of a background, it's like a job.
And the implementation is kind of split between the parent class and the inner class, which is the worker, and… I mean, I think it makes it hard to read, but… The worker has a queue.
It is not strongly typed, it's just a queue, and that queue gets injected, and who creates the worker?
The batch spam processor creates the worker, and… It… passes something from JC Tools. So JC Tools is the implementation of Q.
And I forget what JC Tools does, but I think it's, like, a super efficient, minimal implementation, if I remember.
Yeah, JCTools is a Java concurrency library, so JC means Java concurrency.
So, it looks like it's probably covered in Java.
Through that library.
Yeah, we should fix that.
**Jamie Lynch** 34:05 I'm happy to try and have a look at that sometime this week.
**Hanson Ho** 34:13 Sounds good.
**Jamie Lynch** 34:17 Cool. Anything else that folks want to discuss?
**Jason Plumb** 34:27 Don't think so. The build went smoothly, it sounds like. The release…
**Jamie Lynch** 34:31 Yep, I think everything passed first time, so hopefully… Next one.
**Jason Plumb** 34:38 Knock on wood.
Cool.
**Jamie Lynch** 34:43 Awesome. Everyone gets a bit of time back then.
Thanks, everyone.
**Jason Plumb** 34:48 Cool, thanks, Jamie.
Thanks, everyone.
**Carlos Alberto Cortez** 34:51 See you.
**Jason Plumb** 34:52 Bye.
