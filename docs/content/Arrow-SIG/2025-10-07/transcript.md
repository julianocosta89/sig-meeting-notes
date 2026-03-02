SIG: Arrow SIG
Date: 2025-10-07
Duration: 62 minutes
Zoom Recording URL: https://zoom.us/rec/share/fT18bV6n-fyeClwTiA5Zj3uQsyBUlf_N0Ojq1iOBa3WVdp_I9E1_IPUGOhkOgPo.d1v4Z88vRee6SjeS
============================================================

## Zoom Recording Transcript

albertlockett 00:00:48 Hello.
Danny Chin 00:00:49 Hi.
albertlockett 00:00:51 Hey, Danny, it's, it's nice to meet you.
Danny Chin 00:00:54 Nice to meet you.
albertlockett 00:01:12 Hey, Bill.
Danny Chin 00:01:17 So, you are Albert, or.
albertlockett 00:01:23 Yeah, that's me. Yeah, we'll just wait a few minutes for the rest of the folks to join. In the meantime, I'll put the,
the link to the meeting notes in the chat. Hey Josh.
jmacdonald 00:01:43 Whoa.
All right.
Danny Chin 00:01:47 Hi.
jmacdonald 00:01:48 If I can get my…
Here we are.
Hi, everybody. Let's see… eating notes… In the channel.
I thought the standard practice here is to go through, like, all the new issues, any PRs people want to discuss, and then, any agenda items that are posted.
Here's Laurent.
Laurent Quérel 00:02:16 Hi, guys.
jmacdonald 00:02:18 Hello?
Laurent Quérel 00:02:20 Hi, Denis, nice to meet you.
Danny Chin 00:02:22 Nice to meet you.
Laurent Quérel 00:02:24 That's really cool.
jmacdonald 00:02:26 So I, I, take it you're, you're new, welcome…
I will be glad to project these notes
And then, what do you say, Laurent? Would you be happy to, lead the meeting, or should I?
Laurent Quérel 00:02:45 Whatever you prefer.
jmacdonald 00:02:48 Glad to, glad to share the notes. I…
See, we have the correct dates.
Bring that up.
And so let's start with issue triage. I know I've filed a few, but we can go in, say, reverse order since the last time we discussed this stuff.
And, we have Otzel Arrow, we have… these issues…
Let's see… quite a few since last week. I'd say we could start at the back, things that we've discussed.
How would you like to, start us off?
Laurent, with this work that you began Filing issues about last week.
Laurent Quérel 00:03:54 So we, I was,
But it's something I didn't follow exactly what you said.
jmacdonald 00:04:00 So, starting with 1212,
It looks like you've added to a list of requirements for the next milestone for OTLP.
Laurent Quérel 00:04:09 Yep.
jmacdonald 00:04:10 When I'm seeing this new, maybe, compression configuration, keep alive, that's a tricky one.
And then these sort of standard components, I would almost advise us to stay away from these names, which are pitfalls of their own. You know, the use of sending queue is, like, such a legacy at this point that the actual type names in the Go Collector are
Quite different from that now, but they were once called… anyway.
Laurent Quérel 00:04:40 Yeah, I would be super happy to have your feedback on that. I'm not attached to this specific configuration. What I did is the following.
Inside the Fibre, Because, like, you know.
We are looking to create a minimal viable product, let's say a minimal viable data plane.
On what we are building, and targeting the end of this year.
And, I was looking at various internal projects.
Some of them are super simple, they are basically using very basic configuration for the Go Collector.
And they are leveraging this kind of configuration for the exporter. So I think what matters really there is the TLS support.
And I just copy-past without the specific values, but just putting some
what they add, whatever you think that we need to improve in terms of,
configuration representation, I'm all for it.
jmacdonald 00:05:37 routing.
Laurent Quérel 00:05:38 So feel free to add some additional comment there.
jmacdonald 00:05:42 Right, so…
Laurent Quérel 00:05:43 That's always tears.
jmacdonald 00:05:45 Great, so the idea here is that sending queue and retry on failure, those are, what I would call standard facilities in the Go Collector that I think we've argued
don't belong as, sort of, accessories on the exporter, but retry is its own component that we've got in flight.
Laurent Quérel 00:06:01 totally si.
jmacdonald 00:06:01 And then the sending queue is almost the whole design of the engine, but we will talk about persistent queue here.
Laurent Quérel 00:06:10 Okay, so we… that… to summarize, we will have Keep Alive and TLS, plus, obviously, the compression and endpoint, and that's it.
Okay.
jmacdonald 00:06:19 We can remove those, too. Thank you. Cool,
Retry on failure.
Cool.
Let's…
go forward, which is backward. We have basic filter processor, I think I know what that one's about. This maybe I could speak to for,
But thank you for writing it up. As some of us know, there's work in progress on a KQL language with some sort of minimal support that we can use for the OTAP pipeline. We've been developing that in the experimental repository.
Experimental path of the repository.
So great to see some sort of minimal… we have, column renaming and, what's typically called extend, when you add a column of, like, typically a constant-valued column. Those are sort of a small scope that we find to be quite useful for many users.
Laurent Quérel 00:07:29 So, Joshua, let me explain why I put that. That's the same reasoning from the other one.
Again, we have, in fact, the same internal team.
And, right now, their pipeline is super basic. The TLP receiver.
filter processor, batch processor, OTLP exporter.
So I just put… and it's, like, for me, the, the minimal
Example of an internal integration that we could try to achieve for the end of this year.
So, I know that the KQL processor will be the medium-long-term solution, much more advanced in capabilities. What I put there is, if we are not able to achieve the KQL
Because that will require a total integration with Data Fusion, plus a clear definition of the KQL
operators that will act on matrix, panel, and blah blah blah. Why not supporting a very basic filter processor just to secure
the milestone, the second milestone. So that's more for me, as… I see that as a way to secure a very basic solution based on Apache Arrow kernel functions.
Just supporting, something that is already supported in the filter, processor.
Just basic things, and then we can take whatever we need in terms of time for the KQL processor, and making it great and nice without shortcut.
jmacdonald 00:09:11 I agree. It should share most of the logic with…
Laurent Quérel 00:09:15 Yeah.
jmacdonald 00:09:15 attributes processor, that's typically how these go. In the Go collector, we have OTTL expressions that are, like, one way to do it, and then we have the basic, like, YAML structs, basically.
Laurent Quérel 00:09:28 Yeah. That was… that's the same reasoning we had with the attribute processor. At some point, the attribute processor and the filter processor could be replaced by the KQL processor.
jmacdonald 00:09:41 Alright, something here about, multi-pipeline deployment.
Laurent Quérel 00:09:48 Yeah, so the… this one is, we, we have, we have an…
We need to be able to, support, via an admin API,
a way to deploy multiple pipelines, or multiple DAG,
And ideally, we need to be able also to…
to isolate their deployment when a new pipeline slash DAG is deployed.
We need to make sure that it's isolated in a way that will not impact… okay, that will impact a little bit the performance, but that should not kill the other set of pipelines already running, so admission control and other things like that, and protection that we want to put in place.
the live reconfiguration is also, obviously, an additional… it's, it's not necessarily part of this,
GitHub issue, but it's related. It's the ability to support live reconfiguration on a pipeline that is already configured and deployed.
albertlockett 00:11:25 Oh, Josh, you're muted.
jmacdonald 00:11:28 That is terribly… Tragic. Okay,
Thank you for the issue of multiple pipelines, I understand. Thank you. I found one myself here about Rust confusion. I think we should put all of our versions and features in one place.
for the cargo settings. When I notice the sub crate…
TOML files having their own variations, it seems like the cargo builds take a long time.
Does anyone disagree with me?
Laurent Quérel 00:12:03 No, I think it's a good practice.
Cool. So the initial… let me maybe just explain the initial rationale and why I think what you are saying is even better.
So the… we have a workspace approach, for the OTAP data flow.
rice project.
So there is multiple crates.
And we have a common… a main cargo terminal file, and for each crate, part of this workspace, we have other cargo terminal
And what we did initially was every dependency that were shared into more than one crate will go and be declared into the maincargo.toml file.
And things that are very specific could stay in the corresponding crate. But that is very hard to maintain.
So, having a single place where we specify crates maybe makes more sense. So, they will go into the main
cargo.taml, and we just make reference, like, workspace equal true in all the other, dependent crates. As we do in most places.
jmacdonald 00:13:19 I'm just asking for permission to go clean up stuff like this, where what happens, as far as I understand, is that if you have this feature drive in one place, and you don't have this feature drive in the other place, then you're going to build it differently, and…
in… if you don't… whenever you set the, like, "-P argument to cargo, with or without derive, for example.
Anyway…
Laurent Quérel 00:13:41 Yeah, I think what Cargo is doing in that case is… like…
I'm not sure if I'm 100% sure, but I think it's… it's basically taking the…
All the features, like, merging all the features, and you end up with, the entire.
jmacdonald 00:14:00 Different unions.
Laurent Quérel 00:14:01 to the corresponding features. It's not compiled multiple times, it's, it's only one time.
Bye.
jmacdonald 00:14:07 Well, anyway…
Laurent Quérel 00:14:08 Yeah.
jmacdonald 00:14:09 As a matter of hygiene, I would like to do that, and we can.
Laurent Quérel 00:14:12 I think I saw multiple big ORAS projects doing the same approach, so I think it's okay.
jmacdonald 00:14:20 All right, back to the listing. Does anyone… does anyone want to interject at this point? We have a
I think we could…
rush through these a little bit. So we've talked about, up to… it's only one page. Is the map type being used correctly when, producing batch arrow records? Utkarsh, are you able to…
Describe this one.
utpilla 00:14:48 Yeah. So, I was working on…
something similar, like, on something, some related file in one of the PRs, and I noticed this, that…
This seemed odd, because we were… if you look at line 126 and 128 here, we were writing the same thing twice, which, didn't feel like would make sense.
Then I also checked
arrow, docs, which said that a map should ideally be a struct with key and value, list of structs, and the struct has a key and value. So, I think, yeah, this issue is mainly just to fix the…
Way we are dealing with maps, when… Writing schemas.
albertlockett 00:15:33 I take… I take full responsibility for this. And I didn't even vibe code it, I wrote that out by hand, so it's more lamentable. But, one thing I will say is that our new, our new,
invited person to the… to the meeting, Danny, has a PR for this.
jmacdonald 00:15:54 Yeah!
albertlockett 00:15:55 So, what did you do?
jmacdonald 00:15:57 There it is.
Danny Chin 00:15:58 So, so actually, I have a question. I have a small concern about that. I… I… I didn't really… I don't really know…
whether the schema ID is going to be used anywhere, like, outside of this component.
Like, I was thinking if it's going to be used, like, across… across this Ross.
Repository, maybe we need to have a standard for that.
Hmm, but I don't know.
Or it's just an internal implementation?
Good thing.
albertlockett 00:16:30 So I think it's okay to change the, the implementation like we're doing.
how these schema IDs actually get used is, part of the Omatology Arrow protocol is that
for every type of payload, so for logs, for traces, for, for log attributes, say, we have, an Arrow IPC stream that we're receiving, and anytime that we need to change the schema, let's say because, like, a dictionary overflowed, or,
or we have an optional field that's now included in the arrow batch, we… the schema will change, and so when the schema ID changes, this is a signal for us to
to… to create a new IPC reader.
Danny Chin 00:17:21 But we.
albertlockett 00:17:22 I always compute the schema from the…
from the IPC stream that we receive. So, like, that IPC stream to schema ID logic is always internal to.
process, and so… so I think it's okay for us to change… to make this change in this case.
Danny Chin 00:17:43 I got it.
Got it. Thank you.
And thanks, thanks all for… for the review. I will check later.
So, Albert, regarding that.
Laurent Quérel 00:17:57 We just need to make sure that if we align
If we have a GoCollector with the OTAP exporter enabled, and an OTAP receiver on the REST implementation, they need to be able to talk together.
albertlockett 00:18:14 Is the schema ID sent as part of the…
Laurent Quérel 00:18:17 the schema ID, I think, is sent to… to identify…
At least at some point, he was. I don't remember exactly where we end up, but the schema ID was used in the stream to identify the stream, if I remember well.
Danny Chin 00:18:34 But if it's the same stream, it means it's continuing talking to the…
this OTAP ROS component instead of, like, switching to others, probably.
albertlockett 00:18:50 Yeah, I don't know.
Danny Chin 00:18:52 Well, he switched… switched to other…
collectors and, I don't know.
Laurent Quérel 00:19:01 I'm just trying to…
albertlockett 00:19:03 What IDE is the string you right now? I thought it was just the.
Laurent Quérel 00:19:07 Yeah, I think it's communicated, but I don't… I don't think it will be a big deal, because the…
So, we have, let's imagine we have, two directions possible. The Go Collector…
The co-exporter is the Rust receiver, and the opposite.
the Go Exporter… When we have a schema update.
this side, we create a new schema ID that will identify precisely the OTAP stream.
And on this side, we… the Rust receiver… oh, we have a new, a new stream, so that we will update the state here.
If it's two different IDs, the ID needs to be different. The meaning, in fact, they are not necessarily sharing the same meaning.
So I think we will just update properly the state on the receiver side.
I think it's okay, end up with the two seminar IDs.
Danny Chin 00:20:12 Okay.
Laurent Quérel 00:20:12 Or two things, two different things that will be… that will… that will work.
Danny Chin 00:20:19 Okay.
albertlockett 00:20:19 I think it's okay, Laurent. As long as the… like, as long as when the schema changes, we produce a new ID, it's not, like, completely necessary that they're… we'd like them to be, like, the same, but it… I don't think it, like, breaks anything if they're not exactly the same between Go and Rust.
Danny Chin 00:20:37 Okay, thanks.
jmacdonald 00:20:43 Got it. Cool.
Thank you.
good to have guests here. We didn't really do introductions, just sort of a regular crowd here. Would anyone like to say why they're here, interested in Hotel Aero?
Bill Zuo 00:20:59 Hey, yeah, hi. Hi, guys, son.
My name is Bill, and, you know, that's, I am the, actually, a startup, co-founder, you know, that's, working with some, like, big data, especially recently, trying to investigate, open telemetry.
Because, my startup is Q&2 is just collecting runtime
data for data analytics. It's like a… it's a…
It's a different platform than monitoring, but, you know, we are using very similar technology, just so you know that.
as OpenTelemetry, but, recently we are trying to,
migrate, instead of recreate the tool from scratch, migrating to OpenTelemetry, but data size is massive, you know, comparing to the basic logging and matrix.
So, at least looking at those other solutions, I see finding this error possibly very promising in our case, because we are focusing on data analytics, and it's very natural to use some, like, protocol as Arrow to do this.
you know, I just said, I'm still just a newbie and learning, you know, look forward to join the discussion. I just, you know, that's trying to listen to you guys, listen to the discussions, you know, that's what I'm trying to learn.
You know, before I start, my current startup called Sock Probe, I was the CTO of a NASDAQ company, which has, you know, about,
I feel… I had an engineering team of about 700 engineers there, and building some, like, you know…
Platforms start processing hundreds of millions of, orders.
the day, you know, that's, yeah, we had a lot of operations, we need to do a lot for data mining, but, you know, that data collection becomes the bottleneck. That's why we have this idea, use, OpenTelemetry for data collection, you know, that's it.
Laurent Quérel 00:23:08 Okay, super interesting. Thank you, welcome.
I just want to align with what we are trying to achieve.
Bill Zuo 00:23:15 Yeah, yeah, so that's, I think that's, you know, right now, we personally, we did some, like, monitoring based on, like, a sampling, you know, that's already some data. But, yeah, there are some other many use cases, not just for monitoring,
Application performance, actually, many… I find many business use cases, depending on just, like, data collection, and right now.
you know, I think the industry mostly rely on, you know.
human-written code, you know, that's an… every time the data analytics needs some data, they ask developers, hey, at this,
data, log that into some data files, and then build data pipelines, a very manual.
Yeah, trying to optimize and speed up, you know, that's a typical… that's, like, a data analytic project can take anywhere from a few weeks to a few months.
Yeah, if we can let the… you know, that's our data analytics is.
To help themselves to collecting some…
runtime data from the applications via OpenTermetry, that will be all awesome, you know.
Danny Chin 00:24:29 Thank you.
And for me, I am, like, doing research at CMU, and I'm a master's student.
And I'm working with, two professors, and one… one is from, like, more system…
system, and another is, like, a generative model. So we are trying to… we mainly focus in… focus on traces.
So we want to use generative model to… to… to compress.
Those traces sent by the… Sent by the backend.
And then reconstruct it in the… Telemetry… Back inside.
But it was quite challenging, and I… when I found that you guys use a row.
And I think it's quite… it was quite inspiring, because it's called them.
And, like, I… yeah, like, point gathering, like.
More data you can use it to achieve higher compression rates.
So that's why I'm, like…
interesting. I'm interested in the… what you're working on. Yeah, and I want to learn more.
Laurent Quérel 00:25:51 Very cool.
Danny Chin 00:25:52 No.
Laurent Quérel 00:25:54 Yeah. Did you, I just discovered that yesterday, and that could be complementary with the…
Our own approach, where we try to…
To represent the information in a different way that will be more…
will be better to achieve better compression rates, so that's the old story about,
going from a row-oriented database to a columnar-oriented database, so all the analytical databases, at least the modern ones, are using that, because there are many benefits from the compression rates to data processing speed, the data locality, and so on.
But in complement, to that, did you see the last announcement from Facebook with the OpenZL?
New compression algorithms.
Danny Chin 00:26:45 Oh yeah, I saw that.
I haven't looked very, very deep into that, but I think they say they can automatically analyze the structure.
And, like, use the best compression for every column, but I don't know, I haven't…
Laurent Quérel 00:27:04 Yeah, that's.
Danny Chin 00:27:05 I haven't looked into that.
Laurent Quérel 00:27:06 That's definitively, I think, very interesting for us, because…
Danny Chin 00:27:09 brilliant.
Laurent Quérel 00:27:10 Yo.
Danny Chin 00:27:10 Okay.
Laurent Quérel 00:27:11 that doesn't change anything in our approach, because it's still a generic compression algorithm. It looks, like, super fast.
Danny Chin 00:27:20 And more efficient in terms of completion, so that would be nice to have.
Laurent Quérel 00:27:24 Some kind of analysis.
What we could do, if you are interested by looking at that, that is not directly related to your more innovative approach with generative AI and so on, but at least having a point of comparison between
We have, for same batch of information, an OTMP representation and an OTAP representation.
Danny Chin 00:27:51 And for each of them, we use the STD.
Laurent Quérel 00:27:54 to compress
the information, and then we compress also with OpenZL, and we see the benefits. That will be nice to inform the people working on this project if we need to put some effort to integrate OpenZL natively.
And get much more… I mean, faster and more… faster compression, and better compression rate.
Danny Chin 00:28:21 So, I want to ask a question. So, right now, the ZSTD compression is…
down at, what level? It's down at, like, a row, a row level?
Laurent Quérel 00:28:32 We have to level,
Yeah, we have two levels that could be enabled independently or all together. And in fact, when we work initially on the Go implementation with Joshua.
We observed that, depending on the nature of the workload, sometimes it's better to compress at the gRPC level, so basically.
Danny Chin 00:28:56 Hmm.
Laurent Quérel 00:28:56 entire message, envelope, plus the values, Apache RO, IPC, object, or to compress
at the ROIPC level. And sometimes the two all together will give us a slightly better result, but with more processing.
So…
And recently, we had an issue, and Albert fixed it. It was with another protocol, and where we were not as good as OTLP, that was very surprising, because usually we are always better.
It was because it was the compression applied to the IPC level and not at the connection level, the gRPC connection level, and by enabling the gRPC
Compression level, we get back, we move, we move back to the, to the better result.
So, maybe one conclusion behind that is we could imagine that, depend… we do some analysis, and dynamically we select, what is the best,
scenario or configuration, based on the workload. So this dynamic, selection of where to compress.
could be also part of the protocol. We didn't explore this part, but that could be something for the future.
Danny Chin 00:30:29 Right, that's cool. I… yeah, after digging more into that, I think I have a lot to ask you guys. I will add.
Thank you so much.
For the input.
jmacdonald 00:30:45 I was part of the work, of that work. I remember with the data that we were running through OTL Arrow back then, that we would see
Something like 3-7% improvement.
of the, sort of, from the baseline, which was just… just Aero IPC or just gRPC, but both levels of compression seemed to not cost very much, and seemed to produce substantial savings.
in those ranges, like, it was worth doing. So, that's why we have both of those levels. There's also this weird side note about,
how you set Z standard levels, which is a little tricky to do in a Go server, and so, like, maybe we can redesign that, but the way that system worked, at least sort of worked.
Danny Chin 00:31:32 This is sweet.
jmacdonald 00:31:32 noticed was to have 9 different compression level codecs.
Danny Chin 00:31:36 Registered.
jmacdonald 00:31:37 RPC. That seems like it was a mistake, just so you know.
elaborate that much.
Laurent Quérel 00:31:43 That reminds me something else, in the same area, I think that would… where we basically had no time to spend there, but because you are doing some research, that will be great, in my opinion.
So it's, it's true for, ZSTD, and, and more, even more important for the open, ZL, the new one.
But for ZTD, you have a mode where you can train, the, the compressor.
To create, like, an internal dictionary.
I will name that tokens, but it's not… I don't think it's the terminology that they are using, but… So basically, a dictionary that will be used and communicated, to the… to the ex… to the decompressor.
And because we have a stateful, protocol, we could imagine that we, we liberate.
Danny Chin 00:32:41 Oh, sorry.
Laurent Quérel 00:32:41 approach from the DCD compressor. Right now, what we do is leveraging the standard dictionary for the.
Danny Chin 00:32:52 Appreciate it.
Laurent Quérel 00:32:53 compression, which is based on, probably Facebook did a lot of, analysis on many, many datas and decided.
Danny Chin 00:33:01 Okay.
Laurent Quérel 00:33:01 That's the…
it looks like this dictionary is working well with most of the data, and it's okay. But there are ways to optimize for a specific workload. And that's what the OpenZL is doing dynamically for everything, by default.
Danny Chin 00:33:19 Yeah, that could be also something interesting to investigate.
But it needs a, like, stateful protocol to achieve it, because you need to… Send it.
Laurent Quérel 00:33:31 Yeah, but we already have a stateful protocol. The OTAP protocol is, in fact, stateful.
So we can learn… at the beginning, we could imagine that first messages, we just send them with the standard… Dictionary. Dictionary,
And then we, in the background, we do some analysis, we trend, and with the deadly CD algorithm, we get a new dictionary that is more optimized. We send it
And, and then we, we inform the decompressor what to use.
Danny Chin 00:34:09 Hmm.
Laurent Quérel 00:34:10 That would work.
At least at the IPC level, because we have the full, we have the full,
I mean, control on it. For the gRPC level, that's another story.
Danny Chin 00:34:26 okay.
That's cool.
I'll look into that. Thank you so much.
jmacdonald 00:34:37 I have wild tangents I could throw out there, but I'm not going to.
Fantastic.
Compression is an amazing topic that keeps evolving so much.
Danny Chin 00:34:50 Yeah.
jmacdonald 00:34:51 more about OpenVL.
Yeah, like, every decade, you have to learn it again. Cool. So I know there were a few more issues, and there's still some time, so we're back in the issue list.
I had a little, point of…
conversation here about this one that I already wrote up.
I have strong feelings about how we handle UTF-8 in these collector pipelines. I have seen more than once, more than twice, a sort of invalid UTF-8 completely follow a pipeline. If the service is not careful handling it, it's very easy to lose a whole request.
And then to have a very hard time debugging it, especially in production.
When this happens.
So, Albert and I were chatting. This is what I have to say. Any thoughts and feelings for the group?
albertlockett 00:35:48 Josh, maybe…
would it be helpful to just give a summary of where we landed? Because, like, where we were…
Originally was…
the… the impetus of this issue is that when we receive an invalid UTF-8 token for, like, one field.
the bug is that we're basically throwing away the… the record batch, and producing an error, and so the, like, we were trying to figure out how we handle this, and I think, like, there was some discussion on the original
implementation of the optimization for handling UTF-8 encoding, which was, like, do we insert the, like, the placeholder character and handle it gracefully?
Or do we say, we're not going to do UTF-8 validation at all, and push that, upstream? And I'll admit that I didn't realize you had commented on this, so I didn't read it, so…
jmacdonald 00:36:44 No, it's okay.
albertlockett 00:36:45 What are we gonna do?
jmacdonald 00:36:47 Yeah. I mostly just wanted to record some sort of deep… there's deep knowledge and conversation if you click through all these links. I think for the user, it's best to do what you just said, so not failing the whole batch is great.
If what you're saying is we have the ability to, like, row by row drop, records from a batch, that sounds good.
it's fine, especially if you have, like, an observability solution for the pipeline operator. Like, when the bad UTF-8 comes in, what do you do?
If it's, like, dropping it.
So… What do you do about it next? It's hard to… it's hard to do anything when you can't print it, I know that much.
albertlockett 00:37:34 Yeah, I think our tentative plan was not to drop it, but, like, so what we're doing is we're just, like, we're taking the bytes directly from Proto, and then as we're converting it to OTAP, when we create the string array, that's when we do the validation.
And so our tentative plan was to, instead of just saying, oh, it's not valid UT8, throw the batch away, to use, from UTF-8 lossy, which can put in the
the question mark… character.
And, so that… that was, like, our tentative plan, so it would be to replace the UTF-8… the invalid UTF-8 sequences with a… with a placeholder. Or at least that was our… that was our tentative plan. So…
But I think what you're calling out here is that For a straight… For a straight pass-through pipeline.
the… we wouldn't have that behavior, because we never convert to OTAP. So, is it better to just…
to do no UTFA validation and always have…
Just so we always have the same behavior.
I think that's what you're getting at, and maybe, maybe that's what we want to do. I mean, I'm fine with that if no one has any suggestions. I see Laurent looks angry about it.
Laurent Quérel 00:39:01 I'm not hungry, I'm thinking about the values option and problems.
albertlockett 00:39:05 Browning or deep in thought?
jmacdonald 00:39:09 Yeah.
Laurent Quérel 00:39:10 It looks like when I'm sinking, I look angry, but that's not the case.
jmacdonald 00:39:15 For even more context now that we're here, somewhere I had…
up earlier, where I made my tangent the first time, is that
I was suffering from this issue, like, the nth time I had to debug a bad SDK causing my pipeline to follow up.
And I tried to write something down about it. It is in this old document that never went anywhere, so it's not merged anywhere, but it basically says all the nuance that Albert just laid out, which is that, like, you can drop it, you can modify it, you can pass it through without checking, or you can be strict about it.
In my old company, we had to create a processor that we called… I called Sanity Processor. Basically just said, like, I… I need to be sure that this is UTF-8 clean, because I'm going to pass it to somebody else, and, like, they're not… they're not able to handle it when I give them invalid UTF-8, so I have to check it. That can be an optional processor, for example.
Laurent Quérel 00:40:09 So… I see multiple things, the… So we could have,
client SDKs that are buggy and sending invalid UTF-8 characters. We could also have people that intentionally
are sending us, invalid UTF8.
For those peoples.
We don't want them to be able to kill, basically, a pipeline just because we have a merge procedure, like a batch processing, and we are merging things that are valid and things that are not, and then, that will destroy some,
stages, could be processors, could be exporters, could be backend, that expect a full ETF8. So we need to be able to support, in my opinion, some protection. But at the same time, we want something that is very performant, so we have to figure out a good trade-off there.
Because if we… if we,
And I think the reaction to that…
We replace… we get rid of the entries that are invalid, or we…
message a little bit the invalid entries, to make them, ETF… ETF-8 compatible, even if we put some placeholders.
jmacdonald 00:41:36 Maybe that's a configurable policy.
Laurent Quérel 00:41:40 Some people will prefer the first one, or the second one. So,
Right now, if, the performance
Let's say, if supporting one of the, these two policies
could be done and achieved with the same level of performance, I would prefer something that is flexible and where we can express a policy.
If it's not the case.
then I will say that it's better to select the option that will be the fastest first, and then use sometimes to figure out what could be… how that could be done for the second option.
But propagating errors outside, I will say that,
That will cause us problems. Except in the very, very, very small
A situation where we have a… where we act as pass-through, because we don't decode the message.
But otherwise, I will expect many libraries in Rust to…
work to… to be able only to work on valid UTF-8 information when we are talking about strings. So anyway, we will have to make sure that there are… for example, data fusion, and you are using some kind of operators acting on strings.
I think they will expect to get, valid UTF-8, strings anyway.
So, long, long answer, but I think,
checking if we can have a configurable policy for that, and see if we can achieve that with good performance. If yes, that's great. If no, then we select the
the most performant approach first, and we see how we can implement the other ones. At least that will be my advice.
albertlockett 00:43:40 I agree with that. Ukarsh, did you have a comment?
utpilla 00:43:44 Yeah, so, for the performance part, I think…
the string from UTF8 and string from UTF8 loss ED.
Only difference…
Or, like, the only performance implication would be… would be when you actually encounter a byte slice which has an invalid UTF. If it's valid UTF, both methods
Don't allocate and would return you a string slice.
So… and since we don't expect this to be a common case, most likely, we should be able to just use a string from UTF-8 lossy without seeing any perf hit. But the problem I see is, like, we are trying to use SIMD UTF-8 crate.
Which does not have a from lossy method.
And I checked their repo, somebody has created an issue already that they should…
Add a method for, like,
SIMD UTF, SIMD way of, doing a lossy conversion.
which they don't have it, so, like, if you're just using standard library, I think we won't see much difference in Perf, but maybe, yeah, with the SMD one, unless they offer something like… something…
For the lossy conversion, we probably wouldn't be…
We'll have to see what's the perf diff, I think, only after running it.
Laurent Quérel 00:45:00 Okay.
jmacdonald 00:45:02 It sounds like you could do a SIMD UTF8 validation to check for the problem, and then use the slow path.
utpilla 00:45:09 Then fall back to lossy, yeah? Yeah.
jmacdonald 00:45:12 I didn't want to make a big deal out of this, I just, since some work on UTF8 came through, I'm glad we talked about it, and I'm super glad to hear, Albert, that you fixed the glaring thing, which is when you dumped the whole batch, which I've seen. Cool. I also put in,
once in a while, we talk about the sort of back pressure mechanism that's under development, and how OTLP
has specified this thing called partial success.
partial success is a response in all of the OTLP export methods that is, several years old and lets the server respond with a sort of qualified success code. And there's two fields. One's a message string, it's sort of freeform, and then there's a count.
For the number, rejected.
This is an example of a case where you can use the partial success to say, hey, I took your data, most of it was valid, one field turned out to have an invalid UTF-8, and I fixed it, or I scrubbed that one field.
And then you pass that backward, and it may end up going into a batch, which gets safely, you know, handled. And everybody might see that batch's error to say, like, hey, somebody put a batch together with a field that I can't take, and I dropped one item. That's the message.
That… the count is 1. That's… that's an example of how we can use partial success.
The reason I mention it is it's under development right now in the collectors, so many years later, and I put some comments there about how I expect it to hand… to be handled in cases where,
it's ambiguous. Like, if you're in a batch, what's the rejected count, like, for the upstream host?
no way of really knowing. Zero is good enough for me, as long as I get a string back. Mostly it's about making sure that, usually there's more than one party in these observability systems, the one operating the collector or the gateway.
has minimum communication with the other teams. The teams that are the ones configuring bogus SDKs with invalid UTF-8, they're the ones who need to know about it, so we need to pass that message back to them.
So that the person with the control can actually act on the information.
That's,
For the future, right now, we don't have anything like that in the ACT message, NAC message delivery that we're working on, but it's something I would reserve for the ACT message. Like, this is a success with a comment.
Other reasons are typically, like, metric data model violations. You tried to report a counter where there was a gauge before.
My old company didn't like spans with empty names. That was one example as well.
Any comments.
Laurent Quérel 00:48:02 Makes sense for me.
jmacdonald 00:48:06 Let's see, cool, let's keep going, this is great. We haven't done a full issue roundup for a while. So,
This was more on the same, I take it as before, robust multi-pipeline deployment and split engine settings from pipeline configurations?
Laurent Quérel 00:48:22 Yeah, so nothing special there, but right now, when we start the… the,
The pipeline engine, we provide the pipeline configuration.
But, because we want to support multiple pipeline configurations that could run on the same engine, we need to separate the engine settings, the general settings that are independent of the pipelines, and then we could have some…
pipeline settings that could override the engine settings.
Or it could be specific to the engine parts.
So that's just basic, basically about that.
jmacdonald 00:49:01 Gotcha. So, stuff like health endpoints, those are shared across the host, so even if it's multi-CPU, yeah.
Laurent Quérel 00:49:08 And I thought about that when I was, thinking about the…
The liveness and readiness endpoint, and
And the policies, let's say, what quorum do we expect to detect something, like, live or ready?
Do we expect a full quorum of all the pipeline
per core, to be running, or do we accept 70% of them? So this kind of, policies belong to the engine policy.
by default.
jmacdonald 00:49:46 Gotcha
That sounds great. And so today's DF… there's a command line built called DF Engine, it's one CPU. What I hear what you're saying is that we're going to get soon to a place where you run DFEngine with a
Maybe a different configuration that starts.
Laurent Quérel 00:50:07 Yeah, so the DFNG is already… so the main limitation today…
Is you can only provide one pipeline configuration, but what you can do is describing on how much core you want to deploy it.
And you can also specify a range of core ID. So that's used, for example, by the benchmark infrastructure, because when we deploy on a server with multiple CPU and we want to isolate
the simulator, from the system under test, from the system capturing the performance. They are all running on the independent cores.
And, in fact, they are using the same binary with different configuration for the pipeline, and different range of CPU. So that is already supported. Multiple pipelines on the same engine is not yet supported properly.
jmacdonald 00:51:00 Got it.
Alright, thank you for clarifying, I understand.
There was an issue that didn't, look like it was real. So, I added one earlier today about, test coverage flakiness. Drew has added some toleration for slight variations in coverage, but
I'm still noticing some pretty big swings in some of the areas of code. So, I found this one just to sort of… sort of
make a, example. This is one where
Apparently, coverage jumps up and down 20 or 30%. I just… we filed it, we don't have to do it, but we filed it.
we seem to continue to get coverage violations. One of the reasons I noticed it is that we have this concept of a shared and local receiver, exporter processor, so that's 6 different categories, and if you don't have coverage
If you're… if you're implementing a feature that's, like, an effect handler-based.
method. You're gonna go through one of those six methods.
It's 4 of one type and 4 of the other type.
And if you don't cover them all, you're gonna have bad coverage. So, not sure what I think of as ideal for coverage. I think it's probably a waste of time to go to 100%.
Right now, we're hovering around 80%.
if one file is wobbling around too much, it's not great. That's all I had to say.
Laurent Quérel 00:52:30 Yeah.
I expect, because we are trying to build a first, production-ready version.
For the next milestone, I expect to see more Discoverage, anyway.
Because we will probably observe issues, and we will try to… to,
Detect them with tests and fixing the problem.
But, yeah, I agree. There are probably some design decisions that make the…
Test coverage, hard to maintain.
jmacdonald 00:53:05 We will keep improving.
Here we have one, I put up this morning, or earlier today, in response to your code review feedback on my, ACNAC PR. So this is, encoding that… the idea that.
we can return the sort of data shell, the P data, which includes context, but also this sort of, like.
container for some data with an empty… with the container being empty, and that's going to be the default. So having an interest called return data is what this is about, and I have already opened a PR about that.
It was fairly straightforward. So that's to show, at the moment when you first notify of an ACC or NAC, if there's still data, you will take it out.
And that's fairly straightforward.
The other issue that I filed on the way to, today,
was somewhat related. It was coming out of the same PR. Laurent, you sort of… actually, Albert, you mentioned something about the delay data mechanism, which is now merged as well. This gives you a way to say, I'm going to continue this data… this data will resume in a second.
The point is that we don't have allocation tracking at any level yet, and so once…
Up until now, all the data was somewhere. It was in a pipeline or actively being held by an async thread that we weren't spawning.
many of. So, once you have the ability to put this delayed data struct, now this thing can hold as much memory as there is, and that's a problem.
I do have a number of work streams that I have
picked up and paused over the last 9 months on this topic. I put links to some of them here.
I also…
opened a PR to sort of start actually just finishing the back pressure mechanism that we… that we want, step by step. So, the… I don't want to click into my links 12603 was, like, a long series of drafts in the Go Collector world.
Started here in 95, 91.
The, the, the… PR that I opened just to get us started.
what I found when I looked at the Go Collector land is that there's lots of variation in limiter designs.
One, you have this notion of time-based limits versus count-based limits, where the count goes up and down.
And so then you also have…
sort of extra dimensions often added by users who want to have, like, different tenants, or different, usernames, or different hosts, and different treatment by some variation in the space of attribute values, maybe. And then you have,
the fact that there's metadata, sorry, middleware, which is, like, gRPC-specific stuff, maybe, happening before you even have a record.
But you know there's a request starting. Can you start limiting requests there? You know, versus the number of items, which might require parsing a little bit of the data before you can count.
Versus looking at the bytes themselves, which is often how we want to measure.
whether they're on the network compressed or whether they're uncompressed. So that's what these documents here share, is that we found, like, four primary weights. We found both middleware implementations as well as non-middleware implementations. It's complicated.
But we gotta start somewhere. In my end-to-end prototype for Acnec last week, I shared, an OTLP receiver.
like, proof of concept, and this would be our first receiver that responds to ACNAC, essentially. Most of the weight of that code that… that changed was in this piece I extracted here.
It could get us talking about limits. In order to correlate the RPC, the unary RPC request coming in, and the information I need to act it or NAC it.
I'm gonna build a table.
Of, slots. And these slots can hold a channel of some type.
And I'm gonna… it'll grow automatically up to its maximum.
It will either…
Store a slot number, or either it will give you a slot number and a generation count.
or it will free that value and leave it available in a free list. So what this does is allow you to build call data. Call data now is our new type.
Can show you what it looks like.
Call data is…
two U8s, two 8-byte U8s, so 64 bits, two values that are 64 bits max.
This data structure will let you build a slot
a generic slot mechanism that stores some number of those items and tracks generation numbers so that these tokens can be put into context, passed through a pipeline, and then when it returns in an AC or NAC, you can look it up and do something with a channel.
So…
this is how I would go about both of the OTLP and the OTAP receivers. I would create one of these…
slot… states…
which is general by U data. It has a vector of slots, a vector… a list of free slots, and it has some configuration.
if this would be used to limit requests. Like, I can't have more than a thousand concurrent requests in the OTLP receiver, because this structure is configured with a max slots of a thousand. It won't use all that eagerly, but it will use that much, and it won't free it. So…
Any reactions? We're basically out of time, and this would be my idea for how to implement receivers that also implies a limit.
Giving me quizzes.
Laurent Quérel 00:59:30 Yeah, I think the… an important aspect that you mentioned at the beginning of this conversation
That I want to make sure that, everyone is fully aware
So, today, we have… we know, at any point of time, we know how much pipelines are running, we know the composition of those pipelines, they are composed of
Multiple nodes.
a minimum two, receiver-exporter, and in between, we have channels. All of those… all the channels in our system, there is no exception. They are all, defined with a maximum capacity.
So, the amount of memory that is consumed by this system is directly related to the number of pipeline deployed, number of nodes, but more importantly, number of
Buffers, channels, that are part of this system.
The only, right now, the main state that is used by a node is the batch processor, otherwise, usually, most of them are just stateless. So, obviously, a node like the batch processor needs to be into… need to be,
At least participate to the memory footprint.
But the main one are the channels. If we introduce now a mechanism to delay the processing of a message, we basically indirectly introduce
a new… unbounded channel, which doesn't follow the rule that we initially decided, and that's what worried me.
So we need a header to find a way to make this Unbonded thing bonded?
Or to have an admission controller that is good enough to make sure that we don't authorize any incoming messages into the system, otherwise we will end up with memory… out-of-memory issues, and an easy way to destroy the system.
jmacdonald 01:01:43 Yep. So…
Laurent Quérel 01:01:44 Just delaying something introduced, in fact, indirectly a buffer.
Which is not necessarily a good idea, in my opinion. Or at least we have to do it in a good way. I need to think about the pro… I need to come back with some proposal. Right now, I don't have a good solution.
jmacdonald 01:02:04 Sounds good. Yeah, you know, the retry processor also in its current state, which.
Laurent Quérel 01:02:08 We've talked about replacing with a more stateless variation, but…
jmacdonald 01:02:12 It currently has some configured number of slots in a different type of structure. We could imagine…
You know, just giving the… the…
queue a lim… the delay size a limit, like, how many… how many requests can be delayed? But, I would prefer to… to… to get us a real admission controller, and we should both think about it. We should all think about it.
Laurent Quérel 01:02:37 Yes.
jmacdonald 01:02:38 Sweet.
Well, I know we've come to the end of an hour. That was a lively conversation. Thank you all. I think we've… we've done it, done it again. I'll see you next time. Thank you all, especially to the new guests. Thanks. Yes, thank you. Cheers.
Bill Zuo 01:02:54 Thank you.
