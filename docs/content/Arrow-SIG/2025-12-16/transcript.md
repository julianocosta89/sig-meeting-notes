SIG: Arrow SIG
Date: 2025-12-16
Duration: 59 minutes
============================================================

## Zoom Recording Transcript

**Albert Lockett** 01:35 Yes.
**Aaron Marten** 01:41 Hello.
**Albert Lockett** 01:48 Aaron, the, quiver stuff's looking good.
**Aaron Marten** 01:51 Yeah, I just, published another big PR for it, minutes ago.
**Albert Lockett** 01:57 Awesome, yeah, hopefully, I'll get a chance to look at it tomorrow if, if, Someone else doesn't get to the first.
**Aaron Marten** 02:08 Okay.
**Joshua MacDonald** 05:00 Hi, everybody. Welcome. Alright.
My voice is almost worn out for the day. We'll see how we do here.
I'm gonna pull up our meeting notes.
All right, full house, everybody. I've got the full nine panel, at least. Very good. Coming with the notes.
I do, okay. Found the right notes.
Well… if you were here the last Thursday, it was a meeting where we talked about big visions and statements for Phase 3 of the project, if there is such a thing, and I learned a lot. I don't think we need to repeat any of that stuff. It was healthy.
And I was especially thankful for Trask to be here and talk with us about governance issues, as OpenTelemetry is concerned, as well as Pablo for showing up to represent both GC and the collector there.
So we're kind of back to a normal meeting.
I would like to take us to the issues, because we skipped them last week.
Let me find that.
And then I know we have a couple of good open PRs.
Let's do that here.
Cool.
Alright, since, like, a while back, I don't know how far we want to go. Oh my gosh, look at this.
Well, I know… Well, let's just look at one page of this, because some of this stuff was more than two weeks ago.
As far as what's new and important, we can get through this quickly.
Albert's got some things that he's working on, we'll talk about that, I think, related to your PR, maybe, Albert. Cjo, I definitely want to put a spotlight on any issues that you have or want to, like, discuss with us, and I see there are a couple of them.
And so I think we should reserve time to talk about CJO's work with the benchmarks.
We also have some work going on with Windows builds, And then I have a few, filed about the batch processor, also in OpenPR, and… I'm looking for things that we definitely need to talk about here as far as new issues.
Some flaky tests… We started to consolidate our time duration parsing, When we get to the PRs that are maybe worth discussing, I can go into the fact that there are still some suspicious parts of the arrow-based batching process, but we also have a new method to fall back on.
or OTLP.
Okay.
I… I see CJO is here. I would say, for the most part, some of these issues have to do with ongoing development, and some of them need to be discussed. Do you, have any that you'd like to pull out and bring our attention to CJO?
**Cijo Thomas (Microsoft)** 08:38 I don't have anything to discuss in detail, I just opened issues based on what I observed, because a bunch of performance tests are reporting 100% load losses, and I can reproduce it, locally.
**Joshua MacDonald** 08:53 Yeah.
**Cijo Thomas (Microsoft)** 08:54 So that's just a fact, like, I haven't spent any time investigating why.
So if anyone knows off the top of your heart, like, then I would be, like, glad to make that change. But otherwise, I'll just leave it like that, and continue adding more scenarios.
One good thing is we just merged the saturation baseload test, which I just observed that we are hitting, like, 100% CPU now on one core, so I will be, like, working to improve it so that we can… try running the engine in, like, multiple CPU cores to confirm that we do indeed scale, as we increase the number of cores. I can see it's mostly occurring in my local test. I'm trying to find, like, how best to, like, run it on a nightly basis. I don't have any updates, Yeah, and, like, there is issues about, like, collector tests, which we added last week. That one, unfortunately, is failing, like, it's dropping 100% of the logs.
Yeah, so there are, like, issues to be investigated, before we, we can really get a clean, consistent measurement, or every night.
**Joshua MacDonald** 10:04 Very good. I see… this, item about tracking the binary size of DF Engine, that would be very good to know, resident size, for example. Someone asked me that today, and I didn't have a good answer, so thank you, thank you.
**Cijo Thomas (Microsoft)** 10:18 Yeah, I will learn that. It's also important when we decided to, or at least initially decided to use Tokyo Tracing macros.
For logs, they use heavily, static things, so that might have, like, some impact on the binary size if you have, like, tons and tons of logs. So we may have to consider, like.
excluding some debug-level things at the compilation level. So anyway, that issue is just to track binary size, and as we add more logs, we'll see whether it has any material impact or not.
**Joshua MacDonald** 10:50 Gotcha.
**Cijo Thomas (Microsoft)** 10:52 Yeah, and I also added, like, this is unrelated to bench test, this is basically improving overall, CI test coverage. We are only… we were only testing Linux, x64. I plan to add, like, ARM64, and also Windows, and all the variations. I started with Windows, but… You probably have noticed we are having a lot of failures in Windows. Some of them are just ignored right now, but we still don't have a green CI, so I'll be ignoring more and more things, to make…
**Joshua MacDonald** 11:23 Thank you.
**Cijo Thomas (Microsoft)** 11:24 They're happy, and then eventually come back and start addressing them.
**Joshua MacDonald** 11:28 I have someone coming up to speed, who has more of Windows experience than Linux, and will be working on some of those failures for us, ASAP.
**Cijo Thomas (Microsoft)** 11:37 Perfectly.
**Joshua MacDonald** 11:37 So…
**Cijo Thomas (Microsoft)** 11:38 more, like, compell… like, some… for example, like, Laurenti did use the Gemiloc thing.
**Joshua MacDonald** 11:43 Yes, he broke… he broke Windows 4 days ago, exactly. We had it working for…
**Cijo Thomas (Microsoft)** 11:47 Already brokered before that, but now we don't even compile, so, yeah.
Anyway, like, yeah, that's all, like, I don't have anything in particular to be discussed, but if anyone knows the reason why, like, the engine is dropping logs in low test, just feel free to ping me, but otherwise, I'll keep investigating.
**Joshua MacDonald** 12:05 Thank you. I have, a couple of pieces of feedback on the dropping question. I would like to look at it. I might just take that up myself. I had a sense that you know, there's been a lot of quite speedy development recently, in the last few months even, and first we got ACNAC contributed and, like, got the basic ACNAC mechanism, and then one by one, for each component, I went through and have added support. But I just finished batch processor, like, last week.
So, we had done the OTLP receiver, we had done the OTLP exporter, the no-op exporter, the test exporter, and one by one, anything that needed it was being worked on. But I don't think we ever got to the OTAP exporter, or the OTAP receiver.
I think the OTAP receiver, but not the OTAP exporter, maybe? Anyway, there's… the point is that there's some gray areas that may be not finished with, and I wasn't concerned, too concerned, at least, with the OTAP data path At least a month ago, I wasn't. So it might be easy to explain and not a priority to fix.
But… Thank you.
**Cijo Thomas (Microsoft)** 13:15 Okay, yeah, so for those things which we know, obviously, are not enabled, I just disabled them just to save some… save some CPU.
Okay. We have a very limited, I mean, to be precise, we have a very single, just one machine to run.
**Joshua MacDonald** 13:30 Very responsible.
**Cijo Thomas (Microsoft)** 13:31 Yep, yep.
Okay.
**Joshua MacDonald** 13:34 Very good. I… I think we should… Well… Okay, so… Here we are.
We went through briefly the issues that are new, there are some that are related to Albert's PR, I think we should look at that. I think there are some that are related to my PR, I think we should look at that. But now it's time to put the agenda together, and Aaron has a, FYI.
that he maybe would like to speak about. Aaron?
**Aaron Marten** 14:13 I just wanted to call attention to this PR, just because it's a big PR, and I just submitted it about half an hour ago.
So this is the next, major part of Quiver, which is the persistence layer that I've been building up. So the write-ahead log implementation was completed. This is the next phase, which is the, Reading and writing of these, segment files, which are the, files that contain, you know, multiple streams of, Arrow IPCs so that we can, you know, in some kind of sane manner, serialize OTEP, records the disk, to inform DISC. So, just calling attention to that. I don't know that I want to take up a ton of time in this meeting, discussing it, but just wanted to make sure it was on, on the radar.
**Joshua MacDonald** 15:03 Very good. I have appreciated the pace of your PRs, Aaron. I'll get to it, looking at it tomorrow morning, for sure. Are there any, design highlights or things you're proud of you'd like to share?
Oh, there's quite a bit in there. Let's take a look. Otherwise, we might run out of time.
I mean, otherwise we might have lots of extra time, is what I mean to say.
**Aaron Marten** 15:30 Okay, Yeah, I can talk through some of it. I mean, you can see there's a lot of… there's a lot of commits in here.
**Joshua MacDonald** 15:40 So…
**Aaron Marten** 15:43 The… I think probably the best place to start is if you go to mod RS file under segment.
So, so the changes to ArchitectureMD are also worth going through, just because those were places where, I kind of… Needed to make updates, or thought it was prudent to make an update, in that file, which was the original more or less the original quiver issue we had discussed, so there are some design changes that I tried to capture there.
So this, so ModRS is a great entry point to look at, for kind of understanding what's going on with, the segment files, so it'll… it goes through and will explain, kind of, you know, what's in all the individual files. And then if you look at the writer RS, That, there's a dot comment in the top that will kind of, Show the layout of, kind of, what the segment files actually look like.
So… and this was all covered in that, in the original Quiver issue, but I'm just revisiting it really quickly here. So we've got the different arrow IPC.
streams. So you can think of a, you know, each stream is a single schema. So the idea with this, this file is that we want to still have a memory-mappable file.
But this supports multiple multiple schemas. So… so with a single, you know, arrow IPC file, you can't really have multiple schemas in there, so this… this kind of solves that problem, and allows us to… interleave multiple different streams, each with its own schema. And then there's a manifest that points to the different So that we can reassemble these, you know, OTAP record bundles back into, you know, a cohesive thing, when we're reading the file back, so…
**Joshua MacDonald** 17:34 Cool.
All right, well, very good, and a nice PR for us all to review. After the meeting.
Thanks, Erin. I have proposed at least two topics here. I would put Albert's most important, in mind, maybe a sort of footnote at the end, if we could, I think. And then if there are any other open PRs that are, like.
important that I'm not thinking of, that are new. Let's see, we've got the quiver, we've got the thing that I want to talk about, got the… well, at the end, the footnote, and then the other thing of mine is the batch processor. This is… this is Albert's… And I think the rest of this is… Maybe not something we're going to talk about today. So, Albert, and we saw some issues about this open as well. You've just opened this recently, and I'm excited.
**Albert Lockett** 18:33 Yeah, so, like…
**Joshua MacDonald** 18:38 I think that…
**Albert Lockett** 18:40 probably some of you have been following that I've been working on, a version of our query engine that can… Take the, the abstract syntax tree, the intermediate representation of our the transforms that we want to apply, and then apply them to, OTAP, batches, so we can do these transformations. And so, I've been working on this for the last few weeks, mostly related to, to filtering, and I thought that rather than, you know, keep going deeper on filtering and, trying to support, you know, more filtering patterns, it would be good to kind of integrate this into, into OTAP data flow in a processor, so… Originally I had called this the query engine processor, but thanks to some PR feedback, we decided that Transform Processor was probably, a more appropriate name, so, So this is, is now the… the processor that, we're calling the transform processor, and it's, like, when we go through the processor code here, it's, it's, it's pretty, bare bones. It, it just takes, a, a transformation, in this case, in basically, like, KQL, and then parses it into our AST, which represents the transform we want to apply, and then invokes that call in the query engine to, to apply the transform. And so.
Yeah, and so now, basically, you can use this. Currently, it only supports filtering.
There's an example configuration here, and an example YAML file, that… that you can see here, the… the example YAML file, what it does is it… the example config pipeline here, what it does is it prints… it generates, telemetry using the fake signal generator, and then debugs before and after the transformation is applied, out to a file, so you can see the before and after of the telemetry.
Yeah, so, so that's, that's, that's what this, this processor does.
again, I think that, like, some of the… some of the future enhancements and some of the, issues that I, that I opened. So one of them would be to, validate the, the pipeline definition of the transform eagerly. So right now, what happens is we parse the KQL, and then we have the definition of the pipeline, then when we see the first batch, it does all the planning and creates the data fusion plans and things like that, and so… that is not great, because you might write a pipeline that has some syntax that we don't yet support in the column recovery engine, and you won't know until the data starts flowing, and by then, you're already dropping things, so that sucks. So, that's something I gotta fix.
And then the other issue that I had opened when we looked at the issue backlog was to, extend the capabilities of the columnar query engine And by virtue of doing that, we would get new capabilities, obviously, in this… in this processor. And so, the next things I was going to add were to be able to rename and delete attributes. That's… that's something that we have expressions for in our, in our… expression AST, and that should be relatively easy to support, because we can just take the code that was written for the attribute processor and invoke it in the columnar query engine. So that's the next step and what I'll be working on, this week.
Yeah, so I hope that was an okay explanation of, of the work that I did, and what some of the fast follow-ups will be, and what was in the issue backlog.
Does anyone have any questions?
Or comments.
**Joshua MacDonald** 23:19 Super fantastic.
I know I've talked to Blanche about his, sort of also his exploration into the KQL and the parser, and how it's tricky to do validation when you don't have data types that are concrete, and you can do some validation, but not full validation. So, sounds like a legitimately complicated problem.
To do, to do.
**Albert Lockett** 23:47 Yeah, I think that… I think that there… there is a little bit of complication there, but, like, also, like, one of the reasons that, we do this… this lazy validation was like, the idea that I had in my head was that if you needed to create a DataFusion, like, physical plan, like an execution plan, you need the arrow schema, effectively. And so… And that's why we delay creating the physical plan until we actually see the data, but the validation that I would like to do would be, essentially, like.
looking at, even without creating that physical plan, looking at, like, the expression that we're going to do, and saying, can I create at least a logical plan from this? Because you don't need the data for that.
And then we would be able to inspect that and say, oh, you know, you're filtering by some predicate that we don't support yet, right? Maybe you're invoking a function, or you've had some math expression or something that's not supported yet, and so… I think that, like.
knowing the… the patterns of the transformation that you're going to apply, and, like, what the engine supports, I think that we can do that up front without even seeing any data. And so… so that was, That was the kind of, like, eager pipeline validation that I would like to do.
**Joshua MacDonald** 25:09 Very, I mean, it sounds really good, and I'm glad that you're on top of this.
**Albert Lockett** 25:14 Cool.
Yeah, so… I guess, if no one else has any comments or questions, I'll hand it over to Josh, who built something extremely similar, which is a really funny coincidence.
**Joshua MacDonald** 25:32 Yeah, I, so I'll go there first. I… I… I did some work today and yesterday, on this, so it's kind of quick and dirty. I did… I didn't do metrics, for example. I just… Sorry, this is the wrong… this is the wrong one. Since we're on the topic that, Albert just, mentioned, I'll go there first.
**Albert Lockett** 25:56 You can talk about that other one first, Josh. I didn't mean to screw up your agenda.
**Joshua MacDonald** 25:59 No, it's okay, it's okay, this… this is, like, almost the same, type of design, and it, you know, I think it's okay that we have two copies of this, and they don't need to be the same. This is… this is naming itself the KQL processor, and I… I've been talking to Blanche about doing this for a long time, and finally realized it was actually going to be very easy to do, so this didn't take too long, because the library that's been provided by Blanche for this is… just… takes OTLP bytes input.
gives you OTLP bytes output, so it was very easy for me to just use our current data types and, like, give the bytes in, take the bytes out, it was really simple.
So, So, this is, using something that's called the record set engine. It was interesting to see that we had essentially the same configuration, which is literally just a string. So here's the same thing in the KQL, processor, same exact configuration.
At some level, it's using the same parser, although I don't want us to get too down and dirty in the details there. The reason why this is exciting for me or for us here on the Microsoft side is that there are a number of existing uses that use exactly this language and exactly this, Sort of, construct. And so, the prototype we have uses this, sort of, I would call it… not… not, like, experimental, prototype-y in the sense of incomplete or, like, low quality, but this is, like, a exploration into KQL that, operates one record at a time, so it's called the record set engine.
What's… what's nice about this, is that you are able to write queries that, anyone who knows KQL actually is able to read.
And I put together, again, also a sample configuration that I thought was interesting. This is actually a pretty close to a real use case that we have, which is to say we're going to extend the body, if the event name is something that happens to appear in our test fake data, so I chose this as because it actually appears.
And we would append, like, a troubleshooting guide link or something like that, that says, for this specific error, here's the guide you need to solve it, so that we can ease our support burden.
So this is, maybe not meant for the data plane, but this is supposed to be very useful for our internal telemetry, at least for some of the product cases that we have.
And so, since we have it, I thought I'd put it together and just kind of make it work.
So yeah, that is, what this does. I put together a README that shows how to run it. There's a new feature flag to make it Work, but if you… if you run this, you will actually see that modified log body print.
So, enthusiastic about that, and it, and sort of alongside what Albert's been doing, this, this is a sort of… gives us a way to experiment with KQL over, I guess, SDK events.
Any… Conversation about that, that anyone would like to, have?
**Venkat Allam** 29:17 Yeah, very good here, Josh. Quick question. So this, processor also uses DataFusion for KQL parsing, is it… is it correct?
**Joshua MacDonald** 29:28 No, so we developed a KQL parser, and I know that it's, it's sort of, like, a little bit… more than Albert needed, so it's… there's a question of whether these two parsers are really, really trying to share the same code at this point, I believe, but this was a KQL parser that we developed in the Rust experimental folder of the repository.
And the idea that's being pushed here is one that you might know more about, but, like, there has been, like, talk of a kind of standardized unit telemetry query language, and if anything, we were kind of interested in exploring that. So this parser was developed to help us explore that, and now we have essentially two implementations based on it.
But Alberts is the one that uses DataFusion, and is, I would say, designed for high throughput.
realistic cases, and the one that I just shared is really, extremely capable, but, like, low-scale type of KQL. Very, very close to KQL, though, not, not, not something that's sort of designed, spec-built for open telemetry, more like what what, Albert's been, trying to accomplish with the records… with the Aero-based implementation.
**Venkat Allam** 30:51 Yeah, because I, you know, there is a Python library called IBIS, and which is, you know, based on a fluent API of, essentially, processing the data, like, on data frames, right, on error record batches. I'm pretty sure… folks in the Arrow ecosystem, you know, know about this.
Essentially.
**Joshua MacDonald** 31:13 IBIS? Like, I-V-I-S.
**Venkat Allam** 31:16 Yeah, IBIS framework.
IBIS-framework. Yeah, yeah. IBIS, a Python framework. That, you know, supports a number of SQL backends.
And… and for the longest time, right, I didn't have a lot of time, but… I wanted to create something like that in the Rust ecosystem, you know, using, data fusion, you know, because… with the parser and, you know, because it's extensible, we can support a whole bunch of things. It's very interesting.
**Joshua MacDonald** 31:56 Thank you. I am… I'm, let's say, an observer of this. It's also, I think, an exciting development. I know there is a meeting that has been carved out in the hotel's calendar for this type of discussion exclusively, and I don't know if it's been super popular, but, there might be room in this meeting here to talk about it, and or if you'd like to, maybe meet, this fellow Blanche I've referred to now several times, he may be able to meet you in that meeting as well to talk about this topic.
**Venkat Allam** 32:34 Yeah, sounds good, Josh.
**Joshua MacDonald** 32:36 Or you can reach me on Slack, and I can help guide that conversation or get you introduced to the right people. I think we're all excited to have more ways of, I guess, you know, building telemetry query. May they all succeed.
But, but I, I will say, whenever, I've heard more than once someone say, there should be a Python scripting language, because, like, that's a language that so many people know, and, like, SQL's pretty hard, and who cares what KQL is also very hard, and Anyway, these are query languages versus, like, a kind of programming language approach, which may be interesting.
**Venkat Allam** 33:16 Yeah, and I'd like to, you know, add and then conclude this discussion. So, I understand, you know, KQL, As a query language. You know, it kind of… promotes this imperative way of, you know, describing these transformations, just like the DataFusion, DataFrame API. So this IBIS is also like that. And, you know, you might have come across, something called PRQL, that's also very, you know.
Oh.
orthogonal, like, you describe what you want step-by-step, and the latest developments in the SQL, you know, SQL area with the pipe syntax, right? It's basically describing in a sequential manner, what you want, and so being more… declarative, right? So that kind of actually helps more with, With the open telemetry, you know.
pipeline, right, because… we won't… We're already in that sequential mode of thinking, and we don't want to introduce something that's more declarative.
I don't know, just an idea.
**Joshua MacDonald** 34:36 You're saying the IBIS framework is more imperative and less declarative, I think.
**Venkat Allam** 34:42 Right, right.
It's, the way we describe operations on top of data frames is essentially, you know, we go step by step.
And those… those can be chained on top of… Essentially compost, right?
**Joshua MacDonald** 35:01 That's… that's definitely the aim, I know, behind the language that… that has been… well, Laurent has spoken about, and Albert knows about, and we've discussed briefly in this meeting, a kind of hypothetical open telemetry language.
That is kind of fitted really well with the OpenTelemetry Aero model. That's kind of our, I think, the concept.
And I, again, you know, then, therefore, with data fusion, very natural to express declarative, types of query.
I… what I heard a little bit of what you're saying, and I think we are familiar with the systems you named, PRQL and the Google's pipeline, SQL and stuff, I know we've, like, done some, you know.
research on that. But I think that users might find a Python interface, like many of the Python programmers in the world, would then feel comfortable just saying, record in, modify, modify, modify, record out.
It's interesting to hear you say this for me, because there's been some debate over whether we must have a simple API, whatever simple means, and one way to think of what simple means is to have the data essentially map one-to-one with an OpenTeometry protocol message.
We're all very familiar with OTLP in this room, and so you… and there's a natural protobuf compiler output, which is the objects of the protobuf. That's one simple way to talk about, here you go, you want to do a processor call? I'll give you a protobuf, you give it back to me, and we're done. That's easy, simple.
That's the simple protobuf format, and I think maybe what I'm hearing us talk about right now is the simple column-oriented format, which is not a sophisticated query language, but is simply a data frame in, data frame out.
If that's such a thing.
**Venkat Allam** 36:54 I agree.
**Joshua MacDonald** 36:55 Maybe it could be done in Python.
I… my personal interest in this area, since we're here and talking about big ideas, I… I'm… this is… I keep giving this to Laurent as, like, a nice-to-have feature, is a Prometheus query implementation. That is a PromQL.
I know we have parsers out there. I know Albert knows I want this, so I won't say much more, but I think we… OpenTelemetry will have reached a major milestone in its evolution when we can do Prometheus.
**Venkat Allam** 37:24 So, I already have a solution for you. So, you guys have already seen the GraphtaMDB folks here. So, they have a Prometheus parser that actually uses data fusion.
**Joshua MacDonald** 37:40 I think someone, it could have been you, mentioned this once before, I went looking and couldn't find the data fusion, I only found the parser, but I'm still excited by it, whatever it is.
**Venkat Allam** 37:51 Yeah, yeah. They, they, they do have the Prometheus, So, Prometheus already has this, these definitions for, what is it called, the… The parser generator.
Right?
And then that, actually gets used to generate, some code, and then that eventually produces a data fusion logical plan or something like that. I didn't go looking for that, for that. I, I might paste a link in, in this com… in the Slack chat.
**Joshua MacDonald** 38:29 Well, anyway, that sounds like part of the future that I want us to have.
Definitely. When we can do a recording rule in Prometheus language, or, you know, a standing query in many of the other types of, like, system language, that'll be a major, major, major accomplishment.
And so this is a great place to talk about it. If you're… if you'd like to, like, get together and talk more about the low-level details of KQL, I can… I can arrange that as well.
As far as agenda, the one that we haven't covered now is this one. It's, again, one of my PRs. I do think it's worth everyone knowing what's happening here. I did file also some issues about this. It is… the reason I decided that this was really worth doing, now is it seems like, you know, there's a lot of uses for just a pure OTLP bytes pipeline. The KQL query engine I just showed you, again, uses OTLP bytes, and we've got, at the same time, the batch processor that we had was written using the arrow representation, so I will call it fairly complicated. Like, this arrow batching logic is looking at a set of arrow batches, or hotel arrow batches, which each includes multiple record batches.
They're optional… there's optional fields within those optional record batches, and then they've got parent IDs and child IDs that have restrictions of range, and so it's all quite complicated. So at some level, what I wanted was to de-risk. I know how to batch OTLP bytes, it's super easy. You concatenate the two requests.
I didn't implement something quite that simple, I implemented something a little bit more sophisticated. The… the… I guess the most important part, here is the batch processor has some changes which are related to configuration. In my recent work, what I had done was made it so that the batch processor follows the newest conventions in the Go collector. So you have a min size, a max size, and something called sizer. I'm gonna… and I've now, So we have a sizer method that was added recently. It says that, your configuration can name min-max items in terms of requests or items or bytes.
This PR, replaces a single configuration that was the min, max, and sizer with a new configuration struct, because we're going to have two of these now. So, you can have, the… this is the batcher config, just has a min items, max, or sorry, min size, max size, and sizer.
there's now an OTAP configuration and an OTLP configuration, they're independent, and there's a mode or a format option, which is set to OTAP or OTLP or Preserve, and it'll implement either or both, according to this setting. So, if you set it to Preserve, it won't modify the data.
and it will pass through as OTAP or OTLP, and in case we find, like, bugs, and the batch processor is on fire with OTAP because of the… because of it, we can switch you into OTLP, and you'll… you'll at least have a simpler batching algorithm.
There's… so, this is… You know, I did it using a trait, and I convinced… I did some things with lifetimes, and named lifetimes, and it's very exciting for me to do that.
But it worked out. So now, the… there's an implementation of this batcher API that's for the OTLP bytes and for the OTAP arrow records, so that we're not duplicating a lot of code. And then… If I may, the original OTAP batching logic is still here, but I named it MakeItem Batches, because it only operates in items, and the higher level code will check you're only calling items if you've got an OTAP configuration. And then there's a new implementation, which is the OTLP Bytes Batcher, and it is, delightfully simple compared with anything else in the OTAP implementation. So, you know.
the major data type here is OTLP protobytes. You've got a slice of those, and you're going to output a slice of the same thing, or a vector of the same thing. You know, you… the simple case is that There's no limit, so you're going to make one batch, which is just concatenate them all, like, that's… this is it. This is the entire batching algorithm right here. For the case where there's a max, and you're… and you're trying to limit the maximum request size, this… it's a little bit more complicated. It steps through the top-level fields.
Use the same code for all the different data types, because they're all protobuf, it doesn't care what protobuf, it doesn't validate, it just concatenates fields. So this, has a few lines of proto-specific code, and that's kind of about it.
There we are.
