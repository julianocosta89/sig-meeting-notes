SIG: GO SIG
Date: 2026-09-10
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn (Splunk)** 02:52 Hey, Mark.
**Marc Schäfer (T&A SYSTEME)** 02:54 Hi, Toddler.
**Tyler Yahn (Splunk)** 02:56 How's it going?
**Marc Schäfer (T&A SYSTEME)** 02:57 Good. How's it going on your side?
**Tyler Yahn (Splunk)** 03:00 Good. Yeah. Just, jumping in.
Getting busy. Yeah.
**David Ashpole (Google LLC)** 03:20 It…
**Tyler Yahn (Splunk)** 03:22 Hey, how's it going?
**Marc Schäfer (T&A SYSTEME)** 03:23 Hi.
**David Ashpole (Google LLC)** 03:24 Alright. Sorry, I don't know if you've sent anything out in the past week, but I've been just… Busy with internal stuff, so…
**Tyler Yahn (Splunk)** 03:34 Yeah, fair enough.
Yeah, I have actually a PR we can kind of jump into, in just a second.
But, yeah, other than that, I don't think there's too much more I had in the SIG, at least, the past week, yeah.
**David Ashpole (Google LLC)** 03:55 No, I'm It's a bunch of stuff for me.
**Tyler Yahn (Splunk)** 03:58 Yeah.
Fair enough. Cool. Well, yeah, I see, Prince on, Bryan's on as well. We could probably jump in here and get started. If you haven't yet, go ahead and add your name to the attendees list. If you have agenda items you want to talk about, go ahead and add them there as well, and then we can, Yeah, I'll get started here.
Cool. Alright, yeah, so I just wanted to just… bring this to your attention, mostly for folks that were on the call last time. We were talking about adding experimental features. We merged both interface types at the, API level, for both bind instruments and for this Finish Aware stuff. This is the backend implementation for the Finish Aware, like, sum.
It's a small-ish slice, obviously it's not small, it's like 1,400 lines, so, like, it's not particularly easy to review. It's kind of complicated, so I did want to jump in here.
But, like, I did think that, like, it was worth including in this particular form, just because it kind of shows a full slice. It doesn't actually enable it, which is something I originally wanted to do, but also, like, I didn't want to… again, like, that's just… It's just more. So one of the things, like, if we wanted to jump in here, is, like, this new package for this finish, essentially lifecycle management.
It takes in a particular, stance on, like, the lifecycle of Some sort of instrument measurement, and it hooks that back into, like, the actual aggregation.
It's pretty… this is meant to be universal, so, like, it's hooked into the sum right now, but obviously, like, it's meant to hook into all the other aggregations that we support, so it is… pretty straightforward. There's, like, a life cycle that's gonna be associated with whatever the aggregation is. In the lifecycle measurement, like, process, like, there is a, an acquire measurement, essentially a semaphore, where you're gonna look for some sort of.
lock, it is a, lock-free allocation, to an atomic, for the measurement side, the, the, collection and the finishing, not so much. Those are… those are synchronized. But there's two different kinds of measurements, maybe kind of just start there. Like, one's acquiring a measurement, semaphore, and then the other is acquiring what I call here a shared measurement semaphore, and this is for overflows.
Meaning that when a measurement's gonna overflow, it's gonna become a shared measurement, so, like, it essentially is changing the lifecycle state to this, like, you know, kind of special flag of shared, but lifecycle shared is what it's called here.
Meaning that, like, it just can't, it can't be finished at that point, because, obviously, like, you don't know how to split up the overflow. So this is kind of a special case.
It's there to, again, not to try to, do any sort of lock management, so it is, it's lock-free, in this sense. But yeah, you know, there's implementation here. The other side is that there's a finish.
that means that, like, if you have some sort of life cycle, you could say, like, okay, I'm done with it, and then there's the actual collections, there's a cumulative and a delta collection. These obviously have, like, a little bit different mechanisms based on the fact that, like.
like, Delta's getting rid of something is not really a big problem, because the next collection cycle already would have gotten rid of it, it's just more, like, changing the timestamp. The cumulative stuff, though, is the thing that, like, we're more concerned about, so… Yeah, like, it separates this out. There's obviously, like, implementation for the actual, like, mechanics inside, the sum for the measurement side, but this is essentially the lifecycle high-level overview.
Yeah, so, the retire state, I guess that's another thing I kind of… Yeah, it essentially says that, like, after it's been collected, like, it's been… like, the… if something tries to look this up again, it has to say, like, no, like, this lifecycle's actually done. It's complete. It's not the same thing as, I guess, you could say, because it's, like… I chose the word retire to be a little bit different than essentially, like, a pending finish. There's a lot of… there's a lot of words here.
But essentially, like, something can finish, but then if it's remeasured within that same collection cycle, it'll become active again. So, like, finish is not truly, like, an end. Retire is an end. Like, retire is, like, no, like, it was finished, it was collected, the final point's been sent out.
If you want to start a new, like, make a new measurement, like, you need to literally start a new, you know, measurement for this thing, and then that would be a new start to that collection cycle. Or not collection cycle, the lifetime of the instrument is what, you know, that would be.
So, yeah, retire signifies that, like, it's done-done, is the idea.
**David Ashpole (Google LLC)** 08:49 Interesting, so how would… Would calling finish retire something, or when would retire be used, as opposed to…
**Tyler Yahn (Splunk)** 08:56 Yeah, so Retire is, is done when here, when, things are actually, like, getting collected. If… if the thing is actually, like, a finish, pending, like, then it will go through some sort of finish state.
And then, yeah, it essentially says, like, hey, this is actually done, and when the collection semaphore itself is also cleared, that becomes a retired state at that point.
I guess is the way to say that.
**David Ashpole (Google LLC)** 09:25 I guess, like… What's the difference between a time series that has never existed.
in the SDK, like an attribute set, and an attribute set that's been retired.
**Tyler Yahn (Splunk)** 09:37 Oh, nothing.
**David Ashpole (Google LLC)** 09:39 Hiring just the… Way that you get to that, like, back to the zero state.
**Tyler Yahn (Splunk)** 09:44 Yeah, it's more of, like, since this is, like, managing lifecycle state, like, there is a synchronization problem, right? Like, so say, like, you're here, and you do a measurement, but there's, like, some sort of, like, concurrent access, and concurrently, like, the measurement that you're making has actually been retired.
Like, if it's synchronous, like, it's not really that hard to figure that out, like, because you're the one who's also, like, doing the collection, you're the one who's retiring the measurement, like, you're gonna literally drop that from your map.
But if you're doing this concurrently, like, it may be the case that you actually have a concurrent access to, like.
a similar map, and, like, what your state is is stale. And so what you're gonna try to do is try to do a measurement on a retired state, and, like, what this should do is it should kick you back out and say, like, oh, actually, no, like.
this isn't… this isn't, like, something you should even retry. This is something where you should literally create a new, like, value with a new lifecycle, and so it's more of a synchronization mechanism.
**David Ashpole (Google LLC)** 10:38 Okay, okay, interesting. Yeah. So, like… Right, because sums for cumulative integer sums we do have… there is a hot and a… like, this isn't integrated into the aggregators, right? Or… or is it?
**Tyler Yahn (Splunk)** 10:56 It's… it is, in the sense that, like, these are… yes, like, there is a specific aggregator that's added here as the finishSum value and the finishSum aggregator as well. So yes, like.
It is there, correct.
**David Ashpole (Google LLC)** 11:12 Okay.
**Tyler Yahn (Splunk)** 11:14 It is using the limited sync map, with, like, its hot, hot, cold stuff, but, like.
Still, even then, like, there is, like, a possibility where there's, like, it's not common, I guess is the way to say that. It's not common to see this contention happen, but it is possible, is the idea, and so, like, that's the reason it catches it.
**David Ashpole (Google LLC)** 11:44 And in my mind, I had thought that we would… Do the retiring on the cold?
Stuff.
Again, at collection time, right?
It wouldn't be contention on whatever data structure we're iterating over during collection.
**Tyler Yahn (Splunk)** 12:06 I… I don't think you can say that, though.
Because even, like, you can do the swap, like, that…
**David Ashpole (Google LLC)** 12:13 Farm.
**Tyler Yahn (Splunk)** 12:14 Fine.
But there's nothing saying that, like, there isn't a pending GO routine waiting on trying to make a measurement on that particular state.
**David Ashpole (Google LLC)** 12:23 Okay, I'll have to re-remember, but I think this looks good, and I like that you popped it into a new internal directory so that it's Or at least it's, like, in mostly separate files and stuff, so it's easy for us to keep it separate from…
**Tyler Yahn (Splunk)** 12:41 Yeah.
**David Ashpole (Google LLC)** 12:42 The other things, which is nice.
**Tyler Yahn (Splunk)** 12:43 And I tried to not bleed a lot of the internal, like, semaphore mapping stuff outside of this.
So what's some API design?
Cycles there, but like… Yeah, so, yeah, yeah, absolutely.
The last thing I'd probably mention, though, is that, like, this does add overhead, which I think is fine for, At this stage, maybe… Maybe we want to take another look at it before it goes, like, stable, or we actually do this, but, like, the idea is that, like, how to read this is, False means that it's not implemented, with this finish, functionality. True means that it is implemented with this finish functionality. So, as you can see here, like, in serial, like, there's no contention, it still adds, like, 50% overhead, and in parallel.
It's a scalable amount, so it's still also probably about 50% overhead, in this implementation. It's mostly just about, like, the fact that you still need to… add additional things to Atomics, like, there's… there's an overhead on top of that, for doing this, so… Yeah, that's… that's kind of just a heads up on that one. I… I don't think it's a blocker for this experimental feature. It may be a blocker, or we may want to try to look at, like… If this is… Like, once we start implementing it where this becomes, like, the default, that may become something we want to take a look at, or consider.
stronger, this fact, but for now, I figure, like, it's just more about recognizing it.
**David Ashpole (Google LLC)** 14:10 Interesting. I'm curious… I am curious about that, but I'll probably just dig into it myself, rather than…
**Tyler Yahn (Splunk)** 14:17 Yeah.
**David Ashpole (Google LLC)** 14:18 It's surprising, actually, to me that it's that large. I would think it would be, at most, an atomic Boolean lookup.
**Tyler Yahn (Splunk)** 14:27 No…
**David Ashpole (Google LLC)** 14:28 So… No.
**Tyler Yahn (Splunk)** 14:29 unfortunately, It's… it's… well, it kind of is an atomic… I don't… well, I don't know if the operation really matters too much, but, like, it's more… it's an atomic, increment.
is the issue. Because what you're doing is, like, to handle the writers, it actually keeps track of all of the active measurements that are going on, so every measurement is going to increment a counter.
atomically, and then it needs to also release that, that counter once it's done with the measurement. That's why, like, there's actually a strict requirement on the EPI for the finish, where, like, any sort of measurement that you hand off, like, you have to call, like, measurement done on it, otherwise it's going to never… you're gonna get contention, because it's waiting… On, like, a collect, it'll wait for all of the, the measurements to go to zero before it will actually do the collection, is the idea.
So, it's a little bit more, it does, it does require that, and then there is, additional state checking, so it is, like, also a load to, so it's that increment, but it's also a load for, like, what state are you currently in? So it's kind of that bool lookup in that sense, that it's, like, a UN32. But, like, yeah, Yeah, I did have it all as, like… a single, atomic operation, as well, where, like, the first two bits were state and, like, the last 6, 2 bits? Were all, like, yeah.
And then I, like, got into, like, I found, like, there's actually some, like, concurrency issues that came from that, and then, like, I was just, like, I don't… it didn't… I switched to this, and, like, I noticed the benchmark actually didn't change that much, so I was like, I don't think the complication was actually worth it, so, Yeah. So, like, I think it, like, it's worth understanding, but yeah.
I do wonder, though, like, if, like, there is, You know, like, because, like, this is also coming from, Tom Corporation, so I don't know if there's more integration that can happen if we did want to go stable to try to drop this number. Yeah, but I… I haven't really explored that, to be honest. I just kind of was like, yeah, it seems reasonable. Like, it seems, like, bad percentage-wise.
And it is, it's on, like, the hot path, but it's also, like, you're starting to deal with, like, you know, 20 nanoseconds, which is really hard to get rid of, at this point. So, yeah.
**David Ashpole (Google LLC)** 16:50 just… and just to be clear, is this performance only if you are using a finishable sum? Like, you've turned the feature gate on, or whatever, however we decide to enable it. This is not like if you use the standard aggregate sum.
Today, something that ends up being regressed.
**Tyler Yahn (Splunk)** 17:11 I think so. I think that… I think that's what… I would say yes, but I just want to double check. So, like, I'm literally calling, like, the… this is, like, the false is using, like, the existing default.
And then this is using the different aggregator that I just introduced.
**David Ashpole (Google LLC)** 17:30 Yep.
And so, does the false version change at all?
from…
**Tyler Yahn (Splunk)** 17:35 No, no, that's also the numbers that we see on… yeah. I mean, at least on my machine.
**David Ashpole (Google LLC)** 17:40 Yeah, yeah.
**Tyler Yahn (Splunk)** 17:42 Okay, good.
**David Ashpole (Google LLC)** 17:42 That's… I think that's way more acceptable than… yeah, yeah, I thought… Yeah, okay. No, that's… that's cool. We're good then.
**Tyler Yahn (Splunk)** 17:51 Yeah.
**David Ashpole (Google LLC)** 17:51 I thought initially you were like, yeah, we're adding some fields to the atomics, and that's gonna make everything slower.
**Tyler Yahn (Splunk)** 17:56 Oh, no, no, no, yeah, yeah, this is… no, like, yeah, nothing's actually, literally, it's not even in the same file. Like, if… if I did make a mistake and I'm adding it to the wrong receiver, please call that out, that's a block.
**David Ashpole (Google LLC)** 18:08 No.
**Tyler Yahn (Splunk)** 18:08 But, like, but yeah, like, it shouldn't actually change any… like, this literally doesn't touch any of the stable stuff. So, yeah, it's just more of a comparison, I guess. So, yeah.
**David Ashpole (Google LLC)** 18:17 Bye.
My… my thought is, the thing you described with, like.
the state in a bit, and then the counter is almost exactly what the hot-cold weight group thing is. So, like.
And we already use that in some of the… in a lot of… like, in histogram, for example, we use it for everything, right?
**Tyler Yahn (Splunk)** 18:39 Yeah.
**David Ashpole (Google LLC)** 18:40 So, if we… if we were able to put the state management as something that was also hot-swapped… then I don't think we would have any overhead there, because ideally, when we're doing things like retiring, we would be operating on something that we have exclusive access to.
**Tyler Yahn (Splunk)** 18:56 Yeah, that's a… that's a good point. I kind of considered that, but I also, like, just stopped thinking about it, because I was like, I'm not gonna touch this at this point in the, like, development cycle. But yeah, to your point about, like, performance-wise, I think you're probably on the right track, right? Because if we unify that all into, like, we're literally doing only one flip, then that should… Should definitely, like, provide better concurrent access, I do… how… how do we know in that swap… sorry, I haven't looked at this in a little while, but, like, how do we know in that swap that we're done writing to that cold, once we do the flip?
**David Ashpole (Google LLC)** 19:33 So the hot-cold weight group thing is actually… two counters, right? One is the number of started, and one is the number of completed. So you do, like.
you do two increments. One is when you start working on something, and then when you're done, you increment a second atomic counter. And then the weight group just needs to wait for them to equal each other.
And the… The swap bit is encoded in the number of started ones.
**Tyler Yahn (Splunk)** 20:03 Right, right, okay, I remember that part.
**David Ashpole (Google LLC)** 20:05 You can atomically swap while people are incrementing it, and, like, that… Race.
**Tyler Yahn (Splunk)** 20:13 Won't change the actual, yeah.
Yeah, I definitely think that there's a way we could store This, like, finish date there, then.
Cause you'd have a lot more exclusive access.
**David Ashpole (Google LLC)** 20:29 The only thing about sums is that one of the reasons why they're quick is that I don't remember if we even need to use for… cumulative… sums. I'm not sure if we need to use the hot… cold swap thing for it. We may just.
**Tyler Yahn (Splunk)** 20:47 Oh, yeah.
**David Ashpole (Google LLC)** 20:48 raw, like.
you know, whatever, and… because remember, we had that… we have, I think, still open that bug about, floats.
Being non-atomic, the float increments?
So, if we introduce it, that would introduce this.
cold thing there anyways, but I think there's one case today where there is no swapping going on, and it's just the atomic… the map lookup and the atomic increment.
There's no, like.
**Tyler Yahn (Splunk)** 21:14 Oh, interesting.
**David Ashpole (Google LLC)** 21:15 finishing.
Yeah, yeah.
**Tyler Yahn (Splunk)** 21:17 Yeah, I don't… and I'm definitely measuring in that benchmark the cumulative sum, so that might be relevant here, but I'm also, like, not going through a collection cycle, in that benchmark, so it should be… it shouldn't make a difference, I don't think. Even if I switched to a Delta, I think you'd probably still see a similar… performance from that benchmark. From, like, a real-world use case, probably, probably different, but, yeah, like, I think that that's, that's interesting. Okay.
But yeah, so, I mean, I think that that's, like, it's… it's worth, taking a look at. It looks like Robert's already reviewed it, it needs another review, and it's worth… Yeah, okay, cool.
Awesome. So, next up on the agenda, Puneet, you wanted to talk about meter configure, disabled meter to snowop conflict?
**Puneet Singh** 22:07 So… I mean, during the implementation, currently, as per review, it has two.
Issues with respect to spec?
The one that was discussed in the specification meeting was about, the meter configurator description of disabled estate and its conflict with the no-op state. So my understanding from the feedback was that The issue is still experimental, and… The group didn't have a very strong opinion on the direction to move, but… They gave kind of a favorable, you know, signal that, in case if you want to Separate out the… a part of a no… op behavior as incompatible with disabled estate. That can be pursued, but nothing, nothing more than that. It has to be, I'm just slowly coming to realization that this thing is not going to drive itself. It has to be brought into discussion, but the… The next feedback about the implementation, again, brought back to the same point, which is, the opinion of the SIG itself, that is it okay to move this implementation forward while the, specification catches up on that?
And what I'm saying is this, That the… regarding the conflict, the proposal to drop, the construction type NOA behavior of meter, which is considered in conflict with the disabled state. It was, like, considered okay that this can be dropped.
As a requirement, but currently it is not, like… it has to be discussed before it can be put as a spec guidance, actually, so that will naturally take more time to follow up.
But… but that is something I'm willing to own, so… so yeah, that's the question is.
**Tyler Yahn (Splunk)** 24:15 Yeah, so this is, like… I don't know if you remember, but this is, like, my whole reason why I don't think that the meter configurator is something we wanted to support in general, was this enabled state and disabled.
thing, like… It becomes, like, a duplicative, like, configuration, and then it deals with these kind of complicated, like.
alternate pathways to handle, like, enablement and disablement, which are very, like, implicit and not explicit in, like, the GO sense.
Right? Like, in GO, like, when you get something, it either is or it isn't. It's not like this in-between state where it can change in the future.
And I think this is, like, one of my main, like, reasons why I was, like, not in support of adding this at the specification level.
Especially since, like.
providers, or I'm sorry, processors can also handle this. In, like, in, like, the tracing world, like, it seems like having something at, like, the reader level is a way better way to handle something like this. In fact, we do that. Like, without readers, like, this actually becomes, like, a no-op.
And it becomes disabled. So, like, I don't know, like… I'm… I'm skeptical, like, if, like, what your concerns are, are not… Like, broader issues with the entire concept.
that the specification is kind of not really wanting to, I don't know, dedicate effort to addressing right now.
So, I, I don't know, Yeah, I'm a little bit hesitant to say, like.
You go and you add this new… feature in the end of the day. Like, it's actually gonna reduce the performance of the people that are not using anything, like, using the no-op state.
like, that seems pretty problematic. Like, in the experimental phase, like, I mean, I think that that's reasonable. Like, you turned on an experimental feature, and, like, somehow it's gonna, like.
yeah, it would change the default behavior, like, that seems fair. But, like, as, like, this goes to, like, a stable implementation that we would try to adopt, like, I don't think that's really appropriate, like, for folks that are… running the instrumentation, and it's turned off, and all of a sudden, like, they upgrade Hotel GO, which is something they're not actually using, and it, like, degrades their performance, because now it's having to do things more than just what the no-op was doing, like, that seems… problematic. And it seems like a bug that we could get and be completely validated in saying, like, yeah, that's not really acceptable.
**Puneet Singh** 26:43 I want to come to the point that, you know, about the regression it might cause, or the performance impact. Like, you know, in which… I wanted to understand more that in what cases this is considered as in, that this is a possibility, actually.
The… the… so this is one part. Another is the… the dynamic behavior. It's… it's not, like, it's very much part of the spec as how meter configurator is defined. So it's not supposed to be static. Yeah. So, so, so yeah, I still wanted to, you know, it doesn't clarify for me that, how this is going to impact the, Perform inside, or any other thing.
**Tyler Yahn (Splunk)** 27:37 Well, I mean, I… I think you were arguing that it is going to impact it, because it's not going to be doing nothing anymore.
**Puneet Singh** 27:48 Let me, let me restate a bit. So, the configurator has this meter configured returns, right, which has enabled or disabled a state.
And it's more like a dynamic kind of behavior.
It can, depending on whether you set, whichever value you set meter configurator with, it can enable or disable the meter, and that is very much controlled by the external caller. It's not something that happens, out of blue. And… As long as nobody calls to set the meter configurator, the value that is written by the function is very much deterministic. It's not going to change, So, so yeah, that is the, core part of the meter configurator, and the only, way it's going to change is, is, is, like, some external watcher which is looking for some file change, like the declarative config itself.
And depending on the… change of the path it calls the meter configurator. So the responsibility of identifying and calling the configurator set function is entirely outside the, meter provider itself.
**Tyler Yahn (Splunk)** 29:04 Yeah, but how do I go through a state change?
How do I go from disabled to enabled?
How do I have an API that has a no-op implementation now become an enabled implementation?
**Puneet Singh** 29:17 So that… so the responsibility of the meter providers to allow this, that external entity can call this to change their behavior, the responsibility of.
**Tyler Yahn (Splunk)** 29:28 But how, like, I mean, sorry, I don't mean to, like, be rude and cut you off, but, like, I mean, I understand all of this, like… My point is, is that… you have to change the default NOAP implementation.
to become enabled. Right now, you cannot do that with the default known implementation.
Like, if I get back a meter provider from the global API, it is… Either disabled for its entire lifetime, or it's enabled for its entire lifetime.
Like, there's not an in-between state, right? And so, like, going from an enabled state to a disabled state, like, I can see… That's not really much of a performance regression, like, you're gonna go from something that's doing a lot of work to minimal.
But something that's going from a disabled, which has a no-op implementation, which is doing literally nothing, by the definition of specification, to doing something more than nothing is… is… that's the performance regression that I'm talking about.
**Puneet Singh** 30:20 Yes.
**David Ashpole (Google LLC)** 30:21 Does this all just amount to us needing to update the spec to, instead of saying no op, to say, like.
A delegating meter? Or meter provider?
Like, we have an implementation of, like, the delegating one in… In our global package, right?
**Tyler Yahn (Splunk)** 30:37 Kinda.
Kind of. So, I think…
**David Ashpole (Google LLC)** 30:42 Like, it's obviously not a no-op, so the spec is incorrect, right?
**Tyler Yahn (Splunk)** 30:46 Yeah, sure.
But what happens, I think, for, like, the subsequent Right?
**David Ashpole (Google LLC)** 30:53 When you turn it on, you turn it off. I guess you have to have.
**Tyler Yahn (Splunk)** 30:55 No, no, no, no, so, so, like, so right now we have a delegating meter provider, right? And, like, that returns it, but, like, so then you go register a meter provider with the global, but it's, like, its configuration state is disabled.
Right?
Is that gonna return a no-op?
**David Ashpole (Google LLC)** 31:11 No.
That's what I'm saying, like, I think the spec for this configurator thing says it's a no-op.
And it's… it can't be a no op, right? Like… Like, that's just wrong. And it's… The thing that it needs to be is… like, basically another delegating thing, right? Like, because it needs to be able to delegate to nothing to a NOAP.
when it's false, and delegate to a real thing when it's true. So…
**Tyler Yahn (Splunk)** 31:42 Yeah, I mean, I… this is, like, we're all in agreement, finally agreement.
**David Ashpole (Google LLC)** 31:45 We're all in agreement.
**Tyler Yahn (Splunk)** 31:46 But the problem that I'm saying is that, like, from the user's perspective, where before, they would have got something that was not a delegating, and now they're going to get something that is a delegating.
Won't that have worse performance?
And won't that…
**David Ashpole (Google LLC)** 31:59 percent.
**Tyler Yahn (Splunk)** 32:00 Yeah. So if that's having worse performance, and they've gone through some sort of upgrade path, but they're actually not using it.
Doesn't that mean…
**David Ashpole (Google LLC)** 32:08 I do think.
**Tyler Yahn (Splunk)** 32:08 That's…
**David Ashpole (Google LLC)** 32:09 I agree. I think we would need to make sure that if someone has not used a meter configurator, which I hate saying.
That their performance doesn't change, and it's only when they decide to plug one of these in, that they get this delegating behavior. Kind of like today, like.
Yeah, there's some overhead if you use the globals.
And you'll get better performance if you explicitly pass noops everywhere.
If that's what you want. But… they exist, and they're maybe useful to some… to a lot of people. I think this is significantly less useful, maybe, but… Like, that's… To me, as long as the new thing Only introduces performance regressions when you use the new thing.
I'm, like, more okay with it.
**Tyler Yahn (Splunk)** 32:59 Yeah, but, like, is that… Is that the case, though?
So, like, if you, like, if you get a beta provider, like, say this is, like, I don't know.
6 months from now when it's stable, because we're really fast at things. yeah, so… so it… but, like, I have a meter provider, can I provide it a dynamic configuration at some point in its life cycle?
**David Ashpole (Google LLC)** 33:22 you will… It's a good question. Do you… I forget. Does the, does the configurator get registered after the fact, or do you create it with it?
**Puneet Singh** 33:33 No, you create the provider with a configurator, you cannot do it after the provider is created.
**David Ashpole (Google LLC)** 33:41 So it's like, if you… if you don't pass with meter configurator.
then you should get the same performance you have today. And if you pass this thing.
Which needs to have, like, a disclaimer on it, that basically false is not the same performance as a no-op.
Then, you know, you get a delegating thing that… has some overhead when you're creating instruments and whatnot. But then.
You get this new capability, which hopefully you appreciate.
And.
**Tyler Yahn (Splunk)** 34:07 Yeah, I think that makes sense to me. Like, I… yeah, as long as that's the case, like, where somebody who's, like, not touching the meter configurator.
like, does not experience, like, a change in the behavior, change in the performance, change in anything like that. Like, if you're, like, yeah, if it's not, like, something where you can plug in a new configuration to the meter, like, that seems… that seems fine. That makes a lot of sense to me, especially if it's only on, like, creation that, like, you can essentially set up a dynamic pipeline, but… Yeah, is that how it's defined in the spec? I don't remember.
**David Ashpole (Google LLC)** 34:39 I think it is past it.
Creation time, the configurator.
So I think we're spec compliant there.
The thing… the thing that I feel like just needs to be adjusted in the spec is the language around no-ops, because… I think it's… not correct, but I think we should… For our prototyping and stuff, we should just assume that it will be delegating And not a no-op, and… If it's something we want to introduce and prototype, then we should just move forward with that and separately You know, file an issue and fix it in the spec.
**Tyler Yahn (Splunk)** 35:14 Hmm, yeah.
**David Ashpole (Google LLC)** 35:25 Am I wrong? Are you reading the spec now?
**Tyler Yahn (Splunk)** 35:28 Sorry, I am… yeah, I can…
**David Ashpole (Google LLC)** 35:30 That's fine, that's fine, feel free to correct me.
**Tyler Yahn (Splunk)** 35:37 So, yeah, maybe we can just walk through this really quick. So, yeah, the meter configurator is a function under configuration.
and under meter creation, I'm…
**David Ashpole (Google LLC)** 35:51 It's meter provi… I thought there was something about… meter provider… arguments or something.
**Tyler Yahn (Splunk)** 36:01 Yeah, I thought so too. Oh, that's why I'm a little confused in development.
**David Ashpole (Google LLC)** 36:15 Using the configured meter configurator.
So… Is there some… is there, like, a meter provider configuration? Or, sorry, meter provider creation?
**Tyler Yahn (Splunk)** 36:29 Oh yeah, here it is, oh, I'm sorry, saw the creation of multiple, like, there's nothing, yeah.
**David Ashpole (Google LLC)** 36:35 There's no arguments, okay.
**Tyler Yahn (Splunk)** 36:36 No, it's not where it gets. Hmm.
Function… it's a function for what, though?
Can you imagine?
**David Ashpole (Google LLC)** 36:48 Oh yeah, I added that.
Configurator.
It's like, obviously on the meter provider, right? Because it needs to be able to influence how you create meters.
**Tyler Yahn (Splunk)** 37:02 Yeah, this is… this is the thing that I was remembering, and it's a little bit…
**David Ashpole (Google LLC)** 37:09 Yes.
**Tyler Yahn (Splunk)** 37:10 This is the thing that I'm, like, worried about.
Where a meter provider provides a way to update the configuration, which is not, I guess, the meter configurator.
Or if it is, I'm not exactly sure.
**David Ashpole (Google LLC)** 37:28 Oh, configuration, metric exporters, metric readers, views, and development meter configurator.
Must be owned by the… okay.
the configuration may be applied at the time of meter provider creation, if appropriate. So, like, kind of… you can pa… the spec allows us to pass these whenever we want. We can require that it's on creation, I think.
**Tyler Yahn (Splunk)** 37:51 I think that's right.
I think you're right, yeah, from my understanding of this.
**David Ashpole (Google LLC)** 37:57 I just remembered that the prototypes I was reviewing did that, and assumed that it was spec compliant.
**Tyler Yahn (Splunk)** 38:06 Because that's… that's how hotel spec works.
**David Ashpole (Google LLC)** 38:09 Yep.
**Tyler Yahn (Splunk)** 38:09 Yeah.
Sorry, that's a cynical joke.
Okay, cool. Well, I think that, like, it doesn't say anything about, like.
contrary to what was described. So, Puneet, does that make sense as to, like, the GO direction, and what we're comfortable with, like, approaching this problem with?
**Puneet Singh** 38:30 So, I mean, in case if it is not… Used, there should be no performance impact on the overall usage.
And there should be no change in behavior.
And if it is used, it's… it's, okay to… to… as long as user, like, accepts the corresponding, regression that has to be presented in order to support this. Is that the…
**Tyler Yahn (Splunk)** 38:58 Yeah, yeah, agreed. So, what I would say is that, like, I'm not 100% sure on our implementation right now, but, like.
if you ask for a new meter provider currently, and you don't provide any, like, readers, it'll just give you back a no-op, right? And so, I think that, like, what I'm saying is that, like, the… Change would be, if you ask for a new… meter provider, you don't provide any readers, but you provide a meter config, then you would get some sort of, like, thin implementation, right? Or just a meter config… God, this is horrible to say. A meter config.
aware meter provider, but if they don't provide a meter config, and they don't provide any readers, they still need to get a no-op back, is kind of what I'm saying, yeah.
**Puneet Singh** 39:42 Right.
**Tyler Yahn (Splunk)** 39:42 That can't be changed after the fact, kind of thing.
**Puneet Singh** 39:46 Okay, that makes sense. Other thing I wanted to… ask is… yeah, just delegating no-op, I've heard for first time, actually. So, is that something I should consider using, rather than trying to argue about that we should split no-op behavior, and disabled should be separate, and no ops should be, yeah, the complete thing?
**Tyler Yahn (Splunk)** 40:09 Yeah, so the delegating thing comes from the Global API, and David's right, like, by default, if you get a meter provider from the Global API, you don't actually get a no-op, you get this thing that will, like, eventually give you something if it gets registered after the fact.
Yeah, I guess… I don't know if it was in the same spec meeting, but not a lot of people are happy about that, but yeah.
**Puneet Singh** 40:29 So, I'm not sure if that's the thing that can be used for NOAP.
I mean, yeah, no.
**David Ashpole (Google LLC)** 40:36 That's why I'm saying it's not a NOAA. And actually, I may be overcomplicating things, because we don't need to delegate to an arbitrary meter.
**Tyler Yahn (Splunk)** 40:46 I don't think so.
**David Ashpole (Google LLC)** 40:47 We… we could actually create the actual meter, and then just… ignore the measurements, I think would be… the thing that we could do, right? Like, we don't… I don't know what you think about that. If… If we actually create all the, like, meter and instruments and stuff, but then we're like, oh, you measured something on a disabled, and that's the part where it… It actually… that's where we throw in a no-op, is like… There's a no-op… version of an instrument, or an OAP aggregator, or something, a drop aggregation.
And then… I don't…
**Tyler Yahn (Splunk)** 41:24 Yeah, I think if there's, like, I think… to be… fair. I would want to see benchmarks for a few different implementations. I think David's approach is probably good.
I mean, that still, at minimum, is going to require a Boolean flag at every lookup for, a measurement, which may be the most optimal. It may also be that, like, yeah, you'd want to, like, do something underneath the hood when somebody switches that may be way too heavy. So, yeah, I mean, I don't think… I'm too concerned about that in this experimental phase. So, yeah, if you and David have some really strong opinions on that, I would definitely say, like, collaborate on it, like, but, Yeah, it's more about, like.
Yeah, like, I don't know if I'd look into the delegating or not, but I, you know, when we stabilize, I would want to see, like, performance benchmarks.
But I think you're… to your point, like, I don't think you have to have it that way for this initial implementation.
Like, I think that… like, there's… like David just pointed out, I think that's a totally acceptable way to go about this.
You know, maybe… you have to weigh off the fact that, like, that may have overhead for, like, somebody who hasn't enabled this experimental feature, and, like, weigh that analysis, like… is this adding, you know, 2 nanoseconds to a measurement? Like, maybe that's fine. Is it adding, like, 50, like in mine? Or, you know, like, that may be problematic for the measurement case. So yeah, maybe it's, like, if in this experimental phase, like, it's more trying to isolate, rather than, Yeah, but I guess I'd have to see prototypes at that point, but I think, to your point, like, I think it's time to, like, you could probably start writing code, because I think we have a path forward on, like.
what we're waiting for from the specification, I think is more what I'm trying to say here.
**Puneet Singh** 43:22 Yeah.
**Tyler Yahn (Splunk)** 43:25 That looks like.
**Puneet Singh** 43:25 the face.
**Tyler Yahn (Splunk)** 43:26 If somebody's starting to… Yeah.
**Puneet Singh** 43:28 I mean,
**Tyler Yahn (Splunk)** 43:28 I mean, the cynicism, yeah.
**Puneet Singh** 43:32 Yeah, I think the… I wasn't, like… quite convinced, or, you know, towards the NOAP behavior, that that is… I understand your concern regarding introducing the new feature, but the friction with the NUAP was… More because the… The meter needs to hold its state in order to be enabled again, so… Coming to the point of user paying extra penalty for this, so… I mean, yeah, I agree that there will be some performance penalty.
By opting into this, but it also allows user to… to disable the… particular meters which are not in use, actually. So, if this is, let's say, not available, the meters that a user has created will continue to run, whether they are not used or not, but that is more of the user side of the story. I'm not, like, trying to, We'll be on…
**Tyler Yahn (Splunk)** 44:37 I'm not particularly worried about that, from, like, what we were saying, though. If they're enabling this experimental, like, meter configurator as an option, into this, like, meter provider creation, like.
there's gonna be warnings associated with that in the docs, like, they're literally importing it from an experimental package, like, there's going to be impacts, like, that, like, I mean, I wouldn't… I wouldn't want to create, like, exponentially, like, scaling things that are coming out of this, but, like, I'm also saying that, like.
yeah, if a user adds experimental features that say, like, the no-op behavior is going to have, you know, increased overhead of this scale, like, you know, inbounded on some way, then, like, yeah, let's go for it. Like, that just… If this feature is that important to the user.
And they're willing to make that trade-off, then… We're all in harmony at that point.
If they come back, and, like, the feedback is, like, look, this is great, but, like.
You know, every time the 100 nanosecond, like.
delay on this measurement is just way too much, like, then it's, like, an engineering problem. It's like, okay, then can we fix that? You know, if we can, then we can look into doing something like that. Yeah.
**David Ashpole (Google LLC)** 45:46 I think this… the state tracking, I'm less concerned about, right? Like, we will have to track state to make this work, no matter how it works.
I think it's the…
**Tyler Yahn (Splunk)** 45:55 Yeah.
**David Ashpole (Google LLC)** 45:55 the performance, hopefully, we can find a way to make it, at least on actual… like, instrument creation is whatever. If it's a little bit slower, fine. If it's, like, Hot Path.
Measurement performance penalties, then that feels… less acceptable.
But… Agreed, yeah, like…
**Tyler Yahn (Splunk)** 46:15 Sorry, like, yeah, that's just… I'm just immediately jumping there. David and I are both, like… because that's, like, the one thing that actually matters, like, yeah. So, like, that's really the only thing that, like, that, like, it really is key that, like, that performance there is going to be fine, especially if somebody's, like, doing a no-op around that, like, because that's happening continuously, all the time.
And even then, like, with, like, the state, like, setup, like, if it's disabled, like, there's gonna be maybe some overhead in the no-op once they've opted into this feature. That's, like… like David said, like, I don't think there's getting around that. There's definitely ways to try to, like, minimize it, but again, like, it's just more about what's… what's the performance overhead and benefits there.
**Puneet Singh** 46:58 Sounds, sounds, okay, could be your debit?
**David Ashpole (Google LLC)** 47:01 I was just gonna say, I also, unfortunately, haven't had time to do a deep review of your PR since… since, Maybe for a week and a half, so… I owe you one there. I think I'm talking in generalities, but, like, it may very well be that your PR is fine.
For all the things we're saying.
**Puneet Singh** 47:19 Yeah, I was going to say at the end, you know, might… that, you know, a look at the PR once more would be helpful, that, you know, if I try to, like, focus more on the benchmark on… on the specific, side, which I haven't covered, maybe. So, yeah, that would be very useful.
**Tyler Yahn (Splunk)** 47:37 Could you, link your PR in the, Meeting agenda notes, just to make sure that, like, I don't lose track. I'll try to take…
**Puneet Singh** 47:45 Sure.
**David Ashpole (Google LLC)** 47:47 I think it's there.
**Tyler Yahn (Splunk)** 47:49 Oh, it is? Sorry.
**Puneet Singh** 47:50 No, that was wrong.
**David Ashpole (Google LLC)** 47:52 That's a different PR.
**Puneet Singh** 47:53 That was the spec.
**Tyler Yahn (Splunk)** 47:56 Yeah.
Okay.
**David Ashpole (Google LLC)** 47:59 No.
**Tyler Yahn (Splunk)** 48:00 Cool. Well, it sounds like that's ready for another review then, is kind of the takeaway I got on this.
**David Ashpole (Google LLC)** 48:05 I was looking at last week, that's why.
**Tyler Yahn (Splunk)** 48:09 Oh, it's there? Oh.
**David Ashpole (Google LLC)** 48:10 Well, it was, like, last week, yeah.
**Tyler Yahn (Splunk)** 48:14 Okay, cool.
Alright, cool, that's the end of the written agenda.
Any other topics top of mind for folks they wanted to talk about?
I do feel like, our experimental… functionality that we're adding here is probably worth a talk, at some really obscure GO conference, probably. But, like, yeah, if folks are interested in proposing talks, I don't know if it's a KubeCon talk, but yeah.
**Puneet Singh** 48:55 I think it's an interesting one, based on the challenges I have seen so far, so… so yeah, definitely.
**Tyler Yahn (Splunk)** 49:00 Yeah, yeah, agreed.
But that's kind of a segue into the fact that the KubeCon EU CFP is open currently till, I think, early October, so… If you have other weird and interesting talks around OTEL, probably this is a little too specific to go. But yeah, like, I definitely encourage people to reach out to other people. Doing a talk and getting it accepted by yourself is hard.
not impossible, but it's way easier to do if you have folks from other companies, or other projects, or other things like that. So, yeah, definitely start… please start thinking about them. I think the more visibility we can have, the better.
I imagine there's going to be some, talk about logging from Robert, but… That is completely unsubstantiated by any sort of facts, it's just feeling.
**Puneet Singh** 49:55 I started watching some of the previous talks from this SIG just for Motivation, actually.
I started with, yeah, David's stock from his Kubernetes days, and then… I think then I went back… I found this stock from, I think, a KubeCon?
for, a spec share, and that was chaired by, I think, Tyra regarding… they were talking about how to move stuff during… in OTEP and the specification, actually.
Yeah, just before my specific, you know, the last Tuesday's call, actually, I thought it might come useful.
**Tyler Yahn (Splunk)** 50:31 Well, was it?
**Puneet Singh** 50:33 I mean, it, definitely.
**Tyler Yahn (Splunk)** 50:35 You can say no.
**Puneet Singh** 50:36 calm myself, actually. I mean, I was like, yeah, let's go with it and see how it goes. So, yeah.
**Tyler Yahn (Splunk)** 50:41 Okay. Yeah, I mean, that's definitely… hopefully the takeaway is…
**Puneet Singh** 50:45 But overall, I think the talk itself was really good, that when someone comes to grips with the whole process, then it has a lot of useful things that were covered, so yeah.
**Tyler Yahn (Splunk)** 50:55 Okay, cool, yeah, that's actually really good feedback.
Because I know there's more Maintainer Talks coming up at this next Maintainer Summit, so… yeah, that's also… Good to hear. Good to hear that people are actually watching those things, so yeah.
Well, cool.
Alright, we could probably end the meeting here. Thanks everyone for joining.
I will see you all in a week's time, or asynchronously. Till then, bye.
**Marc Schäfer (T&A SYSTEME)** 51:21 R.
**David Ashpole (Google LLC)** 51:22 Vegas.
