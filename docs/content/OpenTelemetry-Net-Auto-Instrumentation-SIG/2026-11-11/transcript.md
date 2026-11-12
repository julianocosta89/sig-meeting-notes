SIG: OpenTelemetry .Net Auto Instrumentation SIG
Date: 2026-11-11
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Zach Montoya** 01:58 Hey, Chris.
**Chris Ventura (New Relic, Inc.)** 02:01 Hey, Zach.
**Zach Montoya** 02:02 It's… appears as if there's a Splunk thing going on simultaneously, because we have no Splunk attendance.
**Chris Ventura (New Relic, Inc.)** 02:11 Ugh, that's okay, I've barely been able to make these meetings with everything going on.
**Zach Montoya** 02:17 Yeah. Yeah. Same.
You also have a bunch of things coming up for reInvent, or is that just us?
**Chris Ventura (New Relic, Inc.)** 02:25 Honestly, I'm left out of that. I've got enough.
**Zach Montoya** 02:29 Oh.
**Chris Ventura (New Relic, Inc.)** 02:29 You're.
**Zach Montoya** 02:30 Good for you. Yeah, yeah, good for you. Definitely want to avoid the deadline engineering.
**Chris Ventura (New Relic, Inc.)** 02:36 I think that's a common thing.
Across the industry.
**Zach Montoya** 02:43 laughs.
**Chris Ventura (New Relic, Inc.)** 02:45 I think we're all given deadlines.
**Zach Montoya** 02:47 But we can do so much with AI these days, you know?
**Chris Ventura (New Relic, Inc.)** 02:51 That's right, there's a deadline.
**Zach Montoya** 02:52 Ha ha ha.
you Oh, yeah, I, on my side, I… Started one PR… in the Datadog repo to address, a duct typing thing that we can port over.
**Chris Ventura (New Relic, Inc.)** 03:09 Oh, yeah, yeah.
**Zach Montoya** 03:10 So I started that, it's got one approval there. Once that's done, we can port it over to the Donna Instrumentation, and then… There's one outstanding issue about runtime async, of, how right now our mechanism isn't compatible with, running in our, like, on async method, like, end, whatever the handler, we cannot ourselves invoke async code right now, and have it work correctly with the runtime async feature. Okay. It exists in both repos. It's currently not a blocker for either of us, so…
**Chris Ventura (New Relic, Inc.)** 03:52 Yeah, is that specifically dealing with the… Task of a task.
A situation that happens.
**Zach Montoya** 04:01 No, so the question is… so we can currently instrument. Any, like, task-based methods, or anything async, and we will… now, with, correctly instrument it, even if it's, a runtime async method.
The issue exists when we have our… Our handler run, and if we need to run anything async ourselves, then we have to make.
our method async.
**Chris Ventura (New Relic, Inc.)** 04:31 Okay.
**Zach Montoya** 04:33 Let's say we need to await, like, some… some flush or something like that. In our own handler. Today, like.
With normal… without the runtime async methods.
We can actually create a… A handler method for the… the… Async end.
**Chris Ventura (New Relic, Inc.)** 04:51 Gotcha.
**Zach Montoya** 04:51 And so we can make that async, we can await stuff in there. But, we can't do that right now with runtime async. Everything that we run inside the handler has to be synchronous. So… It's not used anywhere in this project. Yeah.
**Chris Ventura (New Relic, Inc.)** 05:07 Okay.
**Zach Montoya** 05:08 So no blockers, no blockers here.
**Chris Ventura (New Relic, Inc.)** 05:09 Yeah.
**Zach Montoya** 05:09 There's a couple places in the Datadog one that are, using it, but it's not, like, the hot path, so… Gotcha. But we plan to address it, probably the beginning of next year, so…
**Chris Ventura (New Relic, Inc.)** 05:21 Once you have time, right?
**Zach Montoya** 05:23 Yeah, so I just commented on the issue that Piatra opened, that we can simply just wait, because there's no urgency. We don't have anything blocked on that, so…
**Chris Ventura (New Relic, Inc.)** 05:32 Okay.
**Zach Montoya** 05:33 That's just my updates. That's all I've been able to dedicate to this repo, is investigate some of the shared code gaps and issues, and at least keep track of them, and then… Hopefully ports them over, but yeah, my capacity has been pretty limited.
**Chris Ventura (New Relic, Inc.)** 05:52 Yeah, I hear you on that.
Yeah, I'm just thinking through the runtime async stuff.
Yeah, I think we're in a good enough spot… Because I don't think… for OTEL, we have any bytecode instrumentation.
That deals with methods that have been converted over to runtime async.
And… We've got the bare minimum support for it.
I'm.
**Zach Montoya** 06:29 I mean, if we have the smoke tests that show that it runs on .NET 11, then that's sufficient because the only things that are gonna be built with Runtime Async, at least immediately, would be BCL stuff.
**Chris Ventura (New Relic, Inc.)** 06:42 Yeah, and I think we did the smoke test for .NET 10.
Since it is technically available on .NET 10.
**Zach Montoya** 06:53 Oh yeah, I guess that's his opt-in, right?
**Chris Ventura (New Relic, Inc.)** 06:55 Yeah, and then we just had to update the, declarative configuration?
**Zach Montoya** 07:02 Okay, yeah.
**Chris Ventura (New Relic, Inc.)** 07:03 So where you can specify the custom instrumentation in the declarative configuration, it was that hook that was primarily affected by runtime async.
**Zach Montoya** 07:13 Got it.
**Chris Ventura (New Relic, Inc.)** 07:14 Just because… Somebody could be using that for a method that's been converted over.
**Zach Montoya** 07:22 Yeah, and I guess if there's any issue with that, like, a user report about that, then we can address that.
**Chris Ventura (New Relic, Inc.)** 07:29 Right, but that hook doesn't use the custom handler that you mentioned.
**Zach Montoya** 07:36 Right, it's just a completely synchronous end where we just close the activity.
**Chris Ventura (New Relic, Inc.)** 07:41 Yeah, exactly.
**Zach Montoya** 07:43 Yeah, so that should be fine.
**Chris Ventura (New Relic, Inc.)** 07:45 Yeah, because runtime async behaves differently anyways.
It does behave more synchronously.
From everything I've seen.
So, by the time, you exit the method, so you get that exit method notification, all the async work's done at that point.
And you have the final result.
So it's not like you've got a promise that you still need to await.
**Zach Montoya** 08:20 Gotcha.
**Chris Ventura (New Relic, Inc.)** 08:23 So, I think we should be okay.
**Zach Montoya** 08:28 Yeah, I would expect so.
**Chris Ventura (New Relic, Inc.)** 08:30 Yeah, and then the next priorities for this month will be… So the SDK just released their .NET 11 changes, so… We'll be getting it pulled into, auto instrumentation. Yep. Then cutting that release. I don't remember if there's, There's probably still a handful of other… NET 11-related tasks to do in addition to that dependency update.
**Zach Montoya** 09:00 Yeah, I think… I think there was one draft PR for just updating our… Correct.
**Chris Ventura (New Relic, Inc.)** 09:06 Right.
Where we're dropping 8 and 9 support.
**Zach Montoya** 09:10 yes.
**Chris Ventura (New Relic, Inc.)** 09:12 And then a few other things.
**Zach Montoya** 09:15 Yeah.
So we got a couple things.
**Chris Ventura (New Relic, Inc.)** 09:19 Yep.
Okay. Yeah, I don't see a point in going through the agenda too much.
**Zach Montoya** 09:27 the.
**Chris Ventura (New Relic, Inc.)** 09:28 of us.
**Zach Montoya** 09:28 Yeah, yeah, yeah.
Alright, cool.
**Chris Ventura (New Relic, Inc.)** 09:33 Okay.
**Zach Montoya** 09:34 Talk to you later. Have a good one.
**Chris Ventura (New Relic, Inc.)** 09:35 Yep. See ya.
