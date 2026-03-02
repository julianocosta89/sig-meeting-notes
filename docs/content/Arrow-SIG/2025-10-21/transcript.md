SIG: Arrow SIG
Date: 2025-10-21
Duration: 57 minutes
Zoom Recording URL: https://zoom.us/rec/share/827LULcvmbr2idsbCPNtZ1nWTrbKMHG4hlVlrz18M4oywvUASVPcudXZetZA1ws.MAjumm3a4oYTCEFL
============================================================

## Zoom Recording Transcript

**Laurent Querel** 01:24 I guess…
Joshua, I'm creating a new entry into the Google Doc.
Just to,
make sure that, okay, we… today we have, we don't have Alberta, we have Utarch.
myself, Rosha, we don't have Pablo, Jack is not there.
Mac is not… Oh, maybe Mike is there.
Oh, sorry, Jack was there, I will.
Okay… And I let other people add their name.
**Albert Lockett** 04:17 Hey, guys.
**Laurent Querel** 04:22 Bye.
**Joshua MacDonald** 04:23 All right, well, I'm sharing my screen, and I'd be glad to get started,
I think we should… first of all, have a link to our issues here.
How many since… hopefully not so many since last Thursday, but I know we have some, because I've been breaking stuff with AC and NAC handling, and we can talk about that.
So, we have…
these issues that I just filed, which I'm referring to, these were, things that we uncovered as I merged my first changes to add ACNAC handling.
I'm conditioned to thinking that we should be strict about ACNAC handling. We basically, by default, wait for responses, but it's breaking our benchmarks, and I can show you
What happens today?
So… these are things that we can talk about. I filed separate issues for each component, so…
the OTLP receiver now has a mode called wait for result. Its default is true. That's me being aggressive. You can push back on that, but… or we could wait and do it later. I think it is the safe default. So we can see, for example.
OTLP, ATR, OTLP, dropped… In, dropped some number of logs, and that could be…
For a number of reasons that we need to look into, but it has to do with something about back pressure.
actually working.
In the case of the OTAP protocols, they are not affected, basically, because those components do not implement, Akronack yet. So, in the case of these
of the OTLP exporter specifically, we can see in the code that it's got a single-threaded export call, and that's going to be a sort of
correlated factor in all of those low benchmarks. It's because somewhere in the benchmark, we have an OTLP exporter that will only issue one request at a time, so anybody else doing ACNAC handling will slow down a pipeline if somebody's got one concurrent request.
And so I've had all these issues saying, first of all, you need to have ACNAC handling, and then you need to make sure that you can have more than one concurrent request somehow.
That's…
that's the issue. Those are the issues that I've filed recently, and I think that's, for the most part, my contribution to triage.
**Laurent Querel** 07:08 Okay.
the, whether or not.
**Joshua MacDonald** 07:12 Oops.
**Laurent Querel** 07:16 So, so, I see this, this, let's say,
very light blue, I don't know how to define this color.
Yeah, the OTLP to OTAP…
**Joshua MacDonald** 07:31 This one.
**Laurent Querel** 07:33 Yeah, which…
**Joshua MacDonald** 07:35 Dropped.
**Laurent Querel** 07:36 drop alerts. How do you explain… oh, you expand that because OTAD does not implement yet the… the,
the act… properly. So you don't, return an AC or NAC, let's say a hack to the…
**Joshua MacDonald** 07:57 I… I don't actually have a great explanation for why it's… Half and not zero.
Let's see… That…
**Chris Hain** 08:09 I think is… so there… it looks like 100,000 there, so I think the pipeline will hold 100 messages. Each message has a thousand signals in it.
**Joshua MacDonald** 08:17 Right, something like that.
So, there's no ACK in the OCHAP exporter. So the OTLP receiver on the first side never gets its thing, and it's waiting for the result.
So I think that's the explanation. Now, would you like… would anybody like to see that default change to false? Which means, you know, let it… let it respond as soon as it's in someone else's memory?
**Laurent Querel** 08:45 Personally, what is… what really matters for me is to have into the… The… the continuous benchmark.
this flag.
true and false.
So we, we can, we can see the impact of having it true.
And try to figure out if it's normal, or if we can do something to improve the… to reduce the gap between these two approaches.
**Joshua MacDonald** 09:12 Right. I totally understand the rational of having.
**Laurent Querel** 09:19 But we have to message that properly also, because if we have a default that is different from the Go Collector, for sure people will compare things with two different defaults, which is not great.
So, we have to make that… very clear.
And that's why we need also,
To include that into the continuous benchmark, because then we can enable
for our default, behavior, which will be, true, in some way, we have also to enable the same kind of guarantees with the Go Collector, and then compare.
**Joshua MacDonald** 10:03 Yeah.
Do we have GoCollector tests in any way? Because I would love to have us configure both of these in each case. There has been discussion in the
OpenTelemetry community at large about the…
the CNCF Technical Oversight Committee, having kind of feedback on the quality of hotel releases. This was, in my opinion, one of the issues from customer feedback, which is, like, there are ways you can figure this, and it just drops data, and that's not great.
By default.
**Laurent Querel** 10:40 It'll be really hard to change that default.
**Joshua MacDonald** 10:43 it could take a while. So we should just, I think, test both, and…
be clear, I… I think.
**Laurent Querel** 10:52 Shop.
Yeah, I mean, what was demonstrated internally at F5 was, in September, A comparison between
So, leveraging exactly the same benchmark infrastructure, comparing the Go Collector with the Rust-based engine.
What we have in this page is more…
focus on the data flow engine, so the REST implementation.
I know that Chris had a plan at some point to…
Have another series of… that may be on the same page, or with a different section, or a different page.
Does not really matter, but, having a series of charts, describing or showing the comparison between the Go and the Rust, pipeline system with exactly the same scenarios and same, synthetic,
telemetry traffic.
**Chris Hain** 11:52 Yeah, I kind of had 3 scenarios in mind. Like, there's the continuous integration, which we've got there, so every commit, it does it. Figured we don't want to wait for go-collector comparisons there, or, like, all these different protocols we might wind up supporting.
So another one would be, like, a nightly version that exercises, you know, syslog receivers and any other random things that get written that aren't really the core OTAP, OTOP.
Different other configuration settings around batching and, you know, all the junk that's gonna take a long time to run.
And then the third was kind of comparisons against other agent-type things. I was gonna throw, like, vector and alloy and whatever else I could think of in there. But if we wanted to do some that were just, like, more extensive tests against
the Go Collector, that is cool, too.
However you guys want to structure it, it's fine.
**Laurent Querel** 12:44 Okay, so I started to, to update the Google Doc, benchmark plan.
Could you, Chris, maybe just,
refine what I started to write there.
Just to make it more on…
**Chris Hain** 13:04 Yeah.
**Laurent Querel** 13:05 We, we have a… We keep track on that.
**Chris Hain** 13:09 Yep.
**Joshua MacDonald** 13:14 Okay, so I will take this as a very serious issue. There actually is not an issue found about it in the community. There should be. I know it's been discussed in Slack on the maintainer's channel for the collector, so I'll just kind of follow up on that.
**Laurent Querel** 13:31 Okay.
**Joshua MacDonald** 13:33 Alright, you ever talked about this, OTLP metric export first, or multivariate metrics?
Dreaming.
**utpilla** 13:42 Hey, Josh, very, like, quickly, just following up on that default thing, like, now after looking at the, the graphs, I feel like maybe,
setting that to true is not the best default, because I think, like, from a user experience standpoint.
The default configuration should just let things work,
I mean, should have my logs flowing, and…
I shouldn't see performance issues. Like, if I want more reliability, of course, I can turn that on, but, like, now, as a user, I also have to know,
like, what kind of components are in my pipeline, and, like, do they send an ACPAC or not? So…
If it requires some knowledge of the pipeline beforehand, then…
Maybe it's not a good default setting.
**Joshua MacDonald** 14:34 Yeah, I think you're probably right about that, now that you say it. Does anybody else have a thought on that topic?
**Laurent Querel** 14:41 I think there are some telemetry where people don't expect necessarily full reliability.
For example, I can… at F5, we expect full reliability for
Security or the clocks, for example.
But for the majority of logs, we don't really expect,
To have this, default behavior, of having the guarantee of delivery for every logs.
something is, is true… the same thing is true for matrix in general.
Except some very uncommon metrics. Most of… most of the time, we don't necessarily need
A full, guarantee of delivery for all the metrics.
**Joshua MacDonald** 15:30 Well, okay, so the default is a good question, then.
I think to unblock the tests from having this crazy confusion, we should definitely change it now that we've talked about it. I'll do that myself.
Set it to wait for a result false.
And we can elaborate on this.
After we've…
Well, first of all, part of the problem is we haven't implemented ACNAC everywhere, and if you don't… if you have wait for result true, and ACNAC is somehow malfunctioning, it's a… it's a bad situation.
So, I think we should revisit this later. Thanks.
**Laurent Querel** 16:06 Yeah.
**Joshua MacDonald** 16:07 Thanks.
**Laurent Querel** 16:08 Yeah, and when we look at the charts… for the… The light blue,
chart, I think, something that indicates that there is, probably something that is more than just,
The CPU usage was close to zero, so it looks like there is a blocking situation there.
So I don't know why we had these 100K logs.
But at least, for sure, we had a…
0% of CPU usage, which look very, very slunch.
**Joshua MacDonald** 16:44 Yeah, yeah.
Okay, I will send a change to undo that default. I will leave the feature. In the future, I think we might put this on a HyperEdge level configuration anyway.
**Laurent Querel** 16:57 Yeah, ideally, I don't know how much work that will present for Chris, but,
Maybe what we could have is just having, this…
Two set of, this entire set of configurations, continuous benchmark, replicated a second time with this flag turned off or on, depending on…
So, we have these two…
way of comparing, testing the performance and the behavior of pipelines, one with
I acknowledge the guarantee of delivery, and one without the guarantee of delivery.
**Joshua MacDonald** 17:37 Gotcha.
Cool. Alright. I will not… Do such things again as well.
Alright, so we were, prioritizing some attention on the metric export path. I know I'm interested in seeing us
take the SDK outputs, those structs, and turn them into
I think, ideally, OTAP, but I think, baby steps, we should start with getting the OTLP to OTAP and OTAP to OTLP paths.
Solid. I know that's a lot of work.
Do we have a status report?
**Laurent Querel** 18:20 Well, so we, I was,
disturbed by something else. Did you ask something for me, Joshua?
**Joshua MacDonald** 18:27 I was, I was looking at this one here, talk about OTLP metric export.
**Laurent Querel** 18:32 Oh, okay.
**Joshua MacDonald** 18:33 Being an area of wide interest.
I think I'm partly interested in pushing metrics in a sort of, like, getting a timeline on that one. We need the OTLP to OTAP conversions to work really well first.
So, I think that's what this is about.
**Laurent Querel** 18:51 Okay.
And we are talking about, internal OTIP metrics, right?
**Joshua MacDonald** 18:58 That's my… my… the reason I'm… I'm sort of prioritizing this topic for myself.
I know that you had… last week, we said that there was work underway, but it's only been, you know, 4 working days or so since that last meeting.
**Laurent Querel** 19:14 Yeah, and I was focused on something else in between.
Yeah, I mean, I can probably do it, or helping someone to work on it.
That should not be a big deal.
what we need to do is basically integrate the REST client SDK.
I always, the metric system that we have inside, the engine.
All the work of capturing the information periodically, and Local aggregation, and
And collecting that into a single point is there. Now it's more…
from this, global metric system using the parent SDK.
to report that to whatever destination we define into the configuration. I think as a first step, it's… that would be,
Good enough, and a more long-term approach will be to
Reuse the pipeline… the pipeline system that we have.
In a way that will give us
Option to generate the internal matrix.
Same thing for events in values format, into a TLP or a tap.
But if we need an OTLP export for the internal metrics quickly, I think the easiest way to do… to do that is to
to start with the integration with, the current SDK.
**Joshua MacDonald** 20:54 Right.
You mean the OTEL Rust SDK?
**Laurent Querel** 21:01 Yeah.
**Joshua MacDonald** 21:01 Got it. Yeah, I mean, I would…
There are two levels at which you could integrate with an SDK, and I'm not sure I'm super familiar with this, but you can integrate at the level of the SDK, like, by issuing metric events, and having it aggregate, and so on.
Or you can integrate at the level of an exporter, which is where you have some intermediate representation that goes to an OTLP export path. And that's not very different than constructing
Well, I think, actually, for our testing and validation purposes, we actually have
the Prost objects that you can build to and from these OTLP exports.
And then we should just be able to, like.
serialize them as vectors, and use our existing pipeline. But our existing pipeline has to have
I think it has to have been built out a little bit more. That's more the type of question I was having, which is to say the OTLP metric view for bytes and the OTLP metric view for
for records.
has to be built out, and I… because I think that was what we were, focused on first.
**Laurent Querel** 22:17 So… Can I ask, the…
Because… so, for example, for the benchmark infrastructure, we are already using metrics to… to build those charts.
So, I'd like to understand the… because we need to prioritize some tasks, and we know that we have a lot to do on the engine itself.
So that will help me to understand exactly what we want to do with those internal
Metrics and the corresponding export function.
What will be the…
what would be the benefits? I mean, obviously, we need to do that. I'm just trying to figure out if it's a priority, or if it's something that needs to be done, let's say, in one month.
So…
The question is, what do we want to do with that right now? Because we already have,
Without that, a probitous endpoint that is exposed, used by the benchmark infrastructure right now.
**Joshua MacDonald** 23:25 Gotcha. Yeah, I apologize, I think I have over-prioritized this, at least for today's meeting, for sure.
**Laurent Querel** 23:32 Oh, okay.
**Joshua MacDonald** 23:33 You know, a month from now, it's fine. I didn't want to talk about the SDK stuff specifically, more about the state of there being an OTLP signal
That our pipeline… a metric signal that our pipeline is good at.
Because I believe there were some to-dos in that low level of the OCHL Arrow Rust packages.
**Laurent Querel** 23:56 Okay.
**Joshua MacDonald** 23:57 Well, we don't have to talk about now.
**Laurent Querel** 23:59 Collective.
**Joshua MacDonald** 24:00 Would… would someone like to talk about this bullet point list here on the issue triage list?
**utpilla** 24:13 what is it more about Josh? Like, I just want to make sure that we are still…
We still have the same plan of using the Rust client SDK in the global metrics aggregator. Like, our internal metric set SDK… metric set implementation is used to collect all the internal telemetry, and then we kind of model it as
An input for the Rust client SDK. That's not changing, right?
**Joshua MacDonald** 24:43 I…
Don't know. I think we should stop having this conversation about Metrics SDK, because I've already derailed us quite a bit.
If what you're saying is that you thought the plan of action was that we will centrally aggregate metrics for the purposes of, say, self-feedback loops and self…
scraping Prometheus, for example. But if we are going to do OTLP export for now, We're focused on logs.
Principally, and therefore, we will use an OTLP exporter from an OTL Rust SDK.
And even on top of that, we're going to use the API, the Metrics API, which means to say we're going to aggregate
counters.
periodically through an OTL SDK and have it export OTLP. I'm fine with that. It probably makes it hard to do, like, histogram instruments and so on, but we can worry about that later.
**utpilla** 25:43 Yeah, I was… I mean, if you open the chat on this call, I think I… I was just referring to the diagram that Laurent had initially shared, like, a few weeks ago.
So yeah, I just wanted to know if there's, like, We're still on,
Agreement about, like, how the final… how the internal metrics finally get exported.
**Laurent Querel** 26:08 Yeah, I think, so… I will say the following. I think, as a first step.
In my opinion, that definitively the right, the right approach.
No.
a long-term solution, then I'm not sure, because if we… so in this global metric aggregator that we already have.
And which promptly expose a primativious HTTP endpoint.
we could embed a REST Hotel Client SDK, and with your help, figure out a way to
report, the… The pre-aggregated metric that we collect from the values pipeline instances.
And then generate a lot of TLP traffic.
For any consumer.
That's, I think, is… Should be fairly easy.
But now, if we want to support different way to represent those metrics, events, and so on, generated from
this, solution.
And let's say we want to expose them in OTAP format.
Right now, there is no… Rust Client SDK able to generate OTA.
And in fact, we already have exporters
For OTAP, for TLP, and so on.
So the idea was, why not reusing a special instance of
the pipeline engine that we already have.
To ex… to export, the corresponding internal matrix, internal events, to whatever,
OpenTelemetry consumer, needs to be connected with this system.
So that was, like, a long-term vision.
Now, maybe there are some other options. You could imagine that the rest hotel client SDK,
move progressively and support OTAP.
maybe with, reusing some component that we implemented. They are both… they are both, Rust,
ROS-based, so that's not impossible.
But to be honest, for me,
all those things are definitively, at least for us at F5, they are not the top priorities.
The top priority is for me to have a very strong, robust, efficient pipeline engine.
And having the minimal set of observability that will be required to
to check that properly. And I think we already reached this point.
Having an OTLP export is nice.
But at least for F5, it's not a top priority right now.
But definitively something we need to achieve.
**utpilla** 29:06 Okay. Yeah, I think the benefits of using, like, the OTL client SDK at the global metrics aggregator level would be that we don't… we wouldn't have to, implement logic for renaming metrics or dropping metrics, and, like, metrics SDK… Client SDK already has views.
And has OTLP exporter as well. Like, one way to… one thing to do, probably, would be to, like, have an exporter that exports OTAP, like, have an exporter at the client repo.
But yeah, I mean, if we go our… if we go the route of, like, using our own specialized pipeline, because we have a way to export OTAP traffic, then we would also have to…
Worry about, like, offering a way for users to rename the metrics, or drop the metrics, or…
Change the histogram bucket.
Bucket details, or something like that.
Which the SDK has already taken care of. So, yeah, I guess…
**Laurent Querel** 30:00 So, yeah, understood, but do you agree that this entire pipeline system that Is represented in red.
We'll most likely be,
let's say, a bigger version of any pipeline that you already have in the Client SDK at some point.
Because there, you will also have things like filtering, like renaming.
like, batching, like, I mean, anything, in fact.
**utpilla** 30:30 Yeah, I mean, the thing in the red, which is our own… it's kind of like our own SDK implementation, in some sense.
It has an API to emit metrics, and then…
It gets aggregated and sent out, so…
It is sort of an SDK already, but…
Yeah, I'm not saying that we should, like, totally do it only using client SDKs, just,
Just wanted to, like, mention that, like, we would have to consider, like, implementing views and those kind of functionalities if we…
**Laurent Querel** 31:01 okay.
**utpilla** 31:04 Okay.
**Joshua MacDonald** 31:06 And in a long stretch of time, we can definitely imagine having metrics capabilities like those views. We won't prioritize this, I agree. So, I would say, passing it to whoever wants to speak next on this list, I think we have not talked about multivariate, and it's on this list from someone.
Ever, I have not heard from anyone on that topic. Laurent, do you have a list down here that you want to go through?
**Laurent Querel** 31:38 Yes, I was, as you know.
**Joshua MacDonald** 31:42 Sorry, down here, like, okay, back to the… back to…
**Laurent Querel** 31:46 So…
**Joshua MacDonald** 31:47 problems with Windows.
**Laurent Querel** 31:49 I will be able to focus a little bit more of my time,
starting tomorrow, and be back on the engine itself. So I was trying to…
To define a list of, engine-related tasks, that currently are…
Important things that are missing, or blocking, or not… not working well.
I'm aware of some of them. So, for example, I had a discussion with, with Chris.
Regarding the… The status that is not exactly, perfectly in sync with the…
Some elements of the status are okay, some of them are, especially the ones that try to aggregate the
the different phases.
Of different instances of the pipeline are not necessarily, logic… logically correct.
So that's an example of something on which we need to,
to, to, to put some effort. We also have this,
issues regarding the ACNAC retry mechanism, and… and see if we can, improve the performance, making sure that,
we have a strong story there, so I'm… I would be very happy to help there.
I'm just trying to figure out what are the most important aspect…
That, and get that from various people, so we can…
From there, we can figure out a list of things with their priority, and
that will define a nice plan for the next,
Next week, or next two weeks.
**Joshua MacDonald** 33:41 Gotcha.
Well, I… We'll take another look at the list, I…
in general, was… haven't looked back since the last time we looked at this, so it's probably worth me going through the whole list. This is the December milestone.
The things that I've filed are the ones that I knew weren't part of it, so in some sense, those are definitely priorities, like, all this stuff.
About OTLP. I'm less concerned about the OTAP exporter receiver. We would like to have, performance comparison in that regard, to kind of repeat the Phase 1 performance. We're definitely interested in that.
But it's not a priority, I would say.
Does anybody else on the call want to speak to their wish lists or priorities for the engine? I know my priorities, and I'll take a look at that over the coming week.
Well, it seems like we may have reached the end of our call. That would not disappoint me. I like it when we finish a little bit early.
**Laurent Querel** 34:59 Maybe, maybe, we could have, so, Shen Li, I didn't see that Shanli was present.
So… Chen Li, let me know if it's not feasible for you right now, but if it's feasible, I'd like to see Chen Li making a demo of the
the new filter processor that has been implemented, I think that's,
That would be… that would be interesting for everyone.
**Joshua MacDonald** 35:24 Yeah, sounds great.
**Chanly Ly** 35:26 Yeah, I could do that really quick.
**Joshua MacDonald** 35:30 Would you like me to release the screen share, or, would that be great?
**Chanly Ly** 35:35 Yeah.
**Joshua MacDonald** 35:36 Cool.
Alright…
**Chanly Ly** 35:39 Let's see…
Okay, so here's the current configuration of what I have for the filter processor, which currently supports logs.
Here we define, Certain things we want to exclude or include.
For, the things we match here, we're matching on resource attributes, record attributes, severity text, and bodies, and then an optional, thing you can match on is the severity number, so you could like to find a minimum.
Severity number you're looking for, or if you want to include, undefined as well.
So… Here's a simple processor, pipeline I have configured with the fake data as sending out logs.
At, 100 signals per second.
And that's connected to the filter processor that we have to filter out
We want to look for,
Logs that have the attributes that match this key-value pair, Gen AI with OpenAI value.
And that's just gonna pipe out to the debug, where we're just gonna output everything, just so we can just confirm.
Now we're seeing it correctly.
And then we have a new op as the, export.
So let me run this really quick.
Okay.
**Laurent Querel** 37:13 during the compilation of this thing, so this filter processor is acting directly on OTAP data, so it means that,
what Shenmi did was… basically using the Apache RO kernel functions.
directly.
To implement the values, filter options that he was mentioning.
**Chanly Ly** 37:37 Yeah, so now we're getting,
30, it's down from… so when we, set up the fake data generator, it's sending out 100, so now we've filtered it down to 30. And if I turn on the…
Detailed mode, you can see.
That the, data we're filtering out should have that attribute we're looking for.
Yeah.
Right there. And then there's an edge case we have to fix where,
or signals with no attributes are getting through, but yeah.
**Laurent Querel** 38:14 Yeah, I think that's, nice validation of,
The feasibility of filtering by different type of information.
into those, OTAP, the PDATA messages with the OTAF format,
And what… what we put into the single milestone, we…
we didn't add so much new processors. One of them was the filter processor, which is, in my opinion.
For our use reason, it's important for us because we…
we won't… we have a basic scenario for F5 where we need this filter processor.
And I think it's also nice to demonstrate end-to-end
the fact that we use OTAP not only to optimize the transport, to optimize the internal representation, but also to optimize the
Some, some important aspects, like filtering.
So that was the… the reason why we put this filter processor part of the single milestone.
We are not using, yet, the data fusion energy.
Because we don't need to for this simple situation, but for more complicated things, we are experimenting…
Data fusion, and trying to see, to check, basically, how to… To express, more complicated
Say, filters and additional transformation directly mapped to…
A data fusion, logic plan.
It's more long-term. I don't think that will happen for the second milestone, but that's definitely something
on which we… That we are exploring.
**Joshua MacDonald** 40:12 Really great to see. I think, yeah, I think it's important that you have a non-data fusion solution at some level for this simple case.
**Laurent Querel** 40:20 Yeah.
**Joshua MacDonald** 40:21 To help… to help everyone.
Thanks, Chan Lee. Looks good.
I thought of one more topic, if there's nothing else on the agenda, I put it in the parking lot area.
And I thought I'd just shoot my question out. This comes out, this comes to be… this comes up on the topic of metric instrumentation on the, kind of, component side, where we're counting
In the current retry processor, we're trying to follow that, what we call the, kind of.
telemetry RFC from the Go Collector, which says to count things by success, failure, or refusal. So failure is when you generate the error, and refusal is downstream error.
And then there's a producer side and a consumer side, since you might send more than once, like in the retry processor. So the retry processor is a good test case, and I do have an open PR about it.
The question is about the instrumentation for each of these success, failure, refusal counts, input or output, is based on num items, and the num items requires you to have a payload. And so, in my AC and NAC handling, there are places where,
I am going to do some instrumentation to see, like, finally this has failed, I don't… if I finally know the outcome, I want to count how many failed.
But I don't have the payload because of various conditions, or I don't have correct information because the call data maybe was incorrect. So there's a few cases where I don't know num items, and it made me think that I should put the num items somehow in the context.
But that worries me. It would be, like, you know, maybe something that we could think about doing. It's also something you could cache, but for now, in the retry process or change I've been working on, which is using a stateless approach, the point here is that
in order to handle the NAC case and the ACT case, you need to know how many items there were, and by then, if you're…
you should… you may not have payload, and you shouldn't have asked to keep the payload anyway for the ACK return case. I wonder what people think about how to compute num items essentially once, and whether you think it would be worth
for example, in my change here, it's a work in progress, I don't want to show you anymore. Now, I've added to the…
call data, which is currently a 2-wide vector of U64, making it a 3-wide vector of U64, simply so that I can put the number of items in it.
Which means I don't have to compute it more than once, which means I know it even when the payload is missing or absent for good reason. I wanted to hear if anyone has thoughts on this topic.
**Laurent Querel** 43:25 But the new ETEM is basically,
Is it as simple as,
querying the arpeggio record of the main payload.
to determining the number of rows. So if the main payload is…
All the logs, or all the span, or all some… some kind of matrix.
If it's just that, it's… it's a pretty… In its,
It's a function that already exists for Apachello that is basically free in terms of, overhead.
**Joshua MacDonald** 44:03 And in the case of a NAC and the retry processor, you may have the payload, and it might be inexpensive.
For metrics, it's a bit more complicated, I think. But you're correct about logs and spans, and
So there's the… there's the current case where you… where you didn't get a payload back, but you're right. I still don't think, really, that the ACT case should have to return the payload, just in order to count the number of items.
**Laurent Querel** 44:29 There's also…
**Joshua MacDonald** 44:30 the case of an OTLP vector of bytes before it's been converted to OTAP records to.
**Laurent Querel** 44:38 Certainly.
**Joshua MacDonald** 44:38 That's why I was kind of curious about it.
I'm not sure what you all would prefer.
**Laurent Querel** 44:47 Yeah, so having some kind of summary representing the…
This number of items, so you can report properly into the receiver side.
internal matrix.
Following the, the…
the guidance that the Go Collector is following with the old fusel and so on. Is it a…
A fair summary of what you want to achieve?
**Joshua MacDonald** 45:14 Yeah, I think so. Like, if it… right now, we have call data as two, essentially, words of data, 8-byte words, and we could imagine widening call data and letting people make their own mind up. For a receiver that has an existing slot-based storage, you could put it in there as well.
For my retry processor, I couldn't, because I don't have a state table, so… or a slot mechanism, so I put it in the call data. But you could also put it alongside the call data, having a kind of set of standard fields.
Which would then incline me to always have it. Then the question is, do you really want to kind of thread through num items through every frame of your call stack? Well, if you have a log filter processor, it changes the number of items, so you're going to have to…
make sure that we don't ever mutate data, but I don't think we do, which just means caching the num items, like, effectively in the context at every level in the pipeline.
**Laurent Querel** 46:14 Does that sound about right?
I think so.
Yeah, we… I mean, the… We can't, in fact, update in place.
Data, we… if we have to filter out things, or if we have to mutate.
the values Apachello records we have first to create a new version.
So that will end up into a new,
for the downstream nodes, we will get a new PData instance with the…
with those new, Apachello records.
If there is no modification, we just get the same one with this arc mechanism.
So we could reuse directly the previous number without the cost.
I think that's, that seems okay for me.
**Joshua MacDonald** 47:05 I see.
**Albert Lockett** 47:08 Bye.
**Joshua MacDonald** 47:10 We haven't done this yet. We would have to look at how to handle ACK and NAC for a filter processor.
**Laurent Querel** 47:17 And a batch processor also.
**Joshua MacDonald** 47:19 Yeah, that's actually the one I have next in mind, if we go back to my list. So we'll keep… we'll take this up in another meeting.
**Laurent Querel** 47:28 Yeah, okay.
**Joshua MacDonald** 47:29 Thank you all. I think that might be the end. If not, speak up.
**Jake Dern** 47:35 Sorry, I just caught the words batch processor as I was, tuning out, but I did have a question in the chat there, but it sounds like maybe the answer is that we're still working on, kind of, how AC and NAC are going to behave for that, but that was one thing that I was curious about, seeing your,
your PR, you know, with the wait for result, flag.
**Joshua MacDonald** 47:56 Well, I can definitely speak to that topic. You're right, I do see this on this chat now.
I have lots of thoughts and opinions on this topic. I'm not sure that we should go at length into them, but I have written on this topic and sort of extensively pushed around and studied the hotel collector implementation of that.
So there's a legacy batch processor. We're trying to upgrade it to avoid leaving a legacy or removing a legacy, just to, like, fix it, essentially. And this is based on this newer functionality, which does implement wait for result. So.
It's a very long story, but the correct thing, in my opinion, if you want back pressure to work, is to make sure that the OTAP batch processor stores the context of all the incoming requests.
associates it with each export that goes out. Taking care to… like, there's corner cases here where an input is split into smaller outputs that you have to consider as well. So, like.
each request comes in and goes into one or more batches out, and you just have to keep those contexts and reply to them to enable back pressure. And the thing that I wrote in the issue… I'll just click around to get there.
Is that…
you don't want to limit concurrency. That's actually the fatal flaw of the Go Collector's batch processor, is that it limits concurrency effectively, so that you need to have wait for result false downstream. In a world where you're going to have wait for result true, you need the batch processor to both
supply ACNAC support, as well as supply concurrency. Does that sound reasonable?
**Jake Dern** 49:47 Are you asking me if that sounds reasonable?
**Joshua MacDonald** 49:49 Well, that's the state of the system, as I understand it. And,
My… my intention, as summarized here, is to take this up myself, because I've done it a bunch of times. There's a Go Collector component we had here called Concurrent Batch Processor in the Phase 1 project, which I removed because it was just so much maintenance, but…
And… and that's why this legacy upgrade of mine, I could… I could find you the change. It's… I don't know if anyone cares. Here it is. Here it is. Modernize the batch processor that I'm working on. This is,
essentially an option that we would have feature gate and turned on over time to eliminate the old implementation and use the new exporter helper internally, which means enabling wait for result, which means enabling block-on overflow, which also means,
allowing the concurrency that we need, which is actually not even done in this PR. So this is just replacing that old thing with a new thing, which propagates errors correctly.
So I will do the same in the Rust world.
**Laurent Querel** 51:01 On this topic, Joshua, what is the current state of the art for the open telemetry collector co-implementation when you have multiple destinations?
So, serving the…
the interaction between the retry ACNAC mechanism with the batch processor is one thing. Another example of complexity is when you have two exporters
bothersome messages.
I guess there are value strategies that could be implemented.
We could imagine that we just need one, and we… we send an app message to the…
To the producer of this information, or we need to wait for the…
The hack from the two exporters, then we can send back
act for the producer, the initial producer of this telemetry. So, what… what are the value strategies currently supported by the Go Collector in this specific situation?
**Joshua MacDonald** 52:07 That's this… well, that brings me back to this issue I talked about last week, which is called fan-out processor. It's like the…
internal… it's actually called a connector in the Go Collector, which is this sort of hidden glue between the receivers and the pipelines. For each pipeline, the export is sort of independent.
And, so…
because of the way the Go collector is configured, batching happens now. What we're encouraging users to do is to have batching happen in the exporter, in this helper, so that you may have multiple pipelines with data, they all end up in a single exporter, which is doing independent batching then.
And this legacy thing I'm talking about called Batch Processor is a way that lets you batch before you send to multiple destinations, which is really one of the reasons why people want to keep it.
And the point of my change that I browsed into earlier is that the legacy batch processor has never handled errors correctly, and it will after my change by using the new exporter strategy, which is essentially, again, setting wait for result true.
To enable back pressure, with error handling.
**Laurent Querel** 53:18 understood, but how that solves the fundamental problem that you have two exporters, they have some kind of values resistance to what you are sending to them.
But the… the receiver that was…
The system receiving data from… from a telemetry producer.
I need to determine when to send
AC or NAC to this telemetry producer. So is it based on the response of these two exporters sending AC, or a combination of AC-NAC? How that works?
**Joshua MacDonald** 53:56 Yeah, that's… that's more or less what I was trying to talk about in this piece of code that I linked to in the fan-out consume… the fan-out connector.
which is the place… the one place, the common location in the Go Collector where you issue a request by either copying it or cloning it into multiple pipelines, and then wait for all of them. There's no option anywhere to kind of short-circuit, I think, maybe what you're thinking about.
Or to, .
**Laurent Querel** 54:28 Hmm, we can.
**Joshua MacDonald** 54:29 But you can batch before or after, is sort of what I was trying to get at earlier.
an ACC or a NAC, and as long as the batch processors do the right thing, which they will, and they should, then you can, you can… you can imagine designing strategies for the fan-out
Processor that lets you have, you know, first success, wins, or, you know, like, what you… in order to be strict, you have to wait for all the responses, but…
You know, maybe, you know, you have some other policy in mind.
**Laurent Querel** 55:02 Yeah, definitely, depending on the situation, I think…
Ideally, I think we need to design a system where people can precise their policies and how they want this system to behave.
Because we could imagine that, some, some destination or…
could accept some, could accept losing some information.
But, let's say that you have a Kafkia topic that is, one of the exporter, but…
Kafka Topic, that is the destination, so you have a Kafka exporter, and on the lower one, you have,
Might not know, something like, an observability backend.
That is slightly, slower.
So you, you could accept that,
everything needs to be hacked by the Kafka exporter, but if we…
if we… if the Oxality backend is not able to… To follow the,
The current amount of telemetry signals, it's less…
it's a lower priority, because we can replace from the Kafka topic.
And, and then we accept that, we, we only, we have a policy where we have,
app that is mandatory for the Kafka exporter, but not necessarily mandatory for…
Probably to use Exporter, or whatever backend you are using.
**Joshua MacDonald** 56:28 Yeah, so you can imagine a kind of hyper-edge level configuration that says whether you must have or may have.
**Laurent Querel** 56:35 Yeah. Or, you know, would return. The way I've thought about that one in the Go Collector in the past is to separate the topic of waiting for the result from the topic of.
**Joshua MacDonald** 56:45 of, essentially suppressing the error result. So, you can have a separate feature called error suppression, which is to say, do you want to admit the error, even if you've waited for it?
So one thing you can do is have the… have the consumers that you don't care about failure for suppress their errors, and only propagate the errors that matter, in that sense.
**Laurent Querel** 57:11 Okay.
**Joshua MacDonald** 57:20 And sorry, my phone has rung, and I think now we've really reached the end of the meeting. Thank you all, and I would love to hear more about all this stuff on Slack. Thank you all.
**Laurent Querel** 57:31 Thank you.
**Joshua MacDonald** 57:31 Alright, see you next time.
**Albert Lockett** 57:34 Hi, everyone.
**Jake Dern** 57:36 Thanks.
**Danny Chin** 57:37 Thanks.
