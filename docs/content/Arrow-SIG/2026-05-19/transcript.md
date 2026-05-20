SIG: Arrow SIG
Date: 2026-05-19
Duration: 65 minutes
Zoom Recording URL: https://zoom.us/rec/share/yppdKfgLWfrcCdeEw36UvtQXACM-24i0LlqfivVnDC66vw-E9i4t1LV8FuOo6eXW.GKml31wWsVrcZxZc
============================================================

## Zoom Recording Transcript

Albert Lockett 00:00:08 They will…
Will Butler 00:00:11 Albert?
Laurent Querel 00:00:33 Hi, everyone.
kennedybushnell 00:00:37 Oh.
Will Butler 00:00:38 Hello!
Laurent Querel 00:01:35 So we have today…
jmacdonald 00:02:45 Hello, everybody.
Laurent Querel 00:02:47 Le Josh.
jmacdonald 00:02:50 payroll.
Laurent Querel 00:02:50 the session today, or…
jmacdonald 00:02:53 I had no special desire to, but I'd be glad to. I realized that I missed the last meeting sort of unintentionally.
last week.
Laurent Querel 00:03:03 Yeah, look for them.
Yeah, last week was, more about, Yeah, we talk a lot about the plugins proposal.
And, I think we… unfortunately, we didn't put too much, which, that's… We didn't put at all any summary there, which is my fault.
Story for that.
maybe we can… I don't know if Aaron maybe wants to continue the conversation on that, I think we didn't, really finish.
And there are probably some additional, perfect to discuss.
I know that, I don't know if C. Joe will be there to talk about, the situation, benchmark.
Jake is there, we have, A new version of the public, benchmark, also.
We have some early results for staff that could be, Even if it's not, fully finalized, but…
jmacdonald 00:04:17 Stop.
Laurent Querel 00:04:17 Maybe that could be interesting topics.
jmacdonald 00:04:23 Yeah, it sounds great. I think we should start with the triage, unless you think it's, worth, sort of giving up on the whole triage thing.
Laurent Querel 00:04:32 Yeah, yeah.
Okay, so we are… I don't know, issue… Last week, entire first.
jmacdonald 00:04:47 We're just triage deciding, maybe, that we didn't update those.
Laurent Querel 00:04:53 Let me see, I think we didn't. That, I remember we talked about that.
I think that… yeah, I think that was discussed, that also… that also… This one… Not remember exactly.
Jake Dern 00:05:11 We did. We covered it.
Laurent Querel 00:05:13 Brilliant? Okay.
Jake Dern 00:05:16 As much as we could.
jmacdonald 00:05:19 Yeah.
Laurent Querel 00:05:19 It's like just the first.
jmacdonald 00:05:20 Thank you, then, for today.
Laurent Querel 00:05:21 Yeah, so… What did you say, Josh?
jmacdonald 00:05:26 I think it'll be just the first page, then, that's new.
Laurent Querel 00:05:28 Yeah.
Okay, so… that's done.
It's updating… And then we should move on to… Okay, go back there.
Okay. And then… revert commit… Yeah, I don't think we talked about that, support life pipeline generation. Well, this one, I remember. We talked about it a bit, so probably we talk perfect also about that status, conditions, semantic.
Looking at the two… That's true.
The two… I think we may probably end up here.
So let's… Biage.
accepted.
Kevin?
Yeah, so in… So the binary site tracking, I guess it's something we want to track during the… In the CR pipeline, I guess.
In general, I don't think we have any, CIOT observability, right?
Do we?
jmacdonald 00:06:54 I know we filed an issue to start tracking it eventually, because it is a pretty important metric for us.
Jake Dern 00:07:00 We have a step for this, it just, it was failing for a long time.
But I think it's supposed to be fixed now?
Laurent Querel 00:07:09 With this one?
Jake Dern 00:07:10 Yeah, CJ thought that merging this PR would fix it, and it's merged.
Laurent Querel 00:07:14 Okay.
Cijo Thomas (Microsoft) 00:07:16 It should be closed now, I just said it's working now.
Laurent Querel 00:07:19 Okay, and how can we see Joel look at those, Next week's… for the CI pipeline.
Sorry to be.
Cijo Thomas (Microsoft) 00:07:31 Sorry, I… yeah, we don't have any metrics about the CA pipeline itself.
It was just, like, yeah, the performance test. One of them is slicing the binaries size itself.
Laurent Querel 00:07:47 Can you, sorry, go ahead, Josh.
jmacdonald 00:07:49 There's a chart link there, can we use that link?
Laurent Querel 00:07:54 Did you say?
jmacdonald 00:07:55 The chart link is on the bottom of the PR description.
I wonder if we can just click that link.
Cijo Thomas (Microsoft) 00:08:01 Oh, no, no, the issue description. Issue description.
Laurent Querel 00:08:04 Oh, okay, okay, sorry.
Cijo Thomas (Microsoft) 00:08:06 Yeah, that should be filled with, expand the scenario charts.
Here, now we should see both.
dots coming from history.
Laurent Querel 00:08:15 Okay, okay.
Cijo Thomas (Microsoft) 00:08:17 Yep.
Jake Dern 00:08:19 Yeah, I think the purple dot was the broken one.
Cijo Thomas (Microsoft) 00:08:21 Yep.
Laurent Querel 00:08:22 But in general, I remember some OpenTelemetry projects, that's… get, in some way, some, for example, duration for every CI stage and other things like that. So is this something that we can enable?
Not necessarily related to this, Benchmark that we do ourselves, but, maybe I dream about it, but I think there are some…
Cijo Thomas (Microsoft) 00:08:54 There is no free thing, like, yeah, I don't think there is anything built in which will…
Jake Dern 00:08:59 I thought GitHub Actions had something for that. Just when I was poking around in a dashboard on my fork the other day, I thought GitHub Actions might have some stuff.
I don't know, I could be wrong.
Laurent Querel 00:09:09 Yeah, that's something we could explore, maybe. And, maybe, we could ask, maybe Trask, or, Drew?
I try to remember the guy that was part of semantic collection.
He was, part of the SIG, CI… And I remember that he was mentioning a lot of, Internal observability integrated into semantic convention projects, and… And a few additional other, client SDK project to look at CI phases, tracing of it, and some, Some rendering and charts about that.
jmacdonald 00:09:55 Hmm.
Laurent Querel 00:09:57 Would be interesting to follow, for example, the… if we are going in the right direction regarding the duration for the PR, and In the build process in general, or if we are just accumulating.
jmacdonald 00:10:11 Well, we sure were accumulating binary size, it looked like, there, having risen from 80 to 100 megabytes.
We should start to have a stable target.
Laurent Querel 00:10:22 Yeah, that's true. We… Yeah, we passed from, 6080 to something like close to 100, 115.
Yeah.
It's not too big, but yeah, definitely be, And do we know if this binary size is… I mean, we don't have any clue about the… I guess that's the default feature.
Cijo Thomas (Microsoft) 00:10:53 Yeah, this is just a default feature. I don't think we…
Laurent Querel 00:10:55 Hmm.
Cijo Thomas (Microsoft) 00:10:55 One with… which enables all the features.
Laurent Querel 00:10:59 Okay.
jmacdonald 00:11:02 Thank you.
Laurent Querel 00:11:05 Okay, so that's, particular… Sorry, I'm lost. Okay, let's see y'all.
add structure entropy to see… so, Sidville, you want to talk about that?
Cijo Thomas (Microsoft) 00:11:22 I… I'm actually… I'm not prepared for it, so I'll have to, like… Okay. I'm still experimenting with… Sure. A few things on that thing, so maybe in another week, I'll come back with.
Laurent Querel 00:11:32 Yeah.
Cijo Thomas (Microsoft) 00:11:33 a bit.
Laurent Querel 00:11:35 Okay.
So this, okay.
binary plugin system for a top… So that's, Yeah, probably that's, the outcome of… Oh, that's what we discussed last week, sorry.
Right, Hong.
Aaron Marten 00:11:55 Yeah, yeah, there really hasn't been any change to that since last week, although I did leave a comment where I tried to capture some of the Especially from last week, and some of the offline feedback.
Laurent Querel 00:12:09 And did you also, trying to figure out if you added, A comment about, having the concept of WASM extensions. Extension in the sense of what we have today, where we We have pipeline extension, we have group, and we will have group extension and engine-level extensions.
We could imagine that at some point, those extensions could be implemented not only in REST, but also as a WASM plugin.
Aaron Marten 00:12:42 Yeah, I did mention in the proposal, the notion that you could have, you know, receivers, processors, exporters, and extensions… Oh, okay.
Laurent Querel 00:12:53 Oh, okay.
I see.
Thank you.
Aaron Marten 00:12:56 There… not a lot of design around that, but it is captured there as a requirement.
Laurent Querel 00:13:02 I definitively to read that, more carefully, Let's see, I just need to open that into another tab for me to read it.
Okay.
jmacdonald 00:13:18 I just wanted to say thank you. This is why I was sorry I missed the last meeting, and I really liked the proposal from Aaron, having read it. Thank you very much.
Laurent Querel 00:13:27 Okay.
Great. Yes, thank you.
That will definitely be a great addition to the… To the project, to have this, wisdom support.
Definitely to have an ecosystem that is, Under control and, very extensible at the same time.
Adoptional Lumaware, SOU Sport… oh, yeah, that is cool.
I think, Islamit is with us.
Yeah, I'm dead. Oh, yeah, you are, you are. Perfect.
You want to say a word about that?
lalitb 00:14:09 You're fine.
Laurent Querel 00:14:10 probably saw this, stuff also, I could be passed.
lalitb 00:14:12 Yes, I did put that reference in the… Issue?
And I think probably the issue talks about The details, what exactly we want to do.
Yeah. So… Yeah, I mean, nothing more to say, but I did do some prototype testing, for, load balancing for the ports in a single NEMA node, which kind of… I mean, for my basic rough, some tests, I think it looks to work fine, but, too early to say anything. But yeah, I'll…
Laurent Querel 00:14:47 Okay.
lalitb 00:14:48 Probably, come back to this once I'm done on general de-export to a receiver.
Laurent Querel 00:14:54 Excellent.
And for the EDPF stuff, did you use the… I don't remember the name of this, rest… they are different.
lalitb 00:15:03 No, I didn't… I didn't use… I think II is one of them, but I used libbpf.rs.
Laurent Querel 00:15:11 Okay.
lalitb 00:15:11 So, II is more, more heavyweight, you just want, probably.
I… that's the reason why I… as of now, I'm using libbpf.rs.
Laurent Querel 00:15:23 Okay.
Okay, great. Okay, anyway, that's a very interesting exploration.
Oh, that will be nice, also.
We can do a lot of things with that. Okay, excellent.
Do we, do we have, because I remember last week we talked about, Some optimization we need to achieve in order to support, server with many human nodes and CPUs, and do we have, not directly related to that, but, the pneuma stuff reminds me that. Do we have somewhere… A list of requirements.
describe into, as a GitHub, issue.
To drive the future development around that, just to be ready for this kind of deployment.
lalitb 00:16:21 Not that I… No, I won't.
Laurent Querel 00:16:24 talk about that with, with Kennedy, or, or, don't remember.
jmacdonald 00:16:31 Yeah, I… there were… there were notes taken at last week's summit, and I did write down one section that was sort of like, everybody agrees NUMA, and we don't… I don't believe we have a… at least a fresh design document calling out NUMA-specific requirements.
For myself, I was tasked with writing something about multi-tenancy issues in general, and NUMA's gonna feature there quite a bit, but I think you're right that we would like to have a dedicated NUMA document.
Laurent Querel 00:16:59 Yeah, yeah, I think we… we… it will be even before to see how we… We enabled that with, some… some configuration.
And more importantly, with a controller that optimizes the Luma deployments.
Having a good understanding on what will be the ideal option for this kind of deployment on Bing Machine, Big Server.
For the Microsoft use case.
Will be great, because from there, we can, Have a second iteration and start to see how that could be integrated into the… The control… the local controller.
jmacdonald 00:17:43 Right, I've also… I'm sort of aware of wanting to have dedicated ports rather than having SO reuse port fanciness, but I'd like to hear from Kennedy.
kennedybushnell 00:17:55 I'm gonna say, like, I think a dock around… teaching OTAP Dataflow NUMA awareness. It's NUMA-friendly right now, and it has the right plugs in place for us to make it NUMA-aware, and it's more than just the big machine. The big machine exacerbates the issue and makes it a big problem, but even on a… on a, you know.
as soon as you have two NUMA nodes, you can have the problem where you're pinning the CPU or pinning your thread to a CPU that isn't directly attached to your network card, or any resource that you're touching. So, being aware of that and being able to make, like, a weighted decision to drop and pin on the right CPU would be awesome.
Laurent Querel 00:18:40 Definitely, yeah, that was the goal initially, but we never, PDFER achieved that, Definitely align with that. Making sure that we minimize the… the cross-communication between me and Od, that's the goal.
Independently of the… the size of the machine. And like you said, it could be because we have a… SmartNik, or we have a disk attached to a different mannode, and that will not be optimal.
Okay, cool. So yeah, maybe at some point I will have some time to dedicate to that, but if someone wants to… Just describe them.
The requirement level, that will be nice.
Enable co-pilot… automated copilot call review for these people. Yeah, I think that's… oh, that's his proposal. Let's see.
Cijo Thomas (Microsoft) 00:19:43 It's done already. Tom has created issues.
Laurent Querel 00:19:46 It's so cute.
Cijo Thomas (Microsoft) 00:19:47 Never.
Laurent Querel 00:19:48 Okay.
Oh, yes, yeah, yeah, I saw that. That's cool, so we can close this one, right? No.
Cijo Thomas (Microsoft) 00:19:55 We can actually close, yeah, the community issue is closed, so we can just close this one too.
Laurent Querel 00:19:59 Okay, excellent.
And just a question regarding that, because I'm not fully, I don't know perfectly how the Copilot review stuff works. Is the Copilot review capability leveraging the agent.nd, and potentially the… the document linked into this agent.nd, or we need to do something else to leverage, for example, the… the document I added recently regarding the specific code review for the repo.
Cijo Thomas (Microsoft) 00:20:44 I need to take a look, because we do have agents.md and other files. I… I believe the reviewing co-pilot will take a look at that, and if that is pointing to the newly added document, it should take that into consideration.
But it.
Laurent Querel 00:20:58 for TV.
Cijo Thomas (Microsoft) 00:20:58 verified.
Laurent Querel 00:21:00 Okay.
kennedybushnell 00:21:01 Yeah, so it'll pick up the agents.md, and then depending on which model is selected, it'll pick up those instructions, because there's, like, ClaudeMD or Copilot.
It's called Copilot Instructions, so yeah, it'll pick up those types of things. We just need to make sure that your documents that you added are in one of those, or maybe even all of them, so that they certainly get picked up.
Laurent Querel 00:21:27 Okay.
Brilliant. Thank you.
jmacdonald 00:21:32 And I think… just start experimenting, because I think you can tell when it does or doesn't have the correct instructions.
I'm also slightly concerned that those instructions that you wrote are kind of more for humans than for machines, but we'll.
I work.
Laurent Querel 00:21:47 Okay, yeah, I'm using AI, and I think that also depends on the model. I'm definitively using them with, with Codex regularly, and I'm relatively happy with it, but doesn't mean that they are necessarily fully optimized.
Depending on the model, and probably that could be improved, maybe summarized.
I know that, more we… bigger those instructions are, lower is the… smaller is the con… the useful context for the code, so you probably need to take care of that also.
Adding compressed by parallel metric to traffic generators. See, Joe, you want to talk about that?
Cijo Thomas (Microsoft) 00:22:32 Mmm…
Laurent Querel 00:22:34 Oh, it's too early.
Cijo Thomas (Microsoft) 00:22:35 un… Yeah, I think this already has a PR, so what we… what I was trying to do was almost all the performance tests, it… like, few weeks ago, I noticed that we were getting, like, unrealistic compression ratios.
Because we are able to hit, like, compressor.
Laurent Querel 00:22:53 $1.
Cijo Thomas (Microsoft) 00:22:53 200 kind of thing. And we didn't have an easy way to tell by looking at any of the benchmarks itself what is the actual ratio, and we kind of, have to guess, because we know the input size.
whether a log is, on an average, like, 300 bytes or 400. We know that, and we have to use that knowledge to figure out the actual compression ratio. So this proposal is simply to add a metric to the log generator.
Which will emit… it has a bunch of metrics it's currently having. So this is just an additional metric which tracks the… Uncompressed size of each log, individually.
metrics and spans. Once we have this metric, and then we can look at the performance suit, and then compare what is the actual ratio. So this is very, like, small PR on its own. It should be… Yeah, I thought I made the PR. Yeah, okay, the PR is there already.
Laurent Querel 00:23:51 Yeah, that reminds me of something. We had so many PRs during the last few days that.
Cijo Thomas (Microsoft) 00:23:56 Yes.
Laurent Querel 00:23:58 Yeah, that's good.
That reminds me also a discussion we… some of us had on the Slack channel.
We're getting the traffic generator.
The debates regarding static versus, semantic conventional-based.
Cijo Thomas (Microsoft) 00:24:22 So, that's the thing which I said I'll need some more time, because it, like, every time I explore, I learn, like, something new, because there is this entropy within a batch, which is affecting compressibility in, like, OTLP, and then for OTAP, it looks like it has gross batch compressibility, so if you repeat the same thing in the next batch, it has… like, OTAP is able to leverage that. So I'm still exploring that to figure out, like, what is the right thing.
to use in that traffic generator? Like, should we just rely on semantic conventions as we do today, or should we… do a modified version of that, or should we write, like, our own, or do something like… there are, like, Collector Ripper has their own load gener… traffic generator, forget the name, yeah. So maybe, like, in another few days, I'll get a good summary of what's the current state.
Laurent Querel 00:25:19 I can give you my, my, two cents.
Cijo Thomas (Microsoft) 00:25:22 Go there.
Laurent Querel 00:25:23 And my analysis of the current problem, ultimately, in my opinion.
It will be better to rely on semantic convention. Unfortunately, the current semantic… and I will explain why.
Currently, the semantic conventions are far from… Being equal in terms of, signal description.
We have a fair amount of metrics, so it means that, The current implementation of this, perfect gen based on Semantic Convention, is doing a relatively good job, in my opinion, for metrics. It's not the case for events, because we… the pool of existing events is very low, so that's why we observe Too much, repetition.
For logs? Because you're, you're, Test was only based on logs and not metrics.
Cijo Thomas (Microsoft) 00:26:24 Only logs, yeah, yeah. And what you said is that we only have 25 or 30 events in the entire semantic conventions, which we are.
Laurent Querel 00:26:32 Yeah. So, yeah, exactly. So what we could do is, and what could be fun is… Generating a semantic convention registry.
For the project itself, based on the existing metrics and, events that we have into the system. Anyway, it's interesting with the other, I think, work that you did, to, to check, for example, the us metric.
Internal telemetry generated from the osmetric receiver, if I remember well.
Cijo Thomas (Microsoft) 00:27:07 Yep, yep, that didn't be that license.
Laurent Querel 00:27:09 Yeah, so we could let some that.
To all the internal telemetry, covering all the events and all the… The metric, then we will have a registry that will be Fairly significant in terms of, Number of signal for event and metrics.
We could add the… the span from the, the standard semantic convention. Then we will end up with the semantic convention that starts to be big enough To generate a useful traffic.
And why I prefer that, it's because… We know that a standard traffic will follow some pattern.
In semantic convention, there are attributes that are marked as optional, some are marked as, Required.
So we… we should be able to have some variation, Some attribute that will be purely freeform.
Some attribute that will be, a selection among a list of possible values, the idioms that are defined into the semantic convention.
That should be a very good representation, or very good synthetic traffic, in my opinion.
And at the end of the day, We should be able to validate the compression rate for different protocols.
And it's not only about compression, right? It's also about the CPU usage. That's something we, we saw yesterday, Jake and I, during one of the benchmark sessions, OTAP is not only about… the fact that you compress a little bit… you compress more than OTLP, but you compress less than Steph, for example.
But even if, we compress the same size, The same initial batch.
Between OTLP and OTAP.
the CPU cycle consumed to compress OTAP batches will be much smaller than the number of CPU cycles used to compress the same batch for TLP.
Because… the entropy will… is higher for TLP. It's not well organized, it's, like, hierarchical, organized by row and so on, versus organized per column, where we have some orders, some sort that is Done before compression.
And it means that you will reach much… Faster, good completion rates, so the, the… The compressor will, will, will not use as much as CPU cycle to get a good compression ratio. That's my thought.
And that will be well exercised if we have also A good representative, generated traffic.
With… with, for example, repetition for the attribute name, but not necessarily repetition… a lot of repetition for the values. Ideally, for the metric, we need also some… something that looks like a real metric stream, where everything is not necessarily super undone.
The data delta encoding, that, was, for example, used in Goria from Facebook, demonstrate that most… most of the time, metrics are not purely random, they are following some pattern, and they are not, like, going across the… the scope of possible value, every data point, there are… there are some… Delta that are not too big.
No pros and gentlemen.
jmacdonald 00:31:09 This all sounds good. I don't want to, I wanted to add to that topic that… I've got a proposal open about the metrics… internal metrics SDK work, where I've proposed having a detailed level metric that would tell you the bytes of payload size for basically all the… all the components, since that's sometimes a useful measure to know.
And I wanted to recall back to the Phase 1 components. The OTIL Aero receiver in Phase 1 had an integrated admission controller for basically limiting memory of the current in-flight request batch.
And what was nice was to have an integrated measurement of the byte size of each request uncompressed.
combined with an admission controller limit that was effective over that same number. So, you would compute the size of a request once, you would request it from the memory limiter, and that would automatically enter it into a Uncompressed bytes measurement, which would be both a counter for rate computation, as well as a memory resource counter, which is an up-down counter, counting live bytes in the pipeline.
Just to say we should have that for basically all components.
Laurent Querel 00:32:22 Yeah, yeah, which is… yeah, okay, I see it.
Which is different from what we discussed just before, but I understand the need, yeah.
jmacdonald 00:32:31 Yep.
Cijo Thomas (Microsoft) 00:32:32 Yeah, for this one, like, the fact that our Existing semantic conventions for events is… quite, sparse. I think, it should be relatively easy for us to tackle that based on what you described. Like, we'll define a semantic convention.
for our own internal event, and then use that as the source. Okay, I understood.
Laurent Querel 00:32:53 Right, because that, that will, that will solve two problems, in, in, in one,
Cijo Thomas (Microsoft) 00:32:58 Yep, exactly.
Laurent Querel 00:32:59 Did you win it.
Cijo Thomas (Microsoft) 00:32:59 Great timing, actually, because I also already created some issues in the semantic conventions for the semantic convention to define SDKs, internal events. I didn't include, like, arrow there, because it's not considered, like, an SDK.
So hopefully, like, we can just define our own events in our own YAML, and then solve two problems in one shot, yeah. I'll… I have a draft for that already, so I'll share it, most likely by early next week, because, like, next three days.
Laurent Querel 00:33:29 weekend.
Cijo Thomas (Microsoft) 00:33:29 paper.
Laurent Querel 00:33:30 Excellent.
Cijo Thomas (Microsoft) 00:33:31 I got the idea, like, we generally prefer, let's use more realistic load by leveraging semantic conventions to give that load for us, and right now, it's not doing a very good job for events, which We can also fix.
Laurent Querel 00:33:45 Yeah, there is a French expression, I'm sure I'm not translating that properly in English, but Something like, you kill two targets with one stone.
Cijo Thomas (Microsoft) 00:33:55 Yeah, yeah, we, we use the, same thing. It's two birds, two birds with one stone.
Laurent Querel 00:34:02 Yeah, okay.
Sorry, add a higher rate to the single-core DFE test.
Oh, that's the idea field. So, okay, that is a recent thing that, so, Jake is working on adding, data fluent gene baseline for staph.
So there is, an open PR. I'm not ready yet for… preview.
But, it was good enough for, running… a set of tests. I think maybe we will let Jake talk about that later.
Isn't it ostimetric? For people that are not aware of what is TEF, TEF is, like, a third Not necessarily endorsed official protocol for open telemetry, but that's something that, followed OTAP, With a different trade-off.
It's, trying to get the maximum in terms of, compression… to the… But it's not a purely columnar loyalty, not leveraging Arrow, so the trade-off is more, when you have to communicate telemetry across different data centers, that could be a good fit. If it's about processing a lot of telemetry.
Whatapp will be a better, a better target.
Jake Dern 00:35:39 Hey Laurent, just real quick on the, task right before the Steph one, the higher rates.
Laurent Querel 00:35:46 Yeah.
Jake Dern 00:35:46 This is probably the most, like, interesting one that I have open currently. I just wanted to mention, So, like, yesterday I posted in Slack as well, I ran an experiment with some higher rates, and I did observe, some saturation at different points, for the data flow engine, so… Not that we have to discuss it too much here, but, yeah, I did see some saturation, at different points for metrics and logs.
Without compression, and then at the same point for metrics and logs when ZSTD compression was involved, so… Yeah. Something worth following up on, but yeah, metrics with no compression topped out at about 21% CPU utilization, and I couldn't push it higher.
And logs topped out at about, 47%, and I couldn't push it any higher than that.
Laurent Querel 00:36:32 Yeah, we had a discussion yesterday, I think, about that, yeah, really well.
Yeah, that'd definitely be something to investigate and see if we can, Yeah, improve the situation there a little bit.
Okay.
is an electro symmetric clock, so that's valid.
Onto talking about that.
We lost it. Okay, that's, crypto feature or not.
jmacdonald 00:37:25 We want to talk about.
Laurent Querel 00:37:28 Sorry.
jmacdonald 00:37:29 This next one is important that we talk about a little bit. It's just about setting the default crypto library for Windows versus other platforms. There seems to be some chaos. This is proposing to clean it up.
Laurent Querel 00:37:42 Okay.
Sounds good.
So that's what I'll… yeah, unified expression evaluation. I think Albert is there. Do you want to say a few words about this one?
Albert Lockett 00:37:55 Yeah, sure, just briefly. We basically have, when we're evaluating expressions, like, in our query engine, we have one code path for filters, so basically all expressions that return, like, binary or booleans, and we have another separate code path for every other type of expression, and… that is… I… I don't like it. I wish that they were unified. So this work item is basically, like, unify the two code paths, so we just have basically one way to evaluate expressions in the query engine, just… I think it'll just make maintenance easier, and… Make the… make it more easy to add different types of expressions, because you don't need to add them in two places and worry about it, so…
Laurent Querel 00:38:37 Perfect.
Albert Lockett 00:38:38 I'll be working on this this week.
Laurent Querel 00:38:41 So it's… configuration time checking for flow metrics and reachability. I remember seeing that.
Will, you want to talk about that?
Will Butler 00:38:54 Sure, hello. Nice to meet you.
I was just going through some of Drew's items around flow metrics, just to kind of teach myself the feature and some internals, and in the PR for one of those, Lalit called out an extra edge case we've been hardened against. Basically, it's possible in the config to create a flow metric where the end is before the start, and so we've already implemented a BFS walk of the processor tree, so it's very straightforward to add an incremental check for this. I almost just sent a PR, this is a really small change, but I figured I'd err on the side of documenting my work.
Laurent Querel 00:39:28 Excellent. And did you… I remember also a comment about, checking that there is a pass between the start and the end.
So that's.
Will Butler 00:39:39 Yeah.
Laurent Querel 00:39:39 There is a connected graph between these two nodes.
Will Butler 00:39:43 Yeah, mentally, these are the same for me. I can make the issue a little more explicit if you like.
Laurent Querel 00:39:47 Okay, no, no, no, that's okay, if it's in the PR, that's perfect.
Will Butler 00:39:51 Okay, I haven't done the PR yet, but I'll send it in next week.
Laurent Querel 00:39:55 Okay, great.
Will Butler 00:39:56 Thanks, sir.
Laurent Querel 00:39:58 I think in general, not related to this one, but, I think it's true for, It was part of my review also yesterday for the extension.
I think we need to create, in my opinion, a checklist Somewhere, an explicit checklist for when someone is creating some kind of configuration header for the component, like receiver, exporter, processors, but also for the exemptions.
We'd like to end up to a situation where We can validate that, a specific exca… sorry, a specific configuration is Correct, not only, at the high-level structure, but also correct for the individual components and extensions.
And that's not only when we start the engine, but also when we run the… the LIVO configuration, which is… Probably something where we need to… improve a little bit the existing code, because I think there is two… Two locations in the code where this validation is done.
But, we, we shouldn't… Be able to end up in a situation where If something is… Valid in terms of, configuration structure.
When we start the engine, or when we use the dry run option that Sigio created a long time ago now.
We should be able to be sure that it will also work for level configuration.
Okay, rename static to synthetic in traffic generator code… I think there is someone working on that, right?
Cijo Thomas (Microsoft) 00:41:57 There is a PR already, so we can skip it now.
Laurent Querel 00:42:01 Okay.
Package AI assisted development guidance has imported… yeah, that's something… We… We discussed briefly previously, and methodologized.
Oh, yes, so Jake, you want to… discuss about that, and I will open the… In between the… The benchmark, we compare… Yeah, right.
Jake Dern 00:42:35 Not slash benchmark slash compare, just slash compare.
Yeah, extension should do it.
Yeah, for the methodology tab, I think there's just a few details that are kind of left unsaid.
In terms of how we're generating the load, and, you know, what exactly is in the load that we're generating, and that kind of thing. There's also some details about, well, like, what exactly are we testing here? Like, what capabilities does the engine have? Are there synchronous acknowledgements coming back? Like, that kind of stuff.
So, just some things to be mentioned. I'm planning on basically adding more tabs next to that test details header there.
And just, you know, putting something in here that lets us explain, like, okay, this is, like.
What the experiment is doing, like, you know, this is the characteristics of the load that we're generating, and, you know, we're testing with synchronous acknowledgements and all that kind of stuff.
Laurent Querel 00:43:25 Great. Any question on that?
Okay, yeah, I strongly encourage to also look at the… this, website, Oh, you to bidgies.
To… to get feedback from you guys, Right now, based on the decision we made last week, we only have the result for the data for engine.
But, yeah, having, feedback on that will be, definitely useful.
Cijo Thomas (Microsoft) 00:44:05 I have one question on that. Like, where is the data stored? Like, is it just in the benchmarks branch, and… Yep, where is it pulling this data from? Okay, is it in…
Jake Dern 00:44:17 Yeah, Benchmarks branch, yep.
Cijo Thomas (Microsoft) 00:44:19 Can, like, can we, like, leverage our own, like, nightly runs to populate the data? Because right now, I think you are running it in a separate machine and feeding the data?
Jake Dern 00:44:31 Yeah, that's correct. So the reason I'm doing it that way is just because it takes so long to get the data for this. So, like, the data for those runs took about 24 hours to produce.
Of content.
Cijo Thomas (Microsoft) 00:44:42 Okay, so trainer.
Jake Dern 00:44:42 Because of the number of rates in the observation interval?
Cijo Thomas (Microsoft) 00:44:45 Yeah, so once we get, like, a powerful machine, from the CNCF, we should be able to, like, run it, like, once every week or something.
Instead of the… because when you're running it, you kind of manually have to run it, right? It's not, like, fully automated.
Jake Dern 00:45:02 Yeah, I have an agent administer, and…
Cijo Thomas (Microsoft) 00:45:04 Yeah, check.
Jake Dern 00:45:05 check the results and stuff, you know, kind of in the background, and then I, you know, I kind of check everything before publishing. But yeah, you're right, it's not ideal. And, like, something else to note is, like, yeah, it takes 24 hours, and, like, all we have are the baselines on this chart.
And there's not really a way to speed it up unless you have a machine big enough that we could do, like, multiple runs at one time, for example, or try to do something clever where, you know, we run, like, one benchmark on some cores and, like, a different one on, like, another one or something. The time is, like, pretty much early determined by The number of, like, tests you want to run in terms of rates, and the number of suites that you have.
Cijo Thomas (Microsoft) 00:45:41 Okay, yeah, so there is already an open issue in the open elementary community to get us more machines, because there is a single machine everyone is fighting for.
I think we would get, like, a new machine if we really asked for it, like, with some justification.
The reason why I didn't push for it earlier was the machine is now dominated by OpenTelemetry Go Collector… sorry, not Go Collector, the Go SDK. They run their suits on every commit, and each of them takes 3 plus hours.
So if, on a good day, like, Gomer, just, like, 5PRs, that's going to take the machine for, like, 15 hours. So I have requested them to, like, come down and do it, like, nightly, or reduce the number of tests. They are already working on that. So once that is done, we'll get, like, much more availability of the CNCF Even though it's a single machine, we'll get, like, much more of the machine, and then we can definitely ask for, like, one more machine, or two more machines, depending on how much we want.
Anyway, like, for now, yeah, just continue with what you're doing, but I want us to eventually move to the formal verification methods, so instead of we running it by hand.
Jake Dern 00:46:49 Yeah, definitely, and it'll be an easy change to make, I think. Yeah, like, running the tests is, like, all automated, it's just, yeah, so many of them.
Cijo Thomas (Microsoft) 00:46:57 Yeah, yeah, one reason why I wanted to be, like, in that machine is because it gives much more trust to people who look at the dashboard, because they can see the logs when the benchmark itself are running. It's just like a normal GitHub action, so it's more trustable than, like, anyone, like, running it in their own machine.
So that's why I want to make it, like, more officially packed. But yeah, let's do this for now, and once we have the machines.
We can do some migration to that machine.
Jake Dern 00:47:28 Yeah, totally agree.
Laurent Querel 00:47:31 But… Yeah, remove the work in progress meter from the site, Here, shutdown leaves the kernel ETW session running, Would Capture want to talk about that?
Utkarsh 00:47:48 Yeah, so there's one PR already out there, it's not merged yet, which is adding a very basic implementation for an ETW receiver, and there were some issues that were discovered while reviewing the PR.
fixing those issues in that same PR would make it too big, so I just… create… I'm just creating this, I created this tracking issue to… track that problem. So, I can explain the problem, it's more about… the way we set up the receiver is we have one background thread that's initialized. Whichever core gets to run the initialization code first runs it, and the other ones don't.
So, the background thread, right now we don't, join it. We don't… we throw away its handle, we don't wait for, we don't do any graceful shutdown there.
That might cause issues, with, like, collector restart… with the, engine restart, or even, like, hot… Reload configuration when that happens.
So, it's just to track, like, what can we possibly do to fix those things, and… Trying to keep that existing PR small and focused.
Laurent Querel 00:49:02 Yeah.
Regarding the… what I noticed is… Sometimes… it's hard to… currently, the library reconfiguration is, by default, working this way. We have, let's say, we have a pipeline deployed on two CPUs.
And then we, we LIFO configure this pipeline.
The lead's flocking… we will start a new… a new version of the pipeline on one CPU. We keep the two previous ones.
We inspect, what is… how this new pipeline, with the new configuration is behaving, and then once we determine that it's going well, we… We shut down one of the… to other… of a previous pipeline.
So now we go back to 2CPU, And then we, we repeat the operation.
So it's going… it's working well for things like, like, pipeline, where… we have, TCP-based, or even UDP-based receivers.
With, combined with the SOU Sport. It's not necessarily going well with things like the… the VTW, or a few other, file-oriented, for example, receiver.
So probably we need to… Other people make an important effort to make that compatible with the process I just described, which is possible. For example, that's what I did for the For the file log receiver, in the spec, there is a description of how to do that.
But it will not be necessarily worth it to do that, so we could imagine a mod Where the component, like a receiver, will declare The type of library configuration they support.
And then we could imagine that, When one of the components into a pipeline Does not support, This kind of rollout deployment, where there is no interruption of traffic.
Then we could switch back to… we could fall back to a mode where we stop and we restart. Would be, an easy way to manage this kind of pipeline well.
So I don't know if that applied to ETW receiver, but I can imagine that could be useful.
Utkarsh 00:51:50 Yeah, yeah, okay. I think, I think when we work on this issue, we'll, keep that in mind.
And try to see if there are any gaps.
Thanks.
Laurent Querel 00:52:02 Extension cycle follow-up, so, Bukan, you want to talk about that?
you know, Ken is… GoCan is with us, yeah.
Gokhan Uslu 00:52:13 Yeah, yeah, yeah.
I mean, not much to talk about, it's just a track with the things that you ask, and the pull request.
So…
Laurent Querel 00:52:23 Yeah.
Gokhan Uslu 00:52:24 Yeah, just, just that. I think…
Laurent Querel 00:52:26 Okay.
Gokhan Uslu 00:52:27 One of the things is… probably to ask there, is the readiness probe is needed anytime soon? I have a plan to implement it. I can prioritize or deprioritize. And the shutdown channel sounds like… my understanding was, if it is incorrect there.
my understanding, maybe we can correct it, but it seemed like there was an ask for a specific channel just for shutdown. If that's not it, we can dismiss that, but otherwise… You know…
Laurent Querel 00:52:55 I think that, that was, yeah, part of my, feedback, and, and regarding the… the lives… Lifeness probe.
I think that's the general, What do we consider, the readiness and the liveness pubs that already exist?
How extension impact that?
Because if… For example, if we have to… if one extension communicates with a service, an online service.
And, if for whatever reason, this online service is not available, it means that indirectly the… The liveness and readiness of the corresponding pipeline using this extension will be impacted So, yeah, I think that definitively will be part of the… The protocol, the internal protocol to… To determine the liveness and readiness of, of pipeline based on The component and the extensions.
Gokhan Uslu 00:53:56 Yeah, I plan to make it so that an extension author can opt in to do it, and then notify the engine back when it is ready.
Laurent Querel 00:54:09 Okay.
Great. But it configs, CI check has no platform gating.
Oh, wood couch.
Utkarsh 00:54:26 Yeah, sorry, it took me long to unmute.
So, that same existing PR for ETW receiver, one of the checks for… which is the validate config CI check, that is failing.
And, that's mainly because, that check is run on a Linux machine, and ETW receiver… is conditionally compiled only on Windows.
So, there are a few things we can do. That check, which is… the CI check, which is running, could skip Windows-only components.
And, that way, at least we don't, fail that CI check.
And then we might also want to consider adding a config validation check on Windows for such components.
So… Yeah, it's just covering that part, and again, didn't want this to be fixed in that same PR to keep it focused.
Laurent Querel 00:55:22 Yeah.
Utkarsh 00:55:22 switches.
Laurent Querel 00:55:23 Oh my god.
Utkarsh 00:55:23 I'm sure for that, yep.
Laurent Querel 00:55:24 Yeah, ultimately, I think having a… a dedicated Windows IoT, CI, where we validate those components, and we'll be, will be, useful.
Utkarsh 00:55:41 Hmm.
Laurent Querel 00:55:43 Okay, security disabling HTTP admin server, or adding read-only authentication mod, yeah, oh yes, that is, Oh, and then… Don't play if we are never with us today? No.
But that's definitively something we also need on our side.
Being able to… Yeah, to secure a little bit more the… The existing admin endpoint.
I didn't read the description, but I'm pretty sure that it's about security.
Okay.
jmacdonald 00:56:23 Yeah, I think we had talked about also potentially removing the admin server just to save a little bit of memory.
But I agree on the security issue. That's what he's asking.
Laurent Querel 00:56:34 Removing entirely the HTTP admin server is problematic, in my opinion, but Because how do you… how do you manage this thing if you don't have the… At least right now, we don't have any other option, right?
jmacdonald 00:56:52 True.
Laurent Querel 00:56:53 So, disabling, in my opinion, is a very bad idea for now.
If we have OpAhmp or whatever to replace it, maybe why not? Even… even… I mean, the live nest readiness in Kubernetes, for example, it's mostly based on HTTP.
Still.
jmacdonald 00:57:16 At the very least, we could have it default to 000…
Laurent Querel 00:57:20 Yeah, that… Yeah, yeah, exactly.
I think that's the minimum we need to do, yeah.
jmacdonald 00:57:28 Okay.
Laurent Querel 00:57:29 Okay, so…
jmacdonald 00:57:31 steps.
Laurent Querel 00:57:33 So we accept everything there, and So let's see, we were from… there, and we basically review everything. I don't think we decided to… Not do something there, so let's select everything.
And then, do we have some topic to discuss?
Oh, it's already, silly.
jmacdonald 00:58:04 We did it!
Laurent Querel 00:58:05 We did it, yeah.
I think it was in.
jmacdonald 00:58:10 Trust me.
Laurent Querel 00:58:10 To review all of that, anyway.
jmacdonald 00:58:14 It was, I kept a couple few notes on the things that we talked about, which were more than just, like, kind of routine. Mostly the NUMA discussion, what we thought about co-pilot reviews, and the fake data generator, idea.
I jotted down. Link to the comparison dashboard.
All very good.
Laurent Querel 00:58:32 Yeah, thank you so much for the… Rebuilding this, the summary, this summary.
Okay.
jmacdonald 00:58:40 Aaron has his hand up.
Aaron Marten 00:58:43 I just had one really quick thing. On that binary plugins proposal, I wanted to create, like, after getting initial, kind of.
approval to keep going with this. I wanted to create some sub-issues to dive into some more of the detailed aspects that aren't covered in the top of a proposal. I don't seem to have permissions to create sub-issues.
Laurent Querel 00:59:03 Oh.
Okay.
Aaron Marten 00:59:08 Maybe it's… maybe it's something we can handle offline.
Laurent Querel 00:59:11 Yeah, yeah.
That's, that's strange.
So you can create an issue, but not a sub-issue.
Aaron Marten 00:59:20 Yeah.
Jake Dern 00:59:21 I had the same problem until…
jmacdonald 00:59:23 or…
Laurent Querel 00:59:27 That's where… maybe we can… do you think that we… Joshua, maybe we can talk with, Drew and see if there is, acceptor issue, receptor… Configuration settings that we can enable to otherwise people create sub-issue.
jmacdonald 00:59:44 Yeah, I can check with him, or else with Trask, who usually handles this type of.
Laurent Querel 00:59:48 Yeah, oh yes, yeah.
jmacdonald 00:59:50 Sometimes it should work.
Laurent Querel 00:59:51 Because that looks like…
jmacdonald 00:59:52 Andrew's back tomorrow as well.
Laurent Querel 00:59:55 Okay.
Aaron Marten 00:59:56 Yeah, I just looked in the GitHub docs, it looks like you need to have triage permissions.
In order to do that.
Laurent Querel 01:00:03 Which is fine for me.
Boom, boop.
I think it's, who cares?
jmacdonald 01:00:09 I was gonna suggest something along the lines of adding Aaron as some level of… Holder of power. That sounds good to me.
Laurent Querel 01:00:16 You know?
Yeah.
Okay.
jmacdonald 01:00:20 Alright, well, we've reached the end, legitimately. Thank you all. Thanks a lot for running the show.
Laurent Querel 01:00:26 And see you soon, at the facility summit.
jmacdonald 01:00:31 Yes. See you all soon.
Laurent Querel 01:00:33 No, thanks.
