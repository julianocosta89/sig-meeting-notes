SIG: Arrow SIG
Date: 2025-08-21
Duration: 80 minutes
Zoom Recording URL: https://zoom.us/rec/share/SPcJzF4bF8rXCaSjNzVVeJcjHNzB0H12tuBUO2AUGkbkXkFU4OhDMwR54KPX0_W3.1u3XXoiVP2UIuATS
============================================================

## Zoom Recording Transcript

albertlockett 00:00:13 Yes.
Tristan Sloughter 00:00:17 Nope.
Laurent Quérel 00:00:34 Hallelujah.
Yeah, so I think we will wait, 2 minutes for the others to join.
In between, I will, prepare the… the Google Doc for people that… Load up the Google Doc, I will copy-past.
the… Link into the chat.
Then created… A new entry into the document.
Alright… 21 August down… I see Jake… I don't know for the other, so you can add your name.
If you want, into the, attendees.
Section.
And, … In the agenda, … I see that we have, … The pleasure to see people from, … It's so-ish.
Disturbed by something else.
Oh, weird.
Okay, back. So, we have the pleasure to see people from a hotel, so I guess we could, … spend some time on that, so I will, … The hotel as a subject.
We also have this new, … Instrumentation slash matrix.
Mitrix.
The peak?
We're some news on that.
I think we… we could also talk about the attribute processor.
And, … P-detta related.
Operations.
And I think with that, we will be already, … Pretty bugged.
Okay, … So I think Joshua will join us, so I will, because we have new people in this, position.
We'll do a quick introduction, so, … What we do, from which company we are, coming, and … So I will start by myself, Laurent Kirill.
I am one of the maintainers of this, … Hotel Aru project. In fact, I created Hotel Arrow, 3 years ago, or maybe a little bit more.
No.
Which was mostly based on the creation of, … A new optimized protocol?
for, open telemetry.
combining, gRPC and Apache Arrow together.
the first implementation was in Rust.
with a proof of concept of a Rust Collector a long time ago.
But, for… the community basically asked me to rewrite some part of it in Go to be integrated into the Go Collector.
And then, we are back to rest.
With, a new, data flow engine.
Supporting, OTAP, so Open Telemetry, Apache all natively.
And one of the main differences, except the fact that it's are implemented in Rust. It's, the fact that the pipeline itself is end-to-end hotel.
Meaning that we don't have… we don't need transformation from OTAP to OTLP inside the pipeline, which, changed a lot of things, and, changed also the way that we, We create processors and other things like that.
I'm working for A5, and we are, … a small team here at F5 working on this project.
David Dahl 00:05:13 Day-to-day.
Laurent Quérel 00:05:15 Okay, so, we want to donate.
jmacdonald 00:05:21 Hi, so I walked in in the middle of a meeting, but I'll say hello, I can figure out what we're doing. Ray has joined us, from the Rotel project. I met with him last week, so I'm already familiar.
So I'm Josh, I work at Microsoft, co-founded this effort with Laurent a while back, and yeah, I'm excited, I'll pass it on. So, I guess we're doing introductions. Please proceed.
Laurent Quérel 00:05:46 Yep, indeed. Thank you.
albertlockett 00:05:50 Hey, I can go next. Hi, my name's Albert Lockett. I also work at F5 on the ROMS team. I've been working a lot on, the code that kind of transforms, OTLP data into, OTel Arrow representation, and then adding… mostly working on all the transforms that… or many of the transforms that we do on, the, … On the aero data.
Yeah.
Laurent Quérel 00:06:21 Good.
Okay, next.
Tristan Sloughter 00:06:27 go next. I'm Tristan, … I maintain… I run the Erlang SIG, maintain it, and I'm part of the Developer Experience SIG, the Spec SIG, and … not working anywhere right now, so I'm here, personal interest, and the… I don't work on anything inside Hotel Arrow right now, except trying to… I did one. I hope to do more fix-ups for all the renovate pull requests that don't work.
jmacdonald 00:06:57 So that's….
Tristan Sloughter 00:06:59 the work I hope to be doing more of.
Laurent Quérel 00:07:03 Thank you.
David Dahl 00:07:07 Yeah, I'm David, I work at, … Oh, I apologize, you wanna go?
Ray Jenkins 00:07:13 It's fine. Yeah, go ahead.
David Dahl 00:07:14 No worries. I work at F5 with Laurent, and Albert, and others, and … I've been, steadily working on learning Rust, and I've been just building the, sort of scaffolding for most of the… or not most of, but for several different processors, both in OTLP and in OTAP land.
learning a lot from, this crew. So, welcome, welcome.
Ray Jenkins 00:07:46 Cool. I'm Ray. I'm a founder of the Rotel Project. The company's actually called Streamfold. We started… started that company a few years ago. We were doing closed source, proprietary stuff, kind of interested in telemetry pipelines, but about 9 months ago, we started working on Rotel and sourced it right away. Prior to that, I worked at Snowflake on FoundationDB.
And, focus on performance and observability of FoundationDB. … And I'm really passionate about performance, so when I saw the OTAP project, we were, like, super pumped, particularly coming from places like Snowflake. Prior to that, I was at Segment.
And I worked on all of their distributed systems there, in stream processing. A lot of performance. I was primarily brought into the segment to solve a lot of performance and… Reliability issues to the platform.
So that's my background.
Been doing observability for… I don't know, almost 30 years now. I love Erlang. I used to work on Erlang back in the day at a company called Boundary. Was a big REAC.
Tristan Sloughter 00:09:01 I agree.
Ray Jenkins 00:09:01 React user, you know, React, LevelDB, all that stuff, so, I'm just happy to be, here, hanging out with y'all, and, making OTLP and OTAP, it's much more high performance and valuable for people who are, like, Hyperscaling.
Laurent Quérel 00:09:22 Excellent. Great.
The kids?
Jake Dern 00:09:27 I can go next. So, hey folks, I'm Jake from Microsoft. I'm actually on the SQL Server team, so I don't work directly on telemetry stuff at Microsoft, but rather just, you know, with an interest for SQL Server-related features, so… We collect, basically, telemetry from customer databases. We only do that for, like, a very small set of SQL customers today. For folks that know what Arc is.
That's the subset of customers that my team is currently focused on. But we have ambitions in the next few years to scale that out to, like, the entire SQL estate, which is millions and millions of clients. And so, eventually along the way, we came across this project, and so we've been very interested, and I've been kind of tagging along for the ride, so….
Laurent Quérel 00:10:13 Sort of….
Utkarsh Umesan Pillai 00:10:18 Thanks.
Drew Relmas 00:10:20 I can introduce myself super quick. Oh, Ukarsh, sorry. Go ahead, Drew, no, go ahead. Yeah, I'm Drew, I'm also coming from Microsoft. I've been in the Hotel Arrow repo. I work with Josh and company in, kind of, our telemetry spaces, but in Hotel Arrow, I've been, Mainly doing a bunch of repo maintenance so far, as well as working on a little experimental side project.
Looking at how we can transform data in the middle of the pipeline, in our Rust pipeline. It hasn't been super connected to a lot of the OTAB data flow stuff yet, but hopefully that's going to change in the next few weeks.
Laurent Quérel 00:11:02 Yeah, that would be great. Excellent.
Utkarsh Umesan Pillai 00:11:06 Yeah. Hi, I'm Mutkash. I also work at Microsoft. I'm in the same team as Josh at Microsoft.
And within the Otelaro repo, I'm primarily working on the syslog and set receiver implementation.
We already have some of it in place, but yeah, it's… there's some more things left to do to make it production-ready, and I'd be working on that.
Laurent Quérel 00:11:30 Yeah, and you're also working on the REST client SDK.
Utkarsh Umesan Pillai 00:11:34 Yes, the OpenTelemetry Rust SDK, I'm also one of the maintainers there, yep.
Laurent Quérel 00:11:40 Yep.
Great.
Okay, … I don't know, I think we, we, … Everyone….
jmacdonald 00:11:49 Let me hit up, everybody.
Laurent Quérel 00:11:50 Yeah, so I'll let you, Josh, continue maybe the… drive this, ….
jmacdonald 00:11:56 Sure, well, I, I can, yeah, we, we have on the agenda a few things, I'm looking at just the sort of issue roundup, talking about Rotel. I do definitely want to connect the topic that Drew just mentioned with Ray, because I know, Ray, you got… you had some interest in query… query support, query representations.
other forms of filter and transform language, so I think that would be an interesting one. But my interest today, I think.
I was thinking we… we should talk about current issues. I'm worried that I broke the repository with my big change this week, and I want to make sure that we get a chance to talk about that, and then I have a question for the end. So, should we start with Issue Roundup? Does anybody want to… let's see, here's my share.
Did I share it? I thought I did.
Okay.
Laurent Quérel 00:12:51 No, now, yes.
jmacdonald 00:12:54 Alright.
Laurent Quérel 00:12:54 Yes.
jmacdonald 00:12:55 So… … Let's see… And… I'm gonna go… that's not where I wanna go. … … issues.
Alright, well, … I may as well start then. So I filed this big… I merged a big PR this week, and it was my first, like, getting to know the engine code base, getting to know quite a bit of the code, and I have a fear that I broke some things.
The main goal behind the change was to have a direct lookup for finding a node when you have a message to send it in the pipeline. So instead of having a HashMap lookup with a copy-on-write string, we're using an index into a vector, so that that would be a… presumably a faster lookup.
But also just sort of, like, I think improves code organization quite a bit.
… However, it was a big change. I inserted a node ID, into each component, a constructor path, so it kind of touched everything. And it came down to, … a concern that I had, there was a duplicate method name in two traits, and I think they were… so we talked about this a little bit yesterday. It looked like I was doing the right thing. We eliminated one wrapper, one… one… one level of indirection.
And what I noticed when I was trying to get that merged was I had broken some tests, and it wasn't clear that those were because of timing changes, potentially. Like, there are threads and context switches, I understand, happening. So I filed some issues, and we're kind of looking at, like, the first one, These tests, failed.
I don't really understand this one at all. There's a db parameter.key on one side, and there's a db.parameter query.parameter on the other, so there's an actual difference coming through. And I couldn't quite see how my change would have broken it, so I… I just ignored that test.
And that same failure happened in both places. We've essentially copied one of the pieces of code out of OTLP into OTAP.
… And for the background story that, like, for newcomers here, the idea is that we've got this engine which is runtime agnostic and data type agnostic. Well, I shouldn't say runtime agnostic exactly, but we'd like it to be. And the data type would be sort of a generic parameter, and then we have these OTLP crates, where the data type is OTLP, and we have an OTAP crate where the data type is OTAP.
We're trying to get away from OTLP.
trying to focus on OTAP. So, when I said we copied something, we had one in OTLP, we copied into OTAP, we're trying to get rid of OTLP, so ignore the copy. We have two copies of the same test that both failed.
And I couldn't quite figure out how that would happen, so I want that to be….
Laurent Quérel 00:15:55 Well, what surprised me is the fact that we can even merge.
With such, failure into the test infrastructure?
jmacdonald 00:16:05 Well, I… This is an ignore….
Laurent Quérel 00:16:08 in the… in the CIA.
Sorry?
jmacdonald 00:16:11 I added an ignore,
Laurent Quérel 00:16:14 Oh, you changed merch.
jmacdonald 00:16:16 I pushed… I pushed it in, because I was afraid of all the merge conflicts that were gonna happen either way, so….
Laurent Quérel 00:16:23 Okay, okay, that's… Okay, I understand now, okay, because that was very surprising to see that we had, … a such issue into the CI.
jmacdonald 00:16:33 Yeah.
Laurent Quérel 00:16:34 But I see that Chen Li, that is part of my team also, was saying that he will work on it. That doesn't look, like, related to your change?
jmacdonald 00:16:43 The batch processor, yeah, that's right. And then I….
Laurent Quérel 00:16:48 It looks like, because the fake data generator, so for people that don't know.
It's, it's a new receiver.
That we will use massively in many situations, like the benchmark infrastructure that we put in place.
And the goal of this effect data receiver is to To use the, … the Semitic Convention Registry Project.
As a way to define, … semi-random HTTP, OLTP traffic that we can transform on the, on the fly by unattapped traffic, depending on what we want to test. And maybe, there are some randomness there, or some, Dependency on an external registry that… where we had changes, that's why maybe the… the test failed.
I will look that… I will check that.
jmacdonald 00:17:43 Yeah.
Laurent Quérel 00:17:43 research only.
jmacdonald 00:17:44 the… the… yeah, the fake signal generator didn't make sense at all to me. This one in front of us now, this was the one where I started to think maybe I had broken something.
Because… and the reason I went and put the ignore in and merged it anyway is I was able to see it be flaky on my local machine. Like, I was running it on my local machine in passing, and then I ran it and it failed, and I decided it wasn't my fault. So I… so I put the ignore in, and… and… but I… but I do… I'm starting to have suspicions remember, because the duplicate method that I came into was a thing called send control message, and there were… and, like, I was wondering if there was, like, a send control message that went into an asynchronous channel, and then there was another send control message that was a blocking call. And if I replaced a send into a channel with a blocking call.
having the same name, that could silently break a lot of stuff, I guess, and that was… that's my fear, is what I did. Now, I don't know that that's what happened.
… So now I've shown you two categories of test failure, that… that I created, and I'm… I'm having doubts about them, but I… but I have a feeling that I didn't actually create them, so I wanted to run through them.
… The last issue I filed, was one related to our conversation, Laurent, about the, A, the merge conflicts that were going to create… be created in your PR, which, I think we're going to talk about today. But I don't need to talk about them here.
Those were just a rundown of issues I created when I merged that big PR.
….
Laurent Quérel 00:19:19 Yeah, the second one, … yeah.
jmacdonald 00:19:22 This is a part….
Laurent Quérel 00:19:23 And what, what, yeah.
So you… yeah.
Okay, we'll figure out a way to fix that, because it's a real problem there.
Yeah, the next time, I think we should avoid to put, ignore and fix the issue before we merge, because….
jmacdonald 00:19:38 Okay.
Laurent Quérel 00:19:39 ….
jmacdonald 00:19:40 the presence of flakiness made me feel that I was doing the right thing, but I… I will… I will not do it again.
… in any case, there should be a simple fix if that is indeed what happened, and we will… we will uncover the confusion.
I, … would anyone else like to… Albert, you've filed a number of issues within the last week as well, here. Do you have anything that you'd like to bring up that's new and exciting?
albertlockett 00:20:15 … not, … Not… per… particularly. These issues are kind of, I guess, like, what's on the label. There's a… you know, and I'm gonna… I'm gonna try to run through them and fix them, basically this week. The three that we see there that… that I opened, 1, 2, 3, I should have those pretty much all fixed by Friday. We see there's, like, PRs up for two of them, and then, … the last one, 952, I'll fix after 931 goes in. And, and this, this work is just, … … to unblock some of the work that, I guess, Chris on our team wanted to do to test out sending, OTAP, or OTAP data between the Go collector and our new Rust data flow pipeline, and we just ran into a few issues, expectations that the Go collector had, about the format of the data that didn't align with the data that we were actually producing by our P data and our OTAP exporter. Things like column encodings and just optional columns and things like that. So, yeah, I'll clean those up, this week.
jmacdonald 00:21:31 At some point, are we gonna have to, … keep track of… are there incompatibilities with the Go code and the Rust code that we need to, like, put in, say, version information to, like, handle multiple variations, or are we still in a place where all the variations make sense, and like, you know, like, there's lots of different representations for each column, and so, in the record batch. Are you concerned about, like, backwards compatibility at all?
albertlockett 00:22:04 … Not, … not really, … At this juncture, like a, … No, not, not, not really. ….
Laurent Quérel 00:22:24 I think most of the… the… some of the issue that, … Albert, discovered, are other things that, Was missing, or… Not fully accurate in the translation.
So, for example, the delta encoding, … Before we re-emit, the hotel traffic was missing.
… It's not impossible that we… I think Michael discovered one or two issues in terms of, Optionality, on some columns.
both… in both sides, Go and, and, and Rust, so I think the… the right way to go will be to fix both sides. … Maybe at some point we will have some divergence, some… And then we, we could introduce versioning, if needed.
jmacdonald 00:23:24 Thank you, that was my question, I appreciate it.
… I think we've talked through all the new issues.
Laurent Quérel 00:23:31 Yeah, okay. Joshua, I was thinking that we should, … keep at least 15, 20 minutes to talk about hotel, and depending on the remaining time, talk about the two….
jmacdonald 00:23:43 So I think we should, I think I'd love to talk about Rotel, right now.
Laurent Quérel 00:23:49 Nope.
jmacdonald 00:23:49 Ray, do you want to give us a leadoff?
Laurent Quérel 00:23:52 Sorry, what'd you say?
jmacdonald 00:23:54 I was asking Ray if he'd like to give us a brief introduction to Rotel. It seems like the place to start.
Laurent Quérel 00:24:00 Yeah.
Ray Jenkins 00:24:01 Hmm.
Sure. Sounds good. How long do we have? I just want to make sure I don't run….
jmacdonald 00:24:07 It's an hour-long meeting. I think 20 minutes would be fine, as Laurent just said. If there are other items at the end of the meeting, we can always run over, or, you know, run into the next meeting.
Ray Jenkins 00:24:18 Okay, sounds good. Okay, cool. So, where to start? I guess, probably, maybe just speaking about… a little bit of my own experience, with OpenTelemetry Collector, and sort of maybe what's… why we started the project?
If that makes sense.
Laurent Quérel 00:24:36 Yeah, sure.
Ray Jenkins 00:24:36 So, yeah, yeah, so, Mike and I.
Laurent Quérel 00:24:39 And if you have questions for what we are doing, let us know also. We can definitely explain why we did that.
Ray Jenkins 00:24:47 Yeah, definitely.
So, … yeah, so my co-founder, who you'll meet next week, but we met, … Over a decade ago, we were working on this company called Librato, which was a metrics-as-a-service platform.
We, we, eventually, like many others, we sort of lost out to Datadog, but we got quite large for a while. We were acquired by SolarWinds eventually, so they acquired Paper Trail, Tracelytics.
and Librato, the founder of Librato, ended up, is running the internal cloud service offering inside of SolarWinds, putting these products together, essentially, to create an observability platform.
And, … So, that was where we met, and, you know, at the time, OpenTelemetry wasn't really a thing, but we were always very passionate about observability. And later, you know, as we saw the OpenTelemetry sort of really take off, the the, OpenTracing.io and, and, and, what was going on with LightStep, And then the merge with OpenCensus and all this stuff. We're really excited, but when I started to pick up the OpenTelemetry collector in practice, you know, at Segment, and at Snowflake, it was really sort of a non-starter for us. Particularly at Snowflake, we couldn't use the collector everywhere due to just the performance needs, and requirements at Snowflake.
you couldn't… you couldn't put… you can't put something on a box that's gonna take up 5% CPU or something, that Terry wouldn't let that happen. So we were always kind of like, this is really awesome, and the promise of sort of democratizing, you know, telemetry and just having this open standard. We love that.
But we felt like, from a performance standpoint, we knew that… I knew personally, using hyperscaling organizations, the performance was an issue. And so, when we started, we said we started Streamfold a few years ago, we were working on closed-source solutions, and we built a much more elaborate telemetry pipeline solution with a control plane, and a SAS, and a UI, and all these sort of things. And … that didn't… that… that didn't really take off. We had a bunch of users on the platform, but we decided, that they weren't using it in anger. And we decided where the real problem was, where we needed to focus was, you know, this sort of high-performance, really resource-efficient, collection tier, and one of the first areas where we really… we got some traction… so we started working on Rotel, we started talking to users, and one of the areas, and probably the areas where Rotel's used the most today, is in the serverless space.
So, AWS Lambda, there is an open telemetry collector distribution called ADOT, that many users have tried to use. I'm sure there's some people using that in production, but it suffers from sort of really long cold start times.
over a second or so. And so, as we were building out Rotel, that was sort of one of the first communities we started to talk to. And just, you know, we focused on… initially, we said, well, let's just focus on open telemetry.
as the core receiver, and the exporter. Let's just try to make this also as simple as possible, so it's very easy to use, small binary.
extremely fast startup time, so Rotel's startup time's at under 60 milliseconds, and really try to reduce the footprint of that, because all of… how much memory you use, is really important in Lambda. It affects your cost, and overall performance, and whatnot. So, … that was where we initially found users that were excited about using it and started using Rotel in production. At the same time, there's several other, things that we thought were sort of interesting areas to explore. One of them was if we built those small and fast enough, collection, data plane, we could embed it in other, runtimes and languages. So Rotel is actually, can be distributed as a Lambda layer, as I mentioned, but also as a Python package. So directly from a Python project, you can pip install this thing called PyRotel.
And it brings in Rotel, and it actually forks and runs that as a separate, you know, a separate collection sort of process. And that alleviates the need, as you see in many Cases where people deploy an application, and then they also have to manually deploy a sidecar, perform configuration on that, build all that stuff out.
So we did that for Node.js, we did that for Python, And, another area that was really interesting to us was the, the processor layer. So thinking about, when you look at the OpenTelemetry collector, OTTL is pretty powerful, and you can do some stuff. Historically, the processors were all sort of individually done as, you know, individually written and sort of, like, one-offs with their own sort of configuration. Ott, I was trying to bring that together, and we said, can we take that a step forward and just allow you to write Python? So we started exploring with Rust and the FFI, Could we provide a processor layer that allows you to just write, like, native Python, but backed by Rust as a REST extension?
And so that was one of the key features, in Rotel, so far.
People have been really interested in that. And they're using that, and that's pretty powerful. … we've also added… so we've also started just to expand the… the exporter support. We're really kind of focused on, ClickHouse has been… has been really popular, and people like the… the ClickHouse integration, adding Kafka, you know, trying to get to parity with the collector on that stuff is… that's just… there's so many, re… receivers and exporters, it didn't seem like an area where we wanted to go. So we wanted to focus on the users that had the highest performance problem, maybe some of the more complex, and powerful, you know, receivers and exporters, and really mostly just focusing on exporters at first. The only receiver today is OTLP. We're about to add a Kafka receiver as well. That's sort of the state of the project, and the primary drivers behind it to date.
Laurent Quérel 00:31:20 Thanks, Scott Twisting.
Just some reaction based on your… presentation.
So, definitively, a lot of overlap with what we are doing.
whiz… Probably some differences, and that we could explore, and… And that will be interesting to see, … What kind of collaboration we could put in place.
So, reaction, so the… regarding the processing layer, the Drew and, and other folks also are working Microsoft side on, KQL.
And, OTTL. So, basically, they are creating, a query, a query abstraction.
on which you could have multiple… exactly like data fusion, where you could have, … and they want to use data fusion at the end of the day, but, they are working on the KQL grammar and the OTTL.
So if, Drew, you want to… To talk about that a little bit more in detail, feel free.
… The… regarding the… the ability to… To extend the processing layer.
And in fact, to extend anything into the system.
Right now, so we have two phases.
First phase, … like, a static plug-in system, if that's strange, but that's entirely feasible.
Where we basically rely on things like Linkme, if you know this straight.
It's used by Fuchsia inside Google, but it's a way to, combine plugins in full host, at the compile slash link phase.
So, it's entirely possible, because we deliver threats.
To have another project relying on what we do, and adding their own processors, receivers, whatever, and there is a fully automatic discovery at the engine level.
That meaning that you are able to create configuration combining all those various plugins. So that is what we have today.
It's not perfect, obviously, because there is no dynamic discovery.
But, it's, it's good enough if you, if you want to combine at the binary level, various projects.
The second phase will be, a support for WASM, And, so that will open the door for Whatever language you want to use.
And we will start with processors, because that's definitely the easiest part.
And… and because, recently we decided to… I need to introduce something else. So the… like you, you have multiple types of protocols and potentially data models, for the receiver side. Same thing on the exporter side.
Right now, we basically support OTLP, syslog, values version of syslog.
And, OTAP, the Open Telemetry Apachevo Protocol.
On the exporter side, it's mostly right now OTLP and OTEP.
something… we will add other things later. So, what I'm saying is, independently of the receiver side, everything inside the pipeline engine is OTAP-based, so we… we spent a lot of time to create Abstraction and very, optimized solution to translate For example, OTLP protobuf-based messages.
the desalization is not using Prost. We have a native desalization taking this kind of protot wire format, messages directly translated into this Apache Arrow, presentation. So everything inside the pipeline is Apache RO, and that matter for… Not only the data processing speed and queries that we could apply, because of the memory layout, data locality, and … in the instruction set that we can leverage on that.
But also, for the plugin system, it's super important.
Because… if you are familiar with WASM, What freely matter is the… How you transfer the information?
from your, color, site to the WASM component. And, copying an entire, OTLP batch Will be massively inefficient.
And paying the cost of the standardization each time we call a WASM component will be massively inefficient.
So… One of the benefits of the Apache Arrow approach, and the fact that we have a pure Apache Arrow-based pipeline.
First, xerocopy.
So we can, instead of sending a big buffer, we send a memory regime.
So it's one printer. And then, because it's serialization free, because Apache RO is designed this way.
no cellulation at all. So the communication between the ROST engine and the WASM component will be very, very slow overhead. So that's another reason why we are moving in this direction.
Just in….
Ray Jenkins 00:37:13 a lot.
Laurent Quérel 00:37:14 As a reaction to what you said.
Ray Jenkins 00:37:16 I've fiddled around with WASM a bit in the API. I mean, essentially, you can just pass a pointer. If you're trying to serialize, I mean, that would defeat a lot of the performance objectives, but it's very difficult to do. So, passing a pointer to a memory region in WASM is its way… I had done this some go work in WASM as well, previously. So that makes a lot of sense. It's really interesting, we've seen as well, too, and … so using ProS, we use ProS internally. I mean, it allocates for all the strings, things like, actually, the default stubs that are built, for, like, things like trace ID, it allocates back to U8s, which are all heap allocated. This is inefficient. In the amount of time, and even though we've got some great performance gains with Rotel, the amount of time we're spending allocating and deallocating those values, that's a tremendous amount of CPU. Never mind… And, obviously, then the repetition, of the data, like, all these things could be interned, doing something, like, efficient in a columnar format, like error.
Laurent Quérel 00:38:13 That's exactly what we address.
with, the OTAP protocol.
Even if we… so the first preliminary result.
for the infrastructure that we have to deserialize a TLP to a tap without intermediary steps.
is already equivalent or faster than the pure pros.
And we have a real transformation there, it's not just, … And we expect to see even better results. We have some optimization that we didn't put in place.
fundamentally, leveraging the fact that we have a dictionary encoding into the Apache Arrow project, but the OTAP project. And, and there are ways to… in fact, to postpone or to delay the ETF-8 validation phase.
to the dictionary, After the duplication, which will increase massively, in my opinion, the performance of this, decoder, a TLP, to a test.
So we expect to see even better results. Even if you are purely OTLP on the reserver side, and OTLP exporter side, we should not, at the minimum, add any override with this OTAP internal OTAP pipeline. And I expect also to have, even if we don't leverage the data processing speed, if it's purely routine.
we should not observe, decrease in performance because of that. And, and we have, … We have some shortcuts, depending on the pipeline configuration.
If you have, for example, OTLP receiver connected to an OTLP exporter just for routing purposes, or if in between you have a basic router leveraging signal type.
it's a scenario where we… we don't do anything. It's just basically a TCP proxy, where we don't even try to deserialize in a tap. We… we… we, we do lazy, … Based on the needs, we only, deserialize if we have a need to look inside the information, otherwise we just take the binary representation and, and… And transit that to some destination.
Ray Jenkins 00:40:46 Yeah, that makes sense.
Laurent Quérel 00:40:47 Yeah, so that was my feedback on… on the… based on what you said. I think that will be, massively interesting to… to see how we could collaborate.
….
Ray Jenkins 00:40:58 Yes.
Laurent Quérel 00:40:58 How do you… how do you… you see that?
Ray Jenkins 00:41:01 Yeah, yeah, and when we spoke with Joss last week, we… we stepped away from that discussion. We said we spent a bit of time prioritizing what, you know, we thought was the next steps for OTAP, but we're putting that together, so a lot of these things we're discussing here are… are aligning. So, essentially, you know, collaborating on, having OTAP, support internally, the zero-copy, delayed deserialization, all those things are very interesting. The component piece is actually really interesting, too. So today, you know, we don't have, like, an OCB layer in Rotel.
We just were leveraging, basically, Rust features to turn some things on and off.
So for certain builds, obviously, like the Lambda one, right, we're not including some things to keep that thing small, but one of the things we want to talk about is that component, that component layer, and basically having a standard component interface, as you spoke about, so we can publish things in crates and share and things like that.
That's also very interesting, … Yeah.
Laurent Quérel 00:42:07 Yeah, so, so regarding the… So, regarding the, let's say, the vision behind the, what we name right now Hotel Arrow Project.
Phase 2.
Which is, in fact, a set of libraries to… Basically to create, a Rust-based, what I named Dataflow Engine.
fully compatible with OpenTelemetry, that could be embedded into the GoCollector, if needed.
both side Microsoft and F5, we have internal stuff, and we will use directly those libraries to To create our own, let's say, host-based distribution.
But, we, we want to share, and, and having, a set of libraries that could be embedded into the Go Collector.
So we have a lot of discussion right… in fact, not right now, but we had some discussion with the rest of the community around that.
… Yeah, so… One of the vision is first being able to, … to reuse the… the configuration format. It's not the configuration format.
That we natively support, but one of the aspects One of the constraints is Even if we have a superset of these configuration formats.
I mean, at least semanti… at least semantically.
We should be able to create a bridge.
bum… a GoCollector configuration file to this internal configuration file. That is a superset, because … providing additional capabilities that are not… could not be expressed into the Go Collector.
So fundamentally, some differences.
We'd like to be able to, to create real DAG, and not just, … relatively basic pipelines with… that have a lot of limitation into the Go Collector.
So, we'd like to be able to express more complex pipelines, and we have this concept of, … HyperEdge into the project, so you have a node, and … imagine that you want to create a node to… To express the failover, … Or, let's say a failover component.
generic one. Something that will, not rely on the fact that some people decided to put some failover, behavior into their exporter, which is what most of the people do in the GoCollector, because this behavior is not a generic one. So we want to fix that, and for that, we need some additional ways to to represent a node into this DAG. So, having a failover processor will require to have two outputs.
Like the… let's say the regular output and the fallback output.
And the logic of this failover will be expressed into the processor. So that's an example.
Ray Jenkins 00:45:25 Yeah.
Laurent Quérel 00:45:25 of HyperEdge, and, and we have different, Semantic for the channel between the scenes, with broadcast, and and load balancing, and those other things like that.
Ray Jenkins 00:45:40 Yes, yeah, right now, their interface, for example, it's just, like, it's an interface, right? And you're calling a function versus, I think you're using the MPSC, and we are as well. This makes a lot of sense to me. So, historically, working on, let's say.
let's say outside of a process, let's talk about distributed systems for a moment. When you're building distributed stream processing systems, it's quite common people essentially stitch together a serial pipeline, and though there may be branches, it's difficult to make a DAG out of it, right? But what you find over time is that you build functionality upstream, which you then need downstream, and then people then tend to copy it. A great example is deduplication. So you may perform some deduplication, like, early in a pipeline, then you may have to do some other processing, and then it It turns out maybe you're doing some enrichment, you need to deduplicate again.
So now you have the choices. Do I feed this into the front of the pipeline and rerun this again, or can I have a DAG that's powerful enough to express, hey, send this to this node, with some sort of, you know, a command, essentially, that provides, hey, I'd like you to perform this again. So that's a really powerful… that's a really powerful primitive, I think, to have a pipeline.
Laurent Quérel 00:46:49 Yeah, so that's it. We have the same, … foundation or background on that, so the… definitively, that's, So that's one difference that we… on which we don't want to compromise, and that's why we have this… Configuration model, that is a suckerset.
But with the constraint of being able to -oh.
let's say, adopt the GoCollector model if needed.
Ray Jenkins 00:47:22 I've seen that.
Laurent Quérel 00:47:23 Yeah, that's amazing.
Ray Jenkins 00:47:24 important to the, to the, the project, the CNCF overall. There's a requirement for collectors to… to support the.
Laurent Quérel 00:47:32 I see Josh, Joshua, Joshua want to, to say something.
jmacdonald 00:47:36 Yeah, I wanted to remind us of the time, and I thought that there would be an interesting direction to steer us, since we have Ray, and I think this is a really interesting conversation.
I know both of you, have mentioned NUMA architectures. It's one of the reasons that we wouldn't follow exactly the same configuration model.
You know, like, there's just no way to set up NUMA in that configuration. And I know that both of you, Laurent and Ray, have spoken about, instrumentation.
self-instrumentation of collector pipelines and how we need to think about optimizing our SDKs. It's an exciting conversation to have, partly because we we, made some commitments and promises to the hotel group, saying what we were going to do, talking about building Rust and building pipelines, but we also said, and I think this is a pretty key, important feature statement, that we're going to innovate, or try to innovate, how we… how we self-instrument these pipelines, because….
Laurent Quérel 00:48:42 Yep.
jmacdonald 00:48:43 the… like, I think OpenTelemetry as a whole.
gained its popularity in the trace space from taking on the open tracing, and then we, like, shoved ourselves into metrics, and, you know, like, there's a model there, and there's a data model that people are liking, but the actual instrumentation procedure, especially in metrics.
it's pretty heavyweight, and doesn't feel very usable. It doesn't feel like OpenTelemetry has done enough, and that's why I think we both should and can, given the statements we made, experiment. So, I know, Laurent, you have a draft piece I want to talk about, and I'd love to hear Ray's thoughts, or, like, just talk about that with Ray here.
Laurent Quérel 00:49:23 Sure, makes totally sense, and I will do my….
jmacdonald 00:49:25 It's a more exciting area than plugins and componentization, which we're going to have to do anyway.
Laurent Quérel 00:49:31 Perfect, and I will do my best to, … to keep that in the remaining 10 minutes, if people want to stay, I can stay more.
Okay, so let's share my screen. So the… Let's see, I want to… Maybe open the REME first.
… So, I'm working on an internal telemetry SDK with some core principle, schema first.
So I'm also, metowner of the, Hotel Weaver project.
Which is… the tooling behind the semantic convention project.
And, and we have code generation in this system and so on. So I'm experimenting, this approach also for this project. So, being able to Basically, at the end of the day, I'd like to see the system able to generate or to use a semantic convention registry to describe perfectly the set of signal that could be produced by this engine.
… So… request generation is super important. Right now, it's done with macro, I will… I will show you that.
It means that we… we have a real type-safe API. There is no way to misuse the system. And also, the fact that it is, there is third generation, there is no, stringly type, lookup, there is no, abstraction that, We'll, add some overhead.
Another, important aspect behind this telemetry SDK is the fact that, One of my main issues with OpenTelemetry is the fact that multivariate matrix are not natively supported, and that's a massive issue for i5 and for me. So, as a reminder, multivariate matrix are a collection of matrix that share the same attributes And the share, share the same timestamp.
People that want to use this concept right now with OpenTelemetry, they have basically to duplicate.
For each metric, a new set of attributes, and then again.
So… I want to fix that. Performance focus… that's the focus of this project, being massively faster than what we have with the Go Collector, leveraging Apache Arrow, blah blah blah, and leveraging also the hardware architecture on which you are running, leveraging CND solution set, a knowledge of the NUMA topology in order to organize properly, the various pipeline engine.
So, performance is fundamental also for this telemetry SDK, because on the, what I named the hot pass, or the data plane, like you said, … I don't want to do any, synchronization, anatomic.
And, so I will present how it's fixed, I mean, how it's implemented, and there is this last piece, auto-describing, or auto-description. It's basically what I said, being able to, at any point of time, to get, a semantic convention registry that is.
By design, totally aligned with the binary that you are using.
And then you can use it to do whatever you want, do some validation and other things like that.
So, there is two phases, in this, telemetry SDK. We are close to the end for the phase one.
… So, right now, what I name the local controller.
as opposed to the controller that you mentioned, which will be, something more global, for example, running on a Kubernetes cluster.
So this one is internal, and basically orchestrates the, … Different pipeline engines, so we have a thread-per-core approach.
And so we… what we do… what we do right now is only thread pinning. So we discover all the cores, we, create… depending on the configuration, we create one pipeline engine per core.
And inside this pipeline engine, we have, like, a local runtime, which, will run inside the thread that is pinned to the corresponding call.
And for each pipeline engine, we have what I name the metric reporter.
There is a registration phase to a global metric system, which maintains a metric registry.
And, and… Based on configuration, regularly, there is a… a local collection, so that all the implementation of hunters and so on are done inside each pipeline engine, like, just, a strip of, hunters, which are, U64, for example.
So super fast.
But at some point, based on the, … for people that are familiar, we have this, … for every node, we have node being receiver, exporter, processor. We have, at the minimum, we have what we name a controller channel.
And optionally, we have a PData channel, so receivers don't have P data channel, because they are… they interface with the outside world. Processor, they have both controller and P data channels. Exporters, they have both, P… like the processors. So, we have a way to… Dialog with each of node, and say, okay, by the way, please take some time just to report your matrix.
And that is done with the metric reporter.
Otherwise, everything is done locally inside this node, and because we are a thread-per-core share-nessing approach, we don't have to deal with complex synchronization. And then we have this metric system that will we aggregate, and I have this notion of static attribute versus dynamic attribute. I will show you how that's… is… use, as a developer experience. So the roadmap is now… Oh, there is, something wrong there.
I put the 2 times the 10, the same geogram, which is not what… So, the pneuma aware things will basically be the same thing, except that, there is, in a future PR, a way to discover the new methodology. This local controller will, Create a collection of, pipeline and gene with thread pinning and memory pinning.
For a corresponding luminode.
And the metric system will exist for each new method, so we don't have any… inter a new mandate.
communication related to the internal telemetry system with this approach. So the goal is really to minimize as much as possible any internal communication.
So that's the… the… the overall design, and now, in terms of experience, … let's see… Let me start with attributes.
jmacdonald 00:57:21 Can I just interject some sort of commentary? What I see here is, is good. I, you know, I'm… I'm very familiar with OpenTeometry metrics, been involved with it for a long time. What you're just describing doesn't look like an OpenTeometry SDK, and that is okay with me.
what I… what I want to do here is let you innovate and get to the performance story and the usability story that you like, and we will work backwards to the OpenTelemetry data model and the OpenTelemetry SDK model.
Because I just want to say that, especially for the other people in the room who do know OpenTelemetry metrics closely, I think it's time to just break the mold and, like, start fresh, and that's what I'm enjoying about this. I see an asynchronous SDK. We can put terms on it that make it look like OpenTelemetry SDKs later. Continue.
Laurent Quérel 00:58:11 Yep, and … … knowing relatively well also open telemetry, I… I've designed this system to be… to be compatible at some, I mean, at some level.
jmacdonald 00:58:26 is concerned.
Laurent Quérel 00:58:27 So,
jmacdonald 00:58:27 It's just, it looks different from the outside right now.
Laurent Quérel 00:58:30 Yeah, definitely. Especially the metilite metric that you will see soon. So, because it's schema-first approach, everything is designed in a way where you, you specify… so in… here, for example, it's, what a name attributes it, … That's, attributes set that are used by the engine itself.
providing some context to, the matrix. Also, here you see the declaration of an attribute set for the… at the engine level, so, where we talk about things like core ID, new manhood ID, and process ID, or process UID.
Just basic script, you just specify the fact that it's a little bit set, you can provide a name that will be exported into the semantic convention registry.
Otherwise, those, comments will be used as a brief in the semantic convention world.
the… the type are used and converted into semantic convention data types. This… that's… that's done.
Now, if we… if we want to… so usually we have some hierarchical, … design. So we have the engine, and then we have the pipeline engine.
Let's say, we have the controller, we have the pipeline engine, then we have the nodes.
So there is some kind of hierarchy. It's logical to have attribute set per layers, and they will be nested together at the end of the day. So that's how it's done.
We, we, we have… pipeline attribute set.
that composed with an angel attribute set. So at the end of the day, it's… it's like a merging of these two, attribute sets. Everything is static, everything is, … when… when I'm talking about static attribute set, we just send to the… to the… to the metric system only one time an instance of those attributes set. There is no longer… every time we collect metrics, we send attributes.
When those attributes are, let's say, static, it's only one time.
For instance, so then, let's go to the metric to understand how these things, is represented.
So now, we, we have this, so for, for the perfect starter, exporter. We, we, … I was interested by a set of metrics.
multivariate matrix in that case. So, … so I just create a script with the… In the, in that case, inter U64.
So… you will interact directly with this script. That will be part of your state for this exporter. So if we look at the state of this exporter.
It's directly that. It's a metric set.
parameterized with the perf exporter P-data metric, which is something that you described here locally.
And, and use, … macros to define the fact that first it's a metric set, and then you have multiple metrics that are part of this metric set. That's the multivariate part. You can define the unit, you can define the description if you want, with those commands again, and various things like that.
So now, … Now that we basically create a raw strut, or a strut, a basic one.
The… there is two phases. The first phase is about, … Registration. So the registration is… so we have this path exporter with a constructor, and the constructor gets what I named the pipeline context, and we register the metric. It's just a generic method. You post the… The structure type, and the system behind the scene will register that into this generic global metric system that could be at the numelod level in the second phase, and you get directly an instance That you will put directly into your state, which is, … this field.
That's it. And the register metric will add automatically, if we look at the implementation of this thing.
We will see that… In fact, the attributes set for pipeline and node are automatically populated.
So if… we will have a way in the second phase also to define, if needed, some additional attribute set for the perfect spotter itself. Right now, it's not supported, but good enough for me for now.
Ray Jenkins 01:03:34 Mmm.
Laurent Quérel 01:03:36 And now, you want to report something, so you just, if we, if we look at the… so let's see… we can do… I will do the usage.
So we see, … Where it's used, So, for example, … In that case, we had to increment some counters based on the number of arrow payloads of a specific type.
So the, the counter exposed.
implement, decrement, add, that's for the Kunter, but for up-down counter, we will have different, method exposed, and for gauge, we will get additional other, method. So we, we just basically implement, a U64 inside a strip that is part of your, of your context. So.
I thought it might have been anything faster than that.
And, and then, the engine itself will call us With a control message.
And the control message in that case will be, collect telemetry.
And the node has just to comply with this control message and say, okay, I have a specific state that is represented here, and I just need to report to the metric exporter that the system gave me.
And that's it.
And then, behind the scene, this information will be, … Translated, into, … so if we go there… So we, we basically, … So first, we check if we need to flash, because maybe your node is unused. There is no activity at all, so there is no reason to report anything.
So that's a method that is automatically generated by the microsystem.
Based on your street.
And, and then we do a snapshot.
So the snapshot is… A generic way to extract the values And to create a message with that.
It could be as easy as… it could be as fast as a memcopy.
Everything is aligned, 64, packed, and so on.
And… And if the emission of this snapshot success?
we clear the values. Otherwise, we keep everything. So the, … I need to fix that, but instead of a send, I think, it will be, like, a try-send.
Soon. That's something I need to, basically, I need to, I need to have a to-do there.
Because what I, I, I like to, … Sorry, I send logic… … If we, let's say, we have this NPSC channel full, we don't want to include the data plane.
So, so we will not….
Ray Jenkins 01:06:55 you've.
Laurent Quérel 01:06:56 Clear values in that case.
And next time, we will be more lucky, and we will basically send the information. So that's how the system works, and obviously, we have, on the new manhood level, we have a thread with some different priorities, and we collect those information, we do the aggregation into a slot map.
Which gives us, a direct look at. And that's the reason why maybe you, you ask yourself, why do we have this concept of, metric set. We defined that, but we got, during the registration, a metric set. In fact, a metric set is… … the mid… the… the… the… The script that you defined, and a metrics key.
And this matrix key is, in fact, just a raw number.
That is its two number, in fact, returned by the submap.
So when we, when we send the information, the snapshot, over the MPSC channel.
We send the values, just a binary, … U64 VEC, and the metric keys, which is… which are two numbers, and that's it. And the aggregator will take that and aggregate that directly into the slot map.
Based on those two numbers, which are in the express version, and we know, for people that know SOTMAP, that's a regular approach.
Yeah, so at the end, we end up with something that is type-safe, schema-driven, in my opinion, super fast, and … Yeah, and… And anyone can define their own metric.
Ray Jenkins 01:08:45 It needs… so… fantastic, Lauren. … taking a… so, when you… you need… everyone needs metrics, but when you need them the most is in the hot path. Generally, this is the code that you care about.
Laurent Quérel 01:08:58 Exactly.
Ray Jenkins 01:08:59 And this is why you're instrumenting. And the problem is, if you don't have a metrics library that is built from first principles to essentially be as low overhead as possible, now you're affecting your measurements. And we cannot slow down the hot path just to instrument the hot path. So, this fundamental approach of… and I think, you know, Josh.
was excited. He had… I know he had worked with Go before, and he looked at the segment library, and we did a lot to essentially remove locking, you know, making sure there's no false sharing, striping, basically, a somewhat similar approach, not necessarily pneumo-aware, but, … very powerful and high-performance metric system. It does need to be rethought. And then, so that's wonderful. Also, I think, then when we talk about the duplication of data, just regardless of the actual waste of just repeating all of these values again and again, Being able to essentially intern that data, only have one copy, and then encode it in a format that's obviously much more efficient.
That's… it's great, yeah.
On our side, on Rotel, we haven't done… you know, we're using Tokyo right now, and we haven't, you know, set up multiple Tokyo pipelines and thought about NUMA awareness yet, but it's something that, you know, we… we think is something we might want to address. So it's really exciting, rethinking the metrics SDK.
being able to instrument really, really hot pass, with, like, zero overhead is, like, it's… it's big, I think. And I think, as Josh said, you know.
OpenTelemetry really hit it with tracing, but I do… I think metrics needs a first principle approach.
Laurent Quérel 01:10:42 Yeah, definitely, and we will apply the same approach for traces and structured events.
It's part of the roadmap for this telemetry… internal telemetry SDK.
But it's a lot of work, so, I focus first on the… The metric system, because right now we, … We have a milestone, beginning of September, where we want to do some demo.
And … and we basically have a benchmark infrastructure, different from the one that is used by the Go Collector, but one where we will compare the Go Collector with this first-based system.
And, with different, pipeline configuration.
To expose the… the benefits.
It's still super early, because obviously we don't support, all the ecosystem, and, so we have exporters, we have receivers, like the syslog receiver, which will be, very optimized. Utkarch is still there, and, he was working on it. We also have an, a packet exporter, able to store on S3 and compatible solutions.
Where we leverage the Apache RO, approach. … But, yeah, so we will be able to compare some scenarios, but far from what we should.
Ray Jenkins 01:12:10 In theory, if we want to do a real comparison.
Laurent Quérel 01:12:14 Knowing that we already have better performance, obviously, like you have, in any dimension, from memory to CPU usage, latency in general, and so on. But, the difference will increase massively once We end up with… pipelines definition involving, data processing.
So we will highlight that a bit, in September, but that will be far from the end of the story.
An example is the attribute processor, for example.
Oh… Relaying is not a thing in the attribute processor, or… So they, they, they told you that you have to delete and reinsert with a new name.
Everything is based on the fact that they have, basically, to navigate across this gigantic hierarchy of small objects.
Representing… that represent this batch of It tweaks silence.
Ray Jenkins 01:13:17 Right.
Laurent Quérel 01:13:18 have to do that. And what we do is, we leverage the fact that we have the Apache RO records, and we can just translate the So a renaming is basically a change into the one entry into the dictionary.
And boom.
It's so that the gain will be really, really massive, for… for… for this kind of operation.
Ray Jenkins 01:13:44 So we want to show that.
Laurent Quérel 01:13:47 But, obviously.
We don't have an OTTL processor or a KQL processor yet, but that's where the things will start to show big differences.
Ray Jenkins 01:13:58 Yeah, no, it will be massive. Yeah, I mean, it's… today, it's just this massive hierarchy, and you're just literally just chasing pointers all the way down to just get to this. And the structure, when it's in Protobuff, it's like, it's… logically represented the P data as a map, and then it gets actually physically turned into that inside the collector. It's really… it's a list in, in, in… key values, and yeah, just to be able to basically… just to basically be able to go to a column and just go, okay, here's my index, and then it's just going to be… it's going to be so many orders of magnitude faster. Yeah.
Laurent Quérel 01:14:35 And the, and the defense.
Ray Jenkins 01:14:36 nanoseconds.
Laurent Quérel 01:14:37 the… Yeah, the difference will increase with the size of the batch. Bigger the batch will be, the bigger the difference will be.
Ray Jenkins 01:14:45 Damn.
Yeah, a lot of….
Laurent Quérel 01:14:48 Okay, well done. Yeah, any question, feedback, or ideas, ….
Ray Jenkins 01:14:55 I'm interested to see about what we didn't, we didn't talk about, in the metrics design about, just sort of dynamic attributes and things like that. So that… that's one thing I wanted to see.
Laurent Quérel 01:15:08 Yeah, so the first phase of this telemetry SDK will not include the dynamic attribute, because I basically don't need it right now for the benchmark infrastructure.
Knowing that… if you think about it, you have those pipelines with a DAG collecting nodes, the, … the metrics are important, the attributes also, but the attributes aren't really defined by those information, like the node ID, the thread ID, core ID, and so on.
if I want to observe unbalanced situations, if I want to know, that, this instance, specific instance of the Perfect Exporter is behaving better than this one.
I have everything already there in terms of context definition. Now I'm aware that we need sometimes to get some value for attributes coming from incoming messages.
That will be done in the second step. But I really want, in the SDK, make a clear distinction between what I name static attribute and dynamic attributes, because static attribute will be communicated only one time to the telemetry system.
Dynamic attributes, when they exist, they will, communicate it Every… at every time, at every reporting time.
So that's why there is this distinction.
Ray Jenkins 01:16:37 Cool.
… Yes, I think the biggest thing's, … is… and I think we'll follow up with Josh, we can talk about this more, where we can find, you know, opportunities to collaborate together, and what are the sort of highest priorities there, yeah, where we could help.
And, yeah, and just… and push this forward, so I think it's just… the community's just gonna benefit from this, so… Tremendously.
He's really exciting, so….
Laurent Quérel 01:17:06 Trip.
Yeah, feel free to have a discussion with, with Joshua and myself on that, and… I think, we could probably figure out something that will be, ….
Ray Jenkins 01:17:18 Yep.
Laurent Quérel 01:17:19 Useful for all the parties.
Ray Jenkins 01:17:21 Sounds great. Well, thank you for all the presentation and introduction today, and look forward to, yeah, the next one. We'll see you Tuesday.
Laurent Quérel 01:17:31 Yes, indeed.
Thank you. Bye, guys.
Ray Jenkins 01:17:36 Have a great weekend.
