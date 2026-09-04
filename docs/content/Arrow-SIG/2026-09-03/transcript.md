SIG: Arrow SIG
Date: 2026-09-03
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Brian Sapozhnikov** 01:58 Hello!
**Drew Relmas** 02:01 Hey, hello, everyone.
I'll give it a moment, I'm sure Laurent or Josh will be joining.
**Pierre Mariani** 02:17 Hello, good morning. This is Pierre. I'm joining for the first time today. I've just started contributing to the project, earlier in the week.
Nice to meet you, everybody.
**Drew Relmas** 02:27 Hey, yeah, nice to meet you too, Pierre. Great to have you.
**Jake Dern** 02:30 Hey, nice to meet you.
**Pierre Mariani** 02:32 Thank you, thank you.
**Drew Relmas** 02:34 If we want to, you know, if anyone… let me, update.
section on the SIG meeting notes, if you want to leave.
topics and or, your names as well. Give me one second… September 3rd.
**Laurent Quérel** 03:10 Are you willing?
**Drew Relmas** 03:12 Hi, Laurent.
**Jake Dern** 03:13 Hey, morning.
**Laurent Quérel** 03:15 I'm engaged.
**Brian Sapozhnikov** 03:18 Aye.
**Laurent Quérel** 03:18 Oops.
Okay… I don't know if Joshua will join today.
Okay, so let's, share… Can you use some estimating?
**Drew Relmas** 03:49 Yep, I can.
**Laurent Quérel** 03:51 Great.
So, as usual, I encourage everyone to add their name in this list.
And to add… some topics… They'd like to discuss other questions, new things.
So on my side, if we have time, I will have… There's something to discuss, let's see… Where I cheat.
**Drew Relmas** 05:10 Laurent, I think you're writing in last week's.
**Laurent Quérel** 05:13 Nice Okay, thank you.
**Drew Relmas** 05:19 Yeah.
**Laurent Quérel** 05:26 Okay, okay, I'll let others to add their own stuff.
So hi, everybody.
So let's start with the… additional, if anyone want to… to drive the meeting, no… no problem. I will be happy. I just woke up, and I'm not fully operational, so sorry for that, but I can definitely, Do the triage, but if anyone wants to do it, feel free to… Who rescue.
Okay, so… Let's start with that. Avoid rebuilding empty attribute batch during query assignment. That's something I did. Try to remember.
Oh, yes, I think it's, yeah, it's following… This Pierre… Which was… An issue when, in OPL, and I think it was also, like.
some issue into the attribute processor.
When we try to assign Value to an attribute that didn't exist, and more importantly, where… the corresponding OTAP signal didn't add any attributes at all.
Then we had a bug that has been fixed into this, into this PR.
And, and there is, in terms of performance and memory allocation, there is a way to do slightly better, and that's the… basically the… The proposal that is here, just explaining that we could improve slightly the approach.
I don't think there is anything controversial.
Maybe what was maybe problematic, I don't know if we have with us, because I saw that yesterday.
british…
**Drew Relmas** 07:48 I was just about… bring this up. I'm not sure if Patricia's in the call, but, I think this is a related Issue.
I was just looking at the PR.
**Laurent Quérel** 08:02 No, I… Absurd, attribute, panic.
I think it's a new issue, probably related, but not exactly the same, because in our case.
It was not really a panic, it was the, an invalid, Or not complete, set of attributes.
**Drew Relmas** 08:28 I see. Okay.
**Laurent Quérel** 08:29 Yeah, so,
**Drew Relmas** 08:32 Anyway, this looks like something…
**Laurent Quérel** 08:34 So, looks like there is something to… super interesting to… to see. I didn't read at all, but yeah, definitely something we… on which… on which we need to… To focus, Pierre Accepted, so it's already, Okay, great. So, for this one, I think there is no, Big problem to accept it.
Let's go to the next step.
Add batch processor, pass-through optimization.
Judge?
Thank you, you are with us, if I remember well.
**Jake Dern** 09:12 Yeah, this is, okay. I did see this morning that there's a bunch of stale items. I think we should just remove the stale, tag from this.
**Laurent Quérel** 09:20 Okay.
Great.
That was first.
Proposal remove CAZ data, metadata, encoding, I think that's in the same kind of,
**Jake Dern** 09:34 Yeah, I think all of these, proposals for protocol, enhancements or changes, we can probably take the stale off. At some point, we do need to discuss these, but, definitely don't have to do it right now.
**Laurent Quérel** 09:48 Yeah, so I think we… I don't know if I can do the same thing for all of them.
And then… labor… Oh, nice.
Didn't know.
Yes, refrigerated at the edge.
Okay, we also need to remove… Okay.
**Jake Dern** 10:26 Yeah, I'm not sure if we want to leave the needs discussion on them or not, they definitely, Yeah, they definitely will need discussion at some point, but if they're cluttering the dashboard…
**Laurent Quérel** 10:37 Yeah, so…
**Joshua MacDonald (Microsoft)** 10:37 We sort of likely want a category that's future discussion, stop bugging us until we know we're ready.
**Jake Dern** 10:44 Yep.
**Laurent Quérel** 10:46 So, do we have Shani with us?
Otherwise, I can't talk about this one.
Okay, I don't think we have Jenny. So… It's an interesting topic. So we, as you know, we have, support for Kafka, Kafka receiver, Kafka Exporter, which start to be… fairly complex… And, there are situations where… We… let's say we have a permanent neck.
So, as a reminder, we have two types of, the category of snack.
transient and permanent. They are emitted in different situations.
For the transient, we have some, downstream system, downstream backend, or the Kafka… even the Kafka broker that is not available, on the exporter side.
So we want to retry, so we… the exporter will emit a transient NAC… Then the retry processor will retry it with, an exponential Bank of… For, some, some number of attempts.
At some point, we will decide, okay, it's enough.
we emit a permanent NAC.
So, on the Kafka receiver, let's imagine you have a pipeline with, And the message originated from a Kafka receiver.
In that case, what we do is the corresponding message when we receive a permanent NAC.
So, one technique, classic technique is to use, a dead letter Q, So we, basically, we send the message to… In that case, a topic that will serve as a deadlier queue for further analysis.
And the technical problem that was raised is to… what do we put into this DMQ? Because when we receive a permanent NAC, we receive, in fact, usually the OTAP representation of the message. It's not necessarily the initial message that enters into the pipeline. Let's say you… into your Kafka topic, you have an OTLP, byte representation, or even a sysplug, or a packet, we discuss different, scenarios at some point regarding the usage of Kafka.
So we could imagine in the future that we support multiple formats.
But when we do this conversion, we basically lose the initial version of the message, which is not… A problem, because now, usually this conversion is… is lossless.
But it's not strictly equivalent to the original message.
So the question was, okay, can we do better? Can we, in fact.
re-inject into the DLQ the real message that was present into Kafkia.
So, I think, Shanley is discussing an option here.
Yesterday, I started to look at, the best practices and pattern used. I think I finally figured out A way to do it, with a minimum of work and without additional memory.
into the DFE engine, because the problem that I like to avoid is Avoid to put in memory All the incoming message, Just in case we have a parallel knock.
And basically, having… duplication of data, one in a binary format, one in a no-type format. And, so that will basically, more or less, double the memory used, in comparison with today, when a CAFK receiver is enabled, and the IQ is enabled.
So, I like to avoid that, and I think we have an option.
I still need to… I need to read what Chen Li put there, but at least now you know the problem.
And, if the approach that, if one of the approaches described here is not, satisfying, I will add a new one that I discovered yesterday.
One thing, maybe, that will be discussed, so, the proposal that Shenly puts in terms of configuration, when the DLQ is declared into the the Kafka receiver, configuration.
A level is missing there, but anyway. So, the idea is to specify… A topic for the DLQ.
the type of event that could, leads to… to the injection of a message into the DAQ. So it's super easy when we are not able to decode, so we are still in the Kafka receiver.
What the… if this, value is present into the capture.
Pin that, depending on the nature of the problem.
we decide or not to send the message into the DAQ. This, value decode happened in the Kafka receiver, it's a… very easy to achieve, because we still have the original information, but things like terminal NAC, I'll… Much harder to implement correctly.
And, but what I didn't like into this configuration, and I already started a discussion with Shani about that.
with that, in fact, the Kafka receiver is becoming also, in some way, a Kafka exporter, because we need to send the data into a DLQ Kafka topic.
I'm not a big fan of that.
So what I'm suggesting is to… to use the multi-output mechanism that we have, so we have a default output.
and we have a DLP output, and then we can connect whatever we want to the… not DLP, a DLQ output, and then on the DLQ output, we can connect a Kafka exporter, or… Whatever exporter we think is the right thing.
Drew, you have a question?
**Drew Relmas** 17:35 Yeah, it's slightly tangential to this topic, but it's just something that came to mind as I was looking at the config you have, which is the auth block.
I know we have another later issue coming in that's going to talk a little bit about other pole-based receivers, normally by specifically connecting to databases.
And I think Gokhan would also be interested in this topic. I'd like to… us to think about if we can have a… Auth extension.
typically used for, you know, pulling data. You know, similar, we have the bearer Auth extension for exporters.
I'd like to avoid having auth stuff inlined in a specific Kafka receiver. We should think about using extensions for this.
**Laurent Quérel** 18:23 Yeah, yeah, I agree. Feel free to, you or Gokhan to… To, add some comments, into this, 3940.
GitHub issue, yeah, I will also add my, my, comments.
like I said, regarding, in fact, regarding the… Yeah, all the… All the exporter definitions.
**Drew Relmas** 18:50 I'll assume you can do that. Thanks.
**Laurent Quérel** 18:55 What did you say, Ru? I did not hear you very well.
**Drew Relmas** 18:57 I said Gokhan did a thumbs-up reaction, I'll assume that means.
**Laurent Quérel** 19:01 Oh, okay, okay, okay, great.
**Gokhan Uslu** 19:03 Yeah, I'm trying to solve a lot of art-related stuff, so happy to look into them as a whole.
**Laurent Quérel** 19:15 Yeah, if you can, take the time, just to To let you remark on that, because… That's something on which we will work and, minimizing the number of, What is super important in terms of contract is the configuration model.
It's much harder to change the configuration later than it is to change the code, in fact.
Because the only contract we have with users is about the configuration, most of the time.
So I encourage everyone to… Really think hard about the configuration model, and making sure that this configuration model is As stable as possible, and when you see something that is not correct, not ideal for the configuration model, please feel free to comment it as soon as possible, because that will, I think that will save us a lot of time.
In the, in the future.
Okay…
**Joshua MacDonald (Microsoft)** 20:25 This looks good to me. I take it we might be considering using the, pluggable bytes representation to represent dead letters. I mean, if they fail to parse as OTLP, what are they?
in the pipeline.
I assume bytes.
**Laurent Quérel** 20:42 Yeah, oh, I see. When… if we follow the path of having a DMQ output.
we need, and let's say that we want to inject something into the DLQ, That could be a Kafka topic, or whatever.
we need a way to operate on this invalid message. That's what you are saying.
**Joshua MacDonald (Microsoft)** 21:06 That's right, I was proposing that we might just represent this as unknown bytes encoding.
**Laurent Quérel** 21:11 Yes, that's definitely interesting, and, correlated to the, a topic I'd like to discuss, at the end of this meeting, if we have time. I totally agree with that.
**Joshua MacDonald (Microsoft)** 21:24 Sounds good.
**Laurent Quérel** 21:25 Okay, so this one, I didn't read it.
**Drew Relmas** 21:30 Exactly.
So, Laurent, I had…
**Laurent Quérel** 21:36 Oh, I read it.
Good.
**Drew Relmas** 21:41 group about this. We have… partner team here inside Microsoft that is interested in starting contribution, focused on these polling receivers that I was talking about, talking to various, vendor databases. So… There's been some good commentary on it already from… I saw Albert and Jake and a few other maintainers left some, comments.
it seems like we're all kind of aligned that this is a good thing that we want to bring in. I can envision a few sets of work where, In order that we could pursue this.
Starting with defining kind of a shared interface for any pole-based receiver. In the Go Collector world, as Josh has commented, this is referred to as a scraper, although we don't have to keep that name.
So, the biggest concern, you know, Jake and Albert commented a little bit about the conversion of database rows to OTLP.
But the only other big thing in my mind is how we properly partition the thread-per-core architecture, when we're talking about querying a database. You know, Kafka topics have kind of partitioning built into the implementation itself, but It's not as obvious for databases.
**Laurent Quérel** 23:12 No, I think the most… One example of a receiver that is very similar in terms of, managing the type of problem that you are describing, I think it's the file.
The file was here.
Because it's also scrapping a bunch of, files.
And when we deploy this, and that's what, I guess, I guess, Lalit… which is working on, on this topic, probably,
**Drew Relmas** 23:46 Yes, I believe.
**Laurent Quérel** 23:47 I need some… I need some color on that, but yeah, when we will deploy the file log receiver on multiple pipeline instances, we have exactly the same problem. How we orchestrate the distribution of what to do Among the values, among the various pipeline instances. I think in this case, the problem is even harder.
Because it's… It's not only into a single process, but it could be multiprocess.
Let's say we have multiple instances of the same DFE and Gene.
They will scrub the same, database backend.
How they, they communicate together?
To avoid duplication of work.
so I think it's slightly harder than what we already, Define into the log receiver, because for the log receiver.
In fact, for the log receiver, that could also happen if the file system is a shared file system.
If it's a local PHY system, that's fine.
But if it's, yeah, I need to read the comments, but I started to read this, this thing, and I was thinking maybe we… If we have a right access to the database, we could consider the database as a way to Basically to do some bookkeeping and, and… And some orchestration could be part of the DFEM gene.
And talking with this, bookkeeping table.
To keep track of who is doing what, basically.
**Drew Relmas** 25:39 I mean, I see where you're going there. I feel like it could also be something, you know, I'm not… it depends on the use… on the auth model, right? You know, a lot of people here might be using auth credentials that only have read access on tables. I don't think we can depend on having write josh?
**Laurent Quérel** 26:00 Yeah, yeah.
**Joshua MacDonald (Microsoft)** 26:03 Yeah, I was, wondering if we could ask Lalit his thoughts, mainly because I've read through his fatalog receiver work.
document, and it… it does include a checkpoint file for recording the state… these states about which pieces of data have been gathered and which have not. And it does talk about expanding into that future where we have shared Shared file systems, or shared disks, or shared databases, and the need to partition work.
and I sent… and my feedback on that document was basically that we need to generalize this type of feature that we use to provision and partition Stable work for collecting data.
**Laurent Quérel** 26:45 Yeah, and I remember in the original 5-log receiver, One of the phase was to introduce A new capability into the extension mechanism.
Either at the pipeline group or on gene level.
Which will play the role of, Discovering the work to do, and distributing the work To the various, Pipeline instances, so that we could imagine that we specify properly this interface.
And then, we could have multiple implementation of, this kind of discovery bookkeeping capability.
That could be used, by different types of, Receiver of this kind.
And some of those extensions could only work on, let's say, the local PHY system, or could rely on… A database, which is not necessarily… The same database than the one that is used or scrapped by the… this, set of receivers.
Yeah, definitely, that's something we need to… to properly specify.
**Drew Relmas** 28:11 I guess, what do we think is the next steps here? Like, I'm… yes, okay, Laurent, you just did what I… I was gonna ask if we could move this to accepted. I think the start work here is really defining that kind of shared scraper, for lack of a better term, scraper, interface. Do the other maintainers agree?
**Laurent Quérel** 28:37 Yeah, I think we need to do that. I mean, I don't know if it… the right name is Craper, but because in that case, it's more about orchestrating and bookkeeping, in my opinion.
But that will be used by swapper-oriented receiver.
Because what will be externalized, I see, will be a sub-function of the scraper. The scraper by itself, I think, is still the receiver thing.
**Joshua MacDonald (Microsoft)** 29:07 Right, it's sort of a distributed state management task that's separate from the actual act of scraping.
**Laurent Quérel** 29:12 Yeah.
**Joshua MacDonald (Microsoft)** 29:13 The orchestration also works for me.
**Laurent Quérel** 29:16 Yeah, yeah.
Yeah, I totally agree, we need to define that. It will… it could be, I think it's a… it's a work that needs to be done by a different person already working on this kind of, It's copper-oriented receiver, so I'm definitely thinking about, so this person… Which,
**Drew Relmas** 29:43 Name is Jitender, he's…
**Laurent Quérel** 29:45 G-Tender, and, Lalit, infuser, office.
in The Mainer, I saw Jake also, and Albert, and myself, and Lou. Yeah, I think it's definitely an important work on which we need to have some kind of, workforce group, and, and end up with A well-defined interface, and rely also on the extension mechanism.
I don't remember where we are, Gokhan, in terms of, Support for extension at a different level.
Do we already support extension at the group level or engine level?
**Gokhan Uslu** 30:30 Not yet. I haven't gotten to it, but if there's a need for it, I can definitely start looking to it as well.
**Laurent Quérel** 30:41 I think for the first initial version, probably the pipeline level will be enough.
Oh, leave.
the chill.
What we need at the minimum is… An extension shared across Different instances of the same pipeline.
So it's not local to a pipeline instance, it's, it's, it's shared across…
**Gokhan Uslu** 31:11 language.
**Laurent Quérel** 31:13 Not exact. It could be the pipeline group.
Earl, it's not attached to a pipeline instance, but to multiple instances of the same pipeline configuration.
**Gokhan Uslu** 31:29 Okay, I will need to first understand what it means, but, yeah, definitely.
**Laurent Quérel** 31:33 Yeah.
Okay, great. Very interesting topic,
**Drew Relmas** 31:40 End up, Andre?
**Laurent Quérel** 31:41 Andres, you want to say something?
**Andres** 31:43 Yeah, so… I agree, it's a pretty complex problem, and we should not… I mean, we should do it, like, in a central place, from a standard way.
But I was thinking that… We are… talking about two slightly different use cases, and that depends on how you name it, right? So you have… one use case where you are more, like, with a bookkeeping, where you distribute tasks between the different… I mean, different tasks for the… For the different pipeline instances or processes.
That is kind of, like, one use case, but the other use case is… is taking turns over the same task.
So you want the bookkeeping when you want to distribute tasks, like different files, for example.
But you want to, take turns, for the database use case, because it's the same task, it's just that they cannot be done in parallel.
They need to be done, like, like, taking turns.
So… I would not… think on something external, like a database, because this is also expected to work under an agent situation, so in an agent, most likely will not have a database.
So, I agree that it should be something external to the pipeline, centralized to the different processes.
But it should be part of… the solution should be part of the… Of the engine itself, as a separate process, probably, but… but it should be part of it.
**Laurent Quérel** 33:23 Yeah, I'm not sure that I agree with that, because… I think that the idea to rely on the extension system is the ability to To, to, to provide solutions that will work for… a local adjunct without database access, and for simple use case, we could rely on Like you said, something running locally, the file system or whatever.
But there are… there are situations where… we deployed the DFE engine into a data center, and we have access to the database, and we have plenty of, of instance, instances of this system. And then we need a way to coordinate efficiently this cluster of DFE engine.
And then we could have a different extension exposing the same interface, and it's up to this extension to define where they would put this state. Maybe that could be a database, maybe that could be… ATCD, or whatever.
So… Yeah,
**Andres** 34:38 raised.
**Laurent Quérel** 34:38 I think, yeah, I think a different type of implementation will, We'll adapt a different implementation.
**Andres** 34:46 Correct, we should… you know, provide different types of sources or storage for that solution, I agree, yeah.
**Laurent Quérel** 34:55 Yep.
Anyway, so don't hesitate also, Andres, to, to add, your, your thought about, what you just described, I think, but we agree on the fact that maybe database in some situation could be the right solution also for the state.
Joshua?
**Joshua MacDonald (Microsoft)** 35:18 Yes, so, this is an issue, epic, with a bunch of children that I've filed. I don't think we should really speak much about it here in this meeting. There was an RFC, and this just breaks down the work of the RFC into, you know.
**Laurent Quérel** 35:32 more stuff.
**Joshua MacDonald (Microsoft)** 35:32 And I had the PR open this week. Some of you have seen it. I put it back into draft. I realized it had some issues, and I'm… and I'm just, trying to wrap my head around this problem a little bit more in depth before I reopen that. So this is just covering all that work.
Yeah. And I don't think we need to go through the 9 children that I made.
**Laurent Quérel** 35:54 Okay.
tools.
**Drew Relmas** 36:03 Aha, yes. Okay, so we… I don't recall if we spoke about this at a previous SIG meeting, but we have, you know, I've been doing some work with duration. We have… flow duration, we have processor compute duration, and we are rapidly getting closer to the shared metric sets, receiver, and exporter durations. However, I also noted that we actually have node output duration and node input duration.
And for me, these are a little, misleading, in that their duration associated with the node, scope But it actually refers to from the point of measurement to the end of ACNEC unwinding, so going all the way through the rest of the pipeline.
So, this was meant to capture, like.
how can we make these names? One, are these measurements useful from a single point in time from this node looking forward?
Is that a useful thing to keep track of?
And two, if it is, how can we improve the metric name to make it more clear?
**Laurent Quérel** 37:19 Yeah.
**Drew Relmas** 37:20 I…
**Laurent Quérel** 37:21 For me, the clarity, I think I proposed that at some point.
Something like completion duration, an attribute saying if it's the completion is successful or not.
So the outcome, maybe?
Will make sense, because we, we basically… if I remember well, the, the, the… the timer that you will use, I mean, the time that you will measure will be between When this node sends something, In one of the outputs?
And when he will receive… if he… if this nod is interested, by the way, register to the ACNAC system.
**Drew Relmas** 38:09 Correct. And it's also asymmetric, like, the receiver has output duration, and processor and exporter have input durations, meaning it starts measuring when… the processor measures from when it sees the data to start, receiver measures from when it sent the data out, and I just don't like how it's… asymmetric in that way.
**Laurent Quérel** 38:29 Yeah, and the other aspect also that… I mean… A lot of node types.
processors, especially Don't care about acne.
So they will, anyway, they will not receive the AC or the NAC.
So the duration… If we… if we make that systematic.
That will basically, go back to… A situation that we try to avoid.
To be aware of ACNAC everywhere into the… into the pipeline.
So, I don't think we want that, in my opinion.
So the duration could not be a general metric, that's my point.
**Drew Relmas** 39:19 Josh, you wanna say something?
**Joshua MacDonald (Microsoft)** 39:21 Yeah, so I think the name duration may stem from some history in hotel, and that… that… I don't mind if we have… if we break apart with that. The… the thing that… when I… as I recall putting this in, was that the… the Go Collector, which we are basing our, sort of.
Our mental model off of when we build some of this.
as duration measurements, and because that system is synchronous, when you issue a request into a receiver, you, like, you wait until the response. Like, there's no real… and if you're going to return right away, then that is your duration. So, like, the amount of time spent, like, blocking for one request is a meaningful number.
If we had to rename it, I would… I would probably choose the word latency here. It is a measure of your average throughput when you consider how much memory you have and look at average… average duration, that gives you a very meaningful number.
And you can use it to calculate how much memory you need if you know your average latency, for example.
And so… you know, I think it's true that, like, this only means something when you have AC and NAC enabled, so maybe we should have a metric that is only enabled when you have ACNAC tracking, and then… Call it something that signals the fact that you are measuring the whole duration of the request, which tells you something about your back pressure number and your current throughput number.
**Laurent Quérel** 40:49 Yeah, and that makes me thinking that in the metric name, I think we shouldn't, make very visible the fact that it's not… it's ACNAC-related.
**Drew Relmas** 41:05 Yes, I agree.
**Laurent Quérel** 41:07 Because otherwise, duration could mean, for example, for processor, okay, duration, it's, how long that takes to process locally.
Exactly.
**Drew Relmas** 41:16 That's my… that's my major concern, is I don't want this to be interpreted as time spent in the node, because it's not, it's the rest of the pipeline.
**Laurent Quérel** 41:23 Yeah, so we should see something like that into the metric name, or… related. And, it's only when the node is in fact registering to ACNAC mechanism.
So it's an optional metric.
Okay. Because I…
**Drew Relmas** 41:44 I don't.
**Laurent Quérel** 41:44 Yeah.
**Drew Relmas** 41:45 I think I have enough direction, I don't think we need to spend more time on it.
**Laurent Quérel** 41:49 Oh, okay.
**Drew Relmas** 41:50 But thanks for the conversation.
**Andres** 41:56 Sorry, before that, the… the…
**Laurent Quérel** 41:59 learn.
**Andres** 41:59 The… the metric is calling the node Level, you know, so… so it should… Definitely.
Take the duration of their nose.
If we want the duration of the whole pipeline, maybe we need to call it pipeline instead of node, no?
**Laurent Quérel** 42:18 So it's, if I, if I understood well.
**Andres** 42:22 I think Do you have value on having the duration of the node, especially for the processing use case. I want to know how long it's taking to process.
**Laurent Quérel** 42:30 But it's a two… it's…
**Drew Relmas** 42:32 Christmas summer.
**Laurent Quérel** 42:32 We agree with that. I think it's already existing, right, Joel?
**Drew Relmas** 42:37 Processor.compute.duration.
**Laurent Quérel** 42:40 Yeah, so that's… what you said, Andres, already exists.
For this one, it's more… For the point of view of a nud.
Not at the pipeline level. For the point of view of a nerd, that… is interested by ACNAC message.
Do we want a metric that represents locally for this node?
The duration from when this nod receive a message, if it's a processor, To when he will receive the AC or the neck. That's, So it's not at the pipeline level. What you say at the pipeline level will be true for a receiver.
Beginning of the pipeline, the entire, back and forth.
will be measured, will be equivalent to a pipeline National Sea.
But per receiver.
Which could be different depending on how many receivers you have in your pipeline.
**Andres** 43:44 I think we want to respond to two different questions, right? One is.
How long is it taking these nodes, no matter if it's a receiver, a processor, or an exporter?
**Laurent Quérel** 43:53 already existing?
**Andres** 43:55 And how long does it take, average, to deliver for the pipeline end-to-end, and including RTMACs, and so on?
**Laurent Quérel** 44:05 I think we, we, we agree on the sensing, We are just focusing on one aspect, but the other aspect, they are already underd.
The net compute duration already exists.
**Andres** 44:19 Okay, and it's still paid mode, not by pipeline.
**Laurent Quérel** 44:22 And per pipeline, right now, it's not exactly per pipeline, it's per receiver.
Because per pipeline doesn't mean really… doesn't represent well.
You could derive the per-pipeline by looking at the… Latency observed, at pitch receiver.
When I say each receiver, Different type of receiver.
Because the pipeline is not only a single receiver thing, could be multiple. So the… The latency could be different depending on the path that you are following.
Into this, more or less complex pipeline.
Again, don't hesitate to, to add your thoughts about that.
Let's move on on the next,
**Drew Relmas** 45:22 As a time check, I see we have 15 minutes left.
**Laurent Quérel** 45:27 Yeah, okay, so we… to be respectful with the… Duro, you want to focus on that, maybe?
**Drew Relmas** 45:35 I… honestly, I… we don't need to take time for this here. Suffice to say, I've been discussing with a few people about the receiver and exporter shared metric sets that I was proposing, and Udkarsh had some feedback about duration, and… I have a PR out that, aligns some things. Basically… what do we actually want to count as receiver-receive duration? So we can do this offline, we don't have to spend time right now.
**Laurent Quérel** 46:10 Okay.
Is there anything super important there? Exposed KFC, a consumer lag? I think it was a request from one of, Microsoft, contributor… I don't know, if,
**Joshua MacDonald (Microsoft)** 46:31 Brian's on the call. We spoke about this last week a little bit. Remember, it was like, this is sort of the question of a gauge histogram.
**Brian Sapozhnikov** 46:41 Yeah, I think probably we can talk about this. Josh, you had some ideas on it, so I don't think I need to spend time on it this time.
**Joshua MacDonald (Microsoft)** 46:52 Yeah, we can, take this offline. I agree.
**Laurent Quérel** 46:58 Okay.
Yeah, that is… I don't think it's controversial, it's a bug that, I discovered in during one of the… review, so I just, tracked the issue.
Oh, my question.
**Joshua MacDonald (Microsoft)** 47:20 The next… next one, this is… the next one on the list was a bug that I noticed that's not very controversial, just that the OTLP HTTP exporter doesn't use transport headers.
Okay. As far as I can tell.
And I'll take care of it.
**Laurent Quérel** 47:34 Right.
Okay, and oh, that was the one.
**Joshua MacDonald (Microsoft)** 47:42 And we keep.
**Laurent Quérel** 47:42 pushing her.
**Joshua MacDonald (Microsoft)** 47:43 Off the one on the bottom, because…
**Laurent Quérel** 47:44 Yeah, so I think we are… we are… yeah, perfect. So I think we are good with that.
Oh, that's the… stale with stuff.
**Joshua MacDonald (Microsoft)** 48:02 I propose that we move on to the agenda and ask someone, maybe Jake, maybe me, to go through that stale list.
**Laurent Quérel** 48:11 Okay, so for this, so I can talk about that if you're interested.
So we, we, we had a predisposition Probably 1 month ago, or 2 months ago.
The idea was… so right now, in the engine, we have this, otap pitata message.
Which is basically, more or less anonym, where we have two main variants.
OTIP byte representation, or type representation.
And, depending on… What a processor or an exporter need it will request… either the native representation, so the, let's say, if it's a OTLP byte representation, you will get that. So something like a typewriter.
a batch processor.
will not have to basically decode the content. If it's OTLP byte, it can read the message without decoding the OTLP byte. If it's a batch, we can combine multiple OTLP byte representation together.
By just, putting them one after the other, and that's still… it's still a valid, a valid OTLP byte batch.
So this capability has been used to implement what we named the password model.
which basically removes the decoding, encoding phase of OTLP byte. So that's why we are able to have very efficient pipeline implementation for OTLP when the pipeline is relatively basic.
tight routing, batching, we can stay in pass formula.
So the idea here is to generalize this mechanism to any beta format that, That could traverse the pipeline system.
And… and expose a pass-through mode.
So, an example of that could be a syslog. So, we have a syslog receiver.
And right now, the way that the system receiver is working.
we have a TCP socket or EDP socket, then we have to parse line by line The… the C slogan trees, and they will… and the output of the, the syslog receiver will be an OTAP representation of those, let's say, a collection of syslog entries.
If we want to support, a pass-through mode for syslog, right now, we can't.
But if we have an abstraction, like, that I named the pluggable P-data codec, system.
We could, basically expose an interface Where, we… we say, okay, we have a method to decode, a method to encode. Each of those methods are… I mean, it's, in fact, we have an encoder trait, a decoder trait, a batcher thread.
And I think I also introduced, something to count the number of items into it.
And, and when you create a codec, you can implement Some of those traits.
And and then that will enable the system to support natively, a new data format with the type of advanced optimization we did. And when… and transparently, when a processor, like the transform processor, like the filter, that repeat processor, and so on, when they really need to inspect into the data.
The engine will automatically convert whatever, connect base Pilata message.
We have, at this time.
And because the processor is requiring an ATAP representation, if it's not already in a tap representation, the conversion will be done transparently.
And that's how we can implement a pass-through mode support, constantly, for any kind of, sorry, message representation via the codec infrastructure. So that's… so this PR is the first of a series of five PR.
And basically focus so that there is no… In this Pierre, there is no impact on the existing code. It's, like, just creating the foundation for the codec.
It's not integrated.
But, I already have the 5 PR, and basically the results are, here.
And I, so it's… it's close to the… In terms of performance having no impact.
To… To the ex… in comparison with the existing system.
when I say no impact, it's less than 2%, usually. Except, for the syslog, where we have multiple CPU, it's… I need to figure out why we have that. I have some ideas, but I didn't yet, fully, Analyze the situation.
But I'm relatively confident that we… we could have this level of flexibility.
Without having, A significant impact on the overall performance of the system.
questions. If you are interested by understanding the detail, The design principles are there.
And, the interface…
**Joshua MacDonald (Microsoft)** 54:41 For the record, I looked at your first PR in this sequence, and it looked pretty easy to review. Like, it just wasn't a major change, and this seems like a very natural direction for us to go.
**Laurent Quérel** 54:53 Yeah.
And, so you… the trait I was mentioning, the decoder, encoder.
There is this notion of registry.
It's very similar to the… To the factory mechanism that we already have into the… into our system for many things, for extension, for receiver, declaration, and so on. Same approach.
Oh, yes, I forgot to mention something, and that's something that I'm exploring into this work.
That we cooled at some point, report to the… To the factory mechanism that we have.
So… F5, and I think it's also true for Microsoft.
This, open source project is the foundation, and we built on top of that some internal, additional layer on top of it. So basically, we… we don't deploy… we don't necessarily deploy the main The main, main binary generated by the project, the open source project, but we have our own main that basically imports all the crates and do some additional stuff.
what I'd like to achieve, and it was not… possible before.
But for the collect, I think it's essential.
It's the ability to… to let… People that import the crates of this project.
To modify a codec that already exists.
So we can imagine that we have an open source codec implementation for XYZ format.
But for… because we have some, let's say, specific capabilities, hardware capabilities or whatever, We'd like to provide A specific implementation that works only in some system.
But trust only, The existing configuration file for our pipeline will still work.
Because we… we, we support the same interface, the codec is doing the same thing, but in a different way.
So I just extended the, The factory mechanism that we use every day for receiver, processor, exporter extension.
in a such way that, in this binary that, for example, Microsoft RF5 could redefine, they will be able to override a codec implementation by their own implementation, so that's, this Pierre defined that.
Okay.
Any other topic that, we have, 3 minutes, it's not a lot, not a lot.
**Joshua MacDonald (Microsoft)** 58:10 Thanks for this. I like this issue a lot. I look forward to us passing through data and then having WebAssembly blocks decode it for us. So, like, file log receiver should not have to… we should not have to hard code a million file formats, we should just plug in little bits of WebAssembly, it'll be great. This is one.
**Laurent Quérel** 58:28 Wonderful.
**Joshua MacDonald (Microsoft)** 58:28 Also for MQTT data, same thing, this is gonna be wonderful. Appreciate it.
**Laurent Quérel** 58:34 So if when… if someone, wants to review this, this Pierre, which is the first of a series of five, that will be the REP. That will be merged sooner, soon.
Great, I think we are at the end, Any last minute, message.
**Joshua MacDonald (Microsoft)** 59:02 We did it. Thanks, Al.
**Laurent Quérel** 59:04 Yeah, thank you.
Have a good week. Bye.
**Andres** 59:07 Take care of.
**Brian Sapozhnikov** 59:13 Thanks.
