SIG: Arrow SIG
Date: 2026-04-21
Duration: 58 minutes
============================================================

## Zoom Recording Transcript

**jmacdonald** 00:24 Hi, everybody.
Hello, everybody.
Let's see, I copied this.
Just gonna delete people who aren't here. Drew can't make it today.
Cut Aaron.
Got Jake.
GEICO can.
Welcome, everybody. The notes document is, here, and now I'm going to put it in the channel, and you can see it. Please add your name, please add your agenda items. We'll start in a few minutes. We're gonna walk through the, issues. Last week, we got through 2687.
And… I will bring you there.
I started noticing a trend while we're here, that the number of issues tends to be about 10 times the number of pull requests. So, if you're gonna open new issues, think about adding a pull request. Or if you're gonna add a new pull request, think about new issues.
At a ratio of 10 to 1.
And the last number was 2687… Great. We have less than a page, because it's the short interval.
2687 has closed.
Or into what I can tell.
And we're looking at… all the issues starting with 2689 Starting with one from Albert, and going through one that I filed a few minutes ago.
Let's see, how are we on attendance? Who's here, and who wants to be here?
don't see Laurent yet. I think we should just start.
If you do object, please say so.
And, okay, we'll work backwards.
And we're going to do the bulk update operation that I saw last time.
I don't know if I see Albert. I can't put him on the spot. Albert has one about Logs Body Field. We've seen some of those PRs, they look good to me.
All looks well.
There's one that I know Drew wants us to look at, so I'm gonna pull it up.
This appears to be a bug report in how we are measuring compute time. I believe it's just the omission of conversions that happen into this sort of try into And he has some data to prove it.
I know he couldn't be here today, and I know he wants us to talk about it, so here we are. It's probably worth saying that Drew has this, long-running PR that's been open and received, I would say a large amount of feedback this is As you see, there are a number of conversations And… Is this the second implementation of Drew's work? Yes. The original one… It's funny when they're off by a round number. It was 2569, not 2669.
More conversation here. If you're not following, you can go see it there.
Laurent has joined, Albert has joined.
Budkarsh is here today. I know Drew couldn't be. Does anyone have an update that they'd like to share about Drew's work with the chain inlined or otherwise?
**utpilla** 04:56 Yeah, I think, like, I just had one, update. I haven't… I don't think I've posted it on this PR, but… yeah, like, there was… there are ways to do this, I think just at an engine level without each processor getting involved in the… computation directly. Similar to what, Josh, you had done for the compute duration for process, we can Extend some of that logic to… calculate these, metrics. But then, yeah, it doesn't help with, memory reduction. So if memory reduction is also a goal, then, yeah, I think then we have to do chaining, but I think there are some other problems with chaining, which are mainly, like.
you can make it work only for, like, good… good nodes, like, nodes that have actually implemented it well. If somebody has a… there's no way to statically tell if a processor is only going to emit one data out, or, like.
We'll have a one-to-one mapping from… for the input to output.
So, if any processor… if you have a buggy processor.
puts in more values to the queue than it receives, then it's tough to, like, statically find those things, and then you will run into these bounded memory and unbounded memory issues, so… Yeah, I feel the validation part is going to be difficult in the chaining approach.
Yep.
**jmacdonald** 06:26 Thank you.
Yeah, I know, I feel like the memory usage argument is important, but I've also had this sense just sort of, like, this is a lot of work to imagine doing just for a new measurement, and we could, you know, kind of using these examples right here, imagine… I can imagine, like, a sort of, like, an instrument that you would say, I'm going to trigger the start time when I see the classic receiver, and I'm gonna trigger the stop sign when I see classic insert B, and it… and then I know that when I see it pass through the first component, I start my timer, and then I… second time… second component, I stop my timer.
That's a little bit complicated from a metrics perspective, but, not… not impossible to imagine.
With that said, I know that there are other reasons to go for a processor chain.
**Laurent Querel** 07:22 Yeah, hi everyone, sorry to be late.
I didn't review the last version of this PR.
The… the discussion about, building data structure, so when… We could imagine that we… we should not be in this position where Oh… this chain introduced something that is worse than what we can do already today. Today, we have between processors, two input channels that are bonded.
And at the minimum, one bonded channel. Could be multiple if we have multiple output for this processor.
So the, the, the sizing of those, channel are… There is a maximum specified at the configuration level.
I don't think… I don't think that we will have If… what we could achieve, if we have this inline processor, constrict.
I agree with, with Karch that a processor could generate more than… in fact, it could generate zero, it could generate 1, or more than one.
Otap pilot, object.
But, we could limit the number of, What this processor is generating, anyway, at the same… with the same mechanism that we do for the channel.
And if, some processor tried to generate more.
We could imagine that, is blocked, to the, to the maximum. When we reach the maximum, it is blocked, and, and the corresponding buffer needs to be, Emptied.
So the… And so basically, this chain has… is a list of processors when we are… At the semantic level, we have some kind of loop.
And we… and we, go over this loop of, this chain of processors, and we take the outputs. The output need to be… The number of entries into this put… in this output need to be, controlled with a maximum. The benefit is, most of the time, we will be able to just, Take the input… the output of one, and put that in the input of the other one.
Or to iterate over this second processor, take each of the output of the previous stage, and enumerate the corresponding. But we… I think we can implement something where the maximum is still enforced.
I don't think that magically, this, this thing disappeared because we, we have, an internal chain.
**jmacdonald** 10:43 Yeah, it's true. Also, as we know, there's a policies object which sets the, sort of, default sizes of various things, and there's one for the node level that's… or for the pipeline level that says.
I'm sorry, or for the group level, that says the pipe… the P data channel size. And in some sense, if we really just want to save memory, we could lower the channel size to 1, for the chain that Drew is imagining here. And that would let you have one output from each processor, and it would force you by blocking to, like, reschedule the task.
So, it sounds like both… in both this, sort of.
Both benefits that we've discussed here could be achieved on their own through a simpler mechanism.
That's maybe another reason against these two drafts. The second draft, Laurent, that you haven't seen here, is it uses a trait to sort of specialize, and…
**Laurent Querel** 11:38 Not a big fan.
**jmacdonald** 11:39 Yeah, I'm starting to not like any of these approaches, to be honest. It's easier to say that without Drew here.
Maybe we should revisit this stopwatch idea, but I think I will be able to report back to Drew what we discussed. And I think we…
**Laurent Querel** 11:56 I can't remember well, Drew mentioned that, he… He figured out a way to keep the exact same Basically interface for the processors.
**jmacdonald** 12:09 My understanding was the first attempt did that.
I don't know if it's… Easy to see here, but let's… let's move on. I think we're gonna.
**Laurent Querel** 12:18 Yeah, yeah, I think we need to have a discussion with Drew and look at the last iteration, and… And try to have a discussion on top of this last iteration in order to, To determine if it's a direction that we would like to implement right away, or… or if we need to just answer the initial requirement, which was, if I understand well, Having the ability Because the initial requirement for… on your side, Microsoft's side, was to have some kind of… aggregated matrix.
Combining multiple metrics from multiple processors in order to Let's say, hide a shell of processors, From an external, observer.
That's my understanding, basically, of what you want to achieve, right?
**jmacdonald** 13:13 That's right.
**Laurent Querel** 13:14 Okay. And then we end up with value subscriptions, which, and the one that we just discussed.
The creation of an explicit chain of processor As other benefits, potentially, related to memory consumption, with a side effect of generating an aggregated matrix by design, because we also have metrics related to this chain that will express, for example, duration and input-output at the boundary of the chain, and not individual boundaries for each sub-processor part of this chain. It's like leveraging the side effect of a solution To answer the initial requirement, which could be fine, but if we have some difficulties.
In terms of generalization, maybe we could think about just solving the initial requirement and taking more time for… I'm not… I'm not saying that it's necessarily… that the last situation is necessarily bad. Probably it's… Maybe good, but I think we should keep that as an option.
**jmacdonald** 14:30 Yep.
Alright, I made a little note there, and I will follow up with Drew.
Okay, this one I know is also sensitive, and we do, I think, have Lauett on the call, maybe coming in and out. So this one is, you know, eventually we need to start publishing crates, and, like, maybe what we could do is start small by having a single crate. This is what Lawett proposed.
There is a bigger issue, of course, that's like, let's publish all the crates.
And I haven't followed this discussion.
Without Drew… Okarsh, do you have any follow-up here? I see you're commenting on this.
**utpilla** 15:17 Oh.
No, I think there was just a question for me. I had created the issue for the async abstraction, and I think Drew just asked me a question on, like, whether this matters. It doesn't matter for the first initial pre-releases.
the issue that I have for async runtime abstractions?
It's more of a 1.0 blocker.
**Laurent Querel** 15:39 So the… the initial, so that… okay, so… So, the initial requirement expressed by Lalit was Having a crate or tap views that could be used in various contexts.
Potentially not necessarily directly, And let me know if I'm not going in the right direction.
I need to read this description, maybe, to have a good understanding. Okay, open telemetry REST contribib… like to depend on OTAP views to… to process OTAP messages. That's what we need to understand.
**jmacdonald** 16:20 Yeah, so what we're doing is we're taking, one of the… the Geneva exporter is handing… is handed an OTAP P data object, and the goal is to… to use a view to iterate through it without copying it.
And we have this shared code that the Rust contrib for the SDK also uses, which happens to be where it's currently housed. So… if we moved it, the Rust contrib would still need to depend on it, so that's why, having a common location would help.
**Laurent Querel** 16:53 Yeah, that seems reasonable to have.
**jmacdonald** 16:59 I'm, so I… the only question I've been having for this is that, currently, maybe the proposal is that we use this OTAPDF prefix.
For this specific case, we could call this part of the OpenTelemetry crate prefix that already exists, and already has, like, a publication flow, or already has some crates published. So we could call this the OpenTelemetry OTAP views, and then just not call it part of this project, but call it part of the OpenTelemetry SDK for a while.
That would also address my desire to combine our two protobuf The two pro-syntonic-generated codebases are different right now, but it's only creating problems for us, and probably two copies of a protobuf library.
**Laurent Querel** 17:48 I mean, we had this discussion having a prefix for the crate.
That will basically scope, each of the crates we have in the project.
with something that will be meaningful and recognized by users. So, obviously, OpenTelemetry Dash will be, A good fit for that.
Because OTAP is, is like, well understood by us, but not necessarily very well known by the rest of the world. So, But in this specific case, we are talking about OTAP views, so OpenTelemetry-OTAP-views will make sense, and we could have open telemetry-OTAP-engine.
For example, to represent the engine that is able to To process pipelines that are natively designed to To, to, to, to, to exchange OTAP messages across nodes that are part of the same pipeline.
So the open telemetry is the prefix, it's not hotel, in the… in the existing, creates that are currently published by the SDK. Okay.
**jmacdonald** 19:05 Yeah.
I guess the real question here is what's blocking… what's the hard blocker for us? And maybe the answer is nothing, other than deciding on that prefix for the first crate, and I think… You know, someone might say that we need to ask a higher power, and, and, like, we could go ask you know, OpenTelemetry as a group, the GC, for example, do we have permission to publish OpenTelemetry OTAP stuff now?
And I bet the answer will be yes. I can take that up if you think I should ask.
**Laurent Querel** 19:39 Yeah, and I think we can… decouple the… the, the, the, these, Decision of using the same prefix from the decision Of which crates we have in the project that are ready for such publication.
So we, we could start, like you, you, you are suggesting, we start, small, and And we control what we publish.
If the views Or something that… is anyway useful because it's shared across multiple projects. Let's start with that and making sure that We, we deliver a crate.
Where we are confident enough in the… at the API level.
Even if at the beginning it's not necessarily a 1.0, it could be a 0.something, because anyway, I think Geneva is also a 0.5, If I… if I read correctly, so… But at the minimum, we have, we are satisfied by the API. Maybe we will do some changes, but not dramatic changes.
**jmacdonald** 20:53 Okay, I think we have enough… decided at this point to do something, and to me, it involves moving a little bit more than just the OTAP views, like the proto directory as well.
Okay.
Lauett and I will talk about that one, soon.
Okay, so where were we? We were right about… here… 2691. I got the next one.
I'm trying to ban OpenSSL. As you may know that we were having a very slow build time on Windows. It turns out to be because of an OpenSSL sys crate, which will just try to install OpenSSL, which it does by compiling it. So we found, essentially a 7-minute build step that was just to compile OpenSSL, And it's coming in through Weaver, and what I learned last week was, wow, this world of choosing your crypto libraries is really hard. But now I know this. So… after we fix some Weaver things, we should be able to remove OpenSSL. And then I think we can ban it, because really… you should choose the native crypto, or you should choose the Rust TLS, and you should choose one of the cryptos that you explicitly choose.
But you should not build OpenSSL from source, no matter what.
**Laurent Querel** 22:16 There's a chance.
**jmacdonald** 22:17 you.
**Laurent Querel** 22:17 Yeah, I'm not necessarily the best for this topic, but the question I will have is.
Do we cover all the… the scenarios for people that need to be FIPS compatible.
Let's say they have, their own OpenSSL stack that has been, That is compliant with FIPS.
Yeah. They are satisfied by it, and they don't want to change. Will that be… oh, yes, that will be probably the native one.
**jmacdonald** 22:54 I think this is what you want for that, but we definitely are pointing at this one. We covered that one last week.
So, I agree. If someone really wants OpenSSL, they probably really want it, but they probably won't get it through building the source mode.
And we… we shouldn't… we just really shouldn't be building… In our CI pipeline. Okay, thank you.
Oh, my back button is totally not working.
So Lalit, again, has filed an issue about a project that we are beginning here. This is user events, the Linux equivalent of ETW, if you're… And so we want both of those, or what some people call flight recorder mode, like.
High-volume logs through the kernel, that are common in all these places.
So, we're interested in that. If there's any comments, please let me know.
**Laurent Querel** 23:55 That's super nice. But I have a question regarding the user event for the Linux.
user event.
It looks like there is this concept of a schema.
I remember reading some comment about the Microsoft schema thing.
Could you elaborate a little bit more? Because we… I think we need something that is, general, and not necessarily… tied to, to any kind of Microsoft schema. Is it something that will be supported by, at some point by this, Linux user event receiver, or… There is some complexities there that we require to… to extend.
**jmacdonald** 24:43 The way…
**Laurent Querel** 24:44 in some way, how that works.
**jmacdonald** 24:46 I might invite somebody else to answer this one if they'd like to, but the way I understand it, the mechanism is built with parity for ETW in mind, and there is a type and a schema, like, associated with every specific source.
That's as much information as I'm able to come up with off the top of my head.
while it's not on the call, does anybody, want to volunteer information about either question? This question? I think we have more ETW experts.
And I know it's supposed to have pairs.
**Laurent Querel** 25:22 Otherwise, I can add my question into the… The thread of commands for the corresponding, GitHub issue, but my main question will be, basically, if we… we want to use this receiver in the context that is not Microsoft. There is someone with an application using the Linux user event, generating logs that are structured.
Following some schema.
how can we basically configure this Linux user event receiver to comply with the corresponding schema? Is it something that will be feasible? If not, then I think that should be a Microsoft Linux user event, but not a generic I mean, I would prefer definitively a generic one, but .
**jmacdonald** 26:15 I think it's generic the way you want, that… and we can follow up on this, but my understanding of the way user events is designed is that the trace point, whatever it's called, will Declare its own schema, which is really just a mapping of field name and type.
And, and it's, So that when you begin consuming these events, whether it's user events or ETW, you will, receive Effectively, through the descriptor or the handle that you have, some sort of information about the type and the field names.
So that it's not specific to Microsoft.
**Laurent Querel** 26:57 Okay, sounds good.
**jmacdonald** 26:59 Hopefully I understood that correctly. We'll follow up.
This is more, me talking about the Windows build time. Let's not talk… let's not dwell on it, but right now, I have broken the build… I've modified the Windows CI to only build certain targets, and this is to say we should go back to building all the targets, which takes 7 more minutes, essentially, through the Weaver dependency.
Yeah, that was fun. Okay, Aaron has a point about an unnecessary copy.
Anything you'd like to add to that, Aaron?
**Aaron Marten** 27:42 No, not really. This was, actually, credit goes to Cars for pointing this out to me offline.
**jmacdonald** 27:47 Okay.
**Aaron Marten** 27:47 typed up the issue. But this is basically an optimization. However, we're doing a copy where we don't need to be doing it. We could… we could get a zero copy here. There was somebody else, from Microsoft who's a new contributor who, I think has already submitted a PR to incorporate this, so I will… I'll take a look at that and leave some feedback in the.
**jmacdonald** 28:05 hot.
Here, perhaps.
Great. Guillermo. Alright, sweet.
Very good. Okay, moving forward, Chanley is working on the validation framework for transport headers.
**Laurent Querel** 28:23 Yeah, so the… Recently, I think it was 2 weeks ago, we, we added into the OTAP letter message.
which is the wrapper, basically, to represent any PDATA message.
traversing the DAG, there is… we already had a context, there that was mostly used, for example, for the the framing for the ACC subscription mechanism, but, we extended it with the concept of, headers.
So we have a headers extractor at the receiver level, that could be implemented by any receiver, and they can feed, basically, this part of the context with the extracted headers, and then we can, propagate the headers at the exporter level if the… the corresponding exporter support those headers. So the… I think the idea was, how can we validate the extraction and propagation with the validation framework that Shen Li implemented? So that's nothing really super fancy, but extending the framework to support new capabilities.
**jmacdonald** 29:41 Good.
Very good.
Chan Lee was unmuted for a second, but you spoke instead, that's great.
**Laurent Querel** 29:49 Sorry, I was thinking that Shani was not there. Yeah, so…
**Chanly Ly** 29:52 You're good.
**jmacdonald** 29:53 I'm kidding.
**Laurent Querel** 29:53 Sweet.
**jmacdonald** 29:55 Thank you, Chen Lee. let's see, Jake, I want to hear about this one.
Jake said… Jake also has said he's on the move, so maybe he can't directly comment.
**Jake Dern** 30:05 Yeah, I am. I'm… if it's too noisy, just cut me off and let me know.
But, there's kind of two things on this front.
The main one is that there's a bug inside the reports, so we're just kind of looking for a wrong, like, time window, and that's causing inflation by, like.
15-20%, depending on the duration, like, the observation window, whatever benchmark or whatever. Then the other thing is the fake data generator, it doesn't always do the best job at Reporting its metrics, and, like, and also, like, exporting its data at a really even rate. I have a draft out for this.
**jmacdonald** 30:40 It's amazing.
**Jake Dern** 30:40 take a look at both of the shoes, but, yeah, we should be getting it pretty close, after that.
**jmacdonald** 30:46 Great. Yeah, I noticed this funny little line on the benchmarks, you know.
And I wondered what that was, and I suspected something was off, with the.
**Jake Dern** 30:56 Yeah.
**jmacdonald** 30:57 Yeah.
**Jake Dern** 30:58 This was, like, so the funny line, that was related to three fixes that I made last week, but there's still some issues there. So it doesn't say negative 1000%, now it says 100%, which is still bad, because we're missing 100% of our logs in this case, but accurately missing 100%, whereas obviously we were never missing minus 1,000, so…
**jmacdonald** 31:17 Alright, thank you.
**Jake Dern** 31:18 One problem at a time.
**jmacdonald** 31:19 Okay, sounds good. One more about crypto. This was… Aaron had a PR about it, and I closed it saying I was gonna do it, and then I realized how hard it was, so I just filed an issue instead. This is yet another kind of, like, alignment problem between all the various crypto libraries.
and all the various TLS libraries, and you have a cross product there of all the various things times all the various things.
I feel like I entered a new learning curve for Rust last week, so I found this one.
Anyone who wants to learn this stuff can. I won't click into that.
Lowett has one, about… Retry, and this is one I'm familiar with from the Go Collector as well.
This is probably connected with the issue that you were mentioning, Laurent, about, structured NACs.
**Laurent Querel** 32:14 Yes.
So there is a comment, basically, describe… so…
**jmacdonald** 32:21 this one.
**Laurent Querel** 32:21 So when Lalit created this entry, we were, in a situation where basically the NAC message was only a reason, refused and, unwind and permanent, these, four fields. And, in between, we had, I introduced… this concept of structured, NAC, where we have a cause, and the cause could be today, We have a nag because the route is full, because the route is closed, or because we are shut down… we shut down the node, but we could introduce there additional cause that will be, for example, a retry after.
Oh… we need to figure out what will be the best model for that. But, Yeah, so we… now we have structured NAC, we just need to figure out what will be the… how we will put the retry after in this, structured NAC representation.
**jmacdonald** 33:24 As well, we have a question about whether permanent belongs.
**Laurent Querel** 33:27 Yes, indeed.
**jmacdonald** 33:28 in the Natcause as well. So if you feel like talking about that one, join our issue here, 2718.
We almost made it. Aaron, we… Aaron deserves a round of applause, everybody, for starting a flaky test automation process. Thank you, Aaron. This was one of our first reports.
**Laurent Querel** 33:49 Yeah. Right.
**jmacdonald** 33:51 Everybody clap, alright, cool. This is really great. I think the title will be better after the next, iteration. I know that there were a couple fixes already.
But yeah, this is great. And then… I suppose we should actually assign these issues to somebody. Oh.
Lowett, again, not here, or I'm gonna name him. Okay.
**Aaron Marten** 34:14 So.
**jmacdonald** 34:14 And it fails in both places.
**Aaron Marten** 34:16 One thing that I guess I'll ask for feedback here on, too, is right now, this is just going to be running every night, and it'll be updating the body text on this one issue.
**jmacdonald** 34:25 Okay.
**Aaron Marten** 34:26 We could change the workflow so that it, you know, files new, separate issues for separate tests, but I figure we can start with this and then see how it goes.
**jmacdonald** 34:34 I kinda like it this way.
**Laurent Querel** 34:36 Yeah.
**jmacdonald** 34:37 I see, so this is the title. This is gonna be the continuous running, all… all issues, up to date.
Sounds good.
Cool. All right, well then check back here. We… maybe we should pin this one for a while.
I'll figure out how to pin this.
**Laurent Querel** 34:55 Just a question for Aaron, how hard that will be to generate this report into the Slack channel?
**Aaron Marten** 35:10 I don't know, I can look into that, though.
**Laurent Querel** 35:13 Thank you.
**jmacdonald** 35:14 Let's ask Trask for help, I bet he knows how to do that.
**Laurent Querel** 35:18 Just throwing an idea, not necessarily, I mean, I didn't think about it too much, but I was thinking that If we want the… I'm not looking at the GitHub issue every day, that's, but I'm looking at the Slack channel every day. So if we want to maximize the chance to having someone fixing the flaky test as soon as possible, maybe the Slack channel will be a good, A good approach.
**jmacdonald** 35:54 Alright, well, for now, it's pinned at the top of the issues list.
You may have noticed I just unpinned a couple of issues that were kind of stale.
**Laurent Querel** 36:03 We have some work to do.
**jmacdonald** 36:04 on our next milestone, but I'm aware of that.
Yeah. Last one here, I filed this one. I was, Well, I was looking at this issue, I should have connected it. It's about our SDK, and about how we allocate when we log, and I was trying to, like… the protobuffer object that we have is the reason why we're allocating, and This is not the highest priority, but I… I was looking into it, and when we have, like, an impulse try from block, like, there's no limit on that OTLP protobuff, so you could end up with… Some sort of, like.
decompression attack, where, you know, an arrow record batch comes in, and then you try to convert it into OTLP, and it becomes huge. And right now, there's actually no limit. However, there's a technical limit that we should have, which is there's a 4-byte placeholder, and that's, you know, quite large, 256 megabytes.
So right now, if you… if you tried to write larger than 256 megabytes, it would… it would be corrupted.
So we should limit there, but… I… I kind of think that that's unreasonable, and I'm not sure that anyone wants larger Then, if you imagined a smaller limit, but then it's… it's something we might configure, but, you know, there's no configuration anywhere in this input block. This is just a conversion routine.
So I don't know if we wanted a fine-grain or configurable limit how to do it.
Any thoughts?
**Laurent Querel** 37:34 Yeah, definitely we need to address, this kind of issues. For me, in the, at the gRPC level for, for Tonic, we already have I think we already handle… not 100% sure, but I think if I remember well, we already handled the situation where we have a boom, Don't remember the exact name of this attack, but bomb compress attack, or something like that.
**jmacdonald** 38:03 From, yeah, Zip Balm or whatever, yeah.
**Laurent Querel** 38:05 Yeah, zip boom, what you are seeing there is more, It's not related to compression, but it's related to… A conversion from one format to another format?
**jmacdonald** 38:23 That is why, I mean, that's the one place I've seen it. I know that there is some other code in our library that's, like.
The original code had a OTAP to OTLP protobuf message object. It also does this conversion.
Without any configuration or limit.
Yeah, so…
**Laurent Querel** 38:44 We probably need to come with our own trait to express that, because the trite form does not take any input.
So, and we don't want to have, I think what we have to avoid, obviously, is a global variable that will, where we will set that. It could be a thread level, That could work if, really, we want to use the thread, but I don't think there is a huge value to To reuse this one, we can just create our own.
**jmacdonald** 39:15 Yeah.
**Laurent Querel** 39:16 Price one.
**jmacdonald** 39:17 Mustang.
**Laurent Querel** 39:17 Limited, yes, and, and then.
**jmacdonald** 39:20 Okay.
That's useful.
Someone speaking?
**Albert Lockett** 39:25 I was just gonna say, I think it was maybe me who added that try-from implementation, and I'm not necessarily, like, tied to using the try-from crate. I think I was just doing it because it was like, oh, we're converting one type to another, and it might throw an error. It seemed like a natural usage of it, but, like, if we want to… you know, change it to use, like you said, another method called try from limited, or, you know, try… try to convert with options or something, like, I'm… I'm totally fine with it. So, you know, the… the current API isn't something that should, like, block us necessarily from some deep-seated API design that was done. I honestly think it… I didn't think through it that deeply.
**jmacdonald** 40:09 That's great.
Yes, that was my first thought, was I don't want a global, I don't want a compile time constant.
So some sort of options to act or limit, just… Hard-coded through configuration, or not hard-coded, but coded through configuration sounds good.
Well, we reached the end, very good.
And now, if anyone wants to put something on the agenda, it's a good time.
No one has.
Laurent, I know you were gonna try and, send out a live configuration PR, Anything to say on that topic?
**Laurent Querel** 40:50 Yes, I think I can, let me, Sorry, I didn't prepare very well this meeting, so give me… Hussegome, just to retrieve the… So, yeah, the next PR will be the 2618.
I made a demonstration last week, yes, this one.
**jmacdonald** 41:23 Okay.
**Laurent Querel** 41:24 So the last, last week was about, showing that live. So basically, demonstrating that we, we will be able to basically either scale up, scale down in number of CPU, any pipeline in the system, or we could, redeploy an existing pipeline with a new configuration. And, so basically this, this PR implements the engine side.
Of this, demo.
plus the… the admin SDK.
That will be exposed currently with an HTTP endpoint, so a set of HTTP endpoints That will give you a way, basically, to, To, yeah, we have here, shut… we can shut down specifically a pipeline, we can… Reconfigure, so there is a rollout, a rollout endpoint that will give you a way to specify the new configuration.
And then you will have a way to… you will get back an ID, That could be used, basically, to, Follow the progress of this rollout.
Or follow the progress of this shutdown operation.
So, that's the… this entire, thing. The… the client… The CLI that was part of the demo last week is not part of this PR, it's a separated PR that is not yet.
**jmacdonald** 43:06 Okay.
**Laurent Querel** 43:07 Even, it's still in my, private branch, but, I will, I will, I will work on that next week. So, my goal is tomorrow, maximum Thursday morning.
to convert this PR into a ready-for-review state.
And, if I can have some eyes to look at this PR, In order to… My goal is to merge that by the end of the week, ideally. We have some internal, let's say, commitment.
Oh… And, I like to have this thing merge by the end of the week.
If really we have some big issues, it's okay, obviously, we can, we can always, postpone next week, but, At least on my side, I will do my best to fix any issues that will be, reported.
So yeah, in term now… so there are… So the… I was hesitating between two approaches, and, so the… Live reconfiguration means that we need some kind of collaboration from every NUD implementation to behave properly For example, to implement properly graceful shutdown.
That's a minimal requirement.
we don't necessarily have this contract properly implemented, or validated, I should say, for every, NUD implementation that exists.
So… what I'm seeing is… We will have the, endpoint and the end… engine mechanic to, live reconfigure pipelines.
I'm sure that we will find configurations where, that will not work well. In my opinion, not because of a problem in the mechanic itself, but more the lack of, collaboration of the node. It's also a sign that we have some, probably, contract that needs to be a little bit more… Either enforced by typing, or at the minimum, validated by A test infrastructure that is not necessarily currently, Perfect.
So we, we, from, now a long time in this project, we have this test runtime construct that is used in various situations. I was thinking that at some point, the test runtime could have some flavor.
That will, validate The very common situation for any processor, for example, or for any receiver, any exporter. Typically, Is your component behaving well when you have a shutdown event, and you have a constant stream of inputs?
Or when the… one of the output is full. And that, I think, could be, We could create… we could create a test runtime Infrastructure that exercise this kind of, Situation.
And, and then, making systematic the validation of any node with this framework will make sure that The level of confidence of having any Any pipeline configuration able to be lively configured will be much higher than it is today.
**jmacdonald** 46:56 Got it. I tried to take notes, I think I understood, that we will move forward with live reconfiguration first. We will find problems with our queen shutdown and fix them as we go.
Anyone want to comment on this topic?
Not required. I was talking today about OpAmp with some people, maybe who are on this call, some of them, and I'm starting to learn more about OpAmp myself.
I… I… what I see, as a requirement emerging, I may as well say this right now, is that this client SDK that you've created is pretty essential to us. The op-amp project is pretty essential to OpenTelemetry, but what I think we're finding is that it's not essential for any particular vendor to choose op-amp when you could, for example, build a custom controller and plug it into the engine directly. And if that's the case, what I see as sort of offering build time features, which to say, which control approach would you like? You can have the plain old original admin component control that we have. You could have the new SDK, which is probably the lowest level, through a CLI that is able to speak that SDK, or something like that.
Or you could go with an op-amp component, where any vendor that speaks op-amp on the server can then control you through the op-amp client.
Or, you can bring your own, and that's… most likely what we would end up doing on our side, which is to say that op-amp isn't quite perfect for us, and if it's not being forced, we may as well just build the component.
Nevertheless, it will require us to bulk up and really understand this API for live reconfiguration. I think, what I'm saying is I think it's more important to do the API for live reconfiguration than to do op-amp.
**Laurent Querel** 48:55 Yeah, that's exactly the approach I tried to apply at different levels. So, we have a REST API, which is the lowest level of thing that does not expose on HTTP, does not expose on gRPC WebSocket stuff for OpenMP.
So it's basically a crate where we can act on pipelines and do something with it, and we can add an interface on top of it, I mean, a network interface on top of it. Then we have an existing list of HTTP endpoints.
which are the ones that we had historically, because it was easier for testing that through a broader, or for a curl command, or whatever.
And… and then we… what I did is created an admin SDK, and the design of this admin SDK At least the intent is to make it agnostic to the protocol.
So… you will not find into the SDK things that are related to HTTP code. You will find semantic errors that could be mapped to, whatever the protocol is, will favor to represent something that does not exist, or different things like that. So the client SDK is really there… you can provide a backend.
that could be an up-hump client, or that could be an HTTP client, and depending on what the engine exposed, like you said, we could have configurations or feature, if we want to implement that this way. And then the client SDK, could be configured to use the right backend, and communicate with the engine the proper way. But still, the… the… the… what we name the DFCTL, this common line I demonstrated last week.
should be able, I think, in theory, to use either the existing HTTP or the op-amp. At least that's the intent.
**jmacdonald** 51:17 Gotcha.
I think the high-level summary for me is that this looks like an extension point. One of the main extension points is, how do you control this thing? And it will be through a number of means.
Yeah. And probably for the large companies, it will be through specific internal means.
Yeah, well, there we are.
**Laurent Querel** 51:38 Occiosity, joshua, because you, you already, look at Hump.
And you said that maybe for the internal needs, you, you will not rely on Open. What are the… if it's possible to share that with us, what are the limits or the constraints that make you… Selecting a different protocol.
**jmacdonald** 52:03 Good question, and I will be careful. I don't actually know the total, the whole story, but… as with… As you can probably imagine, there are a number of global and regional load balancing requirements, and we don't think a WebSocket is quite the right approach.
**Laurent Querel** 52:28 Technically speaking.
**jmacdonald** 52:31 and whether there are alternatives that are not WebSocket-based, they might answer us… they might be the right long-term solution, but we know what our current agent control looks like, and it would not fit… be a great fit in a short term, trying to make OpenOPAMP work for us.
**Laurent Querel** 52:51 Okay.
Understood.
**jmacdonald** 52:52 I hope that's fair.
**Laurent Querel** 52:55 Yeah, that makes sense.
**jmacdonald** 52:58 Right.
Anybody else want to talk about OutBAMP?
You're not required to.
We may have reached the end, of the hour. We have a few minutes left over. If anybody else wants to, raise a topic, now's the time.
Otherwise, spend the extra minutes reviewing a PR in the repo, please. And thank you all. I'll see you next time.
**Laurent Querel** 53:27 Bye.
