SIG: Arrow SIG
Date: 2026-11-12
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Bartek Plotka @bwplotka (Google)** 00:47 Hello.
**Jake Dern (F5, Inc.)** 00:53 Abe, how's it going?
**Bartek Plotka @bwplotka (Google)** 00:56 Good, how are you?
**Jake Dern (F5, Inc.)** 00:57 Doing good.
I saw your, your post this morning.
**Bartek Plotka @bwplotka (Google)** 01:04 like it.
**Jake Dern (F5, Inc.)** 01:05 Oh, yeah.
**Bartek Plotka @bwplotka (Google)** 01:07 Yeah, it wouldn't be possible without you guys.
Pretty impressive.
**Jake Dern (F5, Inc.)** 01:14 Yeah, we're, we're excited about it. Happy year.
**Bartek Plotka @bwplotka (Google)** 01:17 I still don't believe it, by the way. Like, do you think this is true?
possible.
Crazy.
And I think this is what we needed to do, you know, like… change the direction of the whole Prometheus community as well.
**Jake Dern (F5, Inc.)** 01:44 Yeah.
Definitely, plenty to be excited about.
**Drew Relmas** 01:49 Hello, everyone.
**Bartek Plotka @bwplotka (Google)** 01:51 No.
**Drew Relmas** 02:10 So I expect we should have, either Josh or Laurent with us, I know they were… At a conference. Jake, do you know if, Laurent is… back.
**Jake Dern (F5, Inc.)** 02:25 I believe he's still traveling, I think he's actually in, in Vegas right now, for some of the 5 thing.
I'm not sure if he'll be here.
**Drew Relmas** 02:35 Okay, I thought Joshua is back already, but we'll give it another… Minute or so.
I see we have a bunch of folks from the Microsoft side as well. Hey, Sapneel, Brian, bhala.
Eve.
**bhala ranganathan** 02:57 Yeah, good morning, folks. Yeah, I just joined new, so I'm interested in this project.
**Drew Relmas** 03:03 Great.
Welcome to have you, baala.
**bhala ranganathan** 03:06 Yeah.
**Brian Sapozhnikov** 03:09 Hello.
**Drew Relmas** 03:12 Oh, Albert, I didn't recognize your thing. It says Albert, Albert.
**Albert Albert** 03:18 Oh… Yeah, it's, my, I don't know why the Linux Foundation has that as my identity, or whatever, but it… it has been a problem when I've gone to, like, CNCF events and stuff, because they'll print off the name tags, and they'll show up.
But it's a good icebreaker if people think that your first name and your last name are the same name, so… It kind of works for networking.
**Drew Relmas** 03:50 Well, it's considering we don't have Josh or… Laurent, I guess I can share my screen and kick us off.
Let's… Alright, well, hello, everyone.
Happy… what day is today? Thursday. Jeez.
I see we have, a number of… oh, I forgot. We haven't put in the date.
And the regular agenda.
links.
I'll do that.
**Bartek Plotka @bwplotka (Google)** 04:32 Yeah, by the way, sorry for spam on agenda, like, we can… we don't need to spend time on all my stuff, I just, you know, feel free to totally put something else, I just propose something.
**Drew Relmas** 04:43 Yeah, we'll probably run through the regular links we have here about some recent issues marked need to be discussed, and then we can jump into it, unless anyone else on the call has another agenda topic as well. So to start… Issues that need… to be discussed.
We have… A really old one here about… console output dropping. When did this get?
huh.
Josh added needs discussion, but he's not here, so I think we'll skip this one.
OTLP… Oh, okay, this is actually someone from the Microsoft side. I believe we are talking about this, internally. Basically.
There was an idea of adding specific uploads per second metric to the Geneva exporter, which is, again, a Microsoft component, directly into the dashboard, and I'm talking with the contributor behind it. I think we can satisfy this requirement with the standard exporter.attempted metrics that we already have.
So we probably don't need to discuss that.
And we have… again, another one from Josh, header capture support for the HTTP extensions. This is, like, more work on the context side, but since Josh isn't here to talk about it, I guess we are skipping that as well.
marked as stale.
Milestone December 2025. I think we are, a little… Past this point.
We haven't typically… I think there was a project added at some point. Not a project, a, like, milestone.
Yeah, there's a couple milestones here. We haven't really been using the project planning view, so if anyone wants to… us to get into that, please let a maintainer know, and we can talk about it.
And then there's process-level metrics.
Oh, so we have metrics for CPU, memory, etc, but… There's no on-off switch, they're always collected, so I'm gonna go ahead and mark this as, Good first issue. See if we can get someone to pick it up.
And needs deciding.
Oh, Laurent, I see we have you, but I'll continue, I'll continue leading the way.
Not sure if you're in a position to lead the meeting right now.
**Albert Albert** 07:51 Oh, I see, this, this first one, 4726,
**Drew Relmas** 07:58 Yes.
is breaking down.
**Albert Albert** 08:02 Yeah, this is, I've actually started working on this, so, started… I think, Yeah, so there is this, I can, I can speak about this a little bit, I'm still kind of, still kind of, like, just starting the work, but there's this, this OTEP here, 4738, that specifies this thing called, telemetry policies, and these are kind of interesting. They're basically used to, They're a declarative way that you can specify how you want to keep, filter, sample, and do certain transformations on telemetry. So, for example, you can say things like, I want to discard all the telemetry that has a certain attribute, or a certain field with some given value.
Or I want to, for every, log that has a certain value, I want to do some transformations to it. I want to… Set attributes or rename attributes and things like that, so… There… and then, on the GoCollector side, there's already an implementation of, basically, like.
this thing that, like, works on OTLP data, it's already embedded into a processor. There's also, like, a reference implementation in Rust. So, the idea here is it would be really nice if we had the ability to do this on, on, OTAP batches. It's quite a nice fit, because clearly you could, do this filtering in a very, efficient way on the, on the columnar data format. We have a bunch of primitives that can do this, like, attribute rename, attribute insert, attribute delete in a very efficient way.
And so, it seems like a good fit. So, yeah, I actually, have been, like, starting to look into this the last, day and a half, Have been having some pretty good luck with, like, getting it implemented, just because it's a pretty clear spec, and, pretty clear what to do, so… Should have prototype that I can share, early next week. And, yeah, so that's, what's… And I think.
**Drew Relmas** 10:19 I have one question, which might turn into… a naming thing. We already have a concept of policy, specifically telemetry policies in DF Engine, typically controlling things like You know, runtime metric granularity, as well as… for, like, all the standard, node metrics, input, output, item, size, etc. So, we have telemetry policies to control that sort of collection, so I'm curious, do we need to re-change our… do we need to rename ours to a different thing?
**Laurent** 10:56 Nope.
I can answer that because, when I wrote the proposal.
I had exactly the same question. Sorry for the quality of the… maybe the voice.
I'm using my phone, so… and, on the cellular, so it's not ideal. But, So, in the proposal, It's named Telemetry Policy Set.
As opposed to the policy, engine.
So the policies that we have today are named policy, they are not named telemetry policy.
So, I'm using the concept of telemetry policy sets.
to make a difference between these two, these two things. That's my proposal. I don't know if you agree with that, but, For me, that's, well aligned with, anyway, with the OTEP.
They are also using the term telemetry policy.
**Albert Albert** 11:51 Yeah, and there's, if you go back, Drew, there's a… there's a, an issue on Hotel Arrow. Yeah, so on the top left of the description here, where it says 4718, this is, like, the issue in our… this is another issue in our.
**Drew Relmas** 12:04 Oh, okay, yeah, this would probably explain it. I hadn't, I hadn't seen this, so…
**Albert Albert** 12:09 It's called Telemetry Policy Sets, which is a slightly different name, so we don't have that name in conflict.
I see.
**Laurent** 12:20 I think we have, today we have engine policies, group policies, pipeline policies, NUT policies.
**Drew Relmas** 12:27 Okay, so we're technically okay. Yeah.
**Laurent** 12:31 All these policies, and if we look at the various type of policies we have today, it's already a… multiple variations. It's basically a set of declarative intents That we can use to address a specific, specific domain. Now, we have another one, which is the telemetry policy, and effectively, when you read the tip.
It's about simple rules.
To rename, to update signal, to, express rate limit, to express sampling.
So this kind of thing.
I think what is very cool with this approach.
We have, a way to express this relatively complicated pipeline.
DAG, where you connect multiple receivers.
Processor, exporters, and so on.
And we also support level configuration.
But the policies, the way that they are designed, they are really… the telemetry policies. It's like a bag of… Small actions.
with the material.
They can be downloaded, from a different remote location.
Either an HTTP endpoint, a gRPC endpoint, even an OH AMP in the future.
Or a file, locally.
And, and the way that they are working, you can have multiple telemetry policy providers.
Following those, different protocols. And, and the pipeline engine will download regularly those policy sets.
Recompile them, inject them into the existing pipeline.
And, those bags or set of telemetry policies.
The intent is to have different… role, or let's say in a big enterprise, you have people that are specialized in security, in privacy, data governance.
I don't know, network management. So the… those different people, really, the way that the telemetry policies are designed.
Everyone can contribute.
They form a set specialized to their specific domain, and then everything will be merged, compiled, injected into the pipeline.
And the life cycle of each individual telemetry set is independent of the other one.
So that's the philosophy behind this thing. So it's very, very compatible, in my opinion, with… The… the engine that we have.
And I think we can leverage, like, Like it was said before, we can really leverage the columnar representation to make that super fast.
**Drew Relmas** 15:28 Yeah, I was gonna comment, I guess we need an added, header in here to talk about what it means for Otoler Arrow. Yeah.
All in due time.
Okay, great. That was a good one to talk about, I'm glad we did.
Let's see, we have… I guess we'll go through… A few more.
Retry processor, print silent. Data loss when payload item counts are unknown.
That definitely feels like a bug. We should… Take care of.
This one's accepted, so I won't remove the siding.
Albert, you have this work, I assume.
**Albert Albert** 16:20 Yeah, sorry, I,
**Drew Relmas** 16:22 Oh, you're good.
**Albert Albert** 16:23 been… Not good at updating the labels.
And now, everyone's time is being wasted while we… or sorry, not That's okay, maybe… It's happening in private.
**Drew Relmas** 16:36 maybe we stop here. I know Ukarsh has a bunch Ben has a few… And I know this is actually one of the, discussion topics, that we're gonna go to, so… Why don't we hop over to the actual agenda? And I think we have Bartek here with us to… talk about a number of things. So, Bartek, welcome. I think we haven't met in person or online before, but, I saw, you know, all the work you've been putting into the repo in the last few days, so excited to hear you chat.
**Bartek Plotka @bwplotka (Google)** 17:13 No, thank you for welcoming. Yeah, good to, you know, nice to meet you guys. I'm super excited to just join this community and learn about your work more, other than numbers, the results, which are amazing. And, you know, short background, I… I'm kind of Go expert. I wrote, like, efficient Go book, and I'm a really… love Golang, right? And, so it's extraordinary that I'm here, kind of.
Because I was always against, you know, Rust, because it's too complex, like, super verbose, like, it takes ages to write. But this year, like, things changed, right? Like, with AI, it's so much easier to understand it. AI is actually much better at generating Rust code.
than GoCode, because there are so many more compiler, you know, just checks, and, you know, it's kind of, like, just safer. And then it's readable enough, right? So, I was able to literally learn Rust, you know, last month, and… and contribute something that works. I wasn't VIP coding, by the way, I was, like, looking on the code.
If I'm too sloppy or whatever, just let me know, I'm still learning Rust.
And it's not only RAS, like, all those things that you put in the architecture of the collector, and, you know, the shirt nothing architecture, and Arrow, and lots of things to learn.
But, you know, surprisingly, we managed to put some, feature-complete sort of version, good enough version.
For Prometheus packages, right? Prometheus crate, for scraping Prometheus exposition formats, so something that you had open issue about. We generally, a month ago, we thought of, like, okay, let's do something fun, let's see if this is even faster or better on memory.
And we will, you know, kind of play with it.
So we propose even kube context around it. Long story short, we benchmarked, and the results are ridiculous, right? Like, it's normally… I already optimized lots of things in my GoPro ETUs, because I'm Produce Maintainer, by the way, I forgot to mention.
And we kind of, like, really care about efficiency as a Prometheus binary. I also started Thanos projects, so I also kind of were responsible by scaling Prometheus backends, right?
And it's all Go, it's all role-based DSDB, and… And this kind of told me that, hey, I mean, there's something here, like, really nicely optimized Go code.
and role-based, you know, it's, like, 1GB of memory for my workload, which is not small, and then it's only, like, 3.0 max. I don't… I still don't believe this is, like, possible. So, I did, like, I triple-checked it, and, you know, you can kind of find the… explanation… at least my explanation, how the heck this is even possible. I can share a screen if you want.
Oh, maybe, I would just…
**Drew Relmas** 20:13 It's muted. Sure, go ahead.
**Bartek Plotka @bwplotka (Google)** 20:15 Honestly, you can maybe… Open things from my… Or yeah, I can show you as well.
**Drew Relmas** 20:26 By the way, I saw we merged the Prometheus receiver.
**Bartek Plotka @bwplotka (Google)** 20:30 Yes, thank you so much, yeah. You kind of, like, motivate me to, you know, put… publish the crate, officially, was super easy.
Yeah.
What am I sharing? Can I see what I'm sharing? Yes. No. Okay. Whatever. I hope I'm sharing. Can you see any screen?
**Laurent** 20:48 Yes.
**Drew Relmas** 20:49 Yes.
**Bartek Plotka @bwplotka (Google)** 20:50 Yeah, so this is kind of, like, the scenario, YAMLs, really. I put in GKE for my benchmark, so anybody can reproduce it, and anyone can run it. And in this benchmark, I just had those results, and I kind of, like, tried to explain to myself as well, like, how this is possible. It's not Rust, right? It's not only Rust. Rust has a lot.
But it's mostly auto Arrow, right? So the fact that we kind of stream into 200 batches, like, we parse into 200 batches streams, you know, kind of like packages, let's say, or like batches, right, essentially, and… it goes through the whole pipeline, and it's, everything is reused, like, you know, one-to-one. It's not like you wait for some eventual consistency or some pooling. Pulling can go. It's so bad. I hate it so much because you cannot micro-benchmark it. It's super bad. So, I'm glad that there's no problem like this in Rust.
And then, you know, all the zero-copy stuff, just… and then shrinking, turning, just makes it so much fast. We actually did a lot of stuff on, scraping collection, innovations, so why it's so… so fast is, like, there is no state.
And I'm cheating a little bit, because, we have something like staleness. Do you know staleness?
**Laurent** 22:06 Nope.
**Bartek Plotka @bwplotka (Google)** 22:07 stainless in metrics for Prometheus, pool-based metrics is when you don't see a target anymore, you can actually put a special metric that mentions that the stream is done, and that actually super… it improves reliability of your metrics, because then you exactly know if the time series just finished, right?
You only do this on the pull-based metrics. And to really know if the metric was before, and now it's not, you need to have some caching. And I didn't have that initially, but here are my disclaimers. I already work on this, and there are essentially some… that's not this, that's like… here, stainless. I already benchmarked it, so it will add more memory, but not that much. It is, like, maybe 5 megs more, right? So, it's still good.
And then the sequential, we actually do something with scrapes, where we… whatever, I won't go into details. There are some things, but, like, none of those specific things, makes it not true. Like, the result not true on production that we will see, right? So… we looked at it, and I shared with Prometheus community, with Grafana, with, like, Shopify, Cloudflare, people who already touched, you know, this Rust and Columnar topic, and we were like, there's no way we are keeping investing our time in Prometheus in Go. Like, there's no point. Like, we are switching to Columnar and Rust, so we created, like, today, we just have, like, the first Rust Read Seek, right, where we discuss, kind of, the scopes, and we are really rebuilding Prometheus ecosystem. Not only, like, Prometheus binary, but the whole ecosystem. And I don't know if you're familiar with Thanos, Mimi, or Cortex, are you?
**Laurent** 23:52 Yes.
**Bartek Plotka @bwplotka (Google)** 23:53 So those are essentially… there's a long story what happens with this project, but effectively, in CNCF, you have 3 projects that are really good for metrics, for Prometheus metrics, right, in open source. It's Cortex, Thanos, and Memories outside of CNCF, AGPL3.
And all have a common history, but we never kind of joined together. So here, we actually have, like, people from all of those, and we might have a new project that combines those. And we already have, like, some, kind of reasonable, you know, like, design for how we want to do this, and it's great, and it's all because you're inspiration, Rich.
And also, in Cloudflare and all those projects, they already started, you know, something like that, so I'm essentially coordinating, like, already things that were… there. So this is big, I think.
Thank you.
**Laurent** 24:46 Fantastic. Yeah, that's fantastic.
Yeah, for me, the explanation, the one that you provided, definitively, I'm totally aligned with it. I think there are some few other things.
The lack of serialization, desertization?
**Bartek Plotka @bwplotka (Google)** 25:03 Yep.
**Laurent** 25:03 Is, a big element.
In your case, I don't think you have so much processing on the metric itself.
**Bartek Plotka @bwplotka (Google)** 25:14 We actually, have Relabellink, I just created, which is similar to what we discussed about telemetry policies.
And we… I even, like, built into, like, data fusion, so it can be super, super fast.
But we have reliable link, yeah, I'm just working on it, yeah.
**Laurent** 25:30 Yeah.
But the fact that you will have end-to-end columnar representation.
Including into the hotel Arrow project.
The benefit is also on the processing speed, because everything is, the number of allocation is super, super small.
And independent of the batch size.
Which is a big, big, big, difference with, if you, if you look at, OTLP, where you will have.
Millions of objects.
Depending on the batch size, number of metric, number of data points.
everything there will be transformed into millions of objects. So the pressure on the memory allocator will be, very big, as opposed to the columnar representation, where the number of allocation will be in the order of, I don't know, 50.
Okay, bigger space, but just 50, and always the same.
Which is a dramatic optimization.
**Bartek Plotka @bwplotka (Google)** 26:35 Yeah, yeah, and something… I don't know if you noticed, but, like, I am… I am translating into OTLP. I'm not even using OTAP, because Google doesn't support OTAP yet, so it's… I'm already paying the price, and if we do OTAP, then it's even better, right?
**Laurent** 26:49 Yes.
**Bartek Plotka @bwplotka (Google)** 26:50 So, it's crazy. It's, we are discussing, because our protocol is remote, right, in Prometheus, and we need something columnar, so… We'll be discussing if OTAP will be adopted or something else, but likely OTAP looks good. And yeah, but there are bigger discussions around, like, schema for Columnar, for Tanos, or this new project that will be a backend.
and if OTAP fits to it, because I think you have… can have really multiple different schemas that can have trade-offs, and I noticed that OTAP has lots of tables and lots of joins, and that's sometimes good, sometimes not very good.
So, I think this will be an interesting conversation, right? Like, what kind of thing we'd choose?
**Laurent** 27:33 I was, talking about this, this type of, rid of… with, Adrian from Piontic.
At Kupkun.
And, the conclusion was, for the transport.
Both the multi-table approach makes entirely sense, that's how you can get the maximum.
**Bartek Plotka @bwplotka (Google)** 27:56 The best compression, right?
**Laurent** 27:58 But for the, the, the storage, a flat table.
With, the ability to adapt to… for each batch that you have on disk.
Potentially with some variation on the schema.
And on the data fusion, you can basically ignore… there are ways to make sure that you can query something Where the something does not necessarily have always the same schema.
There are obviously overlaps, and you can adapt when you connect with, an Apache Arrow record with a different schema, you can just ignore the columns that are not used, or consider that missing columns are null, this kind of stuff. So they are doing that in their infrastructure, and that's definitely something that, It's probably a better trade-off for the storage, as opposed to what we do for the transport and the stream processing.
But the good news is, when you are already columnar on the transport and in the stream processing.
The… the match between that and the storage is much better than having a pure OTLP representation transformed to a columnar representation, because there are many columns that you can just reuse directly.
So that the effort, the conversion effort is much, much smaller, even if the columnar representation is not exactly compatible.
The effort is, massively smaller.
So that will also help for the ingestion, or the storage in your side.
**Bartek Plotka @bwplotka (Google)** 29:37 Yeah, yeah, thank you. So… Yeah, the point is, like, we will be discussing this, and… and also, like, promote use binary monolid, move to columnar. It's… it's… this is gonna be probably later, like, I think we'll first go with, like, the scalable backend.
Because on the scale, the performance is much more important.
So… but we'll have Prometheus discussions, and for all of this, you know, all your work is super relevant, like.
this is a mess, but essentially what I want to show is, like, likely Prometheus will have multiple backends. We want to maintain the old TSDB role-based, because it's adopted everywhere, and we want to integrate with it, so that would be an efficient, you know, essentially, you know, kind of like some conversion to this.
But then we want to have some vortex engine, likely, or vortex-based, right, or packet.
Parquet, and… but we have this agent mode, which is kind of auto-collector, just with Prometia's configuration.
And, we always didn't have a good people to… I mean, good amount of people to maintain it, kind of like a duplicates effort with AutoCollector, but from a Cijo's ecosystem likes it, but I'm thinking about just literally embedding your work Except for me to use binary or something, because we can reuse and we can collaborate together.
**Laurent** 30:57 Yeah, that's great. And we are delivered already as crates, already available on crates.io, so that will simplify the story.
Something, just a small reaction to… One element that you mentioned, so what you did, with the… In the script.ai creates.
To basically create a system of view basically… parse the primitives endpoint.
the different formats into the columnar representation. So we are also… we generalized that, and we are using that also for TLP. So that's an interesting aspect that could be reused also, in my opinion, in your project.
So we never, so we don't use, a standard portable library.
We, we basically, interpret the, the protobytes.
And they are converted into the OTAP representation without intermediary, object representation.
So, when I said before that the number of allocation is relatively constant.
depending on… only on the number of columns. It's also true for TLP.
Because we get this, protobyte.
**Bartek Plotka @bwplotka (Google)** 32:16 Yep.
**Laurent** 32:17 And, we just allocate the number of columns, and that's it. And then there is a mechanism to deserialize on the fly and construct the OTAP representation.
**Bartek Plotka @bwplotka (Google)** 32:28 That makes sense, that makes sense so much, yeah. So yeah, thank you, and I will… I mean, yeah, we are kind of like… that's separation… that separates this open source backend stuff, that's one thing.
we will make… we will productionize, essentially, the scrape RS. We're adding, like, more discoveries, and I will… we can chat later, but I'm curious how to… how to have, like.
20 discoveries without crazy amount of dependencies in Rust? Like, how… is there any plugin ability I could use?
Other than just compile flags?
But we can chat about that later, but we'll work on it.
So, so yeah, please expect some PRs from us, not only me, but, like, other maintainers, and teach us what's your style. Let me know if I'm too sloppy or whatever, but I'm trying to review my code.
properly, although I am creating lots of PRs. I cannot make them ready for some reason. Maybe you're limiting to 3, I think? Can you.
**Drew Relmas** 33:30 I think,
**Bartek Plotka @bwplotka (Google)** 33:31 I love that.
**Laurent** 33:31 I think.
**Drew Relmas** 33:32 Yeah, folks… Oh, Laurent, go ahead.
**Laurent** 33:35 No, no, no, I was just answering the number, I think it's 2 right now.
**Bartek Plotka @bwplotka (Google)** 33:40 Yes.
And that's, not ideal, because I'm marking when it's ready.
only when I review it properly, so that… to let you know. I kind of cannot, but whatever, that's fine.
**Drew Relmas** 33:54 Yeah, we originally did this to kind of encourage, especially new contributors to, you know.
pay a lot of attention to, getting things merged before opening more PRs. But, there are certain controls to, change those rules, so that's something, the maintainer group can… talk about.
**Bartek Plotka @bwplotka (Google)** 34:19 Up to you.
So that's.
**Drew Relmas** 34:22 Thanks for the feedback.
**Bartek Plotka @bwplotka (Google)** 34:23 Yeah, thanks, yeah, this… Yeah, whatever, we can, we can, we can move on. There were so many kind of questions I had, but yeah, let's move on to other topics.
Maybe, like, my top… I have another kind of, like, item on the agenda, and, like, I already removed… kind of trimmed this down, and maybe the only thing I want to chat about, or two things I want to chat about today.
If we have time. One is, like, self-observability. I added, like, a guide. Tell me if it's useful or not, but I learned a lot, like, what exactly metrics are I having, like, from… to observe AutoRL?
And I added a bunch of metrics, so let me know if this is useful. And then benchmarking framework, we could chat.
**Drew Relmas** 35:07 So, I have one comment on the self-observability guide. I think it's… I think it's good in that it ties together a lot of the other docs we have. Like, we have a metrics guide, but it's more framed at, you know, contributors and node authors, rather than strictly operators, but I am a little skeptical of maintaining a hard-coded list. I know we're doing it right now in a lot of node readmees.
**Bartek Plotka @bwplotka (Google)** 35:34 Yeah, let me find some automation, no problem, yeah.
**Drew Relmas** 35:37 Well, so, Laurent, for a long time, we've wanted… Laurent here is a maintainer of the Hotel Weaver project as well. So, we were thinking of ways to leverage Weaver and have a full like, auto-generated registry of all the telemetry OTel Arrow produces, and there's even some CI status checks. There's only a few metrics checked, but essentially we can run OTel Arrow and confirm we actually emit the stated telemetry. So, I'm… very happy with having the guide, I just don't know, if we're really ready to codify the full list of metrics, especially because, I linked two issues that are still open, that I'm, I've been working on about standardizing metric formats throughout all the nodes, in terms of Making sure we are using enum attributes, for bounded cardinality of attribute values and things like that. And we're not at full coverage yet across the whole all of the nodes, so I think we should get to a stable point and then talk about the generated version. I mean, I guess we could generate today, and the generation will change as we continue the migration. That's another option, but… I just got scared of the long, hard-coded list.
**Bartek Plotka @bwplotka (Google)** 36:58 Absolutely, yeah, I am, yeah, I can set up Weaver. I was using it in the past.
**Laurent** 37:03 Yeah, I'd like to add some compliment to that. So the… I have a branch where… Basically, where the semantic convention registry corresponding to the project exists.
Both for the… The metrics and the event.
So that's one aspect. At some point, I will find some time to finalize this work. Once we have this semantic convention registry, then we will be able to exercise, like Drew was mentioning.
We veer directly into the CAICD pipeline for all the tests and integration tests that we have, in order to have a check, a telemetry contract, which is checked directly, in the CICD pipeline.
And, like, also, like, a telemetry coverage or instrumentation coverage, I think that will be a better term.
That's also one of the goals. Now, regarding the, the documentation, we already have a lot of, We have a slash dock slash telemetry.
I don't know if you saw this one, Bartek, but, So it's already a set of guidelines.
Some generic, some specific to events, some specific to, to, metric, we have this concept in the project which is, I think, relatively fundamental for high-performance solution like we are trying to build. That's the concept of metric set.
And unfortunately, OpenTelemetry is not yet supporting that.
**Bartek Plotka @bwplotka (Google)** 38:43 Yeah, I saw that you were not using Rust SDK, and I was like.
**Laurent** 38:46 Yeah, yeah, yeah, yeah, that's… it's intentional, obviously.
**Bartek Plotka @bwplotka (Google)** 38:50 They're too hot.
**Laurent** 38:50 And the reason of that is performance. We, we really want to… I mean, when you raise on about that, and you look at every node, every element of the engine.
everything that is instrumented, and we are instrumenting a lot. I was talking during the KubeCon event, someone that was very familiar with the collector, he was telling me, or the number of metrics you have is just incredible.
Yeah, I think we have more metrics now in this project than there is in the collector. But the reason behind that…
**Bartek Plotka @bwplotka (Google)** 39:25 I think. Really?
That's not always a good thing, right?
**Laurent** 39:29 I think, in production, we, we, we had some incidents recently, inside F5, and I can tell you that, we have been able to, yeah, to determine the issue with all the instrumentation we had, and I was glad to see everything that was already embedded into the system to help us on that. So, yeah, I agree, sometimes when you have too much, it's problematic.
But the metric set concept, I think, is fundamental. Making sure that you have multiple metrics that are connected together with the same set of attributes, same timestamp.
is a huge win. And also the fact that we… we pre-declare the number for the attribute set for this group of metrics, and we just communicate, internally the… the updates.
For those metrics, is also a huge win in terms of, memory location and, and CPU usage.
And finally, the… I think I didn't review the PR that you were mentioning regarding instrumentation.
But, I saw things about CPU usage. We already have all of that, so maybe you didn't see them, but, Or maybe I didn't read entirely the PR.
**Bartek Plotka @bwplotka (Google)** 40:52 We'll double-check, I'll double check, yeah.
**Laurent** 40:54 Yeah, we will double-check. And finally, there is… An endpoint.
that you can run online, which expose a kind of semantic convention registry for the existing instance of the DFE engine.
So it's automatically generated already, and depending on the compilation feature that you selected.
Some nodes will be there, some will not.
But the production, the telemetry registry, the semantic convention registry produced into this endpoint, are, automatically adapted.
For the corresponding note. Hey!
**Bartek Plotka @bwplotka (Google)** 41:48 Great, makes sense, yeah, thanks. I think, Drew, you have… yeah.
**Drew Relmas** 41:51 Yeah, I just wanted to mention one thing about the number of metrics, just because I've also been pretty involved with standardizing metric instrumentation throughout the engine, is I think we are doing pretty well with policies in terms of being able to turn metrics on and off. That was kind of one of the issues, that… was open about, CPU memory, like, we need to have an off switch for them. So at least, the standard ones, like input and output item counts from nodes, we have the granularity to turn those on you know, at a node level. So, if I care about how long a process… this processor takes, but I don't care about how long that processor takes, I can only… I can turn on just what I need. So it's… we're trying to keep a lot of it in the operator control.
**Bartek Plotka @bwplotka (Google)** 42:41 Boop.
**Drew Relmas** 42:41 But your point about too many metrics is still well taken.
**Bartek Plotka @bwplotka (Google)** 42:45 Yeah, and, yeah, just make sure the default has a low cardinality, right, so that people are not killing their setups, and… And let's, let's document so I'm not creating new metrics where the others are existing. That's kind of, like, why there might be a problem with a lot of them.
But, thanks. And also, like, writing your own optimized SDK, like, don't worry, like, we already do this in Prometheus as well sometimes. Like, CubeState metrics have, like, a very, optimized go, like, directly writing lines into text format, because there are so many metrics, for example, so it happens… Actually…
**Drew Relmas** 43:21 I linked to a relevant PR in the chat that was remove the OTEL Metrics SDK dependency. So, we have a bunch of OTEL Rust maintainers involved with OTEL Arrow as well, so they've been heavily consulted on this.
**Bartek Plotka @bwplotka (Google)** 43:36 But they were… were they happy?
Or…
**Drew Relmas** 43:39 I think so.
**Laurent** 43:43 I think they were not against, at least, and the rationale that we provided was… Meaningful enough for them to… To accept the fact that we were following this approach.
**Drew Relmas** 43:56 I see we actually have Cijo… I see we have Cijo joining the call.
**Cijo Thomas** 44:02 Hey.
**Drew Relmas** 44:06 I don't know if you want to chime in on this topic.
**Cijo Thomas** 44:09 No, I do have some opinions, like, I'll quickly share it, like I say, maintainer for Autel Rust, I wouldn't want… OTL SDK to be used in Arrow, because we know it's not designed with the same, like, performance characteristics in mind, so it will definitely show up in profiles, and that's not something I would be happy if it shows up in profiles, that performance issues caused by Autel Rust SDK, so it's simply not optimized for this scenario.
So also, as a person working on Autel Arrow, I wouldn't want to use OTL SDK, because it will definitely kill my own throughput.
But there is another aspect, which is, as an open elementary person, I'm quite concerned that we are not able to use a project within the ecosystem in the other project. So that is giving a wrong message to the community as a whole, because we are asking the entire world to use Auto SDK, but for our own needs, we are not able to use it. So that is giving a wrong message.
I think I mentioned this few times in the past, but unfortunately, it's not something we can fix overnight, because the AutoRust SDK has to be… Redesigned or re-architected to take into account the thread local.
and also bound… those concepts are not yet there. Also, multivariant metrics. So, until that happens, yeah, we'll be diverging, but that's… acceptable for now, but I would expect that long-term, we would be able to use and follow the same SDK which we ask everyone else to use, so that… yeah, that's my two statements.
**Bartek Plotka @bwplotka (Google)** 45:39 No, it makes sense, don't worry, don't be, you know, we don't need to explain this too much, like, we… the main SDK has to be generic enough, has to have, like, all the.
**Cijo Thomas** 45:49 a chain.
**Bartek Plotka @bwplotka (Google)** 45:50 like, exactly the same as we have in, like, Go, or any, like, standard library parsing integer. I can write, like.
10 times faster parsing integer, because I don't need to check, for example, like, some checks that, you know, like, a standard library has to do. So, so totally expectable. And again, happens in Prometheus Client Golang. I maintain SDK for Go in Prometheus.
and cube symmetric doesn't work, doesn't use it, because it's trying to go, like, too slow, you know, I'm not offended by this, so it's okay, no one judging.
**Cijo Thomas** 46:19 Yep.
**Laurent** 46:22 Another aspect regarding the safe telemetry.
And I see that we have Jake with us. So the… from the beginning, what we decided to do is to follow an entity model. So a node is an entity, a pipeline is an entity, a group, and the engine itself.
channel, and so on. So they have… when… and we declare them. So we have, a registry of those entities internally.
And when you declare an entity, you provide a set of attributes, they are fixed.
Once the corresponding entity has been created.
And then you have this entity ID, which is basically an integer.
Just, encapsulated with, a small struct, but, This entity ID is used to attach any metric and event.
So there is no metric and no, events.
as far as I know, that are not related to a specific entity. So, once you have that, we have an embedded, admin UI into this project. I don't know if you saw it.
But, we are able to… So if you go to the port 8080, when you have the DFE engine running, you will see, a web UI where we are inferring automatically the topology of all pipelines, and that is mechanically done Without reading the configuration.
We, in fact, we rely only on the fact that we have those entities that are declared.
Which are interconnected with well-defined mechanisms, the channels.
And, so that gives us a very nice way to… Build automatically, from this construct, like a twin or a representation of the internal system.
**Bartek Plotka @bwplotka (Google)** 48:26 Yeah, makes sense, and also, that's why I'm writing this guide, Self-Observability, to even explain those UIs, and what you have is… so I think that's kind of my… that was my main goal, actually.
**Laurent** 48:39 Okay.
Yeah, that's a very good feedback. I think we, yeah, we definitely need to be better at, exposing this catalog of, telemetry signals.
And, and make the… this part a much more, Easier to, to grasp in the… And to adopt, yeah.
**Bartek Plotka @bwplotka (Google)** 49:01 So yeah, I think we could chat about the benchmarking frameworks, if you want.
**Laurent** 49:07 Yeah, that would be nice, yeah.
**Bartek Plotka @bwplotka (Google)** 49:11 Alright, so… I don't have, like, a strong opinion, like, I'm new to Rust, like, one month, and the first thing I did was I created this benchmarking framework, because, again, I'm used to bench that, and it's just kind of my preference. I was working with it for so long.
And I feel it has nice features to it, but I'm coming from Go, so people coming from different languages or Rust, probably they don't have the same feeling, so I'm biased. But I… and also, I didn't check every possible alternative that you mentioned.
But I'm… every Prometheus project now will use Bench FMT RS, RS, whatever, and in my PRs, if you don't mind, I will show the output of those, and I will write temporary benchmarks if needed. So I'm not super, like… I don't, you know, up to you, you don't need to adopt this, but I'll be using it, and I want to share it, and it's up to you, like… But what I want is, like, every PR should have a micro benchmark. That's kind of the main goal.
**Laurent** 50:13 Yeah.
**Bartek Plotka @bwplotka (Google)** 50:13 of mine.
**Laurent** 50:14 Totally agree. No, I'm… personally, I'm not against… I think we should start with, A subset of the project, exercise that.
Si, how good it is, how accurate it is.
And, and including the… so elements that we don't really have right now, the… that you have into your system regarding the memory consumption.
definitively interesting. We, we, we were working with the… the main contributor of Mimaloc.
We had, he's part of Microsoft, so that's nice. And we had a discussion a few months ago about, memory profiling, so now that it's part of… it's part of Mimalog, so that's also, something that we should leverage.
Because it's, very low, override in terms of implementation into BMalloc.
And that will provide us even more granular visibility I think it's also supporting the PProf, the people format, which will also be closer to what you are used to to use with, with Go, Yeah, I'm absolutely not against, I'm just saying that, before migrating everything, we should try and,
**Bartek Plotka @bwplotka (Google)** 51:38 Let's.
**Laurent** 51:38 And maybe improve, and then at some point, most likely to adopt it.
**Bartek Plotka @bwplotka (Google)** 51:49 Thank you, yeah, that's what I want to hear.
**Drew Relmas** 51:55 So I see we have about 8 minutes left. If there's any other topic from someone on the call, feel free to bring it up. Otherwise, maybe we end a little bit early.
I guess.
**Bartek Plotka @bwplotka (Google)** 52:15 Can anyone share anything about KubeCon? How was it? Anyone…
**Drew Relmas** 52:18 That's actually what I was about to ask Laurent about.
**Laurent** 52:21 Oh, okay, yeah.
**Drew Relmas** 52:22 I mean, stories.
**Laurent** 52:24 Yeah, KipCoin, it's… so we had a talk, Monday, went well.
We basically talked only about the Hotel Arrow project, and it was… Talking about the Phase 2 of this project, so no longer too much about the protocol, but more about the… The engine itself and the performance.
So, seeing what Bartek published, this morning on LinkedIn is fantastic, because it's, it's a very nice validation, from, someone not necessarily initially involved into this project, using it, so that's, fantastic. Then, We had, a nice surprise, someone from a buying plane.
That was, was there, during the, the talk, and came to us, and, told us, oh, I have a demo for you guys, Joshua and I.
Okay, show us. And it was, an integration of the Dataflow engine into their, control plane, buying plane, which was fantastic to see. So they basically, integrated the, op-amp, Protocol that we support directly into their system, and they were able to basically live reconfigure, expose the internal pipelines, read the various telemetry signal that we expose.
That was pretty cool.
Otherwise, I mostly discussed with… oh, no, another thing, it was also a good opportunity to discuss with, the various members of the governance and technical committee from OpenTelemetry.
And, I think the… The global message for us is, they are now much more open to re-discuss the positioning of this project, against the collector.
I think the, the… I don't want to talk for them, so I will be careful, but what I understood is the fact that, we are innovating a lot in this space with what we are doing. It's not only about performance, but we have some mechanisms, some, Some elements into this, new engine that are relatively unique.
And, they are thinking that we are really innovating, and that's the place where they want to see, this collector's story, moving. Not to… let's say there is definitely other competition in this space, and they want to keep up, and I think it's definitely a good project to achieve that.
So I think we will reopen conversation with the governance committee, in the following months, in my opinion.
And probably define a plan on how that could work, and making sure that the community will not be hurt, and and we will have a good message and a good integration between these two, these two systems.
So it's way too early to have the detail, but that's definitively, I had a multiple reaction, around that.
A lot of things, obviously, in KubeCon related to AI, connected to observability and telemetry, the classical MCP, API, to… Ask an agent to discover things.
root code analysis, automated with AI, this kind of stuff. Nothing really new, I mean, it's something that we see now for more than a year, but some kind of generalization among the various vendors.
Trying to remember the various interesting things.
Yeah, a lot of discussion around, storage of telemetry.
I briefly mentioned that, so a discussion with, Brian, one of the top, data flow… the data fusion maintainer.
Talking about what they are doing in Pydontec.
And, how they store matrix, how they store span, and so on.
Basically a flat schema.
And like I said before, They accumulate in memory, let's say, enough signals, and when they decide that it's enough based on their… buffer limit. They, determine on the fly the corresponding schema, so basically merging the various attributes, that will form, a wide, table.
They also derive the data type for each of those columns based on the values. So, for example, for the matrix, sometimes it's a combination between integer and float. So they have different rules and conventions to serve this kind of, change?
And then, once they have this batch and the schema inferred, they are basically, storing that into Parquet or Vortex, and and then Data Fusion is flexible enough To have a unified representation of those values files, that's where the schema are not exactly the same.
So we had a discussion around that, and it looks like, every vendor that are, involved in data fusion and using it are following more or less the same approach.
Yeah, I will say that's it.
**Drew Relmas** 58:42 That's… that's good, and all good stuff.
Well, we're at the end of the hour, so another SIG meeting done. I'm gonna go read Bartek's LinkedIn post now.
**Laurent** 58:53 Yeah, thank you so much, Bartek, for that.
**Bartek Plotka @bwplotka (Google)** 58:57 Copies of mine, I'm making this public, kind of.
**Laurent** 59:01 That's true.
**Bartek Plotka @bwplotka (Google)** 59:02 I honestly think with the Thanos and what you do in the collection, like, we can… we are bringing some competition, some vendors, is what I'm saying.
**Laurent** 59:11 Yeah.
**Bartek Plotka @bwplotka (Google)** 59:14 Yep.
**Laurent** 59:14 Definitively.
I agree.
Alright? Okay.
**Drew Relmas** 59:19 Bye, everyone. Have a good day.
**Laurent** 59:20 Bye. Have a good day.
**Bartek Plotka @bwplotka (Google)** 59:21 True.
