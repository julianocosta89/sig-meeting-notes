SIG: Arrow SIG
Date: 2025-06-26
Duration: 64 minutes
Zoom Recording URL: https://zoom.us/rec/share/bMmpUzAzXlMs5Kx7uoUIlh73O6-FiRFiwc97B_PimhpJa9hT7QnAd4CIt0mvlXxP._-a87ITu1BecUJjv
============================================================

## Zoom Recording Transcript

jmacdonald 00:01:31 Morning.
We've I think you can hear me cool.
It's nice when it works the 1st time.
Good morning, everybody. Here we are.
And is another another Thursday.
So it's been 2 weeks.
Gonna go ahead and fix up this header.
If someone has an agenda in a moment we'll be ready to paste it in.
Today's the 26.th
How do you make it today?
There it is.
I'm copying the attendees, so I might have copied them incorrectly. I think we're all here. See everybody cool.
Well, I copied this from the last time.
so agenda items. If you've been involved in the repository in the last 2 weeks. I want you to have an agenda item. And I know what Albert's been up to.
I myself have been focusing on the Go side for a bit, so I don't have a ton to update you all with
And so I see agenda items. I'm excited about what Albert has to say, because I read his code in the last week, and I'd love to have that agenda item, start. I'm excited by what you've got, Albert. Let's talk about it.
albertlockett 00:03:09 yeah, sure. So we talked a little bit about this last week, but just as a refresher we are trying to build
and
a set of traits that we're calling views that will give us a way to traverse the the structure of Otlp data agnostic of how that data is actually represented.
physically. So that, like the data, the hotel P data could be the
just the rust structs and enums that are generated from prost, or it could be serialized Protobuff messages for that data. So this Pr that we're looking at landed this week. This had the definition of those view traits. It had an implementation of those traits for the
the structs the Otlp structs. And it also had a
a function that would visit those those view implementations and encode a batch of
otap data for logs. So this week. I'm iterating on that to
write the view implementation that will read from otlp bytes. So protobuff serialized otlp messages, and then theoretically, we should be able to use the same function that encodes that otap data to encode otap batches directly from
directly from the serialized protof byte. So I have that almost
done hoping to land that pr
or to get that pr, I guess, in review hopefully, tomorrow.
the the performance numbers are looking.
Okay. So, for example, I have some benchmarks written. Just with some. Okay, and question marks. I have some benchmarks written that are that generate some so some logs data. And then, I just have a visitor that goes and visits all the fields. And just calls like state hand black box on it. Right?
And so for my generated data, let's say I'm visiting a batch of logs in my in my benchmark. I 1st
decode those bytes into a struct and then visit using the struct implementation of the visitor of the views. And then I have another benchmark that will just
visit the bytes, and so visiting the bytes seems to be about 20% faster than visit than decoding and then visiting the structs. It's it's okay. I was hoping that it would be a little bit faster than that. But it's still a decent improvement. But I'm going to keep iterating on it to see if there's any
performance to be games one of the
things that I think, is maybe making things a little bit slower is that we talked about this last week. But as you're visiting the the byte buffer you'll be iterating through it, and you'll be seeing you know this field is this offset? This field is at that offset, and so we need to keep track of those offsets. So if you're visiting the the data in an order.
that is not like the natural order of the portal buff encoding. Then you might need to jump around the the byte buffer a bit, so it's good to keep track of those offsets, but because we have a
different I guess. Objects, for let's say, iterating resource logs versus visiting
or sorry. Let's say iterating scope logs versus visiting the resource laws. Object? Which
of those 2 things keeps like has ownership of the of the offsets a little bit tricky. So I was using a ref cell for that. And I think there's performance overhead of using that. So I might see if I can refactor to get rid of that ref cell implementation hopefully, that will that will speed things up. So gonna keep iterating on that
today. But the you know the moral of the stories, I guess at this point is that we we are able to at least encode otap batches directly from Otlp bytes, and it and it is a little bit faster than encoding from the structs, which is what we expected. So, yeah, that's where I'm at with my work.
jmacdonald 00:08:48 That's really great, Albert. I I don't want our bar, our performance bar to be super high, like we are mainly trying to avoid a double cost, and if you're 20% less, that's way less than double
so I I think this is the right architecture. And I hope to hear, you know, that you are able to squeeze out a bit more performance. But I would be happy with what you just said myself.
I think that's great.
albertlockett 00:09:14 Yeah. So so I guess, like worst case scenario. Then if I if I can't get that optimized further, I'll just get the Pr up, and that way we'll have the code up before the end of the week. Because, because I'll I'll be on Pto the next 2 weeks, and I was hoping to get this code in before I leave, so.
jmacdonald 00:09:33 Yes, Laurent has mentioned that you have a new coworker starting soon. Who's gonna sort of gradually take up this work while you're away on Pto. I look forward to that.
albertlockett 00:09:42 Maybe you'll introduce my new colleague because he's here today. Welcome, Michael.
Michael Salib (F5) 00:09:47 Hey, folks, it's
jmacdonald 00:09:48 Yes, but we'll be here.
I was wondering. Hi, Michael!
I understand that you're a former Microsoft employee. Welcome! Thank you.
Good to see you so welcome to the group, and thank you for joining us. I will. I know Laurent and Albert will be telling you lots and lots more. But I'll be glad to help you in any way I can. I'm on slack
So right so for the rest of us. That means michael is here new from and and you're not on the the agenda notes. We can put you in there. You can put yourself there. But thank you for joining us. So we have another person on the F 5 side.
well, I'm looking at who's here and who could speak? And I if I may, Drew, I'd like to put you on the spot.
Drew Relmas 00:10:38 Oops!
jmacdonald 00:10:39 You're here. Okay, drew hello!
for these meetings now every week I kind of keep wishing to come back to you. I just briefly. You may have noticed.
and I'll come back to the notes in a second. Come
looked at all the closed Prs, and we can see that you and Blanche are doing a lot, and I
what I wanted to do.
there's not a problem with that. By the way, this is good. What I was what I was thinking of is, you'll notice that?
Well, actually, let me open. Look! Look at open Prs and laurent had started.
I guess it's merged. But Laurent has started a document on instrumentation like what he wants to do to instrument the otap pipeline the data flow engine that he's working on.
and
he and I have have been discussing the idea of an Otap SDK for a long time, which is like a big idea for open telemetry. The idea that we're gonna start to develop sdks that are like natively optimized for this representation we think that maybe that's good for large scale servers. Maybe it's just sort of an idea.
But in the shorter term the question is, are we gonna end up using the hotel SDK, as it is. And you know, obviously, we are a telemetry system. So we have all kinds of ideas about literally how to process our own telemetry. And we're building pipelines to process telemetry. So the question.
basically, I'm I'm asking this mainly to drew to put you on the spot. Laurent was trying trying to ask me. And now I'm asking you what we'd like to see. What I'd like to see is
ways that we can take the work you're doing. And I want to ignore metrics. Because when when we talk about metrics, it's like, Hey, Prom, Ql is the thing that everyone needs to do, especially in the open source. But when it comes to logs and spans there's not a dominant query language out there.
And we're building something as an experiment.
and we know what Otto is. We've seen some of the other alternatives, but one of the sort of selling points of the Kql language is. It's very concise syntax, and it's like fairly compact representation of a query that you can do some useful things with.
in my like in an old career of mine like long ago, I once wrote a tool that would take structure logs from a fairly condensed producer
of this is long before open geometry that would write out its structured logs in a binary format.
And then there was a tool that was like a fairly simple command line tool that would receive the binary format from whoever was logging it, and could let you write simple queries. And I'm seeing the potential to do that with Blanche's engine today. And it's a selling point for this like kind of minimal query engine like, I don't need a data fusion dependency.
I actually am interested in the lowest level of I'm debugging my own system. Data fusion may not be working yet. I have a simple SDK with simple instrumentation and simple output.
And now I would like to write some simple queries that can take this sort of vast amount of data that's coming out of my pipeline and tell me simple things, and I think what Laurent is asking is to say he has some ideas about how to instrument the data flow.
I have some ideas. We all have some ideas about how like, well.
I want to write a query that can find that one data flow operation that was really long. And I want to extract a trace.
And I want that to happen, using a tool that we've that we have and we know how to use. So starting to think about examples that could take the Kql
query engine.
And let us find examples that will be useful to us as we develop
potentially by framing those questions in ways that an open source user of our software could benefit from. Like, we're going to put a a tracing event statement at the beginning of our data flow operation, we're going to put a tracing event at the end of our data flow operation. We're going to pass context around, so that you, when you get a bunch of log events, they'll have a correlation identifier. Now, I want to write a Kql query that can like. Take that correlation identifier, form a trace filter by latency, and spit it out something like that.
And those are things that Kql should be good at.
And that's what I want to put you on the spot about. Is there a path forward here where we can,
you know, begin to have a tool that lets us
play around with Kql expressions for our own diagnostic purposes. As we develop our logs.
Drew Relmas 00:15:21 Yeah. So thanks for bringing this up. I also wish Blanche was here in order to talk more about it, but I can do my best to speak a little bit. So for those of you who don't have context, what we're working on right? There's an issue for it that largely explains, like our goal. I don't think it's actually linkedin to read me. But our.
jmacdonald 00:15:42 Prolific Coder. If you can see this.
Drew Relmas 00:15:45 Yeah. So a lot of these have been, you know, very small bite size chunks, which I enjoy as a reviewer. So one of the one of the things we're trying to do is
you know, the collector today has its concept of Ottl and the transform processor, along with a few others that use Ottl statements to manipulate data during the workflow. One of the things we're trying to do in Hotel Arrow is. See what kind of transform we can bring to this rust pipeline that we're building
we are interested in. Not just Ottl, but something a little bit more generic. So we chose coming from Microsoft. Kusto. Query language for those of you who don't know which is, you know, a very prominent, I guess.
Simple
query language, Josh, you probably praise it a little bit better than us. One of the initial challenges that I think we're still working through is the fact that Kql is very much designed. It's designed a little bit differently than Ottl in that it's
by default meant for like a flat table structure like you're already looking at data sitting in a data store. We're having to get a little bit inventive and following some Ottl practices on how to work with a more complex like open telemetry data object which has resource scope
and like a log record. So we're having to get a little inventive on the acoustic syntax there. But that's not strictly important for the question you're talking about now.
actually, on my list of things to do is a little. I had played around with it a little bit in my previous experimental folder. It was query. Abstractions. I do think one of the immediate goals for us should be this little cli that you're talking about which can take in a very simple query and
show some output on the command line. That'd be great. I think
you're talking about instrumentation in the pipeline itself right.
jmacdonald 00:18:02 Yeah. So what I'm imagining. So, Laurent, I would need to find it. But Laurent has merged something, and it's
I'm not able to find it right now. But it's here. And it was just talking about the basic event structure that he wanted to have annotated or instrumented inside the data flow engine, and I'm extrapolating to from what he asked me to like, what I remember wanting myself in the same type of scenario was like, we're building a telemetry solution. We're we're experts at telemetry and instrumentation. We know how to run an SDK. But at the end of the day what we're doing is outputting these events which are have structure and ha! And and have the schema that we want.
And now.
you know, like, as a matter of debugging my own system. I don't yet care about performance. And this is not a large scale problem. This is like me on my developer box I run a test or a small example, it produces 1015, 20, MB of logs, data which is way too much for me to read. But I literally know how to query it.
because I understand the data. And now I just want to write A, I want to start my own query debugging cycle with my own tools that I like. I. As I mentioned, I built something like this in the past, but every time I did the project got canceled before I really got to use it.
It you know what I mean.
Drew Relmas 00:19:18 Right? Okay, okay. So we should talk about you know.
doing Std out into, I don't know, like a local file or something. And then, or it doesn't even need to be that. But yes, I think there is a path forward here to start using statements over actual data as long as we transform it into. You know, a format that the data engine understands. We're not there.
Yeah. Yeah.
Columnar.
Oh, sorry.
jmacdonald 00:19:46 There's a couple. Yeah, there's a couple of like little details here which I sort of. I'm trying to wave my hands at like we? We do know
format telemetry data. We could. We could write it as protobuf into a log file. We could put it in text as a way, you can turn back. This is in this example of what I'm not trying to get to is high performance. And I'm trying. I said 20 MB, because it's literally enough that you could just like load it into memory and do your dumb queries.
we, what do we get productionizing these ideas? That's when data fusion, and, like many gigabytes, are involved.
and that a different problem at that scale.
But for our own, like small debugging, it would be really great. My the example I gave is one that I feel like is a important query. It's 1 that turns logs into traces
as a as a telemetry person, and the idea is that like, if I have a event for every start and an event for every finish, I have an error code on the finish, and I can join it with a start time from the start event. Now I have a duration and an error code. If I join those 2 together I should be able to output a span. Now I should be able to query its latency. Those are the types of queries that I've always wanted to write, and I'm hoping that we can do something like that
gotcha tool
so that we could, you know, just begin to to like as the expression in anger like, I'm literally using my tools to try to answer questions about my own system. That's where I want to be.
Drew Relmas 00:21:08 Okay, gotcha. Yeah, I I think I think we should go down this direction. I'll try and write up an issue about it and talk with Blanche.
jmacdonald 00:21:17 Sweet. Yeah, and we'll bring this to Laurent, because he was the one who kind of pushed me to ask for it so. But I understood exactly what he was asking. So it's coming from my words, anyway.
Appreciate that.
Laurent Quérel 00:21:27 Guys. Sorry to be late.
jmacdonald 00:21:29 Oh, I just arrived.
They're all
I just gave Drew kind of a high, high, level overview of the conversation we had a couple of days ago, looking for a sort of simple Command line interface to use Kql to begin earnestly using our own telemetry.
Laurent Quérel 00:21:44 Yeah.
jmacdonald 00:21:46 And and so so if if you have anything to say on that topic, maybe do. And then
I'm gonna find the Pr. So that I can give it to Drew. This is the one.
Laurent Quérel 00:21:56 I'm sure.
The for me. The my main
advice for that will be to figure out what we want. But
the type of operator we want to support natively for Kql.
In order to query a stream of matrix, or a stream of span or string of logs.
In a very natural way. So I think we we need to see what that mean to use Kql on open telemetry.
stream of objects.
Because then and
I think that will be high level things, because the the term model is a little bit complex.
and we need to see how we can interface
high level intent in terms of queries to the the low, level
aspect of it. How we will integrate that with data, fusion and
oral, or maybe just directly aperture hotel functions.
And
I think, having a good representation or working 1st on what will look like the what, what will be the the
the aspect of this query. Language, and what would be the most important parameter will be super important.
jmacdonald 00:23:41 Thank you. Yeah. The way I
that sounds right to me, we we wanna we wanna get experience with our instrumentation and our queries. See if they're useful and functional and operational, then we can think about scaling them out and data fusionizing them and so on. That's at least what I'm hearing.
See pages with query, interface.
Laurent Quérel 00:24:01 Another aspect that I just remember now.
Sorry for that, if you compare that. But if you compare this potential Kql approach
with what we have right now in the go collector world.
So we have either a bunch of very specialized processors
or we have some ottl language that is not necessarily super turn to right.
but it's a it's a big collection of scenes. There is no, in my opinion, real uniform query language
tailored for matrix span and loads
as we could imagine create.
So I don't know.
For me. It's also an opportunity for us.
Create very efficient and very expressive.
Take your Cosiso to replace a lot of
multiple things that already exist in the go collector engagement.
jmacdonald 00:25:23 I'm reading the chat. By the way, Tristan, you know
I'm trying to stay away from this topic because I've sunk a lot of time into it in my past. But I mentioned a query, there's a story here. I'm going to tell it now. So back at Google, my old career there. There were Z pages. That's almost, I think that's where the idea that the name Z Pages comes from.
There was a a servlet we called request. Z. And I was sort of the owner of that, like a prototypical tracing system where there was a a servlet that you you could log log it. You could just load the page and and like start clicking into latencies, and so on.
And then, when you find a latency, you, you would either have a live trace, or you, you would find sample traces either, or
and then you would click through that to get to the the actual user interface that the tracing team gave you. But this Servlet was part of like the base library, and so everyone had it, and no one knew how to use the tracing system. They only knew how to use the servlet that was on every single machine, every single C plus plus binary. And we had debugged and, like feature, extended this thing to like crazy. And it was this like super specialized piece of code.
it was like full of hand optimization.
and as a budding observability engineer. I was sort of thinking to myself, wouldn't it be nice if I could take a query and compile it into something, and then upload that as the implementation of my servlet, rather than having this extremely bespoke piece of hand coded thing that was literally just doing one query by hand.
and the query I already told you the query. It literally was the query that I just described, which is like, find your starts, compute your durations for anything alive. Look at the errors, look at the the like everything else, and then choose one that was interesting, and then sample them. So you should be able to take a query expression, compile it into something, and then put it into a servlet and have it be that access point that gives you a way to browse through the the most interesting query, essentially,
that's what I want. I didn't say it, but now that Tristan put me to it, I said it. So there you are.
this would be amazing if you could take a Kql query that we've found useful, and then turn it into a an actual debugging tool that you would have available at Runtime. That's at least the idea.
Now, you see our ambition.
that was a good topic. I'm glad we spoke about it.
I think we've reached the end of that agenda item. And I wanted to
at this point ask if anybody has next topic.
why is the docs being weird? Okay.
I'm not hearing a next topic.
I don't. I've already put one person on the spot. Laurent, how about I put you on the spot.
Laurent Quérel 00:28:21 Yeah.
Just arriving in the office right now. So I'm a little bit more available.
jmacdonald 00:28:32 Okay. I.
Laurent Quérel 00:28:32 You want to talk about.
jmacdonald 00:28:33 I I was just wondering if there were any any important issues that you wanted to discuss.
as a matter of. We, we have a meeting with 9 people here or so.
Laurent Quérel 00:28:45 Yeah.
is. Do you think that? I was thinking about something about the internal tracing system that
we documented and started to review a few weeks a few days ago.
jmacdonald 00:29:00 This is.
Laurent Quérel 00:29:01 So that 6, 30, yeah, to peek, yeah, rather than yeah. This one.
jmacdonald 00:29:07 This one, this.
Laurent Quérel 00:29:08 Is actually.
jmacdonald 00:29:09 Kind of how I I steered the conversation just before you arrived.
Laurent Quérel 00:29:12 Oh, okay. So you already.
jmacdonald 00:29:13 Bharat has.
Laurent Quérel 00:29:14 It's.
jmacdonald 00:29:15 Well, I I didn't talk about it in specifics. I it. It was kind of given as the precursor to the conversation with drew where I said, Hey, we're producing these instrumentation events. We know what we're doing. Laurent has written up what he sees as the sort of good path towards instrumentation. I want to see us have a query that tool that we can use for ourselves. So you know, I think we've sort of covered it. But
th, this will become a question, and I may ask someone in the call. So so, for example, Ukars, to give us a an update on his thinking, when he sees this, you know, as an owner or maintainer of the hotel rest. SDK, how does this make you feel?
maybe I will do that. Utkars. Have you seen this? Pr.
Utkarsh Umesan Pillai 00:29:59 Yeah, but I haven't like gone into the details. I I saw that this was out, and I just like gave it a very brief look. I haven't gone into that.
jmacdonald 00:30:09 That's okay.
What I think we're the question we're facing right now. And 1st of all, is that the hotel collector has some its own project. The Go. The Go Lane Collector has its own project to develop metrics on itself, and it has taken a lot longer than you'd think, and it's like a top. It's a sort of a tricky, tricky topic.
we are
pretty close to that with this, but Laurent kind of came up with it from from scratch as I can, as as I would say.
And we'll bring them together. So the idea is that there's a standard schema for annotating a an event. As a piece of data passes through your data, flow engine, and the the
well, we should probably add a link to it. I'll I'll get us a link and put it in the notes. The the Rfc.
Was mentioned.
Laurent Quérel 00:30:58 I put a link into the document. When when you yeah, you you gave me the the info.
jmacdonald 00:31:06 Yeah, okay, there is a document. We we will link to it. It's not this one.
Yeah, it is this one. So this is the current work that the collectors are doing. So you get standard annotation standard attributes like component name, component signal kind, and standard response values like a refused count is someone downstream created a failure, and I'm just passing it back. Failed is the original failure. Type? And success.
This. This is something that I've been involved in dev designing and debating for you for a while, so I'm happy to take part in this conversation. The the work happening
in the collector is
the the reason why it's tricky, I think, at the high level is that the collectors model is receivers are shared by multiple pipelines. Each pipeline has a sequence of linear processors in it. So
because of of fan in and fan out
what I what I originally wanted for wanted in this case was some sort of rule of conservation.
I can look at a collector and drop all of its metrics. But if I know the the inputs and the and the downstream outputs, I should be able to infer what's missing. There's a sort of like I need to make sure that there's a sum which adds up to the total number, and that they either failed or were refused or successful, and then I should be able to take like verticals, like all of my sdks, add up all their trace, all of their production.
add up all of their refusals.
Looking at the collector that received all that data, I should be able to add up the pipeline totals at that stage in the pipeline, and so on. This argument sounds nice until you look at the details, and you realize well, there's Retries at every level, and there are places where things fan in and fan out so that you're going to count things more than once at an exporter, because it came through
and fanned out, and so on. So then, when you look at the actual complexity of these real pipelines which have fan in and fan out and retry. The most conservative thing we could do is just like count. Every single phase, every single component is going to have a full count of what comes in and what comes out.
which was perhaps more than you'd expect like it
if pipelines were simple and didn't have fan in and fan out. You would just count all the receiver statuses, and it would tell you everything, because the the exporters feed errors, feed back to the receivers. So you don't want to count too much, in my opinion. But the current status of this of this here is that we are counting effectively every component because of the potential for fan in and fan out, and the the desire to have full information, I think, is what I'd say.
This is an area where any one of you are invited to kind of like, investigate further and become an expert. I would enjoy that.
Utkarsh Umesan Pillai 00:34:07 Yeah.
Laurent Quérel 00:34:08 So I was not aware of these documents initially. But the
I'm happy that we we end up in a relatively similar approach.
even if there are some differences, because
the the data flow system that we are designing is
really a superset of what the the Google Connector can achieve.
So they aren't necessarily differences. Think that
could happen. That we can represent with this new rest, base data flow engine that we can't with the go collector. So we have to take that into account, especially in the tracing mechanism.
jmacdonald 00:34:49 Would you say that it is possible to construct a a go pipeline that represents the similar configuration by using connectors in weird ways? Or is it true? A true superset?
I've I've thought it.
Laurent Quérel 00:35:05 I think it's I think it's a true superset. I don't think that there there are some elements where
so, for example, this notion of output.
this notion of hyper edge with a dispatch strategy
as far as I know, it's not something that is generalized at all.
So it mean that for the, for the tracing
system, because we want it to be as
automated as possible. We. We don't want to rely on each component to participate to this tracing mechanism.
By default that should be able, the the engine itself should be able to generate those span or a subset of metrics without the intervention or the obviously the the component can add some additional elements that are specific
to them. But so if you go back to this concept of dispatch strategy, hyper agent output
they will be reported automatically. That's not something that obviously you can do with the
the pipeline system that is integrated into the go collector.
jmacdonald 00:36:27 Think I understand. It's something we what are we blinking?
Sorry. I want to make sure we all have all these links
I will add the to the to the doc. These links
Laurent Quérel 00:36:45 Yeah.
jmacdonald 00:36:46 That we have.
Laurent Quérel 00:36:47 Another aspect. Which is, I think,
of importance. And and a major difference
is the it's like we have, in fact.
2 type of flows in this new data flow engine.
We have this filter flow.
So receivers generate P data, pipeline data.
and and the traverse the the data flow and up to a set of exporters.
and and in between. It's really a dagger.
But we also have for each of those not participating to the dag. We have a controller.
We have a set of Controller messages. So we have effectively
for each node to except for the receiver, we have 2 channels
and and and the system. Listen to these 2 channel.
So you have a receiver
the. The priority will be to the control message channel, and if there is no control message channel, we go to the Pdata Channel.
and the processor will consume any of those messages.
So that in terms of tracing and debugging and troubleshooting, having a a good view on what is happening on these 2 type of flows. P data and control is also relatively fundamental. Because
What? Another major difference, in my opinion, is the fact that we want to
by having this control message infrastructure.
It's a way for us to externalize some
general capabilities. You you mentioned Retry.
We also identify failover and and many other control oriented processes.
That could be created as independent component, like a a set of
many tools that we can combine into a pipeline to create something that will be robust.
so that the retry mechanism. The failover will no longer be part of the exporter code.
That will be something externalized that could be composed very easily.
So the the charge or the load on creating a new exporter should be much smaller.
but at the same time we will get a much more uniform way to configure retry and and failover because there are
pre-built or built in operators or built in processors
that could be combined. That will for any data flow.
so those control messages will will participate greatly into the the debugging troubleshooting, and they will be very well instrumented, and always the same way
which make things much simpler, in my opinion, and more and more uniform.
jmacdonald 00:40:01 Th, this sounds fine to me. I think you're what the high level I'm taking away is that you know asynchronous programming is different. Russ is different. The synchronous versus asynchronous is different. The control message strategy is different. It's all different. We aren't gonna debug these exactly the same. And what we're focusing on is debugging, not standard monitoring at this point.
and and there just are differences, especially as you mentioned from the having an arrow frame means that we can assume 0 copy in many ways. This makes it possible to put all of those Retries queuing to disk everything else can be anywhere in the pipeline as opposed to right at the exporter because of the design
Laurent Quérel 00:40:42 Yeah.
jmacdonald 00:40:44 Cool.
I
I think it would be nice at this point. Since that I think we've covered that topic very well. Just as a kind of last topic, maybe, for the for the meeting here to give us a a kind of hopeful look forward. It looks like we've been talking a lot a lot of stuff and don't have anything built here kind of, but I know we do and I know that we're pretty close to standing up a kind of like bare bones, pipeline that can pass either otap or otlp data through it.
At the same time. I know we're pretty close to getting this benchmarking harness that we've got going up and running as well. And I'm pretty excited to have the the capability to begin running tests. Even of the existing go collector. So Laurent, would you agree with that state statement that we're pretty close to having an artifact that you actually could call a pipeline.
Laurent Quérel 00:41:42 Yeah, yes, I agree.
jmacdonald 00:41:44 Awesome.
Laurent Quérel 00:41:45 I was even thinking 2 days ago that we will have it
for today. It's not the case. I'm late, but
yeah, I think we are very close.
The We-we, the the decision. Let's say the
that we organize the the work right now. We started by defining interfaces for each of those
major component receiver processor exporters. And we created some kind of
test infrastructure. So each person can. In fact, each developer can, in fact, test their in isolation. They can test the receiver processor exporter. So we, we made some progress.
Even if we are not able to assemble those elements into pipelines, we are able to at least
initiate the development of many of those individual components.
At the same time, we have this pipeline engine and
and we are really at the end of the the 1st iteration, where message
P data message and and control messages will be able to move across this pipeline
but unfortunately,
I had too too much things to do
out of this project during the last 2 days.
That's unfortunate and
and then I don't have a ready pr, but what I can say is.
and a stage where tasks start to be assigned to each of those components?
So that we receive a configuration describing the data flow.
We we have a multi-stage process 1st
discovering the component described into this pipeline based on the the plugin system that we have in place.
we are able to instantiate the corresponding component.
Then there is a second phase of analysis of those node that are connected together.
Depending on the nature of those nodes.
If we have to note that our not send.
we, we can deduce that. Okay, we can use this category of channel. If any of this node is, send.
oh, 2 of them, or one of them. Then we have another category of channel that we can use, and then depending on the
the, the cardinality, the number of destination for this hyper edge.
we we can determine if we have to use an Spmc and Mpmc blah blah, so that exists. And and the last piece was, okay. Let's
start each of those node into their own
Sm task so they can consume their corresponding channels. P data and control channels. And that's where I am. I still have some.
Let's say, rust design issues that. I like to to optimize or to
refine a bit. Hopefully. Maybe tomorrow I will be able to do that, I hope? No, but it's very close.
jmacdonald 00:45:18 And then we'll take just a sec, Tristan. We'll take Albert's work. We'll we'll figure out how to make a raw otlp receiver. I think that doesn't parse the otlp as message objects. Turn it into ocap and and we're off the races. At that point. I'm excited.
Tristan, you have your hand up.
Laurent Quérel 00:45:39 Yeah.
Tristan Sloughter 00:45:42 Yeah, I. It sounded like it. And it might be answered in your
comment in the Google Doc. But this test framework for performance can be used for the go collector as well.
jmacdonald 00:45:55 Yeah, let me talk about that for a second. So
we. So let's see, we have a member from each of each side of the the F. 5 and Microsoft side here working together, and I don't think any of them are in the room right now, but we have C. Joe, who, you probably know as a Long Time hotel contributor
as well as Chris on the F. 5 side, and they've been developing a python framework to just like, you know, we've seen these before, but but they don't. They're often not reusable, and the idea is that this is a way to to kick off a dockerized container with a collector artifact in it and a configuration, and like, have it execute and like, give it some predictable load and measure it, you know.
of
fairly you know, bare bones, benchmarking framework. But but the idea is that we'll be able to use this kind of like to do canned testing of of full, fully assembled collectors.
And I'm interested because, you know, I've been. And I was gonna give a quick update. I've been working on the Go side on the collector side for a while, and one of the things I'm working on is limiter extension interfaces right now. And I really need to be able to just like, do an experiment where I where I say, this is a thousand Qps. And like, I'm gonna run it without the memory limiter. And I'm gonna run it with the memory limiter. And like, I need to be able to see the memory profile, the throughput and the latency.
and I and I want to be able to show them side by side, and I want it to be very easy, because once I get that test I got 3 or 4 more that I want to do to show you like. Here's the new limiter. Here's no limiter.
Here's crashing because you have no limiter, and so on like and and I really want these tests to be able to measure, not just like pass fail. But like, okay, did you drop 3%? Or did you drop 17%? Or did you drop 65% like those are different kind of regimes and at some level we want to test
failure. Near failure modes like you're overloaded. What's happening? Those are the tests. I want to be able to run, and we're getting there as well.
so so that's that's one reason I'm looking forward to this testing update. I ha have been busy my update for the last couple of weeks. I've been busy in the Go side and have produced some progress there. So we've got extension interface limiter interfaces coming coming soon.
And I sort of checked that off and and send it out for review. My work this coming week. Week or 2 will be, for this group will be starting to design, based on tremendous work by my teammates. Here. Go plug in system that will give us the 1st type of interoperability story for for rust.
I have been doing quite a bit of research. I'm favoring this from bytedance. The rust to go repository, which is a sort of framework for bridging. Go and rust. It appears to be pretty good, and that's where I am, so we'll be I'll be looking into. How do we
make plugins in? Go? That can also be rust plugins?
Laurent. You had asked me how we will get to the collectors. Configuration, which is you know, something that we don't want to parse ourselves, and and like probably can't I've started tackling that topic first, st just to, because we should be able to to get the configuration from a go collector. Even on the command line. I want to be able to print the configuration that's parsed by the go collector. And that's currently not possible.
but but one of the one of the things that we should be able to do is start a start, a go collector on a single thread, ask it for the configuration, ask it to start one component, have it do something with us in a, in a shared environment. That's where I'm where I'm kind of investigating right now.
Anybody have thoughts on that topic.
Laurent Quérel 00:49:50 Yeah. The yeah.
Try to to assemble my ideas on that. The.
jmacdonald 00:50:02 I'm aware that investigate.
Laurent Quérel 00:50:05 Yeah.
jmacdonald 00:50:06 I'm aware that the idea of rust interrupt with go worries you a lot. And I and I definitely want you to have the freedom to, to kind of pursue pure rust for for sure. And that would be one reason why I could imagine saying, Hey, go, collector, I want to invoke you on the command line to spit out 1st Json instead of Yaml, for example. But but but we definitely have
plans that involve, you know, maybe not as a performance requirement, but as a sort of like bare requirement, a minimum requirement to be able to interoperate some way in some way.
even if it's not what's for the short term.
Laurent Quérel 00:50:46 What not worry me is so, for example, interpreting the
the yam, reconfiguration files from the go collector, or any version of it does not worry. You mean at all. In fact, in the
the proof of concept that you are aware of that has been created. 3 years ago I was already able to read entirely the file. It's it's not a big deal it's.
jmacdonald 00:51:13 Yaml is unsupported. Dead code. There's no Yaml parser in rust that anyone trusts.
Laurent Quérel 00:51:20 Yeah, we solve this problem with other things in, for example. But no, that doesn't worry me. What worries me more is
there are so many ways to integrate the good connector with resourced. And if you look just at that in terms of
graduality of integration, you could ever imagine to integrate
these 2 components at the pipeline level.
or, like you said at the node level.
In my opinion, it's so much easier to integrate at the pipeline level first, st
and then maybe at the node level, than trying to start at the node level. First, st because that is.
I mean, without comparison, much complex.
jmacdonald 00:52:19 I I think I agree. But but tell me exactly what you mean by pipeline level in this case.
Laurent Quérel 00:52:24 Pipeline level will mean will mean that
either we, the go collector, provide a configuration, a definition of a pipeline that we know has to be
instantiated as a tap pipeline.
So the go collector is analyzing the the Go collector. Ml, configuration determining. Oh, this pipeline is of this network boom. I just delegate that to the to the rust library that is integrated into the go collector super easy.
It's just a matter of defining an Api Google connector extract the the configuration. And
and this library is responsible to
to analyze and start the pipeline and reporting potentially some
some matrix span, and so on. So the Google Collector will be the only components to
to read the configuration and to report the metric corresponding to the
anything that represents observability, for the the go collector will will be I mean, that will be transparent for the the end. User.
Now, if we are talking about. So a zoom pipeline integration will be
the boundary of those pipeline. We can start by that, maybe. Imagine that we have
receivers. that are in go. And then we we create some kind of connectors between those receivers and
the rest of the pipeline could be an attack pipeline that, I think, is achievable in a reasonable way, and will give us a
a nice way to reuse the the existing ecosystem for receivers. We could imagine to some extent.
That for the exporter I think it's slightly more complex. But the most complex things, in my opinion, is for the processors.
when they are part of the pipeline.
and because of the control messages, because of the way that go and rest are working differently. That's where I think is.
I'm not saying, it's impossible. I think it's possible.
But if we start with that, it's like starting with the most complex thing, and I'm not sure that at the end we will. The the gain of doing that will be that great
I really think that if we start with spike food, pipeline, and then maybe boundaries. I think it will be already
a very nice gain.
Let me see if I can. Swimming integration.
jmacdonald 00:55:14 You you would like to see integration start at the start where you you look at your your
combined pipeline configuration, and you say, Oh, this is a pure go pipe. This is a pure rest pipe first.st That's easy, like those are like basically parallel processes. You could start them in the same addresses. Then, you could imagine a refinement of that where?
there are interfaces between pipelines, where you're you're gonna reach a terminal on one rust, say, and then like, do something fairly expensive to like. Move that pipeline into move that data from one pipeline into the other, and that's the the naive way to do that would be to use an Otlp receiver and an Otlp exporter, and just like literally cross pipelines by exporter receiver. And that would be
the worst potential performance, simplest integration, because it's like just reusing what we have.
And I think what you're suggesting is that we should not aim for a more
more optimized foreign function. Type interface calling convention between the go and the rust components. I think I agree with you on that. Nevertheless, the stuff we're building here in rust. If I can't make it available and go.
despite performance penalties in the shorter term. I'm I'm getting resistance. Like I I need I want to be able to
expose the stuff that we're building in rust to a go collector user
as a like proof of concept like this may not be fast. But like you can do this stuff that we're like. Here's a way to run. Kql, that we've prototyped. That's the idea that we're what we're aiming for. So it doesn't necessarily have to be super high performant.
which is why, I'm willing to fall back on that
worst case. But we're investigating the like. Better case of you know Ffi, instead of like rpc,
but I hear your concern. I'm I'm gonna be working on this design for the next couple of weeks, and I'll make sure that you see it
soon.
Laurent Quérel 00:57:30 Cool.
jmacdonald 00:57:34 Alright. I think we've definitely reached the end of the call. I want to apologize to
Didn't run through introductions because almost everyone's been here. And we did introduce Michael. I want to introduce Gokhan, who is joining us from my team at Microsoft.
and who is one of our experts on testing the collector as well. So I expect more to come from this collaboration, Gokhan, if you'd like to say Hello, if you're still listening, please do.
Sometimes I catch people off guard. There's.
gouslu 00:58:10 Could be.
jmacdonald 00:58:12 Hi Gokhan just wanted to say hello, since we had a couple of minutes at the end, just to to greet you and welcome you to the group. Thank you for being here.
gouslu 00:58:20 Yeah, thanks. Yeah. I'm trying to find some issues to work on
to warm up. And, you know, get involved in.
Let's see how that goes. Hopefully, I'll be able to contribute within the testing front as well.
jmacdonald 00:58:35 Yeah, I mean, I think you've been like actually leading the work inside of our company on this. So you should be able to share a lot of your knowledge with Cjo and Chris, and we'll we'll go from there. So thank you very much. We'll see you again. We've reached the end. All. Thank you all for being here.
Laurent Quérel 00:58:50 Oh, we also have the so so, Josh, I like to introduce Michael Salib also on our side
that joined the team. This week.
and he will work with with us on on various things. So, for example, Albert will.
we'll go in Pto for 2 weeks, and and Michael will take what albert did. Logs and try to
to recreate that for span Michael, do you want to say a few words.
Michael Salib (F5) 00:59:24 Yeah, I actually spoke up a bit before you showed up Laurent. So.
Laurent Quérel 00:59:27 Oh, okay. Now. Sorry.
Michael Salib (F5) 00:59:29 No worries. You're good, but I am. I am trying to extend Albert's amazing work on logs and taking it to the span world and so then we'll go from there. So works underway.
Laurent Quérel 00:59:40 Okay.
jmacdonald 00:59:41 Oh, yeah, I meant to. I meant to sort of throw out one thing. So my original work, my prototype on the on the views. Idea was to use Macros and to generate Code Albert. That code could not have been written by a macro. There was quite complex. Is that what you think we're going to maintain these by hand? If a new field arrives in Otlp, we'll just go.
Just go do it.
albertlockett 01:00:08 Yeah, I I mean that that would be my preference.
Like it it. It doesn't. It doesn't take too long to to add
a feel to these things. And I don't know how
you know how often, how often the protocols change. But but I imagine that you, you know, like.
when that happens, we we could just go add it, and even like you know, if if there's like a few like, you know
a few different places that we need to like. Add that field
you know. I think once we do it once at least, we'll have like a Pr that has like, hey, here was the change set when we went back and added, like event, name or entity ref, and then we'll be able to, you know. Use that as an example. Next time we need to add a field, so that that would be that would be my preference. to.
jmacdonald 01:01:05 Makes sense.
albertlockett 01:01:05 Complexity. But but then again, like I'm not, I'm not as deep in the prop macro world, so.
jmacdonald 01:01:09 No, I I feel like in hindsight. It took me like 2 weeks to make a macro, and then you took one week to do it by hand, and it was way more complicated. What you did, and and more successful. I think so. The sort of a a proof that we don't want macros in this case. Of course we still have that macro infrastructure. I will be interested. Let's follow up another time. How you feel about it. What's what's worth keeping and what's not? But that'll be another time. Thank you all.
Laurent Quérel 01:01:37 Thank you.
jmacdonald 01:01:37 Bye. We'll see you next time.
Drew Relmas 01:01:40 Thanks, bye, bye.
gouslu 01:01:42 Bye.
