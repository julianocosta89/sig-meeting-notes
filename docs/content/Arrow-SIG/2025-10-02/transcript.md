SIG: Arrow SIG
Date: 2025-10-02
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**albertlockett** 00:13 Hey, Laurel.
**Laurent Quérel** 00:14 So do you have now?
**albertlockett** 00:15 So what?
**Laurent Quérel** 00:17 But… leisure.
Good God.
**albertlockett** 00:23 Nope.
**Laurent Quérel** 00:24 ma'am.
**albertlockett** 00:27 Oh.
**Laurent Quérel** 00:29 Ms, you know, sera.
the double.
**albertlockett** 00:35 apres de seventh.
**Laurent Quérel** 00:41 But…
**albertlockett** 00:41 The dessert.
**Laurent Quérel** 00:42 cares, mais…
**albertlockett** 00:44 Yeah, but…
**Laurent Quérel** 00:45 Non, c'est fait deux autrend pour trois, c'est fait…
**albertlockett** 00:51 See, it's a fact.
So that's for sure.
**Laurent Quérel** 00:56 Okay, okay.
**albertlockett** 01:00 Bye.
**Laurent Quérel** 01:02 parler des journee.
surre… Quest les…
**albertlockett** 01:15 oui, j'ai j'ai montree ce que fait il y a 3 semaine avec… KQLP Data Fusion.
Hey, Kirk.
**Laurent Quérel** 01:26 How you catch?
I'm updating the… the document.
**albertlockett** 01:53 Okay.
The agenda from last week, it looks like Drew was all alone.
**Laurent Quérel** 02:09 Yeah, yeah, yes.
Okay.
**albertlockett** 03:21 Thanks, Josh.
**Laurent Quérel** 03:27 Pleasures.
**jmacdonald** 03:31 There it is. Hi, good morning.
**albertlockett** 03:34 Right now.
**jmacdonald** 03:38 I didn't prepare much for this meeting, I've been having a little, sort of, like, backlog for stuff, so…
Laurent and I spoke yesterday. We are agreeing to make milestone plans for the future, looking at what happens in the next month and a half, especially.
If I had a takeaway from the conversation we had yesterday, I thought two things. One is I'd like to talk about KQL and the work that you did, Albert, for your, hackathon-type effect, two weeks ago.
And second is, I don't think I should walk through the…
ACNAC message, if it's just the four of us, since I've kind of explained it already to Laurent. I'm feeling good about the work I did as far as proof of concepts go. I'm going to start back at the beginning and make it pieces that we can actually merge and not break the bill and so on.
With that said,
Yeah, so I… so, let's see, I never, in this forum, really walked through my… my hackathon project, in depth. I don't think Albert has gotten to hear about it, so I think that is the conversation I would like to have.
Since it connects with this KQL topic, connects with, I think, the most ambitious part of our goal over the next
you know, 3 to 6 months, is that we would like to turn the KQL
effort that we've begun to prove out into a real processor that
ideally leverages Data Fusion, or is better. I think it's going to leverage Data Fusion.
So, for me, there was a lot of learning about data fusion.
And I think that was the real benefit of the project.
So, I would… if that seems like an okay topic, I will carry on then.
Alright, give me a moment to find the document I want to share. It's not very good, but it'll be a starting point.
So… I do have this… I want to make… actually, what…
Yeah, I have a branch.
On the public site, so that we can all see it.
But I have to find it.
Bear with me.
It's somewhere.
There it is. Okay.
I'll share my screen. I… I was thinking I would make a proper PR out of this, just to make it easier to share, but there's a few bits I want to scrub out. It's just kind of a mess, and it has all kinds of…
messy stuff that was a little off-topic. Okay, here we are.
And, so I… first thing I did was clone the entire repository, put it into a place I could mess around.
And we can look at all the changes I made. One of the things I had to add was a bunch of debug logging, because I was having major difficulties. You saw the thing with configuration structs, like, I had to add logging everywhere before I was really making sense of it. So I do have a, like, longer-term question about…
I mean, obviously, we're open telemetry, we know about logging, we know about telemetry SDKs, but…
I want to see how we're going to do this, and I don't have a strong opinion. I used the Rust log environment, you know, the Envlogger and the standard Rust log package, which I'm getting comfortable with, though…
Partly, I've noticed, these, Copilot and the agents that we use have memorized how to use some existing software. Try to tell them to use an alternative telemetry SDK. It will not work. They know how to use the one that we have, so that's what I've observed. Tell your agent to just go instrument with some logs.
That's what it knows how to do, you don't have to teach it. Try to teach it to do a different logging API, terrible idea.
So anyway, I did add a bunch of logging.
This is the wrong directory.
So… I'll get to the point here, somewhere.
So, the key idea was I wanted to write a tail sampler. Obviously, we didn't get anywhere near complete, but I've wanted to… my other role in OpenTelemetry, I run the sampling SIG every other Thursday with this meeting.
And we've got some new specifications that are, like, coming through, and…
the Go tail sampling processor is a big mess, so the idea is that there's an opportunity, and I would like to see us explore it. So, that's where I started.
I was… I was so pleased to see Albert's demo of the Parquet exporter, and… and Laurent, you… both of you showed, I think, actually it was Albert's, the SQL query that I believe was Data Fusion, just tailing some Parquet files. So I took that as inspiration.
So I've kind of talked about the vision, is we're gonna do… we're gonna do tail sampling with OTAP and Parquet. The idea of using Parquet is to facilitate… well, the concept of tail sampling is you're gonna… is you're gonna sample down a lot of data, so I want, like, an entire minute
or 10 minutes of data, and I want to put a sample together that's a few spans. So I'm going to read a tremendous amount of data. I can't store it all in memory, which is how the Go tail sampler processing works. So background, you know, this is actually what you guys know. This is Albert's output from the Parquet exporter.
I love sampling, and I… and I explained all this stuff to Ukarsh, who was very patient with me while I rambled on about weighted sampling.
So, the first thing I did was try to implement Parquet Receiver, which required me to learn a bunch of stuff. You know, you can… you can open a Parquet reader on each file, so first of all, you have to organize them into partitions and directories with timestamps, and they're sorted, and so on. And you can stream through each file, and you can stream through a sequence of files with a Parquet reader. So then I have
I only did logs, so I have 4 types of file in my partition, and so on, you all know this.
what I did then was…
You know, do a sort of super simple, monitor the file system, like, every 5 seconds, look for new directories. sort, like, discover new files in each partition, order them by timestamp.
begin reading streams of them, starting with the logs table first, which has the ID, and then join it with all the parent IDs. This gives us, essentially, a cursor through each partitioned file series.
And then, you know, the logic is fairly straightforward. You're going to have these four cursors. You have to limit the maximum size to a Uint 16, but they come in as UINT32s.
you have to do some basic manipulation, arithmetic there to offset each frame, but it was actually quite straightforward. The hardest part that I had was making sense of the code, and
explaining to the agent what I wanted done, because I was doing a lot of this with the AI assistant. Eventually, the last piece of it was getting that plane encoding tag correct, and then all of a sudden, it just worked. So…
So then, this was basically a proof of concept that I could, like, spot some data on the file system with the exporter, and then start a pipeline and read it back without a lot of sophistication. Because obviously, it's just replaying every piece of data it can find, and there's no state.
So… so that qualified as a success for me, and I moved on. I decided
now I wanted to actually try to do a sampling effect… effect. And…
I wrote it down here, I don't want to read it, so basically the idea is that the key concept we want in weighted sampling is to have an input weight and an output weight.
In spans, there's a field there that you can do in the main table.
It's in the trace state column.
But in logs, there's not, so it makes a lot of sense, and there's precedent for using the attributes table. So, the key idea is I need to, like, read all the data.
Filter by attributes.
Read one of the attribute values, do some math and sampling logic.
and then output a new value. So, did a bunch of research on data fusion, learned how the user-defined aggregate functions work.
I never actually implemented all of this, but, you know, the concept of a UDF or a UDAF is fairly clear.
So, then the high level here is that I'm going to write a query over the logged actors table, I'm going to select the
at the sampling weight attribute that I want, I'm gonna do a UDAF, I'm gonna output a sampling weight that I want. That's the core query. It's over attributes.
To make this whole, I need to join with a logs table for timestamp queries, join with other tables for resources and scopes, and so on.
The thing I haven't… I haven't mastered Data Fusion yet, but in order to do this, we… I'm using the listing table, the partitioned virtual table.
providers.
The listing table just reads the Parquet files, the partition file knows how to add this virtual column.
So then, I've issued a sampling query that returns attributes. I'm just going to jump to it. This is approximately what it looks like. I did get this to work approximately.
This coalesce block here is the part where we take the input weight from the attributes.
and output it. If it's missing, we fill it in by a coalesce.
We're able to use the service name in a WHERE clause below by identifying it here.
So that's in… in a WHERE clause here.
The logs table is what carries the timestamp. I've left that out of the presentation here, but in the actual query, we throw on another clause for timestamp queries. And that's because in order to do sampling, I'm putting them into timeframes. What I really want is to have a series of one-minute windows. It could be any interval, but I want to say all the data for one window I'm going to sample.
And of course, there's questions about late arriving data. We're not going to talk about those. What I've done now is just put in a delay. Like, I'm gonna wait 10 minutes, and then I'm going to sample 1 minute of data, assume it all arrived.
So, by the time I've actually assembled my list of Parquet files and partitions and so on, I've identified roughly which time bucket they belong in, and then there may be some overlaps. So, one Parquet file may span a window or an interval, so then we add a time query by filtering that logs table.
In the table… in the data fusion query.
This would be the step where we apply a weighted user-defined aggregate function. I didn't actually implement this, but it's not far, and the pseudocode below will help explain it.
So this would choose 100 log parent IDs.
Matching the attribute We could group by service name, so this query should select 100 per unique service.
Which is the kind of… kind of sophistication that we expect to see in a tail sampler.
And then, and then, now that I've explained the query, all… basically, I have this major query, which is fairly sophisticated, that can select all the attributes. What I do is I compute an array of parent IDs.
So I say, select 65,000 or 16 bits worth.
of parent IDs that match my sampling query over attributes. Put them in a mem table, and then issue four queries, one per table. These are my IDs. I want… I put them in a mem table, table provider, table provider for it, and then I… and then I just query those four tables for just the IDs I want.
DataFusion goes and finds them, and then I do the same sort of cursor stitching back together OTAP frames with offsets and everything.
It did end up, of course, what I did was program the 100% query, which is a sampling query, I'll tell you, but all it does is pass through the data in this much more query-rich way.
In the end, it just prints the same stuff, but it runs… it does inject a sampling adjusted count, and it's ready for me to implement the weighted aggregate function.
As you see, I really like sampling. This is… the algorithm I would use.
If we were going to use, and this is sort of how it looks. You just maintain a heap of n plus 1 items and their weights, and, the magic happens in the math.
Yeah, I wrote a bunch of documents, mostly by my co-pilot. I had a ton of fun, but basically, the bottom line is I learned how to use DataFusion, I learned how to work with OTAP in Data Fusion, I learned to successfully turned Parquet into data… into OTAP frames. I feel very good about it.
That all…
leaves me feeling confident that we can do something very good with Data Fusion and OTAP, but it's in front of us. I think Laurent has some ideas. I can feel them, but I don't see them yet, you know, like.
those queries are not very easy to write. We don't really expect users to write that type of SQL query, and this is where the motivation to consider KQL
arises, I think. And even if it's not users writing KQL,
or users writing SQL, we're going to have to program these, and I don't think we want to write those SQL expressions in code either, so we're starting to learn… I want to start to learn more about, you know, creating logical plans directly, and what are the patterns that work for manipulating OTAP data? That's what we're sort of looking at.
Yeah, that's what I had for, for my, my,
my little data fusion extravaganza. Seems like it connects with what you were doing as well, Albert.
**albertlockett** 17:20 Hmm,
Yeah, that's, that's really cool. I guess, like, my… my two experiments were, like, maybe, like, quite a bit more basic, where it was just more, like, write everything out to Park A, see if we can query it using Data Fusion SQL.
And then, obviously, that SQL gets translated into, like, a logical plan underneath the cover, so then I tried building the logical plan directly from our intermediate
expressions, which is what gets priced from KQL. So it was a very basic mapping of,
those intermediate expressions to expressions in a data fusion logical plan. Just trying to connect those two pieces, basically.
**jmacdonald** 18:07 And it was, like, the first…
first query, essentially. Like, I can't remember what it was.
**albertlockett** 18:12 Yeah, I had a couple.
**jmacdonald** 18:16 Here it is.
**albertlockett** 18:17 Yeah, if you pull up that…
And then, yeah, if you scroll down here, so it was just, like, I just had a handful of, like.
It's…
**Laurent Quérel** 18:28 Really, I just shirt.
**albertlockett** 18:29 collect…
**Laurent Quérel** 18:29 This kind of stuff.
**albertlockett** 18:31 select star… like, these essentially get translated into, like, select star from…
the log attributes table where, and then translating the KQL where clauses into the data fusion, like, filter expressions.
**jmacdonald** 18:49 So, and that means that this query only retrieves attributes, but if we look at what I just described, effectively, we combine these, I think.
Because I was also querying attributes and then reconstructing OTAP with the other tables there.
Well, I guess one of my bigger questions about data fusion that I've started to have here is that we do this query over four tables, right? We have a query that writes
like a… resource name, a scope name, an attribute value, and a timestamp. Now we've hit all four tables.
And I'm producing a query that's gonna output IDs. And I just read all those tables.
I'm gonna have to re-query the tables with the IDs to get the full records, because I…
the limitation that I feel, which I'm not an expert on SQL, is that, like, I can only query one table in SQL, and I want to query four tables all at once, and have a DataFusion execution plan that's like, this query is going to touch all the same data as these queries.
And they're gonna be… I can't tell… if I'm…
because of the many-to-one relationships between the tables, I can't write one query and produce all the data, is what I'm… what I'm struggling against.
In my example, it was that I… I have a sophisticated query to retrieve log attributes. I put it in memory as a list of IDs, and then I re-query the tables I just used to get the full data. That bothers me a bit, and I don't…
Have a sense of what is possible.
**Laurent Quérel** 20:24 Yeah, that's why I think the…
Looking at the most efficient way to achieve, for example, rewriting, transformation.
We, we'll… in some circumstances, I think, involved, us to directly use Apache kernel functions.
With the knowledge that we have on the… on the… the values type of table.
To optimize the production of the resulting, OTAP messages.
there are ways in SQL, for example, to create, especially… it's more on the select side than in the creation, or the, let's say, the insert, or the create table from a selection.
Because when you… when you just have to select, you… you could select multiple tables at the same time, merge the result.
in a single query, and apply some modification on it, and derive from that some result, like, what, what are the logs that match XYZ, and that they have,
Resource attribute or a scope attribute of a specific value.
That could be achieved with a set of join, and that's super easy to write. Let's say super easy. Not too complicated.
But now…
saying, okay, I have this select that, is indeed selecting the right set, the right subset of logs.
Please now filter out all the… the logs and attributes that doesn't match this select. That is…
**jmacdonald** 22:17 Hmm.
**Laurent Quérel** 22:19 not that too complicated. It's not necessarily super easy, because, like, SQL is not… is not designed, as far as I know, to…
To create multiple tables in a single query from a set.
And I think it's not necessarily super complicated for us to use the result of this first query.
get the… the values ID,
And make the filtering ourselves in a single… say, in a single pass per table.
And that way, just recreate efficiently the resulting batch. I think we need definitively to explore this, this space.
Maybe we will have to create some, maybe a way to do that also is to… to create some kind of UDF function into data fusion to help us
Create, a new batch full of multiple tables.
from the result of a SQL query. Maybe that's another option.
That will basically do what I just said or described.
I think everything is open, but I agree. Right now, with data fusion alone.
It's a little bit cumbersome or complicated, and probably not super efficient to do it.
**jmacdonald** 23:45 Makes sense to me. And it's curious and interesting. I mean, like, those ideas sound viable, and I think we…
We'll have to learn more.
Yeah.
**albertlockett** 24:01 I've… I struggle with this too, Josh.
**jmacdonald** 24:03 Yeah,
So yeah, if you look at my PR, you'll see that it was not written by me, but lots of logging.
Well, since we don't have Drew, I'm gonna meet with him later today and see if I can wrangle some, like, focus on this next…
Milestone project, but let's talk about the milestones now.
**Laurent Quérel** 24:27 Yeah, so can you share a…
**jmacdonald** 24:30 Oh, I was… I can share it with you, Ken.
**Laurent Quérel** 24:34 Okay, we shall.
Okay,
Sweet.
So… There is a new milestone
the label of this milestone is not necessarily definitive. Maybe that will become December 2025, I don't know. We have to…
to determine that, but I think the most important part is…
The, the goal that we, we are fixing,
both sides, Maplesoft and F5.
To summarize, in fact, it's…
Trying to reach a point where…
what I named the data plan, so that this, this, open source project,
Able to run pipelines.
Relatively simple right now, because the number of receivers and processors are limited.
But at least we have… maybe we will have one or more additional of those components.
But…
For the end of this milestone, the goal is to have something where we are feeling comfortable that we could deploy it in production.
Or at least in a beta mode, for… F5 and Microsoft internal teams.
In replacement for, for example, for the GoCollector to achieve better performance.
So that means that we…
**jmacdonald** 26:31 set of processors or bespoke processors that are custom exporters and so on, that we're not going to publish, as you were talking about.
**Laurent Quérel** 26:38 Yeah, same thing for us, so the… for this specific, aspect
that Josh just mentioned, we have already identified a way to do it. We didn't implement it, so maybe we will have some bad surprise, but at least the theory is the following. We have this GitHub repo, public, on which we are working every day.
both Microsoft and F5 said that they will have their own private repo, could be for us in GitLab, for you, probably in GitHub.
And, we can make a reference to the public repo.
extend the CLI app that we already have in the public repo.
And, add, one or more, type of nodes that are, bespoke, specific to our environment.
And when we compile this new extended CLI, we should be able to create a configuration file that
are, in fact, have access to the merge of the various notes type that have been declared with the NCME mechanism.
So…
The goal of this milestone is, one, to support these kind of things, second, to, to be, robust. So we have to create something that, could be
Put in beta mode in production, or with some,
Environment with a minimal risk.
We need to make sure that the performance are demonstrable and better.
Ideally, in all the dimensions.
CPU, memory, and network usage.
We need to… to implement to make sure that the back pressure mechanism, or it's biologic, phylogic, is in place.
But maybe it's a stretch goal, but we need to see how to encrypt and potentially put in place some kind of authentication.
So, I will put that as a stretch goal, but for us, for example, there are some scenarios where it's not required, and for other scenarios, it is. So that will just restrict a little bit more the perimeter of the
the experiment with internal team, if we are not supporting authentication.
a minimal support for the level configuration. Again, I think it's a stretch goal. I need to… to split those goals in two parts.
the… what I consider switch gold, and… and we could have a different view on that.
I think we need to take the…
the most restrictive one. So, if, for example, Microsoft think that,
LIVO configuration is mandatory. We have to put that not as a stretch goal, but more as something that needs to be there.
Some basic query processing,
And another important aspect is the serviceability, so because we want to deploy that effectively, for example, into Kubernetes clusters, we need to make sure that we have the
the standard required endpoints to operate the system, and in order to make that… to make some automation around it, like the else endpoint, like the status endpoint for troubleshooting.
And making sure that we produce metrics and events, that could be sent to some kind of, production observability stack.
**jmacdonald** 30:29 Yeah.
**Laurent Quérel** 30:30 And.
**jmacdonald** 30:31 We definitely need to have a way to push metrics as OTLP to fill in, you know, the current use cases.
**Laurent Quérel** 30:39 Yeah, I'm comfortable with that, I think. Yeah, I think it's,
I didn't implement it yet, because I was focusing more on the troubleshooting
For the… for the tech summit, where we… we just had to…
to query locally the aggregated metrics, and it was also used for the benchmark infrastructure that Chris implemented.
**jmacdonald** 31:02 Yeah, I like that.
**Laurent Quérel** 31:03 But yes, I agree, we need to produce those metrics with the…
OTLP matrix. And something that is fundamental, it's at the end, but in my opinion, that should be one of the first items into this milestone, and we are very close to have it. In fact, it's more because I… I'm still working on something for Chris.
But we need a continuous, benchmark infrastructure.
as soon as possible, so every… so the goal here is to make sure that We have a reference.
Where we know that for a new PR,
We have no performance regression. And if we are,
we need to come with an explanation. We have a regression because we have a new capability, and this capability is required, it's important. Right now, that's the best that we are able to do. Maybe at some point, we will be able to optimize it a little bit and go back to the previous result.
Otherwise, and most of the time, that will be the second option, we'll produce, without knowing it, some performance regression, and we will be able to capture this event
Pierre, pure, Pierre.
**jmacdonald** 32:21 Yep.
**Laurent Quérel** 32:21 And yeah, that's very, very fundamental. The second part is,
simulation-based CIO testing to chaos testing. I think we already talked about that, but there are multiple types of environments, with… compatible with Tokyo or not. I mean, some of those environments are agnostic to the…
asynchron time, or even the approach that we are following, because they are very low level, only working on Linux, and…
Creating some kind of virtual environment where you can inject Issues.
And, and some of them are, like, turmoil, and might seem more specific to, to procure. And, and basically, they let you create
Unit tests, where you are able to simulate the creation of multiple servers.
And you define the property of the network connection between these virtual nodes.
Our virtual process. And then you run your system, you can act, define a scenario for the various error that you want to inject.
And you see how the system behaves. That's… I did that on a various project before.
It's a fantastic way to capture a complicated problem without observing them in production and trying to reproduce those complicated scenarios.
Yeah, so for me, that's the goal of the next milestone.
Joshua, do you have anything else to add to that?
Oh, you are muted.
**jmacdonald** 34:23 I'm… I think I mostly, 100% agree. I don't have a sort of strong standout list here. I'm looking at the one about rate limiting, thinking that's… that's the furthest behind now, because I started looking at that, and then I got…
you know, all the ACNAC stuff.
But I… I…
I also really liked what you just said about how, like, what I want to see us testing is, like, let's put a rate limiter in place and see what actually happens, because either it's not going to run on memory and
correct back pressure, or it's gonna, like, fall apart, and I'd like to start testing that type of
you know, limits so that we don't run on memory. It's like, the big problem with the collector, the Go collector, is that… is that we don't have a lot of control like that, and so, I would more or less just…
emphasize what you said. We want reliability, we want never to crash or run into memory, and have, you know, predictable back pressure behavior.
Mostly. And then I… without getting into, like, December, January, March, like.
My… my priority is to see, a release
even that's not… has no focus on what the companies want with their internal builds that we are all focused on. But, like, I can say to the community and the 25 internal teams that have GoCollectors.
This is coming. This is what it looks like now. It's pretty rough. It's just finished, like, 0.9.
we want to run this in 6 months, we're gonna run this in 6 months. You can see it now. Like, that's what… what I kind of want to… or, you know, four and a half months from now. So, I would… I would just put all the emphasis into reliability and, you know, sort of stability efforts.
Yup.
If we have…
**Laurent Quérel** 36:18 We are to delete.
**jmacdonald** 36:19 Memory limit.
**Laurent Quérel** 36:19 urge, and…
**jmacdonald** 36:20 Andreas.
**Laurent Quérel** 36:20 And kind of film.
**jmacdonald** 36:22 I'll be happy.
I want memory limits and rate limits. I think that's what it comes down to.
**Laurent Quérel** 36:31 You said memory limit, and…
**jmacdonald** 36:33 Just… it's already there, it's already there. I just… that's where.
**Laurent Quérel** 36:37 Okay, okay.
**jmacdonald** 36:38 The priority, you know.
**Laurent Quérel** 36:40 Okay, okay.
Okay, so that's what I had in mind regarding the milestone.
So the next step,
Hopefully, maybe tomorrow, or beginning of next week, I will try to…
put some order into this long list. So, as you see, we have 72.
I'm sure that this will grow a little bit more.
**jmacdonald** 37:08 There are some of… some of those entries are super basic.
**Laurent Quérel** 37:12 Some of them are much more involved in terms of,
design and, and development, but I will try to put some, some order there.
First categorize the, the values, The various setup issues.
And try to figure out, what are the most important ones to implement first.
Determine the dependencies between those issues, and then come with a plan.
Discuss this plan with, with Joshua and, and, on my side with my team.
And, and…
**jmacdonald** 37:53 Another answer.
**Laurent Quérel** 37:55 Okay.
**jmacdonald** 37:56 Another answer to your question about this milestone is that the stuff that's important to me are the things that
I would say Ukarsh and I have already been focused on
you know, the syslog CEF receiver and the reliable AC back pressure retry stuff.
That's, like…
core functionality that we really want to get as right as fast as we can. But during this next milestone, I also have people that are not core contributing on that… in that sense, like the effort on KQL with Drew and Michael, and then… and then there's this fellow that hasn't
showed up yet, but I promise he is. His name, Aaron is going to be working with us, I hope, on Persistent Q, which is to fill a… sort of check another box that I don't expect to have this in, you know, mid-November, but I want us to see progress on both of those fronts, that we have KQL moving in the right direction.
And we have persistent queuing moving in that direction as well.
And that will leave us with more to talk about. Like, yesterday we talked about how there's… there's persistent queuing, like, I need storage, and there's also, like, scalable, load-balanced, persistent type of queuing, which is usually a multiple-tier system arrangement, and that's…
fairly different system design, one that I'm eager to hear about, look at, but it's not my expertise, and so I… I look to others.
In that space.
But this would be, like, group racing.
**Laurent Quérel** 39:27 So we're getting the persistent queuing, it's,
what this person, I did, don't remember the name,
is… we'll create some kind of local persistent…
**jmacdonald** 39:41 Yeah, that's what we're kind of looking at, is the use of an Arrow IPC log file, that would be effectively the OTAP stream format in a log file, that would let us…
**Laurent Quérel** 39:51 As opposed to a shared persistent queuing system like Kafka or similar approach. Okay.
**jmacdonald** 39:58 So we may still.
**Laurent Quérel** 39:59 We need both, in fact, yes. I think we need both.
**jmacdonald** 40:01 external load balancers often use, like, destination… like, data-aware routing strategies, and the Go Collector is called the…
load balancing exporter, I guess. It's Kubernetes Aware.
**Laurent Quérel** 40:15 And, and regarding, the… what you've shown us, with the… with the Akaton.
I think the… another approach, instead of having packet files stored into a file.
into a file system, sorry. Another approach could be to use, depending on the scenario, so if you are on the edge, using a local persistent queue as a way to store, Apache Arrow records.
But done in a way that are… they are queryable with data fusion, so the parent ID have to be,
To get the same kind of treatment that we have into the pocket file.
That will give us… so you could imagine that you have a partition per 10 minutes.
**jmacdonald** 41:08 And that will give you a way, a very easy way, to…
**Laurent Quérel** 41:12 To query a bucket of 10 minutes and do whatever you want in order to generate, the sampling
So that's… That would be a good option for HKZs.
for edge, user use cases. And,
And when you have to do this sampling for, let's say, a fleet of systems, and you have a
this collector, doing this sampling, then, most likely you need multiple instances of this,
Pipeline engine, a shared persistent queue will be the solution in that case.
Another one will be to use S3, as, or S3-compatible, object store.
and packet file, like you did.
**jmacdonald** 42:00 Yeah.
**Laurent Quérel** 42:01 Yeah, there are multiple options, but I definitely see the benefits of having those different kind of persistent queues into the mix.
**jmacdonald** 42:10 Yeah, often our… we have a lot of agents, and they're edge devices, as you said, and they're not necessarily part of a scalable pool, like you're imagining. So it's sort of a different, like, it's the… the…
client-adjacent agents that we're thinking about here. And, you know, I wouldn't want to have to wait to flush four Parquet files, or whatever, for my one log request. And…
there's a sense in which we could just forward it to the next destination and wait for the response, and that's good enough. But, you know, that's why the collector has this option to turn on persistent storage, and that's basically what we want.
As a, as a sort of check-the-box type of feature.
But this, this, queuing that, that I've described, and I… and I really
pushing out is very much aligned with the idea of temporal bucketing, like, trying to be correct about timestamps. And eventually, I know this is not a super common topic, but OpenTelemetry has not addressed how to handle late-arriving data.
And no one has in this industry, and we can. Like, it's ready for us. So, as far as conventions for saying, I did a 10-minute collection, this is, like, 90% of the data, but I know there's some late arrivers. I'm gonna send you more data later. That's what we… no one's done that, and we can, if we want.
**Laurent Quérel** 43:30 Yeah. Yeah, definitely, right, it's,
Definitely, like, definitively a super, Important aspect.
**jmacdonald** 43:42 I will… I can go update this milestone for… within.
**Laurent Quérel** 43:44 Yeah, okay, so, to be done, and, I will, do… Listening for voice.
So I think this, description of the focus will help us to
To determine what is, for me, the goal at the end will be to determine what is the real stretch goal.
from what is fundamental, which is the intersection between Microsoft and FIFO QC.
**jmacdonald** 44:16 Okay, that's the width, got it.
**Laurent Quérel** 44:19 Okay, so the next topic, I think, was, is there any, first, is there any feedback or question regarding the…
Regarding the next milestone.
Okay, so, let me see… where is this stuff?
Yeah, so I was, so, I'm working on two things,
So one is to make… what we observed during the…
The demos, and the previous milestone is definitively we
We don't necessarily have the right elements or the right systems to troubleshoot
When something bad happened into the pipeline,
It's hard to figure out exactly what is happening.
So now we have metrics, so that's… and I think they are working relatively well. We have some,
discussion regarding, how much metrics we need, blah blah blah. So, I will say that this is a more a refinement, but the mechanism is there.
And we need to extend it to be able to publish the result of those metrics.
you know, TLP, for example, in various things like that.
You want to say something, Joshua?
**jmacdonald** 45:48 Yeah, I have a question. This has brought me to a point that it was wedged in my head from the… the…
Hackathon. So… or from the ACNAC handling, and I… I feel like I have a…
A question about error handling in general.
That I haven't gotten the full picture of… of your vision, or the vision that we have.
And it's a… it's that there are channels that are, I believe, blocking by default. So anytime you send a message, or a node control message.
If you're not calling tri-send, it's gonna block you when that channel is full.
And yet we have, there's… there's so many places in the code where I am going to make a send message call, or a send… and so I have to handle this. I'm looking at code like, okay, send message. Was it a success? Good. Was it a failure? Now what?
Do I just return my failure to the controller, the pipeline controller, or do I begin…
Do I… so let's suppose I'm a processor.
retry processor. I have just received a message, I'm going to send it downstream.
But my send fails.
Because that… because that… because I don't know why. It's not because the channel's full, because that would block me. My send has failed.
am I obligated to now try and send a NAC to the caller? I'm holding this, like, this is the last chance for this data, because if I drop it, it's dropped forever.
Because I couldn't send it.
And now I'm going to try and send it back to the node control channel of my recipient, but that could fail too, and I… and I don't want to see handling like that at every call site.
Moreover.
**Laurent Quérel** 47:33 Yeah, yeah, yeah.
**jmacdonald** 47:33 metrics.
consistent for this type of situation. And if I do drop.
Then there's gonna be someone waiting for an ACK,
And that's why we have timeouts, I guess, but I'm not feeling comfortable with this sort of vision for consistent error handling, in this environment. And I wonder if we want helpers to, like.
always suppress an error by either dropping, counting, etc, doing the right thing gracefully, or whether I haven't thought about this correctly. I just raised… you raised that for me as you were talking, and I hope it wasn't too off-topic.
**Laurent Quérel** 48:05 Bless you.
Yeah, we need to, I think I see that as a two-phase, exercise.
or, approach.
First, we have to,
To look at the system, as a whole, and, and determine what are the…
The type of behavior we want to see into the system.
And I will come back on that later. And second, we, once we have this, cliente in the…
The design principle on how to behave when we want to send something, and what happens if
There is an error.
these kind of things. Then we have to refine a little bit the APIs or the values component.
to make them… as error-prone as possible, not error-prone.
You're all safe, sorry.
as error-safe as possible. So we guide people, basically, by the various developer of the various type of nodes by creating an API that basically prevents misuse.
When it's possible, and when we can't, because the logic is so complicated, that's translated that into
Some kind of, typeSafe API, then we will create a document to describe the best practice.
And we would add the necessary metrics slash events to capture the… those bad behaviors. So the… for me, the design principles, we…
So the first one, related to the channel will be back pressure.
So, it's, in my opinion, Most of the time.
We need to use send.
Except in some circumstances where Tricent
Could make more sense, because we could be in a situation where we have some kind of loop
And we called deadlock.
So it's mostly for the compo messages. That should not be the case, in my opinion, for PDATA.
So, that's why, ID, So, control messages…
They'll… the make it… the way that they are… Addressed and underd.
needs to be, embedded into the effect number.
In some way.
So this logic of retry, this logic of tricend, blah, blah, blah.
Yeah. It's invisible. That should be invisible. I like that. And then the P data, send message.
By the way, there is no try-send message. It's on purpose, because if…
If the… if the buffer, or the buffers, let's say the channels.
Behind that are full, we should block the node that he's trying to send, because otherwise the back pressure will not be in place.
**jmacdonald** 51:19 Right.
It has an option to not do back pressure, but it's, like, a bad setting to choose.
**Laurent Quérel** 51:28 Yeah, but that's, so… And what happened? You mean that you lost some.
**jmacdonald** 51:37 Yeah, well, when the queue is full, it will return a failure immediately, instead of waiting.
Like a fail-fast mode.
And it's… unfortunately, it's the original default, so it's current default as well.
You can turn on wait for result now, you can turn block on full now.
**Laurent Quérel** 51:54 Okay.
**jmacdonald** 51:55 Walk on full is the right way to go, though. It's not… it's not a good behavior, I think.
**Laurent Quérel** 51:59 Yeah, and if we want to enable this kind of, fast,
approach where data loss is authorized. Maybe we will have to define some kind of global policy that would be applied to the channel themselves, and those channels will behave differently.
Maybe that's, a way to under that. So…
**jmacdonald** 52:22 But it's not data loss, it's really just returning a failure.
**Laurent Quérel** 52:26 Thank you, yeah.
Okay, so we need to think about that. But I agree, default will be what we have today.
So the back pressure is one thing, the…
send first, and try send only in some very, very specific circumstances, and ideally hide this kind of complex logic. The other one is…
What happens when we have, on the same message, an error?
So, the reason why we could have a send message returning an error
Is when, for example, there is no longer any consumer for this public corresponding channel.
**jmacdonald** 53:06 Channel closed.
**Laurent Quérel** 53:07 And that's… Is typically… when we, when we, we stopped, we stop a channel.
Let's say, when we create a… sorry, when we create a pipeline, currently the system is starting from the exporters.
and moving… Moving back to the, to the receivers.
Following the DAG, the Global DAG Order.
**jmacdonald** 53:41 shouldn't.
**Laurent Quérel** 53:41 So that means that we open the connection, we don't send anything, because there is no… there is no channel connected, on this side. So we are sure that everything will be in place.
Once we connect the receivers, everything is ready to go.
But when we do the opposite… when we do a shutdown, we do the opposite direction. We start from the receivers.
And, so usually we should not see, a send message that failed, because we killed first the producer's side, or the sender side of the channel, and then, next iteration, we kill the next, the, the receiver side, and so on.
But it's entirely possible when we will support the live reconfiguration.
That, a specific node fail, And, or…
Not everybody in that case.
**jmacdonald** 54:43 Like, maybe a dynamic reconfiguration would cause something like that.
**Laurent Quérel** 54:47 Maybe, maybe the dynamic reconfiguration, some very bad situation, let's say the… I think we… what we should be able to achieve is, let's say the new configuration is invalid.
Or refused, rejected by the nerd.
We should be able to detect that.
Conserve the receiver part of the channel.
And put back again the previous version of the configuration, so the sender is never lost.
So, the worst case scenario, we feel the channel is full, because during this operation, we accumulate messages.
But we should not be in a situation where the receiver side is…
No longer existing, and then the channel failed when we send something on it.
Maybe there are some other situations where an error can happen, but right now, in my opinion, that should not happen.
And if that happens, we need to understand why.
But the reaction to that, in my opinion, right now is, okay, we report the error, and we are done with the corresponding node.
And then that means that that will propagate there for now.
And we'll make the entire pipeline in a mode that is not HC, not ready.
**jmacdonald** 56:11 Makes sense to me. We shouldn't see these errors, I agree.
**Laurent Quérel** 56:15 Yeah. But…
**jmacdonald** 56:17 Nevertheless, we have to handle them in the code, and I'm just worried about, sort of, repetition and, like, inconsistency.
**Laurent Quérel** 56:25 Yeah, yeah. I'm sure we will discover many, many issues there. That will be definitely a big part of the…
the next Maystone.
And
We… so Chris is there, but so with the benchmark infrastructure, the continuous benchmark infrastructure, we will also add some additional
Continuous test to…
That will not necessarily run for every commit, but let's say every day, where we will stress the system.
To, to the limit.
In order to discover this kind of, issues?
So we will automate, a maximum of that, and if you remember, Joshua,
We, we created,
a validation framework, when the… when we implemented the, OTAP on… in the Go Collector.
**jmacdonald** 57:20 Yes.
**Laurent Quérel** 57:20 I shown that yesterday to Michael. He was on his side already thinking about that, so I sent him the…
a document that, I wrote, that is part of the Go part of this project. So he will also think about, the type of infrastructure to validate that, OTLP to OTAP, OTAP to OTLP, blah blah blah.
Are valid, and also, resistant to… .
**jmacdonald** 57:52 reordering and things.
**Laurent Quérel** 57:53 bad actors that try to… to pervert the…
The stream in order to do some denial of services.
**jmacdonald** 58:02 Oh, I see. Yeah, we… in the version 1, we… we kind of, like, waved our hands at the risk of malicious data, because the receiver will gladly allocate large arrays right now if you give it data asking to. Is that kind of where you're talking about?
**Laurent Quérel** 58:16 That, and also when you try to…
poor, invalid UTF-8, strings, for example, or these kind of things. I saw a discussion yesterday between, Utkarch and… don't remember,
the other person, but, it was probably in a PR.
**jmacdonald** 58:39 Well, Albert had a SIMD UTF-8.
**Laurent Quérel** 58:41 Yeah, oh, that was… yes. So these kind of things, is… if we don't have a systematic way to validate that.
And that could be, and the validation process I'm mentioning.
Was, basically, we, we have,
A system producing data, we have a system that is under test.
And we have a control, exactly like in the benchmark infrastructure, except that, we can,
Change the binary representation of the messages that are sent to the system under test.
And we have a way to mark each message that our… Change?
And we expect to see a good behavior for the system under test, and we need to see, okay, the system has been able to handle this issue or not. And the result will be compared with what was expected, and that could be done automatically and randomly.
I need to grow, unfortunately.
**jmacdonald** 59:48 Yeah, it sounds good. All right, we've reached the end. Thank you all. I think we'll have more, more firm planning. I'll go update those milestones with our priorities. Thank you all for being here.
**Laurent Quérel** 59:58 Yep, bye.
**jmacdonald** 59:59 Happy Thursday.
