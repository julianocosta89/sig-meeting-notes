SIG: Arrow SIG
Date: 2025-08-26
Duration: 69 minutes
Zoom Recording URL: https://zoom.us/rec/share/Aqn3fwG9D1yK352-ETTfiqSnvt5FWAyFumrj-BjXjEVI7CC7KQgtUJl8-HmbbzXF.pYgdph3C9C7tL1IG
============================================================

## Zoom Recording Transcript

albertlockett 00:00:58 Hey there.
Gokhan 00:01:00 Hello.
Laurent Quérel 00:02:23 Can you hear me?
jmacdonald 00:02:24 Hello, I can hear you.
Laurent Quérel 00:02:25 Great.
So, it'll be late.
Hi, Mike! So, nice to meet you. You are working also on this, hotel project, right?
MH Mike Heffner 00:02:47 Yeah, hey, nice to meet y'all. Yeah, working with, Ray from, on the Rotel stuff.
Laurent Quérel 00:02:54 Right, so we had a… A brief introduction last week, on this topic.
And, … We are super happy to see how we could collaborate in some ways.
With what we are doing.
I don't know if you had the chance to discuss that between you and, … so… There are people that are working on the hotel, but if you have any kind of conclusion, we will be happy to hear them.
MH Mike Heffner 00:03:24 Cool. Yeah, yeah, Ray and I caught up, and yeah, excited to, yeah, see how we can collaborate on this.
Laurent Quérel 00:03:36 Okay, Josh, how do you want to, … To organize this meeting.
jmacdonald 00:03:41 I was, going to suggest, that we start with issue review, and I was going to pull up the Google Docs. I just started making an entry for this week, so we can put in our names and so on.
Laurent Quérel 00:03:54 tools.
jmacdonald 00:04:15 All right. Yeah, so I don't see very many new issues. I filed one myself.
So… … As you know, I have been working on… well, the larger picture was rate limiting. I started by looking at how the retry processor worked.
in the current codebase, and then kind of recognized that some development was needed. So I've been looking into, Bringing that, essentially the concept of back pressure and error propagation into this pipeline.
One of the things that I noticed right away when I was converting the retry processor code was that there were tests where it would send one request and, like, wait for the request to come through, and then verify that that request matched the original.
… And I remember… and so the current data type that we're using, as I move this code out of the engine into the OTAP, crate, now has a different type, and so there's no, there's no partial EQ implemented for the OTAP P data. Therefore, I can't just test that these two objects are the same. Now, Laurent, you remember in Go, we have, a whole assert package for making sure that two OTLP objects that had been transformed by Arrow were equivalent, and I was looking for something similar. That's my issue.
Laurent Quérel 00:05:43 I see.
Yeah, that's definitely something that helped us a lot in the… in the first phase of this project.
We need to find a way to produce that.
jmacdonald 00:05:55 ….
Laurent Quérel 00:05:57 I think we should, create, … did you already create a GitHub issue?
jmacdonald 00:06:03 That's this issue right here. Yes.
Laurent Quérel 00:06:06 Okay, sorry.
Yeah, so that definitively, we need… I need to see, if I have someone in my team that could, that could help on that.
I definitely have a good idea on… at least how we achieve it, in the, in the Go implementation.
….
jmacdonald 00:06:31 Right. Okay.
Laurent Quérel 00:06:32 Right now, we have no one to work on that on my side, but I will, ….
jmacdonald 00:06:40 Except if you have someone on your side, but I will do my best to see when we can, ….
Laurent Quérel 00:06:44 We can welcome that.
jmacdonald 00:06:47 Sure, thank you. It sounds like Albert put something in the issue. I agree, and we can move on.
I don't know if you wanted to try and continue the conversation that was happening, a week, last week on Thursday. Now that we have Mike here, perhaps we should discuss further if there is anything pressing.
On the topic of Rotel, I know that for myself, I had, I had committed to kind of a roadmap document, which I'm still working on. so, sort of things, areas for opportunity.
Of opportunity for us to kind of collaborate.
I can… I can already tell that the op… the sort of, like, very, like, big, obvious, kind of, like, potential collaboration involves, running integrations with other languages. Your work with Node and, Python is awesome, so thank you.
MH Mike Heffner 00:07:43 Thank you.
Ray Jenkins 00:07:44 Man.
MH Mike Heffner 00:07:45 Yeah, we are also, yeah, we're also working to get, sort of, a list of sort of, at least from our perspective, sort of like a priority, sort of, based breakout, and yeah, hopefully see sort of where there's some overlap.
jmacdonald 00:08:08 Well, Laurent, you have something on the agenda. Would you like to have the screen share?
Laurent Quérel 00:08:14 Oh, yes?
… Thank you.
Sorry, sorry, it's taking a bit more time than… I was expecting… What's happening?
Okay.
Okay, sorry.
Maybe it's too small, I can, … Maybe bitter now.
So, yes, … finally, we have, … a PR for this, … instrumentation system or telemetry system that I integrated into the engine.
And started to, to describe, Last… last… last week.
But now we have a more final version, and with some additional capabilities, so I will just take 5 minutes to talk about that. People that are interested by more detail can definitely look at the PR.
So as a reminder, we, we, … What we… what we have today is a straight-per-core engine.
It's still not yet NUMA-aware, but that's something that is on the table, and on which I will work, Probably not this week, but, beginning of September.
But anyway, so the goal is to make sure that we have the minimum of interaction across score.
And when we talk about a telemetry system where we have aggregation, and we want to deliver a good observability of this entire system, at some point, we need some kind of aggregation that will happen.
So in this design, we have, … let's say two… two paths, what I name the odd pass and the cold pass. So the odd pass is where All the pipeline instances are running, and so basically we have one thread per pipeline.
thread or pin to a core, and that's what I named the hot pass. The goal here is to minimize, at the maximum, the override related to the instrumentation.
So that we end up with a solution where we basically have no synchronization mechanism each time we increment a counter.
And, … and we also have this concept of multivariate matrix.
That is directly accessible at this level.
And… and depending on… where we are sending or reporting the telemetry, those multivariate metrics will be either split into univariate metrics, for example, to support the open telemetry model, or they will be reported all together.
In order to get the maximum, performance when the underlying transport support this kind of, solution. An example of that is, for example, in FixDB, support natively, material matrix.
So, … Right now, we have a way to describe, … let's see… yeah, that's here.
So this code is what we can use now directly in any nodes or anywhere into the system, in fact, to describe, what I name a matrix set.
Matrix set is another name for multivariate matrix.
So a metric set is described with a name, and then it's basically a script.
containing, multiple fields, each of those fields are matrix. And, right now we support Kunter, and… and soon we'll support uptown Kunter, gauge, and… and… and histogram in, last iteration. And, but probably very soon, gauge and, and, up, down, counter.
So then we… we already have an integration with semantic convention in this system, so we… we can attach, … Metadata to each of those metrics.
And, and we have a way, to, … describe, basically to auto-describe the telemetry that this system is able to produce. So there is an endpoint And then telemetry Live Schema, which represents… … The merge of all the… The matrix attributes, and in the future, span and an event that this system can produce at any point of time.
And it's named Live, just because, depending on the type of pipe… the pipeline that are deployed and running in this engine, obviously, the metric reported will be different. So, let's say you have a pipeline composed of OTLP, receiver, some batch processing, some retry mechanism, and, let's say, an OTAP exporter.
You will have… The telemetry corresponding to those nodes.
But if, later on you have another pipeline running on the same system with new, … new type of nodes, we will discover at this point, the, for example, the matrix that will be reported by this new node. Then the live schema will be automatically updated and will express directly the, The semantic convention corresponding to the… to the… The signal that could be, … Produced by this system.
So we have a declarative way to describe A metric set.
And we have similarly a declarative way to describe attributes. I think I have an example, if we go in the… in this huge, huge PR. Sorry, guys, for that.
But it was a huge modification, so I think if we go… let's see… ER… Yes.
Similarly to the matrix set, we have a similar mechanism to describe attributes.
And… and we can stack attributes, a group of attributes together. So, in this example, for example.
The node attribute set is… Two… two fields combined with things coming from the pipeline attribute set.
And similarly, the pipeline attribute set defines some local defini- local, … feeds… our local attributes, and so on. So it's a… it's a stack of attribute sets, and depending on where, the metric is, used, we have the corresponding attribute set that is attached to it.
And I think that's something I mentioned last time, but we have two types of attributes.
Static attributes. So basically, once the instance of a node or a pipeline is defined.
The corresponding attributes are properly, … Are created with the corresponding values defining the context.
But, both attributes are only communicated to the telemetry system.
One time during the registration.
Then each time we have, data points that are… or contours that are implemented, we don't need to, report again and again those attributes.
They are, let's say, stored and, And attached to the metric, the aggregating metric inside the telemetry registry.
As opposed to the dynamic attributes that could depend… dollar value could depend on… incoming traffic.
Right now, those dynamic attributes are not yet supported in the system, so… Back to this diagram.
So we have the registration phase, basically describing the metric set, describing the static attributes.
And they are recorded into the metric registry.
And then, each of those engines periodically We'll, request from each of the nodes that, make a registration of multivariate matrix. We'll receive a message, a control message, saying, okay, please report your metric.
And that will be… that's what we see here. So the… the local Kunters are… Done between each of those, … report, interval.
And then, once we have this importing table.
That is translated into a control message received by each of those nodes.
We report the corresponding matrix, and they are aggregated and recorded into the metric registry.
And that… this entire box is running into the, … a different thread. We are trying to minimize the communication between these two worlds, the cold pass and the old pass.
And, … and right now, we are exposing So these three HTTP endpoints, and the next step will be to, to use the the rest, client SDK, the rest open… open TM3 Client SDK to report The aggregating matrix to whatever endpoint we want to report those information.
In between, we have those HTTP endpoints that are able to deliver … All the metrics part of this metric registry are an aggregated view.
Of those metrics.
in various formats, either in GZERN or the line protocol used by InfixDB or Commitius.
Yeah, I think that's, … That's the general idea behind this system.
And, … Open to, feedback or question.
Ray Jenkins 00:19:44 I'll take a look at the PR. I don't have anything else to add from the last discussion, but it makes a lot of sense, just basically eliminating any locking in the hot path for this.
Laurent Quérel 00:19:54 Yeah.
Yeah, and … An instantiation of that, once we are in a fully pneuma-aware version of the engine, will be slightly easy, because, in fact, we will have a metric system per NUMA node.
So basically, we will have, … when the controller will… will discover the NUMA topology, We will, … create one thread per core, talking about a pipeline deployment. So we will create one thread Pure Coral?
The memory, so the first, the thread will be, will be, pinned to the corresponding call.
The memory of the pneumonode will be pinned to the corresponding, thread for this pneumonode.
And we will start… we will do that for each of the cores available for this manhood, and we will also, create a low priority thread Where the metric system will run.
Again, attached to the corresponding nanode that is assigned to it.
And, so the only, for me, the… so in this design, it means that we don't have any communication across the manhood.
We have multiple reporting points, one per minute.
Which is, in my opinion, acceptable, because even on big, servers, you just have few pneumonodes. Usually, you have a long list, of course, per pneumonode.
And 2, 4, maybe 8 pneumonodes.
it's already a D machine. So it means that, at the maximum, we will have 2 to 8, Thread reporting… aggregated matrix.
And I don't see the value to have only one, at least right now.
To have only, like, an additional level that will aggregate the values matrix from multiple limited.
If we need to, we could add an additional level.
So basically, we will have a metric system here.
Combining the result from multiple metric systems running per nuance.
jmacdonald 00:22:20 Good crush.
utpilla 00:22:22 Yeah, hi. I still haven't, like… I mean, I'm still going through some of the changes in the PR, so I just had a question about the metrics reporting in terms of, like, delta versus cumulative. So, in this diagram, like.
where, … like, usually, like, within the SDK space, it's the snapshot time or the collection time where we actually… … Make that decision based on whether the User wants to see delta reported metrics, or cumulative reporting metrics, so… How are we dealing with that here?
Laurent Quérel 00:23:03 … So… I think that this system can be, so the metric registry is the place where Metric values, are aggregated.
utpilla 00:23:18 ….
Laurent Quérel 00:23:20 And… Each time we decide to export this information somewhere, either in response to the to this endpoint, or we decide to extort the corresponding information with the REST client SDK.
we could decide if we report the delta. In that case, this metric registry The values here will be, visit to zero, or, we can report the… the cumulative information. And then, the next time, again, we will report a bigger value, because we will most likely receive information from there. The only purely delta stuff is in this space.
I don't see the… any interest to… to do any kind of accumulation except for… for the specific interval, but each time that we collect something.
And if… Obviously, there are some color cases. Let's imagine that this, link is, fool.
for whatever reason.
Either because the low priority thread here is not able to follow the number of metrics, or for whatever reason, we are not able to to accept more messages. So there is a mechanism already in place where we try to send, and if we are not able to send, then we keep The… the existing values, we don't do the… the result.
But otherwise, it's always a snapshot we try to send.
If it's success, then we reset. If we don't success.
We, we just forget the subset, and we continue the accumulation.
Is it, acceptable for your point of view? The way that this system is working? It could be either… used to get the delta, or it could be used to get only the cumulative information. I think it's just the way that we interact with it, that we define the The behavior of those, matrix.
utpilla 00:25:34 Okay.
jmacdonald 00:25:37 In my review of the PR, I put a link to a metric SDK I worked on in Go. It's old, so it's hard for me to recall the specific details here.
But, in my commentary on yours, I recognized the pattern that I had used before. It's the one in the diagram up here, where I used the word stop half to describe, like, the instrument-facing side of the SDK.
Laurent Quérel 00:26:04 Just do….
jmacdonald 00:26:04 with potentially high concurrency, and usually, the way I think of it, it's got a single cycle over which it's it's flushing aggregations on a delta-like thing. It potentially can drop record sets completely from its own state.
when things go stale, and it's just sort of statelessly flushing out, essentially, a series of short deltas. In the OTEL SDK specification, there's a concept of a metric reader, which gives you the ability to have more than one, like, consumer of those those updates. And this is where that decision that Ukarsh is getting at comes in, where you have to decide between delta output and cumulative output. And if you're doing cumulative output, you're sort of required to, like, keep state, and there's some complex stuff we could talk about with timestamps and… How you, like, just say that you've forgotten things.
Potentially, but it's much… if… and there is not much interest, I think you're right, in expressing this delta mode of temp… of output, even though the data dogs of the world are very happy to consume it, it's not something that most OTEL users are asking for. So, like, give me a bunch of kind of Prometheus compatibility is assumed.
So, you do end up having a chance to, again, do that read and reset that you do with Delta.
metrics versus read and accumulate mode that you do with cumulative metrics. It's a decision that you could, you know, we could do later, essentially.
Laurent Quérel 00:27:46 Okay, so… Is it fair to say that I think we are… In agreement with the mechanism currently used.
We, we, we have this, … delta mode or reset mode available and up to the way that… to the consumer of this thing, to decide in which mode they want to use the… To consume the matrix.
But it looks like… the design decision there makes sense for you, both Joshua and Utkarche, right?
utpilla 00:28:24 So, yeah, I just want to make sure, like, I haven't seen the exact, implementation details of, like, how that reporting of metrics is happening, but I assume you're using a channel because it says periodic MPSC reporting.
So So, we put the snapshot or the snapshotted data in the channel, but… I believe we would also need timestamp-related information for it, to actually make those decisions later on in the… that green box metric system.
Laurent Quérel 00:28:58 Yeah, so the, the… There is a shortcut there, but we could definitively, … Update the message that is… used to, to parameterize the MPSC channel.
Right now, this MTNC channel is basically I contain… Structs that are defined with two fields, a list of values.
the order of those values matter. It has to be aligned with what has been registered, but it's enforced by the macrosystem I've shown you, so there is no option of doing things in the wrong order.
It's, … It's the code that's generated in a way that we enforce this order.
… And in addition to these, snapshot values, we have, a metric set key.
Which is, in fact, two numbers, and they are, the… the key for the slot map that we have here, so we know where those snapshot values belong. What we don't have is a timestamp, because it's a shortcut, and definitely, I think I will update that. We could report, in addition to the snapshot values, the timestamp when this snapshot has been done.
And then, independently of the time that this information stays into this channel, at least we have, … A reported timestamp in the metric registry, where we accumulate things that Reflect the reality a little bit more than what we have today.
… Know that you have that in mind, … That corresponds to the… The model that you are expecting from such system?
utpilla 00:31:01 Yeah, yeah, I think so. That's, … at least that's how the way we are used to doing it in the OpenTelemetry SDK implementation.
So….
Laurent Quérel 00:31:09 Yeah.
jmacdonald 00:31:10 Yeah, I don't think people are really expecting, like, a timestamp accuracy across NUMA regions.
And if they did, we would… we would be able to point it… potentially point at, like, a calculation you could do to correctly approximately combine things that weren't quite measured at the same time, basically. Yeah. We could do that, but it's, like, that's… that's a metrics engine right there, and I don't think we want that.
Yup.
Laurent Quérel 00:31:37 Something that is not… Part of this design, but, that, … I use as, … I mean, this system has been designed also to enable some capabilities in the future.
jmacdonald 00:31:55 One of them is, ….
Laurent Quérel 00:31:59 Being able to use internal telemetry, specifically internal metrics.
To let the controller, decide, for example, if we have to rebalance the traffic in some way.
So detecting, for example, unbalanced situation across a thread.
So, a cross-core is essential for this kind of, … design, and the metric system that we have here will play an important role. So, what we don't see here is the feedback loop From this metric system to the controller.
So, and, and, and even maybe some… Nodes inside the pipeline engine.
could subscribe to Internal Matrix.
… So the… The speed at which those metrics are collected, the minimizing the overhead is fundamental if we want to support this kind of scenarios.
And I really think that what we have now is… I can't imagine a way where we are minimizing more of the override, at least for each of the… what we do in the core. Right now, it's just incrementing … U64, even not Atonic U64, so….
jmacdonald 00:33:30 ….
Laurent Quérel 00:33:31 I think that that should be, super fast.
So, feedback loop is missing, another aspect that is not yet, integrated.
that I had also in mind.
is… Here, we are running pipelines, telemetry pipelines. So we basically apply some transformation on metrics, logs, spam, and so on, and we deliver The corresponding transform signal to a destination.
We should be able to use, … The same pipeline technique?
Here in the metric system.
Because there is no reason why not applying some transformation, even on internal metrics. So, at some point, instead of creating dedicated, metric exporter, I think we will just reuse … A dedicated instance of the pipeline engine running into this space, but reusing and leveraging all the components that are supported by the pipeline engine.
Obviously, we need to figure out a way to solve the security that we have here regarding the metric system itself, but I don't see that as a big deal.
jmacdonald 00:34:56 Sounds good to me. There's a lot… there's a lot there, and we can always continue this discussion, again in the future.
Laurent Quérel 00:35:02 Done.
Okay.
jmacdonald 00:35:06 Great. I was wondering if you could say a little bit more, like, for me, one of the… always the biggest challenge in implementing a metrics SDK is, the operation of looking up your attribute set. So, I've got an attribute set, it's… I know in your setup here, it's a struct with some scalar values, probably.
how do I give you a struct, or an attribute set struct.
And look up the counter value.
And then the next natural question that comes out of OTEL every time is this idea of a bound instrument. Like, I could do that lookup once, and then, like, just increment an atomic every single, you know, like.
Quickly, and usually the cost of the attribute set lookup dwarfs the cost of the atomic, so it's a conversation that becomes important.
Laurent Quérel 00:36:00 When you talk about lookup, that's for the aggregation part?
jmacdonald 00:36:06 no, usually it's for the increment part, so… I assume that you've got some static location in memory where you're going to do these increments, otherwise you have to produce an attribute set.
Laurent Quérel 00:36:18 Yeah, but the… so the… Yeah, so when… in this version where dynamic attributes does not exist.
There is no such problem.
jmacdonald 00:36:30 Because, in fact, for….
Laurent Quérel 00:36:32 You… you… the static attribute defines precisely the context for that, so the values level that I mentioned, So every event that happened For all the corresponding metric set.
Attached to this, … static attribute set.
are… should be incremented anyway in the center. There is no need to, … to split the bucket in multiple states. If we have….
jmacdonald 00:37:01 Basically, a zero, a zero-dimensional,
Laurent Quérel 00:37:04 Yeah, yeah. It's not really zero, because you have a set of attributes that That are known when this node is created, and this set of attributes can be As big as you want, but … yeah, it's… zero dynamic dimensions. By dynamic, I mean dimensions that depend on things that are not well known when the corresponding observed system is created.
jmacdonald 00:37:33 And I know about the registry. Is it, … Is it the case that … You consult the registry to find, … the… I guess, definitions you're looking for.
Laurent Quérel 00:37:52 Yes, we can use the registry to, to retrieve the definition of ….
jmacdonald 00:37:59 I'm imagining, like, when it comes time to read, collect from the metric instruments, do you walk through each node, or is it… do you broadcast a node message to all the nodes? Are there other producers of metrics?
I'm making a lot of references to Prometheus in my head, at least. Like, they have a concept of a registry, and they have a concept of a producer, I guess, I can't remember the name of it. And then, when it comes to collect, you just walk through all these things, and you call their method, and they produce outputs for you. It seems like you're doing the same thing through a control message. Node could.
Laurent Quérel 00:38:33 Yeah, exactly. Each of the pipeline engines, they are running independently, and they are orchestrating A control message that will be sent, … every, X millenn.
And, that… this control message will be sent to all nodes that, effectively register at least one metric set.
Any nodes that didn't, register anything?
We'll not receive this control message.
… Yeah, and then the… in the reaction, those nodes receiving this control message We'll have to report their metrics.
With a specific method. And, and this method is doing the logic I was, describing. Snapshot, try to send.
Success Reset.
unsuccessful, send, then we… we keep the… We don't touch the local information, and we wait for the next, … … time or tick.
The next control message, requesting a collect for the metric.
jmacdonald 00:39:55 Yeah, you've also included this concept that Prometheus has called a constant attribute value, or a constant label, they would call it, so it's.
Laurent Quérel 00:40:02 Yeah, that's the static attribute I was mentioning, I think that's a similar concept.
But the… the term set… Static or constant is… misleading. I didn't find any good, description of that. It's misleading because it's not really constant, in the absolute. It's becoming constant once a component is running, so the entire context Before this event, is part of the definition of the attributes.
jmacdonald 00:40:36 Right, and one of the things that comes up is that we have this location in the OpenTelemetry data model called Scope, where there's an attribute bag, you might say, that's above the level of the instrument, and you could put your constant attributes there, but it forces you to have a bunch of repetition at the metric level then, potentially. And so… at times, the way Prometheus would represent that is just to put those attributes into the output as you're generating the kind of Exposition, they will call it.
Anyway, this all looks really good to me, and very cool. I, I do think that because of the Both the feedback component and the explicit goal of making multivariate metrics.
happen, you have a lot of freedom and license, from me at least, with OpenTelemetry.
Laurent Quérel 00:41:32 Yeah, and … In, in a further final… follow-up here, when I will, myself or someone else will, integrate the rest, OpenTelemetry Client SDK. We will split, basically, the multivariate matrix into multiple multivariate matrix for now, and… and… At some point, … If we are able to demonstrate a native support for material reclicks, for example, in OTAP.
We already have some ideas regarding the data model.
And if we are able to demonstrate the benefits in terms of, A volume of information in transit.
That will be… obviously much smaller. I think that will be a good motivation and starting point for discussion with the rest of the community to to say, okay, I think we need to go there, and we need to provide a… A satisfying solution.
jmacdonald 00:42:33 can even imagine a new Rust InfluxDB exporter for our pipeline.
Laurent Quérel 00:42:39 Yeah.
Ray Jenkins 00:42:42 Is….
MH Mike Heffner 00:42:42 Maybe a naive question, I was curious, like… Are… you mentioned that dynamic attributes are not supported in this, which, you know, makes sense without, sort of, like, having to do LRU. Is that something that would be folded into this sort of design, or would that be sort of kept separate due to, sort of, the performance requirements?
Laurent Quérel 00:43:03 I think I will, I think we need to, to support dynamic attributes, as an option, directly, in the Outpass.
For… for components that… Where that really matters.
… I think with what we have today, we already have a lot of potential for debugging and troubleshooting and performance analysis.
… if you think about it, does that… I mean, I don't think that really matters a lot right now to understand that a specific batch is coming from client IP address 1 or client IP address 2.
Maybe that there are some scenarios where these things, really matter.
But, that's why I focus on that first.
But, I do agree with you that, Supporting dynamic attributes will really be an important point at some… Yeah, will be important to support.
Ray Jenkins 00:44:11 Makes… it makes a lot of sense internally for, like, the internal pipelines, because that is somewhat static. It's more on, like, the receivers and exporters. This… it raises… I had two questions that, like, sort of came out of this. One is, so is there any… Is there any need or thought around coordination of, like, so you send this control message, is it gonna be an MPSC channel that's always there? And, like, for example.
Well, you know, you talked about one, … you know, one pipeline could be, you know, you could have basically an imbalance between the pipelines, and so… and then… and I think, you know, it was mentioned about timestamps, but perhaps, like, I don't know if, like, a… monotonic incrementing? Like, are you expecting some sort of… do you need some sort of coordination, or, like… a weight group, essential concept of, like, I've sent this message, now I'm waiting for these all coming back from these cores. And another piece, I think, that… that's not clear to me yet, and Mike, I think we spoke about it briefly, but looking at the architecture of how this is gonna work out. I'm assuming there's… at the receiver side, there's some sort of… asynchronous layer to be able to handle a high number of connections, and these messages are getting put on a queue somewhere, where we're going from that model to thread per core.
how is that… what does that runtime look like? You mentioned, like, a tick. Essentially, we do a certain amount of processing, and we check a channel, and oh, now we have, you know, requests to run this actor that essentially is doing the metrics reporting, or… Looking… if there's any sort of overall design around those pieces, I'm kind of curious, like, how that works, and would like to read a bit more about.
Laurent Quérel 00:45:58 Flexible.
Yeah, so, … So, at the beginning of this project, we had to decide the execution model?
So I'm answering more of the second question first.
So the, the, … The two most obvious, execution models are… work-steining approach, the standard Tokyo approach.
Ray Jenkins 00:46:26 Versus, ….
Laurent Quérel 00:46:28 The thread per coercion-leasing approach used by… multiple high-performance solutions, like, everything that is based on C-Star.
Framework or fundamentally straight-per-core approach.
solutions, like, ….
Ray Jenkins 00:46:44 Foundation.
Laurent Quérel 00:46:44 Should be me.
Ray Jenkins 00:46:45 Foundation.
FoundationDB is a.
Laurent Quérel 00:46:48 Yeah, FoundationDB is an example, but … there are values… declination of that, it could be thread per core, or it could be event loop per process. So, for example, thread per core is, what is used by Envoy. Event loop per process is what is used by, NGINX.
And, Red Ponda is based on Sister and doing the same thing. So… The discussion we had initially at the beginning of this project, Joshua and I, when we defined, the global requirement?
we, we decided… One aspect that we really want to, to serve is having An engine system that is super fast, very high performance.
And we want to go in a direction where we don't compromise with that. That's why we spend so much time, for example, to do this kind of exercise, trying to figure out what would be the best way to report metrics at a very high frequency level and under load, with a minimum of override.
So, knowing… knowing the… this requirement, that, is… that really matters for F5 and Microsoft.
The decision was, okay.
The best design for the most high-performance system right now are the ones that usually rely on a spread-per-core shareholding approach.
That also, means that we have to… Be careful, and … so, for example, when you say that we have some async task.
They need… they have to return back to the… to the runtime, the control, otherwise we will end up into a situation where … A thread will not be used at 100%.
So, it's not easy, and … I think right now, we try to achieve that as much as possible. I'm sure that we will observe some issues, and we will have to fix them.
So the way that now the… each of those pipelines That are attached to a thread, pinned to a coil.
There is this concept of effect on Blair into the design. So, you have different… as you know, because you are designing hotels, so you know that very well, we have 3 main, or depending on how you see that, but 3 or 4 type of nodes into those DAG, or pipeline.
receiver, processors, exporter, and you could imagine that connectors are another one, even if I personally don't consider them specific.
But, the receiver side, when they have to interact with the rest of the world.
They, they use the effect humbler provided by the engine, the pipeline engine itself.
And, one of them… service offered by this serv… this effect on the is providing sockets, that will be used by those facilities, either to implement a gRPC endpoint for the OTLP, or OTAP, or syslog, or whatever.
But it's not a regular circuit. It's a circuit that has been pre-configured properly by the engine itself to work well in a context where we are straight per core. So, typically, we will configure the circuit with a SRIU support.
Option, in order to make sure that we will have some load balancing that will be Manage at the kernel level.
to dispatch, basically, incoming, either TCP socket or UDP, UDP, packet to the, to the, to the various receiver instances running on different, thread.
Now, with that, we could still have an unbalanced situation if we… if we have, let's say, a gigantic, A gigantic producer, and… and we don't have so much variability into the, … the telemetry producer space. … We thought about that, and there are various ways to serve that, either with eBPF or other options like that.
But right now, we are not focusing on that. We consider that, most likely, those collectors will be used in an environment where you have enough clients?
And then the balance will be automatically be… automatically be observed, and the kernel will do the good job for that.
So the… so that's how we see the design of this system. And… and minimizing… minimizing or avoid At any cost, the communication across those pipelines is important.
And the ultimate refinement in when we want to also minimize communication across core that are not… dependent on the same memory region, so that's why the new manhood, Discussion is, … is important. We also want to make sure that we are not adding invisible communication from… High latency, it's relative, but high latency communication across … element, specifically the metric system and each of those pipeline engines, making sure that we don't have a metric system running on one pneumonode and pipeline, reporting, dermatrix, events, and so on, to a different method than because we will add, interconnect, communication across the manner, and that will be, … That will add some additional latencies, and, and we'll also, Disturb in some way the… each of the core running on those standards.
I don't know if I answered all of your questions, but I tried to give you a little bit more of a… Deep view on the design of what we are trying to achieve.
jmacdonald 00:53:12 I put my hand up to see if I could, like, try and clarify, or see if we've answered, Ray's question in… maybe. And so, I mean, I heard the question about a weight group, and I heard the question about, essentially load balance across these threads and so on, and I couldn't tell whether, you know, from the start, whether we were looking at, like.
a challenge related to dynamic attributes, as we started the conversation with, or whether there was something about, what I consider to be called, like, a stream shuffle, or a, like, a data shuffle, where you say, there's a stream node that's overloaded, and what we really want to do is, like.
find a way to split that load somehow across either, like, threads within a machine or process, or across nodes within a cluster. I think that both angles get discussed.
are… is… like, what sort of are you looking for, Ray? I'm interested, or Mike, to hear, like, if you have ideas in this space,
Ray Jenkins 00:54:14 So, there's… I guess it was a two-part question. One was just, like, do you need coordination on this piece? I didn't see anything where there was, like.
coordination to say, well, I've asked this one… I've asked these new nodes to, like, report their metrics, and I was… I know that the collector handles it, but there was no, like, how do I know I'm getting it all? What does that scheduling look like that's happening there? Like.
what's the interrupt? How does it know, like, when… oh, I've got to go do this? There's a job? Because I'm assuming pipeline engine to me, that red box, I'm not exactly sure what's all inside that. And I guess that's where the question branched out.
So, like, do the receivers, are they part of that, you know, inside?
Laurent Quérel 00:54:50 Yeah, but a pipeline engine is the entity.
Ray Jenkins 00:54:54 Taking a pipeline configuration?
Laurent Quérel 00:54:57 And, instantiating the values node.
Ray Jenkins 00:55:01 Okay. Making sure that they are able to communicate between each other, and managing the control part.
Laurent Quérel 00:55:07 Of this pipeline.
jmacdonald 00:55:10 I would imagine that the latency of requesting metrics from each core, or from each thread, or from each NUMA region is going to be small in relation to the interval of over which your measurements are made, and then I'm expecting that there's some… even within a single SDK of all the OTEL SDKs I worked on.
Like, you issue these asynchronous callbacks, and, you know, there's a spread of time, like, when they were evaluated from the start to the end of your, like, asynchronous round.
And you kind of give them one timestamp, because, like, really, who's really… who really wants to be so precise with timestamps as to record, like.
non-exactly overlapping windows from all the instruments, because you collected them in sequence, and they weren't all collected at the same time anyway, right? I don't think that we need that. And if we ever do need something along those lines, again, we're looking at a metrics engine that's capable of, like, reasoning about time and doing, like.
proration and, like, interpolation and so on, which is something that you need to do in order to align temporal boundaries, usually, when you're combining metric data. So I would expect At some point, either you're going to wave your hands and approximate, like, this is a metrics SDK, and they may be off by microseconds, but they're not off by, hundreds of milliseconds. And then you're going to issue a request to each node, you're going to get back your metrics, and you're going to call it one time unit for the whole machine. Whereas.
In a more sophisticated model, you might actually maintain those separate time series, put them in a metrics engine, and tell the metrics engine to do the aggregation. And then the metrics engine might be responsible for noticing that it took a whole second to evaluate all your metrics, and so the boundaries aren't exactly aligned, and so you're like.
Break apart all the boundaries, put a fixed time window boundary in.
reshuffle all your counters so that they're approximately correct, and then redo the summation. That's a metric engine task.
We don't need that.
Ray Jenkins 00:57:11 Cleop.
jmacdonald 00:57:12 But I do want a metric engine.
I know we're almost out of time. I did want to come back just briefly to that discussion about dynamic attributes. It's one that users ask for in OpenTelemetry as well. I asked the question about bound instruments as a teaser, kind of. Like, I like to know what people think about bound instruments, because usually by the time you get to bound instruments, you say, oh, wait a second, I wanted something else, which was dynamic… dynamic attributes.
… the solution that I've seen… there are two. One is it's discussed… has an ongoing discussion in OTEL called a measurement processor. It's this idea that you're going to intercept the set of attributes As it happens dynamically, usually that's… because the application gave you some dynamic information, and then you're going to drop attributes or extend them with attributes from the context. So that's one solution that's been proposed, and I have seen that used. Like, I'm going to take a header from the context and make a metric attribute out of it. That's a pretty basic way to apply that.
But then, I don't actually think that that's a realistic way to go for us. It's an expensive way to go.
even though I have heard people discuss esoteric ways to approach it, like, you can, like.
on the same thread, do the work of, like, filtering your attribute set, or you can record the attribute set and let somebody downstream do the filter for you. Again, it's like… This is a metric SDK we're talking about.
In the real world, when I look at, rate limiting, as I mentioned earlier, I told you that I was looking at the Envoy model for how to configure rate limits.
And the way they would approach this problem of extracting dynamic attributes is really to define these things that you might call descriptors that are bound to routes, and so each route is going to have a different way of describing which attributes get dynamically extracted. And I think of this in terms, like.
gRPC is going to have one way to extract attributes, and HTTP is going to have a different way to extract attributes. And then they go through these definitions, which… extracts those things and then puts names on them, and then you can map the names into attribute values in a very well-defined configuration that is also used for rate limiting. So, typically, you make a quantity by extracting it, you rate limit on it, and now you can also report that as a metric.
MH Mike Heffner 00:59:40 Yeah. That makes sense.
Laurent Quérel 00:59:41 Definitively, I think the tenant example is a very nice example of where we could use the Or where we will have to use dynamic attributes.
… Yeah, I definitely like this example.
Ray Jenkins 00:59:59 the Envoy example really… … is complementary to, basically, the declarative model that you're… that you've already put in place, because you're… now you're just… as opposed to just doing dynamically, you know, writing the code, you're declaring, these are the rules that I'm going to use to extract it, and so it can fit into that declarative model.
Laurent Quérel 01:00:20 Yeah, yeah.
Ray Jenkins 01:00:21 Like, attribute set.
Laurent Quérel 01:00:24 ended.
I had a question for, … from Mike and Ray, … How do you see the… the… This collaboration between these two projects.
Ray Jenkins 01:00:44 We were just talking about that before we got on the call. I think, as Mike mentioned and Josh mentioned, we both had some, you know, some actions to take away, which was to do some prioritization on our side.
And Josh was gonna do some on his side, so probably get together and compare those notes. And then I told Mike, you know, about the first call and what we discussed, and one of the questions I walked away with when, you know, I chatted with Mike was just sort of, you know, what is the… You know, what is the sort of process, for, like, you know, figuring out what needs to be done, what work needs to be done, prioritizing it, where, you know, and uncovering where there's… you know, a fit for us to collaborate, and you know, could… where can we help contribute? What is… is there even a process yet? Because I… I think today, the SIG and the team, it's pretty tight. There's a lot of… folks from F5, you know, and then you have Josh, and so, just… have you guys given any thought to that? You know, how you're prioritizing this, breaking… breaking stuff up is, you know, is there a place… is there a process already in place that we could look at and say, oh, this is something that we're interested in?
Laurent Quérel 01:01:56 Yeah, we, we, … We started to define a concept of milestone.
I think it's referred there, if you go there.
we started to define, let's say, an intermediary goal for both F5 and Microsoft.
And, and we, we try to… to figure out a set of, GitHub issues attached to this milestone, and we… everyone in the Microsoft slash F5 team refer to that and try to, to see how they can contribute and make this, this goal, achievable.
So right now, we are starting to split the work in this way.
But we are still a small number.
And, and we have, … We initiate, usually, this meeting with, a first, Round of, discussion regarding the ongoing, effort, and if there are anything blocking, and if someone is available to do something, that's the period where they can mention it, and we can talk about what could be interesting to achieve.
Ray Jenkins 01:03:08 I think that's….
Laurent Quérel 01:03:09 the Chrome state.
Ray Jenkins 01:03:12 Makes a lot of sense. I think one of the things, I think, in order for… in order for us to collaborate in a manner where we're… contributing something to Rotel and, let's say, Arrow, one of the things is most of the work here on the Arrow project, obviously, requires OTAP support. So, for example, an attributes processor. This is an attributes processor that works with the underlying OTAP.
Yeah. So, we don't have that today. And I imagine a bunch of that work may be like that, but there may be some items in there that aren't so… hopefully when we get together and we talk about the the priorities. We'll find… find the things that line up, and then also likely find the… The… the blockers to… collaboration, I guess.
Laurent Quérel 01:04:00 Yeah.
Ray Jenkins 01:04:00 Try to knock those.
Laurent Quérel 01:04:02 This speed is a concept that we are using quite often in the discussion. Consider that it's like an abstraction layer, on top of either an OTLP message or an OTAP message.
And, and we started to… To investigate ways to… To use the underlying, … better model.
Either as a columnar-oriented model, or as a hierarchical model. So, I'm saying that because if you have, let's say, an exporter for PCAW, so an exporter for I know you have that. You could, in fact, consume the p-data in a way that will be probably closer to what you are already doing.
jmacdonald 01:04:54 Yeah, I was going to identify that as an area as well. Like, we've… we've committed much of our current, like, 6-month kind of experiment to the OTAP arrow representation, and I was going to mention the 6-month timeline really as, like.
this was the permission we requested from the hotel governance committee to, like, have this project scope, and that's why that milestone for the September demo is kind of, like.
we're all… we've already made those priorities, like, 5 or 6 months ago. And… And then when we get to that, hopefully the demo looks good, and then we create a sort of next step charter that the hotel GC will… and technical committee will approve, or not, that says what we're going to do in the next year or so.
for this project, that… remember, creating a Rust project in OTEL was already contentious, and so this is, like, how we manage that.
I would like to find ways to collaborate, and I think that one of the opportunities is to have that OTLP… plain old protocol buffer message transport, which I think of as a smaller scale from the producer side. Like, I don't want the whole arrow library here, I just want to, like, give you a piece of data. It's, like, one point, or, like, whatever. So it's like a smaller-scale SDK-like model, as opposed to a large-scale, like, mega telemetry processor model.
And when we look at the OTel Rust group, SDK has exporters, and we've already prototyped in this repository a batch processor, an OTLP exporter, and so on, that would work with protocol objects.
But what we found was that objects are a really expensive intermediate place to be. We would rather either talk about bytes, in which case the OTAP pipeline that we're dealing with is good, or maybe talk about bytes, and you guys have a better way to represent them And it's just a different runtime, like, a different runtime data type. And it's worth maintaining, too, because we need a good SDK. And also, not on the call today, but… but my co-workers, Drew and team, working on this KQL engine.
They don't either have an OTAP representation, they have something that looks a lot more like plain old OTEL data.
a lot more like what the SDK would output, and I'm pushing them to get to where we could run their… some of their KQL logic over SDK, like, events.
And then you wouldn't want OTAP in the middle of that. So I see opportunities to have Two good pipelines, one that's Aero and one that's not.
MH Mike Heffner 01:07:30 Yeah, I was gonna… I mean, I was gonna answer a little, … background, I mean, I think, you know, part of this is, you know, we went into… Ray and I went into this, sort of, with some opinionated ideas as to, sort of, what we wanted to build, and sort of what was sort of important.
To get in there, and that still sort of leads a lot of our prioritization, and I think, you know, it would be great to sort of see where that overlaps. I think the other thing, you know, how we've been balancing it is also sort of what are people that are coming in to either the Discord or opening some issues, like, what's sort of immediate interest? And that's also sort of changing a bit of our priorities on a sort of rolling basis, a bit as to sort of what we tackle.
Just to sort of give you an understanding of, like, how we've sort of prioritized things, and… Sometimes it's pretty fluid if somebody's, you know, coming in and sort of voicing support for, you know, some exporter or some processor-type support.
Laurent Quérel 01:08:33 Yep.
Okay.
MH Mike Heffner 01:08:35 So….
Ray Jenkins 01:08:39 I hope we answered the question.
Laurent Quérel 01:08:43 I think we're not.
MH Mike Heffner 01:08:44 Maybe muted there.
If you're saying something.
jmacdonald 01:08:46 Oh, there it is. My speakers are… my mic's working now. Anyway, I have committed to doing some work on roadmap projection, because it's become the end of the period over which I did that before, so… I don't have it here or now.
Much like I don't have my complete rate-limiting proposal either. So, but soon. I also haven't mentioned to everyone here, but Microsoft has an effort that's looking at ThreadPerCore runtimes, and I'm trying to get them to look at what we've got as well.
for some reasons which I will share more about in the future, I need the roadmap for them as well, so I'm putting together some work on where we are, how we got here, and what's ahead. And I would still love to look for ways to keep, to get you and Ray and Mike involved.
however we can help. I'm… we'll meet more and talk more about that.
MH Mike Heffner 01:09:37 Sounds good.
jmacdonald 01:09:40 All right, thank you all. I'll see you next time. It'll be a Tuesday.
Laurent Quérel 01:09:45 Thank you.
jmacdonald 01:09:45 Thursday. Thursday. Next week, Thursday.
Laurent Quérel 01:09:47 Thrilled to you.
