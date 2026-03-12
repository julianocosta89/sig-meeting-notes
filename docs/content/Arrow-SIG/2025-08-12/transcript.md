SIG: Arrow SIG
Date: 2025-08-12
Duration: 63 minutes
Zoom Recording URL: https://zoom.us/rec/share/1b4a60JKwedKPBA7n2pfHiU06xcDVnEiyp-YJqsvEl3XVt5pDZIU14nHOOULExR-.nOvsfQDg7eQC5HJy
============================================================

## Zoom Recording Transcript

Laurent Quérel 00:01:47 Cheers!
I was creating a new entry into the Google Doc.
So, in the angenda, I just put one topic.
But I'd like to discuss on my side, … Okay, so… Jack, I'm sure maybe you will have also your own, topics.
Trying to think about all things.
jmacdonald 00:02:31 Yeah, I didn't have a great deal of agenda for myself today, having spoken with you directly about the topic of rate limiting, and I can… I could fill in a little bit for the agenda.
We… we might go ahead and look at our issues list. How's that sound?
Laurent Quérel 00:02:48 Yeah, sounds good.
jmacdonald 00:02:49 Alright, I'll bring… I'll bring it up.
Laurent Quérel 00:02:52 It's….
jmacdonald 00:02:58 Okay. Yeah, today Albert will not join.
Laurent Quérel 00:03:01 Oss… as some constraint.
And on the F5 side, … I don't expect any winners today.
jmacdonald 00:03:14 Well, let's, maybe keep it short.
Laurent Quérel 00:03:17 So yeah, why don't you… why don't we take a look at the issues? I've got them here.
jmacdonald 00:03:22 … I… since Drew's not here, I won't bring up, I won't… I won't go into the topics that I know he and this, fellow Blanche are working on. We can do an update on that later. So… so my… so let's see.
… you have created an issue called Rate Limiting Component, and I also have one called… Somewhere, I can't remember. … Oh, this was in the milestones. So, sorry, the complete list… of issues….
Laurent Quérel 00:03:58 You can join the milestone from the issue. If you go back to the issue, there is an icon Milestone, you click on milestone, just on the, on the right.
Yeah, well, maybe that's another way to do it, okay?
So, go back to the… to the list of issues.
jmacdonald 00:04:22 Okay.
Laurent Quérel 00:04:23 And then, just, close to the green button, new issue, there is milestone.
Click on it, and then you can click on the demo, and then you have the full list.
Maybe there are better ways to do that. Okay. That's my way to achieve that.
jmacdonald 00:04:42 And I know… the reason why I was briefly confused is that I know I filed my own issue about rate limiting, and I don't see Where it went, but… That… that's okay. Just… just… I think it's enough for me to say that I am, in fact, working on a rate limit design. I have been working on this rate limit design for a while, And… Let's find me… Because I'm not seeing it, so….
Laurent Quérel 00:05:14 Alright, great, and memory limiter framework, that's the one that.
jmacdonald 00:05:17 There it is. Yeah, so I put this in, and then I can put this in, a milestone.
Laurent Quérel 00:05:24 Yeah.
jmacdonald 00:05:25 There we go. Okay, … So, back to the milestones, … Apologize for my tool troubles.
… So, I would say it looks like, for the most part, we have No new issues, that's good, except I'm not sure why we're not seeing the one I just put in.
Oh, there it is. It's in reverse order.
It's changed.
Let me change that? Okay.
I will do.
Then we probably need to do some cleanup, maybe the right limiting component could be just….
Laurent Quérel 00:06:12 Maybe removed, and we keep the, you know.
jmacdonald 00:06:16 And how does this task? ….
Laurent Quérel 00:06:21 Off….
jmacdonald 00:06:21 Complete.
Laurent Quérel 00:06:22 It's just because I tried to, to use, GitHub postscript, as much as I was able to do.
jmacdonald 00:06:31 Gotcha.
Laurent Quérel 00:06:31 To organize the project, but honestly, the task part is not the most useful one. I think that what is more useful is assigning to a milestone, assigning a label, so we have a good understanding on We can basically, filter by labels if we need.
But the… the task part… I'm not sure it's super useful.
jmacdonald 00:07:00 So, anything… that you'd like to call out here? You know, I don't really have much to say more about rate limits, other than that I've been looking at it for a long time.
Laurent Quérel 00:07:10 Yeah, so, so, maybe what we can just mention regarding the rate limit is… you are working on, A complete solution for the rate-limiting approach.
jmacdonald 00:07:22 Pretty much we rebuilt.
Laurent Quérel 00:07:23 I were to apply to the… to a pipeline, or to a branch of a pipeline. The only thing I'd like to highlight is… something very basic and intermediary that we achieved into the fake data generator.
There is a very, very basic, … concept of… Not rate limits, but, … signal per second configuration in the fake data generator.
That will be replaced by your rate limiter, or a more generic approach, but right now, because we don't have it, and we know that it's a complex piece.
With a lot of implications, like we discussed this morning.
… In between, we will have a signal per second parameter into the fake data generator. That will do its best, and that will be good enough for the traffic generation for the next following weeks.
And if we have the rate limiter, fine. If we don't have it, we have a… an intermediary solution.
jmacdonald 00:08:33 And do you have in mind that we will implement a rate limiter to be precise, and then basically create a surplus of load to produce more load than the rate limiter will allow, and then just.
Laurent Quérel 00:08:44 Yeah, I think that's something we will, we will test also, indeed.
… Especially because we, we, … with this threat limiter, we… I mean, what we discussed… What are the policies when we reach the limits?
do we drop? Do we, … send the surplus to some other destination? Do we do some sampling?
… So the… this kind of policy attached to the rate limiter.
Has to be tasted, like you said.
….
jmacdonald 00:09:28 Yeah, that makes sense. … I… so, yeah, the big idea that I've been grappling with here is that we see this pattern emerging in the sampler, as you say, in the batch processor, you know, like, perhaps you want, you know, and we see it again and again.
perhaps we should, if we're going to invent a rate limiter, follow an existing model, and then try and apply it backward to those other things. So, having a sampling component.
is nice, but first I'd like to talk about batching or simple partitioning or something like that. And rate limiting will serve, I think, as a good foundation. So, yes.
Laurent Quérel 00:10:12 Yeah. I just added the back pressure, because the default behavior will be back pressure, then we could say.
A drop policy, or we could say a redirect policy, or whatever.
jmacdonald 00:10:24 Cool. Yeah, and so, as you know, I'm starting to learn the… effect handler and the pipeline engine, and so on. So I will be… I will be continuing on that. Thank you.
Laurent Quérel 00:10:34 Yeah, and … and like we discussed.
There are a lot of things missing in the engine.
to achieve some of that. So, … We will make progress on both sides, both in the engine and into this rate limiter.
That will, ….
jmacdonald 00:10:54 Great. This does fit with my understanding of what I'm trying to build, so I will be back with more.
Laurent Quérel 00:10:59 Okay.
jmacdonald 00:11:03 Whoa. Okay.
This Numaware client stuff.
Laurent Quérel 00:11:07 Yep.
jmacdonald 00:11:08 Ukarsh has his hand. Hi.
Utkarsh 00:11:10 Hey, hi, Josh. Hi, Lauren.
I also… I mean, I saw your chat, on the Slack channel, Otolerodev, and I was wondering, like, has that also been decided upon? Like.
Laurent mentioned that since we're using SREU support, we either Assume that every… that the load is uniformly distributed, or we have, like, a global… … config of sorts, where we can see, like, if the rate limiting has to be applied per Core level, or, like, at a global level, so did we….
Laurent Quérel 00:11:43 Yeah, yeah, that's definitively a discussion we started also with Joshua.
And it's… it's in some way related to the… the next topic, the… It's not well documented in my, agenda, But the telemetry framework, on which I'm working.
Will be also a way to… Keep track of some global metrics that could be used for different purposes. One of them could be what you just said. If we… if we need to keep track of a global Number of message that we observed.
And use this, this information For the different per core pipeline.
So we will have some kind of internal feedback loop that we could reuse Right now, we don't have that, so the… My suggestion was… Let's simplify the problem.
Consider that, right now.
At scale, at least, we should see some… Relatively good, balance among the values Coral?
And… and we can just take a chocolate and say, the rate limiter will basically write limit For each… locally for each pipeline, divided by the number of core. Or, I mean, the number of core where we effectively instantiated the pipeline… pipeline instances.
That will give us an approximation that will be, in my opinion, if things are relatively well balanced, good enough to begin with, with the benefits of zero synchronization communication.
The zero communication, effectively, between cores, which is a very nice… property as well. But, for some more advanced, or… Situation where the balance is not, a guarantee.
then we could fall back to what I just discussed, using a global metric that is maintained effectively into the system.
And, and then apply these, … A global weight limiter.
Utkarsh 00:14:09 And I know that, like, when you wrote that load balancing doc, you had suggested using eBPF as a way to, like, a server-side technique to do effective load balancing, maybe?
Laurent Quérel 00:14:21 Yeah. Even rate limiting can happen through an eBPS.
Yes.
Utkarsh 00:14:26 Right?
Laurent Quérel 00:14:33 To some extent, maybe, yeah.
Utkarsh 00:14:36 Some of the writing need to interpret the, ….
Laurent Quérel 00:14:43 need to interpret the content, the messages, it's not just staying at the TCP level.
But I think we could imagine some interaction … leading to some action that could be done at the ABPF level.
Based on information provided by the rate limiter.
I mean, it's probably something more advanced that we can imagine later is.
Utkarsh 00:15:10 Okay, so we are maybe looking at rate limiting based on more than just the IP and like, the source IP and, also looking at the GRPC-level details, basically? Is that what you're saying? Like, we might have to… Our rate-limiting logic has to, like, parse the actual… data in the… passed in the gRPC payload.
jmacdonald 00:15:34 I would give… I would give you, sort of, that I've been doing this research, and I don't quite have a report yet. I have a draft internally, but… Looking at how Envoy has addressed this question, what we see is that there are limits built in basically everywhere in the system. Like, you're going to find low-level limits about the rate of new connections, and you're going to find intermediate like, limits on the rate of new requests, perhaps, but then once you get to the actual HTTP handler route path, you're… you've got an HTTP request object at that point. And the design that I'm pursuing would be to kind of emulate that. There's this notion of a… … A rate limit request, which is a sort of key value set that has been derived from the request somehow, and the idea would be that each route has its own way of deriving these rate limit requests.
The, Envoy model is quite sophisticated in allowing for, both to encapsulate, kind of, like, per tenant details, like, I can have a rate limit for one tenant that's different from the default, and I could also encapsulate multiple types of rate limits. So I could have a user-wide limit, I could have a, like, account-wide limit, I could have, like, a machine-wide limit.
And those can all be applied in a user-defined sequence. And then they also… and there's a concept that I'm actually leaving out called stage, which is… which is like a way to have completely orthogonal rate… rate limits defined. So you could imagine having a limit that was by resource count.
Where… or you can imagine it being by, some other details. … And, so that's the kind of capability that's built into Envoy.
And I'm basically going to be proposing that.
For… for us.
It's quite sophisticated, and that there's a built-in, like, kind of expression that's conditional before you… Assign the rate limits.
Utkarsh 00:17:35 Okay.
jmacdonald 00:17:36 The other aspect of that design that I'm following is this global and local… is… is something that you can't imagine. So once you've defined a rate limit request and put it into the context, it's going to go through multiple stages of rate limit, or multiple filters, as they're called, in Envoy.
And the idea is that you apply a local limit first, because it's cheaper, and that's just to insulate the individual core from becoming saturated by one, you know, user, maybe.
But then, as you get through the core and the local rate limit, then you can again go to a global limit. And in the envoy setting, global means making an RPC to a coordinator somewhere.
But in our example here, I think you can think of global as being That version that takes the sync or the send, and, you know, sends to a multi-threaded coordinator or something like that, at which point you're doing global balancing, or global rate limiting as well.
So it's all a framework, that I was… that I'm sort of imagining we will propose, and you can have local and global limits.
Using the same request. That's sort of the key of this design.
Laurent Quérel 00:18:43 Yeah.
Utkarsh 00:18:43 Thank you.
Laurent Quérel 00:18:44 And what I like with this, rate limit, … component that will exercise the engine in many, many directions.
The fact that you said that, we… we could imagine a global a write limit mechanism that will be applied globally for the process, where we… we run multiple instances of the same pipeline on multiple cores, but we could also imagine across, like, a distributed version of it.
It's a distributed global, rate perimeter.
Where we have some kind of orchestrator. That's another dimension where we also need to specify some interfaces … So people can extend that, … Yeah, there are so many things, beyond this threat limiter that will exercise the… where we will definitely see a lot of missing pieces in the engine. Right now, it's fairly basic.
Even if there are some parts that are not basic at all.
But, a lot of, … Control mechanism or simplistic.
jmacdonald 00:19:57 Yeah, some of the details that I'm still kind of hoping to achieve and haven't quite sorted out yet are, … actually, I'm taking inspiration from the Go Collector SIG right now, which is doing some work on partitioning in the batcher.
And I think that, ultimately, the batcher is where this thing gets the most complicated, so we'll get there. But one of the cases that I've been thinking about, sort of, in the last day or two, is having, I think, understood most of the other problems involved in this space is that we want to be able to rate limit by resource, so that, like, if I see a batch of requests that's been aggregated by an agent somewhere.
contains multiple resource values, and I want to have some way of saying, I'm going to separate the resource by something about the data, whether it's the scope variables or the resource variables, so that I'm gonna have data coming into a, like, a buffer, which is hopefully the engine's queue channel, and I'm going to be able to, like.
split it apart by some function, the partitioning function, which then produces, like, multiple fragments, which I can then independently rate limit.
by the data, And I'm… I guess I'm comparing and contrasting that with how we might achieve say, a rate limit by the number of logs per resource value, or, you know… like, in the Prometheus world, just to keep it simple, you've got job and instance, and job is the name of, like, your task set. And so, like, I would want to be able to have… A rate limit per job, … And therefore, when I get one OTLP payload, I'm going to look at the top-level resource, find the job identifier, and then split it, and then each job gets its own independent rate limit.
Do I put that into the rate limiter, or do I split the request physically I'm not sure I know the answer.
Laurent Quérel 00:22:02 Yeah.
Do you want to add something, Josh, regarding the rate limiter?
jmacdonald 00:22:13 That's about what I have. I think… My hypothesis now, and it's getting complicated, it's been… keeps getting more and more complicated, but the hypothesis is that there's some sort of shared conditional logic that is a filter configuration, or a sampling configuration, or a partitioning function, or a rate limiter. And there's, like, there's a logical layer that's how you decide which Outcome you're going to take, and then, sort of procedural layer that says what happens when you take those actions, what happens when the matching occurs. And hopefully, we get to a place where You configure your rate limits the same way you configure your sampler limits, the same way you configure your batch limits.
And the application is slightly different in each one of those cases, but we don't have to learn a different language each time. That's the hypothesis, is that OpenTelemetry would adopt this as a, like, filter configuration standard.
Laurent Quérel 00:23:14 Yeah, I agree.
jmacdonald 00:23:16 Complicated.
Laurent Quérel 00:23:16 Good idea. Yeah, complicated anyway.
Okay.
… So, if there is no other additional question regarding the right limiter, I can talk about the… the other topic, I am.
added today in this agenda, … So… I think we discussed in the past the fact that we need, … a way to report telemetry, and I'm focusing right now on metrics.
Similar approach will be used for span and logs in the future, but right now, I'm trying to… to, … To investigate, to explore, how to report metrics.
Efficiently when we have a thread per core approach and share the same architecture.
… And, so we can't use directly the Rust, in my opinion, we can't choose directly the Rust, open telemetry SDK.
We will use it, more as… A crate that will be used in… A component that will collect from the multiple core aggregating matrix.
And then we will use the Royce Clarent SDK to report them to whatever destination we configure.
But, … In the pipeline themselves, in the node, more specifically in the node that are running in different cores.
We need something that will not, involve Any, synchronization mechanism.
So the… I did some research also, and … The usual approach to sub that when you are in a straight poker approach, And… Some more advanced solutions are also taking into account the fact that when you are running this kind of system on a server machine.
That is relying on a new architecture.
So numerous architecture is, in fact, a hierarchy of… so you have a set of cores attached to what we name a pneuma node.
The pneumonode is attached to a memory.
So each core inside this human node, in fact, stores or can access directly and efficiently to this, memory, space.
that is attached to the human node, and you could have a server with multiple of those three modes, so you replicate the block I just described multiple times, and there is an interconnect… there is interconnection between those two modes, but The latency property is different, obviously, when you reach an information that is Attached to your local memory versus, you reach something that is attached to the memory of another human node.
Obviously, the latency is much higher when you reach the memory of another human element. So… Right now, we have a controller that takes a pipeline configuration look at the quota definition, how many cores do we want to use? If it's zero, we use all the available core, and the controller is basically creating one native thread per core.
that are requested.
And pin the thread to the specific core.
The next step, and it's not yet done, the next step will be to pin the memory region Corresponding to the niemann node of the corresponding core.
So we have a perfect, alignment between a core and the memory attached to the pneumonode.
So the metric system that we have to implement has to be aligned with that.
So we, we have calls, And the corresponding native thread.
Each of the nodes running into the pipeline will maintain contours, and they will not be atomic contours, they will be just basic contours.
They will update that, and sometimes they will receive a control message saying, oh, please snapshot… create a snapshot of the local matrix.
And… and report that. And that will be aggregated to a first … Stage, that will be the new man node aggregation stage.
And then we will have a global aggregation in order to That will be across limited node in order to reduce, at the maximum, the number of exchanges we have to do to get a fully aggregated view of the corresponding matrix for all the nodes.
So, that's the best way to minimize communication across NUD and across LumaNUD.
And this global aggregator will be the one that will use the… The open telemetry roasts SDK to report the aggregated metrics to whatever, destination we decided.
to, to send those metrics. So that's one thing.
The signal, … element, the TypeSafe API, that's a discussion we had many times with Joshua in the past, and that's obviously a discussion I had also with people working on Weaver.
And I'd like to explore this space at the same time.
Because I think that's… first… … Will give us ways to optimize things.
And, for me, it's a way to do… to solve two… I mean, to work on two projects at the same time, and validating that what I'm doing is… is, valuable, not only for us, but also for the direction that we are taking with Weaver and this schema-first approach.
… So, what I did is… I created a new crate. It's not yet, integrated into the, into the… it's not a PR for review rate yet, it's still in the private branch. But I created a telemetry crate.
this telemetry crate right now is done manually. I mean, it's implemented manually.
Inside, we will have stripped, Rust stripped, representing multivariate matrix for a specific node, so… The first example on which I'm working is a list of metrics that will be generated by the Perf Exporter.
We could imagine that for A nodes into the pipeline that we have.
So we will have a street where each field represents a different metric, but each of those metrics are part of the same multivariate metric group And they use the same set of attributes.
And the same time zone, they will connect it at the same time.
Now, we know that OpenTelemetry is not supporting multivariat matrix, so… if we are reporting those multivariate matrix with the Rust, SDK, we will translate them automatically into Univariate matrix. That's fine. It's not optimal, but it's okay. If we expose those multivariate matrix, let's say with an HTTP endpoint.
that the data flow engine could expose.
We don't have to do this transformation, and we could represent a single set of attributes with all the multivariate metrics, that would be optimal.
And that's what I want to achieve. So these telemetry crates I will code manually the struct, but in fact, this telemetry crate will be automatically generated at some point by Weaver.
We will take a schema-first approach, so that the semantic convention describes the metric, saying that both metrics are part of the same group.
And we will use Weaver to generate, in fact, this entire telemetry crate that will, behind the scenes, will rely on the Rust telemetry SDK.
And potentially with an HTTP endpoint to, like I said before.
So it's like a multi-stage, set of modifications, so I will start with a basic PR, where everything will be, Manually created, and we will progressively go to a schema-driven approach.
So right now, my focus is more trying to get the best possible approach to minimize the override when we increment contours.
Knowing that we are in a suite-per-core approach, and taking into account the NUMA, and having a NUMA-aware approach also to maximize, or to minimize the communication across team management.
Sorry for this longer discussion, but ….
jmacdonald 00:33:04 This sounds good. Can I ask a few questions? Let's see. Sure.
Is there a way to get from this representation directly into the OTAP representation. I know that Jake has been interested in multivariate representations. Is that where we're heading?
Laurent Quérel 00:33:22 Yeah, I think that's, that's one of the multiple stages that I didn't mention, but, definitively, we… … Right now, I'm… I'm trying to solve short-term issues. One of them was, okay, how can we use the perf exporter, and also the fake data generator that we already have.
And use them as a traffic load generator and as a way to measure the efficiency of what the system under test.
We need to import metrics.
So we have the mechanism to generate traffic, we have the mechanism to internally, but we don't have anything to report the metric.
So I'm… I'm… Using that to… Investigate how we can achieve a very good metric infrastructure.
Compatible with the… The approach that we are following.
First set, find a nice way just to export those metrics so the… the benchmark infrastructure on which Chris is working will be able to leverage that and collect the information.
… And… and then we will, go in multiple stages, integration with the client SDK from the Rust Client SDK for OpenTelemetry, leveraging the fact that we have natively multivariate matrix, and translate that into an OTAT representation To demonstrate the potential improvement, if we have a fully, a native support for multivariate matrix. But that's the… an initial step that will be, followed by many other things.
And an additional stage is, how can we leverage This efficient telemetry system To maintain global contours, or global metrics that could be reused as a feedback loop.
jmacdonald 00:35:29 Yeah.
Laurent Quérel 00:35:29 Directly, in the nerd themselves.
So, for example, the rate limiter could leverage that.
jmacdonald 00:35:37 Yeah, okay, so I'm understanding. I think it's, like, playing devil's advocate, I think there's probably a question or two about why we're not just improving the OTel REST SDK, which is gonna… the good answer is we might do that later, if we find a good solution to this problem.
Laurent Quérel 00:35:55 Are you? Yeah.
jmacdonald 00:35:56 But, however, I know that implementing metrics is hard, so does Ukarsh, and, to get the, like, efficient… the, like.
The performance that we've… often reached for as implementors is hard to achieve without having what we call a bound instrument API, where you kind of, like, declare your attributes somehow.
hopefully statically, or at least once per request, and then, like, use that attribute set again and again. To me, the hard part of a metrics SDK is to do that very efficiently, because we know that atomic increment is… especially when you're in a fed-per-core environment, the increment is cheap. It's finding the thing you want to increment that's hard.
So… so… so anyway, I'm looking for reasons why we can't just use OTel at Rust. That's my kind of, like, background question for you.
Laurent Quérel 00:36:49 So, for me, the… I mean, the client SDK is not designed to to be perfectly aligned with a very, very specific design, which is thread-per-core Luma-aware architecture.
I mean, there is no concept of, on which core, which luminode, on which memory we are running in the client SDK, and I'm not sure that that will really make sense to go in this direction for a generic client SDK.
So that's why… I mean, I'm obviously not against it, I mean, it's… if we can derive, … interesting things from this exploration, directly put that into the generic land SDK, why not? But I will be surprised if… Maybe we could imagine a mode for the client SDK that is Numa aware, but I don't think that will be the generic version of it.
So, and I think, right now, it's better for us to obviously rely on the client SDK, As much as possible, especially to export things in various formats.
But, I don't want, personally, to… limits… the performance of the engine, just because we want to use the client SDK at any stage. I think it's normal… I mean, that's also true for any application we're using, in fact, the client SDK. They can decide at which level they want to use the client SDK.
… And for some very high-performance sensitive solution, maybe they just will do their own stuff, and … and they will have some aggregation points. That will be connected to the client SDK, not necessarily directly on the odd pass.
jmacdonald 00:38:49 Okay, not a problem. I, I think we should look for ways that OpenTelemetry can evolve once we learn what we need to do.
Laurent Quérel 00:38:58 Yeah, I mean I think it'll definitely be an exploration, … On this side, and, and we will probably find some interesting, Learning from that.
jmacdonald 00:39:14 Ukarsh.
Utkarsh 00:39:16 Yeah, so, like, I think we've… Like, discussed this part before as well, like… like Laurent mentioned, like, SDK is not, designed with like, knew my awareness was never, like, … thing when developing the SDK. And… the workaround, which I think we… yeah, the workaround which we suggested before was… every thread, on each core will… like, how today it creates its own instance of Tokyo Runtime?
… its own dedicated runtime instance. You could… create your dedicated SDK instance. So then, you have, like, 8 cores, so you have, like, 8 SDK, metrics SDK instances.
And there should be, like, a way to, like, implement, like, a custom pool exporter or something, so that you can merge those values coming from the different threads.
… Periodically, yeah, maybe, like, Have some timer that sends a control message, which… Triggers the pull exporter to do something, maybe, but yeah, until we do the implementation, it's tough to tell.
… Also, I feel like even though those things include, like, atomic increments and all of those things.
If… There's only one thread updating the actual, like.
cache, CPU cache, and everything, and nobody's reading from it.
There's no contention. It should be… … Like, fast enough for most cases.
But yeah, I mean, given our… Focus on performance, maybe, yeah, we can definitely even get rid of the atomic increment, but… Yeah.
Laurent Quérel 00:41:01 Yeah, and also the, … This fruity variet, … Metric concept that will be all over the place in this system.
As, as some fundamental implication.
Ideally, I'd like to be in a situation where I just report a set of numbers.
For all my matrix.
And share the same attributes.
And not be constrained by… Not having any constraints regarding the fact that, unfortunately.
the open telemetry metric model does not support those metivariate metrics. And then, if we use the client SDK, which obviously does not support multivariate metric. We will add additional overheads that are honestly in contradiction with what we are trying to achieve. So that's why I really think that, for now at least, and I think that could be a very nice demonstration to do at… for some folks, part of the open telemetry community.
So, the real benefits of having Multivate Matrix natively supported.
And the impact on the performance is, in my opinion, massive.
And showing that, and then trying to encourage those communities… this community to move And adopt a multivariate metric model, a native multivariate metric model, and then we could maybe, at some point.
reconsider the client SDK integration and move it a little bit closer to the… to the odd pass, but right now, using it to what I name the cold pass, so that this, single aggregator receiving periodically pre-aggregated stuff from the odd pass.
I think that's leveraging the Rustparent SDK for what is the… is really, I mean.
It's well done for this use case, and already integrated with, A lot of configuration and possible destination.
… And, and use this, this experiment to demonstrate multivariate, demonstrate, a schema-driven approach.
And… and reduce, at the maximum, the… Override, values type of overrides, and… and… Also, exploring a new malware approach.
Which is very specific to what we do.
And not necessarily… Applyable to a generic case.
jmacdonald 00:44:01 This is great. I don't have a… I really don't have a problem. Let me ask a few more questions out of curiosity, though.
Do you see, these multivariate metric, metrics as events, in the sense that, you know, you produce one metric multi-event, which is a timestamp, set of attributes, and then a set of key value… metric name-value pairs. … Is that… is that just, like, a recorded sort of line of data that goes out into the, sort of, stream of data? Or is there, … Or is there, like, within, like, a short period of time, are you taking multiple counts and accumulating them together?
inside of each of these per-core areas, I mean, to say.
Are you actually doing any aggregation, or are you just outputting events?
Laurent Quérel 00:44:59 I think, … so, let's use the example of the perf exporter.
the Perth Exporter… We'll maintain multiple contours.
I mean, all is to run.
whatever. The type of matrix doesn't really matter, but it's safe to simplify, maintain multiple contours.
One will be a number of batch received, one will be number of Metric signal, log signal.
spell signal. And the list of metrics that we can maintain in this Perfect Exporter could vary, but let's say, at the minimum, we have these three.
men, … metrics.
They will be part of a single multivariate metric.
when I say that is… Each data point, we… we will have four Contour values for the same type stump.
And for the same set of attributes.
That's from what I name a multivariate metric.
So there is no duplication of attributes, there is a single timestamp, and there is multiple value for the contours, one per metric type. I mean, not… One per, immediate metric, part of the same multivariate set.
… So now, … I compare that to… if I'm reasoning in terms of open telemetry, telemetry model.
Right now, we have… realistically univariate metric support. We have logs, and we have span, and we have profile.
We should introduce multivariate metric, to this mix. … But will be defined, in fact, as a collection of univariate matrix sharing the same set of attributes.
and the same time slot. When we collect that apprent.
There is multiple data points with the same timestamp, the same set of attributes.
And, and right now.
I need that for the… for the sake that… in fact, we need that for every… close to every node. I could generate independence, that happened, but… We will end up with a lot of duplication.
The attribute and the time slot.
jmacdonald 00:47:35 So, no, I buy the part about multivariate metrics. I'm still trying to understand if there's, like, a… … the challenge that I always find with metrics SDKs is the… is I'm trying to answer whether this gets re-implemented again, which is the part where you say, I just received a message, I'm the… I'm the perf… exporter. I just received a message, I'm going to… I'm going to count how many Items were received according to this message type.
and then I look up… Somewhere in my three-dimensional metrics, in my attribute space.
the counter.
Laurent Quérel 00:48:13 So, so the attributes….
jmacdonald 00:48:16 I mean, I don't know what the attributes are.
But somewhere in my attribute… the hard part of being an SDK is to say… to dynamically take a set of attributes and find that row.
Laurent Quérel 00:48:27 Let's see.
jmacdonald 00:48:27 increment a thing. I know how to increment, it's finding the dynamic row.
And one way to avoid that is to just treat every row as a singleton. I had an event, I spit it out. I had an event, I spit it out.
And you can get around that by, like, I kept all my counters in a struct, and then I incremented them, and at the end of a period, I output my struct with its 10 counters.
And then… then it's… like you said, it's going to be simple, and later on, we can do, I think, an OTAP frame from those 10 counters, plus the timestamp and the attributes.
Laurent Quérel 00:49:04 Yeah, so, … Regarding the attributes, that's not something I… I discussed, but you… now you re… you are reminding me something I had in mind related to what you just said.
So not only we have multiple metrics sharing the same set of attributes and time stone, but inside the attributes, we have two categories of attributes.
In my opinion.
We have attributes where the values is none.
At the construction time of this multivariate metric.
Example of that.
For the fake… for the… the perfect supporter.
the… the new manhood ID, the core ID, the process ID, the name of this node in the configuration of the pipeline, the pipeline ID, these five, attributes.
Are… not changing.
over the time, once, at least for the same reporter, so for the same NUD instance, the same perfect supporter.
instance… These five attributes are fixed at the beginning of… when this node is constructed.
So, we should be able to, declare to this new type of SDK that those 5 attributes, okay, they are none during the runtime.
But at the difference of other type of attributes, they are constant. Once they are Define and set to the… To represent this specific instance of the metevite metric, they no longer change.
And sometimes it's enough. So for my specific case, for the Perf Exporter.
by default, I just need that, and that means that this mechanism of reporting that happened very efficiently I will know… I will never have to transmit the value of those attributes for each attachment. It will be done only one time at the beginning, initialization time, and done.
And then we just report numbers, super fast.
As opposed to… what we could name, contextual attributes, or dynamic attributes, where… contextually, based on the P that I will receive.
Maybe we will have a tenant ID. Maybe we will have, I don't know.
Whatever information that we can derive from the incoming messages.
Then, if we need this type of, demo… dimension, To… to do some analysis.
… then those attributes are contextual, and they will be reported, and that's where we enter into a more complex situation, where we have to do some aggregation per set of dynamic attributes, or contextual attributes. I'm not going there for now, but I totally understand what you are seeing. In fact, we have two types of attributes, and the client SDK ideally has to take that into account in order to To get the maximum performance we can get.
Depending on the situation.
That's… well aligned with what you have in mind, Joshua?
jmacdonald 00:52:38 Yeah, I've definitely seen that pattern. I know Prometheus has a concept of a constant attribute to match what you said.
And, right, it's the second category, which is where the hard part arises for most metrics SDKs. In the first part, one thing I will say before I ask Utkarsh his thoughts is that OpenTeometry has sort of flirted with the idea of lifting certain constant attributes into the scope.
It's been brought with challenges and sort of, like, legitimate worries.
Since the start, but the idea of, of, of having A scope instance that has some constant-valued attributes in it.
and then has a container for simpler metrics is one idea that exists, and it doesn't get you all the way to multivariate metrics. It just gets you some reduction of space in the univariate reporting scheme. So you're still repeating your timestamps, for example, and … But it's something that you can imagine. In some sense, when you have constant attributes, it's very much like the bound instrument case that we've talked about, but it's like a singleton, so you've got… you could have 20 counters in your struct.
and one attribute set that's constant. And then, basically, the API doesn't involve attributes at all at that point.
Until you get to your local… sorry, your sort of secondary place where you're aggregating those structs, now you have to look up I suppose you've ensured statically that the constants do not overlap, so aggregation is just concatenation when you have non-overlapping constants.
Laurent Quérel 00:54:24 Yeah, interesting.
jmacdonald 00:54:30 Well, I look forward to where this… where this goes. But Karsh, any thoughts?
Utkarsh 00:54:33 Yeah, I mean, I think you, said it already, like, so I lowered my hand, because I was also thinking along similar lines, where, like, within OpenTelemetry.
SDK, we have the concept of scopes, and also resources. So, like, the first things… if I were to model this whole thing as what we do with our Tokyo runtime instance, if we were to create a instance of Metrics SDK for each thread.
then… these static attributes, like numer region ID and CPU ID and all of those can act as… can be modeled as resource attributes for that SDK instantiation. And then, at that point, what you have, like, from a compute… computation standpoint, is effectively like a bound instrument, because then the SDK doesn't have to do the job of looking up any attributes, because Whatever attributes were related to the metric are constant resources, resource attributes.
So, we… within the SDK, there is optimization for measurements with zero attributes, zero dimensions at the time of reporting. So that path is well optimized, to just do the increment and not do any HashMap lookup or anything.
But, yeah, but then again, like.
It's not exactly multivariate, because we are gonna expect an instrument for each metric, but… I don't understand multivariate fully, but, like, from what it seems like, one instrument will be enough to act like a… act like one multivariate metric, is what … We're going for.
jmacdonald 00:56:06 I've… I've definitely studied this a little bit, so I'm writing in the notes. The idea of an instrument, a multivariate instrument, which is, I think, what Laurent is working on, is that you'd have an API, like RecordBatch.
And I'm gonna sort of mix my Rust and my Go right now. So you have your context argument, that's where the SDK has access to dynamic keys from the context, and then it's, like, attributes.
… are empty.
Because we, like… Probably, we did something like this. We said instrument, equals… meter provider.
I'm just gonna butcher this.get… … And this is the name of the scope.
And then it's like, with constant attributes, and then this is where I put NUMA, etc.
And then after… after I've done all the constant assignment, my… my… I have a multiple observation.
Where I'm… I'm… I'm… I've taken away attributes, but you could imagine it being derived dynamically. So, it's something like… it's like measurement… Metric, value, measurement.
So… so you do this three times, and now you have an event entering the API that's got one context, one… hence one timestamp, one attribute set, and then pairs of metric value. And OpenCensus had something very much like this.
And so, that's why I've looked at it a few times over the years. We never put it in OpenTelemetry.
And we talked about bound instruments a lot instead, but there is the concept of a multi-observation somewhere in the history, and we can bring it back.
Utkarsh 00:57:55 Nope.
Laurent Quérel 00:57:57 Yeah, the… knowing that, for the record batch, I'm not using what you… which you have on the screen. The recall batch, okay, there is this… constant attributes, and we don't have to report them each time we have a new set of attachments. But we could also have, in the multivariate context.
multiple measurements.
and… and… regular attributes.
But still, it's, it's still okay.
jmacdonald 00:58:30 Yeah. And the client SDK has to support that.
Laurent Quérel 00:58:35 And it's a major optimization, because then you don't have to replicate those attributes again and again for each attachment.
And the… and the aggregation beyond the scene can take that… can yield this, this fact… To avoid, to recompute the… the values look at, it's only one time.
Instead of n time for the n unilivariate metric part of the same multivariate set.
… Yeah, … Now, the discussion regarding resource versus scope versus, … those constant attributes I was mentioning, Beautiful.
maybe that's an… maybe that's a way. I don't know if OSUS is the right location.
Knowing that now with resource, I think we have OTT.
I'm not necessarily extremely familiar with the new direction we're getting on TT and resource, but I think we have to be careful there, because I think the attribute resources are now leveraged by this new RTT concept.
So maybe it's more scope?
I, I, I don't know, that's, ….
jmacdonald 00:59:57 I think what Akarsh was getting to was the idea that you could try to leverage the existing OTel Rust SDK as follows. Each thread in the thread per core design will use one OTEL REST SDK with a resource equal to, let's say, CPUID, and nothing else.
And then you'll have one thread, one SDK per core, and it has a resource, which is just the CPU ID. And then after you aggregate all those.
you are able to form the true hotel payload, which is combined of the 16 cores or whatever.
Laurent Quérel 01:00:31 But, so, so that means that on my, 60, 72, core machine.
on my desktop, I will create, 72, client SDK that will report on the circuit.
That's the… I'm not sure that's the ideal.
Utkarsh 01:00:49 72 client SDKs, yes, but, I mean, the reporting part, we have to manage, like, somehow we have to… Get them aggregated together.
Laurent Quérel 01:00:59 Yeah. Like, how you pointed out, and then….
Utkarsh 01:01:01 Like, the export part has to be managed, they can't be individually just… exporting, ….
Laurent Quérel 01:01:06 Yes, exactly. So that's why my other proposal was, let's do the… let's do the meteorite stuff and optimization for this threat marker, or blah blah blah, and let's just use the Client SDK, At the aggregation point.
For me, I don't see the advantage to use it directly on each call, because I also have the, the, the, the, the full, … view on what this current SDK is doing, and the potential impact that could have on my performance… And anyway, I can't use it as is because of what you just said. So, right now, I would prefer to use it at the aggregation point.
And support nicely the multivariate scenario.
At the core level.
Utkarsh 01:02:10 You're on mute.
jmacdonald 01:02:13 I… I like how you're using structs in this definition, the idea that it's type-safe, and that you can… that we can eventually imagine combining the engine, which… with its pipeline data model, and having a pipeline which is for these structs.
Of observations that include timestamp and context and multivariate metric observations in the form of a strongly typed struct that then, if you, if you will, you can imagine just directly computing based on To, you know, put in some, say, rate limit control based on history or, like, whatever you're imagining.
Laurent Quérel 01:02:49 Yeah.
jmacdonald 01:02:50 So keeping the pipeline structural and not OpenTelemetry's generic representation does make sense to me quite a bit. I look forward to it.
Laurent Quérel 01:02:59 Yeah, I hope to… to have a first version to move.
jmacdonald 01:03:05 Great, and we can, look at what the sort of future plans for integrating with Hotel Rust in the future. I promise we won't make a mess with Karsh. Thank you all. I think we're out of time.
Laurent Quérel 01:03:14 Yeah.
jmacdonald 01:03:15 See, you know.
Laurent Quérel 01:03:16 Which is?
Thank you. Bye.
jmacdonald 01:03:19 Right.
Utkarsh 01:03:20 Thank you all.
