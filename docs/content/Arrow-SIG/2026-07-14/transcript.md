SIG: Arrow SIG
Date: 2026-07-14
Duration: 55 minutes
============================================================

## Zoom Recording Transcript

**Laurent Querel** 01:12 Hello, guys!
**drewrelmas** 01:15 Hello, everyone.
**Laurent Querel** 01:31 So quick reminder.
Add your name in these documents.
The topic that you'd like to discuss… Vineet.
Okay.
Okay, you're showing my screen now.
Okay, great.
Let's start this issue now.
So we follow the same process that we initiated last week.
We have two parts of the triage.
issues that need to be discussed and issues that have been just marked as stale.
So on this one.
Drew, can you, mark the… can you update the label once we… We're in Europe.
**drewrelmas** 02:49 I got it.
**Laurent Querel** 02:50 Okay, great.
So this time I will start from the, from the top, just to change the a bit. So the, That one, so implement a native Prometheus exporter, that's something I… Added, there is 2 interns beyond that.
Right now.
So, as… Some of you probably know we have the Its system, the internal telemetry system.
It's already 100% use for logs. It will be for metrics very soon. That's another topic.
That will be discussed today.
But once we have that, and it's basically reusing the engine.
for internal telemetry.
And It's, it's really nice because everything in the ecosystem that we will support.
for the processors and exporters will be reusable even for internal telemetry. So we could, for example, export in OTAP, OTLP, We could also imagine that we expose metrics with.
A promote with exporter. So the first use.
Of this, native RTMS exporter is… Mainly for internal telemetry, because today we have, like, a custom prometheus endpoint the slash matrix Implemented into the the admin crate.
Which exposed an HTTP endpoint.
It's ad hoc, it's custom. So the purpose here is to make that more generic, reusable not only for this internal telemetry system, but also for other pipelines.
So I encourage you to review this doc. There is already an RFC that is this one, the 3466, with much more detail.
And I'm discussing there how the.
the inherent limit that we have with the the sweat per car approach, and how we can deal with that.
And, and how we deal with, The memory usage, making sure that we We, we follow the same principle that we are already following for everything in this project.
Every data structure has to be bounded. We keep everything under control. So because we have to maintain a state for this, native… pool-oriented Prometheus exporter, that's the type of consideration we have to take into account.
Any question on that?
Okay, the next one, again, something I added, but it's… It's like a follow-up.
To a discussion I had with Utkarch and Joshua.
Last week, or beginning of this week.
So.
There are some situations where So let let me rephrase.
today.
All the components are, especially processors and exporters, they rely, they consume… the receiver produces PDATA, the processor consumes and produces PDATA, the exporter consumes PDATA.
PData is this generic object that traverses the DAG.
And The nice thing with the the pedata implementation we have in this project is.
We we support multiple variants of this pdata.
by default. The the OTAP PData, so basically the content of this PData message is an OTAP representation, so a collection of habitual records.
Following the OTAP schema.
And in some situation, we could have a protobyte representation of an OTLP message.
And, that give us a way to implement what we name the pass-through mode. It's an optimized mode for OTAP traffic. When you have the combination of a simple Quite simple, pipeline.
And an OTAP traffic. So when you have something like an OTAP receiver.
And… a type router based on the type of the signal you route to different destinations, which are also, let's say, OTLP exporter.
In this… Configuration, we don't decode.
We don't deserialize at all the protobuf messages that represent this OTAP message.
Because we… we just need the envelope of the message to know what to do and where to send the information, so it's a very nice optimization.
We think that we could extend this principle.
In a generic way.
to have what we name the pluggable data byte representation.
So instead of making this thing specific.
We can making this thing.
We could create an extension.
that say, okay, as an extension. So it's not the same type of extension that we already do for for nodes, but a different type of extension.
Where we could, basically assigned to an extension like a MAM type or something equivalent, so something representing the type of the nature of the message.
So we could imagine Protobyte, for example, for OTLP, OTLP Prot And then the extension will provide an encoder-decoder method.
So we could already easily replace what we have today by this type of extension and we could implement a default extension for this flugable PData byte mechanism.
For OTLP.
So we will stay exactly at the same level of what we are already able to do. I don't expect to see any meaningful performance degradation, but that could be extended.
Later on, for example, for a parquet byte, p data. So there are situations like this one.
Where… For some rea- for some reason, it could be interesting to We receive a package file.
our packet representation in in byte represent an array of bytes. And we are in a pass through mode. And and we don't decode the packet.
We don't even decompress it.
And we can act on the headers.
and the signal type.
We can make some decision in terms of putting and send that to.
For example, a packet exporter or Yeah, a packet exporter that will basically get that, do nothing with it and just store that into an object store.
So it's a way to extend this pass through mode to more than just OTAP.
Any feedback on that?
Okay.
Add a generic, so, from Manish, add a generic vendor bundle capability.
I didn't read this one. Is Manish with us?
**Manish** 10:56 Yeah, I'm here and I can go over this request. So I had created this yesterday.
So we are working on building an, agent-supplied authentication approach for exporters.
And, for… for that, I have adopted the, bearer token… Bearer token provider capability.
But one gap that was noticed was that, exporters, sometimes requires, vendor-specific routing data.
To upload the data correctly, along with the token.
So, and, these values, these routing values, these, need to refresh, in lockstep, with the token.
So if the backend rotates this routing info, even if you have a fresh token, all subsequent uploads would get rejected by the endpoint.
So, the solution that I'm proposing here is to add a small generic capability And the capability will be called, Vendor Bundle. It will be, implemented as, like, a OTAP extension.
And what will ha- what it will have, it will be, like, a typed attribute map.
And, agent basically will be pushing this data onto the same extension along with the token.
And, the, Beef Engine core, it will pass this data as, like, a plain string value map.
It will never interpret this data.
But the data remains introspectable, so that it's not, like, some opaque vendor blob hiding in the core.
So that's what the proposal is, Couple of points, I kept it, deliberately off of the existing, capability, the, bearer token provider, so that, that capability, is not overloaded with, vendor-specific data.
This is going to be a companion to that capability. It will be purely additive.
And it will not require any changes to any of the existing, exporters. And it can be something that the exporters can just opt into.
So, yeah, just, like, a quick context on this request, yeah.
**Laurent Querel** 13:24 Okay. I don't know if anyone has a question on that. I have one.
Well, feel free to, raise your hand if you have any questions. So, in between, what I… my question is… Here I see a string.
Here is the sedges and map string value.
So, so what exactly this trait will expose?
If it's really opaque and the intent is to have an exporter that is not interpreting it, I can understand that it's a string or… Battery, or whatever.
But so what is exactly the meaning of that if we have that here?
**Manish** 14:13 So what we will be passing as part of this JSON data will be routing information like endpoint details, and moniker data that sometimes some of the exporters uses. So that information will be passed as part of this. These attributes typed attributes.
**Laurent Querel** 14:36 Okay, so let me ask the question differently.
So if that is structured and will be interpreted by the exporter, why is it a string?
**Manish** 14:48 Okay, what would be your recommendation here, then?
**Laurent Querel** 14:51 Just avoid to, I mean, if, if it's interpreted.
And let's say that this thing is used by different exporters. I'd like to avoid to have the JSON passing again and again happening on the same object.
So I guess this… the vendor bundle and the capability behind it, The, the… The refresh… The life cycle of this value is is probably not every call. It's something that will be.
Provided, by the vendor.
At some point. So what I'd like to see is, a parsing of this thing done just when we need, and we deliver it again and again for every call to this attribute JSON, or to this attribute, whatever.
You see what I mean?
**Manish** 15:47 Right, and so yeah, the intent is to get this updated when the token expires. So yeah, yeah, I can make that change.
**Laurent Querel** 15:57 Yeah, so if it's, yeah, so if it's something that's happening not so often.
We should avoid to force consumer of this trait.
to do the same work again and again.
Okay,
**Manish** 16:13 Sounds good.
**Laurent Querel** 16:14 I probably need to read in more detail that, but that looks, acceptable for me.
So introduce an NFT process for a TAB data flow design proposal. Oh, yes, so that one.
That's something that, yeah, we started to discuss last time.
And there is already a RingMe now.
No, sorry, read me this one in the… so we already have this, folder now merged. I think there is a first version of the README also merged.
And I was discussing here the various status that we could imagine.
and the the process. So I think we oh, I think we already. Okay.
We already have some comments. So I didn't read them.
I don't know, Drew, or,
**drewrelmas** 17:26 Mine at least, so there was a, yes, there was an individual contributor that was willing to go move some docs around for us. My comment was just about the interplay between component readmes and design docs.
Meaning oftentimes there might be drift naturally over time.
So I would like us to figure out what we think belongs in a doc subfolder versus in a component readme. Pratish had a very fair comment that Really, what the README should have, it should serve as the user guide, not necessarily implementation details. So, it might be worth having a small separate RFC in the repo, just calling out the delineation between those two.
**Laurent Querel** 18:17 Yeah, I agree.
Yeah. And and for me, the the Rfc. Is They are like a log, a history log of.
Design ideas, discuss decision around design architecture.
And we don't expect to see all the files in these RFCs to be updated I mean, let's say you have an RFC talking about a first atom for extension, and then we A few months after, we have another, complementary or a different view on how to implement extensions, so in that case, we will open a new ARFC, we will not update the first one. The goal is not to make them always up-to-date, as opposed to the README5 That will be part of each of the components that are.
align with the code and and those one are the one that will be user face facing and need to be updated.
So I think we are on the same page.
**drewrelmas** 19:30 I think there's three docs we're talking about here. There's RFCs about larger repo or engine-wide constraints. There's… regular docs subfolder, not necessarily RFCs, which might be about a particular component, and then there's a component README, which has, you know, user-facing information. So… that's what I'm looking for, is the delineation between all three. I understand what you're saying about not updating RFCs once they are accepted, that makes sense to me, but I'm talking about the evolving Design documentation for a component and the user.
Focused.
**Laurent Querel** 20:12 Okay, thank you.
**drewrelmas** 20:12 Readme.
**Laurent Querel** 20:13 Yeah, that makes sense for me.
Yeah, okay, I see.
Yeah, I will update the proposal to include that.
I agree with this.
I will let that open just to.
to keep track of that. So let's see.
Just need to open that into a new tab. Just Okay, a generic dependency status and optional readiness integration.
Okay, yeah, I remember this one.
Yeah, so that's, that's, something.
That, so right now, the readiness is basically… Something that where nodes are not really involved, they have no word to say.
We… we determine when the… The pipeline has been able to, we initialize the pipeline, we.
We assign a corresponding thread.
Tasks have been started.
We though it's your… that make this this pipeline ready.
But we could imagine that in some situations, some nodes.
We'll, we'll require external, for example, They have some external dependencies and the readiness of the pipeline by itself could be extended by.
Those, dependencies that are not visible, at the controller level.
So that's a proposal to add a way to express that.
So again, feel free to read that provide feedback. If you have also use cases, we I mentioned some, I think I mentioned some use cases here, like, Try to remember, like, because I created that, Yeah, a long time ago, June 4.
Yeah, please read it. I'm sorry I don't remember all the details. I just remember why I think that would be a nice extension.
I don't think it's super urgent right now, but I still think it's it's useful.
Okay.
Retry processor, although infinite retry.
**Albert Lockett** 23:18 Yeah, I can speak to this one. So, CLAB, with our retry processor. You can configure it to CLAB, to retry.
quite, quite, quite a high number of times. But there is a hard limit of 1,000, which I think is is probably maybe appropriate, but, like.
So the request comes from someone who might come to us and say, hey, like. With the go collector.
Technically, it's possible to configure my retry such that there's realistically never any limit. It will just keep retrying whatever operation it's trying to do indefinitely until it eventually succeeds.
And so my thinking here is that given some folks might look at what we're building and say, hey, you know what? Does it do the exact same thing that the Go Collector does?
with respect to retries. It's like mostly. But like we do have to call out this little caveat.
And so I was thinking like, Hey, you know, if if it's acceptable, if no one can think… if no one thinks that this is, like, a very bad thing to do, then maybe we just want to fix this so we have parity with what you can configure in the Go Collector. So, in the go collector. What what you do to configure like a basically an infinite retry is you set this configuration value, max elapsed time equals zero. And our retry processor does actually have that same configuration value, so my… idea here was, you know, maybe we just say, hey, you know what? If the user sets this max elapsed time equal to zero, then in the retry processor, when we're when we do this check to make sure that like, hey? You know what the number of retries isn't infinite, if they've configured the specific value, then we just say, hey, you know what, like, you're allowed to do, you're allowed to configure infinite retries. We basically don't throw a configuration error, in that case.
So yeah, that was that was what this one was about. Again, getting this getting this implemented isn't something that's pressing. It was more just for kind of, kind of posterity as folks are comparing our engine and the… and the Go Collector, there is this small functionality difference that we might consider, closing.
**Laurent Querel** 26:15 Yeah, makes sense for me.
Okay.
Again. Don't hesitate to raise your raise your own if you have any.
Question.
I think this one, we… That's something on which we need to, so, when we… once we… We had this meeting with, the… hotel maintenance and the people from the the technical slash governance committee. So we presented the result of the phase 2 and And we basically, said that it would be nice to talk about phase 3 and how we could align the this hotel project with the existing go collector. So we it's still obviously an ongoing conversation, I should say, even we didn't even started the conversation with the, with those folks. There is, We talked with Trask, last week.
To, to initiate the process.
I don't have so much to discuss there, but What I did here is my perspective on what needs to be done.
to consider, I mean, the perimeter of this phase 3.
Things like, pipeline level control mechanism. I tried to list different things.
Making sure that we have a good coverage in terms of component, this WASM story, and in general, extension story.
Either REST extension or WASM-based extension.
when I discussed about the internal temperature system.
the, one of the stretch goals was also to have what we name an SDK-level OTAP export, so the ability to export OTAP, so that what we are doing with this ITS, the metric integration into the ITS, will give us That's for free.
And the stretch goal could be to… demonstrate a prototype of a client SDK, to report metrics and logs with the ability to use the Dataflow engine itself.
To define what you want to export in which format.
press, fuse, or things like that.
So, feel free to to add some comment. If you think that phase 3 absolutely need something super important.
I think this thread will serve as.
a way for us to to determine and to select what will be the final parameter for phase three, knowing that we didn't really start the conversation with the governance committee.
Okay, I think we are done with this list.
The next list is, okay, so we have two new… So just as a reminder, here this list will present There is a represent, Issues that are marked stale and there is a grace period of 30 days.
And then they are closed. So they are still open. So the goal here is to determine if we Let them stay, or if we remove the tag.
So I think we have with us Aaron.
No, we don't, oh no, we don'.
**drewrelmas** 30:12 Yeah, I don't believe Aaron'.
**Laurent Querel** 30:14 Okay, so maybe, Drew, can you, Talk about that and, and, because I know that you are aware of, probably this stuff.
**drewrelmas** 30:24 I do not know this one.
Oh, yes.
**Laurent Querel** 30:28 Can you just, check with Aaron and determine.
**drewrelmas** 30:31 Yeah, yeah, I'll…
**Laurent Querel** 30:33 Oh, okay, great.
Columnar query engine, additional filter optimization opportunities using ID mask. Albert, it's for you.
**Albert Lockett** 30:43 I… I think this might actually be stale. We… and we can… close it. We refactored all this code, and it doesn't exist anymore.
**Laurent Querel** 31:00 Perfect.
**Albert Lockett** 31:01 Yeah. That's.
**Laurent Querel** 31:02 Perfect. Close, close issue.
Okay.
Okay, great.
I think we are done regarding the review of the issues.
So back to this stuff. Oh, we don't have so much, to discuss in the.
In the agenda.
Okay, so I can, I can talk about the ITS integration, and if in between You have some ideas, just ping me and I will accelerate if I do.
looking too much.
Okay, so… The ITS internal telemetry system. So the current situation and what this PR is doing. So the current situation.
We… we… The the engine when the the engine starts.
There is a special, it's not so special, but, There is a semi-special pipeline engine.
A runtime.
Started by the system first.
And also shut down last.
That is the ITS, and it's pre-configured, so there is a way to configure it.
And, It's part of the configuration, and there is a special listener which is named internal telemetry receiver.
That will be usually the, the starting point of this internal telemetry pipeline.
Then you can put whatever processor you want.
And then you basically define how this internal telemetry will be exported. It could be on the console. It could be the OTLP exporter, the OTAP exporter.
Market, whatever. I mean, everything that, in fact, we support, that's the benefits of this approach.
We, we basically, it's like dog fooding. We, we reuse the, The engine itself to observe itself itself.
So until now, the, the, the situation was.
Logs were captured by the the internal telemetry receiver.
and propagated along this DAG that you described into your configuration. Metrics, we are following a different Bess… Because historically we used the client, the hotel client SDK.
to report metrics.
And, one of the pending tasks was to align everything to follow the exact same pattern. Use the, the, The Otero data flow engine also for internal telemetry.
So, to do that, what I did is… Basically, there is this concept of metric registry.
So we on the hot pass. We have a clear separation between instrumentation into the hot pass and the cold pass.
The instrumentation in the past need to be.
things like implementing a counter or incrementing several counters.
But, there is usually no allocation.
In the old pass for this kind of thing.
So we start with… We start a pipeline instance.
Then for each node, there is a registration phase where they have the opportunity to register.
Different metric set.
the metric registry will get those registration. Registration consists to provide a metric name.
Sorry, a metric set name, a set of metrics.
And… Common to all those metrics, a set of attributes.
That will where the values will be determined during the registration phase.
Then that will be stored into the metric registry and periodically, during the, the life cycle of the, each.
Pipeline runtime.
We have a collection phase that will just capture all the numerical value. We create basically a snapshot.
of all the metrics set.
And that will be sent.
That will be published on an MPSC channel.
And this MPSC channel is consumed by the metric or by the what we name an internal collector.
That will basically update.
The the metric registry.
So the… Could I…
**drewrelmas** 36:17 Could I suggest, as you're sharing your screen, as you're talking about this, could you open the sample config, like the internal telemetry YAML? I feel like that might help people visualize what we're talking about.
**Laurent Querel** 36:28 Yeah, I'm sorry. I can easily imagine that it's relatively abstract.
I agree. You see here we have the the 6, this section name on Jean.
So the other top level section is group. Inside group, we have pipelines. Inside pipeline, we can specify different pipeline by name, and then we specify the nodes. So this specific section is reserved.
for the engine itself, and then we have a subsection telemetry.
And until now, for the metrics, we had some specific custom Client SDK related configuration.
And when now we say, oh, the provider for the metric is ITS, that is a temporary approach. Once we remove the client SDK, everything will be ITS. So this thing will probably disappear.
So let's say for the purpose of this PR, we have this additional option.
And then you just specify, like any other pipeline.
So in that case, we have this first node, the internal telemetry receiver.
I will talk about the specific config after that, and then you can… you can set up So here I set up, A metrics, a processor debug, just to look at the metrics.
console, but obviously, you put whatever you want. It could be an OTLP or TAP exporter, or a target exporter, like I mentioned.
It's really up to the… the end user.
So this PR… Update this internal telemetry receiver to support metrics. So you will basically internally be connected with this metric registry.
And capture the, the snapshot and the aggregated snapshot.
And and transform the metric set into individual metrics.
Because, As you know, in the standard hotel model, there is no concept of multivariate matrix. Everything is univariate.
And so we have to translate those metric set into multiple individual metrics sharing in fact the same attributes. So we have to repeat that. That's what it is regarding OTLP.
So that's what this, implementation is doing, converting the metric set to individual metrics.
And then.
I also added this concept of view inherited from The, the client SDK, which also have a concept of view, where you can basically specify metric renaming, Change of unit and things like that. So I just implemented a subset of the views.
After discussion with Drew, And internal stuff that we need to achieve also inside F5. The subset that is implemented cover the need that we have.
Both sides, Microsoft and F5. It could be extended in the future, to other, view statement.
Knowing that, in my opinion, I think views we say, but ideally, what I like to see is We we have this transform processor that Has been implemented by Albert, with a support for OPL, where we basically have a full language to express, signal transformation.
Signal enrichment and various other things.
Unfortunately, OPL in terms of metric support is very lightweight. We don't support so much on the metric side.
So that's why I decided to.
In order to, to move, to the ITS event for metrics.
To implement a minimal subset of views.
And then that will buy us time to extend OPL to support, to have a better support for metrics.
And then people will be able to express.
any complicated transformation Either by the view mechanism, which will define a subset, or in a very generic way with a PL.
**drewrelmas** 41:22 I want to add here.
**Laurent Querel** 41:24 Mmh.
**drewrelmas** 41:25 If I could interject, Laurent. Sure. Yeah, this is going to be super valuable for us. It's partially related to another issue that was in the needs discussion queue. But, you know, we talked about… And it's related to my work with standardizing metric names with the enum attributes, as you're well aware.
And we want to move the engine into a place where there's a single consistent pattern for how component authors declare metric sets in the code. But the ITS will be very, very valuable.
to, like, help reach parity with the OTC.
historical metrics. We, as Hotel Arrow, seem to be taking a stance where we prefer singular metrics with signal attribute, for example, whereas a very common use case for compatible backends might be separate metrics per signal. So, when we talk about extending OPL, like, one of the stretch goals, I would say, is maybe we can even have an OPL function for… I would call it partition signal metric, or something like that, where all you need to do is give it a metric name, that has a signal attribute, and it will automatically split it out for you. So… I like… I really, really like moving to ITS instead of the views, and I think the more we lean into the OPL implementation, the happier we'll all be.
So I really love this work. Thank you for picking it up.
**Laurent Querel** 43:09 Right? Cool.
Yeah, so I will not go too much into detail, but… So basically, I think, In terms of why we implemented that, how that has been done.
I think I covered it in terms of, testing. And, so for the validation, that's described here.
What I did is, So in fact, the metrics are still exposed by the /metrics admin endpoint. So you have this metric registry, and it's like there is two destinations, still the existing, producing.
And this new integration with ITS. So what I did is To make sure that metrics were properly represent, integrated, I basically.
created a script.
to compare the existing output, which has been used many times, with this new ITS output, and compare the… If it's equivalent, and when it's not equivalent, is it because we had a view in the configuration that will explain this difference?
That's how I validated, Technically, obviously, in addition to a set of unit tests.
So that's what we have here. And I also did an estimate.
to determine what throughput we could achieve. I don't think we have any issue regarding throughput, especially for internal telemetry.
So as you can see, with or without you, results are pretty good.
Obviously, with you, we pay some overhead. But… This override is relatively linear, depending on the size of the batch.
So I was relatively happy with the With the result in terms of performance evaluation.
So I still need to… still, draft mode. But I will work just after this meeting to Probably later today, maybe beginning of tomorrow morning, but that will be ready for review pretty soon.
Any question on that.
Cool. Yeah, I think that combined with, what, the work that Drew is doing, I think we, in terms of internal telemetry, we will be in much better shape.
Something much more stable and flexible that and still performant.
So that's cool. Any last minute topic to discuss?
Maybe we can, if we don't have, because there is still 15 minutes, let's do a quick View on the pull request,
**drewrelmas** 46:49 Yeah, we are at 42.
**Laurent Querel** 46:51 Yes.
**drewrelmas** 46:52 Around the upper.
**Laurent Querel** 46:53 Oh, wow.
**drewrelmas** 46:53 40.
**Laurent Querel** 46:54 It's a lot.
So, is there… important. Pr, that need some attention.
Because I will definitely be able to review 42 soon, but I can definitely spend some time on some of them.
Which you consider, urgent to to be reviewed.
**drewrelmas** 47:22 Laurent, I mean, you already know about the one that I requested you to look at, which is the data point level enum attribute. Does anyone else on the SIG call have a PR that they'd like attention paid to?
**lalitb** 47:38 Hey Laurent, I have a couple of PRs, more of a design document PRs.
Probably whenever you have time. One thing is… Okay. …for NEMA, where, I think design, I already have an implementation for that, but before that.
There is a design, RFC, Which probably would be good, somebody can have a look into that.
**Laurent Querel** 48:01 That this one?
**lalitb** 48:03 Oh.
Yeah, let me just open that. Yeah.
**Laurent Querel** 48:09 Oh, no, I think it's probably the the proposal behind it. Right?
But you are.
**lalitb** 48:14 Yeah, this is, this is more of an implementation, yeah.
**Laurent Querel** 48:16 Oh, okay, okay, okay, okay, yeah.
**lalitb** 48:19 Yeah, I think you had some earlier comments where you proposed to split that into two different documents.
**Laurent Querel** 48:24 Yes, I remember.
**lalitb** 48:26 you know, So that, that part was done.
**Laurent Querel** 48:31 Okay.
**lalitb** 48:32 earned.
**Laurent Querel** 48:32 Okay, I look at the, I will look at that. Yeah, the, regarding the, Specifically the, the new malware core placement.
**lalitb** 48:45 Yes.
**Laurent Querel** 48:45 planning and, and the corresponding configuration. So, did you, I didn't read at all. So did you, so I see that you are covering the Linux topology discovery. Yes. Okay.
**lalitb** 49:00 This only covers Linux topology as of now.
**Laurent Querel** 49:03 Okay.
**lalitb** 49:04 Probably we have to add separately for other…
**Laurent Querel** 49:06 Because what I was thinking is, and I don't think we have any In an unformal spec somewhere. That's strange because I remember working on that at some point at the design level and I didn't retrieve it. But basically.
If we take an example, when we… We have many benchmarks running now, and we have multiple configuration files used Oh.
to basically express those benchmarks. And very, very often what we have to do is We have to know the number of CPU core.
On which those benchmark will will will run.
And we have to manually assign.
Core ID.
Let's say we want to test this specific pipeline on 10 cores.
So we have to assign either a range or core ID 1 up to 10.
It's it's it's super manual and and relatively fragile because.
because when when we have the same engine running multiple pipelines, we could have overlap, and it will be much better if we could express constraint.
**lalitb** 50:24 Yeah, sure.
**Laurent Querel** 50:25 It's like, okay, I want to run on 10 cores. I don't care, I don't care about which one, but, please optimize the deployment to minimize.
overlap as much as possible. And you are free to select core one, core three, core 10, up to the number. So that's something we need to be able to express.
**lalitb** 50:49 Yeah, it does not… I mean, as of now, this configuration does not explicitly express it, but it's more of an implicit. Like, if you specify core count.
It will ensure that you use… you… it will… that there won't be any overlap of the core count, and it… all those core count would be packed in a symbol in the same node.
Okay, so… But I think we can… Okay, cool. Yeah.
**Laurent Querel** 51:13 Corcant is the way to express the constraint.
**lalitb** 51:18 Yes.
**Laurent Querel** 51:18 Without specifying the core ID, which is okay.
And when it's explicit.
We use core set to specify the number. That's the idea, right?
**lalitb** 51:30 Yeah, so.
**Laurent Querel** 51:31 Okay.
Yeah, I need to think about it a little bit more. But on the principle, for me, that's exactly what I was looking for.
We're getting the naming… It's probably okay, I don't know, But yes, that's that's good.
Can you see this?
**lalitb** 51:57 Yeah, no, once this is done, probably I can have the subsequent… I mean, once it looks fine and this is done, the subsequent PR would be more for the BPF-based load balancing, because that is going to use this.
**Laurent Querel** 52:09 Yah.
**lalitb** 52:10 So.
**Laurent Querel** 52:11 So let it, I'm sure that you're aware of that. You are looking at every PR mostly, most of the time. Yeah. It's, it's impressive by the way. But So you are aware that we have this new type of extension that has been merged a few weeks ago, the controller extension.
**lalitb** 52:33 Oh, yes.
**Laurent Querel** 52:35 So… Typically, the reason why we have this controller extension is to let So, for example, we are building we built, in fact, an op amp.
Client extension.
Relying on on this concept.
But we could imagine that for some advanced work, it could be useful to have custom code that will make some decision on the placement based on some external rules.
Constraint.
So I think maybe not in the in the 1st iteration. But keep in mind that Probably the, either the, the, the controller extension So… Something in a room that another type of extension will be introduced at some point to.
To give ways to people that are embedding the system into a bigger system.
**lalitb** 53:40 Yes.
**Laurent Querel** 53:41 To basically delegate decision on placement.
I think we we need to design the system in With with that in mind.
**lalitb** 53:55 Got it, yeah.
**Laurent Querel** 53:56 Okay, cool.
Okay, if there is no other, topic. I think we can get back the last 5 min.
**Albert Lockett** 54:12 Great.
**Laurent Querel** 54:14 Predict.
**drewrelmas** 54:14 Good time, everyone.
Bye-by Bye.
