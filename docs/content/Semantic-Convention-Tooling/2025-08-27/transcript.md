SIG: Semantic Convention Tooling
Date: 2025-08-27
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Jeremy Blythe** 01:44 Hey there, man.
**Liudmila Molkova** 01:49 Oh, hi, Jeremy. I was not sure if anybody is going to come anytime soon.
How are you?
**Jeremy Blythe** 01:57 I'm good. How are you doing?
**Liudmila Molkova** 01:59 I am good.
**Jeremy Blythe** 02:01 Yeah, it's just crazy busy right now, but anyway….
**Liudmila Molkova** 02:07 Busy is good.
**Jeremy Blythe** 02:10 It is. How's your new, … Your new job?
**Liudmila Molkova** 02:15 It's awesome, I'm… I'm learning to… what developer advocates do. Turns out nobody knows what.
But yeah, people… well, they do know, but it's a very broad… Spectrum of things.
**Jeremy Blythe** 02:32 Yeah.
**Liudmila Molkova** 02:34 Which includes sometimes writing REST code.
**Jeremy Blythe** 02:39 Nice.
So do you get… do you get, like…
Time to work specifically on open source, and…
Like, as part of… as part of the role? Is that, like, included in… the role?
**Liudmila Molkova** 02:57 It is included in my role, and Grafana is very big on OpenTelemetry, so there are other people at Grafana who work
On up a telemetry on the….
**Jeremy Blythe** 03:10 That was fun. Wow.
**Liudmila Molkova** 03:11 Like, 90% or something.
**Jeremy Blythe** 03:17 That must be nice. Yeah, I'm just…
Struggling to find pockets of time where I can do anything other than work at the moment.
Anyway, I did get the go-ahead for our talk to… …
put it in the actual code, and then we can show, like, like, work code, and then I can show some of that. Actually, I can use, like…
probably next couple of weeks, I'll… …
like, share an idea of what… of what I could show.
With you, and then maybe we can figure it out from there, but… … Yeah, I'm thinking….
**Liudmila Molkova** 03:58 Go ahead.
**Jeremy Blythe** 03:59 It's a new thing that we're making, and it's got different microservices, and so this is a classic case where you want to have
… a single… … sort of…
Company-wide or department-wide, registry of
I'll have attributes and some metrics.
… But those microservices need to… All use the same…
Stuff, obviously, is the whole point of this. And so, the live check will show …
I want the live check to pull from the… the master source…
when it's in CI CD, so it's gonna pull… it will pull… it will always pull the latest to do the check, and then it will fail you because, you haven't… you haven't kept up with the changes in the…
In the registry, right?
**Liudmila Molkova** 04:57 Nice.
**Jeremy Blythe** 04:58 If you've got, like, 3 or 4 microservices, they're all… they all should be talking the same, they actually… they won't… they won't pass.
Which I think is, like, a key point of life check, right, is that…
So I think if… if somehow I… somehow we can bottle that into…
part of the 25… 25 minutes. Show some bits and bobs.
I think, … That would be good.
**Liudmila Molkova** 05:22 Yeah, and I mean, it sounds like a Dhamma, right?
**Jeremy Blythe** 05:26 Yeah, demos are dangerous, though, aren't they?
**Liudmila Molkova** 05:30 We… it's actually the… this…
Previously, on observability Day, they recommended pre-recording demos, so you can just record it.
And then you don't… you talk through it live, right? But then you don't need to spend time typing and, running things.
**Jeremy Blythe** 05:54 Right, yeah, that makes sense. Okay, so you can just, like, play a recording and hit pause and talk and play and….
**Liudmila Molkova** 06:01 Yeah.
**Jeremy Blythe** 06:02 Okay.
**Laurent Quérel** 06:04 I wouldn't belong, do you know what I mean?
**Liudmila Molkova** 06:06 Sorry to be late.
**Jeremy Blythe** 06:08 That's right.
**Liudmila Molkova** 06:12 I'll probably need to drop off around…
30 minutes, so I have just 20 minutes today.
**Laurent Quérel** 06:21 I have a small topic to discuss, if we don't have anything, urgent.
Last week, I mentioned this concept of metric, multivariate matrix, or matrix set.
**Jeremy Blythe** 06:36 ….
**Laurent Quérel** 06:38 So I took, … Not too many times, unfortunately, but, …
I can share what I have and discuss the concept.
And potentially, get your feedback.
… if that's okay.
**Liudmila Molkova** 06:55 Good.
**Jeremy Blythe** 06:56 Let's do that.
I may have to cut this short myself, so….
**Laurent Quérel** 07:06 Yeah.
**Jeremy Blythe** 07:06 If we jump into that, that would be a good use of time.
**Laurent Quérel** 07:09 Okay.
So, let me see…
Yeah, so it's, it's super light in terms of explanation, so that's why I think it's, …
And I will definitively update, …
the GitHub issue, and link into the…
to what we discussed, last week. This earlier session started
while Lumila was mentioning the concept for reintroducing attribute groups into the version 2 of the schema.
**Jeremy Blythe** 07:43 Yep.
**Laurent Quérel** 07:44 And I was saying that, … Attribute groups could be…
Not only useful has a logical entity to group attributes.
But also as, a way to define
The fact that, when you have multiple metrics that are related together.
And they transformed… and we want to transform them into…
A logical, multivariate set of metrics.
then, we have two choices. So, I created an example here. Imagine that you have this list of attributes.
… This list of metrics.
And in that case, they are still… what I named Univariate matrix.
… As you see, there is no attribute in this case, but that's part of the discussion.
And then we have, a metric set.
This metric set is named this way. We're grouping this list of attributes, and this is… this list of metrics.
This entire thing is… what I will name a composite… a composite signal. It's, in fact, a signal with…
a timestamp, a group of attributes, and a group of metrics all together. And when we report.
That we report multiple detachments.
Pulled together. So they share the same timestamp and the same attributes.
So, one option is being able to group multiple metrics, Inside this metric set.
And if… and just link the attributes.
Another ex… another option would be…
Reuse an attribute group that already do this grouping of attributes.
And then, we can just say here, attribute group, and add the name, and then we have, by construction, the fact that those metrics share
All the symmetry bits.
So now, what happened for Matrix?
Individual matrix that already have attributes.
My proposal is, in that case, I think we could imagine two… two options.
… at least I can imagine two options, maybe they are more.
First option…
We just ignore, individual attributes or individual metrics, and what matters is the… either the list of attributes.
Defined for this metric set.
All the achieving group.
Second option, if a list of attribute is not defined.
And what we do is grouping metrics that share already implicitly
I would say… I should say, explicitly.
That will be better. The same group of attributes, but it's inferred by the tool.
then we could authorize also the fact that in this metric set, we don't redefine the DSF attribute. Personally.
I think the silver option is a little bit brittle, because…
Any intervention on the list of metrics?
Could make this metric set, … No longer metric cents.
So that's why I think being explicit
And… and forcing people to describe
The list of attributes explicitly, either with an attribute group or with a list.
of attribute is probably better.
no, … And I… And I should have started with that as an introduction, why we need metric sets.
… So this example is not coming from nowhere. It's an example coming from… this, Rust base, …
I should not say collector, but, let's say, …
A pipeline engine that the group collector could use.
And…
We are designing this system to be very efficient, in terms of performance, in terms of memory usage, and so on.
And we want to come with a predefined pipeline instrumentation.
that, for any node into the system, and as the collector, we have… we use exactly the same concept. Receivers, processors, exporters.
They are interconnected with… Some kind of communication channel.
And, … By default, we define an automated instrumentation But, …
For each of those nodes for, …
Each of them… there is a collection of metrics that we… So, for example, the…
what we name the Perf Exporter, so it's a new kind of exporter.
We could imagine the batch processor, for example.
… It's relatively obvious that we have to define multiple metrics.
That will, for example, for the batch processor.
We'll rely on the type of batches we receive, how we accumulate them, what are the conditions that are triggered.
The size of this batch.
So, all those metrics are, in fact, captured by the batch processor.
When this processor receives, Group of signals.
… So, either we maintain multiple metrics.
And then we report each individual matrix with our group of attributes, and the override is not negligible, especially when
The… the list of metric is, important.
Let's say you have 10, 20.
With the existing, client SDK and the way that we define metrics inside OpenTelemetry.
Even if all those metrics, and most likely in this specific context, the batch processor, all those metrics will in fact capture the same context. So there is no reason that they will not capture the same attribute.
So, … Artificially, we are forced to…
Report multiple metrics with the same group of attributes.
So, and that's why, when performance matters, it's important to
Keep only the contours, or the gauge, or whatever matrix your instrument you are maintaining for this specific node.
And report this set of metrics with a common set of attributes.
You will avoid a lot of duplication.
The reporting will be easier.
The memory consumption will be smaller.
And, once we have an update, At the protocol level, The amount of information transported
To report this type of information to a backend will be also a lot smaller.
And, and there is, …
A nice fallback, in case you are using a backend that does not support
a concept of multivariate matrix. We can always decompose a multivariate matrix, or a matrix set, into multiple univariate matrix.
So that during the ingestion, we will basically recreate individual metrics, take each… and duplicate each time the attribute loop.
So that's, … how I see the concepts
And, how we could leverage semantic convention to describe
This new type of entity?
So, Telsey, by your… by getting your feedback and, and the discussion regarding the attribute group. I didn't mention Attribute Group there, but…
I mean, I mentioned it, but I didn't represent it. That could be something like,
attribute, groups… So, I think here we have a name.
… It's June… just, … Not thinking a lot about that, but that will be something like that.
… Except that we have reference, I think.
The format is not exactly this one, right?
**Liudmila Molkova** 17:01 Yeah, I mean, for your proposal, the attribute groups can be used, or you don't… but don't have to be. You don't really care about the attributes.
**Laurent Quérel** 17:08 Yes.
Yes.
Yeah. Yeah.
when I wrote this example, I was thinking, okay, what are the different options?
And indeed, attribute groups could be an option, definitively.
But that's not the only one.
**Liudmila Molkova** 17:26 Yeah.
Which is nice. So it is just, it would use the attribute groups in the same way as,
Any other, signal?
**Laurent Quérel** 17:36 Yes.
**Liudmila Molkova** 17:39 And you… under the metrics, you would actually say, okay, this… the… you would provide different unions, different descriptions, right?
Different notes, different deprecations… Different.
**Laurent Quérel** 17:53 Oh.
**Liudmila Molkova** 17:53 Or same stability on all? I guess same stability on the whole.
**Laurent Quérel** 17:58 Yeah, I think the same rule would apply.
… Yeah, that's definitely, the kind of detail that needs to be, …
defined more precisely. To be honest, I didn't, …
Think too much about it yet.
**Liudmila Molkova** 18:19 Yeah, it seems straightforward, there is nothing that wouldn't work. Yeah.
The deprecation on one of them. Well, why not?
Yeah, it… I mean, your proposal makes total sense.
**Laurent Quérel** 18:50 Okay.
Okay, great.
**Jeremy Blythe** 18:59 So… Today, you could use this definition, but for plain…
Plain old OTLP as it is today.
We would create a metric for batches, invalid batches, record, like…
So we'd have 1, 2, 3, 4, 5, 6, metrics produced.
And each one of them would have those… Movement, it is 8 attributes.
**Laurent Quérel** 19:26 Yes.
Yeah, and so technically, because of the… underlying…
constraint we have with the protocol. And also, in fact, with the…
the API of the client SDK.
We… we force people to, in this specific context.
To create 6 times more attributes that we should.
Because for each metric, you have to replicate this set of attributes.
Again and again.
**Jeremy Blythe** 20:01 Yep.
**Laurent Quérel** 20:02 And it's far from negligible, especially if this group, increase, obviously. For example,
at F5, we do different projects. We, we have, I think something like 30… HTTP-related metrics.
So, and those metrics are captured …
We use those metrics to measure the initiative in traffic.
There is no reason to separate those metrics.
Because, in fact, they are captured at the same time. Some will be more focused on latency, some will be more focused on size.
And various other things. At the end, we end up with something like 30 metrics.
And, I don't remember the exact number of attributes, but it's something like 15.
So… 30 metrics, multiply by 15, that's the increase that we, artificially …
force people to do when they want to use open telemetry in this kind of context. And my idea is…
In fact, That's probably the most common situation when you are reporting metrics.
And, people are so used to, to consider that, each metric.
All metrics are independent.
But in fact, they are not solely independent.
And that's why we have this concept of correlation and other things like that, because…
The example I'm taking always is the X and Z coordinates for a mouse. Imagine that you transform the X and Y, sorry, the X and Y
as metric.
they are not independent. When you move.
Your mouse, each of your movements.
the X and the Y will not move in random situations if it's a real mouse. You will have some behavior between the X and the Y, just because they are physically,
Related.
Same thing happened here, for example, the number of logs, span, and matrix
when you combine them all together, the number of batches should not be totally… for example, we could not have more batches than the sum of logs, files, and metrics.
At least we have one of those elements per batch, minimum.
So the… that's another example.
**Jeremy Blythe** 22:59 It's interesting not to do with this, but it's… It's interesting why… I guess…
You could represent all this data as attributes on a single span.
Right, I could have… I could have an attribute called….
**Laurent Quérel** 23:14 We… we could imagine using…
I will say that differently, but I see where you go. I will say you could have metrics integrated into the span, all those metrics integrated into the span, so they will share the same list of attributes.
**Jeremy Blythe** 23:30 Yeah.
**Laurent Quérel** 23:30 People… some people are doing that.
But that's very limited, because, …
Then, what happens if you want to describe an Instagram?
… histogram are complex, … Object.
And, and there is no good way, … to encode an histogram into an…
an attribute of span.
**Jeremy Blythe** 24:03 Yeah.
**Laurent Quérel** 24:04 You could, in theory, because attributes are, …
Or basically, there could be anything in open telemetry.
Could be, object of, object, and blah blah blah, but, …
But it's, it's unfortunate that, and then when, when this specific kind of span traverses the collector, oh.
Valerie Medina. Thank you for the feedback.
**Liudmila Molkova** 24:30 Yeah, thank you. See you later.
**Laurent Quérel** 24:33 Yep.
**Jeremy Blythe** 24:35 Yeah, I'm not saying, like, I guess I'm just saying it's something that…
At my company, we haven't done an awful lot of metrics yet.
But we've… we often have, like.
I guess.
Chunks of data like this.
And to this… Up until we get more…
I'm trying to make things more… Standardized.
And so I'm going through a journey of, like, hmm, actually this stuff should be…
Would be better represented as a metric at this point, where we've…
always gone through and gone… like, we just use spans for pretty much everything, even though we have data that's not….
**Laurent Quérel** 25:21 Yeah, and the override of a span… a pure span approach is not negligible.
So that's why, in that case, some people, when they figure out that their system starts to be a little bit, …
Unperformance, because we collect too much span.
We, we observed that in some projects also, in, inside AFL. Then they, they, logically moved to matrix
For some situations.
Hi, Josh, … I was, presenting, the concept of matrix set, or multivariate matrix, It's, …
clearly a not well-defined, definition into the schema V2.
But that's something that's, … We are using for the, this, …
a Rusty, engine that you are aware of?
… We, we, where performance really matters, and we, basically…
Introduce, a new kind of, … telemetry SDK.
Where we, we can report multiple, metrics.
For the same timestamp and the same group of attributes.
Saving us a lot of, duplication and, …
And I was, thinking that we… we could imagine at some point encode…
This, semantic of a group of metrics.
using the schema V2.
And, we could even, at some point, generate a client SDK that natively …
Simplify the… this specific use case.
Where we… we want to report multiple metrics and… and avoid all the internal duplication that, …
People have to use today.
And even later, we could imagine some extension for TLP and OTAP, …
In order to reduce the volume, the traffic.
That's… and the example is… is there. We… we…
We have all those metrics that are reported by one of the components. In that case, it's the… what I named the perfect supporter, so it's a…
Specific type of exporter.
Maintaining all those metrics altogether.
For the same context?
And, … and we could describe These metric sets?
That's the name I use to represent multivariate matrix.
And, and we specify… The common set of attributes.
And for which metrics this common set of attributes is applied.
And this entire thing represents… A composite signal.
With this name, And with this definition that will rely on metrics and attributes.
Obviously, there are some details about, okay, some metrics here could already have attributes, what happened for them, and so on, so we discussed that before, but my conclusion, or my proposal is
we force the definition, the local definition of attributes for a metric set, and we ignore any attributes for the metrics that are grouped here. So they can either be used individually.
Or when they are used, As a group, or as a set.
They share both attributes.
**Josh Suereth** 29:12 So… I… Sorry I'm late, but I…
I think that's kind of bad, Lauren. Like, I think…
How do I want to phrase this? I think you should define metric sets that have metrics in them, and then just require the metrics to have the same labels.
….
**Laurent Quérel** 29:32 That's another option that I mentioned, but I don't like this one, but I have my own reasoning behind that. Looks like you have the opposite.
**Josh Suereth** 29:40 Don't define the raw metrics.
Like, just don't define the raw metrics, just define them as multivariate to begin with.
Right? ….
**Laurent Quérel** 29:50 That's a solution, okay?
**Josh Suereth** 29:54 But here's the thing, I have generic code that, like, renders all metrics, and I'm gonna have a thing called batches that has no attributes associated with it.
In the world that you're showing here. And that's weird.
Right? That's, that's, that's like… that's not what you want.
**Laurent Quérel** 30:11 So let me, let me, ….
**Josh Suereth** 30:13 It has these same 7 attributes as invalid batches, right?
**Laurent Quérel** 30:17 So… so let me, … oppose some argumentation that are not aligned with what you are saying. …
Okay. My TVs is… already today, inside semantic convention, and obviously inside OpenTelemetry.
We have a long list of multivariate metrics that are, …
described as univariate matrix. So, example.
All the processor-related matrix, all the memory or disk-related matrix, they are all motivated by nature.
**Josh Suereth** 30:57 Yep.
**Laurent Quérel** 30:58 Most of them, if not all, are already sharing all the same attributes.
**Josh Suereth** 31:03 Yep.
**Laurent Quérel** 31:03 So what you are saying, if I follow.
We should redefine all those… all of those metrics.
artificially, to create a metric set. What I say is either we reuse the existing attributes.
And we just put them here, and they could be used independently or grouped into a metric set.
Or we infer this list of attributes because all those metrics, share the same attributes.
The problem with that… is… in my opinion, it's a little bit brighter.
Because… If someone is changing one of the attributes into one of those metrics.
Then, it's no longer a metric set.
So that's why I was more explicit, but ….
**Josh Suereth** 31:56 this is why we could… we could… okay, so there's a few things you can do to… to work around that, but yeah, I… I'm a fan of, …
If you're going to allow them to be metric sets and raw metrics, right?
It means that we have to support both models, which means it has to be true that if I look at the metric, I get all the attributes. If I look at a metric set, all the attributes are the same. Both of those things have to hold true, somehow.
So, like, I think we could infer and fail builds if the inference fails. So if
If you try to put a metric in that doesn't match the other ones, you fail and explain which one is not the same.
Right?
We're actually… Yeah, okay. We're getting closer and closer to building a structural type system here. It's pretty exciting. Anyway, …
But, like, that… I think that would be a better experience, and then if you want to share attributes to make it explicit, if the attribute group comes back, the way, like, Ludmilla wants to do this for sharing things… Yeah, that's….
**Laurent Quérel** 32:56 I was.
**Josh Suereth** 32:56 group, yeah, that we use in all the metrics. So instead of, like, basically there'd be a convention where we'd have document… we'd have a YAML comment on each metric that says, this is used in a metric set, don't add attributes here, add it in the shared group.
Right?
As an example. So we could have, like, a convention for how to make metric sets, and then just make Weaver fail if you do it wrong, and tell you… and give you good error messages, right?
**Laurent Quérel** 33:24 Okay, … I understand the argument.
I will complete this, … GitHub To describe the value subscriptions.
… So we… so we can feed, ….
**Josh Suereth** 33:49 a discussion between the… between us and Lumilia and anyone that is interested by this topic, in fact.
**Laurent Quérel** 33:55 So to summarize your… what… to summarize what you are, advising, …
We… when we group univariate matrix, this, list of attributes is inferred And we have, …
A checking stage, … That makes sure that all the metrics that participate in this metric set
are, in fact, really sharing the same set of attributes. Either we rely on the attribute group, or we inspect all the attributes defined in the attribute list of the corresponding matrix.
And we fail, the, this, …
Checking, phase by saying, oh, you have one other metrics that does not have the same attribute, so it's not really a metric set.
Maybe another option for people that want to create natively a metric set.
will be… The matrix will be… a new kind of matrix without attributes will be defined locally here.
And, and then it's… Because they, they, let's say they don't have any meaning alone.
And then we can explicitly mention a list of attributes. Is it, exactly what you described, or, …
I'm contradicting what you are, describing.
**Josh Suereth** 35:33 I'm not sure, because I have to think through it, but the…
I don't know if I caught everything. The…
the thing I want to make sure of is, if I look at a metric.
All the attributes that are needed for that metric are there, regardless of if it's a metric set or a raw metric.
That has to be true.
The second thing I want to make sure of is I can't put a metric set
That has attributes that aren't used by the metric set.
They should use… have the same set of attributes, if it's in the metric set.
Those are the two things I want to enforce are true.
And whatever design we come up with that makes sure that those things are always true, and Weaver will fail
To resolve your schema if they are not true.
Is important to me.
Right? And then secondarily, can we give good error messages when that happens? But those are the two things, I think… those are invariates in this design.
**Laurent Quérel** 36:30 And can you explain the reasoning for the first invite, for example?
**Josh Suereth** 36:35 The first invariate… so, if I define a metric, and I say, here's a metric, right? Regardless of whether I send it as a multivariate metric, or send it as a raw metric, that's a choice that I make around optimizing my reporting interval. It's not necessarily a choice I make when I consume the metric.
Right? So, like, if I'm using a metric database, and I want to query a metric based on attributes.
I, I might, I may or may not…
Care that it was reported
In a group, right? That doesn't matter to me, necessarily. I just need to know the name of the metric and the attributes that I query from the database that I'm querying them.
**Laurent Quérel** 37:14 Commission… Don't you think that, …
There are, in this world, matrix that…
Without, correlative matrix, does not have any meaning.
**Josh Suereth** 37:28 There are metrics that what, without multivariate, have no meaning.
**Laurent Quérel** 37:33 … the example that I took with Lynn Miller, for example, and Jeremy, was, …
The coordinate, for example, longitude, latitude.
or the X and the Y for….
**Josh Suereth** 37:49 Coordinate of what?
**Laurent Quérel** 37:51 Longitude and latitude, it's not many….
**Josh Suereth** 37:54 Absolutely. That's not a metric.
**Laurent Quérel** 37:57 No, it's not a good example, but, I mean, the…
Let's set, like, another example, which will be better than that.
…
We have a physical system, and we measure two elements of this physical system, and those metrics are
Really correlated together.
**Josh Suereth** 38:25 Independently, they… I mean, they are never used independently.
**Laurent Quérel** 38:30 I think we could… we could imagine such, … Physical system where, …
There is sometimes combination of metrics that matter, but independently, they are, in my opinion.
**Josh Suereth** 38:43 I mean, we can.
**Laurent Quérel** 38:45 So the….
**Josh Suereth** 38:45 imagine that system, but if you want that to exist, you need to propose that to the metric data model. In the metric data model today, for open telemetry, we only have individual time series.
**Laurent Quérel** 38:56 Yeah, I know, I know. That's very unfortunate.
**Josh Suereth** 38:59 I… right, but I guess what I'm saying is, if you want, like.
The behavior we have today, and the notion of metric set today.
Like, let's pretend I report a metric set, and I want to use it in Prometheus. It's gonna expand out into multiple time series, and I want that experience to not be crap.
It doesn't have to be great, but it has to not be bad.
**Laurent Quérel** 39:20 Yeah, but that is automatically, derived from any multivariat metric could be… could be, derived into multivariat matrix.
**Josh Suereth** 39:29 Sure, in which case, all of the attributes are part of the raw metric. So now, if we talk about data modeling, if you're going to have raw metric names that are called metrics, those are time series in Prometheus. And so, if you're going to go from metric set to metric.
version, it needs to be consistent, it needs to, it needs to fit. Like, like, the models have to match. So that's why I have that first invariant of, if you're gonna have a set of attributes for these metrics, if I look at the metric individually, all those attributes need to show up, because I've converted into something Prometheus.
**Laurent Quérel** 40:04 Yeah, yeah.
**Josh Suereth** 40:05 Right? Okay.
**Laurent Quérel** 40:06 Yeah.
**Josh Suereth** 40:07 I'm fine if you want to change our metric data model to have a notion of metric set, where you don't need backing raw time series and metrics, that's fine, but we have to make that proposal in the spec, right? If we don't, then what I would say is metric sets are kind of an advanced concept that Weaver layers on top of OpenTelemetry.
I… I personally still think you need to do some protocol support for metric sets. Like, I would….
**Laurent Quérel** 40:31 I mean, that's, that's, I mean, so used for me that, I mentioned that when you were not, present during the meeting, but,
I mean, matrix set, if we want to leverage this concept, we have to do it end-to-end. It's not only the protocol, it's also the client SDK, in fact.
**Josh Suereth** 40:47 And we shouldn't.
**Laurent Quérel** 40:49 I was talking about primitives that doesn't support that properly, but … and fortunately, some of the backend already support this kind of concept.
Yeah, yeah.
**Josh Suereth** 40:59 This is, this is why, when I say protocol, the reason I mention that is, I think, in terms of dependency chains.
**Laurent Quérel** 41:05 So, like, the protocol is the foundation of OpenTelemetry.
**Josh Suereth** 41:08 We have to figure out how to layer it through all… so it's not just that… it's like the APIs need it, all the SDKs need it, all the downstream consumers need it, we need… we need some sort of data model mapping. Like, it's… it's almost metrics v2.
Which, by the way, I'm proposing that we have a Phase 2 of metrics that we, specification that we go through and clean up all the things we didn't do for Phase 1.
Oh, that'.
**Laurent Quérel** 41:32 Which will, what would be the…
the new things into this metric V2.
**Josh Suereth** 41:38 In Phase 2… so Phase 2, I think there's a few things we need to do. One is we need to finish all the advice API work and get that rolled out. That's… that's a big part. We want to move to exponential histograms being default.
Gauge histograms is another thing we kind of discussed and negotiated.
There are a set of data points we have to sort of sort out, whether we're going to support them or not. Like, one would be info and stat metrics. Multivariate metrics is another thing for us to kind of sort out and understand.
So, I think there's those. The last one is, …
We don't use… so we have an exponential distribution in our protocol, right?
There are still systems that use, sketch-based or quantile-based.
**Laurent Quérel** 42:25 I really like Datadog.
**Josh Suereth** 42:26 So the question would be.
We never defined a compatibility layer from our distribution to those sketch-based protocols. Are we going to provide one or not?
**Laurent Quérel** 42:37 Okay.
**Josh Suereth** 42:38 Do we need something like that? So there's, like, a set of things. Now, we have to, like, prioritize those, because not everything I said is actually worthwhile. I think multivariate metrics would be high on my list, because today….
**Laurent Quérel** 42:50 Maybe that's the only one that matters, but ….
**Josh Suereth** 42:53 Well, multivariate metrics, I tell them to use logs.
It's not a great solution.
**Laurent Quérel** 43:00 Yeah, that's exactly what Jamie was mentioning, why not using span, but honestly, that's a shame to use span or logs.
To represent multivariate matrix. We did that, by the way. But, ….
**Josh Suereth** 43:14 Then you, you….
**Laurent Quérel** 43:15 You can't use the connector to manipulate those metrics, because it does not recognize the….
**Josh Suereth** 43:23 The main thing is with multivariate metrics, if you have multivariate metrics, you need to make sure they have the same set of, start-stop timestamps.
Right? Because the key is, the difference between a log event and a metric is a metric is an aggregation of events over time.
Yeah. In some form. And so.
You know, like, if we think span is a time span, if you will.
Like, a start-stop time, or a latency.
At a point in code, right?
We think events are just… structural data.
**Laurent Quérel** 44:04 What I'm seeing is… And metrics for aggregated events, right? I'm not advocating to use span or to use log.
and I….
**Josh Suereth** 44:13 No, no.
**Laurent Quérel** 44:13 it's a very bad idea to do it, but right now, people are using that because that's… they are… they have no other choice, unfortunately. And it's not correct, yeah.
**Josh Suereth** 44:24 If you look at these descriptions, though, it motivates the need for multivariate metrics, because we can explicitly say, we don't have… like, events are one point in time.
But it doesn't remember the aggregation capabilities that were used behind
that set of events that are aggregated. So multivariate metrics being a counter is important.
Because the same way our metrics model is supposed to have implicit spatial aggregation, or temporal aggregation, you could do that with multivariate metrics, right? If I get reported of a timestamp and report of another timestamp, and they're delta aggregated, I could put those two together by default without understanding anything specific to the metric.
Because I know it's a bunch of counters, or….
**Laurent Quérel** 45:08 You all try… I mean…
don't try to convince me on that, because I'm working on that now for 4 years, and … I'm trying to change that inside OpenTelemetry for more than 3 years.
**Josh Suereth** 45:20 Yeah. In fact, that's something new.
**Laurent Quérel** 45:22 the Open Telemetry Apache RO project just for that, and … when I discovered that it was way too much work to convince everyone that multivariate matrix matters, then I decided to
to, reduce the scope of the open telemetry Apache Arrow protocol just to support the existing signal and not multivariate, because at the beginning, it was supporting multivariate matrix at the protocol level.
**Josh Suereth** 45:47 I think at the time when you're trying to push multivariate metrics, we didn't have metrics working.
Fully. So it was just, like, a, compounding interest problem of OpenTelemetry and our attention… our ability to do things, right? We need to have, like, laser-focused attention on stuff. So, I do think what I would say with this metric set stuff, and I know that you need it, I still think we need to finish…
V2 gives us the capability to add metric sets in, I think, a comprehensive and clear way in the future. I still think we need to finish the V2 specification of Weaver, get the application telemetry schema stable and advertised and fully specified.
**Laurent Quérel** 46:30 Understood.
**Josh Suereth** 46:30 Yeah, because until we do that, we're in this limbo of… we have a whole bunch of work sitting here, and we have these big projects we need to pick up. So, I think we need to finish some of the projects we have now, and I know you're busy with, like, Arrow and the, …
The way I think of it is a SIMD-based collection.
The thing you're working on now, right? And I know that that's taking a lot of time, and I think that's valuable.
I still think when it comes to Weaver, like, let's… we need to nail that and land it.
So that we can take time to then pick up the next big thing. And I think multivariate metrics, I agree with you, we should build them.
I think it's gonna take time to motivate that. We could make… we could do writing and the, explanation of the community, the gardening of the idea.
But I don't think we're at a point we can execute on it.
**Laurent Quérel** 47:23 I totally agree. I just, opened this conversation in direction to…
the discussion we had last week with Romila when she was
asking, okay, do we need to reintroduce the concept of attribute group? And I told her.
In fact, there is a direct use for attribute group independently of this logical group of attributes.
**Josh Suereth** 47:48 It could be also something a little bit more semantic, because….
**Laurent Quérel** 47:52 For, for a metric set, …
Semantically, this concept of attribute group makes total sense.
**Josh Suereth** 48:01 Okay. I'm also thinking of proposing, … proposing a attribute type.
**Laurent Quérel** 48:10 Oh, yeah? To define, more precisely the…
the… the verification, or the… the checking of the, yeah, the fintech, yeah.
**Josh Suereth** 48:20 Yeah, but it would also let us define, say, like, any values. Like, so we could say this attribute type has a structure that's, like, lat-long points, right? We could say this is a location, it has a latitude and a longitude.
Yeah, and then we can reference that type in the type column on attributes by name.
**Laurent Quérel** 48:40 Yeah.
**Josh Suereth** 48:41 So, yeah, that's the other thing I want to add to V2. I think it's… we're long past due for that.
It also means in Noomes, I'm hoping, will actually have names.
And instead of type is just an open YAML hell.
**Laurent Quérel** 48:57 We change it to be type, and then the name of the enumeration, and we have explicitly defined enums that you can reuse places. Yeah, yeah, yeah.
Yeah, I agree.
That's really nice.
**Josh Suereth** 49:09 I'm sorry I missed everything. If there's anything else you wanted to talk about or whatever, let me know. I, ….
**Laurent Quérel** 49:15 ….
**Josh Suereth** 49:16 In terms of work, I'm working on V2, the phase where we… after we resolve schema, generating something that looks like V2 from resolved schema.
and firing that into Weaver Forge and things. And there's a bunch of, like, … there's a bunch of open questions we'll have to talk through, but I'm still in the…
sorting through my thinking of it, so I can't coherently talk about it yet.
But just for context, it's things like, how do we want to deal with lineage? Because I have to convert from lineage of groups to lineage of, you know, metrics and attributes. So, that's gonna be kind of the questions I'm bringing, I just haven't sorted through what I want to do initially yet.
**Laurent Quérel** 50:01 Yeah, and thank you so much for working on this, SlimHavy tool.
If you see anything that, …
Where we could split a little bit the work. Let me know,
Yeah, right now I'm super busy, but, …
depending on the nature of this work and the size of this work, maybe I will be able to help.
**Josh Suereth** 50:25 I think… a foundation?
And then have a lot of, like, little things that we can clean up, so we might be working in the same code file, but we'd be working in different functions of that file, if that makes sense.
**Laurent Quérel** 50:40 Easily. Yup.
No, I had, some, …
weird ideas, recently, after reading an article, and I just want to share that with you, because I think,
You will instantly see the… The optionality that we have there, …
So, do you know, KCN?
**Josh Suereth** 51:05 Which, which VM?
**Laurent Quérel** 51:07 the… this configuration language named KCL.
**Josh Suereth** 51:12 Oh, no, how did… can you spell it for me? Sorry.
**Laurent Quérel** 51:16 K?
**Josh Suereth** 51:19 KCM.
That's what's wrong.
**Laurent Quérel** 51:22 L, L, like Florence.
**Josh Suereth** 51:23 CCLM.
configuration.
**Laurent Quérel** 51:26 KCL.
**Josh Suereth** 51:28 Yeah.
**Laurent Quérel** 51:29 Sorry for my very, very bad accent.
**Josh Suereth** 51:34 ….
**Laurent Quérel** 51:35 KCN, programming language.
Let me send you the….
**Josh Suereth** 51:41 Yeah, send it to me. I, …
Oh, wait, no, I just… I think I found it. kcl-lang.io.
**Laurent Quérel** 51:48 Exactly. So….
**Josh Suereth** 51:50 Oh, this, CNCF sandbox project, got it.
**Laurent Quérel** 51:53 Yes, use a lot in the Kubernetes world. …
There are some very interesting stuff there.
You define schema, you define constraint.
But what I'm… I'm talking about that because it happens that recently, the entire group behind KCL.
has rewrote, rewrote the, the…
they rewrote the… their entire language in Rust. So the…
In fact, those, those crates are available.
And…
it's like a mix between our own YAML definition and Rego, to some extent, when you have to do some validation.
Except that it's fully integrated into, a nicer language, easier to understand.
So I was…
just exploring, the idea of how could we leverage that? And right now, my ideas are not very clear and… and, …
And well-defined, but, …
I just want to let you know that, maybe there are some options that we could, Checked.
with this schema V2.
Initiative, and see if there are ways to leverage that, because they have, … bridges.
between their language and any, things like, JSON, YAML, whatever. So the… there is a direct translation
… we could consume a YAML as it is with the…
the schema V2, and describe the schema of this YAML, like we do with the JSON API, for example.
Except that we could do it with KCL, and we could also integrate constraints inside this description.
So we could have, in fact, a smart YAML parser.
Not only checking the schema bag itself, but also checking some properties inside the subject.
So that's, maybe an interesting project to… to check.
In, in this, … Current initiative.
**Josh Suereth** 54:20 I'll take a look at it. It looks interesting so far.
…
Interesting.
I'll get you created Docker Compose, right.
Does it have, … it looks like there might be, a lot of overlap with some other config languages I've used. I have to drop in, like, 2 seconds to go.
**Laurent Quérel** 54:43 Yeah, sure.
**Josh Suereth** 54:43 But yeah, I'll take a look at this one. I had been looking for different config languages to see if they're adopted. If this is a CNCF one, and we think this is going to be adopted by CNCF and, like, Kubernetes and things, then that lends a lot more power to it than, like, designing our own thing, you know?
**Laurent Quérel** 55:03 Yep.
But for Jan, I was interested by Jan, by that, indeed.
**Josh Suereth** 55:08 Yeah, interesting. Okay.
It looks like it imports YAML and JSON itself in the language it has.
**Laurent Quérel** 55:18 But you can convert, you can parse or serialize or deserialize, I think, JSON
and, YAML, the same way.
…
They also… they are also able to import, fragments of YAML and JSON, but that's not necessarily the way that I was thinking about it. More like, …
You, you have a smart person.
to read any YAML, and you have a way to express the schema, and some kind of checking that we are… where we are using, rego, …
Policies to, to express them.
But, they could also be expressed directly into this system the same way.
**Josh Suereth** 56:09 Yeah, it's interesting. I'm just checking their union of and how they do expansion here to see if it has inheritance in any way.
like, structural inheritance. Oh, crap, I gotta go. Alright, man. Yeah. Okay.
**Laurent Quérel** 56:22 Right.
**Josh Suereth** 56:22 Yep, have a good day.
