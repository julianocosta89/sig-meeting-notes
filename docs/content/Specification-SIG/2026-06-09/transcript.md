SIG: Specification SIG
Date: 2026-06-09
Duration: 65 minutes
============================================================

## Zoom Recording Transcript

Reiley 00:00:22 Hey, Lauren. Hey, you both.
Laurent Querel 00:00:26 How are they? Hey, everyone.
Reiley 00:00:46 While we're waiting, if you haven't put your name on the agenda doc, please.
Hey, Josh.
What do you…
jmacdonald 00:01:05 Good morning.
Laurent Querel 00:01:12 Good morning.
Jack Berg 00:01:59 Hi, everyone.
Please add any topics you have to the agenda, add your name and estimated amount of time. If I remember correctly, we have a presentation today by Laurent about Apache, or OTLP Arrow.
So, that's gonna be a chunk of time on the agenda, but there should still be time for other topics as well.
Add your name to the attendees list, as well.
We'll get started in just 2 minutes.
So, I'm just looking at this agenda here, and CJO has a couple of topics, but is only available the first 20 minutes.
And it seems like we have enough time right now for everything, so unless anyone disagrees, I'm going to shift CJO's topics to the top of the agenda, and yeah, that way we can get to everything.
Cijo Thomas 00:03:40 Yes, that's check.
Reiley 00:03:42 Thanks.
Jack Berg 00:03:47 And… Why don't we get started? CJ, you want to kick us off about hotel clients' self-observability?
Cijo Thomas 00:03:54 Yeah, sure. I won't be able to share my screen, so whoever is sharing, just please continue. I think, Jack, you are doing it right now, yeah. So this is just continuing what we discussed last week and the week before, so there was an ask to add few additional guidelines outside of the main spec, so I added a supplementary guidelines for self-absorbability.
I think I have received some feedback, so mostly asking more reviews on this one, especially those people who have already implemented it in their languages.
But the main thing which I want to ask today is, it seems like to really complete this entire idea of self-observability for Each client, we need work across, languages.
semantic conventions, potentially in Weaver, and all of them are, like, already in progress. I think, like, a couple of years as well, like, I'm adding the very first event in semantic conventions for SDKs on top of matrix. There is some improvements for Weaver, there is some effort to stabilize the conventions themselves. So based on my experience with a similar project, which is also in my second agenda, I was asked to create a project first.
In the community report, and then take it from there. I'm still not sure, like, what criteria we use to decide whether we need a project proposal.
So that's the main question. If it's not required, we'll just continue whatever I'm doing right now. We don't really need to spend the… Effort creating the proposal, seeking sponsorship for that as well.
So really the question is, like, do I… how do I determine whether I need a hotel community project proposal and sponsorship for… The self-observability part.
Jack Berg 00:05:40 I see Trask is on this call, and, from the GC. Unfortunately, I'm not sure that there is, like, a hard standard for when something requires a community project proposal, and when it does not.
you know, I can go off examples, and I have some sort of, like, heuristics in my head. I think it'd be good to codify these at some point, but we haven't so far.
But, you know, some of the things that I think is of a project proposal is like, hey, are you looking to have a new meeting? Like, a new Zoom meeting and new notes?
And if yes, project proposal. Are you looking to work across, SIG boundaries? Like, are you looking to bring together people from multiple groups, to get together and talk at this new meeting? Versus, like, hey, is this just, like, a new initiative within an existing city?
If it's a new initiative within an existing SIG scope, just go with that. Don't, you know, ask for a community project proposal. And I guess, you know.
does anybody else have anything to add to that? Like, in this case, for internal telemetry, it does cut across SIG boundaries, there, like you said, there are semantic conventions involved, there's Weaver involved, there's SDKs involved, there's the spec involved, but up to this point, we've sort of just, like, accepted the fact that it's, like, cross-functional work, and just, like, let things progress asynchronously without, like, a dedicated meeting.
Do you think that that's… hasn't been, you know, enough? Are you trying to see a new meeting be added to the calendar to bring people together to work exclusively.
Cijo Thomas 00:07:26 So, I'm actually… Yeah, I'm actually trying to do the opposite. I don't want to request a new meeting or community project, because that takes away a lot of effort to even set up things, get people behind it. I actually prefer the way it's currently going. It's just background job.
But it is making progress, like, somewhat slow, but it's still making progress without taking up much attention from anyone.
So I'm just fine with the current way as is.
So I don't need to bother, like, so many people, and I'm already getting enough support from the prospective community. Like, Weaver folks are happy with changes, they are approving it, giving guidance, semantic conventions is progressing.
And SDK clients, like, it's, like, even before I started looking at it, it was already in place, so I don't think I'm asking for a community, new project or anything. I prefer to do it, as silent as possible.
Jack Berg 00:08:20 Okay.
That sounds good to me. Ludmila, since we have you here from Semantic Inventions, wondering if you have any sort of intuition or feelings about the, the stability of the internal telemetry semantic conventions? You know, do you have any intuition about how many implementations of those there are in, you know, just, like, how, I guess, like, solid the foundation is over there?
Liudmila Molkova 00:08:50 Yeah, so this, metrics were added relatively recently, maybe a year ago, and… but I think they were implemented, I think, in Java and Python, people can correct me. The, maybe in some other languages, Uchijo is implementing them in other places.
The most interesting question, I think, is that there are SDK self-observability.
And some level of similarity should exist for a collector.
It shouldn't be, like, completely disjointed set. The metric names might be different, the component names are different, but the general look and feel should be pretty much the same.
So, I think how we usually handle things like this in some conf, we start a stabilization project.
We don't really have to have a group associated with it, but we would like to see if there are existing instrumentations, and there are.
We would like to get some thoughts from Josh McD and other collector people who are familiar with the subject. I think, Josh, you wrote some document for the collector around this. And if everybody is happy with it, we can stabilize them. We definitely need to go through the open issues and, any discussions with any controversy, and either say, okay, it can be addressed after, or that it has to be addressed now.
Based on what I've seen, I would not… I don't know about any blocking issues. I would be supportive of starting destabilization in semantic conventions, and depending on our findings, finishing it pretty… pretty soon.
Cijo Thomas 00:10:33 There are, like, few issues which I identified, which I'll be sending PRs. I already did, like, a very small one last week. There will be some follow-ups. It's mostly, like, clarifying a few things here and there, not… questioning anything in general, it's just, like, a few clarifications, especially around, like, what to do if, certain conditions are met. Do we emit this attribute, or do we not… some minor clarifications. And I already looked at the collector one, and I… at least in my effort, it's… I've been might be spiritually aligned with that, not necessarily picking the same name, because collector already has a different set of names. So it's not, like, one-on-one aligned, but spiritually, they are defining the same thing, even descriptions, when to do what, those are, like, inspired from the collector's own.
metric. So, I hope that is good enough to be spiritually aligned, and wherever attributes are.
shareable, yeah, we can, but as of now, the semantic conventions are not used by Craptor. It has its own way of defining metrics, generating them.
And implementing them, so I can only try to be, like, spiritually following that, not literally following them.
Robert? Anyway, yeah, go ahead, forward.
Pellared 00:11:53 Can you hear me?
Cijo Thomas 00:11:54 Yup. Yes.
Pellared 00:11:55 Okay, so the only thing that I suggest, because this work will be mostly asynchronous, will be to create, like, some GitHub project, similar to what semantic conventions often do.
So it will be easier to track everything, and track everything, and have some kind of backlog. And CG, I think you can own this, you know, project, reorder things as you wish, and I think it will also help others help you, I don't think you'd be the only one who's working on this. I remember that David Ashpole was also working on this stuff in the semantic conventions, and… Maybe I'll be able to go past 12, yeah.
Cijo Thomas 00:12:32 Okay, yeah. Yeah, so this is, like, one step short of creating an actual community, like, proposal, just create a project. Okay, I can take care of that.
Pellared 00:12:41 Just a GitHub project, not Open Development.
Cijo Thomas 00:12:43 Understood.
Pellared 00:12:43 Exactly.
Cijo Thomas 00:12:44 Got it, got it, yeah. So that ends my topic. The next one is very, lightweight. It's, another thing which is trying to add a centralized benchmark for entire OpenLelementary HDK clients. It has started as an OTEP, But then I was asked to create a community project, which is also why I was stepping forward.
self-absorbability, do I need to do that part?
But at this point, the other one, the centralized benchmark, has, I think, 5 approvals for both the OTEC and the community proposal. So at this point, it's just waiting for someone from PC or GC to bless it. So I'll link the discussion, trust specifically tagged TC and GC. So all I'm asking is someone from TC and GC2 support, right? It can be done offline, but just bringing it to this group, if anyone has hands to support.
Please let me know. I intentionally made it lightweight. It also says in the community, we expect this to be a very lightweight thing. We don't really expect any active time commitment from TC or GC. It's more like a blessing of the direction, itself, not really any, actual work. Hopefully, it should be, like, close to zero for it.
But anyway, that's all. Thank you for considering my topic in the beginning.
Jack Berg 00:14:03 You were talking about the benchmarking.
Cijo Thomas 00:14:06 Yeah. Proposal.
Jack Berg 00:14:07 Right?
Cijo Thomas 00:14:07 Yep, yep.
Jack Berg 00:14:08 Josh McDonald, did you… I saw you had your hand up for a bit. Did… was that on the previous topic of…
jmacdonald 00:14:13 It was. Just because Lyudmila named me, I put a link in the side chat to the current documentation on the collector, and then there was a conversation that proceeded after that, which I think is… kind of highlights the major point here, is that we already have very well-established semantic conventions. They're already different.
This is going to, I think, be our first real test. Can we change semantic conventions from the SDKs and the collector in a coordinated and harmless way that makes users happy with tooling and choice at runtime that gives you the choice?
I think this is gonna be our big test.
Jack Berg 00:14:50 Thanks for that. So, a key part of this… the stabilization of internal telemetry then will be coordination between the collector and the SDK. So, yeah, a new test for working together.
Okay, so your other topic, CJ, was about this, the benchmarking project proposal. I just wanted to share some context. The TC talked about this in our last meeting. It was in… it was in the TC inbox, and so that prompted us to talk about it at our meeting, and this Riley for… this comment from Riley was representative of where we landed on this.
We don't have an issue with this in principle. We would like people to vote in their support for this project proposal by going and approving, like, the OTEP first.
So, we agree with you that it seems like it's, like, relatively small scope that, we could probably get away with just, like, an escalating sponsor rather than, you know, a guiding or leading sponsor. But yeah, so for anybody that's listening that wants to see this move forward, go review the OTEP on the specification and, you know, support that through your approval.
Cijo Thomas 00:15:55 Okay, thank you. Yeah, so I can also check with other six, to express their support in the roadmap itself.
Jack Berg 00:16:01 Okay.
All right, We let those topics go a little long, because we had extra time in the agenda, And so, let's move on to this presentation from Laurent and Josh about OTAP.
So, do you want to take over the screen share, or how do you want to do this?
jmacdonald 00:16:20 How about I introduce Laurent while he takes over the screen share? So, I'm pleased that we're here today, and I just wanted to give a little background for this project proposal for anyone who hasn't been you know, following. We began… you know, for me, this began when Laurent showed up at an OpenTeometry meeting, I think 4 years ago, 5 years ago?
roughly somewhere in four to five years ago, pitching the idea of a column-oriented protocol and transport mechanism for OpenTometry. And it perked my ears up at the time we were looking for improving the compression at my company back then, and it was enough to get started.
So then we did phase one, 23, 24, and then, you know, we're ready for the next phase a couple, a year and a half ago, and then we started that phase, phase two, and Laurent is here to tell us about the progress we've made. And I'm very excited, so please, why don't you take it over, Laurent?
Laurent Querel 00:17:18 Thank you, Rush, and I really won.
So, I'd like to introduce Joshua. I will talk very quickly about Phase 1, just as a reminder to, To, sorry.
Okay. To explain what is OTAP, and what we did in Phase 1, very quickly, one slide, and then we will spend the rest of the time on Phase 2.
So, OTAP stands for Open Telemetry Apache Arrow Protocol.
And, initially it was only focused on making the protocol more efficient, compressing better, basically.
So the… the… The nature of the protocol, it's a columnar IoT protocol, leveraging Apache RO representation.
We created another tab, 0156.
That has been approved, and we created a Go implementation inside the OpenTelemetry Collector Contrader.
And then from there, we validated this protocol on real deployment, and we measured, basically, a network bandwidth reduction of About 30% to 70%, depending on the signal, and depending on the… The tour of the… the traffic.
This improvement is compared against the OTLP GRPC plus ZACD compression.
of the Go Collector implementation for OTIP.
The main focus of this first phase was basically to improve the transmission or the transport of telemetry telemetry signal between two collectors.
And the traffic travers… traversing, basically, internet.
So, from the beginning, it's very important to understand that OTAP was designed as a trade-off, optimizing bus transport and processing. It's not only a protocol to optimize transport, it's a protocol also to optimize data processing.
So, in Phase 2, after discussion with the governance committee, the governance committee gave us the opportunity to validate the processing side of that design.
So, phase two is, basically asking a different question.
What happens if arrow is used not only on the wire, but as the representation the pipeline works with internal?
So this Phase 2, started in 25.
We just ended the Phase 2 now, and we definitively want to… we'd like to continue on that.
For the next… for the… the following year.
the rest of the year. So in order to create a realistic validation of this assumption.
which is, OTAP should be able to accelerate, basically, the OTAP processing. We had to create a new vehicle, and, for this experiment.
This new vehicle is named Hoteler Road de Afrongin.
So it's, like the name, mentioned it, it's a betafluent gene, so it's something able to Take incoming, telemetry signals Apply some processing on it, and sending that to different destinations. Very similar to the collector.
So the reason why we had to create a new engine is mostly because, if you want to leverage the full potential of Apache RO, you have, basically, to change the interaction model between what we name Pdata into the collector, which is A representation of a batch of signal.
We have to change the interaction model between PLATA and components. Components in that case are receiver, processor, exporters.
So instead of traversing an object tree, like we do in the collector.
we have multiple tables, it's a simplification of the regulatory, but it's more or less the model, and you apply some query on those tables, and then behind the scene, we use Apache kernel functions and data fusion The data fusion engine to apply those, small queries And behind the scenes, there are SIMD instructions set for optimization and processing of this information.
This engine also, was designed to really test and compare OTLP versus OTAP, which was also one of the goals for Phase 2. So we implemented a native OTLP, native OTAP, Pair of receiver exporters.
So internally, it's… everything is a tap, but when we have an OTLP traffic, we have to convert OTLP to a tap.
And we do that in a very optimized way. There is no intermediary, in-memory representation of a standard quota buff object, we just transcode OTLP bytes, To an OTAP representation.
We also, considered that it's very important to look at what we learned from the GoCollector from the other telemetry data plane, and obviously, high performance data system in general. So we used this opportunity to rethink the telemetry data plane, and With the goal to have something that is More efficient, more scalable, and, also being able to behave better under pressure.
So, to answer the first question, that we mentioned just before, we decided to split that into a smaller question.
With the OTAP representation, are we able to have a shipper processing?
Are we able to scale more, and are we able to have a higher throughput when we use OTAP end-to-end?
So the benchmark now. So there is 3 slides, explorative evidence, Sorry for that.
So the column on the left, is focused on measuring the impact Of data processing when The… the pipeline system is… Pulotap?
or, an OTLP representation.
So we have here OTC, that stands for Open Telemetry Collector, DAFE, Dataflow Engine.
receiving and producing OTIP traffic, and DFEOTAP Similarly, receiving and producing OTAP.
So the… you know, you have the… The first that happened are when we have an attribute processor doing one renaming.
And when you have foreign M's, so we see the evolution between the two, and we can measure, basically, the influence of doing some data processing On a stream of telemetry signal.
So let's start from the FEO tab. So, the first observation that we can see, when we have a traffic of 200 kilogs per second.
Each logs are about, 300 bytes.
So, the CPU overage on the Dataflow engine, when we have a search traffic, is a double 6.4%.
For the DFE or TLP, 48.
So the main reason why we see this huge difference, it's because OTAP is relying on Apache RO, and Apache RO is an in-memory representation That, does not require deserialization, serialization, encoding and decoding.
So basically, you will remove the whole overhead of… you receive something from a circuit, you have to deserialize it and create a representation.
That can be removed entirely.
And the second benefit, and that explains the difference between the DAP, OTLP, and OTC, OTLP, It's, the way that you represent the information in memory. In our case, we represent that into a collection of Apache Arrow Records, which are a collection of columns.
Each column is basically a big array.
And, independently of the size of the batch.
you will always have more or less the same number of allocations. They will be bigger, but you will have Maybe 100, 200 allocation maximum per batch.
As opposed to… the internal representation that we use into the GoCollector, which is a gigantic tree of small object. So the pressure on the memory allocator, the pressure on the garbage collector is much bigger.
And let's explain the difference between these two later points.
So now, when we… we add more and more, rename operation, What we see is… close to no, impact. There is a slow impact, obviously, but close to no impact.
when the engine internally is OTAP-based. So that's the case for the DFE OTAP, DFEOTAP. We pay the cost of deserization and decoding here, but after that, we don't pay anything.
As opposed to the, open telemetry collector, when you have to traverse this tree and do some operation, in that case, checking that we have, where is this attribute, and now we have to rename, and we have to convert this, That will be named. So this type of traversing, is, is more… is much more, assuming much more CPU cycle.
In the case of the OpenTel MSP collector, and it's directly related to the fact that we represent batches in a columnar-oriented fashion versus a row-oriented or hierarchical representation like we have in the open telemetry collector.
the signaled, benchmark is about Muslim, the influence.
of batch size on the behavior of the engine, especially in this case, CPU overage.
So I will go very quickly, but what we can observe is… from 256 to basically 4K, it's the number of logs per batch.
The influence of the batch size.
On the internal representation is much bigger when we, we use an OTAP representation versus a pure OTLP representation.
The third column is now, more focused on understanding the behavioral.
of the engine when we are close to the limit. So, in this case, we have one CPU, and we… we basically try to push the system to the limit.
So, for example, here we have the OpenTech collector, we put a memory limiter, because if we don't put… by default, there is no memory limiter, and if you push the system to the maximum.
Basically, you will accumulate a huge amount of memory by the order of multiple gigabytes. So we put a memory limiter, 512 megabytes in this case.
And before to reach 100% CPU usage, we, we… something about 80%, 90%, we were able to reach, basically 500K, logs per signal.
And at this regime, And, the memory consumption is relatively low, 100 megabits.
But when we push the system.
To, 1.5 or even 2.2 times more than the maximum the system is able to achieve.
Then, what we observe is the following behavior. We observe an increase in memory, even bigger than the memory linter.
And we observe a decrease in terms of throughput.
The reason of that… it's because, basically, the garbage tractor has to do much more work, there is much more objects that are created because of the incoming traffic, and that's why we are observing this behavior.
So, in this case, for the FE, OTLP, and OTAP, So first, when we reach the 100%, we are closer to 700 kilogs per second for the DFE OTAP.
And 1.7 million locks per second when we are with DFEOTAP.
And because of the design and the architecture of the engine.
We basically, we don't have garbage collector, and we basically have a stable memory consumption.
And we keep… the school puts… Independently of the pressure that you put on it.
Okay, so, the next, set of benchmarks is trying to measure the scalability of the engine by itself.
In this case, we had one CPU, for each of those experiments, now we try to test the engine with multiple CPUs, and we want to measure the efficiency when we add a second CPU, a surf CPU, and so on.
How would that behave in terms of throughput?
So the… and I will talk briefly on why we are very close to the ideal scalability.
So what we observe is from 2 to 16, we are very close, very close to the ideal.
And it's related to the architecture that we, we decided to follow. So it's a thread blocker, shared nursing, and where we, also try to take into account the, we have some kind of pneuma awareness in the engine to optimize the communication across CPU core.
Now the… the last, benchmark is about measuring When we have, for us, an ideal situation where we have an incoming attack traffic.
the Dataflow engine, or the OTAB Dataflow engine, and then we generate an OTAP traffic.
How would that compare with the same engine, but using OTLP?
So in this specific case, we go from one CPU core to 8 CPU cores.
The main reason is that could be, that looks a little bit strange, but For this experiment, we had a server with 128 cores.
And the efficiency of the system is such that to generate the traffic.
we had to spend so much CPU core that we were not able to reach the… the same level of, of, test for, for this one.
So, the main difference is obviously the throughput.
The comparison is about… 20 times more year.
To, 13 times more when we are, in this, in this region.
So, it's more than one order, one order of magnitude.
Besto.
So, and why we have this, big gap here. It's more related to the fact that we have not been able to generate enough traffic in this specific test.
The… the reality is probably closer to, 16 millions.
In this specific case, we don't have a log with 300 bytes, it's 1 kilobyte.
per login tree. Again, the reason was we had to increase the log size to which, A search level, in order to use, let's say, to demonstrate the scalability over a CPU core, we had to increase the size of the logs, because otherwise, we were not able to generate enough traffic.
Okay, so now, how we achieved those results?
In terms of architecture in this, Dataflow engine, we, like I mentioned, we use a straightforward channeling.
So the goal here is really to optimize the… or to minimize the synchronization primitive. We basically have no synchronization primitive except channels.
And we are also trying to, position the pipeline runtimes.
per CPU, and we take care… we are making sure that we are not communicating across the new method.
Like I said, the PDATA is, in fact, a collection of Apache Arrow records, and we use our OCamel functions to enable a vectorized computation.
And we use that efficient, to evaluate expression.
We have this, native OTLP, native OTAP integration, so… we… We reimplemented, basically, We don't use a protobf library. We take the protobytes.
And we read it, and we translate that directly into a collection of columnar representation.
We do that also for syslog, and we have an experiment for Steph where we did exactly the same thing.
A very strong and important aspect of this architecture is to make sure that we have a eye control on the memory.
So everything is bonded.
And, and we, we also have an explicit back tissue mechanism we implemented an end-to-end acknowledgement mechanism. When it's enabled, and it's highly optimized, when it's enabled, we don't see so much difference between the case where we don't have an acknowledgement at all versus the one where we have acknowledgement end-to-end.
And finally, we, We considered also that it was super important for us to be able to reconfigure live. It was like an experiment. When I said before, that's an opportunity to rethink a telemetry data plane we were thinking that, what is missing mostly in the… most of the engine that we see in the observability ecosystem, the ability to reconfigure live without the Talos.
So that's what we also experiment… experimented. We could have a different conversation on that, if needed.
Jack Berg 00:36:49 Hey, Lauren, I just want to jump in real quick. A 4-minute warning before we have to move on to the other topics. Thanks for your presentation so far.
Laurent Querel 00:36:57 Okay.
So I think that's good… we could go over that, because it's as a clear, Nothing specific new, project status very quickly.
35 active contributors, for a total of 81, 6 partners, 2 approvers.
Forward, K, line of first.
We have now a huge amount of components, about 33 components overall.
Like I said, we support also syslog, and we have an experiment with Steph.
We have a continuous benchmark that's super important for us to be able to do that on every merge.
And we have a weekly SIG meeting.
the end, I think it's… let's say that I will go directly to the number 3, phase 2, produce strong evidence, I think it's already abused that, The conclusion is, if you have a tap end-to-end, the, the improvement in terms of performance, in terms of stability, is… is gigantic. So we… we strongly think that, we… that should diversify a deeper community discussion.
With, the governance committee.
And see what we can do for Phase 3.
jmacdonald 00:38:27 Thank you, Ronald.
Tigran Najaryan 00:38:28 I just wanted to say that this is so cool, guys. This, I'm actually very interested in the details, but we don't have time to do that. I'll sync with you guys, but really, really great job to see improvements like that.
And, yeah, thank you for sharing it. Thank you.
jmacdonald 00:38:46 I want to quickly address perhaps the most pressing question that someone's here gonna… someone here will ask, and this is about the community engagement with the collector between the projects that we now have, sort of two. I wanted to just really upfront say that my… one of my missions for the last year and a half has been to get involved with the OpenTelemetry Collector Project so that we're not pulling these two apart.
So if you've seen me get involved in leadership of the collector, it was mainly so that we could have a nice convergence in the future. And I'm very excited about that.
Laurent Querel 00:39:25 Any additional questions?
Tigran Najaryan 00:39:34 I'm gonna ping you on Slack, Lauren. I don't want to waste time here. Sure. I have a ton. I have a ton of questions, but…
Laurent Querel 00:39:41 Right.
Jack Berg 00:39:41 Just real quickly, regarding the interaction between the collector and this, what's it called? The aero engine?
Laurent Querel 00:39:49 The, hotel, Aru d'Ataffron Engine.
Jack Berg 00:39:53 the OTEL Aero data flow engine. Regarding the interaction between those, maybe this is an opportunity to solve something that we've been talking about for a while, which is having specifications for how this class of component works.
Right? So, it never really made sense when the collector was the only thing that did this type of, receive, process, export, but if there's two components within the OpenTelemetry ecosystem that are doing similar things, the coordination point could and maybe should be the spec.
Laurent Querel 00:40:24 Yeah.
Do you agree?
Jack Berg 00:40:33 Alright, well, exciting stuff, Unless there's any final comments to wrap that up, I think we can hand the floor over to Ivo. Thank you for the presentation, Laurent. I'm going to share my screen again.
Laurent Querel 00:40:47 Thank you.
Jack Berg 00:40:51 And Ivo, are you still around?
Ivo Anjo 00:40:54 Yep. Alright, great.
So, yes, I'd put around 5 minutes for this, but actually, in retrospect, maybe we don't even need that much, so… I kind of, so I've been doing a lot of this work around, like, getting what we call context sharing, so from the SDKs, getting information about what's going on in the SDKs, and getting it to be accessible to outside readers.
with, like, kind of the two big, use cases we're targeting first being the, eBPF Profiler, as well as OBI, the OpenTelemetry BPF instrumentation, so kind of, like, things that sit outside the SDKs, but would like to know more about what's going on in the SDKs.
And so we have, like, I think the big… the second big OTEP that we have is that, that PR there, OTEP4947, and so… I was kind of hoping to raise more attention to it and get more feedback. We've been getting feedback from a bunch of people. We've been trying to address all of the feedback and discuss and whatnot, but I think this is one of those things that… The more feedback, the better, so that… it kind of reflects the… I don't know, the wisdom of the community that we're kind of, like, happy with the trade-offs being made here, because there are trade… trade-offs being made, and I think it's good if we kind of, Get multiple people together and figure out, okay, these are the trade-offs that we want, and… What are we leaving on the table by picking this and not other options?
Jack Berg 00:42:29 Ivo, what are the groups of, sort of, people that still need to engage on this? You know, there's, like, the OBI folks, there's the spec folks, there's the profiling folks, there's the SDK maintainers, like, are there any groups that you haven't seen enough engagement yet?
From.
Ivo Anjo 00:42:47 No, I think those are the main groups, so, but I think more people might be interested from those groups that I wanted to kind of bring this to attention.
Jack Berg 00:42:56 Okay.
Ivo Anjo 00:43:00 Mmm… Yes.
Jack Berg 00:43:05 I notice you haven't approved this, Ivo.
Ivo Anjo 00:43:08 Have I not…
Jack Berg 00:43:09 Oh, oh, there you have. Oh, I'm sorry.
Ivo Anjo 00:43:11 I am, though.
Jack Berg 00:43:12 Alright.
Great.
Does anybody else have any, comments on this? Or, you know, I haven't… I'm not sure I've reviewed this. Yeah, I haven't had time to take a look at this.
Is there anybody on the… that, you know, is a spec approver, whose approval will count towards the required approvers that, you know, has lingering questions, issues with this? Josh, I see your hand is raised.
Josh Suereth 00:43:40 Yeah, I… apologies it took me forever to get this all written down, but I was looking at it and trying to figure out how to implement it, from an SDK standpoint, and so all of my concerns are around, and I think you tried to address these, but, how are we going to efficiently do this From an SDK. And the biggest thing that I think we need to address is there's a dictionary that needs to get written. And that dictionary is the only way you can represent an attribute key in the shared context today, from what I can tell in the spec.
That dictionary would then require us to know about all the attribute keys that could be put into thread local context at the start of the application, so you can write it. Or, we need the ability to rewrite the dictionary going forward, which, like, the current proposal doesn't allow.
I don't think we have that ability right now in our SDK, and I think that needs to get addressed in some fashion. I don't know if you're planning to, like, force that as a requirement, where we would know about all keys that could go into context ahead of time.
Or if you need to find a way to address that. But that's actually my main concern, is… that… I think you need the dictionary.
But from when I've implemented this myself, like, a class of this with the OTLP MMAP stuff I was toying with, you actually need to put concurrency protection in the memap.
So that you can actually rewrite that dictionary over time. And that is killer on performance if you can't… if you're not careful with it, right? So… Like, that's actually my main… and I know that this is really nitty-gritty, so, like, I've probably already classed out half the people in this call that don't care. That's fine. Maybe you and I can take this offline, but that's… that's my main thing right now.
Jack Berg 00:45:21 Josh, could it be configurable?
The set of keys.
Josh Suereth 00:45:27 you could have it, like, that's an option. I just think we have to solve it. So, like, we either decide, are we gonna have a hard-coded list at startup, right?
Or not, and if not, we need to handle threading concerns around being able to update the dictionary over time, and make sure that readers have a way to safely read, and writers have a way to safely write, right? The second option would be, that we have things configurable ahead of time and just force you to only use that, and if you try to write to context something that wasn't configured, we give you a good error message. I actually think that second thing is probably likely to be more successful.
And deficient. So, but, again, this is to get into the OTEP.
Jack Berg 00:46:12 Alright, well… Let's look out for Josh, you and Ivo to work that out, and you know, we'll look for an approval from you, Josh, as, like, a signal.
Ivo Anjo 00:46:26 Sounds good.
Reiley 00:46:27 I mean, blocker here? I think the performance issue is not something new, like, there are languages will require you to pre-register the strings, so they don't need to do the string mapping at runtime. There are plenty of, like.
like, technical solutions for this. But for this old hive, I think it's a continuation of the process level contacts, and I… I think, like, it's clear that we want to work on that, and the direction is good. There… of course, there will be details, but those details are not supposed to be answered by O-type. It'll be answered by the prototype, and it'll be eventually hammered out in the spec.
So my question is, do we want to move this OTAP forward? If yes, then I would ask people to not worry too much about the details for now.
Like, if the direction is good enough, then we get more approvals, we get this merged, and people can work on that.
Josh Suereth 00:47:21 I agree with that, Riley, but I think we should make a decision of what direction we're going to go, or that this is an important thing to solve.
So, like, when it's not addressed at all in the OTEP at all, or igno… like, when it's not called out as a problem, I think we need to call it out. So I agree with you that, like, we could move forward without sorting out all the details.
But at a minimum, I think it has to say, here's a problem we have to address.
Reiley 00:47:45 Performance, and concurrency.
Josh Suereth 00:47:47 performance, I mean, like, how to actually write this dictionary from SDKs today, if we have unbounded, or unbounded, like, unknown sets of keys. Like, if you read the OTEP and you try to implement it today with SDKs, you cannot.
And the problem that exists is not, like, called out in the OTEP. So, I think that it's solvable, but I think it just needs to be called out with, like, a proposal for what we're gonna try to go forward with that we agree to at a high level.
So, I agree with you, and I'm not… I'm not trying to, like, stop or block this. I actually want this to succeed. It's just, I think this is a question we need to actually drive in and try to answer in prototypes, in, you know, going forward, but we need to agree it's a problem we're gonna solve.
Reiley 00:48:30 Yeah, sounds good to me.
Jack Berg 00:48:33 Great, okay, looking forward to seeing some progress on that. Let's hand the floor over to Robert. I see there was a last item added to the agenda by Braden. We'll see if we can get to that, but we'll start with Robert's two items.
Pellared 00:48:51 So, can I please open those? So, here I'm asking for reviews, and I saw that a lot of people have already reviewed this one.
So, Jack, I mostly also want you to review it, because it is a different way than it was originally, like, created when you were working on the Java implementation.
So, I think you are the most important one to review this one at this point of time.
And, yeah, but others are also welcome to this one. I will probably also ping other people who are working on the implementation. I will find later who was implementing in Python, if I remember correctly. I don't remember. I think I listed somewhere all the languages. I will ping them individually later.
Some people who are implementing this.
Any question? I do not want to spend too much time here.
Jack Berg 00:49:46 Alright, sounds good, I'll review.
Pellared 00:49:48 Okay, let's go next, then.
So the next one is a little bit longer.
I think, Ludomiwa can also help, entrust describing this PR.
As part of the log-seq, we have been working for, I don't know, a month, or something like this, to… Find out what will be the guidance for the semantic convention for events, being the events which are log-record-based.
So, this PR tries to codify all the guidelines for the semantic conventions, what are… how… how semantic conventions for events should be described.
And, because these are, like, this is the core, like.
the core thing, like adding a guideline for how to capture a semantic condition for a new signal, I thought that it's worth bringing this PR here in the specification sig.
Ludomi or Trask, is there anything that you want to add?
Okay, so, are there any questions?
Jack Berg 00:50:56 I see Trask unmute… I see Trask unmuted.
Trask Stalnaker 00:50:58 I tried to unmute.
No, only, did I approve this already?
Jack Berg 00:51:05 Waiting approval.
Trask Stalnaker 00:51:08 Hopefully.
Yes, okay.
Jack Berg 00:51:12 At risk of opening a can of worms, attributes and body, what's the story there? That's been, like, a… A repeated source of conversation, let's call it.
Trask Stalnaker 00:51:25 I think it's covered in here.
Jack Berg 00:51:26 Oh, okay. So I should just read the manual.
Pellared 00:51:30 for attributes and body, at least, it's just restructuring. Oh, okay.
Just moving, yeah.
Trask Stalnaker 00:51:39 For body, the guidance now is only use body as a display string, like a human-readable display string.
Jack Berg 00:51:50 Okay.
Okay, great. So, I don't know if you have any other things you want to share about that? I see Bogdan unmuted, so maybe Bogdan wants to jump in.
Bogdan Drutu 00:52:00 Yeah, so I can tell you our experience at Snowflake, and what we try to do with events.
And why we may need something like attributes in the body, by the way. The main reason is we have things that change over time with every occurrence of the same event, and we don't know if that is appropriate to represent as normal attributes.
Versus, something in the body.
that, that changes over time.
Jack Berg 00:52:34 You mean the values of the attributes, or the set of attributes themselves?
Bogdan Drutu 00:52:38 The values, like, think about things like, I don't know, you want to record latency as an attribute for an event.
Well, not as an attribute, as a structural thing. Like, let's assume you want an event about the end of an operation, you say success or failure of this operation, okay?
don't ask me necessarily why I want to do that, but that's my canonical example. You know, one of the things I want to put there is number of bytes written.
number of bytes, read, latency, and a couple of things. Think about, for Snowflake, as a SQL operation, we want to give a bunch of stats at the end of every SQL.
Should I put those into record?
Trask Stalnaker 00:53:27 Probably what we would recommend from semantic conventions would be to put that into, if it is dynamic, to put that into a complex attribute, like result stats.
And then you can have So you have one top-level attribute that's consistent, but then you can have, you know, it can be an any value underneath that.
Bogdan Drutu 00:53:55 But it's not any value. Attribute is very restrictive to compare with a bad attribute.
Trask Stalnaker 00:54:02 It is?
Bogdan Drutu 00:54:03 Yes.
Tigran Najaryan 00:54:06 So why is it not individual attributes, then? What's the problem with that?
Bogdan Drutu 00:54:13 I didn't.
Trask Stalnaker 00:54:13 I just want to, just to clarify, attributes… It cannot happen.
Bogdan Drutu 00:54:20 Attributes is, per the definition of the attributes.
Correct, is not any value. I cannot have a map.
Trask Stalnaker 00:54:28 camera.
Yeah, that got changed.
Bogdan Drutu 00:54:32 Okay, even if I have a map.
Still, is it okay to change over time like that?
Trask Stalnaker 00:54:40 Yes.
Bogdan Drutu 00:54:41 Nope.
Jack Berg 00:54:51 All right, so, Robert and friends, semantic conventions and logs friends, are you looking for, specifically for specification approvers on this type of thing? I know it lives over in the semantic conventions repo, but is it close enough to, kind of, stuff that you're sort of blocked or waiting on?
Additional approvals.
Pellared 00:55:14 In my opinion, it would be good if some people who are working on the spec or SDKs will also double-check this.
If it feels, you know, if it doesn't break some, I don't know, expectations of the APIs, SDKs, or whatever.
Jack Berg 00:55:29 Okay.
I'll take a look.
Alright, any other comments before we wrap that up? We're at the 55 mark, so, you know, it seems like we do have a quick, a short amount of time for Braden's additional topic, so, if there's no other questions, let's move to that, and maybe, Braden, you can jump in.
Braydon Kains (Google) 00:55:53 Yeah, so this should be relatively quick.
In the semantic conventions, we… I wanted to start a project for networking semantic conventions, mostly because I run the system semantic conventions, and we were getting a lot of requests about networking stuff that, was kind of out of scope for us, so I wanted to try and start up this new It was originally just going to be a lightweight approvers group, but it's had such widespread, like.
number of volunteers, someone suggested that I make it a larger hotel project.
basically, I want to know if that's appropriate. Like, this is… as far as I can tell, essentially scoped to semantic conventions. Like, it's heavily, linked with what the eBPF group is doing, but they're gonna come work under, like, the semantic conventions umbrella for this stuff. So, I'm wondering, this is kind of related to the earlier discussion, like, is this appropriate for a… broad hotel project, or should we keep it within semantic conventions.
Jack Berg 00:57:04 Josh, jump in.
Josh Suereth 00:57:06 Yeah, we talked about this, like, Braden, you missed the lot… I don't know if you watched the recap, and I know you and I didn't have a chance to sync on it. We talked about this in the semantic convention things.
There's a… there's just a group of people that are looking for network observability, including instrumentation, right? So, like, there, and I… sorry that I forget names, but there was… there was someone looking to do, like, SNMP traps and SNMP semantic conventions and modeling entities that, like, came and wanted to talk to the entity SIG about how to model these, which is related to semantic conventions. There's OB, which is doing instrumentation, which will need semantic conventions around networking, and then obviously, like, what you're doing in the collector with, networking and system, right? So, I think that… From my perspective, the answer to your question is kind of twofold. One is, are there new pieces of instrumentation that don't exist in OpenTelemetry that we need to build out?
And if so… I would say that this needs to be a major project for that piece of instrumentation, whenever that instrumentation gets added, which I don't think is the case today. Like, even the folks working on S&MP might… that might be, like, a Phase 2 proposal to figure out how to have instrumentation around it. Maybe that's part of the collector SIG, maybe that's not, right? But that would be the way I think about it. The second thing would be, then.
If what you're doing is taking existing instrumentation OpenTelemetry already has.
but taking an area and making semantic conventions around it, I think that's what semantic invention groups are about, right? Because it's staffed by people who are working on instrumentation and other pieces.
So, to me, that's the litmus test of if you really need a big, broad, like, new set of people working on a new piece of instrumentation.
then it's, like, a generally, you know, it should be in this… I mean, but we should discuss it in this meeting a little bit, no matter what, depending on what you find, but that's, like, a new, big effort, versus, like, a semantic convention effort, which is still a project, right? It still goes through a project proposal, but it's staffed by people who are already doing the instrumentation. So, like, you're pulling the people doing OB, you're pulling in yourself and folks doing system networking stuff, like, that's… that's what would staff it. Does that make sense?
That would be my proposal.
Braydon Kains (Google) 00:59:10 That does make sense, but that does then mean this should go in as a, like, an overall project proposal with TCGC sponsorship, etc.
the SEMCOM thing? I may have misunderstood.
Josh Suereth 00:59:27 Yeah, I think even for Semcov, we… I'd like to see the… like, again, hopefully it's not onerous, and if it is, I think we should talk to the GC and TC to, like.
make sure that this is relatively efficient. But even for SEMCOM, I think we want to do, like, project-level tracking to know where people are spending time, to make sure that we're advertising things appropriately, and to make sure we see if something's off the rails and not making progress.
Right, that's the idea behind the project proposal process.
Jack Berg 00:59:54 If it's strictly related to SEMCOMF, if there's no new instrumentation like Josh was describing, the position that I've taken is that, like, if it's a new project proposal that is completely within the boundaries of an existing SIGS scope, then it's that SIG's, like, you know, purely that SIG's responsibility to manage that project's lifecycle.
Right? So, like, semantic conventions gets to approve or deny, set staffing requirements, all that type of stuff, and we can still codify it in the projects documents in the community repo, but it's like, I'm not looking for the TC or the GC to approve this. I'm looking for SEMCOV maintainers to approve this.
Braydon Kains (Google) 01:00:33 Okay.
Trask Stalnaker 01:00:34 So, historically has been… oh, sorry, we're out of time, so… yeah.
Jack Berg 01:00:39 Should we take this async? You wanna, Brandon, can you open a… start a message in the specifications Slack channel, just so we can, like, not drop the ball on this?
Braydon Kains (Google) 01:00:48 Sure, yeah, I can.
Jack Berg 01:00:50 Alright, see you all. Thanks for coming.
Braydon Kains (Google) 01:00:53 Thanks.
Trask Stalnaker 01:00:53 Bye.
