SIG: Arrow SIG
Date: 2026-03-24
Duration: 63 minutes
============================================================

## Zoom Recording Transcript

Albert Lockett 00:00:26 Hey, guys.
Utkarsh 00:00:35 Albert, Niger can't.
Gokhan Uslu 00:00:43 Hello, hello?
Laurent Querel 00:01:10 I would win.
Joey 00:01:15 Hello.
Laurent Querel 00:01:17 Yeah, June.
We will wait a little bit. I think, Joshua will join, and probably a few other… books on Microsoft.
In between, I will, share… the Google Doc that we… we use.
Okay, so… A little bit of, work to… prepare the… to prepare the meeting, so we are March 24.
Okay, that's the general meeting we have today.
But yeah.
So myself, Jake, is not there. Albert is there, Utkarch is there.
Max, no… Oh, and… No.
Andres, Drew, no.
European waste. Okay, Good thing, what I lack here is… So, Drew, I'm adding you as… So, a demo for the… Remove for the, oh, benchmark, UI… We have also, Part 3 Barring… Yeah, I think that this, on… this one.
I think we want to talk about that.
It was the title of Unified Internal.
unified internal… Good in between… Around the OTAP pipeline.
I care.
And guys, feel free to add some additional, Some additional elements into the agenda.
Hi, Josh. Do you have any topic to add into the agenda?
jmacdonald 00:04:47 I don't. I was just looking over the new issues, and I think the triage might take a minute. There are some ones to talk about there, but.
Laurent Querel 00:04:54 Yeah.
jmacdonald 00:04:55 I think you've, called out the important one. 2405 covers a lot of that, and I do have some related conversation. I filed one new one under the same category about exponential histograms, so I think we should start.
Laurent Querel 00:05:10 Yeah? Do you want to talk about the triage, or you want me to do it?
jmacdonald 00:05:15 Well, I can… I can talk through it.
Laurent Querel 00:05:18 Yes, okay.
jmacdonald 00:05:19 where the dividing line was. Last Thursday, so it's a shorter period since the last meeting than the other week, I think we talked about Jake's issue about time zone designation last week, as well as abstract runtime.
I may or may not have filed the issue about duplicate and redundant metrics, but now that we have channel instrumentation, I want to, like, go through many of the nodes that we have. We're instrumented before we had standard metrics, and now it's time to sort of clean that up.
Do you… Laurent Querel 00:05:51 Do you want to share the… jmacdonald 00:05:54 Oh yeah, sorry, I will share.
So I'm sort of running backwards from this list of 20 or so. I wanted to remove some metrics, and now that we have these producer, consumer, success, failed, and refused metrics across the board, we don't need as many of the instrumentation points that we have in the existing notes. No big deal.
And, let's see, what?
So, going back as far as this last week, there had been a question about ACMAC handling, and I filed an issue, about a couple of the issues in my PR that merged.
If you recall, that was the one that introduced this metric stuff. So, I noticed while I was implementing that there's a sort of unsafe interface. We have this method called Route ACK and Routen Act. You're not supposed to use it, but if you do, it'll just work, but you won't get the correct instrumentation.
So I filed a couple things at that level. This one here is a bug report. I have an open PR about it, and it took me a minute to convince myself it was correct, but… but the current behavior is a little bit, difficult for new users. Like, you have to fill in all the levels of the policy currently for it to work, and otherwise you get confusing results.
I noticed that I couldn't get my Prometheus metrics that I had just merged, so that's how I figured it out.
Laurent Querel 00:07:19 So you already fixed this one, right?
jmacdonald 00:07:22 I haven't merged my PR yet. There was a request.
Laurent Querel 00:07:24 Oh, okay, okay, but that's the one we… I already reviewed this.
jmacdonald 00:07:27 Yeah, but I wanted to document what was being fixed.
Laurent Querel 00:07:30 So it's already decided, in that case. I think, triage deciding.
jmacdonald 00:07:34 Yes, let's get that one. So we can go through this, correct, sorry, I forget we're supposed to, in real time, update these labels. Would someone else like to update the labels as we go?
Laurent Querel 00:07:45 Yeah. Okay. Can probably do it.
jmacdonald 00:07:47 Albert filed one about further optimizing, And this might already have a PR open… Albert Lockett 00:07:56 No, it doesn't… this is a… this is kind of like a performance, thing for posterity, basically, like, in the column recovery engine, when we're, doing something that's, like, setting a value, like, setting an attribute or setting a column value, we try to coalesce them, into, like, the same pipeline stage, so we only need to.
produce a record batch or an OTAP batch, like, for… we, like, if we can coalesce the assignments, then we need to produce fewer materialized batches, effectively. And so we have some basic logic in there now that can, coalesce all these assignments into one, pipeline stage, but, it's not very advanced, it's not very sophisticated, and so the idea was just to say, hey, you know what, like, there are some additional things we can do here, it's… it's just… and so I wanted to basically, like, document that, just so we don't, like, forget about it.
Laurent Querel 00:09:02 Okay, so it's not top priority, but.
Albert Lockett 00:09:05 Yeah, not in top priority.
jmacdonald 00:09:09 All right, and then… and then comes the long, list that Laurent posted. We're going to have a dedicated section, I think, to talk about 2405 all the way through… well, 2412, which is all about internal telemetry. If I go digging, I can find a few that I've filed myself on some of our requirements, and we were also planning as a requirement, to get the internal metrics pipeline onto the data flow engine. So some of these things cross over. So that'll be its own topic, I think.
And then… so then, there's gonna be an issue where we talk about your large PR, the AC redesign, or the sort of upgrade. I think this orchestrates shutdown is about that, and we have discovered, sort of, like, there's a… it's not quite complete with regards to clean shutdown, as far as I understand.
So that's what this one's about.
Laurent Querel 00:10:05 Yes.
jmacdonald 00:10:06 Okay, all right. We'll get to that then. Metrics temporal reaggregation, I know a little bit about this. Jake, do you want to tell us?
Jake's here, maybe?
Jake Dern 00:10:19 Sorry, I was muted.
Laurent Querel 00:10:19 Sure, here we go, we'll fix this.
Jake Dern 00:10:21 You're probably more familiar than me, but there's this interval processor over on the Go collector side, and they do some temporal reaggregation with some limitations. They don't support all metrics, they only do cumulative ones.
There's, like, a table and a list there. Basically, we are looking to kind of add the same.
jmacdonald 00:10:44 Cool. I'm familiar with it. This is an opportunity to nerd out about the hotel metrics data model, and we shouldn't do it here. I'm also aware that this component is the one, or node, is one that people optionally look for storage extensions to be used, so not only do you want to store your metrics, you want to store your metrics going back 3 hours, or whatever. And I've seen that, so I know that there's at least someone looking at it, if not already being done in this component, with Pebble, the RoxDB thing.
Very cool.
So there we are, down… so then, a little bit more, we're still having some issues. We're going to discuss shutdown and drain.
Lowett has defined, design, filed an issue about process-wide memory and OOM prevention.
I don't know if Lalit's on the call, and I don't know specifics about the request, but I can say that this is definitely the first extension in the collector after auth was Memory Limiter.
And that's based on the Go Garbage collection stats, but I think, Laurent, you might have some ideas about how to do Process-wide memory limits.
Laurent Querel 00:11:58 Oh, okay, process-wide, I think, yeah, process-wide will be interesting, but also pipeline level will be interesting.
Because of the model that we have.
We, we, we are, in fact.
In my opinion, obviously, the process level will be, like, the last, The last barrier, that we… we could implement, But a limiter… a memory limiter at the pipeline instance level would be great, also.
In addition to that.
I didn't read precisely this, this thing, but I definitively agree with the overall.
jmacdonald 00:12:42 Yeah, that sounds… Laurent Querel 00:12:43 Jordan, yeah.
jmacdonald 00:12:44 As well, I, so we'll redo that. I think we want… we've talked about NUMA-aware memory logic as well, so that would be, like, as you say, after that, we get to go.
Laurent Querel 00:12:55 Yeah, we have an interaction with, also with the memory allocator that we use.
That is already instrumented to measure The memory usage. That could be used, as a way to To basically, capture the current memory usage.
And, and determine, when we are close to the limit, and then, Sending a signal to the receiver, maybe to, To limit the incoming traffic, or something like that.
jmacdonald 00:13:30 Yeah, that's great. Let's talk about that after this long list of agenda items that we have here today.
I see one more about, well, complicated stuff.
Here, Laurent, from you.
Bound completion dispatcher pending sends, is that right up?
Laurent Querel 00:13:50 That's a reaction to… it's basically, follow-up, to track, the… the values, some, not all. Some of the, the comments, we had… I had on the ICMAC, gigantic PR.
So there are some, some comments I'm addressing directly, and some others that I think, will be better to address into a follow-up PR, because it's already a better situation right now, and we know that, yes, I agree, there are some elements that we could improve.
One of them, for example, is the fact that we have an unbounded, data structure.
We definitely want to get rid of that, but I don't want to increase again the size of this PR, it starts to be, Could be you.
jmacdonald 00:14:44 We'll talk about that. I know that the delay data queue is also unbounded.
Laurent Querel 00:14:49 Yeah, I didn't add the corresponding stuff into the GitHub issue, but yeah, we could.
jmacdonald 00:14:56 Suppose we skip these two that were filed after the start of the meeting, including my own and Albert's. So then… We can talk about them next time.
Then, I would propose, to hand over to Joe for the demo that, that we're going to see.
Laurent Querel 00:15:13 Nice. So maybe just a quick introduction for that, and I will let Joe, to the duo, So, so Blue is working in the FF team.
And, I asked Joe, basically, to, to work on an interactive benchmark UI in order to compare our Rust Dataflow engine.
Perth with the Go Collector, and we could extend the system to compare it with some other solution, if we want.
So the… so, regard… in comparison with the current continuous benchmark infrastructure, or the nightly system that we have.
The goal here is really to compare solutions, not just us.
Over the time. It's to compare for a specific release, okay, how we behave for various scenarios in comparison with other solutions, and, with different variation, batch size, throughput and so on, and people can basically interact with the UI. So that's what Joe will demonstrate.
Joey 00:16:23 Thanks a lot.
I'll go ahead and share my… My screen here, make sure everybody can see that.
Laurent Querel 00:16:32 Okay.
Joey 00:16:33 Okay, cool. Yeah, so effectively, like LeBron is saying, what we're trying to do is just capture the benchmark performances between, what I'll refer to as components, but effectively the different style of, collectors. And then, in the comparison aspect of it, I am starting with an apples-to-apples. I do… I did have a concept of doing a characteristics comparison, so as an example, you know.
compared VZIP versus ZStandard, or something like that, and that might just come down to a filtering exercise, but effectively, what we're seeing here is we're running these 9 different scenarios. These are our main metrics. We do have more metrics that actually show, as far as log throughput and And things like that that you'll see when we do the pop-up, and then we have the ability to filter on certain of the… the characteristics for the run, like Laurent was mentioning, so how many… however many laws we want to try to push through, what the batch particular sizes are, what compressions we particularly use, and then the duration, is one of the other ones. So… Some of the… and you guys can stop me at any point, I'll take, feedback and criticisms and, and all that fun stuff. The main… you guys can see the pop-up, right?
jmacdonald 00:17:47 Yep.
Joey 00:17:48 Okay. So, you know, the main thing that I think most of the conversions usually look at is CPU and memory. The… if you weren't necessarily saying, we start out with just the CPU average, and then we can kind of click through.
The different ones, but if you wanted to particular… take a particular run.
You'd want to come in here, and so right on this one, we're looking at the OTAP that is filtered, and then, ingress is OTAP out. There's a filter process, that's established, and then there's OTLP that's out. And so, if we want to look at all the characteristics, or all the metrics for that particular scenario, we can go into this.
This is a, This is an implementation that's still in work. I continue to iterate, and Laurent and I work over the UI, but a lot of the things that I was coming across was sometimes inconsistencies in data, so I do want to be very data integrity intense.
So I've put additions in here as far as, like, what the scenario details were from a configuration standpoint, so these are all configurable. You know, you can tell that you want it to run for 5 minutes, you can tell if you want to run at 300K, all these different things. It'll actually tell you what the initialized configuration was for the component. So, in this case, this config would be the benchmark, and then this is the DF engine.
That… it should load. And then, ultimately, the, the low gen. We show some of the raw metrics. So far, I do want to have simple math, because we do give you a nice little description of what this log flow particular meaning means, and so on. Obviously, the other metrics are sort of self-explanatory, with the exception of these drop logs and log deviations.
But I do want to work into what the actual math and how we're rendering these, where these are coming from. And because we're in the selected CPU average, that's what this is going to be. So if we were to come back out, and we were to look at the memory average or something like that, and we come back in here, the rural CPU will be the mem.
And so it's just kind of specifically for the metric that we're selecting, or that we're viewing.
And then I am… I'm creating these additions, for an admin situation to where we can sort of purge particular runs. We do want to keep, you know, a good amount of data over time for historical purposes, as Laurent was mentioning, sort of like the nightly bills or the, you know, continuous integrations, where if we have a deviation, okay, maybe we can go back to that particular run and see that, or we can mark it as being invalid.
And then you have the capabilities of exporting all of the raw data that goes on behind to generate all of the data that we're looking at.
So that's a pretty massive JSON object right now. I don't know about shrinking that down, but we can look into that.
And then as I continue to go on, you'll pay… you'll see the… the, the advantages that we're looking at over here, as far as, like, you know, how the comparisons are between these two different collectors. As Laurent said, we're going to add FluentD and then other collectors as it goes. It's very easy to see the call out on the memory… excuse me, the CPU average performance of which one's better.
And then, one of the last things that I'm working on is to add in the historical charts. So, anything over time, we can go and we can dig into it, and again, see what the differences are over time.
I'll stop right here, see if you guys have any comments or questions. Feedback.
jmacdonald 00:21:18 Very cool. Very cool.
Joey 00:21:20 Alright.
Rock, did you want to explain or discuss anything further?
Laurent Querel 00:21:26 No, I think it's really cool, I mean, I'm super happy with that. I think that will help, us a lot to position the… What we are doing in this project.
the data that we have, we have here, I'm sure that we, we, we still have inconsistencies, and we, we need to really, double, triple validate the data. I want to make sure that we are fair for the system that we are comparing.
But, the exercise here is more how… what kind of UI we need to put in place To make those comparisons super straightforward, and, where… where people can really, very… quickly capture what matters for them. And we know, depending on the scenario, sometimes it's CPU, sometimes it's memory, both of them, or maybe they want to optimize the traffic, or that's why we have the network transmit, receive, rates.
And they will be able to see, it's not only a comparison, basically, between Collector-like system, but also between, protocols. So right now, we have scenarios with OTLP and OTAP. We could imagine that let's say we have the Go Collector that is already supporting staff, We could add the staff We will not have a comparison with the Rust collector, because the Rust Collector does not support Ceph yet.
But at least it will be interesting if you select the metric network, we will see the difference between the two, and we will also see the impact on the memory and the CPU usage. So that will give to future users of the system A good understanding on the trade-off.
okay, maybe staff is better for the compression ride, but you pursue more safety usage, this kind of stuff. So that's the goal behind this UI. That we… I'd like to put directly accessible directly from the… the main, README page at some point.
jmacdonald 00:23:52 This is very good. What would happen if you clicked on one of the OTAP filter and OTLP filter? Like, can we compare the protocols here and now?
Joey 00:24:01 Yeah, so as it… so I put the latest run up at the top just because I'm working through these, purging out old data, so I wanted to make sure that I had the cleanest runs up at the top, but you can see that, that this run is ultimately right here. So, if you're looking at just one particular filter, you have the ability to do the comparisons across the, Across the different, components.
Laurent Querel 00:24:26 What, what, what, was, seen.
Joey 00:24:28 Yeah.
Across different protocols right now.
Laurent Querel 00:24:31 Yes, so having… having the ability to select multiple scenarios, I think that's what… that's what will be done. Oh, it's already supported. Nice.
Joey 00:24:42 I can… I can do multiple… yeah, that's supported as far as the scenarios, but these are hard-coded. If you wanted to take something specific and compare the two, then that's… that's where we can't do it at, but we can.
Laurent Querel 00:24:52 Yeah, true.
Joey 00:24:53 American.
So, like, if you were to do… Laurent Querel 00:24:55 We will have OTAP to OTAP and OTLP to OTLP, and then that will compare, yeah, native OTLP or native OTAP scenarios. That's nice. And with, like, the transmission, for the compression rate, metric, and that will give us the right answer. Okay, sounds good.
Joey 00:25:16 Yup.
Cool. And the intent is to not… I know that logs are the primary on the current benchmark, but I do intend on going and putting metrics and traces.
Laurent Querel 00:25:31 Excellent.
Joey 00:25:32 Cool, thank you.
jmacdonald 00:25:34 Very good.
All right, well, I will represent the notes we were in, here we are, and Gosh, I think the next thing we should do is… Well, looking at the time, I do want to make sure that we talk about all those deadlock-related control flow issues, and I… and I think we should put that on the agenda next. But perhaps we could walk through the topic of internal plummetry, just since you've filed 9 new issues.
Laurent Querel 00:26:08 Yep.
So maybe we can open the… The 2425… no, sorry, not 24-25. 2405.
Yeah, that's the umbrella stuff.
jmacdonald 00:26:24 There we are.
Laurent Querel 00:26:25 Yeah, so the… So we, we already started, I think we started this work, two months ago, something like that, because we, we observed that we, The initial, status slash metric endpoint that is exposed by the admin, Subsystem.
Was not really, I mean, it was, like, an ad hoc solution.
To… to help us troubleshoot the first version of this engine. And then, we… we started to add, an integration with the Rust Hotel Collector.
But the Ross Hotel Connector… jmacdonald 00:27:09 Intel SDK.
Laurent Querel 00:27:10 Yes, sorry, there was total SDK, sorry.
But, we have some limitation there, because we can't support OTLP and OTAP, we can just support OTLP. We… we can't leverage the processing component that the pipeline system is already able to support. So the goal really is Reusing the internal… reusing the pipeline engine that we use already and support.
For internal telemetry.
And that's the end goal. And, and basically, this unified internal, telemetry, umbrella, issue is, is talking about how we can achieve that, the, the values, intermediary step. So maybe I will share my screen, that will be easier for me, virtual.
jmacdonald 00:28:05 Sure.
Stop. There we go.
Laurent Querel 00:28:11 Yeah, sweet.
Okay.
Yeah, so… I'm just listing and describing, I think in the logical order, what we need to achieve to finalize this goal, basically.
So the… the first one is something that we… we started here and there in different occasions. It's, we… we already have in the project I can show you the… the document… So, if you look inside Rust, you have this, doc… telemetry. Here, we have a collection of guidelines.
That we wrote, a few months ago.
And it's talking about, the entity model, naming convention for signal, metric, event, and so on.
So we, we… We try to be aligned with that, but definitively, we are not exactly, there yet, and we need to, review all the event metric logs, and making sure that we comply with this, uniformed, with this set of guidelines.
And, and we also have some, metrics, or even that are, duplicated, either at the node level, and they are duplicate of what is already generic, generically, and automatically instrumented at the engine level, so we need to deduplicate things. So that's the goal of this 2406.
Then, this one is… So… We, we have, before being able to move the… The slash matrix and slash status and perm that already exists today.
That we… we use, not only for the UI, but we can also use for the… the ELS endpoints, when we deploy on Kubernetes, they are very important endpoints to make sure that the pod is up and Kubernetes can do its thing.
So we need to keep that healthy and working, but in order to move those endpoints and expose them as spatial exporter into the internal telemetry pipeline.
We need to do a few, but to create new exporters, that doesn't exist yet.
But, what I was thinking is… We need to improve a little bit more the status, even before being able to do this migration, so that's the purpose of this 2407.
is… with the PR that is, not yet moved, the one I created, last week.
We have a collection of metrics that should help us troubleshoot liveness issues.
And… Usually, those slugness metrics, they need to be combined together, or they need to be observed over the time in order to generate useful, let's say, engine-level event that could be exposed into the status endpoint. So the goal of this detector-based solution is to To complement the existing admin endpoints with this concept of detector, To, generate derived events.
That will help us determine if the system is in a good health or not, based on those likeness-oriented metrics.
I think it's more urgent to do that than to move everything into the internal pipeline, and that's why I put this one in the second position.
Then, we… what I'm proposing here, is… Starting to expose the internal metric.
To this, internal pipeline system.
But the limit that we have here is… Internally, we use metric set to multivariate metrics for efficiency, and also for, It's infinitely better, in my opinion, to have a collection of metrics already attached to an entity.
So we don't have to do, join, complex join, to retrieve the correlated matrix.
They are already there, all together.
But it's not supported by OTLP.
And not also supported completely by OTAP. So the first step here will be To export those multivariate metrics, we can convert them into univariate matrix. That's super easy. We take one metric after the other, and we duplicate the same attribute set That represents the entity, set of attributes.
And then we… we can basically mechanically, generate, those metrics from the metric set, and then we can export them with OTLP and OTAP.
pure step.
And, so that's the… this bridge internal metric set, blah blah blah.
Then, at this point, I think we can remove the, the direct, for the open telemetry Client SDK, metric pass.
That is basically doing already this conversion metric set to univariate.
But, we could do it by leveraging the internal pipeline once this, This, task is, is, is achieved.
So that's the… clean up the system, removing the OpenTelemetry Clunt SDK. That will also… remove, I think that… that was Lalit mentioning, sorry if it's not the right, person, but, yeah, I remember Lalit mentioning that we need to… B… FIPS compliant, and we have we had two issues to be fully FIPS compliant. Weaver was one of them, but now there is a feature flag that is present, and we can basically disable this dependency.
And the last one was… jmacdonald 00:35:23 with the OTL SDK, you're saying. I've seen that as well.
Laurent Querel 00:35:26 Yes, so, so by removing the client SDK, we will basically finalize entirely the… the FIPS compliance, because we will no longer have… we could basically generate a binary without any, Non-compliant, TLS, library, or crypto library.
jmacdonald 00:35:50 I would say that's not the reason for us to drop the OTel SDK.
Laurent Querel 00:35:53 No, that's.
jmacdonald 00:35:54 Shouldn't be hot out.
feelings either. It's really that we're building the most appropriate SDK for this engine.
Laurent Querel 00:36:00 Yeah.
jmacdonald 00:36:00 There's another issue felt about it. I've started attaching some of the ones that I know that are… but please continue.
Laurent Querel 00:36:06 Yeah, yeah, I agree, it's not the only one. I don't know why I just mentioned that, but it was, like, An indirect outcome.
So… Once we are there, we can start to… to create, A new type of exporter that will basically expose the HTTP and PUB status, Regis and Leipzi.
And they will maintain this observed state that we have currently into the admin. So, same logic, but, we, exposed as, A stateful exporter.
That, that will basically export those, those, endpoints.
And, Obviously, that will be special exporter that we will use only for this internal pipeline system. They are not really general-oriented, at least at this point.
The next is… I think this one will not happen soon, but, I see those two last… step in the process. Maybe we should, create a second, high-level, Issue, because this one is, okay, how can we support natively multivariate metric, or metric set?
into a tab.
That will require some extension to the existing OTAP model.
And once we are there, then we can remove, the, the translation, the automatic translation from multivariate metric set to univariate, and we can go, multivariate end-to-end. That will be, real benefits in terms of transport and data processing, but that will require an extension of the existing OTAP data model.
And once we are there, then we can, Finalize the… we can remove the code that we have into the admin.
For the metric aggregation, the detector that has been introduced in the second step.
the Prometus, exporter and so on, and, and, and create them as… dedicated node into this internal pipeline, but that will require the support of MIT via the metric set.
jmacdonald 00:38:45 So, to wrap the whole story up, for example, you could… you could wish for a detector, which might be, like, the average utilization or CPU utilization across my whole engine, and originally, early on, you would compute that directly from the instrumentation stream coming into the, kind of, state observer. Your eventual goal is that we might produce OTAP and then have OTAP logic computing the derived averages, for example, this all sounds very good to me.
Laurent Querel 00:39:13 Yep.
That's definitely the goal.
Yeah, I don't want to… I try to find the most rational approach.
So delivering the value first, so the detector will bring a lot of value for us in order to troubleshoot efficiently, likeness issues, and we could imagine reusing the same detector logic for other things. So that in place will basically help you or us, for example, to deploy this system on Kubernetes, and, And making sure that the live Z release is… is… is based on potentially complex, logic detection. And, And that's the most urgent part. And then, to be very clean and nice, we will progressively migrate this complex logic into a regular pipeline. That's the G behind it.
jmacdonald 00:40:17 Alright, that's the end of the, of, of the, new telemetry issues, I would say. I found one myself about exponential histograms.
Which has to come after we get rid of the client SDK for reasons. You know, there's no direct way to instrument histogram data into the API of OpenTelemetry. So there's reasons why we are iterating and designing new APIs here, that I'm seeing, at least.
I've also filed some issues. I will continue filing issues. At the bottom of 1905, I listed some about the exponential histogram. I think, given what I'm hearing, there's an appetite for thinking about distributions. I'm interested in OpenTelemetry, like, working on the gauge histogram, for example.
There's also work on sampling and tracing that's implied, like, for an OpenTelemetry project. We'd like to be able to trace the data flow engine, that'd be cool, but it's not a priority. So lots of things come to mind when I think about what we could do. And it was also a Slack conversation that some of us have had recently in the AeroDev channel, which is about, as we begin to deduplicate the metrics, you'll note that some of the nodes have, like, per-signal metric counters, like, how many logs did I receive? How many metrics did I receive? How many… whatever did I receive? And there's a question about how we might get to attributes instead for, like, for signal type, for example, which is how an OpenTelemetry user might do it. So you can have a counter, which is all the things consumed, and then you can add dimensions, like signal type. So you still have a counter, you can sub… you can have sub-sums of that counter tell you something about each signal, but then you can just collapse that signal attribute, come back to the same counter that you could have had in the beginning.
And this lets us mix agri… mix the detail of our metric instrumentation. So, I would like to get us there, and that involves, like.
I'm not quite sure what, but we don't want to lose the properties we have, you know, that you're just counting… you just… when you have a counter, you're just incrementing a counter.
And so, this is somehow being able to add the additional dimension. Instead of having one counter, we might have three counters, and when they come out as univariate metrics, we're going to have an attribute. When it comes out as multivariate metrics, I think we're going to have three columns.
And that's a topic for the future.
Laurent Querel 00:42:44 Nope.
Any, if you see any additional, or if you see any missing, important aspects behind this, overall goal, feel free to… To add some comment there.
If you have any questions on those ones, don't hesitate.
Otherwise, we can move to a different topic.
jmacdonald 00:43:14 So, my goal, for the agenda, the next item would be for us to talk about the large PR, we've been saying… calling it that, but it's an ACNAC refinement, I'll call it, and I've… I've read it. It's a long PR, but I have read it, and My goal is that we get it merged, and any discussion that we could have now would be good to have.
And then I know that we need to limit the size of this. We can't just keep doing work in this PR, so I want to figure out how we merge it, and then admit that it's not quite done, that there's more work on graceful Shutdown.
And that you've even talked a little bit about, you know, like, formal verification that we might be able to do, on our system.
Laurent Querel 00:43:56 Yeah, with that. Okay, So, I can go over the various comments, and for some of them, I either provided an answer.
or a follow-up GitHub issue. So, for example, for this one, I created this one, so this one was attached to the previous list.
But I didn't talk about it.
So, once we… we have this internal, telemetry pipeline system.
And in general, when we have… since we introduced the… the topic.
So, we need to figure out what is the… let's say we want to shut down the entire system.
So when we shut down a pipeline.
We know that we have to shut down first the receivers, and there is a propagation that is in place.
coming… going from the receivers to the exporters. So that's what we have in place. But if we go a level up, and we consider multiple pipelines, and we shut down the entire system, and those pipelines are, for some of them, connected through topics.
Then we have a chain of dependency.
We have ingress pipeline, and we have egress pipeline, maybe something in between.
And we have to apply the same kind of logic.
the ingress… Pipeline need to be shut down first.
And and so the… The system-level observability pipeline should be the last one that we shut down, because that's the one receiving all the internal telemetry.
Of pipeline that we shut down.
And then, the last one is the, system-level observability pipeline. But it's… if we… if we, use the topic system generically.
To connect the system-level observability pipeline with the rest of the other pipeline.
Creating this logic of analyzing the topology, and the dependencies between pipelines across topics, through the topic.
We… we will get… Naturally, this, dependency chain, and obviously this one will be shut down last, because that's the one that is used by every pipeline.
So that's what I'm explaining there. We are definitely not yet there. We could, just create, to begin with, an internal rule saying, oh, this one will be shut down last.
And I think at some point, we will be able to make a generic version of that, that will be… Yeah, just the result of what we will do anyway.
So obviously, it's, it's, a lot of work, so, I, I, I didn't, It was an easy choice to just create a follow-up product.
jmacdonald 00:47:08 That's fine, that's great, actually.
Laurent Querel 00:47:09 Yeah, sorry, I picked, my mistake. So, next.
Or the dirty, I didn't answer yet this one, but… so basically, behind this one, it's because the… In the control plane matrix the, the s… I'm still not sure if… so basically, the answer right now is I'm not using the metric set system to maintain the state of the control plane. And the metrics are derived from this state.
So, basically, I'm creating on the fly the matrix set and the snapshot.
And the way that they are integrated with the rest is not exactly equivalent to the way that it's done for the node, because it's a very low-level component.
So, most likely, I will keep the… this design right now. Maybe at some point we could make that a little bit more generic.
Oh… Yeah, so there is, a follow-up, there is another comment around that, and we… I already, follow the recommendation from Woodcarch regarding this one. We will go back there.
Yeah, the, the costume budget, so… I provided an explanation there, why we need that.
Would be, would Karch mention, maybe, so that's another… Tokyo-specific coupling.
We could… it's not strictly equivalent, but for the purpose of making the engine Tokyo Agnostic, we could imagine that, Calling the yield now every n iteration.
could be a good… a good enough solution. It needs to be validated, but, it's basically this, for people that don't… don't know necessarily this, call.
It's very nice. It could be used, for example, by Albert into the transform processor.
So the transform processor is typically a processor doing a lot of data processing.
And all the KQL processor will be the same, the same issue.
If we… if we consume too much time into the KQL processor, or into the transform processor OPL, It means that the… and if this thing is not async.
Or if it's not granular enough in terms of async processing.
Then we will basically consume a lot of time On a pure, data processing, tasks, and if we don't give back the control to the Tokyo runtime.
basically that will be in competition with the I.O, and we will basically not be able to, basically to handle the I.O. So the idea… there is two options. Either you… you, you, you, you yield now, in specific locations, so you, let's say you have, an iteration or a for loop somewhere, doing some ED stuff, and you called every n iteration, giving back the… the… to the Tokyo, I think, runtime, giving back the control.
Or you can use the costume widget, which is nice, because, That will be, let's say, If you need Tokyo Runtime to get back the control, I give you a chance to get it. Otherwise, if my budget is not fully consumed, give me back right away my option to continue the processing. That's basically what the consume budget is doing.
Which is nice.
And why I used that, it's because we were in a draining, loop.
So following, a global shutdown, we enter into, A drilling ingress step in… at the receiver level.
And, then we consume the… All the, the incoming, control message.
And let's say that we have, A lot of them, for whatever reason, we… and this loop is not a sync.
We, we need a way to basically giving back the control to the one time, and that's why we, introduced this, consume budget stuff.
You will find that in different, parts of the project.
Oh, comments have been added.
Yes, this thing needs to be configurable, could be a follow-up, I didn't work on that yet.
Same thing here… Yeah, okay… So, Lalit was mentioning that for him it was going in the right direction.
So, question for Lalit, if Lalit is there.
jmacdonald 00:52:53 He's not on the call.
Laurent Querel 00:52:55 Okay, so it will be… do you have the answer to the question I had with you, Joshua?
jmacdonald 00:53:02 I don't… Laurent Querel 00:53:03 Soda.
jmacdonald 00:53:03 It's… I don't actually know, I apologize. The question was whether Lali has run… Lalit has run the… whatever tests we've run to exercise these benchmarks again with this PR.
I apologize, I don't have an answer.
Laurent Querel 00:53:18 Okay, no problems.
So this one, I'm not sure that I already, read this one.
I will… I will skip the one where I… that I didn't read yet, because that will take too much time to… so I will just, So this one was about, No, I didn't address this one yet… Yeah, this one, I started to work on it.
So it was a fair, feedback, again.
end up with… so basically, this one being analyzed, I know it a bit more, so it's… it's about… there is… In the… the pipeline controller.
There is, an unbounded data structure, and, definitively, that's not something we need… that we should have.
So, I created a follow-up, GitHub issue.
And we need to create a follow-up PR to address that. I think my rational why it's a follow-up PR is because, even in the current situation, I think the… the outcome of this year will be better than the previous option.
And, and then we can finalize the small thing like that, in a future PR. That's, so obviously, we will see what, Lalit return, or comment on that, but, my proposal is to create, a follow-up PR.
I think these two, this one, and, this one, and this one.
I think I tried to address… Wait a minute. I think… I was thinking that I tried to create… Yes.
It's about… It's a discussion with valueception, it's a discussion around, Making the… The exporter, drenched down policy, explicit.
Different option, one from GoCan that has been mentioned regarding exposing directly the P-data channel and control channel.
I'm not a big fan of this approach, I think Lalit was also mentioning that, but I understand the concern.
And I think Lalit, mentioned, and I think, Gokal was in agreement with that. Lalit was mentioning that maybe we could.
exposed, a joint policy, directly into the, Into the trade of the exporter.
We could imagine that it's also a policy, no, I think it's something that needs to be done at the code level, not the configuration level. So, yeah, I like this approach, where we explicit… we make explicit the drain policy, and it's exposed with the method, and by default, we have a default value.
Gokal, you want to specify something there? Or to… Gokhan Uslu 00:56:43 Yeah, just, maybe not directly related to this pull request, but just wanted to clarify the idea about separating the channels, just to… is a food for thought, because I understand Lalit's concern here, but I also saw that two of the main things that the message channel core as there is, too.
delay the shutdown to give time for draining, and also the other is to limit the burst, etc. But I also thought that I had a few design ideas that would eliminate the need for having that, altogether, I don't… necessarily disagree with what Lalit says, but Lalit says… what Lalit says seems to me, is also a little bit tied to the status quo, but I was coming from a different angle, where, for example.
shutdown is received immediately, and drain is handled via handle, with an explicit drain policy choice, or something like that, by the exporters, and maybe the engine honors that policy after the exporters exit, or something like that. And also.
The burst, wouldn't be an issue if ACNAC channels were separate and not… control channel, etc. Stuff like that, I was thinking, but I'm also not in complete disagreement with… like, I agree with Lalit's comment as well as the direction.
Laurent Querel 00:58:25 So, two things. Definitely, I would appreciate if you can create, not a PR, But, Gitavi, if you're describing your approach?
So we can talk about it, and think about, your, your… alternative design.
And I'm all for simplification.
I disagree with the exposing the control, receiver, key letter receiver, to the exporter, because, as you know.
The message channel core, the logic behind it, is fairly complicated.
And… and providing… and hoping that every, exporter, implementer.
we'll do the right thing for those things, is, in my opinion, a wish that will never happen. So… the complex logic regarding the shutdown and so on, need to be at the engine level, managed at the engine level, and it's not something that, every exporter needs to implement. We know that in the GoCollector, we had similar issues, and then we end… we end up with some helper mechanism to To factorize the… some of the recurrent behavior But there is no real enforcement to use those helpers.
Yeah, so I… Gokhan Uslu 00:59:54 Oh, sorry, I thought you were done. Go ahead.
Laurent Querel 00:59:57 Yeah, so what I'm saying is, to summarize.
There are some concerns that are engine-level concern, and on which we want to Really enforce some behavior and rules.
That need to stay at the engine level and, control LP later.
Exposure, direct exposure, is definitely not a good idea, in my opinion.
Gokhan Uslu 01:00:22 I see. So, this is also the conclusion that I came to after I was also sharing the same idea with Lalit in private chat. So, I see as a big value of that message channel core implementation to be keeping simple exporters You know, not having to worry about it.
But then… then the compromise in my mind was that why could we not choose either, like, take the channels right away, so that you can implement everything you want in the exporter with full flexibility?
And… or, you know, just use that multiplexed channel that has all the complicated logic, so it would be, like, an option. That's… this is the, you know, like, final compromise that I reached, because in the exporter that I wrote, I would love to have that, Laurent Querel 01:01:11 Yeah, so I think it would be nice to create a GitHub issue with your alternative, and also exposing the problem, with, let's say a concrete example based on your exporter, and we will iterate on that to figure out a solution That, does not break I think a good design principle, which is Things that are engine-level concern need to stay at the engine level, because then we know for sure that we have some guarantees that don't rely on A good implementation of an exporter.
Gokhan Uslu 01:01:56 Yeah, I agree on that. That's the part that also… Laurent Querel 01:02:01 Okay, so let's… Gokhan Uslu 01:02:02 Yeah, just you.
Laurent Querel 01:02:02 Once you have this, gitHub issue, design-oriented, Entry, and that will be a definitively a good thing on which we can think about.
Gokhan Uslu 01:02:16 Okay, thank you.
Laurent Querel 01:02:16 Okay Sounds good, yeah.
End of the… any last minute, feedback, or… jmacdonald 01:02:30 I think we're out of time… out of time, because I'm going to go to another, collector SIG meeting right now.
I will definitely try and understand in more depth the topic that you and Gokan just discussed, follow this conversation, but I think we should get this merged, nevertheless, and, move us forward.
Laurent Querel 01:02:50 So, I'm just waiting for your confirmation regarding the… the, the… jmacdonald 01:02:56 Got it.
Laurent Querel 01:02:56 that, and, and one… once it's confirmed, yes, I will, I would merge it.
jmacdonald 01:03:05 Thank you. I will do that right now.
Laurent Querel 01:03:07 Okay. Thank you guys, have a good, good day.
jmacdonald 01:03:11 Thank you all.
Gokhan Uslu 01:03:16 Goodbye.
Laurent Querel 01:03:17 Good day.
