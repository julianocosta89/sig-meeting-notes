SIG: Rust SIG
Date: 2026-02-10
Duration: 34 minutes
Zoom Recording URL: https://zoom.us/rec/share/96FeorQ3INVcFSyga0fGhz5Xgi3dBMcrbuv4_29s1DMG8NoprLA8CbaN_pYQe7u6.0xOv9P9kqgVVgJ4v
============================================================

## Zoom Recording Transcript

**Cijo Thomas (Microsoft)** 03:47 Hey, hello.
Can you hear me?
**Paul Le Grand des Cloizeaux** 03:53 Hey, how are you?
**Cijo Thomas (Microsoft)** 03:55 Root, how are you?
**Paul Le Grand des Cloizeaux** 03:56 Good! It's been a long time since I've joined LSC.
**Cijo Thomas (Microsoft)** 04:00 Yeah, I was assuming there was no one, but then, yeah, it looks like people… Let me…
Second, let me share my screen.
Oops, sorry.
Okay…
Yeah, I mean, there is nothing added in the agenda, so feel free to, add anything you want to discuss.
Yeah, we still have, like, quite a number of open PRs. I… I haven't had any chance to look at them yet.
Let it help with few, but yeah, we still have a backlog we need to go through.
**Björn Antonsson** 05:07 So, a question with regards to that. There are PRs that, for example, one PR that I have
Approved? Yeah.
3 weeks ago.
**Cijo Thomas (Microsoft)** 05:25 If it already has an approver, then it's super easy.
I believe you asked to take a look at the context-related fix, which is…
**Björn Antonsson** 05:36 Yeah, I can…
**Cijo Thomas (Microsoft)** 05:38 I should be able to find that. I did open it, like, a couple of times. This one, this one.
Let's see if it can be bought right away.
Unfortunately, that got into conflict. Oh, it's only changed loading, yeah, okay.
**Björn Antonsson** 05:56 Yeah. Not that dark color.
**Paul Le Grand des Cloizeaux** 06:00 Yep.
**Cijo Thomas (Microsoft)** 06:02 Yeah, I'm sorry, like, we have, like, quite a backlog cover.
Yeah, I also have, like, some small piers opened,
**Björn Antonsson** 06:18 Yeah.
**Cijo Thomas (Microsoft)** 06:19 Nothing.
**Björn Antonsson** 06:20 Crucial, but yeah.
I can try to go through them.
**Cijo Thomas (Microsoft)** 06:25 I also have something in the country prep as well, we have…
a couple of instrumentation libraries. I'm hoping that we can…
Pill them, parallel to stabilizing the tracing, because then we'll have proper
Instrumentation libraries leveraging the pricing.
Thing which we are building as well.
Boom.
I think we merged most PRs, but yeah, I have, like, one which is adding, like, some fixes to the Actix one.
The one for XM at Tower got mars last week.
Yeah, we heard it much, okay,
Let's look at the topics in the agenda. I think this is the one which we already opened. Yep, yep, I will ask for the conflicts to be resolved, and then we can get back to merge it.
I think, Paul, this is something which you opened a while ago, yep.
**Paul Le Grand des Cloizeaux** 07:27 Yeah, yeah, since it was mentioned in the comments on the PR, the previous PR that you opened, Bjorn asked me if we want to get it merged, and I mean, I can…
Updated.
And we can restart.
**Cijo Thomas (Microsoft)** 07:44 Sorry, you were discuss… referring to this PR, right? The one which…
**Paul Le Grand des Cloizeaux** 07:48 Yeah, yeah, yeah, yeah. Okay.
That, we didn't merge, because it was a breaking change, and we didn't…
**Cijo Thomas (Microsoft)** 07:57 Yeah, but not.
**Paul Le Grand des Cloizeaux** 07:57 We wanted to make a manual release, and so, yeah.
**Cijo Thomas (Microsoft)** 08:01 Yeah, so we should be able to… I don't have any concern with breaking change, because we have a milestone back the next release. It's sometime…
Late.
March, I believe, yeah. Okay, so this is… hopefully, like, we can get rid of, or do all the breaking changes in one shot.
**Paul Le Grand des Cloizeaux** 08:19 Okay. Then, then, if you're okay with it, I will…
put it up to date, and then we can… I'll probably close this one, or…
I don't know if we're able to create a new one, or keep this one in the.
**Cijo Thomas (Microsoft)** 08:32 It's up to you, like, I don't have any strong opinion. Okay. It's… yeah, do what is most convenient for you.
**Paul Le Grand des Cloizeaux** 08:39 Okay, sure.
Thank you.
**Cijo Thomas (Microsoft)** 08:43 So while, working on, like, distributed tracing, I have seen some performance issues.
I don't have the,
the flamecraft handy, but it looks like we have quite a, like, overhead. I think I found it…
when I was working on the…
Some tests for instrumentation libraries.
I…
Don't know where did I post about it, yeah, okay? It's probably in the PR itself, so PR doing quite a lot of work
While we are trying to…
Collect all the attributes, and, like, invoke the span builder, then add more attributes.
Though… Like, even before the sampler is…
even invoked, we do, like, quite…
Significant amount of work, and if the sampling decision is not favorable, we are just
throwing it out. So that is something which I believe, something we need to tackle.
I think, yeah, I think. This is a PR where I tried. I didn't share the actual numbers, but it was quite,
significant. A lot of… One of them has to do with…
the way our API is designed, because the Span Builder API requires ownership.
So it accepts collection of attributes.
Only to throw it away at the end of sampling. So this is something which was noted, like, long ago, I believe, like, long ago, I was saying, like, quite long ago. Let me see if I can find that issue.
I think this is probably the issue.
Yeah, oh yeah, I did tag, beyond here. So this is something which I want to, like, resurrect as we work towards stabilizing the…
tracing API, because if we can avoid the…
avoid the cost before we know the sampling decision. That would be, like, really, helpful, because right now we spend, like, most of the time even before sampling, which is why this issue was opened originally, like, basically saying that we spend, like, a lot of…
Things even, even before we get to sampling.
Boom.
**Björn Antonsson** 11:05 Yep.
**Cijo Thomas (Microsoft)** 11:06 Doesn't.
**Paul Le Grand des Cloizeaux** 11:07 The sampler need the attributes, right?
**Cijo Thomas (Microsoft)** 11:11 It needs attributes, so there is something in the spec which is kind of standing in our way, the…
**Paul Le Grand des Cloizeaux** 11:16 Yeah.
**Cijo Thomas (Microsoft)** 11:17 wording from spec says you must add… attributes at span creation.
as opposed to… Providing them after the sampling decision, so I…
have, opened a PR in the spec. It's still draft.
To…
reconsider that, statement from the spec, because spec is written with mostly, like, web applications in mind.
It's usually fine, like, spending, like, few hundreds of nanoseconds, it's okay, but I have seen people who write Rust code, they really want, like, a much, much higher expectation, so the spec is standing in our…
some votes standing in our way, because spec really recommends provide all the attributes at span creation time, and that is costly, because we have a vector, and
We don't even know how many attributes usually is going to provide, so we start with vector of size 0, 1, then we do, like, resizing. I don't have the flame graph, but yeah, we are spending, like, quite a lot of time on that one.
So I try to see if the spec can relax the wording there.
Or at least recommend something like, use your discretion to provide
More attributes at startup versus providing them later.
I mean, based on my observation, like, C++ does not have, like, much activity, so I cannot really ask for feedback, but .NET has faced this exact same problem, and they decided to violate the spec. They're only providing, like.
Almost, like, no attribute at the beginning.
And then wait for the sampling decision, and then provide the attributes.
So it's not, like, explicit violation of the spec, it's more like a recommendation from the spec.
So if the spec is, like, somewhat relaxed, then we can ask the Rusty instrumentations to also…
be more efficient, by avoiding all the work, without knowing someone decision. But that's one thing, and second aspect is,
Like, we don't have any… thing in the
span APA, where we can pass a reference, like, everything in the span builder.
requires ownership, so that's why…
That's another thing which we want to revisit, because if you compare with metrics, metrics API only takes a slice.
So you don't really need to clone or copy anything for metrics, because majority of the time, you're just looking up whether this pattern is seen before or not. For span also, if you can do
something with the slice, up to the point where we make the sampling decision, and then we can quickly decide, okay, I'm not planning to sample it anyway, so don't bother with ownership or copy.
But in the event sampling is favorable, then, yeah, we can afford to pay the cloning cost, so we can convert the slices into owned ones. That is something what, like, Sean opened, like, long ago.
He's not active, right now, but he did share, like, a lot of screenshots from FlameGraph at that time.
It's spreading, like, different, different issues. It's very hard to find them, but it's not that hard to rerun a…
Of test to reconfirm, this program.
Anyway, the ask is, number one, I will first… I'll first follow the spec part from my side to see if we can get some blessing from the specification. Second is, so most likely a question for, Bjorn and Paul, like, do you… either of you have
some bandwidth to explore, like, can we… modify Span Builder.
In such a way that we can afford to take just a slice.
And run the sampler with that information, and if…
Decision is favorable to the cloning.
Yeah, I mean, it needs, like, some time to, like, write down all these thoughts, but I'm just sharing, since I have both of you in the call.
**Paul Le Grand des Cloizeaux** 15:15 Yeah.
I'm not sure I have the time right now. I don't know beyond if you're interested.
**Björn Antonsson** 15:25 Yeah, I would be interested. I don't have the time right right now, but if we're aiming for…
March, at least, then… then I will probably try to,
**Cijo Thomas (Microsoft)** 15:38 Yeah, that sounds good, actually, yeah. Because, like, I'm the… one of the reasons, like, why I was not comfortable calling, distributed tracing as stable in Rust, like, two years ago when I joined the project was I was said.
some benchmark numbers, and it looks, like, very bad, especially considering that we are writing Rust code. We expect things to be, like, much more faster.
There are a lot of discussions, like, this is just one thing which I was able to recollect, but there were quite a large number of discussions in the past where people shared, fleeing graphs where, of their entire project, like, open telemetry was, like, 10 or 20% of overhead, and that was, like, pretty bad.
Yeah, I mean, I'll find, like, a few things, like, yeah, even this discussion might have…
some numbers… Yeah, and we can see, like, span.
But this was the time when they were using the tracing macros to create span, and we were converting that into OpenTelementary. You can see, like, we are taking, like, too much time here.
But these are, like, old, like, 2 years plus old. Since we haven't done much to improve the situation in tracing signal, these… I would expect these will be…
The same thing if you're on it right now.
And I did observe that last week when I did the ground trip PR review. So this is something which I consider, like, without performance, like, I don't know, like, for a Rust project, we really want to…
be, like, extremely performant, so I really consider this as a prerequisite before we can call our APIs, and SDKs as stable. So that's my one thing I want to see if we can get more people. There is one more thing, which…
is worth discussing,
There is something in the… again, there is something in the spec which is standing in our way.
Best way to find that is… if I can find the person who… Opened the…
change, one sec here. So there is something in the spec which says that, even if the assembling decision is completely unfavorable.
It says we had to generate a new span ID and create the span irrespective of the sampling decision.
Of course, the spanned.east recording will be false, but still the span is created, and we add that to context, we activate that, we do, like, a bunch of things. So, based on
my performance testing in, like, 5 years ago in .NET, we concluded this is too much. So .NET decided to do a big, blatant spec violation, where in .NET, this statement is not true. So if the sampling is…
To… sambling decision is to drop.
We check whether it's a root span, or it's a child of an existing root, and depending on that, we…
violate the span. So if it's root span, yeah, we rate the span, we materialize it, we add it to the context and activate it, but if it's child spans, we completely avoid creating the span, so it'll be, like, equivalent of none in Rust or null in .NET.
So we try to retrospectively, get the spec to plus something like this, because again, like, most languages don't care for them, like, creating few spans is not a big concern, especially when people are writing, like, web applications.
few hundred nanoseconds, they don't really care. But with Rust, this has been a concern, so I will try to see if we can get the blessing from spec.
**Björn Antonsson** 19:21 To do something like that. This is just a quick quest.
Turning around this.
I mean, I assume it's still sort of like the root span that gets propagated in the context.
**Cijo Thomas (Microsoft)** 19:37 Yes, yes, since we are not creating the child span, the root span is the one which gets propagated in the context, yes.
**Björn Antonsson** 19:44 Okay, yep.
**Cijo Thomas (Microsoft)** 19:46 Yeah, I mean, like, you can argue, like, both ways. So one argument was that if you end up creating span IDs for the newly
created span, which we are not recording. The logs which you are emitting inside this span, they'll point to
This span as their parents, but if you search your backend, you'll never find such a span, because that span is anywhere dropped by the assembly.
So there were, like, arguments back and forth in 2020 when the spec was being returned.
And this wording was added after, like, a huge debate, so that's why it's not going to be, like, super easy to spec to relax or revert its span, which is why this wording is returned in such a way that it's allowing, like, some flexibility. It says if it's non-road span, SDKs may skip the creation.
So it's more like relaxing the requirements, not changing the entire, thing, which is why, like, there is a reasonable chance we can get this thing into the spec, but nobody was actively working on it.
So this person is from the .NET group.net already decided we don't care about the spec, we are violating it anyway. So he's trying to get the spec to retroactively bless what .NET is doing. But for us, we are still building it up, so we are… as of now, we are compliant with the spec, but we are paying the performance cost.
So yeah, I'll try to see if something can be done at the spec level.
So we get, like, we can do things…
without being, like, completely violating the spec, and also offering, like, reasonable performance. Because if you literally take the spec essay Bible and follow it.
we'll be, like, compliant, but then we have the problem where people start questioning, like, what are you building in Rust? Which is not even doing the basic buff checkmark.
And this is, like, not just my… so many issues, were open in the past.
Which pointed to, like, issues like this, where people are complaining that
I only want to create a span if I know that I'm in the actively
Recorded parent span context, but…
to even determine that, it's… it's somewhat non-trivial amount of work, and even if I determine that, and I call the span.start, I was hoping that SDK would be smart enough to not circuit everything, but unfortunately, we are doing a lot of work, including creating a span, a new span ID.
Only to drop it, like, like…
in the exporting, or even… it never leaves the SDK. Those dummy spans, the non-recording one, it just gets created, and we just drop it. And unfortunately, we spend a lot of force to materialize that in memory and navigate or manipulate the context with the one.
Anyway, like, I just shared, like, these things, these were, like, top for me. I mean, of course, APS stability is important, but, performance is equally important, and most likely.
these performance changes might require either clicking the existing API or creating, like, new API. So that's why I consider, like, this is important enough for us to consider before we call our APIs table, because if we
later conclude that to fix this, you need to break the API, then, like, we failed. So I want to, like, spend enough time making sure we are, like, pretty sold on the…
current shape of the EPA, and they can achieve, as.
**Paul Le Grand des Cloizeaux** 23:11 Yeah.
**Cijo Thomas (Microsoft)** 23:11 Oh, the high performer thing. Yeah, sorry, I spoke, like, too much, but yeah, go ahead, go ahead.
**Paul Le Grand des Cloizeaux** 23:16 Yeah, yeah, so usually, I mean, in Datadog libraries, there is a concept of span filters, which is different from span sampling.
In the sense that span filters, they drop spans completely, like, out of existence.
Which is probably what you want in this case, whereas, like.
Span sampling keeps the span, even if they are not simple, they keep them alive, and… Yeah.
So…
**Cijo Thomas (Microsoft)** 23:45 Yeah, but, no, no, even if you do that, like, there is already a lot of cost paid until that point, because to create the spend, you need to, like…
**Paul Le Grand des Cloizeaux** 23:54 Right.
**Cijo Thomas (Microsoft)** 23:55 Yep, yep, so those are… all of them recurs, like, ownership, so pretty much…
Like, that's the main pattern. Also, it's a vector, which can regrow under the cover. So there are a lot of cost, and even the context manipulation, like, attaching something to a context, like, we have to run the span inside a synchronized span with our kind matrix, so there is, like, a lot of work we do.
For a span to be thrown away, slightly later.
Yeah, the people, so…
**Paul Le Grand des Cloizeaux** 24:23 Also, I know of people that use tracing to do this filtering. So, tracing has a way to disable trace points, and make them almost zero cost, right? And so, I mean, obviously it's not doable with the OpenTelemetry API.
**Cijo Thomas (Microsoft)** 24:42 By itself, right? Yeah.
**Paul Le Grand des Cloizeaux** 24:44 But.
**Cijo Thomas (Microsoft)** 24:45 So one of the… what he said, like, totally makes sense, because one of the maintainers of…
placing, they also commented on the issue which I opened earlier, because in placing, they make the decision using the metadata alone, like, event-enabled thing. So that metadata is, like, static, so you know the…
name of the span, I heard, you know the attribute names, not the values.
So they make decisions based purely on the static metadata, so they don't really have to allocate to make that decision, which is where, like, OpenTelemetry completely fails, because we make decisions based on things on the heap.
Which means we had to assemble them and allocate them on the heap, arrange it in a way, like, sample it's accept, and then code it. So that's, like, already, like, too much.
**Paul Le Grand des Cloizeaux** 25:29 It's kind of even stronger than that, because for each trace point, like, they keep a static variable, like a global static, and they cache the decision, so it's even better than having to filter every time you.
**Cijo Thomas (Microsoft)** 25:42 Exactly, yeah, yeah.
Yeah, that's why, like, like, the tracing maintenance gave some suggestion to us, like, open telemetries.
It's good, like, our intent, vision, mission, everything is good, but, like, the performance is, like, too bad for a Rust project. I mean, if it's, like, Python or Java or, like, even .NET, I wouldn't mind, like, a few nanoseconds.
**Paul Le Grand des Cloizeaux** 26:05 Yeah.
**Cijo Thomas (Microsoft)** 26:06 your building, rough, you should really take performance into serious consideration.
Anyway, let's, use, like, the, like, weeks till, like, March to see if we can improve some of these things. I won't have the time to…
Oh… Implement any code changes.
I will do, my, like, my main focus is, can I, like, fix the spec itself, or at least get some pricing? So I'll be pursuing the spec route, but as part of that, I'll be writing benchmarks, in the Rust repo, so…
it's easy for people to be, like, what is the cost which I'm talking about? Is it, like, 1 nanosecond, or is it 100, or is it even measured in nanoseconds?
So then people will start paying more, like, serious attention to what we are seeing. Because most of the time, these conversations end up nowhere, because people are spending, like… they measure their API in, like.
milliseconds, so adding, like, few hundred seconds, add nanosecond is, like, not even worth the discussion. But in Rust, many people, they don't use it just for web applications, they use it for, like, a few other things, where things are pretty, pretty sick.
**Paul Le Grand des Cloizeaux** 27:16 Hmm.
**Cijo Thomas (Microsoft)** 27:19 We also work on something called Arrow. I'm not sure, like, if you're familiar with Arrow. Arrow is a exploratory project in OpenTelemetry to build telemetry pipelines.
It is built completely in trust, and I…
they are not using OpenTelemetry for essentially the same reason I described, like, we are not performant enough. They measure everything in nanoseconds, so they cannot just afford to put OpenTelemetry into their stack. There are other… I mean, performance is the main reason.
But not specifically the span API issues, which I described earlier. They are mostly concerned with our metrics. We're not… we have a lot of contention at all, so they have… generally, they are concerned with the performance cost of open telemetry rush, so they just created their own telemetry crate to do their internal logging and metrics.
So these are, like, real problems. If, if the performance was pretty good, they would have directly used Open Elementary Rest.
I'm an approver in that report, so I know the pain from both sides, like, I'm, like, an approver here in Rust, and also in the consumer side, so… Yeah, anyway, let's see if we can get some progress here. I will, like, keep adding benchmarks, do some prototypes.
But depending on how much bandwidth, we'll be able to, like, tackle them together.
**Paul Le Grand des Cloizeaux** 28:37 Thank you.
**Cijo Thomas (Microsoft)** 28:39 Oh, okay, yeah. By the way, I want to, like, ask, like, I think Bjorn and Paul, like, you have previously done, like, some smaller PRs where you did fix, like, performance of, like, things, which nobody else noticed, so I have a feeling that you also have a passion for looking for, improving perf.
Are you seeing, like, any signal such that, like, is such… about the performance of OpenTelementary Rusty is not good from your customers? Do you have any…
Like, complaints or feedback, or even, like, good feedback from your customers about performance in general.
**Paul Le Grand des Cloizeaux** 29:12 We… we wish we had feedback, but we don't. Oh, okay. Yeah.
Internally, something, I guess, we have noticed, but, I mean, it's no longer noticeable because, anyway. So the… the exporter, or, I mean, the… the thing that end cuts to…
GRPC or to, sorry, Protobuff.
Does a lot of copying around?
Which is not super good.
The fact is, for the distribution of the SDK that we did, we replaced the span exporter, so we don't really use these functions anymore.
**Cijo Thomas (Microsoft)** 29:52 Okay. But, yeah, when I was looking at the profiles.
**Paul Le Grand des Cloizeaux** 29:57 of the hotel SDK using the… the protobuf exporter.
It wasn't, like, yeah.
The thing is Prost forces you to use its own data structure, and so you have to basically copy all of the strings.
**Cijo Thomas (Microsoft)** 30:14 Yeah, good to be.
**Paul Le Grand des Cloizeaux** 30:14 Which isn't super efficient.
**Cijo Thomas (Microsoft)** 30:17 I think I covered that with a benchmark here. I was looking at this cost.
I was able to, like.
But, like, figure out, like, or break down the overall cost, like, we spend, like.
this much time to just convert from our in-memory structure to the protobo phone, and then another 66 on the serialization, and then, for GCP. This is purely the conversion in the proto, and then if you look at the OTLP,
It's… it'll give you, like, a breakdown, like, what are… where are we spending?
Again, this was mostly… I'm trying to quantify, like, what's the performance over, because without that, we cannot really claim that we include anything, so my first step was to…
figure out, like, where exactly are we spending, and yeah, the OTLP one is quite concerning, like, a lot of OPs involved.
As you already noticed, yeah.
**Paul Le Grand des Cloizeaux** 31:09 Nope.
But, other than that, it's… It's kind of hard.
**Cijo Thomas (Microsoft)** 31:16 Got it, yeah, yeah. Anyway, like, if you see, like, any complaining, like, feel free to open an issue, so we'll know, like, are we solving any… we know we are solving real problems. I'm quite convinced from my side, because inside Microsoft, when I joined the Rust project in 2023,
There was a internal talk where people talked about how open telemetry Rust was pretty bad.
So that's the time when I joined the project. So I… I confirmed what they… they found.
But I didn't do anything to fix it. We only did improvements to, like, metrics and logs. Crisis was, like, somewhat messy at that time, because we were doing, like, a lot of special things for tracing and all. So with Beyond…
doing the heavy lifting there. We kind of got rid of that, so now, it's…
perfect time for us to revisit our own API and fix things which doesn't make sense.
**Paul Le Grand des Cloizeaux** 32:12 Yep, hopefully. But I think the… basically the low-hanging fruits…
are already taken, so any optimization is… like, it involves refactoring quite a lot of code, or changing the API.
Or, like, I mean, you know, we've token, we've…
We've spoken about the sampler and stuff like that.
**Cijo Thomas (Microsoft)** 32:35 Yeah, yeah, I'll see, like, if I get time, I'll try to, like, add some comments to, this issue, so…
So we'll know, like, what a ideal API would look like. A span builder, which can operate purely on Slice, or something like that.
I'll write down some thoughts, into here, and depending on our bandwidth, we can, feel free to comment, or even try some different approaches, to get the better both.
**Paul Le Grand des Cloizeaux** 33:02 Yeah, the worst thing is, for me, is that there is no single place where we can.
**Cijo Thomas (Microsoft)** 33:07 discover all the issues. It's, like, spread throughout the repo.
So it will even take a good amount of effort to consolidate all of them into a single issue. Maybe, like, depending on my bandwidth, I'll try to… because some of them are in the API, some of them in SDK, and the thing which I just showed earlier, right, it was in the exporter, the OTLP exporter, so it, like, spread across the pipeline.
**Paul Le Grand des Cloizeaux** 33:29 No.
Registering one.
**Cijo Thomas (Microsoft)** 33:32 Yeah, okay, yeah, I think, let's, meet again next week, so by that time, I'll try to get your PR. So you said you'll reset your PR for the span processor.
**Paul Le Grand des Cloizeaux** 33:43 Yeah, yeah, I will, I will revive it.
Probably split it in two, or something, yep.
**Cijo Thomas (Microsoft)** 33:50 Okay, and I will, try to ask the person to resolve the conflict so I can get this loan pending, yeah.
Okay, anything else to…
Discuss…
Okay.
**Björn Antonsson** 34:06 on the nice side.
**Cijo Thomas (Microsoft)** 34:08 Yeah. Thank you, bye-bye.
**Björn Antonsson** 34:11 But…
