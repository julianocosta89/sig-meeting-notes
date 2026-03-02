SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2025-09-10
Duration: 45 minutes
============================================================

## Zoom Recording Transcript

**Jim Porell** 00:28 Hey, Rudiger.
**Ruediger Schulze (IBM)** 00:31 Hi, Jim.
**Jim Porell** 00:36 Hey, did you see, David's, comments on the SOC channel about the PR?
**Ruediger Schulze (IBM)** 00:41 Oh, yes, this one, yeah, I need to respond to that, yeah, I've seen it. I was looking at a couple of other things, but yeah, you're right, that was another one.
**Jim Porell** 00:51 Yeah, okay.
**Ruediger Schulze (IBM)** 00:52 I will respond to that.
**Jim Porell** 00:57 Okay.
**Ruediger Schulze (IBM)** 00:58 And there are… there are a couple of things that we need to clean up… clean up, apparently. I would talk to some of this now, but there's probably more to… to come.
**Jim Porell** 01:09 Okay.
Thanks.
Let's wait another minute. Hey, Anand, thanks for joining.
**Anand Somasundaram** 01:17 Good afternoon.
**Ruediger Schulze (IBM)** 01:48 Let's wait 2 more minutes, and we get started.
Hey, Greg, thanks for joining.
**Greg Shriver** 02:21 Hello.
**Ruediger Schulze (IBM)** 02:23 Okay, put a couple of agenda items into… the meeting notes…
Let me share my screen.
What else is now?
Sharing the screen.
Okay.
So, Greg, the first thing that I would like to ask you is, as you, as you agreed to become a co-lead for the sick, or be the co-lead for the sick, there's an administrative task to be done.
you need to request an organization membership at the Open Telemetry project, and I send you on the CNCF Slack
the instructions.
**Greg Shriver** 03:19 Oh, I didn't see that. Okay.
**Ruediger Schulze (IBM)** 03:21 And you need to give,
sponsors there, and I think it's okay if you give Morgan and myself as a sponsor.
And once this is done, we can add you as a… as a maintainer, and then…
I think this becomes important if it's a.
**Jim Porell** 03:39 That's okay.
**Ruediger Schulze (IBM)** 03:40 PRs in future, I think,
Presuming I would write some of these PRs, you would have at least have to approve them then as another maintainer of the SIC.
**Greg Shriver** 03:52 Okay.
**Ruediger Schulze (IBM)** 03:53 Yeah. Okay.
**Greg Shriver** 03:54 Thank you for that.
**Ruediger Schulze (IBM)** 03:56 Good. Then, you know, our long-running PR for the transaction processing system.
Finally, I responded to all the comments that have been made there. I also cleaned it up after, you know, there have been several falls on back, on the…
On the upstream.
branch. And a couple of things to highlight, and I think we will see this moving forward, still, you know, happening a couple of times.
So, with the introduction of entity.
I think there's a need to introduce something like a TPS entity, because,
There needs to be this,
this information needs to be associated with a resource and a proper entity. And information, when I say this, this could be a spend, could be a metric, or it could be also lock information. Now, there is a glitch in our definition that we have been making so far.
You may, you know, remember we had discussions around the CUS software, and if you look at CUS software and the current attributes as they are.
being defined, and they, in fact, just describe this U.S. system, but not a… Not a, COS software.
Now, with the introduction of entities, my understanding is the following.
That if you have a resource, the resource can actually hold multiple entities.
So, the…
consideration that we can make is we can have a CUS software, but the question is then, what's the identifying attribute of the CUS software?
And we can have a TPS entity, which is, for instance, then describing the…
KICS region, or the IMS region.
And…
On the other hand, the TPS entity could also just run on a CUS system, but then we will have to change the CUS software, as we have it currently defined here.
for the PR that we have been open for so long, I didn't want it to go in further any of these discussions. What I would suggest is we…
aim to close this PR as it stands now, currently. And then on top of this, I think we need to do a couple of updates, also with current releases that are either coming, or…
Have been already released.
I think we will see also additional attributes being introduced.
I hope that makes sense to some extent.
**Jim Porell** 07:00 Yeah, it does. Sorry, I was on mute.
**Ruediger Schulze (IBM)** 07:04 And essentially what this implies as we move forward, we need to…
We probably will have a couple of discussions around what all these entities… What are these identifying attributes?
And, if you look also over the course of the last year, when we started to make those definitions, entity haven't been added yet. Potentially, some of the developments that have been done throughout the year, they are basing purely on this concept of resources.
moving forward, I think we will see that entities are stabilizing. I think we need to develop a point of view of what these entities are that we want to associate our telemetry with, and then, presumably, any developed
functionalities we'll have to update, but I think key is really that we need to…
Have a clear point of view of how the…
Entities are represented as part of these resources, and also what entities we see on the…
on the CUS side, for instance, or more generically also on the mainframe side,
I have to say, while I posted a couple of
Documents describing this concept of resources and entities.
And, I think you find them in the notes from last week here.
I still have also a number of questions of how they work, and also, just from a… also pure representation in a JSON files of what's…
you know, what's the representation on the wire, essentially, that an observability product would be receiving? So there's…
I think still, work in progress by the community. Also, if you look at this, relationships, while they are
A concept of entities, these definitions.
For relationships, they are not yet done.
So this was also something… That…
That would have to go into these, you know,
definitions over time, and then, of course.
Any product that is in this space, will have to, you know, once we have been stabilizing our definitions, we'll have to adopt to this.
Right.
**Anand Somasundaram** 09:28 Well, Rudiger, just from my understanding, I'm just looking at what is an entity. It says…
It is the one that produces the telemetry, right? Whether it's traces, metrics, profiles, or logs.
Given that, explanation, Should the entity be the…
KICS region and the IMS regions that produce the entity, telemetry.
**Ruediger Schulze (IBM)** 09:54 That, I think, is the way forward.
Hence, I was also… because there was a related question on the… on the PR,
which triggered then the, you know, my thinking that we, in fact, need to introduce a TPS entity, and the TPS entity would be, like you just said, it would be a KICS region or an IMS region, and that would be then associated with the related span information or other telemetry.
Also, just to say it, an entity always has a telemetry, or needs always to be associated with a telemetry. It can't exist without any telemetry being created.
**Anand Somasundaram** 10:36 Okay, thank you.
**Ruediger Schulze (IBM)** 10:40 Okay,
So, as it says here also in the notes, so there is obviously, you know, a couple of follow-ups, then once we get the PR, the current PR approved.
This is, you know, looking at this from a TPS perspective, I think, you know, as there have been certain developments.
happening for Kix, you may have seen the announcement for Kix 6.3, which also talks about open telemetry functionality.
There are a couple of additional attributes which have been used in the implementation. I think we want to look at this. Also, I think with the background of entities, we need to
More broadly looked and to align the definitions that we have been making and, update.
the semantic conventions on top of this, and relating to this is also what I just said about CES software as a current definition. Obviously, this is not sufficient, sufficient in this way that it's only representing an
System currently. But also, if you see this warning here, and this is also part of this entity implementation by the community.
The, requirement is that, on entities, you have definitions of attributes which have a certain role, and they can either be identifying, or they can be descriptive.
And this needs to be, as well, encoded into the semantic conventions. Now, if you look at the current state of definitions on entities, only UP, in fact, has a…
Distinction between identifying attributes and other attributes.
All the other entities still need to be updated by the community as well. ODeployment also has it. This is a, you know, lucky shot right now. But I think if you look at the…
The Azor…
or minority of those, you will find the warning here as well as the… So, I think this also represents the current state that semantic conventions are in. It's this transition from resources to… to entity.
Yeah, and we will… we will have to follow that.
as I was speaking about, you know, most recent releases.
We will have a couple of more PRs than also in the space of MQ, DP2, KICS, and IMS.
Specific to attributes that, you know, you can find on those…
Related spends, and again, we need to look at them from a…
SICK point of view, have these PRs being reviewed and approved by the SICK, and then moving forward, but the intention here is
To provide a complete picture from… of a spend functionality.
Okay.
Any questions on that?
Okay.
And just as an update, this… finally, this survey block, I sent it to Maeve, so she will put it to the OMP blog.
I will open the PR for the open telemetry.
block in the next days. Should be more or less content-wise the same, block,
content. I think you have seen the charts already in previous meetings, so, finally, I think we will have the publication then done within September.
And the last thing that I wanted to discuss, but maybe before I go there, any other topics that somebody wants to add? And Jim, you said it already, there was this question.
from.
**Jim Porell** 14:47 It would die, yeah.
**Ruediger Schulze (IBM)** 14:48 Yeah, from Dai on the… on the chat here. Maybe we can briefly look at this.
And I think this also goes into this direction that we just discussed. We need, probably, to make sure we have
consistent settings there. I can see that we have defined an attribute group, for service CUS Software.
And… And this model is currently not being referenced in the doc. Okay, though this is,
Obviously, also something we need to fix, then, on the… Documentation side, yeah.
I can… I will take a look at this and, reply to… to him.
**Jim Porell** 15:29 After the meeting.
Thanks.
**Ruediger Schulze (IBM)** 15:31 Okay.
Other questions?
Okay, if not, then let's focus on…
And this is work in progress, obviously.
Metric semantic conventions, the next big topic that we wanna… wanna look at.
And we had… oops.
we had earlier, I said, you know, we started to set up a spreadsheet, just to remind ourselves the spreadsheet
So, I think it was the… panel from…
This is not what I wanted.
Okay.
This panel includes metric names, but also then includes definitions for
For, for instance, attributes, so that we can have a consistent Way of checking…
What has been defined, and, you know, also listing of…
Of entities. This might be not complete yet.
But, what I wanted to point out is,
we started to look at this from a pure HMC perspective, so… and you may be aware there is the… there's a Promise,
HMCX portal, this is open source.
You can also find this somewhere on the internet.
And, we just started from the metrics that you find there to
You know, look at what definitions we would have to make, and where we have a fit between definitions that you have on semantic conventions today, and what would have to be changed, obviously.
And if you look at this, that's in some way… Not very trivial.
Because if we take, for instance, things like, you know, CPU count.
we have different types of processors on the machine, right? So, why we are aiming to…
You know, use what is there already by the community being defined, and also be, you know, as much as possible, not, you know, mainframe-specific.
We will have to introduce a couple of things which then represent the mainframe.
Likely as an entity, but also with specific attributes.
And, as we also earlier discussed, probably we need to have a representation of the CPC.
And then if you think about the attributes to be supplied there, in order to identify the CPU type, we probably need to
Okay, here's obviously… Field… Gonna change that.
Guys, Jesus, this should be… Okay, this is Tia.
Yeah, here you can see it, it's actually CPU type. Currently, mainframe CPU type as a name, but we could also put forward a system.cpu type, but the important point is then the population of this attribute would anyway have to be mainframe-specific, because the mainframe is the only platform which has
attributes like, IFLs, like chips, and, and also… Processor types, obviously.
And, as we would make these definitions, remember, you know, if we do these semantic conventions definitions, there's the attribute registry. We would have to make the definition for these respective attributes.
We would have… probably have to define an enum.
And then in this ANAM, list the respective CPU or CP types.
And, then provide a definition
that, for an entity CPC, mainframe CPC,
the CPU would be represented in this way.
And if we would be relying on existing metrics, I think we would have to update the metric specification to also allow the specification of this mainframe-specific attribute.
And,
Other way around, if you, you know, see that this particular metric is mainframe-specific, then obviously we need to do the definition for the metric, but also for the metrics, and then
Have a proper representation for this.
Long story short…
**Jim Porell** 20:17 Regret, just… I hear what you're saying, and I get it.
I haven't done any research on this, but what about GPUs versus CPUs in some of these servers?
you know, that is a different processor type. I don't know if they're doing distinctions there, but…
**Ruediger Schulze (IBM)** 20:35 That's a good one. I think GPU…
I would have to actually look at this, how they represent the GPU as a CPU.
**Jim Porell** 20:44 Oh, fair.
**Ruediger Schulze (IBM)** 20:44 Fair question… fair question.
**Jim Porell** 20:46 I think that would be… that would be something… it's not the same, but the fact that they distinguish, then we might be able to replicate some of that knowledge instead of being truly unique.
**Richard Nikula** 20:58 Because from my perspective, if you start enumerating the types of things as Different metrics?
You're gonna have a never-ending task to do that.
Right? I mean, it really almost seems like it should be…
You know, a number of processors, and then a corresponding processor type.
Right, because then you have one metric to define, and then you just have to qualify it with what type it is.
As part of the… of the…
thing, because otherwise, I mean, as soon as they add a new processor type, you've got to redo your whole model here to just.
**Ruediger Schulze (IBM)** 21:40 Hey.
**Jim Porell** 21:41 Well, I'm thinking differently than that. You know, a GPU… because, again, we got processor types that, you know, a Z17, 16, 15, that's one thing, but GPU…
IFL, those kind of things are specific, and customers are measuring them.
Because of the cost, and especially, you know, things like zips versus CPUs, if there's a zip overrun onto the CPU, it's costing them more in software. So, it does make a difference in accounting.
On the mainframe anyways, but…
And I don't know if the same thing, you know, this is where you gotta compare to what…
being leveraged on others, but go ahead.
**Richard Nikula** 22:29 I guess I was… maybe I didn't say it quite right. I'm not disagreeing that they want to know the type differences.
I'm just saying that I'm not sure that it's a different metric.
Rather than its count of processors.
And then its type, and it actually has a typing
you know, attribute that says I'm an EIFL.
**Jim Porell** 22:52 Yeah, so that might… yeah, that's probably the enum that… that he was just saying, yeah. That's right.
I would agree with that, yep.
**Ruediger Schulze (IBM)** 23:00 So, we put a couple of things in here. This is not complete yet for a number of reasons.
And let me just pick on a couple of these.
One example, for instance, is, you know, for hardware, would we, you know, for… or, let me be more specific.
There's a couple of environmental, metrics, obviously, on the HMC.
We could associate them with… with hardware as a predefined
metric, and also a predefined namespace. But as you can see here in red, humidity and also the viewpoint, they are not currently defined. We could introduce them under this namespace. They do not necessarily have to be mainframe-specific.
So this is something we would have to discuss.
or also, in this case, I didn't fill it out, if you… if you scroll down, you will see here
A number of, metrics that we have, obviously, relating to, data transmitted and so on, packets transmitted on…
on a particular port. I haven't seen anything in the semantic conventions yet that is representing ports of a particular NIC.
Can be that it's something we would have to introduce, but still, this is a generic concept, right? So we don't need to make this necessarily mainframe-specific.
But we would have to look at what is then a proper way of doing this. For NICs, obviously, there is predefined ways of how you could do that. It's not fully representing what we would be needing.
But,
We could start with, obviously, with system.network to populate that, and to have some attributes here in addition, to…
Broadcast type, we would have to…
To obviously introduce us something that would allow us then also to…
Differentiate between what is being sent via multicast and via broadcast.
So there's a couple of additions that we would have to anyway do.
Now, what I want to propose here, and you'll find the link to this Excel spreadsheet also in our
in our meetings logs. If you could go through this, and just generally maybe take a look at this, and then, in fact, what we are thinking is, as we also need to bring this forward as PRs, we would like to split this in smaller PRs, which are reasonable.
That maybe could be a discussion next week, or in two weeks.
on a SIG meeting, that we just say, you know, this is a good way of splitting, and we can start with the CPU-type discussion that we just had. We could also take network
port, as an example. It's probably, you know, already two PRs. And then, start to submit small PRs, and actually, over time.
To, you know, get this…
first of all, discuss with NOWSIC, so that we have a point of view, what's the right thing. Also, it will help us, in fact, to define these
These entities that we spoke about, and then…
As we approve them, they would go to the semantic convention SIC, and they can
Then, as well, take a point of view, and over time, we can actually assemble the matrix from an HMC perspective. And also, as we discussed previously, when we looked at the spreadsheet, based on that, then we can build up
CUS metrics, which we consider as important, that should be, you know, part of semantic conventions, or CVM, I mentioned earlier as well.
So we could, use this as the… Kind of like…
Principles of how we name things, what entities we have, and so on, to move forward with.
**Greg Shriver** 27:15 So, a question on the gauges.
What's… I mean, it looks… I mean, I haven't reviewed this, unfortunately, but it looks like there are a number of these that are defined as gauges.
And… What's the frequency that that…
telemetry would be admitted? Is that configurable? Is that… I mean…
**Ruediger Schulze (IBM)** 27:42 Dude, this… yeah, this is a good one.
It's actually unrelated to semantic conventions, because this is more about the way of how you collect. And just to say, probably we also need to revisit if everything here is a gauge or something, some of them might also actually be counters, which I have not correctly reflected here yet.
So counters in the sense of how open telemetry defines them, so up and down counters, for instance.
**Greg Shriver** 28:10 Sure.
**Ruediger Schulze (IBM)** 28:13 So, frequency, in this case would be, I think, something that is not being related to semantic conventions.
But you would, that's actually a good question, so…
Okay, I can't answer this from the top of my head, but my assumption is…
That, the way how the process works from…
measurements in OpenTelemetry towards aggregations, and then to actual metrics being emitted. Okay. There needs to be an encoding, what the…
the interval is?
And…
**Greg Shriver** 28:58 I got it.
**Ruediger Schulze (IBM)** 28:59 In fact, it's one of these things that I always wanted to look at, of how can you… how can you actually change the aggregation interval, because this is one of the value props that OTEL makes for metrics.
And how would that work for… if you have, you know, an existing instrumentation which comes with a certain interval, let's say CVM is max or minimal 6 seconds, or, you know, other, you know, other intervals.
Can you, you know, yeah.
Well, that…
**Greg Shriver** 29:34 That makes sense, because…
I mean, so, if I'm hearing you correctly, it sounds like these gauges, many of them are already
Interval… interval base.
**Richard Nikula** 29:45 The gauge is an interval of data. It represents the current…
**Greg Shriver** 29:49 Okay.
**Richard Nikula** 29:50 sampling, interval instance data. This is where it's at.
Right? And then, to the point, though, you're right, is that this is one of the things I don't exactly know how all of this stuff is going to all sort eventually, but you're going to have cases where some things are sampling, like, every minute, like, you know… Sure.
publishing, publishing, publishing, and then there are others that may only publish every 15 minutes. Now.
Right, so…
Okay, now the question is, well, how do you, you know, how do you interpret that data? And then, you know, if… is it that everybody has to be in sync? Well, no, that can never happen, I don't think, right? And then…
**Greg Shriver** 30:30 Right.
**Richard Nikula** 30:30 The alternative, yes, there is the way in… within the
Within the collector, you actually can aggregate, that is a feature of the… there, but aggregating aggregated data, as we all know, is typically flawed. So.
You know, I think the answer is you're going to have to ultimately deal with the fact that not everything is at the same rate. And we do that all the time, technically, right? If you think about your car, not every metric is published at the same interval.
And it really is dependent on what, you know, what the criticality of the underlying data is, and we handle that very well, but…
Your car has metrics, Richard?
**Greg Shriver** 31:13 Wow.
**Richard Nikula** 31:14 Zari?
**Greg Shriver** 31:15 Your car has metrics.
**Richard Nikula** 31:17 My car has a lot of metrics, it publishes them constantly.
**Ruediger Schulze (IBM)** 31:20 Yeah.
**Richard Nikula** 31:22 I guess one of the reasons I was asking was, I mean, we…
**Greg Shriver** 31:27 have… Some metrics that we were publishing, but they weren't interval-based metrics, they were observation-based metrics, so…
That you… if… in that situation, it's an event, almost.
**Richard Nikula** 31:43 It's published.
**Greg Shriver** 31:44 gauge.
**Richard Nikula** 31:45 Right, yeah.
But I mean, it still could be… I mean, that could be still an interpretation of a metric, right? I mean, it's…
**Greg Shriver** 31:52 True.
**Richard Nikula** 31:53 True. Whether you collect it and publish it, or you collect it instantaneously and publish it, it's still metric.
**Jim Porell** 32:00 Yeah, no, we just had that along the lines that Greg just talked about.
we'll collect metrics, let's… and I'll just use Kicks as an example. We'll have the same metric will come out for real time at the moment.
We'll also capture it for an interval, and we'll call it history, and it's now a summary. And then we'll also do it for event processing, like, if you have a situation, and if such and such occurs in this time, we've got to take action, or do something, but it's…
The same information collected multiple times a ways based on how it's used.
**Richard Nikula** 32:40 Right, so CPU is a simple example, right? I mean, you could collect CPU, and you could go look right now and say, exactly right now, how busy is the CPU?
**Jim Porell** 32:49 Right.
**Richard Nikula** 32:50 But what most people are interested in is, okay, give me at least a running average of the CPU, right? So that I can spot, you know, trending of what's going on, right? And so…
Yeah, so you have that, you know, and there are tools
Kafka comes to mind as one that drove… drove me crazy, right, is that all of their metrics are…
They have…
like, 20 different metrics, and they're all the same thing, it's just different intervals of what they collect, right? So they're…
So…
**Greg Shriver** 33:30 Well, I… one of the reasons I brought it up was…
I wonder if… and I know this is going to be a lot of work, but I wonder if it makes sense for us to
You know, as trying to… coming up… come up with the standard is, are some of these good candidates for histograms as opposed to gauges?
But that would be… I mean, that would… that may be a lot of work, depending on how many gauges we're talking about, and…
**Richard Nikula** 34:03 Actually, I think it's fine, actually. So, when you bring up a gauge in Grafana, you can display it as a gauge, but you can also display it historically.
So you can get a histogram from a gauge, because as long as you have something, like.
an underlying engine, Prometheus, for example, with Grafana, that can capture the gauge over time, that's where the history comes from.
**Greg Shriver** 34:30 But that comes at an increased cost for the customer, especially if they're running Grafana in the cloud.
**Richard Nikula** 34:36 Yeah. So…
**Greg Shriver** 34:37 So, I think from their perspective, they would probably prefer it be emitted as a histogram from the get-go.
it would be less cost for them. Now, I'm not sure if that's… if that's true across all of the observability backends.
But certainly, Grafana Cloud comes to mind as one that… where… where the decisions that we might be making in a standard, you know, or in these conventions may ultimately translate into
The cost that it's going to be for the customer to be able to, emit and use this telemetry.
You know, in their back-end observability systems.
**Ruediger Schulze (IBM)** 35:26 This is a good question, in fact.
Hmm… I have to look on the metrics. I wonder if something similar is already being considered, or…
If this would be actually… Question to…
I mean, you know, just maybe taking the example of CPU utilization, and maybe this is the first one where we want to discuss this in more detail.
**Jim Porell** 35:55 Where's the system metrics? That's something to ask Morgan, worth asking.
**Ruediger Schulze (IBM)** 35:59 Yeah, right.
System metrics…
I think he has all gauges. Don't see his tubramine inhaler on the system.
There's a couple of condos, which I still have miss… miss… represented in the… Spreadsheet, obviously, but…
Thing I haven't seen.
Hograms in this… in this context here, but…
I think it's a good question, Craig, to… so maybe let's make a note and… Indeed.
Let me doc here.
**Greg Shriver** 36:47 And then I guess the other consideration associated with that is if we… if we
propose something as a histogram, then, of course, that
That… that, adds responsibility for, you know, the folks that are collecting that stuff.
It might be more difficult for them to adopt the standard.
**Ruediger Schulze (IBM)** 37:08 Right, right. It's a… it's a fine balance, right?
what I was thinking, and probably need to look at this, could be also that we…
We allow for both in the definition. Obviously, the data that you would get from the HMC would be gauges or counters.
But, if… if a histogram is a better way of representing the same data.
Maybe there's ways to express this, and…
And allow for that as well, moving forward.
And having instrumentation that supports that, in fact.
Good.
I think it was…
**Greg Shriver** 38:04 Oh, and the system… the system CPU, I mean, that… that's one example, but like Richard brought up, I mean, I can sample the CPU right now, how busy is it? I might…
you know, I… I might…
I could also sample that a microsecond from now, and it would be a different number. That wouldn't make a whole lot of sense, though. So something like system CPU utilization is something that's going to be
Hold at certain intervals, so it's already gonna be… Aggregated.
As opposed to something that's an event, like…
you know, how long did this particular CICS transaction take?
You know, this transaction took… You know, 23 milliseconds
And, oh, by the way, I'm processing, you know, 100,000 CICS transactions a second. That's a lot of telemetry.
that would be a situation where we would really want to consider a histogram as opposed to just sending out a gauge for each one of the KICS transactions.
I use that as just an example.
**Ruediger Schulze (IBM)** 39:13 Yeah, yeah.
**Jim Porell** 39:13 Yeah, the interesting thing you're distinguishing there, though, is subsystem, and because we have this within Stana, is subsystem metrics versus application metrics. And that's, you know, so we distinguish the subsystem as infrastructure.
versus application.
**Greg Shriver** 39:32 Okay.
**Jim Porell** 39:32 And… But both valuable, both important. Because when you're looking at your application.
Is it constrained because of the application, or because of the environment it's running within?
**Greg Shriver** 39:45 Yeah. And so both are important.
**Jim Porell** 39:54 And it's really the difference… it's… to be honest, it's almost like the difference between traces and metrics, too, because traces are kind of giving you information about the specific application and metrics.
**Greg Shriver** 40:05 That's true.
**Jim Porell** 40:06 A little bit about both.
**Richard Nikula** 40:10 And oddly, I was having a discussion with somebody this morning that was saying that, oh, this really is an event, even though it was.
**Jim Porell** 40:18 Yeah.
**Richard Nikula** 40:19 publishing a metric with a current value, saying, oh, this is, you know, this is something we should treat as an event.
Nope. Yeah, maybe.
**Ruediger Schulze (IBM)** 40:34 Okay, good. Yeah, so, so maybe if you, if you can take a look, and, you know, like I say, this is debatable, but I think it gives us a structure to get started with some PRs.
**Greg Shriver** 40:46 Sure.
**Ruediger Schulze (IBM)** 40:47 And, anyway, we would like to have the discussion on the PRs.
So… Maybe next, or the week after, we can start to maybe…
split this up in a set of PRs that we want to bring forward.
And then we can look to make that happen.
**Jim Porell** 41:09 Regarding the next two weeks, Truth in Advertising, I'm out on vacation, so…
**Ruediger Schulze (IBM)** 41:15 Yeah, that's a good one.
**Jim Porell** 41:16 Yeah, I leave the 17th, come back the 28th, so…
**Ruediger Schulze (IBM)** 41:19 Okay, have a good one.
**Jim Porell** 41:21 Alright, buddy.
**Ruediger Schulze (IBM)** 41:22 By the way, Rachel, are you still going for tech exchange? Or anybody going for tech exchange?
**Richard Nikula** 41:28 I am… I am booked and confirmed at Tech Exchanges.
**Ruediger Schulze (IBM)** 41:31 Okay, good. Okay, good.
And.
**Richard Nikula** 41:35 And I think your session, the one session you have is on Monday.
**Ruediger Schulze (IBM)** 41:39 Yes.
**Richard Nikula** 41:40 That's correct. Right, yeah. I've got that in my calendar.
**Ruediger Schulze (IBM)** 41:44 Okay, yeah, then, let's, let's definitely meet there. Okay, very good.
Any other topics that you would want to cover?
**Anand Somasundaram** 41:55 More of a question, the namespace column had system as well as mainframe.
**Ruediger Schulze (IBM)** 42:02 Right.
**Anand Somasundaram** 42:02 How do we differentiate that?
**Ruediger Schulze (IBM)** 42:05 So, the current approach that we took here, and in fact… let me go back there.
So, a system is, you know, when we…
when this is either something predefined already, like system CPU utilization, and we can make reuse of the related metric.
This would be good.
the…
system would be also still applicable if he, you know, can introduce the concept, because simply it wasn't there yet, but it's generic, and, like, you know, with hardware, what I was talking about.
These environmental metrics. It's probably something we could introduce.
Done to lose.
Mainframe currently?
we started to use to represent the mainframe-specific metrics, or telemetry in general. It's maybe good to mention, in context of a terminology discussion internally.
We had some considerations around… I mean.
While the mainframe is special, and we want to represent the concepts of the mainframe.
We also want to make sure that, you know, the mainframe aligns with condiment concepts. We, you know, we don't want to necessarily
Make the mainframe look special, or different.
So, one of the considerations that, moving forward, I think we need to have is…
Also, you know, is there any concept that, you know, is generic
And actually, we should be creating semantic conventions for this generic concept.
Instead of making this a mainframe-specific representation. And as an example, as we also discussed here, virtualization, right? So virtualization is a generic concept. There's not much on the semantic conventions today, as we have seen earlier, so we… at some point, we will get there and
We'll have to look at how can we make a generic concept of virtualization work in the semantic conventions.
On the other hand, if there's really, you know, if the concept is very specific to the mainframe.
I think there is a need for a namespace mainframe. We also see this with CUS, for instance, as a namespace, as we introduced it. So,
Right.
Right, good. Then, let's meet next week, and,
Then let's look of how we can split this.
into, you know, workable items and start to have some PRs on this. I think this will be interesting to see how the community is also looking at this.
Moving forward, good. Okay.
Thank you.
**Anand Somasundaram** 45:11 Thank you.
**Jim Porell** 45:12 Alright, thanks a lot.
**Greg Shriver** 45:13 Thank you.
Thanks. Bye-bye.
**Richard Nikula** 45:16 Wow.
