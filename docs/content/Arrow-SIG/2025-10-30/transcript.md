SIG: Arrow SIG
Date: 2025-10-30
Duration: 43 minutes
============================================================

## Zoom Recording Transcript

**Jake Dern** 01:10 Hey, Matthias, good morning.
Or maybe not morning for you. You in Germany?
I think I, I think I met some of your colleagues at Rust Conference in Seattle.
Yeah, no worries.
**Joshua MacDonald** 05:37 Hi, good morning.
Thank you for joining.
I, am going to share my screen. Hello. So
We are here on October 30th. I'll just copy some stuff.
It could be an interesting…
challenging meeting without Albert or Laurent.
Today, but we'll do our best.
If they're not showing up today, I can handle it.
I'll just delete some people. Alright, hi, everybody.
Jake's here, Ukarsh is here, I'm here.
I'll just, alright, cool. Danny's here. Hi, everybody,
Well, another week has come. I'm gonna pull up the issue triage. Thank you, Matias. Been a while since…
We met on a Tuesday, a Thursday, so… Here we are.
I will say we are kind of, like, moving forward in our progress towards the December milestone.
And… It's been a little bit… oh, my browser is frozen.
Have I frozen? No.
Oh, there we go.
I will give you a brief summary that, you know, the codebase is coming together,
We are working on ACNAC handling concurrency. Concurrency is a big deal in this… in this situation, so I'll say that some of that work is in progress.
And, we have…
number of improvements on the benchmarks. This is going to be awkward if I have to keep talking and don't have a moment to think about the agenda. Okay,
no new issues that I can see since…
Except one for 3 days ago.
And, as you may know, Albert is working on a data fusion integration. We are very pleased to be taking this step forward.
So, I imagine there's some curiosity. I'm just gonna,
show you what I'm talking about.
So, Albert, has taken a beginning stab at using Data Fusion on the OTAP records payload.
And, this is awesome, this is, like, literally what I thought we were here for, to get to the point where we could use Arrow and DataFusion. So, we are,
looking at a language that has a sort of feel of KQL, but, they're interested in, pipeline definition. So,
Have begun adding conditional logic.
So that you could have a expression with some pipes and some conditionals in them.
And these are some examples. This is gonna feel like KQL to you, if you're familiar with KQL.
And this is the type of exploration that's happening. Okay, so I'm super excited about that. Would anyone like to discuss this? Without the authors of it, I can do my best.
But this was really the… the reason to be here, and so I'm super glad to see it happen, start happening.
I assume that this is…
We have… we have added now also a low-level, filter. So, one of the purposes of doing data… one of the things we're doing with DataFusion is, like, beginning to make it work, and then as soon as we get it working, we're benchmarking. So Albert has been benchmarking
Against some new filtering code. So we have a…
processor that just filters logs directly using Arrow kernels, rather than trying to use DataFusion.
And… And… He's trying to include criteria for what he wants.
to include… Unfortunately, this doesn't seem to give the behavior…
Okay, so the API is confusing…
This appears to be… log match properties appears to take, you know, 5 arguments, vectors of attributes for the resources.
log attributes.
Severity. I noticed when I reviewed this PR there was no attention to scopes. That's okay.
And… okay, this has been filed, I have acknowledged it.
So, that's the only new issue, and we have done our issue triage.
Danny, you came off mute, maybe you'd like to ask a question.
Okay, then…
I can have my… I can have my discussion, and there's a chance that some of you will be able to answer me. I'm looking at you, Jake, especially, but anybody who is more… getting to be familiar with OCHAP,
So there was, I think it's okay to say this, there was a little bit of a staffing problem. Somebody who joined the project at F5 left.
Unexpectedly, we won't name names. And it left a piece of code that he had written unmaintained already. So, I have become…
the batch processor. Batch processor is actually quite complicated when you look at Arrow, and the questions I was going to ask, I'm not sure anyone here will have answers to. But I'll ask them anyway.
So, this… the reason I,
what I… what I observed… so we have… we have a component that does the batch processor, and then we have a library in the Otel Arrow Rust crate that has some low-level support for batching. At a distance, I admired that code. At a close level, I could see it actually had a few bugs.
So there was one test that exposed the bug, and it was being ignored, and I… and I now have assigned this to myself.
So the question that I was going to have was about
optional ID columns in the log signal. According to my research, some of the signals will let you omit an ID column if it's,
if it's the identity column, meaning if the column is going to have row number equal to sequence number or ID value, then we can omit that column.
And that seems like a sensible optimization, but it tripped up the batch processor logic, because it was looking for an ID column. Why the ID column is taking a bunch of batches and then it's concatenating them, and it has to move the row index… the row numbers and the ID values, it has to shift them.
So, And the… the code…
Was being inconsistent about this detail.
I wanted to ask Laurent his thoughts, and he's not here, so…
I am struggling to figure out what else I'm going to say about it.
But unless anyone speaks up with an opinion or thought or question, I'm going to write this. Josh will open a PR with more detailed questions outlined.
This is me talking in the third person about myself.
**Danny Chin** 13:26 Can you hear my…
Oh, sorry. I think I had a microphone issue. So, I have a question about data fusion. Is it an existing library, like, something like that, or…
Okay.
**Joshua MacDonald** 13:43 Moving up. Okay, so let me talk about data fusion. That's an exciting reason for… that's something exciting for me to talk about.
They just go…
Let me just pull up, let's say, a web search and see if I can find it. So, this is,
DataFusion is a library that It's been around for, I don't know, 7 or 8 years? I don't know.
**Danny Chin** 14:06 Oh, man.
**Joshua MacDonald** 14:07 But it's been around. It's been around, basically, since Rust and Arrow began growing and becoming popular. So…
I think of this, and it… it…
it sells itself pretty well. It's an engine… a SQL engine, out of the box, gives you a SQL processor. So, what takes a while to figure out what that means. And they talk about having, a number of extension points, and
like, where do they call… what do they call it? So the… the built-in support,
extension enabling. So, what… what they have is a,
Is there an introduction to this concept?
What they have is,
It's all in on Arrow, so you're able to create table providers, which are interfaces that act like tables in the Data Fusion world, and you can provide an abstraction that's like, I'm a table, and you could go fetch it from somewhere else.
You can also have an abstraction that's like, I'm, you know, going to pretend to be some data, and you can scan me, you can push down predicates, you can, project columns and so on, so that the data fusion is able to
To interact with this table provider.
So then, once you've implemented Table Provider, or used some of their off-the-shelf table providers, they can just… you can, like, push in the files that you want, you can say, these are my Parquet files, or this is my other data source, and then you can write SQL queries. So,
And they're talking about all the users of it. New language query engines can use it. Have you ever heard of PRQL query? Like…
Archived. I wonder what happened to it.
This is a very similar approach to, pipeline queries.
If you've ever seen this language, it's implemented on top of data fusion as well.
So, there's a long list of… this is not a very good introduction.
the point here, this is an example of a Rust program, obviously. So, to use Data Fusion is super easy. You say, I want a new session. Grade it.
you put your tables and providers into it, and then you ask a SQL question. So, like, we're trying to get this for the OTel Arrow data, basically. And, you know, it can take CSV files, it can take
you know, Parquet files, it can take every type of file out there. And then there's various ways to bridge it with other SQL providers, and anyone who can produce arrow frames can be, you know, can participate in this. So it's become,
I don't know, let me see if I can say this fairly. It's widely used in industry.
**Danny Chin** 16:45 Hmm.
**Joshua MacDonald** 16:45 In the sense that,
this is the sense I'm getting. I could… I'm making this up from, sort of, our secondhand, kind of, conversations, but,
The people who are contributing to Data Fusion all work at big data companies. These companies are competing with each other.
This sounds familiar. OpenTelemetry has a lot of observability vendors competing with each other. The point is that we… they come together and they build this common library that everyone's using.
**Danny Chin** 17:14 It's become…
**Joshua MacDonald** 17:14 very powerful.
And it's been, you know, producing competitive results with all the kind of database benchmarks pretty recently. So, for me, the famous contributor comes from, like, the InfluxDB company has done a ton of work on this project.
And, and it is, you know, it's quite… it's quite a lot to take in. It's got… it's a pretty big library. So.
That's the… that's the goal here, is that you should be able to build a collector of data flow pipeline
you know, putting OpenTelemetry data in, and then suddenly get into this world where you're able to transform it using SQL queries. Or…
**Danny Chin** 17:54 Hmm.
**Joshua MacDonald** 17:54 other language queries, and that's getting back to what Albert's looking at here, is that these… is that I think there's an opinion in the industry, it's held pretty wildly, especially in observability, that these SQL queries are really hard to write, especially when you have windows, time windows, grouping by time buckets.
joining multiple expressions grouped by time buckets that are aligned, like, it's really difficult to write these SQL queries, and so there's this new grouping… there's this sort of new world of languages, like KQL, like a bunch of others that I'm not gonna name, but, like, in the observability space, there's lots.
None of them have kind of taken hold as the dominant, though. So, this is like KQL in the sense that many other languages are like KQL that have been attempted to work with observability data.
**Danny Chin** 18:43 So this language is defined in data fusion, or we try to… we are trying to define.
**Joshua MacDonald** 18:50 So this language is being derived from a parser that my team worked on, and I'll show you where that is. So in the Rust hierarchy.
We've got,
we've got… the two main crates are these two. So OTAP Dataflow is the engine for data pipelines and so on, and then OTel Arrow Rust is, like, the protocol layer that we do for transforming to and from Arrow, right?
**Danny Chin** 19:15 Alongside that, we have this experimental directory, and.
Okay.
**Joshua MacDonald** 19:20 added. These two directories were meant to get us to where we are now. They have a KQL parser that's, like, very close to real KQL, and it's got some sort of experimental uses where we're trying to
bridge with Microsoft customers who are quite used to using KQL, but it was just a parser, and we called it an abstraction because the goal is also to support other
other languages that OpenTelemetry users want or experience a desire for. So, like, OTTL is a language that OpenTelemetry has. It is not very powerful, but it is existing, and it is, you know, it's, like, YAML configurable, so it's pretty easy to put a
transform processor together with some snippets of OTTL. We wanted to be able to implement OTTL again on Data Fusion, and so we were… we were sort of first trying to parse KQL to get an abstract query, you know, abstract syntax tree.
But we also wanted to process OTTL and get an abstract syntax tree, and then figure out what's the lower level abstraction.
Right now, the closest I can answer that question is data fusion is the lower-level abstraction.
**Danny Chin** 20:26 If you can…
**Joshua MacDonald** 20:26 produce a logical plan. Data Fusion will take it from there.
**Danny Chin** 20:30 Hmm, I see, I see.
**Joshua MacDonald** 20:31 That's the big idea.
**Danny Chin** 20:33 Okay, so are we targeting to use it for all of them, of, like, trace, logs, and metrics?
**Joshua MacDonald** 20:41 That's the… that's the, I guess, the ambition. I will say this, that we're using KQL kind of as a model, because it's pretty well established in the log space.
But…
**Danny Chin** 20:53 But, like, in Trace, there is a, like, TraceQ.
**Joshua MacDonald** 20:56 I didn't know.
**Danny Chin** 20:58 Perfect.
**Joshua MacDonald** 20:58 No one can… you can't get by without doing PromQL. So we know that there are many languages, and we're absolutely not looking for there to be one language that rules them all.
Having a data fusion layer means that you can have more than one language.
**Danny Chin** 21:11 Cooling.
**Joshua MacDonald** 21:12 We like that idea.
**Danny Chin** 21:14 I am…
**Joshua MacDonald** 21:15 My background, I came from a company that did metrics. I've been involved in OpenTelemetry metrics for a long time. I'm very excited about seeing us build.
**Danny Chin** 21:25 Hmm.
**Joshua MacDonald** 21:26 say, PromQL. Or trying. This has been tried by many people. You get to the corners, and it's hard to do. We know that.
**Danny Chin** 21:34 Hmm.
That's cool. So…
**Joshua MacDonald** 21:37 for me, I mentioned that we're starting kind of with logs here, and it's because we also know that when it comes to metrics query.
it's not as easy as logs, and I'm…
Let me see if I can…
trying to figure out what resource I want to share. So I could… I could name a bunch of languages that do stuff like this for us to.
**Danny Chin** 22:05 So, like, if you're curious about this topic, I want to…
Hmm.
**Joshua MacDonald** 22:12 So, I'll name some.
**Danny Chin** 22:16 Yeah, it's…
Thanks, Mutrison.
**Joshua MacDonald** 22:19 So, PromQL, you can't… you can't not do PromQL in this… in this world that we're in, and it's… so it's one kind of whole space.
You've heard of TraceQL.
**Danny Chin** 22:29 No.
**Joshua MacDonald** 22:30 I'm not familiar with it, especially.
**Danny Chin** 22:32 We've heard of KQL.
**Joshua MacDonald** 22:34 We've heard of OTTL.
Those are all…
Well, ChaseQL, KQL, OTTL, you know, there's sort of a different, there's sort of a different…
needs for dealing with event data, like logs, like spans, where it's one row of data for one event.
Whereas when you get into the metric signal, you've got one row of data represents a range of time, and there are sort of logical inferences that you can and can't do with ranges of time, and do they overlap, and so on. Are they in line, and so on. So, when it comes to metrics query.
So Google…
as a monarch language. They've published that 10 years ago. It's pipeline-like oriented with metrics. Focus on alignment.
And…
reduce. So, I would say… so, personally, because I come from Google, I'm quite biased in this direction. I just… I knew that system very well, but there are others. I went to another company called LightStep, so there's my other bias. We had one called UQL. It's very similar to Google Monarch, because the same people went and did it.
There's, Axiom has one called APO,
There are a lot of these. The Oxide Computer Company?
AuxQL. I actually like OxQL because it's open source and it's Rust, but that doesn't mean it's great.
good for us. It just means it's cool that they're doing it in Rust, and they've, implemented something like it. So all of these four that I just named are very similar, and they're… they take it much further than the others do, including PromQL.
if you're going to be joining time series, there are lots of alignment and reduction strategies that come into play, and it's much more explicit in this modern group of languages. My personal interest is in seeing us get to where OpenTelemetry has a metrics engine.
Because optometry has been in a place where
it can… it can sort of describe its data model. It can say, here's what you do when you want to aggregate the data, but it doesn't have any proof of existence that you… like, it doesn't have an engine to show you how to do it. It has no reference implementation, so… so OpenTeometry has specified a lot of things to do with its aggregation
of its data, but hasn't given away a tool to do that, and that's really what I'm getting at here. So, I'm excited about DataFusion because we can start to implement this group of metrics query languages, which means we can start to have a metrics query engine.
One of the things that PromQL can do that we can't do in OpenTelemetry on our own is a recording rule. Like, you're just gonna…
look at a window of data, like 10 minutes of metrics, and, like, you're gonna decide that all the data has arrived, and now I can join it. I can write queries, and I can output new data from my incoming data. We need a way to compute metric time series and open telemetry, and this is… for me, this is an exciting path to do it with data fusion.
But it's all very experimental, and like, you know, proof of concepts are not even here.
**Danny Chin** 25:47 So think of the, like, feature in the language listed here in metrics can be implemented in our current architecture, or…
**Joshua MacDonald** 26:01 That… so,
I wish I had, I know there's a document that Laurent's working on, but I don't think he's ready to share it. The…
You may be familiar with how,
you know, there's different capabilities or levels of support in a query engine, generally speaking. If you look at the SQL research, you know, on database, it's like 50 years
of history, right? There are, query engines that you can do for sort of stateless, like, I'm giving you my entire batch of data, you can do whatever you want, and then give me the entire batch of data back, modified.
I would call that a stateless approach. Most of our telemetry operations, when you're collecting data in a pipeline, it's coming in one side and it's going out the other. You usually have a stateless approach. It's so much harder to get past that. Of course, that's where all the real interesting stuff starts to happen.
**Danny Chin** 26:53 So.
**Joshua MacDonald** 26:55 So then, Laurent kind of was sketching out this
for us, like, there's two more levels past stateless. The first is where you've got some fixed window of time, and that's the one where I think there's a lot of value for open telemetry. So you say, I'm going to have an acceptance window, I will accept data for 3 hours, or 10 hours, or 24 hours, or 1 hour. Whatever you decide to do, that's your threshold.
You will not accept data before that. So then…
**Danny Chin** 27:21 Hmm.
**Joshua MacDonald** 27:22 So then you can begin to reason about, well, I have all my data from before a certain period of time. So it might be that you want to do some metric joining, and you're going to wait a few minutes for all the data to arrive, but then you have the sort of confidence to say, I have an entire frame of data. Now.
Then you can start to do real interesting aggregations.
Of course.
The problem space just got way harder.
**Danny Chin** 27:49 You have to also decide whether you have the entire set of data, or whether you have just a sort of partition of it.
**Joshua MacDonald** 27:55 And that can depend on external factors. Is there a load balancer? Are you part of a pool?
So, we know this space is really hard.
Of course, we also know that Prometheus solved it by making simplifications and assumptions that are feasible, you know, so Prometheus does something by assuming that it's, like, that it's got the entire view of some subset of the data, so…
It, you know, like, it's got the partition baked into it, and there's no… it doesn't have to worry about talking to all the other Prometheuses by design.
We have some of those… we can… we can construct systems which are the same. Like, I'm gonna say, you must send all of your data from one SDK to this thing so I can do aggregations.
**Danny Chin** 28:35 Hmm.
**Joshua MacDonald** 28:36 But that's not always realistic, so we recognize that before we can get to this second phase of, like, what I'm calling the stream processing, where we have some state, and we can join with other series.
there's often a need to do a grand global shuffle at that phase, too. So you want to take all your data in, do some consistent hashing, maybe, do some load balancing logic, and then redirect the data so that each partition has a whole view of something. That's another hard problem that comes up before you go
of this journey.
And then after that, it's where the vendors are, where, you know, you're gonna have an entire data store with the entire history of every metric forever. Now you can go do long-range queries and stuff like that, but that's not where OpenTelemetry really wants to be.
However, if we could do a streaming metric calculation by some assumptions, like, I'm gonna assume that I have all my data, or I'm gonna assume that I have a full shard, or after some period of time, so it comes at a stream processing problem. I think there's a lot of excitement there.
And data fusion should be applicable, but it's, like, not the whole solution. And, you know, some people will pull out Kafka to do that shuffle that we talked about. Lots of open questions here.
**Danny Chin** 29:50 Sounds a lot of work to do.
**Joshua MacDonald** 29:53 Yeah, thank you.
If you're… if you're interested in following this… this topic, I do recommend the Google paper. It's very… it was very influential, and it'll give you a much stronger feeling about what all these languages are trying to do, with their, kind of, syntax.
So, it will go more narcotter.
**Danny Chin** 30:15 Okay.
**Joshua MacDonald** 30:16 Yes.
Well, that was interesting.
**Danny Chin** 30:19 wicked.
**Joshua MacDonald** 30:19 I think it would be nice to hear more from the F5 side that's been working on this, but they're not here today, and that's okay.
**Utkarsh Umesan Pillai** 30:29 Hey, Josh.
**Joshua MacDonald** 30:30 I have much more agenda, to be honest. If there's a question, it would be a great time for questions and answers, if anyone wants to…
**Utkarsh Umesan Pillai** 30:36 Yeah, Josh, I had a question about, like, related to querying site itself.
**Joshua MacDonald** 30:41 Sure.
**Utkarsh Umesan Pillai** 30:42 So, at least with the current implementation, we have KQL and OTTL, and I think we also have our own intermediate language, right? So we convert the KQL or OTTL queries to our intermediate language, which then gets converted to Data Fusion query? Is that how things are working?
**Joshua MacDonald** 31:03 My impression is that… is that Albert has been working with the abstract syntax tree that Drew and Blanche produced, which is that abstract syntax tree.
I don't know if we have gone as far as using an intermediate representation. To me, this is actually where the research and the kind of discovery is happening.
There… You know, people have called like…
Datafusion has been referred to as the LLVM of Query Engine.
That's a common phrase these days, the LLVM of whatever it is, right? So it's sort of like a toolkit for building, and it does represent an intermediate representation, much like LLVM does for compilers. The intermediate representation in DataFusion is a logical query plan.
And in some sense, that is the natural intermediate representation.
**Utkarsh Umesan Pillai** 31:59 But…
**Joshua MacDonald** 32:01 We have a data model on top of it, and so it's, like, has to be a logical query plan
Framed around our data model.
And so, the way Albert… the way that Laurent and Albert were talking about this the last I spoke to them, it was like.
we understand, let's say, for example, that the OTAP logs format has four… four tables in it. So you… so you have a batch of OTAP records. It's really four…
record batches.
One is logs, one is log attributes, one is scopes, one is resources.
And… So…
so it's hard to work with four tables at once, when there's a foreign relationship between them. And I think the abstraction that we're looking at, or experimenting with here.
Is the idea that we produce, let's say, a table provider.
That has flattened those tables somehow.
flattened those tables into where you can now think of it as one logical OTAP record… record, and it will have
Features that are, mashed together in one logical row. So then, the intermediate representation is
OTAP records in the model.
And there's a table provider, potentially, that could, like, present that abstraction, and then you could start writing your queries. That's sort of the idea that I'm trying to convey.
It's all very.
**Utkarsh Umesan Pillai** 33:30 It's all very, vaporous right now. I haven't seen more.
**Joshua MacDonald** 33:34 But that's where I think we're heading.
**Utkarsh Umesan Pillai** 33:36 Okay, and another… I think I don't fully… haven't checked the Data Fusion docs, but, like.
you mentioned something about, when… in the Alberts PR about filtering, that it uses the Arrow compute kernels directly, so, like, is…
When data fusion queries are running on OTAP data, are they using compute kernels always, or is it…
Or, like, how does that…
**Joshua MacDonald** 34:03 Your question is about the data fusion implementation, I take it?
**Utkarsh Umesan Pillai** 34:07 I heard you mention that the filtering work was happening through compute kernels, so I was not sure if, like, data fusion queries itself get executed using compute kernels, or, like, somehow the…
**Joshua MacDonald** 34:21 Yeah, I mean, the DataFusion implementation will be optimized to make as much use of Arrow as possible. What I was referring to, though, was… oh, there's no…
So, I'm referring to how I can click in and show. So, just as a tour of the OTAP Dataflow repository, right? We've got… we've got a number of crates, and
the sort of high-level components for the data flow pipeline are in the OTAP crate.
And what, what, albert's question was about the filter processor, which is… Here.
And it… this… this is a…
dedicated component that has low-level Aero facilities and doesn't use data fusion. Also uses Arrow kernels. So…
So… And as an example of that, what?
This is testing. I don't think I should try and find the implementation of this
In front of all of you, but… but the point is that Albert was comparing this implementation with a DataFusion-based implementation. I know he was doing performance comparison, like, so the nice result that I heard from Laurent two days ago was that,
the… first attempt to implement a logs filter on DataFusion had poor performance. It was because of…
the logical query plan being compiled to a physical query plan on every request, and that was because in OPTAP, one of our challenges is the sort of, like, variation of the schema from one request to another, because of the potential for absent columns and so on. So,
Albert had worked out a solution to that that was, going to let us cache
query plans by schema, I guess.
I wish we could hear more. I think we'll have to wait till the next meeting for that.
**Utkarsh Umesan Pillai** 36:21 Okay.
**Joshua MacDonald** 36:25 Alright, audience, are there any questions? Otherwise, save me from not having anything to say.
**Matthias Loibl** 36:30 Well, thank you for… I can unmute myself now. My partner was in a meeting on the other side of the room, but yeah, thank you for walking us through all of this. I'm… I haven't been here in quite some time, but it's great seeing where things have gotten, and…
**Joshua MacDonald** 36:47 Thanks for joining us, I know, I know that you're out.
**Matthias Loibl** 36:49 fusion.
**Joshua MacDonald** 36:49 You know, I know, I know you guys are still working on your end, and that Arrow will be useful to you one day, I hope.
**Matthias Loibl** 36:56 Yeah, and I dropped some links in the chat while you were talking as well.
**Joshua MacDonald** 37:01 Oh, okay.
**Matthias Loibl** 37:02 Seems like there was some discussion happening there as well, like, I was just at PromCon, the Prometheus conference last week, and the ReptTimeDB folks have also talked about their PromQL parser that is, essentially parsing PromQL, and then
again, yeah, creating logical plans for data fusion. So, like, there's something in the works already on that side. I don't know how…
Compliant, that is. But, yeah, I think we're eventually gonna talk to them as well, which is quite exciting. And then, the other thing I want to point out is that there is a working group within
Prometheus that are looking to storing Parquet files, directly. They are not, like.
I think they could, like, push it a bit further, like, they still put the XOR and delta-encoded chunks of Chrome ETS into Parquet files. I think they can push it a bit further and, like, go all Parquet all the way in, and then there would be, like, a nice interoperability story, on, like, reading Parquet files from…
from, Prometheus directly in the future as well.
Yeah, it's like a Parquet, I think… SIG Parquet, or working group, Parquet Working Group within Prometheus.
**Joshua MacDonald** 38:19 Cool.
**Matthias Loibl** 38:20 So, yeah, like…
I also try to talk these people into, like, doing more Arrow, because they are, like, only talking about Parquet at the moment, but I think the real benefit comes from, like, speaking Arrow on top of Parquet. But they are not there yet, and yeah.
Maybe, maybe in the future, but I think a lot of things are kind of, like, pointing towards a future where Prometheus also goes more into this direction. Yeah, I think we're all having…
**Joshua MacDonald** 38:47 Heading this.
**Matthias Loibl** 38:47 Exactly, yeah.
**Joshua MacDonald** 38:49 to see a PromQL parser, thanks for adding that little detail. Of course, we know the grepTime group in this group here, like, they created the first OTel Arrow Rust.
**Matthias Loibl** 38:58 Yeah.
**Joshua MacDonald** 38:59 as well. So I'm excited to hear that they've been doing that, and thanks for sharing.
**Matthias Loibl** 39:03 Yeah, anything else I wanted to add while I couldn't speak? I think, I think you pretty much covered, like, data fusion. I, I just, like, dropped the, Andrew Lamp,
there was, like, a one-hour introduction talk to Data Fusion at CMU, like, a year ago or something. I don't know from when it is. Okay, thank you. That's a great talk for anyone who wants to put those in the meeting later.
**Joshua MacDonald** 39:27 Meeting notes.
Yeah, Andrew Lamb is, like, probably the most famous name,
In that group. He's, at InfluxDB, Influx Data. Cool. Well, this is great. I,
I…
I mostly… I want to make sure people don't… don't see, like, an anti-anything here. Like, I embrace Prometheus, I really want to get PromQL.
hard language to get, though, and so, we know that. And I've worked a lot with these others, and they also are very natural for certain types of queries, so I think that we should have both of these languages. People are never going to.
**Matthias Loibl** 40:12 So, if we can get data fusion into these ecosystems, like, we have a common ground, and I think that's kind of where, like, Policing is heading as well, and, like, I can see us, like, dabbling with some PromQL in the future, too, and, like, becoming a strong…
Strong partner in that side of the ecosystem in the future, so… yeah.
**Joshua MacDonald** 40:32 Alright, well, I appreciate sharing, Matthias, and, Danny, thanks for the questions. Ukaj, thanks for the questions. Everybody here, thank you. I think we've reached the end.
**Matthias Loibl** 40:42 Yeah, thank you for walking us through. Thank you so much. I at least tried to, like, show myself on video, because I know how painful that is. Appreciate it.
**Joshua MacDonald** 40:50 Yeah. I'm by myself.
**Danny Chin** 40:52 Alright.
**Joshua MacDonald** 40:53 We've reached the end, thank you all, I'll see you next time.
**Danny Chin** 40:57 Okay.
**Andres Borja** 40:58 Thank you, Al.
**Utkarsh Umesan Pillai** 40:58 I do. Thank you.
