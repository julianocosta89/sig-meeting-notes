SIG: .NET Auto-Instr SIG
Date: 2025-07-09
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

Piotr Kiełkowicz 00:01:42 Hello, guys, sorry for being late, but we have internal meetings a bit longer than usual.
Rasmus Kuusmann 00:01:49 Hey!
Zach Montoya 00:01:50 Hello! No worries.
Piotr Kiełkowicz 00:01:57 Paolo mentioned that he's not able to join.
Mateusz Łach 00:02:00 Hello!
Piotr Kiełkowicz 00:02:06 Matterus, can you share the screen and drive the meeting today?
Sorry.
Mateusz Łach 00:02:15 Yeah, no worries, no worries. Let me just parts.
Okay? Yeah. Let's go with the the usual stuff.
So let me take a look at the Prs.
There is one from depend about. So does this.
Yeah. So we we aim for a release late last week. But we didn't have a chance to run tests on Mac OS. Erasmus was trying to help with that. We have some basically issues with availability of of mark to run the tests.
But at the same time, I think, yeah. So do you want to add anything? Because I think there is a change in the in the country related to one of the packages that we might want to wait for right.
Piotr Kiełkowicz 00:03:56 Yes. The SQL client instrumentation has a Pr with context propagation using context info.
yes, this one. And if Alan from neuralik will be able to review it. I would like to also include changes from this.
There will be possibility to include trace span id by contacts. Info and configuration would be through the experimental, environmental, variable, variable.
Chris Ventura 00:04:37 So I'm curious about that. How does that work with a database?
Is it just certain database operations can in turn pass that context around.
Piotr Kiełkowicz 00:04:50 Only for the SQL. Client server, SQL. Server.
Chris Ventura 00:04:56 So like right.
Zach Montoya 00:04:57 So that one it sets. It basically issues a separate command separate from the intended one to set the contents info. So it sets a binary blob, which would be the trace parent header and then, if there's a transaction for that transaction, it'll use the same transaction and set that so yeah, it makes one additional call, and then it makes the intended call, and then, so now you have that correlation.
If the dB, provider uses that somehow or the yeah, like, sample stuff.
Chris Ventura 00:05:32 Maybe it's a way to provide a infrastructure level linkage or or something.
I was imagining. It's related to that queuing technology that you can do in SQL. Server that I don't know. I thought it was deprecated, but I was just curious.
Piotr Kiełkowicz 00:05:52 It was accepted by this open telemetry specification.
There is also ongoing effort for similar functionalities for other databases, but there will be no trace context propagation, there will be only service name propagated to the through. The comments probably.
Zach Montoya 00:06:18 Yeah. Cause at least this one with SQL. Server. By setting the context, you don't actually change the intended query so that one can have like. You won't have like cache misses, or anything like that. But with the other ones we can only do low cardinality service name, because otherwise you do start to change the the query, if you're injecting the trace. Id on every single one, so.
Piotr Kiełkowicz 00:06:41 Sorry, very sure, that it's actually reusing the transaction.
Zach Montoya 00:06:48 I'd have to check.
but.
Piotr Kiełkowicz 00:06:54 Have time. It will be great if you can review.
Zach Montoya 00:06:56 I'll take a look at this. Yes.
Rasmus Kuusmann 00:06:59 Yeah, I was looking into this one and didn't. I didn't understand? How is it actually isn't a transaction or not.
And what happens if it's blowing up.
because it seems to be completely a separate transaction.
Zach Montoya 00:07:21 Yeah, so it should. It should reuse the transaction so it should copy it over from the original SQL. Command.
If it's not, then that's that's an issue, or that's going to be an issue very quickly.
Rasmus Kuusmann 00:07:37 yeah, there seems to be just one little test, but nothing that that's the failing point or transaction. Sir.
Mateusz Łach 00:07:54 Okay. Can you take a look at this as well? Rasmus.
Rasmus Kuusmann 00:08:01 I can try. Maybe I didn't want to push back, because I'm not completely sure about the feature.
Mateusz Łach 00:08:10 Okay.
And, by the way, any like Eta, or where you might have Mac for testing the before the release.
Chris Ventura 00:08:29 What type of Mac? Are you needing.
Rasmus Kuusmann 00:08:34 Rubber bidding.
Piotr Kiełkowicz 00:08:35 Part of the risk process require execution. Integration. Test on Mac OS. With Docker.
Chris Ventura 00:08:43 Yeah, but I I just wasn't sure. Do you need it? Our Mac or Intel Mac.
Piotr Kiełkowicz 00:08:47 Alright.
I've whatever probably.
Chris Ventura 00:08:52 Okay.
Rasmus Kuusmann 00:08:54 There is a small risk, but should execute the same test. I think.
Chris Ventura 00:09:01 I can see if I can run the test later on. My machine.
Mateusz Łach 00:09:07 Okay.
Piotr Kiełkowicz 00:09:08 New new workflow with containers or set to Linux, should should do the trick.
Chris Ventura 00:09:16 Yep.
Piotr Kiełkowicz 00:09:16 It. The comment is in the.
Mateusz Łach 00:09:20 Interesting.
Piotr Kiełkowicz 00:09:20 Md.
Chris Ventura 00:09:29 Yep, I just gotta get my my repo updated locally.
Mateusz Łach 00:09:35 Okay, thank you.
For the file spaced config.
Anything you'd like to discuss related to this one.
Piotr Kiełkowicz 00:10:03 I think there's not so much changes from from the last week I still didn't have time to review it in detail, so I'm not sure if you guys have have time to look into it.
Mateusz Łach 00:10:16 Yeah, me neither.
Okay. If there's like.
should I move on or.
Rasmus Kuusmann 00:10:44 It's probably great to take some time to review this one. So let's move on.
Mateusz Łach 00:10:52 Okay?
Then there is update. And Pyotr, you are working on this one. Right?
You are on mute. Sorry.
Piotr Kiełkowicz 00:11:11 Sorry it is already passed before merging.net update to domain. So it is just rewriting. So, waiting for approval because I've made kind of additional changes, and it is ready to merge, in my opinion.
Mateusz Łach 00:11:28 Okay. You had.
Rasmus Kuusmann 00:11:29 It's not.
Mateusz Łach 00:11:29 Some insecure package versions, right?
Piotr Kiełkowicz 00:11:33 Yes, 1, 4 and 1, 6, 2 transistory dependencies vulnerable Z. Lip packet.
This native library.
It was not detected automatically. But I've checked it manually and removed at the same time.
Mateusz Łach 00:11:52 Okay.
Rasmus Kuusmann 00:11:53 Are we going to update the supported range.
Piotr Kiełkowicz 00:11:58 No, who are still supporting all, all the ranges.
Rasmus Kuusmann 00:12:03 But we're not testing.
Piotr Kiełkowicz 00:12:04 Yes, and it is compliant with our policy.
Rasmus Kuusmann 00:12:09 But how can we say that.
Chris Ventura 00:12:12 We? We don't.
Rasmus Kuusmann 00:12:13 Thank you.
Chris Ventura 00:12:13 Test all the versions, anyways.
Piotr Kiełkowicz 00:12:16 Which is in our policy. We we are telling that we are testing against latest, safe version.
the oldest save version and the latest release, and all others are.
We are assuming that it will be working fine.
Rasmus Kuusmann 00:12:43 I guess if it's dispatches, then it's fine to assume it. But if it's a minor version, then.
Piotr Kiełkowicz 00:12:56 I agree with you, Rasmus, but we are not changing the policy which we have already in place.
We have a lot of packages in the same situation, and we are not able to include into the big pipeline due to security reasons.
If somebody will be complaining, we just need to run a locally test, fix it, and hopefully, we will not do regression any longer.
and 3 dispatch version or main mine, or whatever.
So far we are good with current solution.
Mateusz Łach 00:13:37 Rasmus. Do do you think that we should create a like an issue to do? Discuss the approach or.
Rasmus Kuusmann 00:13:47 Sure it's a good question. Actually.
Mateusz Łach 00:13:55 Okay?
I'll create the create something after the after the meeting.
Because this is just confirm. This is already approach that we are using with other packages. Right? So this is not something specific to this one.
Chris Ventura 00:14:11 Yeah. Probably the most interesting thing regarding this one is that we're relying on a 0 code approach to to do it. So all of the instrumentation is in the Auto Instrumentation Project instead of us pulling in an instrumentation library.
So that's where I think it's a little bit more unique.
however, at least in my experience, most libraries are fairly stable, and I've only seen a handful of libraries where we've had to update that type of instrumentation for for minor versions.
And, Zach, I'm assuming you've had similar experience with that.
Zach Montoya 00:15:07 Yeah, most of the changes happen on major version boundaries. It's pretty rare that we have minor versions that affect bytecode instrumentation, although it has happened.
Piotr Kiełkowicz 00:15:18 B is kind of exception.
Chris Ventura 00:15:22 Mongo postgres, I think. Elastic. We ran into that.
but that's about it.
Mateusz Łach 00:15:49 Okay? Yeah. So should I create an issue after the meeting, Rasmus, you or.
Rasmus Kuusmann 00:15:59 If you have good ideas out there, then maybe somebody can contribute a great idea, and again, at least check.
Piotr Kiełkowicz 00:16:16 I put the link to the policy we have for the accreditation integration tests.
Mateusz Łach 00:16:26 Okay.
Okay.
yeah, that's it's in the developing, doc. Maybe we should.
I don't know. Maybe there'll be a better place for it.
I will create the issue link to this. And we can discuss it offline, probably.
Yeah, for this one for the next one, I think. I was absent last week, I think Pablo suggested to like to create, to like, prepare a demo. So I can.
I can show a like a small demo high, of how I how I think this could work.
so I'm not sure we can do it. After the we go over the rest of the stuff that work.
Okay? And then we have the configuration based instrumentation Poc peel through any progress here.
Piotr Kiełkowicz 00:18:04 Oh.
I've tried to look into task. It should be possible. It's needs some adjustment on the manage code level and.
Mateusz Łach 00:18:13 Okay.
Piotr Kiełkowicz 00:18:14 That's all. No more progress.
Mateusz Łach 00:18:18 Okay.
Piotr Kiełkowicz 00:18:19 Unfortunately, still, a lot of internal issues on my side.
Mateusz Łach 00:18:24 No?
So for the issues.
let me take a look.
Yeah.
Seems like there was no activity last week to hmm.
Do you want to keep it open, or.
Rasmus Kuusmann 00:19:03 It was kind of confusing. Either it's a theoretical issue or actually practical.
Piotr Kiełkowicz 00:19:12 I would put style label, and
Rasmus Kuusmann 00:19:22 I think, at least, I never saw an issue with this one.
Piotr Kiełkowicz 00:19:26 Me, neither.
Mateusz Łach 00:19:31 Okay, so stay, label, wait one more week, and we consider closing it next week. If there is no no activity here, does that sound. Okay for you.
Okay.
yeah. So this one Rasmus, do you? Do you happen to remember the details? Here is, are we waiting for some additional input from from the person creating the issue. Or it wasn't just like we didn't have time to look into it yet.
Rasmus Kuusmann 00:20:22 Probably should also look at first, st and then being again, I guess.
Mateusz Łach 00:20:31 Okay, so.
Rasmus Kuusmann 00:20:32 Repo seems to be there according to the are you sure.
Mateusz Łach 00:20:41 Yeah. So the person mentioned here, that's he or she's on vacation right now. So it's I won't be marking it just there for now, so let's oh, do you? Do you expect to have some time in the in the next week to to look into it?
Rasmus Kuusmann 00:21:05 It's like 50, 50.
Mateusz Łach 00:21:13 Okay, let's give it one more week, and we can discuss it again on the next next meeting.
Oh, yeah.
Should I ping for a for an update again, or.
Chris Ventura 00:21:31 That person is usually pretty responsive, so I suspect that when they come back we'll hear something.
Mateusz Łach 00:21:42 Okay, so I'll leave it as it is, for now and then there is this one.
Rasmus Kuusmann 00:21:57 At least for me, it seems.
it's not reporting the full exception. It should contain information. What is actually missing there.
Mateusz Łach 00:22:14 Okay.
Chris Ventura 00:23:23 Yeah. So either we need the full exception, or we need a repro.
Mateusz Łach 00:24:15 Yeah, but that's convey the right message here.
Chris Ventura 00:24:26 I think so.
Mateusz Łach 00:24:27 Okay, yeah, that's all for the issues. I think there are no no discussions matching the criteria.
So it seems like, no new discussions.
Yeah. Okay.
okay, no. New milestones.
What is that? Exactly?
So.
Chris Ventura 00:25:25 That's just making sure we've added things to the project.
Mateusz Łach 00:25:29 Yeah, okay, so this one is not other to the project. I think.
Chris Ventura 00:25:33 Yeah.
Mateusz Łach 00:25:36 Yeah. So, Piotr, you are.
I think you. You were wondering if the recently fixed basically, the recently updated version of of the instrumentation package could could help with this one. So I run a quick smoke test and it did not. It should still exist. So do you want to do. We want to keep the milestone. So basically, the next release.
Piotr Kiełkowicz 00:26:04 I think so.
Mateusz Łach 00:26:06 Hey?
I won't be assigning it yet, because I haven't started working on it yet. So unless there is someone else that might have some time to take a look at it.
Oh, no, we'll keep it so.
Should I assign it to project.
Piotr Kiełkowicz 00:26:29 Yes, please.
Mateusz Łach 00:26:32 Okay.
okay.
And here this is in progress. And this is something that Igor is looking into.
I think Igor is on Pto at the moment, so probably I need to wait for him to get back to to discuss it.
This one is committed.
Yeah, I haven't made any progress here. So no update related to this one.
Yeah, the rest is outlook.
Okay. Is there anything else you'd like to discuss apart from the standard?
Oh, outside of a standard agenda.
Zach Montoya 00:28:05 So for the release. We're just waiting on some testing, and then after that we'll be good to ship that, or are we blocking on the SQL. Clients. Changes.
Piotr Kiełkowicz 00:28:15 I think if the SQL. Client changes will be good. From your perspective, we can include changes. But I would not postpone longer than early next week.
Zach Montoya 00:28:28 Okay, yeah, I'll I'll make sure to review that today.
Piotr Kiełkowicz 00:28:32 Cool. Thank you.
Mateusz Łach 00:28:37 Okay? Yeah. If if there is nothing else, I can go back to the this frequent thread something, and how this could be used in a plugin, basically for for a demo.
Yeah. So I've modified the modified, the the sample from the micro service example.
Yeah. But let me start with the plugin. So basically, what's what this gives us is an option to trigger like a frequent something and this is like trace centric something so Plugin could use it to to to trigger a frequent sampling for selected subset of traces.
So yeah. So there were some questions how to how to track think the issue. So I was thinking about using the using the baggage to store the decision. If to store, if a given trace should be should be marked loud or not, and if it's marked loud, then we want to Do we want to sample it frequently?
So the part in the upstream is basically is this exposes their ability to to start and stop something given thread.
And so we are.
Chris Ventura 00:30:15 Can we pause real? Really quickly if we're storing the decision in baggage?
Yeah. And there's a downstream service that's also using auto instrumentation.
Mateusz Łach 00:30:29 Yeah, then that downstream service would also.
Chris Ventura 00:30:33 Have that frequent sampling triggered potentially because the baggage would be propagated across the wire.
Mateusz Łach 00:30:41 Yeah.
Chris Ventura 00:30:42 Is that desired or.
Mateusz Łach 00:30:49 Yes, that'd be desired So I started working in our plugin. So basically.
Piotr Kiełkowicz 00:30:58 Chris. One more comment here it should work in the similar way, as the sampling decision with always on parent base. Propagator.
Chris Ventura 00:31:13 Okay, yeah, I I just wanted to make sure that we weren't that this needed to be a trace global thing. Or if it was just a like a trace segment, as in just for this one service instance.
and then not the rest of the trace.
Mateusz Łach 00:31:32 Yeah. So the idea was to for it to to be trade, global.
Yeah. So this is so, the changes here will allow us to to start frequent something, and so so the the samples collected will be stored in a buffer similar to to the buffers that we already have for basically always on profiling. So the and so that manage stack sampling and allocation profiling. And then we have, we have a thread on a on a managed site that consumes the buffers. And basically provides the the data rate to the exporters and the plugins supply the exporters, parse the samples and send the data. So this would be the like like high level overview.
So one of the one of the questions raised by Chris was, basically, how we want to handle the asking operations and suspensions and resumes on possibly different threads.
So I was thinking about using the activity changed event. So basically, oh.
we would. We would subscribe to the events. And so this event notifies you about the changes to the activity which which are due to setting the value basically changing the value. But we would also want to be notified about the changes related to thread context changes.
So in order to do that similar to what we already have in always on profiler, we would create like supporting a sync local and set its value.
Whenever the the activity current changed this.
we we get a callback for this one.
And then we would be able to basically track both like like, the direct changes to the activity and also the changes that are for example, due to due to suspensions, and and I think operation and its continuation resuming on on different thread.
So the changes would be so the from the Plugin side that, the changes would be to basically handle this these callbacks. And the idea would be if if the current value is is an activity that we want to track.
And if there is a decision in a context that this is that this is a basically spun from a trace that.
and we want to consider loud. We would start something, and if the context changed and the new activity is is oh, and current baggage is it's not, does not indicate the car, the like the loud span or loud trace. We would stop something.
And this starting and stopping the something is basically oh.
adding, adding current thread id to the list of the threads that we want to sample at the high frequency.
And for the place we will, where we would make a decision.
That would be, probably I. So I was thinking about oh.
so we. So we might use a propagator. But this is this is like, So we basically, we need some place to decide if we want to treat current trace as as allowed or not.
So for the criteria, for the selections for starters I would be using, like selecting the traces uniformly at random.
So basically, this I would add this propagator as a very last propagator. And if there is, if baggage already has a decision. So it was. The decision was made upstream that we would basically honor the decision, and if not, then we would make the decision and add it to the baggage.
So oh, so I have some helper classes. So for now I'm as this is using.
So one of the things is that I wanted to discuss is how to best expose these new methods. So for starting and stopping something. So for now I'm using reflection to call it.
and I'm also using some very simple exporter which parse the samples serializes and writes them to console.
Oh, yeah. So I think that's mostly it. So for the for the tracer. SDK, oh.
so so for the as far as the modifications for the tracer SDK are concerned.
I would add a propagator in a plugin and also So this one. So basically this suspension tracker, we could add it as an instrumentation. So that is properly disposed. When the tracer tracer SDK is is being disposed about this.
there are other options as well.
So yeah, so this. So this is like high level overview of the changes in the Plugin. And this builds on top of the changes from this Pr, so changes from this. Pr.
oh.
basically give us an option. And then we can read the collected samples, and then we use the plugin to make the decision start the decision in in baggage, and also we process the samples by parsing them and and exporting them.
So yeah, in order to. So so for a simple demo, I modified the this micro savers example from the although.net SDK repository.
So I I've added I've modified the compose setup like like slightly. So I've added another like web service, which call. So I I've added another web service which calls the Web Api service, which puts the message on the rabbit Mq. Queue. And then there is a worker service which reads from the queue and processes the message.
So in order to verify the the working of it, I've modified the code slightly.
So so, for example. This I have added some.
I've added some yields in order to force the methods to continue asynchronously and continuation to run asynchronously. And also I've added some slips to basically like, simulate some work. This will block a thread for a for a while, so we'll capture the samples with we'll be able to capture the samples. Basically.
Yeah. So oh, as this is as this requires the baggage to be propagated and set.
I have updated the I updated the the Worker service to use the most recent version of of Ravi, Mq client. And also I've ensured that the baggage is properly extracted and set.
Oh, yeah. So the whole setup is basically just 2 web services. Oh, yeah. So the so the first.st So this service calls the users, like basically the sync version of uses a sync Api from the Http client to call the the other service.
So I have this.
I have this setup running already. So I can oh, basically start processing.
So as a selector as I, the selector for the selector for the, you know.
So basically, in order to decide if we want to treat given trace as loud or not, I'm using the like. This is, basically, we are randomly choosing the traces. So I configured it to.
It was like, yeah, to to take like the 50% of the of the traces so I can also configure the sampling interval to be 100 ms.
And I'm logging the captured samples to console.
So yeah, let me check.
Oh, I also I also placed some like like print statements. So I'm writing to console from from some of this complements in order to to verify what's what's happening. So yeah, let me let me show you the the trace really quickly.
Yeah. So this is the worker service. So this is basically the the component that takes the message of the queue and process it. So the duration is one second at 2020, basically 210 ms, because I placed some slips in there.
And also I place some delay. Let me show you this.
yeah. So similar to the to the other one. So I'm processing the message, and I'm delaying the message here to simulate some work. And then I'm adding a delay, and then then we yield and block up block some more. So let me show you the the samples that were, oh.
that we capture in an export it.
So, as you can see, we captured some samples and there was some.
There were some context changes.
Yeah. And we have some.
You have some more samples collected here.
So we have like.
oh, 6 samples. So.
Yeah. So it's so. We have the call stacks. So the call stacks shows that process message in a receiver and a sleep there. So this is what we have here.
So we sleep here for 500 ms, and we sample with 100 ms interval. So we have, like 1, 2, 3, 4, 5 samples from there.
And then we delay for a half a half a second. So so this is like the last sample. And and this continues, as you can see, there's like over the our second over a half second gap, because we were not sampling at this at this time, and then we we collected additional samples. So this we have like 2 samples here. So and this comes from block after processing methods, which is this one which makes thread go to sleep for 200 ms.
So this is for the for the processor. So oh, and we can also verify them.
We could verify the span context. So yeah. So all. All of these samples were collected for this for this spun id, and for this trace. Id so oh, yeah, so this is for the part processing the message on.
So basically the message processor. And we also. And this is by the way.
this is, by the way, the rabid Mq. Instrumentation, which uses the new semantic conventions for messaging. So the so the spans are correlated using links, and they are not part of the same trace. So we have a reference to spun in another trace. And there's another trace is basically just the span comes from here from the from the message sent.
So for the front end.
Let me take. Let me give you a quick overview of the samples that we collected in the front end front end service.
So yeah.
yeah, so this samples.
Oh.
we collect it from the front end. Serve web front end service. And this web front end service uses the the Sync Api to, and basically blocks waiting for the response from the service.
So response, hmm, yeah. So this one took like 800 ms.
And we have samples indicating basically collected the samples there. So there's Htt clients. And here, so we have like one.
Yeah. So oh, we have like 7 samples.
And we sample with like 100 ms interval. So.
yeah, well, I I think, like, based on, when do you start sample where we example, we we might be missing one sample. So, yeah, it's something with a like a smaller interval would give us a better like resolution. But oh.
all of the samples are basically like 100 ms apart and all of them indicates. So basically, I think the all the call stacks look similar. Look, the same which is expected.
Yeah. So all of the 7 call stacks are exactly the same, because we are basically waiting synchronously for the reasons from the service.
So this is for web front end. And then we have also web. Api.
Oh, so the web Api.
There is a controller which which send them sends a message. So again sleep. There is yield.
and then we send a message, and when sending the message we sleep some more. So let me verify. This is what our samples show at the moment.
Yeah. So we have like one sample from like from framework code.
And then we have a sleep from a send message controller.
another sleep from send message controller.
So yeah, so we have like 3 sleeps. So we have like 100 ms. So we are sleeping for approximately like, yeah, 300 ms. Let me quickly verify that.
Yeah. So we were, we were able to collect 3 samples here and then additional samples come from the rest of the sent message method. And we have like 2 samples from from there. And this is yeah. So this through.
Yeah. So we have also the sleep from in insights and message here captured as well.
Oh, yes. So, oh, yeah. So this is basically like.
this shows that we are collecting the expected samples, and also that we are not collecting the samples when a thread is not blocked, because when we had a task delay.
and Fred was not blocked, and we were not collecting the samples for half a half a second. Sorry for half 500 ms, so that there is like bigger gap between the samples there.
And yeah, as you can see, this is like 600 ms.
Oh, oh, oh.
yeah. So go ahead.
Chris Ventura 00:52:25 Yeah, I got a couple of questions. So one is.
let's say, somebody customizes the propagators and disables baggage propagation. It will. The additional propagator that you added, ensure that that piece of the baggage gets propagated.
Mateusz Łach 00:52:53 Yeah, so oh.
how how like, how often do you think? That's how often do you? Because of like baggage propagator. It's like default setting right part of the default settings is the SDK, so do you expect this to be common case for someone to remove the baggage propagator?
Chris Ventura 00:53:15 I would think somebody would have to go out of their way to say that I only want to support B. 3 propagation.
and then they forget to add baggage or something like that that that's kind of what I'm imagining.
Mateusz Łach 00:53:30 Okay.
Chris Ventura 00:53:33 And and I'm this is something that we could handle either via Docu documentation.
Or if it's common enough, maybe we look into a code based solution.
It's just a thought.
Mateusz Łach 00:53:51 Yeah, sure. So, as I said, I think we could so basically check the configured propagators before we try to add it like, add the new propagator in Plugin, right? So basically like, inspect the configuration before trying to modify it.
Oh.
Chris Ventura 00:54:08 Yeah, otherwise, we would have to rely on something like W. 3 C. Trace state.
or at least the trace state header in order to pass something similar along. But then, once again, they could decide that they don't want to use the W. 3 C. Trace context and use a different propagation. So we're kind of back to the same problem. So it's just some thoughts there and then. The other question I have is so so my assumption with how this is working is on the native side.
Yeah, we have a timer. That's that's basically going to take basically pause the runtime and do all of the stack walks for all of the threads at that frequent rate.
Mateusz Łach 00:55:04 Oh, so not not all, not for all of the threads. We are only.
Chris Ventura 00:55:08 Yeah.
Mateusz Łach 00:55:09 For for the frequent something we are only we have like a separate list that we add to and remove from. And if there is like, if this is empty, we don't pause the the runtime at all. But yeah, so on the on this more frequent interval. We only work the stacks of the threads that are in the list. So not not like all of the threads.
Chris Ventura 00:55:31 Okay, yeah. So so if there's no threads in the list at that frequent time, then we don't pause the Runtime. But if there is.
then we still have to pause the entire runtime to to do the stack walks. But then we're just grabbing the data from those threads to to make it faster. Okay.
Mateusz Łach 00:55:54 Yeah.
Chris Ventura 00:55:55 So it's not like you have to do the stack walk of every thread for.
Mateusz Łach 00:55:58 No, no.
Chris Ventura 00:55:59 Was, okay.
Mateusz Łach 00:56:00 Yeah, yeah. So yeah. So yeah, that's that's a good point. And also the point that you raised in the past. So for now, the code responsible for resolving the symbols is basically we do it inside the Runtime suspension. So it it wasn't that much of a issue for us before, because we were expecting continuous profiling to be configured with like high frequency. I think the default is like 10 seconds in our distribution.
But if we want to. So for this frequency, something we want to use much higher frequency. So the overhead of resolving the symbols is much more like.
I think it's much more important in this case. So, as we, I think, as we discussed already, we should look into moving, the resolving the symbols outside of the suspension. But this is like a follow up for the Pr that I've created. Yeah, because, yeah.
so yeah. And also, I've run some very simple, like.
very, very, very simple test. So it seems like the so the the suspensions pro plus resolving the symbols. It was, usually around. How millisecond? I think so. And it was like the resolving symbols. Part was like a significant part of it. So moving it outside of the suspension should like help here. So.
Chris Ventura 00:57:47 Are there scenarios where we think that somebody wouldn't want the whole trace affected by the frequent sampling.
I'm just thinking of a situation where you got an upstream service and a downstream service.
and they're managed by different teams.
Mateusz Łach 00:58:10 Okay.
But the upstream service is trying to investigate a particular issue. So they decide to enable frequent sampling.
Yeah, so.
Chris Ventura 00:58:22 If that triggers the downstream service, which is maybe a high throughput service, can that cause an overload of that downstream service which is maintained by a separate team.
And I'm asking this question in case we need some sort of setting to to, perhaps not enable the propagation.
Mateusz Łach 00:58:49 Okay, yeah. So for for starters, for the, for the simple version of it, we we expect to to be it to be used like across the trace. So for all of the services. But yeah, so that definitely, there's a I like like a good idea. So that you know.
yeah. So this is, that's a very good idea. Let me look into that, or maybe just even create some like issue to to investigate how to best handle it. Future.
Chris Ventura 00:59:21 Yeah, yeah, I'm not saying we need to to solve it now. But it's just something to consider.
Mateusz Łach 00:59:26 Sure.
Okay, are there any other questions?
Yeah. So I think I'll I'll clean up the code that I have in Plugin, and I'll probably create a Pr. Even in, even if draft in our distribution and link to it from the Pr. That we have in our repository.
and that might be like that might also like oh.
serve as a as a some example. And I'm not sure if there is like recommendation, how how to how? What would be the best way to move forward with trying to yeah, to trying basically to to oh.
have this like, ready to be reviewed and open like, ready to to like receive feedback. I think so.
Yeah, I I've I've updated the description few times. So basically, I think there are some parts that I definitely like to add. And also there was some good early feedback from your gaining and ft car. So I think the like.
the main question for me would be, if we are. If we are okay with with going forward with this one what would be the like? The seek recommendation how to best expose the feature? Because for now I'm using some like.
I'm using reflection, and I'm using some hacks, but I was wondering what would be like the recommended way to to enable it, or basically to expose it.
Yeah. So if you could give it some thought, and so any recommendations would be very hopeful.
Chris Ventura 01:01:37 Yeah, you you might even be able to just create an issue for that piece to to start a discussion.
Mateusz Łach 01:01:44 Okay.
Chris Ventura 01:01:45 For that, because it feels separate enough from this Pr.
But still necessary for the feature.
Mateusz Łach 01:01:52 Sure. Yeah. So we to give like a brief description. So I I try to describe the approach that I've taken here. The approach is like simply in order for, or have to, in order for us to have something working. But at the same time I try to cover the like cover. It's working with tests. I I know there are some tests missing. There might be some like duplication, or we might to optimize some parts of the code. But yeah, I think like, this is like ready to be reviewed. And I tried to reuse as much of the continuous profiler code as possible. So I, I modified some of the continuous profiler code, so probably we we could. I I should rename some stuff or stuff, or do some like clean up. So I can definitely do this in this, in either this Pr or A or like, follow up. Pr, yeah. But from the thing I I think from the things that we I would like to like tackle if this was to be merged. The next thing I would like to tackle would be definitely Co, better test coverage for the native code. And yeah, and trying to move the the symbols, resolving outside of the suspension, because this is this is costly. And this is definitely something that's that's critical to it is critical for us to to like, minimize the time spent when the runtime suspended so.
Chris Ventura 01:03:28 Yeah, I say, go ahead and submit issues for those follow up things so that we can keep this Pr smaller.
And then this this way we have an idea of all the things that we want to do as part of completing this feature.
Mateusz Łach 01:03:46 Okay.
so I think that's that's all from my side. Thanks a lot. By the way, Chris, for for the feedback.
Oh, I don't know if there's anything else that she could like to discuss at this time, or I think we are over time. Thanks for staying on car. By the way.
if not, thank you.
Piotr Kiełkowicz 01:04:13 Thank you. See you. Next week.
