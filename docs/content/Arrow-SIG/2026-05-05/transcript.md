SIG: Arrow SIG
Date: 2026-05-05
Duration: 67 minutes
============================================================

## Zoom Recording Transcript

jmacdonald 00:03:26 Wow, it's a big group.
Everybody.
Laurent Querel 00:03:32 Ew.
I was sharing my screen, Just to let people, add their name and, That's some, topic for the… for the agenda.
Wow, big group indeed.
Busy good.
Really cool. So… We need news… Oops.
So, is there any additional topics to discuss today?
In addition to this, so…
jmacdonald 00:05:14 I know you put up the file log receiver, that one's an interesting one.
Got some new people coming to hear about that.
And… I think we're all interested in seeing Jake's benchmarks.
Laurent Querel 00:05:32 No.
Definitively.
Okay, so let's start with the traditional triage. We will go fast this time, because I think we have a lot to discuss.
So I don't remember where we were…
jmacdonald 00:05:57 I think we were at $27.69 or so, because we did.
Laurent Querel 00:06:00 69?
Oh, 2769, so it was the first page. 27… 60… oh, oh, 69, okay.
Global tracing subscriber… conflict with embedding OTAB Dataflow as a library.
Not sure to understand this one. So maybe, Arun… is Aaron with us?
Yes.
Aaron Marten 00:06:31 Yes, I'm here.
Laurent Querel 00:06:33 Can you just, in a few sentences, maybe summarize the goal of this one?
Aaron Marten 00:06:41 Yeah, the goal of this one is we had a application where we were trying to include OTAP Dataflow, as a library so that we could, create an instance of the, you know, of a pipeline in our own process.
there is a, issue where, if… when you start up the pipeline, it will register a, global tracing subscriber.
Which, you know, would normally be fine, except for the fact that, we need to have a, Global Tracing subscriber registered prior to that, simply to get some of the early startup messages. So… Nice.
Laurent Querel 00:07:20 Yeah, I see.
Aaron Marten 00:07:21 So it's just, you know, resolving one of these kind of, like, you know, Contention around… around the global subscriber, and making sure that the host can get All the necessary messages for debugging.
Laurent Querel 00:07:34 Yeah.
I think that's a great example of, We have similar issues on our side. We use the… the OTA data flow engine, as a library, and we have our own system embedding it. And, extension points or insertion points, need to be improved in general. That's an example of it.
Yeah, definitively cool. We… I think we need to maybe open also, A document where we could make an inventory of the various extension points on which we need to be a little bit more, to apply the summer quatch, that would be nice to have that.
Okay, implement PLATAP, propagate it, stopwatch, so this one, Drew, I think we are in, it's already, Yeah, it's already accepted.
drewrelmas 00:08:36 So…
Laurent Querel 00:08:37 And, smirch.
drewrelmas 00:08:39 Yeah, I can say, a word about this. Initially this started as just the… kind of the simpler approach, compared to a full processor chain implementation. So, the first iteration is merged, which added a, stopwatch for measuring compute across a number of processors by tagging a time on the P data itself as it moves through the pipeline.
there is a second PR out, which I am, is in the merge queue right now, to add, Processor incoming items, or sorry, incoming items and outgoing items at the start and end of the stopwatch bound.
There's also been discussion on Slack that stopwatch isn't really a great word to use anymore if we're doing more than just timing. We're also now counting items and potentially counting… messages in the future, so once this thing lands in main, I'm going to be refactoring to call it, flow measurements, as Laurent, you suggested, over Slack.
And once that's done, it… we're in a pretty good shape, and I think I have what I need for my own use cases here.
Laurent Querel 00:09:59 Yeah, excellent. I think that's a very cool feature, especially if we generalize it.
I think that will be, really cool.
I still have to… To propose, some way to identify this, subgraph.
I'm pretty sure that the Kubernetes selector mechanism could be, an alternative. I'm not saying that that needs to be replaced by the one that you are already using, where you specify the beginning and the end of the… the subgraph notified by some node IDs.
But I'm pretty sure that we could imagine Other approaches, where we tag nodes And then we have a selector saying, oh, by the way, I like to have Flow measurement for this region identified by tagging.
Correct. Yeah. And overlap of, Flow measurement could have also, I don't see them as a problem. We should be able to have I mean, we have to discuss about that. Maybe close version, we don't have overlap.
At some point, maybe we could extend the mechanism to have overlap for something.
drewrelmas 00:11:22 Sure, sure. I mean, all… so, one note is, like, the… The item counting at the beginning and end is very easy. It doesn't require tagging anything on the P data. All that's tagged on the P data is the timing.
So, if we wanted to have overlapping, that's fine. PData just, will carry a list of times associated with stopwatch or flow measurement, config ID, or something like that, and each one knows to increment the proper ones at the proper time.
Laurent Querel 00:12:00 Yeah.
Okay, great, thank you.
Very cool feature.
drewrelmas 00:12:05 Not overlapping is definitely the easier case to start with, though.
Laurent Querel 00:12:08 Yeah, yeah, and I think we… that… that will be good enough to begin with.
And it… it's interesting… For your specific use case, it's interesting for troubleshooting, it's interesting for, in fact, many a many scenarios.
So that's when it was already, accepted. So, add the Windows ETW receiver, ETW receiver, I think this one is… We'll also, is there any, A specific thing that we want to discuss there?
it's, it's very close to the, the Linux user event, receiver that, on which, that it… that it is already working on.
Okay, better config time validation for overlapping, yeah, we just discussed that. Add time to processor missing configuration instrumentation.
drewrelmas 00:13:11 So this was an artifact back when I was actually depending on the times call to produce the composite.
But, that's no longer the case, it happens in the engine loop.
That said, there are a couple processors, specifically Transform, which I think should use timed, just as a best practice for observability.
Laurent Querel 00:13:33 Yeah.
drewrelmas 00:13:34 That's why I tagged this one, Help Wanted. It isn't a, it isn't a direct requirement, it's just a good thing we should get around to.
Laurent Querel 00:13:44 I need to look at this one, I'm just questioning the…
drewrelmas 00:13:54 If we need timed at all, or at.
Laurent Querel 00:13:56 Yeah, yeah.
Now that we have this more generic solution, I'm no longer sure.
Personally, for… just for the… For now, I will remove the help frontage.
drewrelmas 00:14:08 Sure, sure.
Laurent Querel 00:14:09 we put that back to Creaging.
drewrelmas 00:14:12 Yeah, I can…
Laurent Querel 00:14:13 And, deciding, I mean, and, and we will talk about that, in my opinion. Joshua, do you have a… Different points of view on that?
Yeah, we consider that.
drewrelmas 00:14:30 I agree with you on principle. I think if we make it automatic, it's one less thing for processor authors.
Laurent Querel 00:14:40 about. Yeah.
I think this one, Is school, and, maybe we… do we have, So, Victor, with us.
Yes, I am here.
Nice to meet you.
Victor Lu 00:14:56 Hi. Hi, Laura.
Laurent Querel 00:14:58 Hi, so, nice feature, so, can you maybe, just describe it, for sure.
Victor Lu 00:15:05 Yeah, sure. So, number one, I'll, I'll, I'll, proceeded by saying that I don't really know where it's supposed to go, but based on my looking at the code and looking at some of the existing feature requests, it looks like we currently today have a config provider for file and for environment, and recently they've been added for, like, a URI and HTTP.
So, what I'm looking, or to help with, is potentially adding something that's like a HTTP config provider, but the content of that config provider is more complicated than one simple request to one known endpoint.
Whereas the problem space that I'm trying to resolve is providing a config, but that… to retrieve the config requires multiple stages or steps, and thus I'm just calling it a more complex control plane.
you know, provider, a config provider.
Now, having spoken to Gawkin and others, I don't know where that fit. I've spoken to Josh, and now maybe they're saying that maybe this is more of an extension, or part of the extension work. But regardless, my goal is to be able to provide Something that will be able to retrieve a more complex control plane in a complex way, and then to be able to have that be distilled down to what is needed, either at the individual pipeline instance level, or potentially maybe at the engine, because it might create multiple pipelines. So, this is where I am now lost.
and need guidance.
Laurent Querel 00:16:49 Okay, great.
based on what you said, I think the next step would be to have a specification or architecture design step To identify at the end of the day, what will be the best approach. You mentioned, so this, HTTP config provider, you mentioned extension.
I think we need to figure that out.
Bursts, and, but definitely super interesting.
Victor Lu 00:17:29 So… Yeah, so I'm looking for, you know, someone to tell me where to go next, or how to approach, so…
Laurent Querel 00:17:38 Yeah, we can definitely discuss that, on the, Hotel AeroDev channel, or, with a subset of person, present on this, on this channel. Don't hesitate to initiate the conversation and, We… we can definitively guide you, and… and also, together, Reason about the best approach.
Victor Lu 00:18:05 That would be great.
Laurent Querel 00:18:07 Okay, so that is already marked, accepted, accepted, accepted, just going very fast.
Albert Lockett 00:18:14 Can I just say one thing about this?
Laurent Querel 00:18:15 Yeah.
Albert Lockett 00:18:16 It's like a bunch of.
Laurent Querel 00:18:16 mature.
Albert Lockett 00:18:17 the call. Yeah, so, for everyone who's on the call and, like, sees all these issues related to query engine, that I've marked, good first issue and help wanted, especially the ones related to adding support for new functions, so the ones that are part of the EPICT 2818, If there… like, I see that… I see there's some new people on the call, that's why I'm saying it. If anyone is, like, looking to get involved and thinking, hey, like, is there something that I could take on as a way to, like, introduce myself to the… to the process of, like, working on Hotel Arrow, adding support for some of these functions might be really good ones.
We see that on 29, or 2819, there was already a, a function, or a PR that was, that was added, and then… the… so that's a pattern that can be followed. And then, on the Epic 2818, there's, like, like, detailed instructions written out for, like, how to… how to, like, actually do this that you could follow, or you could feed to an LLM agent, if that's what you're working with, so… Yeah, so just, you know, get involved if you want, tell your friends if they're looking to get involved, and yeah, that's all I have to say about these. We'll keep the triage moving.
Laurent Querel 00:19:31 That's really cool. I think it's an interesting pattern that we need to reuse in the future when we have something that is well-defined.
In the engine, OPL, the main components of this architecture are well designed, now we need to extend, adding more and more functions.
So that's, in my opinion, a very good approach to… amplified the… Or to accelerate, the integration of those functions, and at the same time, getting more contributors and, On some tasks that are well-defined.
Pretty cool.
Then, then we have this one, but we will discuss it separately, and, we just have, The flow measurement that we briefly discussed, the discussion we had, Previously on the Hotel LaRue dev channel.
Where we generalize, basically, the stopwatch mechanism to something that is Identifying a flow, and we can enable different, measurements.
Okay, cool. So… I think we are done with the… the triage, Jake, what about to start, with Benchmark?
I don't know how much time that will take for the 5-log receiver, so I prefer you to have time to… Because it's a big piece for the 5 logo receiver.
Jake Dern 00:21:11 Yeah.
Laurent Querel 00:21:12 let you share your screen, I think that will be… the best option.
Jake Dern 00:21:18 Yeah, let me do that.
Alright, can we see that?
Laurent Querel 00:21:32 Yes…
Jake Dern 00:21:34 Awesome. Yeah, so I think… I'm trying to remember exactly what, I showed last week at the SIG meeting. These graphs are kind of seared into my brain, but I think this is, a new chart, at this point. So, kind of what I've been working on recently is expanding the set of engines, for testing.
And, you know, I just kind of want to emphasize that these are, like, very new benchmarks. I've mostly been working on them today. They're definitely not final. There could definitely be some mistakes in terms of configuration, but… The initial results are more or less believable, and there's a couple kind of, like, interesting things here, to show. So, one interesting thing is, in addition to the new engines, previously I had only been testing with OTLP gRPC, but now I'm also testing with just the HTTP version.
And so if we kind of look at these results, maybe one at a time, we can start with the GRPC.
So generally, just like the results for this test, the flow engine performing the best, the hotel collector performing second best, which actually kind of surprised me a little bit, because Rotel is also, in the picture here.
But it's performing third best, and then followed by FluentPit at 4th. I did try to also test Vector.
But Vector, having a little bit of issues with configuration on this one. It could definitely be user error, but I can't really seem to get much throughput out of it. I also don't know too much about Vector, and so it could be the case that it's really just not suited to converting from OTLP to whatever its, like, internal representation is.
Totally no idea. If anybody does or has experience with Vector, I'd definitely be interested, to kind of hear your thoughts on it, but… I haven't really been able to get much, much out of it in terms of throughput, just a few thousand logs per second.
So if we kind of take a look at the OTLP HTTP, we do see actually a slightly different result, kind of in terms of ordering.
Which is interesting. So, in this case, actually Rotel does perform the best, other than the data flow engine.
Otel Collector is actually coming in last, and then FluentBit kind of coming in somewhere in the middle.
You might notice that I've done somewhat of a poor job of controlling the single core for some of these, so Rotel and FluentPit are, you know, allocating a little bit more than I intended them to, and so they're kind of able to keep up with the higher rates.
But they are using more than one core, which was not my intent for this test, so I need to go back and control a little bit more for that.
Otherwise, something that we might find interesting, and maybe this is partially an explanation for why the hotel collector is kind of on different ends of the spectrum when you compare OTLP gRPC versus just HTTP, so if we look at, like, each engine individually, and look at the two protocols.
Pretty much universally, everybody's doing better, with HTTP.
As opposed to GRPC, so this is true for the Dataflow engine, this is true for Fluentbit. It's also true for Rotel, although to a slightly lesser extent than the other engines.
But for the hotel collector, actually, it's the only one that's performing significantly better with gRPC. So I found that interesting, and I don't know if anybody's, kind of seen that before, but… Yeah, this is kind of the update of what I've been working on in the last, Last day or two here.
Laurent Querel 00:24:58 Yeah, so, Can you go back to the… to the one where we see either OTAP or OTAP HTTP with all the… Leon Jean…
Jake Dern 00:25:10 Yeah, you want everything on the chart?
Laurent Querel 00:25:11 Yeah, that this one is perfect.
I think that's interesting to see, that if we consider that, The… oh, sorry, the issue that we are not able right now just to limit, the hotel and the Freon bits to one single CPU, In fact, I think… Baldwin with K is probably… the last… part where some of the other engine are able to… they are basically able to sustain this load, more or less. Not all, but some of them. But after that, we are the only engine able to go Up to much… even more than 1 million, in fact.
We, we measure already the, 1.4, 1.5, just for a single CPU.
So that's, so we, we have those, signals, the… the young girl with the exclamation point.
When you see them, it's been that there are some issues, that we notify.
Jake Dern 00:26:23 Yeah, mainly with these, we're looking at two things primarily for this, so one is the dropped logs, which is… just showing a discrepancy between the logs that, the producer measured and the logs that we actually received, on the back end. And then the other thing that we're monitoring is the back… like, the overall backend received rate, as is compared to the expected. So, oftentimes what happens if… there's, like, a nice, you know, sane back pressure for the system under test, is the offered load rate will just go down because, you know, our load generator is going to be seeing the back pressure, and, you know, rather than producing 500K, it's gonna produce 250K.
But we know we were expecting 500, so if we weren't seeing that through the test, then, you know, we're gonna put that, like, exclamation mark on it saying, like, yeah, we did not actually process the throughput that we should have, for this one.
Laurent Querel 00:27:13 And, so right now, we focus only on OTLP, but obviously we have a similar result for OTAP.
obviously, where OTAP is mostly only implemented by OTC or DFE, But, we, we, we will, we will, look at a way to represent the overall performance Across protocol. So to demonstrate at the end that, If you combine the overall performance that we have with the engine, plus a better protocol, plus a better representation.
At the end, we… we get, a huge, Performance gain, or dimension.
Jake Dern 00:27:59 Yeah, so some of the comparisons, like you mentioned, that we're kind of working on next are incorporating some of these processors, and I've already started on the batch processors a little bit.
Like you also mentioned, we have comparisons for OTAP, but of course, you know, the only engines that are implementing that are the Dataflow engine and the OTEL collector, so that's why they weren't on that chart that has all the other engines, but I do have kind of a… a massive chart that's got everything, but it's starting to get to be a little bit too much data to interpret at one time, so that's why I've been kind of splitting them up.
Laurent Querel 00:28:32 Yep.
jmacdonald 00:28:33 that the GRPC is performing worse for everybody. That's… I would love to know why. Sorry, Kennedy.
kennedybushnell 00:28:43 You're good. I'm curious, I asked in chat, I'm assuming this was all ran on Linux and not Windows, or was this ran on both?
Jake Dern 00:28:52 Yeah, this is all run on Linux, on a laptop, so yeah, definitely something to be improved there, but luckily it's all, you know, very automated and repeatable, so, yeah, we'll be able to… I think that's one topic for discussion, is, you know, kind of long-term, obviously, we can't just run them on Jake's laptop, so… how we're gonna run those and publish them or whatever, I think that's a topic that, I don't know, maybe for this meeting or maybe for a future one.
kennedybushnell 00:29:18 Yeah, that'd be cool to get codified, too, because we'd love… like, this is awesome data, first of all, but if… Yeah, Windows and Linux comparisons would be cool. The other thing I wanted to make sure of this… oh, now I see OTAP. Okay, I wanted to make sure that this is OTLP and not OTAP, so you are running all three. Cool.
Jake Dern 00:29:35 Yeah, yeah, all three. Yeah, so that last chart where I had, just the, like, different engines, yeah, I was just dialing in on the OTLP, gRPC, and HTTP, but yeah, we have OTAP, of course. That's the… that's the big one.
kennedybushnell 00:29:48 Yeah, this is awesome stuff. Cool.
Laurent Querel 00:29:51 Yeah, so, the ultimate… I mean, the… our goal is, at some point, and Hopefully soon, to publish those benchmarks.
as GitHub pages.
Because basically the… this, it's a bunch of, beta JSON file, or something like that, plus, web pages.
So that could be served as a static, website.
And So I think we should, add that into the HotelRo repo as soon as possible, once we are confident in the result, and we serve the various issues regarding Vector, and… and we make sure that We are doing a fair comparison with the other, but that's definitely the goal, ideally before the observability Summit.
And then we need a way to run those benchmarks. Maybe we can just reuse the runner that we are already using for the continuous benchmark.
And run that… and run this kind of more extensive benchmark, maybe one time per week.
That's something we need to discuss, not necessarily in this meeting, but we need to open this conversation in the hotel or dev channel and, and figure out the best approach.
Jake Dern 00:31:19 Yeah. One thing I do just want to, like, mention, you know, there… I would almost be a little bit nervous about running these benchmarks automatically, not because they're not mostly repeatable, but because the number of tests is now, just with the matrix that we have, over 200.
So, like, one, I think… and I'm only running them for 20 seconds, just for the sake of expediency, in development. You can see the test duration here.
So it will take quite a few hours to run them, and across so many tests, it's basically, like, 100% likely that some of the tests are going to flake a little bit.
Partially due to the way that we're, like, computing these, like, metrics down here. Because, you know, the data flow engine internally is aggregating every so often, and we're scraping those, and so every now and then we will, like.
you know, kind of get some funny data, and we need to do a rerun and that kind of thing. And so, you know, just kind of making sure that You know, if we do run these all automatically, that, you know, we have some way to Automatically go and say, these runs didn't quite work, rerun them, and, you know, that kind of thing. So we're not ever publishing anything that we're not confident in.
Laurent Querel 00:32:24 Yep.
Great.
Jake Dern 00:32:28 I think Aaron set his hand up, for a little bit.
Aaron Marten 00:32:32 Hey, I just had a question, kind of selfishly, I was wondering, if you're including the durable buffer processor in the processors that you're exploring for some of these benchmarks.
Jake Dern 00:32:42 Not yet, but we should, for sure.
Aaron Marten 00:32:45 Cool, yeah.
Jake Dern 00:32:46 I'm no expert in it, and yeah, I'm not sure what, what all these other engines offer in that area, too, and what would be appropriate to compare, but if you have.
Aaron Marten 00:32:55 Right.
Jake Dern 00:32:55 Definitely.
Aaron Marten 00:32:56 Yeah, exactly, exactly. Yeah, it'd be… we'd have to make sure we're doing fair comparisons to see. I know some of them do offer Disperseth.
Laurent Querel 00:33:04 Yeah, FionDeat, I'm pretty sure, is offering that, and I think Vector also, they have some.
Aaron Marten 00:33:10 Yes.
jmacdonald 00:33:11 GoCollector has a storage extension you can use for that as well.
Laurent Querel 00:33:15 Okay.
Jake Dern 00:33:17 Yeah, my hope with, like, this dashboard also is that, like, once we start checking in, kind of the individual pieces of, like, the harness, it's, like, very, very lightweight, and I hope people will find it pretty easy to, like, add new scenarios in, you know, so far, like, it should just be, like, a few lines of YAML. You know, I think most of the… and maybe a couple extra lines to, like, define a template for something that you need, so… Yeah, hopefully over time, we start to accumulate a pretty big library of these.
Laurent Querel 00:33:46 Nope.
jmacdonald 00:33:48 I'm sure with enough effort, we could make them reliable enough to automate, but I think I agree that the risk and reward of trying to do that maybe is not the right time to do that.
Jake Dern 00:33:58 Yeah, and even if we do, it's so many. Like, already it's over 200, and we don't even have… we're really just at, like, the baseline comparisons, you know, just the different protocols and compressions and engines. We haven't even gotten into the really interesting stuff, so yeah, that's a lot of time on the server.
Laurent Querel 00:34:15 And for fairness, I think we should, so not only will we probably increase the number of, tests, but, We should also increase a bit the duration of those tests.
Just for fairness, because… For, Yamiche Killing.
tool-based solution.
they will not behave so much… I mean, they will probably behave better the first few seconds, and… and… Probably worse, after, 20, 30 cmoon of, of, incoming, traffic, so, I think for fairness for the others, that would be nice to have, something like, 2 minutes, minimum, maybe five, five, 5-minute duration for each of those tests. I don't know, we need to figure that out, but 20 seconds, in my opinion, is, Is not enough.
Jake Dern 00:35:11 Yeah, I absolutely agree. Yeah, this is mostly for the sake of.
Laurent Querel 00:35:15 Because there is legit for some time, so that's not the case here, because we don't have, No, Vector is Rust, Rotel is Rust.
Blue and Beat, I think, is C++.
Jake Dern 00:35:28 I think it's…
Laurent Querel 00:35:29 Otc is Go, so for Go, we have the garbage collector.
But we could imagine that at some point we have some, GVM-based or, C-sharp, the VM for C-sharp.
And, and then, Jeet will also, Play a role, in addition to the garbage collector, so yeah, duration will, will matter.
Okay, great. Excellent.
If we are okay, we can now move to the 5-log receiver.
Sofa…
jmacdonald 00:36:07 Since we think that one's going to take a long time, I wonder if we should just briefly cover what this… the muscle C library.
Laurent Querel 00:36:14 Oh, yes, yeah.
Yeah, that's… that's, Something we… we discovered, Jake and I, during this benchmark, experiment.
So we… we initially noticed that, we, we had, bad performance… And, and also.
very different performances between environments. So, for example, I was running The engine on my, server without, docker involved.
And Jake was running on his laptop the… version with Docker, which was initially, was containing, basically, a binary compiled with muscle.
And, initially, we didn't understand at all what was happening. I was aware that, with muscle, you have a very bad… if you don't do anything, you have very bad performance, because the, the internal, the memory allocator used by muscle is… Very well known to be, very slow.
So that, that was, Something that we took into account day one in the project, we use a custom allocator.
We are using either Mimalog from Microsoft or GeoMalog from Facebook.
So that was not the problem, and then we… we discovered that, Messer role.
based binary are also Or is it super slow when you have something like a data plane?
Where networking and, eye concurrency, is involved.
So, I think it's… it's fair to say that narrow muscle is probably, no longer an option for us, and we tested Value subscriptions.
The one that we, we think is a good compromise.
Is a good trade-off is, the, the Dockerless… the distro-less, sorry, from Google.
There is two versions of it, one that is static and the other one that is dynamic, so the dynamic one will give us a way to just generate A binary with the standard option.
And, And then, because the distro-less basic version contains agility, we can just use it, and it's performing very well.
So, that's the learning we got from this, one of the benchmark, Mystery that we discovered during the last few weeks, and that ended up with just a banned muscle.
jmacdonald 00:39:18 Gotcha. So do we know what the actual performance, like, caused… what was causing that performance regression?
Laurent Querel 00:39:27 I am aware of a very well-known, but I don't think that was the case for us.
The memory allocator is definitively super, super slow with, When you… when you don't use your own custom memory allocator, And I was able to… To find, here and there, people talking about, Bad performance regarding networking and multi-threading. Without a lot of detail, in fact.
But the fact that when we basically switch from A muscle-based binary to a standard, binary.
And we observe with, so we move also from, alpine to… this for us.
the difference was used. I don't remember the exact number, maybe, Jake, you remember the… Some numbers that we observe in terms of performance.
Jake Dern 00:40:29 Yeah, it's tough because it varied heavily based on whose machine it was. In my case, in particular, I did see, like, over 50% difference across OTAP and OTLP, so… Pretty significant.
jmacdonald 00:40:44 Got it. It's probably not… not worth digging any deeper. Thank you.
kennedybushnell 00:40:50 So, are we just, like, informing here, or are we wanting to put in docs that… You need to watch out if you use… I think we…
Laurent Querel 00:41:00 We, yeah, I think we should document that, and and I think that the… the default Docker image that we will, publish, needs to be, For example, one based on distro less.
With our atmosphere.
kennedybushnell 00:41:20 Sounds good.
jmacdonald 00:41:23 Thanks, Kennedy. I think we should… I'll follow up to make sure we follow an issue about that.
Okay, well, the big show, let's talk about file log.
Laurent Querel 00:41:34 Oh, big show. I don't know if it's a big show. But, so we, we, We started with, recently, I think it was a few weeks ago, with, specification for the host metric receiver.
And, Lalit is working on it.
And, I decided to… Following exactly the same process, Which is looking at… what the Go Collector is doing, so that was the case for the OS metric, and now for the file… the file log receiver, what the GoCollector is providing.
What are the feedback from the community?
What are the other options in the rest of the ecosystem?
Compile all of that, and try to come with A design that is solving all those issues, and a design that is also well Integrated with, our own architecture and the corresponding constraints that come with it. So, we… We are, we have a thread-per-core approach.
We try to make everything bonded.
We try to avoid synchronization as much as possible.
we have now a live reconfiguration mechanism that has a huge impact. I think we need to revise some of the Nodes that we already implemented, because some of them will not behave very well with level configuration.
We… similarly to that, CPU scale-up… scale down is also a thing that needs to be… that we need to take into account in the design.
Specifically for, for the fire log receiver.
How this file log receiver will behave when we restart the corresponding engine.
In this specific case, the ideal situation is We can kill, the fail… the engine, and we restart it, and we should be able to Worst case scenario, have some duplicates.
That will be sent to the, to the backends, the Optality backends, but we should not lose any information.
And that means that we need to do that properly. We already have, in my opinion, a strong ACNAC A mechanism in place.
And for this specific one, we need some kind of checkpointing, similarly to the durable processor that Aaron implemented.
And… So that's the overall, idea behind this, file log receiver, trying to… to take into account all those, aspects.
There is an additional set of, let's say, observation, not necessarily my own observations, but something I read here and there from feedback in the community. The 5-log receiver is… is a huge piece of, of code. With, with, let's say, with, different, I would say, concern.
There is, file discovery, file reading, offset tracking… We try to detect, our… low framing, so meaning that how to extract a singular entry.
rotational link, parsing, field extraction, and so on. So it's a long list. Everything is, in fact, grouped into the single entity file log receiver.
So, based on the feedback, it looks like we could easily Put that into a pilot receiver, and put that, basically, into processors.
And the benefits of splitting that this way We will be able to reuse some of those elements for other, receivers.
That make the system more flexible, more extensible, and so on.
So, at the high level, I think this image will present, basically, the general idea.
So for the file discovery, so when we have a configuration describing that we want to Be notified when there is new logs in different, directories.
We zoom… And, recursive… you can inspect those directories in a recursive way or not.
You can exclude, based on some pattern.
So the way to integrate a file log receiver, in my opinion, into this engine is to leverage the extension mechanism.
So we need to support extension at the engine level, that's not something that is currently the focus. We have, Pipeline stop for extension.
To implement a fiber receiver, we will need an engine, level.
type of extension. So once we have that, we could have an extension that basically Just focus on file discovery and assignment.
So it's, it's, it's not too much work.
It could be, could be done in one thread.
But, the… the… this extension will basically… Identify with the classic, 5 system watch API, like I notify, PQ and so on, the redirectory changes for Windows.
And, we will… the, the… The extension will have the responsibility to basically assign virtual partition.
For each of those files.
And, and we will have, Configurable number of, active slots.
And the goal of this extension will be to deliver, to assign, basically, to… a file receiver.
instance, a subset of this, of this, Number of files that are partitioned.
So then we have, fire bug receivers that just get this information from the extension.
And we'll just process the corresponding assignment.
So, basically, the corresponding file, they will open, read the file, they will decode, That will extract the values record, attach some file metadata.
That will also handle the… the fire rotation.
And we, properly track the ACNAC.
And making sure that we… we checkpoint all the file… all this file has been, hacked properly, so we can delete it.
So that's the kind of thing that the 5-log receiver will do.
What will be emitted by the file log receiver will be OTAP log messages, but semi-structured. So, where we will have some attributes or body.
So the attributes will be basically metadata-related, collected here.
But the… the record by itself.
Will be… probably in the body.
And then we could, just… Based on the type of the… the log, and… So the format, is it, an NGINX log file, or is it, I don't know, A system log of some kind.
file… So we have to apply different transformation, and that's where this collection of processors will play a role. So whether the body is a JSON, or maybe it's pure text, or maybe it's a binary representation. So we have to come with, some way to express the… How to extract the structure from that.
And we will deliver a set of processors to normalize, to enrich with some additional information, like resource attributes, and so on.
I think OPL will play a big role there. We already have, some capabilities to cover some of those, Post-form and enrich, type of operation.
And then, the next step is routing.
So it's an optional, set, but we could root based on content.
To different destination.
So that's the overall, idea behind this, file log receiver.
So… Yeah, that's here.
So the important point, I think, is the receiver side on the file, offset and framing and so on. The processor will just extract the semantic from The values record extracted, and the extension is there to orchestrate, basically, the distribution of this, the discovered file.
To the various, file loads.
receivers. I think this architecture covers all the aspects that we have here. We can scale up, down, we can support pliable configuration.
We have, on the old pass, Basically, no synchronization at all.
And we… we support natively the ACNAC, mechanism with the check… the corresponding checkpointing.
Yeah, after that, I put some detail, And here are dependencies, so I think we have a lot to do before we are able to get a first version of this file on receiver. The first one is making sure that we have an extension mechanism That is, are able to work at the engine level.
And, a few other things.
Feedback, questions?
jmacdonald 00:52:49 Yeah, question. The diagram made me want to ask about what the checkpoint store in your file log receiver column is durable, and yet the… but it's separate from file discovery and assignment, and I couldn't quite figure out how the fire log… File discovery and assignment would be sort of stateless if the durable state was in the checkpoint store.
Laurent Querel 00:53:17 So the checkpoint store is an entity where, for a specific, I think there is a file identity here, yes.
So, it's something that will be, I think shared across the… that's something we need to… I need to refine again, that, Yeah, I see your friends.
jmacdonald 00:53:47 It's just an open question. I don't think.
Laurent Querel 00:53:49 Yeah, yeah, yeah, yeah.
jmacdonald 00:53:50 Right here.
I had been thinking about the sort of technique that Quiver is using to, you know, and whether we could reuse some of Quiver or, you know, a piece of it, but that's just a thought. We can think about it.
Laurent Querel 00:54:05 Yeah, so I think that… I think I remember now that… It's, it's, it's like a collection of files.
Where we, we have basically, checkpoint per, per file.
So the… every file, file log receiver where we have this assignment.
We could imagine that we have the checkpoint for the 305 And it's an independent file.
So, when we restart, or when we scale up, scale down.
It doesn't really matter, if, if it's one 5-log receiver instance or the other.
But now the format of this file, I don't know, we need to specify it.
jmacdonald 00:54:59 Gotcha. We'll be thinking about that. I see Kennedy has…
kennedybushnell 00:55:06 Yeah, so this has been discussed quite a bit internally. It's not… currently a priority, but it's definitely something that kind of causes us pain. We use Fluent a lot. So I dropped a comment with a couple of the comments, but just… kind of want to raise them here so people can leave their… their thoughts, too. One of the common feature requests that I've heard is file logovers, or rollovers, so… literally reusing the same file and just kind of popping back to head. That'd be cool to support. I don't think it's critical for us, but… If we could do it, that'd be cool. I saw that you mentioned that you're using the Oto Collector file receiver kind of feature set as kind of the base. Fluent bit might be good to look for… look at as well, to see if there's any non-overlapping pieces that we might be able to grab.
Laurent Querel 00:55:56 jump.
kennedybushnell 00:55:56 Cool stuff from there.
One thing that definitely causes us a lot of pain is the number of file descriptors that Fluent will open. Can, in some cases, be unbounded or high. I think that your design covered that with the way that it was kind of looking and assigning to to things, but if we could… Have… So, like, find control over that, that'd be great. Obvious max byte and line length, kind of just kind of guards around that.
And another one that I've been thinking about is NUMA Awareness.
and not just pneuma-friendly. So I think that… OTAP data flow in general is NUMA-friendly, but being aware of where, like, if we assign the the task for a file to a CPU that the disk is actually attached to, that'll provide even higher performance and lower latency. Yeah. If we could do that, that'd be sick.
And then the last note, it looked like the design was going to shove everything that it read, like, maybe into body or message or something. Some file formats have schema, kind of, Defined in them, and it might make sense to… Kind of drop the data into columns when it makes sense for different file types.
Laurent Querel 00:57:23 Yeah.
Yeah, definitely. Thank you for the feedback.
We're getting the numeral awareness, Definitively a goal for the project.
Right now, I agree, we could do even more than what we do.
It's not only to align the CPU with the disk, but also align the CPU with the network interfaces, for example.
kennedybushnell 00:57:50 Right.
Laurent Querel 00:57:50 I think we are very close to that. We didn't, Put a lot of effort in this, area.
But, yeah, that will be definitively, at some point when we… We are happy with the… Let's see the, all the nodes implemented that give us, a good comparison with the rest of the ecosystem, then we will focus, I think, on that definitively.
Regarding the schema, that would be interesting if you have, Yeah, CSV with headers, yes.
If you have some other examples that could be interesting to… to have some additional examples, and I will look at the… the Freon beat, Specific, file log receiver equivalent.
Maybe they have scenes like that already.
kennedybushnell 00:58:55 Yeah, I've shared this issue with a couple of people that have been kind of thinking about this internally. Sid's actually here, he's one of them. I'll have them.
Laurent Querel 00:59:04 Okay.
kennedybushnell 00:59:05 And add some comments.
Exam.
Laurent Querel 00:59:07 Providence.
kennedybushnell 00:59:07 possible as well.
Laurent Querel 00:59:11 Great.
Two minutes, is there any additional, question or feedback?
jmacdonald 00:59:23 This is exciting.
Laurent Querel 00:59:26 Yeah, maybe I can use the last 2 minutes to… Explain my approach, maybe a little bit better overall, So, we, we, we have, What we did… what we did with this engine is not only to… translate the GoCollector into a reservation of it.
We… We basically rethink about the entire architecture.
And the design decision behind it.
I think we need to do that, not only at the engine level, but also for every… Receiver, exporter, or processor that we will implement.
We really need to take this opportunity to look at what exists.
So the host metric and the 5-log receiver are an example.
And, look at that, learn from the, the… The existing, issues… And, and figure out what will be the, the best, the best solution.
Or, an equivalent capability, but, that fit well with the engine, and that solves also the major issues.
I think when I said that I think we need to… Revisit some of the receiver, or some of the… The node that we already have.
It's… it's mostly for the… For the level configuration, because… The live role configuration, if we want to support that, Without, worrying about, oh, my pipeline contains this component and is not very live or configuration friendly.
We definitely need to, to make sure that part of the design, we have a section that is fully dedicated to that, and we make sure that We took that into consideration.
I don't have an example right now, but I'm sure that if I take some time, we will find some of the existing Nodes that are not really, friendly with level configuration, and that's normal, because we didn't, implement This, library configuration day one, so the constraints were not very well known initially.
Okay, have a good day, and see you next week.
drewrelmas 01:02:16 Goodbye, everyone.
kennedybushnell 01:02:17 It's awesome. Thanks all.
Jake Dern 01:02:19 Beautiful.
Nikhil Manchanda (SlickNik) 01:02:20 Thanks, folks.
